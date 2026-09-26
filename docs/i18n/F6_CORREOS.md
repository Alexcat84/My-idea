# i18n F6: los correos en el idioma de la persona (D4)

**Rama:** `i18n`. **Decisión:** D4 de `DISENO.md §7`: sí al Send Email Hook de Supabase, con Resend
y el catálogo. Este documento es la parte que toca al fundador: configurar el hook en el tablero de
Supabase y en Vercel, probarlo y, si hace falta, apagarlo.

## Qué hay en el código

- **El correo del código de 2FA** (`web/app/api/cuenta/2fa/email/enviar/route.ts`) ya salía del
  catálogo `servidorDosFactores` en el idioma de la interfaz (la cookie `myidea_idioma`), con los
  once idiomas completos. F6 le agrega `lang` y `dir` al html: en árabe se lee de derecha a
  izquierda. En español el texto no cambia ni una letra.
- **Los correos de Supabase Auth** (confirmar la cuenta, reenviar la confirmación, recuperar la
  contraseña y, si algún día se usan, invitación, enlace para entrar, cambio de correo, código de
  confirmación y los avisos de seguridad) hoy salen de las plantillas del tablero de Supabase, solo
  en español. Con el hook activo, Supabase deja de usar esas plantillas y llama a
  **`/api/auth/hook-correo`**, que:
  1. verifica la firma de Supabase (Standard Webhooks, con `SEND_EMAIL_HOOK_SECRET`); sin secreto o
     con una firma mala no manda nada y responde error (falla cerrada, y queda en el log);
  2. elige el idioma: el que la persona tenía en la interfaz, guardado en `user_metadata.idioma`
     (lo escribe el registro al crear la cuenta y la entrada con contraseña cada vez que cambia); si
     no hay, español;
  3. arma asunto, texto y html desde el catálogo `web/lib/i18n/mensajes/correosAuth.ts` (once
     idiomas) con el mismo enlace que ponía `{{ .ConfirmationURL }}`:
     `https://<proyecto>.supabase.co/auth/v1/verify?token=…&type=…&redirect_to=…`, así que el
     enlace sigue llegando a `/auth/callback` igual que hoy;
  4. lo manda por Resend con la misma clave y el mismo remitente del 2FA (`RESEND_API_KEY`,
     `TWO_FACTOR_EMAIL_FROM`).

**Una cosa a saber:** las cuentas que ya existen no tienen idioma guardado hasta su próxima entrada
con contraseña. Mientras tanto, sus correos salen en español, como hoy. Quien entra con Google no
pasa por esa ruta; sus correos de Supabase (raros: no tiene contraseña que recuperar) salen en
español o en el idioma con que se registró.

## Lo que hace falta del fundador

Primero el código tiene que estar desplegado en producción (la ruta `/api/auth/hook-correo` debe
existir antes de activar el hook; si no, cada registro fallaría). Después, en este orden:

### 1. Generar el secreto y activar el hook en Supabase (proyecto de producción)
1. Supabase → tu proyecto de **producción** → **Authentication** → **Hooks** (en algunos tableros
   aparece como "Auth Hooks").
2. **Add hook** → **Send Email hook**.
3. Tipo: **HTTPS**.
4. URL: `https://www.myideaproject.com/api/auth/hook-correo`
   (con `www`: si el dominio sin `www` redirige, Supabase no sigue la redirección y el hook falla).
5. En la sección del secreto, **Generate secret**. Copia el valor completo, empieza por
   `v1,whsec_`. **No lo guardes en ningún archivo del repo** (AGENTS.md: ninguna credencial en
   archivos versionados); va solo al `.env` de la raíz y a Vercel.
6. **Todavía no lo actives**: primero el secreto tiene que estar en Vercel (paso 2). Guarda el hook
   desactivado si el tablero lo permite; si no lo permite, haz el paso 2 antes del 1.

### 2. Pegar el secreto en Vercel y redesplegar
1. Vercel → my-idea → **Settings** → **Environment Variables** → **Add**.
2. Nombre: `SEND_EMAIL_HOOK_SECRET`. Valor: el secreto del paso 1.
3. Entornos: **Production** y **Preview** con el mismo valor. My Idea usa **un solo proyecto de
   Supabase** para producción y vista previa (las variables de Supabase en Vercel son las mismas en los
   dos entornos), así que hay un solo hook y un solo secreto. El hook siempre llama a la dirección de
   producción; la vista previa no recibe llamadas.
4. Verifica que ya existen `RESEND_API_KEY`, `TWO_FACTOR_EMAIL_FROM` y `SUPABASE_URL` en Production
   (las usa el 2FA desde hace tiempo).
5. **Redeploy** de producción (Deployments → el último de producción → Redeploy), para que la
   variable nueva entre.
6. Anota el secreto en el `.env` de la raíz (local, jamás en git) junto a los demás.

### 3. Activar el hook
Vuelve a Supabase → Authentication → Hooks → el Send Email hook → **Enable** → Save.

**Nota sobre la vista previa:** hay un solo proyecto de Supabase y el hook apunta a producción. Un
correo que se dispare desde la vista previa (un registro de prueba allí) también lo escribe la ruta de
producción, con el código que esté en producción. Por eso el código del hook tiene que estar en
producción ANTES de activar el hook (ver arriba).

## Cómo probarlo (en producción, con tu cuenta)
1. **Recuperar la contraseña en otro idioma.** En la app, cambia el idioma a English. Entra con tu
   correo y contraseña (esto guarda `en` en tu cuenta). Sal. En el login, "olvidé mi contraseña" con
   tu correo. Debe llegar "Choose a new password for My Idea". El enlace debe abrir
   `/auth/update-password` como siempre.
2. **Confirmar una cuenta nueva.** Con un correo tuyo que esté en la allowlist y sin cuenta, cambia
   el idioma a 한국어 y regístrate. Debe llegar "My Idea 이메일 주소를 확인해 주세요" y el enlace debe
   confirmar la cuenta y entrar.
3. **El árabe.** Igual que el 1 con العربية: el correo debe leerse de derecha a izquierda.
4. **Vuelve a español** y repite el 1: el correo debe llegar en español.
5. **Los registros:** Vercel → Logs, filtra por `hook-correo`. Una prueba buena no deja líneas de
   error. Supabase → Logs → Auth muestra cada llamada al hook con su resultado.

## Qué pasa si el hook falla
- El hook responde error cuando: falta el secreto, la firma no calza, falta la configuración de
  Resend, Resend falla, o todo tarda más de 5 segundos (el límite de Supabase; la ruta corta a
  Resend a los 4). Cada caso deja una línea `[hook-correo]` en los logs de Vercel.
- Supabase entonces **no da el correo por enviado** y la acción falla:
  - **Registro:** la pantalla muestra el error de siempre ("no pudimos crear tu cuenta"); la cuenta
    puede quedar creada sin confirmar, y "reenviar el correo" la rescata cuando el hook vuelva.
  - **Olvidé mi contraseña y reenviar la confirmación:** la pantalla dice "enviado" pase lo que pase
    (así no revela qué correos tienen cuenta), pero el correo no llega. El error queda en los logs.
- Si Resend responde 429 (límite), la ruta responde 429 y Supabase reintenta solo, dentro de sus
  5 segundos.

## Cómo volver atrás
Supabase → Authentication → Hooks → el Send Email hook → **Disable** (o borrarlo). Supabase vuelve al
instante a mandar sus propias plantillas por el SMTP de Resend, en español, como antes. No hace
falta redesplegar ni tocar código. Para eso, **no borres las plantillas del tablero** ni la
configuración SMTP: son el respaldo.

## Pruebas (sin secretos reales)
- `web/lib/correosAuth.test.ts`: la firma contra el vector publicado por Standard Webhooks (válida,
  cuerpo alterado, otro secreto, sin cabeceras, fuera de los 5 minutos, secreto vacío), el idioma
  guardado, el enlace de cada acción calculado a mano, los dos correos del cambio de correo seguro,
  el código de reautenticación, los avisos, el tipo desconocido y el escape del html; y que ningún
  secreto está escrito en el código.
- `web/app/api/auth/hook-correo/route.test.ts`: la ruta con entorno falso y Resend simulado.
- `web/app/api/auth/registrar/route.test.ts` y `web/app/api/auth/entrar/route.test.ts`: el idioma
  queda en `user_metadata.idioma`.
- `web/app/api/cuenta/2fa/email/enviar/route.test.ts`: el correo del 2FA con `lang` y `dir`.
