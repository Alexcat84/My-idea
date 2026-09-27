/** El riel del recorrido (app/ui/ArbolPensante.tsx). */
import type { PorIdioma } from "../config";

const es = {
  fueUnSalto: "fue un salto",
  generandoCon: "generando: {{etiqueta}}",
  generando: "generando…",
};

const en: typeof es = {
  fueUnSalto: "a jump in topic",
  generandoCon: "generating: {{etiqueta}}",
  generando: "generating…",
};

const fr: typeof es = {
  fueUnSalto: "changement de sujet",
  generandoCon: "génération : {{etiqueta}}",
  generando: "génération…",
};

const pt: typeof es = {
  fueUnSalto: "foi um salto",
  generandoCon: "gerando: {{etiqueta}}",
  generando: "gerando…",
};

const de: typeof es = {
  fueUnSalto: "war ein Sprung",
  generandoCon: "entsteht gerade: {{etiqueta}}",
  generando: "entsteht gerade…",
};

const it: typeof es = {
  fueUnSalto: "un salto di tema",
  generandoCon: "in generazione: {{etiqueta}}",
  generando: "in generazione…",
};

const ja: typeof es = {
  fueUnSalto: "話題が飛びました",
  generandoCon: "生成中：{{etiqueta}}",
  generando: "生成中…",
};

const zh: typeof es = {
  fueUnSalto: "换了个话题",
  generandoCon: "正在生成：{{etiqueta}}",
  generando: "正在生成…",
};

const ko: typeof es = {
  fueUnSalto: "주제 전환",
  generandoCon: "생성 중: {{etiqueta}}",
  generando: "생성 중…",
};

const ar: typeof es = {
  fueUnSalto: "قفزة إلى موضوع آخر",
  generandoCon: "جارٍ الإنشاء: {{etiqueta}}",
  generando: "جارٍ الإنشاء…",
};

const hi: typeof es = {
  fueUnSalto: "यह एक छलांग थी",
  generandoCon: "बन रहा है: {{etiqueta}}",
  generando: "बन रहा है…",
};

export const ARBOL_PENSANTE: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
