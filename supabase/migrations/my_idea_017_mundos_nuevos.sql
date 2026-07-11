-- my_idea_017_mundos_nuevos.sql — Fase v1.3.2: tres mundos nuevos.
-- Los CHECK de dominio se amplían a los 6 packs (seguridad_digital,
-- exportacion, franquicias se suman a los HSEQ de la 016).
--
-- Nombres de constraint verificados contra las migraciones fuente:
-- * sessions_dominio_check y plans_dominio_check: nombrados explícitamente
--   en la 016 (ADD CONSTRAINT).
-- * project_unlocks_dominio_check y pack_clicks_pack_check: CHECK inline de
--   columna en 016/014 — Postgres los bautiza <tabla>_<columna>_check.
-- El bloque 017 de my_idea_check_migraciones.sql confirma los 4 contra
-- pg_constraint ANTES y DESPUÉS de aplicar (paste-and-run en SQL Editor).
--
-- Nota de forma: DROP y ADD van como sentencias separadas (no encadenadas
-- con coma) para que dbContract.test.ts pueda parsear el CHECK vigente.

ALTER TABLE public.project_unlocks
  DROP CONSTRAINT project_unlocks_dominio_check;
ALTER TABLE public.project_unlocks
  ADD CONSTRAINT project_unlocks_dominio_check CHECK (dominio IN
    ('quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias'));

ALTER TABLE public.sessions
  DROP CONSTRAINT sessions_dominio_check;
ALTER TABLE public.sessions
  ADD CONSTRAINT sessions_dominio_check CHECK (dominio IN
    ('core', 'quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias'));

ALTER TABLE public.plans
  DROP CONSTRAINT plans_dominio_check;
ALTER TABLE public.plans
  ADD CONSTRAINT plans_dominio_check CHECK (dominio IN
    ('core', 'quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias'));

ALTER TABLE public.pack_clicks
  DROP CONSTRAINT pack_clicks_pack_check;
ALTER TABLE public.pack_clicks
  ADD CONSTRAINT pack_clicks_pack_check CHECK (pack IN
    ('quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias'));
