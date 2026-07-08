// Fase 3.0: cliente Supabase falso compartido entre pruebas de rutas de
// API. Imita el contrato thenable de supabase-js -- cada punto de la
// cadena .from().insert()/.update()/.select().eq().limit() es awaitable
// directamente, ademas de soportar .single() como metodo terminal
// explicito -- sin depender de una base de datos real. No es un archivo
// *.test.ts: vitest no lo recoge como su propia suite, solo como helper.
import { vi } from "vitest";

export interface EstadoFalso {
  projects: Record<string, Record<string, unknown>>;
  sessions: Record<string, Record<string, unknown>>;
  plans: Record<string, unknown>[];
  projectNodes: Record<string, unknown>[];
  contadorProject: number;
  contadorSession: number;
}

export function estadoFalsoVacio(): EstadoFalso {
  return { projects: {}, sessions: {}, plans: [], projectNodes: [], contadorProject: 0, contadorSession: 0 };
}

interface Builder {
  _insert?: Record<string, unknown> | Record<string, unknown>[];
  _update?: Record<string, unknown>;
  _filters: Record<string, unknown>;
  _single: boolean;
}

function resolverTabla(nombre: string, estado: EstadoFalso, b: Builder) {
  if (nombre === "projects") {
    if (b._insert) {
      estado.contadorProject++;
      const id = `project-${estado.contadorProject}`;
      estado.projects[id] = { id, session_count: 0, ...b._insert };
      return { data: b._single ? { id } : [{ id }], error: null };
    }
    if (b._update) {
      const id = b._filters.id as string;
      if (estado.projects[id]) Object.assign(estado.projects[id], b._update);
      return { data: null, error: null };
    }
    const id = b._filters.id as string | undefined;
    const rows = id ? (estado.projects[id] ? [estado.projects[id]] : []) : Object.values(estado.projects);
    return { data: rows, error: null };
  }
  if (nombre === "sessions") {
    if (b._insert) {
      estado.contadorSession++;
      const id = `session-${estado.contadorSession}`;
      estado.sessions[id] = { id, ruta: [], costo_usd: 0, presupuesto_excedido: false, closed_at: null, estado_recorrido: null, ...b._insert };
      return { data: b._single ? { id } : [{ id }], error: null };
    }
    if (b._update) {
      const id = b._filters.id as string;
      if (estado.sessions[id]) Object.assign(estado.sessions[id], b._update);
      return { data: null, error: null };
    }
    const id = b._filters.id as string | undefined;
    const rows = id ? (estado.sessions[id] ? [estado.sessions[id]] : []) : Object.values(estado.sessions);
    return { data: rows, error: null };
  }
  if (nombre === "plans" && b._insert) {
    estado.plans.push(b._insert as Record<string, unknown>);
    return { data: null, error: null };
  }
  if (nombre === "project_nodes") {
    if (b._insert) {
      const filas = Array.isArray(b._insert) ? b._insert : [b._insert];
      estado.projectNodes.push(...filas);
      return { data: null, error: null };
    }
    const projectId = b._filters.project_id as string | undefined;
    const rows = projectId ? estado.projectNodes.filter((r) => r.project_id === projectId) : estado.projectNodes;
    return { data: rows.map((r) => ({ node_id: r.node_id })), error: null };
  }
  return { data: null, error: null };
}

function crearTabla(nombre: string, estado: EstadoFalso) {
  const builder: Builder & Record<string, unknown> = {
    _filters: {},
    _single: false,
    insert(payload: Record<string, unknown> | Record<string, unknown>[]) {
      builder._insert = payload;
      return builder;
    },
    update(payload: Record<string, unknown>) {
      builder._update = payload;
      return builder;
    },
    select() {
      return builder;
    },
    eq(col: string, val: unknown) {
      builder._filters[col] = val;
      return builder;
    },
    limit() {
      return builder;
    },
    async single() {
      builder._single = true;
      return resolverTabla(nombre, estado, builder);
    },
    then(resolve: (v: unknown) => unknown, reject: (e: unknown) => unknown) {
      return Promise.resolve(resolverTabla(nombre, estado, builder)).then(resolve, reject);
    },
  };
  return builder;
}

export function crearSupabaseFalso(estado: EstadoFalso, userId: string | null = "user-fake") {
  const getUser = vi.fn<() => Promise<{ data: { user: { id: string } | null } }>>(async () => ({
    data: { user: userId ? { id: userId } : null },
  }));
  return {
    auth: { getUser },
    from: vi.fn((nombre: string) => crearTabla(nombre, estado)),
  };
}
