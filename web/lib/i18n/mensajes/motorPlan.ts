/** El redactor del plan (lib/engine/planRedactor.ts): lo que el código escribe en
 * el plan sin la IA. El aviso del plan básico, el plan armado sin IA (ensamblado
 * offline), la etiqueta del plan y el encabezado de lo que aún no cubre. */
import type { PorIdioma } from "../config";

const es = {
  avisoVersionBasica:
    "Esta es una versión básica de tu plan: la armé sin la redacción con IA porque esta conversación llegó a su tope de trabajo. No se te cobró. Puedes regenerarlo completo desde lo que ya me contaste: solo se cobra si la IA lo entrega.",
  /** El plan armado sin la IA (ensamblarOffline). "## Etapa N:" es además el
   * marcador que lee checklist.ts. */
  offline: {
    titulo: "# Tu plan de acción",
    contexto: "## Contexto",
    puntoDePartida: "Punto de partida: {{texto}}",
    loQueSabemos: "Lo que sabemos de tu idea: {{perfil}}",
    etapa: "## Etapa {{n}}: {{concepto}}",
    puntoDeControl: "Punto de control: {{entregable}}",
  },
  etiquetaCompleto: "Plan completo",
  etiquetaInicial: "Plan inicial",
  noCubre: "## Lo que este plan aún no cubre",
  /** i18n F5: rótulos del plan que pinta lib/i18n/rotulosPlan.ts (el neutro es
   * el español: "**El lunes que viene:**" y la sección económica). */
  elLunes: "El lunes que viene",
  seccionEconomica: "¿Puede sostenerse tu idea? Los números en simple",
};

const en: typeof es = {
  avisoVersionBasica:
    "This is a basic version of your plan: I put it together without the AI write-up because this conversation reached its work limit. You weren't charged. You can regenerate the full plan from what you already told me: you're only charged if the AI delivers it.",
  offline: {
    titulo: "# Your action plan",
    contexto: "## Context",
    puntoDePartida: "Starting point: {{texto}}",
    loQueSabemos: "What we know about your idea: {{perfil}}",
    etapa: "## Stage {{n}}: {{concepto}}",
    puntoDeControl: "Checkpoint: {{entregable}}",
  },
  etiquetaCompleto: "Full plan",
  etiquetaInicial: "Initial plan",
  noCubre: "## What this plan doesn't cover yet",
  elLunes: "Next Monday",
  seccionEconomica: "Can your idea sustain itself? The numbers, simply put",
};

const fr: typeof es = {
  avisoVersionBasica: "Voici une version de base de ton plan : je l'ai préparée sans la rédaction par IA, parce que cette conversation a atteint sa limite de travail. Rien ne t'a été facturé. Tu peux le régénérer au complet à partir de ce que tu m'as déjà raconté : tu ne paies que si l'IA le livre.",
  offline: {
    titulo: "# Ton plan d'action",
    contexto: "## Contexte",
    puntoDePartida: "Point de départ : {{texto}}",
    loQueSabemos: "Ce que nous savons de ton idée : {{perfil}}",
    etapa: "## Étape {{n}} : {{concepto}}",
    puntoDeControl: "Point de contrôle : {{entregable}}",
  },
  etiquetaCompleto: "Plan complet",
  etiquetaInicial: "Plan initial",
  noCubre: "## Ce que ce plan ne couvre pas encore",
  elLunes: "Lundi prochain",
  seccionEconomica: "Ton idée peut-elle tenir la route? Les chiffres en clair",
};

const pt: typeof es = {
  avisoVersionBasica: "Esta é uma versão básica do seu plano: eu a montei sem a redação com IA porque esta conversa chegou ao limite de trabalho. Nada foi cobrado. Você pode gerá-lo de novo completo a partir do que já me contou: só há cobrança se a IA entregar.",
  offline: {
    titulo: "# Seu plano de ação",
    contexto: "## Contexto",
    puntoDePartida: "Ponto de partida: {{texto}}",
    loQueSabemos: "O que sabemos da sua ideia: {{perfil}}",
    etapa: "## Etapa {{n}}: {{concepto}}",
    puntoDeControl: "Ponto de controle: {{entregable}}",
  },
  etiquetaCompleto: "Plano completo",
  etiquetaInicial: "Plano inicial",
  noCubre: "## O que este plano ainda não cobre",
  elLunes: "Na próxima segunda-feira",
  seccionEconomica: "Sua ideia se sustenta? Os números de um jeito simples",
};

const de: typeof es = {
  avisoVersionBasica: "Das ist eine einfache Version deines Plans: Ich habe sie ohne die Ausarbeitung durch die KI erstellt, weil dieses Gespräch an seine Arbeitsgrenze gekommen ist. Dir wurde nichts berechnet. Du kannst den vollständigen Plan aus dem, was du mir schon erzählt hast, neu erstellen lassen: Berechnet wird nur, wenn die KI ihn liefert.",
  offline: {
    titulo: "# Dein Handlungsplan",
    contexto: "## Kontext",
    puntoDePartida: "Ausgangspunkt: {{texto}}",
    loQueSabemos: "Was wir über deine Idee wissen: {{perfil}}",
    etapa: "## Etappe {{n}}: {{concepto}}",
    puntoDeControl: "Kontrollpunkt: {{entregable}}",
  },
  etiquetaCompleto: "Vollständiger Plan",
  etiquetaInicial: "Erster Plan",
  noCubre: "## Was dieser Plan noch nicht abdeckt",
  elLunes: "Nächsten Montag",
  seccionEconomica: "Kann sich deine Idee tragen? Die Zahlen, einfach erklärt",
};

const it: typeof es = {
  avisoVersionBasica: "Questa è una versione base del tuo piano: l'ho preparata senza la stesura con l'IA perché questa conversazione ha raggiunto il suo limite di lavoro. Non ti è stato addebitato nulla. Puoi rigenerarlo completo a partire da quello che mi hai già raccontato: paghi solo se l'IA lo consegna.",
  offline: {
    titulo: "# Il tuo piano d'azione",
    contexto: "## Contesto",
    puntoDePartida: "Punto di partenza: {{texto}}",
    loQueSabemos: "Quello che sappiamo della tua idea: {{perfil}}",
    etapa: "## Tappa {{n}}: {{concepto}}",
    puntoDeControl: "Punto di controllo: {{entregable}}",
  },
  etiquetaCompleto: "Piano completo",
  etiquetaInicial: "Piano iniziale",
  noCubre: "## Cosa questo piano non copre ancora",
  elLunes: "Lunedì prossimo",
  seccionEconomica: "La tua idea può reggersi? I numeri in parole semplici",
};

const ja: typeof es = {
  avisoVersionBasica: "これはプランの基本版です。この会話が作業量の上限に達したため、AIによる文章作成なしでまとめました。ポイントは差し引かれていません。すでに話してくれた内容から、完全版を作り直せます。ポイントが差し引かれるのは、AIが完全版をお届けした場合だけです。",
  offline: {
    titulo: "# アクションプラン",
    contexto: "## 背景",
    puntoDePartida: "出発点：{{texto}}",
    loQueSabemos: "アイデアについてわかっていること：{{perfil}}",
    etapa: "## ステージ{{n}}：{{concepto}}",
    puntoDeControl: "チェックポイント：{{entregable}}",
  },
  etiquetaCompleto: "完全版プラン",
  etiquetaInicial: "最初のプラン",
  noCubre: "## このプランがまだカバーしていないこと",
  elLunes: "次の月曜日",
  seccionEconomica: "あなたのアイデアは続けていけますか？ 数字をわかりやすく",
};

const zh: typeof es = {
  avisoVersionBasica: "这是你计划的基础版：这次对话已经达到工作上限，所以我没用AI撰写，先把它整理了出来。没有向你收费。你可以根据你已经告诉我的内容重新生成完整版：只有AI交付了才会收费。",
  offline: {
    titulo: "# 你的行动计划",
    contexto: "## 背景",
    puntoDePartida: "起点：{{texto}}",
    loQueSabemos: "我们对你的想法的了解：{{perfil}}",
    etapa: "## 第{{n}}阶段：{{concepto}}",
    puntoDeControl: "检查点：{{entregable}}",
  },
  etiquetaCompleto: "完整计划",
  etiquetaInicial: "初始计划",
  noCubre: "## 这份计划还没涵盖的内容",
  elLunes: "下周一",
  seccionEconomica: "你的想法能持续下去吗？ 用简单的话看数字",
};

const ko: typeof es = {
  avisoVersionBasica: "이건 계획의 기본 버전이에요. 이 대화가 작업 한도에 도달해서 AI 작성 없이 만들었어요. 크레딧은 차감되지 않았어요. 이미 들려준 내용으로 전체 계획을 다시 만들 수 있고, AI가 전달할 때만 차감돼요.",
  offline: {
    titulo: "# 나의 실행 계획",
    contexto: "## 배경",
    puntoDePartida: "출발점: {{texto}}",
    loQueSabemos: "아이디어에 대해 알고 있는 것: {{perfil}}",
    etapa: "## {{n}}단계: {{concepto}}",
    puntoDeControl: "점검 지점: {{entregable}}",
  },
  etiquetaCompleto: "전체 계획",
  etiquetaInicial: "초기 계획",
  noCubre: "## 이 계획이 아직 다루지 않는 것",
  elLunes: "다음 월요일",
  seccionEconomica: "아이디어가 지속될 수 있을까요? 쉽게 보는 숫자",
};

const ar: typeof es = {
  avisoVersionBasica: "هذه نسخة أساسية من خطتكم: أعددتها دون الصياغة بالذكاء الاصطناعي لأن هذه المحادثة بلغت حدّها من العمل. لم يُخصم منكم شيء. يمكنكم إعادة إنشائها كاملة مما رويتموه لي: ولا يُخصم شيء إلا إذا سلّمها الذكاء الاصطناعي.",
  offline: {
    titulo: "# خطة عملكم",
    contexto: "## السياق",
    puntoDePartida: "نقطة البداية: {{texto}}",
    loQueSabemos: "ما نعرفه عن فكرتكم: {{perfil}}",
    etapa: "## المرحلة {{n}}: {{concepto}}",
    puntoDeControl: "نقطة التحقّق: {{entregable}}",
  },
  etiquetaCompleto: "الخطة الكاملة",
  etiquetaInicial: "الخطة الأولى",
  noCubre: "## ما لا تغطيه هذه الخطة بعد",
  elLunes: "يوم الإثنين القادم",
  seccionEconomica: "هل يمكن أن تستمر فكرتكم؟ الأرقام ببساطة",
};

const hi: typeof es = {
  avisoVersionBasica: "यह आपकी योजना का एक बुनियादी संस्करण है: इसे AI के लेखन के बिना बनाया गया, क्योंकि यह बातचीत अपने काम की सीमा तक पहुँच गई। आपसे कुछ नहीं काटा गया। आपने जो पहले ही बताया है, उसी से पूरी योजना फिर से बनवाई जा सकती है: क्रेडिट तभी कटते हैं जब AI उसे पूरा करके देता है।",
  offline: {
    titulo: "# आपकी कार्य योजना",
    contexto: "## संदर्भ",
    puntoDePartida: "शुरुआती बिंदु: {{texto}}",
    loQueSabemos: "आपके विचार के बारे में हम जो जानते हैं: {{perfil}}",
    etapa: "## चरण {{n}}: {{concepto}}",
    puntoDeControl: "जाँच बिंदु: {{entregable}}",
  },
  etiquetaCompleto: "पूरी योजना",
  etiquetaInicial: "शुरुआती योजना",
  noCubre: "## यह योजना अभी क्या कवर नहीं करती",
  elLunes: "अगले सोमवार",
  seccionEconomica: "क्या आपका विचार टिक सकता है? आंकड़े आसान भाषा में",
};

export const MOTOR_PLAN: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
