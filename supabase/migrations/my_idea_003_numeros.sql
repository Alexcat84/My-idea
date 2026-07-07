-- Motor v2.1: memoria numerica del proyecto (Reporte de Sostenibilidad).
-- Guarda los numeros que el usuario declara a lo largo de TODAS sus
-- sesiones (inicial y seguimiento): costo_materiales_unidad,
-- horas_por_unidad, valor_hora, precio_tentativo, capacidad_semanal,
-- costos_fijos_mensuales, unidades_vendidas, precio_pagado_real. Cada
-- campo es un objeto {valor, unidad, session_id, updated_at,
-- texto_original} (valor puede ser un numero o {min, max} si el usuario
-- dio un rango). Solo se guardan numeros que el usuario declaro
-- explicitamente; el motor nunca infiere cifras no dichas.
-- Aplicar manualmente en el SQL Editor de Supabase, igual que las
-- migraciones anteriores.

alter table projects
    add column if not exists numeros_proyecto jsonb not null default '{}'::jsonb;
