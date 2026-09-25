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

const en: typeof es = {
  turno: {
    faltaRespuesta: "missing 'respuesta'",
  },
  regenerar: {
    noEncontrePlan: "I couldn't find that plan.",
    planCompleto: "This plan is already complete: there's nothing to regenerate.",
  },
  plan: {
    noPudeTerminar: "I couldn't finish writing your plan. What you told me is saved; try again.",
  },
  organizador: {
    noPudeOrganizar: "I couldn't organize your idea right now. Try again in a little while.",
    yaOrdenada: "This idea is already organized.",
    truncado:
      "your idea has a lot in it, more than I can organize in one go; trim it a little or tell it to me in parts and try again",
    noPudimosOrganizar: "we couldn't organize your idea right now; your text is saved, try again",
  },
  cierre: {
    caminoTitulo: "Down this path, I can't find a plan that's worth your time.",
    caminoCuerpo:
      "I explored what you told me and, to be honest, this angle doesn't give me enough material to " +
      "build you a plan that would really move you forward. I'd rather tell you than hand you filler. It's not a no to " +
      "your idea: it's a no to this path.",
    mundoTitulo: "{{nombre}} isn't for this idea, not yet.",
    mundoCuerpo:
      "I activated and explored this world with what you have today, and I didn't find a subproject that adds real value without " +
      "inventing busywork for you. Rather than give you a filler checklist, I'd rather stop here. This world is " +
      "still waiting for you: you can come back in when your project grows.",
    mundoSinNombre: "This world",
    seguimientoTitulo: "This cycle, I didn't find a new door in {{nombre}}.",
    seguimientoCuerpo:
      "I went over what you told me and didn't find anything new that's worth a plan in this world without " +
      "inventing busywork for you. Your plan and your progress in this world are still intact: you can keep going with " +
      "them and come back to tell me when there's news.",
    seguimientoSinNombre: "this world",
  },
};

export const SERVIDOR_SESION: PorIdioma<typeof es> = { es, en };
