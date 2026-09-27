/** La portada pública ("/"): ui/Landing.tsx y los metadatos de app/page.tsx. */
import type { PorIdioma } from "../config";

const es = {
  meta: {
    titulo: "My Idea: transforma tu creatividad en acción",
    descripcion:
      "A los emprendedores no les faltan ideas. Les falta un interlocutor serio. Cuéntala, recibe tu plan y ejecútalo.",
  },
  nav: {
    inicio: "Inicio",
    acercaDe: "Acerca de",
    comoFunciona: "Cómo funciona",
    app: "App",
  },
  salir: "Salir",
  iniciarSesion: "Iniciar sesión",
  misIdeas: "Mis ideas",
  comenzar: "Comenzar",
  comenzarGratis: "Comenzar gratis",
  tituloOculto: "My Idea: transforma tu creatividad en acción",
  /** Las cinco etapas del recorrido (marquesina, mockup y banda del árbol). */
  etapas: {
    chispa: "La Chispa",
    claridad: "Claridad",
    exploracion: "La Exploración",
    plan: "Tu Plan",
    manos: "Manos a la Obra",
  },
  recorridoDeLaIdea: "Recorrido de la idea",
  marquesina: {
    unaAccion: "Una acción para esta semana",
    proyectoVivo: "Tu proyecto vivo",
  },
  acerca: {
    titulo: "A los emprendedores no les faltan ideas. Les falta un interlocutor serio",
    parrafo1:
      "My Idea nace de esa convicción. Construimos un motor de conocimiento que pregunta como un buen mentor y estructura como un buen consultor: escucha tu contexto, no repite plantillas, y sabe cuándo una etapa ya quedó cubierta por lo que contaste.",
    parrafo2:
      "El resultado no es una conversación que se pierde: es un proyecto vivo. Pausa, ejecuta en el mundo real y regresa cuando quieras. My Idea recalcula dónde estás parado y te muestra los siguientes pasos exactos, hasta el cierre definitivo. Y si el proyecto lo exige, se expande con módulos especializados.",
  },
  como: {
    titulo: "De la idea al mundo real",
    cuentameTuIdea: "Cuéntame tu idea, o en qué punto estás con ella",
    paso1: {
      titulo: "Describe tu idea",
      texto: "Escríbela o díctala tal como la tienes en mente. Ese es todo el requisito.",
    },
    paso2: {
      demo: "generando…",
      titulo: "Aporta más detalles",
      texto:
        "Nada de plantillas: una entrevista específica evoluciona en tiempo real con la naturaleza de tu idea y te habla en tu propio lenguaje, sin barreras técnicas.",
    },
    paso3: {
      demo: "Esta semana",
      titulo: "Recibe tu plan",
      texto:
        "Un plan detallado con etapas, experimentos y acciones concretas para ejecutarlo. Aquí se genera tu hoja de ruta.",
    },
    paso4: {
      demo: "siguiente paso exacto",
      titulo: "Ejecuta y regresa",
      texto:
        "Pausa, actúa en el mundo real y vuelve: el plan recalcula dónde estás y te muestra los pasos exactos hasta el cierre.",
    },
  },
  mockup: {
    titulo: "No es un chatbot, es tu espacio de trabajo",
    barra: "Cafetería de especialidad a domicilio · Entrevista",
    enCurso: "en curso…",
    categoria: "Calidad y diseño en tu primera versión",
    pregunta:
      "De estos dos riesgos, el café que llega frío y el costo del empaque térmico, ¿cuál necesitas resolver PRIMERO para confiar en que el negocio funciona como sistema?",
    fraseDemo: "Primero la temperatura: si el café llega frío, el empaque ya no importa.",
    enviar: "Enviar",
  },
  banda: {
    titulo: "De la chispa a la realidad",
    texto:
      "Cinco etapas acompañan tu idea desde el primer destello hasta verla funcionando en el mundo real. En cada una sabes dónde estás y cuál es el siguiente paso.",
  },
  descargar: {
    etiqueta: "La app",
    titulo: "Llévala en el bolsillo",
    texto: "Las mejores respuestas llegan lejos del escritorio.",
    googlePlay: "Descargar en Google Play",
    dictar: "también puedes dictarla",
  },
  cta: {
    titulo: "Aquí acaba tu idea y nace tu proyecto",
  },
  pie: {
    privacidad: "Privacidad",
    terminos: "Términos",
    derechos: "© {{ano}} My Idea",
  },
};

const en: typeof es = {
  meta: {
    titulo: "My Idea: turn your creativity into action",
    descripcion:
      "Entrepreneurs don't lack ideas. What they lack is a serious sounding board. Share yours, get your plan, and put it to work.",
  },
  nav: {
    inicio: "Home",
    acercaDe: "About",
    comoFunciona: "How it works",
    app: "App",
  },
  salir: "Log out",
  iniciarSesion: "Log in",
  misIdeas: "My ideas",
  comenzar: "Get started",
  comenzarGratis: "Start for free",
  tituloOculto: "My Idea: turn your creativity into action",
  etapas: {
    chispa: "The Spark",
    claridad: "Clarity",
    exploracion: "Exploration",
    plan: "Your Plan",
    manos: "Get to Work",
  },
  recorridoDeLaIdea: "Your idea's journey",
  marquesina: {
    unaAccion: "One action for this week",
    proyectoVivo: "Your living project",
  },
  acerca: {
    titulo: "Entrepreneurs don't lack ideas. What they lack is a serious sounding board",
    parrafo1:
      "My Idea was born from that belief. We built a knowledge engine that asks like a good mentor and structures like a good consultant: it listens to your context, doesn't recycle templates, and knows when what you've shared already covers a stage.",
    parrafo2:
      "What you get isn't a conversation that fades away: it's a living project. Pause, act in the real world, and come back whenever you want. My Idea works out where you stand and shows you the exact next steps, all the way to the finish line. And if your project calls for it, it grows with specialized modules.",
  },
  como: {
    titulo: "From idea to the real world",
    cuentameTuIdea: "Tell me your idea, or where you are with it",
    paso1: {
      titulo: "Describe your idea",
      texto: "Write it or say it, just as you picture it. That's all it takes.",
    },
    paso2: {
      demo: "generating…",
      titulo: "Add more detail",
      texto:
        "No templates: a tailored interview evolves in real time with the nature of your idea and speaks your language, with no technical barriers.",
    },
    paso3: {
      demo: "This week",
      titulo: "Get your plan",
      texto:
        "A detailed plan with stages, experiments, and concrete actions to carry it out. This is where your roadmap comes together.",
    },
    paso4: {
      demo: "exact next step",
      titulo: "Act and come back",
      texto:
        "Pause, take action in the real world, and come back: the plan works out where you are and shows you the exact steps to the finish line.",
    },
  },
  mockup: {
    titulo: "It's not a chatbot, it's your workspace",
    barra: "Specialty coffee delivery · Interview",
    enCurso: "in progress…",
    categoria: "Quality and design in your first version",
    pregunta:
      "Of these two risks, coffee that arrives cold and the cost of insulated packaging, which one do you need to solve FIRST to trust that the business works as a system?",
    fraseDemo: "Temperature first: if the coffee arrives cold, the packaging doesn't matter anymore.",
    enviar: "Send",
  },
  banda: {
    titulo: "From spark to reality",
    texto:
      "Five stages carry your idea from the first spark to seeing it work in the real world. At every one, you know where you are and what comes next.",
  },
  descargar: {
    etiqueta: "The app",
    titulo: "Keep it in your pocket",
    texto: "The best answers come to you away from your desk.",
    googlePlay: "Get it on Google Play",
    dictar: "you can also just say it",
  },
  cta: {
    titulo: "This is where your idea ends and your project begins",
  },
  pie: {
    privacidad: "Privacy",
    terminos: "Terms",
    derechos: "© {{ano}} My Idea",
  },
};

const fr: typeof es = {
  meta: {
    titulo: "My Idea : mets ta créativité en action",
    descripcion: "Les entrepreneurs ne manquent pas d'idées. Ce qui leur manque, c'est un interlocuteur sérieux. Raconte la tienne, reçois ton plan et passe à l'action.",
  },
  nav: {
    inicio: "Accueil",
    acercaDe: "À propos",
    comoFunciona: "Comment ça marche",
    app: "Appli",
  },
  salir: "Se déconnecter",
  iniciarSesion: "Se connecter",
  misIdeas: "Mes idées",
  comenzar: "Commencer",
  comenzarGratis: "Commencer gratuitement",
  tituloOculto: "My Idea : mets ta créativité en action",
  etapas: {
    chispa: "L'Étincelle",
    claridad: "Clarté",
    exploracion: "L'Exploration",
    plan: "Ton plan",
    manos: "À l'ouvrage",
  },
  recorridoDeLaIdea: "Le cheminement de l'idée",
  marquesina: {
    unaAccion: "Une action pour cette semaine",
    proyectoVivo: "Ton projet vivant",
  },
  acerca: {
    titulo: "Les entrepreneurs ne manquent pas d'idées. Ce qui leur manque, c'est un interlocuteur sérieux",
    parrafo1: "My Idea est né de cette conviction. Nous avons construit un moteur de connaissances qui questionne comme un bon mentor et structure comme un bon consultant : il écoute ton contexte, ne ressert pas de modèles tout faits, et sait quand ce que tu as raconté couvre déjà une étape.",
    parrafo2: "Le résultat n'est pas une conversation qui s'envole : c'est un projet vivant. Fais une pause, passe à l'action dans le monde réel et reviens quand tu veux. My Idea recalcule où tu en es et te montre précisément quoi faire ensuite, jusqu'à la clôture finale. Et si le projet l'exige, il s'enrichit de modules spécialisés.",
  },
  como: {
    titulo: "De l'idée au monde réel",
    cuentameTuIdea: "Raconte-moi ton idée, ou où tu en es avec elle",
    paso1: {
      titulo: "Décris ton idée",
      texto: "Écris-la ou dicte-la telle que tu l'as en tête. C'est tout ce qu'il faut.",
    },
    paso2: {
      demo: "génération…",
      titulo: "Ajoute des détails",
      texto: "Pas de modèles : un entretien sur mesure évolue en temps réel selon la nature de ton idée et te parle dans tes mots, sans barrière technique.",
    },
    paso3: {
      demo: "Cette semaine",
      titulo: "Reçois ton plan",
      texto: "Un plan détaillé avec des étapes, des expériences et des actions concrètes pour le réaliser. C'est ici que se dessine ta feuille de route.",
    },
    paso4: {
      demo: "prochain pas précis",
      titulo: "Agis et reviens",
      texto: "Fais une pause, agis dans le monde réel et reviens : le plan recalcule où tu en es et te montre le chemin précis jusqu'à la clôture.",
    },
  },
  mockup: {
    titulo: "Ce n'est pas un robot conversationnel, c'est ton espace de travail",
    barra: "Café de spécialité livré à domicile · Entretien",
    enCurso: "en cours…",
    categoria: "Qualité et conception dès ta première version",
    pregunta: "De ces deux risques, le café qui arrive froid et le coût de l'emballage isotherme, lequel dois-tu régler EN PREMIER pour avoir la certitude que ton commerce fonctionne comme un tout?",
    fraseDemo: "D'abord la température : si le café arrive froid, l'emballage ne compte plus.",
    enviar: "Envoyer",
  },
  banda: {
    titulo: "De l'étincelle à la réalité",
    texto: "Cinq étapes accompagnent ton idée, de la première lueur jusqu'au jour où tu la vois fonctionner dans le monde réel. À chacune, tu sais où tu en es et ce qui vient ensuite.",
  },
  descargar: {
    etiqueta: "L'appli",
    titulo: "Garde-la dans ta poche",
    texto: "Les meilleures réponses arrivent loin du bureau.",
    googlePlay: "Disponible sur Google Play",
    dictar: "tu peux aussi la dicter",
  },
  cta: {
    titulo: "Ici s'achève ton idée et naît ton projet",
  },
  pie: {
    privacidad: "Confidentialité",
    terminos: "Conditions",
    derechos: "© {{ano}} My Idea",
  },
};

const pt: typeof es = {
  meta: {
    titulo: "My Idea: transforme sua criatividade em ação",
    descripcion: "Aos empreendedores não faltam ideias. Falta alguém sério do outro lado da conversa. Conte a sua, receba seu plano e coloque em prática.",
  },
  nav: {
    inicio: "Início",
    acercaDe: "Sobre",
    comoFunciona: "Como funciona",
    app: "App",
  },
  salir: "Sair",
  iniciarSesion: "Entrar",
  misIdeas: "Minhas ideias",
  comenzar: "Começar",
  comenzarGratis: "Começar grátis",
  tituloOculto: "My Idea: transforme sua criatividade em ação",
  etapas: {
    chispa: "A Faísca",
    claridad: "Clareza",
    exploracion: "A Exploração",
    plan: "Seu Plano",
    manos: "Mãos à Obra",
  },
  recorridoDeLaIdea: "Percurso da ideia",
  marquesina: {
    unaAccion: "Uma ação para esta semana",
    proyectoVivo: "Seu projeto vivo",
  },
  acerca: {
    titulo: "Aos empreendedores não faltam ideias. Falta alguém sério do outro lado da conversa",
    parrafo1: "O My Idea nasce dessa convicção. Construímos um motor de conhecimento que pergunta como um bom mentor e estrutura como um bom consultor: escuta o seu contexto, não repete modelos prontos e sabe quando uma etapa já ficou coberta pelo que você contou.",
    parrafo2: "O resultado não é uma conversa que se perde: é um projeto vivo. Pause, execute no mundo real e volte quando quiser. O My Idea recalcula onde você está e mostra os próximos passos exatos, até o encerramento definitivo. E, se o projeto pedir, ele se expande com módulos especializados.",
  },
  como: {
    titulo: "Da ideia ao mundo real",
    cuentameTuIdea: "Me conte sua ideia, ou em que ponto você está com ela",
    paso1: {
      titulo: "Descreva sua ideia",
      texto: "Escreva ou dite do jeito que ela está na sua cabeça. Esse é o único requisito.",
    },
    paso2: {
      demo: "gerando…",
      titulo: "Traga mais detalhes",
      texto: "Nada de modelos prontos: uma entrevista feita sob medida evolui em tempo real conforme a natureza da sua ideia e fala a sua língua, sem barreiras técnicas.",
    },
    paso3: {
      demo: "Esta semana",
      titulo: "Receba seu plano",
      texto: "Um plano detalhado com etapas, experimentos e ações concretas para colocá-lo em prática. É aqui que seu roteiro ganha forma.",
    },
    paso4: {
      demo: "próximo passo exato",
      titulo: "Execute e volte",
      texto: "Pause, aja no mundo real e volte: o plano recalcula onde você está e mostra os passos exatos até o encerramento.",
    },
  },
  mockup: {
    titulo: "Não é um chatbot, é o seu espaço de trabalho",
    barra: "Delivery de café especial · Entrevista",
    enCurso: "em andamento…",
    categoria: "Qualidade e design na sua primeira versão",
    pregunta: "Destes dois riscos, o café que chega frio e o custo da embalagem térmica, qual você precisa resolver PRIMEIRO para confiar que o negócio funciona como sistema?",
    fraseDemo: "Primeiro a temperatura: se o café chega frio, a embalagem já não importa.",
    enviar: "Enviar",
  },
  banda: {
    titulo: "Da faísca à realidade",
    texto: "Cinco etapas acompanham sua ideia desde o primeiro lampejo até vê-la funcionando no mundo real. Em cada uma, você sabe onde está e qual é o próximo passo.",
  },
  descargar: {
    etiqueta: "O app",
    titulo: "Leve no bolso",
    texto: "As melhores respostas chegam longe da mesa de trabalho.",
    googlePlay: "Disponível no Google Play",
    dictar: "você também pode ditar",
  },
  cta: {
    titulo: "Aqui termina sua ideia e nasce seu projeto",
  },
  pie: {
    privacidad: "Privacidade",
    terminos: "Termos",
    derechos: "© {{ano}} My Idea",
  },
};

const de: typeof es = {
  meta: {
    titulo: "My Idea: Verwandle deine Kreativität in Taten",
    descripcion: "Wer etwas gründen will, hat genug Ideen. Was fehlt, ist ein Gegenüber, das sie ernst nimmt. Erzähl deine Idee, hol dir deinen Plan und setz ihn um.",
  },
  nav: {
    inicio: "Start",
    acercaDe: "Über uns",
    comoFunciona: "So funktioniert's",
    app: "App",
  },
  salir: "Abmelden",
  iniciarSesion: "Anmelden",
  misIdeas: "Meine Ideen",
  comenzar: "Loslegen",
  comenzarGratis: "Kostenlos loslegen",
  tituloOculto: "My Idea: Verwandle deine Kreativität in Taten",
  etapas: {
    chispa: "Der Funke",
    claridad: "Klarheit",
    exploracion: "Die Erkundung",
    plan: "Dein Plan",
    manos: "Ans Werk",
  },
  recorridoDeLaIdea: "Der Weg deiner Idee",
  marquesina: {
    unaAccion: "Ein Schritt für diese Woche",
    proyectoVivo: "Dein lebendiges Projekt",
  },
  acerca: {
    titulo: "Wer etwas gründen will, hat genug Ideen. Was fehlt, ist ein Gegenüber, das sie ernst nimmt",
    parrafo1: "My Idea ist aus dieser Überzeugung entstanden. Wir haben ein Wissenssystem gebaut, das fragt wie ein guter Mentor und ordnet wie ein guter Berater: Es hört auf deine Situation, spult keine Vorlagen ab und merkt, wann das, was du erzählt hast, eine Etappe schon abdeckt.",
    parrafo2: "Am Ende steht kein Gespräch, das verloren geht, sondern ein lebendiges Projekt. Mach Pause, handle in der echten Welt und komm zurück, wann du willst. My Idea ermittelt neu, wo du stehst, und zeigt dir die genauen nächsten Schritte, bis zum endgültigen Abschluss. Und wenn dein Projekt es verlangt, wächst es mit spezialisierten Modulen.",
  },
  como: {
    titulo: "Von der Idee in die echte Welt",
    cuentameTuIdea: "Erzähl mir deine Idee oder wo du damit gerade stehst",
    paso1: {
      titulo: "Beschreib deine Idee",
      texto: "Schreib sie auf oder sprich sie ein, so wie du sie im Kopf hast. Mehr braucht es nicht.",
    },
    paso2: {
      demo: "wird erstellt…",
      titulo: "Erzähl mehr",
      texto: "Keine Vorlagen: Ein Gespräch, das genau zu dir passt, entwickelt sich in Echtzeit mit deiner Idee und spricht deine Sprache, ganz ohne technische Hürden.",
    },
    paso3: {
      demo: "Diese Woche",
      titulo: "Hol dir deinen Plan",
      texto: "Ein detaillierter Plan mit Etappen, Experimenten und konkreten Schritten zur Umsetzung. Hier entsteht dein Fahrplan.",
    },
    paso4: {
      demo: "genau der nächste Schritt",
      titulo: "Setz um und komm zurück",
      texto: "Mach Pause, handle in der echten Welt und komm zurück: Der Plan ermittelt neu, wo du stehst, und zeigt dir die genauen Schritte bis zum Abschluss.",
    },
  },
  mockup: {
    titulo: "Kein Chatbot, sondern dein Arbeitsbereich",
    barra: "Spezialitätenkaffee als Lieferservice · Gespräch",
    enCurso: "läuft…",
    categoria: "Qualität und Design in deiner ersten Version",
    pregunta: "Von diesen beiden Risiken, dem Kaffee, der kalt ankommt, und den Kosten der Thermoverpackung: Welches musst du ZUERST lösen, um darauf vertrauen zu können, dass das Geschäft als System funktioniert?",
    fraseDemo: "Zuerst die Temperatur: Wenn der Kaffee kalt ankommt, ist die Verpackung egal.",
    enviar: "Senden",
  },
  banda: {
    titulo: "Vom Funken zur Wirklichkeit",
    texto: "Fünf Etappen begleiten deine Idee vom ersten Funken, bis du sie in der echten Welt funktionieren siehst. In jeder weißt du, wo du stehst und was als Nächstes kommt.",
  },
  descargar: {
    etiqueta: "Die App",
    titulo: "Immer in deiner Tasche",
    texto: "Die besten Antworten kommen dir fern vom Schreibtisch.",
    googlePlay: "Jetzt bei Google Play",
    dictar: "du kannst sie auch einsprechen",
  },
  cta: {
    titulo: "Hier endet deine Idee und beginnt dein Projekt",
  },
  pie: {
    privacidad: "Datenschutz",
    terminos: "Nutzungsbedingungen",
    derechos: "© {{ano}} My Idea",
  },
};

const it: typeof es = {
  meta: {
    titulo: "My Idea: trasforma la tua creatività in azione",
    descripcion: "Agli imprenditori non mancano le idee. Manca un interlocutore serio. Racconta la tua, ricevi il tuo piano e mettilo in pratica.",
  },
  nav: {
    inicio: "Home",
    acercaDe: "Chi siamo",
    comoFunciona: "Come funziona",
    app: "App",
  },
  salir: "Esci",
  iniciarSesion: "Accedi",
  misIdeas: "Le mie idee",
  comenzar: "Inizia",
  comenzarGratis: "Inizia gratis",
  tituloOculto: "My Idea: trasforma la tua creatività in azione",
  etapas: {
    chispa: "La Scintilla",
    claridad: "Chiarezza",
    exploracion: "L'Esplorazione",
    plan: "Il tuo piano",
    manos: "Al lavoro",
  },
  recorridoDeLaIdea: "Il percorso dell'idea",
  marquesina: {
    unaAccion: "Un'azione per questa settimana",
    proyectoVivo: "Il tuo progetto, vivo",
  },
  acerca: {
    titulo: "Agli imprenditori non mancano le idee. Manca un interlocutore serio",
    parrafo1: "My Idea nasce da questa convinzione. Abbiamo costruito un motore di conoscenza che fa domande come un buon mentore e mette ordine come un buon consulente: ascolta il tuo contesto, non ripete modelli preconfezionati e capisce quando quello che hai raccontato copre già una tappa.",
    parrafo2: "Il risultato non è una conversazione che si perde: è un progetto vivo. Fermati, agisci nel mondo reale e torna quando vuoi. My Idea ricalcola a che punto sei e ti mostra i prossimi passi esatti, fino al traguardo finale. E se il progetto lo richiede, si amplia con moduli specializzati.",
  },
  como: {
    titulo: "Dall'idea al mondo reale",
    cuentameTuIdea: "Raccontami la tua idea, o a che punto sei",
    paso1: {
      titulo: "Descrivi la tua idea",
      texto: "Scrivila o dettala così come ce l'hai in testa. Non serve altro.",
    },
    paso2: {
      demo: "in generazione…",
      titulo: "Aggiungi dettagli",
      texto: "Niente modelli: un'intervista su misura si evolve in tempo reale secondo la natura della tua idea e ti parla con parole tue, senza barriere tecniche.",
    },
    paso3: {
      demo: "Questa settimana",
      titulo: "Ricevi il tuo piano",
      texto: "Un piano dettagliato con tappe, esperimenti e azioni concrete per metterlo in pratica. Qui prende forma la tua tabella di marcia.",
    },
    paso4: {
      demo: "prossimo passo esatto",
      titulo: "Agisci e torna",
      texto: "Fermati, agisci nel mondo reale e torna: il piano ricalcola a che punto sei e ti mostra i passi esatti fino al traguardo.",
    },
  },
  mockup: {
    titulo: "Non è un chatbot, è il tuo spazio di lavoro",
    barra: "Caffè di qualità a domicilio · Intervista",
    enCurso: "in corso…",
    categoria: "Qualità e design nella tua prima versione",
    pregunta: "Di questi due rischi, il caffè che arriva freddo e il costo dell'imballaggio termico, quale devi risolvere PER PRIMO per avere la certezza che l'attività funzioni come sistema?",
    fraseDemo: "Prima la temperatura: se il caffè arriva freddo, l'imballaggio non conta più.",
    enviar: "Invia",
  },
  banda: {
    titulo: "Dalla scintilla alla realtà",
    texto: "Cinque tappe accompagnano la tua idea dalla prima intuizione fino a vederla funzionare nel mondo reale. In ognuna sai dove sei e qual è il passo successivo.",
  },
  descargar: {
    etiqueta: "L'app",
    titulo: "Portala sempre con te",
    texto: "Le risposte migliori arrivano lontano dalla scrivania.",
    googlePlay: "Disponibile su Google Play",
    dictar: "puoi anche dettarla",
  },
  cta: {
    titulo: "Qui finisce la tua idea e nasce il tuo progetto",
  },
  pie: {
    privacidad: "Privacy",
    terminos: "Termini",
    derechos: "© {{ano}} My Idea",
  },
};

const ja: typeof es = {
  meta: {
    titulo: "My Idea：あなたの創造力を、行動に変える",
    descripcion: "起業家に足りないのは、アイデアではありません。真剣に向き合ってくれる相手です。アイデアを話して、プランを受け取り、実行に移しましょう。",
  },
  nav: {
    inicio: "ホーム",
    acercaDe: "私たちについて",
    comoFunciona: "使い方",
    app: "アプリ",
  },
  salir: "ログアウト",
  iniciarSesion: "ログイン",
  misIdeas: "アイデア一覧",
  comenzar: "はじめる",
  comenzarGratis: "無料ではじめる",
  tituloOculto: "My Idea：あなたの創造力を、行動に変える",
  etapas: {
    chispa: "ひらめき",
    claridad: "明確さ",
    exploracion: "探求",
    plan: "あなたのプラン",
    manos: "実行",
  },
  recorridoDeLaIdea: "アイデアの道のり",
  marquesina: {
    unaAccion: "今週やる、ひとつのアクション",
    proyectoVivo: "動き続けるプロジェクト",
  },
  acerca: {
    titulo: "起業家に足りないのは、アイデアではありません。真剣に向き合ってくれる相手です",
    parrafo1: "My Ideaは、その確信から生まれました。私たちがつくったのは、良きメンターのように問いかけ、優れたコンサルタントのように整理するナレッジエンジンです。あなたの状況に耳を傾け、テンプレートを繰り返さず、話した内容でステージがもう満たされたかどうかを見極めます。",
    parrafo2: "手元に残るのは、流れて消えていく会話ではありません。動き続けるプロジェクトです。一度止めて、現実の世界で動き、いつでも戻ってきてください。My Ideaが今の立ち位置を計算し直し、最後の締めくくりまで、次にやるべき具体的な一歩を示します。プロジェクトが必要とすれば、専門のモジュールで広がっていきます。",
  },
  como: {
    titulo: "アイデアを、現実の世界へ",
    cuentameTuIdea: "アイデアを聞かせてください。今どこまで進んでいるかでもかまいません",
    paso1: {
      titulo: "アイデアを伝える",
      texto: "頭の中にあるままを、書くか話すだけ。必要なのはそれだけです。",
    },
    paso2: {
      demo: "生成中…",
      titulo: "詳しく話す",
      texto: "テンプレートはありません。アイデアの性質に合わせて専用のインタビューがリアルタイムに変化し、専門用語の壁なしに、あなたの言葉で語りかけます。",
    },
    paso3: {
      demo: "今週",
      titulo: "プランを受け取る",
      texto: "ステージ、実験、実行のための具体的なアクションまでそろった、詳しいプラン。あなたのロードマップは、ここで生まれます。",
    },
    paso4: {
      demo: "次にやるべき一歩",
      titulo: "実行して、戻ってくる",
      texto: "一度止めて、現実の世界で動いて、戻ってくる。プランが今の位置を計算し直し、締めくくりまでの具体的なステップを示します。",
    },
  },
  mockup: {
    titulo: "チャットボットではなく、あなたの作業スペースです",
    barra: "スペシャルティコーヒーの宅配 · インタビュー",
    enCurso: "進行中…",
    categoria: "最初のバージョンの品質とデザイン",
    pregunta: "コーヒーが冷めて届くことと、保温パッケージのコスト。この2つのリスクのうち、ビジネスが仕組みとして成り立つと信じるために、まず解決すべきなのはどちらですか？",
    fraseDemo: "まずは温度です。コーヒーが冷めて届いたら、パッケージはもう関係ありません。",
    enviar: "送信",
  },
  banda: {
    titulo: "ひらめきを、現実に",
    texto: "最初のひらめきから、現実の世界で動き出すその日まで、5つのステージがあなたのアイデアに寄り添います。どのステージでも、今どこにいて、次に何をすればいいかがわかります。",
  },
  descargar: {
    etiqueta: "アプリ",
    titulo: "いつもポケットの中に",
    texto: "いい答えは、机を離れたときに浮かぶものです。",
    googlePlay: "Google Play で手に入れよう",
    dictar: "話して入力することもできます",
  },
  cta: {
    titulo: "ここでアイデアは終わり、プロジェクトが生まれます",
  },
  pie: {
    privacidad: "プライバシー",
    terminos: "利用規約",
    derechos: "© {{ano}} My Idea",
  },
};

const zh: typeof es = {
  meta: {
    titulo: "My Idea：把你的创意变成行动",
    descripcion: "创业者从不缺想法，缺的是一个认真的对话者。说出你的想法，拿到你的计划，然后动手去做。",
  },
  nav: {
    inicio: "首页",
    acercaDe: "关于我们",
    comoFunciona: "如何运作",
    app: "应用",
  },
  salir: "退出",
  iniciarSesion: "登录",
  misIdeas: "我的想法",
  comenzar: "开始",
  comenzarGratis: "免费开始",
  tituloOculto: "My Idea：把你的创意变成行动",
  etapas: {
    chispa: "灵光一闪",
    claridad: "清晰",
    exploracion: "探索",
    plan: "你的计划",
    manos: "动手做",
  },
  recorridoDeLaIdea: "想法的旅程",
  marquesina: {
    unaAccion: "本周的一项行动",
    proyectoVivo: "你的项目，持续生长",
  },
  acerca: {
    titulo: "创业者从不缺想法，缺的是一个认真的对话者",
    parrafo1: "My Idea 正是从这个信念中诞生的。我们打造了一个知识引擎：它像好导师一样提问，像好顾问一样梳理。它倾听你的具体情况，不套用模板，也知道你讲过的内容什么时候已经覆盖了某个阶段。",
    parrafo2: "你得到的不是一段聊完就散的对话，而是一个持续生长的项目。你可以暂停，去现实中行动，随时回来。My Idea 会重新判断你所处的位置，给出确切的下一步，一直陪你走到最后的收尾。如果项目需要，它还能接入专业模块，继续扩展。",
  },
  como: {
    titulo: "从想法到现实",
    cuentameTuIdea: "跟我说说你的想法，或者你现在走到哪一步了",
    paso1: {
      titulo: "描述你的想法",
      texto: "按你脑海中的样子写下来，或者直接说出来。这就是全部要求。",
    },
    paso2: {
      demo: "生成中…",
      titulo: "补充更多细节",
      texto: "没有模板：一场专属访谈会随着你想法的特点实时调整，用你自己的语言和你交流，没有任何技术门槛。",
    },
    paso3: {
      demo: "本周",
      titulo: "拿到你的计划",
      texto: "一份详细的计划，包含阶段、实验和具体行动，帮你把它落地。你的路线图就在这里生成。",
    },
    paso4: {
      demo: "确切的下一步",
      titulo: "去执行，再回来",
      texto: "暂停，去现实中行动，再回来：计划会重新判断你所处的位置，给出直到收尾的每一个确切步骤。",
    },
  },
  mockup: {
    titulo: "这不是聊天机器人，而是你的工作空间",
    barra: "精品咖啡外送 · 访谈",
    enCurso: "进行中…",
    categoria: "第一版的质量与设计",
    pregunta: "咖啡送到时已经凉了，保温包装的成本太高，这两个风险里，你最先需要解决哪一个，才能确信这门生意作为一个整体能跑得通？",
    fraseDemo: "先解决温度：如果咖啡送到时已经凉了，包装再好也没用。",
    enviar: "发送",
  },
  banda: {
    titulo: "从灵光一闪，到落地成真",
    texto: "五个阶段陪伴你的想法，从最初的灵光一现，一直到它在现实中运转起来。每个阶段，你都清楚自己在哪里、下一步是什么。",
  },
  descargar: {
    etiqueta: "应用",
    titulo: "把它装进口袋",
    texto: "最好的答案，往往在你离开办公桌时出现。",
    googlePlay: "在 Google Play 下载",
    dictar: "也可以直接说出来",
  },
  cta: {
    titulo: "你的想法在这里圆满，你的项目从这里启程",
  },
  pie: {
    privacidad: "隐私",
    terminos: "条款",
    derechos: "© {{ano}} My Idea",
  },
};

const ko: typeof es = {
  meta: {
    titulo: "My Idea: 창의력을 실행으로 바꿔 보세요",
    descripcion: "창업가에게 부족한 건 아이디어가 아니에요. 진지하게 함께 고민해 줄 상대예요. 아이디어를 들려주고, 계획을 받아, 실행해 보세요.",
  },
  nav: {
    inicio: "홈",
    acercaDe: "소개",
    comoFunciona: "이용 방법",
    app: "앱",
  },
  salir: "로그아웃",
  iniciarSesion: "로그인",
  misIdeas: "내 아이디어",
  comenzar: "시작하기",
  comenzarGratis: "무료로 시작하기",
  tituloOculto: "My Idea: 창의력을 실행으로 바꿔 보세요",
  etapas: {
    chispa: "불꽃",
    claridad: "명확함",
    exploracion: "탐색",
    plan: "나의 계획",
    manos: "실행하기",
  },
  recorridoDeLaIdea: "아이디어의 여정",
  marquesina: {
    unaAccion: "이번 주의 실행 항목 하나",
    proyectoVivo: "살아 움직이는 나의 프로젝트",
  },
  acerca: {
    titulo: "창업가에게 부족한 건 아이디어가 아니에요. 진지하게 함께 고민해 줄 상대예요",
    parrafo1: "My Idea는 바로 이 믿음에서 시작했어요. 좋은 멘토처럼 질문하고 좋은 컨설턴트처럼 정리하는 지식 엔진을 만들었어요. 상황에 귀 기울이고, 뻔한 템플릿을 되풀이하지 않으며, 들려준 이야기로 어떤 단계가 이미 채워졌는지 알아차려요.",
    parrafo2: "그 결과는 흘러가 버리는 대화가 아니라 살아 있는 프로젝트예요. 잠시 멈추고, 현실에서 실행하고, 언제든 돌아오세요. My Idea가 지금 어디쯤 서 있는지 다시 계산해서 정확한 다음 단계를 보여 줘요. 마지막 마무리까지요. 프로젝트에 필요하면 전문 모듈로 확장돼요.",
  },
  como: {
    titulo: "아이디어에서 현실로",
    cuentameTuIdea: "아이디어를 들려주세요. 지금 어디까지 왔는지도요",
    paso1: {
      titulo: "아이디어를 들려주세요",
      texto: "머릿속에 있는 그대로 쓰거나 말로 하세요. 필요한 건 그게 전부예요.",
    },
    paso2: {
      demo: "생성하는 중…",
      titulo: "조금 더 자세히 알려 주세요",
      texto: "템플릿은 없어요. 아이디어의 성격에 맞춰 실시간으로 달라지는 맞춤 인터뷰가, 어려운 전문 용어 없이 내 언어로 말을 걸어요.",
    },
    paso3: {
      demo: "이번 주",
      titulo: "계획을 받아 보세요",
      texto: "단계, 실험, 구체적인 실행 항목까지 담은 상세한 계획이에요. 나만의 로드맵이 여기서 만들어져요.",
    },
    paso4: {
      demo: "정확한 다음 단계",
      titulo: "실행하고 돌아오세요",
      texto: "잠시 멈추고, 현실에서 움직인 뒤 돌아오세요. 계획이 지금 위치를 다시 계산해서 마무리까지 정확한 단계를 보여 줘요.",
    },
  },
  mockup: {
    titulo: "챗봇이 아니에요. 나의 작업 공간이에요",
    barra: "스페셜티 커피 배달 · 인터뷰",
    enCurso: "진행 중…",
    categoria: "첫 버전의 품질과 디자인",
    pregunta: "식은 채 도착하는 커피, 그리고 보온 포장 비용. 이 두 가지 위험 중에서 사업이 하나의 시스템으로 돌아간다고 믿으려면 무엇을 가장 먼저 해결해야 하나요?",
    fraseDemo: "온도가 먼저예요. 커피가 식어서 도착하면 포장은 아무 의미가 없어요.",
    enviar: "보내기",
  },
  banda: {
    titulo: "불꽃에서 현실까지",
    texto: "첫 번째 불꽃부터 현실에서 실제로 돌아가는 모습을 보기까지, 다섯 단계가 아이디어와 함께해요. 단계마다 지금 어디에 있고 다음에 무엇을 할지 알 수 있어요.",
  },
  descargar: {
    etiqueta: "앱",
    titulo: "주머니 속에 넣고 다니세요",
    texto: "가장 좋은 답은 책상에서 멀리 떨어져 있을 때 떠올라요.",
    googlePlay: "Google Play에서 다운로드",
    dictar: "말로 해도 돼요",
  },
  cta: {
    titulo: "여기서 아이디어가 끝나고 프로젝트가 태어나요",
  },
  pie: {
    privacidad: "개인정보 처리방침",
    terminos: "이용약관",
    derechos: "© {{ano}} My Idea",
  },
};

const ar: typeof es = {
  meta: {
    titulo: "My Idea: حوّلوا إبداعكم إلى فعل",
    descripcion: "رواد الأعمال لا تنقصهم الأفكار، بل ينقصهم محاور جادّ. احكوا لنا فكرتكم، واحصلوا على خطتكم، ونفّذوها.",
  },
  nav: {
    inicio: "الرئيسية",
    acercaDe: "من نحن",
    comoFunciona: "كيف يعمل",
    app: "التطبيق",
  },
  salir: "تسجيل الخروج",
  iniciarSesion: "تسجيل الدخول",
  misIdeas: "أفكاري",
  comenzar: "ابدؤوا الآن",
  comenzarGratis: "ابدؤوا مجانًا",
  tituloOculto: "My Idea: حوّلوا إبداعكم إلى فعل",
  etapas: {
    chispa: "الشرارة",
    claridad: "الوضوح",
    exploracion: "الاستكشاف",
    plan: "خطتكم",
    manos: "إلى العمل",
  },
  recorridoDeLaIdea: "مسار الفكرة",
  marquesina: {
    unaAccion: "إجراء واحد لهذا الأسبوع",
    proyectoVivo: "مشروعكم الحيّ",
  },
  acerca: {
    titulo: "رواد الأعمال لا تنقصهم الأفكار، بل ينقصهم محاور جادّ",
    parrafo1: "من هذه القناعة وُلدت My Idea. بنينا محرّك معرفة يسأل كما يسأل مرشد جيد، وينظّم كما ينظّم مستشار جيد: يصغي إلى سياقكم، ولا يكرّر القوالب، ويعرف متى صارت مرحلة ما مغطّاة بما رويتموه.",
    parrafo2: "النتيجة ليست محادثة تضيع، بل مشروع حيّ. توقّفوا، ونفّذوا في العالم الحقيقي، وعودوا متى شئتم. تعيد My Idea حساب موقعكم وتُريكم الخطوات التالية بدقة، حتى الإغلاق النهائي. وإن تطلّب المشروع ذلك، يتّسع بوحدات متخصّصة.",
  },
  como: {
    titulo: "من الفكرة إلى العالم الحقيقي",
    cuentameTuIdea: "احكوا لي فكرتكم، أو إلى أين وصلتم بها",
    paso1: {
      titulo: "صِفوا فكرتكم",
      texto: "اكتبوها أو أملوها كما هي في أذهانكم. هذا كل المطلوب.",
    },
    paso2: {
      demo: "جارٍ الإنشاء…",
      titulo: "أضيفوا تفاصيل أكثر",
      texto: "لا قوالب هنا: مقابلة مصمَّمة لفكرتكم تتطوّر في الوقت الفعلي مع طبيعتها، وتخاطبكم بلغتكم أنتم، بلا حواجز تقنية.",
    },
    paso3: {
      demo: "هذا الأسبوع",
      titulo: "احصلوا على خطتكم",
      texto: "خطة مفصّلة بمراحل وتجارب وإجراءات ملموسة لتنفيذها. هنا تُرسم خارطة طريقكم.",
    },
    paso4: {
      demo: "الخطوة التالية بدقة",
      titulo: "نفّذوا وعودوا",
      texto: "توقّفوا، واعملوا في العالم الحقيقي، ثم عودوا: تعيد الخطة حساب موقعكم وتُريكم الخطوات الدقيقة حتى الإغلاق.",
    },
  },
  mockup: {
    titulo: "ليس روبوت دردشة، بل مساحة عملكم",
    barra: "توصيل القهوة المختصّة إلى المنازل · مقابلة",
    enCurso: "جارية…",
    categoria: "الجودة والتصميم في نسختكم الأولى",
    pregunta: "من بين هذين الخطرين، القهوة التي تصل باردة وتكلفة التغليف الحراري، أيّهما تحتاجون إلى حلّه أولًا، قبل أي شيء، لتثقوا بأن المشروع يعمل كمنظومة متكاملة؟",
    fraseDemo: "الحرارة أولًا: إن وصلت القهوة باردة، فلن يعود للتغليف أي أهمية.",
    enviar: "إرسال",
  },
  banda: {
    titulo: "من الشرارة إلى الواقع",
    texto: "خمس مراحل ترافق فكرتكم من أول ومضة حتى ترونها تعمل في العالم الحقيقي. في كل منها تعرفون أين أنتم وما الخطوة التالية.",
  },
  descargar: {
    etiqueta: "التطبيق",
    titulo: "احملوه في جيبكم",
    texto: "أفضل الإجابات تأتي بعيدًا عن المكتب.",
    googlePlay: "متوفر على Google Play",
    dictar: "ويمكنكم أيضًا إملاؤها",
  },
  cta: {
    titulo: "هنا تنتهي فكرتكم ويولد مشروعكم",
  },
  pie: {
    privacidad: "الخصوصية",
    terminos: "الشروط",
    derechos: "© {{ano}} My Idea",
  },
};

const hi: typeof es = {
  meta: {
    titulo: "My Idea: अपनी रचनात्मकता को अमल में लाएँ",
    descripcion: "उद्यमियों के पास विचारों की कमी नहीं होती। कमी होती है ऐसे साथी की जो उनकी बात गंभीरता से ले। अपना विचार बताएँ, अपनी योजना पाएँ और उसे अमल में लाएँ।",
  },
  nav: {
    inicio: "होम",
    acercaDe: "हमारे बारे में",
    comoFunciona: "यह कैसे काम करता है",
    app: "ऐप",
  },
  salir: "लॉग आउट",
  iniciarSesion: "लॉग इन करें",
  misIdeas: "मेरे विचार",
  comenzar: "शुरू करें",
  comenzarGratis: "मुफ़्त में शुरू करें",
  tituloOculto: "My Idea: अपनी रचनात्मकता को अमल में लाएँ",
  etapas: {
    chispa: "चिंगारी",
    claridad: "स्पष्टता",
    exploracion: "अन्वेषण",
    plan: "आपकी योजना",
    manos: "काम शुरू करें",
  },
  recorridoDeLaIdea: "विचार का रास्ता",
  marquesina: {
    unaAccion: "इस हफ़्ते के लिए एक कदम",
    proyectoVivo: "आपकी जीवंत परियोजना",
  },
  acerca: {
    titulo: "उद्यमियों के पास विचारों की कमी नहीं होती। कमी होती है ऐसे साथी की जो उनकी बात गंभीरता से ले",
    parrafo1: "My Idea इसी सोच से जन्मा है। हमने एक ज्ञान इंजन बनाया है जो एक अच्छे मेंटर की तरह सवाल पूछता है और एक अच्छे सलाहकार की तरह चीज़ों को ढाँचा देता है: यह आपकी पूरी स्थिति सुनता है, रटे-रटाए टेम्पलेट नहीं दोहराता, और समझता है कि आपकी बताई बातों से कोई चरण कब पूरा हो चुका है।",
    parrafo2: "नतीजा कोई ऐसी बातचीत नहीं जो कहीं खो जाए: यह एक जीवंत परियोजना है। रुकें, असल दुनिया में काम करें और जब चाहें लौट आएँ। My Idea फिर से हिसाब लगाता है कि आप अभी कहाँ हैं और आपको अगले सटीक कदम दिखाता है, आख़िरी मंज़िल तक। और अगर परियोजना को ज़रूरत हो, तो यह खास मॉड्यूल के साथ और बड़ा हो जाता है।",
  },
  como: {
    titulo: "विचार से असल दुनिया तक",
    cuentameTuIdea: "मुझे अपना विचार बताएँ, या यह कि वह अभी किस मोड़ पर है",
    paso1: {
      titulo: "अपना विचार बताएँ",
      texto: "इसे लिखें या बोलकर लिखवाएँ, ठीक वैसे ही जैसे यह आपके मन में है। बस इतना ही चाहिए।",
    },
    paso2: {
      demo: "बन रहा है…",
      titulo: "और जानकारी दें",
      texto: "कोई टेम्पलेट नहीं: एक खास बातचीत आपके विचार के स्वभाव के हिसाब से उसी वक़्त ढलती जाती है और आपकी अपनी भाषा में बात करती है, बिना किसी तकनीकी रुकावट के।",
    },
    paso3: {
      demo: "इस हफ़्ते",
      titulo: "अपनी योजना पाएँ",
      texto: "चरणों, प्रयोगों और ठोस कदमों वाली एक विस्तृत योजना, जिस पर आप अमल कर सकें। यहीं आपका रोडमैप तैयार होता है।",
    },
    paso4: {
      demo: "अगला सटीक कदम",
      titulo: "अमल करें और लौटें",
      texto: "रुकें, असल दुनिया में कदम उठाएँ और लौट आएँ: योजना फिर से हिसाब लगाती है कि आप कहाँ हैं और आपको मंज़िल तक के सटीक कदम दिखाती है।",
    },
  },
  mockup: {
    titulo: "यह चैटबॉट नहीं, आपके काम करने की जगह है",
    barra: "घर तक स्पेशलिटी कॉफ़ी · बातचीत",
    enCurso: "चल रही है…",
    categoria: "आपके पहले संस्करण में गुणवत्ता और डिज़ाइन",
    pregunta: "इन दो जोखिमों में से, ठंडी पहुँचने वाली कॉफ़ी और थर्मल पैकेजिंग की लागत, आपको सबसे पहले किसे हल करना होगा ताकि भरोसा हो कि कारोबार एक सिस्टम की तरह चलता है?",
    fraseDemo: "पहले तापमान: अगर कॉफ़ी ठंडी पहुँची, तो पैकेजिंग का कोई मतलब नहीं रहता।",
    enviar: "भेजें",
  },
  banda: {
    titulo: "चिंगारी से हकीकत तक",
    texto: "पाँच चरण आपके विचार के साथ चलते हैं, पहली चमक से लेकर उसे असल दुनिया में चलता देखने तक। हर चरण में आपको पता रहता है कि आप कहाँ हैं और अगला कदम क्या है।",
  },
  descargar: {
    etiqueta: "ऐप",
    titulo: "इसे अपनी जेब में रखें",
    texto: "सबसे अच्छे जवाब अक्सर डेस्क से दूर सूझते हैं।",
    googlePlay: "Google Play पर पाएँ",
    dictar: "इसे बोलकर भी लिखवाया जा सकता है",
  },
  cta: {
    titulo: "यहाँ आपका विचार पूरा होता है और आपकी परियोजना जन्म लेती है",
  },
  pie: {
    privacidad: "गोपनीयता",
    terminos: "शर्तें",
    derechos: "© {{ano}} My Idea",
  },
};

export const PORTADA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
