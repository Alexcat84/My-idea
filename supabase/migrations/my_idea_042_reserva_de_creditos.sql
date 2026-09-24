-- my_idea_042_reserva_de_creditos.sql — AUD-09 M25 (decisión del fundador,
-- 25 sep 2026): RESERVA DE CRÉDITOS al empezar la sesión, cobro al entregar,
-- liberación si la IA falla. La promesa visible no cambia (se verifica al
-- empezar, se cobra al final y solo si se entregó lo prometido).
--
-- El hueco que cierra: la verificación del inicio no apartaba nada. Con saldo
-- para UNA entrega se podían abrir varias sesiones en paralelo; todas pasaban la
-- verificación, todas se entregaban y solo la primera se cobraba (la "carrera
-- rara" duraba toda la generación, no un instante).
--
-- credit_reservas: una fila por entrega en curso, con la MISMA clave que su
-- cobro (`plan:{sessionId}`). El disponible es creditos_total menos las
-- reservas activas y no vencidas. Una reserva:
--   · nace 'activa' con un vencimiento (el llamador pasa los minutos): una
--     sesión abandonada no aparta créditos para siempre;
--   · pasa a 'cobrada' cuando su entrega se cobra, o a 'liberada' cuando la
--     entrega no se cobra (plan sin IA, carrera, fallo). Nada se borra.
-- La reserva NO mueve el saldo: el cobro sigue siendo consumir_creditos (021),
-- con su guard atómico y su idempotencia por la misma clave.
--
-- Solo service_role la toca (RLS sin políticas + REVOKE), como el ledger.

CREATE TABLE IF NOT EXISTS public.credit_reservas (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     uuid NOT NULL REFERENCES auth.users (id) ON DELETE CASCADE,
  clave       text NOT NULL,
  concepto    text NOT NULL,
  monto       integer NOT NULL,
  estado      text NOT NULL DEFAULT 'activa',
  expira_at   timestamptz NOT NULL,
  created_at  timestamptz NOT NULL DEFAULT now(),
  resuelta_at timestamptz,
  CONSTRAINT credit_reservas_clave_unica UNIQUE (clave),
  CONSTRAINT credit_reservas_monto_check CHECK (monto >= 0),
  CONSTRAINT credit_reservas_estado_check CHECK (estado IN ('activa', 'cobrada', 'liberada'))
);

CREATE INDEX IF NOT EXISTS credit_reservas_activas_idx
  ON public.credit_reservas (user_id, expira_at)
  WHERE estado = 'activa';

ALTER TABLE public.credit_reservas ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON public.credit_reservas FROM anon, authenticated;

-- Reserva atómica. Bloquea la cuenta del usuario (FOR UPDATE) para que dos
-- sesiones que reservan a la vez se ordenen: la segunda ve lo que apartó la
-- primera. Devuelve el disponible tras apartar, o -1 si no alcanza o no hay
-- cuenta. Idempotente por clave: reservar otra vez la misma clave la renueva
-- (monto y vencimiento) sin contarse a sí misma; una clave ya cobrada no aparta.
CREATE OR REPLACE FUNCTION public.reservar_creditos(
  p_user_id  uuid,
  p_clave    text,
  p_concepto text,
  p_monto    integer,
  p_minutos  integer
) RETURNS integer
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  v_total    integer;
  v_apartado integer;
  v_estado   text;
BEGIN
  IF p_monto IS NULL OR p_monto < 0 OR p_clave IS NULL OR p_minutos IS NULL OR p_minutos <= 0 THEN
    RETURN -1;
  END IF;

  SELECT creditos_total INTO v_total
  FROM public.credit_accounts
  WHERE user_id = p_user_id
  FOR UPDATE;
  IF NOT FOUND THEN
    RETURN -1;
  END IF;

  SELECT estado INTO v_estado
  FROM public.credit_reservas
  WHERE clave = p_clave AND user_id = p_user_id;
  IF v_estado = 'cobrada' THEN
    RETURN v_total;
  END IF;

  SELECT COALESCE(SUM(monto), 0) INTO v_apartado
  FROM public.credit_reservas
  WHERE user_id = p_user_id
    AND estado = 'activa'
    AND expira_at > now()
    AND clave <> p_clave;

  IF v_total - v_apartado < p_monto THEN
    RETURN -1;
  END IF;

  INSERT INTO public.credit_reservas (user_id, clave, concepto, monto, estado, expira_at)
  VALUES (p_user_id, p_clave, p_concepto, p_monto, 'activa', now() + make_interval(mins => p_minutos))
  ON CONFLICT (clave) DO UPDATE
    SET monto       = EXCLUDED.monto,
        concepto    = EXCLUDED.concepto,
        estado      = 'activa',
        expira_at   = EXCLUDED.expira_at,
        resuelta_at = NULL
    WHERE credit_reservas.user_id = EXCLUDED.user_id;

  RETURN v_total - v_apartado - p_monto;
END;
$$;

-- Resolver una reserva activa: 'cobrada' (su entrega se cobró) o 'liberada'
-- (no se cobró). Solo se mueve desde 'activa'; devuelve si movió algo.
CREATE OR REPLACE FUNCTION public.resolver_reserva(
  p_clave  text,
  p_estado text
) RETURNS boolean
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
  IF p_estado NOT IN ('cobrada', 'liberada') THEN
    RETURN false;
  END IF;
  UPDATE public.credit_reservas
  SET estado = p_estado,
      resuelta_at = now()
  WHERE clave = p_clave
    AND estado = 'activa';
  RETURN FOUND;
END;
$$;

REVOKE EXECUTE ON FUNCTION public.reservar_creditos(uuid, text, text, integer, integer)
  FROM PUBLIC, anon, authenticated;
REVOKE EXECUTE ON FUNCTION public.resolver_reserva(text, text)
  FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION public.reservar_creditos(uuid, text, text, integer, integer)
  TO service_role;
GRANT EXECUTE ON FUNCTION public.resolver_reserva(text, text)
  TO service_role;
