// Fase 3.8 §5 — POST /api/project/[id]/realizar: marcar realizada / reabrir.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio, type EstadoFalso } from "@/lib/testUtils/fakeSupabase";

let estadoFalso: EstadoFalso = estadoFalsoVacio();
let supabaseFalso = crearSupabaseFalso(estadoFalso);

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));

import { POST } from "./route";

const PARAMS = { params: Promise.resolve({ id: "p1" }) };

function req(body: unknown) {
  return new Request("http://x/api/project/p1/realizar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

function sembrar(realizada: string | null = null) {
  estadoFalso.projects["p1"] = {
    id: "p1",
    user_id: "user-fake",
    entrada_original: "idea",
    session_count: 1,
    realizada_at: realizada,
  };
}

describe("POST /api/project/[id]/realizar (Fase 3.8)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("400 si la accion es inválida", async () => {
    sembrar();
    expect((await POST(req({ accion: "borrar" }), PARAMS)).status).toBe(400);
  });

  it("401 si no hay usuario", async () => {
    sembrar();
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    expect((await POST(req({ accion: "realizar" }), PARAMS)).status).toBe(401);
  });

  it("realizar sella realizada_at (no null)", async () => {
    sembrar(null);
    const res = await POST(req({ accion: "realizar" }), PARAMS);
    expect(res.status).toBe(200);
    expect((await res.json()).realizada_at).toBeTruthy();
    expect(estadoFalso.projects["p1"].realizada_at).toBeTruthy();
  });

  // AUD-09 (tanda 5, dinero e historia): volver a cerrar una idea YA cerrada no
  // reescribe la fecha del primer cierre ("la historia no se reescribe").
  it("realizar una idea ya realizada conserva la fecha del primer cierre", async () => {
    sembrar("2026-05-01T12:00:00.000Z");
    const res = await POST(req({ accion: "realizar" }), PARAMS);
    expect(res.status).toBe(200);
    expect((await res.json()).realizada_at).toBe("2026-05-01T12:00:00.000Z");
    expect(estadoFalso.projects["p1"].realizada_at).toBe("2026-05-01T12:00:00.000Z");
  });

  it("reabrir pone realizada_at a null", async () => {
    sembrar("2026-05-01T12:00:00.000Z");
    const res = await POST(req({ accion: "reabrir" }), PARAMS);
    expect(res.status).toBe(200);
    expect((await res.json()).realizada_at).toBeNull();
    expect(estadoFalso.projects["p1"].realizada_at).toBeNull();
  });

  // AUD-09 M04 (decisión del fundador, 25 sep 2026): EL ACTA ES UNA FOTO.
  describe("el cierre guarda la foto del acta en su propio registro", () => {
    it("cerrar guarda una instantánea (dominio core) con la fecha y el motivo", async () => {
      sembrar(null);
      const res = await POST(req({ accion: "realizar", motivo: "ya vendo cada semana" }), PARAMS);
      expect(res.status).toBe(200);
      expect(estadoFalso.projectActas).toHaveLength(1);
      const acta = estadoFalso.projectActas[0] as Record<string, unknown>;
      expect(acta.dominio).toBe("core");
      expect(acta.cierre_motivo).toBe("ya vendo cada semana");
      expect(acta.cerrada_at).toBe(estadoFalso.projects["p1"].realizada_at);
      expect((acta.instantanea as { acciones: unknown }).acciones).toEqual({ hechas: 0, total: 0 });
    });

    it("volver a cerrar tras reabrir guarda OTRA foto al lado, sin pisar la primera", async () => {
      sembrar(null);
      await POST(req({ accion: "realizar" }), PARAMS);
      const primera = { ...(estadoFalso.projectActas[0] as Record<string, unknown>) };
      await POST(req({ accion: "reabrir" }), PARAMS);
      await POST(req({ accion: "realizar" }), PARAMS);
      expect(estadoFalso.projectActas).toHaveLength(2);
      expect(estadoFalso.projectActas[0]).toEqual(primera);
    });

    it("cerrar una idea YA cerrada no toma otra foto (no hubo un cierre nuevo)", async () => {
      sembrar("2026-05-01T12:00:00.000Z");
      await POST(req({ accion: "realizar" }), PARAMS);
      expect(estadoFalso.projectActas).toHaveLength(0);
    });

    it("si la foto no se puede guardar, el cierre no ocurre y se dice (500)", async () => {
      sembrar(null);
      const fromReal = supabaseFalso.from.getMockImplementation()!;
      supabaseFalso.from.mockImplementation((nombre: string) => {
        const t = fromReal(nombre) as Record<string, unknown>;
        if (nombre === "project_actas") {
          t.insert = () => {
            t.then = (res: (v: unknown) => unknown) =>
              Promise.resolve({ data: null, error: { message: "la tabla no existe" } }).then(res);
            return t;
          };
        }
        return t as never;
      });
      const errores = vi.spyOn(console, "error").mockImplementation(() => {});
      const res = await POST(req({ accion: "realizar" }), PARAMS);
      expect(res.status).toBe(500);
      expect(estadoFalso.projects["p1"].realizada_at ?? null).toBeNull();
      errores.mockRestore();
    });
  });
});

// AUD-09 M09 (tanda 7A, datos): una acción que no cambia nada no deja historia.
// "Reabrir" una idea que no estaba cerrada (la Celebración se abría por URL sin
// cierre) escribía una reapertura falsa en la bitácora; cerrar lo ya cerrado
// dejaba otro "realizada" y podía pisar el motivo del primer cierre.
describe("sin cambio de estado no hay rastro (AUD-09 M09)", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("reabrir una idea que no está cerrada no escribe una reapertura", async () => {
    sembrar(null);
    const res = await POST(req({ accion: "reabrir" }), PARAMS);
    expect(res.status).toBe(200);
    expect(estadoFalso.bitacora.filter((e) => e.tipo === "realizada")).toHaveLength(0);
  });

  it("cerrar una idea ya cerrada no escribe otro cierre ni pisa su motivo", async () => {
    sembrar("2026-05-01T12:00:00.000Z");
    estadoFalso.projects["p1"].cierre_motivo = "el motivo del primer cierre";
    const res = await POST(req({ accion: "realizar", motivo: "otro motivo" }), PARAMS);
    expect(res.status).toBe(200);
    expect(estadoFalso.bitacora.filter((e) => e.tipo === "realizada")).toHaveLength(0);
    expect(estadoFalso.projects["p1"].cierre_motivo).toBe("el motivo del primer cierre");
  });
});

