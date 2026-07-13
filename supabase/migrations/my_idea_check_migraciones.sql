-- ─────────────────────────────────────────────────────────────────────────────
-- Migration verification script — My Idea (La Telaraña del Emprendedor)
-- Run in Supabase SQL Editor. Each row shows migration number + status.
-- Paste this whole file and run it as-is — no setup, no functions to apply
-- first: it's a plain query, the rows show up directly in Results.
--
-- Deliberately unnumbered (not my_idea_NNN_*.sql): this is a maintenance
-- script, not an app schema change. Update it in the SAME commit every
-- time a new migration is added, by appending one more UNION ALL block.
-- ─────────────────────────────────────────────────────────────────────────────

SELECT num, description,
  CASE WHEN check_result THEN '✓ OK' ELSE '✗ MISSING' END AS status
FROM (

  -- 001 · Core tables
  SELECT '001' AS num, 'Core tables (projects, sessions, project_nodes, plans, query_credits)' AS description,
    EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='projects')
    AND EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='sessions')
    AND EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='project_nodes')
    AND EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='plans')
    AND EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='query_credits')
    AS check_result

  UNION ALL
  -- 002 · Cost breakdown per session (Fase 2.7)
  SELECT '002', 'sessions.costo_desglose (JSONB)',
    EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='sessions' AND column_name='costo_desglose')

  UNION ALL
  -- 003 · Motor v2.1 numeric memory
  SELECT '003', 'projects.numeros_proyecto (JSONB)',
    EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='projects' AND column_name='numeros_proyecto')

  UNION ALL
  -- 004 · Hotfix v2.1.2, sessions.tipo widened for 'reporte'
  SELECT '004', 'sessions_tipo_check allows ''reporte''',
    EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'sessions_tipo_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%reporte%'
    )

  UNION ALL
  -- 005 · Hotfix v2.1.2 continued, plans.etiqueta widened for 'reporte_numeros'
  SELECT '005', 'plans_etiqueta_check allows ''reporte_numeros''',
    EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'plans_etiqueta_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%reporte_numeros%'
    )

  UNION ALL
  -- 006 · Security linter fix, revoke rls_auto_enable() from anon/authenticated
  SELECT '006', 'rls_auto_enable() has no EXECUTE for anon/authenticated',
    NOT EXISTS (
      SELECT 1 FROM information_schema.role_routine_grants
      WHERE routine_schema = 'public' AND routine_name = 'rls_auto_enable'
        AND grantee IN ('anon', 'authenticated') AND privilege_type = 'EXECUTE'
    )

  UNION ALL
  -- 007 · Motor v2.2 offer type / unit / discarded numbers
  SELECT '007', 'projects.tipo_oferta / unidad_venta / numeros_descartados',
    EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='projects' AND column_name='tipo_oferta')
    AND EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='projects' AND column_name='unidad_venta')
    AND EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='projects' AND column_name='numeros_descartados')

  UNION ALL
  -- 008 · Phase 3.0 beta gate
  SELECT '008', 'beta_allowlist table',
    EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='beta_allowlist')

  UNION ALL
  -- 009 · Phase 3.0 resumable interview-loop state
  SELECT '009', 'sessions.estado_recorrido (JSONB)',
    EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='sessions' AND column_name='estado_recorrido')

  UNION ALL
  -- 010 · Phase 3.0 resumable report mini-interview state
  SELECT '010', 'projects.estado_reporte (JSONB)',
    EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='projects' AND column_name='estado_reporte')

  UNION ALL
  -- 011 · Hotfix v2.2.1 configurable session budget, persisted per session
  SELECT '011', 'sessions.presupuesto_usd (NUMERIC)',
    EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='sessions' AND column_name='presupuesto_usd')

  UNION ALL
  -- 012 · Bug fix found verifying Hotfix v2.2.1 live: project_nodes_tipo_check allows 'salto'
  SELECT '012', 'project_nodes_tipo_check allows ''salto''',
    EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'project_nodes_tipo_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%salto%'
    )

  UNION ALL
  -- 013 · Phase 3.1 glass box: sessions.decisiones (event log) + sessions.calidad (session judge verdict)
  SELECT '013', 'sessions.decisiones + sessions.calidad (JSONB)',
    EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='sessions' AND column_name='decisiones')
    AND EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='sessions' AND column_name='calidad')

  UNION ALL
  -- 014 · Phase 3.2 pack facade demand telemetry
  SELECT '014', 'pack_clicks table (quality/health_safety/environmental)',
    EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='pack_clicks')

  UNION ALL
  -- 015 · Phase 3.3 checklist loop: one row per actionable plan step
  SELECT '015', 'checklist_items table + estado CHECK + RLS policy',
    EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='checklist_items')
    AND EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'checklist_items_estado_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%a_medias%'
    )
    AND EXISTS (SELECT 1 FROM pg_policies WHERE schemaname='public' AND tablename='checklist_items' AND policyname='checklist_items_own')

  UNION ALL
  -- 016 · Phase 3.5 HSEQ worlds behind flags: unlocks + dominio provenance
  SELECT '016', 'project_unlocks table + sessions.dominio + plans.dominio (CHECK core+3 packs)',
    EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='project_unlocks')
    AND EXISTS (SELECT 1 FROM pg_policies WHERE schemaname='public' AND tablename='project_unlocks' AND policyname='project_unlocks_own')
    AND EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'sessions_dominio_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%health_safety%'
    )
    AND EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'plans_dominio_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%health_safety%'
    )

  UNION ALL
  -- 017 · Fase v1.3.2 tres mundos nuevos: los 4 CHECK de dominio amplían a 6 packs.
  -- ANTES de aplicar la 017, esta fila debe decir MISSING pero los 4 conname
  -- deben EXISTIR (verificación de nombres del patch); DESPUÉS, ✓ OK.
  SELECT '017', 'CHECKs de dominio con 6 packs (seguridad_digital/exportacion/franquicias)',
    EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'project_unlocks_dominio_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%seguridad_digital%'
    )
    AND EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'sessions_dominio_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%exportacion%'
    )
    AND EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'plans_dominio_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%franquicias%'
    )
    AND EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'pack_clicks_pack_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%seguridad_digital%'
    )

  UNION ALL
  -- 018 · Fase 3.8 el sentido del tiempo: columnas de tiempo/modo/baseline,
  -- CHECKs nombrados de modo_camino y fecha_base_origen, y project_bitacora.
  SELECT '018', 'tiempo real + modo_camino + baseline + fecha_base(_origen/_original) + project_bitacora',
    EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='projects' AND column_name='realizada_at')
    AND EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='projects' AND column_name='modo_camino')
    AND EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'projects_modo_camino_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%fechas%'
    )
    AND EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='plans' AND column_name='baseline_confirmada_at')
    AND EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='checklist_items' AND column_name='completed_at')
    AND EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='checklist_items' AND column_name='fecha_base')
    AND EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='checklist_items' AND column_name='fecha_base_original')
    AND EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'checklist_items_fecha_base_origen_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%sugerida%'
    )
    AND EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='project_bitacora')
    AND EXISTS (SELECT 1 FROM pg_policies WHERE schemaname='public' AND tablename='project_bitacora' AND policyname='project_bitacora_own')

  UNION ALL
  -- 019 · Fase v1.4 séptimo pack: los 4 CHECK de dominio amplían a 7 packs
  -- (risk_management). ANTES de aplicar debe decir MISSING pero los 4 conname
  -- deben EXISTIR; DESPUÉS, ✓ OK.
  SELECT '019', 'CHECKs de dominio con 7 packs (+risk_management)',
    EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'project_unlocks_dominio_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%risk_management%'
    )
    AND EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'sessions_dominio_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%risk_management%'
    )
    AND EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'plans_dominio_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%risk_management%'
    )
    AND EXISTS (
      SELECT 1 FROM pg_constraint
      WHERE conname = 'pack_clicks_pack_check' AND connamespace = 'public'::regnamespace
        AND pg_get_constraintdef(oid) LIKE '%risk_management%'
    )

  UNION ALL
  -- 020 · Cuentas y créditos: ledger balance-based + caja de vidrio + RLS de solo-lectura del dueño
  SELECT '020', 'ledger de créditos (credit_accounts + credit_transactions + RLS + índice idempotencia)',
    EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='credit_accounts')
    AND EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='credit_transactions')
    AND EXISTS (SELECT 1 FROM pg_policies WHERE schemaname='public' AND tablename='credit_accounts' AND policyname='credit_accounts_own_select')
    AND EXISTS (SELECT 1 FROM pg_indexes WHERE schemaname='public' AND indexname='credit_transactions_idempotency_key')

  UNION ALL
  -- 021 · RPC atómicas de consumo/otorgamiento: SECURITY DEFINER y sin EXECUTE para anon/authenticated
  SELECT '021', 'RPC consumir_creditos + otorgar_creditos (SECURITY DEFINER, service-role-only)',
    EXISTS (SELECT 1 FROM pg_proc WHERE proname='consumir_creditos' AND pronamespace='public'::regnamespace AND prosecdef)
    AND EXISTS (SELECT 1 FROM pg_proc WHERE proname='otorgar_creditos' AND pronamespace='public'::regnamespace AND prosecdef)
    AND NOT EXISTS (
      SELECT 1 FROM information_schema.role_routine_grants
      WHERE routine_schema='public' AND routine_name='consumir_creditos'
        AND grantee IN ('anon','authenticated') AND privilege_type='EXECUTE'
    )

  UNION ALL
  -- 022 · Cortesía de beta: 20 créditos una sola vez (blindaje beta_courtesy_log)
  SELECT '022', 'cortesía (beta_courtesy_log + otorgar_cortesia)',
    EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='beta_courtesy_log')
    AND EXISTS (SELECT 1 FROM pg_proc WHERE proname='otorgar_cortesia' AND pronamespace='public'::regnamespace AND prosecdef)

  UNION ALL
  -- 023 · RevenueCat: idempotencia de webhook + grant idempotente (esquema; pasarelas NO activadas)
  SELECT '023', 'RevenueCat (revenuecat_webhook_events + otorgar_creditos_idempotente)',
    EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='revenuecat_webhook_events')
    AND EXISTS (SELECT 1 FROM pg_proc WHERE proname='otorgar_creditos_idempotente' AND pronamespace='public'::regnamespace AND prosecdef)

  UNION ALL
  -- 024 · Refund: nadie pierde créditos por un fallo del sistema
  SELECT '024', 'refund (credit_refund_log + reembolsar_creditos)',
    EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='credit_refund_log')
    AND EXISTS (SELECT 1 FROM pg_proc WHERE proname='reembolsar_creditos' AND pronamespace='public'::regnamespace AND prosecdef)

) checks
ORDER BY num;
