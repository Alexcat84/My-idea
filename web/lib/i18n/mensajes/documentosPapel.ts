/** Los documentos en papel (PDF) estructurados: el resumen "Cómo te fue" del
 * Expediente (app/ui/ResumenPapel.tsx) y la bitácora impresa
 * (app/ui/BitacoraPapel.tsx). */
import type { PorIdioma } from "../config";

const es = {
  resumen: {
    comoTeFue: "Cómo te fue",
    tuProgreso: "Tu progreso hasta aquí",
    diasDeCamino: "días de camino",
    accionesCumplidas: "acciones cumplidas",
    hitosAlcanzados: "hitos alcanzados",
    tuViajeCompleto: "Tu viaje completo",
    cierre: "Aquí acaba tu idea y nace tu proyecto",
    sigueEnMarcha:
      "Tu idea sigue en marcha. Cuando la des por realizada, aquí quedará tu cierre con tus propias palabras.",
    loQueMasTeMovio: "Lo que más te movió el camino",
    loQueQuedoPendiente: "Lo que quedó pendiente",
    /** los meses abreviados del mapa de hitos ("3 may") */
    meses: ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"],
    /** la fecha corta: "3 feb" (i18n F3: el orden lo pone cada idioma) */
    fechaCorta: "{{d}} {{mes}}",
  },
  bitacora: {
    rango:
      "Del {{desde}} al {{hasta}}, día por día, tal como quedó registrado. Si moviste una fecha, la original sigue aquí: nada se reescribe.",
    laSecuencia: "La secuencia de tu viaje",
    pie: "Esta es tu historia tal como quedó registrada, día por día. Puedes descargarla aparte cuando quieras.",
  },
  /** los rótulos del pie de página */
  pieExpediente: "Expediente",
  pieMiBitacora: "Mi bitácora",
};

const en: typeof es = {
  resumen: {
    comoTeFue: "How it went",
    tuProgreso: "Your progress so far",
    diasDeCamino: "days on the road",
    accionesCumplidas: "actions completed",
    hitosAlcanzados: "milestones reached",
    tuViajeCompleto: "Your whole journey",
    cierre: "This is where your idea ends and your project begins",
    sigueEnMarcha:
      "Your idea is still underway. When you call it achieved, your close will be here, in your own words.",
    loQueMasTeMovio: "What moved your journey forward the most",
    loQueQuedoPendiente: "What's still open",
    meses: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    fechaCorta: "{{mes}} {{d}}",
  },
  bitacora: {
    rango:
      "From {{desde}} to {{hasta}}, day by day, just as it was recorded. If you moved a date, the original is still here: nothing gets rewritten.",
    laSecuencia: "The sequence of your journey",
    pie: "This is your story just as it was recorded, day by day. You can download it separately whenever you like.",
  },
  pieExpediente: "Full Record",
  pieMiBitacora: "My Logbook",
};

const fr: typeof es = {
  resumen: {
    comoTeFue: "Comment ça s'est passé",
    tuProgreso: "Ta progression jusqu'ici",
    diasDeCamino: "jours de parcours",
    accionesCumplidas: "actions accomplies",
    hitosAlcanzados: "jalons atteints",
    tuViajeCompleto: "Ton parcours complet",
    cierre: "Ici s'achève ton idée et naît ton projet",
    sigueEnMarcha: "Ton idée est toujours en marche. Quand tu la considéreras comme réalisée, ta clôture sera ici, dans tes propres mots.",
    loQueMasTeMovio: "Ce qui t'a le plus fait avancer",
    loQueQuedoPendiente: "Ce qui est resté en suspens",
    meses: ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."],
    fechaCorta: "{{d}} {{mes}}",
  },
  bitacora: {
    rango: "Du {{desde}} au {{hasta}}, jour après jour, tel que tout a été consigné. Si tu as déplacé une date, l'originale est toujours ici : rien n'est réécrit.",
    laSecuencia: "Le déroulement de ton parcours",
    pie: "Voici ton histoire telle qu'elle a été consignée, jour après jour. Tu peux la télécharger à part quand tu veux.",
  },
  pieExpediente: "Dossier",
  pieMiBitacora: "Mon journal de bord",
};

const pt: typeof es = {
  resumen: {
    comoTeFue: "Como foi",
    tuProgreso: "Seu progresso até aqui",
    diasDeCamino: "dias de caminhada",
    accionesCumplidas: "ações concluídas",
    hitosAlcanzados: "marcos alcançados",
    tuViajeCompleto: "Sua jornada completa",
    cierre: "Aqui termina sua ideia e nasce seu projeto",
    sigueEnMarcha: "Sua ideia continua em andamento. Quando você a der por realizada, seu encerramento vai ficar aqui, com suas próprias palavras.",
    loQueMasTeMovio: "O que mais fez seu caminho avançar",
    loQueQuedoPendiente: "O que ficou pendente",
    meses: ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"],
    fechaCorta: "{{d}} de {{mes}}",
  },
  bitacora: {
    rango: "De {{desde}} a {{hasta}}, dia a dia, tal como ficou registrado. Se você mudou uma data, a original continua aqui: nada é reescrito.",
    laSecuencia: "A sequência da sua jornada",
    pie: "Esta é a sua história tal como ficou registrada, dia a dia. Você pode baixá-la separadamente quando quiser.",
  },
  pieExpediente: "Dossiê",
  pieMiBitacora: "Meu diário de bordo",
};

const de: typeof es = {
  resumen: {
    comoTeFue: "Wie es gelaufen ist",
    tuProgreso: "Dein Fortschritt bis hierher",
    diasDeCamino: "Tage unterwegs",
    accionesCumplidas: "erledigte Schritte",
    hitosAlcanzados: "erreichte Meilensteine",
    tuViajeCompleto: "Deine ganze Reise",
    cierre: "Hier endet deine Idee und beginnt dein Projekt",
    sigueEnMarcha: "Deine Idee läuft noch. Sobald du sie für verwirklicht erklärst, steht hier dein Abschluss in deinen eigenen Worten.",
    loQueMasTeMovio: "Was dich auf dem Weg am meisten vorangebracht hat",
    loQueQuedoPendiente: "Was noch offen ist",
    meses: ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"],
    fechaCorta: "{{d}}. {{mes}}",
  },
  bitacora: {
    rango: "Vom {{desde}} bis zum {{hasta}}, Tag für Tag, genau so, wie es festgehalten wurde. Wenn du einen Termin verschoben hast, steht der ursprüngliche noch hier: Nichts wird umgeschrieben.",
    laSecuencia: "Der Ablauf deiner Reise",
    pie: "Das ist deine Geschichte, genau so, wie sie Tag für Tag festgehalten wurde. Du kannst sie jederzeit separat herunterladen.",
  },
  pieExpediente: "Dossier",
  pieMiBitacora: "Mein Logbuch",
};

const it: typeof es = {
  resumen: {
    comoTeFue: "Com'è andata",
    tuProgreso: "I tuoi progressi fin qui",
    diasDeCamino: "giorni di cammino",
    accionesCumplidas: "azioni completate",
    hitosAlcanzados: "traguardi raggiunti",
    tuViajeCompleto: "Il tuo viaggio completo",
    cierre: "Qui finisce la tua idea e nasce il tuo progetto",
    sigueEnMarcha: "La tua idea è ancora in cammino. Quando la considererai realizzata, qui troverai la tua chiusura, con parole tue.",
    loQueMasTeMovio: "Quello che ti ha fatto avanzare di più",
    loQueQuedoPendiente: "Quello che è rimasto in sospeso",
    meses: ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"],
    fechaCorta: "{{d}} {{mes}}",
  },
  bitacora: {
    rango: "Dal {{desde}} al {{hasta}}, giorno per giorno, così come è stato registrato. Se hai spostato una data, quella originale è ancora qui: niente viene riscritto.",
    laSecuencia: "La sequenza del tuo viaggio",
    pie: "Questa è la tua storia così come è stata registrata, giorno per giorno. Puoi scaricarla a parte quando vuoi.",
  },
  pieExpediente: "Fascicolo",
  pieMiBitacora: "Il mio diario di bordo",
};

const ja: typeof es = {
  resumen: {
    comoTeFue: "ふり返り",
    tuProgreso: "ここまでの歩み",
    diasDeCamino: "道のりの日数",
    accionesCumplidas: "完了したアクション",
    hitosAlcanzados: "達成したマイルストーン",
    tuViajeCompleto: "旅の全体",
    cierre: "ここでアイデアは終わり、プロジェクトが生まれます",
    sigueEnMarcha: "アイデアはまだ進行中です。実現したと感じたら、ここに自分の言葉で書いた締めくくりが残ります。",
    loQueMasTeMovio: "道のりをいちばん前に進めたもの",
    loQueQuedoPendiente: "残っていること",
    meses: ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
    fechaCorta: "{{mes}}{{d}}日",
  },
  bitacora: {
    rango: "{{desde}}から{{hasta}}まで、記録されたとおりに1日ずつ。日付を移動していても、元の日付はここに残ります。書き換えられるものは何もありません。",
    laSecuencia: "旅の流れ",
    pie: "記録されたとおりの、1日ずつの歩みです。いつでも別にダウンロードできます。",
  },
  pieExpediente: "全記録",
  pieMiBitacora: "活動ログ",
};

const zh: typeof es = {
  resumen: {
    comoTeFue: "这一路的成果",
    tuProgreso: "你目前的进展",
    diasDeCamino: "天的旅程",
    accionesCumplidas: "项行动已完成",
    hitosAlcanzados: "个里程碑已达成",
    tuViajeCompleto: "你的完整旅程",
    cierre: "你的想法在这里圆满，你的项目从这里启程",
    sigueEnMarcha: "你的想法仍在推进中。等你认定它已实现，这里会用你自己的话记下你的收尾。",
    loQueMasTeMovio: "最推动你前进的事",
    loQueQuedoPendiente: "尚未完成的部分",
    meses: ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
    fechaCorta: "{{mes}}{{d}}日",
  },
  bitacora: {
    rango: "从{{desde}}到{{hasta}}，逐日记录，原样保留。即使你改过日期，原来的日期也仍在这里：什么都不会被改写。",
    laSecuencia: "你的旅程时间线",
    pie: "这是你的故事，按记录原样逐日呈现。你随时可以单独下载它。",
  },
  pieExpediente: "完整档案",
  pieMiBitacora: "我的日志",
};

const ko: typeof es = {
  resumen: {
    comoTeFue: "나의 여정 돌아보기",
    tuProgreso: "지금까지의 진행 상황",
    diasDeCamino: "여정 일수",
    accionesCumplidas: "완료한 실행 항목",
    hitosAlcanzados: "도달한 이정표",
    tuViajeCompleto: "나의 여정 전체",
    cierre: "여기서 아이디어가 끝나고 프로젝트가 태어나요",
    sigueEnMarcha: "아이디어는 아직 진행 중이에요. 실현으로 마무리하면, 직접 쓴 마무리 글이 여기에 남아요.",
    loQueMasTeMovio: "여정을 가장 크게 움직인 것",
    loQueQuedoPendiente: "아직 남아 있는 것",
    meses: ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"],
    fechaCorta: "{{mes}} {{d}}일",
  },
  bitacora: {
    rango: "{{desde}}부터 {{hasta}}까지, 기록된 그대로 하루하루 담았어요. 날짜를 옮겼다면 원래 날짜도 여기 남아 있어요. 다시 쓰이는 건 없어요.",
    laSecuencia: "나의 여정이 흘러온 순서",
    pie: "기록된 그대로, 하루하루 쌓인 나의 이야기예요. 언제든 따로 다운로드할 수 있어요.",
  },
  pieExpediente: "전체 자료",
  pieMiBitacora: "나의 기록장",
};

const ar: typeof es = {
  resumen: {
    comoTeFue: "كيف سارت الأمور",
    tuProgreso: "تقدّمكم حتى الآن",
    diasDeCamino: "أيام الرحلة",
    accionesCumplidas: "إجراءات منجزة",
    hitosAlcanzados: "محطات بلغتموها",
    tuViajeCompleto: "رحلتكم كاملة",
    cierre: "هنا تنتهي فكرتكم ويولد مشروعكم",
    sigueEnMarcha: "فكرتكم ما زالت ماضية. حين تعدّونها متحقّقة، سيبقى هنا ختامكم بكلماتكم أنتم.",
    loQueMasTeMovio: "أكثر ما دفع مسيرتكم إلى الأمام",
    loQueQuedoPendiente: "ما بقي معلّقًا",
    meses: [
      "يناير",
      "فبراير",
      "مارس",
      "أبريل",
      "مايو",
      "يونيو",
      "يوليو",
      "أغسطس",
      "سبتمبر",
      "أكتوبر",
      "نوفمبر",
      "ديسمبر",
    ],
    fechaCorta: "{{d}} {{mes}}",
  },
  bitacora: {
    rango: "من {{desde}} إلى {{hasta}}، يومًا بيوم، كما سُجّل تمامًا. إن نقلتم موعدًا، فالموعد الأصلي باقٍ هنا: لا شيء يُعاد كتابته.",
    laSecuencia: "تسلسل رحلتكم",
    pie: "هذه قصتكم كما سُجّلت، يومًا بيوم. يمكنكم تنزيلها منفصلة متى شئتم.",
  },
  pieExpediente: "الملف الكامل",
  pieMiBitacora: "سجلّ رحلتي",
};

const hi: typeof es = {
  resumen: {
    comoTeFue: "आपका सफ़र कैसा रहा",
    tuProgreso: "अब तक की आपकी प्रगति",
    diasDeCamino: "दिन का सफ़र",
    accionesCumplidas: "पूरे हुए कदम",
    hitosAlcanzados: "पार किए गए पड़ाव",
    tuViajeCompleto: "आपकी पूरी यात्रा",
    cierre: "यहाँ आपका विचार पूरा होता है और आपकी परियोजना जन्म लेती है",
    sigueEnMarcha: "आपका विचार अभी आगे बढ़ रहा है। जब आप इसे साकार मान लें, तब आपका समापन आपके अपने शब्दों में यहाँ रहेगा।",
    loQueMasTeMovio: "आपके सफ़र को सबसे ज़्यादा किसने आगे बढ़ाया",
    loQueQuedoPendiente: "जो बाकी रह गया",
    meses: ["जन॰", "फ़र॰", "मार्च", "अप्रैल", "मई", "जून", "जुल॰", "अग॰", "सित॰", "अक्टू॰", "नव॰", "दिस॰"],
    fechaCorta: "{{d}} {{mes}}",
  },
  bitacora: {
    rango: "{{desde}} से {{hasta}} तक, दिन-ब-दिन, ठीक वैसे ही जैसे दर्ज हुआ। अगर आपने कोई तारीख बदली, तो मूल तारीख भी यहीं है: कुछ भी दोबारा नहीं लिखा जाता।",
    laSecuencia: "आपकी यात्रा का क्रम",
    pie: "यह आपकी कहानी है, ठीक वैसे ही जैसे दिन-ब-दिन दर्ज हुई। इसे जब चाहें अलग से डाउनलोड करें।",
  },
  pieExpediente: "पूरा ब्यौरा",
  pieMiBitacora: "मेरी लॉगबुक",
};

export const DOCUMENTOS_PAPEL: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
