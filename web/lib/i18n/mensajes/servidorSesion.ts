/** Rutas de la entrevista (/api/session/*), del organizador (/api/organizer*) y los cierres honestos de lib/apiSesion.ts. */
import type { PorIdioma } from "../config";

const es = {
  turno: {
    faltaRespuesta: "falta 'respuesta'",
  },
  regenerar: {
    noEncontrePlan: "No encontré ese plan.",
    planCompleto: "Este plan ya está completo: no hay nada que regenerar.",
  },
  plan: {
    noPudeTerminar: "No pude terminar de escribir tu plan. Lo que contaste está guardado; intenta de nuevo.",
  },
  organizador: {
    noPudeOrganizar: "No pude organizar tu idea en este momento. Intenta de nuevo en un rato.",
    yaOrdenada: "Esta idea ya está ordenada.",
    truncado:
      "tu idea trae mucho y se pasó de lo que puedo organizar de una sola vez; recórtala un poco o cuéntamela por partes e intenta de nuevo",
    noPudimosOrganizar: "no pudimos organizar tu idea en este momento; tu texto quedó guardado, intenta de nuevo",
  },
  /** FASE B (canon 12): el cierre honesto, título y cuerpo (apiSesion.ts). */
  cierre: {
    caminoTitulo: "Por aquí no encuentro un plan que valga tu tiempo.",
    caminoCuerpo:
      "Exploré lo que me contaste y, siendo honesto, este ángulo no me da material suficiente para " +
      "armarte un plan que de verdad te mueva. Prefiero decírtelo a entregarte relleno. No es un no a " +
      "tu idea: es un no a este camino.",
    mundoTitulo: "{{nombre}} no es para esta idea, todavía.",
    mundoCuerpo:
      "Activé y exploré este mundo con lo que hay hoy, y no encontré un subproyecto que te sume sin " +
      "inventarte trabajo. Antes que darte un checklist de relleno, prefiero parar aquí. Este mundo te " +
      "sigue esperando: puedes volver a entrar cuando tu proyecto crezca.",
    mundoSinNombre: "Este mundo",
    seguimientoTitulo: "En este ciclo no encontré una puerta nueva en {{nombre}}.",
    seguimientoCuerpo:
      "Revisé lo que me contaste y no encontré algo nuevo que valga un plan en este mundo sin " +
      "inventarte trabajo. Tu plan y tu avance en este mundo siguen intactos: puedes seguir con " +
      "ellos y volver a contarme cuando haya novedades.",
    seguimientoSinNombre: "este mundo",
  },
};

export const SERVIDOR_SESION: PorIdioma<typeof es> = { es };
