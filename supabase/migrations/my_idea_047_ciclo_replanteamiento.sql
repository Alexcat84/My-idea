-- my_idea_047_ciclo_replanteamiento.sql — Ciclo de replanteamiento, FASE 2
-- (decisiones del fundador, 27 sep 2026; docs/producto/CICLO_REPLANTEAMIENTO.md).
--
-- 1. plans.etiqueta admite 'replanteamiento': la entrada "Replantear mi camino"
--    deja su plan con su propia etiqueta, distinta de 'seguimiento' (que queda
--    para "Profundizar mi plan"), para que la bitácora, el Expediente y la
--    Historia cuenten cada ciclo con su nombre.
--
-- 2. checklist_items.heredado_de: al replantear, lo marcado "me sigue sirviendo"
--    pasa al plan nuevo COMO HECHO. La fila nueva apunta a la tarea original para
--    que el análisis y la bitácora no la cuenten dos veces (la original sigue
--    bajo su plan viejo). NULL = tarea nacida en su propio plan (todas las de
--    antes de esta migración). Si la original se borra, el enlace se suelta.

ALTER TABLE public.plans DROP CONSTRAINT IF EXISTS plans_etiqueta_check;
ALTER TABLE public.plans ADD CONSTRAINT plans_etiqueta_check
  CHECK (etiqueta IN ('organizador','inicial','completo','seguimiento','reporte_numeros','replanteamiento'));

ALTER TABLE public.checklist_items
  ADD COLUMN IF NOT EXISTS heredado_de uuid REFERENCES public.checklist_items(id) ON DELETE SET NULL;

COMMENT ON COLUMN public.checklist_items.heredado_de IS
  '047: la tarea original de un plan anterior que esta fila trae como hecha al replantear. NULL = nacida en su plan.';
