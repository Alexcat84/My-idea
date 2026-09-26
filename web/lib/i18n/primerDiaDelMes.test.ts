// i18n F6: el primer día del mes se escribe como ordinal en francés y en
// italiano (misma clase de regla tipográfica); el resto de los días, cardinal.
//
//   - fr: "1er mars" (premier), y "2 mars", "11 mars", "21 mars": SOLO el 1
//     lleva "er" (el 21 se lee "vingt et un", cardinal; no es "21er").
//   - it: "1º marzo" (primo), "2 marzo", "11 marzo", "21 marzo".
//   - es y los demás: la cifra tal cual ("1 de marzo").
//
// Catálogo de FECHAS en francés: diaDeMes "{{d}} {{mes}}", diaDeMesAno
// "{{d}} {{mes}} {{ano}}", diaSemanaDeMes "{{dia}} {{d}} {{mes}}", meses en
// minúscula ("mars"), días en minúscula (el 1 de marzo de 2026 es domingo,
// "dimanche"). Contado a mano:
//   fechaHumanaCorta(1 mar 2026, fr)  = "1er mars"
//   fechaHumanaConAno(1 mar 2026, fr) = "1er mars 2026"
//   fechaHumana(1 mar 2026, fr)       = "dimanche 1er mars"
//   fechaHumanaCorta(21 mar 2026, fr) = "21 mars"
import { describe, expect, it } from "vitest";
import { fechaHumana, fechaHumanaConAno, fechaHumanaCorta, numeroDeDia } from "../fechas";

// Mediodía local: el día del calendario no se corre por la zona horaria.
const dia = (d: number) => new Date(2026, 2, d, 12).toISOString();

describe("numeroDeDia: el ordinal del primero del mes", () => {
  it("francés: 1er, y 2, 11, 21 cardinales", () => {
    expect(numeroDeDia(1, "fr")).toBe("1er");
    expect(numeroDeDia(2, "fr")).toBe("2");
    expect(numeroDeDia(11, "fr")).toBe("11");
    expect(numeroDeDia(21, "fr")).toBe("21");
  });
  it("italiano: 1º, y 2, 11, 21 cardinales", () => {
    expect(numeroDeDia(1, "it")).toBe("1º");
    expect(numeroDeDia(2, "it")).toBe("2");
    expect(numeroDeDia(11, "it")).toBe("11");
    expect(numeroDeDia(21, "it")).toBe("21");
  });
  it("español, inglés y portugués: la cifra tal cual", () => {
    expect(numeroDeDia(1, "es")).toBe("1");
    expect(numeroDeDia(1, "en")).toBe("1");
    expect(numeroDeDia(1, "pt")).toBe("1");
  });
});

describe("las fechas en palabras en francés", () => {
  it("el 1 de marzo de 2026", () => {
    expect(fechaHumanaCorta(dia(1), "fr")).toBe("1er mars");
    expect(fechaHumanaConAno(dia(1), "fr")).toBe("1er mars 2026");
    expect(fechaHumana(dia(1), "fr")).toBe("dimanche 1er mars");
  });
  it("el 2, el 11 y el 21, sin marca", () => {
    expect(fechaHumanaCorta(dia(2), "fr")).toBe("2 mars");
    expect(fechaHumanaCorta(dia(11), "fr")).toBe("11 mars");
    expect(fechaHumanaConAno(dia(21), "fr")).toBe("21 mars 2026");
  });
  it("en español no cambia nada", () => {
    expect(fechaHumanaCorta(dia(1), "es")).toBe("1 de marzo");
  });
});
