/**
 * expediente.ts — Fase 4.6: los documentos que el usuario se lleva.
 *
 * El viaje tiene fases y cada fase deja un documento propio: el plan con el
 * que arrancaste, cada seguimiento que replanteó el camino, y al final el
 * expediente con TODO el desarrollo. Este módulo es PURO: arma el índice y el
 * markdown a partir de lo ya persistido, sin tocar Supabase ni el motor (una
 * descarga no cuesta créditos ni llama al LLM).
 *
 * Confidencialidad (BANCO §5, decisión del fundador): el expediente jamás
 * nombra nodos, grafos, conteos internos ni la mecánica del sistema. Narra el
 * viaje del usuario con lo que el usuario reconoce.
 *
 * Sin guiones largos en el texto generado: es copy visible.
 */
import { esMundoProteccion } from "./espacios";
import { fechaHumanaConAno } from "./fechas";

/** Un ciclo del viaje: el plan original o cada seguimiento posterior. */
export interface CicloExpediente {
  planId: string;
  /** 'inicial' | 'completo' | 'seguimiento' */
  etiqueta: string;
  createdAt: string;
  contenidoMd: string;
}

export interface AccionExpediente {
  etapa: number;
  texto: string;
  /** dbContract CHECKLIST_ESTADO: pendiente|empezado|en_proceso|hecho|no_aplica */
  estado: string;
  completedAt: string | null;
  fechaBase: string | null;
  /** gestor de estados: el porqué de una tarea retirada (estado 'no_aplica') */
  noAplicaMotivo?: string | null;
}

export interface MundoExpediente {
  nombre: string;
  contenidoMd: string | null;
  completadoAt: string | null;
  /** Fase 3 (tanda 5): las acciones del mundo (su checklist) y su "cómo te fue"
   * (resumenEspacioMd ya armado por quien llama), para COMPLETAR su sección en el
   * expediente global — no solo su plan. */
  acciones?: AccionExpediente[];
  comoTeFueMd?: string | null;
}

export interface DocumentoIndice {
  /** identificador estable que la UI manda de vuelta para pedir el contenido */
  clave: string;
  tipo: "ciclo" | "expediente" | "bitacora" | "analisis" | "reporte" | "registro";
  titulo: string;
  subtitulo: string;
  /** ISO; null solo si el documento no cuelga de una fecha concreta */
  fecha: string | null;
  /** Fase 3 (tanda 5): el espacio (nombre de cara) de un documento por-mundo,
   * para agruparlo/etiquetarlo. Ausente en los del viaje principal. */
  espacio?: string;
}

/**
 * "Todo separado" (T7, D4): parte el índice de documentos, visto desde UN
 * espacio, en dos recuadros — lo GLOBAL (el Expediente completo, SIEMPRE
 * presente en todo espacio) y lo DEL ESPACIO actual (el núcleo, o un mundo).
 *   - globales   = los de tipo "expediente" (etiquetados "Global" en el panel).
 *   - delEspacio = si es un mundo, los que llevan SU etiqueta de espacio; si es
 *     el núcleo, los del viaje principal (sin `espacio`) que NO son el expediente.
 *   - hayMundos  = si el proyecto tiene algún documento por-mundo. En false, el
 *     panel muestra UN solo recuadro sin etiquetas (ruido cero).
 * Puro y testeable en los dos sentidos (núcleo / mundo).
 */
export function particionDocumentos(
  docs: DocumentoIndice[],
  dominio?: string,
  nombreEspacio?: string
): { hayMundos: boolean; globales: DocumentoIndice[]; delEspacio: DocumentoIndice[] } {
  const hayMundos = docs.some((d) => d.espacio);
  const esScoped = Boolean(dominio);
  const globales = docs.filter((d) => d.tipo === "expediente");
  const delEspacio = esScoped
    ? docs.filter((d) => d.espacio === nombreEspacio)
    : docs.filter((d) => !d.espacio && d.tipo !== "expediente");
  return { hayMundos, globales, delEspacio };
}

export interface DatosExpediente {
  nombre: string;
  entradaOriginal: string;
  creadaAt: string;
  realizadaAt: string | null;
  cierreMotivo: string | null;
  organizadorMd: string | null;
  ciclos: CicloExpediente[];
  acciones: AccionExpediente[];
  numerosMd: string | null;
  mundos: MundoExpediente[];
  /** el informe de analytics.ts, ya calculado por quien llama */
  informeMd: string | null;
  /** Fase 4.8: el CUERPO de la bitácora (secuencia por día, sin portada), ya
   * armado por bitacoraCliente. Entra como la sección FINAL del expediente. */
  bitacoraMd: string | null;
  /** ISO del momento de la descarga (inyectable para tests deterministas) */
  generadoAt: string;
}

/** Clave del documento de un ciclo. La UI la trata como opaca. */
export const claveDeCiclo = (planId: string) => `ciclo:${planId}`;
/** Fase 3 (tanda 5): la clave del Reporte de un mundo (documento por espacio). */
export const claveDeReporte = (dominio: string) => `reporte:${dominio}`;
/** Mundos de protección (P3): la herramienta canónica instanciada, descargable. */
export const claveDeRegistro = (dominio: string) => `registro:${dominio}`;
export const CLAVE_EXPEDIENTE = "expediente";
export const CLAVE_BITACORA = "bitacora";
export const CLAVE_ANALISIS = "analisis";

/**
 * Baja de nivel los títulos de un markdown incrustado: un plan trae su propio
 * `# Título`, y al meterlo bajo un `## ` del expediente la jerarquía quedaría
 * al revés. Respeta los bloques de código cercados (``` y ~~~), donde un `#`
 * es un comentario y no un título.
 */
export function rebajarTitulos(md: string, niveles: number): string {
  if (niveles <= 0) return md;
  let dentroDeCodigo = false;
  let cerca = "";
  return md
    .split("\n")
    .map((linea) => {
      const apertura = /^\s{0,3}(`{3,}|~{3,})/.exec(linea);
      if (apertura) {
        const marca = apertura[1][0];
        if (!dentroDeCodigo) {
          dentroDeCodigo = true;
          cerca = marca;
        } else if (marca === cerca) {
          dentroDeCodigo = false;
        }
        return linea;
      }
      if (dentroDeCodigo) return linea;
      const titulo = /^(#{1,6})(\s)/.exec(linea);
      if (!titulo) return linea;
      // Markdown no pasa de h6: lo que ya está al fondo se queda donde está.
      const nuevo = Math.min(6, titulo[1].length + niveles);
      return "#".repeat(nuevo) + linea.slice(titulo[1].length);
    })
    .join("\n");
}

/**
 * Nombra cada ciclo como lo vive el usuario: el primero es "Tu Plan" y cada
 * uno posterior es un seguimiento numerado. El orden es cronológico, así que
 * la posición manda; la etiqueta de base de datos no se le enseña a nadie.
 */
export function titulosDeCiclos(ciclos: CicloExpediente[]): Array<{ ciclo: CicloExpediente; titulo: string; subtitulo: string }> {
  return ciclos.map((ciclo, i) => {
    if (i === 0) {
      return { ciclo, titulo: "Tu Plan", subtitulo: "El plan con el que arrancaste" };
    }
    return {
      ciclo,
      titulo: `Seguimiento ${i}`,
      subtitulo: "Lo que pasó y el plan recalculado",
    };
  });
}

/** El índice de descargas: un documento por fase del viaje, más el completo, y
 * un Reporte por cada mundo (Fase 3, tanda 5). */
export function indiceDeDocumentos(
  ciclos: CicloExpediente[],
  realizadaAt: string | null,
  mundos: Array<{ dominio: string; nombre: string }> = [],
): DocumentoIndice[] {
  const docs: DocumentoIndice[] = titulosDeCiclos(ciclos).map(({ ciclo, titulo, subtitulo }) => ({
    clave: claveDeCiclo(ciclo.planId),
    tipo: "ciclo" as const,
    titulo,
    subtitulo,
    fecha: ciclo.createdAt,
  }));
  // El expediente y la bitácora existen desde el primer plan: antes no hay
  // desarrollo que contar, y ofrecer una descarga vacía sería prometer de más.
  if (docs.length > 0) {
    docs.push({
      clave: CLAVE_ANALISIS,
      tipo: "analisis",
      titulo: "Análisis del proyecto",
      subtitulo: "Tu ritmo, tus etapas y tu cumplimiento, calculados de lo que hiciste",
      fecha: null,
    });
    docs.push({
      clave: CLAVE_BITACORA,
      tipo: "bitacora",
      titulo: "Tu bitácora",
      subtitulo: "La historia de tu idea, paso a paso, del inicio a hoy",
      fecha: null,
    });
    docs.push({
      clave: CLAVE_EXPEDIENTE,
      tipo: "expediente",
      titulo: "Expediente completo",
      subtitulo: realizadaAt
        ? "Todo tu desarrollo, de la idea al cierre"
        : "Todo tu desarrollo hasta hoy, en un solo documento",
      fecha: realizadaAt,
    });
    // Fase 3 (tanda 5): un Reporte por cada mundo — su plan, su avance y su cómo
    // te fue, scopeado. Etiquetado con el nombre de cara del espacio.
    for (const m of mundos) {
      docs.push({
        clave: claveDeReporte(m.dominio),
        tipo: "reporte",
        titulo: `Reporte de ${m.nombre}`,
        subtitulo: "El plan, el avance y el cómo te fue de este mundo",
        fecha: null,
        espacio: m.nombre,
      });
      // Mundos de protección (P3): el registro es SU herramienta canónica, así
      // que solo existe en los tres mundos de protección (ruido cero: un mundo
      // de mejora no lo lista jamás).
      if (esMundoProteccion(m.dominio)) {
        docs.push({
          clave: claveDeRegistro(m.dominio),
          tipo: "registro",
          titulo: `Registro de ${m.nombre}`,
          subtitulo: "Lo que este mundo detectó y la respuesta que lo atiende, sobre tu plan real",
          fecha: null,
          espacio: m.nombre,
        });
      }
    }
  }
  return docs;
}

/** El markdown de un ciclo suelto, con su portadilla. */
export function cicloMarkdown(nombre: string, titulo: string, ciclo: CicloExpediente): string {
  const l: string[] = [];
  l.push(`> ${nombre} · ${titulo} · ${fechaHumanaConAno(ciclo.createdAt)}`);
  l.push("");
  l.push(ciclo.contenidoMd.trim());
  l.push("");
  return l.join("\n");
}

export function seccionAcciones(acciones: AccionExpediente[], nivelEtapa = 3): string[] {
  const l: string[] = [];
  const alm = "#".repeat(nivelEtapa);
  // Cuentas honestas (gestor de estados): el avance se mide sobre las ACTIVAS;
  // las retiradas (no_aplica) salen del denominador y van en su propia sección.
  const activas = acciones.filter((a) => a.estado !== "no_aplica");
  const retiradas = acciones.filter((a) => a.estado === "no_aplica");
  const hechas = activas.filter((a) => a.estado === "hecho");
  l.push(`Completaste **${hechas.length} de ${activas.length}** acciones activas.`);
  l.push("");
  const etapas = [...new Set(activas.map((a) => a.etapa))].sort((a, b) => a - b);
  for (const etapa of etapas) {
    l.push(`${alm} Etapa ${etapa}`);
    l.push("");
    // Las fechas se ORDENAN en una tabla, con su propia columna "Cuándo": antes
    // colgaban al final de cada línea y se leían como un desorden. La fecha va
    // como enlace-centinela para que el PDF la pinte: lo HECHO en verde
    // (cumplimiento) y lo PREVISTO en azul (planificación). El retraso no se
    // castiga: nunca rojo. En .md la tabla se lee igual de bien.
    l.push("| Acción | Cuándo |");
    l.push("| :-- | :-- |");
    for (const a of activas.filter((x) => x.etapa === etapa)) {
      const check = a.estado === "hecho" ? "✓ " : "";
      const texto = a.texto.replace(/\s+/g, " ").trim().replace(/\|/g, "\\|");
      const cuando = a.completedAt
        ? `[hecho el ${fechaHumanaConAno(a.completedAt)}](#f-hecho)`
        : a.fechaBase
          ? `[previsto para el ${fechaHumanaConAno(a.fechaBase)}](#f-prev)`
          : "sin fecha";
      l.push(`| ${check}${texto} | ${cuando} |`);
    }
    l.push("");
  }
  if (retiradas.length) {
    l.push(`${alm} Retiradas (no aplican): ${retiradas.length}`);
    l.push("");
    l.push("Tareas que decidiste que no corren para esta idea. No son pendientes ni fracasos: son parte de tu criterio.");
    l.push("");
    for (const a of retiradas) {
      const motivo = a.noAplicaMotivo ? ` (${a.noAplicaMotivo.replace(/\s+/g, " ").trim()})` : "";
      l.push(`- ${a.texto.replace(/\s+/g, " ").trim()}${motivo}`);
    }
    l.push("");
  }
  return l;
}

/**
 * El expediente completo: la idea como la escribiste, cada ciclo del plan en
 * orden, el registro de lo que hiciste y cuándo, tus números, los mundos que
 * trabajaste y, si la cerraste, cómo te fue.
 */
export function expedienteMarkdown(d: DatosExpediente): string {
  const l: string[] = [];
  // Claves de sección según el estado del proyecto (lo pidió el fundador: cada
  // punto de control con su clave clara). Mientras hay camino por delante NO se
  // habla en pasado: el registro de acciones es "Tu avance", y el resumen es
  // "Tu progreso hasta aquí". Solo al cerrar cambian a la voz de cierre.
  const tituloAcciones = d.realizadaAt ? "Lo que hiciste" : "Tu avance";
  const tituloResumen = d.realizadaAt ? "Cómo te fue" : "Tu progreso hasta aquí";

  l.push(`# ${d.nombre}`);
  l.push("");
  l.push(`> Expediente completo · generado el ${fechaHumanaConAno(d.generadoAt)}`);
  l.push("");
  l.push(`**Empezaste** el ${fechaHumanaConAno(d.creadaAt)}`);
  l.push("");
  l.push(
    d.realizadaAt
      ? `**Estado** Proyecto realizado el ${fechaHumanaConAno(d.realizadaAt)}`
      : "**Estado** En marcha"
  );
  l.push("");

  // Índice: un expediente largo se navega, no se lee de corrido.
  const secciones: string[] = ["Tu idea, tal como la escribiste"];
  if (d.organizadorMd) secciones.push("Tu idea, ordenada");
  const ciclos = titulosDeCiclos(d.ciclos);
  for (const c of ciclos) secciones.push(c.titulo);
  if (d.acciones.length) secciones.push(tituloAcciones);
  if (d.numerosMd) secciones.push("Tus Números");
  for (const m of d.mundos) if (m.contenidoMd) secciones.push(m.nombre);
  if (d.informeMd) secciones.push(tituloResumen);

  l.push("## Contenido");
  l.push("");
  for (const s of secciones) l.push(`- ${s}`);
  l.push("");
  l.push("---");
  l.push("");

  l.push("## Tu idea, tal como la escribiste");
  l.push("");
  l.push(d.entradaOriginal.trim());
  l.push("");

  if (d.organizadorMd) {
    l.push("## Tu idea, ordenada");
    l.push("");
    l.push(rebajarTitulos(d.organizadorMd.trim(), 2));
    l.push("");
  }

  for (const { ciclo, titulo } of ciclos) {
    l.push(`## ${titulo}`);
    l.push("");
    l.push(`_${fechaHumanaConAno(ciclo.createdAt)}_`);
    l.push("");
    l.push(rebajarTitulos(ciclo.contenidoMd.trim(), 2));
    l.push("");
  }

  if (d.acciones.length) {
    l.push(`## ${tituloAcciones}`);
    l.push("");
    l.push(...seccionAcciones(d.acciones));
  }

  if (d.numerosMd) {
    l.push("## Tus Números");
    l.push("");
    l.push(rebajarTitulos(d.numerosMd.trim(), 2));
    l.push("");
  }

  for (const m of d.mundos) {
    if (!m.contenidoMd) continue;
    l.push(`## ${m.nombre}`);
    l.push("");
    if (m.completadoAt) {
      l.push(`_Lo diste por terminado el ${fechaHumanaConAno(m.completadoAt)}_`);
      l.push("");
    }
    l.push(rebajarTitulos(m.contenidoMd.trim(), 2));
    l.push("");
    // Fase 3 (tanda 5): el mundo se COMPLETA con su avance y su cómo te fue, no
    // solo su plan. Las etapas van a h4 (### Etapa) bajo el ### de la sección.
    if (m.acciones && m.acciones.length) {
      l.push(`### ${m.completadoAt ? "Lo que hiciste" : "Tu avance"}`);
      l.push("");
      l.push(...seccionAcciones(m.acciones, 4));
    }
    if (m.comoTeFueMd && m.comoTeFueMd.trim()) {
      l.push(`### ${m.completadoAt ? "Cómo te fue" : "Tu progreso hasta aquí"}`);
      l.push("");
      l.push(m.comoTeFueMd.trim());
      l.push("");
    }
  }

  if (d.informeMd) {
    l.push(`## ${tituloResumen}`);
    l.push("");
    l.push(rebajarTitulos(d.informeMd.trim(), 1));
    l.push("");
  }

  if (d.cierreMotivo) {
    l.push("## Por qué la cerraste aquí");
    l.push("");
    l.push(`> ${d.cierreMotivo.replace(/\s+/g, " ").trim()}`);
    l.push("");
  }

  // Fase 4.8: la secuencia del viaje cierra el expediente (su sección final).
  if (d.bitacoraMd && d.bitacoraMd.trim()) {
    l.push("## La secuencia de tu viaje");
    l.push("");
    l.push(d.bitacoraMd.trim());
    l.push("");
  }

  return l.join("\n");
}

/** Los datos del Reporte de UN mundo (Fase 3, tanda 5): filtrados a su dominio. */
export interface DatosReporteMundo {
  nombreIdea: string;
  nombreMundo: string;
  /** el plan del mundo + sus seguimientos (ya filtrados por dominio) */
  ciclos: CicloExpediente[];
  acciones: AccionExpediente[];
  /** "cómo te fue" del mundo (resumenEspacioMd, ya armado por quien llama) */
  comoTeFueMd: string | null;
  /** la secuencia (bitácora) del mundo, scopeada, ya armada por quien llama */
  bitacoraMd: string | null;
  completadoAt: string | null;
  generadoAt: string;
}

/**
 * El Reporte de un mundo: el MISMO armador del expediente (sus builders), pero
 * scopeado a un espacio — su plan y seguimientos, su avance, su cómo te fue y su
 * secuencia. Sin las secciones del viaje principal (idea original, Tus Números):
 * un mundo es un frente, no la idea entera.
 */
export function reporteMundoMarkdown(d: DatosReporteMundo): string {
  const l: string[] = [];
  l.push(`# Reporte de ${d.nombreMundo}`);
  l.push("");
  l.push(`> ${d.nombreIdea} · generado el ${fechaHumanaConAno(d.generadoAt)}`);
  l.push("");
  l.push(d.completadoAt ? `**Estado** Terminado el ${fechaHumanaConAno(d.completadoAt)}` : "**Estado** En marcha");
  l.push("");

  // El plan del mundo + sus seguimientos, con el mismo naming ("Tu Plan",
  // "Seguimiento N") filtrado a su dominio.
  for (const { ciclo, titulo } of titulosDeCiclos(d.ciclos)) {
    l.push(`## ${titulo}`);
    l.push("");
    l.push(`_${fechaHumanaConAno(ciclo.createdAt)}_`);
    l.push("");
    l.push(rebajarTitulos(ciclo.contenidoMd.trim(), 2));
    l.push("");
  }

  if (d.acciones.length) {
    l.push(`## ${d.completadoAt ? "Lo que hiciste" : "Tu avance"}`);
    l.push("");
    l.push(...seccionAcciones(d.acciones, 3));
  }

  if (d.comoTeFueMd && d.comoTeFueMd.trim()) {
    l.push(`## ${d.completadoAt ? "Cómo te fue" : "Tu progreso hasta aquí"}`);
    l.push("");
    l.push(d.comoTeFueMd.trim());
    l.push("");
  }

  if (d.bitacoraMd && d.bitacoraMd.trim()) {
    l.push("## La secuencia de este mundo");
    l.push("");
    l.push(d.bitacoraMd.trim());
    l.push("");
  }

  return l.join("\n");
}

/** Nombre de archivo seguro para la descarga (sin extensión). */
export function nombreArchivo(nombreIdea: string, titulo: string): string {
  const limpio = (s: string) =>
    s
      .replace(/[^\p{L}\p{N} _-]/gu, "")
      .trim()
      .replace(/\s+/g, "-")
      .slice(0, 40);
  const base = limpio(nombreIdea) || "mi-idea";
  const sufijo = limpio(titulo) || "documento";
  return `${base}-${sufijo}`.toLowerCase();
}
