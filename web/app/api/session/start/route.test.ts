// Fase 3.0: prueba de integracion de POST /api/session/start. clasificar.ts
// y recorrido.ts ya tienen su propia cobertura (clasificar via
// interprete.test.ts's misma familia de fixtures, recorrido.test.ts en
// detalle) -- esta prueba mockea ambos y se enfoca en la orquestacion de
// la ruta: validacion, autenticacion, creacion de proyecto/sesion, y que
// la respuesta y el cierre de sesion dependan correctamente del
// resultado.tipo devuelto por avanzarTurno.
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

const clasificarEntradaFalso = vi.fn();
vi.mock("@/lib/engine/clasificar", () => ({
  clasificarEntrada: (...args: unknown[]) => clasificarEntradaFalso(...args),
}));

const avanzarTurnoFalso = vi.fn();
vi.mock("@/lib/engine/recorrido", () => ({
  avanzarTurno: (...args: unknown[]) => avanzarTurnoFalso(...args),
  estadoInicial: (p: { actualId: string; perfilSesion: string; textoOriginal: string }) => ({
    ruta: [p.actualId],
    modos: ["conversado"],
    perfilSesion: p.perfilSesion,
    textoOriginal: p.textoOriginal,
    profundizarOfrecido: false,
    esSeguimiento: false,
    estadoVivoPrevio: null,
    fallbackEvents: [],
    prioridadDeclarada: null,
    preguntaPendiente: null,
    ultimasPreguntas: [],
    repreguntasUsadas: 0,
    historialMensajes: [],
    numerosDetectadosSesion: {},
    tipoOfertaSesion: null,
    unidadVentaSesion: null,
    fase: "esperando_respuesta",
    sigamosDirigido: null,
  }),
}));

import { POST } from "./route";

const acumuladoFalso = { uso: {}, uso_por_componente: {}, presupuesto_excedido: false };

function requestFalso(payload: unknown) {
  return new Request("http://test/api/session/start", { method: "POST", body: JSON.stringify(payload) });
}

describe("POST /api/session/start", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    clasificarEntradaFalso.mockReset();
    avanzarTurnoFalso.mockReset();
    clasificarEntradaFalso.mockResolvedValue({
      puertaId: "design_thinking_fundamentos",
      perfilSesion: "perfil inicial",
      acumulado: acumuladoFalso,
    });
  });

  it("rechaza sin 'texto'", async () => {
    const res = await POST(requestFalso({}));
    expect(res.status).toBe(400);
  });

  it("rechaza texto que supera el maximo de 4000 caracteres", async () => {
    const res = await POST(requestFalso({ texto: "a".repeat(4001) }));
    expect(res.status).toBe(400);
  });

  it("401 si no hay usuario autenticado", async () => {
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    const res = await POST(requestFalso({ texto: "mi idea" }));
    expect(res.status).toBe(401);
  });

  it("clasifica, crea proyecto+sesion, y devuelve la primera pregunta", async () => {
    avanzarTurnoFalso.mockResolvedValueOnce({
      tipo: "pregunta",
      estado: { fase: "esperando_respuesta", ruta: ["design_thinking_fundamentos", "mapeo_capas_diseno"] },
      pregunta: "¿que capas has mapeado?",
      acumulado: acumuladoFalso,
      nodosNuevos: [{ id: "mapeo_capas_diseno", titulo: "Mapeo de capas", modo: "conversado" }],
    });

    const res = await POST(requestFalso({ texto: "quiero vender macetas de cemento" }));
    expect(res.status).toBe(200);
    const body = await res.json();
    expect(body.tipo).toBe("pregunta");
    expect(body.pregunta).toBe("¿que capas has mapeado?");
    expect(typeof body.project_id).toBe("string");
    expect(typeof body.session_id).toBe("string");

    expect(Object.values(estadoFalso.projects)).toHaveLength(1);
    expect(Object.values(estadoFalso.sessions)).toHaveLength(1);
    const sesion = Object.values(estadoFalso.sessions)[0] as Record<string, unknown>;
    expect(sesion.tipo).toBe("inicial");
    expect(sesion.closed_at).toBeNull();
    expect(sesion.estado_recorrido).toBeTruthy();

    expect(clasificarEntradaFalso).toHaveBeenCalledTimes(1);
    expect(avanzarTurnoFalso).toHaveBeenCalledTimes(1);
  });

  it("tipo=salio cierra la sesion y mergea numeros_proyecto/tipo_oferta detectados", async () => {
    avanzarTurnoFalso.mockResolvedValueOnce({
      tipo: "salio",
      estado: {
        fase: "cerrada",
        ruta: ["design_thinking_fundamentos"],
        numerosDetectadosSesion: { precio_tentativo: { valor: 13, unidad: "pack", texto_original: "13 dolares" } },
        tipoOfertaSesion: "digital",
        unidadVentaSesion: "pack",
      },
      acumulado: acumuladoFalso,
    });

    const res = await POST(requestFalso({ texto: "vendo un pack digital" }));
    expect(res.status).toBe(200);
    const body = await res.json();
    expect(body.tipo).toBe("salio");

    const sesion = Object.values(estadoFalso.sessions)[0] as Record<string, unknown>;
    expect(sesion.closed_at).toBeTruthy();
    expect(sesion.ruta).toEqual([]);

    const proyecto = Object.values(estadoFalso.projects)[0] as Record<string, unknown>;
    expect(proyecto.tipo_oferta).toBe("digital");
    expect(proyecto.unidad_venta).toBe("pack");
    expect((proyecto.numeros_proyecto as Record<string, unknown>).precio_tentativo).toBeTruthy();
  });

  it("tipo=error_temporal responde 502 sin cerrar la sesion", async () => {
    avanzarTurnoFalso.mockResolvedValueOnce({
      tipo: "error_temporal",
      estado: { fase: "esperando_respuesta", ruta: ["design_thinking_fundamentos"] },
      acumulado: acumuladoFalso,
      opciones: [{ id: "mapeo_capas_diseno", titulo: "Mapeo de capas" }],
    });

    const res = await POST(requestFalso({ texto: "algo" }));
    expect(res.status).toBe(502);
    const sesion = Object.values(estadoFalso.sessions)[0] as Record<string, unknown>;
    expect(sesion.closed_at).toBeNull();
  });
});
