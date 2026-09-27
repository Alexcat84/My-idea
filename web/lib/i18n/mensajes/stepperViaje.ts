/** El stepper del viaje (app/ui/Stepper.tsx): los seis hitos (términos de marca
 * del glosario) y la etiqueta accesible del riel. */
import type { PorIdioma } from "../config";

const es = {
  etapas: ["La Chispa", "Claridad", "La Exploración", "Tu Plan", "Manos a la Obra", "Realizado"],
  ariaEtapa: "Etapa {{etapa}} de {{total}}: {{nombre}}",
};

const en: typeof es = {
  etapas: ["The Spark", "Clarity", "Exploration", "Your Plan", "Get to Work", "Achieved"],
  ariaEtapa: "Stage {{etapa}} of {{total}}: {{nombre}}",
};

const fr: typeof es = {
  etapas: ["L'Étincelle", "Clarté", "L'Exploration", "Ton plan", "À l'ouvrage", "Réalisé"],
  ariaEtapa: "Étape {{etapa}} sur {{total}} : {{nombre}}",
};

const pt: typeof es = {
  etapas: ["A Faísca", "Clareza", "A Exploração", "Seu Plano", "Mãos à Obra", "Realizado"],
  ariaEtapa: "Etapa {{etapa}} de {{total}}: {{nombre}}",
};

const de: typeof es = {
  etapas: ["Der Funke", "Klarheit", "Die Erkundung", "Dein Plan", "Ans Werk", "Verwirklicht"],
  ariaEtapa: "Etappe {{etapa}} von {{total}}: {{nombre}}",
};

const it: typeof es = {
  etapas: ["La Scintilla", "Chiarezza", "L'Esplorazione", "Il tuo piano", "Al lavoro", "Realizzato"],
  ariaEtapa: "Tappa {{etapa}} di {{total}}: {{nombre}}",
};

const ja: typeof es = {
  etapas: ["ひらめき", "明確さ", "探求", "あなたのプラン", "実行", "実現"],
  ariaEtapa: "ステージ{{etapa}}/{{total}}：{{nombre}}",
};

const zh: typeof es = {
  etapas: ["灵光一闪", "清晰", "探索", "你的计划", "动手做", "已实现"],
  ariaEtapa: "第 {{etapa}} 阶段，共 {{total}} 个阶段：{{nombre}}",
};

const ko: typeof es = {
  etapas: ["불꽃", "명확함", "탐색", "나의 계획", "실행하기", "실현"],
  ariaEtapa: "{{total}}단계 중 {{etapa}}단계: {{nombre}}",
};

const ar: typeof es = {
  etapas: ["الشرارة", "الوضوح", "الاستكشاف", "خطتكم", "إلى العمل", "تحقّق"],
  ariaEtapa: "المرحلة {{etapa}} من {{total}}: {{nombre}}",
};

const hi: typeof es = {
  etapas: ["चिंगारी", "स्पष्टता", "अन्वेषण", "आपकी योजना", "काम शुरू करें", "साकार"],
  ariaEtapa: "{{total}} में से चरण {{etapa}}: {{nombre}}",
};

export const STEPPER_VIAJE: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
