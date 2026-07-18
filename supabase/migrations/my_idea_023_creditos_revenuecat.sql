-- ─────────────────────────────────────────────────────────────────────────────
-- NO APLICAR hasta aprobación del fundador (ETAPA 2 · paso b: pasarelas).
-- Migración 023 · Idempotencia de webhooks RevenueCat + grant idempotente
--
-- RevenueCat es el puente ÚNICO hacia las pasarelas (Stripe en web, Play en
-- móvil): la app nunca habla con ellas directo. Patrón I Ching 005 (tabla de
-- eventos con event_hash UNIQUE) + 039 (dedup + grant en UNA transacción, para
-- que un fallo de base jamás produzca doble crédito).
--
-- Esta migración define el esquema pero las PASARELAS NO SE ACTIVAN aquí:
-- el endpoint /api/account/sync-billing y sus claves llegan en ETAPA 2/b, tras
-- validar la mecánica con créditos de cortesía.
-- ─────────────────────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS public.revenuecat_webhook_events (
  id           bigserial PRIMARY KEY,
  event_hash   text NOT NULL UNIQUE,
  event_type   text,
  app_user_id  uuid,
  processed_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE public.revenuecat_webhook_events ENABLE ROW LEVEL SECURITY;
-- Sin policies: interna, solo service_role.

CREATE INDEX IF NOT EXISTS revenuecat_webhook_events_user_idx
  ON public.revenuecat_webhook_events (app_user_id, processed_at DESC);

-- Registra el evento (event_hash UNIQUE) y otorga en la MISMA transacción.
-- Devuelve 'granted' (evento nuevo, créditos otorgados) o 'already_processed'.
CREATE OR REPLACE FUNCTION public.otorgar_creditos_idempotente(
  p_event_hash text,
  p_event_type text,
  p_user_id    uuid,
  p_monto      integer,
  p_pack       text
) RETURNS text
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
  -- unique_violation (23505) si el evento ya fue procesado.
  INSERT INTO public.revenuecat_webhook_events (event_hash, event_type, app_user_id)
  VALUES (p_event_hash, p_event_type, p_user_id);

  -- Solo eventos nuevos llegan aquí. El event_hash viaja como idempotency_key
  -- del grant: doble blindaje contra doble crédito.
  PERFORM public.otorgar_creditos(p_user_id, p_monto, 'revenuecat', p_event_hash, p_pack);

  RETURN 'granted';
EXCEPTION
  WHEN unique_violation THEN
    RETURN 'already_processed';
END;
$$;

REVOKE EXECUTE ON FUNCTION public.otorgar_creditos_idempotente(text, text, uuid, integer, text)
  FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION public.otorgar_creditos_idempotente(text, text, uuid, integer, text)
  TO service_role;

DO $$ BEGIN RAISE NOTICE 'revenuecat_webhook_events + otorgar_creditos_idempotente creadas (pasarelas NO activadas).'; END $$;
