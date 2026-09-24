// El micrófono se desactivaba aunque el usuario siguiera hablando (reporte del
// fundador, 26 sep 2026). El reconocimiento de voz del navegador cierra la
// sesión tras una pausa, un corte de red o al minuto, aunque sea continuo, y
// useSpeech lo tomaba como el fin del dictado. Ahora, si el usuario no lo
// detuvo y el error no es definitivo, se reanuda solo; lo provisional queda
// fijo al reanudar para no perderse.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { debeReanudar, esErrorFatalVoz, MAX_CORTES_RAPIDOS } from "./useSpeech";

describe("el dictado se reanuda solo cuando el navegador lo corta", () => {
  it("un corte del navegador (pausa, red, minuto) se reanuda", () => {
    expect(debeReanudar({ detenidoPorUsuario: false, errorFatal: false, cortesRapidosSeguidos: 0 })).toBe(true);
  });
  it("si lo detuvo el usuario, no", () => {
    expect(debeReanudar({ detenidoPorUsuario: true, errorFatal: false, cortesRapidosSeguidos: 0 })).toBe(false);
  });
  it("sin permiso o sin micrófono, no (error definitivo)", () => {
    expect(esErrorFatalVoz("not-allowed")).toBe(true);
    expect(esErrorFatalVoz("service-not-allowed")).toBe(true);
    expect(esErrorFatalVoz("audio-capture")).toBe(true);
    expect(esErrorFatalVoz("no-speech")).toBe(false);
    expect(esErrorFatalVoz("network")).toBe(false);
    expect(debeReanudar({ detenidoPorUsuario: false, errorFatal: true, cortesRapidosSeguidos: 0 })).toBe(false);
  });
  it("si se corta en seguida una y otra vez, para (sin bucle)", () => {
    expect(debeReanudar({ detenidoPorUsuario: false, errorFatal: false, cortesRapidosSeguidos: MAX_CORTES_RAPIDOS })).toBe(false);
  });
  it("useSpeech reanuda en onend y el campo fija lo provisional al reanudar", () => {
    const hook = readFileSync(path.join(__dirname, "useSpeech.ts"), "utf8");
    expect(hook).toMatch(/debeReanudar\(/);
    const campo = readFileSync(path.join(__dirname, "..", "app", "ui", "CampoConVoz.tsx"), "utf8");
    expect(campo).toMatch(/sufijoProvisional\.current = ""/);
    expect(campo).toMatch(/useSpeech\([\s\S]*?\(\) => \{\s*sufijoProvisional\.current = "";\s*\}\s*\)/);
  });
});
