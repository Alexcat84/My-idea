-- my_idea_018_sentido_del_tiempo.sql
-- Fase 3.8: el sentido del tiempo. Columnas de tiempo real y modo del
-- camino, la baseline por ciclo de plan, y una bitacora de eventos de
-- PROYECTO (distinta de la caja de vidrio por sesion, migration 013).
--
-- Notas de verificacion (mismas reglas que 015/016):
-- * Los CHECK de projects.modo_camino y checklist_items.fecha_base_origen
--   van como ADD CONSTRAINT nombrado (no inline en ADD COLUMN): asi los
--   parsea dbContract.test.ts y asi se pueden relajar por nombre a futuro.
-- * La policy de project_bitacora espeja project_nodes_own
--   (my_idea_001:103-105): EXISTS + (SELECT auth.uid()).

-- 1. La idea que se vuelve proyecto: cuando el usuario la marca realizada.
ALTER TABLE public.projects ADD COLUMN realizada_at timestamptz;

-- 2. Modo del camino (Fase 3.8 §3): null hasta la primera eleccion en
--    Manos a la Obra. 'ritmo' = todo como hoy; 'fechas' = con linea base.
ALTER TABLE public.projects ADD COLUMN modo_camino text;
ALTER TABLE public.projects
  ADD CONSTRAINT projects_modo_camino_check CHECK (modo_camino IN ('ritmo', 'fechas'));

-- 3. Baseline por ciclo de plan (Fase 3.8 §4): se sella al confirmar las
--    fechas. La base VIGENTE de lectura es la del ultimo plan con baseline.
ALTER TABLE public.plans ADD COLUMN baseline_confirmada_at timestamptz;

-- 4. Tiempo real del checklist (Fase 3.8 §2 y §4):
--    completed_at         cuando se hizo el item (timeline real, para TODOS)
--    fecha_base           fecha objetivo VIGENTE del item (solo modo fechas)
--    fecha_base_original  la PRIMERA fecha_base confirmada, preservada al
--                         replanificar -- nunca se reescribe la historia
--    fecha_base_origen    procedencia de la fecha_base vigente
ALTER TABLE public.checklist_items ADD COLUMN completed_at timestamptz;
ALTER TABLE public.checklist_items ADD COLUMN fecha_base timestamptz;
ALTER TABLE public.checklist_items ADD COLUMN fecha_base_original timestamptz;
ALTER TABLE public.checklist_items ADD COLUMN fecha_base_origen text;
ALTER TABLE public.checklist_items
  ADD CONSTRAINT checklist_items_fecha_base_origen_check
    CHECK (fecha_base_origen IN ('sugerida', 'ajustada', 'manual'));

-- 5. Bitacora de eventos de PROYECTO (Fase 3.8): el mueble que hoy no
--    existe. Los eventos de proyecto (cambio de modo, realizar/reabrir, y
--    a futuro replanificaciones y activacion de mundos) no viven en
--    ninguna sesion. Distinta de sessions.decisiones (013), que es la caja
--    de vidrio del motor POR SESION. tipo es texto libre (no enum: no
--    entra a dbContract). El timeline de la Celebracion NO lee esta tabla:
--    se arma de lo persistido (created_at, planes, completed_at, unlocks,
--    realizada_at).
CREATE TABLE public.project_bitacora (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id uuid NOT NULL REFERENCES public.projects(id) ON DELETE CASCADE,
  tipo text NOT NULL,
  payload jsonb NOT NULL DEFAULT '{}',
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX project_bitacora_project_idx ON public.project_bitacora (project_id, created_at);

ALTER TABLE public.project_bitacora ENABLE ROW LEVEL SECURITY;

-- Espejo exacto del patron de project_nodes_own (my_idea_001:103-105).
CREATE POLICY project_bitacora_own ON public.project_bitacora
  FOR ALL USING (EXISTS (SELECT 1 FROM public.projects p
                         WHERE p.id = project_id AND p.user_id = (SELECT auth.uid())));
