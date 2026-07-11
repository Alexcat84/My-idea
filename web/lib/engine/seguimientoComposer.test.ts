// Fase 3.3. Esperados escritos A MANO antes de correr (regla AGENTS.md).
// Composer: determinístico puro. candidatosSeguimiento: puntajes a mano
// sobre un mini-grafo sintético de 4 nodos (no hay test Python espejo:
// candidatos_seguimiento no tiene test en engine/ — verificado).
import { describe, expect, it } from "vitest";
import type { Grafo } from "./graph";
import { candidatosSeguimiento } from "./puertaAvanzada";
import { componerMensajeSeguimiento } from "./seguimientoComposer";

describe("componerMensajeSeguimiento", () => {
  it("agrupa por estado en orden hecho→a_medias→empezado→pendiente, con notas", () => {
    const msg = componerMensajeSeguimiento({
      items: [
        { etapa: 1, texto: "Habla con 3 clientes", destacado: false, estado: "pendiente" },
        { etapa: 1, texto: "Escribe la lista", destacado: false, estado: "hecho", nota: " me tomó 2 días " },
        { etapa: 2, texto: "Prepara la demo", destacado: true, estado: "a_medias" },
      ],
      detalles: "Conseguí un local prestado",
      enfoque: "precios",
    });
    const lineas = msg.split("\n");
    // Cálculo manual: encabezado + HECHO(1) + item + A MEDIAS(1) + item +
    // SIN EMPEZAR(1) + item + Además + enfoque = 9 líneas.
    expect(lineas).toHaveLength(9);
    expect(lineas[0]).toBe("Desde el último plan, este es mi avance real:");
    expect(lineas[1]).toBe("HECHO (1):");
    expect(lineas[2]).toBe("- Escribe la lista (nota: me tomó 2 días)");
    expect(lineas[3]).toBe("A MEDIAS (1):");
    expect(lineas[5]).toBe("SIN EMPEZAR (1):");
    expect(lineas[7]).toBe("Además: Conseguí un local prestado");
    expect(lineas[8]).toBe("Lo que más me interesa profundizar ahora: precios");
  });

  it("sin items ni enfoque: aviso de checklist vacío + guía abierta", () => {
    const msg = componerMensajeSeguimiento({ items: [] });
    expect(msg).toContain("(aún no actualicé el checklist; cuéntame desde donde estaba)");
    expect(msg).toContain("No estoy seguro de hacia dónde profundizar");
  });
});

describe("candidatosSeguimiento (puntajes a mano sobre mini-grafo)", () => {
  // Grafo sintético: 4 nodos. cubiertos = {a}. faseActual = "validacion".
  //   a (validacion, familia accion_clientes) — CUBIERTO: nunca candidato.
  //   b (validacion, viabilidad_economica): fase igual +5, familia sin cubrir +6 = 11
  //   c (planificacion, accion_clientes): fase siguiente +3, familia YA cubierta +0 = 3
  //   d (ideacion, general): fase anterior +0, general +0 = 0
  // Esperado: [b, c, d].
  const graph = {
    a: { titulo_concepto: "A", resumen_teorico: "", fase_proyecto: "validacion", condiciones_activacion: [] },
    b: { titulo_concepto: "B", resumen_teorico: "", fase_proyecto: "validacion", condiciones_activacion: [] },
    c: { titulo_concepto: "C", resumen_teorico: "", fase_proyecto: "planificacion", condiciones_activacion: [] },
    d: { titulo_concepto: "D", resumen_teorico: "", fase_proyecto: "ideacion", condiciones_activacion: [] },
  } as unknown as Grafo;
  const families = { a: "accion_clientes", b: "viabilidad_economica", c: "accion_clientes", d: "general" };

  it("excluye cubiertos y ordena por puntaje calculado a mano", () => {
    const r = candidatosSeguimiento("", null, "validacion", families, graph, new Set(["a"]));
    expect(r).toEqual(["b", "c", "d"]);
  });

  it("las palabras del mensaje inclinan la balanza (afinidad por tokens)", () => {
    // d gana +tokens si su título coincide con el mensaje; con fase 0 vs 3
    // de c no alcanza a superarlo, así que se prueba contra un empate: con
    // faseActual "ejecucion" nadie suma por fase; c y d quedan 0 y 0, y el
    // mensaje que menciona a D debe ponerlo antes que c.
    const graphD = {
      ...graph,
      d: { ...graph.d, titulo_concepto: "Estrategia de distribución mayorista" },
    } as unknown as Grafo;
    const r = candidatosSeguimiento(
      "quiero revisar la distribución mayorista de mi producto",
      null,
      "ejecucion",
      families,
      graphD,
      new Set(["a"])
    );
    expect(r.indexOf("d")).toBeLessThan(r.indexOf("c"));
  });
});
