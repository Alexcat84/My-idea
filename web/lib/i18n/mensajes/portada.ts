/** La portada pública ("/"): ui/Landing.tsx y los metadatos de app/page.tsx. */
import type { PorIdioma } from "../config";

const es = {
  meta: {
    titulo: "My Idea: Transforma tu creatividad en acción",
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
    categoria: "Calidad y Diseño en el MVP",
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
    derechos: "© 2026 My Idea",
  },
};

export const PORTADA: PorIdioma<typeof es> = { es };
