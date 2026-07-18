-- my_idea_027_tus_numeros_vivo.sql
-- FASE B (canon 14): Tus Numeros deja de ser un reporte de tiro unico y se
-- vuelve un TABLERO VIVO. Dos cosas nuevas que persistir:
--
-- 1. El historial de VERSIONES de cifras. Cada vez que el usuario corre o
--    recalcula Tus Numeros con un juego de cifras, se guarda una version con
--    su fecha. La historia NO se reescribe: corregir las cifras crea una
--    version nueva y archiva la narracion vieja, nunca la borra. La pantalla
--    muestra "calculado con tus cifras del [fecha]" mas el historial.
--    projects.numeros_proyecto sigue siendo el juego VIGENTE de cifras (lo
--    leen la entrevista y el seguimiento, migration 003); cada fila de
--    project_numeros_versiones es un snapshot de lo que se calculo y narro en
--    ese momento.
--
-- 2. El cobro de UNA vez por idea. tus_numeros_activado_at marca que Tus
--    Numeros ya se pago para esta idea. Es un ancla de la ETAPA 2 (rama
--    cuentas-y-creditos): el credito paga el trabajo del motor, y activar el
--    potenciador es ese trabajo. El recalculo determinista y la re-narracion
--    posteriores son gratis (el limite diario de re-narracion es el freno, no
--    un cobro); los 2 creditos (precios.ts: tus_numeros) se cobran UNA vez, al
--    activar, no por corrida. Null = no activado todavia. En beta no se cobra;
--    la columna existe para que la ETAPA 2 la cablee sin otra migracion.
--
-- Numeracion: se saltan 020-024, RESERVADAS al frente de cuentas y creditos
-- (rama cuentas-y-creditos, sin aplicar). Esta es la 027, tras 025/026.
--
-- Notas de verificacion (mismas reglas que 016/018):
-- * Sin CHECK nuevos: tipo_oferta aqui es un snapshot de projects.tipo_oferta,
--   que ya trae su CHECK en origen (migration 007). No entra a dbContract.
-- * La policy de project_numeros_versiones espeja project_bitacora
--   (my_idea_018:61-63) / project_nodes_own (my_idea_001:103-105).

-- 1. Ancla de cobro una vez por idea (ETAPA 2).
ALTER TABLE public.projects ADD COLUMN tus_numeros_activado_at timestamptz;

-- 2. Historial append-only de versiones de cifras con su narracion archivada.
--    numeros      snapshot de numeros_proyecto usado en este calculo
--    tipo_oferta  el molde con que se calculo (texto libre, ver nota)
--    calculo      el ReporteCalculado determinista + palancas de esa corrida
--                 (null si aun no se calculo; lo llena la ruta de Tus Numeros)
--    narracion    el reporte narrado en markdown (null si solo hubo recalculo
--                 determinista sin re-narrar, ej. tope diario alcanzado)
--    narracion_at cuando se (re)narro; null si esta version no tiene narracion
CREATE TABLE public.project_numeros_versiones (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id uuid NOT NULL REFERENCES public.projects(id) ON DELETE CASCADE,
  numeros jsonb NOT NULL,
  tipo_oferta text,
  calculo jsonb,
  narracion text,
  narracion_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX project_numeros_versiones_project_idx
  ON public.project_numeros_versiones (project_id, created_at);

ALTER TABLE public.project_numeros_versiones ENABLE ROW LEVEL SECURITY;

-- Espejo exacto del patron de project_bitacora (my_idea_018:61-63).
CREATE POLICY project_numeros_versiones_own ON public.project_numeros_versiones
  FOR ALL USING (EXISTS (SELECT 1 FROM public.projects p
                         WHERE p.id = project_id AND p.user_id = (SELECT auth.uid())));
