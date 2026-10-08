// Bitácora, decisión del fundador (8 oct 2026, revierte la restricción de esa
// mañana): una tarea SÍ se puede marcar hecha con fecha ANTERIOR al inicio del
// proyecto. Esta función la reconoce para contarla como "Ya lo habías hecho".
//
// El servidor no conoce la zona horaria de la persona. La pantalla ancla el día
// elegido al MEDIODÍA local (isoDesdeInputLocal), así que el mediodía del día de
// creación queda a menos de 12 h del instante de creación, y el de un día antes,
// a 12 h o más. Regla: es anterior si completed < creado - 12 h (estricto).
// Una fecha sin hora ("2026-03-10") se lee como su mediodía UTC.
//
// Cálculo a mano, creado = 2026-03-10T15:00:00Z (creado - 12 h = 2026-03-10T03:00:00Z):
//   2026-03-10T08:00:00Z → 7 h antes  → NO es anterior (mismo día posible)
//   2026-03-10T03:00:00Z → 12 h antes → NO (el borde no cuenta)
//   2026-03-10T02:59:00Z → 12 h 1 min → SÍ
//   2026-03-09T12:00:00Z → 27 h antes → SÍ
//   "2026-03-10"         → 2026-03-10T12:00Z, 3 h antes  → NO
//   "2026-03-09"         → 2026-03-09T12:00Z, 27 h antes → SÍ
//   sin fecha de creación → NO (no hay contra qué comparar)
import { describe, expect, it } from "vitest";
import { anteriorAlInicio } from "./inicioProyecto";

const CREADO = "2026-03-10T15:00:00Z";

describe("anteriorAlInicio", () => {
  it.each([
    ["2026-03-10T08:00:00Z", false],
    ["2026-03-10T03:00:00Z", false],
    ["2026-03-10T02:59:00Z", true],
    ["2026-03-09T12:00:00Z", true],
    ["2026-03-10", false],
    ["2026-03-09", true],
  ])("%s → %s", (valor, esperado) => {
    expect(anteriorAlInicio(valor, CREADO)).toBe(esperado);
  });

  it("sin fecha de creación no bloquea", () => {
    expect(anteriorAlInicio("2020-01-01T12:00:00Z", null)).toBe(false);
    expect(anteriorAlInicio("2020-01-01T12:00:00Z", undefined)).toBe(false);
  });
});
