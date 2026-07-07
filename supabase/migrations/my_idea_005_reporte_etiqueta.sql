-- ============================================================================
-- MY IDEA · Migration 005_reporte_etiqueta
-- Hotfix v2.1.2 (continuacion): la migracion 004 arreglo sessions.tipo para
-- aceptar 'reporte', pero modo_reporte() tambien llama a
-- db.guardar_plan(..., "reporte_numeros", ...), y plans.etiqueta tiene el
-- mismo tipo de CHECK constraint que nunca se actualizo para Motor v2.1.
-- Con 004 sola aplicada, --reporte avanza un paso mas (crear_sesion ya no
-- revienta) pero sigue reventando en guardar_plan con el mismo codigo de
-- error (23514, esta vez plans_etiqueta_check). Encontrado en la misma
-- sesion en vivo, re-probando --reporte tras aplicar 004.
-- ============================================================================

ALTER TABLE public.plans DROP CONSTRAINT plans_etiqueta_check;
ALTER TABLE public.plans ADD CONSTRAINT plans_etiqueta_check
  CHECK (etiqueta IN ('organizador','inicial','completo','seguimiento','reporte_numeros'));
