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
    'Pensando en "{{titulo}}", cuentame en tus palabras donde estas parado ahora mismo con tu idea y que es lo que mas te preocupa o te entusiasma.',
  /** recorrido.ts: el nombre humano de una familia cuando la brújula no responde. */
  temaFamilia: {
    accionClientes: "Salir a validar con clientes",
    viabilidadEconomica: "Tus numeros de verdad",
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

export const MOTOR: PorIdioma<typeof es> = { es };
