-- ============================================================================
-- MY IDEA · Migration 013_caja_de_vidrio
-- Fase 3.1: observabilidad del cerebro (prerequisito de la beta). Dos
-- columnas nuevas en sessions, ambas JSONB sin CHECK (son bitacoras de
-- forma libre, no valores enumerados -- no aplica a dbContract.ts):
--
--   decisiones: lista completa de eventos de la sesion (decision_turno
--   por turno del interprete -- candidatos locales, saltos_posibles con
--   sus scores, la decision tomada y el razonamiento corto del modelo --
--   mas fallback_auto, autodeclaracion_fallida, coherencia_cobertura_
--   corregida, procedencia_invalida y numero_huerfano). Se persiste de
--   una sola vez al cerrar la sesion (cerrar_sesion/cerrarSesion), no
--   requiere un write por turno: Python y la web ya acumulan estos
--   eventos en memoria/estado_recorrido durante el recorrido.
--
--   calidad: veredicto del juez de sesion muestreado (Haiku), JSON con
--   {pertinencia_transiciones, repeticion_detectada, señales_fuera_de_
--   material, comentario}. Null en sesiones no muestreadas.
-- ============================================================================

ALTER TABLE public.sessions ADD COLUMN IF NOT EXISTS decisiones JSONB;
ALTER TABLE public.sessions ADD COLUMN IF NOT EXISTS calidad JSONB;

COMMENT ON COLUMN public.sessions.decisiones IS
  'Fase 3.1: bitacora completa de eventos de la sesion (decision_turno, fallback_auto, autodeclaracion_fallida, coherencia_cobertura_corregida, procedencia_invalida, numero_huerfano). Persistida al cerrar la sesion.';
COMMENT ON COLUMN public.sessions.calidad IS
  'Fase 3.1: veredicto JSON del juez de sesion muestreado (Haiku) -- señal de triage para revision humana, no un veredicto final. Null si la sesion no fue muestreada.';
