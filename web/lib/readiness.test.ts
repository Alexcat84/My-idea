// Fase 3.0: paridad exacta contra plan_readiness.py -- en vez de un
// puñado de casos de mano, reclasifica los 1266 nodos reales del grafo
// (ya sincronizados como assets) y compara contra node_families.json,
// que es la clasificacion que YA genero engine/plan_readiness.py. Si la
// normalizacion de acentos o alguna keyword se transcribio distinto, esto
// lo detecta con los datos reales, no con un ejemplo inventado.
import { describe, expect, it } from "vitest";
import masterGraph from "./assets/master_graph.json";
import nodeFamiliesGroundTruth from "./assets/node_families.json";
import { clasificarGrafo, evaluarRuta, type Familia } from "./readiness";

const graph = (masterGraph as { nodos: Record<string, { titulo_concepto?: string; resumen_teorico?: string }> }).nodos;
const groundTruth = nodeFamiliesGroundTruth as Record<string, Familia>;

describe("clasificarGrafo: paridad exacta contra node_families.json (1266 nodos reales)", () => {
  it("reclasifica cada nodo real identico a lo que ya calculo Python", () => {
    const reclasificado = clasificarGrafo(graph);
    const divergencias: string[] = [];
    for (const [nid, familia] of Object.entries(groundTruth)) {
      if (reclasificado[nid] !== familia) {
        divergencias.push(`${nid}: Python=${familia}, TS=${reclasificado[nid]}`);
      }
    }
    expect(divergencias).toEqual([]);
    expect(Object.keys(reclasificado).length).toBe(Object.keys(groundTruth).length);
  });
});

describe("evaluarRuta -- mismo caso que el escenario macetas (Fase 2.6-2.9)", () => {
  it("ruta con accion_clientes + viabilidad_economica + >=5 nodos = completa", () => {
    const families: Record<string, Familia> = {
      a: "accion_clientes",
      b: "viabilidad_economica",
      c: "general",
      d: "general",
      e: "general",
    };
    const evaluacion = evaluarRuta(["a", "b", "c", "d", "e"], families);
    expect(evaluacion.es_completa).toBe(true);
    expect(evaluacion.familias_faltantes).toEqual([]);
  });

  it("ruta sin viabilidad_economica queda incompleta con el mensaje correcto", () => {
    const families: Record<string, Familia> = { a: "accion_clientes", b: "general", c: "general", d: "general", e: "general" };
    const evaluacion = evaluarRuta(["a", "b", "c", "d", "e"], families);
    expect(evaluacion.es_completa).toBe(false);
    expect(evaluacion.tiene_viabilidad_economica).toBe(false);
    expect(evaluacion.familias_faltantes).toContain(
      "si tu idea puede sostenerse economicamente (costos, precios, punto de equilibrio)"
    );
  });
});
