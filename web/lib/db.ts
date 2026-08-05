/**
 * db.ts - Fase 3.0: port de la porcion de engine/db.py que las rutas de
 * API necesitan (proyectos, sesiones, planes). A diferencia del CLI, no
 * hay modo --offline aqui: la web SIEMPRE tiene Supabase. El cliente se
 * recibe por parametro (nunca un singleton propio) porque cada ruta debe
 * usar el cliente RLS-scoped de la request (lib/supabase/server.ts), que
 * ya sabe quien es el usuario autenticado via cookies -- las politicas
 * RLS de projects/sessions/plans (auth.uid() = user_id) hacen el resto.
 */
import type { SupabaseClient } from "@supabase/supabase-js";
import type { NumerosProyecto } from "./calculadora";
import type { UsoAcumulado } from "./costmeter";
import type { CapacidadSemanal, ModoCamino, ModoRuta, PlanEtiqueta, ProjectNodeTipo, SessionTipo } from "./dbContract";
import type { EstadoRecorrido } from "./engine/recorrido";
import type { EstadoReporte } from "./engine/reporteFlow";

export const FASES = ["ideacion", "validacion", "planificacion", "ejecucion"] as const;
export type Fase = (typeof FASES)[number];

export interface Proyecto {
  id: string;
  user_id: string;
  titulo: string | null;
  entrada_original: string;
  estado_vivo: string | null;
  fase_actual: Fase;
  session_count: number;
  status: "active" | "archived";
  tipo_oferta?: string | null;
  unidad_venta?: string | null;
  numeros_proyecto?: NumerosProyecto;
  numeros_descartados?: unknown;
  estado_reporte?: EstadoReportePersistido | null;
  /** Fase 3.8: la idea marcada como realizada (nace un "Proyecto"). */
  realizada_at?: string | null;
  /** Fase 3.8: cómo lleva el usuario su camino en Manos a la Obra. */
  modo_camino?: ModoCamino | null;
  /** Fase 4.0 §8 (acta de cierre): por qué el usuario cerró la idea aquí, en
   * sus palabras. null si cerró sin escribir nada (el campo es opcional). */
  cierre_motivo?: string | null;
  /** FASE B (canon 14, migration 027): cuándo se activó Tus Números para esta
   * idea. Ancla del cobro UNA vez por idea (ETAPA 2). null = no activado. */
  tus_numeros_activado_at?: string | null;
  created_at: string;
  updated_at: string;
}

/** Estado resumible de la mini-entrevista de POST /api/project/[id]/report
 * (projects.estado_reporte, migration 010) entre una pregunta y la
 * siguiente. numeros_proyecto ya vive en su propia columna (fuente de
 * verdad, se re-lee y se re-escribe en cada paso, igual que Python), asi
 * que aqui solo hace falta el progreso de la mini-entrevista en si mas el
 * acumulado de costo (tope propio PRESUPUESTO_REPORTE_USD). */
export interface EstadoReportePersistido {
  estado: EstadoReporte;
  acumulado: UsoAcumulado;
}

export interface RutaNodo {
  node_id: string;
  tipo: ModoRuta;
}

export interface Sesion {
  id: string;
  project_id: string;
  user_id: string;
  session_position: number;
  tipo: SessionTipo;
  mensaje_entrada: string;
  puerta_entrada: string | null;
  ruta: RutaNodo[];
  costo_usd: number;
  presupuesto_excedido: boolean;
  presupuesto_usd?: number | null;
  decisiones?: unknown[] | null;
  calidad?: Record<string, unknown> | null;
  estado_recorrido: EstadoSesionPersistido | null;
  created_at: string;
  closed_at: string | null;
}

/** Todo lo que hace falta para resumir un turno: el estado del bucle de
 * entrevista (recorrido) MAS el acumulado de costo real (uso, no solo el
 * total en dolares) -- llamarClaude necesita el desglose de tokens por
 * modelo para decidir si el presupuesto de la sesion ya se supero, asi
 * que no alcanza con persistir costo_usd. */
/** Una pareja del recorrido conversado: la pregunta que se hizo y lo que el
 * usuario respondió. */
export interface TurnoRegistrado {
  pregunta: string;
  respuesta: string;
  en: string;
}

export interface EstadoSesionPersistido {
  recorrido: EstadoRecorrido;
  acumulado: UsoAcumulado;
  /** El recorrido conversado completo. Se persiste para que el usuario lo
   * vuelva a ver al reentrar a su idea (antes solo vivía en pantalla y se
   * perdía) y para el análisis de la beta. Es texto: unos pocos KB por
   * sesión, sin riesgo de saturar. */
  turnos?: TurnoRegistrado[];
  /** La pregunta que quedó en pantalla; con la respuesta del turno siguiente
   * se arma la pareja. */
  ultimaPregunta?: string | null;
}

function ahora(): string {
  return new Date().toISOString();
}

export async function crearProyecto(supabase: SupabaseClient, userId: string, entradaOriginal: string): Promise<string> {
  const { data, error } = await supabase
    .from("projects")
    .insert({ user_id: userId, entrada_original: entradaOriginal, fase_actual: "ideacion" })
    .select("id")
    .single();
  if (error) throw error;
  return (data as { id: string }).id;
}

export async function obtenerProyecto(supabase: SupabaseClient, projectId: string): Promise<Proyecto | null> {
  const { data, error } = await supabase.from("projects").select("*").eq("id", projectId).limit(1);
  if (error) throw error;
  const filas = data as Proyecto[];
  return filas.length > 0 ? filas[0] : null;
}

/** Lista los proyectos del usuario autenticado (RLS ya filtra por
 * user_id), mas recientes primero -- reemplaza a --seguir/necesitar saber
 * el project_id de memoria: la UI muestra esta lista para retomar. */
export async function listarProyectos(supabase: SupabaseClient): Promise<Proyecto[]> {
  const { data, error } = await supabase.from("projects").select("*").order("updated_at", { ascending: false });
  if (error) throw error;
  return data as Proyecto[];
}

export async function actualizarProyecto(
  supabase: SupabaseClient,
  projectId: string,
  campos: Record<string, unknown>
): Promise<void> {
  const { error } = await supabase
    .from("projects")
    .update({ ...campos, updated_at: ahora() })
    .eq("id", projectId);
  if (error) throw error;
}

// ── "Todo separado" (T3, migration 032): el MODO del camino POR ESPACIO ───────
// Cada espacio (core y cada mundo) elige su modo ('ritmo' | 'fechas') por su
// cuenta. Vive en project_modos (project_id, dominio, modo_camino). El core
// DUAL-LEE en la transición: si no hay fila 'core', el llamador cae a
// projects.modo_camino (que 032 dejó de escribir pero conserva).

/** El mapa dominio → modo desde project_modos (vacío si el proyecto no tiene). */
export async function obtenerModosPorEspacio(
  supabase: SupabaseClient,
  projectId: string
): Promise<Record<string, "ritmo" | "fechas">> {
  const { data, error } = await supabase.from("project_modos").select("dominio, modo_camino").eq("project_id", projectId);
  if (error) throw error;
  const modos: Record<string, "ritmo" | "fechas"> = {};
  for (const f of (data ?? []) as Array<{ dominio: string; modo_camino: "ritmo" | "fechas" }>) modos[f.dominio] = f.modo_camino;
  return modos;
}

/** Scheduler F2: las horas por semana que el usuario le da a CADA espacio
 * (project_modos.capacidad_semanal, migración 033). El empaquetado las usa para
 * repartir las semanas. Un espacio sin declarar no aparece en el mapa: el ritual
 * arranca con el chip por defecto y no inventa una capacidad ajena. */
export async function obtenerCapacidadesPorEspacio(
  supabase: SupabaseClient,
  projectId: string
): Promise<Record<string, CapacidadSemanal>> {
  const { data, error } = await supabase
    .from("project_modos")
    .select("dominio, capacidad_semanal")
    .eq("project_id", projectId);
  if (error) throw error;
  const caps: Record<string, CapacidadSemanal> = {};
  for (const f of (data ?? []) as Array<{ dominio: string; capacidad_semanal: CapacidadSemanal | null }>) {
    if (f.capacidad_semanal) caps[f.dominio] = f.capacidad_semanal;
  }
  return caps;
}

/** Guarda la capacidad de un espacio. modo_camino es NOT NULL en la tabla, así
 * que el upsert lleva el modo vigente; el llamador ya lo leyó (y un espacio que
 * está declarando capacidad está, por definición, en modo fechas). */
export async function guardarCapacidadEspacio(
  supabase: SupabaseClient,
  projectId: string,
  dominio: string,
  capacidad: CapacidadSemanal,
  modoVigente: "ritmo" | "fechas" = "fechas"
): Promise<void> {
  const { error } = await supabase.from("project_modos").upsert(
    {
      project_id: projectId,
      dominio,
      modo_camino: modoVigente,
      capacidad_semanal: capacidad,
      updated_at: ahora(),
    },
    { onConflict: "project_id,dominio" }
  );
  if (error) throw error;
}

/** Upsert del modo de UN espacio (por project_id + dominio) en project_modos. */
export async function guardarModoEspacio(
  supabase: SupabaseClient,
  projectId: string,
  dominio: string,
  modo: "ritmo" | "fechas"
): Promise<void> {
  const { error } = await supabase
    .from("project_modos")
    .upsert({ project_id: projectId, dominio, modo_camino: modo, updated_at: ahora() }, { onConflict: "project_id,dominio" });
  if (error) throw error;
}

// ── FASE B (canon 14, migration 027): Tus Numeros como TABLERO VIVO ──────────

/** Una version de cifras guardada. La tabla es APPEND-ONLY: cada fila es un
 * snapshot inmutable, la historia no se reescribe (no hay UPDATE nunca). */
export interface VersionNumeros {
  id: string;
  project_id: string;
  numeros: NumerosProyecto;
  tipo_oferta: string | null;
  calculo: unknown | null;
  narracion: string | null;
  narracion_at: string | null;
  created_at: string;
}

/**
 * Activa Tus Numeros para una idea de forma IDEMPOTENTE: el ancla del cobro
 * UNA vez por idea (ETAPA 2). El WHERE atomico (`tus_numeros_activado_at IS
 * NULL`, via .is()) garantiza que dos requests simultaneos no marquen dos
 * veces: la base serializa el UPDATE, el primero setea, el segundo ya no
 * matchea y afecta 0 filas. `activadoAhora` es true solo para el que
 * realmente activo: AHI, en la ETAPA 2, ira el cobro de PRECIOS.tus_numeros,
 * una sola vez, nunca en el camino idempotente.
 */
export async function activarTusNumeros(
  supabase: SupabaseClient,
  projectId: string
): Promise<{ activadoAhora: boolean; activadoAt: string | null }> {
  const ts = ahora();
  const { data, error } = await supabase
    .from("projects")
    .update({ tus_numeros_activado_at: ts, updated_at: ts })
    .eq("id", projectId)
    .is("tus_numeros_activado_at", null)
    .select("tus_numeros_activado_at");
  if (error) throw error;
  const filas = (data ?? []) as { tus_numeros_activado_at: string }[];
  if (filas.length > 0) {
    return { activadoAhora: true, activadoAt: filas[0].tus_numeros_activado_at };
  }
  // Ya estaba activo (o no es del usuario): idempotente, sin doble marca.
  const proyecto = await obtenerProyecto(supabase, projectId);
  return { activadoAhora: false, activadoAt: proyecto?.tus_numeros_activado_at ?? null };
}

/** Inserta una version de cifras. Solo INSERT, jamas UPDATE: corregir cifras
 * o re-narrar crea una fila nueva y la anterior queda archivada con su fecha. */
export async function insertarVersionNumeros(
  supabase: SupabaseClient,
  projectId: string,
  version: {
    numeros: NumerosProyecto;
    tipoOferta?: string | null;
    calculo?: unknown;
    narracion?: string | null;
    narracionAt?: string | null;
  }
): Promise<string> {
  const { data, error } = await supabase
    .from("project_numeros_versiones")
    .insert({
      project_id: projectId,
      numeros: version.numeros,
      tipo_oferta: version.tipoOferta ?? null,
      calculo: version.calculo ?? null,
      narracion: version.narracion ?? null,
      narracion_at: version.narracionAt ?? null,
    })
    .select("id")
    .single();
  if (error) throw error;
  return (data as { id: string }).id;
}

/** La ultima version guardada (la vigente), o null si nunca se corrio. */
export async function ultimaVersionNumeros(
  supabase: SupabaseClient,
  projectId: string
): Promise<VersionNumeros | null> {
  const { data, error } = await supabase
    .from("project_numeros_versiones")
    .select("*")
    .eq("project_id", projectId)
    .order("created_at", { ascending: false })
    .limit(1);
  if (error) throw error;
  const filas = data as VersionNumeros[];
  return filas.length > 0 ? filas[0] : null;
}

/** El historial de versiones, mas recientes primero. Trae el `calculo`
 * (snapshot) para que la ruta arme el resumen de cada fila (fecha + veredicto
 * + margen) SIN recalcular nada: es la foto de ese momento, tal cual quedo. */
export async function historialVersionesNumeros(
  supabase: SupabaseClient,
  projectId: string
): Promise<Array<{ id: string; created_at: string; narracion_at: string | null; calculo: unknown | null }>> {
  const { data, error } = await supabase
    .from("project_numeros_versiones")
    .select("id, created_at, narracion_at, calculo")
    .eq("project_id", projectId)
    .order("created_at", { ascending: false });
  if (error) throw error;
  return (data ?? []) as Array<{ id: string; created_at: string; narracion_at: string | null; calculo: unknown | null }>;
}

/** Una version concreta (para VISITARLA en modo lectura). Devuelve su snapshot
 * inmutable: las cifras de entonces, el calculo de entonces, y su fecha. RLS
 * ya filtra por dueño; el project_id se exige ademas por defensa. */
export async function obtenerVersionNumeros(
  supabase: SupabaseClient,
  projectId: string,
  versionId: string
): Promise<VersionNumeros | null> {
  const { data, error } = await supabase
    .from("project_numeros_versiones")
    .select("*")
    .eq("project_id", projectId)
    .eq("id", versionId)
    .limit(1);
  if (error) throw error;
  const filas = data as VersionNumeros[];
  return filas.length > 0 ? filas[0] : null;
}

/** Cuantas re-narraciones del modelo se hicieron HOY para esta idea (freno del
 * tope diario). Cuenta filas con narracion_at desde el inicio del dia UTC. */
export async function contarNarracionesHoy(supabase: SupabaseClient, projectId: string): Promise<number> {
  const inicioDia = new Date();
  inicioDia.setUTCHours(0, 0, 0, 0);
  const { count, error } = await supabase
    .from("project_numeros_versiones")
    .select("id", { count: "exact", head: true })
    .eq("project_id", projectId)
    .gte("narracion_at", inicioDia.toISOString());
  if (error) throw error;
  return count ?? 0;
}

/** Fase 3.8 — bitácora de eventos de PROYECTO (migration 018): el mueble
 * que las sesiones no daban (sessions.decisiones es por sesión). Eventos:
 * 'modo_camino' {de, a}, 'realizada' {accion, motivo}. No falla la request si el
 * insert falla (es telemetría/memoria, no la acción principal). */
export async function registrarBitacora(
  supabase: SupabaseClient,
  projectId: string,
  tipo: string,
  payload: Record<string, unknown> = {}
): Promise<void> {
  try {
    await supabase.from("project_bitacora").insert({ project_id: projectId, tipo, payload });
  } catch {
    /* la bitácora nunca bloquea la acción del usuario */
  }
}

export async function crearSesion(
  supabase: SupabaseClient,
  userId: string,
  projectId: string,
  tipo: SessionTipo,
  mensajeEntrada: string,
  puertaEntrada: string | null = null,
  dominio: string = "core"
): Promise<string> {
  const proyecto = await obtenerProyecto(supabase, projectId);
  const posicion = (proyecto?.session_count ?? 0) + 1;
  const { data, error } = await supabase
    .from("sessions")
    .insert({
      project_id: projectId,
      user_id: userId,
      session_position: posicion,
      tipo,
      mensaje_entrada: mensajeEntrada,
      puerta_entrada: puertaEntrada,
      // 'core' es el DEFAULT de la columna (016): se omite para que las
      // sesiones normales sigan funcionando aun antes de aplicar la 016.
      ...(dominio !== "core" ? { dominio } : {}),
    })
    .select("id")
    .single();
  if (error) throw error;
  return (data as { id: string }).id;
}

export async function cerrarSesion(
  supabase: SupabaseClient,
  projectId: string,
  sessionId: string,
  rutaConModos: RutaNodo[],
  costoUsd: number,
  presupuestoExcedido: boolean,
  costoDesglose?: Record<string, number>,
  presupuestoUsd?: number,
  decisiones?: unknown[],
  calidad?: unknown
): Promise<void> {
  const campos: Record<string, unknown> = {
    ruta: rutaConModos,
    costo_usd: costoUsd,
    presupuesto_excedido: presupuestoExcedido,
    closed_at: ahora(),
  };
  if (costoDesglose && Object.keys(costoDesglose).length > 0) {
    campos.costo_desglose = costoDesglose;
  }
  // Hotfix v2.2.1: presupuesto vigente con el que esta sesion realmente
  // corrio (--reporte usa PRESUPUESTO_REPORTE_USD en vez del default de
  // sesion, asi que puede diferir entre sesiones).
  if (presupuestoUsd !== undefined) {
    campos.presupuesto_usd = presupuestoUsd;
  }
  // Fase 3.1 (caja de vidrio): bitacora completa de eventos de la sesion
  // (decision_turno por turno, fallback_auto, etc.), acumulada en
  // estado_recorrido turno a turno y persistida de una sola vez aqui.
  if (decisiones && decisiones.length > 0) {
    campos.decisiones = decisiones;
  }
  // Fase 3.1: veredicto del juez de sesion muestreado, o ausente si esta
  // sesion no se muestreo.
  if (calidad) {
    campos.calidad = calidad;
  }
  const { error } = await supabase.from("sessions").update(campos).eq("id", sessionId);
  if (error) throw error;
  const proyecto = await obtenerProyecto(supabase, projectId);
  const nuevoConteo = (proyecto?.session_count ?? 0) + 1;
  await actualizarProyecto(supabase, projectId, { session_count: nuevoConteo });
}

export async function obtenerSesion(supabase: SupabaseClient, sessionId: string): Promise<Sesion | null> {
  const { data, error } = await supabase.from("sessions").select("*").eq("id", sessionId).limit(1);
  if (error) throw error;
  const filas = data as Sesion[];
  return filas.length > 0 ? filas[0] : null;
}

/** Persiste el estado resumible del bucle de entrevista entre turnos
 * (sessions.estado_recorrido, migration 009). No cierra la sesion. */
export async function guardarEstadoSesion(
  supabase: SupabaseClient,
  sessionId: string,
  estado: EstadoSesionPersistido
): Promise<void> {
  const { error } = await supabase.from("sessions").update({ estado_recorrido: estado }).eq("id", sessionId);
  if (error) throw error;
}

/** Motor v2.1: mergea lo detectado ESTA sesion dentro de
 * projects.numeros_proyecto (solo pisa los campos que esta sesion SI
 * detecto; el resto del historial numerico del proyecto queda intacto). */
export async function mergeNumerosProyecto(
  supabase: SupabaseClient,
  projectId: string,
  numerosDetectadosSesion: Record<string, unknown> | null | undefined
): Promise<void> {
  if (!numerosDetectadosSesion || Object.keys(numerosDetectadosSesion).length === 0) return;
  const proyecto = await obtenerProyecto(supabase, projectId);
  const numeros = { ...((proyecto?.numeros_proyecto as Record<string, unknown>) ?? {}), ...numerosDetectadosSesion };
  await actualizarProyecto(supabase, projectId, { numeros_proyecto: numeros });
}

/** Motor v2.2: persiste tipo_oferta/unidad_venta si esta sesion detecto
 * algo nuevo (nunca pisa con null lo que ya estaba guardado de una
 * sesion anterior). */
export async function mergeTipoOferta(
  supabase: SupabaseClient,
  projectId: string,
  tipoOfertaSesion: string | null | undefined,
  unidadVentaSesion: string | null | undefined
): Promise<void> {
  if (!tipoOfertaSesion && !unidadVentaSesion) return;
  const campos: Record<string, unknown> = {};
  if (tipoOfertaSesion) campos.tipo_oferta = tipoOfertaSesion;
  if (unidadVentaSesion) campos.unidad_venta = unidadVentaSesion;
  await actualizarProyecto(supabase, projectId, campos);
}

export async function nodosCubiertos(supabase: SupabaseClient, projectId: string): Promise<Set<string>> {
  const { data, error } = await supabase.from("project_nodes").select("node_id").eq("project_id", projectId);
  if (error) throw error;
  return new Set((data as Array<{ node_id: string }>).map((row) => row.node_id));
}

/** Fase 3.5: los dominios que este proyecto puede recorrer — 'core'
 * siempre, más un dominio por cada fila de project_unlocks. Sin fila,
 * el dominio no existe para el motor (el filtro es el muro). */
export async function dominiosDesbloqueados(supabase: SupabaseClient, projectId: string): Promise<string[]> {
  const { data, error } = await supabase.from("project_unlocks").select("dominio").eq("project_id", projectId);
  if (error) throw error;
  return ["core", ...(data as Array<{ dominio: string }>).map((row) => row.dominio)];
}

export interface NodoConTipo {
  node_id: string;
  tipo: ProjectNodeTipo;
}

/** Port de registrar_nodos: ignora duplicados (un nodo cuenta una sola
 * vez por proyecto, sin importar en que sesion se cubrio primero). */
export async function registrarNodos(
  supabase: SupabaseClient,
  projectId: string,
  sessionId: string,
  nodosConTipo: NodoConTipo[]
): Promise<void> {
  const yaCubiertos = await nodosCubiertos(supabase, projectId);
  const nuevos = nodosConTipo.filter((n) => !yaCubiertos.has(n.node_id));
  if (nuevos.length === 0) return;
  const { error } = await supabase.from("project_nodes").insert(
    nuevos.map((n) => ({ project_id: projectId, session_id: sessionId, node_id: n.node_id, tipo: n.tipo }))
  );
  if (error) throw error;
}

/** Devuelve el id del plan insertado (Fase 3.3: el checklist derivado
 * necesita plan_id para encadenarse). */
export async function guardarPlan(
  supabase: SupabaseClient,
  userId: string,
  sessionId: string,
  etiqueta: PlanEtiqueta,
  contenidoMd: string,
  conceptosUsados: number,
  familiasCubiertas: string[],
  dominio: string = "core"
): Promise<string> {
  const { data, error } = await supabase
    .from("plans")
    .insert({
      session_id: sessionId,
      user_id: userId,
      etiqueta,
      contenido_md: contenidoMd,
      conceptos_usados: conceptosUsados,
      familias_cubiertas: familiasCubiertas,
      // igual que crearSesion: 'core' es el DEFAULT de la columna (016).
      ...(dominio !== "core" ? { dominio } : {}),
    })
    .select("id")
    .single();
  if (error) throw error;
  return data.id as string;
}

/** Fase 3.3: persiste el checklist derivado de un plan recién guardado.
 * Solo los planes de entrevista (inicial|completo|seguimiento) derivan
 * checklist; organizador y reporte_numeros NO llegan aquí. */
/** Mundos de proteccion (P2): el id del plan de NUCLEO mas reciente, que es el
 * "ciclo vigente" contra el que se enlaza. Misma consulta que el candado de
 * secuencia de world/start, en un solo sitio. null si el proyecto aun no tiene
 * plan de nucleo (entonces no hay nada que proteger). */
export async function obtenerPlanCoreVigente(supabase: SupabaseClient, projectId: string): Promise<string | null> {
  const { data: sesiones } = await supabase.from("sessions").select("id").eq("project_id", projectId);
  const ids = (sesiones ?? []).map((x: { id: string }) => x.id);
  if (ids.length === 0) return null;
  const { data } = await supabase
    .from("plans")
    .select("id")
    .in("session_id", ids)
    .eq("dominio", "core")
    .in("etiqueta", ["inicial", "completo", "seguimiento"])
    .order("created_at", { ascending: false })
    .limit(1);
  return ((data ?? [])[0] as { id: string } | undefined)?.id ?? null;
}

/** Mundos de proteccion (P1): las actividades de UN plan (el ciclo vigente del
 * nucleo). Lectura pura: la usa el armador del snapshot, que jamas escribe. Las
 * retiradas las filtra el armador, no la consulta, para que el corte de
 * "vigentes" viva en un solo sitio testeado. */
export async function obtenerItemsDePlan(
  supabase: SupabaseClient,
  projectId: string,
  planId: string
): Promise<Array<{ id: string; texto: string; etapa: number; orden: number; estado: string; fecha_base: string | null; banda: string | null }>> {
  const columnas = "id, texto, etapa, orden, estado, fecha_base, banda";
  const leer = (cols: string) =>
    supabase.from("checklist_items").select(cols).eq("project_id", projectId).eq("plan_id", planId);
  let { data, error } = await leer(columnas);
  // Resiliencia de columnas (patron del GET del checklist): si 'banda' aun no
  // existiera, el snapshot se arma sin ella en vez de caerse entero.
  if (error) ({ data, error } = await leer(columnas.replace(", banda", "")));
  if (error) throw error;
  return (data ?? []) as unknown as Array<{
    id: string; texto: string; etapa: number; orden: number; estado: string; fecha_base: string | null; banda: string | null;
  }>;
}

export async function insertarChecklist(
  supabase: SupabaseClient,
  projectId: string,
  planId: string,
  items: Array<{
    etapa: number;
    orden: number;
    texto: string;
    destacado: boolean;
    // Scheduler F1: la banda de esfuerzo estimada (mayoría-de-3) al nacer el
    // plan. Ausente/null = estimación fallida o plan sin scheduler (fallback).
    banda?: string | null;
    espera_externa?: boolean | null;
    // Mundos de proteccion (P2): el enlace con la actividad del nucleo que esta
    // respuesta protege, su deteccion y su severidad en palabras. Ausente en
    // todo lo que no sea un plan de proteccion.
    protege_item?: string | null;
    deteccion?: string | null;
    probabilidad?: string | null;
    dolor?: string | null;
    camino?: string | null;
  }>,
  dominio: string = "core"
): Promise<void> {
  if (items.length === 0) return;
  const { error } = await supabase.from("checklist_items").insert(
    items.map((i) => ({
      project_id: projectId,
      plan_id: planId,
      dominio,
      etapa: i.etapa,
      orden: i.orden,
      texto: i.texto,
      destacado: i.destacado,
      banda: i.banda ?? null,
      espera_externa: i.espera_externa ?? null,
      // Solo viajan si el plan es de proteccion: en los demas ni siquiera se
      // nombran, para no escribir cuatro nulls por item en cada plan de la casa.
      ...(i.protege_item !== undefined || i.deteccion !== undefined
        ? {
            protege_item: i.protege_item ?? null,
            deteccion: i.deteccion ?? null,
            probabilidad: i.probabilidad ?? null,
            dolor: i.dolor ?? null,
            camino: i.camino ?? null,
          }
        : {}),
    }))
  );
  if (error) throw error;
}
