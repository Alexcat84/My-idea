# Inventario de datos personales de My Idea

**Fecha:** 26 sep 2026. **Base:** lectura del código (`web/`, `engine/`) y de las 44 migraciones de
`supabase/migrations/`, en la rama `i18n` (`main` en `dc5f5e65`). Lo que el código no permite
afirmar va marcado **POR VERIFICAR**. Este inventario es la base de los borradores de Términos,
Privacidad y Cookies de esta carpeta.

## 1. Qué se guarda y dónde

Todo vive en la base de datos de **Supabase** (PostgreSQL + autenticación). Salvo donde se indica,
cada tabla cuelga de la cuenta con `ON DELETE CASCADE` (se borra con la cuenta), directo o a través
de `projects`.

| dato | tabla o lugar | contenido |
|---|---|---|
| Cuenta | `auth.users` (gestionada por Supabase) | correo, hash de la contraseña o identidad de Google, fechas; en `app_metadata`, las identidades invisibles pendientes de adoptar |
| Identidad invisible (visitante) | `auth.users` anónimo, creado en la primera visita (`proxy.ts`) | un id sin correo; las ideas escritas antes de crear cuenta cuelgan de ella hasta que se adoptan |
| Ideas | `projects` | el texto original de la idea tal como se escribió o dictó, título, resumen vivo generado por la IA, tipo de oferta, motivo de cierre |
| Respuestas de la entrevista | `sessions` | mensaje de entrada, estado del recorrido (el historial de la conversación y las cifras detectadas), registro de decisiones del motor, calidad, costo de IA |
| Planes y documentos | `plans`, `project_unlocks` (diagnósticos de mundo), `project_actas` (fotos del cierre) | el plan en texto, los diagnósticos, las fotos del acta |
| Tareas y notas | `checklist_items` | el texto de cada tarea, las notas del usuario, el motivo de retirar una tarea, fechas, campos de protección |
| Bitácora | `project_bitacora` | los eventos de lo que el usuario decidió (con un `payload` libre) |
| Números del negocio | `projects.numeros_proyecto`, `project_numeros_versiones` | costos, horas, precios, gastos fijos, ventas, con el texto que el usuario escribió; cada versión del tablero y su narración |
| Recorrido por el grafo | `project_nodes`, `node_visits`, `project_modos` | qué conceptos se trabajaron; el modo y la capacidad de cada espacio |
| Créditos | `credit_accounts`, `credit_transactions`, `credit_reservas`, `query_credits` (antiguo), `beta_courtesy_log` | saldo, movimientos (cobros, otorgamientos, reembolsos), reservas en curso |
| Reembolsos | `credit_refund_log` | id de usuario, monto y motivo. **Sin FK a la cuenta: sobrevive al borrado** (hallazgo B1) |
| Eventos de pago | `revenuecat_webhook_events` | id de usuario del procesador, tipo de evento. **Sin FK: sobreviviría al borrado** (hallazgo B2). Hoy no hay código que la escriba |
| Doble factor | `user_seguridad` (secreto TOTP cifrado AES-256-GCM), `two_factor_recovery_codes` (hash bcrypt), `two_factor_email_codes` (hash, vence a los 10 min), `two_factor_attempts` | secretos cifrados, códigos en hash, **dirección IP** y sesión de cada intento |
| Lista de invitados de la beta | `beta_allowlist` | **el correo en claro**, quién invitó y notas. **Sin vínculo con la cuenta: sobrevive al borrado** (hallazgo B3) |
| Huella anti-abuso de la cortesía | `cortesia_email_log` | el hash SHA-256 del correo. Sin vínculo con la cuenta **a propósito**: evita que borrar y volver a crear la cuenta repita la cortesía (hoy la cortesía está dormida) |
| Clics en mundos | `pack_clicks` | id de usuario y mundo |
| Calendario de Google | `google_calendar_cuenta` (token cifrado, correo de Google), `google_calendar_evento` | tablas creadas (migración 031) **sin ningún código que las use** |
| Calendario suscrito | el feed `/api/calendar/feed/<token>.ics` | sirve los nombres de las ideas y el texto de las tareas con fechas a la app de calendario del usuario; el token es un HMAC del id de usuario |
| Límites de uso | **Upstash Redis** | claves con la **IP** o el id de usuario: límite diario (24 h), fusible global (48 h), envíos de código de 2FA (10 min) |
| Registros del servidor | **Vercel** (logs) | algunas líneas llevan ids de usuario y correos (por ejemplo, el correo de un intento de entrada no invitado) |

## 2. Cuánto tiempo

- **Mientras la cuenta exista**, todo lo de §1. No hay limpieza por tiempo (ningún cron, `vercel.json`
  sin tareas programadas).
- **Por tiempo:** Upstash hasta 48 h; códigos de 2FA por correo 10 min (los usados quedan); la
  cookie de regreso tras el login 10 min.
- **Identidades invisibles y sus ideas no adoptadas:** para siempre hasta el arreglo de
  `borrado-cuenta`; con él, se borran a los 30 días sin actividad.
- **Tras borrar la cuenta:** ver §4.
- **Copias de seguridad de Supabase y retención de logs de Vercel:** POR VERIFICAR (dependen del
  plan contratado).

## 3. A quién se envía (proveedores)

| proveedor | función | qué recibe | país |
|---|---|---|---|
| **Anthropic** (Claude) | redactar la entrevista, la Claridad, el plan, los diagnósticos, los números narrados | el texto de la idea, las respuestas, el resumen vivo, las cifras del negocio | POR VERIFICAR (probablemente Estados Unidos) |
| **Voyage AI** | búsqueda semántica en el grafo (embeddings) | el texto de las respuestas, el perfil de la sesión o la idea original, en cada turno | POR VERIFICAR (probablemente Estados Unidos) |
| **Supabase** | base de datos y autenticación | todo lo de §1 | POR VERIFICAR (región del proyecto en el tablero de Supabase) |
| **Vercel** | alojamiento y ejecución de la app | todas las peticiones; registros con ids y correos | POR VERIFICAR (probablemente Estados Unidos; región de funciones en el tablero) |
| **Resend** | correo del código de 2FA y, según `.env.example`, el SMTP de los correos de Supabase | el correo del usuario y el código | POR VERIFICAR (probablemente Estados Unidos) |
| **Upstash** | límites de uso | la IP o el id de usuario dentro de las claves | POR VERIFICAR (región de la base) |
| **Google** | entrar con Google (OAuth, a través de Supabase) | la identidad de Google del usuario que elige ese método | POR VERIFICAR (probablemente Estados Unidos) |
| **Procesador de pagos** | cobrar la compra de créditos | ninguno todavía: la compra con dinero no está activa (hay un esquema preparado para RevenueCat, sin código ni claves) | POR VERIFICAR cuando se active |

- **Tipografías:** `next/font/google` descarga la tipografía al construir la app y la sirve desde
  nuestro dominio, así que el navegador no llama a Google por ella (POR VERIFICAR en el despliegue).
- **No hay analítica ni publicidad de terceros:** ni Vercel Analytics, ni PostHog, ni Sentry, ni
  píxeles.
- **Si un proveedor usa los datos para entrenar sus modelos:** POR VERIFICAR en su política (enlaces
  en el borrador de Privacidad). El código no lo puede afirmar.

## 4. El borrado de la cuenta (comprobado en el código)

`/api/cuenta/eliminar` pide la palabra "ELIMINAR" (y el doble factor si está activo), guarda la
huella anti-abuso de la cortesía si hace falta, y llama a `auth.admin.deleteUser`. **Todo lo demás
depende del `ON DELETE CASCADE`.** Se borra con la cuenta: ideas, sesiones, planes, tareas, bitácora,
números, actas, créditos, reservas y los datos de doble factor.

**Sobrevivía al borrado (hallazgos B1 a B4). ARREGLADO en la rama `borrado-cuenta` (decisiones del
fundador, 26 sep 2026), pendiente de su visto para ir a `main` y de aplicar la migración 044:**
B3 y B4 se borran; B1 y B2 se anonimizan (queda importe y fecha); las ideas de invitado sin dueño
se borran solas a los 30 días sin actividad (tarea programada diaria). Lo que se encontró:
- **B1.** `credit_refund_log`: id de usuario, monto y motivo.
- **B2.** `revenuecat_webhook_events`: el id de usuario del procesador (hoy sin filas).
- **B3.** `beta_allowlist`: el correo en claro, con quién invitó y notas.
- **B4.** Las identidades invisibles pendientes de adopción y **las ideas que escribió antes de
  entrar**.

**Sobrevive y se declara, sin ser un defecto:**
- La huella hash del correo en `cortesia_email_log`, a propósito (base legal POR VERIFICAR).
- Las claves de Upstash, hasta 48 h.
- Los registros de Vercel, según su retención.
- Las copias ya enviadas a Anthropic, Voyage y Resend, según sus políticas.

**Nota contable:** borrar la cuenta borra también el historial de créditos. Si alguna obligación
fiscal o de consumo exige conservar registros de transacciones cuando haya pagos reales, habrá que
conservarlos anonimizados (POR VERIFICAR con un profesional).

## 5. Navegador

- **Cookies de Supabase** (`sb-*`): la sesión, también la de la identidad invisible; y el verificador
  PKCE al entrar con Google.
- **`post_login_next`:** a dónde volver tras el login (httpOnly, 10 min).
- **localStorage:** `mi-idea:gantt-vista` (vista preferida del Gantt) y
  `mi-idea:selector-estado-usado` (una pista ya vista).
- **Próxima (i18n, F2):** `myidea_idioma`, el idioma preferido.

## 6. El dictado

`web/lib/useSpeech.ts` usa solo el reconocimiento de voz del navegador (`SpeechRecognition`). La app
no graba ni sube audio. El texto dictado entra al campo y viaja como texto escrito. Dónde procesa
el audio el propio navegador (por ejemplo, en servidores del fabricante): POR VERIFICAR, y
depende del navegador.

## 7. Todo lo POR VERIFICAR

1. País y región de cada proveedor (§3), en sus tableros y contratos.
2. Si Anthropic, Voyage, Supabase, Vercel, Resend, Upstash o Google usan los datos para entrenar o
   para otros fines; y sus plazos de retención.
3. Retención de las copias de seguridad de Supabase y de los registros de Vercel.
4. El procesador de pagos, cuando se active.
5. La base legal para conservar la huella hash de la cortesía tras el borrado.
6. Si hay obligación de conservar registros de transacciones (fiscal o de consumo) cuando existan
   pagos reales.
7. Dónde procesa el audio el navegador al dictar.
8. Que `next/font` no llame a Google en el despliegue real.
9. La razón social registrada en Quebec y el correo de contacto de privacidad.
