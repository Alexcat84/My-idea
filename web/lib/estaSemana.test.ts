/**
 * "Esta semana" calculado por la app (decisión del fundador, 26 sep 2026).
 *
 * El plan ya no repite "Esta semana" en cada etapa (prometía tiempos imposibles
 * entre etapas secuenciales): cada etapa trae su "Primera acción" sin fecha, y
 * Manos a la Obra calcula UNA vez qué toca: la etapa activa, su primera acción
 * y lo que cabe en las horas por semana del espacio.
 *
 * Regla AGENTS.md: cada esperado de abajo se calculó A MANO, con las horas de
 * empaquetado.ts escritas aquí mismo:
 *   HORAS_MEDIA:       S = 1 h, M = 3 h, L = 8 h, XL = 16 h
 *   HORAS_POR_SEMANA:  "2-5" = 2 h, "5-10" = 5 h, "10-20" = 10 h, "20+" = 20 h
 *   capacidad sin declarar = CAPACIDAD_DEFAULT "5-10" = 5 h
 */
import { describe, expect, it } from "vitest";
import { calcularEstaSemana, primerasAccionesDelPlan, type ItemSemana } from "./estaSemana";
import { SYSTEM_PLAN } from "./prompts";

function it_(over: Partial<ItemSemana> & { id: string; etapa: number; orden: number }): ItemSemana {
  return { texto: `tarea ${over.id}`, destacado: false, estado: "pendiente", banda: null, ...over };
}

// Etapa 1 cerrada entera (hecha, hecha, no aplica). Etapa 2 abierta. Etapa 3 intacta.
const ITEMS: ItemSemana[] = [
  it_({ id: "a", etapa: 1, orden: 1, estado: "hecho", banda: "S" }),
  it_({ id: "b", etapa: 1, orden: 2, estado: "hecho", banda: "M" }),
  it_({ id: "c", etapa: 1, orden: 3, estado: "no_aplica", destacado: true, banda: "S" }),
  // En el plan la destacada (la primera acción) va al final de la etapa: orden 4.
  it_({ id: "e", etapa: 2, orden: 1, banda: "M" }),
  it_({ id: "f", etapa: 2, orden: 2, banda: "S", estado: "en_proceso" }),
  it_({ id: "g", etapa: 2, orden: 3, banda: "L" }),
  it_({ id: "d", etapa: 2, orden: 4, destacado: true, banda: "S", texto: "Publica tu vela" }),
  it_({ id: "h", etapa: 3, orden: 1, banda: "S" }),
  it_({ id: "i", etapa: 3, orden: 2, destacado: true, banda: "S" }),
];

describe("calcularEstaSemana: la etapa activa", () => {
  it("es la PRIMERA etapa con algo sin terminar (hecho y no aplica terminan; en proceso no)", () => {
    // Etapa 1: a hecho, b hecho, c no aplica → terminada. Etapa 2 tiene e, f, g, d abiertas.
    const r = calcularEstaSemana({ items: ITEMS, modo: "fechas", capacidad: "5-10" })!;
    expect(r.etapa).toBe(2);
  });

  it("una etapa con una sola tarea EN PROCESO sigue activa: la siguiente no se sugiere", () => {
    const items = [
      it_({ id: "x", etapa: 1, orden: 1, estado: "en_proceso", banda: "S" }),
      it_({ id: "y", etapa: 2, orden: 1, destacado: true, banda: "S" }),
    ];
    const r = calcularEstaSemana({ items, modo: "fechas", capacidad: "20+" })!;
    // A MANO: etapa 1 tiene x (en proceso) → activa. Primera acción: sin destacada
    // en la etapa 1 → la primera pendiente, x. Con 20 h caben de sobra, pero y es
    // de la etapa 2: jamás entra.
    expect(r.etapa).toBe(1);
    expect(r.primeraAccion.itemId).toBe("x");
    expect(r.tambienCaben).toEqual([]);
  });

  it("todo terminado: no hay bloque", () => {
    const items = ITEMS.map((i) => ({ ...i, estado: "hecho" as const }));
    expect(calcularEstaSemana({ items, modo: "fechas", capacidad: "5-10" })).toBeNull();
    expect(calcularEstaSemana({ items: [], modo: "ritmo", capacidad: null })).toBeNull();
  });
});

describe("calcularEstaSemana: con fechas, lo que cabe en las horas de la semana", () => {
  it("5-10 (5 h): la primera acción y lo que cabe en orden, nunca la etapa 3", () => {
    // A MANO, etapa 2 en orden (la destacada primero, luego por orden):
    //   d (S) 1 h → acumulado 1 ≤ 5 → primera acción
    //   e (M) 3 h → acumulado 4 ≤ 5 → cabe
    //   f (S) 1 h → acumulado 5 ≤ 5 → cabe
    //   g (L) 8 h → acumulado 13 > 5 → no cabe, y ahí se corta
    // h e i (etapa 3) nunca, aunque sobrara tiempo.
    const r = calcularEstaSemana({ items: ITEMS, modo: "fechas", capacidad: "5-10" })!;
    expect(r.modo).toBe("semana");
    expect(r.horasSemana).toBe(5);
    expect(r.primeraAccion).toEqual({ texto: "Publica tu vela", itemId: "d" });
    expect(r.tambienCaben.map((i) => i.id)).toEqual(["e", "f"]);
    expect(r.siguiente).toBeNull();
  });

  it("2-5 (2 h): lo que no cabe corta la lista; una tarea chica de después no se cuela", () => {
    // A MANO: d 1 h → 1 ≤ 2; e 3 h → 4 > 2 → corte. f (1 h) cabría en lo que
    // queda (1 + 1 = 2) pero va después de e en el plan: no se salta el orden.
    const r = calcularEstaSemana({ items: ITEMS, modo: "fechas", capacidad: "2-5" })!;
    expect(r.horasSemana).toBe(2);
    expect(r.tambienCaben).toEqual([]);
  });

  it("10-20 (10 h): d 1 + e 3 + f 1 = 5 ≤ 10; g 8 → 13 > 10: corte", () => {
    const r = calcularEstaSemana({ items: ITEMS, modo: "fechas", capacidad: "10-20" })!;
    expect(r.tambienCaben.map((i) => i.id)).toEqual(["e", "f"]);
  });

  it("20+ (20 h): d 1 + e 3 + f 1 + g 8 = 13 ≤ 20: cabe toda la etapa 2 y nada de la 3", () => {
    const r = calcularEstaSemana({ items: ITEMS, modo: "fechas", capacidad: "20+" })!;
    expect(r.tambienCaben.map((i) => i.id)).toEqual(["e", "f", "g"]);
  });

  it("sin capacidad declarada se planifica con la de por defecto (5-10 = 5 h)", () => {
    const r = calcularEstaSemana({ items: ITEMS, modo: "fechas", capacidad: null })!;
    expect(r.horasSemana).toBe(5);
    expect(r.tambienCaben.map((i) => i.id)).toEqual(["e", "f"]);
  });

  it("la primera acción del plan manda sobre el texto corto de la tarea", () => {
    const r = calcularEstaSemana({
      items: ITEMS,
      modo: "fechas",
      capacidad: "5-10",
      primerasAcciones: { 2: "Publica tu vela con precio y foto en un grupo local." },
    })!;
    expect(r.primeraAccion).toEqual({ texto: "Publica tu vela con precio y foto en un grupo local.", itemId: "d" });
  });

  it("si la primera acción ya está hecha, arranca por la primera pendiente de la etapa", () => {
    const items = ITEMS.map((i) => (i.id === "d" ? { ...i, estado: "hecho" as const } : i));
    // A MANO: etapa 2 sin d → e (M) 3 h es la primera acción; f 1 h → 4 ≤ 5 cabe;
    // g 8 h → 12 > 5 corte. El texto del plan ya no aplica (esa acción se hizo).
    const r = calcularEstaSemana({ items, modo: "fechas", capacidad: "5-10", primerasAcciones: { 2: "Publica tu vela" } })!;
    expect(r.primeraAccion).toEqual({ texto: "tarea e", itemId: "e" });
    expect(r.tambienCaben.map((i) => i.id)).toEqual(["f"]);
  });

  it("una tarea sin banda no se estima: corta la lista (cero invención)", () => {
    const items = ITEMS.map((i) => (i.id === "e" ? { ...i, banda: null } : i));
    const r = calcularEstaSemana({ items, modo: "fechas", capacidad: "20+" })!;
    expect(r.tambienCaben).toEqual([]);
  });

  it("una primera acción más grande que la semana deja la lista vacía", () => {
    const items = ITEMS.map((i) => (i.id === "d" ? { ...i, banda: "XL" as const } : i));
    // A MANO: d XL 16 h > 5 h → nada más cabe.
    const r = calcularEstaSemana({ items, modo: "fechas", capacidad: "5-10" })!;
    expect(r.primeraAccion.itemId).toBe("d");
    expect(r.tambienCaben).toEqual([]);
  });
});

describe("calcularEstaSemana: a mi ritmo, 'Tu siguiente paso' sin plazo", () => {
  it("la etapa activa, su primera acción y la siguiente tarea; sin horas", () => {
    // A MANO: etapa 2; primera acción d; la siguiente en orden del plan: e.
    const r = calcularEstaSemana({ items: ITEMS, modo: "ritmo", capacidad: "5-10" })!;
    expect(r.modo).toBe("ritmo");
    expect(r.etapa).toBe(2);
    expect(r.primeraAccion.itemId).toBe("d");
    expect(r.siguiente?.id).toBe("e");
    expect(r.tambienCaben).toEqual([]);
    expect(r.horasSemana).toBeNull();
  });

  it("sin modo elegido todavía tampoco se promete una semana", () => {
    const r = calcularEstaSemana({ items: ITEMS, modo: null, capacidad: null })!;
    expect(r.modo).toBe("ritmo");
  });

  it("la etapa con una sola tarea pendiente: no hay siguiente", () => {
    const items = [it_({ id: "z", etapa: 4, orden: 1, destacado: true, banda: "S" })];
    const r = calcularEstaSemana({ items, modo: "ritmo", capacidad: null })!;
    expect(r.primeraAccion.itemId).toBe("z");
    expect(r.siguiente).toBeNull();
  });
});

describe("primerasAccionesDelPlan: lee el marcador nuevo y el viejo como el mismo campo", () => {
  it("plan nuevo con **Primera acción:** y plan viejo con **Esta semana:**", () => {
    const md = [
      "# Plan",
      "## Etapa 1: Valida",
      "1. Algo.",
      "**Esta semana:** Llama a tres clientes.",
      "## Etapa 2: Cobra",
      "**Primera acción:** Pon un precio.",
      "## ¿Puede sostenerse tu idea? Los números en simple",
      "**Primera acción:** Esta no es de una etapa.",
    ].join("\n");
    expect(primerasAccionesDelPlan(md)).toEqual({ 1: "Llama a tres clientes.", 2: "Pon un precio." });
  });
});

// El prompt del redactor (engine/prototipo_motor.py, sincronizado en
// lib/assets/prompts.json): cada etapa pide su Primera acción sin fecha, y ya
// no pide "Esta semana" por etapa.
describe("SYSTEM_PLAN: la Primera acción reemplaza a 'Esta semana' en cada etapa", () => {
  it("la regla 3 pide '**Primera acción:**' sin fecha ni plazo", () => {
    expect(SYSTEM_PLAN).toContain("3. Cada etapa termina con una linea '**Primera acción:**'");
    expect(SYSTEM_PLAN).toContain("SIN fecha ni plazo");
  });

  it("ya no pide 'Esta semana' como rótulo de ninguna etapa ni del cierre", () => {
    expect(SYSTEM_PLAN).not.toContain("linea 'Esta semana:'");
    expect(SYSTEM_PLAN).not.toContain("**Esta semana:**");
    expect(SYSTEM_PLAN).not.toContain("El lunes que viene");
    expect(SYSTEM_PLAN).not.toContain("ejecutable en 7 dias");
  });
});
