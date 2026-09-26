/**
 * Los MARCADORES NEUTROS del plan (i18n F5, DISENO §5).
 *
 * El markdown de un plan se GUARDA siempre con sus rótulos de estructura en
 * español ("## Etapa N:", "**Pasos:**", "**Entregable:**", "**Primera acción:**",
 * "**El lunes que viene:**", la sección económica, "_Plan completo_" y "## Lo
 * que este plan aún no cubre"): son las claves que leen checklist.ts,
 * planParser.ts y el redactor. El contenido va en el idioma de la idea.
 *
 * Decisión del fundador (26 sep 2026): la acción de cada etapa dejó de ser
 * "**Esta semana:**" (prometía tiempos imposibles entre etapas secuenciales) y
 * es "**Primera acción:**", sin fecha. Los planes guardados antes siguen con el
 * rótulo viejo y no se regeneran: `neutralizarRotulos` lo lleva al nuevo (y
 * también su traducción) y `pintarRotulos` lo muestra como "Primera acción" en
 * el idioma de quien lee, español incluido.
 *
 * - `neutralizarRotulos`: si la IA tradujo un rótulo pese a la regla (o lo
 *   escribió con otra puntuación), vuelve a su forma neutra ANTES de guardar.
 * - `pintarRotulos`: la pantalla y los documentos lo muestran en el idioma de
 *   quien lee.
 *
 * Las palabras salen de los catálogos (MOTOR_PLAN y PLAN_DOCUMENTO): una sola
 * fuente, la misma que ya pinta la pantalla.
 */
import { ACTIVE_LOCALES, elegir, LOCALE_BASE, type ActiveLocale, type Locale } from "./config";
import { interpolar } from "./interpolar";
import { MOTOR_PLAN } from "./mensajes/motorPlan";
import { PLAN_DOCUMENTO } from "./mensajes/planDocumento";

export interface RotulosPlan {
  /** "## Etapa {{n}}: {{concepto}}" en el idioma. */
  etapaPlantilla: string;
  /** El rótulo de la acción de cada etapa (el marcador neutro que se guarda). */
  primeraAccion: string;
  /** El rótulo VIEJO de esa acción: solo se lee (planes guardados, IA terca). */
  estaSemana: string;
  elLunes: string;
  entregable: string;
  pasos: string;
  etiquetaCompleto: string;
  etiquetaInicial: string;
  /** Sin el "## ". */
  noCubre: string;
  seccionEconomica: string;
  /** Los dos puntos del idioma: " :" (con espacio de no separación) en francés, "：" en japonés y chino. */
  dosPuntos: string;
}

// El francés, con el espacio de no separación de sus catálogos (U+00A0).
const DOS_PUNTOS: Record<Locale, string> = {
  es: ":",
  en: ":",
  pt: ":",
  fr: "\u00a0:",
  de: ":",
  it: ":",
  ja: "：",
  zh: "：",
  ko: ":",
  ar: ":",
  hi: ":",
};

export function rotulosPlan(idioma: Locale): RotulosPlan {
  const m = elegir(MOTOR_PLAN, idioma);
  const d = elegir(PLAN_DOCUMENTO, idioma);
  return {
    etapaPlantilla: m.offline.etapa,
    primeraAccion: d.primeraAccion,
    estaSemana: d.estaSemana,
    elLunes: m.elLunes,
    entregable: d.entregable,
    pasos: d.pasos,
    etiquetaCompleto: m.etiquetaCompleto,
    etiquetaInicial: m.etiquetaInicial,
    noCubre: m.noCubre.replace(/^##\s*/, ""),
    seccionEconomica: m.seccionEconomica,
    dosPuntos: DOS_PUNTOS[idioma],
  };
}

const NEUTRO = rotulosPlan(LOCALE_BASE);

function escapar(x: string): string {
  return x.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

/** La pregunta de la sección económica (hasta su signo de cierre). */
function preguntaEconomica(sec: string): string {
  const i = sec.search(/[?？؟]/);
  return i >= 0 ? sec.slice(0, i + 1) : sec;
}

/** "## Stage 3: X" (en cualquier idioma, con cualquier separador) → [3, "X"]. */
function reEtapa(plantilla: string): RegExp {
  const cuerpo = plantilla.replace(/^##\s*/, "");
  const [antes, resto] = cuerpo.split("{{n}}");
  const despues = resto.split("{{concepto}}")[0].replace(/[\s:：.·\-—–]+/g, "");
  return new RegExp(
    `^##\\s*${escapar(antes.trim())}\\s*(\\d+)\\s*${escapar(despues)}\\s*(?:[:：.·\\-—–]\\s*)?(.*)$`,
    "u"
  );
}

/** "**This week:**", "**This week**:", "**This week :**" → el resto de la línea.
 * Tolera la "ó" escrita sin tilde ("Primera accion"): el prompt va sin tildes y
 * la IA a veces lo imita. */
function reEtiqueta(palabra: string): RegExp {
  return new RegExp(`^\\*\\*\\s*${escapar(palabra).replace(/ó/g, "[oó]")}\\s*[:：]?\\s*\\*\\*\\s*[:：]?\\s*(.*)$`, "u");
}

interface Lector {
  etapa: RegExp;
  etiquetas: Array<[RegExp, keyof Pick<RotulosPlan, "primeraAccion" | "estaSemana" | "elLunes" | "entregable" | "pasos">]>;
  r: RotulosPlan;
}

const LECTORES: Lector[] = ACTIVE_LOCALES.map((l) => {
  const r = rotulosPlan(l);
  return {
    r,
    etapa: reEtapa(r.etapaPlantilla),
    etiquetas: (["primeraAccion", "estaSemana", "elLunes", "entregable", "pasos"] as const).map((k) => [reEtiqueta(r[k]), k]),
  };
});

function neutralizarLinea(linea: string): string {
  const t = linea.trim();
  for (const { r, etapa, etiquetas } of LECTORES) {
    const me = etapa.exec(t);
    if (me) return `## Etapa ${me[1]}: ${me[2].trim()}`.trimEnd();
    for (const [re, k] of etiquetas) {
      // "**Pasos para construir:**" del español se queda como está.
      if (r === NEUTRO && k === "pasos") continue;
      const mk = re.exec(t);
      // El rótulo viejo (o su traducción) es el mismo campo: se guarda con el nuevo.
      const neutro = k === "estaSemana" ? NEUTRO.primeraAccion : NEUTRO[k];
      if (mk) return `**${neutro}:**${mk[1] ? ` ${mk[1]}` : ""}`;
    }
    if (t === `_${r.etiquetaCompleto}_`) return `_${NEUTRO.etiquetaCompleto}_`;
    if (t === `_${r.etiquetaInicial}_`) return `_${NEUTRO.etiquetaInicial}_`;
    if (t === `## ${r.noCubre}`) return `## ${NEUTRO.noCubre}`;
    if (t.startsWith(`## ${preguntaEconomica(r.seccionEconomica)}`)) return `## ${NEUTRO.seccionEconomica}`;
  }
  return linea;
}

/** Devuelve los rótulos de estructura a su forma neutra (la que se guarda). */
export function neutralizarRotulos(md: string): string {
  return md
    .split("\n")
    .map((l) => neutralizarLinea(l))
    .join("\n");
}

const RE_ETAPA_NEUTRA = /^##\s+Etapa\s+(\d+)\s*:\s*(.*)$/;
const RE_PASOS_NEUTRA = /^\*\*\s*Pasos\b[^*]*?:?\s*\*\*\s*(.*)$/;

const RE_ESTA_SEMANA_NEUTRA = reEtiqueta(NEUTRO.estaSemana);

/** Pinta los rótulos neutros en el idioma de quien lee. En español, solo el
 * rótulo viejo "**Esta semana:**" de los planes guardados, que se muestra como
 * "**Primera acción:**" (decisión del fundador, 26 sep 2026). */
export function pintarRotulos(md: string, idioma: ActiveLocale): string {
  const r = rotulosPlan(idioma);
  const etiqueta = (palabra: string, resto: string) => `**${palabra}${r.dosPuntos}**${resto ? ` ${resto}` : ""}`;
  return md
    .split("\n")
    .map((linea) => {
      const t = linea.trim();
      const mv = RE_ESTA_SEMANA_NEUTRA.exec(t);
      if (mv) return etiqueta(r.primeraAccion, mv[1]);
      if (idioma === LOCALE_BASE) return linea;
      const me = RE_ETAPA_NEUTRA.exec(t);
      if (me) return interpolar(r.etapaPlantilla, { n: me[1], concepto: me[2].trim() }).trimEnd();
      const mp = RE_PASOS_NEUTRA.exec(t);
      if (mp) return etiqueta(r.pasos, mp[1]);
      for (const k of ["primeraAccion", "elLunes", "entregable"] as const) {
        const m = reEtiqueta(NEUTRO[k]).exec(t);
        if (m) return etiqueta(r[k], m[1]);
      }
      if (t === `_${NEUTRO.etiquetaCompleto}_`) return `_${r.etiquetaCompleto}_`;
      if (t === `_${NEUTRO.etiquetaInicial}_`) return `_${r.etiquetaInicial}_`;
      if (t === `## ${NEUTRO.noCubre}`) return `## ${r.noCubre}`;
      if (t.startsWith(`## ${preguntaEconomica(NEUTRO.seccionEconomica)}`)) return `## ${r.seccionEconomica}`;
      return linea;
    })
    .join("\n");
}

/** Para la pantalla (planParser.ts): el texto de UN rótulo ya separado de su
 * marca markdown, pintado en el idioma. `forma` dice cuál era la marca. */
export function pintarRotulo(texto: string, forma: "encabezado" | "etiqueta" | "negrita", idioma: ActiveLocale): string {
  if (idioma === LOCALE_BASE) return texto;
  if (forma === "encabezado") return pintarRotulos(`## ${texto}`, idioma).replace(/^##\s*/, "");
  if (forma === "etiqueta") return pintarRotulos(`_${texto}_`, idioma).replace(/^_|_$/g, "");
  const r = rotulosPlan(idioma);
  return /^Pasos\b/.test(texto) ? r.pasos : texto;
}
