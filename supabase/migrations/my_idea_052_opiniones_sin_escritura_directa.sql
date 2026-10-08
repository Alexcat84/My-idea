-- my_idea_052_opiniones_sin_escritura_directa.sql — LAS OPINIONES SOLO SE ESCRIBEN POR LA RUTA DEL SERVIDOR
-- (revisión de seguridad del commit de opiniones, 8 oct 2026).
--
-- La 051 dejaba a `authenticated` insertar directo en public.opiniones (sus columnas públicas, con la política
-- opiniones_own_insert). Eso se saltaba todo lo que la ruta /api/opiniones garantiza:
--   · el invitado de respaldo de proxy.ts (correo @invitado.my-idea.local) NO es anónimo en su token: pasaba la
--     política y opinaba sin cuenta real;
--   · los topes (30 escrituras y 5 comentarios por día) y la regla de "solo si la tarjeta tocaba" (sin ella, el
--     seguimiento admite filas sin fin);
--   · que lo valorado sea un plan de esa misma cuenta.
-- Desde aquí nadie escribe directo desde el cliente (el patrón de la 050): solo la ruta del servidor, con service_role,
-- después de validar la sesión. "Cada usuario solo inserta lo suyo" sigue valiendo: la ruta inserta siempre con el id
-- de la sesión, nunca con uno que mande el navegador. La lectura de lo propio (sin el contexto interno) no cambia.
-- El bloque 052 de my_idea_check_migraciones.sql la confirma ANTES (MISSING) y DESPUÉS (OK).

DROP POLICY IF EXISTS opiniones_own_insert ON public.opiniones;
REVOKE INSERT ON public.opiniones FROM authenticated;
-- Las columnas: un REVOKE de tabla no retira los permisos concedidos por columna en la 051.
REVOKE INSERT (user_id, tipo, objeto_id, valoracion, motivo, texto, idioma) ON public.opiniones FROM authenticated;

DO $$ BEGIN RAISE NOTICE 'opiniones: sin escritura directa del cliente (solo la ruta del servidor).'; END $$;
