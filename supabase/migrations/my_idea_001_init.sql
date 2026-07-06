-- ============================================================================
-- MY IDEA · Migration 001_init
-- Esquema inicial, trasplantado de los patrones probados en producción de
-- The Original I Ching App (misma jerarquía de dos niveles, mismo modelo de
-- tokens consumibles por balance, mismo RLS por user_id).
--
-- Mapeo de patrones I Ching -> My Idea:
--   consultation_sessions  -> projects        (el contenedor de largo plazo)
--   consultations          -> sessions        (cada interacción, con posición)
--   pattern_analyses       -> estado_vivo     (síntesis acumulativa comprimida,
--                             aquí como columna del proyecto porque se
--                             sobreescribe, no se acumula en filas)
--   query_credits (021)    -> query_credits   (idéntico: balance de tokens)
--   session_position       -> session_position (orden de seguimientos)
--   random_public_id       -> reservado para compartir planes en el futuro
-- ============================================================================

-- El contenedor de largo plazo: un proyecto = una idea del usuario
CREATE TABLE public.projects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  titulo TEXT,                                  -- generado por Haiku desde la entrada
  entrada_original TEXT NOT NULL,               -- el primer mensaje del usuario, intacto
  estado_vivo TEXT,                             -- síntesis comprimida (300-500 tokens),
                                                -- se SOBREESCRIBE al cierre de cada sesión
  fase_actual TEXT NOT NULL DEFAULT 'ideacion'
    CHECK (fase_actual IN ('ideacion','validacion','planificacion','ejecucion')),
  session_count INTEGER NOT NULL DEFAULT 0,
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active','archived')),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Cada interacción: gratuita, inicial o de seguimiento
CREATE TABLE public.sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID NOT NULL REFERENCES public.projects(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  session_position INTEGER NOT NULL DEFAULT 1,  -- orden dentro del proyecto
  tipo TEXT NOT NULL CHECK (tipo IN ('gratuito','inicial','seguimiento')),
  mensaje_entrada TEXT NOT NULL,                -- lo que el usuario escribió al abrir
  puerta_entrada TEXT,                          -- node_id por el que entró al grafo
  ruta JSONB NOT NULL DEFAULT '[]',             -- [{node_id, tipo: conversado|silencioso}]
  costo_usd NUMERIC(8,4) NOT NULL DEFAULT 0,    -- costo real de API, del contador
  presupuesto_excedido BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  closed_at TIMESTAMPTZ
);

-- Nodos cubiertos por proyecto (memoria de "no repetir lo básico")
CREATE TABLE public.project_nodes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID NOT NULL REFERENCES public.projects(id) ON DELETE CASCADE,
  session_id UUID NOT NULL REFERENCES public.sessions(id) ON DELETE CASCADE,
  node_id TEXT NOT NULL,                        -- id del nodo del grafo (no FK: el
                                                -- grafo vive en archivo, no en DB)
  tipo TEXT NOT NULL CHECK (tipo IN ('conversado','silencioso','cosechado')),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE (project_id, node_id)                  -- un nodo cuenta una sola vez por proyecto
);

-- Salidas entregadas al usuario
CREATE TABLE public.plans (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id UUID NOT NULL REFERENCES public.sessions(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  etiqueta TEXT NOT NULL CHECK (etiqueta IN ('organizador','inicial','completo','seguimiento')),
  contenido_md TEXT NOT NULL,
  conceptos_usados INTEGER NOT NULL DEFAULT 0,
  familias_cubiertas JSONB NOT NULL DEFAULT '[]',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tokens consumibles por balance (idéntico al modelo post-021 del I Ching)
CREATE TABLE public.query_credits (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  credits_total INTEGER NOT NULL DEFAULT 0,     -- balance disponible
  credits_used INTEGER NOT NULL DEFAULT 0,
  total_purchased INTEGER NOT NULL DEFAULT 0,
  last_pack TEXT NOT NULL DEFAULT 'free',
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE UNIQUE INDEX query_credits_user_id_key ON public.query_credits(user_id);

-- Índices de acceso frecuente
CREATE INDEX projects_user_idx ON public.projects(user_id, updated_at DESC);
CREATE INDEX sessions_project_idx ON public.sessions(project_id, session_position);
CREATE INDEX project_nodes_project_idx ON public.project_nodes(project_id);
CREATE INDEX plans_session_idx ON public.plans(session_id);

-- RLS: cada usuario ve solo lo suyo (patrón I Ching)
ALTER TABLE public.projects       ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.sessions       ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.project_nodes  ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.plans          ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.query_credits  ENABLE ROW LEVEL SECURITY;

CREATE POLICY projects_own ON public.projects
  FOR ALL USING ((SELECT auth.uid()) = user_id) WITH CHECK ((SELECT auth.uid()) = user_id);
CREATE POLICY sessions_own ON public.sessions
  FOR ALL USING ((SELECT auth.uid()) = user_id) WITH CHECK ((SELECT auth.uid()) = user_id);
CREATE POLICY project_nodes_own ON public.project_nodes
  FOR ALL USING (EXISTS (SELECT 1 FROM public.projects p
                         WHERE p.id = project_id AND p.user_id = (SELECT auth.uid())));
CREATE POLICY plans_own ON public.plans
  FOR ALL USING ((SELECT auth.uid()) = user_id) WITH CHECK ((SELECT auth.uid()) = user_id);
CREATE POLICY query_credits_read_own ON public.query_credits
  FOR SELECT USING ((SELECT auth.uid()) = user_id);
-- Escritura de créditos SOLO vía funciones SECURITY DEFINER (grant/consume),
-- como en I Ching 024: el cliente jamás escribe su propio balance.
