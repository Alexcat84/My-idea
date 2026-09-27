// Ciclo de replanteamiento, Fase 2 (decisiones del fundador, 27 sep 2026): lo
// común a "Profundizar mi plan" y "Replantear mi camino" del lado del redactor
// y del cobro. Esperados calculados a mano sobre un mini-grafo (regla AGENTS.md).
import { describe, expect, it } from "vitest";
import { ETIQUETAS_CICLO, esCicloPosterior, PLANS_ETIQUETA } from "../dbContract";
import { conceptoDelPlan, montoDelPlan, PRECIOS } from "../precios";
import type { Familia } from "../readiness";
import type { Grafo } from "./graph";
import { cosecharVecindario, prepararPlan } from "./planRedactor";

// Mini-grafo: a -> {b, c}; los tres del núcleo, misma fase, sin familia.
const nodo = (sig: string[], prev: string[]) => ({
  titulo_concepto: "x",
  resumen_teorico: "",
  fase_proyecto: "ideacion",
  condiciones_activacion: [],
  pasos_accionables: [],
  nodos_siguientes: sig,
  nodos_previos: prev,
});
const graph = { a: nodo(["b", "c"], []), b: nodo([], ["a"]), c: nodo([], ["a"]) } as unknown as Grafo;
const families = { a: "general", b: "general", c: "general" } as unknown as Record<string, Familia>;
const evaluacion = { tiene_accion_clientes: true, tiene_viabilidad_economica: true };

describe("la cosecha excluye lo ya cubierto (SYSTEM_PLAN regla 8 lo promete)", () => {
  it("sin exclusión, los dos vecinos; con b cubierto en una sesión anterior, solo c", () => {
    expect(cosecharVecindario(["a"], graph, families, evaluacion, null).sort()).toEqual(["b", "c"]);
    expect(cosecharVecindario(["a"], graph, families, evaluacion, null, null, undefined, null, ["b"])).toEqual(["c"]);
  });

  it("prepararPlan pasa la exclusión a la cosecha y el plan anterior al payload del redactor", () => {
    const planAnterior = { etapas: [{ numero: 1, titulo: "Valida", tareas: [{ texto: "Hablar con 5", estado: "hecho" as const }] }] };
    const prep = prepararPlan(["a"], graph, families, "mi idea", "perfil", null, true, "vivo", null, {
      excluir: ["b"],
      planAnterior,
    });
    expect(prep.cosechaIds).toEqual(["c"]);
    expect(prep.payload.plan_anterior).toEqual(planAnterior);
    expect(prep.payload.es_seguimiento).toBe(true);
  });

  it("un replanteamiento lleva su bloque al payload; un plan sin extras no lleva nada nuevo", () => {
    const replanteamiento = {
      historia: "Se cayó el local.",
      se_conserva: ["Hablar con 5"],
      se_suelta: ["Rentar local"],
      camino_elegido: { titulo: "Por encargo", descripcion: "Sin local." },
    };
    const conRe = prepararPlan(["a"], graph, families, "m", "p", null, true, null, null, { replanteamiento });
    expect(conRe.payload.replanteamiento).toEqual(replanteamiento);
    const sin = prepararPlan(["a"], graph, families, "m", "p", null, false, null);
    expect("plan_anterior" in sin.payload).toBe(false);
    expect("replanteamiento" in sin.payload).toBe(false);
  });
});

describe("precio y etiqueta del replanteamiento (los dos a 5 por ahora)", () => {
  it("replanteamiento cobra su propia clave, a 5, en el núcleo y en un mundo", () => {
    expect(PRECIOS.replanteamiento).toBe(5);
    expect(PRECIOS.mundo_replanteamiento).toBe(5);
    expect(conceptoDelPlan("core", true, true)).toBe("replanteamiento");
    expect(conceptoDelPlan("calidad", true, true)).toBe("mundo_replanteamiento");
    expect(montoDelPlan("core", true, true)).toBe(5);
    // Profundizar sigue siendo el seguimiento de siempre.
    expect(conceptoDelPlan("core", true)).toBe("seguimiento");
    expect(conceptoDelPlan("calidad", true)).toBe("mundo_seguimiento");
  });

  it("'replanteamiento' es etiqueta de plan y cuenta como ciclo posterior", () => {
    expect(PLANS_ETIQUETA).toContain("replanteamiento");
    expect([...ETIQUETAS_CICLO]).toEqual(["inicial", "completo", "seguimiento", "replanteamiento"]);
    expect(esCicloPosterior("replanteamiento")).toBe(true);
    expect(esCicloPosterior("seguimiento")).toBe(true);
    expect(esCicloPosterior("completo")).toBe(false);
    expect(esCicloPosterior(null)).toBe(false);
  });
});
