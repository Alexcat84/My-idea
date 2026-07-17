// Fase 4.3.2 — fechaSello HÍBRIDO: la marca de tiempo de la UI viva (relativo
// para lo reciente, absoluto como ancla). `ahora` se inyecta para que los casos
// sean deterministas (sin esto, un test de fechas envejece y miente en verde).
// Todos calculados a mano.
//
// Regla del fundador: "la UI respira, las actas constan". Esta función es SOLO
// UI; los registros (acta, informe .md, análisis) van en absoluto y NO la usan.
import { describe, expect, it } from "vitest";
import { fechaSello } from "./fechas";

// Ancla de "ahora": jueves 16 de julio de 2026, 14:05 hora local.
const AHORA = new Date(2026, 6, 16, 14, 5, 0);
const t = (y: number, m: number, d: number, hh = 0, mm = 0) => new Date(y, m, d, hh, mm).toISOString();

describe("fechaSello — híbrido (UI viva)", () => {
  it("< 2 min → 'hace un momento'", () => {
    expect(fechaSello(t(2026, 6, 16, 14, 4), AHORA)).toBe("hace un momento");
  });

  it("minutos recientes → 'hace N min' (relativo, se siente inmediato)", () => {
    expect(fechaSello(t(2026, 6, 16, 13, 44), AHORA)).toBe("hace 21 min");
    expect(fechaSello(t(2026, 6, 16, 13, 6), AHORA)).toBe("hace 59 min");
  });

  it("hoy, más de una hora → 'hoy HH:MM' (ancla absoluta)", () => {
    expect(fechaSello(t(2026, 6, 16, 8, 14), AHORA)).toBe("hoy 08:14");
    expect(fechaSello(t(2026, 6, 16, 13, 5), AHORA)).toBe("hoy 13:05"); // 60 min justos
  });

  it("ayer → 'ayer HH:MM'", () => {
    expect(fechaSello(t(2026, 6, 15, 21, 26), AHORA)).toBe("ayer 21:26");
  });

  it("2 a 6 días → 'hace N días' (relativo), por días de CALENDARIO", () => {
    expect(fechaSello(t(2026, 6, 13, 11, 0), AHORA)).toBe("hace 3 días");
    // 14 jul 23:50 a 16 jul 14:05 son <48h pero 2 días de calendario -> "hace 2 días"
    expect(fechaSello(t(2026, 6, 14, 23, 50), AHORA)).toBe("hace 2 días");
    expect(fechaSello(t(2026, 6, 10, 9, 0), AHORA)).toBe("hace 6 días");
  });

  it("7+ días, este año → fecha absoluta con mes completo, sin año", () => {
    expect(fechaSello(t(2026, 6, 9, 9, 0), AHORA)).toBe("9 de julio");
    expect(fechaSello(t(2026, 2, 12, 8, 0), AHORA)).toBe("12 de marzo");
  });

  it("otro año → fecha absoluta con el año (ancla lo viejo)", () => {
    expect(fechaSello(t(2025, 11, 31, 23, 0), AHORA)).toBe("31 de diciembre de 2025");
    expect(fechaSello(t(2024, 0, 1, 0, 0), AHORA)).toBe("1 de enero de 2024");
  });

  it("minutos con cero a la izquierda en la hora ancla (08, no 8)", () => {
    expect(fechaSello(t(2026, 6, 16, 8, 4), AHORA)).toBe("hoy 08:04");
  });

  it("'ayer' y 'hoy' se deciden por FECHA de calendario, no por 24h exactas", () => {
    // 00:10 de hoy es HOY aunque hayan pasado casi 14h.
    expect(fechaSello(t(2026, 6, 16, 0, 10), AHORA)).toBe("hoy 00:10");
  });
});
