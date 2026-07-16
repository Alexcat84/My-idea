// Fase 4.3.1 — fechaSello: el timestamp que ancla el historial en el
// calendario. `ahora` se inyecta para que los casos sean deterministas (sin
// esto, un test de fechas envejece y miente en verde). Todos calculados a mano.
import { describe, expect, it } from "vitest";
import { fechaSello } from "./fechas";

// Ancla de "ahora": jueves 16 de julio de 2026, 14:05 hora local.
const AHORA = new Date(2026, 6, 16, 14, 5, 0);

describe("fechaSello", () => {
  it("hoy → 'hoy HH:MM' (la hora, no la fecha: es de hace un rato)", () => {
    expect(fechaSello(new Date(2026, 6, 16, 9, 30).toISOString(), AHORA)).toBe("hoy 09:30");
    expect(fechaSello(new Date(2026, 6, 16, 14, 5).toISOString(), AHORA)).toBe("hoy 14:05");
  });

  it("ayer → 'ayer HH:MM'", () => {
    expect(fechaSello(new Date(2026, 6, 15, 20, 0).toISOString(), AHORA)).toBe("ayer 20:00");
  });

  it("este año, más de un día → 'D mes' SIN año (no se repite el año actual)", () => {
    expect(fechaSello(new Date(2026, 6, 14, 11, 0).toISOString(), AHORA)).toBe("14 jul");
    expect(fechaSello(new Date(2026, 2, 3, 8, 0).toISOString(), AHORA)).toBe("3 mar");
  });

  it("otro año → 'D mes AÑO' (el año ancla lo viejo)", () => {
    expect(fechaSello(new Date(2025, 11, 31, 23, 0).toISOString(), AHORA)).toBe("31 dic 2025");
    expect(fechaSello(new Date(2024, 0, 1, 0, 0).toISOString(), AHORA)).toBe("1 ene 2024");
  });

  it("minutos con cero a la izquierda (04, no 4)", () => {
    expect(fechaSello(new Date(2026, 6, 16, 8, 4).toISOString(), AHORA)).toBe("hoy 08:04");
  });

  it("'ayer' se decide por FECHA de calendario, no por 24h exactas", () => {
    // 23:50 de ayer a 14:05 de hoy son <24h, pero es AYER (otro día del reloj).
    expect(fechaSello(new Date(2026, 6, 15, 23, 50).toISOString(), AHORA)).toBe("ayer 23:50");
    // Y 00:10 de hoy es HOY aunque hayan pasado casi 14h.
    expect(fechaSello(new Date(2026, 6, 16, 0, 10).toISOString(), AHORA)).toBe("hoy 00:10");
  });
});
