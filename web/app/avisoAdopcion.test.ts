// AUD-09 H07: si la adopción de las ideas del invitado queda pendiente, la
// pantalla lo dice (fallar en voz alta, BANCO §9). Antes el usuario veía /ideas
// vacío o "esa idea no existe o no es tuya".
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { MENSAJE_ADOPCION_PENDIENTE, mensajeAdopcionPendiente } from "@/lib/constants";

const leer = (rel: string) => readFileSync(path.join(__dirname, rel), "utf8");

describe("el aviso de adopción pendiente llega a la pantalla", () => {
  it("dice que se reintenta y que nada se perdió", () => {
    expect(MENSAJE_ADOPCION_PENDIENTE).toMatch(/reintento/);
    expect(MENSAJE_ADOPCION_PENDIENTE).toMatch(/no se perdió nada/);
    expect(mensajeAdopcionPendiente("es")).toBe(MENSAJE_ADOPCION_PENDIENTE);
  });
  it("/ideas lo muestra con adopcion=pendiente", () => {
    const f = leer("ideas/page.tsx");
    // i18n: el aviso se elige por el idioma de la interfaz (misma fuente).
    expect(f).toContain("mensajeAdopcionPendiente(idioma)");
    expect(f).toMatch(/adopcion === "pendiente"/);
  });
  it("la página de la idea lo muestra en vez de 'esa idea no existe o no es tuya'", () => {
    expect(leer("idea/[id]/IdeaView.tsx")).toContain("mensajeAdopcionPendiente(idioma)");
  });
  it("el login lleva el aviso al destino", () => {
    expect(leer("login/page.tsx")).toMatch(/adopcion_pendiente/);
  });
});
