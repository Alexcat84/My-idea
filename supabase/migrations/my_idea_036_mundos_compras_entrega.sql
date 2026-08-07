-- my_idea_036_mundos_compras_entrega.sql — octavo y noveno mundo:
-- "Tu Compra Correcta" (compras) y "Del Taller a sus Manos" (entrega).
-- Los 4 CHECK de dominio se amplían a los 9 packs (compras y entrega se suman
-- a los 7 de la 019).
--
-- Mismo patrón que la 017 y la 019:
-- * DROP y ADD como sentencias separadas (no encadenadas) para que
--   dbContract.test.ts pueda parsear el CHECK vigente.
-- * Nombres de constraint verificados contra el esquema: sessions_dominio_check,
--   plans_dominio_check, project_unlocks_dominio_check, pack_clicks_pack_check.
--
-- SON LOS CUATRO ÚNICOS. Se revisó el esquema entero buscando otras aduanas que
-- nombren dominios: project_modos.dominio y checklist_items.dominio NO tienen
-- CHECK propio (el único de project_modos es project_modos_modo_camino_check,
-- sobre 'ritmo'/'fechas'), así que no hay nada más que ampliar aquí.
--
-- El bloque 036 de my_idea_check_migraciones.sql confirma los 4 contra
-- pg_constraint ANTES y DESPUÉS (paste-and-run en SQL Editor).
--
-- NOTA DE VISIBILIDAD: esta migración solo abre la ADUANA de la base. Los dos
-- mundos quedan OCULTOS en el catálogo hasta el visto del fundador; el
-- interruptor vive en el front (web/lib/espacios.ts), no aquí.

ALTER TABLE public.project_unlocks
  DROP CONSTRAINT project_unlocks_dominio_check;
ALTER TABLE public.project_unlocks
  ADD CONSTRAINT project_unlocks_dominio_check CHECK (dominio IN
    ('quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias', 'risk_management',
     'compras', 'entrega'));

ALTER TABLE public.sessions
  DROP CONSTRAINT sessions_dominio_check;
ALTER TABLE public.sessions
  ADD CONSTRAINT sessions_dominio_check CHECK (dominio IN
    ('core', 'quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias', 'risk_management',
     'compras', 'entrega'));

ALTER TABLE public.plans
  DROP CONSTRAINT plans_dominio_check;
ALTER TABLE public.plans
  ADD CONSTRAINT plans_dominio_check CHECK (dominio IN
    ('core', 'quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias', 'risk_management',
     'compras', 'entrega'));

ALTER TABLE public.pack_clicks
  DROP CONSTRAINT pack_clicks_pack_check;
ALTER TABLE public.pack_clicks
  ADD CONSTRAINT pack_clicks_pack_check CHECK (pack IN
    ('quality', 'health_safety', 'environmental',
     'seguridad_digital', 'exportacion', 'franquicias', 'risk_management',
     'compras', 'entrega'));
