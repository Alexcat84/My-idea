// Fase 3.5: el muro de dominios en las cuatro capas del motor. Con un
// unlock sintético de 'quality' el nodo del pack es alcanzable; sin la
// fila (solo core), invisible. Esperados calculados a mano sobre un
// mini-grafo de 3 nodos (regla AGENTS.md).
import { describe, expect, it } from "vitest";
import { dominioPermitido, sucesoresNivel, type Grafo } from "./graph";
import { cosecharVecindario } from "./planRedactor";
import { candidatosSeguimiento } from "./puertaAvanzada";

// Mini-grafo: core_a -> {core_b, q_1}; q_1 es del dominio quality.
const graph = {
  core_a: {
    titulo_concepto: "Nodo core A",
    resumen_teorico: "",
    fase_proyecto: "ideacion",
    condiciones_activacion: [],
    nodos_siguientes: ["core_b", "q_1"],
    nodos_previos: [],
  },
  core_b: {
    titulo_concepto: "Nodo core B",
    resumen_teorico: "",
    fase_proyecto: "ideacion",
    condiciones_activacion: [],
    nodos_siguientes: [],
    nodos_previos: ["core_a"],
  },
  q_1: {
    titulo_concepto: "Nodo quality 1",
    resumen_teorico: "",
    fase_proyecto: "ideacion",
    condiciones_activacion: [],
    dominio: "quality",
    nodos_siguientes: [],
    nodos_previos: ["core_a"],
  },
} as unknown as Grafo;

const families = { core_a: "general", core_b: "general", q_1: "general" } as const satisfies Record<string, string>;
// cosecharVecindario tipa families como Record<string, Familia>:
const familiesTipadas = families as unknown as Record<string, import("../readiness").Familia>;
const SOLO_CORE = null; // default del motor
const CON_QUALITY = ["core", "quality"];

describe("el muro de dominios (Fase 3.5): 4 capas, con y sin unlock", () => {
  it("capa dominioPermitido: la base del muro", () => {
    expect(dominioPermitido("q_1", graph, SOLO_CORE)).toBe(false);
    expect(dominioPermitido("q_1", graph, CON_QUALITY)).toBe(true);
    expect(dominioPermitido("core_b", graph, SOLO_CORE)).toBe(true);
  });

  it("capa sucesores (turno): q_1 invisible sin unlock, visible con él", () => {
    expect(sucesoresNivel("core_a", graph, new Set(), undefined, SOLO_CORE)).toEqual(["core_b"]);
    expect(sucesoresNivel("core_a", graph, new Set(), undefined, CON_QUALITY)).toEqual(["core_b", "q_1"]);
  });

  it("capa cosecha del plan (la bomba dormida de planRedactor:76)", () => {
    const evaluacion = { tiene_accion_clientes: true, tiene_viabilidad_economica: true };
    const sinUnlock = cosecharVecindario(["core_a"], graph, familiesTipadas, evaluacion, null, null, undefined, SOLO_CORE);
    const conUnlock = cosecharVecindario(["core_a"], graph, familiesTipadas, evaluacion, null, null, undefined, CON_QUALITY);
    expect(sinUnlock).not.toContain("q_1");
    expect(conUnlock).toContain("q_1");
    expect(sinUnlock).toContain("core_b");
  });

  it("capa puerta avanzada (seguimiento): candidatos filtrados por dominio", () => {
    const sinUnlock = candidatosSeguimiento("", null, "ideacion", families, graph, new Set(), undefined, SOLO_CORE);
    const conUnlock = candidatosSeguimiento("", null, "ideacion", families, graph, new Set(), undefined, CON_QUALITY);
    expect(sinUnlock).not.toContain("q_1");
    expect(conUnlock).toContain("q_1");
  });
});
