/** El motor TypeScript (lib/engine/): los textos que llegan a la persona tal cual,
 * sin pasar por la IA. Constantes del motor (constants.ts), la pregunta genérica
 * de un nodo sin pregunta curada (graph.ts), los temas de respaldo de la oferta
 * del plan (recorrido.ts), el rango de una banda de esfuerzo (estimacion.ts), la
 * tarea de respaldo del bloque "Esta semana" (checklist.ts) y el error del
 * snapshot de un mundo de protección (snapshotProyecto.ts). */
import type { PorIdioma } from "../config";

const es = {
  /** Lo que el plan aún no cubre (constants.ts TEXTO_FAMILIA_FALTANTE). */
  familiaFaltante: {
    accion_clientes:
      "validar con clientes reales (conversaciones, una primera versión sencilla de tu producto, pruebas con usuarios, una venta o preventa real)",
    viabilidad_economica: "si tu idea puede sostenerse económicamente (costos, precios, punto de equilibrio)",
    profundidad: "más profundidad en el recorrido",
  },
  /** La nota al pie del reporte de sostenibilidad (constants.ts REPORTE_DISCLAIMER). */
  /** i18n F5: la unidad con que se guarda cada número declarado en el reporte
   * (reporte.ts unidadDeclaradaCampo), en el idioma de la idea. */
  unidadCampo: {
    porMes: "por mes",
    porHora: "por hora",
    porUnidad: "por {{u}}",
    alMes: "{{u}}/mes",
    unidad: "unidad",
  },
  reporteDisclaimer:
    "\n\n---\n_Estimaciones basadas en las cifras que tú diste; no sustituyen contabilidad formal ni asesoría fiscal, que varían según tu país._",
  /** La primera pregunta del reporte (constants.ts PREGUNTA_TIPO_OFERTA). */
  preguntaTipoOferta: "¿Qué vendes exactamente y cómo se cobra?",
  /** graph.ts obtenerPregunta: la pregunta de un nodo sin pregunta en el caché. */
  preguntaGenerica:
    'Pensando en "{{titulo}}", cuéntame en tus palabras dónde estás parado ahora mismo con tu idea y qué es lo que más te preocupa o te entusiasma.',
  /** recorrido.ts: el nombre humano de una familia cuando la brújula no responde. */
  temaFamilia: {
    accionClientes: "Salir a validar con clientes",
    viabilidadEconomica: "Tus números de verdad",
  },
  /** estimacion.ts rangoDeBanda: el rango en palabras de cada banda de esfuerzo. */
  rangoBanda: {
    S: "~1 h",
    M: "~2-4 h",
    L: "una jornada",
    XL: "varios días",
  },
  /** checklist.ts: la tarea cuando el bloque "Esta semana" viene sin texto. */
  checklistEstaSemana: "Esta semana",
  /** snapshotProyecto.ts ERROR_SNAPSHOT_ILEGIBLE. */
  errorSnapshotIlegible: "no pudimos leer las actividades de tu plan; intenta de nuevo en un momento",
};

const en: typeof es = {
  familiaFaltante: {
    accion_clientes:
      "validating with real customers (conversations, a simple first version of your product, user testing, a real sale or pre-sale)",
    viabilidad_economica: "whether your idea can sustain itself financially (costs, prices, break-even point)",
    profundidad: "more depth in the path you explored",
  },
  unidadCampo: {
    porMes: "per month",
    porHora: "per hour",
    porUnidad: "per {{u}}",
    alMes: "{{u}}/month",
    unidad: "unit",
  },
  reporteDisclaimer:
    "\n\n---\n_Estimates based on the figures you provided; they don't replace formal accounting or tax advice, which vary by country._",
  preguntaTipoOferta: "What exactly do you sell, and how do you charge for it?",
  preguntaGenerica:
    'Thinking about "{{titulo}}", tell me in your own words where you stand with your idea right now and what worries or excites you most.',
  temaFamilia: {
    accionClientes: "Go validate with customers",
    viabilidadEconomica: "Your real numbers",
  },
  rangoBanda: {
    S: "~1 h",
    M: "~2-4 h",
    L: "a full day",
    XL: "several days",
  },
  checklistEstaSemana: "This week",
  errorSnapshotIlegible: "we couldn't read your plan's activities; try again in a moment",
};

const fr: typeof es = {
  familiaFaltante: {
    accion_clientes: "valider auprès de vrais clients (conversations, une première version simple de ton produit, des essais avec des utilisateurs, une vraie vente ou prévente)",
    viabilidad_economica: "si ton idée peut tenir financièrement (coûts, prix, seuil de rentabilité)",
    profundidad: "plus de profondeur dans le cheminement",
  },
  unidadCampo: {
    porMes: "par mois",
    porHora: "par heure",
    porUnidad: "par {{u}}",
    alMes: "{{u}}/mois",
    unidad: "unité",
  },
  reporteDisclaimer: "\n\n---\n_Estimations basées sur les chiffres que tu as donnés; elles ne remplacent pas une comptabilité en bonne et due forme ni des conseils fiscaux, qui varient selon ton pays._",
  preguntaTipoOferta: "Qu'est-ce que tu vends exactement, et comment te fais-tu payer?",
  preguntaGenerica: "En pensant à « {{titulo}} », raconte-moi dans tes mots où tu en es avec ton idée en ce moment, et ce qui t'inquiète ou t'enthousiasme le plus.",
  temaFamilia: {
    accionClientes: "Aller valider auprès de clients",
    viabilidadEconomica: "Tes vrais chiffres",
  },
  rangoBanda: {
    S: "~1 h",
    M: "~2-4 h",
    L: "une journée",
    XL: "plusieurs jours",
  },
  checklistEstaSemana: "Cette semaine",
  errorSnapshotIlegible: "nous n'avons pas pu lire les activités de ton plan; réessaie dans un instant",
};

const pt: typeof es = {
  familiaFaltante: {
    accion_clientes: "validar com clientes reais (conversas, uma primeira versão simples do seu produto, testes com usuários, uma venda ou pré-venda real)",
    viabilidad_economica: "se sua ideia consegue se sustentar financeiramente (custos, preços, ponto de equilíbrio)",
    profundidad: "mais profundidade no percurso",
  },
  unidadCampo: {
    porMes: "por mês",
    porHora: "por hora",
    porUnidad: "por {{u}}",
    alMes: "{{u}}/mês",
    unidad: "unidade",
  },
  reporteDisclaimer: "\n\n---\n_Estimativas baseadas nos valores que você informou; não substituem contabilidade formal nem assessoria tributária, que variam conforme o seu país._",
  preguntaTipoOferta: "O que exatamente você vende e como cobra por isso?",
  preguntaGenerica: "Pensando em \"{{titulo}}\", me conte com suas palavras em que ponto você está agora com sua ideia e o que mais preocupa ou empolga você.",
  temaFamilia: {
    accionClientes: "Sair para validar com clientes",
    viabilidadEconomica: "Seus números de verdade",
  },
  rangoBanda: {
    S: "~1 h",
    M: "~2-4 h",
    L: "um dia de trabalho",
    XL: "vários dias",
  },
  checklistEstaSemana: "Esta semana",
  errorSnapshotIlegible: "não conseguimos ler as atividades do seu plano; tente de novo daqui a pouco",
};

const de: typeof es = {
  familiaFaltante: {
    accion_clientes: "mit echten Kunden prüfen (Gespräche, eine einfache erste Version deines Produkts, Tests mit Nutzern, ein echter Verkauf oder Vorverkauf)",
    viabilidad_economica: "ob sich deine Idee wirtschaftlich tragen kann (Kosten, Preise, Gewinnschwelle)",
    profundidad: "mehr Tiefe auf dem Weg, den du erkundet hast",
  },
  unidadCampo: {
    porMes: "pro Monat",
    porHora: "pro Stunde",
    porUnidad: "pro {{u}}",
    alMes: "{{u}}/Monat",
    unidad: "Einheit",
  },
  reporteDisclaimer: "\n\n---\n_Schätzungen auf Grundlage der Zahlen, die du angegeben hast; sie ersetzen keine ordentliche Buchhaltung und keine Steuerberatung, die je nach Land verschieden sind._",
  preguntaTipoOferta: "Was genau verkaufst du, und wie rechnest du ab?",
  preguntaGenerica: "Mit Blick auf „{{titulo}}“: Erzähl mir in deinen eigenen Worten, wo du gerade mit deiner Idee stehst und was dich am meisten beschäftigt oder begeistert.",
  temaFamilia: {
    accionClientes: "Raus zu echten Kunden",
    viabilidadEconomica: "Deine echten Zahlen",
  },
  rangoBanda: {
    S: "~1 Std.",
    M: "~2-4 Std.",
    L: "ein ganzer Tag",
    XL: "mehrere Tage",
  },
  checklistEstaSemana: "Diese Woche",
  errorSnapshotIlegible: "wir konnten die Aufgaben deines Plans nicht lesen; versuch es gleich noch einmal",
};

const it: typeof es = {
  familiaFaltante: {
    accion_clientes: "verificare l'idea con clienti reali (conversazioni, una prima versione semplice del tuo prodotto, prove con utenti, una vendita o prevendita reale)",
    viabilidad_economica: "se la tua idea sta in piedi economicamente (costi, prezzi, punto di pareggio)",
    profundidad: "più profondità nel percorso",
  },
  unidadCampo: {
    porMes: "al mese",
    porHora: "all'ora",
    porUnidad: "per {{u}}",
    alMes: "{{u}}/mese",
    unidad: "unità",
  },
  reporteDisclaimer: "\n\n---\n_Stime basate sulle cifre che hai fornito tu; non sostituiscono una contabilità formale né una consulenza fiscale, che variano a seconda del tuo paese._",
  preguntaTipoOferta: "Cosa vendi esattamente e come ti fai pagare?",
  preguntaGenerica: "Pensando a \"{{titulo}}\", raccontami con parole tue a che punto sei adesso con la tua idea e cosa ti preoccupa o ti entusiasma di più.",
  temaFamilia: {
    accionClientes: "Andare a verificare con i clienti",
    viabilidadEconomica: "I tuoi numeri, quelli veri",
  },
  rangoBanda: {
    S: "~1 h",
    M: "~2-4 h",
    L: "una giornata",
    XL: "diversi giorni",
  },
  checklistEstaSemana: "Questa settimana",
  errorSnapshotIlegible: "non siamo riusciti a leggere le attività del tuo piano; riprova tra un momento",
};

const ja: typeof es = {
  familiaFaltante: {
    accion_clientes: "実際のお客様との検証（会話、製品のシンプルな最初のバージョン、ユーザーテスト、実際の販売や予約販売）",
    viabilidad_economica: "アイデアが経済的に成り立つかどうか（コスト、価格、損益分岐点）",
    profundidad: "これまでの道のりを、さらに深めること",
  },
  unidadCampo: {
    porMes: "月あたり",
    porHora: "1時間あたり",
    porUnidad: "{{u}}あたり",
    alMes: "{{u}}/月",
    unidad: "単位",
  },
  reporteDisclaimer: "\n\n---\n_これは入力した数字にもとづく見積もりです。正式な会計や税務の助言に代わるものではありません。会計や税務は国によって異なります。_",
  preguntaTipoOferta: "具体的に何を売っていて、どうやって代金を受け取りますか？",
  preguntaGenerica: "「{{titulo}}」について、今アイデアはどんな段階にありますか？いちばん不安なこと、またはいちばんワクワクしていることは何ですか？自分の言葉で聞かせてください。",
  temaFamilia: {
    accionClientes: "お客様と検証しに行く",
    viabilidadEconomica: "本当の数字",
  },
  rangoBanda: {
    S: "約1時間",
    M: "約2〜4時間",
    L: "丸1日",
    XL: "数日",
  },
  checklistEstaSemana: "今週",
  errorSnapshotIlegible: "プランのアクションを読み込めませんでした。少し待ってからもう一度お試しください",
};

const zh: typeof es = {
  familiaFaltante: {
    accion_clientes: "用真实客户来验证（和他们交谈、做一个简单的产品初版、用户测试、一次真实的销售或预售）",
    viabilidad_economica: "你的想法在经济上能否持续（成本、价格、盈亏平衡点）",
    profundidad: "在探索路径上再深入一些",
  },
  unidadCampo: {
    porMes: "每月",
    porHora: "每小时",
    porUnidad: "每{{u}}",
    alMes: "{{u}}/月",
    unidad: "单位",
  },
  reporteDisclaimer: "\n\n---\n_以上估算基于你提供的数字；不能替代正式的会计或税务咨询，这些因国家而异。_",
  preguntaTipoOferta: "你具体卖的是什么？怎么收费？",
  preguntaGenerica: "想想“{{titulo}}”，用你自己的话告诉我：你的想法现在进展到哪一步了，最让你担心或兴奋的是什么？",
  temaFamilia: {
    accionClientes: "去找客户验证",
    viabilidadEconomica: "你真实的数字",
  },
  rangoBanda: {
    S: "约1小时",
    M: "约2-4小时",
    L: "一整天",
    XL: "好几天",
  },
  checklistEstaSemana: "本周",
  errorSnapshotIlegible: "我们没能读取你计划中的活动，请稍后再试",
};

const ko: typeof es = {
  familiaFaltante: {
    accion_clientes: "실제 고객과의 검증(대화, 간단한 첫 버전의 제품, 사용자 테스트, 실제 판매나 사전 판매)",
    viabilidad_economica: "아이디어가 경제적으로 버틸 수 있는지(비용, 가격, 손익분기점)",
    profundidad: "탐색 경로를 더 깊이 파고들기",
  },
  unidadCampo: {
    porMes: "월당",
    porHora: "시간당",
    porUnidad: "{{u}}당",
    alMes: "{{u}}/월",
    unidad: "단위",
  },
  reporteDisclaimer: "\n\n---\n_입력한 수치를 바탕으로 한 추정이에요. 정식 회계나 세무 상담을 대신하지 않으며, 이런 부분은 나라마다 달라요._",
  preguntaTipoOferta: "정확히 무엇을 팔고, 돈은 어떻게 받나요?",
  preguntaGenerica: "“{{titulo}}”에 대해 생각해 보면서, 지금 아이디어가 어디쯤 와 있는지, 그리고 무엇이 가장 걱정되거나 설레는지 편하게 이야기해 주세요.",
  temaFamilia: {
    accionClientes: "고객과 검증하러 나가기",
    viabilidadEconomica: "나의 진짜 숫자",
  },
  rangoBanda: {
    S: "~1시간",
    M: "~2-4시간",
    L: "하루 종일",
    XL: "며칠",
  },
  checklistEstaSemana: "이번 주",
  errorSnapshotIlegible: "계획의 활동을 읽지 못했어요. 잠시 후 다시 시도해 주세요",
};

const ar: typeof es = {
  familiaFaltante: {
    accion_clientes: "التحقّق مع عملاء حقيقيين (محادثات، ونسخة أولى بسيطة من منتجكم، وتجارب مع المستخدمين، وبيع أو بيع مسبق حقيقي)",
    viabilidad_economica: "هل تستطيع فكرتكم أن تصمد ماليًا (التكاليف، والأسعار، ونقطة التعادل)",
    profundidad: "مزيد من العمق في المسار",
  },
  unidadCampo: {
    porMes: "شهريًا",
    porHora: "في الساعة",
    porUnidad: "لكل {{u}}",
    alMes: "{{u}}/شهر",
    unidad: "وحدة",
  },
  reporteDisclaimer: "\n\n---\n_تقديرات مبنية على الأرقام التي قدّمتموها؛ ولا تغني عن المحاسبة الرسمية ولا عن الاستشارة الضريبية، إذ تختلفان من بلد إلى آخر._",
  preguntaTipoOferta: "ماذا تبيعون بالضبط، وكيف تتقاضون مقابله؟",
  preguntaGenerica: "بالتفكير في «{{titulo}}»، احكوا لي بكلماتكم أين تقفون الآن مع فكرتكم، وما أكثر ما يقلقكم أو يحمّسكم.",
  temaFamilia: {
    accionClientes: "الخروج للتحقّق مع العملاء",
    viabilidadEconomica: "أرقامكم الحقيقية",
  },
  rangoBanda: {
    S: "~1 س",
    M: "~2-4 س",
    L: "يوم عمل كامل",
    XL: "عدة أيام",
  },
  checklistEstaSemana: "هذا الأسبوع",
  errorSnapshotIlegible: "لم نتمكّن من قراءة مهام خطتكم؛ حاولوا مجددًا بعد لحظات",
};

const hi: typeof es = {
  familiaFaltante: {
    accion_clientes: "असली ग्राहकों के साथ परखना (बातचीत, आपके प्रोडक्ट का एक सरल पहला संस्करण, लोगों के साथ परीक्षण, एक असली बिक्री या एडवांस बुकिंग)",
    viabilidad_economica: "क्या आपका विचार आर्थिक रूप से टिक सकता है (लागत, कीमतें, ब्रेक-ईवन बिंदु)",
    profundidad: "रास्ते में और गहराई",
  },
  unidadCampo: {
    porMes: "प्रति माह",
    porHora: "प्रति घंटा",
    porUnidad: "प्रति {{u}}",
    alMes: "{{u}}/माह",
    unidad: "इकाई",
  },
  reporteDisclaimer: "\n\n---\n_ये अनुमान आपकी दी गई संख्याओं पर आधारित हैं; ये औपचारिक अकाउंटिंग या टैक्स सलाह की जगह नहीं लेते, जो हर देश में अलग होती है।_",
  preguntaTipoOferta: "आप ठीक-ठीक क्या बेचते हैं, और उसका पैसा कैसे लेते हैं?",
  preguntaGenerica: "“{{titulo}}” के बारे में सोचते हुए, अपने शब्दों में बताइए कि अभी आप अपने विचार के साथ कहाँ हैं, और किस बात की आपको सबसे ज़्यादा चिंता है या किस बात का सबसे ज़्यादा उत्साह।",
  temaFamilia: {
    accionClientes: "ग्राहकों के बीच जाकर परखें",
    viabilidadEconomica: "आपके असली आंकड़े",
  },
  rangoBanda: {
    S: "~1 घंटा",
    M: "~2-4 घंटे",
    L: "पूरा एक दिन",
    XL: "कई दिन",
  },
  checklistEstaSemana: "इस हफ़्ते",
  errorSnapshotIlegible: "हम आपकी योजना की गतिविधियाँ नहीं पढ़ सके; थोड़ी देर में फिर से कोशिश करें",
};

export const MOTOR: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
