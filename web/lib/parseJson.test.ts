import { describe, expect, it } from "vitest";
import { parsearJson } from "./parseJson";

describe("parsearJson", () => {
  it("parsea JSON plano", () => {
    expect(parsearJson('{"a": 1}')).toEqual({ a: 1 });
  });

  it("quita el cerco ```json ... ```", () => {
    expect(parsearJson('```json\n{"a": 1}\n```')).toEqual({ a: 1 });
  });

  it("toma solo el primer objeto si el modelo agrega texto despues", () => {
    expect(parsearJson('{"a": 1}\n\nNota: esto es solo un ejemplo.')).toEqual({ a: 1 });
  });

  it("respeta llaves dentro de strings al contar profundidad", () => {
    expect(parsearJson('{"a": "texto con { llave } adentro"}')).toEqual({
      a: "texto con { llave } adentro",
    });
  });

  it("lanza si no hay JSON valido", () => {
    expect(() => parsearJson("esto no es json")).toThrow();
  });
});
