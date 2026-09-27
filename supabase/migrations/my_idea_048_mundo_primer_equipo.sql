-- my_idea_048_mundo_primer_equipo.sql — undecimo mundo: "Primer Equipo" (primer_equipo).
-- Los 4 CHECK de dominio se amplian a los 10 packs (primer_equipo se suma a los 9 de la 036).
--
-- Mismo patron que la 017, la 019 y la 036:
-- * DROP y ADD como sentencias separadas (no encadenadas) para que
--   dbContract.test.ts pueda parsear el CHECK vigente.
-- * Los cuatro nombres de constraint son los de la 036: sessions_dominio_check,
--   plans_dominio_check, project_unlocks_dominio_check, pack_clicks_pack_check.
--   Ninguna migracion entre la 037 y la 047 toco una aduana de dominio.
--
-- El bloque 048 de my_idea_check_migraciones.sql confirma los 4 contra
-- pg_constraint ANTES y DESPUES (paste-and-run en SQL Editor).
--
-- NOTA DE VISIBILIDAD: esta migracion solo abre la ADUANA de la base; no
-- publica nada. El mundo entra OCULTO en web/lib/assets/packs_catalog.json
-- hasta el visto del fundador.

ALTER TABLE public.project_unlocks
  DROP CONSTRAINT project_unlocks_dominio_check;
ALTER TABLE public.project_unlocks
  ADD CONSTRAINT project_unlocks_dominio_check CHECK (dominio IN
    ('quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias', 'risk_management',
     'compras', 'entrega', 'primer_equipo'));

ALTER TABLE public.sessions
  DROP CONSTRAINT sessions_dominio_check;
ALTER TABLE public.sessions
  ADD CONSTRAINT sessions_dominio_check CHECK (dominio IN
    ('core', 'quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias', 'risk_management',
     'compras', 'entrega', 'primer_equipo'));

ALTER TABLE public.plans
  DROP CONSTRAINT plans_dominio_check;
ALTER TABLE public.plans
  ADD CONSTRAINT plans_dominio_check CHECK (dominio IN
    ('core', 'quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias', 'risk_management',
     'compras', 'entrega', 'primer_equipo'));

ALTER TABLE public.pack_clicks
  DROP CONSTRAINT pack_clicks_pack_check;
ALTER TABLE public.pack_clicks
  ADD CONSTRAINT pack_clicks_pack_check CHECK (pack IN
    ('quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias', 'risk_management',
     'compras', 'entrega', 'primer_equipo'));
