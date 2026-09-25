/**
 * D3 (i18n F5): el auditor de las etiquetas del riel. Decisión del fundador:
 * "el auditor exige etiqueta en cada idioma para todo nodo vivo; al cambiar el
 * grafo, se regeneran solo las que falten". Si el grafo gana un nodo, esta
 * prueba falla hasta que se traduzca su etiqueta (scripts/i18n/etiquetasRiel.ts
 * exporta solo las que faltan).
 */
import { describe, expect, it } from "vitest";
import { cargarGrafo } from "../engine/graph";
import { ETIQUETAS_RIEL, type IdiomaDerivado } from "./etiquetasRiel";
import { validarEtiquetaRiel } from "./etiquetasRielValidar";

const grafo = cargarGrafo();
const vivos = Object.keys(grafo).filter((id) => !grafo[id].deprecado && grafo[id].etiqueta_arbol);
const idiomas = Object.keys(ETIQUETAS_RIEL) as IdiomaDerivado[];

describe("las etiquetas del riel en cada idioma (D3)", () => {
  it("hay nodos vivos que auditar", () => {
    expect(vivos.length).toBeGreaterThan(3000);
  });

  it.each(idiomas)("%s: todo nodo vivo tiene su etiqueta", (idioma) => {
    const faltan = vivos.filter((id) => !ETIQUETAS_RIEL[idioma][id]);
    expect(faltan, `faltan ${faltan.length}; npx tsx scripts/i18n/etiquetasRiel.ts exportar ${idioma} …`).toEqual([]);
  });

  it.each(idiomas)("%s: cada etiqueta pasa la vara (corta, sin rayas ni ¿¡, sin plantillas)", (idioma) => {
    const malas = Object.entries(ETIQUETAS_RIEL[idioma])
      .map(([id, v]) => [id, validarEtiquetaRiel(v)] as const)
      .filter(([, e]) => e);
    expect(malas).toEqual([]);
  });

  it.each(idiomas)("%s: ninguna etiqueta de un nodo que ya no existe", (idioma) => {
    const huerfanas = Object.keys(ETIQUETAS_RIEL[idioma]).filter((id) => !grafo[id]);
    expect(huerfanas).toEqual([]);
  });
});
