-- my_idea_038_siembra_beta_en_el_ledger.sql: siembra_beta admitida en el
-- origen del ledger, como el manual decia desde el principio.
--
-- EL MOTIVO, Y ES UNA CONTRADICCION QUE LLEVABA VIVA DESDE LA 020.
--
-- La casa declara `siembra_beta` como un origen VIVO, y lo declara en TRES
-- sitios, con instrucciones y todo:
--
--   docs/BETA_CUENTAS_README.md:152-165: trae el SQL completo con
--     `p_origen => 'siembra_beta'`, afirma que "deja rastro en
--     credit_transactions (tipo grant)", y su tabla de estado (linea 173)
--     lo marca VIVA (§2.f).
--   web/lib/creditos.ts:24: "el fundador siembra creditos A MANO
--     (RPC otorgar_creditos, origen 'siembra_beta')".
--   web/lib/cuentas.ts:69: lo repite y remite al README.
--
-- Y EL ESQUEMA LO RECHAZABA. La 020 escribio:
--
--   CONSTRAINT credit_transactions_origen_check
--     CHECK (origen IS NULL OR origen IN ('cortesia','revenuecat'))
--
-- de modo que la llamada documentada muere SIEMPRE con 23514
-- (check constraint violation). Comprobado en vivo el 4 sep 2026 contra la
-- base real: la RPC devolvio 23514 y la fila rechazada era
-- (..., 60, 62, grant, siembra_beta, siembra_beta, ...). El saldo no se movio
-- y no se escribio ni una fila: el rollback fue limpio.
--
-- O SEA QUE LA SIEMBRA MANUAL NUNCA PUDO FUNCIONAR, y ninguna prueba lo
-- ejercitaba, asi que nadie se entero hasta que el vuelo se quedo sin creditos
-- y hubo que sembrarlos.
--
-- ESTA MIGRACION ES ADITIVA Y NO HACE NADA MAS: anade `siembra_beta` a los
-- valores admitidos. NO toca datos, NO toca la restriccion de `tipo`, NO toca
-- el indice de idempotencia y NO cambia el comportamiento de ningun origen ya
-- existente. `total_comprado` sigue moviendose SOLO con 'revenuecat', tal como
-- la 021 lo escribio y como el README declara en su linea 165.
--
-- Decision del fundador, 4 sep 2026, sesion con credencial (opcion 1 de las
-- tres que se le trajeron: ensanchar la restriccion, en vez de mentir en el
-- ledger poniendo 'cortesia' o de perder la etiqueta poniendo NULL).

ALTER TABLE public.credit_transactions
  DROP CONSTRAINT IF EXISTS credit_transactions_origen_check;

ALTER TABLE public.credit_transactions
  ADD CONSTRAINT credit_transactions_origen_check
  CHECK (origen IS NULL OR origen IN ('cortesia','revenuecat','siembra_beta'));

-- El comentario de la columna, para que la proxima lectura del esquema no
-- tenga que ir al README a enterarse.
COMMENT ON COLUMN public.credit_transactions.origen IS
  '''cortesia'' | ''revenuecat'' | ''siembra_beta'' (solo grants). siembra_beta = siembra manual del fundador (RPC otorgar_creditos), admitida desde la 038.';
