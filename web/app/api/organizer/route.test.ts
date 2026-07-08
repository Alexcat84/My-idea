// Fase 3.0: prueba de integracion de POST /api/organizer con un cliente
// Supabase falso (imita el contrato thenable de supabase-js: cada punto
// de la cadena .from().insert()/.update()/.select().eq().limit() es
// awaitable directamente, ademas de soportar .single() como metodo
// terminal explicito) y un cliente Anthropic falso (mismo patron de
// vi.mock ya usado en el resto del port).
import { beforeEach, describe, expect, it, vi } from "vitest";

interface EstadoFalso {
  projects: Record<string, Record<string, unknown>>;
  sessions: Record<string, Record<string, unknown>>;
  plans: Record<string, unknown>[];
  contadorProject: number;
  contadorSession: number;
}

function estadoVacio(): EstadoFalso {
  return { projects: {}, sessions: {}, plans: [], contadorProject: 0, contadorSession: 0 };
}

let estadoFalso: EstadoFalso = estadoVacio();

function resolverTabla(
  nombre: string,
  b: { _insert?: Record<string, unknown>; _update?: Record<string, unknown>; _filters: Record<string, unknown>; _single: boolean }
) {
  if (nombre === "projects") {
    if (b._insert) {
      estadoFalso.contadorProject++;
      const id = `project-${estadoFalso.contadorProject}`;
      estadoFalso.projects[id] = { id, session_count: 0, ...b._insert };
      return { data: b._single ? { id } : [{ id }], error: null };
    }
    if (b._update) {
      const id = b._filters.id as string;
      if (estadoFalso.projects[id]) Object.assign(estadoFalso.projects[id], b._update);
      return { data: null, error: null };
    }
    const id = b._filters.id as string | undefined;
    const rows = id ? (estadoFalso.projects[id] ? [estadoFalso.projects[id]] : []) : Object.values(estadoFalso.projects);
    return { data: rows, error: null };
  }
  if (nombre === "sessions") {
    if (b._insert) {
      estadoFalso.contadorSession++;
      const id = `session-${estadoFalso.contadorSession}`;
      estadoFalso.sessions[id] = { id, ...b._insert };
      return { data: b._single ? { id } : [{ id }], error: null };
    }
    if (b._update) {
      const id = b._filters.id as string;
      if (estadoFalso.sessions[id]) Object.assign(estadoFalso.sessions[id], b._update);
      return { data: null, error: null };
    }
    return { data: Object.values(estadoFalso.sessions), error: null };
  }
  if (nombre === "plans" && b._insert) {
    estadoFalso.plans.push(b._insert);
    return { data: null, error: null };
  }
  return { data: null, error: null };
}

function crearTabla(nombre: string) {
  const builder = {
    _insert: undefined as Record<string, unknown> | undefined,
    _update: undefined as Record<string, unknown> | undefined,
    _filters: {} as Record<string, unknown>,
    _single: false,
    insert(payload: Record<string, unknown>) {
      this._insert = payload;
      return this;
    },
    update(payload: Record<string, unknown>) {
      this._update = payload;
      return this;
    },
    select() {
      return this;
    },
    eq(col: string, val: unknown) {
      this._filters[col] = val;
      return this;
    },
    limit() {
      return this;
    },
    async single() {
      this._single = true;
      return resolverTabla(nombre, this);
    },
    then(resolve: (v: unknown) => unknown, reject: (e: unknown) => unknown) {
      return Promise.resolve(resolverTabla(nombre, this)).then(resolve, reject);
    },
  };
  return builder;
}

const getUserFalso = vi.fn<() => Promise<{ data: { user: { id: string } | null } }>>(async () => ({
  data: { user: { id: "user-fake" } },
}));
const supabaseFalso = {
  auth: { getUser: getUserFalso },
  from: vi.fn((nombre: string) => crearTabla(nombre)),
};

const messagesCreateFalso = vi.fn();

vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => supabaseFalso),
}));
vi.mock("@/lib/anthropicClient", () => ({
  createAnthropicClient: vi.fn(() => ({ messages: { create: messagesCreateFalso } })),
}));

import { POST } from "./route";

function respuestaClaudeFalsa(json: unknown) {
  return {
    content: [{ type: "text", text: JSON.stringify(json) }],
    usage: { input_tokens: 200, output_tokens: 80, cache_read_input_tokens: 0, cache_creation_input_tokens: 0 },
  };
}

function requestFalso(payload: unknown) {
  return new Request("http://test/api/organizer", { method: "POST", body: JSON.stringify(payload) });
}

describe("POST /api/organizer", () => {
  beforeEach(() => {
    estadoFalso = estadoVacio();
    messagesCreateFalso.mockReset();
    getUserFalso.mockReset();
    getUserFalso.mockResolvedValue({ data: { user: { id: "user-fake" } } });
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
    getUserFalso.mockResolvedValueOnce({ data: { user: null } });
    const res = await POST(requestFalso({ texto: "algo" }));
    expect(res.status).toBe(401);
  });

  it("organiza la idea, persiste proyecto/sesion/plan, y actualiza la fase detectada", async () => {
    messagesCreateFalso.mockResolvedValueOnce(
      respuestaClaudeFalsa({
        idea_en_una_frase: "Una app de I Ching",
        etapa_detectada: "validacion",
        lo_que_ya_tienes_claro: ["ya tienes un producto publicado"],
        lo_que_estas_asumiendo_sin_saberlo: ["que tus amigos usaran la app"],
        areas_que_cubriria_tu_plan_completo: ["modelo de ingresos", "canal de adquisicion"],
      })
    );

    const res = await POST(requestFalso({ texto: "Tengo una app de I Ching publicada, quiero mas usuarios." }));
    expect(res.status).toBe(200);
    const body = await res.json();

    expect(body.markdown).toContain("# Organizador de tu idea");
    expect(body.markdown).toContain("Una app de I Ching");
    expect(body.markdown).toContain("modelo de ingresos");
    expect(body.data.etapa_detectada).toBe("validacion");
    expect(typeof body.project_id).toBe("string");
    expect(body.costo_usd).toBeGreaterThan(0);

    expect(Object.values(estadoFalso.projects)).toHaveLength(1);
    const proyecto = Object.values(estadoFalso.projects)[0] as Record<string, unknown>;
    expect(proyecto.fase_actual).toBe("validacion");

    expect(estadoFalso.plans).toHaveLength(1);
    expect(estadoFalso.plans[0].etiqueta).toBe("organizador");

    expect(Object.values(estadoFalso.sessions)).toHaveLength(1);
    const sesion = Object.values(estadoFalso.sessions)[0] as Record<string, unknown>;
    expect(sesion.closed_at).toBeTruthy();
    expect(sesion.tipo).toBe("gratuito");
  });

  it("502 si Claude falla, pero aun asi cierra la sesion con el costo acumulado hasta ese punto", async () => {
    messagesCreateFalso.mockRejectedValueOnce(new Error("fallo de red simulado"));
    const res = await POST(requestFalso({ texto: "otra idea distinta" }));
    expect(res.status).toBe(502);

    expect(Object.values(estadoFalso.sessions)).toHaveLength(1);
    const sesion = Object.values(estadoFalso.sessions)[0] as Record<string, unknown>;
    expect(sesion.closed_at).toBeTruthy();
    expect(estadoFalso.plans).toHaveLength(0);
  });
});
