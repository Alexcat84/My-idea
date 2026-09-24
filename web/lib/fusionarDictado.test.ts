// AUD-09 B14b (tanda 7A, datos): el texto PROVISIONAL del dictado se pintaba en
// el campo pero nunca llegaba al valor: pulsar "Continuar" o "Enviar" mientras
// se dictaba, o detener el micrófono, lo perdía. Ahora lo provisional vive
// DENTRO del valor como un sufijo que el siguiente trozo reemplaza. Casos a mano.
import { describe, expect, it } from "vitest";
import { fusionarDictado } from "./fusionarDictado";

describe("fusionarDictado (AUD-09 B14b)", () => {
  it("lo provisional entra al valor", () => {
    expect(fusionarDictado("", "", "", "hola")).toEqual({ valor: "hola", sufijo: "hola" });
    expect(fusionarDictado("tengo", "", "", "dos")).toEqual({ valor: "tengo dos", sufijo: " dos" });
  });

  it("el final reemplaza a su provisional, sin duplicar", () => {
    expect(fusionarDictado("hola", "hola", "hola mundo", "")).toEqual({ valor: "hola mundo", sufijo: "" });
    expect(fusionarDictado("tengo dos", " dos", "dos clientes", "y")).toEqual({ valor: "tengo dos clientes y", sufijo: " y" });
  });

  it("si el usuario editó a mano, lo suyo se respeta y el dictado sigue encima", () => {
    // el sufijo " dos" ya no está al final: no se recorta nada
    expect(fusionarDictado("tengo tres", " dos", "", "más")).toEqual({ valor: "tengo tres más", sufijo: " más" });
  });
});
