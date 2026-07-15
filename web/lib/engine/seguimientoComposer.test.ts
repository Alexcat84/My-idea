// Fase 3.3. Esperados escritos A MANO antes de correr (regla AGENTS.md).
// Composer: determinístico puro. candidatosSeguimiento: puntajes a mano
// sobre un mini-grafo sintético de 4 nodos (no hay test Python espejo:
// candidatos_seguimiento no tiene test en engine/ — verificado).
import { describe, expect, it } from "vitest";
import type { Grafo } from "./graph";
import { candidatosSeguimiento } from "./puertaAvanzada";
import { componerMensajeSeguimiento, itemsDelUltimoPlanDe } from "./seguimientoComposer";

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

// ---------------------------------------------------------------------------
// Fase 4.1 (V4, auditoria de paridad de mundos): el follow es SIEMPRE core, y
// antes tomaba el plan del item MAS RECIENTE fuera cual fuera su dominio. Si el
// usuario acababa de explorar un mundo, "Contar que paso" componia su avance
// real con el checklist del MUNDO mientras el bloque llevaba cumplimiento core.
// ---------------------------------------------------------------------------
describe("itemsDelUltimoPlanDe (Fase 4.1 V4 + Fase 4.2)", () => {
  // El escenario exacto del hallazgo: el mundo es MAS RECIENTE que el core.
  const filas = [
    { plan_id: "mundo1", dominio: "quality", etapa: 1, orden: 1, texto: "Audita tu calidad", destacado: false, estado: "pendiente" as const, created_at: "2026-03-10T17:08:00Z" },
    { plan_id: "mundo1", dominio: "quality", etapa: 1, orden: 2, texto: "Mide la variacion", destacado: false, estado: "pendiente" as const, created_at: "2026-03-10T17:08:00Z" },
    { plan_id: "core2", dominio: "core", etapa: 2, orden: 1, texto: "Sal a vender", destacado: true, estado: "a_medias" as const, created_at: "2026-03-10T16:59:00Z" },
    { plan_id: "core2", dominio: "core", etapa: 1, orden: 1, texto: "Cierra tu costo", destacado: false, estado: "hecho" as const, nota: "la tabla quedo lista", created_at: "2026-03-10T16:59:00Z" },
    { plan_id: "core1", dominio: "core", etapa: 1, orden: 1, texto: "Plan viejo, ciclo anterior", destacado: false, estado: "hecho" as const, created_at: "2026-03-01T10:00:00Z" },
  ];

  it("con items de mundo MAS RECIENTES, el follow NO los toma", () => {
    const items = itemsDelUltimoPlanDe(filas, "core");
    expect(items.map((i) => i.texto)).toEqual(["Cierra tu costo", "Sal a vender"]);
    expect(items.some((i) => i.texto.includes("calidad") || i.texto.includes("variacion"))).toBe(false);
  });

  it("elige el ULTIMO plan core, no el primero (los ciclos viejos no vuelven)", () => {
    const items = itemsDelUltimoPlanDe(filas, "core");
    expect(items.some((i) => i.texto.includes("Plan viejo"))).toBe(false);
  });

  it("conserva estado, nota, destacado y el orden etapa->orden", () => {
    const items = itemsDelUltimoPlanDe(filas, "core");
    expect(items[0]).toEqual({ etapa: 1, texto: "Cierra tu costo", destacado: false, estado: "hecho", nota: "la tabla quedo lista" });
    expect(items[1].destacado).toBe(true);
  });

  it("dominio null cuenta como core (items previos a la migracion 016)", () => {
    const viejos = [
      { plan_id: "p1", etapa: 1, orden: 1, texto: "Sin dominio", destacado: false, estado: "hecho" as const, created_at: "2026-03-05T10:00:00Z" },
    ];
    expect(itemsDelUltimoPlanDe(viejos, "core").map((i) => i.texto)).toEqual(["Sin dominio"]);
  });

  it("un proyecto SOLO con items de mundo no compone nada core", () => {
    expect(itemsDelUltimoPlanDe(filas.filter((f) => f.dominio === "quality"), "core")).toEqual([]);
  });

  it("no depende del orden en que venga la consulta", () => {
    const alReves = [...filas].reverse();
    expect(itemsDelUltimoPlanDe(alReves, "core").map((i) => i.texto)).toEqual(["Cierra tu costo", "Sal a vender"]);
  });

  // Fase 4.2: el mundo tiene su PROPIO follow. El espejo del hallazgo V4, en la
  // otra direccion: si el follow de un mundo tomara items core, el motor
  // replanificaria el mundo con la historia del viaje principal.
  it("el follow de un mundo toma SUS items, aunque el core sea mas reciente", () => {
    const coreMasNuevo = [
      ...filas,
      { plan_id: "core3", dominio: "core", etapa: 1, orden: 1, texto: "Lo ultimo del core", destacado: false, estado: "hecho" as const, created_at: "2026-03-11T09:00:00Z" },
    ];
    const items = itemsDelUltimoPlanDe(coreMasNuevo, "quality");
    expect(items.map((i) => i.texto)).toEqual(["Audita tu calidad", "Mide la variacion"]);
    expect(items.some((i) => i.texto.includes("core"))).toBe(false);
  });

  it("el follow de un mundo elige el ULTIMO plan DE ESE MUNDO (su ciclo nuevo)", () => {
    const conCiclo2 = [
      ...filas,
      { plan_id: "mundo2", dominio: "quality", etapa: 1, orden: 1, texto: "Ciclo 2 del mundo", destacado: false, estado: "pendiente" as const, created_at: "2026-03-20T10:00:00Z" },
    ];
    expect(itemsDelUltimoPlanDe(conCiclo2, "quality").map((i) => i.texto)).toEqual(["Ciclo 2 del mundo"]);
  });

  it("un mundo sin checklist propio no compone nada (jamas cae al core)", () => {
    expect(itemsDelUltimoPlanDe(filas, "environmental")).toEqual([]);
  });

  it("dominio null NO se cuela en el follow de un mundo", () => {
    const viejos = [
      { plan_id: "p1", etapa: 1, orden: 1, texto: "Sin dominio", destacado: false, estado: "hecho" as const, created_at: "2026-03-05T10:00:00Z" },
    ];
    expect(itemsDelUltimoPlanDe(viejos, "quality")).toEqual([]);
  });
});
