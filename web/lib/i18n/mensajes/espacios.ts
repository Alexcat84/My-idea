/** Campaña "Espacios": la muralla del sin plan (lib/espacios.ts), las pestañas
 * de los espacios (CambiadorEspacios) y el selector de caras (SelectorCara). */
import type { PorIdioma } from "../config";

const es = {
  /** UNA sola frase para toda la casa: la ruta (409) y la pantalla del escaparate. */
  murallaSinPlan: "Primero genera el plan de tu idea: tu mundo de {{mundo}} se construirá sobre él.",
  cambiador: {
    aria: "Los espacios de tu proyecto",
    tuViaje: "Tu viaje",
    anadirMundo: "Añadir un mundo",
    mundo: "Mundo",
  },
  caras: {
    aria: "Las caras de este espacio",
  },
};

const en: typeof es = {
  murallaSinPlan: "First generate your idea's plan: your {{mundo}} world will be built on top of it.",
  cambiador: {
    aria: "Your project's spaces",
    tuViaje: "Your Journey",
    anadirMundo: "Add a world",
    mundo: "World",
  },
  caras: {
    aria: "The views of this space",
  },
};

const fr: typeof es = {
  murallaSinPlan: "Génère d'abord le plan de ton idée : ton monde {{mundo}} se construira dessus.",
  cambiador: {
    aria: "Les espaces de ton projet",
    tuViaje: "Ton parcours",
    anadirMundo: "Ajouter un monde",
    mundo: "Monde",
  },
  caras: {
    aria: "Les vues de cet espace",
  },
};

const pt: typeof es = {
  murallaSinPlan: "Primeiro gere o plano da sua ideia: seu mundo de {{mundo}} será construído sobre ele.",
  cambiador: {
    aria: "Os espaços do seu projeto",
    tuViaje: "Sua Jornada",
    anadirMundo: "Adicionar um mundo",
    mundo: "Mundo",
  },
  caras: {
    aria: "As visões deste espaço",
  },
};

const de: typeof es = {
  murallaSinPlan: "Erstelle zuerst den Plan für deine Idee: Deine Welt {{mundo}} baut darauf auf.",
  cambiador: {
    aria: "Die Bereiche deines Projekts",
    tuViaje: "Deine Reise",
    anadirMundo: "Welt hinzufügen",
    mundo: "Welt",
  },
  caras: {
    aria: "Die Ansichten dieses Bereichs",
  },
};

const it: typeof es = {
  murallaSinPlan: "Prima genera il piano della tua idea: il tuo mondo {{mundo}} verrà costruito su quello.",
  cambiador: {
    aria: "Gli spazi del tuo progetto",
    tuViaje: "Il tuo viaggio",
    anadirMundo: "Aggiungi un mondo",
    mundo: "Mondo",
  },
  caras: {
    aria: "Le viste di questo spazio",
  },
};

const ja: typeof es = {
  murallaSinPlan: "まずはアイデアのプランを作成してください。ワールド「{{mundo}}」は、そのプランの上に組み立てられます。",
  cambiador: {
    aria: "プロジェクトのスペース",
    tuViaje: "あなたの旅",
    anadirMundo: "ワールドを追加",
    mundo: "ワールド",
  },
  caras: {
    aria: "このスペースのビュー",
  },
};

const zh: typeof es = {
  murallaSinPlan: "先生成你想法的计划：你的“{{mundo}}”世界会在它的基础上搭建。",
  cambiador: {
    aria: "你项目的各个空间",
    tuViaje: "你的旅程",
    anadirMundo: "添加一个世界",
    mundo: "世界",
  },
  caras: {
    aria: "这个空间的各个视图",
  },
};

const ko: typeof es = {
  murallaSinPlan: "먼저 아이디어의 계획을 만들어 주세요. {{mundo}} 월드는 그 계획 위에 세워져요.",
  cambiador: {
    aria: "프로젝트의 공간",
    tuViaje: "나의 여정",
    anadirMundo: "월드 추가",
    mundo: "월드",
  },
  caras: {
    aria: "이 공간의 보기",
  },
};

const ar: typeof es = {
  murallaSinPlan: "أعدّوا خطة فكرتكم أولًا: فعالم {{mundo}} سيُبنى عليها.",
  cambiador: {
    aria: "مساحات مشروعكم",
    tuViaje: "رحلتكم",
    anadirMundo: "إضافة عالم",
    mundo: "عالم",
  },
  caras: {
    aria: "عروض هذه المساحة",
  },
};

const hi: typeof es = {
  murallaSinPlan: "पहले अपने विचार की योजना बनाएँ: आपकी {{mundo}} दुनिया उसी पर बनेगी।",
  cambiador: {
    aria: "आपकी परियोजना के क्षेत्र",
    tuViaje: "आपकी यात्रा",
    anadirMundo: "एक दुनिया जोड़ें",
    mundo: "दुनिया",
  },
  caras: {
    aria: "इस क्षेत्र के दृश्य",
  },
};

export const ESPACIOS: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
