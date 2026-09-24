// AUD-09 H08: toda espera tiene tiempo límite y salida. /nueva podía quedarse
// para siempre en "Organizando tu idea…": si el stream moría sin done ni error
// después de "inicio", o la conexión quedaba colgada, nada lo detectaba.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { consumirSSE, EsperaAgotadaError } from "./sseCliente";

function respuestaQueSeCallaDespuesDe(frames: string[]) {
  const enc = new TextEncoder();
  const cuerpo = new ReadableStream<Uint8Array>({
    start(c) {
      for (const f of frames) c.enqueue(enc.encode(f));
      // y nunca cierra ni manda nada más: una conexión colgada
    },
  });
  return new Response(cuerpo);
}

describe("consumirSSE con límite de silencio", () => {
  it("una conexión colgada termina con EsperaAgotadaError, no espera para siempre", async () => {
    const vistos: string[] = [];
    const res = respuestaQueSeCallaDespuesDe(['event: inicio\ndata: {"project_id":"p1"}\n\n']);
    await expect(consumirSSE(res, (e) => vistos.push(e.evento), { silencioMaxMs: 40 })).rejects.toBeInstanceOf(
      EsperaAgotadaError
    );
    expect(vistos).toEqual(["inicio"]);
  }, 2000);

  it("un stream normal se lee entero y resuelve", async () => {
    const enc = new TextEncoder();
    const res = new Response(
      new ReadableStream<Uint8Array>({
        start(c) {
          c.enqueue(enc.encode(": heartbeat\n\nevent: inicio\ndata: {}\n\nevent: done\ndata: {\"ok\":true}\n\n"));
          c.close();
        },
      })
    );
    const vistos: string[] = [];
    await consumirSSE(res, (e) => vistos.push(e.evento), { silencioMaxMs: 1000 });
    expect(vistos).toEqual(["inicio", "done"]);
  });
});

const leer = (rel: string) => readFileSync(path.join(__dirname, "..", "app", rel), "utf8");

describe("las esperas del organizador tienen salida", () => {
  it("/nueva decide por el evento final, no por si llegó 'inicio'", () => {
    const f = leer("nueva/page.tsx");
    expect(f).not.toMatch(/if \(!projectId && !huboError\)/);
    expect(f).toMatch(/EsperaAgotadaError/);
  });
  it("la ruta del organizador garantiza un evento final", () => {
    expect(leer("api/organizer/stream/route.ts")).toMatch(/garantizarTerminal\(/);
  });
});
