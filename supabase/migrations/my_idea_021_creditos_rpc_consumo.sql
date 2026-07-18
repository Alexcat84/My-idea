-- ─────────────────────────────────────────────────────────────────────────────
-- NO APLICAR hasta aprobación del fundador (ETAPA 2).
-- Migración 021 · RPCs de consumo y otorgamiento (atómicas, service-role-only)
--
-- El consumo ocurre EN LA BASE, no en el código de la app: patrón consume_token
-- (I Ching 032_atomic_token_consumption) — deducción en un solo UPDATE con guard
-- de saldo que previene carreras. Devuelve el saldo restante, o -1 si no alcanza.
-- Ambas RPC son idempotentes por idempotency_key (una acción aplica una sola vez).
-- ─────────────────────────────────────────────────────────────────────────────

-- Consumo atómico. Devuelve saldo restante, o -1 si saldo insuficiente / sin cuenta.
CREATE OR REPLACE FUNCTION public.consumir_creditos(
  p_user_id        uuid,
  p_concepto       text,
  p_monto          integer,
  p_idempotency_key text DEFAULT NULL
) RETURNS integer
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  v_remaining integer;
  v_prev      integer;
BEGIN
  IF p_monto IS NULL OR p_monto < 0 THEN
    RETURN -1;
  END IF;

  -- Idempotencia: si la clave ya se aplicó, devolver su saldo sin re-cobrar.
  IF p_idempotency_key IS NOT NULL THEN
    SELECT saldo_resultante INTO v_prev
    FROM public.credit_transactions
    WHERE idempotency_key = p_idempotency_key
    LIMIT 1;
    IF FOUND THEN
      RETURN v_prev;
    END IF;
  END IF;

  -- Deducción atómica: el guard de saldo en el WHERE impide gastar de más
  -- aunque dos pestañas lleguen a la vez (una gana, la otra no encuentra fila).
  UPDATE public.credit_accounts
  SET creditos_total  = creditos_total - p_monto,
      creditos_usados = creditos_usados + p_monto,
      updated_at      = now()
  WHERE user_id = p_user_id
    AND creditos_total >= p_monto
  RETURNING creditos_total INTO v_remaining;

  IF NOT FOUND THEN
    RETURN -1;  -- saldo insuficiente o cuenta inexistente
  END IF;

  INSERT INTO public.credit_transactions
    (user_id, delta, saldo_resultante, tipo, concepto, idempotency_key)
  VALUES
    (p_user_id, -p_monto, v_remaining, 'consumo', p_concepto, p_idempotency_key);

  RETURN v_remaining;
END;
$$;

-- Otorgamiento (compra o ajuste). SIEMPRE suma. Idempotente por clave.
CREATE OR REPLACE FUNCTION public.otorgar_creditos(
  p_user_id        uuid,
  p_monto          integer,
  p_origen         text,
  p_idempotency_key text DEFAULT NULL,
  p_pack           text DEFAULT NULL
) RETURNS integer
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  v_remaining integer;
  v_prev      integer;
BEGIN
  IF p_monto IS NULL OR p_monto <= 0 THEN
    RETURN -1;
  END IF;

  IF p_idempotency_key IS NOT NULL THEN
    SELECT saldo_resultante INTO v_prev
    FROM public.credit_transactions
    WHERE idempotency_key = p_idempotency_key
    LIMIT 1;
    IF FOUND THEN
      RETURN v_prev;
    END IF;
  END IF;

  INSERT INTO public.credit_accounts (user_id, creditos_total, total_comprado, ultimo_pack)
  VALUES (
    p_user_id,
    p_monto,
    CASE WHEN p_origen = 'revenuecat' THEN p_monto ELSE 0 END,
    COALESCE(p_pack, p_origen)
  )
  ON CONFLICT (user_id) DO UPDATE
    SET creditos_total = credit_accounts.creditos_total + p_monto,
        total_comprado = credit_accounts.total_comprado
                         + CASE WHEN p_origen = 'revenuecat' THEN p_monto ELSE 0 END,
        ultimo_pack    = COALESCE(p_pack, credit_accounts.ultimo_pack),
        updated_at     = now()
  RETURNING creditos_total INTO v_remaining;

  INSERT INTO public.credit_transactions
    (user_id, delta, saldo_resultante, tipo, concepto, origen, idempotency_key)
  VALUES
    (p_user_id, p_monto, v_remaining, 'grant', p_pack, p_origen, p_idempotency_key);

  RETURN v_remaining;
END;
$$;

-- Seguridad: ejecutable SOLO por service_role (patrón I Ching 035).
REVOKE EXECUTE ON FUNCTION public.consumir_creditos(uuid, text, integer, text)
  FROM PUBLIC, anon, authenticated;
REVOKE EXECUTE ON FUNCTION public.otorgar_creditos(uuid, integer, text, text, text)
  FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION public.consumir_creditos(uuid, text, integer, text)
  TO service_role;
GRANT EXECUTE ON FUNCTION public.otorgar_creditos(uuid, integer, text, text, text)
  TO service_role;

DO $$ BEGIN RAISE NOTICE 'consumir_creditos + otorgar_creditos creadas y aseguradas a service_role.'; END $$;
