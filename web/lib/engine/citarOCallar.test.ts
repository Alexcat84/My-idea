/**
 * CITAR O CALLAR (decision del fundador, 9 oct 2026, REDACTOR_CON_RESPALDO.md punto 3). Cada frase que afirma algo del
 * negocio o de la situacion de la persona lleva la marca de su respaldo: ⟦R7⟧ (una respuesta suya, numerada en
 * respuestas_de_la_persona) o ⟦N:id⟧ (un tema que recibio). Lo que no tiene respaldo se escribe como pregunta ⟦?⟧. El
 * codigo, sin un segundo modelo:
 *  - en vivo: quita las marcas de cada trozo antes de mandarlo a la pantalla, aunque una marca llegue partida;
 *  - al guardar: valida cada cita (que exista, que las cifras de la frase esten en lo citado, que comparta al menos una
 *    palabra con lo citado), cambia lo que no vale por su pregunta de reserva ⟦R7|¿…?⟧ o lo quita, quita de la
 *    introduccion la frase sin marca y corta en los pasos la cola causal sin respaldo ("…, porque …").
 * Las marcas nunca llegan a la pantalla. Casos reales de las mediciones donde aplican.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { describe, expect, it, vi } from "vitest";
import { usoVacio } from "../costmeter";
import { filtroDeMarcas, validarCitas, type Respaldo } from "./citarOCallar";
import { generarTextoPlan } from "./redactorPlan";
import { cargarFamilies } from "../readiness";
import { cargarGrafo } from "./graph";
import { finalizarPlan, prepararPlan } from "./planRedactor";
import prompts from "../assets/prompts.json";

const RESPALDO: Respaldo = {
  respuestas: [
    { id: "R1", texto: "Vendo unas 12 macetas al mes por Instagram, y el proveedor nuevo me baja el cemento un 20%." },
    { id: "R2", texto: "Mi mayor riesgo es que dependo de un solo proveedor de resina." },
  ],
  nodos: [{ id: "punto_equilibrio_unidades", textos: ["Calcula cuántas unidades necesitas vender al mes para cubrir tus costos fijos"] }],
  cifras: ["130", "250"],
};

describe("en vivo: las marcas nunca llegan a la pantalla", () => {
  it("quita la marca aunque llegue partida en varios trozos", () => {
    const visto: string[] = [];
    const f = filtroDeMarcas((t) => visto.push(t));
    for (const trozo of ["Vendes 12 macetas al mes por Instagram ⟦", "R", "1⟧. Anota ", "cuántas ⟦R1|¿Vend", "es más?⟧ salen."]) f.onChunk(trozo);
    f.finalizar();
    const todo = visto.join("");
    expect(todo).not.toMatch(/[⟦⟧]/);
    expect(todo).toBe("Vendes 12 macetas al mes por Instagram. Anota cuántas salen.");
  });

  it("generarTextoPlan nunca le pasa una marca a onDelta", async () => {
    const trozos = ["Vendes 12 al mes ⟦R", "1⟧. Sigue."];
    const stream = vi.fn(() => ({
      on: (_ev: string, cb: (t: string) => void) => trozos.forEach(cb),
      finalMessage: async () => ({ content: [{ type: "text", text: trozos.join("") }], stop_reason: "end_turn", usage: { input_tokens: 1, output_tokens: 1 } }),
    }));
    const client = { messages: { stream } } as unknown as Anthropic;
    const visto: string[] = [];
    const r = await generarTextoPlan(client, { payload: {} } as never, usoVacio(), (t) => visto.push(t), () => undefined, null, { backoffsMs: [0] });
    expect(visto.join("")).not.toMatch(/[⟦⟧]/);
    expect(r.rawTexto).toContain("⟦R1⟧"); // el texto crudo las conserva para validarlas al guardar
  });
});

describe("al guardar: cada cita se valida, lo que no vale se cambia por su pregunta o se quita", () => {
  const v = (t: string) => validarCitas(t, RESPALDO);

  it("una cita que respalda se queda, sin la marca", () => {
    expect(v("# Plan\n\nVendes unas 12 macetas al mes por Instagram ⟦R1⟧.").texto).toBe("# Plan\n\nVendes unas 12 macetas al mes por Instagram.");
  });

  it("una respuesta que no existe: se quita, o se cambia por su pregunta de reserva", () => {
    expect(v("# Plan\n\nTu tienda te paga menos ⟦R9⟧.").texto).toBe("# Plan");
    expect(v("# Plan\n\nTu tienda te paga menos ⟦R9|¿La tienda te paga lo mismo que Instagram?⟧.").texto).toBe(
      "# Plan\n\n¿La tienda te paga lo mismo que Instagram?"
    );
  });

  it("una cifra que no está en lo citado no pasa (12, no 30)", () => {
    expect(v("# Plan\n\nVendes 30 macetas al mes por Instagram ⟦R1⟧.").texto).toBe("# Plan");
  });

  it("una cita que no comparte ni una palabra con lo citado no pasa", () => {
    expect(v("# Plan\n\nTus compradores te recomiendan a sus conocidos ⟦R2⟧.").texto).toBe("# Plan");
  });

  it("un tema que vino en el material respalda; uno que no vino, no", () => {
    expect(v("# Plan\n\n## Etapa 1: X\n\n1. Calcula cuántas unidades vender para cubrir tus costos fijos ⟦N:punto_equilibrio_unidades⟧.").texto).toContain(
      "1. Calcula cuántas unidades vender para cubrir tus costos fijos."
    );
    expect(v("# Plan\n\n## Etapa 1: X\n\n1. Anota tus costos.\n2. Tus clientes prefieren lo barato ⟦N:inventado⟧.").texto).not.toContain("prefieren");
  });

  it("lo que se escribe como pregunta ⟦?⟧ se queda", () => {
    expect(v("# Plan\n\n## Etapa 1: X\n\n1. ¿La tienda te paga lo mismo que Instagram? ⟦?⟧").texto).toContain("1. ¿La tienda te paga lo mismo que Instagram?");
  });

  it("caso real: en la introducción, la frase sin marca sale", () => {
    const r = v(
      "# Seguridad en tu taller\n\nVendes unas 12 macetas al mes por Instagram ⟦R1⟧. Este plan lo convierte en un cuidado ordenado sin frenar la producción.\n\n## Etapa 1: X\n\n1. Anota."
    );
    expect(r.texto).toContain("Vendes unas 12 macetas al mes por Instagram.");
    expect(r.texto).not.toContain("sin frenar la producción");
  });

  it("caso real M3A-f002-1: en un paso, la cola causal sin respaldo se corta", () => {
    const r = v("# Plan\n\n## Etapa 1: X\n\n1. Haz el cálculo por separado para el tamaño chico y para el mediano, porque no cuestan lo mismo.");
    expect(r.texto).toContain("1. Haz el cálculo por separado para el tamaño chico y para el mediano.");
    expect(r.texto).not.toContain("no cuestan lo mismo");
  });

  it("caso real M3A-f003-2: un hecho del negocio que nadie dio, sin marca en la introducción, sale", () => {
    expect(v("# Plan\n\nLa tienda de plantas y Instagram no pagan lo mismo.\n\n## Etapa 1: X\n\n1. Anota.").texto).not.toContain("no pagan lo mismo");
  });

  it("nunca queda una marca en el texto guardado", () => {
    const r = v("# Plan\n\nVendes 12 ⟦R1⟧ y ⟦mal formada.\n\n## Etapa 1: X\n\n1. Anota ⟦R2⟧ tu riesgo del proveedor ⟦R2⟧.");
    expect(r.texto).not.toMatch(/[⟦⟧]/);
  });
});

describe("el redactor recibe las respuestas numeradas y la regla, y finalizarPlan valida", () => {
  it("prepararPlan numera las respuestas de la persona (sin repetir)", () => {
    const prep = prepararPlan(["punto_equilibrio_unidades"], cargarGrafo(), cargarFamilies(), "idea", "perfil", null, false, null, null, {
      respuestas: ["Vendo 12 al mes", "Dependo de un proveedor", "Vendo 12 al mes"],
    });
    expect(prep.payload.respuestas_de_la_persona).toEqual([
      { id: "R1", texto: "Vendo 12 al mes" },
      { id: "R2", texto: "Dependo de un proveedor" },
    ]);
  });

  it("SYSTEM_PLAN pide citar o callar con las marcas", () => {
    expect(prompts.SYSTEM_PLAN).toMatch(/CITAR O CALLAR/);
    expect(prompts.SYSTEM_PLAN).toContain("⟦R");
    expect(prompts.SYSTEM_PLAN).toContain("⟦?⟧");
  });

  it("el plan guardado sale validado y sin marcas, y deja el rastro", () => {
    const graph = cargarGrafo();
    const families = cargarFamilies();
    const ruta = ["punto_equilibrio_unidades"];
    const prep = prepararPlan(ruta, graph, families, "idea", "perfil", null, false, null, null, { respuestas: ["Vendo unas 12 macetas al mes por Instagram"] });
    const raw =
      "# Tu plan\n\nVendes unas 12 macetas al mes por Instagram ⟦R1⟧. Tus clientes te adoran ⟦R5⟧.\n\n## Etapa 1: Ordena tus números\n\n**Pasos:**\n1. Anota tus costos.\n\n**Entregable:** La lista.\n\n**Primera acción:** Anota el costo.\n\n" +
      '===JSON===\n{"familias_tratadas": [], "etapas": {"1": ["punto_equilibrio_unidades"]}}';
    const eventos: Array<Record<string, unknown>> = [];
    const r = finalizarPlan(raw, prep, ruta, families, "idea", (e) => eventos.push(e));
    expect(r.markdown).not.toMatch(/[⟦⟧]/);
    expect(r.markdown).toContain("Vendes unas 12 macetas al mes por Instagram.");
    expect(r.markdown).not.toContain("te adoran");
    expect(eventos.some((e) => e.tipo === "cita_sin_respaldo")).toBe(true);
  });
});
