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
      a_tiempo: "planificado · a tiempo",
      adelantada: "planificado · adelantada",
      tardia: "planificado · tardía",
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

export const ANALYTICS_INFORME: PorIdioma<typeof es> = { es };
