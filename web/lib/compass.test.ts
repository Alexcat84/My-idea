// Fase 3.0: paridad contra la recalibracion real hecha en
// scripts/build_semantic_index_voyage.py (mismos 2 casos de referencia de
// la Fase 2.9, mismo modelo voyage-4-lite). Hace llamadas REALES a Voyage
// (costo ~$0.0001, dentro de la franja gratuita de 200M tokens/mes) --
// esto es deliberado: es la unica forma de verificar que el
// embedQuery+coseno de TypeScript reproduce lo mismo que ya goberno la
// eleccion de MIN_SCORE_SALTO=0.30 en compass.ts.
import "./loadRootEnv";
import { describe, expect, it } from "vitest";
import { MIN_SCORE_SALTO, buscarAfines } from "./compass";

const QUERY_POSITIVA = "no he calculado bien cuanto me cuesta cada pieza";
const NODO_ESPERADO_POSITIVO = "hoja_estimacion_costos";
const QUERY_NEGATIVA = "mi resina hace burbujas y mi QR grabado con laser se borra";
const NODO_ESPERADO_EXCLUIDO = "alfabetizacion_en_materiales_maliciosos";

describe("buscarAfines (Voyage AI real) -- mismos 2 casos de referencia de la Fase 2.9", () => {
  it(`query positiva encuentra '${NODO_ESPERADO_POSITIVO}' por encima de MIN_SCORE_SALTO`, async () => {
    // Calculado por scripts/build_semantic_index_voyage.py: score=0.3507
    const candidatos = await buscarAfines(QUERY_POSITIVA, new Set(), { k: 8, minScore: MIN_SCORE_SALTO });
    const encontrado = candidatos.find((c) => c.id === NODO_ESPERADO_POSITIVO);
    expect(encontrado).toBeDefined();
    expect(encontrado!.score).toBeGreaterThan(MIN_SCORE_SALTO);
    expect(encontrado!.score).toBeCloseTo(0.3507, 1);
  }, 15000);

  it(`query negativa NO ofrece '${NODO_ESPERADO_EXCLUIDO}' (queda bajo el umbral)`, async () => {
    // Calculado por scripts/build_semantic_index_voyage.py: score=0.2581
    const candidatosSinFiltro = await buscarAfines(QUERY_NEGATIVA, new Set(), { k: 20, minScore: 0.0 });
    const crudo = candidatosSinFiltro.find((c) => c.id === NODO_ESPERADO_EXCLUIDO);
    expect(crudo).toBeDefined();
    expect(crudo!.score).toBeCloseTo(0.2581, 1);
    expect(crudo!.score).toBeLessThan(MIN_SCORE_SALTO);

    const candidatosConFiltro = await buscarAfines(QUERY_NEGATIVA, new Set(), { k: 8, minScore: MIN_SCORE_SALTO });
    expect(candidatosConFiltro.find((c) => c.id === NODO_ESPERADO_EXCLUIDO)).toBeUndefined();
  }, 15000);

  it("excluye ids ya visitados", async () => {
    const candidatos = await buscarAfines(QUERY_POSITIVA, new Set([NODO_ESPERADO_POSITIVO]), { k: 8, minScore: 0.0 });
    expect(candidatos.find((c) => c.id === NODO_ESPERADO_POSITIVO)).toBeUndefined();
  }, 15000);
});

describe("buscarAfines: fallback silencioso sin VOYAGE_API_KEY", () => {
  it("devuelve [] sin lanzar si falta la API key (navegacion solo local)", async () => {
    const original = process.env.VOYAGE_API_KEY;
    delete process.env.VOYAGE_API_KEY;
    try {
      const candidatos = await buscarAfines("cualquier texto", new Set());
      expect(candidatos).toEqual([]);
    } finally {
      process.env.VOYAGE_API_KEY = original;
    }
  });

  it("texto vacio devuelve [] sin llamar a la API", async () => {
    expect(await buscarAfines("", new Set())).toEqual([]);
    expect(await buscarAfines("   ", new Set())).toEqual([]);
  });
});
