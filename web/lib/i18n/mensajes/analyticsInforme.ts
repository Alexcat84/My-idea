/** analytics.ts y analyticsEntrada.ts: los hitos del timeline, el informe descargable (.md)
 * del Análisis, el "Cómo te fue" compacto de un espacio y el aviso de lectura fallida. */
import type { PorIdioma } from "../config";

const es = {
  hitos: {
    laChispa: "La Chispa",
    laIdeaNace: "La idea nace",
    claridad: "Claridad",
    tuIdeaOrganizada: "Tu idea, organizada",
    conLineaBase: "con línea base",
    replanificado: "replanificado con lo aprendido",
    tuPlanCiclo: "Tu Plan · ciclo {{n}}",
    mundoActivado: "Mundo activado",
    mundoCompletado: "Mundo completado",
    accionCompletada: "Acción completada",
    realizada: "REALIZADA",
    /** El subtítulo de un hito de acción por su cumplimiento (el cumplimiento es el DATO). */
    cumplimiento: {
      a_tiempo: "planificada · a tiempo",
      adelantada: "planificada · adelantada",
      tardia: "planificada · tardía",
    },
  },
  /** Líneas del markdown (el informe y el resumen de un espacio). */
  md: {
    duracion: "- Duración: **{{n}} días**",
    accionesActivas: "- Acciones completadas: **{{hechas}} de {{total}}** activas",
    ritmo: "- Ritmo: **{{n}} acciones por semana**",
    racha: "- Racha más larga: **{{n}} días**",
    retiradas: "- Retiradas (no aplican): **{{n}}**",
    cumplimiento:
      "- Cumplimiento: **{{aTiempo}} a tiempo, {{adelantadas}} adelantadas, {{tardias}} tardías** (de {{total}} con fecha)",
    titulo: "# Análisis de {{nombre}}",
    estadoActual: "## Estado actual",
    ideaRealizada: "- Idea realizada el {{fecha}}",
    accionesHoy: "- Acciones hoy: **{{hechas}} de {{total}}**",
    pct: " ({{pct}}%)",
    mundoCompletadoEl: "completado el {{fecha}}",
    mundoAbierto: "abierto",
    mundoLinea: "- {{mundo}}: **{{hechas}} de {{total}}**{{pct}}, {{estado}}",
    porQueLaCerraste: "### Por qué la cerraste aquí",
    loQueConstruiste: "## Lo que construiste",
    duracionTotal: "- Duración total: **{{n}} días**",
    accionesCompletadas: "- Acciones completadas: **{{hechas}}** de **{{total}}** activas",
    ciclosYMundos: "- Ciclos de plan: **{{ciclos}}** · Mundos: **{{mundos}}**",
    retiradasTitulo: "### Retiradas (no aplican): {{n}}",
    duracionPorEtapa: "### Duración real por etapa",
    etapaDias: "- Etapa {{etapa}}: {{dias}} días",
    cumplimientoTitulo: "## Cumplimiento (comparado con tus fechas)",
    aTiempo: "- A tiempo: **{{n}}** ({{pct}}%)",
    adelantadas: "- Adelantadas: **{{n}}** ({{pct}}%)",
    tardias: "- Tardías: **{{n}}** ({{pct}}%)",
    desviacionVigente: "- Desviación media sobre tu plan vigente: **{{signo}}{{dias}} días**",
    frentePlanInicial:
      "- Frente a tu plan inicial: **{{signo}}{{dias}} días** de desviación media · **{{n}}** replanificaciones.",
    replanificarEsMetodo:
      "Replanificar es parte del método. Tu plan vigente asume tu ritmo real; ajustar el mapa no es fallar.",
    hitos: "## Hitos",
  },
  lecturaFallida: "No pude leer tu avance en este momento; intenta de nuevo en un rato.",
};

const en: typeof es = {
  hitos: {
    laChispa: "The Spark",
    laIdeaNace: "Your idea is born",
    claridad: "Clarity",
    tuIdeaOrganizada: "Your idea, organized",
    conLineaBase: "with a baseline",
    replanificado: "replanned with what you learned",
    tuPlanCiclo: "Your Plan · cycle {{n}}",
    mundoActivado: "World activated",
    mundoCompletado: "World completed",
    accionCompletada: "Action completed",
    realizada: "ACHIEVED",
    cumplimiento: {
      a_tiempo: "planned · on time",
      adelantada: "planned · early",
      tardia: "planned · late",
    },
  },
  md: {
    duracion: "- Duration: **{{n}} days**",
    accionesActivas: "- Actions completed: **{{hechas}} of {{total}}** active",
    ritmo: "- Pace: **{{n}} actions per week**",
    racha: "- Longest streak: **{{n}} days**",
    retiradas: "- Set aside (don't apply): **{{n}}**",
    cumplimiento:
      "- On-time record: **{{aTiempo}} on time, {{adelantadas}} early, {{tardias}} late** (out of {{total}} with a date)",
    titulo: "# Analysis of {{nombre}}",
    estadoActual: "## Current status",
    ideaRealizada: "- Idea achieved on {{fecha}}",
    accionesHoy: "- Actions today: **{{hechas}} of {{total}}**",
    pct: " ({{pct}}%)",
    mundoCompletadoEl: "completed on {{fecha}}",
    mundoAbierto: "open",
    mundoLinea: "- {{mundo}}: **{{hechas}} of {{total}}**{{pct}}, {{estado}}",
    porQueLaCerraste: "### Why you closed it here",
    loQueConstruiste: "## What you built",
    duracionTotal: "- Total duration: **{{n}} days**",
    accionesCompletadas: "- Actions completed: **{{hechas}}** of **{{total}}** active",
    ciclosYMundos: "- Plan cycles: **{{ciclos}}** · Worlds: **{{mundos}}**",
    retiradasTitulo: "### Set aside (don't apply): {{n}}",
    duracionPorEtapa: "### Actual duration by stage",
    etapaDias: "- Stage {{etapa}}: {{dias}} days",
    cumplimientoTitulo: "## On-time record (against your dates)",
    aTiempo: "- On time: **{{n}}** ({{pct}}%)",
    adelantadas: "- Early: **{{n}}** ({{pct}}%)",
    tardias: "- Late: **{{n}}** ({{pct}}%)",
    desviacionVigente: "- Average deviation from your current plan: **{{signo}}{{dias}} days**",
    frentePlanInicial:
      "- Compared with your original plan: **{{signo}}{{dias}} days** of average deviation · **{{n}}** plan updates.",
    replanificarEsMetodo:
      "Replanning is part of the method. Your current plan follows your real pace; adjusting the map isn't failing.",
    hitos: "## Milestones",
  },
  lecturaFallida: "I couldn't read your progress right now; try again in a little while.",
};

export const ANALYTICS_INFORME: PorIdioma<typeof es> = { es, en };
