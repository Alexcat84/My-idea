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
