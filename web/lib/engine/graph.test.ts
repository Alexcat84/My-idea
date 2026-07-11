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
  it("carga los 3260 nodos reales (1266 core + 455 OLA1 v1.3 + 1539 de packs)", () => {
    const graph = cargarGrafo();
    expect(Object.keys(graph).length).toBe(3260);
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

describe("dominioPermitido: el muro de mundos (Fase 3.5/3.6)", () => {
  it("los nodos core pasan con el default {core}", () => {
    const graph = cargarGrafo();
    const cores = Object.keys(graph)
      .filter((id) => (graph[id].dominio ?? "core") === "core")
      .slice(0, 50);
    expect(cores.length).toBe(50);
    for (const id of cores) {
      expect(dominioPermitido(id, graph)).toBe(true);
    }
  });

  it("los nodos de packs integrados NO pasan por defecto (mundos tras flags), y sí con su unlock", () => {
    const graph = cargarGrafo();
    for (const dominio of ["quality", "health_safety", "environmental"]) {
      const delPack = Object.keys(graph).filter((id) => graph[id].dominio === dominio);
      expect(delPack.length).toBeGreaterThan(0);
      for (const id of delPack.slice(0, 10)) {
        expect(dominioPermitido(id, graph)).toBe(false);
        expect(dominioPermitido(id, graph, ["core", dominio])).toBe(true);
      }
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
