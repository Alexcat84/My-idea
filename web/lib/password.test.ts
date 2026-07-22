import { describe, expect, it } from "vitest";
import { passwordValida, validarPassword } from "./password";

describe("validarPassword: mín. 8, una mayúscula, un dígito (regla I Ching)", () => {
  it("acepta una contraseña que cumple las tres reglas", () => {
    expect(validarPassword("Miclave123")).toBeNull();
    expect(passwordValida("Abcdefg9")).toBe(true);
  });

  it("rechaza por corta, y lo dice en palabras", () => {
    expect(validarPassword("Ab1")).toContain("8 caracteres");
  });

  it("rechaza sin mayúscula", () => {
    expect(validarPassword("miclave123")).toContain("mayúscula");
  });

  it("rechaza sin dígito", () => {
    expect(validarPassword("Miclavesegura")).toContain("número");
  });
});
