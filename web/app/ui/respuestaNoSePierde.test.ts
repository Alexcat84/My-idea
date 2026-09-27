// AUD-09 M27 (tanda 7A, datos): si el turno fallaba (red, límite, doble
// factor), la respuesta escrita se borraba: TarjetaPregunta vaciaba el campo en
// el mismo clic, antes de saber si el servidor la recibió. La regla: el campo
// se vacía solo cuando el turno llegó.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const tarjeta = readFileSync(path.join(__dirname, "TarjetaPregunta.tsx"), "utf8");
const idea = readFileSync(path.join(__dirname, "..", "idea", "[id]", "IdeaView.tsx"), "utf8");

describe("la respuesta escrita no se pierde si el turno falla (AUD-09 M27)", () => {
  it("onEnviar dice si el turno llegó", () => {
    expect(tarjeta).toMatch(/onEnviar: \(respuesta: string\) => Promise<boolean>/);
  });

  it("el campo se vacía solo tras un envío aceptado", () => {
    expect(tarjeta).toMatch(/if \(await onEnviar\(respuesta\)\) setRespuesta\(""\)/);
    expect(tarjeta).not.toMatch(/onEnviar\(respuesta\);\s*setRespuesta\(""\);/);
  });

  it("responder devuelve true solo cuando el servidor aceptó", () => {
    const fn = idea.match(/async function responder\(respuesta: string\)[\s\S]*?\r?\n  \}\r?\n/)?.[0] ?? "";
    expect(fn).toMatch(/Promise<boolean>/);
    expect(fn).toMatch(/return true;/);
  });
});
