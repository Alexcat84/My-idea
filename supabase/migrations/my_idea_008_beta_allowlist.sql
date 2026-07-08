-- ============================================================================
-- MY IDEA · Migration 008_beta_allowlist
-- Fase 3.0: la web queda detras de una allowlist de beta (magic link por
-- email, Supabase Auth). No hay pagos en esta fase; query_credits ya
-- existe desde la migracion 001 (identico al modelo del I Ching) y se usa
-- como "sesiones de cortesia" para el usuario beta -- otorgar
-- credits_total al aprobar el email, consumir con las funciones
-- SECURITY DEFINER existentes.
-- ============================================================================

CREATE TABLE public.beta_allowlist (
  email TEXT PRIMARY KEY,
  invitado_por TEXT,
  notas TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Solo el service role (proxy.ts / route handlers server-side) puede leer
-- esta tabla -- nunca expuesta directo al cliente. RLS habilitado sin
-- ninguna policy = nadie con anon/authenticated puede tocarla; solo la
-- service role key (que salta RLS) puede.
ALTER TABLE public.beta_allowlist ENABLE ROW LEVEL SECURITY;

-- Semilla: el propio fundador, para la primera sesion en vivo por la web
-- (prueba de paridad 5 del prompt de Fase 3.0). Agregar mas emails aqui
-- o directo en el SQL Editor conforme se invite a los 10 emprendedores.
INSERT INTO public.beta_allowlist (email, invitado_por, notas)
VALUES ('alexcatbaster@gmail.com', 'fundador', 'usuario cero de la Fase 3.0')
ON CONFLICT (email) DO NOTHING;
