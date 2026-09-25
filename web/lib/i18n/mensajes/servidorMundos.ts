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

export const SERVIDOR_MUNDOS: PorIdioma<typeof es> = { es };
