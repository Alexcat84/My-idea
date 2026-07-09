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

export async function consumirSSE(
  respuesta: Response,
  onEvento: (e: EventoSSE) => void
): Promise<void> {
  const reader = respuesta.body!.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  for (;;) {
    const { done, value } = await reader.read();
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
