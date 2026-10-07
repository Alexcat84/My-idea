/**
 * Los nombres visibles de las recargas de lib/precios.ts (PACKS) y para qué
 * alcanza cada una. SOLO texto: las cifras viven en precios.ts y solo ahí
 * (AGENTS.md). Las claves son el `clave` de cada pack.
 */
import type { PorIdioma } from "../config";

const es = {
  recarga: { nombre: "Recarga", alcanza: "un seguimiento o el plan de un mundo" },
  basico: { nombre: "Básico", alcanza: "tu plan completo, con tus números incluidos" },
  premium: { nombre: "Premium", alcanza: "tu plan y tu primer seguimiento" },
  profesional: { nombre: "Profesional", alcanza: "tu plan, dos seguimientos y un mundo con su seguimiento" },
};

const en: typeof es = {
  recarga: { nombre: "Top-up", alcanza: "one follow-up or the plan for a world" },
  basico: { nombre: "Basic", alcanza: "your full plan, with your numbers included" },
  premium: { nombre: "Premium", alcanza: "your plan and your first follow-up" },
  profesional: { nombre: "Professional", alcanza: "your plan, two follow-ups, and a world with its follow-up" },
};

const fr: typeof es = {
  recarga: {
    nombre: "Recharge",
    alcanza: "un suivi ou le plan d'un monde",
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
    alcanza: "ton plan, deux suivis et un monde avec son suivi",
  },
};

const pt: typeof es = {
  recarga: {
    nombre: "Recarga",
    alcanza: "um acompanhamento ou o plano de um mundo",
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
    alcanza: "seu plano, dois acompanhamentos e um mundo com seu acompanhamento",
  },
};

const de: typeof es = {
  recarga: {
    nombre: "Aufladung",
    alcanza: "ein Zwischenstand oder der Plan für eine Welt",
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
    alcanza: "dein Plan, zwei Zwischenstände und eine Welt mit ihrem Zwischenstand",
  },
};

const it: typeof es = {
  recarga: {
    nombre: "Ricarica",
    alcanza: "una revisione o il piano di un mondo",
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
    alcanza: "il tuo piano, due revisioni e un mondo con la sua revisione",
  },
};

const ja: typeof es = {
  recarga: {
    nombre: "チャージ",
    alcanza: "フォローアップ1回、またはワールド1つのプラン",
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
    alcanza: "プラン、フォローアップ2回、ワールド1つとそのフォローアップ",
  },
};

const zh: typeof es = {
  recarga: {
    nombre: "充值包",
    alcanza: "一次跟进，或一个世界的计划",
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
    alcanza: "你的计划、两次跟进，以及一个世界和它的跟进",
  },
};

const ko: typeof es = {
  recarga: {
    nombre: "충전",
    alcanza: "후속 점검 한 번 또는 월드 하나의 계획",
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
    alcanza: "계획, 후속 점검 두 번, 월드 하나와 그 후속 점검",
  },
};

const ar: typeof es = {
  recarga: {
    nombre: "شحن",
    alcanza: "متابعة واحدة أو خطة عالم",
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
    alcanza: "خطتكم، ومتابعتان، وعالم واحد مع متابعته",
  },
};

const hi: typeof es = {
  recarga: {
    nombre: "रिचार्ज",
    alcanza: "एक फ़ॉलो-अप या एक दुनिया की योजना",
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
    alcanza: "आपकी योजना, दो फ़ॉलो-अप, और एक दुनिया उसके फ़ॉलो-अप के साथ",
  },
};

export const PACKS_RECARGA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
