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
  checklistItems: Record<string, unknown>[];
  contadorProject: number;
  contadorSession: number;
  contadorPlan: number;
}

export function estadoFalsoVacio(): EstadoFalso {
  return {
    projects: {},
    sessions: {},
    plans: [],
    projectNodes: [],
    checklistItems: [],
    contadorProject: 0,
    contadorSession: 0,
    contadorPlan: 0,
  };
}

interface Builder {
  _insert?: Record<string, unknown> | Record<string, unknown>[];
  _update?: Record<string, unknown>;
  _filters: Record<string, unknown>;
  _single: boolean;
  _order?: { col: string; ascending: boolean };
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
    let rows = id ? (estado.projects[id] ? [estado.projects[id]] : []) : Object.values(estado.projects);
    if (b._order) {
      const { col, ascending } = b._order;
      rows = [...rows].sort((a, c) => {
        const av = String(a[col] ?? "");
        const cv = String(c[col] ?? "");
        return ascending ? av.localeCompare(cv) : cv.localeCompare(av);
      });
    }
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
    // Fase 3.3: guardarPlan encadena .select("id").single() para devolver
    // el plan_id que el checklist derivado necesita — el fake lo imita.
    estado.contadorPlan++;
    const id = `plan-${estado.contadorPlan}`;
    estado.plans.push({ id, ...(b._insert as Record<string, unknown>) });
    return { data: b._single ? { id } : [{ id }], error: null };
  }
  if (nombre === "checklist_items") {
    if (b._insert) {
      const filas = Array.isArray(b._insert) ? b._insert : [b._insert];
      estado.checklistItems.push(...filas);
      return { data: null, error: null };
    }
    if (b._update) {
      const id = b._filters.id as string | undefined;
      const fila = estado.checklistItems.find((r) => r.id === id);
      if (!fila) return { data: null, error: { message: "no encontrado" } };
      Object.assign(fila, b._update);
      return { data: b._single ? fila : [fila], error: null };
    }
    let rows = estado.checklistItems;
    for (const [col, val] of Object.entries(b._filters)) {
      rows = rows.filter((r) => r[col] === val);
    }
    // .single() en una lectura (Fase 3.8: la ruta lee el ítem previo para
    // preservar la fecha_base al replanificar) devuelve la fila, no un array.
    if (b._single) return { data: rows[0] ?? null, error: rows[0] ? null : { message: "no encontrado" } };
    return { data: rows, error: null };
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
    order(col: string, opts?: { ascending?: boolean }) {
      builder._order = { col, ascending: opts?.ascending ?? true };
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
