// Campaña "Espacios" — la cara "Tu avance": los hitos por espacio, calculados a
// mano (fechas conocidas) antes del assert (regla AGENTS.md).
import { describe, expect, it } from "vitest";
import { hitosDeEspacio } from "./hitosEspacio";

describe("hitosDeEspacio: el core cuenta su historia desde La Chispa", () => {
  const base = hitosDeEspacio({
    espacio: "core",
    chispaAt: "2026-01-01T00:00:00Z",
    claridadAt: "2026-01-01T00:05:00Z",
    planAt: "2026-01-02T00:00:00Z",
    realizadaAt: null,
    items: [
      { texto: "Habla con un desconocido", completedAt: "2026-01-05T00:00:00Z" },
      { texto: "Cobra tu primera venta", completedAt: "2026-01-04T00:00:00Z" }, // fuera de orden a propósito
      { texto: "Tarea pendiente", completedAt: null }, // sin fecha: NO aparece
    ],
  });

  it("orden: Chispa · Claridad · Plan · acciones (por fecha) · cierre pendiente", () => {
    expect(base.map((h) => h.etiqueta)).toEqual([
      "La Chispa",
      "Claridad",
      "Tu Plan",
      "Cobra tu primera venta", // 04 antes que 05
      "Habla con un desconocido",
      "El cierre",
    ]);
  });
  it("una acción sin completed_at no es hito", () => {
    expect(base.some((h) => h.etiqueta === "Tarea pendiente")).toBe(false);
  });
  it("sin realizada, el cierre es pendiente (gris)", () => {
    const cierre = base.at(-1)!;
    expect(cierre.tipo).toBe("cierre");
    expect(cierre.alcanzado).toBe(false);
    expect(cierre.fecha).toBeNull();
  });
  it("con realizada, el cierre es 'Realizada' y alcanzado", () => {
    const cerrado = hitosDeEspacio({ espacio: "core", chispaAt: "2026-01-01T00:00:00Z", planAt: "2026-01-02T00:00:00Z", realizadaAt: "2026-02-01T00:00:00Z", items: [] });
    const cierre = cerrado.at(-1)!;
    expect(cierre.etiqueta).toBe("Realizada");
    expect(cierre.alcanzado).toBe(true);
  });
  it("un arranque sin fecha (Claridad null) no se dibuja", () => {
    const sinClaridad = hitosDeEspacio({ espacio: "core", chispaAt: "2026-01-01T00:00:00Z", claridadAt: null, planAt: "2026-01-02T00:00:00Z", realizadaAt: null, items: [] });
    expect(sinClaridad.some((h) => h.etiqueta === "Claridad")).toBe(false);
    expect(sinClaridad.map((h) => h.etiqueta)).toEqual(["La Chispa", "Tu Plan", "El cierre"]);
  });
});

describe("hitosDeEspacio: un mundo cuenta desde su diagnóstico", () => {
  const mundo = hitosDeEspacio({
    espacio: "mundo",
    nombre: "Calidad y Confianza",
    diagnosticoAt: "2026-03-01T00:00:00Z",
    planAt: "2026-03-02T00:00:00Z",
    cerradoAt: "2026-03-20T00:00:00Z",
    items: [{ texto: "Llama a un cliente que se fue", completedAt: "2026-03-10T00:00:00Z" }],
  });
  it("orden: diagnóstico · su plan · acción · cerrado (alcanzado)", () => {
    expect(mundo.map((h) => h.etiqueta)).toEqual([
      "Tu diagnóstico",
      "El plan de Calidad y Confianza",
      "Llama a un cliente que se fue",
      "Cerrado",
    ]);
    expect(mundo.at(-1)!.alcanzado).toBe(true);
  });
  it("el core NO trae hitos de mundo (cada espacio, lo suyo)", () => {
    // Partición: la entrada del core no conoce mundos; sus items ya vienen
    // scopeados por dominio en la UI (grupoVigente). Aquí lo garantiza el tipo.
    const core = hitosDeEspacio({ espacio: "core", chispaAt: "2026-01-01T00:00:00Z", planAt: "2026-01-02T00:00:00Z", realizadaAt: null, items: [] });
    expect(core.some((h) => h.tipo === "diagnostico")).toBe(false);
  });
});
