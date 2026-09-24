// AUD-09 M24 (tanda 7A, dinero): Tus Números dice "Incluido con tu plan"
// (PRECIOS.tus_numeros === 0: el plan es su cobro), pero la ruta no exigía
// plan: sin plan del núcleo se podía activar el tablero y narrar con la IA
// gratis. La regla: activar y narrar piden plan del núcleo, igual que /report
// desde la tanda 1. El recálculo determinista de un tablero ya activo sigue
// gratis y sin tope, por ley.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));
vi.mock("@/lib/anthropicClient", () => ({
  createAnthropicClient: vi.fn(() => ({ messages: { create: vi.fn() } })),
}));
vi.mock("@/lib/seguridad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/seguridad")>()),
  faltaSegundoFactor: async () => false,
}));
const narrarFalso = vi.fn(async () => ({ contenido: "narración", sinIA: false, acumulado: { uso: {}, uso_por_componente: {}, presupuesto_excedido: false } }));
vi.mock("@/lib/engine/reporte", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/engine/reporte")>()),
  narrarReporte: (...a: unknown[]) => narrarFalso(...(a as [])),
}));
let planCore: string | null = "plan-core-1";
const activarFalso = vi.fn(async () => ({ activadoAhora: true, activadoAt: "2026-09-25T12:00:00Z" }));
vi.mock("@/lib/db", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/db")>()),
  obtenerPlanCoreVigente: async () => planCore,
  activarTusNumeros: (...a: unknown[]) => activarFalso(...(a as [])),
  contarNarracionesHoy: async () => 0,
  ultimaVersionNumeros: async () => null,
  insertarVersionNumeros: async () => undefined,
  historialVersionesNumeros: async () => [],
}));

import { POST } from "./route";

const ctx = { params: Promise.resolve({ id: "p1" }) };
const req = (body: unknown) =>
  new Request("http://test/api/project/p1/numeros", { method: "POST", body: JSON.stringify(body) });

describe("Tus Números pide plan para activar y narrar (AUD-09 M24)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    planCore = "plan-core-1";
    narrarFalso.mockClear();
    activarFalso.mockClear();
  });

  it("sin plan del núcleo, activar responde 409 y no activa", async () => {
    estadoFalso.projects["p1"] = { id: "p1", numeros_proyecto: {}, tus_numeros_activado_at: null };
    planCore = null;
    const res = await POST(req({ activar: true }), ctx);
    expect(res.status).toBe(409);
    expect((await res.json()).error).toMatch(/plan/);
    expect(activarFalso).not.toHaveBeenCalled();
  });

  it("sin plan del núcleo, narrar responde 409 y no llama a la IA (aunque ya estuviera activado)", async () => {
    estadoFalso.projects["p1"] = { id: "p1", numeros_proyecto: {}, tus_numeros_activado_at: "2026-09-01T00:00:00Z" };
    planCore = null;
    const res = await POST(req({ narrar: true }), ctx);
    expect(res.status).toBe(409);
    expect(narrarFalso).not.toHaveBeenCalled();
  });

  it("con plan, activar funciona como siempre", async () => {
    estadoFalso.projects["p1"] = { id: "p1", numeros_proyecto: {}, tus_numeros_activado_at: null };
    const res = await POST(req({ activar: true }), ctx);
    expect(res.status).toBe(200);
    expect(activarFalso).toHaveBeenCalledTimes(1);
  });

  it("el recálculo de un tablero ya activo sigue gratis aunque no haya plan", async () => {
    estadoFalso.projects["p1"] = { id: "p1", numeros_proyecto: {}, tus_numeros_activado_at: "2026-09-01T00:00:00Z" };
    planCore = null;
    const res = await POST(req({}), ctx);
    expect(res.status).toBe(200);
  });
});
