-- my_idea_034_enlace_proteccion.sql — Campaña "Mundos de protección" (P2):
-- EL ENLACE.
--
-- Una respuesta del plan de un mundo de protección apunta a la actividad del
-- NÚCLEO que protege, con la detección que la originó y su severidad en
-- palabras. Es la única migración de la campaña.
--
-- protege_item: referencia a un ítem del checklist (el del núcleo). NULL = la
-- respuesta es SISTÉMICA ("el negocio entero"), que es un valor declarado y no
-- un dato faltante. ON DELETE SET NULL a propósito: si un día se borra la
-- actividad protegida, la respuesta SOBREVIVE como sistémica en vez de irse con
-- ella; borrar una tarea del núcleo no puede llevarse por delante el trabajo de
-- protección que el usuario ya pagó. Retirar una tarea ('no_aplica') NO rompe el
-- enlace: la fila sigue existiendo y el chip lo dice.
--
-- deteccion: la frase que originó la respuesta ("depende de un solo proveedor").
-- Nace con el plan del mundo; jamás editable por PATCH (estructura del plan, no
-- percepción del usuario: mismo criterio que espera_externa).
--
-- probabilidad / dolor: la severidad EN PALABRAS. El vocabulario es cerrado y
-- viene del propio grafo (nodo "la matriz de colores te engaña"): nada de
-- puntajes numéricos ni colores que fingen precisión. Lo que el modelo devuelva
-- fuera del enum se descarta y queda NULL: no se aproxima.
--
-- CHECK nombrado (patrón 016/018/032/033) para que dbContract.test.ts lo parsee.

ALTER TABLE public.checklist_items ADD COLUMN IF NOT EXISTS protege_item uuid
  REFERENCES public.checklist_items(id) ON DELETE SET NULL;
ALTER TABLE public.checklist_items ADD COLUMN IF NOT EXISTS deteccion text;
ALTER TABLE public.checklist_items ADD COLUMN IF NOT EXISTS probabilidad text;
ALTER TABLE public.checklist_items ADD COLUMN IF NOT EXISTS dolor text;

ALTER TABLE public.checklist_items
  ADD CONSTRAINT checklist_items_probabilidad_check CHECK (probabilidad IN ('poco_probable', 'probable', 'muy_probable'));

ALTER TABLE public.checklist_items
  ADD CONSTRAINT checklist_items_dolor_check CHECK (dolor IN ('poco', 'bastante', 'mucho'));

-- El carril del Gantt y los chips buscan "las respuestas que protegen a X".
CREATE INDEX IF NOT EXISTS checklist_items_protege_item_idx
  ON public.checklist_items (protege_item) WHERE protege_item IS NOT NULL;
