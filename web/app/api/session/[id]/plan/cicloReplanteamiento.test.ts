// Ciclo de replanteamiento, Fase 2 (decisiones del fundador, 27 sep 2026): la
// ENTREGA del plan de un ciclo posterior en POST /api/session/[id]/plan.
//  - Replantear: sin camino elegido no se genera; con él, la ruta es la del
//    camino, el plan sale 'replanteamiento', se aparta y se cobra la clave
//    replanteamiento de precios.ts, lo que "me sigue sirviendo" entra HECHO al
//    checklist nuevo con su enlace a la original, y la historia queda en la
//    bitácora.
//  - Profundizar: el plan sale 'seguimiento' y lo que la persona contó queda en
//    la bitácora.
//  - Los dos: la IA recibe el plan anterior (etapas y tareas con su estado).
// Mismo arnés que route.test.ts: grafo real, Anthropic y Supabase falsos.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { cargarGrafo } from "@/lib/engine/graph";
import { SERVIDOR_SESION } from "@/lib/i18n/mensajes/servidorSesion";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/creditos", async (importOriginal) => {
  const real = await importOriginal<typeof import("@/lib/creditos")>();
  return {
    ...real,
    verificarSaldo: vi.fn(async () => ({ alcanza: true, creditos: 20 })),
    cobrar: vi.fn(async () => 15),
    reembolsar: vi.fn(async () => 20),
    reservarCreditos: vi.fn(async () => ({ reservado: true, disponible: 10 })),
    resolverReserva: vi.fn(async () => undefined),
  };
});
vi.mock("@/lib/seguridad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/seguridad")>()),
  faltaSegundoFactor: async () => false,
}));
vi.mock("@/lib/supabase/server", () => ({ createClient: vi.fn(async () => supabaseFalso) }));
const messagesStreamFalso = vi.fn();
vi.mock("@/lib/anthropicClient", () => ({
  createAnthropicClient: vi.fn(() => ({ messages: { stream: messagesStreamFalso } })),
}));

import { POST } from "./route";
import { cobrar, reservarCreditos } from "@/lib/creditos";

const RAW = '# Plan nuevo\n\n## Etapa 1: Arranca\n\n**Pasos:**\n1. Llama a Ana.\n\n===JSON===\n{"familias_tratadas": []}';
function streamOk() {
  return {
    on(evento: string, cb: (t: string) => void) {
      if (evento === "text") cb(RAW);
      return this;
    },
    async finalMessage() {
      return { content: [{ type: "text", text: RAW }], usage: { input_tokens: 500, output_tokens: 200 } };
    },
  };
}

const graph = cargarGrafo();
const N1 = "design_thinking_fundamentos";
const N2 = graph[N1].nodos_siguientes!.find((n) => n in graph && (graph[n].dominio ?? "core") === "core") as string;

function sembrar(ciclo: Record<string, unknown>) {
  estadoFalso.projects["p1"] = { id: "p1", session_count: 2, titulo: "Pan", numeros_proyecto: {} };
  estadoFalso.sessions["s0"] = { id: "s0", project_id: "p1", closed_at: "2026-09-01T00:00:00Z" };
  estadoFalso.plans.push({
    id: "pl0",
    session_id: "s0",
    dominio: "core",
    etiqueta: "completo",
    contenido_md: "# Pan\n\n## Etapa 1: Valida\n",
    created_at: "2026-09-01T00:00:00Z",
  });
  estadoFalso.checklistItems.push(
    { id: "t1", project_id: "p1", plan_id: "pl0", dominio: "core", etapa: 1, orden: 1, texto: "Hablar con 5 panaderías", destacado: false, estado: "hecho", nota: "dos sí", completed_at: "2026-09-10T15:00:00Z" },
    { id: "t3", project_id: "p1", plan_id: "pl0", dominio: "core", etapa: 1, orden: 2, texto: "Pintar el local", destacado: false, estado: "pendiente", nota: null, completed_at: null }
  );
  estadoFalso.sessions["s1"] = {
    id: "s1",
    project_id: "p1",
    closed_at: null,
    estado_recorrido: {
      recorrido: {
        ruta: [N1],
        modos: ["conversado"],
        perfilSesion: "vende pan",
        textoOriginal: "Quiero replantear mi camino.",
        profundizarOfrecido: false,
        esSeguimiento: true,
        estadoVivoPrevio: "vende pan",
        nodosCubiertosPrevios: [],
        dominiosDesbloqueados: ["core"],
        dominioSesion: "core",
        puertasDescartadas: [],
        snapshotNucleo: null,
        fallbackEvents: [],
        prioridadDeclarada: null,
        preguntaPendiente: null,
        ultimasPreguntas: [],
        repreguntasUsadas: 0,
        historialMensajes: [],
        numerosDetectadosSesion: {},
        tipoOfertaSesion: null,
        unidadVentaSesion: null,
        fase: "listo_para_plan",
        sigamosDirigido: null,
        ciclo,
      },
      acumulado: { uso: {}, uso_por_componente: {}, presupuesto_excedido: false },
    },
  };
}

const REPLANTEO = {
  tipo: "replantear",
  historia: "Se cayó el local.",
  conserva: [{ id: "t1", texto: "Hablar con 5 panaderías", nota: "dos sí", completed_at: "2026-09-10T15:00:00Z", etapa: 1 }],
  suelta: [],
  caminos: [{ id: "a", titulo: "Vender por encargo", descripcion: "Sin local.", nodos: [N1, N2] }],
  caminoElegido: null,
};

const pedir = (body?: unknown) =>
  POST(
    new Request("http://test/api/session/s1/plan", {
      method: "POST",
      ...(body === undefined ? {} : { headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) }),
    }),
    { params: Promise.resolve({ id: "s1" }) }
  );

describe("la entrega de un replanteamiento", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    messagesStreamFalso.mockReset();
    vi.mocked(cobrar).mockClear();
    vi.mocked(reservarCreditos).mockClear();
  });

  it("sin camino elegido: 400 con el mensaje del catálogo, sin apartar ni llamar a la IA", async () => {
    sembrar(REPLANTEO);
    const res = await pedir();
    expect(res.status).toBe(400);
    expect((await res.json()).error).toBe(SERVIDOR_SESION.es.plan.eligeCamino);
    expect(messagesStreamFalso).not.toHaveBeenCalled();
    expect(reservarCreditos).not.toHaveBeenCalled();
  });

  it("con el camino: su ruta, etiqueta replanteamiento, cobro de su clave, la heredada hecha y la historia en la bitácora", async () => {
    sembrar(REPLANTEO);
    messagesStreamFalso.mockReturnValueOnce(streamOk());
    const res = await pedir({ camino: "a" });
    await res.text();

    // A MANO: núcleo + replanteamiento -> PRECIOS.replanteamiento = 5.
    expect(reservarCreditos).toHaveBeenCalledWith(expect.any(String), "plan:s1", "replanteamiento", 5);
    expect(cobrar).toHaveBeenCalledWith(expect.any(String), "replanteamiento", 5, "plan:s1");

    const payload = JSON.parse(messagesStreamFalso.mock.calls[0][0].messages[0].content);
    expect(payload.material_principal.map((m: { id: string }) => m.id)).toEqual([N1, N2]);
    expect(payload.replanteamiento).toEqual({
      historia: "Se cayó el local.",
      se_conserva: ["Hablar con 5 panaderías"],
      se_suelta: [],
      camino_elegido: { titulo: "Vender por encargo", descripcion: "Sin local." },
    });
    expect(payload.plan_anterior).toEqual({
      etapas: [
        {
          numero: 1,
          titulo: "Valida",
          tareas: [
            { texto: "Hablar con 5 panaderías", estado: "hecho", nota: "dos sí" },
            { texto: "Pintar el local", estado: "pendiente" },
          ],
        },
      ],
    });

    const nuevo = estadoFalso.plans.find((p) => p.session_id === "s1") as Record<string, unknown>;
    expect(nuevo.etiqueta).toBe("replanteamiento");
    const heredada = estadoFalso.checklistItems.find((i) => i.heredado_de === "t1") as Record<string, unknown>;
    expect(heredada).toMatchObject({
      plan_id: nuevo.id,
      estado: "hecho",
      texto: "Hablar con 5 panaderías",
      completed_at: "2026-09-10T15:00:00Z",
      nota: "dos sí",
      etapa: 1,
      orden: -1,
    });
    const evento = estadoFalso.bitacora.find((e) => e.tipo === "ciclo_replanteado") as { payload: Record<string, unknown> };
    expect(evento.payload).toEqual({
      dominio: "core",
      plan_id: nuevo.id,
      relato: "Se cayó el local.",
      camino: "Vender por encargo",
      conserva: 1,
      suelta: 0,
    });
  });
});

describe("la entrega de una profundización", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    messagesStreamFalso.mockReset();
    vi.mocked(cobrar).mockClear();
  });

  it("etiqueta seguimiento, cobro del seguimiento, el plan anterior a la IA y lo que contó en la bitácora", async () => {
    sembrar({ tipo: "profundizar", detalles: "Vendí 10 panes.", enfoque: null });
    messagesStreamFalso.mockReturnValueOnce(streamOk());
    const res = await pedir();
    await res.text();
    expect(cobrar).toHaveBeenCalledWith(expect.any(String), "seguimiento", 5, "plan:s1");
    const payload = JSON.parse(messagesStreamFalso.mock.calls[0][0].messages[0].content);
    expect(payload.plan_anterior.etapas[0].titulo).toBe("Valida");
    expect("replanteamiento" in payload).toBe(false);
    const nuevo = estadoFalso.plans.find((p) => p.session_id === "s1") as Record<string, unknown>;
    expect(nuevo.etiqueta).toBe("seguimiento");
    expect(estadoFalso.checklistItems.some((i) => i.heredado_de)).toBe(false);
    const evento = estadoFalso.bitacora.find((e) => e.tipo === "ciclo_profundizado") as { payload: Record<string, unknown> };
    expect(evento.payload).toEqual({ dominio: "core", plan_id: nuevo.id, relato: "Vendí 10 panes." });
  });
});
