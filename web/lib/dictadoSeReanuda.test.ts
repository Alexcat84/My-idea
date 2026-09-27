// El micrófono se desactivaba aunque el usuario siguiera hablando (reporte del
// fundador, 26 sep 2026). El reconocimiento de voz del navegador cierra la
// sesión tras una pausa, un corte de red o al minuto, aunque sea continuo, y
// useSpeech lo tomaba como el fin del dictado. Ahora, si el usuario no lo
// detuvo y el error no es definitivo, se reanuda solo; lo provisional queda
// fijo al reanudar para no perderse.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { CORTE_RAPIDO_MS, debeReanudar, esCorteRapido, esErrorFatalVoz, MAX_CORTES_RAPIDOS, SILENCIO_MAX_MS } from "./useSpeech";

const normal = { detenidoPorUsuario: false, errorFatal: false, cortesRapidosSeguidos: 0, silencioMs: 0 };

describe("el dictado se reanuda solo cuando el navegador lo corta", () => {
  it("un corte del navegador (pausa, red, minuto) se reanuda", () => {
    expect(debeReanudar(normal)).toBe(true);
  });
  it("si lo detuvo el usuario, no", () => {
    expect(debeReanudar({ ...normal, detenidoPorUsuario: true })).toBe(false);
  });
  it("sin permiso o sin micrófono, no (error definitivo)", () => {
    expect(esErrorFatalVoz("not-allowed")).toBe(true);
    expect(esErrorFatalVoz("service-not-allowed")).toBe(true);
    expect(esErrorFatalVoz("audio-capture")).toBe(true);
    expect(esErrorFatalVoz("no-speech")).toBe(false);
    expect(esErrorFatalVoz("network")).toBe(false);
    expect(debeReanudar({ ...normal, errorFatal: true })).toBe(false);
  });
  it("si se corta en seguida una y otra vez, para (sin bucle)", () => {
    expect(debeReanudar({ ...normal, cortesRapidosSeguidos: MAX_CORTES_RAPIDOS })).toBe(false);
  });
  it("un corte rápido solo cuenta si en esa sesión no se oyó nada", () => {
    // una frase corta ("sí") dura menos de CORTE_RAPIDO_MS y no es un bucle
    expect(esCorteRapido(CORTE_RAPIDO_MS - 1, false)).toBe(true);
    expect(esCorteRapido(CORTE_RAPIDO_MS - 1, true)).toBe(false);
    expect(esCorteRapido(CORTE_RAPIDO_MS, false)).toBe(false);
  });
  it("tras 30 segundos sin oír nada, se apaga (y lo dice)", () => {
    expect(SILENCIO_MAX_MS).toBe(30_000);
    expect(debeReanudar({ ...normal, silencioMs: 29_999 })).toBe(true);
    expect(debeReanudar({ ...normal, silencioMs: 30_000 })).toBe(false);
  });
  it("useSpeech: una frase por sesión, reanuda en onend, y el campo empieza de cero en cada sesión", () => {
    const hook = readFileSync(path.join(__dirname, "useSpeech.ts"), "utf8");
    expect(hook).toMatch(/debeReanudar\(/);
    expect(hook).toMatch(/rec\.continuous = false;/);
    expect(hook).toMatch(/textoDeSesion\(lista\)/);
    // un evento vacío no borra lo que la sesión ya puso
    expect(hook).toMatch(/if \(!texto\) return;/);
    const campo = readFileSync(path.join(__dirname, "..", "app", "ui", "CampoConVoz.tsx"), "utf8");
    expect(campo).toMatch(/useSpeech\([\s\S]*?\(\) => \{\s*estadoDictado\.current = estadoDictadoInicial\(\);/);
  });
});
