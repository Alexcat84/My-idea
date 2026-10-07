/** La portada pública ("/"): ui/Landing.tsx y los metadatos de app/page.tsx. */
import type { PorIdioma } from "../config";
import { PRECIOS } from "../../precios";

/** El precio de Tu Plan en "Recibe tu plan": sale de precios.ts y de ningún otro
 * lado (AGENTS.md, los precios viven en precios.ts). Promesas públicas del
 * 1 oct 2026: la portada no promete lo que la app no hace (el plan usa créditos
 * y solo se cobra si se entrega). */
const PLAN = PRECIOS.plan_completo;

const es = {
  meta: {
    titulo: "My Idea: transforma tu creatividad en acción",
    descripcion:
      "A los emprendedores no les faltan ideas. Les falta un interlocutor serio. Cuéntala, ordénala gratis y, cuando quieras, conviértela en un plan para ejecutarla.",
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
  comenzarGratis: "Ordena tu idea gratis",
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
      "My Idea nace de esa convicción. Construimos un motor de conocimiento que te pregunta con método y ordena lo que respondes en un plan: escucha tu contexto, adapta sus preguntas a lo que ya contaste y sabe cuándo una etapa ya quedó cubierta.",
    parrafo2:
      "El resultado no es una conversación que se pierde: es un proyecto vivo. Pausa, ejecuta en el mundo real y vuelve cuando quieras: con tu cuenta, tu idea te espera tal como la dejaste. Y si tu idea lo necesita, puedes sumarle mundos especializados, cada uno con su diagnóstico gratis.",
  },
  como: {
    titulo: "De la idea al mundo real",
    cuentameTuIdea: "Cuéntame tu idea, o en qué punto estás con ella",
    paso1: {
      titulo: "Describe tu idea",
      texto: "Escríbela tal como la tienes en mente, o díctala si tu navegador lo permite. Ese es todo el requisito.",
    },
    paso2: {
      demo: "generando…",
      titulo: "Aporta más detalles",
      texto:
        "Una entrevista que se adapta a tu idea: elige cada pregunta según lo que ya contaste y te habla en tu propio lenguaje, sin barreras técnicas.",
    },
    paso3: {
      demo: "Esta semana",
      titulo: "Recibe tu plan",
      texto:
        `Un plan detallado con etapas, experimentos y acciones concretas para ejecutarlo. Usa ${PLAN} créditos, que solo se cobran si lo recibes. Por ahora estamos en beta privada, por invitación.`,
    },
    paso4: {
      demo: "tu siguiente paso",
      titulo: "Ejecuta y regresa",
      texto:
        "Pausa, actúa en el mundo real y vuelve: marca lo que hiciste y ve tu avance. Si la realidad cambia, pide un nuevo ciclo con tus créditos y tu plan se rehace desde donde estás.",
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
      "Cinco etapas acompañan tu idea desde el primer destello hasta llevarla a la práctica. En cada una sabes dónde estás y cuál es el siguiente paso.",
  },
  descargar: {
    etiqueta: "La app",
    titulo: "Llévala en el bolsillo",
    texto: "Las mejores respuestas llegan lejos del escritorio.",
    googlePlay: "Próximamente en Google Play",
    dictar: "si tu navegador lo permite, también puedes dictarla",
  },
  cta: {
    titulo: "Aquí acaba tu idea y nace tu proyecto",
  },
  pie: {
    privacidad: "Privacidad",
    terminos: "Términos",
    cookies: "Cookies",
    preguntas: "Preguntas frecuentes",
    eliminarCuenta: "Eliminar cuenta",
    /** la tarjeta de ayuda del pie */
    preguntasDesc: "Lo que más nos preguntan, respondido en claro.",
    /** etiqueta del grupo de enlaces legales */
    legal: "Información legal",
    derechos: "© {{ano}} My Idea",
  },
};

const en: typeof es = {
  meta: {
    titulo: "My Idea: turn your creativity into action",
    descripcion:
      "Entrepreneurs don't lack ideas. What they lack is a serious sounding board. Share yours, get it organized for free and, whenever you're ready, turn it into a plan you can put to work.",
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
  comenzarGratis: "Organize your idea for free",
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
      "My Idea was born from that belief. We built a knowledge engine that asks you questions methodically and organizes your answers into a plan: it listens to your context, adapts its questions to what you've already shared, and knows when a stage is already covered.",
    parrafo2:
      "What you get isn't a conversation that fades away: it's a living project. Pause, act in the real world, and come back whenever you want: with your account, your idea waits for you just as you left it. And if your idea needs it, you can add specialized worlds, each with a free diagnosis.",
  },
  como: {
    titulo: "From idea to the real world",
    cuentameTuIdea: "Tell me your idea, or where you are with it",
    paso1: {
      titulo: "Describe your idea",
      texto: "Write it just as you picture it, or say it out loud if your browser supports it. That's all it takes.",
    },
    paso2: {
      demo: "generating…",
      titulo: "Add more detail",
      texto:
        "An interview that adapts to your idea: it picks each question based on what you've already shared and speaks your language, with no technical barriers.",
    },
    paso3: {
      demo: "This week",
      titulo: "Get your plan",
      texto:
        `A detailed plan with stages, experiments, and concrete actions to carry it out. It uses ${PLAN} credits, charged only if you receive it. For now we're in private beta, by invitation.`,
    },
    paso4: {
      demo: "your next step",
      titulo: "Act and come back",
      texto:
        "Pause, take action in the real world, and come back: check off what you've done and see your progress. If reality changes, request a new cycle with your credits and your plan is rebuilt from where you are.",
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
      "Five stages carry your idea from the first spark to putting it into practice. At every one, you know where you are and what comes next.",
  },
  descargar: {
    etiqueta: "The app",
    titulo: "Keep it in your pocket",
    texto: "The best answers come to you away from your desk.",
    googlePlay: "Coming soon to Google Play",
    dictar: "you can also say it, if your browser supports it",
  },
  cta: {
    titulo: "This is where your idea ends and your project begins",
  },
  pie: {
    privacidad: "Privacy",
    terminos: "Terms",
    cookies: "Cookies",
    preguntas: "FAQ",
    eliminarCuenta: "Delete account",
    /** la tarjeta de ayuda del pie */
    preguntasDesc: "The questions we hear most, answered plainly.",
    /** etiqueta del grupo de enlaces legales */
    legal: "Legal",
    derechos: "© {{ano}} My Idea",
  },
};

const fr: typeof es = {
  meta: {
    titulo: "My Idea : mets ta créativité en action",
    descripcion: "Les entrepreneurs ne manquent pas d'idées. Ce qui leur manque, c'est un interlocuteur sérieux. Raconte la tienne, mets-la en ordre gratuitement et, quand tu veux, transforme-la en plan pour la réaliser.",
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
  comenzarGratis: "Organise ton idée gratuitement",
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
    parrafo1: "My Idea est né de cette conviction. Nous avons construit un moteur de connaissances qui te pose des questions avec méthode et transforme tes réponses en plan : il écoute ton contexte, adapte ses questions à ce que tu as déjà raconté et sait quand une étape est déjà couverte.",
    parrafo2: "Le résultat n'est pas une conversation qui s'envole : c'est un projet vivant. Fais une pause, passe à l'action dans le monde réel et reviens quand tu veux : avec ton compte, ton idée t'attend telle que tu l'as laissée. Et si ton idée en a besoin, tu peux y ajouter des mondes spécialisés, chacun avec son diagnostic gratuit.",
  },
  como: {
    titulo: "De l'idée au monde réel",
    cuentameTuIdea: "Raconte-moi ton idée, ou où tu en es avec elle",
    paso1: {
      titulo: "Décris ton idée",
      texto: "Écris-la telle que tu l'as en tête, ou dicte-la si ton navigateur le permet. C'est tout ce qu'il faut.",
    },
    paso2: {
      demo: "génération…",
      titulo: "Ajoute des détails",
      texto: "Un entretien qui s'adapte à ton idée : il choisit chaque question selon ce que tu as déjà raconté et te parle dans tes mots, sans barrière technique.",
    },
    paso3: {
      demo: "Cette semaine",
      titulo: "Reçois ton plan",
      texto: `Un plan détaillé avec des étapes, des expériences et des actions concrètes pour le réaliser. Il utilise ${PLAN} crédits, débités seulement si tu le reçois. Pour l'instant, nous sommes en bêta privée, sur invitation.`,
    },
    paso4: {
      demo: "ton prochain pas",
      titulo: "Agis et reviens",
      texto: "Fais une pause, agis dans le monde réel et reviens : coche ce que tu as fait et vois ton avancement. Si la réalité change, demande un nouveau cycle avec tes crédits et ton plan se refait à partir de là où tu en es.",
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
    texto: "Cinq étapes accompagnent ton idée, de la première lueur jusqu'à sa mise en pratique. À chacune, tu sais où tu en es et ce qui vient ensuite.",
  },
  descargar: {
    etiqueta: "L'appli",
    titulo: "Garde-la dans ta poche",
    texto: "Les meilleures réponses arrivent loin du bureau.",
    googlePlay: "Bientôt sur Google Play",
    dictar: "tu peux aussi la dicter, si ton navigateur le permet",
  },
  cta: {
    titulo: "Ici s'achève ton idée et naît ton projet",
  },
  pie: {
    privacidad: "Confidentialité",
    terminos: "Conditions",
    cookies: "Témoins",
    preguntas: "Questions fréquentes",
    eliminarCuenta: "Supprimer le compte",
    /** la tarjeta de ayuda del pie */
    preguntasDesc: "Les questions qu'on nous pose le plus, avec des réponses claires.",
    /** etiqueta del grupo de enlaces legales */
    legal: "Mentions légales",
    derechos: "© {{ano}} My Idea",
  },
};

const pt: typeof es = {
  meta: {
    titulo: "My Idea: transforme sua criatividade em ação",
    descripcion: "Aos empreendedores não faltam ideias. Falta alguém sério do outro lado da conversa. Conte a sua, organize-a de graça e, quando quiser, transforme-a em um plano para colocá-la em prática.",
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
  comenzarGratis: "Organize sua ideia grátis",
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
    parrafo1: "O My Idea nasce dessa convicção. Construímos um motor de conhecimento que faz perguntas com método e organiza suas respostas em um plano: escuta o seu contexto, adapta as perguntas ao que você já contou e sabe quando uma etapa já ficou coberta.",
    parrafo2: "O resultado não é uma conversa que se perde: é um projeto vivo. Pause, execute no mundo real e volte quando quiser: com a sua conta, sua ideia espera por você do jeito que você deixou. E, se a sua ideia precisar, você pode somar mundos especializados, cada um com seu diagnóstico gratuito.",
  },
  como: {
    titulo: "Da ideia ao mundo real",
    cuentameTuIdea: "Me conte sua ideia, ou em que ponto você está com ela",
    paso1: {
      titulo: "Descreva sua ideia",
      texto: "Escreva do jeito que ela está na sua cabeça, ou dite se o seu navegador permitir. Esse é o único requisito.",
    },
    paso2: {
      demo: "gerando…",
      titulo: "Traga mais detalhes",
      texto: "Uma entrevista que se adapta à sua ideia: escolhe cada pergunta de acordo com o que você já contou e fala a sua língua, sem barreiras técnicas.",
    },
    paso3: {
      demo: "Esta semana",
      titulo: "Receba seu plano",
      texto: `Um plano detalhado com etapas, experimentos e ações concretas para colocá-lo em prática. Usa ${PLAN} créditos, cobrados só se você recebê-lo. Por enquanto estamos em beta privada, só com convite.`,
    },
    paso4: {
      demo: "seu próximo passo",
      titulo: "Execute e volte",
      texto: "Pause, aja no mundo real e volte: marque o que você fez e veja seu avanço. Se a realidade mudar, peça um novo ciclo com seus créditos e seu plano é refeito a partir de onde você está.",
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
    texto: "Cinco etapas acompanham sua ideia desde o primeiro lampejo até colocá-la em prática. Em cada uma, você sabe onde está e qual é o próximo passo.",
  },
  descargar: {
    etiqueta: "O app",
    titulo: "Leve no bolso",
    texto: "As melhores respostas chegam longe da mesa de trabalho.",
    googlePlay: "Em breve no Google Play",
    dictar: "se o seu navegador permitir, você também pode ditar",
  },
  cta: {
    titulo: "Aqui termina sua ideia e nasce seu projeto",
  },
  pie: {
    privacidad: "Privacidade",
    terminos: "Termos",
    cookies: "Cookies",
    preguntas: "Perguntas frequentes",
    eliminarCuenta: "Excluir conta",
    /** la tarjeta de ayuda del pie */
    preguntasDesc: "O que mais nos perguntam, respondido com clareza.",
    /** etiqueta del grupo de enlaces legales */
    legal: "Informações legais",
    derechos: "© {{ano}} My Idea",
  },
};

const de: typeof es = {
  meta: {
    titulo: "My Idea: Verwandle deine Kreativität in Taten",
    descripcion: "Wer etwas gründen will, hat genug Ideen. Was fehlt, ist ein Gegenüber, das sie ernst nimmt. Erzähl deine Idee, ordne sie kostenlos und mach daraus, wann immer du willst, einen Plan zur Umsetzung.",
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
  comenzarGratis: "Ordne deine Idee kostenlos",
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
    parrafo1: "My Idea ist aus dieser Überzeugung entstanden. Wir haben ein Wissenssystem gebaut, das dir mit Methode Fragen stellt und deine Antworten zu einem Plan ordnet: Es hört auf deine Situation, passt seine Fragen an das an, was du schon erzählt hast, und merkt, wann eine Etappe schon abgedeckt ist.",
    parrafo2: "Am Ende steht kein Gespräch, das verloren geht, sondern ein lebendiges Projekt. Mach Pause, handle in der echten Welt und komm zurück, wann du willst: Mit deinem Konto wartet deine Idee genau so auf dich, wie du sie verlassen hast. Und wenn deine Idee es braucht, kannst du spezialisierte Welten hinzufügen, jede mit ihrer kostenlosen Diagnose.",
  },
  como: {
    titulo: "Von der Idee in die echte Welt",
    cuentameTuIdea: "Erzähl mir deine Idee oder wo du damit gerade stehst",
    paso1: {
      titulo: "Beschreib deine Idee",
      texto: "Schreib sie auf, so wie du sie im Kopf hast, oder sprich sie ein, wenn dein Browser das unterstützt. Mehr braucht es nicht.",
    },
    paso2: {
      demo: "wird erstellt…",
      titulo: "Erzähl mehr",
      texto: "Ein Gespräch, das sich deiner Idee anpasst: Es wählt jede Frage nach dem, was du schon erzählt hast, und spricht deine Sprache, ganz ohne technische Hürden.",
    },
    paso3: {
      demo: "Diese Woche",
      titulo: "Hol dir deinen Plan",
      texto: `Ein detaillierter Plan mit Etappen, Experimenten und konkreten Schritten zur Umsetzung. Er kostet ${PLAN} Punkte, die nur abgebucht werden, wenn du ihn erhältst. Im Moment sind wir in einer privaten Beta, nur auf Einladung.`,
    },
    paso4: {
      demo: "dein nächster Schritt",
      titulo: "Setz um und komm zurück",
      texto: "Mach Pause, handle in der echten Welt und komm zurück: Hak ab, was du erledigt hast, und sieh deinen Fortschritt. Wenn sich die Wirklichkeit ändert, fordere mit deinen Punkten einen neuen Zyklus an, und dein Plan wird von deinem jetzigen Stand aus neu erstellt.",
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
    texto: "Fünf Etappen begleiten deine Idee vom ersten Funken, bis du sie in die Praxis umsetzt. In jeder weißt du, wo du stehst und was als Nächstes kommt.",
  },
  descargar: {
    etiqueta: "Die App",
    titulo: "Immer in deiner Tasche",
    texto: "Die besten Antworten kommen dir fern vom Schreibtisch.",
    googlePlay: "Demnächst bei Google Play",
    dictar: "wenn dein Browser es unterstützt, kannst du sie auch einsprechen",
  },
  cta: {
    titulo: "Hier endet deine Idee und beginnt dein Projekt",
  },
  pie: {
    privacidad: "Datenschutz",
    terminos: "Nutzungsbedingungen",
    cookies: "Cookies",
    preguntas: "Häufige Fragen",
    eliminarCuenta: "Konto löschen",
    /** la tarjeta de ayuda del pie */
    preguntasDesc: "Was uns am häufigsten gefragt wird, klar beantwortet.",
    /** etiqueta del grupo de enlaces legales */
    legal: "Rechtliches",
    derechos: "© {{ano}} My Idea",
  },
};

const it: typeof es = {
  meta: {
    titulo: "My Idea: trasforma la tua creatività in azione",
    descripcion: "Agli imprenditori non mancano le idee. Manca un interlocutore serio. Racconta la tua, mettila in ordine gratis e, quando vuoi, trasformala in un piano da mettere in pratica.",
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
  comenzarGratis: "Organizza la tua idea gratis",
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
    parrafo1: "My Idea nasce da questa convinzione. Abbiamo costruito un motore di conoscenza che ti fa domande con metodo e mette in ordine le tue risposte in un piano: ascolta il tuo contesto, adatta le domande a quello che hai già raccontato e capisce quando una tappa è già coperta.",
    parrafo2: "Il risultato non è una conversazione che si perde: è un progetto vivo. Fermati, agisci nel mondo reale e torna quando vuoi: con il tuo account, la tua idea ti aspetta così come l'hai lasciata. E se la tua idea ne ha bisogno, puoi aggiungere mondi specializzati, ognuno con la sua diagnosi gratuita.",
  },
  como: {
    titulo: "Dall'idea al mondo reale",
    cuentameTuIdea: "Raccontami la tua idea, o a che punto sei",
    paso1: {
      titulo: "Descrivi la tua idea",
      texto: "Scrivila così come ce l'hai in testa, o dettala se il tuo browser lo consente. Non serve altro.",
    },
    paso2: {
      demo: "in generazione…",
      titulo: "Aggiungi dettagli",
      texto: "Un'intervista che si adatta alla tua idea: sceglie ogni domanda in base a quello che hai già raccontato e ti parla con parole tue, senza barriere tecniche.",
    },
    paso3: {
      demo: "Questa settimana",
      titulo: "Ricevi il tuo piano",
      texto: `Un piano dettagliato con tappe, esperimenti e azioni concrete per metterlo in pratica. Usa ${PLAN} crediti, addebitati solo se lo ricevi. Per ora siamo in beta privata, su invito.`,
    },
    paso4: {
      demo: "il tuo prossimo passo",
      titulo: "Agisci e torna",
      texto: "Fermati, agisci nel mondo reale e torna: segna quello che hai fatto e guarda i tuoi progressi. Se la realtà cambia, chiedi un nuovo ciclo con i tuoi crediti e il tuo piano si rifà da dove sei.",
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
    texto: "Cinque tappe accompagnano la tua idea dalla prima intuizione fino a metterla in pratica. In ognuna sai dove sei e qual è il passo successivo.",
  },
  descargar: {
    etiqueta: "L'app",
    titulo: "Portala sempre con te",
    texto: "Le risposte migliori arrivano lontano dalla scrivania.",
    googlePlay: "Presto su Google Play",
    dictar: "se il tuo browser lo consente, puoi anche dettarla",
  },
  cta: {
    titulo: "Qui finisce la tua idea e nasce il tuo progetto",
  },
  pie: {
    privacidad: "Privacy",
    terminos: "Termini",
    cookies: "Cookie",
    preguntas: "Domande frequenti",
    eliminarCuenta: "Elimina account",
    /** la tarjeta de ayuda del pie */
    preguntasDesc: "Le domande che ci fanno più spesso, con risposte chiare.",
    /** etiqueta del grupo de enlaces legales */
    legal: "Note legali",
    derechos: "© {{ano}} My Idea",
  },
};

const ja: typeof es = {
  meta: {
    titulo: "My Idea：あなたの創造力を、行動に変える",
    descripcion: "起業家に足りないのは、アイデアではありません。真剣に向き合ってくれる相手です。アイデアを話して、無料で整理し、準備ができたら、実行するためのプランに変えましょう。",
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
  comenzarGratis: "無料でアイデアを整理する",
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
    parrafo1: "My Ideaは、その確信から生まれました。私たちがつくったのは、筋道を立てて問いかけ、あなたの答えをプランへと整理するナレッジエンジンです。あなたの状況に耳を傾け、すでに話した内容に合わせて質問を変え、ステージがもう満たされたかどうかを見極めます。",
    parrafo2: "手元に残るのは、流れて消えていく会話ではありません。動き続けるプロジェクトです。一度止めて、現実の世界で動き、いつでも戻ってきてください。アカウントがあれば、アイデアは離れたときのままあなたを待っています。アイデアに必要なら、専門のワールドを追加することもできます。どのワールドも診断は無料です。",
  },
  como: {
    titulo: "アイデアを、現実の世界へ",
    cuentameTuIdea: "アイデアを聞かせてください。今どこまで進んでいるかでもかまいません",
    paso1: {
      titulo: "アイデアを伝える",
      texto: "頭の中にあるままを書くか、ブラウザが対応していれば話すだけ。必要なのはそれだけです。",
    },
    paso2: {
      demo: "生成中…",
      titulo: "詳しく話す",
      texto: "アイデアに合わせて変わるインタビューです。すでに話した内容をもとに質問を一つずつ選び、専門用語の壁なしに、あなたの言葉で語りかけます。",
    },
    paso3: {
      demo: "今週",
      titulo: "プランを受け取る",
      texto: `ステージ、実験、実行のための具体的なアクションまでそろった、詳しいプラン。${PLAN}ポイントを使いますが、消費されるのはプランを受け取ったときだけです。現在は招待制のプライベートベータです。`,
    },
    paso4: {
      demo: "あなたの次の一歩",
      titulo: "実行して、戻ってくる",
      texto: "一度止めて、現実の世界で動いて、戻ってくる。やったことに印をつけて、進み具合を確かめましょう。状況が変わったら、ポイントで新しいサイクルを依頼すると、今いる地点からプランを作り直します。",
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
    texto: "最初のひらめきから実践に移すその日まで、5つのステージがあなたのアイデアに寄り添います。どのステージでも、今どこにいて、次に何をすればいいかがわかります。",
  },
  descargar: {
    etiqueta: "アプリ",
    titulo: "いつもポケットの中に",
    texto: "いい答えは、机を離れたときに浮かぶものです。",
    googlePlay: "Google Playで近日公開",
    dictar: "ブラウザが対応していれば、話して入力することもできます",
  },
  cta: {
    titulo: "ここでアイデアは終わり、プロジェクトが生まれます",
  },
  pie: {
    privacidad: "プライバシー",
    terminos: "利用規約",
    cookies: "Cookie",
    preguntas: "よくある質問",
    eliminarCuenta: "アカウント削除",
    /** la tarjeta de ayuda del pie */
    preguntasDesc: "よくいただく質問に、わかりやすくお答えします。",
    /** etiqueta del grupo de enlaces legales */
    legal: "法的情報",
    derechos: "© {{ano}} My Idea",
  },
};

const zh: typeof es = {
  meta: {
    titulo: "My Idea：把你的创意变成行动",
    descripcion: "创业者从不缺想法，缺的是一个认真的对话者。说出你的想法，免费把它理清，等你准备好了，再把它变成一份可以执行的计划。",
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
  comenzarGratis: "免费理清你的想法",
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
    parrafo1: "My Idea 正是从这个信念中诞生的。我们打造了一个知识引擎：它有条理地向你提问，把你的回答整理成一份计划。它倾听你的具体情况，根据你已经讲过的内容调整问题，也知道某个阶段什么时候已经覆盖了。",
    parrafo2: "你得到的不是一段聊完就散的对话，而是一个持续生长的项目。你可以暂停，去现实中行动，随时回来：有了账户，你的想法会原样等着你。如果你的想法需要，还可以加入专业的世界，每个世界的诊断都是免费的。",
  },
  como: {
    titulo: "从想法到现实",
    cuentameTuIdea: "跟我说说你的想法，或者你现在走到哪一步了",
    paso1: {
      titulo: "描述你的想法",
      texto: "按你脑海中的样子写下来；如果你的浏览器支持，也可以直接说出来。这就是全部要求。",
    },
    paso2: {
      demo: "生成中…",
      titulo: "补充更多细节",
      texto: "一场随你的想法调整的访谈：它根据你已经讲过的内容挑选每一个问题，用你自己的语言和你交流，没有任何技术门槛。",
    },
    paso3: {
      demo: "本周",
      titulo: "拿到你的计划",
      texto: `一份详细的计划，包含阶段、实验和具体行动，帮你把它落地。它需要${PLAN}点，只有在你收到计划时才会扣除。目前处于邀请制内测阶段。`,
    },
    paso4: {
      demo: "你的下一步",
      titulo: "去执行，再回来",
      texto: "暂停，去现实中行动，再回来：勾选你完成的事，看看自己的进展。如果现实发生变化，用你的点数申请一个新的循环，计划就会根据你目前的进度重新制定。",
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
    texto: "五个阶段陪伴你的想法，从最初的灵光一现，一直到把它付诸实践。每个阶段，你都清楚自己在哪里、下一步是什么。",
  },
  descargar: {
    etiqueta: "应用",
    titulo: "把它装进口袋",
    texto: "最好的答案，往往在你离开办公桌时出现。",
    googlePlay: "即将登陆 Google Play",
    dictar: "如果浏览器支持，也可以直接说出来",
  },
  cta: {
    titulo: "你的想法在这里圆满，你的项目从这里启程",
  },
  pie: {
    privacidad: "隐私",
    terminos: "条款",
    cookies: "Cookie",
    preguntas: "常见问题",
    eliminarCuenta: "删除账户",
    /** la tarjeta de ayuda del pie */
    preguntasDesc: "大家最常问的问题，清楚作答。",
    /** etiqueta del grupo de enlaces legales */
    legal: "法律信息",
    derechos: "© {{ano}} My Idea",
  },
};

const ko: typeof es = {
  meta: {
    titulo: "My Idea: 창의력을 실행으로 바꿔 보세요",
    descripcion: "창업가에게 부족한 건 아이디어가 아니에요. 진지하게 함께 고민해 줄 상대예요. 아이디어를 들려주고, 무료로 정리한 다음, 원할 때 실행할 수 있는 계획으로 바꿔 보세요.",
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
  comenzarGratis: "무료로 아이디어 정리하기",
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
    parrafo1: "My Idea는 바로 이 믿음에서 시작했어요. 체계적으로 질문하고, 답한 내용을 계획으로 정리하는 지식 엔진을 만들었어요. 상황에 귀 기울이고, 이미 들려준 이야기에 맞춰 질문을 바꾸며, 어떤 단계가 이미 채워졌는지 알아차려요.",
    parrafo2: "그 결과는 흘러가 버리는 대화가 아니라 살아 있는 프로젝트예요. 잠시 멈추고, 현실에서 실행하고, 언제든 돌아오세요. 계정이 있으면 아이디어가 두고 간 모습 그대로 기다리고 있어요. 아이디어에 필요하면 전문 월드를 더할 수도 있어요. 월드마다 진단은 무료예요.",
  },
  como: {
    titulo: "아이디어에서 현실로",
    cuentameTuIdea: "아이디어를 들려주세요. 지금 어디까지 왔는지도요",
    paso1: {
      titulo: "아이디어를 들려주세요",
      texto: "머릿속에 있는 그대로 쓰거나, 브라우저가 지원하면 말로 하세요. 필요한 건 그게 전부예요.",
    },
    paso2: {
      demo: "생성하는 중…",
      titulo: "조금 더 자세히 알려 주세요",
      texto: "아이디어에 맞춰 달라지는 인터뷰예요. 이미 들려준 이야기를 바탕으로 질문을 하나하나 고르고, 어려운 전문 용어 없이 내 언어로 말을 걸어요.",
    },
    paso3: {
      demo: "이번 주",
      titulo: "계획을 받아 보세요",
      texto: `단계, 실험, 구체적인 실행 항목까지 담은 상세한 계획이에요. ${PLAN}크레딧이 들고, 계획을 받았을 때만 차감돼요. 지금은 초대받은 분만 쓸 수 있는 비공개 베타예요.`,
    },
    paso4: {
      demo: "나의 다음 단계",
      titulo: "실행하고 돌아오세요",
      texto: "잠시 멈추고, 현실에서 움직인 뒤 돌아오세요. 한 일을 표시하고 진행 상황을 확인해요. 상황이 바뀌면 크레딧으로 새 사이클을 요청하세요. 지금 있는 지점부터 계획을 다시 짜 드려요.",
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
    texto: "첫 번째 불꽃부터 실제로 실행에 옮기기까지, 다섯 단계가 아이디어와 함께해요. 단계마다 지금 어디에 있고 다음에 무엇을 할지 알 수 있어요.",
  },
  descargar: {
    etiqueta: "앱",
    titulo: "주머니 속에 넣고 다니세요",
    texto: "가장 좋은 답은 책상에서 멀리 떨어져 있을 때 떠올라요.",
    googlePlay: "Google Play 출시 예정",
    dictar: "브라우저가 지원하면 말로 해도 돼요",
  },
  cta: {
    titulo: "여기서 아이디어가 끝나고 프로젝트가 태어나요",
  },
  pie: {
    privacidad: "개인정보 처리방침",
    terminos: "이용약관",
    cookies: "쿠키",
    preguntas: "자주 묻는 질문",
    eliminarCuenta: "계정 삭제",
    /** la tarjeta de ayuda del pie */
    preguntasDesc: "가장 많이 받는 질문에 쉽게 답해 드립니다.",
    /** etiqueta del grupo de enlaces legales */
    legal: "법적 고지",
    derechos: "© {{ano}} My Idea",
  },
};

const ar: typeof es = {
  meta: {
    titulo: "My Idea: حوّلوا إبداعكم إلى فعل",
    descripcion: "رواد الأعمال لا تنقصهم الأفكار، بل ينقصهم محاور جادّ. احكوا لنا فكرتكم، ورتّبوها مجانًا، ومتى شئتم حوّلوها إلى خطة لتنفيذها.",
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
  comenzarGratis: "رتّبوا فكرتكم مجانًا",
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
    parrafo1: "من هذه القناعة وُلدت My Idea. بنينا محرّك معرفة يطرح عليكم الأسئلة بمنهج، وينظّم إجاباتكم في خطة: يصغي إلى سياقكم، ويكيّف أسئلته مع ما رويتموه، ويعرف متى صارت مرحلة ما مغطّاة.",
    parrafo2: "النتيجة ليست محادثة تضيع، بل مشروع حيّ. توقّفوا، ونفّذوا في العالم الحقيقي، وعودوا متى شئتم: مع حسابكم، تنتظركم فكرتكم كما تركتموها. وإن احتاجت فكرتكم ذلك، يمكنكم إضافة عوالم متخصّصة، ولكلّ منها تشخيص مجاني.",
  },
  como: {
    titulo: "من الفكرة إلى العالم الحقيقي",
    cuentameTuIdea: "احكوا لي فكرتكم، أو إلى أين وصلتم بها",
    paso1: {
      titulo: "صِفوا فكرتكم",
      texto: "اكتبوها كما هي في أذهانكم، أو أملوها إن كان متصفّحكم يتيح ذلك. هذا كل المطلوب.",
    },
    paso2: {
      demo: "جارٍ الإنشاء…",
      titulo: "أضيفوا تفاصيل أكثر",
      texto: "مقابلة تتكيّف مع فكرتكم: تختار كل سؤال بناءً على ما رويتموه، وتخاطبكم بلغتكم أنتم، بلا حواجز تقنية.",
    },
    paso3: {
      demo: "هذا الأسبوع",
      titulo: "احصلوا على خطتكم",
      texto: `خطة مفصّلة بمراحل وتجارب وإجراءات ملموسة لتنفيذها. تستخدم ${PLAN} من النقاط، ولا تُخصم إلا إذا استلمتموها. نحن الآن في نسخة تجريبية خاصة، بالدعوة فقط.`,
    },
    paso4: {
      demo: "خطوتكم التالية",
      titulo: "نفّذوا وعودوا",
      texto: "توقّفوا، واعملوا في العالم الحقيقي، ثم عودوا: علّموا ما أنجزتموه وتابعوا تقدّمكم. وإن تغيّر الواقع، اطلبوا دورة جديدة بنقاطكم، فيُعاد بناء خطتكم من حيث أنتم.",
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
    texto: "خمس مراحل ترافق فكرتكم من أول ومضة حتى تضعوها موضع التطبيق. في كل منها تعرفون أين أنتم وما الخطوة التالية.",
  },
  descargar: {
    etiqueta: "التطبيق",
    titulo: "احملوه في جيبكم",
    texto: "أفضل الإجابات تأتي بعيدًا عن المكتب.",
    googlePlay: "قريبًا على Google Play",
    dictar: "ويمكنكم أيضًا إملاؤها إن كان متصفّحكم يتيح ذلك",
  },
  cta: {
    titulo: "هنا تنتهي فكرتكم ويولد مشروعكم",
  },
  pie: {
    privacidad: "الخصوصية",
    terminos: "الشروط",
    cookies: "ملفات تعريف الارتباط",
    preguntas: "الأسئلة الشائعة",
    eliminarCuenta: "حذف الحساب",
    /** la tarjeta de ayuda del pie */
    preguntasDesc: "أكثر ما يسألنا عنه الناس، بإجابات واضحة.",
    /** etiqueta del grupo de enlaces legales */
    legal: "معلومات قانونية",
    derechos: "© {{ano}} My Idea",
  },
};

const hi: typeof es = {
  meta: {
    titulo: "My Idea: अपनी रचनात्मकता को अमल में लाएँ",
    descripcion: "उद्यमियों के पास विचारों की कमी नहीं होती। कमी होती है ऐसे साथी की जो उनकी बात गंभीरता से ले। अपना विचार बताएँ, उसे मुफ़्त में व्यवस्थित करें और जब चाहें, उसे अमल में लाने की योजना में बदलें।",
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
  comenzarGratis: "अपना विचार मुफ़्त में व्यवस्थित करें",
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
    parrafo1: "My Idea इसी सोच से जन्मा है। हमने एक ज्ञान इंजन बनाया है जो तरीके से सवाल पूछता है और आपके जवाबों को एक योजना में व्यवस्थित करता है: यह आपकी पूरी स्थिति सुनता है, आपकी बताई बातों के हिसाब से अपने सवाल ढालता है, और समझता है कि कोई चरण कब पूरा हो चुका है।",
    parrafo2: "नतीजा कोई ऐसी बातचीत नहीं जो कहीं खो जाए: यह एक जीवंत परियोजना है। रुकें, असल दुनिया में काम करें और जब चाहें लौट आएँ: आपके खाते में आपका विचार वैसा ही आपका इंतज़ार करता है जैसा आपने छोड़ा था। और अगर आपके विचार को ज़रूरत हो, तो आप खास दुनियाएँ जोड़ सकते हैं, हर एक का आकलन मुफ़्त है।",
  },
  como: {
    titulo: "विचार से असल दुनिया तक",
    cuentameTuIdea: "मुझे अपना विचार बताएँ, या यह कि वह अभी किस मोड़ पर है",
    paso1: {
      titulo: "अपना विचार बताएँ",
      texto: "इसे वैसे ही लिखें जैसे यह आपके मन में है, या आपका ब्राउज़र सपोर्ट करे तो बोलकर लिखवाएँ। बस इतना ही चाहिए।",
    },
    paso2: {
      demo: "बन रहा है…",
      titulo: "और जानकारी दें",
      texto: "एक बातचीत जो आपके विचार के हिसाब से ढलती है: यह आपकी बताई बातों के आधार पर हर सवाल चुनती है और आपकी अपनी भाषा में बात करती है, बिना किसी तकनीकी रुकावट के।",
    },
    paso3: {
      demo: "इस हफ़्ते",
      titulo: "अपनी योजना पाएँ",
      texto: `चरणों, प्रयोगों और ठोस कदमों वाली एक विस्तृत योजना, जिस पर आप अमल कर सकें। इसमें ${PLAN} क्रेडिट लगते हैं, जो तभी कटते हैं जब योजना आपको मिल जाए। अभी हम निजी बीटा में हैं, सिर्फ़ न्योते पर।`,
    },
    paso4: {
      demo: "आपका अगला कदम",
      titulo: "अमल करें और लौटें",
      texto: "रुकें, असल दुनिया में कदम उठाएँ और लौट आएँ: जो किया उस पर निशान लगाएँ और अपनी प्रगति देखें। अगर हालात बदलें, तो अपने क्रेडिट से नया चक्र माँगें, और आपकी योजना वहीं से दोबारा बनती है जहाँ आप हैं।",
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
    texto: "पाँच चरण आपके विचार के साथ चलते हैं, पहली चमक से लेकर उसे अमल में लाने तक। हर चरण में आपको पता रहता है कि आप कहाँ हैं और अगला कदम क्या है।",
  },
  descargar: {
    etiqueta: "ऐप",
    titulo: "इसे अपनी जेब में रखें",
    texto: "सबसे अच्छे जवाब अक्सर डेस्क से दूर सूझते हैं।",
    googlePlay: "जल्द ही Google Play पर",
    dictar: "ब्राउज़र सपोर्ट करे तो इसे बोलकर भी लिखवाया जा सकता है",
  },
  cta: {
    titulo: "यहाँ आपका विचार पूरा होता है और आपकी परियोजना जन्म लेती है",
  },
  pie: {
    privacidad: "गोपनीयता",
    terminos: "शर्तें",
    cookies: "कुकीज़",
    preguntas: "अक्सर पूछे जाने वाले प्रश्न",
    eliminarCuenta: "खाता हटाएँ",
    /** la tarjeta de ayuda del pie */
    preguntasDesc: "जो सबसे ज़्यादा पूछा जाता है, उसके साफ़ जवाब।",
    /** etiqueta del grupo de enlaces legales */
    legal: "कानूनी जानकारी",
    derechos: "© {{ano}} My Idea",
  },
};

export const PORTADA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
