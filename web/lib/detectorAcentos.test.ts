import { describe, it, expect } from "vitest";
import { detectarFaltaDeAcentos } from "./detectorAcentos";

describe("detectarFaltaDeAcentos (Fase 3.9 D11)", () => {
  it("no marca texto correctamente acentuado", () => {
    // Todas las palabras de riesgo, bien acentuadas -> cero sospechosos.
    const bueno =
      "El análisis de la cláusula es lógico; según el método, revisa la " +
      "validación y la restricción crítica en la próxima página. También " +
      "cuenta los días y los créditos.";
    expect(detectarFaltaDeAcentos(bueno)).toEqual([]);
  });

  it("marca terminaciones -cion/-sion sin tilde", () => {
    const malo = "La validacion y la decision dependen de la restriccion.";
    // esperado (orden alfabetico): decision, restriccion, validacion
    expect(detectarFaltaDeAcentos(malo).sort()).toEqual(["decision", "restriccion", "validacion"]);
  });

  it("marca palabras de la lista curada sin tilde", () => {
    const malo = "El analisis usa una logica basica; revisa los numeros aqui.";
    // esperado (orden alfabetico): analisis, aqui, basica, logica, numeros
    expect(detectarFaltaDeAcentos(malo).sort()).toEqual(["analisis", "aqui", "basica", "logica", "numeros"]);
  });

  it("no confunde palabras ambiguas validas sin tilde", () => {
    // "mas" (pero), "esta" (esta cosa), "si" (condicional), "solo" (unicamente)
    // son todas formas validas sin tilde: no deben marcarse.
    const ambiguo = "Si vendes mas de lo que esta en tu plan, solo ajusta el precio.";
    expect(detectarFaltaDeAcentos(ambiguo)).toEqual([]);
  });
});
