/** Los hitos de un espacio (lib/hitosEspacio.ts, la cara "Tu avance") y el mapa
 * horizontal de hitos del Análisis (MapaHitos). */
import type { PorIdioma } from "../config";

const es = {
  core: {
    chispa: "La Chispa",
    chispaSub: "La idea nace",
    claridad: "Claridad",
    claridadSub: "Tu idea, organizada",
    plan: "Tu Plan",
    planSub: "Tu plan de acción, listo",
    realizada: "Realizada",
    realizadaSub: "Aquí nace tu proyecto",
    cierre: "El cierre",
    cierreSub: "Cuando lo sientas real",
  },
  mundo: {
    diagnostico: "Tu diagnóstico",
    diagnosticoSub: "El primer vistazo de este frente",
    plan: "El plan de {{mundo}}",
    planSub: "Listo para ejecutar",
    cerrado: "Cerrado",
    cerradoSub: "Diste este frente por terminado",
    cierre: "El cierre",
    cierreSub: "Cuando lo des por terminado",
  },
  mapa: {
    titulo: "Tus hitos, de un vistazo",
    nota: "Un paso por hito, en el orden en que ocurrieron. Las distancias reales entre fechas viven en la línea de abajo.",
    /** abreviaturas de los meses, de enero a diciembre (la fecha del mapa: "3 feb") */
    meses: ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"],
    /** la fecha corta: "3 feb" (i18n F3: el orden lo pone cada idioma) */
    fechaCorta: "{{d}} {{mes}}",
  },
};

const en: typeof es = {
  core: {
    chispa: "The Spark",
    chispaSub: "The idea is born",
    claridad: "Clarity",
    claridadSub: "Your idea, organized",
    plan: "Your Plan",
    planSub: "Your action plan, ready",
    realizada: "Achieved",
    realizadaSub: "This is where your project is born",
    cierre: "The close",
    cierreSub: "When it feels real",
  },
  mundo: {
    diagnostico: "Your diagnosis",
    diagnosticoSub: "A first look at this area",
    plan: "The {{mundo}} plan",
    planSub: "Ready to put into action",
    cerrado: "Closed",
    cerradoSub: "You called this area done",
    cierre: "The close",
    cierreSub: "When you call it done",
  },
  mapa: {
    titulo: "Your milestones at a glance",
    nota: "One step per milestone, in the order they happened. The real distances between dates live in the line below.",
    meses: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    fechaCorta: "{{mes}} {{d}}",
  },
};

export const HITOS: PorIdioma<typeof es> = { es, en };
