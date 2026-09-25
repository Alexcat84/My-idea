// AUD-09 M48 (tanda 7B, confianza): el registro de un mundo de protección solo
// se muestra (en pantalla y en papel) cuando el mundo YA tiene su plan. Vacío,
// decía "se llenará con el plan de este mundo": falso, el plan ya llegó; lo que
// pasó es que el enlace con las actividades del núcleo falló. Se dice eso, con
// una sola frase para la pantalla y el papel.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { REGISTRO_VACIO, registroMarkdown } from "./registroProteccion";
import { REGISTRO_PROTECCION } from "./i18n/mensajes/registroProteccion";

describe("el registro vacío dice lo que pasó (AUD-09 M48)", () => {
  it("la frase no promete que se llenará", () => {
    expect(REGISTRO_VACIO).toBe(
      "No alcancé a enlazar este plan con tus actividades: sus respuestas están en tu plan, pero este registro quedó vacío."
    );
  });
  it("el papel la usa", () => {
    expect(registroMarkdown("Riesgos Bajo Control", [])).toContain(REGISTRO_VACIO);
  });
  it("la pantalla la usa", () => {
    const manos = readFileSync(path.join(__dirname, "..", "app", "ui", "ManosALaObra.tsx"), "utf8");
    // i18n: la pantalla elige la frase del catálogo por su idioma; el catálogo
    // base es la misma frase que REGISTRO_VACIO.
    expect(manos).toMatch(/\{tr\.registroVacio\}/);
    expect(manos).toMatch(/const tr = elegir\(REGISTRO_PROTECCION, idioma\);/);
    expect(REGISTRO_PROTECCION.es.registroVacio).toBe(REGISTRO_VACIO);
    expect(manos).not.toMatch(/se llenará con el plan de este mundo/);
  });
});
