/** El panel "Tus documentos" (app/ui/Descargas.tsx): la lista de descargas en
 * .md y PDF de cada fase del viaje, el Expediente y los reportes por mundo. */
import type { PorIdioma } from "../config";

const es = {
  preparando: "Preparando…",
  errorCargar: "No pudimos cargar tus documentos. Vuelve a intentarlo en un momento.",
  errorPreparar: "No pudimos preparar ese documento. Vuelve a intentarlo en un momento.",
  esteMundo: "este mundo",
  tuViaje: "Tu viaje",
  cerradoEl: "Cerrado el {{fecha}}",
  volver: "← Volver",
  documentosDe: "Documentos de {{espacio}}",
  tusDocumentos: "Tus documentos",
  descripcionMundo: "Los documentos de este mundo: su reporte y lo que deje cada fase de su camino, en .md o en PDF.",
  descripcion:
    "Cada fase de tu camino deja su propio documento. Llévatelos en .md para editarlos o en PDF para leerlos e imprimirlos.",
  cargando: "Cargando…",
  reportesGlobales: "Reportes globales",
  global: "Global",
  sinExpediente: "Tu expediente completo aparecerá aquí cuando tengas tu plan.",
  reportesDe: "Reportes de {{espacio}}",
  sinDocumentosMundo: "Este mundo todavía no tiene documentos propios. Cuando genere su reporte, aparecerá aquí.",
  sinDocumentosViaje: "Aún no hay documentos de tu viaje principal. Cuando tengas tu plan, aparecerán aquí.",
  sinNada: "Todavía no hay nada que descargar. Cuando tengas tu plan, aparecerá aquí.",
  cierreLista:
    "El .md y el PDF salen del mismo texto: lo que lees aquí es lo que se imprime. Tu bitácora en vivo se abre desde el plan, desde Manos a la Obra y desde tus mundos.",
  /** el rótulo del pie de página del Expediente impreso */
  pieExpediente: "Expediente",
  expedienteCompleto: "Expediente completo",
};

export const DESCARGAS: PorIdioma<typeof es> = { es };
