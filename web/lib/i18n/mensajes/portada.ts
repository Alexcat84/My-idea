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

export const PORTADA: PorIdioma<typeof es> = { es, en };
