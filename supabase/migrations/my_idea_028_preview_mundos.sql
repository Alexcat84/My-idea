-- my_idea_028_preview_mundos.sql
-- Fase 4.5: EL PREVIEW DE LOS MUNDOS (docs/PREVIEW_MUNDOS_PLAN.md). Los mundos
-- dejan de venderse con candado y pasan a probarse gratis: la entrevista y su
-- diagnostico son el escaparate; el PLAN es lo que se compra (3 creditos, a la
-- entrega). La fila de project_unlocks sigue siendo LA presencia del mundo en
-- la idea (el muro de filtros no cambia), pero su semantica evoluciona: nacer
-- ya no significa "pago la activacion", significa "el preview arranco".
--
-- La maquina de cuatro estados y donde vive cada uno:
--   [bloqueado]         no hay plan core (derivado, sin columna).
--   [abierto]           plan core existe, sin fila de unlock (derivado).
--   [diagnostico listo] fila con preview_at + resumen_md (el escaparate).
--   [plan comprado]     fila con plan_pagado_at (el mundo completo actual).
--
-- Notas:
-- * preview_session_id conserva LA sesion del preview: la compra genera el
--   plan DESDE ella sin re-entrevistar (un click al valor). ON DELETE SET NULL:
--   si la sesion se borrara, el resumen persiste igual (esta en la fila).
-- * resumen_md/resumen_at: el diagnostico persistido, releible siempre. La
--   "version" del resumen es su fecha (resumen_at); si el proyecto cambia de
--   ciclo, el derecho a re-preview se deriva comparando resumen_at contra el
--   plan core mas nuevo (sin columna extra).
-- * plan_pagado_at: el ancla del cobro A LA ENTREGA (ETAPA 2). En beta se
--   sella gratis al entregar el plan del mundo. creditos_pagados (016) queda
--   como registro historico del modelo viejo.
-- * Migracion con gracia: los mundos activados de antes que YA tienen plan de
--   su dominio quedan como comprados (plan_pagado_at = unlocked_at).
-- * Numeracion: 020-024 siguen RESERVADAS a cuentas-y-creditos.

ALTER TABLE public.project_unlocks ADD COLUMN preview_at timestamptz;
ALTER TABLE public.project_unlocks ADD COLUMN preview_session_id uuid
  REFERENCES public.sessions(id) ON DELETE SET NULL;
ALTER TABLE public.project_unlocks ADD COLUMN resumen_md text;
ALTER TABLE public.project_unlocks ADD COLUMN resumen_at timestamptz;
ALTER TABLE public.project_unlocks ADD COLUMN plan_pagado_at timestamptz;

COMMENT ON COLUMN public.project_unlocks.preview_at IS
  'Fase 4.5: cuando arranco el preview gratuito de este mundo. Un preview por '
  'mundo por proyecto; re-correrlo requiere compra o ciclo nuevo del proyecto.';
COMMENT ON COLUMN public.project_unlocks.preview_session_id IS
  'Fase 4.5: la sesion del preview. La compra genera el plan DESDE ella sin '
  're-entrevistar.';
COMMENT ON COLUMN public.project_unlocks.resumen_md IS
  'Fase 4.5: el diagnostico del preview (markdown), persistido y releible. '
  'Diagnostico, jamas plan encubierto (frontera del §3 del plan de fase).';
COMMENT ON COLUMN public.project_unlocks.plan_pagado_at IS
  'Fase 4.5: cuando se entrego el plan comprado del mundo (cobro a la entrega, '
  'ancla ETAPA 2). null = aun en escaparate.';

-- Migracion con gracia: unlock viejo con plan de su dominio = comprado.
UPDATE public.project_unlocks u
SET plan_pagado_at = u.unlocked_at
WHERE u.plan_pagado_at IS NULL
  AND EXISTS (
    SELECT 1
    FROM public.plans p
    JOIN public.sessions s ON s.id = p.session_id
    WHERE s.project_id = u.project_id
      AND p.dominio = u.dominio
  );
