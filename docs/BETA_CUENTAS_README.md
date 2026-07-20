# Beta con cuentas y créditos — el manual de operación (ETAPA 2)

Fase: identidad y créditos (rama `beta-identidad-creditos`, tag `web-v1.5.0-beta`).
Diseño: [CUENTAS_DISENO.md](CUENTAS_DISENO.md). Migraciones 020-024: **aplicadas**.
La beta corre 100% con cortesía (20 créditos por invitado); **ninguna pasarela activada**.

## 1. Cómo funciona (el resumen de una pantalla)

- **Libre sin login:** la web pública y el ORGANIZADOR (el gancho). La identidad
  invisible sigue existiendo solo para eso.
- **El login nace en "Iniciar La Exploración"**: código de 6 dígitos o Google
  + allowlist (3.2). Al confirmar: los proyectos del anónimo se **adoptan**
  (la cookie del propio request es la prueba de posesión) y la cuenta recibe
  su **cortesía: 20 créditos, una sola vez** (`beta_courtesy_log`).
  - **Gobierno de la cortesía (aclaración del fundador, 2026-07-20):**
    `CORTESIA_BETA = 20` es la política de la **beta cerrada** (solo
    invitados de `beta_allowlist`), **no** la cortesía de bienvenida del
    lanzamiento público. Esa es **decisión pendiente** del fundador
    (candidata preliminar: organizador gratis + 5 créditos = un plan
    completo; se calibra con la telemetría de esta beta). Ver
    `docs/MATRIZ_DELTAS_CANON_2.0.md` ("Decisiones pendientes") y el
    comentario junto a la constante en `web/lib/creditos.ts`.
- **Cobros (verificar-al-inicio / descontar-A-LA-ENTREGA, idempotentes):**

  | Unidad | Verifica | Cobra a la entrega | Créditos |
  |---|---|---|---|
  | Plan core | `session/start` | plan entregado (`plan:{sessionId}`) | 5 |
  | Seguimiento core | `follow` | plan del ciclo | 2 |
  | Plan de mundo | al abrir el stream del plan | plan entregado (el **preview y el diagnóstico son gratis**, 4.5) | 3 |
  | Seguimiento de mundo | `follow` (dominio) | plan del ciclo | 2 |
  | Tus Números | al activar | el primer tablero (`numeros:{projectId}`), una vez por idea; recálculos gratis | 2 |

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
lista de invitados…" (200 amable, jamás un error técnico).

**Cerrar el grifo de la cortesía (`CORTESIA_BETA`, ver §1.b abajo) es una
operación de datos, no de código**, y las dos puertas de entrada la
respetan por igual: el código verifica la allowlist ANTES de mandar el correo
(`api/auth/magic-link`) y Google la verifica DESPUÉS de autenticar, antes de
otorgar nada (`auth/callback`) — ninguna de las dos llega a
`otorgarCortesia` sin pasar por `estaEnAllowlist` primero. Dos formas de
cerrar, con efectos distintos:

- **Dejar de invitar** (no insertar filas nuevas): la forma quirúrgica. Los
  invitados ya sembrados siguen entrando con su cuenta de siempre (y no
  reciben una segunda cortesía: `beta_courtesy_log` es una-sola-vez por
  cuenta, para siempre). Nadie NUEVO puede crear cuenta ni recibir los 20.
- **`TRUNCATE public.beta_allowlist;`** (o `DELETE FROM ... WHERE true`): la
  forma total. Cierra la cortesía Y bloquea el reingreso de TODOS,
  incluidos los invitados de siempre (ambas rutas vuelven a fallar el
  chequeo en cada intento, no solo en el primero). Úsala solo si de verdad
  quieres cerrar la puerta completa, no solo el grifo de bienvenida.

### b) Entrar por primera vez

1. `https://www.myideaproject.com/login` → tu email → escribir el **código de
   6 dígitos** que llega al correo (decisión jul 2026: el enlace mágico quedó
   obsoleto; `/auth/confirm` sigue vivo solo para correos rezagados).
   O bien: **"Continuar con Google"** (mismo correo = misma cuenta).
2. Al entrar: cortesía 20 otorgada (una sola vez) + destino `/ideas`.

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

La app ofrece "Continuar con Google" además del código (réplica del I Ching:
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

Mismo correo por Google que por código = **la misma cuenta** (Supabase vincula
por email verificado); la cortesía no se duplica (una-sola-vez por cuenta).

## 3. Estado vivo vs dormido

| Pieza | Estado |
|---|---|
| Ledger 020-024 (RPCs atómicas, RLS, courtesy log, refund log) | **VIVO** |
| Cortesía 20 al primer login | **VIVO** |
| Los 5 puntos de cobro + 402 + idempotencia + refund | **VIVOS** (se pagan con cortesía) |
| Login por código (6 dígitos) + allowlist + adopción al login | **VIVO** |
| Login con Google (allowlist post-auth, mundo del anónimo intacto) | **VIVO** (código listo; requiere provider configurado en Supabase) |
| Chip de saldo + precios vivos (el tachado murió) | **VIVO** |
| RevenueCat / Stripe / Play (pasarelas, `otorgar_creditos_idempotente`, webhook) | **DORMIDO** (esquema listo, ancla en 023; post-beta) |
| Bundles de compra del centro de créditos | **DORMIDO** ("$ —", decisión del fundador pendiente) |
| 2FA/TOTP + dominio de correo propio | **DORMIDO** (ETAPA 2/d, anclas del diseño §1) |
| Ruta legacy `project/[id]/report` (mini-entrevista vieja de números) | **DORMIDA para la UI** (sin botón; exige cuenta real; el tablero 14 la reemplazó) |

## 4. El vuelo de dinero (la verificación más seria)

Con `pnpm dev` en :3000 y la 020-024 aplicadas:

```
npx tsx scripts/vuelo_beta.ts
```

Cubre: login de un usuario sembrado → cortesía 20 → **contabilidad a mano**
(20 −5 plan −2 números −3 plan de mundo −2 seguimiento = **8 exactos**,
verificados contra `credit_transactions` fila por fila) → doble-submit sin
doble cobro → 402 limpio sin cobrar → reembolso con log → organizador anónimo
+ adopción → un segundo usuario NO ve los proyectos del primero (RLS en vivo).
