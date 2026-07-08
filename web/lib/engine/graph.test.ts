// Fase 3.0: verifica graph.ts contra el dataset real ya sincronizado.
import { describe, expect, it } from "vitest";
import {
  cargarEntrySeeds,
  cargarGrafo,
  cargarPreguntasCache,
  dominioPermitido,
  obtenerPregunta,
  resumenNodo,
  sucesoresNivel,
} from "./graph";

describe("cargarGrafo / cargarEntrySeeds / cargarPreguntasCache", () => {
  it("carga los 1266 nodos reales", () => {
    const graph = cargarGrafo();
    expect(Object.keys(graph).length).toBe(1266);
  });

  it("carga las 20 puertas de entrada", () => {
    expect(cargarEntrySeeds().length).toBe(20);
    expect(cargarEntrySeeds()).toContain("design_thinking_fundamentos");
  });

  it("carga el cache de preguntas (1240 nodos cacheados)", () => {
    const cache = cargarPreguntasCache();
    expect(Object.keys(cache).length).toBeGreaterThan(1000);
  });
});

describe("sucesoresNivel: mismos sucesores reales que engine/prototipo_motor.py", () => {
  it("design_thinking_fundamentos tiene sus sucesores conocidos (ver AUD-02)", () => {
    const graph = cargarGrafo();
    const sucesores = sucesoresNivel("design_thinking_fundamentos", graph, new Set());
    expect(sucesores).toContain("mapeo_capas_diseno");
    expect(sucesores).toContain("convertir_necesidad_en_demanda");
  });

  it("excluye nodos ya visitados", () => {
    const graph = cargarGrafo();
    const visitados = new Set(["mapeo_capas_diseno"]);
    const sucesores = sucesoresNivel("design_thinking_fundamentos", graph, visitados);
    expect(sucesores).not.toContain("mapeo_capas_diseno");
  });

  it("respeta el limite (default MAX_OPCIONES=6)", () => {
    const graph = cargarGrafo();
    const sucesores = sucesoresNivel("design_thinking_fundamentos", graph, new Set(), 2);
    expect(sucesores.length).toBeLessThanOrEqual(2);
  });
});

describe("dominioPermitido: no-op con el default {core} (Hotfix v2.1.1)", () => {
  it("todos los nodos reales pasan con el default (todo el dataset es 'core')", () => {
    const graph = cargarGrafo();
    const algunosIds = Object.keys(graph).slice(0, 50);
    for (const id of algunosIds) {
      expect(dominioPermitido(id, graph)).toBe(true);
    }
  });
});

describe("obtenerPregunta / resumenNodo", () => {
  it("devuelve la pregunta cacheada si existe", () => {
    const graph = cargarGrafo();
    const cache = cargarPreguntasCache();
    const nid = "design_thinking_fundamentos";
    const pregunta = obtenerPregunta(nid, graph[nid], cache);
    expect(pregunta.length).toBeGreaterThan(0);
    if (cache[nid]?.pregunta) {
      expect(pregunta).toBe(cache[nid].pregunta);
    }
  });

  it("resumenNodo incluye pregunta_cache solo si se pasa el cache", () => {
    const graph = cargarGrafo();
    const cache = cargarPreguntasCache();
    const nid = "design_thinking_fundamentos";
    expect(resumenNodo(nid, graph).pregunta_cache).toBeUndefined();
    expect(resumenNodo(nid, graph, cache).pregunta_cache).toBeDefined();
  });
});
