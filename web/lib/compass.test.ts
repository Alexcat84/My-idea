// Fase 3.0.1: paridad de calibracion en DOS capas.
// Capa 1 (offline, corre siempre): verifica los 2 casos de referencia de la
// Fase 2.9 contra el fixture web/lib/testFixtures/compass_refs.json con
// coseno local -- cero red, cero secretos, verificable en un clon limpio.
// Capa 2 (Voyage real, solo si hay VOYAGE_API_KEY): confirma que
// embedQuery+coseno de TypeScript reproduce en vivo los mismos scores que
// gobernaron MIN_SCORE_SALTO=0.30. En un clon sin key se SALTA, no falla.
import "./loadRootEnv";
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { MIN_SCORE_SALTO, buscarAfines } from "./compass";

const QUERY_POSITIVA = "no he calculado bien cuanto me cuesta cada pieza";
const NODO_ESPERADO_POSITIVO = "hoja_estimacion_costos";
const QUERY_NEGATIVA = "mi resina hace burbujas y mi QR grabado con laser se borra";
const NODO_ESPERADO_EXCLUIDO = "alfabetizacion_en_materiales_maliciosos";
const SCORE_REF_POSITIVO = 0.3507;
const SCORE_REF_NEGATIVO = 0.2581;

const TIENE_VOYAGE = Boolean(process.env.VOYAGE_API_KEY);

function coseno(a: number[], b: number[]): number {
  let dot = 0;
  let na = 0;
  let nb = 0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i];
    na += a[i] * a[i];
    nb += b[i] * b[i];
  }
  return dot / (Math.sqrt(na) * Math.sqrt(nb));
}

describe("calibracion offline (fixture, sin red)", () => {
  const fixturePath = path.resolve(__dirname, "testFixtures", "compass_refs.json");
  const fixture = JSON.parse(readFileSync(fixturePath, "utf-8")) as {
    model: string;
    query_positiva: { texto: string; embedding: number[] };
    query_negativa: { texto: string; embedding: number[] };
  };
  const indexPath = path.resolve(__dirname, "assets", "semantic_index.json");
  const index = JSON.parse(readFileSync(indexPath, "utf-8")) as {
    model: string;
    ids: string[];
    embeddings: number[][];
  };

  function scoreContra(nodoId: string, queryEmbedding: number[]): number {
    const idx = index.ids.indexOf(nodoId);
    expect(idx).toBeGreaterThanOrEqual(0);
    return coseno(queryEmbedding, index.embeddings[idx]);
  }

  it("el fixture y el indice usan el mismo modelo", () => {
    expect(fixture.model).toBe(index.model);
    expect(fixture.query_positiva.texto).toBe(QUERY_POSITIVA);
    expect(fixture.query_negativa.texto).toBe(QUERY_NEGATIVA);
  });

  it(`caso positivo: '${NODO_ESPERADO_POSITIVO}' supera MIN_SCORE_SALTO`, () => {
    const score = scoreContra(NODO_ESPERADO_POSITIVO, fixture.query_positiva.embedding);
    expect(score).toBeCloseTo(SCORE_REF_POSITIVO, 1);
    expect(score).toBeGreaterThan(MIN_SCORE_SALTO);
  });

  it(`caso negativo: '${NODO_ESPERADO_EXCLUIDO}' queda bajo el umbral`, () => {
    const score = scoreContra(NODO_ESPERADO_EXCLUIDO, fixture.query_negativa.embedding);
    expect(score).toBeCloseTo(SCORE_REF_NEGATIVO, 1);
    expect(score).toBeLessThan(MIN_SCORE_SALTO);
  });
});

describe.runIf(TIENE_VOYAGE)(
  "buscarAfines (Voyage AI real) -- mismos 2 casos de referencia de la Fase 2.9",
  () => {
    it(`query positiva encuentra '${NODO_ESPERADO_POSITIVO}' por encima de MIN_SCORE_SALTO`, async () => {
      const candidatos = await buscarAfines(QUERY_POSITIVA, new Set(), { k: 8, minScore: MIN_SCORE_SALTO });
      const encontrado = candidatos.find((c) => c.id === NODO_ESPERADO_POSITIVO);
      expect(encontrado).toBeDefined();
      expect(encontrado!.score).toBeGreaterThan(MIN_SCORE_SALTO);
      expect(encontrado!.score).toBeCloseTo(SCORE_REF_POSITIVO, 1);
    }, 15000);

    it(`query negativa NO ofrece '${NODO_ESPERADO_EXCLUIDO}' (queda bajo el umbral)`, async () => {
      const candidatosSinFiltro = await buscarAfines(QUERY_NEGATIVA, new Set(), { k: 20, minScore: 0.0 });
      const crudo = candidatosSinFiltro.find((c) => c.id === NODO_ESPERADO_EXCLUIDO);
      expect(crudo).toBeDefined();
      expect(crudo!.score).toBeCloseTo(SCORE_REF_NEGATIVO, 1);
      expect(crudo!.score).toBeLessThan(MIN_SCORE_SALTO);

      const candidatosConFiltro = await buscarAfines(QUERY_NEGATIVA, new Set(), { k: 8, minScore: MIN_SCORE_SALTO });
      expect(candidatosConFiltro.find((c) => c.id === NODO_ESPERADO_EXCLUIDO)).toBeUndefined();
    }, 15000);

    it("excluye ids ya visitados", async () => {
      const candidatos = await buscarAfines(QUERY_POSITIVA, new Set([NODO_ESPERADO_POSITIVO]), { k: 8, minScore: 0.0 });
      expect(candidatos.find((c) => c.id === NODO_ESPERADO_POSITIVO)).toBeUndefined();
    }, 15000);
  }
);

describe("buscarAfines: fallback silencioso sin VOYAGE_API_KEY", () => {
  it("devuelve [] sin lanzar si falta la API key (navegacion solo local)", async () => {
    const original = process.env.VOYAGE_API_KEY;
    delete process.env.VOYAGE_API_KEY;
    try {
      const candidatos = await buscarAfines("cualquier texto", new Set());
      expect(candidatos).toEqual([]);
    } finally {
      // Fix Fase 3.0.1: asignar `undefined` a process.env crea el string
      // "undefined" y envenena tests posteriores; restaurar con delete.
      if (original === undefined) {
        delete process.env.VOYAGE_API_KEY;
      } else {
        process.env.VOYAGE_API_KEY = original;
      }
    }
  });

  it("texto vacio devuelve [] sin llamar a la API", async () => {
    expect(await buscarAfines("", new Set())).toEqual([]);
    expect(await buscarAfines("   ", new Set())).toEqual([]);
  });
});
