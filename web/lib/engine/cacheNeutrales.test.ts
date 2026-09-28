/**
 * PRINCIPIO 2 (decision del fundador, 28 sep 2026): la salida segura del adaptador es la version NEUTRAL de cada base
 * (`pregunta_neutral`), y los nodos con siguientes que no tienen pregunta reciben la suya. Las dos cosas se generan en
 * la CORRIDA FINAL (engine/build_question_cache.py --faltantes y --neutrales; ninguna llamada a la API real antes).
 *
 * Trinquete: hoy faltan muchas; la cifra solo puede BAJAR. Tras la corrida final los dos topes pasan a 0 y desde ahi
 * cualquier nodo nuevo sin su pregunta o sin su neutral pone esta prueba en rojo.
 */
import { describe, expect, it } from "vitest";
import { cargarGrafo, cargarPreguntasCache } from "./graph";

/** Bases vivas sin neutral al 28 sep 2026 (engine/build_question_cache.py objetivos_neutrales): 2.940 sin el mundo 11,
 * y 3.287 con las 347 bases de Primer Equipo al traer main a puente-forja. */
const TOPE_SIN_NEUTRAL = 3287;
/** Nodos con siguientes y sin pregunta al 28 sep 2026 (engine/build_question_cache.py faltantes). */
const TOPE_SIN_PREGUNTA = 40;

const graph = cargarGrafo();
const cache = cargarPreguntasCache();

describe("la cache camina hacia completa (trinquete)", () => {
  it("las bases de nodos vivos sin version neutral no suben del tope", () => {
    const sinNeutral = Object.entries(cache).filter(
      ([nid, e]) => e.pregunta && !e.pregunta_neutral && graph[nid] && !graph[nid].deprecado
    );
    expect(sinNeutral.length).toBeLessThanOrEqual(TOPE_SIN_NEUTRAL);
  });

  it("los nodos con siguientes y sin pregunta no suben del tope", () => {
    const sinPregunta = Object.entries(graph).filter(([nid, n]) => {
      if (n.deprecado) return false;
      const siguientes = (n.nodos_siguientes ?? []).filter((s) => graph[s] && s !== nid && !graph[s].deprecado);
      return siguientes.length > 0 && !cache[nid]?.pregunta;
    });
    expect(sinPregunta.length).toBeLessThanOrEqual(TOPE_SIN_PREGUNTA);
  });

  it("una neutral, donde la hay, nunca pisa la base: es un campo aparte", () => {
    for (const e of Object.values(cache)) {
      if (e.pregunta_neutral) {
        expect(typeof e.pregunta).toBe("string");
        expect(typeof e.pregunta_neutral).toBe("string");
      }
    }
  });
});
