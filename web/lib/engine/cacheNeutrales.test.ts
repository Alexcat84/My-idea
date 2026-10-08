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
 * y 3.287 con las 347 bases de Primer Equipo al traer main a puente-forja. 3.288 con la base escrita a mano de la
 * puerta nueva de la auditoria final (repartir_supervision_puesto_funcional_mision, 28 sep 2026): su neutral la
 * genera la corrida final, que es la primera con API. */
const TOPE_SIN_NEUTRAL = 3288;
/** Nodos con siguientes y sin pregunta al 28 sep 2026 (engine/build_question_cache.py faltantes): 40, y 43 desde la
 * auditoria final, cuyas aristas verificadas dieron siguientes a cuestionar_historia_irracional_cabeza,
 * lleva_scorecard_desempeno_proveedor y traduce_stock_muerto_numeros (docs/ACTA_SANEAMIENTO_FINAL.md, 6.1). Se
 * generan en la corrida final con --faltantes. */
const TOPE_SIN_PREGUNTA = 43;
/** Preguntas de ENTRADA de puertas vivas sin su neutral (decisión del fundador para la corrida final, 8 oct 2026: las
 * neutrales de TODAS las preguntas, base y de entrada, en `pregunta_entrada_neutral`). 86 al 8 oct 2026. */
const TOPE_ENTRADA_SIN_NEUTRAL = 86;

const graph = cargarGrafo();
const cache = cargarPreguntasCache();

describe("la cache camina hacia completa (trinquete)", () => {
  it("las bases de nodos vivos sin version neutral no suben del tope", () => {
    const sinNeutral = Object.entries(cache).filter(
      ([nid, e]) => e.pregunta && !e.pregunta_neutral && e.pregunta_neutral_nivel !== 3 && graph[nid] && !graph[nid].deprecado
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

  it("las preguntas de entrada de nodos vivos sin su neutral no suben del tope", () => {
    const sinNeutral = Object.entries(cache).filter(
      ([nid, e]) => e.pregunta_entrada && !e.pregunta_entrada_neutral && e.pregunta_entrada_neutral_nivel !== 3 && graph[nid] && !graph[nid].deprecado
    );
    expect(sinNeutral.length).toBeLessThanOrEqual(TOPE_ENTRADA_SIN_NEUTRAL);
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
