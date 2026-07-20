# Migración a la base de producción

**El plan (decisión del fundador, 2026-07-19):** el proyecto Supabase actual
(`gkcmrxkmkffkpjzmtoqm`) se queda como base de **staging** (previews de
Vercel + dev local + arneses). Un proyecto Supabase **nuevo**, creado en la
cuenta de producción, pasa a servir a `www.myideaproject.com`. El código no
cambia ni una línea: todo es configuración.

El mapa final:

| Entorno | Base | Quién la usa |
|---|---|---|
| Producción | proyecto NUEVO | www.myideaproject.com (Vercel Production) |
| Staging | `gkcmrxkmkffkpjzmtoqm` (la actual) | previews de Vercel, `pnpm dev`, vuelos y gates |

---

## Paso 1 · Crear el proyecto nuevo

En la cuenta/organización de producción de Supabase: **New project**.
- Región: la misma de la actual (menor sorpresa de latencia con Vercel).
- Guarda la contraseña de la base en tu gestor (no se vuelve a mostrar).
- Anota el **ref** del proyecto (la parte de `https://<REF>.supabase.co`):
  aparece en varios pasos de abajo como `<REF-NUEVO>`.

## Paso 2 · El esquema: las 29 migraciones, en orden

SQL Editor del proyecto nuevo → pegar y correr **una por una, en orden**,
cada archivo de `supabase/migrations/`:

```
my_idea_001_init.sql          my_idea_011_presupuesto_sesion.sql   my_idea_021_creditos_rpc_consumo.sql
my_idea_002_costo_desglose.sql my_idea_012_project_nodes_salto.sql my_idea_022_creditos_cortesia.sql
my_idea_003_numeros.sql        my_idea_013_caja_de_vidrio.sql      my_idea_023_creditos_revenuecat.sql
my_idea_004_reporte_tipo.sql   my_idea_014_pack_clicks.sql         my_idea_024_creditos_refund.sql
my_idea_005_reporte_etiqueta.sql my_idea_015_checklist_items.sql   my_idea_025_acta_de_cierre.sql
my_idea_006_revoke_rls_auto_enable.sql my_idea_016_mundos.sql      my_idea_026_cierre_de_mundo.sql
my_idea_007_tipo_oferta.sql    my_idea_017_mundos_nuevos.sql       my_idea_027_tus_numeros_vivo.sql
my_idea_008_beta_allowlist.sql my_idea_018_sentido_del_tiempo.sql  my_idea_028_preview_mundos.sql
my_idea_009_estado_recorrido.sql my_idea_019_mundo_riesgos.sql     my_idea_029_centro_de_cuenta.sql
my_idea_010_estado_reporte.sql my_idea_020_creditos_ledger.sql
```

Al final, correr **`my_idea_check_migraciones.sql`** completo: deben salir
TODAS las filas en ✓ OK (001–029). Si alguna falla, no sigas: esa migración
no entró.

## Paso 3 · Authentication (el clon de la config de staging)

En el proyecto nuevo, **Authentication**:

1. **Sign In / Providers → Email**: activado. **Anonymous sign-ins:
   ACTIVADO** (la identidad invisible del organizador nace de ahí;
   sin esto, proxy.ts cae al plan B de usuarios `visitante-*`).
2. **Providers → Google**: activar y pegar el MISMO Client ID y Secret de
   siempre (Google Cloud, proyecto `my-idea-503000`; respaldados en el
   `.env` de la raíz como `GOOGLE_OAUTH_CLIENT_ID/SECRET`).
3. **En Google Cloud Console** (console.cloud.google.com → Credentials →
   el OAuth client): AÑADIR a *Authorized redirect URIs*:
   `https://<REF-NUEVO>.supabase.co/auth/v1/callback`
   (el URI viejo NO se borra: le sirve a staging).
4. **URL Configuration**:
   - Site URL: `https://www.myideaproject.com`
   - Redirect URLs: `https://www.myideaproject.com/auth/confirm`,
     `https://www.myideaproject.com/auth/callback`,
     `https://myideaproject.com/auth/confirm`,
     `https://myideaproject.com/auth/callback`
   - (Las de localhost y previews NO van aquí: esos entornos usan staging.)
5. **Emails → SMTP** (Resend, igual que hoy): host `smtp.resend.com`,
   puerto `465`, usuario `resend`, contraseña = la `RESEND_API_KEY` del
   `.env`, remitente `no-reply@myideaproject.com`, nombre "My Idea".
6. **Emails → Templates → Magic Link**: copiar el template vigente de
   staging TAL CUAL (el cuerpo debe llevar **`{{ .Token }}`** — el código de
   6 dígitos; sin él, el login por código muere). Ábrelo en staging y
   pégalo; no lo reescribas de memoria.
7. **Rate Limits**: subir el envío de emails al valor que tiene staging
   (el default de 2/hora es demasiado bajo para el login por código).

## Paso 4 · Vercel: separar Production de Preview

Hoy varias variables viven compartidas en production+preview. La migración
consiste en **separarlas**: Production apunta a la base nueva, Preview se
queda con la vieja.

En Vercel → my-idea → Settings → Environment Variables, para CADA una de
estas cinco: editar el valor de **Production** (y solo Production) con los
datos del proyecto nuevo (Project Settings → API):

| Variable | Production (nuevo) | Preview (queda igual) |
|---|---|---|
| `NEXT_PUBLIC_SUPABASE_URL` | `https://<REF-NUEVO>.supabase.co` | la actual |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | anon del nuevo | la actual |
| `SUPABASE_URL` | `https://<REF-NUEVO>.supabase.co` | la actual |
| `SUPABASE_ANON_KEY` | anon del nuevo | la actual |
| `SUPABASE_SERVICE_ROLE_KEY` | service_role del nuevo | la actual |

**Todo lo demás NO se toca** (igual en ambos entornos): `ANTHROPIC_API_KEY`,
`VOYAGE_API_KEY`, `UPSTASH_*` (ver nota abajo), `RATE_LIMIT_POR`,
`RESEND_API_KEY`, `TOTP_ENCRYPTION_KEY`, `TWO_FACTOR_EMAIL_CODE_SECRET`,
`TWO_FACTOR_EMAIL_FROM`.

- **`TOTP_ENCRYPTION_KEY` jamás se rota en esta migración**: es la que
  descifra los secretos 2FA; misma llave en ambos entornos está bien.
- **El `.env` local de la raíz NO cambia**: sigue apuntando a staging.
  Los arneses (vuelos, gates, capturas) nunca tocan producción.

Después: **Redeploy** de Production (y de un preview, para confirmar que
staging sigue vivo).

> **Nota Upstash (fusible compartido):** el fusible global
> (`FUSIBLE_SESIONES_DIA`) cuenta en UNA base de Redis. Si producción y
> staging comparten las mismas credenciales de Upstash, comparten fusible:
> una corrida de vuelos en staging consume cupo de producción. Recomendado:
> crear una segunda base gratis en Upstash y poner SUS credenciales
> (`UPSTASH_REDIS_REST_URL/TOKEN`) solo en **Preview**. Cinco minutos, y
> cada entorno tiene su propio fusible.

## Paso 5 · Semillas de producción

1. **Allowlist** (SQL Editor del nuevo):
   ```sql
   INSERT INTO public.beta_allowlist (email) VALUES
     ('alexcatbaster@gmail.com')
   ON CONFLICT (email) DO NOTHING;
   ```
   (más los invitados que quieras, uno por fila).
2. Tu **primer login** en `www.myideaproject.com/login` (código o Google)
   crea tu cuenta nueva y otorga la cortesía 20.
3. La base nace limpia: no hay proyectos anónimos que adoptar.

## Paso 6 · ¿Llevarte las ideas de la base vieja? (opcional)

**Recomendación de beta: arrancar limpia.** Tus ideas de prueba viven bien
en staging y seguirás viéndolas ahí. Si más adelante quieres mudar UNA idea
real a producción, pídemelo: requiere un script de mudanza con remapeo de
`user_id` (los ids de `auth.users` son distintos en cada base — un dump
directo NO sirve) recorriendo las tablas en orden de FK. Lo preparo cuando
lo necesites; no intentes un pg_dump a mano.

## Paso 7 · Verificación de cierre

1. `my_idea_check_migraciones.sql` en el proyecto nuevo: 001–029 todas ✓.
2. Smoke en `www.myideaproject.com` (la base NUEVA):
   - Landing carga; "Comenzar" → organizador funciona (identidad invisible).
   - Login por código: llega el correo con 6 dígitos, entra, chip **20**.
   - Login con Google: entra a la MISMA cuenta (mismo email), sin doble
     cortesía.
   - /cuenta: activar 2FA con la app, salir, volver a entrar → pide el
     desafío.
   - /potenciadores: packs 5/15/30 con sus precios.
3. Smoke en un preview de staging: sigue funcionando contra la base vieja.

## Checklist de identidad del proyecto NUEVO (adición del auditor)

La configuración de hoy vive en el proyecto que será staging y **se replica,
no se mueve**: nada de lo de abajo se quita del proyecto viejo. Marcar cada
casilla en el proyecto NUEVO antes de tocar Vercel:

**Google Cloud Console** (proyecto `my-idea-503000`):
- [ ] Redirect URI del Supabase nuevo AÑADIDA (no reemplazada):
      `https://<REF-NUEVO>.supabase.co/auth/v1/callback`

**Supabase NUEVO → Authentication:**
- [ ] Email provider activado
- [ ] **Anonymous sign-ins activado** (la identidad invisible del proxy)
- [ ] Google provider activado con Client ID + Secret (los del `.env`)
- [ ] SMTP Resend configurado (smtp.resend.com:465, user `resend`,
      pass = `RESEND_API_KEY`, remitente `no-reply@myideaproject.com`)
- [ ] Template Magic Link con **`{{ .Token }}`** (copiado de staging tal cual)
- [ ] Rate limit de emails subido (no el default 2/hora)
- [ ] Site URL: `https://www.myideaproject.com`
- [ ] Redirect URLs: `/auth/confirm` y `/auth/callback` en www y apex (4)

**Vercel → Environment Variables → Production (inventario COMPLETO tras la
migración — verificar una por una, ninguna puede faltar):**

| Variable | Valor en Production |
|---|---|
| `NEXT_PUBLIC_SUPABASE_URL` | del proyecto NUEVO |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | del proyecto NUEVO |
| `SUPABASE_URL` | del proyecto NUEVO |
| `SUPABASE_ANON_KEY` | del proyecto NUEVO |
| `SUPABASE_SERVICE_ROLE_KEY` | del proyecto NUEVO |
| `ANTHROPIC_API_KEY` | sin cambio |
| `VOYAGE_API_KEY` | sin cambio |
| `UPSTASH_REDIS_REST_URL` / `_TOKEN` | sin cambio (los de producción) |
| `RATE_LIMIT_POR` | `usuario` (sin cambio) |
| `RESEND_API_KEY` | sin cambio (el 2FA por correo la lee) |
| `TOTP_ENCRYPTION_KEY` | **sin cambio y JAMÁS rotada** (descifra los secretos 2FA) |
| `TWO_FACTOR_EMAIL_CODE_SECRET` | sin cambio |
| `TWO_FACTOR_EMAIL_FROM` | `My Idea <no-reply@myideaproject.com>` (sin cambio) |

**Semillas del NUEVO:** `beta_allowlist` con tu email (+ invitados) — sin
esta fila, ni el código ni Google te dejan entrar.

## Rollback (si algo sale mal)

Vercel → las cinco variables de Production de vuelta a los valores viejos →
Redeploy. Producción vuelve a la base actual en un minuto; el proyecto
nuevo queda intacto para reintentar. Nada del código depende de cuál base
está detrás.
