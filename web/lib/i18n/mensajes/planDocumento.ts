/** El plan como documento de acordeones (app/ui/PlanDocumento.tsx) y la
 * etiqueta que agrega su parser (lib/planParser.ts). Los encabezados del
 * markdown que el parser RECONOCE ("Etapa", "Esta semana", "Entregable",
 * "Pasos"...) no viven aquí: son claves de lectura, no texto de pantalla. */
import type { PorIdioma } from "../config";

const es = {
  estaSemana: "Esta semana",
  empezarConEsto: "Empezar con esto",
  pasos: "Pasos",
  entregable: "Entregable",
  generadoDeTuRecorrido: "Generado de tu recorrido",
  etapas: { one: "{{n}} etapa", other: "{{n}} etapas" },
  metaEtapas: "{{etapas}} · cada barra muestra su entregable; despliégala para los pasos y la acción",
  tuPrimeraAccion: "Tu primera acción",
  miBitacora: "Mi bitácora",
  historiaDeTuViaje: "La historia de tu viaje, paso a paso.",
  verMiBitacora: "Ver mi bitácora",
  construidoConTuRecorrido: "Construido con tu recorrido",
  notaRecalculo:
    "¿Cambia algo en el mundo real? Vuelve a la entrevista cuando quieras: el plan se recalcula desde donde estés.",
  /** planParser: el bloque que rescata las cifras en negrita de la sección de números */
  losNumerosQueNecesitas: "Los números que necesitas",
};

const en: typeof es = {
  estaSemana: "This week",
  empezarConEsto: "Start with this",
  pasos: "Steps",
  entregable: "Deliverable",
  generadoDeTuRecorrido: "Generated from your path",
  etapas: { one: "{{n}} stage", other: "{{n}} stages" },
  metaEtapas: "{{etapas}} · each bar shows its deliverable; expand it for the steps and the action",
  tuPrimeraAccion: "Your first action",
  miBitacora: "My Logbook",
  historiaDeTuViaje: "The story of your journey, step by step.",
  verMiBitacora: "See my Logbook",
  construidoConTuRecorrido: "Built from your path",
  notaRecalculo:
    "Something changed in the real world? Go back to the interview whenever you like: the plan recalculates from wherever you are.",
  losNumerosQueNecesitas: "The numbers you need",
};

const fr: typeof es = {
  estaSemana: "Cette semaine",
  empezarConEsto: "Commencer par ceci",
  pasos: "Marche à suivre",
  entregable: "Livrable",
  generadoDeTuRecorrido: "Généré à partir de ton cheminement",
  etapas: {
    one: "{{n}} étape",
    other: "{{n}} étapes",
  },
  metaEtapas: "{{etapas}} · chaque barre montre son livrable; déploie-la pour voir la marche à suivre et l'action",
  tuPrimeraAccion: "Ta première action",
  miBitacora: "Mon journal de bord",
  historiaDeTuViaje: "L'histoire de ton parcours, pas à pas.",
  verMiBitacora: "Voir mon journal de bord",
  construidoConTuRecorrido: "Construit avec ton cheminement",
  notaRecalculo: "Quelque chose change dans la vraie vie? Reviens à l'entretien quand tu veux : le plan se recalcule à partir de là où tu en es.",
  losNumerosQueNecesitas: "Les chiffres dont tu as besoin",
};

const pt: typeof es = {
  estaSemana: "Esta semana",
  empezarConEsto: "Começar por isto",
  pasos: "Passos",
  entregable: "Entrega",
  generadoDeTuRecorrido: "Gerado a partir do seu percurso",
  etapas: {
    one: "{{n}} etapa",
    other: "{{n}} etapas",
  },
  metaEtapas: "{{etapas}} · cada barra mostra sua entrega; abra-a para ver os passos e a ação",
  tuPrimeraAccion: "Sua primeira ação",
  miBitacora: "Meu diário de bordo",
  historiaDeTuViaje: "A história da sua jornada, passo a passo.",
  verMiBitacora: "Ver meu diário de bordo",
  construidoConTuRecorrido: "Construído com o seu percurso",
  notaRecalculo: "Algo mudou no mundo real? Volte à entrevista quando quiser: o plano é recalculado a partir de onde você estiver.",
  losNumerosQueNecesitas: "Os números de que você precisa",
};

const de: typeof es = {
  estaSemana: "Diese Woche",
  empezarConEsto: "Damit anfangen",
  pasos: "Vorgehen",
  entregable: "Ergebnis",
  generadoDeTuRecorrido: "Aus deinem Weg erstellt",
  etapas: {
    one: "{{n}} Etappe",
    other: "{{n}} Etappen",
  },
  metaEtapas: "{{etapas}} · jeder Balken zeigt sein Ergebnis; klapp ihn auf für das Vorgehen und den Schritt dieser Woche",
  tuPrimeraAccion: "Dein erster Schritt",
  miBitacora: "Mein Logbuch",
  historiaDeTuViaje: "Die Geschichte deiner Reise, Schritt für Schritt.",
  verMiBitacora: "Mein Logbuch ansehen",
  construidoConTuRecorrido: "Auf deinem Weg aufgebaut",
  notaRecalculo: "Ändert sich etwas in der echten Welt? Geh zurück ins Gespräch, wann immer du willst: Der Plan wird von dort aus neu berechnet, wo du gerade stehst.",
  losNumerosQueNecesitas: "Die Zahlen, die du brauchst",
};

const it: typeof es = {
  estaSemana: "Questa settimana",
  empezarConEsto: "Comincia da qui",
  pasos: "Passi",
  entregable: "Risultato atteso",
  generadoDeTuRecorrido: "Generato dal tuo percorso",
  etapas: {
    one: "{{n}} tappa",
    other: "{{n}} tappe",
  },
  metaEtapas: "{{etapas}} · ogni barra mostra il suo risultato atteso; aprila per vedere i passi e l'azione",
  tuPrimeraAccion: "La tua prima azione",
  miBitacora: "Il mio diario di bordo",
  historiaDeTuViaje: "La storia del tuo viaggio, passo dopo passo.",
  verMiBitacora: "Vedi il mio diario di bordo",
  construidoConTuRecorrido: "Costruito con il tuo percorso",
  notaRecalculo: "Qualcosa è cambiato nel mondo reale? Torna all'intervista quando vuoi: il piano si ricalcola da dove ti trovi.",
  losNumerosQueNecesitas: "I numeri che ti servono",
};

const ja: typeof es = {
  estaSemana: "今週",
  empezarConEsto: "まずはこれから",
  pasos: "ステップ",
  entregable: "成果物",
  generadoDeTuRecorrido: "これまでの道のりから作成",
  etapas: {
    one: "{{n}}ステージ",
    other: "{{n}}ステージ",
  },
  metaEtapas: "{{etapas}} · 各バーに成果物を表示しています。開くとステップとアクションが見られます",
  tuPrimeraAccion: "最初のアクション",
  miBitacora: "活動ログ",
  historiaDeTuViaje: "あなたの旅の歩みを、一歩ずつ。",
  verMiBitacora: "活動ログを見る",
  construidoConTuRecorrido: "これまでの道のりをもとに作成",
  notaRecalculo: "現実に何か変化がありましたか？いつでもインタビューに戻れます。プランは今いる地点から再計算されます。",
  losNumerosQueNecesitas: "必要な数字",
};

const zh: typeof es = {
  estaSemana: "本周",
  empezarConEsto: "从这里开始",
  pasos: "步骤",
  entregable: "交付成果",
  generadoDeTuRecorrido: "根据你的探索路径生成",
  etapas: {
    one: "{{n}}个阶段",
    other: "{{n}}个阶段",
  },
  metaEtapas: "{{etapas}} · 每一栏显示它的交付成果；展开可查看步骤和行动",
  tuPrimeraAccion: "你的第一项行动",
  miBitacora: "我的日志",
  historiaDeTuViaje: "你的旅程一步步走来的故事。",
  verMiBitacora: "查看我的日志",
  construidoConTuRecorrido: "基于你的探索路径构建",
  notaRecalculo: "现实中有了变化？随时回到访谈：计划会从你现在的位置重新计算。",
  losNumerosQueNecesitas: "你需要的数字",
};

const ko: typeof es = {
  estaSemana: "이번 주",
  empezarConEsto: "이것부터 시작하기",
  pasos: "진행 순서",
  entregable: "결과물",
  generadoDeTuRecorrido: "탐색 경로로 만들었어요",
  etapas: {
    one: "{{n}}개 단계",
    other: "{{n}}개 단계",
  },
  metaEtapas: "{{etapas}} · 막대마다 결과물이 표시돼요. 펼치면 진행 순서와 실행 항목을 볼 수 있어요",
  tuPrimeraAccion: "첫 실행 항목",
  miBitacora: "나의 기록장",
  historiaDeTuViaje: "여정의 이야기를 한 걸음씩.",
  verMiBitacora: "기록장 보기",
  construidoConTuRecorrido: "탐색 경로로 만들었어요",
  notaRecalculo: "현실에서 뭔가 달라졌나요? 언제든 인터뷰로 돌아오세요. 지금 있는 곳에서부터 계획을 다시 계산해요.",
  losNumerosQueNecesitas: "필요한 숫자",
};

const ar: typeof es = {
  estaSemana: "هذا الأسبوع",
  empezarConEsto: "ابدؤوا بهذا",
  pasos: "الخطوات",
  entregable: "المُخرَج",
  generadoDeTuRecorrido: "مُعدّة من مساركم",
  etapas: {
    one: "المراحل: {{n}}",
    other: "المراحل: {{n}}",
  },
  metaEtapas: "{{etapas}} · يعرض كل شريط مُخرَجه؛ افتحوه لرؤية الخطوات والإجراء",
  tuPrimeraAccion: "إجراؤكم الأول",
  miBitacora: "سجلّ رحلتي",
  historiaDeTuViaje: "قصة رحلتكم، خطوة بخطوة.",
  verMiBitacora: "عرض سجلّ رحلتي",
  construidoConTuRecorrido: "مبنيّة على مساركم",
  notaRecalculo: "هل تغيّر شيء في العالم الحقيقي؟ عودوا إلى المقابلة متى شئتم: يُعاد حساب الخطة من حيث وصلتم.",
  losNumerosQueNecesitas: "الأرقام التي تحتاجونها",
};

const hi: typeof es = {
  estaSemana: "इस हफ़्ते",
  empezarConEsto: "इससे शुरू करें",
  pasos: "कैसे करें",
  entregable: "नतीजा",
  generadoDeTuRecorrido: "आपके रास्ते से तैयार",
  etapas: {
    one: "{{n}} चरण",
    other: "{{n}} चरण",
  },
  metaEtapas: "{{etapas}} · हर पट्टी उसका नतीजा दिखाती है; कैसे करें और इस हफ़्ते का कदम देखने के लिए उसे खोलें",
  tuPrimeraAccion: "आपका पहला कदम",
  miBitacora: "मेरी लॉगबुक",
  historiaDeTuViaje: "आपकी यात्रा की कहानी, कदम दर कदम।",
  verMiBitacora: "मेरी लॉगबुक देखें",
  construidoConTuRecorrido: "आपके रास्ते से बना",
  notaRecalculo: "असल दुनिया में कुछ बदला? जब चाहें बातचीत पर लौटें: योजना वहीं से फिर से बनती है जहाँ आप हैं।",
  losNumerosQueNecesitas: "जिन आंकड़ों की आपको ज़रूरत है",
};

export const PLAN_DOCUMENTO: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
