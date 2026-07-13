-- ─────────────────────────────────────────────────────────────────────────────
-- NO APLICAR hasta aprobación del fundador (ETAPA 2).
-- Migración 022 · Créditos de cortesía de beta — 20 por invitado, UNA sola vez
--
-- Patrón init_free_user + user_trial_log (I Ching 022): el otorgamiento de
-- cortesía se registra en un log inmutable por user_id; imposible re-otorgar
-- aunque se borre y recree la cuenta de créditos. Decisión del fundador:
-- 20 créditos por invitado de beta, origen 'cortesia' inmutable, persisten
-- intactos cuando llegue el cobro real y conviven con los comprados.
-- ─────────────────────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS public.beta_courtesy_log (
  user_id    uuid PRIMARY KEY REFERENCES auth.users (id) ON DELETE CASCADE,
  granted_at timestamptz NOT NULL DEFAULT now()
);
COMMENT ON TABLE public.beta_courtesy_log IS
  'Marca única de que el usuario ya recibió los créditos de cortesía de beta. Bloquea re-otorgamiento aunque credit_accounts se borre.';

ALTER TABLE public.beta_courtesy_log ENABLE ROW LEVEL SECURITY;
-- Sin policies: interna, solo service_role (vía RPC) la toca.

-- Otorga la cortesía una sola vez. Idempotente: segunda llamada NO re-otorga.
CREATE OR REPLACE FUNCTION public.otorgar_cortesia(
  p_user_id uuid,
  p_monto   integer DEFAULT 20
) RETURNS integer
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  v_rows      integer;
  v_remaining integer;
BEGIN
  -- Registrar la cortesía. Si ya existía, ROW_COUNT = 0 → no re-otorga.
  INSERT INTO public.beta_courtesy_log (user_id)
  VALUES (p_user_id)
  ON CONFLICT (user_id) DO NOTHING;
  GET DIAGNOSTICS v_rows = ROW_COUNT;

  IF v_rows = 0 THEN
    SELECT creditos_total INTO v_remaining
    FROM public.credit_accounts WHERE user_id = p_user_id;
    RETURN COALESCE(v_remaining, 0);  -- ya tenía cortesía: sin cambios
  END IF;

  -- Primera vez: crear o sumar el saldo de cortesía.
  INSERT INTO public.credit_accounts (user_id, creditos_total, ultimo_pack)
  VALUES (p_user_id, p_monto, 'cortesia')
  ON CONFLICT (user_id) DO UPDATE
    SET creditos_total = credit_accounts.creditos_total + p_monto,
        updated_at     = now()
  RETURNING creditos_total INTO v_remaining;

  INSERT INTO public.credit_transactions
    (user_id, delta, saldo_resultante, tipo, concepto, origen)
  VALUES
    (p_user_id, p_monto, v_remaining, 'grant', 'cortesia_beta', 'cortesia');

  RETURN v_remaining;
END;
$$;

REVOKE EXECUTE ON FUNCTION public.otorgar_cortesia(uuid, integer)
  FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION public.otorgar_cortesia(uuid, integer)
  TO service_role;

DO $$ BEGIN RAISE NOTICE 'beta_courtesy_log + otorgar_cortesia creadas (20 créditos, una sola vez).'; END $$;
