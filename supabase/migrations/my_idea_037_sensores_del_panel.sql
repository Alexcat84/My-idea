-- my_idea_037_sensores_del_panel.sql — los dos sensores del panel de nodos.
--
-- Por qué corre el reloj: la telemetría solo acumula desde que el sensor
-- existe. Un sensor que nace después del primer tester no puede contar lo que
-- ese tester hizo. La meta es que los dos estén vivos ANTES del primer tester.
--
-- Diseño y costo en docs/SENSORES_DEL_PANEL.md. Ambos son de costo CERO por
-- plan: b1 reusa la autodeclaración que el redactor ya emite desde la Fase 3.1,
-- y b2 añade una escritura al lado de la que ya existe.

-- ---------------------------------------------------------------------------
-- b1. El ítem del checklist y su nodo de origen.
--
-- NULLABLE Y SIN DEFAULT, a propósito. Los ítems que ya existen quedan en NULL,
-- que se lee como "nació antes del sensor". Con '{}' por default los planes
-- viejos mentirían diciendo que no tuvieron origen, y esa mentira sería
-- indistinguible de un plan nuevo cuyo redactor omitió la autodeclaración.
--
-- text[] y no una tabla puente: la pregunta siempre va del ítem hacia sus
-- nodos, nunca al revés, así que el arreglo la resuelve sin un JOIN.
-- ---------------------------------------------------------------------------
ALTER TABLE public.checklist_items
  ADD COLUMN nodos_origen text[];

COMMENT ON COLUMN public.checklist_items.nodos_origen IS
  'Los node_id que el redactor autodeclaró para la ETAPA de este ítem (no para el ítem: esa granularidad no existe). NULL = nació antes del sensor o el redactor no autodeclaró. Nunca se guardan ids que verificarProcedenciaEtapas marcó como alucinados.';

-- ---------------------------------------------------------------------------
-- b2. El DIARIO de visitas a nodos.
--
-- project_nodes se queda EXACTAMENTE como está: es el ESTADO, y su
-- UNIQUE(project_id, node_id) es lo que hace que nodosCubiertos() devuelva un
-- conjunto limpio, que el motor usa como lista de exclusión del recorrido.
-- Quitarlo para poder contar visitas habría obligado a deduplicar en cada
-- consulta de cobertura.
--
-- Así que el diario va aparte. Estado y diario son cosas distintas, y
-- mezclarlas fue lo que creó el límite: hoy se sabe cuándo se pisó un nodo por
-- PRIMERA vez, y nada más.
--
-- SIN UNIQUE: aquí cada visita es una fila, y ese es justamente el punto.
-- ---------------------------------------------------------------------------
CREATE TABLE public.node_visits (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id uuid NOT NULL REFERENCES public.projects(id) ON DELETE CASCADE,
  session_id uuid NOT NULL REFERENCES public.sessions(id) ON DELETE CASCADE,
  node_id text NOT NULL,
  tipo text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX node_visits_node_idx ON public.node_visits(node_id);
CREATE INDEX node_visits_project_idx ON public.node_visits(project_id);

-- RLS espejo de project_nodes: el dueño del proyecto, y nadie más.
ALTER TABLE public.node_visits ENABLE ROW LEVEL SECURITY;

CREATE POLICY node_visits_own ON public.node_visits
  FOR ALL
  USING (EXISTS (
    SELECT 1 FROM public.projects p
    WHERE p.id = node_visits.project_id AND p.user_id = auth.uid()
  ));

COMMENT ON TABLE public.node_visits IS
  'El DIARIO: una fila por visita, sin UNIQUE. project_nodes es el ESTADO (un nodo, una vez por proyecto) y no se toca. Esto desbloquea lo que hoy es imposible: cuántas veces se vuelve a un nodo, en qué sesión, cuánto tarda alguien entre pisarlo y cosecharlo, y qué nodos se visitan y NUNCA se cosechan.';
