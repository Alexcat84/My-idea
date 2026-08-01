# Calendario — sincronía con Google (ARCHIVADO, para retomar)

**Estado:** construido, probado en compilación, y **retirado a propósito** a favor
de la **suscripción universal (webcal)**. El código NO está en `main` actual: vive
en el historial de git. La **migración 031 sí quedó aplicada** en el Supabase de
producción (tablas vacías, inofensivas). Este documento deja todo listo para
**retomarlo** sin re-investigar.

> **Por qué se retiró.** El fundador decidió sincronizar con **cualquier**
> calendario de cualquier teléfono (Google, Apple, Outlook…), no solo Google. El
> único mecanismo **universal** es ICS por **suscripción** (webcal): el teléfono
> se suscribe una vez a una URL en vivo y se mantiene al día solo. El API de
> Google da sincronía casi instantánea **pero solo para Google** y exige OAuth +
> verificación de Google. Se eligió lo universal; Google quedó como opción
> "instantánea solo-Google" para el futuro.

---

## Dónde vive el código (para recuperarlo)

| Qué | Commit | Rama |
| --- | --- | --- |
| Implementación completa de Google (Nivel 1) | **`b3c74b2`** | `main` (release) |
| Misma implementación (fuente) | `fb67c67` + fix `7f8a758` | `staging` |
| Migración 031 (tablas) | `c8f9b77` | `staging` |
| **Remoción** de Google + llegada de la suscripción (opción B) | `b5cdc6f` | `staging` → `main` |

**Recuperar los archivos** (sobre la rama que sea):

```bash
git checkout b3c74b2 -- \
  web/app/api/calendar/google \
  web/lib/calendarioSync.ts \
  web/lib/googleCalendar.ts \
  web/lib/cifrado.ts \
  web/app/ui/SincroniaGoogle.tsx
```

Y volver a cablear los **hooks de sincronía** (se quitaron de las mutaciones):
en `web/app/api/project/[id]/checklist/route.ts` y `.../mover-fecha/route.ts`,
tras la escritura en BD, un `after(() => sincronizarIds(...))` **envuelto en
try/catch** (si no, los tests de ruta fallan con *"after outside request scope"*).
Ver esos hooks tal como estaban en `b3c74b2`.

---

## Archivos que componían la implementación

- `web/app/api/calendar/google/conectar/route.ts` — inicia el OAuth propio.
- `web/app/api/calendar/google/callback/route.ts` — canjea el código, crea el
  calendario "My Idea", guarda el refresh_token cifrado, sync inicial en `after()`.
- `web/app/api/calendar/google/estado/route.ts` — estado para la UI (provider-aware).
- `web/app/api/calendar/google/desconectar/route.ts` — borra el calendario + conexión.
- `web/app/api/calendar/google/sync/route.ts` — "sincronizar ahora" (red de seguridad).
- `web/lib/googleCalendar.ts` — cliente REST (sin SDK): consentimiento, canje,
  refresco, crear/borrar calendario y eventos.
- `web/lib/calendarioSync.ts` — reglas del evento + orquestación (admin client).
- `web/lib/cifrado.ts` — AES-256-GCM genérico (para el refresh_token).
- `web/app/ui/SincroniaGoogle.tsx` — la tarjeta del aside (activar/conectar/desconectar).

## Decisiones de arquitectura (las que costaron pensarse)

- **Calendario DEDICADO "My Idea"** en la cuenta del usuario (no su calendario
  principal): scope mínimo **`https://www.googleapis.com/auth/calendar.app.created`**
  (la app solo ve/gestiona los calendarios que ELLA crea).
- **Una vía** (app → Google). La doble vía (Google → app) es mucho más compleja
  (webhooks, canales de escucha) y no se hizo.
- **Flujo OAuth PROPIO**, no el login de Supabase: se reusa el MISMO cliente
  OAuth del login (`GOOGLE_OAUTH_CLIENT_ID`/`SECRET`), añadiéndole el redirect
  URI del calendario. `access_type=offline` + `prompt=consent` para obtener el
  refresh_token.
- **Token cifrado** (AES-256-GCM) con `GOOGLE_TOKEN_ENCRYPTION_KEY`.
- **Regla del evento:** una tarea del viaje principal con fecha y aún abierta
  (no hecha, no retirada) tiene evento; al marcarla hecha/retirada o quitarle la
  fecha, el evento se **borra**. Evento de día completo, **aviso la víspera a las
  20:00** (= 240 min antes de medianoche).
- **UI provider-aware:** "activar sincronía" si el usuario entró con Google (ya
  confía a Google con nosotros; solo falta el permiso de calendario) vs "conectar
  una cuenta de Google" si entró por correo. **OJO — corrección de premisa:**
  entrar con Google da IDENTIDAD, **no** acceso al calendario; el permiso de
  calendario es un consentimiento aparte (por eso el botón no es redundante).
- **Seguridad:** el `next` (a dónde volver tras el OAuth) debe rechazar rutas
  **protocolo-relativas** (`//host`, `/\host`) o es un **open redirect** — lo
  cazó la revisión de seguridad. Regla vigente para cualquier `next`/redirect.

---

## La migración 031 (por qué sigue en Supabase sin uso)

`supabase/migrations/my_idea_031_calendario_google.sql` **se aplicó** en el
Supabase de producción (el fundador la corrió). Crea dos tablas INTERNAS (RLS
encendido sin policies; solo service_role):

- `google_calendar_cuenta` — la conexión de Google por usuario (refresh_token
  cifrado, calendar_id del "My Idea", email, scope).
- `google_calendar_evento` — el mapa tarea → evento de Google.

Al retirar Google, **las tablas quedaron VACÍAS** (nunca hubo conexiones vivas en
producción). **No se hizo down-migration** (no se borraron) por dos razones: (1)
`DROP TABLE` es destructivo y sin beneficio real (tablas vacías no molestan ni
cuestan); (2) queremos **retomar** Google, y así las tablas ya están listas.
`check_migraciones.sql` sigue verificando la 031 (queda en ✓). Cuando se retome,
**no hay que re-aplicar nada**: las tablas ya existen.

## Configuración externa que quedó lista (dormida)

- **Google Cloud** (proyecto del fundador): Calendar API **habilitada**, scope
  `calendar.app.created` en la pantalla de consentimiento, redirect URIs
  registrados (`https://www.myideaproject.com/api/calendar/google/callback` +
  localhost), usuarios de prueba añadidos, app en modo "Testing".
- **Env:** `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET`,
  `GOOGLE_CLOUD_PROJECT_ID` y `GOOGLE_TOKEN_ENCRYPTION_KEY` siguen en `.env` y en
  Vercel. El código actual **ya no** lee `GOOGLE_TOKEN_ENCRYPTION_KEY`, pero
  recuperar el código lo vuelve a usar sin más.
- **Pendiente si se retoma para PRODUCCIÓN abierta:** el scope de calendario es
  "sensible"; Google exige **verificar la app** para pasar de modo prueba (hasta
  100 test users) a todos los usuarios.

## Cómo retomarlo, en corto

1. `git checkout b3c74b2 -- …` (los archivos de arriba) y re-cablear los hooks.
2. Nada de migración/config: la 031 y Google Cloud ya están.
3. Decidir si conviven las dos sincronías (webcal universal + Google instantáneo)
   o si Google reemplaza al webcal para cuentas Google.
