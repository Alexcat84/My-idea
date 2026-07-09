-- ============================================================================
-- MY IDEA · Migration 014_pack_clicks
-- Fase 3.2 (brief seccion 4): telemetria de demanda de los mundos HSEQ.
-- En beta los tres packs son SOLO fachada (tarjetas con candado desde un
-- catalogo estatico); cada click en un candado se registra aqui -- oro
-- para decidir con datos cual pack se lanza primero (v1.3, post-beta).
-- ============================================================================

CREATE TABLE public.pack_clicks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  project_id UUID REFERENCES public.projects(id) ON DELETE SET NULL,
  pack TEXT NOT NULL CHECK (pack IN ('quality','health_safety','environmental')),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX pack_clicks_pack_idx ON public.pack_clicks(pack, created_at DESC);

-- RLS sin policies: solo la service role escribe/lee (la ruta verifica al
-- usuario autenticado ANTES de insertar con el cliente admin); el
-- navegador jamas toca esta tabla directo.
ALTER TABLE public.pack_clicks ENABLE ROW LEVEL SECURITY;
