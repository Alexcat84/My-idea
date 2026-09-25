/** "Mis ideas" (/ideas, app/ideas/page.tsx) y las cintas que arma lib/ideas.ts:
 * chips de estado, pistas, el resumen de las realizadas y haceCuanto(). */
import type { PorIdioma } from "../config";

const es = {
  tuCuenta: "Tu cuenta",
  vacioTitulo: "Tus ideas esperan por ti",
  vacioTexto: "Aún no has guardado ninguna. Cuéntame la primera, lo que sea y como te salga, y la trabajamos juntos, paso a paso.",
  iniciarNuevaIdea: "Iniciar nueva idea",
  capturaRapida: "Cuéntame una idea nueva, o en qué punto estás con ella…",
  tusIdeas: "Tus ideas · {{n}}",
  realizadas: "Realizadas · {{n}}",
  proyecto: "Proyecto",
  potenciarTitulo: "Potenciar mis ideas",
  potenciarTexto: "Tus Números y los mundos, para la idea que elijas.",
  cintas: {
    manosALaObra: "Manos a la Obra · {{hechos}}/{{total}}",
    mundoProgreso: "{{mundo}} · {{hechos}}/{{total}}",
    enExploracion: "En exploración",
    conPlan: "Con plan",
    conClaridad: "Con claridad",
    sinOrdenar: "Sin ordenar",
    pistaPlanListo: "Tu plan está listo para armarse · última acción {{fecha}}",
    pistaPregunta: "Una pregunta te espera · última acción {{fecha}}",
    pistaUltimaAccion: "última acción · {{fecha}}",
    resumenRealizada: {
      one: "realizada {{fecha}} · {{dias}} día de la chispa al proyecto",
      other: "realizada {{fecha}} · {{dias}} días de la chispa al proyecto",
    },
  },
  haceCuanto: {
    ahoraMismo: "ahora mismo",
    haceMin: "hace {{n}} min",
    haceHoras: "hace {{n}} h",
    ayer: "ayer",
    haceDias: "hace {{n}} días",
    haceUnMes: "hace un mes",
    haceMeses: "hace {{n}} meses",
  },
};

const en: typeof es = {
  tuCuenta: "Your account",
  vacioTitulo: "Your ideas are waiting for you",
  vacioTexto: "You haven't saved any yet. Tell me your first one, whatever it is and however it comes out, and we'll work on it together, step by step.",
  iniciarNuevaIdea: "Start a new idea",
  capturaRapida: "Tell me a new idea, or where you're at with it…",
  tusIdeas: "Your ideas · {{n}}",
  realizadas: "Achieved · {{n}}",
  proyecto: "Project",
  potenciarTitulo: "Power up my ideas",
  potenciarTexto: "Your Numbers and the worlds, for whichever idea you choose.",
  cintas: {
    manosALaObra: "Get to Work · {{hechos}}/{{total}}",
    mundoProgreso: "{{mundo}} · {{hechos}}/{{total}}",
    enExploracion: "Exploring",
    conPlan: "Has a plan",
    conClaridad: "Has clarity",
    sinOrdenar: "Unsorted",
    pistaPlanListo: "Your plan is ready to be built · last activity {{fecha}}",
    pistaPregunta: "A question is waiting for you · last activity {{fecha}}",
    pistaUltimaAccion: "last activity · {{fecha}}",
    resumenRealizada: {
      one: "achieved {{fecha}} · {{dias}} day from spark to project",
      other: "achieved {{fecha}} · {{dias}} days from spark to project",
    },
  },
  haceCuanto: {
    ahoraMismo: "just now",
    haceMin: "{{n}} min ago",
    haceHoras: "{{n}} h ago",
    ayer: "yesterday",
    haceDias: "{{n}} days ago",
    haceUnMes: "a month ago",
    haceMeses: "{{n}} months ago",
  },
};

export const MIS_IDEAS: PorIdioma<typeof es> = { es, en };
