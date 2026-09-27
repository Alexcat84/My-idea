// i18n F3: la palabra que confirma el borrado de la cuenta era "ELIMINAR" fija
// en el cliente y en el servidor. Ahora cada idioma tiene la suya (el
// compilador la exige en cada idioma activo) y el servidor acepta la del
// idioma de quien pide y SIEMPRE la del español (quien cambia de idioma a
// mitad del borrado, o un cliente viejo, no queda encerrado).
// Casos a mano: "ELIMINAR" y " eliminar " valen (el servidor recorta y pasa a
// mayúsculas, como antes); "BORRAR", "" y un número no valen.
import { describe, expect, it } from "vitest";
import { ACTIVE_LOCALES } from "./config";
import { esPalabraEliminar, palabraEliminar } from "./palabraEliminar";

describe("palabra de confirmación del borrado", () => {
  it("en español es ELIMINAR, como siempre", () => {
    expect(palabraEliminar("es")).toBe("ELIMINAR");
  });
  it("el servidor acepta la palabra recortada y en cualquier caja", () => {
    expect(esPalabraEliminar("ELIMINAR", "es")).toBe(true);
    expect(esPalabraEliminar(" eliminar ", "es")).toBe(true);
  });
  it("lo demás no vale", () => {
    expect(esPalabraEliminar("BORRAR", "es")).toBe(false);
    expect(esPalabraEliminar("", "es")).toBe(false);
    expect(esPalabraEliminar(undefined, "es")).toBe(false);
    expect(esPalabraEliminar(12, "es")).toBe(false);
  });
  it("en cualquier idioma activo vale la suya y la del español", () => {
    for (const idioma of ACTIVE_LOCALES) {
      expect(esPalabraEliminar(palabraEliminar(idioma), idioma), idioma).toBe(true);
      expect(esPalabraEliminar(palabraEliminar(idioma).toLowerCase(), idioma), idioma).toBe(true);
      expect(esPalabraEliminar("ELIMINAR", idioma), idioma).toBe(true);
    }
  });
});
