/**
 * analyticsEntrada.test.ts — LA PRUEBA DE CRUCE (4 sep 2026, decisión del
 * fundador, sesión con credencial).
 *
 * POR QUÉ EXISTE, y es el ejemplar de una doctrina: las suites de `analytics`
 * fabricaban los `ItemAnalytics` A MANO, con `id` y `protege_item` puestos, y
 * NUNCA pasaban por `cargarEntradaAnalytics`. Por eso ninguna vio que el mapeo
 * de la entrada (analyticsEntrada.ts:79-91) se comía esos dos campos, y que
 * `carrilProteccion` era SIEMPRE [] en la app real, para cualquier proyecto.
 * Lo cazó el vuelo (corridas E y F), no la suite.
 *
 * ESTA PRUEBA CRUZA LAS DOS CAPAS: parte de FILAS como las que devuelve
 * Supabase, las pasa por `cargarEntradaAnalytics` y le pide a `calcularAnalytics`
 * el carril. Si un campo portador se cae en el mapeo, esta prueba se entera.
 */
import { describe, expect, it } from "vitest";
import { cargarEntradaAnalytics } from "./analyticsEntrada";
import { calcularAnalytics } from "./analytics";
import type { Proyecto } from "./db";

const PID = "11111111-1111-1111-1111-111111111111";
const ITEM_CORE = "22222222-2222-2222-2222-222222222222";
const ITEM_RIESGO = "33333333-3333-3333-3333-333333333333";
const PLAN_CORE = "44444444-4444-4444-4444-444444444444";
const PLAN_RIESGO = "55555555-5555-5555-5555-555555555555";

/** Las FILAS tal como salen de Supabase. Nada de ItemAnalytics a mano: ese
 *  atajo es justo el que dejó pasar el defecto. */
const FILAS_ITEMS = [
  {
    id: ITEM_CORE, plan_id: PLAN_CORE, dominio: "core", etapa: 2, estado: "pendiente",
    destacado: false, texto: "Consigue un proveedor alterno", completed_at: null,
    fecha_base: "2026-03-10T12:00:00Z", fecha_base_original: null,
    protege_item: null, no_aplica_motivo: null,
  },
  {
    id: ITEM_RIESGO, plan_id: PLAN_RIESGO, dominio: "risk_management", etapa: 1,
    estado: "pendiente", destacado: false, texto: "Firma con un segundo proveedor",
    completed_at: null, fecha_base: "2026-03-12T12:00:00Z", fecha_base_original: null,
    protege_item: ITEM_CORE, no_aplica_motivo: null,
  },
];

/** Cliente falso con la forma que usa la entrada: from().select().eq()/.in().order() */
function supabaseFalso(items: Array<Record<string, unknown>>) {
  const tablas: Record<string, unknown[]> = {
    sessions: [{ id: "66666666-6666-6666-6666-666666666666" }],
    plans: [
      { id: PLAN_CORE, etiqueta: "completo", created_at: "2026-03-01T10:00:00Z", baseline_confirmada_at: "2026-03-01T11:00:00Z", dominio: null },
      { id: PLAN_RIESGO, etiqueta: "completo", created_at: "2026-03-02T10:00:00Z", baseline_confirmada_at: null, dominio: "risk_management" },
    ],
    checklist_items: items,
    project_unlocks: [{ dominio: "risk_management", unlocked_at: "2026-03-02T09:00:00Z", completado_at: null, cierre_motivo: null }],
    project_modos: [{ dominio: "core", modo_camino: "fechas" }],
  };
  const constructor = (tabla: string) => {
    const res = { data: tablas[tabla] ?? [], error: null };
    const encadenable: Record<string, unknown> = {
      eq: () => encadenable, in: () => encadenable, order: () => res,
      then: (r: (v: typeof res) => unknown) => r(res),
    };
    return { select: () => encadenable };
  };
  return { from: (tabla: string) => constructor(tabla) } as never;
}

const PROYECTO = {
  id: PID, created_at: "2026-03-01T09:00:00Z", realizada_at: null,
  cierre_motivo: null, modo_camino: null,
} as unknown as Proyecto;

describe("la costura entre la entrada REAL y el carril de protección", () => {
  it("el carril trae la marca cuando la entrada pasa por cargarEntradaAnalytics", async () => {
    const entrada = await cargarEntradaAnalytics(supabaseFalso(FILAS_ITEMS), PID, PROYECTO, "2026-03-20T12:00:00Z");

    // Lo que el defecto rompía: los dos campos portadores tienen que SOBREVIVIR.
    const riesgo = entrada.items.find((i) => i.dominio === "risk_management");
    expect(riesgo, "la entrada perdió el item de riesgo").toBeTruthy();
    expect(riesgo!.id, "`id` no sobrevivió al mapeo de la entrada").toBe(ITEM_RIESGO);
    expect(riesgo!.protege_item, "`protege_item` no sobrevivió al mapeo").toBe(ITEM_CORE);

    // Y la consecuencia que de verdad se mide: el carril EXISTE.
    const a = calcularAnalytics(entrada);
    expect(a.carrilProteccion).toHaveLength(1);
    expect(a.carrilProteccion[0].dominio).toBe("risk_management");
    // la marca cae en la etapa del PROTEGIDO (2), no en la de la respuesta (1)
    expect(a.carrilProteccion[0].etapa).toBe(2);
  });

  it("CASO POR MUTACIÓN: si el mapeo pierde `id`, el carril se vacía", async () => {
    // Se muta la FILA quitándole el campo, que es lo mismo que el mapeo no
    // llevarlo: la entrada lo entrega undefined y `porIdCore` queda vacío.
    const mutadas = FILAS_ITEMS.map((f) => {
      const copia: Record<string, unknown> = { ...f };
      delete copia.id;
      return copia;
    });
    const a = calcularAnalytics(await cargarEntradaAnalytics(supabaseFalso(mutadas), PID, PROYECTO, "2026-03-20T12:00:00Z"));
    expect(a.carrilProteccion).toHaveLength(0);
  });

  it("CASO POR MUTACIÓN: si el mapeo pierde `protege_item`, el carril se vacía", async () => {
    const mutadas = FILAS_ITEMS.map((f) => {
      const copia: Record<string, unknown> = { ...f };
      delete copia.protege_item;
      return copia;
    });
    const a = calcularAnalytics(await cargarEntradaAnalytics(supabaseFalso(mutadas), PID, PROYECTO, "2026-03-20T12:00:00Z"));
    expect(a.carrilProteccion).toHaveLength(0);
  });
});

// AUD-09 M15: la protección apunta al NODO. Los dos campos que lo cargan
// (nodos_origen de la tarea del núcleo, protege_nodos de la respuesta) tienen
// que sobrevivir al mapeo de la entrada, o el carril vuelve a resolver solo
// por id y se queda con la tarea de un ciclo viejo.
describe("la entrada lleva los nodos de la protección (AUD-09 M15)", () => {
  it("nodos_origen y protege_nodos sobreviven al mapeo", async () => {
    const filas = [
      { ...FILAS_ITEMS[0], nodos_origen: ["precio_de_venta"] },
      { ...FILAS_ITEMS[1], protege_nodos: ["precio_de_venta"] },
    ];
    const entrada = await cargarEntradaAnalytics(supabaseFalso(filas), PID, PROYECTO, "2026-03-20T12:00:00Z");
    expect(entrada.items.find((i) => i.id === ITEM_CORE)?.nodos_origen).toEqual(["precio_de_venta"]);
    expect(entrada.items.find((i) => i.id === ITEM_RIESGO)?.protege_nodos).toEqual(["precio_de_venta"]);
  });
});

// AUD-09 M18 (tanda 5, fallas silenciosas): una lectura que fallaba se tomaba
// como "no hay nada" y el Análisis, la Celebración o el bloque de realidad del
// seguimiento salían en cero, presentados como verdad. Ahora falla en voz alta.
import { LecturaFallidaError } from "./analyticsEntrada";

function supabaseQueFallaEn(tablaQueFalla: string) {
  const builder = (tabla: string) => {
    const b: Record<string, unknown> = {};
    for (const m of ["select", "eq", "in", "order", "limit", "is"]) b[m] = () => b;
    b.then = (res: (v: unknown) => unknown) =>
      Promise.resolve(tabla === tablaQueFalla ? { data: null, error: { message: "no responde" } } : { data: [], error: null }).then(res);
    return b;
  };
  return { from: (t: string) => builder(t) } as never;
}

describe("cargarEntradaAnalytics no convierte una lectura fallida en ceros (AUD-09 M18)", () => {
  const proyecto = { id: "p1", created_at: "2026-09-01T00:00:00Z", realizada_at: null, modo_camino: null } as never;
  for (const tabla of ["sessions", "checklist_items"]) {
    it(`si falla la lectura de ${tabla}, lanza LecturaFallidaError`, async () => {
      await expect(cargarEntradaAnalytics(supabaseQueFallaEn(tabla), "p1", proyecto)).rejects.toBeInstanceOf(
        LecturaFallidaError
      );
    });
  }
});
