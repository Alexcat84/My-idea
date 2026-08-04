-- my_idea_032_modo_por_espacio.sql — "Todo separado" (T3): el MODO DEL CAMINO
-- POR ESPACIO.
--
-- Hasta ahora projects.modo_camino (018) es UNO por proyecto entero: un mundo no
-- podia elegir 'a mi ritmo' vs 'con fechas' distinto del core. Con la PARIDAD
-- TOTAL, cada espacio (el core y cada mundo) tiene su propio modo, su linea base
-- y su ritual, scopeados a su dominio.
--
-- Hogar UNIFORME: una tabla (project_id, dominio, modo_camino). El core NO tiene
-- fila en project_unlocks (016), por eso no basta una columna alli; esta tabla
-- cubre core y mundos por igual. dominio 'core' = el viaje principal; el resto,
-- la clave del pack (mismo dominio que plans/sessions/checklist_items).
--
-- CHECK nombrado (patron de la 016/018) para que dbContract lo parsee. Mismos
-- valores que projects.modo_camino: 'ritmo' | 'fechas' (dbContract MODO_CAMINO).
--
-- TRANSICION (dual-read, decidido con el fundador): projects.modo_camino se
-- CONSERVA como lectura de respaldo del core mientras el front migra a esta
-- tabla; se hace BACKFILL del modo actual del core. Se deja de ESCRIBIR alli;
-- se podra retirar en una migracion futura.

CREATE TABLE public.project_modos (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id uuid NOT NULL REFERENCES public.projects(id) ON DELETE CASCADE,
  dominio text NOT NULL,
  modo_camino text NOT NULL,
  updated_at timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT project_modos_project_dominio_uniq UNIQUE (project_id, dominio)
);

-- CHECK como ADD CONSTRAINT nombrado (patron 018): asi dbContract.test.ts lo
-- parsea y el contrato codigo<->DB cubre tambien project_modos.modo_camino.
ALTER TABLE public.project_modos
  ADD CONSTRAINT project_modos_modo_camino_check CHECK (modo_camino IN ('ritmo', 'fechas'));

CREATE INDEX project_modos_project_idx ON public.project_modos (project_id);

ALTER TABLE public.project_modos ENABLE ROW LEVEL SECURITY;

-- Espejo exacto del patron project_nodes_own (my_idea_001) / project_bitacora (018).
-- FOR ALL USING sin WITH CHECK: Postgres usa la misma expresion como WITH CHECK
-- del INSERT (el mismo dueno inserta y lee).
CREATE POLICY project_modos_own ON public.project_modos
  FOR ALL USING (EXISTS (SELECT 1 FROM public.projects p
                         WHERE p.id = project_id AND p.user_id = (SELECT auth.uid())));

-- Backfill: el modo actual del core baja a la tabla como la fila 'core'. Solo los
-- proyectos que YA eligieron modo (modo_camino no null). Idempotente.
INSERT INTO public.project_modos (project_id, dominio, modo_camino)
SELECT id, 'core', modo_camino FROM public.projects WHERE modo_camino IS NOT NULL
ON CONFLICT (project_id, dominio) DO NOTHING;
