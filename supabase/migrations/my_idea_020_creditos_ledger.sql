-- ─────────────────────────────────────────────────────────────────────────────
-- NO APLICAR hasta aprobación del fundador (ETAPA 2).
-- Migración 020 · Ledger de créditos de My Idea
--
-- Patrón query_credits (I Ching 021_consumable_tokens) + tabla de transacciones
-- como caja de vidrio. 1 crédito = $1 USD (canon web/lib/precios.ts).
-- Balance-based, sin ciclos de suscripción. Nadie escribe estas tablas
-- directo: solo las RPC SECURITY DEFINER (service_role) de la 021–024.
-- ─────────────────────────────────────────────────────────────────────────────

-- Saldo por usuario.
CREATE TABLE IF NOT EXISTS public.credit_accounts (
  user_id         uuid PRIMARY KEY REFERENCES auth.users (id) ON DELETE CASCADE,
  creditos_total  integer NOT NULL DEFAULT 0,   -- saldo disponible
  creditos_usados integer NOT NULL DEFAULT 0,   -- histórico consumido
  total_comprado  integer NOT NULL DEFAULT 0,   -- histórico comprado (no cortesía)
  ultimo_pack     text    NOT NULL DEFAULT 'cortesia',
  updated_at      timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT credit_accounts_no_negativo CHECK (creditos_total >= 0 AND creditos_usados >= 0)
);

-- Cada movimiento (grant, consumo, refund): la caja de vidrio del saldo.
CREATE TABLE IF NOT EXISTS public.credit_transactions (
  id               bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id          uuid NOT NULL REFERENCES auth.users (id) ON DELETE CASCADE,
  delta            integer NOT NULL,             -- +grant / -consumo / +refund
  saldo_resultante integer NOT NULL,             -- saldo tras el movimiento
  tipo             text NOT NULL,                -- 'grant' | 'consumo' | 'refund'
  concepto         text,                         -- ConceptoPrecio o pack de compra / motivo
  origen           text,                         -- 'cortesia' | 'revenuecat' (solo grants)
  idempotency_key  text,                         -- webhook/acción: aplica una sola vez
  created_at       timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT credit_transactions_tipo_check   CHECK (tipo IN ('grant','consumo','refund')),
  CONSTRAINT credit_transactions_origen_check CHECK (origen IS NULL OR origen IN ('cortesia','revenuecat'))
);

-- Idempotencia global: una misma clave no puede aplicarse dos veces.
CREATE UNIQUE INDEX IF NOT EXISTS credit_transactions_idempotency_key
  ON public.credit_transactions (idempotency_key)
  WHERE idempotency_key IS NOT NULL;

CREATE INDEX IF NOT EXISTS credit_transactions_user_idx
  ON public.credit_transactions (user_id, created_at DESC);

-- RLS: cada quien LEE solo lo suyo; nadie MUTA directo (todo por RPC service-role).
ALTER TABLE public.credit_accounts     ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.credit_transactions ENABLE ROW LEVEL SECURITY;

-- (SELECT auth.uid()) evaluado una vez por consulta: patrón initplan (I Ching 060).
CREATE POLICY credit_accounts_own_select ON public.credit_accounts
  FOR SELECT USING (user_id = (SELECT auth.uid()));
CREATE POLICY credit_transactions_own_select ON public.credit_transactions
  FOR SELECT USING (user_id = (SELECT auth.uid()));
-- Sin policies de INSERT/UPDATE/DELETE: solo las RPC SECURITY DEFINER mutan.

DO $$ BEGIN RAISE NOTICE 'credit_accounts + credit_transactions creadas con RLS de solo-lectura del dueño.'; END $$;
