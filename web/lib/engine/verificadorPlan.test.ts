// VERIFICADOR DE PLANES (decision del fundador, corrida final, 8 oct 2026; implementado SIN desplegar: VERIFICADOR_PLAN).
// Antes de entregar cada plan (nucleo, mundo, replanteamiento, seguimiento), una llamada a Sonnet 5.5 compara cada
// afirmacion con lo que dijo la persona y con sus nodos, y propone quitar frases o convertirlas en pregunta. Reglas:
//  - solo QUITA o convierte en PREGUNTA, citando la frase EXACTA; nunca reescribe ni añade;
//  - si la llamada falla, el plan se entrega igual y queda registrado (el cobro no cambia);
//  - si propone quitar mas del 20 % de las frases, no se aplica nada y queda marcado para revision.
// Las frases de los ejemplos son las del informe del juez (docs/coherencia/2026-10-08/fidelidad.md, tramo C).
import type Anthropic from "@anthropic-ai/sdk";
import { afterEach, describe, expect, it, vi } from "vitest";
import { usoVacio } from "../costmeter";
import { aplicarCorrecciones, frasesDelPlan, verificadorActivo, verificarPlan } from "./verificadorPlan";

const PLAN = [
  "_Plan inicial_",
  "",
  "# De ejecutar a dirigir",
  "",
  "## Etapa 1: Escribe qué debe lograr cada puesto",
  "",
  "Hoy haces tú el trabajo porque nadie sabe con precisión qué se espera de su puesto. Sin eso, no puedes decirle a nadie que va tarde ni que va muy bien.",
  "",
  "**Pasos:**",
  "1. Escribe, para cada uno de tus dos empleados, la razón de ser de su puesto.",
  "2. Anota tres resultados que esperas de cada uno.",
  "3. Revisa la lista con cada uno en una conversación corta.",
  "",
  "## Etapa 2: Da tu opinión a tiempo",
  "",
  "Cuando algo sale mal, díselo el mismo día. Explica qué viste y cómo lo quieres.",
  "",
  "**Primera acción:** Anota el nombre del cliente que más te ha recomendado.",
].join("\n");

describe("frasesDelPlan: las frases que se pueden verificar", () => {
  it("cuenta las frases del cuerpo y deja fuera titulos y rotulos", () => {
    const f = frasesDelPlan(PLAN);
    expect(f).toContain("Hoy haces tú el trabajo porque nadie sabe con precisión qué se espera de su puesto.");
    expect(f.some((x) => x.startsWith("#") || x.startsWith("## Etapa"))).toBe(false);
    expect(f).not.toContain("_Plan inicial_");
  });
});

describe("aplicarCorrecciones: solo quita o convierte en pregunta, citando la frase exacta", () => {
  it("quita la frase citada exacta (el caso real de la causa inventada)", () => {
    const r = aplicarCorrecciones(PLAN, [
      { frase: "Hoy haces tú el trabajo porque nadie sabe con precisión qué se espera de su puesto.", accion: "quitar" },
    ]);
    expect(r.revision).toBe(false);
    expect(r.markdown).not.toContain("nadie sabe con precisión");
    expect(r.markdown).toContain("Sin eso, no puedes decirle a nadie");
    expect(r.aplicadas).toBe(1);
  });

  it("convierte en pregunta con las mismas palabras (el caso real del cliente que recomendo)", () => {
    const r = aplicarCorrecciones(PLAN, [
      {
        frase: "Anota el nombre del cliente que más te ha recomendado.",
        accion: "pregunta",
        pregunta: "¿Algún cliente ya te ha recomendado? Si es así, anota el nombre del cliente que más te ha recomendado.",
      },
    ]);
    expect(r.markdown).toContain("¿Algún cliente ya te ha recomendado?");
    expect(r.markdown).not.toContain("**Primera acción:** Anota el nombre");
  });

  it("una 'pregunta' que reescribe con otras palabras no se acepta: la frase se quita (nunca se añade texto nuevo)", () => {
    const r = aplicarCorrecciones(PLAN, [
      { frase: "Anota el nombre del cliente que más te ha recomendado.", accion: "pregunta", pregunta: "¿Quieres abrir una tienda en línea con descuentos?" },
    ]);
    expect(r.markdown).not.toContain("tienda en línea");
    expect(r.markdown).not.toContain("Anota el nombre del cliente");
    // y el rotulo que se quedo sin su frase tambien sale
    expect(r.markdown).not.toContain("**Primera acción:**");
  });

  it("una frase que no esta tal cual en el plan se ignora", () => {
    const r = aplicarCorrecciones(PLAN, [{ frase: "Esta frase no existe en el plan.", accion: "quitar" }]);
    expect(r.markdown).toBe(PLAN);
    expect(r.ignoradas).toBe(1);
  });

  it("nunca toca un titulo", () => {
    const r = aplicarCorrecciones(PLAN, [{ frase: "## Etapa 1: Escribe qué debe lograr cada puesto", accion: "quitar" }]);
    expect(r.markdown).toBe(PLAN);
  });

  it("si propone quitar mas del 20 % de las frases, no aplica nada y marca revision", () => {
    const f = frasesDelPlan(PLAN);
    const muchas = f.slice(0, Math.floor(f.length * 0.2) + 1).map((frase) => ({ frase, accion: "quitar" as const }));
    const r = aplicarCorrecciones(PLAN, muchas);
    expect(r.revision).toBe(true);
    expect(r.markdown).toBe(PLAN);
    expect(r.aplicadas).toBe(0);
  });
});

describe("el verificador busca tambien lo que la medicion A/B le vio pasar (9 oct 2026)", () => {
  it("marca la premisa de una pregunta de la IA que la persona no confirmo", async () => {
    const { SYSTEM_VERIFICADOR_PLAN } = await import("../prompts");
    expect(SYSTEM_VERIFICADOR_PLAN).toMatch(/lo que solo aparece en una pregunta de la IA/i);
  });
  it("quita el paso o el calculo que contradice al nodo (casos reales: la resta al reves, la cuota de defectos)", async () => {
    const { SYSTEM_VERIFICADOR_PLAN } = await import("../prompts");
    expect(SYSTEM_VERIFICADOR_PLAN).toMatch(/un paso o un c[aá]lculo que contradice al nodo/i);
    expect(SYSTEM_VERIFICADOR_PLAN).toContain("Resta lo segundo de lo primero");
    expect(SYSTEM_VERIFICADOR_PLAN).toContain("cuántas piezas con defecto aceptas por cada lote");
  });
  it("marca lo que da por hecho algo que el estado o el plan anterior dicen pendiente", async () => {
    const { SYSTEM_VERIFICADOR_PLAN } = await import("../prompts");
    expect(SYSTEM_VERIFICADOR_PLAN).toContain("siguen vigentes");
  });
});

describe("verificarPlan: la llamada", () => {
  afterEach(() => {
    delete process.env.VERIFICADOR_PLAN;
  });

  it("esta APAGADO por defecto (sin desplegar) y se enciende con VERIFICADOR_PLAN=1", () => {
    delete process.env.VERIFICADOR_PLAN;
    expect(verificadorActivo()).toBe(false);
    process.env.VERIFICADOR_PLAN = "1";
    expect(verificadorActivo()).toBe(true);
  });

  it("aplica lo que propone el modelo (Sonnet 5.5)", async () => {
    const create = vi.fn(async (_req: { model: string }) => ({
      content: [{ type: "text", text: JSON.stringify({ correcciones: [{ frase: "Sin eso, no puedes decirle a nadie que va tarde ni que va muy bien.", accion: "quitar", motivo: "requisito que ningun nodo pone" }] }) }],
      stop_reason: "end_turn",
      usage: { input_tokens: 100, output_tokens: 20 },
    }));
    const r = await verificarPlan({ messages: { create } } as unknown as Anthropic, { markdown: PLAN, nodos: [], respuestas: ["me cuesta delegar"] }, usoVacio(), { presupuestoUsd: 5, contexto: null });
    expect(create.mock.calls[0][0].model).toBe("claude-sonnet-5-5");
    expect(r.fallo).toBeNull();
    expect(r.markdown).not.toContain("Sin eso, no puedes decirle");
  });

  it("si la llamada falla, el plan sale igual y queda el motivo", async () => {
    const create = vi.fn(async () => {
      throw new Error("sin red");
    });
    const r = await verificarPlan({ messages: { create } } as unknown as Anthropic, { markdown: PLAN, nodos: [], respuestas: [] }, usoVacio(), { presupuestoUsd: 5, contexto: null });
    expect(r.markdown).toBe(PLAN);
    expect(r.fallo).toMatch(/sin red/);
  });
});
