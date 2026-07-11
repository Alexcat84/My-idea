-- my_idea_015_checklist_items.sql
-- Fase 3.3: el bucle de checklist. Un item por paso accionable del plan,
-- derivado deterministicamente por derivarChecklist() al persistir el plan.
-- dominio: 'core' hoy; los mundos HSEQ (migration 016) reutilizan esta misma
-- tabla -- UNA fuente de verdad, vistas filtradas por dominio.
--
-- Nota de verificacion (regla del plan: "si 001 difiere, mandan las de 001"):
-- el patch original proponia USING (project_id IN (SELECT ...)); la forma
-- real de my_idea_001 (project_nodes_own) es EXISTS + (SELECT auth.uid()),
-- asi que la policy de abajo espeja ESA forma. updated_at sin trigger,
-- igual que 001: lo actualiza la app en cada PATCH.

CREATE TABLE public.checklist_items (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id uuid NOT NULL REFERENCES public.projects(id) ON DELETE CASCADE,
  plan_id uuid NOT NULL REFERENCES public.plans(id) ON DELETE CASCADE,
  dominio text NOT NULL DEFAULT 'core',
  etapa int NOT NULL,
  orden int NOT NULL,
  texto text NOT NULL,
  destacado boolean NOT NULL DEFAULT false, -- true = item "Esta semana"
  estado text NOT NULL DEFAULT 'pendiente'
    CHECK (estado IN ('pendiente', 'empezado', 'a_medias', 'hecho')),
  nota text,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX checklist_items_project_idx ON public.checklist_items (project_id, plan_id, etapa, orden);

ALTER TABLE public.checklist_items ENABLE ROW LEVEL SECURITY;

-- Espejo exacto del patron de project_nodes_own (my_idea_001:103-105).
CREATE POLICY checklist_items_own ON public.checklist_items
  FOR ALL USING (EXISTS (SELECT 1 FROM public.projects p
                         WHERE p.id = project_id AND p.user_id = (SELECT auth.uid())));
