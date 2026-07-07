-- ============================================================================
-- MY IDEA · Migration 004_reporte_tipo
-- Hotfix v2.1.2: modo_reporte() (Motor v2.1) llama a db.crear_sesion(project_id,
-- "reporte", ...), pero sessions.tipo nunca se actualizo para aceptar ese
-- valor. Contra un proyecto real con Supabase, --reporte revienta con
-- postgrest.exceptions.APIError (23514, sessions_tipo_check) DESPUES de haber
-- generado y guardado el reporte en disco: el crash es silencioso para el
-- contenido pero real para la persistencia (la sesion de reporte nunca
-- queda registrada en Supabase). Encontrado en una sesion en vivo, no en
-- las pruebas anteriores (corrian todas en modo offline/JSON local, que no
-- tiene este constraint).
-- ============================================================================

ALTER TABLE public.sessions DROP CONSTRAINT sessions_tipo_check;
ALTER TABLE public.sessions ADD CONSTRAINT sessions_tipo_check
  CHECK (tipo IN ('gratuito','inicial','seguimiento','reporte'));
