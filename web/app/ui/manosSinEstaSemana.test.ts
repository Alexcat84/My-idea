// Decisión del fundador (27 sep 2026): en Manos a la Obra, "Esta semana"
// desaparece de las tarjetas de cada etapa, en los once idiomas: la chapa de la
// tarea destacada dice "primera acción" en los dos modos, y ya no existe una
// chapa "esta semana" por fecha. Solo queda el bloque único de arriba
// (BloqueSemana, calculado por la app).
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { ACTIVE_LOCALES } from "@/lib/i18n/config";
import { MANOS_A_LA_OBRA } from "@/lib/i18n/mensajes/manosALaObra";

const src = readFileSync(path.join(__dirname, "ManosALaObra.tsx"), "utf8");

describe("las tarjetas de etapa ya no dicen 'esta semana'", () => {
  it.each([...ACTIVE_LOCALES])("%s: el catálogo de las filas ya no tiene la chapa 'esta semana'", (idioma) => {
    expect((MANOS_A_LA_OBRA[idioma].fila as Record<string, unknown>).estaSemana).toBeUndefined();
    expect(MANOS_A_LA_OBRA[idioma].fila.primeraAccion.trim()).not.toBe("");
  });

  it("la chapa de la fila es la de la tarea destacada (primera acción), en los dos modos", () => {
    expect(src).not.toMatch(/t\.fila\.estaSemana/);
    expect(src).not.toMatch(/chapaEstaSemana/);
    expect(src).toMatch(/item\.destacado && \([\s\S]{0,900}\{t\.fila\.primeraAccion\}/);
  });

  it("el bloque único de arriba se conserva", () => {
    expect(src).toMatch(/function BloqueSemana\(/);
    expect(src).toMatch(/<BloqueSemana/);
  });
});
