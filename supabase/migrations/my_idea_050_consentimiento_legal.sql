-- my_idea_050_consentimiento_legal.sql — EL REGISTRO DE LA ACEPTACIÓN DE LOS TEXTOS LEGALES
-- (decisión del fundador, 7 oct 2026: consentimiento versionado como en The Original I Ching, migración 027
-- user_legal_acceptances y su pantalla auth/complete-legal).
--
-- Una fila por cuenta REAL y por versión aceptada de los Términos y la Privacidad. La versión tiene una sola
-- fuente (docs/legal/version.json, que scripts/sync_legal_web.py publica en web/lib/legal/textos.ts) y la app
-- vuelve a pedir la aceptación cuando la versión vigente no coincide con la última aceptada. La identidad
-- invisible (el invitado anónimo de proxy.ts) jamás escribe aquí: la web sigue abierta, sin muro.
--
-- CORRECCIÓN DEL FUNDADOR (7 oct 2026, después de aplicada; sin SQL nuevo): el modal se retiró. La aceptación
-- se pide en el primer envío de datos y la guarda TODA identidad que envía datos, también la invisible (su fila de
-- auth.users: esta tabla ya la admite); la adopción (web/lib/cuentas.ts) copia esas filas a la cuenta. El texto
-- de arriba y el COMMENT de la tabla ("Solo cuentas reales") quedan como estaban en la base: son historia.
--
-- Columnas:
--   · version       la versión aceptada (p. ej. '2026-10-07'); UNIQUE con user_id: aceptar dos veces la misma
--                   versión no duplica (la ruta trata el 23505 como hecho).
--   · huella_textos sha256 de los textos versionados en esa versión (los de docs/legal/version.json): prueba
--                   de QUÉ texto exacto se aceptó, aunque el registro de versiones cambie después.
--   · idioma_texto  el idioma del texto que la persona tuvo delante ('es' o 'fr': los textos legales existen
--                   en esos dos; cualquier otro idioma lee el español).
--   · motivo        'primera_aceptacion' (la cuenta no tenía ninguna) o 'nueva_version' (ya aceptó una
--                   anterior y la versión cambió).
--   · aceptada_at   la hora del SERVIDOR al guardar (nunca la del navegador).
--
-- Borrado de la cuenta: ON DELETE CASCADE. "Borrar la cuenta borra de verdad" (migración 044, regla C28): el
-- registro de aceptación es un dato personal ligado a la cuenta y se va con ella. Si un profesional dictamina
-- que la prueba del consentimiento debe conservarse un plazo tras el borrado, eso queda POR VERIFICAR
-- (docs/legal/INVENTARIO_DATOS.md) y sería una migración aparte.
--
-- RLS: cada quien LEE solo lo suyo; nadie escribe directo desde el cliente. Solo la ruta del servidor
-- (/api/cuenta/consentimiento, con service_role) inserta, después de validar que la versión es la vigente.
-- Append-only: sin UPDATE ni DELETE (solo la cascada del borrado de la cuenta).
-- El bloque 050 de my_idea_check_migraciones.sql la confirma ANTES (MISSING) y DESPUÉS (OK).

CREATE TABLE IF NOT EXISTS public.aceptaciones_legales (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id       uuid NOT NULL REFERENCES auth.users (id) ON DELETE CASCADE,
  version       text NOT NULL,
  huella_textos text NOT NULL,
  idioma_texto  text NOT NULL,
  motivo        text NOT NULL,
  aceptada_at   timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT aceptaciones_legales_version_unica UNIQUE (user_id, version)
);
-- CHECK nombrados vía ALTER (regla de la 018: así los parsea dbContract.test).
ALTER TABLE public.aceptaciones_legales
  ADD CONSTRAINT aceptaciones_legales_idioma_texto_check
  CHECK (idioma_texto IN ('es', 'fr'));
ALTER TABLE public.aceptaciones_legales
  ADD CONSTRAINT aceptaciones_legales_motivo_check
  CHECK (motivo IN ('primera_aceptacion', 'nueva_version'));
ALTER TABLE public.aceptaciones_legales
  ADD CONSTRAINT aceptaciones_legales_huella_check
  CHECK (huella_textos ~ '^[0-9a-f]{64}$');

CREATE INDEX IF NOT EXISTS aceptaciones_legales_usuario_idx
  ON public.aceptaciones_legales (user_id, aceptada_at DESC);

COMMENT ON TABLE public.aceptaciones_legales IS
  'Aceptacion de los Terminos y la Privacidad por version (decision del fundador, 7 oct 2026). Solo cuentas reales; se borra con la cuenta (ON DELETE CASCADE). Escribe solo service_role.';

ALTER TABLE public.aceptaciones_legales ENABLE ROW LEVEL SECURITY;
-- Supabase concede ALL por defecto a anon y authenticated en las tablas nuevas (TRUNCATE incluido, que RLS no
-- frena): se retira todo y authenticated recupera solo la lectura, que la política limita a sus filas.
-- (Aplicada el 7 oct 2026. La primera version aplicada solo quitaba INSERT, UPDATE y DELETE a authenticated; el
-- fundador corrio despues estas dos lineas aparte, y el verificador 050 lo comprueba.)
REVOKE ALL ON public.aceptaciones_legales FROM anon, authenticated;
GRANT SELECT ON public.aceptaciones_legales TO authenticated;

-- (SELECT auth.uid()) evaluado una vez por consulta: patrón initplan (como la 020).
DROP POLICY IF EXISTS aceptaciones_legales_own_select ON public.aceptaciones_legales;
CREATE POLICY aceptaciones_legales_own_select ON public.aceptaciones_legales
  FOR SELECT TO authenticated USING (user_id = (SELECT auth.uid()));
-- Sin policies de INSERT/UPDATE/DELETE: solo la ruta del servidor (service_role) inserta.

DO $$ BEGIN RAISE NOTICE 'aceptaciones_legales creada con RLS de solo-lectura del dueno.'; END $$;
