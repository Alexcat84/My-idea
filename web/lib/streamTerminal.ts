/**
 * streamTerminal.ts: LA GARANTIA DEL EVENTO TERMINAL (4 sep 2026, decisión
 * del fundador, sesión con credencial).
 *
 * POR QUE EXISTE. La corrida I del vuelo cayó con "el plan de seguimiento no
 * devolvió markdown": el cliente no recibió `done` NI `error`, el servidor
 * respondió 200 en 115s y NO escribió una sola línea `[plan]`, o sea que su
 * catch no llegó a correr como se esperaba. Un stream que termina en silencio
 * es exactamente lo que la doctrina de FALLAR RUIDOSO prohíbe: no deja
 * síntoma, y el que lo sufre no puede distinguirlo de un transitorio.
 *
 * COMO PUEDE PASAR, que es lo que hace falta entender para curarlo: si
 * `enviar("done", ...)` falla (el controller ya roto, un enqueue que tira),
 * el catch intenta `enviar("error", ...)` y falla por lo mismo; ese segundo
 * throw escapa del catch, el `finally` cierra el stream, y el cliente ve un
 * final limpio sin un solo evento terminal.
 *
 * QUE HACE: se llama SIEMPRE desde el `finally` de la ruta. Si ya salió un
 * terminal, no hace nada. Si no salió, GRITA por los dos canales: escribe
 * `[plan] cierre sin terminal` en el log del servidor (con el id de la
 * llamada, lo emitido hasta ahí y la causa) e intenta emitir un `error` con
 * motivo `cierre sin terminal`.
 *
 * LOS DOS CANALES SON A PROPOSITO. Si el controller está roto, el evento no
 * saldrá tampoco; el log del servidor es entonces la única prueba, y es la
 * que faltaba. Por eso el emit va envuelto y su fallo NO se propaga: una
 * garantía que revienta al garantizar no garantiza nada.
 */

export const MOTIVO_CIERRE_SIN_TERMINAL = "cierre sin terminal";

export interface CierreSinTerminal {
  /** null si aún no salió ningún terminal; "done" o "error" si ya salió. */
  terminalEmitido: string | null;
  /** los eventos emitidos hasta aquí, en orden, para poder leer dónde murió. */
  emitidos: string[];
  /** la causa que el SDK expuso, si la expuso. */
  causa?: unknown;
  /** el id de la llamada. */
  sessionId: string;
  projectId?: string;
  /** el emisor real de la ruta. Puede tirar: se absorbe. */
  enviar: (evento: string, data: unknown) => void;
  /** inyectable para poder probarlo sin ensuciar la consola. */
  log?: (mensaje: string, detalle: unknown) => void;
}

/** Devuelve true si tuvo que gritar (o sea, si el cierre venía mudo). */
export function garantizarTerminal(c: CierreSinTerminal): boolean {
  if (c.terminalEmitido) return false;

  const detalle = {
    session_id: c.sessionId,
    project_id: c.projectId ?? null,
    emitidos: c.emitidos,
    causa: c.causa instanceof Error ? c.causa.message : c.causa ?? null,
  };
  const log = c.log ?? ((m: string, d: unknown) => console.error(m, d));
  log("[plan] cierre sin terminal", detalle);

  // El emit puede fallar por la MISMA razón que dejó el cierre mudo. Se
  // intenta igual (si el canal vive, el cliente se entera) y su fallo se
  // absorbe: el log de arriba ya dejó el síntoma.
  try {
    c.enviar("error", {
      error: MOTIVO_CIERRE_SIN_TERMINAL,
      motivo: MOTIVO_CIERRE_SIN_TERMINAL,
      ...detalle,
    });
  } catch {
    /* el canal está roto: el log del servidor es la prueba */
  }
  return true;
}
