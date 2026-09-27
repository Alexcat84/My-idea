/** El cierre honesto cuando el motor decide salir (app/ui/CierreHonesto.tsx, canon 12). */
import type { PorIdioma } from "../config";

const es = {
  unAltoHonesto: "Un alto honesto",
  activacionDevuelta: { one: "Activación devuelta · {{n}} crédito", other: "Activación devuelta · {{n}} créditos" },
  porQueEsteMundo: "Por qué este mundo, no ahora",
  loQueVi: "Lo que vi",
  teDevolvimos: {
    one: "Te devolvimos {{n}} crédito de la activación. Nunca pierdes créditos por algo que no te sirvió.",
    other: "Te devolvimos {{n}} créditos de la activación. Nunca pierdes créditos por algo que no te sirvió.",
  },
  volverAManos: "Volver a Manos a la Obra",
  volverAMiIdea: "Volver a mi idea",
  verOtrosMundos: "Ver los otros mundos",
  explorarOtroAngulo: "Explorar otro ángulo de la idea",
  notaMundo: "Tu viaje principal sigue intacto: cerrar este mundo no toca tu idea.",
  notaCamino: "Nada se pierde: tu recorrido y tu Claridad quedan guardados tal como están.",
};

const en: typeof es = {
  unAltoHonesto: "An honest stop",
  activacionDevuelta: { one: "Activation refunded · {{n}} credit", other: "Activation refunded · {{n}} credits" },
  porQueEsteMundo: "Why this world isn't for now",
  loQueVi: "What I saw",
  teDevolvimos: {
    one: "We refunded {{n}} credit from the activation. You never lose credits on something that didn't help you.",
    other: "We refunded {{n}} credits from the activation. You never lose credits on something that didn't help you.",
  },
  volverAManos: "Back to Get to Work",
  volverAMiIdea: "Back to my idea",
  verOtrosMundos: "See the other worlds",
  explorarOtroAngulo: "Explore another angle of the idea",
  notaMundo: "Your main journey is still intact: closing this world doesn't touch your idea.",
  notaCamino: "Nothing is lost: your path and your Clarity stay saved just as they are.",
};

const fr: typeof es = {
  unAltoHonesto: "Un arrêt honnête",
  activacionDevuelta: {
    one: "Activation remboursée · {{n}} crédit",
    other: "Activation remboursée · {{n}} crédits",
  },
  porQueEsteMundo: "Pourquoi pas ce monde, pour l'instant",
  loQueVi: "Ce que j'ai vu",
  teDevolvimos: {
    one: "Nous t'avons rendu {{n}} crédit de l'activation. Tu ne perds jamais de crédits pour quelque chose qui ne t'a pas servi.",
    other: "Nous t'avons rendu {{n}} crédits de l'activation. Tu ne perds jamais de crédits pour quelque chose qui ne t'a pas servi.",
  },
  volverAManos: "Revenir à « À l'ouvrage »",
  volverAMiIdea: "Revenir à mon idée",
  verOtrosMundos: "Voir les autres mondes",
  explorarOtroAngulo: "Explorer un autre angle de l'idée",
  notaMundo: "Ton parcours principal reste intact : fermer ce monde ne touche pas à ton idée.",
  notaCamino: "Rien ne se perd : ton cheminement et ta Clarté restent enregistrés tels quels.",
};

const pt: typeof es = {
  unAltoHonesto: "Uma parada honesta",
  activacionDevuelta: {
    one: "Ativação devolvida · {{n}} crédito",
    other: "Ativação devolvida · {{n}} créditos",
  },
  porQueEsteMundo: "Por que este mundo fica para depois",
  loQueVi: "O que eu vi",
  teDevolvimos: {
    one: "Devolvemos {{n}} crédito da ativação. Você nunca perde créditos por algo que não serviu para você.",
    other: "Devolvemos {{n}} créditos da ativação. Você nunca perde créditos por algo que não serviu para você.",
  },
  volverAManos: "Voltar para Mãos à Obra",
  volverAMiIdea: "Voltar para minha ideia",
  verOtrosMundos: "Ver os outros mundos",
  explorarOtroAngulo: "Explorar outro ângulo da ideia",
  notaMundo: "Sua jornada principal continua intacta: encerrar este mundo não mexe na sua ideia.",
  notaCamino: "Nada se perde: seu percurso e sua Clareza ficam salvos exatamente como estão.",
};

const de: typeof es = {
  unAltoHonesto: "Ein ehrlicher Halt",
  activacionDevuelta: {
    one: "Aktivierung erstattet · {{n}} Punkt",
    other: "Aktivierung erstattet · {{n}} Punkte",
  },
  porQueEsteMundo: "Warum diese Welt jetzt noch nicht passt",
  loQueVi: "Was ich gesehen habe",
  teDevolvimos: {
    one: "Wir haben dir {{n}} Punkt für die Aktivierung erstattet. Für etwas, das dir nichts gebracht hat, verlierst du nie Guthaben.",
    other: "Wir haben dir {{n}} Punkte für die Aktivierung erstattet. Für etwas, das dir nichts gebracht hat, verlierst du nie Guthaben.",
  },
  volverAManos: "Zurück zu „Ans Werk“",
  volverAMiIdea: "Zurück zu meiner Idee",
  verOtrosMundos: "Die anderen Welten ansehen",
  explorarOtroAngulo: "Die Idee aus einem anderen Blickwinkel erkunden",
  notaMundo: "Deine Hauptreise bleibt unberührt: Diese Welt abzuschließen ändert nichts an deiner Idee.",
  notaCamino: "Nichts geht verloren: Dein Weg und deine Klarheit bleiben genau so gespeichert, wie sie sind.",
};

const it: typeof es = {
  unAltoHonesto: "Una sosta onesta",
  activacionDevuelta: {
    one: "Attivazione rimborsata · {{n}} credito",
    other: "Attivazione rimborsata · {{n}} crediti",
  },
  porQueEsteMundo: "Perché questo mondo non è per adesso",
  loQueVi: "Cosa ho visto",
  teDevolvimos: {
    one: "Ti abbiamo restituito {{n}} credito dell'attivazione. Non perdi mai crediti per qualcosa che non ti è servito.",
    other: "Ti abbiamo restituito {{n}} crediti dell'attivazione. Non perdi mai crediti per qualcosa che non ti è servito.",
  },
  volverAManos: "Torna alla tappa Al lavoro",
  volverAMiIdea: "Torna alla mia idea",
  verOtrosMundos: "Vedi gli altri mondi",
  explorarOtroAngulo: "Esplora un'altra angolazione dell'idea",
  notaMundo: "Il tuo viaggio principale resta intatto: chiudere questo mondo non tocca la tua idea.",
  notaCamino: "Non si perde nulla: il tuo percorso e la tua Chiarezza restano salvati così come sono.",
};

const ja: typeof es = {
  unAltoHonesto: "正直なひと区切り",
  activacionDevuelta: {
    one: "有効化分を返却 · {{n}}ポイント",
    other: "有効化分を返却 · {{n}}ポイント",
  },
  porQueEsteMundo: "このワールドが今ではない理由",
  loQueVi: "見えたこと",
  teDevolvimos: {
    one: "有効化に使った{{n}}ポイントをお返ししました。役に立たなかったもので、ポイントを失うことはありません。",
    other: "有効化に使った{{n}}ポイントをお返ししました。役に立たなかったもので、ポイントを失うことはありません。",
  },
  volverAManos: "「実行」に戻る",
  volverAMiIdea: "アイデアに戻る",
  verOtrosMundos: "ほかのワールドを見る",
  explorarOtroAngulo: "アイデアを別の角度から探る",
  notaMundo: "メインの旅はそのままです。このワールドを閉じても、アイデアには影響しません。",
  notaCamino: "何も失われません。これまでの道のりと「明確さ」は、今のまま保存されています。",
};

const zh: typeof es = {
  unAltoHonesto: "坦诚地停一停",
  activacionDevuelta: {
    one: "已退还开启费用 · {{n}}点",
    other: "已退还开启费用 · {{n}}点",
  },
  porQueEsteMundo: "为什么这个世界现在还不合适",
  loQueVi: "我看到的情况",
  teDevolvimos: {
    one: "开启时用掉的{{n}}点已退还给你。没帮上你的东西，绝不会让你白花点数。",
    other: "开启时用掉的{{n}}点已退还给你。没帮上你的东西，绝不会让你白花点数。",
  },
  volverAManos: "返回动手做",
  volverAMiIdea: "返回我的想法",
  verOtrosMundos: "看看其他世界",
  explorarOtroAngulo: "从另一个角度探索这个想法",
  notaMundo: "你的主旅程完好无损：关闭这个世界不会影响你的想法。",
  notaCamino: "什么都不会丢：你的探索路径和“清晰”阶段的成果都原样保存。",
};

const ko: typeof es = {
  unAltoHonesto: "솔직한 멈춤",
  activacionDevuelta: {
    one: "활성화 비용 환불 · {{n}}크레딧",
    other: "활성화 비용 환불 · {{n}}크레딧",
  },
  porQueEsteMundo: "이 월드가 지금은 아닌 이유",
  loQueVi: "제가 본 것",
  teDevolvimos: {
    one: "활성화에 쓴 {{n}}크레딧을 돌려드렸어요. 도움이 되지 않은 일에 크레딧을 잃는 일은 절대 없어요.",
    other: "활성화에 쓴 {{n}}크레딧을 돌려드렸어요. 도움이 되지 않은 일에 크레딧을 잃는 일은 절대 없어요.",
  },
  volverAManos: "실행하기로 돌아가기",
  volverAMiIdea: "내 아이디어로 돌아가기",
  verOtrosMundos: "다른 월드 보기",
  explorarOtroAngulo: "아이디어를 다른 각도에서 탐색하기",
  notaMundo: "메인 여정은 그대로예요. 이 월드를 닫아도 아이디어에는 영향이 없어요.",
  notaCamino: "잃는 건 없어요. 탐색 경로와 명확함 단계의 결과는 지금 그대로 저장돼 있어요.",
};

const ar: typeof es = {
  unAltoHonesto: "وقفة صادقة",
  activacionDevuelta: {
    one: "استرداد التفعيل · {{n}} نقطة",
    other: "استرداد التفعيل · {{n}} من النقاط",
  },
  porQueEsteMundo: "لماذا لا يناسبكم هذا العالم الآن",
  loQueVi: "ما رأيته",
  teDevolvimos: {
    one: "أعدنا إليكم ما دفعتموه للتفعيل: {{n}} نقطة. لا تخسرون رصيدًا أبدًا على شيء لم يفدكم.",
    other: "أعدنا إليكم ما دفعتموه للتفعيل: {{n}} من النقاط. لا تخسرون رصيدًا أبدًا على شيء لم يفدكم.",
  },
  volverAManos: "العودة إلى «إلى العمل»",
  volverAMiIdea: "العودة إلى فكرتي",
  verOtrosMundos: "عرض العوالم الأخرى",
  explorarOtroAngulo: "استكشاف زاوية أخرى للفكرة",
  notaMundo: "رحلتكم الرئيسية باقية كما هي: إغلاق هذا العالم لا يمسّ فكرتكم.",
  notaCamino: "لا يضيع شيء: مساركم ومرحلة «الوضوح» لديكم محفوظان كما هما.",
};

const hi: typeof es = {
  unAltoHonesto: "एक ईमानदार ठहराव",
  activacionDevuelta: {
    one: "सक्रिय करने का शुल्क लौटाया गया · {{n}} क्रेडिट",
    other: "सक्रिय करने का शुल्क लौटाया गया · {{n}} क्रेडिट",
  },
  porQueEsteMundo: "यह दुनिया अभी क्यों नहीं",
  loQueVi: "मैंने क्या देखा",
  teDevolvimos: {
    one: "हमने सक्रिय करने का {{n}} क्रेडिट आपको लौटा दिया है। जो चीज़ आपके काम नहीं आई, उसके लिए आपके क्रेडिट कभी नहीं कटते।",
    other: "हमने सक्रिय करने के {{n}} क्रेडिट आपको लौटा दिए हैं। जो चीज़ आपके काम नहीं आई, उसके लिए आपके क्रेडिट कभी नहीं कटते।",
  },
  volverAManos: "“काम शुरू करें” पर लौटें",
  volverAMiIdea: "मेरे विचार पर लौटें",
  verOtrosMundos: "बाकी दुनियाएँ देखें",
  explorarOtroAngulo: "विचार का कोई दूसरा पहलू खोजें",
  notaMundo: "आपकी मुख्य यात्रा जैसी थी वैसी ही है: इस दुनिया को बंद करने से आपके विचार पर कोई असर नहीं पड़ता।",
  notaCamino: "कुछ भी नहीं खोता: आपका रास्ता और आपकी स्पष्टता जैसे हैं, वैसे ही सहेजे रहते हैं।",
};

export const CIERRE_HONESTO: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
