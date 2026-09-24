// AUD-09 B14c (tanda 7B, confianza): si el navegador negaba el permiso del
// micrófono, el dictado se apagaba en silencio: el botón dejaba de pulsar y
// nadie decía por qué. Ahora el motivo se dice y se ofrece el camino.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { mensajeErrorVoz } from "./useSpeech";

describe("el micrófono dice por qué se apagó (AUD-09 B14c)", () => {
  it("permiso negado", () => {
    expect(mensajeErrorVoz("not-allowed")).toBe(
      "Tu navegador no me dio permiso para usar el micrófono. Puedes escribir, o darle permiso en la configuración del navegador."
    );
    expect(mensajeErrorVoz("service-not-allowed")).toBe(mensajeErrorVoz("not-allowed"));
  });
  it("sin micrófono, y cualquier otro fallo", () => {
    expect(mensajeErrorVoz("audio-capture")).toBe("No encontré un micrófono. Puedes escribir tu respuesta.");
    expect(mensajeErrorVoz("network")).toBe("El dictado se cortó. Puedes volver a intentarlo o escribir.");
  });
  it("no hablar no es un error que haya que anunciar", () => {
    expect(mensajeErrorVoz("no-speech")).toBeNull();
    expect(mensajeErrorVoz("aborted")).toBeNull();
  });
  it("el campo con voz muestra el motivo", () => {
    const campo = readFileSync(path.join(__dirname, "..", "app", "ui", "CampoConVoz.tsx"), "utf8");
    expect(campo).toMatch(/errorVoz &&/);
  });
});
