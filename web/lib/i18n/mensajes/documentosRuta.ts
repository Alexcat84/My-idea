/** GET /api/project/[id]/documentos: títulos, nombres de archivo y textos que la ruta arma para los documentos. */
import type { PorIdioma } from "../config";

const es = {
  noEncontrado: "documento no encontrado",
  noPudimosLeerRegistro: "no pudimos leer tu registro; intenta de nuevo en un momento",
  tituloReporte: "Reporte de {{mundo}}",
  tituloRegistro: "Registro de {{mundo}}",
  encabezadoRegistro: "> {{nombre}} · Registro de {{mundo}} · {{fecha}}",
  tituloBitacora: "Tu bitácora",
  archivoBitacora: "Tu bitacora",
  tituloAnalisis: "Análisis del proyecto",
  archivoAnalisis: "Análisis del proyecto",
  tituloExpediente: "Expediente completo",
  hitoRealizado: "Realizado",
  loQuePendiente: {
    one: "Queda {{n}} acción por delante. Nada se borró: sigue en tu expediente.",
    other: "Quedan {{n}} acciones por delante. Nada se borró: siguen en tu expediente.",
  },
  loQuePendienteConRetiradas: {
    one: "Queda {{n}} acción por delante y {{retiradas}} que retiraste con su motivo. Nada se borró: siguen en tu expediente.",
    other: "Quedan {{n}} acciones por delante y {{retiradas}} que retiraste con su motivo. Nada se borró: siguen en tu expediente.",
  },
};

export const DOCUMENTOS_RUTA: PorIdioma<typeof es> = { es };
