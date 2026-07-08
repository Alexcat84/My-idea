-- ============================================================================
-- MY IDEA · introspeccion_schema() -- helper para scripts/check_migrations.py
--
-- Deliberadamente SIN numero de secuencia (no es my_idea_NNN): es una
-- funcion de infraestructura para el checklist de migraciones aplicadas,
-- no un cambio de esquema de la app -- vive junto a las migraciones
-- numeradas (mismo directorio, se aplica igual en el SQL Editor de
-- Supabase) pero no es "una migracion mas" en la secuencia.
--
-- Devuelve en un solo JSON las columnas, definiciones de constraints, y
-- privilegios de funciones del esquema public, para que
-- scripts/check_migrations.py pueda verificar que cada migracion ya fue
-- aplicada sin necesitar una conexion Postgres directa ni un driver nuevo
-- -- reusa el mismo cliente supabase-py + SUPABASE_SERVICE_ROLE_KEY que ya
-- usa engine/db.py.
--
-- SECURITY DEFINER, pero solo de lectura de catalogos (pg_catalog/
-- information_schema), y con EXECUTE revocado de PUBLIC/anon/authenticated
-- y otorgado SOLO a service_role -- misma disciplina que motivo la
-- migracion 006 (el linter de seguridad de Supabase marca cualquier
-- funcion SECURITY DEFINER ejecutable por anon/authenticated).
-- ============================================================================

CREATE OR REPLACE FUNCTION public.introspeccion_schema()
RETURNS jsonb
LANGUAGE sql
SECURITY DEFINER
SET search_path = public
AS $$
  SELECT jsonb_build_object(
    'columnas', (
      SELECT coalesce(jsonb_agg(jsonb_build_object('tabla', table_name, 'columna', column_name)), '[]'::jsonb)
      FROM information_schema.columns
      WHERE table_schema = 'public'
    ),
    'constraints', (
      SELECT coalesce(jsonb_object_agg(conname, pg_get_constraintdef(oid)), '{}'::jsonb)
      FROM pg_constraint
      WHERE connamespace = 'public'::regnamespace
    ),
    'funciones', (
      SELECT coalesce(jsonb_object_agg(
        proname,
        jsonb_build_object(
          'anon_execute', has_function_privilege('anon', oid, 'EXECUTE'),
          'authenticated_execute', has_function_privilege('authenticated', oid, 'EXECUTE')
        )
      ), '{}'::jsonb)
      FROM pg_proc
      WHERE pronamespace = 'public'::regnamespace
    )
  );
$$;

REVOKE ALL ON FUNCTION public.introspeccion_schema() FROM PUBLIC;
REVOKE ALL ON FUNCTION public.introspeccion_schema() FROM anon;
REVOKE ALL ON FUNCTION public.introspeccion_schema() FROM authenticated;
GRANT EXECUTE ON FUNCTION public.introspeccion_schema() TO service_role;
