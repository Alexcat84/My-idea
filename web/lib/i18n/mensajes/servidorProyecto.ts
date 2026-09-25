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
    primeroExplora: 'Primero explora "{{mundo}}" — su seguimiento nace de su plan.',
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

export const SERVIDOR_PROYECTO: PorIdioma<typeof es> = { es };
