-- ─────────────────────────────────────────────────────────────────────────────
-- Migración 031 · Calendario Nivel 1: sincronía de UNA VÍA con Google Calendar
--
-- Decisiones del fundador: calendario DEDICADO "My Idea" en la cuenta Google del
-- usuario (no su calendario principal), sincronía de UNA VÍA (app → Google).
-- Flujo OAuth PROPIO (no el login de Supabase) para pedir el scope de calendario
-- con acceso offline; guardamos el refresh_token CIFRADO (AES-256-GCM, el mismo
-- patrón del secreto TOTP, con GOOGLE_TOKEN_ENCRYPTION_KEY).
--
-- Como la 2FA (029): tablas INTERNAS — RLS encendido SIN policies. Solo el
-- service_role las toca, vía rutas de servidor; el token JAMÁS viaja al cliente.
--
-- Piezas:
--   · google_calendar_cuenta  — la conexión de Google del usuario (1:1), con el
--                               refresh_token cifrado y el id del calendario
--                               dedicado "My Idea".
--   · google_calendar_evento  — el mapa tarea → evento de Google, para poder
--                               actualizar/borrar sin adivinar (aparte de
--                               checklist_items: cada proceso en su carril).
-- ─────────────────────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS public.google_calendar_cuenta (
  user_id                uuid PRIMARY KEY REFERENCES auth.users (id) ON DELETE CASCADE,
  refresh_token_cifrado  text NOT NULL,
  calendar_id            text,
  scope                  text,
  -- el correo de Google conectado (para mostrar "conectado como …"); no es el
  -- de login necesariamente (puede haber entrado por correo+contraseña).
  email                  text,
  conectado_at           timestamptz NOT NULL DEFAULT now(),
  updated_at             timestamptz NOT NULL DEFAULT now()
);
COMMENT ON TABLE public.google_calendar_cuenta IS
  'Conexión de Google Calendar por usuario (Nivel 1, una vía). refresh_token_cifrado va cifrado por la app (AES-256-GCM, GOOGLE_TOKEN_ENCRYPTION_KEY). Interna: solo service_role.';
ALTER TABLE public.google_calendar_cuenta ENABLE ROW LEVEL SECURITY;
-- Sin policies: interna, solo service_role (el token nunca toca al cliente).

CREATE TABLE IF NOT EXISTS public.google_calendar_evento (
  item_id         uuid PRIMARY KEY REFERENCES public.checklist_items (id) ON DELETE CASCADE,
  user_id         uuid NOT NULL REFERENCES auth.users (id) ON DELETE CASCADE,
  event_id        text NOT NULL,
  sincronizado_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_gcal_evento_user
  ON public.google_calendar_evento (user_id);
COMMENT ON TABLE public.google_calendar_evento IS
  'Mapa tarea → evento de Google (para actualizar/borrar el evento correcto). Interna: solo service_role.';
ALTER TABLE public.google_calendar_evento ENABLE ROW LEVEL SECURITY;
-- Sin policies: interna, solo service_role.

DO $$ BEGIN RAISE NOTICE 'Migración 031 aplicada: google_calendar_cuenta + google_calendar_evento (Calendario Nivel 1, una vía).'; END $$;
