// Fase 4.2 §2 — POST /api/project/[id]/world/[pack]/completar: el cierre de un
// mundo, el acta en miniatura. Los asertos que importan no son los conteos: son
// las PROMESAS que el producto le hace al usuario y que un refactor podria
// romper en silencio —
//   1. cerrar no exige el checklist al 100% (soberania del usuario),
//   2. los items pendientes quedan INTACTOS (son testigos, no basura),
//   3. reabrir NO borra el motivo (la historia no se reescribe),
//   4. cerrar un mundo NO cierra la idea (§3: jerarquia honesta).
import { beforeEach, describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));

import { POST } from "./route";

const PARAMS = { params: Promise.resolve({ id: "p1", pack: "quality" }) };

function req(body: unknown) {
  return new Request("http://x/api/project/p1/world/quality/completar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

function sembrar({ completadoAt = null, motivo = null }: { completadoAt?: string | null; motivo?: string | null } = {}) {
  estadoFalso.projects["p1"] = {
    id: "p1",
    user_id: "user-fake",
    titulo: "Macetas",
    entrada_original: "vendo macetas",
    session_count: 3,
    realizada_at: null,
  };
  estadoFalso.projectUnlocks.push({
    project_id: "p1",
    dominio: "quality",
    completado_at: completadoAt,
    cierre_motivo: motivo,
  });
  // Un mundo a medias: 1 de 3 hecho. El cierre no puede exigir mas.
  estadoFalso.checklistItems.push(
    { id: "i1", project_id: "p1", dominio: "quality", estado: "hecho" },
    { id: "i2", project_id: "p1", dominio: "quality", estado: "pendiente" },
    { id: "i3", project_id: "p1", dominio: "quality", estado: "a_medias" }
  );
}

const unlock = () => estadoFalso.projectUnlocks[0];

describe("POST world/[pack]/completar (Fase 4.2 §2)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("404 si el mundo no existe en el catálogo", async () => {
    sembrar();
    const res = await POST(req({ accion: "completar" }), {
      params: Promise.resolve({ id: "p1", pack: "mundo_inventado" }),
    });
    expect(res.status).toBe(404);
  });

  it("400 si la acción no es 'completar' ni 'reabrir'", async () => {
    sembrar();
    expect((await POST(req({ accion: "borrar" }), PARAMS)).status).toBe(400);
  });

  it("401 si no hay usuario", async () => {
    sembrar();
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    expect((await POST(req({ accion: "completar" }), PARAMS)).status).toBe(401);
  });

  it("403 si el mundo no está activado para esta idea (el muro)", async () => {
    estadoFalso.projects["p1"] = { id: "p1", user_id: "user-fake", entrada_original: "x", session_count: 1 };
    const res = await POST(req({ accion: "completar" }), PARAMS);
    expect(res.status).toBe(403);
  });

  it("cierra SIN exigir el checklist al 100% (1 de 3 y se cierra igual)", async () => {
    sembrar();
    const res = await POST(req({ accion: "completar", motivo: null }), PARAMS);
    expect(res.status).toBe(200);
    expect(unlock().completado_at).toBeTruthy();
  });

  it("los ítems pendientes quedan INTACTOS: son testigos, no se limpian", async () => {
    sembrar();
    await POST(req({ accion: "completar" }), PARAMS);
    expect(estadoFalso.checklistItems.map((i) => i.estado)).toEqual(["hecho", "pendiente", "a_medias"]);
  });

  it("guarda el motivo cuando lo hay, y lo devuelve", async () => {
    sembrar();
    const res = await POST(req({ accion: "completar", motivo: "  Ya tengo el protocolo.  " }), PARAMS);
    expect((await res.json()).cierre_motivo).toBe("Ya tengo el protocolo.");
    expect(unlock().cierre_motivo).toBe("Ya tengo el protocolo.");
  });

  it("cerrar sin escribir nada es legítimo: cero fricción", async () => {
    sembrar();
    const res = await POST(req({ accion: "completar" }), PARAMS);
    expect(res.status).toBe(200);
    expect(unlock().cierre_motivo).toBeNull();
  });

  it("REABRIR no borra el motivo: la historia no se reescribe", async () => {
    sembrar({ completadoAt: "2026-05-01T10:00:00Z", motivo: "Ya tengo el protocolo." });
    const res = await POST(req({ accion: "reabrir" }), PARAMS);
    expect(res.status).toBe(200);
    expect(unlock().completado_at).toBeNull();
    expect(unlock().cierre_motivo).toBe("Ya tengo el protocolo.");
    expect((await res.json()).cierre_motivo).toBe("Ya tengo el protocolo.");
  });

  it("cerrar de nuevo SIN motivo no pisa el motivo del cierre anterior", async () => {
    sembrar({ completadoAt: null, motivo: "El primer porqué." });
    await POST(req({ accion: "completar" }), PARAMS);
    expect(unlock().cierre_motivo).toBe("El primer porqué.");
  });

  it("cada acción deja su rastro en la bitácora, con mundo y motivo", async () => {
    sembrar();
    await POST(req({ accion: "completar", motivo: "Listo." }), PARAMS);
    await POST(req({ accion: "reabrir" }), PARAMS);
    expect(estadoFalso.bitacora).toEqual([
      { project_id: "p1", tipo: "mundo_completado", payload: { mundo: "quality", accion: "completar", motivo: "Listo." } },
      { project_id: "p1", tipo: "mundo_completado", payload: { mundo: "quality", accion: "reabrir", motivo: null } },
    ]);
  });

  // §3 — LA JERARQUÍA HONESTA, en su dirección más fácil de romper.
  it("completar un mundo NO cierra la idea", async () => {
    sembrar();
    await POST(req({ accion: "completar" }), PARAMS);
    expect(estadoFalso.projects["p1"].realizada_at).toBeNull();
  });

  it("un motivo desmedido se rechaza antes de tocar nada", async () => {
    sembrar();
    const res = await POST(req({ accion: "completar", motivo: "x".repeat(20_000) }), PARAMS);
    expect(res.status).toBe(400);
    expect(unlock().completado_at).toBeNull();
  });
});
