/** Los documentos del viaje (lib/expediente.ts): el índice de descargas, cada
 * ciclo, el Expediente completo y el Reporte de un mundo; y el "cómo te fue"
 * del Expediente (lib/resumenExpediente.ts). Los "## " y "**" son la estructura
 * markdown del documento: se conservan tal cual en cada idioma. */
import type { PorIdioma } from "../config";

const es = {
  ciclos: {
    tuPlan: "Tu Plan",
    tuPlanSubtitulo: "El plan con el que arrancaste",
    seguimiento: "Seguimiento {{n}}",
    seguimientoSubtitulo: "Lo que pasó y el plan recalculado",
  },
  indice: {
    analisisTitulo: "Análisis del proyecto",
    analisisSubtitulo: "Tu ritmo, tus etapas y tu cumplimiento, calculados de lo que hiciste",
    bitacoraTitulo: "Tu bitácora",
    bitacoraSubtitulo: "La historia de tu idea, paso a paso, del inicio a hoy",
    expedienteTitulo: "Expediente completo",
    expedienteSubtituloCerrado:
      "Tu idea, tu plan y sus ciclos, tu avance, cada mundo y tu bitácora, de la idea al cierre",
    expedienteSubtituloEnMarcha: "Tu idea, tu plan y sus ciclos, tu avance, cada mundo y tu bitácora, hasta hoy",
    reporteTitulo: "Reporte de {{mundo}}",
    reporteSubtitulo: "El plan, el avance y el cómo te fue de este mundo",
    registroTitulo: "Registro de {{mundo}}",
    registroSubtitulo: "Lo que este mundo detectó y la respuesta que lo atiende, sobre tu plan real",
  },
  acciones: {
    completaste: "Completaste **{{hechas}} de {{total}}** acciones activas.",
    etapa: "Etapa {{n}}",
    tablaEncabezado: "| Acción | Cuándo |",
    hechoEl: "[hecho el {{fecha}}](#f-hecho)",
    previstoPara: "[previsto para el {{fecha}}](#f-prev)",
    sinFecha: "sin fecha",
    retiradas: "Retiradas (no aplican): {{n}}",
    retiradasExplicacion:
      "Tareas que decidiste que no corren para esta idea. No son pendientes ni fracasos: son parte de tu criterio.",
  },
  expediente: {
    loQueHiciste: "Lo que hiciste",
    tuAvance: "Tu avance",
    comoTeFue: "Cómo te fue",
    tuProgreso: "Tu progreso hasta aquí",
    generado: "> Expediente completo · generado el {{fecha}}",
    empezaste: "**Empezaste** el {{fecha}}",
    estadoRealizado: "**Estado** Proyecto realizado el {{fecha}}",
    estadoEnMarcha: "**Estado** En marcha",
    tituloContenido: "## Contenido",
    // El índice ("## Contenido") lista estos mismos títulos sin el "## ".
    tituloIdeaEscrita: "## Tu idea, tal como la escribiste",
    tituloIdeaOrdenada: "## Tu idea, ordenada",
    tituloNumeros: "## Tus Números",
    mundoTerminado: "_Lo diste por terminado el {{fecha}}_",
    tituloPorQueCerraste: "## Por qué la cerraste aquí",
    tituloSecuencia: "## La secuencia de tu viaje",
  },
  reporteMundo: {
    titulo: "# Reporte de {{mundo}}",
    generado: "> {{idea}} · generado el {{fecha}}",
    estadoTerminado: "**Estado** Terminado el {{fecha}}",
    tituloSecuencia: "## La secuencia de este mundo",
  },
  archivo: {
    ideaPorOmision: "mi-idea",
    documentoPorOmision: "documento",
  },
  resumenCamino: {
    introCerrada: "Empezaste con una idea y llegaste hasta el cierre. Esto es lo que dejó el camino.",
    introEnMarcha: "Esto es lo que llevas hasta aquí.",
    movioReplanificando:
      "Frente a tu plan inicial te moviste {{desviacion}} días de media a lo largo de {{replanificaciones}}. Ajustar el mapa fue parte del método.",
    replanificaciones: { one: "{{n}} replanificación", other: "{{n}} replanificaciones" },
    movioConFechas:
      "De tus {{total}} acciones con fecha, {{aTiempo}} salieron a tiempo, {{adelantadas}} antes y {{tardias}} después de lo planeado.",
    movioARitmo: "Avanzaste a tu ritmo, sin fechas contra las cuales medirte.",
    movioSinFechas: "Aún no sellaste tus fechas, así que no hay un plan contra el cual medir tu ritmo.",
  },
};

const en: typeof es = {
  ciclos: {
    tuPlan: "Your Plan",
    tuPlanSubtitulo: "The plan you started with",
    seguimiento: "Follow-up {{n}}",
    seguimientoSubtitulo: "What happened and the recalculated plan",
  },
  indice: {
    analisisTitulo: "Project analysis",
    analisisSubtitulo: "Your pace, your stages and your follow-through, calculated from what you did",
    bitacoraTitulo: "Your logbook",
    bitacoraSubtitulo: "The story of your idea, step by step, from the start to today",
    expedienteTitulo: "Full Record",
    expedienteSubtituloCerrado:
      "Your idea, your plan and its cycles, your progress, each world and your logbook, from the idea to the close",
    expedienteSubtituloEnMarcha: "Your idea, your plan and its cycles, your progress, each world and your logbook, up to today",
    reporteTitulo: "Report for {{mundo}}",
    reporteSubtitulo: "The plan, the progress and how this world went for you",
    registroTitulo: "{{mundo}} register",
    registroSubtitulo: "What this world spotted and the response that handles it, based on your real plan",
  },
  acciones: {
    completaste: "You completed **{{hechas}} of {{total}}** active actions.",
    etapa: "Stage {{n}}",
    tablaEncabezado: "| Action | When |",
    hechoEl: "[done on {{fecha}}](#f-hecho)",
    previstoPara: "[planned for {{fecha}}](#f-prev)",
    sinFecha: "no date",
    retiradas: "Set aside (don't apply): {{n}}",
    retiradasExplicacion:
      "Tasks you decided don't fit this idea. They aren't pending or failures: they're part of your judgment.",
  },
  expediente: {
    loQueHiciste: "What you did",
    tuAvance: "Your progress",
    comoTeFue: "How it went",
    tuProgreso: "How far you've come",
    generado: "> Full Record · generated on {{fecha}}",
    empezaste: "**You started** on {{fecha}}",
    estadoRealizado: "**Status** Project achieved on {{fecha}}",
    estadoEnMarcha: "**Status** Underway",
    tituloContenido: "## Contents",
    // El índice ("## Contents") lista estos mismos títulos sin el "## ".
    tituloIdeaEscrita: "## Your idea, as you wrote it",
    tituloIdeaOrdenada: "## Your idea, organized",
    tituloNumeros: "## Your Numbers",
    mundoTerminado: "_You called it finished on {{fecha}}_",
    tituloPorQueCerraste: "## Why you closed it here",
    tituloSecuencia: "## The sequence of your journey",
  },
  reporteMundo: {
    titulo: "# Report for {{mundo}}",
    generado: "> {{idea}} · generated on {{fecha}}",
    estadoTerminado: "**Status** Finished on {{fecha}}",
    tituloSecuencia: "## The sequence of this world",
  },
  archivo: {
    ideaPorOmision: "my-idea",
    documentoPorOmision: "document",
  },
  resumenCamino: {
    introCerrada: "You started with an idea and made it all the way to the close. This is what the road left you.",
    introEnMarcha: "This is where you are so far.",
    movioReplanificando:
      "Compared to your first plan, you shifted {{desviacion}} days on average across {{replanificaciones}}. Adjusting the map was part of the method.",
    replanificaciones: { one: "{{n}} plan update", other: "{{n}} plan updates" },
    movioConFechas:
      "Of your {{total}} dated actions, {{aTiempo}} landed on time, {{adelantadas}} early and {{tardias}} later than planned.",
    movioARitmo: "You moved at your own pace, with no dates to measure yourself against.",
    movioSinFechas: "You haven't locked in your dates yet, so there's no plan to measure your pace against.",
  },
};

export const EXPEDIENTE: PorIdioma<typeof es> = { es, en };
