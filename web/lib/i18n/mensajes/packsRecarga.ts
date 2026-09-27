/**
 * Los nombres visibles de las recargas de lib/precios.ts (PACKS) y para qué
 * alcanza cada una. SOLO texto: las cifras viven en precios.ts y solo ahí
 * (AGENTS.md). Las claves son el `clave` de cada pack.
 */
import type { PorIdioma } from "../config";

const es = {
  recarga: { nombre: "Recarga", alcanza: "un seguimiento o un mundo suelto" },
  basico: { nombre: "Básico", alcanza: "tu plan completo, con tus números incluidos" },
  premium: { nombre: "Premium", alcanza: "tu plan y tu primer seguimiento" },
  profesional: { nombre: "Profesional", alcanza: "el viaje entero de una idea" },
};

const en: typeof es = {
  recarga: { nombre: "Top-up", alcanza: "one follow-up or a single world" },
  basico: { nombre: "Basic", alcanza: "your full plan, with your numbers included" },
  premium: { nombre: "Premium", alcanza: "your plan and your first follow-up" },
  profesional: { nombre: "Professional", alcanza: "an idea's whole journey" },
};

const fr: typeof es = {
  recarga: {
    nombre: "Recharge",
    alcanza: "un suivi ou un seul monde",
  },
  basico: {
    nombre: "Essentiel",
    alcanza: "ton plan complet, avec tes chiffres inclus",
  },
  premium: {
    nombre: "Premium",
    alcanza: "ton plan et ton premier suivi",
  },
  profesional: {
    nombre: "Professionnel",
    alcanza: "le parcours complet d'une idée",
  },
};

const pt: typeof es = {
  recarga: {
    nombre: "Recarga",
    alcanza: "um acompanhamento ou um mundo avulso",
  },
  basico: {
    nombre: "Básico",
    alcanza: "seu plano completo, com seus números incluídos",
  },
  premium: {
    nombre: "Premium",
    alcanza: "seu plano e seu primeiro acompanhamento",
  },
  profesional: {
    nombre: "Profissional",
    alcanza: "a jornada inteira de uma ideia",
  },
};

const de: typeof es = {
  recarga: {
    nombre: "Aufladung",
    alcanza: "ein Zwischenstand oder eine einzelne Welt",
  },
  basico: {
    nombre: "Basis",
    alcanza: "dein vollständiger Plan, inklusive deiner Zahlen",
  },
  premium: {
    nombre: "Premium",
    alcanza: "dein Plan und dein erster Zwischenstand",
  },
  profesional: {
    nombre: "Profi",
    alcanza: "die ganze Reise einer Idee",
  },
};

const it: typeof es = {
  recarga: {
    nombre: "Ricarica",
    alcanza: "una revisione o un singolo mondo",
  },
  basico: {
    nombre: "Base",
    alcanza: "il tuo piano completo, con i tuoi numeri inclusi",
  },
  premium: {
    nombre: "Premium",
    alcanza: "il tuo piano e la tua prima revisione",
  },
  profesional: {
    nombre: "Professionale",
    alcanza: "l'intero viaggio di un'idea",
  },
};

const ja: typeof es = {
  recarga: {
    nombre: "チャージ",
    alcanza: "フォローアップ1回、またはワールド1つ",
  },
  basico: {
    nombre: "ベーシック",
    alcanza: "プラン一式（あなたの数字つき）",
  },
  premium: {
    nombre: "プレミアム",
    alcanza: "プランと最初のフォローアップ",
  },
  profesional: {
    nombre: "プロフェッショナル",
    alcanza: "ひとつのアイデアの旅のすべて",
  },
};

const zh: typeof es = {
  recarga: {
    nombre: "充值包",
    alcanza: "一次跟进，或单独一个世界",
  },
  basico: {
    nombre: "基础版",
    alcanza: "你的完整计划，含“你的数字”",
  },
  premium: {
    nombre: "高级版",
    alcanza: "你的计划和第一次跟进",
  },
  profesional: {
    nombre: "专业版",
    alcanza: "一个想法的完整旅程",
  },
};

const ko: typeof es = {
  recarga: {
    nombre: "충전",
    alcanza: "후속 점검 한 번 또는 월드 하나",
  },
  basico: {
    nombre: "베이직",
    alcanza: "나의 숫자까지 포함한 전체 계획",
  },
  premium: {
    nombre: "프리미엄",
    alcanza: "계획과 첫 후속 점검",
  },
  profesional: {
    nombre: "프로페셔널",
    alcanza: "아이디어 하나의 여정 전체",
  },
};

const ar: typeof es = {
  recarga: {
    nombre: "شحن",
    alcanza: "متابعة واحدة أو عالم منفرد",
  },
  basico: {
    nombre: "أساسي",
    alcanza: "خطتكم الكاملة، وأرقامكم ضمنها",
  },
  premium: {
    nombre: "مميّز",
    alcanza: "خطتكم وأول متابعة لها",
  },
  profesional: {
    nombre: "احترافي",
    alcanza: "رحلة فكرة كاملة من أولها إلى آخرها",
  },
};

const hi: typeof es = {
  recarga: {
    nombre: "रिचार्ज",
    alcanza: "एक फ़ॉलो-अप या एक अकेली दुनिया",
  },
  basico: {
    nombre: "बेसिक",
    alcanza: "आपकी पूरी योजना, आपके आंकड़ों के साथ",
  },
  premium: {
    nombre: "प्रीमियम",
    alcanza: "आपकी योजना और आपका पहला फ़ॉलो-अप",
  },
  profesional: {
    nombre: "प्रोफ़ेशनल",
    alcanza: "एक विचार की पूरी यात्रा",
  },
};

export const PACKS_RECARGA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
