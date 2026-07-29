// Fase 3.8 §2/§4 — pruebas del PATCH del checklist ampliado con el sentido
// del tiempo: completed_at (timeline real, para TODOS) y fecha_base
// (replanificación que NO reescribe la historia).
import { beforeEach, describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));

import { PATCH } from "./route";

const PARAMS = { params: Promise.resolve({ id: "p1" }) };

function req(body: unknown) {
  return new Request("http://x/api/project/p1/checklist", {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

function sembrarItem(extra: Record<string, unknown> = {}) {
  estadoFalso.projects["p1"] = {
    id: "p1",
    user_id: "user-fake",
    titulo: "Idea",
    entrada_original: "una idea",
    session_count: 1,
  };
  estadoFalso.checklistItems.push({
    id: "it1",
    project_id: "p1",
    plan_id: "plan-1",
    dominio: "core",
    etapa: 1,
    orden: 0,
    texto: "Compra dos termos",
    destacado: false,
    estado: "pendiente",
    nota: null,
    completed_at: null,
    no_aplica_motivo: null,
    fecha_base: null,
    fecha_base_origen: null,
    fecha_base_original: null,
    ...extra,
  });
}

describe("PATCH /api/project/[id]/checklist — sentido del tiempo (Fase 3.8)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("401 si no hay usuario", async () => {
    sembrarItem();
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    const res = await PATCH(req({ item_id: "it1", estado: "hecho" }), PARAMS);
    expect(res.status).toBe(401);
  });

  it("400 si falta item_id", async () => {
    sembrarItem();
    const res = await PATCH(req({ estado: "hecho" }), PARAMS);
    expect(res.status).toBe(400);
  });

  it("400 si no hay nada que actualizar", async () => {
    sembrarItem();
    const res = await PATCH(req({ item_id: "it1" }), PARAMS);
    expect(res.status).toBe(400);
  });

  it("marcar hecho SIN completed_at → default a ahora (no null)", async () => {
    sembrarItem();
    const antes = Date.now();
    const res = await PATCH(req({ item_id: "it1", estado: "hecho" }), PARAMS);
    expect(res.status).toBe(200);
    const { item } = await res.json();
    expect(item.estado).toBe("hecho");
    expect(item.completed_at).toBeTruthy();
    const t = Date.parse(item.completed_at);
    // el default cae dentro de una ventana razonable alrededor de ahora
    expect(t).toBeGreaterThanOrEqual(antes - 1000);
    expect(t).toBeLessThanOrEqual(Date.now() + 1000);
  });

  it("salir de hecho (a pendiente) limpia completed_at", async () => {
    sembrarItem({ estado: "hecho", completed_at: "2026-03-20T12:00:00.000Z" });
    const res = await PATCH(req({ item_id: "it1", estado: "pendiente" }), PARAMS);
    const { item } = await res.json();
    expect(item.estado).toBe("pendiente");
    expect(item.completed_at).toBeNull();
  });

  // Gestor de estados (migration 030): retirar una tarea guarda el motivo y no
  // la deja como hecha; reactivarla limpia el motivo (la historia va a bitácora).
  it("retirar (no_aplica) guarda el motivo y no queda completada", async () => {
    sembrarItem();
    const res = await PATCH(
      req({ item_id: "it1", estado: "no_aplica", no_aplica_motivo: "  mi negocio es online  " }),
      PARAMS
    );
    expect(res.status).toBe(200);
    const { item } = await res.json();
    expect(item.estado).toBe("no_aplica");
    expect(item.no_aplica_motivo).toBe("mi negocio es online");
    expect(item.completed_at).toBeNull();
  });

  it("retirar sin motivo → no_aplica con motivo null", async () => {
    sembrarItem();
    const { item } = await (await PATCH(req({ item_id: "it1", estado: "no_aplica" }), PARAMS)).json();
    expect(item.estado).toBe("no_aplica");
    expect(item.no_aplica_motivo).toBeNull();
  });

  it("reactivar una retirada (a pendiente) limpia el motivo", async () => {
    sembrarItem({ estado: "no_aplica", no_aplica_motivo: "no aplicaba" });
    const { item } = await (await PATCH(req({ item_id: "it1", estado: "empezado" }), PARAMS)).json();
    expect(item.estado).toBe("empezado");
    expect(item.no_aplica_motivo).toBeNull();
  });

  it("editar solo el motivo de una tarea ya retirada, sin tocar el estado", async () => {
    sembrarItem({ estado: "no_aplica", no_aplica_motivo: "viejo" });
    const { item } = await (await PATCH(req({ item_id: "it1", no_aplica_motivo: "nuevo motivo" }), PARAMS)).json();
    expect(item.estado).toBe("no_aplica");
    expect(item.no_aplica_motivo).toBe("nuevo motivo");
  });

  it("acepta completed_at pasado explícito", async () => {
    sembrarItem();
    // 2026-03-15 mediodía local → una fecha claramente pasada respecto a hoy (2026-07)
    const res = await PATCH(
      req({ item_id: "it1", estado: "hecho", completed_at: "2026-03-15T12:00:00.000Z" }),
      PARAMS
    );
    const { item } = await res.json();
    expect(item.completed_at).toBe("2026-03-15T12:00:00.000Z");
  });

  it("400 si completed_at es futuro", async () => {
    sembrarItem();
    const futuro = new Date(Date.now() + 5 * 24 * 3600 * 1000).toISOString();
    const res = await PATCH(req({ item_id: "it1", estado: "hecho", completed_at: futuro }), PARAMS);
    expect(res.status).toBe(400);
  });

  // Replanificación (§4): mover una fecha_base que existía (origen 'sugerida')
  // preserva la PRIMERA en fecha_base_original y el origen pasa a 'ajustada'.
  it("replan: preserva fecha_base_original y pone origen 'ajustada'", async () => {
    sembrarItem({ fecha_base: "2026-03-20T12:00:00.000Z", fecha_base_origen: "sugerida", fecha_base_original: null });
    const res = await PATCH(req({ item_id: "it1", fecha_base: "2026-03-27" }), PARAMS);
    const { item } = await res.json();
    expect(item.fecha_base).toBe("2026-03-27T00:00:00.000Z");
    expect(item.fecha_base_original).toBe("2026-03-20T12:00:00.000Z");
    expect(item.fecha_base_origen).toBe("ajustada");
  });

  it("replan repetido NO reescribe fecha_base_original (guarda solo la primera)", async () => {
    sembrarItem({
      fecha_base: "2026-03-27T12:00:00.000Z",
      fecha_base_origen: "ajustada",
      fecha_base_original: "2026-03-20T12:00:00.000Z",
    });
    const res = await PATCH(req({ item_id: "it1", fecha_base: "2026-04-03" }), PARAMS);
    const { item } = await res.json();
    expect(item.fecha_base_original).toBe("2026-03-20T12:00:00.000Z");
    expect(item.fecha_base_origen).toBe("ajustada");
  });

  it("primera fecha_base fuera del ritual → origen 'manual', original null", async () => {
    sembrarItem();
    const res = await PATCH(req({ item_id: "it1", fecha_base: "2026-05-01" }), PARAMS);
    const { item } = await res.json();
    expect(item.fecha_base).toBe("2026-05-01T00:00:00.000Z");
    expect(item.fecha_base_origen).toBe("manual");
    expect(item.fecha_base_original).toBeNull();
  });

  // Fase 4.8: cada decisión deja rastro en la bitácora para la historia completa.
  const ult = () => estadoFalso.bitacora.at(-1) as { tipo: string; payload: Record<string, unknown> } | undefined;

  it("cambiar a 'empezado' o 'en proceso' registra item_estado", async () => {
    sembrarItem();
    await PATCH(req({ item_id: "it1", estado: "empezado" }), PARAMS);
    expect(ult()).toMatchObject({ tipo: "item_estado", payload: { de: "pendiente", a: "empezado" } });
    await PATCH(req({ item_id: "it1", estado: "en_proceso" }), PARAMS);
    expect(ult()).toMatchObject({ tipo: "item_estado", payload: { a: "en_proceso" } });
  });

  it("marcar HECHO no registra item_estado (su entrada nace de completed_at)", async () => {
    sembrarItem();
    await PATCH(req({ item_id: "it1", estado: "hecho" }), PARAMS);
    expect(estadoFalso.bitacora.some((b) => (b as { tipo: string }).tipo === "item_estado")).toBe(false);
  });

  it("ajustar la fecha de algo YA hecho registra fecha_hecho_movida", async () => {
    sembrarItem({ estado: "hecho", completed_at: "2026-03-20T12:00:00.000Z" });
    await PATCH(req({ item_id: "it1", completed_at: "2026-03-22" }), PARAMS);
    expect(ult()).toMatchObject({ tipo: "fecha_hecho_movida", payload: { item: "it1" } });
  });

  it("escribir una nota registra nota_escrita (sin el contenido)", async () => {
    sembrarItem();
    await PATCH(req({ item_id: "it1", nota: "recordar llamar al proveedor" }), PARAMS);
    const b = ult()!;
    expect(b.tipo).toBe("nota_escrita");
    expect(JSON.stringify(b.payload)).not.toContain("proveedor");
  });
});
