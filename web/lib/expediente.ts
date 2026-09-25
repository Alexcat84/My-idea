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
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { interpolar } from "./i18n/interpolar";
import { EXPEDIENTE } from "./i18n/mensajes/expediente";

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
  /** i18n F3: un ciclo posterior al primero (un Seguimiento). La UI elige su
   * ícono por aquí: el título está en el idioma de quien lo lee. */
  seguimiento?: boolean;
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
export function titulosDeCiclos(
  ciclos: CicloExpediente[],
  idioma: Locale = LOCALE_BASE
): Array<{ ciclo: CicloExpediente; titulo: string; subtitulo: string }> {
  const t = elegir(EXPEDIENTE, idioma).ciclos;
  return ciclos.map((ciclo, i) => {
    if (i === 0) {
      return { ciclo, titulo: t.tuPlan, subtitulo: t.tuPlanSubtitulo };
    }
    return {
      ciclo,
      titulo: interpolar(t.seguimiento, { n: i }),
      subtitulo: t.seguimientoSubtitulo,
    };
  });
}

/** El índice de descargas: un documento por fase del viaje, más el completo, y
 * un Reporte por cada mundo (Fase 3, tanda 5). */
export function indiceDeDocumentos(
  ciclos: CicloExpediente[],
  realizadaAt: string | null,
  mundos: Array<{ dominio: string; nombre: string }> = [],
  idioma: Locale = LOCALE_BASE,
): DocumentoIndice[] {
  const t = elegir(EXPEDIENTE, idioma).indice;
  const docs: DocumentoIndice[] = titulosDeCiclos(ciclos, idioma).map(({ ciclo, titulo, subtitulo }, i) => ({
    clave: claveDeCiclo(ciclo.planId),
    tipo: "ciclo" as const,
    seguimiento: i > 0,
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
      titulo: t.analisisTitulo,
      subtitulo: t.analisisSubtitulo,
      fecha: null,
    });
    docs.push({
      clave: CLAVE_BITACORA,
      tipo: "bitacora",
      titulo: t.bitacoraTitulo,
      subtitulo: t.bitacoraSubtitulo,
      fecha: null,
    });
    docs.push({
      clave: CLAVE_EXPEDIENTE,
      tipo: "expediente",
      titulo: t.expedienteTitulo,
      // AUD-09 M35: dice exactamente lo que incluye (antes "Todo tu
      // desarrollo", y el tablero vivo de Tus Números no entra aquí).
      subtitulo: realizadaAt ? t.expedienteSubtituloCerrado : t.expedienteSubtituloEnMarcha,
      fecha: realizadaAt,
    });
    // Fase 3 (tanda 5): un Reporte por cada mundo — su plan, su avance y su cómo
    // te fue, scopeado. Etiquetado con el nombre de cara del espacio.
    for (const m of mundos) {
      docs.push({
        clave: claveDeReporte(m.dominio),
        tipo: "reporte",
        titulo: interpolar(t.reporteTitulo, { mundo: m.nombre }),
        subtitulo: t.reporteSubtitulo,
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
          titulo: interpolar(t.registroTitulo, { mundo: m.nombre }),
          subtitulo: t.registroSubtitulo,
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

export function seccionAcciones(acciones: AccionExpediente[], nivelEtapa = 3, idioma: Locale = LOCALE_BASE): string[] {
  const t = elegir(EXPEDIENTE, idioma).acciones;
  const l: string[] = [];
  const alm = "#".repeat(nivelEtapa);
  // Cuentas honestas (gestor de estados): el avance se mide sobre las ACTIVAS;
  // las retiradas (no_aplica) salen del denominador y van en su propia sección.
  const activas = acciones.filter((a) => a.estado !== "no_aplica");
  const retiradas = acciones.filter((a) => a.estado === "no_aplica");
  const hechas = activas.filter((a) => a.estado === "hecho");
  l.push(interpolar(t.completaste, { hechas: hechas.length, total: activas.length }));
  l.push("");
  const etapas = [...new Set(activas.map((a) => a.etapa))].sort((a, b) => a - b);
  for (const etapa of etapas) {
    l.push(`${alm} ${interpolar(t.etapa, { n: etapa })}`);
    l.push("");
    // Las fechas se ORDENAN en una tabla, con su propia columna "Cuándo": antes
    // colgaban al final de cada línea y se leían como un desorden. La fecha va
    // como enlace-centinela para que el PDF la pinte: lo HECHO en verde
    // (cumplimiento) y lo PREVISTO en azul (planificación). El retraso no se
    // castiga: nunca rojo. En .md la tabla se lee igual de bien.
    l.push(t.tablaEncabezado);
    l.push("| :-- | :-- |");
    for (const a of activas.filter((x) => x.etapa === etapa)) {
      const check = a.estado === "hecho" ? "✓ " : "";
      const texto = a.texto.replace(/\s+/g, " ").trim().replace(/\|/g, "\\|");
      const cuando = a.completedAt
        ? interpolar(t.hechoEl, { fecha: fechaHumanaConAno(a.completedAt, idioma) })
        : a.fechaBase
          ? interpolar(t.previstoPara, { fecha: fechaHumanaConAno(a.fechaBase, idioma) })
          : t.sinFecha;
      l.push(`| ${check}${texto} | ${cuando} |`);
    }
    l.push("");
  }
  if (retiradas.length) {
    l.push(`${alm} ${interpolar(t.retiradas, { n: retiradas.length })}`);
    l.push("");
    l.push(t.retiradasExplicacion);
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
export function expedienteMarkdown(d: DatosExpediente, idioma: Locale = LOCALE_BASE): string {
  const t = elegir(EXPEDIENTE, idioma).expediente;
  const l: string[] = [];
  // Claves de sección según el estado del proyecto (lo pidió el fundador: cada
  // punto de control con su clave clara). Mientras hay camino por delante NO se
  // habla en pasado: el registro de acciones es "Tu avance", y el resumen es
  // "Tu progreso hasta aquí". Solo al cerrar cambian a la voz de cierre.
  const tituloAcciones = d.realizadaAt ? t.loQueHiciste : t.tuAvance;
  const tituloResumen = d.realizadaAt ? t.comoTeFue : t.tuProgreso;

  l.push(`# ${d.nombre}`);
  l.push("");
  l.push(interpolar(t.generado, { fecha: fechaHumanaConAno(d.generadoAt, idioma) }));
  l.push("");
  l.push(interpolar(t.empezaste, { fecha: fechaHumanaConAno(d.creadaAt, idioma) }));
  l.push("");
  l.push(
    d.realizadaAt
      ? interpolar(t.estadoRealizado, { fecha: fechaHumanaConAno(d.realizadaAt, idioma) })
      : t.estadoEnMarcha
  );
  l.push("");

  // Índice: un expediente largo se navega, no se lee de corrido.
  // El índice lista los mismos títulos de sección, sin su "## ".
  const sinAlmohadillas = (titulo: string) => titulo.replace(/^#+\s+/, "");
  const secciones: string[] = [sinAlmohadillas(t.tituloIdeaEscrita)];
  if (d.organizadorMd) secciones.push(sinAlmohadillas(t.tituloIdeaOrdenada));
  const ciclos = titulosDeCiclos(d.ciclos, idioma);
  for (const c of ciclos) secciones.push(c.titulo);
  if (d.acciones.length) secciones.push(tituloAcciones);
  if (d.numerosMd) secciones.push(sinAlmohadillas(t.tituloNumeros));
  for (const m of d.mundos) if (m.contenidoMd) secciones.push(m.nombre);
  if (d.informeMd) secciones.push(tituloResumen);

  l.push(t.tituloContenido);
  l.push("");
  for (const s of secciones) l.push(`- ${s}`);
  l.push("");
  l.push("---");
  l.push("");

  l.push(t.tituloIdeaEscrita);
  l.push("");
  l.push(d.entradaOriginal.trim());
  l.push("");

  if (d.organizadorMd) {
    l.push(t.tituloIdeaOrdenada);
    l.push("");
    l.push(rebajarTitulos(d.organizadorMd.trim(), 2));
    l.push("");
  }

  for (const { ciclo, titulo } of ciclos) {
    l.push(`## ${titulo}`);
    l.push("");
    l.push(`_${fechaHumanaConAno(ciclo.createdAt, idioma)}_`);
    l.push("");
    l.push(rebajarTitulos(ciclo.contenidoMd.trim(), 2));
    l.push("");
  }

  if (d.acciones.length) {
    l.push(`## ${tituloAcciones}`);
    l.push("");
    l.push(...seccionAcciones(d.acciones, 3, idioma));
  }

  if (d.numerosMd) {
    l.push(t.tituloNumeros);
    l.push("");
    l.push(rebajarTitulos(d.numerosMd.trim(), 2));
    l.push("");
  }

  for (const m of d.mundos) {
    if (!m.contenidoMd) continue;
    l.push(`## ${m.nombre}`);
    l.push("");
    if (m.completadoAt) {
      l.push(interpolar(t.mundoTerminado, { fecha: fechaHumanaConAno(m.completadoAt, idioma) }));
      l.push("");
    }
    l.push(rebajarTitulos(m.contenidoMd.trim(), 2));
    l.push("");
    // Fase 3 (tanda 5): el mundo se COMPLETA con su avance y su cómo te fue, no
    // solo su plan. Las etapas van a h4 (### Etapa) bajo el ### de la sección.
    if (m.acciones && m.acciones.length) {
      l.push(`### ${m.completadoAt ? t.loQueHiciste : t.tuAvance}`);
      l.push("");
      l.push(...seccionAcciones(m.acciones, 4, idioma));
    }
    if (m.comoTeFueMd && m.comoTeFueMd.trim()) {
      l.push(`### ${m.completadoAt ? t.comoTeFue : t.tuProgreso}`);
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
    l.push(t.tituloPorQueCerraste);
    l.push("");
    l.push(`> ${d.cierreMotivo.replace(/\s+/g, " ").trim()}`);
    l.push("");
  }

  // Fase 4.8: la secuencia del viaje cierra el expediente (su sección final).
  if (d.bitacoraMd && d.bitacoraMd.trim()) {
    l.push(t.tituloSecuencia);
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
export function reporteMundoMarkdown(d: DatosReporteMundo, idioma: Locale = LOCALE_BASE): string {
  const cat = elegir(EXPEDIENTE, idioma);
  const t = cat.reporteMundo;
  const tx = cat.expediente;
  const l: string[] = [];
  l.push(interpolar(t.titulo, { mundo: d.nombreMundo }));
  l.push("");
  l.push(interpolar(t.generado, { idea: d.nombreIdea, fecha: fechaHumanaConAno(d.generadoAt, idioma) }));
  l.push("");
  l.push(d.completadoAt ? interpolar(t.estadoTerminado, { fecha: fechaHumanaConAno(d.completadoAt, idioma) }) : tx.estadoEnMarcha);
  l.push("");

  // El plan del mundo + sus seguimientos, con el mismo naming ("Tu Plan",
  // "Seguimiento N") filtrado a su dominio.
  for (const { ciclo, titulo } of titulosDeCiclos(d.ciclos, idioma)) {
    l.push(`## ${titulo}`);
    l.push("");
    l.push(`_${fechaHumanaConAno(ciclo.createdAt, idioma)}_`);
    l.push("");
    l.push(rebajarTitulos(ciclo.contenidoMd.trim(), 2));
    l.push("");
  }

  if (d.acciones.length) {
    l.push(`## ${d.completadoAt ? tx.loQueHiciste : tx.tuAvance}`);
    l.push("");
    l.push(...seccionAcciones(d.acciones, 3, idioma));
  }

  if (d.comoTeFueMd && d.comoTeFueMd.trim()) {
    l.push(`## ${d.completadoAt ? tx.comoTeFue : tx.tuProgreso}`);
    l.push("");
    l.push(d.comoTeFueMd.trim());
    l.push("");
  }

  if (d.bitacoraMd && d.bitacoraMd.trim()) {
    l.push(t.tituloSecuencia);
    l.push("");
    l.push(d.bitacoraMd.trim());
    l.push("");
  }

  return l.join("\n");
}

/** Nombre de archivo seguro para la descarga (sin extensión). */
export function nombreArchivo(nombreIdea: string, titulo: string, idioma: Locale = LOCALE_BASE): string {
  const t = elegir(EXPEDIENTE, idioma).archivo;
  const limpio = (s: string) =>
    s
      .replace(/[^\p{L}\p{M}\p{N} _-]/gu, "")
      .trim()
      .replace(/\s+/g, "-")
      .slice(0, 40);
  const base = limpio(nombreIdea) || t.ideaPorOmision;
  const sufijo = limpio(titulo) || t.documentoPorOmision;
  return `${base}-${sufijo}`.toLowerCase();
}

/** AUD-09 M02/M03: las tareas del CICLO VIGENTE de cada espacio (el último plan
 * de ciclo: inicial, completo o seguimiento). El tablero cuenta solo ese ciclo;
 * los documentos también, o dicen "22 de 53" donde el tablero dice "3 de 25".
 * Los ciclos anteriores viven en sus propias secciones del Expediente. Pura. */
export function accionesDelCicloVigente<T extends { plan_id?: string | null; dominio: string | null }>(
  acciones: T[],
  planes: ReadonlyArray<{ id: string; dominio: string | null; etiqueta: string; created_at: string }>
): T[] {
  const vigente = new Map<string, { id: string; t: number }>();
  for (const p of planes) {
    if (!["inicial", "completo", "seguimiento"].includes(p.etiqueta)) continue;
    const d = p.dominio || "core";
    const t = new Date(p.created_at).getTime();
    const actual = vigente.get(d);
    if (!actual || t > actual.t) vigente.set(d, { id: p.id, t });
  }
  return acciones.filter((a) => a.plan_id != null && vigente.get(a.dominio || "core")?.id === a.plan_id);
}
