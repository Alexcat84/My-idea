-- ============================================================================
-- MY IDEA · Migration 007_tipo_oferta
-- Motor v2.2: generaliza el Reporte de Sostenibilidad mas alla de "producto
-- fisico vendido por pieza". El intérprete de turno ahora extrae, cuando el
-- usuario lo revela, el tipo de oferta (producto_fisico/servicio/digital/
-- mixto) y la unidad de venta literal (pieza, cliente, pack, usuario...).
--
-- NOTA DE NUMERACION: el prompt original de Fable decia "Migracion 006",
-- pero ese numero ya estaba tomado por el fix de seguridad del linter de
-- Supabase (my_idea_006_revoke_rls_auto_enable.sql, hotfix v2.1.3). Esta es
-- la 007.
--
-- numeros_descartados (item 9 del prompt v2.2): auditoria de campos de
-- numeros_proyecto invalidados por contaminacion de unidad (ej. un
-- presupuesto mensual capturado como costo por pieza) -- se conservan aqui
-- con el motivo, en vez de borrarse, para no perder trazabilidad.
-- ============================================================================

ALTER TABLE public.projects ADD COLUMN IF NOT EXISTS tipo_oferta TEXT
  CHECK (tipo_oferta IN ('producto_fisico','servicio','digital','mixto'));
ALTER TABLE public.projects ADD COLUMN IF NOT EXISTS unidad_venta TEXT;
ALTER TABLE public.projects ADD COLUMN IF NOT EXISTS numeros_descartados JSONB NOT NULL DEFAULT '{}'::jsonb;
