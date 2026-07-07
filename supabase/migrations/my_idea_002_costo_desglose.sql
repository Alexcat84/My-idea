-- Fase 2.7: telemetria de costo por componente.
-- Guarda, ademas del costo_usd total ya existente, un desglose por
-- componente ({"clasificacion": float, "turnos": float, "plan": float,
-- "estado_vivo": float, "organizador": float}) para monitorear que parte
-- de la sesion crece en costo con el tiempo. Aplicar manualmente en el
-- SQL Editor de Supabase, igual que my_idea_001_init.sql.

alter table sessions
    add column if not exists costo_desglose jsonb;
