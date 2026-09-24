"use client";

/**
 * sseCliente — consumidor de Server-Sent Events sobre fetch POST (los
 * EventSource nativos solo hacen GET). Mismo protocolo que ya usan las
 * rutas del motor: frames `event: X\ndata: JSON\n\n`, comentarios de
 * heartbeat (": heartbeat") ignorados.
 */

export interface EventoSSE {
  evento: string;
  data: unknown;
}

/** AUD-09 H08: toda espera tiene tiempo límite y salida. Las rutas del motor
 * mandan un latido cada 15 s; tres latidos perdidos seguidos significan que la
 * conexión murió o quedó colgada. */
export const SILENCIO_MAX_MS = 45_000;

/** La conexión quedó en silencio más allá del límite: se corta la lectura y
 * quien espera recibe este error para mostrar una salida. */
export class EsperaAgotadaError extends Error {
  constructor(ms: number) {
    super(`la conexion quedo en silencio mas de ${Math.round(ms / 1000)} s`);
    this.name = "EsperaAgotadaError";
  }
}

export async function consumirSSE(
  respuesta: Response,
  onEvento: (e: EventoSSE) => void,
  opts: { silencioMaxMs?: number } = {}
): Promise<void> {
  const silencioMaxMs = opts.silencioMaxMs ?? SILENCIO_MAX_MS;
  const reader = respuesta.body!.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  for (;;) {
    let temporizador: ReturnType<typeof setTimeout> | undefined;
    const silencio = new Promise<never>((_, rechazar) => {
      temporizador = setTimeout(() => rechazar(new EsperaAgotadaError(silencioMaxMs)), silencioMaxMs);
    });
    let lectura: ReadableStreamReadResult<Uint8Array>;
    try {
      lectura = await Promise.race([reader.read(), silencio]);
    } catch (e) {
      if (e instanceof EsperaAgotadaError) void reader.cancel().catch(() => {});
      throw e;
    } finally {
      clearTimeout(temporizador);
    }
    const { done, value } = lectura;
    if (done) break;
    buffer += decoder.decode(value, { stream: true });
    let idx: number;
    while ((idx = buffer.indexOf("\n\n")) !== -1) {
      const frame = buffer.slice(0, idx);
      buffer = buffer.slice(idx + 2);
      if (!frame.trim() || frame.startsWith(":")) continue;
      let evento = "message";
      let dataRaw = "";
      for (const linea of frame.split("\n")) {
        if (linea.startsWith("event: ")) evento = linea.slice(7);
        else if (linea.startsWith("data: ")) dataRaw += linea.slice(6);
      }
      onEvento({ evento, data: dataRaw ? JSON.parse(dataRaw) : null });
    }
  }
}
