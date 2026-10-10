/**
 * MENOS PROSA (decision del fundador, 9 oct 2026, REDACTOR_CON_RESPALDO.md punto 4). En las tres mediciones, la prosa
 * narrativa (la introduccion y los parrafos de las etapas) era el 18 % del texto y juntaba el 59 % de los hallazgos
 * sostenidos. Queda una introduccion corta (lo que la persona dijo, sin causas ni promesas) y, en cada etapa, solo lo
 * accionable: los pasos, el entregable (la señal de que esta hecha) y la primera accion. El prompt lo pide y el codigo
 * lo garantiza (podarProsa): en cada etapa sobreviven solo los bloques que empiezan con un rotulo o un paso, y la
 * introduccion se queda en su primer parrafo, con dos frases como mucho. Las secciones fijas no se tocan.
 */
import { readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { cargarFamilies } from "../readiness";
import { cargarGrafo } from "./graph";
import { finalizarPlan, prepararPlan } from "./planRedactor";
import { podarProsa } from "./menosProsa";
import prompts from "../assets/prompts.json";

// Extracto real del plan 85248377 (Salud y Seguridad) de la ultima medicion.
const REAL = `# Seguridad en tu taller de macetas: de ponerte tú la mascarilla a que tu equipo también se cuide

Trabajas con cemento y polvo todos los días, tienes dos empleados recién contratados y nunca has anotado qué podría salir mal en el taller. Este plan parte de la mascarilla que ya elegiste. Al final tendrás un taller más seguro sin frenar la producción.

## Etapa 1: Anota qué puede lastimarte a ti y a tu taller

Hasta hoy has ido apagando incendios. Antes de decidir qué proteger primero, hace falta ver todos los peligros juntos en una sola lista.

**Pasos:**
1. Recorre el taller con calma y anota cada peligro para la salud que veas.
2. Ordena la lista de mayor a menor riesgo.

**Entregable:** Una lista de peligros ordenada por riesgo, con fotos.

**Primera acción:** Anota en tu celular los tres peligros del taller que más te preocupan.

## Etapa 2: Controla primero lo que más te daña

Con la lista hecha, toca decidir cómo protegerte. Esta etapa es la que hace que el cuidado dure sin que te quite tiempo.

**Pasos:**
1. Para cada peligro de tu lista, busca primero si puedes quitarlo o reducirlo en el origen.

**Entregable:**

Un plan de control con cada peligro y la medida elegida.

**Primera acción:** Elige la mascarilla de polvo o los guantes que te pondrás.

Predicar con el ejemplo quita el aire de reproche.

## ¿Puede sostenerse tu idea? Los números en simple

Tu idea se sostiene si lo que entra cubre lo que sale.

- **Costo por unidad:** lo que gastas en cada pieza.`;

describe("podarProsa: queda la introducción corta y lo accionable", () => {
  const r = podarProsa(REAL);

  it("la introducción se queda en dos frases, con lo que la persona contó", () => {
    expect(r.texto).toContain(
      "Trabajas con cemento y polvo todos los días, tienes dos empleados recién contratados y nunca has anotado qué podría salir mal en el taller. Este plan parte de la mascarilla que ya elegiste."
    );
    expect(r.texto).not.toContain("Al final tendrás un taller más seguro");
  });

  it("salen los párrafos narrativos de las etapas (casos reales: «Esta etapa es la que hace que…», «Predicar con el ejemplo…»)", () => {
    expect(r.texto).not.toContain("Hasta hoy has ido apagando incendios");
    expect(r.texto).not.toContain("Esta etapa es la que hace que el cuidado dure");
    expect(r.texto).not.toContain("Predicar con el ejemplo quita el aire de reproche");
    expect(r.quitadas).toBe(3);
  });

  it("se queda todo lo accionable: pasos, entregable (también en su propio párrafo) y primera acción", () => {
    for (const t of [
      "## Etapa 1: Anota qué puede lastimarte a ti y a tu taller",
      "1. Recorre el taller con calma y anota cada peligro para la salud que veas.",
      "**Entregable:** Una lista de peligros ordenada por riesgo, con fotos.",
      "**Primera acción:** Anota en tu celular los tres peligros del taller que más te preocupan.",
      "Un plan de control con cada peligro y la medida elegida.",
      "**Primera acción:** Elige la mascarilla de polvo o los guantes que te pondrás.",
    ])
      expect(r.texto).toContain(t);
  });

  it("la sección de números no se toca", () => {
    expect(r.texto).toContain("Tu idea se sostiene si lo que entra cubre lo que sale.");
    expect(r.texto).toContain("- **Costo por unidad:** lo que gastas en cada pieza.");
  });

  it("una etapa sin pasos ni rótulos (formato roto) se deja como vino: nunca queda vacía", () => {
    const roto = "# Plan\n\nContexto.\n\n## Etapa 1: Algo\n\nSolo un párrafo que explica qué hacer sin lista.";
    expect(podarProsa(roto).texto).toContain("Solo un párrafo que explica qué hacer sin lista.");
  });

  it("es idempotente: un plan ya podado no cambia", () => {
    expect(podarProsa(r.texto)).toEqual({ texto: r.texto, quitadas: 0, introRecortada: false });
  });
});

describe("los casos reales de la última medición que vivían en la prosa de una etapa desaparecen", () => {
  const dir = path.resolve(import.meta.dirname, "../../../docs/corrida_final/2026-10-08/medicion_final/A");
  const planes = readdirSync(dir).map((f) => readFileSync(path.join(dir, f), "utf8"));
  it.each([
    ["M3A-f001-1", "Este es el paso que más te ayuda a dejar de apagar incendios"],
    ["M3A-f001-2", "Quien va bien y nunca lo oye queda sin referencia"],
    ["M3A-f003-1", "ahí se esconde un gasto que aún no estás viendo"],
    ["M3A-f003-3", "El material de este plan no cubre seguridad informática"],
    ["M3A-f007-1", "porque la tienda y Instagram no te pagan lo mismo"],
    ["M3A-f015-1", "El material enseña que la seguridad funciona"],
    ["M3A-f016-1", "y por eso tus lotes no salen parejos"],
    ["M3A-f017-1", "Que no hayan bajado las ventas con gente que ya te conocía"],
  ])("%s", (_id, frase) => {
    const antes = planes.filter((p) => p.includes(frase));
    expect(antes.length).toBeGreaterThan(0);
    for (const p of antes) expect(podarProsa(p).texto).not.toContain(frase);
  });
});

describe("el redactor lo pide y finalizarPlan lo aplica", () => {
  it("SYSTEM_PLAN pide la introducción corta, prohíbe la prosa de enlace y su ejemplo ya no la enseña", () => {
    const p = prompts.SYSTEM_PLAN;
    expect(p).toMatch(/INTRODUCCION CORTA/);
    expect(p).toMatch(/PROHIBIDO un parrafo narrativo/);
    expect(p).not.toContain("Vender a amigas te dice que el producto gusta");
    expect(p).not.toMatch(/un parrafo de contexto que conecte/);
  });

  it("el plan guardado sale podado y deja el rastro", () => {
    const graph = cargarGrafo();
    const families = cargarFamilies();
    const ruta = ["punto_equilibrio_unidades"];
    const prep = prepararPlan(ruta, graph, families, "mi idea", "perfil", null, false, null);
    const raw =
      "# Tu plan\n\nVendes velas a tus amigas.\n\n## Etapa 1: Ordena tus números\n\nEsta etapa te ahorrará problemas.\n\n**Pasos:**\n1. Anota tus costos.\n\n**Entregable:** La lista de costos.\n\n**Primera acción:** Anota el costo de la cera.\n\n" +
      '===JSON===\n{"familias_tratadas": [], "etapas": {"1": ["punto_equilibrio_unidades"]}}';
    const eventos: Array<Record<string, unknown>> = [];
    const r = finalizarPlan(raw, prep, ruta, families, "mi idea", (e) => eventos.push(e));
    expect(r.markdown).not.toContain("Esta etapa te ahorrará problemas");
    expect(r.markdown).toContain("1. Anota tus costos.");
    expect(eventos.some((e) => e.tipo === "prosa_de_enlace_quitada")).toBe(true);
  });
});
