// "LO QUE ESTE PLAN AUN NO CUBRE" contra las etapas REALES del plan (decision del fundador, corrida final, 8 oct 2026).
// El juez de fidelidad sostuvo un contrario en el plan del nucleo ee6de956 (f009): el bloque decia que el plan no cubre
// "validar con clientes reales (conversaciones, una primera version sencilla de tu producto, pruebas con usuarios, una
// venta o preventa real)" cuando sus etapas 2, 4 y 5, sacadas de concierge_mvp, producto_minimo_viable y
// establecer_linea_base_mvp (familia accion_clientes), mandan exactamente eso. El bloque lo arma el CODIGO, pero con lo
// que la IA autodeclara al final (familias_tratadas): si la IA olvida declarar una familia, el codigo contradecia al plan.
// Regla: una familia esta cubierta si un nodo que la IA usa en sus ETAPAS es de esa familia (verificado contra el
// material entregado) o si los encabezados de las etapas la tratan. El bloque nunca contradice las etapas.
import { describe, expect, it } from "vitest";
import { cargarFamilies } from "../readiness";
import { cargarGrafo } from "./graph";
import { SECCION_ECONOMICA_TITULO } from "./constants";
import { finalizarPlan, prepararPlan } from "./planRedactor";

const graph = cargarGrafo();
const families = cargarFamilies();
const NO_CUBRE_CLIENTES = "validar con clientes reales";

describe("el bloque de lo que falta no contradice las etapas", () => {
  it("el caso real: la IA no declaro accion_clientes pero sus etapas usan nodos de esa familia", () => {
    const ruta = ["concierge_mvp", "producto_minimo_viable", "establecer_linea_base_mvp", "punto_equilibrio_unidades"];
    const prep = prepararPlan(ruta, graph, families, "mi idea", "perfil", null, false, null);
    const raw =
      "# Tu plan\n\n## Etapa 1: Ordena tus números\n\nTexto.\n\n" +
      "## Etapa 2: Consigue tu primer cliente que pague\n\nTexto.\n\n" +
      "## Etapa 3: Lanza una primera versión sencilla\n\nTexto.\n\n" +
      `## ${SECCION_ECONOMICA_TITULO} Los números en simple\n\nTexto económico.\n\n` +
      '===JSON===\n{"familias_tratadas": ["viabilidad_economica"], "etapas": {"1": ["punto_equilibrio_unidades"], "2": ["concierge_mvp"], "3": ["producto_minimo_viable", "establecer_linea_base_mvp"]}}';
    const r = finalizarPlan(raw, prep, ruta, families, "mi idea");
    expect(r.markdown).not.toContain(NO_CUBRE_CLIENTES);
    expect(r.evaluacionCobertura.tiene_accion_clientes).toBe(true);
  });

  it("si las etapas de verdad no tratan clientes, el bloque lo sigue diciendo", () => {
    const ruta = ["punto_equilibrio_unidades"];
    const prep = prepararPlan(ruta, graph, families, "mi idea", "perfil", null, false, null);
    const raw =
      "# Tu plan\n\n## Etapa 1: Ordena tus números\n\nTexto.\n\n" +
      `## ${SECCION_ECONOMICA_TITULO} Los números en simple\n\nTexto económico.\n\n` +
      '===JSON===\n{"familias_tratadas": ["viabilidad_economica"], "etapas": {"1": ["punto_equilibrio_unidades"]}}';
    const r = finalizarPlan(raw, prep, ruta, families, "mi idea");
    expect(r.markdown).toContain(NO_CUBRE_CLIENTES);
  });

  it("un id de etapa que no vino en el material no cuenta (no se le cree a la IA un nodo inventado)", () => {
    const ruta = ["punto_equilibrio_unidades"];
    const prep = prepararPlan(ruta, graph, families, "mi idea", "perfil", null, false, null);
    const raw =
      "# Tu plan\n\n## Etapa 1: Ordena tus números\n\nTexto.\n\n" +
      `## ${SECCION_ECONOMICA_TITULO} Los números en simple\n\nTexto económico.\n\n` +
      '===JSON===\n{"familias_tratadas": ["viabilidad_economica"], "etapas": {"1": ["punto_equilibrio_unidades", "concierge_mvp"]}}';
    const r = finalizarPlan(raw, prep, ruta, families, "mi idea");
    expect(r.markdown).toContain(NO_CUBRE_CLIENTES);
  });
});
