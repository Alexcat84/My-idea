-- ============================================================================
-- MY IDEA · introspeccion_schema() + checklist_migraciones() -- helpers para
-- scripts/check_migrations.py Y para verlo directo en el SQL Editor.
--
-- Deliberadamente SIN numero de secuencia (no es my_idea_NNN): son
-- funciones de infraestructura para el checklist de migraciones
-- aplicadas, no un cambio de esquema de la app -- viven junto a las
-- migraciones numeradas (mismo directorio, se aplican igual en el SQL
-- Editor de Supabase) pero no son "una migracion mas" en la secuencia.
--
-- introspeccion_schema() devuelve en un solo JSON las columnas,
-- definiciones de constraints, y privilegios de funciones del esquema
-- public -- la usa scripts/check_migrations.py (via supabase-py +
-- SUPABASE_SERVICE_ROLE_KEY, sin conexion Postgres directa ni driver
-- nuevo) y tambien checklist_migraciones() internamente.
--
-- checklist_migraciones() aplica el MISMO chequeo migracion por migracion
-- que scripts/check_migrations.py, pero devuelve filas (migracion,
-- descripcion, aplicada) para poder correr
-- `SELECT * FROM checklist_migraciones();` directo en el SQL Editor y
-- verlo en la pestaña Results, sin salir del dashboard de Supabase.
--
-- IMPORTANTE: cada vez que se agrega una migracion nueva, hay que
-- actualizar EN LOS DOS LADOS -- la lista MIGRACIONES de
-- scripts/check_migrations.py Y el UNION ALL de checklist_migraciones()
-- aqui abajo. Son dos registros paralelos a proposito (Python para CI/
-- terminal, SQL para el Editor), no uno generado del otro.
--
-- SECURITY DEFINER, pero solo de lectura de catalogos (pg_catalog/
-- information_schema), y con EXECUTE revocado de PUBLIC/anon/authenticated
-- y otorgado SOLO a service_role -- misma disciplina que motivo la
-- migracion 006 (el linter de seguridad de Supabase marca cualquier
-- funcion SECURITY DEFINER ejecutable por anon/authenticated). Estas
-- restricciones solo protegen la API REST (PostgREST) -- el SQL Editor de
-- Supabase corre con credenciales de owner y puede llamarlas igual.
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

-- ----------------------------------------------------------------------------
-- checklist_migraciones(): mismo chequeo que scripts/check_migrations.py,
-- como filas. Uso en el SQL Editor: SELECT * FROM checklist_migraciones();
-- ----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION public.checklist_migraciones()
RETURNS TABLE(migracion text, descripcion text, aplicada boolean)
LANGUAGE sql
SECURITY DEFINER
SET search_path = public
AS $$
  WITH ctx AS (SELECT introspeccion_schema() AS j)
  SELECT migracion, descripcion, aplicada FROM (
    SELECT
      'my_idea_001_init.sql' AS migracion,
      'Esquema inicial: projects/sessions/project_nodes/plans/query_credits + RLS' AS descripcion,
      (
        SELECT bool_and(ctx.j->'columnas' @> jsonb_build_array(jsonb_build_object('tabla', req.t, 'columna', req.c)))
        FROM ctx, (VALUES
          ('projects','id'), ('projects','user_id'), ('projects','fase_actual'),
          ('sessions','id'), ('sessions','tipo'), ('sessions','ruta'),
          ('project_nodes','id'),
          ('plans','id'), ('plans','etiqueta'),
          ('query_credits','id')
        ) AS req(t, c)
      ) AS aplicada
    UNION ALL
    SELECT 'my_idea_002_costo_desglose.sql', 'sessions.costo_desglose (JSONB)',
      (SELECT ctx.j->'columnas' @> jsonb_build_array(jsonb_build_object('tabla','sessions','columna','costo_desglose')) FROM ctx)
    UNION ALL
    SELECT 'my_idea_003_numeros.sql', 'projects.numeros_proyecto (JSONB)',
      (SELECT ctx.j->'columnas' @> jsonb_build_array(jsonb_build_object('tabla','projects','columna','numeros_proyecto')) FROM ctx)
    UNION ALL
    SELECT 'my_idea_004_reporte_tipo.sql', 'sessions_tipo_check permite ''reporte''',
      (SELECT (ctx.j->'constraints'->>'sessions_tipo_check') LIKE '%reporte%' FROM ctx)
    UNION ALL
    SELECT 'my_idea_005_reporte_etiqueta.sql', 'plans_etiqueta_check permite ''reporte_numeros''',
      (SELECT (ctx.j->'constraints'->>'plans_etiqueta_check') LIKE '%reporte_numeros%' FROM ctx)
    UNION ALL
    SELECT 'my_idea_006_revoke_rls_auto_enable.sql', 'rls_auto_enable() sin EXECUTE para anon/authenticated',
      (SELECT coalesce((ctx.j->'funciones'->'rls_auto_enable'->>'anon_execute')::boolean, true) IS NOT TRUE
              AND coalesce((ctx.j->'funciones'->'rls_auto_enable'->>'authenticated_execute')::boolean, true) IS NOT TRUE
       FROM ctx)
    UNION ALL
    SELECT 'my_idea_007_tipo_oferta.sql', 'projects.tipo_oferta / unidad_venta / numeros_descartados',
      (
        SELECT bool_and(ctx.j->'columnas' @> jsonb_build_array(jsonb_build_object('tabla','projects','columna', req.c)))
        FROM ctx, (VALUES ('tipo_oferta'), ('unidad_venta'), ('numeros_descartados')) AS req(c)
      )
    UNION ALL
    SELECT 'my_idea_008_beta_allowlist.sql', 'tabla beta_allowlist',
      (SELECT ctx.j->'columnas' @> jsonb_build_array(jsonb_build_object('tabla','beta_allowlist','columna','email')) FROM ctx)
    UNION ALL
    SELECT 'my_idea_009_estado_recorrido.sql', 'sessions.estado_recorrido (JSONB)',
      (SELECT ctx.j->'columnas' @> jsonb_build_array(jsonb_build_object('tabla','sessions','columna','estado_recorrido')) FROM ctx)
    UNION ALL
    SELECT 'my_idea_010_estado_reporte.sql', 'projects.estado_reporte (JSONB)',
      (SELECT ctx.j->'columnas' @> jsonb_build_array(jsonb_build_object('tabla','projects','columna','estado_reporte')) FROM ctx)
    UNION ALL
    SELECT 'my_idea_fn_introspeccion_schema.sql (sin numero)', 'funciones de checklist bloqueadas para anon/authenticated',
      (SELECT coalesce((ctx.j->'funciones'->'introspeccion_schema'->>'anon_execute')::boolean, true) IS NOT TRUE
              AND coalesce((ctx.j->'funciones'->'introspeccion_schema'->>'authenticated_execute')::boolean, true) IS NOT TRUE
              AND coalesce((ctx.j->'funciones'->'checklist_migraciones'->>'anon_execute')::boolean, true) IS NOT TRUE
              AND coalesce((ctx.j->'funciones'->'checklist_migraciones'->>'authenticated_execute')::boolean, true) IS NOT TRUE
       FROM ctx)
  ) AS filas
  ORDER BY migracion;
$$;

REVOKE ALL ON FUNCTION public.checklist_migraciones() FROM PUBLIC;
REVOKE ALL ON FUNCTION public.checklist_migraciones() FROM anon;
REVOKE ALL ON FUNCTION public.checklist_migraciones() FROM authenticated;
GRANT EXECUTE ON FUNCTION public.checklist_migraciones() TO service_role;
