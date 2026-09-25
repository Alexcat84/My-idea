// i18n F2: en español los formatos con Intl dan EXACTAMENTE lo de hoy. Se
// comparan contra las funciones a mano que reemplazan (copiadas aquí tal cual
// estaban: money() de TusNumeros y pesos() de numerosVivo) y contra toFixed.
import { describe, expect, it } from "vitest";
import { decimal, dinero, entero } from "./formato";

// money() de app/ui/TusNumeros.tsx antes de F2, tal cual.
function moneyDeHoy(n: number): string {
  const neg = n < 0;
  const r = Math.round(Math.abs(n));
  const s = String(r).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  return (neg ? "-$" : "$") + s;
}

const VALORES = [0, 1, 9, 170, 999, 999.5, 1000, 1200, 1234.4, 12_000, 123_456, 1_234_567, 98_765_432, -1, -170, -1200, -1_234_567, 0.4, -0.4];

describe("formato con Intl, idéntico en español", () => {
  it("dinero = money() de hoy en todos los valores de prueba", () => {
    for (const v of VALORES) expect(dinero("es", v), String(v)).toBe(moneyDeHoy(v));
  });
  it("casos a mano: $1.200, $170, -$1.234.567", () => {
    expect(dinero("es", 1200)).toBe("$1.200");
    expect(dinero("es", 170)).toBe("$170");
    expect(dinero("es", -1_234_567)).toBe("-$1.234.567");
  });
  it("entero agrupa siempre con punto: 1.200 (cuatro cifras también)", () => {
    expect(entero("es", 1200)).toBe("1.200");
    expect(entero("es", 12_345_678)).toBe("12.345.678");
    expect(entero("es", -1200)).toBe("-1.200");
    expect(entero("es", 999)).toBe("999");
  });
  it("decimal = toFixed en español", () => {
    for (const v of [0, 1, 1.05, 1.25, 1.45, 12.5, 99.94, 99.96, 1234.56, -3.14159]) {
      expect(decimal("es", v, 1), String(v)).toBe(v.toFixed(1));
      expect(decimal("es", v, 2), String(v)).toBe(v.toFixed(2));
    }
  });
});
