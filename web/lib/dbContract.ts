/**
 * dbContract.ts - Hotfix v2.2.2: unica fuente de verdad para los valores
 * literales que el codigo puede emitir hacia columnas con CHECK
 * constraints en Supabase (sessions.tipo, plans.etiqueta,
 * project_nodes.tipo). db.ts y recorrido.ts importan estos arrays en vez
 * de duplicar la lista de literales -- dbContract.test.ts parsea
 * supabase/migrations/*.sql y falla si alguno de estos arrays llega a
 * declarar un valor que ninguna migracion le permitio aceptar a la base
 * de datos: la misma familia de bug que las migraciones 004, 005 y 012
 * arreglaron, cada vez encontrada tarde, en produccion, en vivo.
 */

export const SESSIONS_TIPO = ["gratuito", "inicial", "seguimiento", "reporte"] as const;
export type SessionTipo = (typeof SESSIONS_TIPO)[number];

export const PLANS_ETIQUETA = ["organizador", "inicial", "completo", "seguimiento", "reporte_numeros"] as const;
export type PlanEtiqueta = (typeof PLANS_ETIQUETA)[number];

/** project_nodes.tipo: cobertura del nodo. 'salto' (migration 012) es un
 * subtipo documentado de 'conversado' -- llegada por salto semantico con
 * pregunta hecha en el destino -- que ambos motores (Python y web)
 * escriben identico; no es una categoria de cobertura distinta, ver la
 * nota de la migracion 012. */
export const PROJECT_NODES_TIPO = ["conversado", "silencioso", "cosechado", "salto"] as const;
export type ProjectNodeTipo = (typeof PROJECT_NODES_TIPO)[number];

/** sessions.ruta (JSONB) guarda el modo de cada nodo conversado -- el
 * mismo conjunto que project_nodes.tipo, salvo 'cosechado' (los nodos
 * cosechados del vecindario no forman parte de la ruta conversada). */
export const MODO_RUTA: readonly Exclude<ProjectNodeTipo, "cosechado">[] = ["conversado", "silencioso", "salto"];
export type ModoRuta = (typeof MODO_RUTA)[number];

/** pack_clicks.pack (Fase 3.2, migration 014; ampliada en 017 y 019): las
 * claves de dominio de los mundos -- las mismas de packs/<clave>/ y del campo
 * `dominio` de sus nodos, y las que emite POST /api/packs/interes.
 * Fase v1.3.2 (migration 017): + seguridad_digital, exportacion, franquicias.
 * Fase v1.4 (migration 019): + risk_management (séptimo pack). */
export const PACK_CLICKS_PACK = [
  "quality",
  "health_safety",
  "environmental",
  "seguridad_digital",
  "exportacion",
  "franquicias",
  "risk_management",
] as const;
export type PackClave = (typeof PACK_CLICKS_PACK)[number];

/** checklist_items.estado (Fase 3.3, migration 015): estados de un toque. */
// Gestor de estados (migration 030): 'a_medias' se renombró a 'en_proceso'
// (mismo estado, vocabulario de la casa), y entró 'no_aplica' (la tarea no
// corre para esta idea: fuera del denominador del avance, jamás tardía).
export const CHECKLIST_ESTADO = ["pendiente", "empezado", "en_proceso", "hecho", "no_aplica"] as const;
export type ChecklistEstado = (typeof CHECKLIST_ESTADO)[number];

/** Los estados que SÍ cuentan para el avance ("X de N activas"): todo menos
 * 'no_aplica', que el usuario retiró a propósito. Fuente única para el
 * denominador honesto en toda superficie. */
export const ESTADOS_ACTIVOS = CHECKLIST_ESTADO.filter((e) => e !== "no_aplica");
export const esActivo = (estado: ChecklistEstado) => estado !== "no_aplica";

/** Dominios válidos de sessions/plans/checklist_items (Fase 3.5, migration
 * 016): core + packs. Sin fila en project_unlocks, un dominio de pack no
 * existe para el motor. */
export const DOMINIOS = ["core", ...PACK_CLICKS_PACK] as const;
export type Dominio = (typeof DOMINIOS)[number];

/** projects.modo_camino (Fase 3.8, migration 018): cómo lleva el usuario su
 * camino en Manos a la Obra. null hasta la primera elección. 'ritmo' = todo
 * como hoy, sin fechas base; 'fechas' = con línea base y recordatorios. El
 * interruptor de "pausar" solo alterna 'fechas' ↔ 'ritmo' (jamás borra las
 * fechas ya puestas en los ítems). */
export const MODO_CAMINO = ["ritmo", "fechas"] as const;
export type ModoCamino = (typeof MODO_CAMINO)[number];

/** checklist_items.fecha_base_origen (Fase 3.8, migration 018): procedencia
 * de la fecha objetivo VIGENTE de un ítem. 'sugerida' = del sugeridor
 * determinístico; 'ajustada' = el usuario movió una fecha que fue sugerida;
 * 'manual' = fecha puesta a mano sin que hubiera sugerencia previa. */
export const FECHA_BASE_ORIGEN = ["sugerida", "ajustada", "manual"] as const;
export type FechaBaseOrigen = (typeof FECHA_BASE_ORIGEN)[number];

/** user_seguridad.two_factor_method (migración 029, centro de cuenta): el
 * método del segundo factor. null = 2FA sin configurar. Réplica del I Ching
 * sin 'sms' (no tenemos SMS). */
export const METODO_2FA = ["totp", "email"] as const;
export type Metodo2FA = (typeof METODO_2FA)[number];
