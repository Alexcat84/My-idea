/** El organizador de la idea (lib/engine/organizador.ts): los nombres de las
 * secciones que enciende el árbol que piensa y el markdown del organizador. */
import type { PorIdioma } from "../config";

const es = {
  /** Las secciones en el orden del contrato JSON (SECCIONES_ORGANIZADOR). */
  secciones: {
    idea_en_una_frase: "En una frase",
    etapa_detectada: "Etapa detectada",
    lo_que_ya_tienes_claro: "Lo que ya tienes claro",
    lo_que_estas_asumiendo_sin_saberlo: "Lo que estás asumiendo sin saberlo",
    areas_que_cubriria_tu_plan_completo: "Áreas de tu plan completo",
  },
  /** El markdown del organizador (construirMarkdown). */
  markdown: {
    titulo: "# Organizador de tu idea",
    enUnaFrase: "**En una frase:** {{frase}}",
    etapaDetectada: "**Etapa detectada:** {{etapa}}",
    yaTienesClaro: "## Lo que ya tienes claro",
    estasAsumiendo: "## Lo que estás asumiendo sin saberlo",
    areasDelPlan: "## Áreas que cubriría tu plan completo",
  },
};

const en: typeof es = {
  secciones: {
    idea_en_una_frase: "In one sentence",
    etapa_detectada: "Detected stage",
    lo_que_ya_tienes_claro: "What you're already clear on",
    lo_que_estas_asumiendo_sin_saberlo: "What you're assuming without realizing it",
    areas_que_cubriria_tu_plan_completo: "Areas of your full plan",
  },
  markdown: {
    titulo: "# Your idea organizer",
    enUnaFrase: "**In one sentence:** {{frase}}",
    etapaDetectada: "**Detected stage:** {{etapa}}",
    yaTienesClaro: "## What you're already clear on",
    estasAsumiendo: "## What you're assuming without realizing it",
    areasDelPlan: "## Areas your full plan would cover",
  },
};

const fr: typeof es = {
  secciones: {
    idea_en_una_frase: "En une phrase",
    etapa_detectada: "Étape détectée",
    lo_que_ya_tienes_claro: "Ce qui est déjà clair pour toi",
    lo_que_estas_asumiendo_sin_saberlo: "Ce que tu tiens pour acquis sans le savoir",
    areas_que_cubriria_tu_plan_completo: "Les volets de ton plan complet",
  },
  markdown: {
    titulo: "# L'organisateur de ton idée",
    enUnaFrase: "**En une phrase :** {{frase}}",
    etapaDetectada: "**Étape détectée :** {{etapa}}",
    yaTienesClaro: "## Ce qui est déjà clair pour toi",
    estasAsumiendo: "## Ce que tu tiens pour acquis sans le savoir",
    areasDelPlan: "## Les volets que couvrirait ton plan complet",
  },
};

const pt: typeof es = {
  secciones: {
    idea_en_una_frase: "Em uma frase",
    etapa_detectada: "Etapa detectada",
    lo_que_ya_tienes_claro: "O que já está claro para você",
    lo_que_estas_asumiendo_sin_saberlo: "O que você está supondo sem perceber",
    areas_que_cubriria_tu_plan_completo: "Áreas do seu plano completo",
  },
  markdown: {
    titulo: "# Organizador da sua ideia",
    enUnaFrase: "**Em uma frase:** {{frase}}",
    etapaDetectada: "**Etapa detectada:** {{etapa}}",
    yaTienesClaro: "## O que já está claro para você",
    estasAsumiendo: "## O que você está supondo sem perceber",
    areasDelPlan: "## Áreas que seu plano completo cobriria",
  },
};

const de: typeof es = {
  secciones: {
    idea_en_una_frase: "In einem Satz",
    etapa_detectada: "Erkannte Etappe",
    lo_que_ya_tienes_claro: "Was dir schon klar ist",
    lo_que_estas_asumiendo_sin_saberlo: "Was du annimmst, ohne es zu merken",
    areas_que_cubriria_tu_plan_completo: "Bereiche deines vollständigen Plans",
  },
  markdown: {
    titulo: "# Deine Idee, geordnet",
    enUnaFrase: "**In einem Satz:** {{frase}}",
    etapaDetectada: "**Erkannte Etappe:** {{etapa}}",
    yaTienesClaro: "## Was dir schon klar ist",
    estasAsumiendo: "## Was du annimmst, ohne es zu merken",
    areasDelPlan: "## Bereiche, die dein vollständiger Plan abdecken würde",
  },
};

const it: typeof es = {
  secciones: {
    idea_en_una_frase: "In una frase",
    etapa_detectada: "Tappa individuata",
    lo_que_ya_tienes_claro: "Quello che hai già chiaro",
    lo_que_estas_asumiendo_sin_saberlo: "Quello che stai dando per scontato senza accorgertene",
    areas_que_cubriria_tu_plan_completo: "Aree del tuo piano completo",
  },
  markdown: {
    titulo: "# La tua idea, in ordine",
    enUnaFrase: "**In una frase:** {{frase}}",
    etapaDetectada: "**Tappa individuata:** {{etapa}}",
    yaTienesClaro: "## Quello che hai già chiaro",
    estasAsumiendo: "## Quello che stai dando per scontato senza accorgertene",
    areasDelPlan: "## Aree che coprirebbe il tuo piano completo",
  },
};

const ja: typeof es = {
  secciones: {
    idea_en_una_frase: "ひとことで言うと",
    etapa_detectada: "今いるステージ",
    lo_que_ya_tienes_claro: "すでに明確なこと",
    lo_que_estas_asumiendo_sin_saberlo: "気づかずに前提にしていること",
    areas_que_cubriria_tu_plan_completo: "プラン全体の領域",
  },
  markdown: {
    titulo: "# アイデアの整理",
    enUnaFrase: "**ひとことで言うと：** {{frase}}",
    etapaDetectada: "**今いるステージ：** {{etapa}}",
    yaTienesClaro: "## すでに明確なこと",
    estasAsumiendo: "## 気づかずに前提にしていること",
    areasDelPlan: "## 完全なプランがカバーする領域",
  },
};

const zh: typeof es = {
  secciones: {
    idea_en_una_frase: "一句话概括",
    etapa_detectada: "识别出的阶段",
    lo_que_ya_tienes_claro: "你已经想清楚的",
    lo_que_estas_asumiendo_sin_saberlo: "你在不知不觉中做出的假设",
    areas_que_cubriria_tu_plan_completo: "你完整计划的各个方面",
  },
  markdown: {
    titulo: "# 你的想法整理",
    enUnaFrase: "**一句话概括**：{{frase}}",
    etapaDetectada: "**识别出的阶段**：{{etapa}}",
    yaTienesClaro: "## 你已经想清楚的",
    estasAsumiendo: "## 你在不知不觉中做出的假设",
    areasDelPlan: "## 你的完整计划会涵盖的方面",
  },
};

const ko: typeof es = {
  secciones: {
    idea_en_una_frase: "한 문장으로",
    etapa_detectada: "파악된 단계",
    lo_que_ya_tienes_claro: "이미 분명한 것",
    lo_que_estas_asumiendo_sin_saberlo: "모르는 사이에 가정하고 있는 것",
    areas_que_cubriria_tu_plan_completo: "전체 계획이 다룰 영역",
  },
  markdown: {
    titulo: "# 아이디어 정리 노트",
    enUnaFrase: "**한 문장으로:** {{frase}}",
    etapaDetectada: "**파악된 단계:** {{etapa}}",
    yaTienesClaro: "## 이미 분명한 것",
    estasAsumiendo: "## 모르는 사이에 가정하고 있는 것",
    areasDelPlan: "## 전체 계획이 다룰 영역",
  },
};

const ar: typeof es = {
  secciones: {
    idea_en_una_frase: "في جملة واحدة",
    etapa_detectada: "المرحلة المرصودة",
    lo_que_ya_tienes_claro: "ما هو واضح لكم بالفعل",
    lo_que_estas_asumiendo_sin_saberlo: "ما تفترضونه دون أن تنتبهوا",
    areas_que_cubriria_tu_plan_completo: "مجالات خطتكم الكاملة",
  },
  markdown: {
    titulo: "# منظِّم فكرتكم",
    enUnaFrase: "**في جملة واحدة:** {{frase}}",
    etapaDetectada: "**المرحلة المرصودة:** {{etapa}}",
    yaTienesClaro: "## ما هو واضح لكم بالفعل",
    estasAsumiendo: "## ما تفترضونه دون أن تنتبهوا",
    areasDelPlan: "## المجالات التي ستغطيها خطتكم الكاملة",
  },
};

const hi: typeof es = {
  secciones: {
    idea_en_una_frase: "एक वाक्य में",
    etapa_detectada: "पहचाना गया चरण",
    lo_que_ya_tienes_claro: "जो आपके लिए पहले से साफ़ है",
    lo_que_estas_asumiendo_sin_saberlo: "जो आपने बिना जाने मान लिया है",
    areas_que_cubriria_tu_plan_completo: "आपकी पूरी योजना के पहलू",
  },
  markdown: {
    titulo: "# आपके विचार की रूपरेखा",
    enUnaFrase: "**एक वाक्य में:** {{frase}}",
    etapaDetectada: "**पहचाना गया चरण:** {{etapa}}",
    yaTienesClaro: "## जो आपके लिए पहले से साफ़ है",
    estasAsumiendo: "## जो आपने बिना जाने मान लिया है",
    areasDelPlan: "## आपकी पूरी योजना किन पहलुओं को कवर करेगी",
  },
};

export const MOTOR_ORGANIZADOR: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
