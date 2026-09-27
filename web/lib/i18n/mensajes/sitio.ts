/** El sitio entero (app/layout.tsx): metadatos y el sello de versión. El título "My Idea" es la marca y no pasa por aquí. */
import type { PorIdioma } from "../config";

const es = {
  descripcion: "El espacio donde tus ideas se trabajan.",
  /** aria-label del sello de versión al pie de cada página. */
  etiquetaVersion: "versión",
};

const en: typeof es = {
  descripcion: "The space where your ideas get worked out.",
  etiquetaVersion: "version",
};

const fr: typeof es = {
  descripcion: "L'espace où tes idées prennent forme.",
  etiquetaVersion: "version",
};

const pt: typeof es = {
  descripcion: "O espaço onde suas ideias ganham forma.",
  etiquetaVersion: "versão",
};

const de: typeof es = {
  descripcion: "Der Ort, an dem du deine Ideen ausarbeitest.",
  etiquetaVersion: "Version",
};

const it: typeof es = {
  descripcion: "Lo spazio dove le tue idee prendono forma.",
  etiquetaVersion: "versione",
};

const ja: typeof es = {
  descripcion: "アイデアを形にしていく場所。",
  etiquetaVersion: "バージョン",
};

const zh: typeof es = {
  descripcion: "打磨你每一个想法的地方。",
  etiquetaVersion: "版本",
};

const ko: typeof es = {
  descripcion: "아이디어를 다듬어 가는 공간.",
  etiquetaVersion: "버전",
};

const ar: typeof es = {
  descripcion: "المساحة التي تعملون فيها على أفكاركم.",
  etiquetaVersion: "الإصدار",
};

const hi: typeof es = {
  descripcion: "वह जगह जहाँ आपके विचारों पर काम होता है।",
  etiquetaVersion: "संस्करण",
};

export const SITIO: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
