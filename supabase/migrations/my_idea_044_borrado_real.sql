-- my_idea_044_borrado_real.sql — BORRADO REAL DE LOS DATOS DEL USUARIO
-- (decisiones del fundador, 26 sep 2026). "Nada se borra jamás" es la doctrina
-- del catálogo de conocimiento, NO de los datos de los usuarios.
--
-- 1. credit_refund_log.user_id admite NULL: al borrar la cuenta, sus reembolsos
--    se ANONIMIZAN (queda el importe y la fecha, sin vínculo con la persona),
--    porque podrían ser registro fiscal. Si pueden borrarse del todo queda POR
--    VERIFICAR con un profesional.
-- 2. limpiar_ideas_de_invitado(p_dias): borra las ideas de invitado SIN DUEÑO
--    (de una identidad invisible: anónima de Supabase o marcada "invitado") sin
--    actividad en p_dias días. La llama la tarea programada diaria
--    /api/cron/limpiar-invitados con 30. El ON DELETE CASCADE de projects se
--    lleva sesiones, planes, tareas, bitácora y demás. Solo service_role.

ALTER TABLE public.credit_refund_log ALTER COLUMN user_id DROP NOT NULL;

CREATE OR REPLACE FUNCTION public.limpiar_ideas_de_invitado(p_dias integer)
RETURNS integer
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  v_borradas integer;
BEGIN
  IF p_dias IS NULL OR p_dias < 1 THEN
    RETURN 0;
  END IF;
  DELETE FROM public.projects p
  USING auth.users u
  WHERE p.user_id = u.id
    AND (u.is_anonymous IS TRUE OR (u.raw_user_meta_data ->> 'invitado') = 'true')
    AND p.updated_at < now() - make_interval(days => p_dias);
  GET DIAGNOSTICS v_borradas = ROW_COUNT;
  RETURN v_borradas;
END;
$$;

REVOKE EXECUTE ON FUNCTION public.limpiar_ideas_de_invitado(integer) FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION public.limpiar_ideas_de_invitado(integer) TO service_role;
