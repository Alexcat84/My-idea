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

const en: typeof es = {
  preparando: "Preparing…",
  errorCargar: "We couldn't load your documents. Try again in a moment.",
  errorPreparar: "We couldn't prepare that document. Try again in a moment.",
  esteMundo: "this world",
  tuViaje: "Your Journey",
  cerradoEl: "Closed on {{fecha}}",
  volver: "← Back",
  documentosDe: "Documents for {{espacio}}",
  tusDocumentos: "Your documents",
  descripcionMundo: "This world's documents: its report and whatever each phase of its path leaves behind, as .md or PDF.",
  descripcion:
    "Each phase of your path leaves its own document. Take them as .md to edit them or as PDF to read and print them.",
  cargando: "Loading…",
  reportesGlobales: "Overall reports",
  global: "Overall",
  sinExpediente: "Your Full Record will show up here once you have your plan.",
  reportesDe: "Reports for {{espacio}}",
  sinDocumentosMundo: "This world doesn't have its own documents yet. Once its report is generated, it'll show up here.",
  sinDocumentosViaje: "There are no documents from your main journey yet. Once you have your plan, they'll show up here.",
  sinNada: "There's nothing to download yet. Once you have your plan, it'll show up here.",
  cierreLista:
    "The .md and the PDF come from the same text: what you read here is what gets printed. Your live Logbook opens from the plan, from Get to Work, and from your worlds.",
  pieExpediente: "Full Record",
  expedienteCompleto: "Full Record",
};

export const DESCARGAS: PorIdioma<typeof es> = { es, en };
