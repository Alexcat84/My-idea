/** Rutas de /api/project/[id]/world/[pack]/* (abrir, explorar, diagnosticar y cerrar un mundo). */
import type { PorIdioma } from "../config";

const es = {
  unlock: {
    noPudimosActivar: "no pudimos activar el mundo, intenta de nuevo",
  },
  start: {
    diagnosticoListo:
      'Tu diagnóstico de "{{mundo}}" ya está listo: puedes releerlo y generar su plan cuando quieras. ' +
      "Cuando tu proyecto avance de ciclo, podrás explorarlo de nuevo gratis.",
    puertasRecorridas: "Ya recorriste todas las puertas de este mundo.",
    preparando: "Este mundo se está preparando. Muy pronto podrás explorarlo.",
    noPudimosAbrir: "no pudimos abrir el mundo, intenta de nuevo",
  },
  completar: {
    accionInvalida: "acción inválida; usa 'completar' o 'reabrir'",
    noPudeGuardarActa:
      'No pude guardar el acta del cierre de "{{mundo}}", así que sigue abierto. Intenta de nuevo en un momento.',
    noPudimosGuardar: "no pudimos guardar; intenta de nuevo",
  },
  diagnostico: {
    sinExploracion: "No encontré la exploración de este mundo. Vuelve a explorarlo desde su espacio.",
    sinRespuestas: "Esta exploración todavía no tiene respuestas que diagnosticar.",
    esSeguimiento: "Este es un ciclo de seguimiento: termina en tu plan, no en un diagnóstico.",
    noPudimosRedactar: "no pudimos redactar tu diagnóstico; intenta de nuevo en un momento",
    noPudimosGuardar: "no pudimos guardar tu diagnóstico; intenta de nuevo",
  },
};

const en: typeof es = {
  unlock: {
    noPudimosActivar: "we couldn't activate the world, try again",
  },
  start: {
    diagnosticoListo:
      'Your "{{mundo}}" diagnosis is ready: you can reread it and generate its plan whenever you want. ' +
      "When your project moves on to its next cycle, you'll be able to explore it again for free.",
    puertasRecorridas: "You've already been through every door in this world.",
    preparando: "This world is still being prepared. You'll be able to explore it very soon.",
    noPudimosAbrir: "we couldn't open the world, try again",
  },
  completar: {
    accionInvalida: "invalid action; use 'completar' or 'reabrir'",
    noPudeGuardarActa:
      'I couldn\'t save the closing record for "{{mundo}}", so it\'s still open. Try again in a moment.',
    noPudimosGuardar: "we couldn't save; try again",
  },
  diagnostico: {
    sinExploracion: "I couldn't find this world's exploration. Explore it again from its space.",
    sinRespuestas: "This exploration doesn't have any answers to diagnose yet.",
    esSeguimiento: "This is a follow-up cycle: it ends in your plan, not in a diagnosis.",
    noPudimosRedactar: "we couldn't write your diagnosis; try again in a moment",
    noPudimosGuardar: "we couldn't save your diagnosis; try again",
  },
};

export const SERVIDOR_MUNDOS: PorIdioma<typeof es> = { es, en };
