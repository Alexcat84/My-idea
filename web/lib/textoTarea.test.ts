// El recorte de una tarea vive SOLO al mostrarla (contexto de la entrevista, 28 sep
// 2026): en la base y en todo lo que viaja al motor va entera. Para mostrarla en una
// lista se corta en la ultima frontera de palabra antes del tope, con "…".
import { describe, expect, it } from "vitest";
import { textoParaMostrar } from "./textoTarea";

const LARGA =
  "Haz una caminata de 20 minutos por tu área de trabajo y anota en papel o celular todo lo que podría " +
  "lastimarte: polvo de cemento en el aire, aditivos o resinas sin ficha de seguridad, cables sueltos y cargas pesadas.";

describe("textoParaMostrar", () => {
  it("un texto corto sale igual", () => {
    expect(textoParaMostrar("Llama a dos proveedores esta semana.")).toBe("Llama a dos proveedores esta semana.");
  });
  it("un texto largo se corta en frontera de palabra, con puntos suspensivos y sin pasar del tope", () => {
    const r = textoParaMostrar(LARGA, 180);
    expect(r.endsWith("…")).toBe(true);
    expect(r.length).toBeLessThanOrEqual(180);
    const cuerpo = r.slice(0, -1);
    expect(LARGA.startsWith(cuerpo)).toBe(true);
    // la letra que sigue al corte en el original es un espacio: no parte una palabra
    expect(LARGA[cuerpo.length]).toBe(" ");
  });
});
