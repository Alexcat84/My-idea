// AUD-09 M49 (tanda 7A, seguridad; decisión del fundador 25 sep 2026): el
// centro de cuenta prometía "Un segundo paso al entrar protege tu cuenta", y
// el candado cubre los usos de créditos y los borrados, no la entrada. REGLA:
// cuando una función falta, el texto no puede prometerla. El texto dice lo que
// protege; el doble factor al entrar queda como función futura en su ficha.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const src = readFileSync(path.join(__dirname, "CuentaCliente.tsx"), "utf8");
// i18n F2: el copy del centro de cuenta vive en su catálogo; el componente lo pinta desde ahí.
const catalogo = readFileSync(path.join(__dirname, "..", "..", "lib", "i18n", "mensajes", "cuenta.ts"), "utf8");

describe("el doble factor dice exactamente lo que protege (AUD-09 M49)", () => {
  it("no promete proteger la entrada", () => {
    expect(src).not.toMatch(/al entrar/);
    expect(catalogo).not.toMatch(/al entrar/);
  });
  it("dice que cubre usar créditos y borrar una idea o la cuenta", () => {
    expect(catalogo).toContain(
      "Te pide un segundo paso antes de usar tus créditos y antes de borrar una idea o tu cuenta. Es opcional y puedes apagarlo cuando quieras."
    );
    expect(src).toContain("{t.seguridad.queHace}");
  });
});
