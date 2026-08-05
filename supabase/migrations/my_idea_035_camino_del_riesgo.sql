-- my_idea_035_camino_del_riesgo.sql — Mundos de protección (P3): EL CAMINO.
--
-- La anatomía canónica del risk register (y del propio grafo, nodo "cuatro
-- caminos ante un riesgo"): ante cada detección se ELIGE un camino, y esa
-- elección es un dato del registro, no una frase implícita en la respuesta.
-- Decisión del fundador (6 ago 2026): barato hoy, retrofit doloroso mañana.
--
-- camino: lo emite el enlazador junto a la detección y la severidad, contra el
-- vocabulario CERRADO del nodo canónico. Fuera del enum o sin confianza → NULL
-- (se calla, patrón de la severidad: jamás se aproxima). Nace con el plan del
-- mundo; jamás editable por PATCH (estructura del plan, no percepción del
-- usuario: mismo criterio que protege_item y espera_externa).
--
-- CHECK nombrado (patrón 016/018/032/033/034) para que dbContract.test.ts lo
-- parsee.

ALTER TABLE public.checklist_items ADD COLUMN IF NOT EXISTS camino text;

ALTER TABLE public.checklist_items
  ADD CONSTRAINT checklist_items_camino_check CHECK (camino IN ('evitar', 'mitigar', 'transferir', 'aceptar'));
