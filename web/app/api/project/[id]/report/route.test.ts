// Fase 3.0: prueba de integracion de POST /api/project/[id]/report.
// reporteFlow.ts ya tiene su propia cobertura detallada (incluida la
// paridad con test_reporte_tipo_oferta.py) -- esta prueba mockea
// iniciarReporte/avanzarReporte y se enfoca en la orquestacion de la
// ruta: validacion, autenticacion, los 409 de estado_reporte
// presente/ausente, persistencia de numeros_proyecto/tipo_oferta paso a
// paso, y el cierre de sesion+plan cuando el reporte queda listo.
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

const iniciarReporteFalso = vi.fn();
const avanzarReporteFalso = vi.fn();
vi.mock("@/lib/engine/reporteFlow", () => ({
  iniciarReporte: (...args: unknown[]) => iniciarReporteFalso(...args),
  avanzarReporte: (...args: unknown[]) => avanzarReporteFalso(...args),
}));

import { POST } from "./route";

const acumuladoFalso = { uso: {}, uso_por_componente: {}, presupuesto_excedido: false };

function ctxFalso(id: string) {
  return { params: Promise.resolve({ id }) };
}

function requestFalso(payload?: unknown) {
  return new Request("http://test/api/project/p1/report", {
    method: "POST",
    body: payload === undefined ? undefined : JSON.stringify(payload),
  });
}

describe("POST /api/project/[id]/report", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
    iniciarReporteFalso.mockReset();
    avanzarReporteFalso.mockReset();
  });

  it("401 si no hay usuario autenticado", async () => {
    supabaseFalso.auth.getUser.mockResolvedValueOnce({ data: { user: null } });
    const res = await POST(requestFalso(), ctxFalso("p1"));
    expect(res.status).toBe(401);
  });

  it("404 si el proyecto no existe", async () => {
    const res = await POST(requestFalso(), ctxFalso("no-existe"));
    expect(res.status).toBe(404);
  });

  it("400 si 'respuesta' viene vacia", async () => {
    estadoFalso.projects["p1"] = { id: "p1", numeros_proyecto: {}, estado_reporte: null };
    const res = await POST(requestFalso({ respuesta: "" }), ctxFalso("p1"));
    expect(res.status).toBe(400);
  });

  it("400 si 'respuesta' supera el maximo de caracteres", async () => {
    estadoFalso.projects["p1"] = { id: "p1", numeros_proyecto: {}, estado_reporte: null };
    const res = await POST(requestFalso({ respuesta: "a".repeat(4001) }), ctxFalso("p1"));
    expect(res.status).toBe(400);
  });

  it("409 si ya hay una entrevista en curso y se llama sin 'respuesta' (iniciar de nuevo)", async () => {
    estadoFalso.projects["p1"] = {
      id: "p1",
      numeros_proyecto: {},
      estado_reporte: { estado: { fase: "preguntando" }, acumulado: acumuladoFalso },
    };
    const res = await POST(requestFalso(), ctxFalso("p1"));
    expect(res.status).toBe(409);
    expect(iniciarReporteFalso).not.toHaveBeenCalled();
  });

  it("409 si se manda 'respuesta' sin una entrevista en curso", async () => {
    estadoFalso.projects["p1"] = { id: "p1", numeros_proyecto: {}, estado_reporte: null };
    const res = await POST(requestFalso({ respuesta: "algo" }), ctxFalso("p1"));
    expect(res.status).toBe(409);
    expect(avanzarReporteFalso).not.toHaveBeenCalled();
  });

  it("inicia la entrevista, persiste el estado_reporte, y devuelve la pregunta", async () => {
    estadoFalso.projects["p1"] = { id: "p1", numeros_proyecto: {}, tipo_oferta: "producto_fisico", unidad_venta: "pieza", estado_reporte: null };
    iniciarReporteFalso.mockResolvedValueOnce({
      tipo: "pregunta",
      estado: { fase: "preguntando", idx: 0 },
      pregunta: "¿Cuánto gastas en materiales por pieza?",
      acumulado: acumuladoFalso,
      numeros: {},
      tipoOfertaActualizado: null,
    });

    const res = await POST(requestFalso(), ctxFalso("p1"));
    expect(res.status).toBe(200);
    const body = await res.json();
    expect(body.tipo).toBe("pregunta");
    expect(body.pregunta).toContain("materiales");

    const proyecto = estadoFalso.projects["p1"] as Record<string, unknown>;
    expect(proyecto.estado_reporte).toBeTruthy();
  });

  it("continua la entrevista con 'respuesta', persistiendo numeros y tipo_oferta actualizados", async () => {
    estadoFalso.projects["p1"] = {
      id: "p1",
      numeros_proyecto: {},
      tipo_oferta: "producto_fisico",
      unidad_venta: "pieza",
      estado_reporte: { estado: { fase: "reclasificando_molde" }, acumulado: acumuladoFalso },
    };
    avanzarReporteFalso.mockResolvedValueOnce({
      tipo: "pregunta",
      estado: { fase: "preguntando", idx: 0 },
      pregunta: "¿Cuánto gastas al mes en costos fijos?",
      acumulado: acumuladoFalso,
      numeros: { costos_fijos_mensuales: { valor: 200, unidad: "por mes" } },
      tipoOfertaActualizado: { tipoOferta: "digital", unidadVenta: "suscripcion" },
    });

    const res = await POST(requestFalso({ respuesta: "es una app de suscripciones" }), ctxFalso("p1"));
    expect(res.status).toBe(200);

    const proyecto = estadoFalso.projects["p1"] as Record<string, unknown>;
    expect(proyecto.tipo_oferta).toBe("digital");
    expect(proyecto.unidad_venta).toBe("suscripcion");
    expect((proyecto.numeros_proyecto as Record<string, unknown>).costos_fijos_mensuales).toBeTruthy();
  });

  it("tipo=reporte_listo limpia estado_reporte, guarda el plan, y cierra una sesion tipo 'reporte'", async () => {
    estadoFalso.projects["p1"] = {
      id: "p1",
      numeros_proyecto: {},
      tipo_oferta: "producto_fisico",
      unidad_venta: "pieza",
      estado_reporte: { estado: { fase: "preguntando" }, acumulado: acumuladoFalso },
    };
    avanzarReporteFalso.mockResolvedValueOnce({
      tipo: "reporte_listo",
      contenido: "## Tus números hoy\n\nnecesitas vender 16 packs al mes",
      acumulado: acumuladoFalso,
      numeros: { precio_tentativo: { valor: 13, unidad: "por pack" } },
      tipoOfertaActualizado: null,
    });

    const res = await POST(requestFalso({ respuesta: "13" }), ctxFalso("p1"));
    expect(res.status).toBe(200);
    const body = await res.json();
    expect(body.tipo).toBe("reporte");
    expect(body.contenido).toContain("16 packs");

    const proyecto = estadoFalso.projects["p1"] as Record<string, unknown>;
    expect(proyecto.estado_reporte).toBeNull();

    expect(estadoFalso.plans).toHaveLength(1);
    expect(estadoFalso.plans[0].etiqueta).toBe("reporte_numeros");

    const sesiones = Object.values(estadoFalso.sessions) as Record<string, unknown>[];
    expect(sesiones).toHaveLength(1);
    expect(sesiones[0].tipo).toBe("reporte");
    expect(sesiones[0].closed_at).toBeTruthy();
  });
});
