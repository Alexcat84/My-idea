-- my_idea_033_scheduler_estimacion.sql — Scheduler Inteligente (Fase 1): la
-- ESTIMACIÓN nace con el plan.
--
-- Al nacer todo plan nuevo (core o mundo), el modelo estima la BANDA de esfuerzo
-- de cada ítem del checklist (S/M/L/XL) + si arrastra ESPERA de terceros, por
-- MAYORÍA-DE-3 (tres corridas batch). Estas dos columnas guardan el resultado.
-- null = plan viejo sin estimación, o la estimación falló: el plan JAMÁS se
-- bloquea por esto (fallback declarado, ver lib/engine/estimacion.ts).
--
-- capacidad_semanal entra en project_modos (una por espacio) para que el
-- EMPAQUETADO de F2 sepa cuántas horas/semana reparte al calendario. La usa F2;
-- se crea ya para no fragmentar migraciones. null = sin declarar.
--
-- CHECK nombrado (patrón 016/018/032) para que dbContract.test.ts lo parsee:
--   checklist_items.banda            IN ('S','M','L','XL')  → dbContract BANDA
--   project_modos.capacidad_semanal  IN ('2-5','5-10','10-20','20+') → CAPACIDAD_SEMANAL
-- espera_externa es boolean puro (sin CHECK).

ALTER TABLE public.checklist_items ADD COLUMN IF NOT EXISTS banda text;
ALTER TABLE public.checklist_items ADD COLUMN IF NOT EXISTS espera_externa boolean;

ALTER TABLE public.checklist_items
  ADD CONSTRAINT checklist_items_banda_check CHECK (banda IN ('S', 'M', 'L', 'XL'));

ALTER TABLE public.project_modos ADD COLUMN IF NOT EXISTS capacidad_semanal text;

ALTER TABLE public.project_modos
  ADD CONSTRAINT project_modos_capacidad_semanal_check CHECK (capacidad_semanal IN ('2-5', '5-10', '10-20', '20+'));
