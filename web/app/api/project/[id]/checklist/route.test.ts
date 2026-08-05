// Fase 3.8 §2/§4 — pruebas del PATCH del checklist ampliado con el sentido
// del tiempo: completed_at (timeline real, para TODOS) y fecha_base
// (replanificación que NO reescribe la historia).
import { readFileSync } from "node:fs";
import path from "node:path";
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

  // Regla del fundador (ago 2026): la bitácora registra CAMBIOS REALES, no clics.
  // Un PATCH que repite el mismo valor NO deja rastro.
  it("repetir el MISMO estado no registra item_estado (clic sin cambio real)", async () => {
    sembrarItem({ estado: "empezado" });
    const antes = estadoFalso.bitacora.length;
    await PATCH(req({ item_id: "it1", estado: "empezado" }), PARAMS);
    expect(estadoFalso.bitacora.length).toBe(antes);
  });

  it("repetir la MISMA nota no registra nota_escrita otra vez", async () => {
    sembrarItem();
    await PATCH(req({ item_id: "it1", nota: "recordar algo" }), PARAMS); // 1.ª vez: sí registra
    const antes = estadoFalso.bitacora.length;
    await PATCH(req({ item_id: "it1", nota: "recordar algo" }), PARAMS); // misma nota
    expect(estadoFalso.bitacora.length).toBe(antes);
  });

  it("guardar una nota VACÍA sobre algo sin nota no registra nada", async () => {
    sembrarItem();
    const antes = estadoFalso.bitacora.length;
    await PATCH(req({ item_id: "it1", nota: "" }), PARAMS);
    expect(estadoFalso.bitacora.length).toBe(antes);
  });
});

// Scheduler F1 — la corrección de la banda por el usuario. Es telemetría de oro
// para el multiplicador por banda de F4: dónde se equivoca el modelo y hacia
// dónde. Por eso el evento guarda {de, a} y solo se registra si CAMBIÓ de veras.
describe("PATCH banda (Scheduler F1): corrección del usuario", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("corrige la banda y la persiste en el ítem", async () => {
    sembrarItem({ banda: "M" });
    const res = await PATCH(req({ item_id: "it1", banda: "L" }), PARAMS);
    expect(res.status).toBe(200);
    expect(estadoFalso.checklistItems[0].banda).toBe("L");
  });

  it("registra banda_corregida {de, a} con el dominio del ítem", async () => {
    sembrarItem({ banda: "M" });
    await PATCH(req({ item_id: "it1", banda: "XL" }), PARAMS);
    const evento = estadoFalso.bitacora.find((b) => b.tipo === "banda_corregida");
    expect(evento).toBeDefined();
    expect(evento!.payload).toMatchObject({ item: "it1", dominio: "core", de: "M", a: "XL" });
  });

  it("corregir un ítem SIN banda previa registra de: null (el modelo no estimó)", async () => {
    sembrarItem({ banda: null });
    await PATCH(req({ item_id: "it1", banda: "S" }), PARAMS);
    const evento = estadoFalso.bitacora.find((b) => b.tipo === "banda_corregida");
    expect(evento!.payload).toMatchObject({ de: null, a: "S" });
  });

  it("re-elegir la MISMA banda no registra nada (clic sin cambio real)", async () => {
    sembrarItem({ banda: "M" });
    const antes = estadoFalso.bitacora.length;
    await PATCH(req({ item_id: "it1", banda: "M" }), PARAMS);
    expect(estadoFalso.bitacora.length).toBe(antes);
  });

  it("una banda inválida se rechaza con 400 y no toca el ítem", async () => {
    sembrarItem({ banda: "M" });
    const res = await PATCH(req({ item_id: "it1", banda: "XXL" }), PARAMS);
    expect(res.status).toBe(400);
    expect(estadoFalso.checklistItems[0].banda).toBe("M");
  });
});

// Mundos de protección (P2): el ENLACE es estructura del plan, no percepción del
// usuario. Nace con el plan y NO se corrige por PATCH, exactamente como
// espera_externa. El usuario corrige su banda; de qué protege su tarea, no.
describe("PATCH y el enlace de protección: protege_item NO es editable", () => {
  beforeEach(() => {
    estadoFalso = estadoFalsoVacio();
    supabaseFalso = crearSupabaseFalso(estadoFalso);
  });

  it("un PATCH que solo manda protege_item no actualiza nada (400)", async () => {
    sembrarItem({ protege_item: "nuc-a" });
    const res = await PATCH(req({ item_id: "it1", protege_item: "otro-item" }), PARAMS);
    expect(res.status).toBe(400);
    expect(estadoFalso.checklistItems[0].protege_item).toBe("nuc-a");
  });

  it("colado junto a un cambio válido, el enlace tampoco se mueve", async () => {
    sembrarItem({ protege_item: "nuc-a", deteccion: "depende de un solo proveedor" });
    const res = await PATCH(req({ item_id: "it1", estado: "hecho", protege_item: "otro-item" }), PARAMS);
    expect(res.status).toBe(200);
    expect(estadoFalso.checklistItems[0].estado).toBe("hecho"); // lo válido sí se aplicó
    expect(estadoFalso.checklistItems[0].protege_item).toBe("nuc-a"); // el enlace, intacto
  });

  it("el CAMINO tampoco se edita: nace del enlazador, como sus hermanos", async () => {
    sembrarItem({ camino: "mitigar" });
    const res = await PATCH(req({ item_id: "it1", estado: "empezado", camino: "aceptar" }), PARAMS);
    expect(res.status).toBe(200);
    expect(estadoFalso.checklistItems[0].camino).toBe("mitigar");
  });

  it("la detección y la severidad tampoco se editan desde el PATCH", async () => {
    sembrarItem({ deteccion: "depende de un solo proveedor", probabilidad: "probable", dolor: "mucho" });
    await PATCH(
      req({ item_id: "it1", estado: "empezado", deteccion: "otra cosa", probabilidad: "poco_probable", dolor: "poco" }),
      PARAMS
    );
    const item = estadoFalso.checklistItems[0];
    expect(item.deteccion).toBe("depende de un solo proveedor");
    expect(item.probabilidad).toBe("probable");
    expect(item.dolor).toBe("mucho");
  });

  it("el fuente del PATCH no nombra esas columnas (la puerta está cerrada, no vigilada)", () => {
    const fuente = readFileSync(path.join(__dirname, "route.ts"), "utf-8");
    expect(fuente).not.toContain("cambios.protege_item");
    expect(fuente).not.toContain("cambios.deteccion");
  });
});
