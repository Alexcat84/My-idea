-- my_idea_045_historial_creditos_anonimo.sql — HISTORIAL DE CRÉDITOS AL BORRAR
-- LA CUENTA (decisión del fundador, 27 sep 2026).
--
-- Antes, el ON DELETE CASCADE de credit_transactions (020) se llevaba el
-- historial entero con la cuenta. Ahora queda ANÓNIMO, igual que los
-- reembolsos (044) y los eventos de pago: el monto (delta, con su tipo:
-- compra, consumo o devolución) y la fecha, sin vínculo con la persona. La
-- ruta /api/cuenta/eliminar pone en NULL user_id, saldo_resultante, concepto,
-- origen e idempotency_key ANTES de borrar la cuenta (una fila con user_id
-- NULL no la alcanza el CASCADE). Los registros fiscales de las ventas los
-- conserva el procesador de pagos.
--
-- La RLS (credit_transactions_own_select: user_id = auth.uid()) ya deja
-- invisibles para todos las filas anónimas. El índice único de
-- idempotency_key es parcial (WHERE idempotency_key IS NOT NULL): los NULL no
-- chocan.

ALTER TABLE public.credit_transactions ALTER COLUMN user_id DROP NOT NULL;
ALTER TABLE public.credit_transactions ALTER COLUMN saldo_resultante DROP NOT NULL;

COMMENT ON COLUMN public.credit_transactions.user_id IS
  '045: NULL = movimiento de una cuenta borrada, anonimizado (queda monto, tipo y fecha).';
