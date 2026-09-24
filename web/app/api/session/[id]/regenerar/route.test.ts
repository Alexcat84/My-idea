// POST /api/session/[id]/regenerar (AUD-09, decisión del fundador 25 sep 2026):
// regenerar un plan básico es una SESIÓN NUEVA con su presupuesto completo,
// que parte del perfil ya capturado (sin repetir la entrevista). La ruta solo
// prepara esa sesión; el plan sale por la ruta de siempre, que cobra el precio
// normal SOLO si la IA entrega.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));
vi.mock("@/lib/seguridad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/seguridad")>()),
  faltaSegundoFactor: async () => false,
}));
const verificarSaldo = vi.fn(async () => ({ alcanza: true, creditos: 20 }));
vi.mock("@/lib/creditos", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/creditos")>()),
  verificarSaldo: (...a: unknown[]) => verificarSaldo(...(a as [])),
}));
const verificarLimiteDiario = vi.fn(async () => ({ permitido: true }));
vi.mock("@/lib/rateLimit", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/rateLimit")>()),
  identidadLimite: () => "id",
  verificarFusibleGlobal: vi.fn(async () => ({ permitido: true })),
  verificarLimiteDiario: (...a: unknown[]) => verificarLimiteDiario(...(a as [])),
}));

import { POST } from "./route";

const agotado = { uso: { "claude-sonnet-4-6": { in: 0, out: 10_000_000 } }, uso_por_componente: {}, presupuesto_excedido: true };

function recorrido(esSeguimiento: boolean) {
  return {
    ruta: ["design_thinking_fundamentos"],
    modos: ["conversado"],
    perfilSesion: "Hace macetas de cemento.",
    textoOriginal: "quiero vender macetas",
    esSeguimiento,
    fase: "cerrada",
    preguntaPendiente: null,
    fallbackEvents: [],
  };
}

function sembrar(opts: { basico: boolean; dominio?: string; esSeguimiento?: boolean }) {
  estadoFalso.projects["p1"] = { id: "p1", session_count: 1 };
  estadoFalso.sessions["s-basico"] = {
    id: "s-basico",
    project_id: "p1",
    tipo: opts.esSeguimiento ? "seguimiento" : "inicial",
    dominio: opts.dominio ?? "core",
    closed_at: "2026-09-20T00:00:00Z",
    decisiones: opts.basico ? [{ tipo: "plan_version_basica", motivo: "techo" }] : [{ tipo: "decision_turno" }],
    estado_recorrido: { recorrido: recorrido(opts.esSeguimiento ?? false), acumulado: agotado },
  };
}

const pedir = () =>
  POST(new Request("http://test/api/session/s-basico/regenerar", { method: "POST" }), {
    params: Promise.resolve({ id: "s-basico" }),
  });

describe("POST /api/session/[id]/regenerar", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    verificarSaldo.mockReset().mockImplementation(async () => ({ alcanza: true, creditos: 20 }));
    verificarLimiteDiario.mockReset().mockImplementation(async () => ({ permitido: true }));
  });

  it("un plan que NO es básico no se regenera (409)", async () => {
    sembrar({ basico: false });
    const res = await pedir();
    expect(res.status).toBe(409);
    expect(Object.keys(estadoFalso.sessions)).toEqual(["s-basico"]);
  });

  it("sin saldo: 402 sin crear sesión ni gastar el límite diario", async () => {
    sembrar({ basico: true });
    verificarSaldo.mockImplementation(async () => ({ alcanza: false, creditos: 0 }));
    const res = await pedir();
    expect(res.status).toBe(402);
    expect(Object.keys(estadoFalso.sessions)).toEqual(["s-basico"]);
    expect(verificarLimiteDiario).not.toHaveBeenCalled();
  });

  it("crea una sesión NUEVA con el perfil ya capturado y presupuesto completo", async () => {
    sembrar({ basico: true });
    const res = await pedir();
    expect(res.status).toBe(200);
    const cuerpo = await res.json();
    // Cálculo a mano: núcleo, primera entrevista -> plan_completo = 10.
    expect(cuerpo.costo).toBe(10);
    const nueva = estadoFalso.sessions[cuerpo.session_id] as Record<string, unknown>;
    expect(nueva).toBeTruthy();
    expect(cuerpo.session_id).not.toBe("s-basico");
    const estado = nueva.estado_recorrido as { recorrido: Record<string, unknown>; acumulado: Record<string, unknown> };
    expect(estado.recorrido.perfilSesion).toBe("Hace macetas de cemento.");
    expect(estado.recorrido.ruta).toEqual(["design_thinking_fundamentos"]);
    expect(estado.recorrido.fase).toBe("listo_para_plan");
    // presupuesto completo: el acumulado arranca vacío
    expect(estado.acumulado.uso).toEqual({});
    expect(estado.acumulado.presupuesto_excedido).toBe(false);
    // la sesión del plan básico queda como estaba (su plan queda archivado)
    expect(estadoFalso.sessions["s-basico"].closed_at).toBe("2026-09-20T00:00:00Z");
  });

  it("un seguimiento básico de mundo se regenera en su mundo y a su precio", async () => {
    sembrar({ basico: true, dominio: "quality", esSeguimiento: true });
    const res = await pedir();
    const cuerpo = await res.json();
    // Cálculo a mano: mundo + seguimiento -> mundo_seguimiento = 5.
    expect(cuerpo.costo).toBe(5);
    const nueva = estadoFalso.sessions[cuerpo.session_id] as Record<string, unknown>;
    expect(nueva.dominio).toBe("quality");
    expect(nueva.tipo).toBe("seguimiento");
  });
});
