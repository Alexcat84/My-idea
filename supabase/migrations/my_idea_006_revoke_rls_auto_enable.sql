-- ============================================================================
-- MY IDEA · Migration 006_revoke_rls_auto_enable
-- Fix para 2 de los 3 hallazgos del linter de seguridad de Supabase:
--
--   - anon_security_definer_function_executable
--   - authenticated_security_definer_function_executable
--
-- public.rls_auto_enable() no fue creada por ninguna migracion de este
-- repo (no aparece en 001-005) — es una funcion SECURITY DEFINER, sin
-- argumentos, cuyo tipo de retorno es "event_trigger" (confirmado al
-- invocarla via RPC: Postgres devuelve "cannot display a value of type
-- event_trigger", el error tipico de una funcion pensada para colgarse de
-- un EVENT TRIGGER, no para llamarse directamente). Es decir: existe para
-- que Postgres la dispare automaticamente en eventos DDL (por ejemplo,
-- para forzar RLS en cada tabla nueva que se cree), no para ser parte de
-- la API publica de la app.
--
-- Al vivir en el schema public sin una revocacion explicita, PostgREST la
-- expone igual que cualquier otra funcion: como endpoint RPC alcanzable
-- por los roles anon y authenticated (/rest/v1/rpc/rls_auto_enable). Eso
-- es lo que el linter marca. La app (este repo) nunca la llama por RPC
-- (grep sin resultados), asi que revocar el EXECUTE de los roles publicos
-- no le quita ninguna funcionalidad usada — el mecanismo de event trigger
-- en si no depende de estos grants para dispararse.
-- ============================================================================

REVOKE EXECUTE ON FUNCTION public.rls_auto_enable() FROM PUBLIC;
REVOKE EXECUTE ON FUNCTION public.rls_auto_enable() FROM anon;
REVOKE EXECUTE ON FUNCTION public.rls_auto_enable() FROM authenticated;
