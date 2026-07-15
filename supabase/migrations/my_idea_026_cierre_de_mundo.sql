-- my_idea_026_cierre_de_mundo.sql
-- Fase 4.2: LOS MUNDOS COMO SUBPROYECTOS COMPLETOS. Un mundo se explora, se
-- planifica, se ejecuta con su checklist... y hasta hoy no se podia CERRAR. La
-- idea principal tiene su acta (025); el mundo no tenia nada: quedaba abierto
-- para siempre, aunque el usuario ya hubiera terminado con el.
--
-- Decision de esquema (el fundador dejo elegir): las dos columnas van en
-- project_unlocks, NO en una tabla nueva. La fila del unlock ES la presencia
-- del mundo en esta idea (sin ella el dominio no existe para el motor); su
-- ciclo de vida completo -- se activo, se completo -- cabe en esa misma fila.
-- Una tabla aparte para dos columnas seria un mueble sin habitantes.
--
-- Espejo deliberado de la 025 (mismos parametros que el viaje principal):
-- * completado_at nullable = reversible ("Reabrir este mundo" lo pone a null),
--   igual que projects.realizada_at.
-- * cierre_motivo text = OPCIONAL, sin CHECK: es texto libre del usuario.
--   Reabrir NO lo borra (la historia no se reescribe), igual que la 025.
-- * La secuencia completa de cierres vive en project_bitacora
--   (tipo 'mundo_completado', payload {mundo, accion, motivo}); payload ya es
--   jsonb desde la 018: NO requiere cambio de esquema, solo del escritor.
--
-- Notas de numeracion: la 020-024 siguen RESERVADAS al frente de cuentas y
-- creditos (rama cuentas-y-creditos, disenadas y sin aplicar). La 025 tomo el
-- salto; esta continua desde ahi.

-- 1. Cuando el usuario dio por terminado este mundo. null = mundo abierto (el
--    estado de siempre). No exige su checklist al 100%: cerrar es soberania
--    del usuario, aqui igual que en la idea principal.
ALTER TABLE public.project_unlocks ADD COLUMN IF NOT EXISTS completado_at timestamptz;

-- 2. El porque, en las palabras del usuario. null = cerro sin escribir nada.
--    Guarda SIEMPRE el motivo del ULTIMO cierre de ESTE mundo.
ALTER TABLE public.project_unlocks ADD COLUMN IF NOT EXISTS cierre_motivo text;

COMMENT ON COLUMN public.project_unlocks.completado_at IS
  'Fase 4.2: el usuario dio por terminado este mundo. null = abierto. '
  'Reversible (reabrir lo pone a null). No exige checklist al 100%: los items '
  'pendientes quedan intactos como testigos.';

COMMENT ON COLUMN public.project_unlocks.cierre_motivo IS
  'Fase 4.2: por que el usuario cerro ESTE mundo, en sus palabras. Opcional. '
  'Reabrir NO lo borra: project_bitacora conserva la secuencia de cierres.';
