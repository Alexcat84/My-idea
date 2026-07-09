-- ============================================================================
-- MY IDEA · Migration 011_presupuesto_sesion
-- Hotfix v2.2.1: PRESUPUESTO_SESION_USD ahora es configurable por variable
-- de entorno (Python ya lo era; web/lib/costmeter.ts se alinea con este
-- hotfix), con default subido de 0.30 a 0.35. Como el valor puede cambiar
-- entre corridas (o bajar temporalmente a PRESUPUESTO_REPORTE_USD=0.10
-- dentro de --reporte), cada fila de sessions guarda el presupuesto REAL
-- con el que esa sesion especifica corrio, para poder auditar despues sin
-- adivinar que configuracion estaba vigente en ese momento.
-- ============================================================================

ALTER TABLE public.sessions ADD COLUMN IF NOT EXISTS presupuesto_usd NUMERIC(8,4);

COMMENT ON COLUMN public.sessions.presupuesto_usd IS
  'Presupuesto en USD vigente cuando esta sesion corrio (PRESUPUESTO_SESION_USD '
  'del entorno en ese momento, o PRESUPUESTO_REPORTE_USD=0.10 si fue una sesion '
  'tipo reporte). Se persiste al cerrar la sesion, no al crearla, porque '
  '--reporte baja el presupuesto DESPUES de crear_sesion. Null en sesiones '
  'creadas antes de este hotfix.';
