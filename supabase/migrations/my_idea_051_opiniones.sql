-- my_idea_051_opiniones.sql — LAS OPINIONES DE LOS USUARIOS (decisión del fundador, 8 oct 2026, antes de la beta).
--
-- Una fila por opinión de una CUENTA REAL (la identidad invisible de proxy.ts jamás opina):
--   · las preguntas de un clic en los momentos clave: al recibir el plan, un plan de mundo, una profundización o un
--     replanteamiento ("¿Qué tal salió tu plan?"), y de vez en cuando en el seguimiento ("¿Qué tal va tu idea?");
--   · "Comentarios y sugerencias" de la cuenta: lo que la persona piensa de la app, con valoración opcional.
--
-- Columnas:
--   · tipo        'plan' (el primer plan del núcleo), 'plan_mundo', 'profundizacion', 'replanteamiento',
--                 'seguimiento' o 'general' (Comentarios y sugerencias). Lo decide el SERVIDOR a partir del plan.
--   · objeto_id   lo valorado: el plan (sus cuatro tipos), la idea ('seguimiento'); NULL en 'general'. Sin FK a
--                 propósito: si la idea se borra, la opinión se queda sin vínculo (ver proyecto_id).
--   · valoracion  'malo', 'bueno' o 'excelente'. NULL = cerró la tarjeta sin responder (cuenta como hecha: no se
--                 vuelve a preguntar) o comentario sin valoración.
--   · motivo      solo con 'malo': 'no_es_correcto', 'no_aplica', 'confuso' u 'otro'.
--   · texto       lo que la persona escribió (opcional; hasta 2000 caracteres).
--   · idioma      el idioma de la pantalla al opinar (los once de la app).
--   · contexto    INTERNO, la persona NUNCA lo ve: la etiqueta del plan, su número de ciclo (la versión), el mundo y
--                 los nodos usados en esa entrevista. Lo arma el servidor; el cliente no puede escribirlo ni leerlo.
--   · proyecto_id la idea de la opinión (interno). ON DELETE SET NULL: borrar una idea no borra lo que la persona
--                 opinó de la app, pero corta el vínculo con la idea.
--   · created_at / updated_at  hora del servidor; updated_at se llena si después de "Malo" la persona añade el
--                 motivo o el texto (lo completa la ruta del servidor, dentro de la hora siguiente).
--
-- Borrado de la cuenta: ON DELETE CASCADE desde auth.users, y además la ruta /api/cuenta/eliminar las borra
-- explícitamente antes de borrar la cuenta (borradoCompleto.test.ts lo prueba).
--
-- Seguridad por filas (decisión del fundador): cada usuario solo INSERTA y LEE lo suyo, y la identidad invisible no
-- inserta. Encima, permisos por COLUMNA: authenticated no lee ni escribe `contexto` ni `proyecto_id` (el contexto
-- interno no se ve y no se puede falsear). La app escribe por la ruta del servidor (service_role), que valida la
-- sesión, comprueba que el plan es de esa persona y arma el contexto. Sin UPDATE ni DELETE para el cliente.
-- El bloque 051 de my_idea_check_migraciones.sql la confirma ANTES (MISSING) y DESPUÉS (OK).
--
-- REVISIÓN DE SEGURIDAD (8 oct 2026, después de aplicada): la inserción directa de authenticated se saltaba los
-- topes, la regla de "solo si la tarjeta tocaba" y dejaba opinar al invitado de respaldo. La retira la 052; lo de
-- abajo queda como se aplicó: es historia.

CREATE TABLE IF NOT EXISTS public.opiniones (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     uuid NOT NULL REFERENCES auth.users (id) ON DELETE CASCADE,
  tipo        text NOT NULL,
  objeto_id   uuid,
  valoracion  text,
  motivo      text,
  texto       text,
  idioma      text NOT NULL,
  contexto    jsonb NOT NULL DEFAULT '{}'::jsonb,
  proyecto_id uuid REFERENCES public.projects (id) ON DELETE SET NULL,
  created_at  timestamptz NOT NULL DEFAULT now(),
  updated_at  timestamptz
);
-- CHECK nombrados vía ALTER (regla de la 018: así los parsea dbContract.test).
ALTER TABLE public.opiniones
  ADD CONSTRAINT opiniones_tipo_check
  CHECK (tipo IN ('plan', 'plan_mundo', 'profundizacion', 'replanteamiento', 'seguimiento', 'general'));
ALTER TABLE public.opiniones
  ADD CONSTRAINT opiniones_valoracion_check
  CHECK (valoracion IN ('malo', 'bueno', 'excelente'));
ALTER TABLE public.opiniones
  ADD CONSTRAINT opiniones_motivo_check
  CHECK (motivo IN ('no_es_correcto', 'no_aplica', 'confuso', 'otro'));
ALTER TABLE public.opiniones
  ADD CONSTRAINT opiniones_idioma_check
  CHECK (idioma IN ('es', 'en', 'fr', 'pt', 'de', 'it', 'ja', 'zh', 'ko', 'ar', 'hi'));
ALTER TABLE public.opiniones
  ADD CONSTRAINT opiniones_motivo_solo_malo_check
  CHECK (motivo IS NULL OR valoracion = 'malo');
ALTER TABLE public.opiniones
  ADD CONSTRAINT opiniones_texto_largo_check
  CHECK (texto IS NULL OR char_length(texto) <= 2000);
ALTER TABLE public.opiniones
  ADD CONSTRAINT opiniones_objeto_check
  CHECK ((tipo = 'general') = (objeto_id IS NULL));

-- Una sola vez por plan: la segunda inserción del mismo plan revienta 23505 y la ruta la trata como hecha.
CREATE UNIQUE INDEX IF NOT EXISTS opiniones_una_por_plan_idx
  ON public.opiniones (user_id, objeto_id)
  WHERE tipo IN ('plan', 'plan_mundo', 'profundizacion', 'replanteamiento');
CREATE INDEX IF NOT EXISTS opiniones_usuario_idx ON public.opiniones (user_id, created_at DESC);
CREATE INDEX IF NOT EXISTS opiniones_fecha_idx ON public.opiniones (created_at DESC);

COMMENT ON TABLE public.opiniones IS
  'Opiniones de las cuentas reales (decision del fundador, 8 oct 2026). contexto y proyecto_id son internos: el cliente no los lee ni los escribe. Se borra con la cuenta (ON DELETE CASCADE).';

ALTER TABLE public.opiniones ENABLE ROW LEVEL SECURITY;
-- Supabase concede ALL por defecto a anon y authenticated en las tablas nuevas (TRUNCATE incluido, que RLS no
-- frena): se retira todo y authenticated recupera solo lo suyo, columna por columna.
REVOKE ALL ON public.opiniones FROM anon, authenticated;
GRANT SELECT (id, user_id, tipo, objeto_id, valoracion, motivo, texto, idioma, created_at, updated_at)
  ON public.opiniones TO authenticated;
GRANT INSERT (user_id, tipo, objeto_id, valoracion, motivo, texto, idioma)
  ON public.opiniones TO authenticated;

-- (SELECT auth.uid()) evaluado una vez por consulta: patrón initplan (como la 020).
DROP POLICY IF EXISTS opiniones_own_select ON public.opiniones;
CREATE POLICY opiniones_own_select ON public.opiniones
  FOR SELECT TO authenticated USING (user_id = (SELECT auth.uid()));
DROP POLICY IF EXISTS opiniones_own_insert ON public.opiniones;
CREATE POLICY opiniones_own_insert ON public.opiniones
  FOR INSERT TO authenticated WITH CHECK (
    user_id = (SELECT auth.uid())
    AND COALESCE(((SELECT auth.jwt()) ->> 'is_anonymous')::boolean, false) = false
  );
-- Sin policies de UPDATE ni DELETE: completar el motivo lo hace la ruta del servidor (service_role); borrar, la
-- cascada de la cuenta y la ruta de eliminar la cuenta.

DO $$ BEGIN RAISE NOTICE 'opiniones creada con RLS (inserta y lee lo suyo; contexto interno oculto).'; END $$;
