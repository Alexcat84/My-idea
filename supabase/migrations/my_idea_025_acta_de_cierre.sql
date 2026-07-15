-- my_idea_025_acta_de_cierre.sql
-- Fase 4.0 (docs/FLUJO_TRACKING.md §8): EL ACTA DE CIERRE. Cerrar una idea es
-- un acto soberano del usuario (nunca exigio el 100% del checklist y nunca lo
-- exigira), pero un cierre sin memoria del porque pierde la mitad de la
-- historia. El acta la conserva.
--
-- Notas de numeracion (importante):
-- * Se salta de la 019 a la 025 A PROPOSITO: las 020-024 estan RESERVADAS al
--   frente de cuentas y creditos (ledger, RPC de consumo, cortesia, RevenueCat,
--   refund) en la rama cuentas-y-creditos, disenadas y sin aplicar. Usar la 020
--   aqui provocaria una colision de numeracion cuando ese frente despierte.
--
-- Notas de verificacion (mismas reglas que 015/016/018):
-- * No hay CHECK que anadir: cierre_motivo es texto libre del usuario (o null).
-- * El payload del evento 'realizada' de project_bitacora pasa de {accion} a
--   {accion, motivo}. project_bitacora.payload ya es jsonb (018): NO requiere
--   cambio de esquema, solo del escritor. Se documenta aqui para que el
--   contrato quede en un solo sitio legible.

-- 1. El motivo del cierre, en las palabras del usuario. null = cerro sin
--    escribir nada (cero friccion: el campo del ritual es OPCIONAL). Guarda
--    SIEMPRE el motivo del ULTIMO cierre; la secuencia completa (si el usuario
--    reabrio y volvio a cerrar) vive en project_bitacora, porque la historia
--    no se reescribe.
ALTER TABLE public.projects ADD COLUMN IF NOT EXISTS cierre_motivo text;

COMMENT ON COLUMN public.projects.cierre_motivo IS
  'Fase 4.0 §8: por que el usuario cerro la idea aqui, en sus palabras. '
  'Opcional (null si cerro sin escribir). Reabrir NO lo borra: la bitacora '
  'conserva la secuencia de cierres con su motivo cada uno.';
