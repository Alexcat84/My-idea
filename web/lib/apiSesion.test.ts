// AUD-09 H04 (decisión del fundador, 25 sep 2026: NADA SE BORRA JAMÁS): el
// cierre honesto de un mundo borraba su fila de project_unlocks. En el
// seguimiento de un mundo ya pagado eso se llevaba el sello de compra, el
// cierre y el diagnóstico, y el texto decía "puedes volver a entrar".
import { describe, expect, it, vi } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio } from "./testUtils/fakeSupabase";
import { responderResultadoTurno } from "./apiSesion";
import { usoVacio } from "./costmeter";
import type { ResultadoTurno } from "./engine/recorrido";
import type { SupabaseClient } from "@supabase/supabase-js";

const resolverReserva = vi.fn(async () => undefined);
vi.mock("./creditos", async (importOriginal) => ({
  ...(await importOriginal<typeof import("./creditos")>()),
  resolverReserva: (...a: unknown[]) => resolverReserva(...(a as [])),
}));

function escenario(esSeguimiento: boolean) {
  const estado = estadoFalsoVacio();
  estado.projects["p1"] = { id: "p1", session_count: 2 };
  estado.sessions["s1"] = { id: "s1", project_id: "p1", closed_at: null };
  estado.projectUnlocks.push({
    project_id: "p1",
    dominio: "quality",
    plan_pagado_at: "2026-09-01T00:00:00Z",
    resumen_md: "El diagnóstico.",
    completado_at: null,
    cierre_motivo: "un motivo anterior",
  });
  const resultado = {
    tipo: "salio",
    estado: {
      esSeguimiento,
      fallbackEvents: [],
      numerosDetectadosSesion: {},
      tipoOfertaSesion: null,
      unidadVentaSesion: null,
    },
    acumulado: usoVacio(),
    cierreMundo: { dominio: "quality", motivo: "no quedan puertas" },
  } as unknown as ResultadoTurno;
  return { estado, supabase: crearSupabaseFalso(estado) as unknown as SupabaseClient, resultado };
}

describe("el cierre honesto de un mundo no borra nada", () => {
  it("en el seguimiento de un mundo pagado, la fila del mundo queda intacta", async () => {
    const { estado, supabase, resultado } = escenario(true);
    const res = await responderResultadoTurno(supabase, "p1", "s1", resultado, usoVacio());
    expect(estado.projectUnlocks).toHaveLength(1);
    expect(estado.projectUnlocks[0].plan_pagado_at).toBe("2026-09-01T00:00:00Z");
    expect(estado.projectUnlocks[0].resumen_md).toBe("El diagnóstico.");
    expect(estado.projectUnlocks[0].cierre_motivo).toBe("un motivo anterior");
    const cuerpo = await res.json();
    expect(cuerpo.unlock_revertido).toBe(false);
    // el texto no dice que el mundo "no es para esta idea" ni que hay que volver a entrar
    expect(cuerpo.cierre.titulo).not.toMatch(/no es para esta idea/);
    expect(cuerpo.cierre.cuerpo).toMatch(/siguen intactos/);
  });

  it("en el preview, la fila tampoco se borra (volver a entrar ya lo permite la ruta de arranque)", async () => {
    const { estado, supabase, resultado } = escenario(false);
    await responderResultadoTurno(supabase, "p1", "s1", resultado, usoVacio());
    expect(estado.projectUnlocks).toHaveLength(1);
    expect(estado.bitacora.some((e) => e.tipo === "mundo_incompatible")).toBe(true);
  });
});

// AUD-09 M25: una sesión que termina sin plan (el cierre honesto) no se va a
// cobrar: lo que apartó al empezar se suelta en el acto, sin esperar el
// vencimiento de la reserva.
describe("el cierre honesto suelta la reserva de la sesión (AUD-09 M25)", () => {
  it("libera plan:{sessionId}", async () => {
    resolverReserva.mockClear();
    const { supabase, resultado } = escenario(false);
    await responderResultadoTurno(supabase, "p1", "s1", resultado, usoVacio());
    expect(resolverReserva).toHaveBeenCalledWith("plan:s1", "liberada");
  });
});
