/**
 * EL TITULO NO AFIRMA NADA DEL NEGOCIO QUE LA PERSONA NO DIJO (decision del fundador, 10 oct 2026). Caso real de la
 * segunda medicion final (b4a01dea, f012): «Plan para tu pieza hecha a mano». La persona dijo que fabrica ella misma cada
 * pieza, una a la vez, pero no como: "hecha a mano" es un hecho que nadie dio. Una marca de cita no basta (el titulo
 * comparte "pieza" con la respuesta). El codigo exige que cada palabra con contenido del titulo venga de lo que dijo la
 * persona, de los temas o del vocabulario generico de un plan; si no, pone el titulo neutro del idioma.
 */
import { describe, expect, it } from "vitest";
import { tituloConRespaldo } from "./tituloConRespaldo";
import { cargarFamilies } from "../readiness";
import { cargarGrafo } from "./graph";
import { finalizarPlan, prepararPlan } from "./planRedactor";

const APOYO = [
  "Hago piezas de cerámica decorativa; cada pieza la fabrico yo misma, una a la vez, y las vendo a 250.",
  "Mi costo real por pieza es 130 incluyendo mi hora. Vendo por Instagram y en una tienda de plantas.",
  "Calcula tu margen bruto. Decide tu precio. Define tu propuesta de valor para tu cliente.",
];
const NEUTRO = "# Tu plan de acción";

describe("tituloConRespaldo", () => {
  it("caso real b4a01dea: «hecha a mano» no lo dijo nadie, el título pasa al neutro", () => {
    const r = tituloConRespaldo("# Plan para tu pieza hecha a mano\n\nIntro.", APOYO, NEUTRO, "es");
    expect(r.texto).toBe("# Tu plan de acción\n\nIntro.");
    expect(r.cambiado).toBe(true);
    expect(r.sinRespaldo).toContain("hecha");
  });

  it("un título hecho con palabras de la persona y de los temas se queda", () => {
    const t = "# Tu precio de 250 y tu costo de 130: calcula tu margen y decide tu precio";
    expect(tituloConRespaldo(`${t}\n\nIntro.`, APOYO, NEUTRO, "es")).toEqual({ texto: `${t}\n\nIntro.`, cambiado: false, sinRespaldo: [] });
  });

  it("el vocabulario genérico de un plan no cuenta como afirmación del negocio", () => {
    const t = "# Primeros pasos para ordenar y validar tu cerámica";
    expect(tituloConRespaldo(t, APOYO, NEUTRO, "es").cambiado).toBe(false);
  });

  it("fuera del español no se juzga por palabras (los temas están en español): se deja como vino", () => {
    const t = "# Your handmade ceramics plan";
    expect(tituloConRespaldo(t, APOYO, "# Your action plan", "en")).toEqual({ texto: t, cambiado: false, sinRespaldo: [] });
  });

  it("sin título, no hace nada", () => {
    expect(tituloConRespaldo("Intro sin título.", APOYO, NEUTRO, "es").cambiado).toBe(false);
  });
});

describe("finalizarPlan juzga el título contra lo que dijo la persona y los nombres de los temas", () => {
  const graph = cargarGrafo();
  const families = cargarFamilies();
  const ruta = ["customer_development_modelo"];
  const cuerpo =
    "\n\nVendes piezas de cerámica.\n\n## Etapa 1: Habla con compradores\n\n**Pasos:**\n1. Pregunta a tres compradores.\n\n" +
    '===JSON===\n{"familias_tratadas": [], "etapas": {"1": ["customer_development_modelo"]}}';
  const prep = () =>
    prepararPlan(ruta, graph, families, "Hago piezas de cerámica decorativa, cada una la fabrico yo misma", "Artesana sola", null, false, null, null, {
      respuestas: ["Las vendo a 250 por Instagram."],
    });

  it("caso real b4a01dea: el cuerpo del tema dice «hechas» (conversaciones hechas), pero eso no respalda «hecha a mano»", () => {
    const eventos: Array<Record<string, unknown>> = [];
    const r = finalizarPlan("# Plan para tu pieza hecha a mano" + cuerpo, prep(), ruta, families, "Hago piezas de cerámica", (e) => eventos.push(e));
    expect(r.markdown).toContain("# Tu plan de acción");
    expect(r.markdown).not.toContain("hecha a mano");
    expect(eventos).toContainEqual(expect.objectContaining({ tipo: "titulo_sin_respaldo", palabras: expect.arrayContaining(["hecha"]) }));
  });

  it("un título con palabras de la persona y de la etiqueta del tema se queda", () => {
    const r = finalizarPlan("# Valida tus piezas de cerámica: sal a descubrir clientes" + cuerpo, prep(), ruta, families, "Hago piezas de cerámica");
    expect(r.markdown).toContain("# Valida tus piezas de cerámica: sal a descubrir clientes");
  });
});

describe("el redactor lo pide", () => {
  it("SYSTEM_PLAN: el título se hace solo con lo que dijo la persona y los nombres de los temas", async () => {
    const prompts = (await import("../assets/prompts.json")).default as Record<string, string>;
    expect(prompts.SYSTEM_PLAN).toMatch(/hecho SOLO con lo que la persona dijo y los nombres de los temas/);
    expect(prompts.SYSTEM_PLAN).toMatch(/nunca afirma del negocio algo que la persona no dijo/);
  });
});
