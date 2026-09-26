/**
 * Decisión del fundador (26 sep 2026): "Esta semana" aparece UNA sola vez en
 * Manos a la Obra, calculado por la app (lib/estaSemana.ts, probado allí con
 * los cálculos a mano). Este contrato cuida el cableado: el bloque sale del
 * cálculo puro, con el modo y la capacidad DEL ESPACIO, y la chapa de la fila a
 * mi ritmo ya no dice "esta semana" (la destacada es la primera acción de su
 * etapa, sin plazo).
 */
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { ACTIVE_LOCALES } from "@/lib/i18n/config";
import { MANOS_A_LA_OBRA } from "@/lib/i18n/mensajes/manosALaObra";

const src = readFileSync(path.join(__dirname, "ManosALaObra.tsx"), "utf8");

describe("Manos a la Obra: el bloque 'Esta semana' calculado", () => {
  it("usa el cálculo puro con la primera acción del plan", () => {
    expect(src).toMatch(/calcularEstaSemana\(\{ items, modo, capacidad, primerasAcciones \}\)/);
    expect(src).toMatch(/primerasAccionesDelPlan\(planMd\)/);
  });

  it("el núcleo lo pinta con SU modo y SU capacidad; el mundo, en su hub, con los suyos", () => {
    expect(src).toMatch(/<BloqueSemana\s+items=\{itemsCore\}[\s\S]*?modo=\{modoCamino\}[\s\S]*?capacidad=\{capacidadDe\(ESPACIO_CORE\)\}/);
    expect(src).toMatch(/<BloqueSemana\s+items=\{items\}[\s\S]*?modo=\{modoMundo\}[\s\S]*?capacidad=\{capacidadDe\(mundo\.dominio\)\}/);
    // Una sola vez por espacio: dos usos (núcleo y hub del mundo), no uno por etapa.
    expect(src.match(/<BloqueSemana\b/g)).toHaveLength(2);
  });

  it("a mi ritmo el título es 'Tu siguiente paso' y la chapa de la fila, 'primera acción'", () => {
    expect(src).toContain('bloque.modo === "semana" ? t.semana.titulo : t.semana.tituloRitmo');
    expect(src).toContain('modo === "fechas" ? t.fila.estaSemana : t.fila.primeraAccion');
    expect(MANOS_A_LA_OBRA.es.semana.titulo).toBe("Esta semana");
    expect(MANOS_A_LA_OBRA.es.semana.tituloRitmo).toBe("Tu siguiente paso");
    expect(MANOS_A_LA_OBRA.es.fila.primeraAccion).toBe("primera acción");
  });

  it("los textos del bloque existen en los once idiomas, sin guiones largos", () => {
    for (const l of ACTIVE_LOCALES) {
      const s = MANOS_A_LA_OBRA[l]!.semana;
      for (const v of Object.values(s)) {
        expect(v.trim()).not.toBe("");
        expect(v).not.toMatch(/[—–]/);
      }
      expect(s.tambienCabe).toContain("{{horas}}");
    }
  });
});
