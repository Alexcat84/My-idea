// Scheduler F1 — la PERSISTENCIA de la estimación: insertarChecklist escribe la
// banda y espera_externa junto al ítem al nacer el plan. El caso que importa de
// verdad es el FALLBACK: un plan cuyos ítems no traen estimación se inserta
// igual, con banda null, en vez de romper el nacimiento del plan.
import { describe, expect, it } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio } from "./testUtils/fakeSupabase";
import { anotarEnMemoria, crearProyecto, guardarEstadoSesion, insertarChecklist } from "./db";
import type { EstadoSesionPersistido } from "./db";
import type { SupabaseClient } from "@supabase/supabase-js";

function falso() {
  const estado = estadoFalsoVacio();
  return { estado, client: crearSupabaseFalso(estado) as unknown as SupabaseClient };
}

describe("insertarChecklist: persiste la banda estimada (Scheduler F1)", () => {
  it("guarda banda y espera_externa por ítem", async () => {
    const { estado, client } = falso();
    await insertarChecklist(
      client,
      "p1",
      "plan-1",
      [
        { etapa: 1, orden: 1, texto: "Redacta el perfil", destacado: false, banda: "M", espera_externa: false },
        { etapa: 1, orden: 2, texto: "Escribe y espera respuesta", destacado: true, banda: "S", espera_externa: true },
      ],
      "core"
    );
    expect(estado.checklistItems).toHaveLength(2);
    expect(estado.checklistItems[0]).toMatchObject({ texto: "Redacta el perfil", banda: "M", espera_externa: false });
    expect(estado.checklistItems[1]).toMatchObject({ banda: "S", espera_externa: true });
  });

  it("FALLBACK: sin estimación, el ítem se inserta con banda null (el plan no se bloquea)", async () => {
    const { estado, client } = falso();
    await insertarChecklist(client, "p1", "plan-1", [{ etapa: 1, orden: 1, texto: "Compra dos termos", destacado: false }]);
    expect(estado.checklistItems).toHaveLength(1);
    expect(estado.checklistItems[0]).toMatchObject({ banda: null, espera_externa: null });
  });

  it("estimación PARCIAL: los ítems que el lote no cubrió quedan sin banda, los demás con la suya", async () => {
    const { estado, client } = falso();
    await insertarChecklist(client, "p1", "plan-1", [
      { etapa: 1, orden: 1, texto: "Con banda", destacado: false, banda: "L", espera_externa: false },
      { etapa: 1, orden: 2, texto: "Sin banda", destacado: false, banda: null, espera_externa: null },
    ]);
    expect(estado.checklistItems[0].banda).toBe("L");
    expect(estado.checklistItems[1].banda).toBeNull();
  });

  it("el dominio del plan viaja con cada ítem (core o mundo)", async () => {
    const { estado, client } = falso();
    await insertarChecklist(
      client,
      "p1",
      "plan-m",
      [{ etapa: 1, orden: 1, texto: "Tarea del mundo", destacado: false, banda: "XL", espera_externa: false }],
      "quality"
    );
    expect(estado.checklistItems[0]).toMatchObject({ dominio: "quality", banda: "XL" });
  });

  it("lista vacía: no escribe nada", async () => {
    const { estado, client } = falso();
    await insertarChecklist(client, "p1", "plan-1", []);
    expect(estado.checklistItems).toHaveLength(0);
  });
});

// AUD-09 M15: protege_nodos llega con la migración 041. Si el código se
// despliega antes de aplicarla, la entrega de un plan de protección no puede
// caerse entera: se reintenta sin esa columna (la protección se resolverá por
// id, como antes) y queda un error fuerte en el log.
describe("insertarChecklist: tolera la 041 ausente (AUD-09 M15)", () => {
  it("si protege_nodos no existe, inserta sin ella y conserva el enlace", async () => {
    const intentos: Array<Array<Record<string, unknown>>> = [];
    const client = {
      from: () => ({
        insert: async (filas: Array<Record<string, unknown>>) => {
          intentos.push(filas);
          if ("protege_nodos" in filas[0]) {
            return { error: { code: "PGRST204", message: "Could not find the 'protege_nodos' column of 'checklist_items' in the schema cache" } };
          }
          return { error: null };
        },
      }),
    } as unknown as SupabaseClient;
    await insertarChecklist(client, "p1", "plan-r", [
      { etapa: 1, orden: 1, texto: "Firma con un segundo proveedor", destacado: false, protege_item: "n1", protege_nodos: ["precio_de_venta"], deteccion: "un solo proveedor" },
    ], "risk_management");
    expect(intentos).toHaveLength(2);
    expect(intentos[1][0]).not.toHaveProperty("protege_nodos");
    expect(intentos[1][0]).toMatchObject({ protege_item: "n1", deteccion: "un solo proveedor" });
  });

  it("cualquier otro error sigue lanzando", async () => {
    const client = {
      from: () => ({ insert: async () => ({ error: { code: "23505", message: "duplicate key" } }) }),
    } as unknown as SupabaseClient;
    await expect(
      insertarChecklist(client, "p1", "plan-r", [{ etapa: 1, orden: 1, texto: "x", destacado: false, protege_item: "n1", protege_nodos: ["a"] }])
    ).rejects.toMatchObject({ code: "23505" });
  });
});

// i18n F5: el idioma de la idea nace con el proyecto (projects.idioma, 046).
// Si el código llega antes que la migración, la idea se crea igual sin él (el
// proyecto se leerá como español, lo mismo que antes de F5) y queda el síntoma
// en el log.
describe("crearProyecto: guarda el idioma de la idea (i18n F5, 046)", () => {
  it("con idioma, la fila nace con él", async () => {
    const { estado, client } = falso();
    const id = await crearProyecto(client, "u1", "우리 동네에서 빵을 팔고 싶어요", "ko");
    expect(estado.projects[id]).toMatchObject({ entrada_original: "우리 동네에서 빵을 팔고 싶어요", idioma: "ko" });
  });

  it("si la columna idioma no existe (046 sin aplicar), se crea sin ella", async () => {
    const intentos: Array<Record<string, unknown>> = [];
    const client = {
      from: () => ({
        insert: (fila: Record<string, unknown>) => {
          intentos.push(fila);
          const respuesta =
            "idioma" in fila
              ? { data: null, error: { code: "PGRST204", message: "Could not find the 'idioma' column of 'projects' in the schema cache" } }
              : { data: { id: "p-nuevo" }, error: null };
          return { select: () => ({ single: async () => respuesta }) };
        },
      }),
    } as unknown as SupabaseClient;
    expect(await crearProyecto(client, "u1", "Quiero vender pan", "es")).toBe("p-nuevo");
    expect(intentos).toHaveLength(2);
    expect(intentos[1]).not.toHaveProperty("idioma");
  });

  it("cualquier otro error sigue lanzando", async () => {
    const client = {
      from: () => ({
        insert: () => ({ select: () => ({ single: async () => ({ data: null, error: { code: "23505", message: "duplicate key" } }) }) }),
      }),
    } as unknown as SupabaseClient;
    await expect(crearProyecto(client, "u1", "x", "es")).rejects.toMatchObject({ code: "23505" });
  });
});

// Costes del vuelo del 27 sep 2026: una sesion que se queda a medias (el usuario
// la deja, o un seguimiento que no llega a plan) gastaba de verdad (turno, puerta
// avanzada) pero su columna costo_usd se quedaba en 0, porque solo la escribia
// el cierre. Cada turno guarda ahora tambien el coste y su desglose.
//
// A mano, con los precios de costmeter.ts (Haiku 1 $ entrada / 5 $ salida por
// millon; lectura de cache al 10 %): 1000 in + 200 out + 10000 cache_read =
//   1000/1e6 * 1 + 200/1e6 * 5 + 10000/1e6 * 1 * 0.1 = 0.001 + 0.001 + 0.001 = 0.003
describe("guardarEstadoSesion: cada turno deja el coste en la sesion", () => {
  it("escribe costo_usd y costo_desglose junto al estado", async () => {
    let escrito: Record<string, unknown> | null = null;
    const client = {
      from: () => ({
        update: (payload: Record<string, unknown>) => {
          escrito = payload;
          return { eq: async () => ({ error: null }) };
        },
      }),
    } as unknown as SupabaseClient;
    const estado = {
      recorrido: {},
      acumulado: {
        uso: { "claude-haiku-4-5": { in: 1000, out: 200, cache_read: 10000, cache_write: 0, llamadas: 2 } },
        uso_por_componente: { turnos: 0.002, clasificacion: 0.001 },
        presupuesto_excedido: false,
      },
      turnos: [],
      ultimaPregunta: "¿Que te preocupa?",
    } as unknown as EstadoSesionPersistido;
    await guardarEstadoSesion(client, "s1", estado);
    expect(escrito).not.toBeNull();
    expect(escrito!.estado_recorrido).toBe(estado);
    expect(escrito!.costo_usd as number).toBeCloseTo(0.003, 10);
    expect(escrito!.costo_desglose).toEqual({ turnos: 0.002, clasificacion: 0.001 });
  });
});

// PRINCIPIO 1 (28 sep 2026): la memoria del proyecto se guarda en la base y se
// actualiza en CADA turno: la ficha fusionada y la pareja pregunta-respuesta al
// final del hilo. A mano: memoria {} + (ficha dueno, pareja 1) -> hilo [1];
// + (ficha con 2 personas, pareja 2) -> papel sigue dueno, personas 2, hilo [1, 2].
describe("anotarEnMemoria: la memoria del proyecto crece en cada turno", () => {
  it("fusiona la ficha y añade la pareja al final del hilo, sin perder lo anterior", async () => {
    let memoria: unknown = {};
    const client = {
      from: () => ({
        select: () => ({ eq: () => ({ limit: async () => ({ data: [{ memoria }], error: null }) }) }),
        update: (payload: { memoria: unknown }) => {
          memoria = payload.memoria;
          return { eq: async () => ({ error: null }) };
        },
      }),
    } as unknown as SupabaseClient;
    const p1 = { sesion: "s1", dominio: "core", nodo: "n1", pregunta: "¿Que vendes?", respuesta: "Macetas", en: "t1" };
    const p2 = { sesion: "s1", dominio: "core", nodo: "n2", pregunta: "¿Con quien?", respuesta: "Con dos empleados", en: "t2" };
    await anotarEnMemoria(client, "p1", { papel: "dueno" }, p1);
    await anotarEnMemoria(client, "p1", { equipo: { personas: 2, descripcion: null } }, p2);
    const m = memoria as { ficha: { papel: string; equipo: { personas: number } }; hilo: unknown[] };
    expect(m.ficha.papel).toBe("dueno");
    expect(m.ficha.equipo.personas).toBe(2);
    expect(m.hilo).toEqual([p1, p2]);
  });

  it("sin pareja (primer turno de una sesion) solo actualiza la ficha", async () => {
    let memoria: unknown = { ficha: { papel: "empleado" }, hilo: [{ sesion: "s0", dominio: "core", nodo: null, pregunta: null, respuesta: "x", en: "t0" }] };
    const client = {
      from: () => ({
        select: () => ({ eq: () => ({ limit: async () => ({ data: [{ memoria }], error: null }) }) }),
        update: (payload: { memoria: unknown }) => {
          memoria = payload.memoria;
          return { eq: async () => ({ error: null }) };
        },
      }),
    } as unknown as SupabaseClient;
    await anotarEnMemoria(client, "p1", { tiene_jefe: true }, null);
    const m = memoria as { ficha: { papel: string; tiene_jefe: boolean }; hilo: unknown[] };
    expect(m.ficha).toMatchObject({ papel: "empleado", tiene_jefe: true });
    expect(m.hilo).toHaveLength(1);
  });
});
