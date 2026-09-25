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

// i18n F3: el formato de cada idioma (D6: Intl por idioma, símbolo "$" por
// ahora). Lo esperado se escribe a mano desde las reglas de cada idioma (CLDR),
// no copiando lo que devuelve la función:
//   - miles: en/ja/zh/ko/ar/hi "," ; pt/de/it "." ; fr espacio fino U+202F.
//     hi agrupa a la india: 1234567 -> 12,34,567 (lakh).
//   - decimales: en/ja/zh/ko/ar/hi "." ; pt/fr/de/it ",".
//   - el "$": delante y pegado en en/ja/zh/ko/hi ($1,200); delante con espacio
//     duro U+00A0 en pt ($ 1.200, como "R$ 1.200"); detrás con U+00A0 en fr, de,
//     it (1 200 $, 1.200 $). El signo menos va delante de todo.
//   - cifras latinas en todos (también ar e hi): el servidor y el navegador
//     deben dar lo mismo, y el "ar" de Intl cambia de cifras según la versión.
const NB = " "; // espacio duro
const FINO = " "; // espacio fino duro (miles en francés)
describe("formato por idioma (i18n F3)", () => {
  it("dinero: 1.200 y -1.234.567 en cada idioma", () => {
    const casos: Array<[Parameters<typeof dinero>[0], string, string]> = [
      ["en", "$1,200", "-$1,234,567"],
      ["pt", `$${NB}1.200`, `-$${NB}1.234.567`],
      ["fr", `1${FINO}200${NB}$`, `-1${FINO}234${FINO}567${NB}$`],
      ["de", `1.200${NB}$`, `-1.234.567${NB}$`],
      ["it", `1.200${NB}$`, `-1.234.567${NB}$`],
      ["ja", "$1,200", "-$1,234,567"],
      ["zh", "$1,200", "-$1,234,567"],
      ["ko", "$1,200", "-$1,234,567"],
      ["hi", "$1,200", "-$12,34,567"],
    ];
    for (const [idioma, mil, neg] of casos) {
      expect(dinero(idioma, 1200), idioma).toBe(mil);
      expect(dinero(idioma, -1_234_567), idioma).toBe(neg);
    }
  });
  it("dinero redondea a entero y no escribe '-$0' fuera del español", () => {
    // 999.5 -> 1000 ; 170.4 -> 170 ; -0.4 -> 0 (sin signo)
    expect(dinero("en", 999.5)).toBe("$1,000");
    expect(dinero("en", 170.4)).toBe("$170");
    expect(dinero("en", -0.4)).toBe("$0");
    expect(dinero("de", 999.5)).toBe(`1.000${NB}$`);
  });
  it("el árabe usa el símbolo $ y cifras latinas (nunca 'US$' ni ١٢٣)", () => {
    const s = dinero("ar", 1200);
    expect(s).toContain("1,200");
    expect(s).toContain("$");
    expect(s).not.toContain("US");
    expect(s).not.toMatch(/[٠-٩]/);
  });
  it("entero: 1200 y 1234567 agrupados en cada idioma", () => {
    expect(entero("en", 1200)).toBe("1,200");
    expect(entero("pt", 1200)).toBe("1.200");
    expect(entero("fr", 1_234_567)).toBe(`1${FINO}234${FINO}567`);
    expect(entero("de", 1200)).toBe("1.200");
    expect(entero("it", 1200)).toBe("1.200");
    expect(entero("ja", 1_234_567)).toBe("1,234,567");
    expect(entero("hi", 1_234_567)).toBe("12,34,567");
    expect(entero("ar", 1200)).toBe("1,200");
    expect(entero("en", -1200)).toBe("-1,200");
  });
  it("decimal: 12.5 con el separador de cada idioma, sin agrupar", () => {
    expect(decimal("en", 12.5)).toBe("12.5");
    expect(decimal("pt", 12.5)).toBe("12,5");
    expect(decimal("fr", 12.5)).toBe("12,5");
    expect(decimal("de", 1234.56, 2)).toBe("1234,56");
    expect(decimal("it", 12.5)).toBe("12,5");
    expect(decimal("ja", 12.5)).toBe("12.5");
    expect(decimal("ar", 12.5)).toBe("12.5");
    expect(decimal("hi", 1234.5)).toBe("1234.5");
  });
});
