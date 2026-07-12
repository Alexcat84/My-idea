-- my_idea_019_mundo_riesgos.sql — Fase v1.4: séptimo pack "Riesgos Bajo
-- Control" (risk_management). Los 4 CHECK de dominio se amplían a los 7 packs
-- (risk_management se suma a los 6 de la 017).
--
-- Mismo patrón que la 017:
-- * DROP y ADD como sentencias separadas (no encadenadas) para que
--   dbContract.test.ts pueda parsear el CHECK vigente.
-- * Nombres de constraint verificados: sessions_dominio_check,
--   plans_dominio_check, project_unlocks_dominio_check, pack_clicks_pack_check.
-- El bloque 019 de my_idea_check_migraciones.sql confirma los 4 contra
-- pg_constraint ANTES y DESPUÉS (paste-and-run en SQL Editor).

ALTER TABLE public.project_unlocks
  DROP CONSTRAINT project_unlocks_dominio_check;
ALTER TABLE public.project_unlocks
  ADD CONSTRAINT project_unlocks_dominio_check CHECK (dominio IN
    ('quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias', 'risk_management'));

ALTER TABLE public.sessions
  DROP CONSTRAINT sessions_dominio_check;
ALTER TABLE public.sessions
  ADD CONSTRAINT sessions_dominio_check CHECK (dominio IN
    ('core', 'quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias', 'risk_management'));

ALTER TABLE public.plans
  DROP CONSTRAINT plans_dominio_check;
ALTER TABLE public.plans
  ADD CONSTRAINT plans_dominio_check CHECK (dominio IN
    ('core', 'quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias', 'risk_management'));

ALTER TABLE public.pack_clicks
  DROP CONSTRAINT pack_clicks_pack_check;
ALTER TABLE public.pack_clicks
  ADD CONSTRAINT pack_clicks_pack_check CHECK (pack IN
    ('quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias', 'risk_management'));
