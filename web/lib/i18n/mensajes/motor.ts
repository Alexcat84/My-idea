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

export const MOTOR: PorIdioma<typeof es> = { es, en };
