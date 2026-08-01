# Beta con cuentas y créditos — el manual de operación (ETAPA 2)

Fase: identidad y créditos (rama `beta-identidad-creditos`, tag `web-v1.5.0-beta`).
Diseño: [CUENTAS_DISENO.md](CUENTAS_DISENO.md). Migraciones 020-024: **aplicadas**.
Catálogo comercial: [ANALISIS_PRECIOS.md](ANALISIS_PRECIOS.md) (§4 es ley).

**Beta sin cortesía (fase "Catálogo congruente", ANÁLISIS §4/§8.3):** ya NO hay
otorgamiento automático al primer login. Los invitados ven la app **exactamente
como se venderá** —precios reales en cada compuerta, cero tachados, cero "gratis
en beta"— y el fundador **siembra créditos a mano** desde Supabase. Así la
retroalimentación incluye la percepción de precio. Ninguna pasarela activada.

## 1. Cómo funciona (el resumen de una pantalla)

- **Libre sin login:** la web pública y el ORGANIZADOR (el gancho). La identidad
  invisible sigue existiendo solo para eso.
- **El login nace en "Iniciar La Exploración"**: correo + **contraseña** o
  Google, con allowlist. (Modelo del I Ching, jul 2026: el código-cada-vez
  murió — chocaba con el límite de correos de producción y con el 2FA. Ahora
  el correo solo se manda UNA vez, al confirmar el registro; entrar es por
  contraseña, sin correos.) Al autenticarse: los proyectos del anónimo se
  **adoptan** (la cookie del propio request es la prueba de posesión). **Ya no
  se otorga cortesía**: la cuenta nace en 0 hasta que el fundador la siembra
  (§2.f). El código de cortesía (`otorgarCortesia`, `CORTESIA_BETA`,
  `beta_courtesy_log`) queda **dormido**, no borrado, por si la cortesía pública
  post-lanzamiento se decide con telemetría.
- **El catálogo (ANÁLISIS §4, precios REALES en créditos, 1 crédito = 1 USD):**

  | Unidad | Verifica | Cobra a la entrega | Créditos |
  |---|---|---|---|
  | Plan core (La Exploración) | `session/start` | plan entregado (`plan:{sessionId}`) | **10** |
  | Seguimiento core | `follow` | plan del ciclo | **5** |
  | Plan de mundo | al abrir el stream del plan | plan entregado (el **preview y el diagnóstico son gratis**) | **5** |
  | Seguimiento de mundo | `follow` (dominio) | plan del ciclo | **5** |
  | Tus Números | al activar | — **incluido en el plan**; la activación ancla `activado_at` pero NO cobra | **0** |

  Congruencia exacta (por qué estos números): cada pack ES un paquete real —
  Recarga 5, Básico 10 (= plan), Premium 15 (= plan + un seguimiento),
  Profesional 30 (= plan + 2 seguimientos + mundo + su seguimiento). La
  Claridad y los diagnósticos de mundos son **gratis**.

- Saldo insuficiente: **402 antes del esfuerzo** ("Te quedan X créditos; esto
  cuesta Y. Tu trabajo queda guardado tal como está.").
- Carrera rara (verificó y otra pestaña gastó): **se entrega igual** y queda en
  bitácora (`cobro_carrera`). Jamás se cobra de más.
- Fallo tras un cobro y antes del done: **reembolso automático** con su log
  (`credit_refund_log`). El usuario jamás pierde créditos por fallo nuestro.

## 2. Checklist de siembra del fundador

### a) Sembrar emails en la allowlist (SQL Editor)

```sql
INSERT INTO public.beta_allowlist (email) VALUES
  ('alexcatbaster@gmail.com'),
  ('invitado2@ejemplo.com')
ON CONFLICT (email) DO NOTHING;
```

Quien no está en la lista recibe en el login: "Ese correo aún no está en la
lista de invitados…" (200 amable, jamás un error técnico). La allowlist es la
**puerta** de la beta (no se toca al retirar la cortesía).

Dos formas de cerrar la puerta, con efectos distintos:

- **Dejar de invitar** (no insertar filas nuevas): los invitados ya sembrados
  siguen entrando con su cuenta de siempre. Nadie NUEVO puede crear cuenta.
- **`TRUNCATE public.beta_allowlist;`**: bloquea el reingreso de TODOS,
  incluidos los invitados de siempre (ambas rutas fallan el chequeo en cada
  intento). Úsala solo si de verdad quieres cerrar la puerta completa.

### b) Entrar por primera vez (correo + contraseña, modelo I Ching)

1. `https://www.myideaproject.com/login` → pestaña **Crear cuenta** → correo +
   contraseña (mín. 8, una mayúscula, un número) → **"Crear mi cuenta"**.
2. Llega **un** correo de confirmación (una sola vez en la vida de la cuenta).
   Abrir el enlace → `/auth/callback` confirma y entra.
3. Las siguientes veces: pestaña **Entrar** → correo + contraseña. **Sin
   correos** (por eso no choca con el límite de Resend). "Olvidé mi
   contraseña" manda un enlace de recuperación a `/auth/update-password`.
4. O bien, en cualquier momento: **"Continuar con Google"** (mismo correo =
   misma cuenta).
5. Al autenticarse la primera vez: adopción de los proyectos del anónimo +
   destino `/ideas` (o la idea que ibas a explorar: `?next=`). **La cuenta
   nace en 0 créditos**; siémbrala con §2.f para que pueda comprar planes.

**El template del correo en Supabase** (Auth → Emails → Templates →
**Confirm signup** y **Reset password**) debe usar el enlace, no el código:
`{{ .ConfirmationURL }}`. (El viejo template de `{{ .Token }}` era del código
que murió.)

### c) Adoptar TUS proyectos de prueba (los que quieras seguir)

Desde `web/`, primero en dry-run y luego con `--si`:

```
npx tsx scripts/adoptar_proyectos.ts alexcatbaster@gmail.com <id1>,<id2>
npx tsx scripts/adoptar_proyectos.ts alexcatbaster@gmail.com <id1>,<id2> --si
```

Los ids se ven en la URL de cada idea (`/idea/<id>`). Los proyectos históricos
de vuelos que NO adoptes quedan invisibles para todos (sin dueño real, ninguna
cuenta los ve: RLS).

### d) Variables de entorno (Vercel → Settings → Environment Variables)

- `RATE_LIMIT_POR=usuario` — ahora que hay identidad real, el límite diario es
  por usuario (el fusible global sigue intacto como respaldo agregado).
  Sembrada por el fundador el 2026-07-19 (production + preview).
- Las demás (`SUPABASE_*`, `ANTHROPIC_API_KEY`, `VUELO_DEV_PASSWORD`) no cambian.
- El `.env` de la raíz (local, jamás en git) es el espejo documentado de todo:
  qué vive también en Vercel, qué vive en Supabase (Google, Resend) y qué es
  solo de los arneses. Plantilla commitada: `.env.example`.

### e) Login con Google (configuración de una sola vez, 2026-07-19)

La app ofrece "Continuar con Google" además del correo+contraseña (réplica del I Ching:
`/api/auth/google` inicia, `/auth/callback` recibe; la allowlist se aplica
DESPUÉS de autenticar y el trabajo del anónimo jamás se pierde — detalle en
los comentarios de ambas rutas).

Configuración que vive FUERA del repo:

1. **Google Cloud** (proyecto `my-idea-503000`): OAuth client tipo Web.
   - Redirect URI: `https://gkcmrxkmkffkpjzmtoqm.supabase.co/auth/v1/callback`
   - JS origins: `myideaproject.com`, `my-idea-psi.vercel.app`, el dominio de
     staging (conviene añadir también `www.myideaproject.com`).
   - Client ID + Secret: respaldados en el `.env` de la raíz (registro).
2. **Supabase → Authentication → Providers → Google**: activar y pegar
   Client ID + Secret.
3. **Supabase → Authentication → URL Configuration → Redirect URLs**: añadir
   `https://www.myideaproject.com/auth/callback` y
   `http://localhost:3000/auth/callback` (y el dominio de preview si se
   prueba en staging).

Mismo correo por Google que por contraseña = **la misma cuenta** (Supabase vincula
por email verificado).

### f) Sembrar créditos a mano (el reemplazo de la cortesía)

La cuenta nace en 0. Para que un invitado pueda trabajar, el fundador le siembra
créditos con la RPC **`otorgar_creditos`** (idempotente, la misma que usarán las
pasarelas). En el **SQL Editor** de Supabase (corre como `postgres`, así que
puede ejecutar la RPC aunque esté restringida a `service_role`):

```sql
-- 1) Encontrar el user_id por correo
select id, email from auth.users where email = 'invitado@ejemplo.com';

-- 2) Sembrar (idempotente por p_idempotency_key: repetir la MISMA clave NO
--    vuelve a sumar, solo devuelve el saldo). 30 = un viaje entero (Profesional).
select public.otorgar_creditos(
  p_user_id         => '00000000-0000-0000-0000-000000000000'::uuid,  -- el id del paso 1
  p_monto           => 30,
  p_origen          => 'siembra_beta',
  p_idempotency_key => 'siembra_beta:00000000-0000-0000-0000-000000000000:v1',
  p_pack            => 'siembra_beta'
);
```

- **Para sembrar MÁS después**, cambia el sufijo de la clave (`:v1` → `:v2`); con
  la misma clave la RPC es un no-op seguro (devuelve el saldo sin doblar).
- `p_origen='siembra_beta'` deja rastro en `credit_transactions` (tipo `grant`)
  para que la contabilidad de la beta sea auditable. NO uses `'revenuecat'`
  (ese origen mueve `total_comprado`, reservado a compras reales).
- Verás el saldo al instante en el chip de `/ideas` y en el centro `/creditos`.

## 3. Estado vivo vs dormido

| Pieza | Estado |
|---|---|
| Ledger 020-024 (RPCs atómicas, RLS, courtesy log, refund log) | **VIVO** |
| Siembra manual de créditos (`otorgar_creditos`, origen `siembra_beta`) | **VIVA** (§2.f) |
| Cortesía automática al primer login (`otorgarCortesia`, `CORTESIA_BETA`) | **DORMIDA** (retirada §8.3; código intacto por si vuelve) |
| Los puntos de cobro + 402 + idempotencia + refund | **VIVOS** (precios reales del §4) |
| Tus Números | **INCLUIDO en el plan** (activa `activado_at`, no cobra) |
| Login por correo + contraseña + allowlist + adopción al login | **VIVO** |
| Login con Google (allowlist post-auth, mundo del anónimo intacto) | **VIVO** (requiere provider configurado en Supabase) |
| Chip de saldo + precios vivos (el tachado murió) | **VIVO** |
| RevenueCat / Stripe / Play (pasarelas, webhook) | **DORMIDO** (esquema listo, ancla en 023; ETAPA 3) |
| Bundles de compra del centro de créditos | **DORMIDO** ("la compra se abre pronto"; pasarela pendiente) |
| 2FA/TOTP + dominio de correo propio | **DORMIDO** (ETAPA 2/d, anclas del diseño §1) |

## 4. El vuelo de dinero (la verificación más seria)

Con `pnpm dev` en :3000 y la 020-024 aplicadas:

```
npx tsx scripts/vuelo_beta.ts
```

Cubre: login de un usuario sembrado → **siembra manual de 30** (`otorgar_creditos`,
origen `siembra_beta`) → **contabilidad a mano** con el catálogo nuevo
(30 −10 plan −5 seguimiento −5 plan de mundo −5 seguimiento de mundo = **5
exactos**, verificados contra `credit_transactions` fila por fila) → **Tus
Números activa sin cobrar** (ancla `activado_at`, cero transacciones) →
doble-submit sin doble cobro → 402 limpio sin cobrar → reembolso con log →
organizador anónimo + adopción → un segundo usuario NO ve los proyectos del
primero (RLS en vivo).
