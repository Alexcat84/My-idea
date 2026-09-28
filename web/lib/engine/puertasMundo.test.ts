// AUD-09 H13: toda puerta de un mundo tiene su pregunta escrita y una salida.
// Cuatro semillas no tenían pregunta en la caché: la primera pregunta del mundo
// caía a la plantilla con el título del libro en crudo y sin tildes
// ('Pensando en "Principio del Apalancamiento: ...", cuentame...'). Las
// preguntas se escribieron leyendo cada nodo en engine/preguntas_cache.json.
import { describe, expect, it } from "vitest";
import semillas from "../assets/packs_entry_seeds.json";
import { cargarPreguntasCache } from "./graph";

const cache = cargarPreguntasCache();
const puertas = Object.entries(semillas as Record<string, Array<{ id: string }>>).flatMap(([dominio, lista]) =>
  lista.map((s) => ({ dominio, id: s.id }))
);

describe("las puertas de los mundos (AUD-09 H13)", () => {
  it("hay puertas que revisar", () => {
    expect(puertas.length).toBeGreaterThan(20);
  });

  it("toda puerta tiene su pregunta escrita en la caché", () => {
    const sinPregunta = puertas.filter((p) => !cache[p.id]?.pregunta).map((p) => `${p.dominio}:${p.id}`);
    expect(sinPregunta).toEqual([]);
  });

  // Punto 3 del fundador (28 sep 2026): cada puerta entra con su pregunta de ENTRADA propia, que parte del concepto
  // de la puerta (la base mira a los siguientes). Se escribieron leyendo cada nodo y se verificaron a ciegas con
  // trampas sin marca (docs/ACTA_SANEAMIENTO_FINAL.md, seccion 9).
  it("toda puerta tiene su pregunta de entrada, una sola pregunta y distinta de la base", () => {
    const fallas = puertas
      .filter((p) => {
        const e = cache[p.id]?.pregunta_entrada;
        return typeof e !== "string" || !e.trim().startsWith("¿") && !e.includes("¿") || (e.match(/\?/g) ?? []).length !== 1 || e === cache[p.id]?.pregunta;
      })
      .map((p) => `${p.dominio}:${p.id}`);
    expect(fallas).toEqual([]);
  });

  it("la puerta de la IA de seguridad digital entra (decisión del fundador, punto 3)", () => {
    expect(puertas.map((p) => p.id)).toContain("gestion_riesgo_seguridad_ia");
  });

  // La salida de la entrevista NO se exige al grafo (decisión del fundador,
  // 25 sep 2026: una arista afirma una continuidad de contenido, y un nodo sin
  // sucesor puede ser un final legítimo). La da el motor: la cubren las pruebas
  // del H13 en recorrido.test.ts, que recorren todos los callejones de los mundos.
});
