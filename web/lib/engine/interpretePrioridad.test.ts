// Pertinencia (vuelo del 27 sep 2026, mundo 11): la entrevista salto a contratar
// a alguien nuevo cuando la prioridad declarada era dirigir al equipo que ya
// tenia. La prioridad declarada solo moldeaba la redaccion de la pregunta; no
// pesaba al elegir el siguiente nodo. Tres piezas, las tres aqui:
//  1. la busqueda de saltos consulta la respuesta Y la prioridad declarada;
//  2. el respaldo sin modelo (elegirPorAfinidad) puntua tambien contra ella;
//  3. el prompt del interprete manda preferir el candidato que la atiende.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { consultaParaBrujula, elegirPorAfinidad } from "./interprete";
import type { Grafo } from "./graph";

describe("la prioridad declarada pesa al elegir el siguiente nodo", () => {
  it("la brujula consulta la respuesta y la prioridad declarada", () => {
    const p = { texto: "dar opinion clara a mi equipo", conteo: 2 };
    expect(consultaParaBrujula("Con eso me basta por ahora.", p)).toBe(
      "Con eso me basta por ahora. dar opinion clara a mi equipo"
    );
    // sin prioridad, lo de siempre: solo la respuesta
    expect(consultaParaBrujula("no se dirigir", null)).toBe("no se dirigir");
    // sin respuesta, la prioridad sola (nunca una cadena vacia si hay algo)
    expect(consultaParaBrujula("", p)).toBe("dar opinion clara a mi equipo");
  });

  it("el respaldo sin modelo prefiere el candidato que atiende la prioridad", () => {
    const grafo = {
      contratar: { titulo_concepto: "Contratar a una persona nueva", condiciones_activacion: ["Cuando vas a contratar"] },
      opinar: { titulo_concepto: "Dar opinion clara a tu equipo", condiciones_activacion: ["Cuando das opinion al equipo"] },
    } as unknown as Grafo;
    // A mano: la respuesta "Con eso me basta por ahora." no comparte ninguna
    // palabra con los dos candidatos (0 y 0): sin prioridad gana el primero.
    expect(elegirPorAfinidad(["contratar", "opinar"], grafo, "Con eso me basta por ahora.", null)).toBe("contratar");
    // Con la prioridad "dar opinion clara a mi equipo": "opinar" comparte
    // opinion, clara, equipo (3) y "contratar" ninguna (0): gana "opinar".
    expect(
      elegirPorAfinidad(["contratar", "opinar"], grafo, "Con eso me basta por ahora.", null, {
        texto: "dar opinion clara a mi equipo",
        conteo: 2,
      })
    ).toBe("opinar");
  });

  it("el prompt del interprete manda elegir con la prioridad declarada", () => {
    const prompts = JSON.parse(readFileSync(path.join(__dirname, "..", "assets", "prompts.json"), "utf-8")) as Record<string, string>;
    expect(prompts.SYSTEM_INTERPRETE_MULTI).toContain("ELEGIR CON LA PRIORIDAD");
  });

  // Contexto del emprendedor (28 sep 2026): la entrevista adapta los roles de
  // empresa grande (jefe, recursos humanos, directivos) a la persona real.
  it("el prompt del interprete adapta los roles de empresa grande", () => {
    const prompts = JSON.parse(readFileSync(path.join(__dirname, "..", "assets", "prompts.json"), "utf-8")) as Record<string, string>;
    const t = prompts.SYSTEM_INTERPRETE_MULTI;
    for (const x of ["ROLES DE EMPRESA GRANDE", "recursos humanos", "no tiene jefe", "condicional"]) expect(t).toContain(x);
  });
});
