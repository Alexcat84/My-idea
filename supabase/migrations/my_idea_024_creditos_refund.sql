-- ─────────────────────────────────────────────────────────────────────────────
-- NO APLICAR hasta aprobación del fundador (ETAPA 2).
-- Migración 024 · Reembolso de créditos + auditoría
--
-- Regla sagrada del fundador: NADIE pierde créditos por un fallo del sistema.
-- Compensación atómica de consumir_creditos ante fallo POST-cobro. Patrón
-- I Ching 072_refund_token.
--   - monto > 0 → reembolso real: creditos_total += monto, creditos_usados -= monto (piso 0)
--   - monto = 0 → registro de auditoría sin reembolso (caso de entrega parcial)
--
-- El modelo de "cobrar a la entrega" (decisión del fundador) hace este refund
-- raro: solo se necesita si el cobro se aplicó pero la entrega se perdió después
-- (p. ej. respuesta HTTP perdida tras descontar). El fallo A MITAD no cobra.
-- ─────────────────────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS public.credit_refund_log (
  id         bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id    uuid NOT NULL,
  monto      integer NOT NULL,
  motivo     text,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS credit_refund_log_user_idx
  ON public.credit_refund_log (user_id, created_at DESC);

ALTER TABLE public.credit_refund_log ENABLE ROW LEVEL SECURITY;
-- Sin policies: interna, solo service_role.

CREATE OR REPLACE FUNCTION public.reembolsar_creditos(
  p_user_id uuid,
  p_monto   integer,
  p_motivo  text DEFAULT NULL
) RETURNS integer
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  v_remaining integer;
BEGIN
  -- Guard: un monto negativo consumiría créditos por esta vía.
  IF p_monto IS NULL OR p_monto < 0 THEN
    RETURN -1;
  END IF;

  -- monto = 0: registro de auditoría sin reembolso.
  IF p_monto = 0 THEN
    INSERT INTO public.credit_refund_log (user_id, monto, motivo)
    VALUES (p_user_id, 0, p_motivo);
    RETURN 0;
  END IF;

  UPDATE public.credit_accounts
  SET creditos_total  = creditos_total + p_monto,
      creditos_usados = GREATEST(0, creditos_usados - p_monto),
      updated_at      = now()
  WHERE user_id = p_user_id
  RETURNING creditos_total INTO v_remaining;

  IF NOT FOUND THEN
    RETURN -1;
  END IF;

  INSERT INTO public.credit_transactions
    (user_id, delta, saldo_resultante, tipo, concepto)
  VALUES
    (p_user_id, p_monto, v_remaining, 'refund', p_motivo);

  INSERT INTO public.credit_refund_log (user_id, monto, motivo)
  VALUES (p_user_id, p_monto, p_motivo);

  RETURN v_remaining;
END;
$$;

REVOKE EXECUTE ON FUNCTION public.reembolsar_creditos(uuid, integer, text)
  FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION public.reembolsar_creditos(uuid, integer, text)
  TO service_role;

DO $$ BEGIN RAISE NOTICE 'credit_refund_log + reembolsar_creditos creadas y aseguradas a service_role.'; END $$;
