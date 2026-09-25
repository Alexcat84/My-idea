/** Rutas de /api/project/[id]/* (sin mundos ni documentos), del calendario y de los packs. */
import type { PorIdioma } from "../config";

const es = {
  borrar: {
    algoSeAtoro: "algo se atoró; intenta de nuevo",
  },
  baseline: {
    faltaPlanOFechas: "falta plan_id o fechas mal formadas",
    noPudimosSellar: "no pudimos sellar la línea base",
  },
  modo: {
    modoInvalido: "modo_camino inválido; usa uno de: {{opciones}}",
    capacidadInvalida: "capacidad_semanal inválida; usa una de: {{opciones}}",
    nadaQueActualizar: "nada que actualizar: manda modo_camino y/o capacidad_semanal",
    espacioNoExiste: "ese espacio no existe",
  },
  checklist: {
    faltaItemId: "falta item_id",
    estadoInvalido: "estado inválido; usa uno de: {{opciones}}",
    notaInvalida: "nota debe ser texto o null",
    completedAtInvalido: "completed_at debe ser una fecha ISO no futura o null",
    motivoInvalido: "no_aplica_motivo debe ser texto o null",
    bandaInvalida: "banda inválida; usa una de: {{opciones}}",
    fechaBaseInvalida: "fecha_base debe ser una fecha ISO o null",
    nadaQueActualizar: "nada que actualizar: manda estado, nota, completed_at, no_aplica_motivo, fecha_base y/o banda",
    itemNoEncontrado: "ítem no encontrado",
  },
  moverFecha: {
    faltaItemOFecha: "falta item_id o fecha mal formada",
    actividadNoEncontrada: "actividad no encontrada",
    yaHecha: "Esta actividad ya está hecha. Si la hiciste en otra fecha, cámbiala desde la actividad.",
    retirada: "Esta actividad está retirada. Reactívala primero para darle una fecha.",
    sinFecha: "esta actividad no tiene una fecha que mover",
  },
  realizar: {
    accionInvalida: "acción inválida; usa 'realizar' o 'reabrir'",
    noPudeGuardarActa:
      "No pude guardar el acta de tu cierre, así que tu idea sigue abierta. Intenta de nuevo en un momento.",
  },
  follow: {
    ideaRealizada: "Diste tu idea por realizada. Reábrela si quieres seguir trabajándola.",
    mundoCompletado: 'Diste "{{mundo}}" por completado. Reábrelo si quieres seguir trabajándolo.',
    primeroExplora: 'Primero explora "{{mundo}}": su seguimiento nace de su plan.',
    puertasRecorridas: 'Ya recorriste todas las puertas de "{{mundo}}".',
  },
  numeros: {
    cifrasNoObjeto: "'numeros' debe ser un objeto de campo: valor",
    valorInvalido: "el valor de '{{campo}}' debe ser un número >= 0 o un rango {min, max}",
    versionNoExiste: "esa versión no existe",
    activaUnaVez: "Tus Números se activa una vez por idea.",
    noNarroInconsistente:
      "No narro una conclusión con estos datos: revisa el guardián de datos y corrige la cifra que no cuadra.",
    noPudeNarrar:
      "No pude narrar tus números en este momento. Tu tablero y tus cifras están al día; intenta narrar de nuevo en un rato.",
  },
  reporte: {
    proyectoNoEncontrado: "proyecto no encontrado",
    respuestaInvalida: "'respuesta' debe ser un string no vacío",
    entrevistaEnCurso: "ya hay una entrevista de reporte en curso; envía 'respuesta' para continuarla",
    sinEntrevista: "no hay una entrevista de reporte en curso; llama sin 'respuesta' para iniciarla",
  },
  bitacora: {
    tituloEspacio: "# Bitácora de {{espacio}}",
  },
  calendario: {
    noEncontrado: "Calendario no encontrado.",
    tuViaje: "Tu viaje",
  },
  packs: {
    packDesconocido: "pack desconocido",
  },
};

const en: typeof es = {
  borrar: {
    algoSeAtoro: "something got stuck; try again",
  },
  baseline: {
    faltaPlanOFechas: "missing plan_id or malformed dates",
    noPudimosSellar: "we couldn't lock in the baseline",
  },
  modo: {
    modoInvalido: "invalid modo_camino; use one of: {{opciones}}",
    capacidadInvalida: "invalid capacidad_semanal; use one of: {{opciones}}",
    nadaQueActualizar: "nothing to update: send modo_camino and/or capacidad_semanal",
    espacioNoExiste: "that space doesn't exist",
  },
  checklist: {
    faltaItemId: "missing item_id",
    estadoInvalido: "invalid estado; use one of: {{opciones}}",
    notaInvalida: "nota must be text or null",
    completedAtInvalido: "completed_at must be an ISO date not in the future, or null",
    motivoInvalido: "no_aplica_motivo must be text or null",
    bandaInvalida: "invalid banda; use one of: {{opciones}}",
    fechaBaseInvalida: "fecha_base must be an ISO date or null",
    nadaQueActualizar: "nothing to update: send estado, nota, completed_at, no_aplica_motivo, fecha_base and/or banda",
    itemNoEncontrado: "item not found",
  },
  moverFecha: {
    faltaItemOFecha: "missing item_id or malformed date",
    actividadNoEncontrada: "activity not found",
    yaHecha: "This activity is already done. If you did it on a different date, change it from the activity itself.",
    retirada: "This activity is set aside. Bring it back first to give it a date.",
    sinFecha: "this activity doesn't have a date to move",
  },
  realizar: {
    accionInvalida: "invalid action; use 'realizar' or 'reabrir'",
    noPudeGuardarActa:
      "I couldn't save the closing record for your idea, so it's still open. Try again in a moment.",
  },
  follow: {
    ideaRealizada: "You marked your idea as achieved. Reopen it if you want to keep working on it.",
    mundoCompletado: 'You marked "{{mundo}}" as completed. Reopen it if you want to keep working on it.',
    primeroExplora: 'Explore "{{mundo}}" first: its follow-up grows out of its plan.',
    puertasRecorridas: 'You\'ve already been through every door in "{{mundo}}".',
  },
  numeros: {
    cifrasNoObjeto: "'numeros' must be an object of field: value",
    valorInvalido: "the value of '{{campo}}' must be a number >= 0 or a range {min, max}",
    versionNoExiste: "that version doesn't exist",
    activaUnaVez: "Your Numbers is activated once per idea.",
    noNarroInconsistente:
      "I won't narrate a conclusion from this data: check the data guardian and fix the figure that doesn't add up.",
    noPudeNarrar:
      "I couldn't narrate your numbers right now. Your dashboard and your figures are up to date; try narrating again in a little while.",
  },
  reporte: {
    proyectoNoEncontrado: "project not found",
    respuestaInvalida: "'respuesta' must be a non-empty string",
    entrevistaEnCurso: "there's already a report interview in progress; send 'respuesta' to continue it",
    sinEntrevista: "there's no report interview in progress; call without 'respuesta' to start one",
  },
  bitacora: {
    tituloEspacio: "# {{espacio}} Logbook",
  },
  calendario: {
    noEncontrado: "Calendar not found.",
    tuViaje: "Your Journey",
  },
  packs: {
    packDesconocido: "unknown pack",
  },
};

export const SERVIDOR_PROYECTO: PorIdioma<typeof es> = { es, en };
