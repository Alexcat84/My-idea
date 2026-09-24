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

  // La salida de la entrevista NO se exige al grafo (decisión del fundador,
  // 25 sep 2026: una arista afirma una continuidad de contenido, y un nodo sin
  // sucesor puede ser un final legítimo). La da el motor: la cubren las pruebas
  // del H13 en recorrido.test.ts, que recorren todos los callejones de los mundos.
});
