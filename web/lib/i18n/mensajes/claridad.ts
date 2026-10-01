/** La Claridad (canon 03): la tarjeta del organizador en /nueva y en la idea
 * (app/ui/Claridad.tsx), el botón para explorar y el aviso de precio de La
 * Exploración (lib/avisoExploracion.ts). */
import type { PorIdioma } from "../config";

const es = {
  estoEntendi: "Esto entendí de tu idea",
  loQueYaTienes: "Lo que ya tienes",
  loQueEstasAsumiendo: "Lo que estás asumiendo",
  notaSuposiciones: "Estas suposiciones son exactamente lo que La Exploración pone a prueba, pregunta a pregunta.",
  explorarSuposiciones: "Explorar estas suposiciones",
  avisoPrecioExploracion:
    "La Exploración usa {{n}} créditos, que se cobran solo cuando recibes tu plan. Tu Claridad es gratis. Con tu cuenta queda guardada; sin cuenta, se borra a los 30 días sin actividad.",
};

const en: typeof es = {
  estoEntendi: "Here's what I understood about your idea",
  loQueYaTienes: "What you already have",
  loQueEstasAsumiendo: "What you're assuming",
  notaSuposiciones: "These assumptions are exactly what Exploration puts to the test, one question at a time.",
  explorarSuposiciones: "Explore these assumptions",
  avisoPrecioExploracion:
    "Exploration uses {{n}} credits, charged only when you receive your plan. Your Clarity is free. With your account it stays saved; without one, it's deleted after 30 days of inactivity.",
};

const fr: typeof es = {
  estoEntendi: "Voici ce que j'ai compris de ton idée",
  loQueYaTienes: "Ce que tu as déjà",
  loQueEstasAsumiendo: "Ce que tu tiens pour acquis",
  notaSuposiciones: "Ce sont justement ces hypothèses que L'Exploration met à l'épreuve, question par question.",
  explorarSuposiciones: "Explorer ces hypothèses",
  avisoPrecioExploracion: "L'Exploration utilise {{n}} crédits, prélevés seulement quand tu reçois ton plan. Ta Clarté est gratuite. Avec ton compte, elle reste enregistrée. Sans compte, elle est supprimée après 30 jours d'inactivité.",
};

const pt: typeof es = {
  estoEntendi: "Foi isto que entendi da sua ideia",
  loQueYaTienes: "O que você já tem",
  loQueEstasAsumiendo: "O que você está supondo",
  notaSuposiciones: "Essas suposições são exatamente o que A Exploração põe à prova, pergunta por pergunta.",
  explorarSuposiciones: "Explorar essas suposições",
  avisoPrecioExploracion: "A Exploração usa {{n}} créditos, que só são cobrados quando você recebe seu plano. Sua Clareza é gratuita. Com sua conta, fica guardada; sem conta, é apagada após 30 dias sem atividade.",
};

const de: typeof es = {
  estoEntendi: "Das habe ich von deiner Idee verstanden",
  loQueYaTienes: "Was du schon hast",
  loQueEstasAsumiendo: "Wovon du ausgehst",
  notaSuposiciones: "Genau diese Annahmen stellt die Erkundung auf die Probe, Frage für Frage.",
  explorarSuposiciones: "Diese Annahmen erkunden",
  avisoPrecioExploracion: "Die Erkundung kostet {{n}} Punkte, die erst abgebucht werden, wenn du deinen Plan bekommst. Deine Klarheit ist kostenlos. Mit deinem Konto bleibt sie gespeichert, ohne Konto wird sie nach 30 Tagen ohne Aktivität gelöscht.",
};

const it: typeof es = {
  estoEntendi: "Ecco cosa ho capito della tua idea",
  loQueYaTienes: "Quello che hai già",
  loQueEstasAsumiendo: "Quello che stai dando per scontato",
  notaSuposiciones: "Queste ipotesi sono proprio ciò che L'Esplorazione mette alla prova, domanda dopo domanda.",
  explorarSuposiciones: "Esplora queste ipotesi",
  avisoPrecioExploracion: "L'Esplorazione usa {{n}} crediti, che vengono scalati solo quando ricevi il tuo piano. La tua Chiarezza è gratis. Con il tuo account resta salvata; senza account viene cancellata dopo 30 giorni di inattività.",
};

const ja: typeof es = {
  estoEntendi: "アイデアを、このように理解しました",
  loQueYaTienes: "すでに持っているもの",
  loQueEstasAsumiendo: "前提にしていること",
  notaSuposiciones: "こうした前提こそ、探求で質問を一つずつ重ねながら確かめていくものです。",
  explorarSuposiciones: "この前提を探求する",
  avisoPrecioExploracion: "探求には{{n}}ポイントを使いますが、差し引かれるのはプランを受け取ったときだけです。明確さは無料です。アカウントがあれば保存され、アカウントがない場合は30日間操作がないと削除されます。",
};

const zh: typeof es = {
  estoEntendi: "这是我对你想法的理解",
  loQueYaTienes: "你已经拥有的",
  loQueEstasAsumiendo: "你正在假设的",
  notaSuposiciones: "这些假设正是“探索”要一个问题一个问题去检验的。",
  explorarSuposiciones: "探索这些假设",
  avisoPrecioExploracion: "“探索”需要{{n}}点，只在你收到计划时扣除。你的“清晰”免费。有账户就会保存；没有账户的话，30天无活动后会被删除。",
};

const ko: typeof es = {
  estoEntendi: "아이디어에서 제가 이해한 내용이에요",
  loQueYaTienes: "이미 가진 것",
  loQueEstasAsumiendo: "가정하고 있는 것",
  notaSuposiciones: "탐색 단계에서 질문 하나하나로 확인해 보는 것이 바로 이 가정들이에요.",
  explorarSuposiciones: "이 가정들 탐색하기",
  avisoPrecioExploracion: "탐색에는 {{n}}크레딧이 들고, 계획을 받을 때만 차감돼요. 명확함 단계는 무료예요. 계정이 있으면 저장되고, 계정이 없으면 30일 동안 활동이 없을 때 삭제돼요.",
};

const ar: typeof es = {
  estoEntendi: "هذا ما فهمته من فكرتكم",
  loQueYaTienes: "ما لديكم بالفعل",
  loQueEstasAsumiendo: "ما تفترضونه",
  notaSuposiciones: "هذه الافتراضات هي بالضبط ما يضعه الاستكشاف على المحك، سؤالًا بعد سؤال.",
  explorarSuposiciones: "استكشاف هذه الافتراضات",
  avisoPrecioExploracion: "يستخدم الاستكشاف {{n}} من النقاط، ولا تُخصم إلا عند استلامكم خطتكم. أما الوضوح فمجاني، ويبقى محفوظًا مع حسابكم؛ ومن دون حساب يُحذف بعد 30 يومًا دون نشاط.",
};

const hi: typeof es = {
  estoEntendi: "आपके विचार के बारे में मैंने यह समझा",
  loQueYaTienes: "जो आपके पास पहले से है",
  loQueEstasAsumiendo: "जो आपने मान रखा है",
  notaSuposiciones: "अन्वेषण सवाल दर सवाल ठीक इन्हीं मान्यताओं को परखता है।",
  explorarSuposiciones: "इन मान्यताओं की खोजबीन करें",
  avisoPrecioExploracion: "अन्वेषण में {{n}} क्रेडिट लगते हैं, जो तभी कटते हैं जब आपको अपनी योजना मिलती है। आपकी स्पष्टता मुफ़्त है। खाते के साथ यह सहेजी रहती है; खाते के बिना 30 दिन तक कोई गतिविधि न होने पर यह मिट जाती है।",
};

export const CLARIDAD: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
