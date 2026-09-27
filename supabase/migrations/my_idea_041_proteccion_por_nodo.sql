-- my_idea_041_proteccion_por_nodo.sql — AUD-09 M15 (decisión del fundador,
-- 25 sep 2026): LA PROTECCIÓN APUNTA AL NODO DE LA TAREA.
--
-- protege_item (034) guarda el id de la tarea del núcleo protegida, y ese id es
-- de UN ciclo: al abrir un ciclo nuevo el núcleo renace con ids nuevos y la
-- respuesta quedaba huérfana sin aviso. protege_nodos guarda los nodos del grafo
-- de la tarea protegida (su nodos_origen, migración 037) al momento del enlace;
-- con ellos la app resuelve contra el plan VIGENTE: si el id sigue vivo manda el
-- id, si no, la tarea vigente que comparte nodos; si ninguna, la pantalla lo dice
-- en claro. protege_item NO se toca: es el ancla exacta dentro del ciclo.
--
-- Límite declarado: nodos_origen es por etapa, así que en un ciclo nuevo la
-- resolución es exacta a nivel de etapa. NULL = enlace nacido antes de esta
-- migración sin nodos que heredar, o respuesta sistémica: se resuelve solo por id.

ALTER TABLE public.checklist_items ADD COLUMN IF NOT EXISTS protege_nodos text[];

COMMENT ON COLUMN public.checklist_items.protege_nodos IS
  'AUD-09 M15: nodos del grafo de la tarea del nucleo protegida (su nodos_origen al enlazar). Resuelve la proteccion contra el plan vigente cuando protege_item es de un ciclo anterior.';

-- Relleno: los enlaces que ya existen heredan los nodos de la tarea a la que
-- apuntan hoy (mientras protege_item siga resolviendo a una fila).
UPDATE public.checklist_items c
   SET protege_nodos = p.nodos_origen
  FROM public.checklist_items p
 WHERE p.id = c.protege_item
   AND c.protege_nodos IS NULL
   AND p.nodos_origen IS NOT NULL;
