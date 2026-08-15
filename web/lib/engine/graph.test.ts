// Fase 3.0: verifica graph.ts contra el dataset real ya sincronizado.
import { describe, expect, it } from "vitest";
import masterGraphJson from "../assets/master_graph.json";
import {
  cargarEntrySeeds,
  cargarGrafo,
  cargarPreguntasCache,
  esOfrecible,
  obtenerPregunta,
  resumenNodo,
  sucesoresNivel,
} from "./graph";

describe("cargarGrafo / cargarEntrySeeds / cargarPreguntasCache", () => {
  it("carga TODOS los nodos reales, paridad contra total_nodos (decision del fundador, 14 ago 2026)", () => {
    // Antes clavaba 3835 a mano: cada nodo propio del plan la rompia y el
    // guardian dejaba el arbol incommitteable. total_nodos lo escribe el
    // compilador Python (step6_compile_master_graph) en el mismo asset que
    // cargarGrafo() ya lee via masterGraphJson: mide que el parser de
    // TypeScript no pierda un nodo en silencio, sin pedir edicion manual
    // por operacion. Un censo que se mueve legitimamente en dataset/ (y por
    // tanto en las dos cifras del asset a la vez) deja esta prueba verde
    // sin tocarla; un nodo que se cae SOLO del lado cargado (grafo != total)
    // la tumba nombrando la diferencia.
    const graph = cargarGrafo();
    const total = (masterGraphJson as { total_nodos: number }).total_nodos;
    const cargados = Object.keys(graph).length;
    expect(cargados, `cargados ${cargados} vs total_nodos ${total}`).toBe(total);
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

describe("esOfrecible: el muro de mundos (Fase 3.5/3.6)", () => {
  it("los nodos core ACTIVOS pasan con el default {core}", () => {
    // El filtro tomaba las 50 primeras claves del core sin mirar `deprecado`, y
    // pasaba porque hasta ago 2026 el core no tenia ninguno. Al fundir el
    // nucleo, una de esas 50 quedo absorbida y el test cayo -- diciendo la
    // verdad: esOfrecible hace bien en rechazarla. El fixture era el accidente.
    const graph = cargarGrafo();
    const cores = Object.keys(graph)
      .filter((id) => (graph[id].dominio ?? "core") === "core" && !graph[id].deprecado)
      .slice(0, 50);
    expect(cores.length).toBe(50);
    for (const id of cores) {
      expect(esOfrecible(id, graph)).toBe(true);
    }
  });

  it("un nodo core DEPRECADO no pasa, que es lo que el fixture tapaba", () => {
    const graph = cargarGrafo();
    const absorbidos = Object.keys(graph).filter(
      (id) => (graph[id].dominio ?? "core") === "core" && graph[id].deprecado);
    expect(absorbidos.length, "el core ya no tiene absorbidos: revisa la fusion")
      .toBeGreaterThan(0);
    for (const id of absorbidos) {
      expect(esOfrecible(id, graph), `${id} se sigue ofreciendo`).toBe(false);
    }
  });

  it("los nodos de packs integrados NO pasan por defecto (mundos tras flags), y sí con su unlock", () => {
    const graph = cargarGrafo();
    // Fase v1.3.2: la muralla vale para los 6 mundos. Fase v1.4: 7.º mundo risk_management.
    for (const dominio of ["quality", "health_safety", "environmental", "seguridad_digital", "exportacion", "franquicias", "risk_management"]) {
      // Se excluyen los DEPRECADOS: este test es sobre la muralla de DOMINIO
      // (un nodo de pack no pasa sin su unlock), no sobre la deprecación. Un
      // nodo fundido no es ofrecible ni con su mundo abierto, y eso lo prueba
      // puertaUnica.test.ts, que es donde vive esa ley.
      const delPack = Object.keys(graph).filter(
        (id) => graph[id].dominio === dominio && !graph[id].deprecado);
      expect(delPack.length).toBeGreaterThan(0);
      for (const id of delPack.slice(0, 10)) {
        expect(esOfrecible(id, graph)).toBe(false);
        expect(esOfrecible(id, graph, ["core", dominio])).toBe(true);
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
