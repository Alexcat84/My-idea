// POST /api/project/[id]/world/[pack]/diagnostico: el diagnóstico gratis del
// PREVIEW de un mundo. Primeras pruebas de esta ruta (AUD-09).
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
vi.mock("@/lib/anthropicClient", () => ({
  createAnthropicClient: vi.fn(() => ({ messages: { create: vi.fn() } })),
}));
const redactarDiagnostico = vi.fn(async (_c: unknown, _m: unknown, acumulado: unknown) => ({
  resumen: "Tu diagnóstico.",
  acumulado,
}));
vi.mock("@/lib/engine/diagnosticoMundo", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/engine/diagnosticoMundo")>()),
  redactarDiagnostico: (...a: unknown[]) => redactarDiagnostico(...(a as [unknown, unknown, unknown])),
}));

import { POST } from "./route";

const acumulado = { uso: {}, uso_por_componente: {}, presupuesto_excedido: false };

function recorrido(esSeguimiento: boolean) {
  return {
    fase: "listo_para_plan",
    ruta: [],
    modos: [],
    preguntaPendiente: null,
    dominioSesion: "quality",
    esSeguimiento,
  };
}

function pedir(sessionId: string) {
  return POST(
    new Request("http://test/api/project/p1/world/quality/diagnostico", {
      method: "POST",
      body: JSON.stringify({ session_id: sessionId }),
    }),
    { params: Promise.resolve({ id: "p1", pack: "quality" }) }
  );
}

describe("POST world/[pack]/diagnostico", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    redactarDiagnostico.mockClear();
    estadoFalso.projects["p1"] = { id: "p1", estado_vivo: null };
    estadoFalso.projectUnlocks.push({
      project_id: "p1",
      dominio: "quality",
      preview_session_id: "s-preview",
      resumen_md: "El diagnóstico del preview.",
      resumen_at: "2026-09-01T00:00:00Z",
    });
  });

  // AUD-09 H01, agravante del mundo: al recargar a mitad de un seguimiento de
  // mundo, la pantalla ofrecía "Ver mi diagnóstico" y esta ruta, que solo
  // miraba el dominio, convertía el ciclo en un diagnóstico nuevo y pisaba el
  // resumen y la sesión del preview.
  it("rechaza una sesión de SEGUIMIENTO y no toca el diagnóstico del preview", async () => {
    estadoFalso.sessions["s-ciclo"] = {
      id: "s-ciclo",
      project_id: "p1",
      dominio: "quality",
      closed_at: null,
      estado_recorrido: { recorrido: recorrido(true), acumulado },
    };
    const res = await pedir("s-ciclo");
    expect(res.status).toBe(409);
    expect(redactarDiagnostico).not.toHaveBeenCalled();
    expect(estadoFalso.projectUnlocks[0].resumen_md).toBe("El diagnóstico del preview.");
    expect(estadoFalso.projectUnlocks[0].preview_session_id).toBe("s-preview");
  });

  it("con la sesión del preview, redacta y guarda el diagnóstico", async () => {
    estadoFalso.sessions["s-preview"] = {
      id: "s-preview",
      project_id: "p1",
      dominio: "quality",
      closed_at: null,
      estado_recorrido: { recorrido: recorrido(false), acumulado },
    };
    const res = await pedir("s-preview");
    expect(res.status).toBe(200);
    expect(estadoFalso.projectUnlocks[0].resumen_md).toBe("Tu diagnóstico.");
  });
});
