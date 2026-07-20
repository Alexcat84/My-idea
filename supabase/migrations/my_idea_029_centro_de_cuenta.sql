-- ─────────────────────────────────────────────────────────────────────────────
-- Migración 029 · Centro de cuenta: 2FA (TOTP + email) y borrado honesto
--
-- Réplica del esquema probado del I Ching (001/007/011/016/030/046), adaptada:
-- allá las columnas 2FA viven en public.users; aquí no existe tabla de perfil,
-- así que nacen en user_seguridad (1:1 con auth.users). Todo es interno:
-- RLS encendido SIN policies (solo service_role vía rutas; el secreto TOTP
-- va cifrado AES-256-GCM por la app y jamás toca al cliente).
--
-- Piezas:
--   · user_seguridad             — estado 2FA por usuario (método totp/email)
--   · two_factor_recovery_codes  — 8 códigos de rescate (hash bcrypt)
--   · two_factor_attempts        — intentos (candado 5 fallos/15 min) y la
--                                  PRUEBA por sesión (session_id: nuestra
--                                  adaptación del gate, verificable en server)
--   · two_factor_email_codes     — códigos de un solo uso por correo
--   · reset_2fa_recovery_codes() — delete+insert atómico (I Ching 030)
--   · cortesia_email_log         — huella por hash de email al BORRAR cuenta:
--                                  borrar-y-volver no re-otorga los 20
--                                  (patrón trial_email_log, I Ching 046)
-- ─────────────────────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS public.user_seguridad (
  user_id             uuid PRIMARY KEY REFERENCES auth.users (id) ON DELETE CASCADE,
  two_factor_enabled  boolean NOT NULL DEFAULT false,
  two_factor_method   text,
  totp_secret         text,
  totp_verified_at    timestamptz,
  totp_last_used_step bigint,
  created_at          timestamptz NOT NULL DEFAULT now(),
  updated_at          timestamptz NOT NULL DEFAULT now()
);
-- CHECK nombrado vía ALTER (regla de la 018: así lo parsea dbContract.test).
-- NULL pasa el CHECK solo (semántica SQL): método null = 2FA sin configurar.
ALTER TABLE public.user_seguridad
  ADD CONSTRAINT user_seguridad_two_factor_method_check
  CHECK (two_factor_method IN ('totp', 'email'));
COMMENT ON TABLE public.user_seguridad IS
  'Estado 2FA por usuario (equivale a las columnas 2FA de public.users del I Ching). totp_secret va cifrado por la app (AES-256-GCM, TOTP_ENCRYPTION_KEY).';
ALTER TABLE public.user_seguridad ENABLE ROW LEVEL SECURITY;
-- Sin policies: interna, solo service_role.

CREATE TABLE IF NOT EXISTS public.two_factor_recovery_codes (
  id         uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id    uuid NOT NULL REFERENCES auth.users (id) ON DELETE CASCADE,
  code_hash  text NOT NULL,
  used_at    timestamptz,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_2fa_recovery_user
  ON public.two_factor_recovery_codes (user_id);
ALTER TABLE public.two_factor_recovery_codes ENABLE ROW LEVEL SECURITY;
-- Sin policies: interna, solo service_role.

CREATE TABLE IF NOT EXISTS public.two_factor_attempts (
  id         uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id    uuid NOT NULL REFERENCES auth.users (id) ON DELETE CASCADE,
  ip_address text NOT NULL DEFAULT 'unknown',
  success    boolean NOT NULL,
  -- Adaptación nuestra (sesión por cookies, no bearer): el desafío superado
  -- se registra con el session_id del JWT de Supabase; las rutas sensibles
  -- exigen un success de ESTA sesión. Prueba en servidor, no en el cliente.
  session_id text,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_2fa_attempts_user_created
  ON public.two_factor_attempts (user_id, created_at DESC);
ALTER TABLE public.two_factor_attempts ENABLE ROW LEVEL SECURITY;
-- Sin policies: interna, solo service_role.

CREATE TABLE IF NOT EXISTS public.two_factor_email_codes (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     uuid NOT NULL REFERENCES auth.users (id) ON DELETE CASCADE,
  code_hash   text NOT NULL,
  expires_at  timestamptz NOT NULL,
  consumed_at timestamptz,
  created_at  timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_2fa_email_codes_user_created
  ON public.two_factor_email_codes (user_id, created_at DESC);
ALTER TABLE public.two_factor_email_codes ENABLE ROW LEVEL SECURITY;
-- Sin policies: interna, solo service_role.

-- Rotación atómica de códigos de rescate (I Ching 030): jamás una ventana
-- sin códigos ni mezcla de tandas.
CREATE OR REPLACE FUNCTION public.reset_2fa_recovery_codes(
  p_user_id      uuid,
  p_hashed_codes text[]
) RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
  DELETE FROM public.two_factor_recovery_codes WHERE user_id = p_user_id;
  INSERT INTO public.two_factor_recovery_codes (user_id, code_hash)
  SELECT p_user_id, unnest(p_hashed_codes);
END;
$$;
REVOKE EXECUTE ON FUNCTION public.reset_2fa_recovery_codes(uuid, text[])
  FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION public.reset_2fa_recovery_codes(uuid, text[])
  TO service_role;

-- La huella de la cortesía que sobrevive al borrado de la cuenta (el log por
-- user_id se va con la cascada). SIN FK a auth.users: ese es el punto.
-- Hash sha256 (hex) del email en minúsculas, calculado por la app.
CREATE TABLE IF NOT EXISTS public.cortesia_email_log (
  email_hash text PRIMARY KEY,
  created_at timestamptz NOT NULL DEFAULT now()
);
COMMENT ON TABLE public.cortesia_email_log IS
  'Huella (sha256 del email) de cortesías ya dadas, escrita al borrar la cuenta. Borrar-y-volver no re-otorga los 20 (patrón trial_email_log del I Ching, 046).';
ALTER TABLE public.cortesia_email_log ENABLE ROW LEVEL SECURITY;
-- Sin policies: interna, solo service_role.

DO $$ BEGIN RAISE NOTICE 'Migración 029 aplicada: user_seguridad + 2FA (recovery/attempts/email) + reset_2fa_recovery_codes + cortesia_email_log.'; END $$;
