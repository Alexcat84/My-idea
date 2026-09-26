/**
 * planParser.ts — el parser del markdown del plan (Fase 3.9.2: extraido de
 * ui/PlanDocumento.tsx para poder probarlo). PURO: sin React, sin DOM.
 * Respeta el markdown REAL del motor: no inventa estructura, solo pliega la
 * que viene, y rescata la que el modelo emitio en prosa densa.
 *
 * i18n F2: los literales en español de las expresiones regulares ("Etapa",
 * "Primera acción", "Esta semana", "El lunes", "Entregable", "Pasos", "_Plan completo_", "Este
 * plan se alimentó") son CLAVES DE LECTURA del markdown que escribe el motor,
 * no texto de pantalla: no van al catálogo. Solo va la etiqueta que el parser
 * agrega ("Los números que necesitas").
 */
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { PLAN_DOCUMENTO } from "./i18n/mensajes/planDocumento";
import { pintarRotulo } from "./i18n/rotulosPlan";

export type TipoSeccion = "etapa" | "cierre" | "otro";

/** Fase 3.9 C8: un bloque de pasos con su sub-encabezado (o null si la lista
 * venía suelta). Varios por etapa: "Pasos para construir", "Pasos para
 * atacarlo", etc. — todos con el MISMO tratamiento visual de puntos + línea. */
export interface BloquePasos {
  label: string | null;
  pasos: string[];
}

export interface Seccion {
  titulo: string;
  numero: string | null;
  tipo: TipoSeccion;
  descripcion: string;
  bloquesPasos: BloquePasos[];
  entregable: string | null;
  /** La acción concreta del tramo: "**Primera acción:**" (decisión del
   * fundador, 26 sep 2026) o, en los planes guardados antes, "**Esta
   * semana:**"; en la sección de números, "**El lunes que viene:**". El nombre
   * del campo se quedó por compatibilidad; la pantalla lo rotula "Primera acción". */
  estaSemana: string | null;
}

export interface PlanParseado {
  etiqueta: string | null;
  titulo: string | null;
  intro: string;
  secciones: Seccion[];
}

/** La línea de procedencia que el motor escribía al pie de cada plan
 * ("_Este plan se alimentó de N conceptos…_"). CONFIDENCIAL (BANCO §5): el
 * usuario nunca debe ver la mecánica interna. El redactor ya no la escribe,
 * pero los planes generados ANTES la llevan grabada en su markdown, así que
 * se limpia AL LEER: si no, cada plan viejo la sigue filtrando en pantalla y
 * en cada descarga. */
const LINEA_PROCEDENCIA = /^\s*_?Este plan se aliment.*$/gim;

/** Quita la procedencia de un markdown de plan ya guardado. */
export function sinProcedencia(md: string): string {
  return md.replace(LINEA_PROCEDENCIA, "").replace(/\n{3,}/g, "\n\n").trim();
}

/** Recorta "**Etiqueta:** …" (hasta la línea en blanco o el fin) del cuerpo. */
function recortarBloque(cuerpo: string, etiqueta: RegExp): { valor: string | null; resto: string } {
  const m = cuerpo.match(etiqueta);
  if (!m || m.index === undefined) return { valor: null, resto: cuerpo };
  const resto = (cuerpo.slice(0, m.index) + cuerpo.slice(m.index + m[0].length)).trim();
  return { valor: m[0].trim(), resto };
}

export function parsearSeccion(tituloCrudo: string, contenido: string, idioma: Locale = LOCALE_BASE): Seccion {
  const mEtapa = tituloCrudo.match(/^Etapa\s+(\d+)\s*[:.·-]?\s*(.*)$/i);
  const numero = mEtapa ? mEtapa[1].padStart(2, "0") : null;
  // i18n F5: los títulos que son marcadores neutros (la sección de números, lo
  // que falta) se pintan en el idioma de quien lee.
  const titulo = (mEtapa ? mEtapa[2].trim() : pintarRotulo(tituloCrudo, "encabezado", idioma)) || tituloCrudo;
  const esCierre = /sosten|n[úu]meros|no cubr|qu[ée] sigue/i.test(tituloCrudo);

  let cuerpo = contenido.replace(/\n---\s*$/g, "\n").trim();

  // 1) La acción concreta del tramo (va al final): "Primera acción" (o el
  //    rótulo viejo "Esta semana" de los planes guardados, el mismo campo) o su
  //    equivalente en la sección de números ("El lunes que viene").
  const RE_SEMANA = /\*\*(?:Primera acci[oó]n|Esta semana|El lunes(?: que viene)?):?\*\*[\s\S]*?(?=\n\s*\n|$)/i;
  const es = recortarBloque(cuerpo, RE_SEMANA);
  cuerpo = es.resto;
  let estaSemana = es.valor
    ? es.valor.replace(/^\*\*(?:Primera acci[oó]n|Esta semana|El lunes(?: que viene)?):?\*\*\s*/i, "").trim()
    : null;

  // 2) "Entregable" — el artefacto que queda.
  const ent = recortarBloque(cuerpo, /\*\*Entregable:?\*\*[\s\S]*?(?=\n\s*\n|$)/);
  cuerpo = ent.resto;
  const entregable = ent.valor ? ent.valor.replace(/^\*\*Entregable:?\*\*\s*/i, "").trim() : null;

  // 3) Pasos (C8): CUALQUIER "**...Pasos...:**" abre un bloque; una lista suelta
  //    cae en un bloque sin label. Todo lo demás (incluidas notas en negrita
  //    como "**Nota crítica:**") es descripción/prosa. Así los pasos reciben el
  //    mismo punto+línea vengan numerados, con viñetas, o en varios sub-bloques.
  const bloquesPasos: BloquePasos[] = [];
  const descripLineas: string[] = [];
  let bloque: BloquePasos | null = null;
  const esItem = (l: string) => /^\s*(?:\d+[.)]|[-*])\s+/.test(l);
  for (const linea of cuerpo.split("\n")) {
    const lab = linea.match(/^\s*\*\*\s*([^*]*[Pp]asos[^*]*?)\s*:?\s*\*\*\s*(.*)$/);
    if (lab) {
      bloque = { label: pintarRotulo(lab[1].trim(), "negrita", idioma), pasos: [] };
      bloquesPasos.push(bloque);
      if (lab[2]?.trim()) bloque.pasos.push(lab[2].trim());
      continue;
    }
    if (esItem(linea)) {
      if (!bloque) {
        bloque = { label: null, pasos: [] };
        bloquesPasos.push(bloque);
      }
      bloque.pasos.push(linea.replace(/^\s*(?:\d+[.)]|[-*])\s+/, "").trim());
      continue;
    }
    // Una línea de PROSA (no-lista, no-blanca) cierra el bloque de pasos y va a
    // la descripción. Una línea EN BLANCO NO lo cierra: los pasos separados por
    // aire (como la sección "¿Puede sostenerse tu idea?") siguen siendo UN solo
    // bloque con su riel, no uno por ítem con su "Pasos" repetido y sin línea.
    if (linea.trim()) {
      bloque = null;
      descripLineas.push(linea);
    }
  }
  for (const b of bloquesPasos) b.pasos = b.pasos.filter(Boolean);

  const tipo: TipoSeccion = numero ? "etapa" : esCierre ? "cierre" : "otro";
  let descripcion = descripLineas.join("\n").trim();

  // 4) Respaldo C9 (Fase 3.9.2) para la sección de números. El redactor ya tiene
  //    orden de emitirla como lista, pero los planes YA generados (y cualquier
  //    salida terca) la traen como UN párrafo denso con las etiquetas en negrita
  //    EN LÍNEA ("**Costo por ciclo:** …") y la acción del lunes suelta al final.
  //    Aquí se rescatan las dos cosas para que reciban el mismo trato que una
  //    etapa. Solo en 'cierre' y solo con 2+ etiquetas: una nota suelta
  //    ("**Nota crítica:**") jamás dispara esto.
  if (tipo === "cierre") {
    if (!estaSemana) {
      const m = descripcion.match(/(?:^|\.\s+)((?:El lunes|Esta semana|Primera acci[oó]n)(?![\p{L}])[\s\S]*)$/iu);
      if (m && m[1].trim().length > 30) {
        estaSemana = m[1].trim();
        descripcion = descripcion.slice(0, (m.index ?? 0) + (m[0].length - m[1].length)).trim();
      }
    }
    if (bloquesPasos.length === 0) {
      const re = /\*\*\s*([^*\n]+?)\s*:\s*\*\*/g;
      const marcas: Array<{ label: string; inicio: number; fin: number }> = [];
      for (let m = re.exec(descripcion); m; m = re.exec(descripcion)) {
        marcas.push({ label: m[1].trim(), inicio: m.index, fin: re.lastIndex });
      }
      if (marcas.length >= 2) {
        const items = marcas.map((mk, i) => {
          const hasta = i + 1 < marcas.length ? marcas[i + 1].inicio : descripcion.length;
          return `**${mk.label}:** ${descripcion.slice(mk.fin, hasta).trim()}`;
        });
        bloquesPasos.push({ label: elegir(PLAN_DOCUMENTO, idioma).losNumerosQueNecesitas, pasos: items });
        descripcion = descripcion.slice(0, marcas[0].inicio).trim();
      }
    }
  }

  return {
    titulo,
    numero,
    tipo,
    descripcion,
    bloquesPasos: bloquesPasos.filter((b) => b.pasos.length > 0),
    entregable,
    estaSemana,
  };
}

export function parsearPlan(md: string, idioma: Locale = LOCALE_BASE): PlanParseado {
  let etiqueta: string | null = null;
  const cuerpo: string[] = [];
  for (const linea of md.split("\n")) {
    const l = linea.trim();
    if (!etiqueta && /^_Plan (completo|inicial|de seguimiento|seguimiento)_$/i.test(l)) {
      etiqueta = pintarRotulo(l.replaceAll("_", ""), "etiqueta", idioma);
      continue;
    }
    // La procedencia se descarta: es interna (ver sinProcedencia).
    if (/^_?Este plan se aliment/i.test(l)) continue;
    cuerpo.push(linea);
  }

  let titulo: string | null = null;
  const intro: string[] = [];
  const rawSecc: { titulo: string; contenido: string }[] = [];
  let actual: { titulo: string; contenido: string } | null = null;
  for (const linea of cuerpo) {
    // El primer encabezado (# o ##) es el TÍTULO del plan; su cuerpo, la intro.
    if (!titulo) {
      const h = linea.match(/^#{1,2}\s+(.+)$/);
      if (h) {
        titulo = h[1].trim();
        continue;
      }
      intro.push(linea);
      continue;
    }
    const h2 = linea.match(/^##\s+(.+)$/);
    if (h2) {
      actual = { titulo: h2[1].trim(), contenido: "" };
      rawSecc.push(actual);
      continue;
    }
    if (actual) actual.contenido += linea + "\n";
    else intro.push(linea);
  }

  const secciones = rawSecc.map((s) => parsearSeccion(s.titulo, s.contenido, idioma));
  const introTxt = intro.join("\n").replace(/\n---\s*$/g, "").trim();
  return { etiqueta, titulo, intro: introTxt, secciones };
}
