-- my_idea_016_mundos.sql
-- Fase 3.5: mundos HSEQ detras de flags. Sin fila en project_unlocks, el
-- dominio no existe para el motor (los filtros de dominio son el muro).
--
-- Notas de verificacion (mismas reglas que la 015):
-- * Policy en la forma real de my_idea_001 (EXISTS + (SELECT auth.uid())),
--   no la del patch.
-- * Los CHECK de sessions.dominio y plans.dominio van como ADD CONSTRAINT
--   nombrado (no inline en ADD COLUMN): asi los parsea dbContract.test.ts
--   y asi se pueden relajar por nombre cuando haya mas dominios.

CREATE TABLE public.project_unlocks (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id uuid NOT NULL REFERENCES public.projects(id) ON DELETE CASCADE,
  dominio text NOT NULL
    CHECK (dominio IN ('quality', 'health_safety', 'environmental')),
  creditos_pagados int NOT NULL DEFAULT 0, -- stub pre-pagos; Stripe llega despues
  unlocked_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (project_id, dominio)
);

ALTER TABLE public.project_unlocks ENABLE ROW LEVEL SECURITY;

-- Espejo exacto del patron de project_nodes_own (my_idea_001:103-105).
CREATE POLICY project_unlocks_own ON public.project_unlocks
  FOR ALL USING (EXISTS (SELECT 1 FROM public.projects p
                         WHERE p.id = project_id AND p.user_id = (SELECT auth.uid())));

-- Procedencia de dominio en sesiones y planes (core por defecto, packs al
-- activarse un mundo). checklist_items.dominio ya existe desde la 015.
ALTER TABLE public.sessions
  ADD COLUMN dominio text NOT NULL DEFAULT 'core';
ALTER TABLE public.sessions
  ADD CONSTRAINT sessions_dominio_check CHECK (dominio IN ('core', 'quality', 'health_safety', 'environmental'));

ALTER TABLE public.plans
  ADD COLUMN dominio text NOT NULL DEFAULT 'core';
ALTER TABLE public.plans
  ADD CONSTRAINT plans_dominio_check CHECK (dominio IN ('core', 'quality', 'health_safety', 'environmental'));
