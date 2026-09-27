/** El registro de un mundo de protección (lib/registroProteccion.ts): la
 * severidad y el camino en palabras (fuente única para pantalla y papel) y el
 * documento descargable. Los "## " y "### " son estructura markdown. */
import type { PorIdioma } from "../config";

const es = {
  probabilidad: {
    poco_probable: "poco probable",
    probable: "probable",
    muy_probable: "muy probable",
  },
  dolor: {
    poco: "dolería poco",
    bastante: "dolería bastante",
    mucho: "dolería mucho",
  },
  camino: {
    evitar: "evitarlo",
    mitigar: "reducirlo",
    transferir: "pasárselo a otro",
    aceptar: "aceptarlo con los ojos abiertos",
  },
  severidad: "{{probabilidad}} y {{dolor}}",
  protegidaDesaparecida: "la actividad que protegía ya no está en tu plan",
  negocioEntero: "tu negocio entero",
  registroVacio:
    "No alcancé a enlazar este plan con tus actividades: sus respuestas están en tu plan, pero este registro quedó vacío.",
  documento: {
    titulo: "## Registro de {{mundo}}",
    queTanSerio: "Qué tan serio: {{severidad}}.",
    elCamino: "El camino: {{camino}}.",
    queProtege: "Qué protege: {{protege}}.",
    tuRespuesta: "Tu respuesta: {{respuesta}}",
  },
};

const en: typeof es = {
  probabilidad: {
    poco_probable: "unlikely",
    probable: "likely",
    muy_probable: "very likely",
  },
  dolor: {
    poco: "would hurt a little",
    bastante: "would hurt quite a bit",
    mucho: "would hurt a lot",
  },
  camino: {
    evitar: "avoid it",
    mitigar: "reduce it",
    transferir: "hand it off to someone else",
    aceptar: "accept it with your eyes open",
  },
  severidad: "{{probabilidad}} and {{dolor}}",
  protegidaDesaparecida: "the activity it protected is no longer in your plan",
  negocioEntero: "your whole business",
  registroVacio:
    "I couldn't link this plan to your activities: its answers are in your plan, but this register came out empty.",
  documento: {
    titulo: "## {{mundo}} register",
    queTanSerio: "How serious: {{severidad}}.",
    elCamino: "The path: {{camino}}.",
    queProtege: "What it protects: {{protege}}.",
    tuRespuesta: "Your response: {{respuesta}}",
  },
};

const fr: typeof es = {
  probabilidad: {
    poco_probable: "peu probable",
    probable: "probable",
    muy_probable: "très probable",
  },
  dolor: {
    poco: "ferait peu mal",
    bastante: "ferait assez mal",
    mucho: "ferait très mal",
  },
  camino: {
    evitar: "l'éviter",
    mitigar: "le réduire",
    transferir: "le confier à quelqu'un d'autre",
    aceptar: "l'accepter en toute connaissance de cause",
  },
  severidad: "{{probabilidad}} et {{dolor}}",
  protegidaDesaparecida: "l'activité qu'il protégeait n'est plus dans ton plan",
  negocioEntero: "toute ton entreprise",
  registroVacio: "Je n'ai pas réussi à relier ce plan à tes activités : ses réponses sont dans ton plan, mais ce registre est resté vide.",
  documento: {
    titulo: "## Registre de {{mundo}}",
    queTanSerio: "Gravité : {{severidad}}.",
    elCamino: "La voie choisie : {{camino}}.",
    queProtege: "Ce qu'il protège : {{protege}}.",
    tuRespuesta: "Ta réponse : {{respuesta}}",
  },
};

const pt: typeof es = {
  probabilidad: {
    poco_probable: "pouco provável",
    probable: "provável",
    muy_probable: "muito provável",
  },
  dolor: {
    poco: "doeria pouco",
    bastante: "doeria bastante",
    mucho: "doeria muito",
  },
  camino: {
    evitar: "evitá-lo",
    mitigar: "reduzi-lo",
    transferir: "passá-lo para outra pessoa",
    aceptar: "aceitá-lo de olhos abertos",
  },
  severidad: "{{probabilidad}} e {{dolor}}",
  protegidaDesaparecida: "a atividade que ele protegia já não está no seu plano",
  negocioEntero: "seu negócio inteiro",
  registroVacio: "Não consegui ligar este plano às suas atividades: as respostas dele estão no seu plano, mas este registro ficou vazio.",
  documento: {
    titulo: "## Registro de {{mundo}}",
    queTanSerio: "Quão sério é: {{severidad}}.",
    elCamino: "O caminho: {{camino}}.",
    queProtege: "O que protege: {{protege}}.",
    tuRespuesta: "Sua resposta: {{respuesta}}",
  },
};

const de: typeof es = {
  probabilidad: {
    poco_probable: "unwahrscheinlich",
    probable: "wahrscheinlich",
    muy_probable: "sehr wahrscheinlich",
  },
  dolor: {
    poco: "würde wenig wehtun",
    bastante: "würde ziemlich wehtun",
    mucho: "würde sehr wehtun",
  },
  camino: {
    evitar: "vermeiden",
    mitigar: "verringern",
    transferir: "an jemand anderen abgeben",
    aceptar: "bewusst in Kauf nehmen",
  },
  severidad: "{{probabilidad}} und {{dolor}}",
  protegidaDesaparecida: "eine Aufgabe, die nicht mehr in deinem Plan steht",
  negocioEntero: "dein ganzes Geschäft",
  registroVacio: "Ich konnte diesen Plan nicht mit deinen Aufgaben verknüpfen: Seine Antworten stehen in deinem Plan, aber dieses Register ist leer geblieben.",
  documento: {
    titulo: "## Register für {{mundo}}",
    queTanSerio: "Wie ernst: {{severidad}}.",
    elCamino: "Der Umgang damit: {{camino}}.",
    queProtege: "Was es schützt: {{protege}}.",
    tuRespuesta: "Deine Antwort: {{respuesta}}",
  },
};

const it: typeof es = {
  probabilidad: {
    poco_probable: "poco probabile",
    probable: "probabile",
    muy_probable: "molto probabile",
  },
  dolor: {
    poco: "farebbe poco male",
    bastante: "farebbe abbastanza male",
    mucho: "farebbe molto male",
  },
  camino: {
    evitar: "evitarlo",
    mitigar: "ridurlo",
    transferir: "passarlo a qualcun altro",
    aceptar: "accettarlo a occhi aperti",
  },
  severidad: "{{probabilidad}} e {{dolor}}",
  protegidaDesaparecida: "l'attività che proteggeva non è più nel tuo piano",
  negocioEntero: "tutta la tua attività",
  registroVacio: "Non ho potuto collegare questo piano alle tue attività: le sue risposte sono nel tuo piano, ma questo registro è rimasto vuoto.",
  documento: {
    titulo: "## Registro di {{mundo}}",
    queTanSerio: "Quanto è serio: {{severidad}}.",
    elCamino: "La strada: {{camino}}.",
    queProtege: "Cosa protegge: {{protege}}.",
    tuRespuesta: "La tua risposta: {{respuesta}}",
  },
};

const ja: typeof es = {
  probabilidad: {
    poco_probable: "起こりにくい",
    probable: "起こりそう",
    muy_probable: "かなり起こりそう",
  },
  dolor: {
    poco: "痛手は小さい",
    bastante: "痛手はそれなりに大きい",
    mucho: "痛手はとても大きい",
  },
  camino: {
    evitar: "避ける",
    mitigar: "減らす",
    transferir: "ほかに引き受けてもらう",
    aceptar: "承知のうえで受け入れる",
  },
  severidad: "{{probabilidad}}、{{dolor}}",
  protegidaDesaparecida: "守っていたアクションは、もうプランにありません",
  negocioEntero: "ビジネス全体",
  registroVacio: "このプランをアクションと結びつけられませんでした。回答はプランに入っていますが、この記録簿は空のままです。",
  documento: {
    titulo: "## {{mundo}}の記録簿",
    queTanSerio: "深刻さ：{{severidad}}。",
    elCamino: "選んだ道：{{camino}}。",
    queProtege: "守るもの：{{protege}}。",
    tuRespuesta: "対応：{{respuesta}}",
  },
};

const zh: typeof es = {
  probabilidad: {
    poco_probable: "不太可能发生",
    probable: "有可能发生",
    muy_probable: "很可能发生",
  },
  dolor: {
    poco: "影响不大",
    bastante: "影响不小",
    mucho: "影响很大",
  },
  camino: {
    evitar: "避开它",
    mitigar: "降低它",
    transferir: "转给别人承担",
    aceptar: "清醒地接受它",
  },
  severidad: "{{probabilidad}}，{{dolor}}",
  protegidaDesaparecida: "它保护的那项活动已经不在你的计划里了",
  negocioEntero: "你的整个生意",
  registroVacio: "我没能把这个计划和你的活动关联起来：相关回答都在你的计划里，但这份登记册是空的。",
  documento: {
    titulo: "## {{mundo}}登记册",
    queTanSerio: "严重程度：{{severidad}}。",
    elCamino: "应对方式：{{camino}}。",
    queProtege: "保护对象：{{protege}}。",
    tuRespuesta: "你的应对：{{respuesta}}",
  },
};

const ko: typeof es = {
  probabilidad: {
    poco_probable: "발생 가능성 낮음",
    probable: "발생 가능성 있음",
    muy_probable: "발생 가능성 높음",
  },
  dolor: {
    poco: "타격 작음",
    bastante: "타격 꽤 큼",
    mucho: "타격 매우 큼",
  },
  camino: {
    evitar: "피하기",
    mitigar: "줄이기",
    transferir: "다른 곳에 넘기기",
    aceptar: "알고서 감수하기",
  },
  severidad: "{{probabilidad}}, {{dolor}}",
  protegidaDesaparecida: "보호하던 활동이 이제 계획에 없음",
  negocioEntero: "사업 전체",
  registroVacio: "이 계획을 활동과 연결하지 못했어요. 답변은 계획에 들어 있지만 이 등록부는 비어 있어요.",
  documento: {
    titulo: "## {{mundo}} 등록부",
    queTanSerio: "심각도: {{severidad}}.",
    elCamino: "대응 방법: {{camino}}.",
    queProtege: "보호 대상: {{protege}}.",
    tuRespuesta: "나의 답변: {{respuesta}}",
  },
};

const ar: typeof es = {
  probabilidad: {
    poco_probable: "قليل الاحتمال",
    probable: "محتمل",
    muy_probable: "محتمل جدًا",
  },
  dolor: {
    poco: "ضرره سيكون قليلًا",
    bastante: "ضرره سيكون كبيرًا",
    mucho: "ضرره سيكون بالغًا",
  },
  camino: {
    evitar: "تجنّبه",
    mitigar: "تقليله",
    transferir: "نقله إلى طرف آخر",
    aceptar: "قبوله عن وعي كامل",
  },
  severidad: "{{probabilidad}} و{{dolor}}",
  protegidaDesaparecida: "المهمة التي كانت تحميها لم تعد في خطتكم",
  negocioEntero: "عملكم بأكمله",
  registroVacio: "لم أتمكّن من ربط هذه الخطة بمهامكم: إجاباتها موجودة في خطتكم، لكن هذا السجل بقي فارغًا.",
  documento: {
    titulo: "## سجل {{mundo}}",
    queTanSerio: "مدى الخطورة: {{severidad}}.",
    elCamino: "الطريق المختار: {{camino}}.",
    queProtege: "ما الذي يحميه: {{protege}}.",
    tuRespuesta: "إجابتكم: {{respuesta}}",
  },
};

const hi: typeof es = {
  probabilidad: {
    poco_probable: "होने की संभावना कम",
    probable: "होने की संभावना",
    muy_probable: "होने की संभावना ज़्यादा",
  },
  dolor: {
    poco: "नुकसान थोड़ा",
    bastante: "नुकसान काफ़ी",
    mucho: "नुकसान बहुत",
  },
  camino: {
    evitar: "इससे बचना",
    mitigar: "इसे कम करना",
    transferir: "इसे किसी और को सौंपना",
    aceptar: "खुली आँखों से इसे स्वीकार करना",
  },
  severidad: "{{probabilidad}}, {{dolor}}",
  protegidaDesaparecida: "यह जिस गतिविधि की रक्षा करता था, वह अब आपकी योजना में नहीं है",
  negocioEntero: "आपका पूरा व्यवसाय",
  registroVacio: "इस योजना को आपकी गतिविधियों से जोड़ा नहीं जा सका: इसके जवाब आपकी योजना में हैं, पर यह रजिस्टर खाली रह गया।",
  documento: {
    titulo: "## {{mundo}} रजिस्टर",
    queTanSerio: "कितना गंभीर: {{severidad}}।",
    elCamino: "रास्ता: {{camino}}।",
    queProtege: "किसकी रक्षा करता है: {{protege}}।",
    tuRespuesta: "आपका जवाब: {{respuesta}}",
  },
};

export const REGISTRO_PROTECCION: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
