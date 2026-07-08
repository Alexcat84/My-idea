-- ============================================================================
-- MY IDEA · Migration 010_estado_reporte
-- Fase 3.0: estado resumible de la mini-entrevista de --reporte (modo_reporte
-- en prototipo_motor.py). El CLI la corre como un bucle bloqueante dentro de
-- UN proceso; la web la expone pregunta por pregunta (POST
-- /api/project/[id]/report, ver spec de Fase 3.0), asi que el progreso entre
-- llamadas (tipo_oferta/unidad_venta de trabajo, la lista de campos
-- faltantes, el indice actual, el conteo de "no aplica", si ya se
-- reclasifico el molde, y el acumulado de costo propio del reporte) tiene
-- que persistir en algun lado entre una pregunta y la siguiente.
-- ============================================================================

ALTER TABLE public.projects ADD COLUMN IF NOT EXISTS estado_reporte JSONB;

COMMENT ON COLUMN public.projects.estado_reporte IS
  'Estado resumible de la mini-entrevista de POST /api/project/[id]/report '
  'entre una pregunta y la siguiente: fase '
  '(clasificando_oferta | preguntando | reclasificando_molde), '
  'tipo_oferta/unidad_venta de trabajo, faltantes_esenciales, indice, '
  'no_aplica_count, molde_cambiado, y el acumulado de costo (tope propio '
  'PRESUPUESTO_REPORTE_USD, independiente del presupuesto de sesion). '
  'Null cuando no hay una mini-entrevista de reporte en curso.';
