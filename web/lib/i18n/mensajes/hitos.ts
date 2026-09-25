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
  },
};

export const HITOS: PorIdioma<typeof es> = { es };
