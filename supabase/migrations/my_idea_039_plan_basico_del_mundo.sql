-- my_idea_039_plan_basico_del_mundo.sql: la marca propia del plan básico de un mundo.
--
-- Por qué existe (AUD-09, decisión del fundador del 25 sep 2026): UN SELLO DE
-- PAGO SOLO EXISTE SI HUBO PAGO. Un plan armado sin la redacción con IA (el
-- ensamblado sin narrar, cuando la conversación llegó a su tope de trabajo) se
-- entrega gratis. Antes ese plan escribía plan_pagado_at, así que el mundo
-- quedaba "comprado" sin que nadie hubiera pagado. Ahora el plan básico escribe
-- SOLO esta columna, y el mundo ofrece "Generar el plan completo", que es una
-- sesión nueva que se cobra solo si la IA entrega.
--
-- NULLABLE Y SIN DEFAULT: NULL = el mundo nunca recibió un plan básico. Si
-- después llega el plan completo (pagado), esta marca se conserva como historia
-- y plan_pagado_at manda en el estado del mundo.
--
-- Aditiva: no toca ninguna columna existente. La app tolera que aún no esté
-- aplicada (el intento de escribirla se registra fuerte en el log y el plan se
-- entrega igual), pero sin ella el mundo no puede ofrecer el plan completo.

ALTER TABLE public.project_unlocks
  ADD COLUMN plan_basico_at timestamptz;

COMMENT ON COLUMN public.project_unlocks.plan_basico_at IS
  'Cuándo este mundo recibió un plan básico (armado sin IA, no cobrado). NULL = nunca. No es un sello de pago: el pago lo sella solo plan_pagado_at.';
