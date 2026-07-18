# Plan — Sistema de cuentas y créditos de My Idea

**Estado:** propuesta para revisión del auditor y del fundador. **Ninguna migración aplicada, ninguna línea de ETAPA 2 ejecutada.**
**Rama:** `cuentas-y-creditos` (base `91b2cf4`, off staging). No toca `main` ni `staging`.
**Referencia probada:** The Original I Ching (clonado en `referencia/iching-app/`, en `.gitignore`) — modelo de packs consumibles sin suscripción, ya en producción.
**Disciplina de dos etapas:** ETAPA 1 = estudio + este plan + migraciones propuestas (no aplicadas) + mapa de cobro → **DETENERSE** para revisión. ETAPA 2 = ejecución del alcance reversible, **solo tras aprobación escrita**.

---

## 0. Resumen ejecutivo

My Idea necesita salir de la beta de cortesía hacia el cobro. El patrón que lo resuelve ya existe, probado, en The Original I Ching: **un saldo de créditos por usuario, consumido de forma atómica en la base de datos (no en el código), y recargado vía RevenueCat como puente único hacia las pasarelas**. Este plan adapta ese patrón a My Idea sin reinventarlo, respetando dos reglas del fundador:

1. **La página web es libre; el motor exige cuenta.** Son dos superficies distintas. La web pública (landing, precios, guía, legal) no tiene muro, jamás. El motor (el producto interactivo con sus packs), al que se entra *desde* la web, requiere una cuenta real autenticada.
2. **Nadie pierde un crédito por un fallo del sistema.** Todo cobro que no entrega su resultado se reembolsa.

El cobro real (pasarelas) queda para después de validar la mecánica con **créditos de cortesía** en beta cerrada — lo único que ETAPA 2 dejaría funcional.

---

## 1. Lo verificado en la referencia (I Ching) y su veredicto

Cada mecanismo se leyó en su archivo real y se clasificó: **(R)** reutilizable tal cual · **(A)** reutilizable adaptado · **(N)** específico del I Ching, no aplica.

| # | Mecanismo | Archivo real verificado | Veredicto |
|---|-----------|--------------------------|-----------|
| 1 | **Ledger de saldo** `query_credits` (`credits_total`, `credits_used`, `total_purchased`, `last_pack`), balance-based sin ciclos | `021_consumable_tokens.sql` | **A** |
| 2 | **Consumo atómico** `consume_token(user, n)`: un solo `UPDATE … WHERE credits_total >= n RETURNING credits_total`; devuelve `-1` si no alcanza. `SECURITY DEFINER`, `search_path=public` | `032_atomic_token_consumption.sql` | **R** (patrón) |
| 3 | **Grant idempotente** `grant_tokens_idempotent(event_hash, …)`: INSERT en tabla de eventos (`event_hash UNIQUE`) → si `unique_violation (23505)` devuelve `already_processed`; si no, `PERFORM grant_tokens` → `granted`. **Todo en una transacción**: un fallo nunca produce doble crédito | `039_atomic_webhook_grant.sql` | **R** |
| 4 | **Idempotencia de webhook** tabla `revenuecat_webhook_events(event_hash UNIQUE, event_type, app_user_id, processed_at)` | `005_revenuecat_webhook_idempotency.sql` | **R** |
| 5 | **Refund** `refund_token(user, tokens, reason)`: compensa un consumo tras fallo post-cobro; `credits_total += tokens`, `credits_used -= tokens` (piso 0); registra en `token_refund_log`; `tokens=0` = registro de auditoría sin reembolso | `072_refund_token.sql` | **R** |
| 6 | **Cortesía/free blindado** `init_free_user(user)` + `user_trial_log`: otorga el saldo inicial **una sola vez**, imposible re-otorgar aunque se borre y recree la fila de saldo (log inmutable por user_id) | `022_user_trial_log.sql` | **A** |
| 7 | **Postura de seguridad** de todas las RPC: `SECURITY DEFINER` + `SET search_path=public` + `REVOKE EXECUTE FROM PUBLIC, anon, authenticated` + `GRANT … TO service_role`; RLS deny-all (sin policies) en tablas internas | `024`, `035`, `060` | **R** |
| 8 | **Bridge de compra** `sync-billing` + webhook RevenueCat → `grant_tokens_idempotent` | `apps/web/src/app/api/account/sync-billing/` | **A** |
| 9 | 2FA/TOTP, replay guard, intentos | `016`, `011`, `030` | **A** (refinamiento de lanzamiento) |
| 10 | Product IDs de RevenueCat hardcodeados/sagrados; tiers por `last_pack`; imágenes por tier | `token-packs.ts`, `credits.ts` | **N** (My Idea define los suyos desde cero) |

### 1.1 Discrepancias detectadas (verificar-antes-de-construir)

1. **El prompt sitúa `consume_token`/`grant_tokens` "en su forma final en 024 y 022".** La versión **atómica** real de `consume_token` está en **`032`**, y el grant idempotente en **`039`**. El diseño se basa en 032/039 (las 024/022 son versiones previas o parciales).
2. **My Idea ya tiene la mitad del andamiaje de beta cerrada:** magic-link + allowlist (`beta_allowlist`, migración 008, solo service-role) en `web/app/api/auth/magic-link/route.ts`, y los puntos de cobro ya validan contra `web/lib/precios.ts` "con créditos stub". "Reactivar" es, en gran parte, **re-cablear** lo que existe, no construir de cero.
3. **La regla vigente del `proxy.ts`** (fundador, 2026-07-09) es "web abierta, ningún muro jamás", con **identidad invisible de invitado**. La beta cerrada del motor va en sentido contrario; el propio `proxy.ts` ya anticipa el puente ("el login real… podrá vincularse a la identidad silenciosa conservando sus ideas"). Se resuelve con la frontera web/motor (§2.1).

---

## 2. Diseño para My Idea

### 2.1 La frontera: web libre, motor autenticado

Decisión del fundador: **son dos cosas distintas.**

- **Página web pública** — landing `/`, `/precios`, `/guia`, `/privacy`, `/terms`: **abierta, sin muro.** No cambia.
- **El motor con sus packs** — `/nueva`, `/ideas`, `/idea/[id]` y su superficie de API (`/api/organizer`, `/api/session/*`, `/api/project/*`, `/api/project/*/world/*`, `/api/project/*/report`): **requiere cuenta real** (magic-link + allowlist en beta cerrada). Se entra al motor desde la web.

**Efecto en `proxy.ts`:** deja la web pública intacta y **exige auth real en la frontera del motor**, en lugar de acuñar un invitado invisible. La identidad invisible se retira para el motor. Las ideas creadas por invitados en la beta abierta reciben un **camino de reclamo/vinculación** al autenticarse (conservar sus ideas), tal como el proxy ya lo anticipaba.

> **Sub-decisión abierta para el auditor/fundador (no bloqueante):** el **organizador es gratis** (`precios.ts: organizador = 0`), es el gancho freemium. Si el motor entero exige cuenta, probar el organizador también pediría registro, angostando el embudo. Dos variantes a decidir en la revisión:
> - **(A) Motor 100% cerrado:** hasta el organizador pide cuenta. Más simple; embudo más angosto.
> - **(B) "Un sorbo" del organizador:** una corrida del organizador permitida antes de pedir cuenta, como anzuelo; el resto del motor cerrado. Preserva el freemium; algo más de complejidad de estado.

### 2.2 Ledger de créditos (tablas nuevas)

`1 crédito = $1 USD` (canon `precios.ts`). Modelo balance-based, espejo de `query_credits`.

```sql
-- Saldo por usuario (patrón query_credits)
credit_accounts (
  user_id         uuid PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  creditos_total  integer NOT NULL DEFAULT 0,   -- saldo disponible
  creditos_usados integer NOT NULL DEFAULT 0,   -- histórico consumido
  total_comprado  integer NOT NULL DEFAULT 0,   -- histórico comprado (no cortesía)
  ultimo_pack     text    NOT NULL DEFAULT 'cortesia',
  updated_at      timestamptz NOT NULL DEFAULT now()
);

-- Caja de vidrio: cada movimiento (grant, consumo, refund)
credit_transactions (
  id               bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id          uuid NOT NULL,
  delta            integer NOT NULL,              -- +grant / -consumo / +refund
  saldo_resultante integer NOT NULL,
  tipo             text NOT NULL,                 -- 'grant' | 'consumo' | 'refund'
  concepto         text,                          -- ConceptoPrecio o pack de compra
  origen           text,                          -- 'cortesia' | 'revenuecat'
  idempotency_key  text,                          -- webhook/acción; UNIQUE parcial
  created_at       timestamptz NOT NULL DEFAULT now()
);

-- Blindaje del otorgamiento único de cortesía (patrón user_trial_log)
beta_courtesy_log ( user_id uuid PRIMARY KEY, granted_at timestamptz NOT NULL DEFAULT now() );

-- Idempotencia de webhooks (tal cual 005)
revenuecat_webhook_events ( id bigserial PK, event_hash text UNIQUE NOT NULL, event_type text, app_user_id uuid, processed_at timestamptz DEFAULT now() );

-- Auditoría de reembolsos (tal cual 072)
token_refund_log ( id bigint GENERATED ALWAYS AS IDENTITY PK, user_id uuid NOT NULL, tokens integer NOT NULL, reason text, created_at timestamptz DEFAULT now() );
```

Todas con **RLS habilitada**. `credit_accounts`/`credit_transactions` legibles por su dueño (policy `own`); tablas internas (`beta_courtesy_log`, `revenuecat_webhook_events`, `token_refund_log`) **deny-all** (solo service-role las toca vía RPC).

### 2.3 RPCs atómicas — el consumo NUNCA en el código de la app

Todas `SECURITY DEFINER`, `SET search_path=public`, `REVOKE` de public/anon/authenticated, `GRANT` solo a `service_role`.

| RPC | Firma | Qué hace |
|-----|-------|----------|
| `consumir_creditos` | `(p_user uuid, p_concepto text, p_monto int) → int` | `UPDATE … WHERE creditos_total >= p_monto RETURNING`; escribe `credit_transactions` en la misma transacción; devuelve saldo restante o **`-1`** si no alcanza (patrón 032) |
| `otorgar_creditos` | `(p_user, p_monto, p_origen, p_idempotency_key) → int` | suma al saldo + transacción; idempotente por `idempotency_key` |
| `otorgar_cortesia` | `(p_user) → void` | otorga el saldo de cortesía **una sola vez** vía `beta_courtesy_log` (patrón `init_free_user`) |
| `otorgar_creditos_idempotente` | `(p_event_hash, p_event_type, p_user, p_monto, p_pack) → text` | webhook: INSERT en `revenuecat_webhook_events` → `already_processed` / `granted` (patrón 039) |
| `reembolsar_creditos` | `(p_user, p_monto, p_motivo) → int` | compensa un consumo tras fallo; `+total`, `-usados` (piso 0); `token_refund_log` (patrón 072) |

### 2.4 Mapa de puntos de cobro (hoy stubs → `consumir_creditos`)

Cada ruta ya valida `precios.ts` "con crédito stub"; se re-cablea al consumo atómico real, cobrando **al entregar** (o con refund si falla después de cobrar).

| Ruta | Concepto (`precios.ts`) | Créditos |
|------|--------------------------|----------|
| `api/session/[id]/plan` (generar plan) | `plan_completo` | **5** |
| `api/project/[id]/follow` | `seguimiento` | **2** |
| `api/project/[id]/report` (tus números) | `tus_numeros` | **2** |
| `api/project/[id]/world/[pack]/unlock` | `mundo_activar` | **3** |
| ciclo de seguimiento dentro de un mundo | `mundo_seguimiento` | **2** |
| `api/organizer` | `organizador` | **0** (gancho gratis; no cobra) |

### 2.5 RevenueCat como puente único

La app **nunca** habla con Stripe ni con Google Play directamente: siempre con RevenueCat.

```
Compra (web: Stripe vía RevenueCat · APK: Play vía RevenueCat)
      → webhook RevenueCat → POST /api/account/sync-billing
      → verificar firma (REVENUECAT_WEBHOOK_SECRET)
      → event_hash = hash(payload)
      → otorgar_creditos_idempotente(event_hash, tipo, user, monto, pack)
      → 'granted' | 'already_processed'
```

El mismo endpoint sirve a las dos caras de My Idea (web y APK) **sin rehacerse**.

---

## 3. Migraciones propuestas (numeradas 020+, marcadas `NO APLICAR`)

Convención My Idea: `supabase/migrations/my_idea_0XX_*.sql` + bloque `UNION ALL` en `my_idea_check_migraciones.sql` (que sigue siendo **SQL plano de pegar-y-correr, sin RPC** — el script de verificación no depende de funciones). La última migración viva es `019`; las nuevas parten de **020**. Cada archivo abre con:

```sql
-- NO APLICAR hasta aprobación del fundador (ETAPA 2).
```

Reparto tentativo (a afinar en la escritura de ETAPA 1):
- **020** — `credit_accounts` + `credit_transactions` + RLS/policies.
- **021** — RPCs `consumir_creditos` / `otorgar_creditos` (+ seguridad).
- **022** — cortesía: `beta_courtesy_log` + `otorgar_cortesia`.
- **023** — RevenueCat: `revenuecat_webhook_events` + `otorgar_creditos_idempotente`.
- **024** — refund: `token_refund_log` + `reembolsar_creditos`.

---

## 4. Orden de construcción (dependencias + reversibilidad)

| Paso | Qué | Depende de | Reversible |
|------|-----|-----------|------------|
| **(a)** | **Beta cerrada + cortesía** — gate del motor a auth real (magic-link + allowlist ya existen) + `otorgar_cortesia` al invitado allowlisted + vinculación de ideas del invitado. **Único alcance de ETAPA 2.** | 020–022 | **Sí** (sin pasarela) |
| **(b)** | **RevenueCat + Stripe (web)** — cobro real en la web | (a), 023 | Dinero real (cuidado) |
| **(c)** | **RevenueCat + Google Play (APK)** | (b) | Dinero real (cuidado) |
| **(d)** | **2FA/TOTP + dominio propio de correo** (Resend + Cloudflare) para magic links con remitente propio | (a) | **Sí** (refinamiento) |

---

## 5. Aristas cubiertas explícitamente

| Arista | Cómo se resuelve |
|--------|------------------|
| **Reembolso** | `reembolsar_creditos` compensa cualquier cobro que no entregó su resultado; regla dura: **un usuario nunca pierde créditos por un fallo del sistema**. Verificación pre-refund en la ruta (si el resultado sí quedó persistido, no se reembolsa: éxito ambiguo por respuesta HTTP perdida). |
| **Idempotencia** | Webhook con `event_hash UNIQUE`; un evento repetido de RevenueCat devuelve `already_processed`, nunca doble crédito. Acciones del motor con `idempotency_key` en la transacción. |
| **Saldo insuficiente** | La RPC devuelve `-1`; la ruta no ejecuta la acción y la UI lo dice en palabras de persona: *"Te quedan X créditos; esto cuesta Y."* |
| **El fusible existente** | Sigue vivo como respaldo agregado, independiente del saldo individual (no se toca `lib/rateLimit.ts`). |
| **Migración de invitados de beta** | Las ideas del invitado se vinculan a su cuenta real al autenticarse; su `origen='cortesia'` persiste; no se rompen al activar el cobro. |
| **Concurrencia** | La atomicidad de `consumir_creditos` (un solo UPDATE con guard) impide que dos pestañas gasten el mismo crédito. Se cubre con un test de doble-consumo concurrente. |

---

## 6. Postura de seguridad (heredada del I Ching)

- Toda RPC de créditos: `SECURITY DEFINER` + `SET search_path=public`, ejecutable **solo por `service_role`** (REVOKE de public/anon/authenticated). La app llama con la service-role key desde el servidor, nunca desde el cliente.
- Tablas internas (`beta_courtesy_log`, `revenuecat_webhook_events`, `token_refund_log`): RLS **deny-all**.
- `credit_accounts`/`credit_transactions`: RLS `own` (cada quien ve solo lo suyo).
- El webhook de RevenueCat verifica firma (`REVENUECAT_WEBHOOK_SECRET`) antes de tocar la DB.

---

## 7. Qué entrega ETAPA 1 (tras el visto bueno) y dónde se detiene

**Entregables de ETAPA 1** (a producir tras aprobar este plan): `docs/CUENTAS_DISENO.md` (los 10 mecanismos con su veredicto R/A/N documentado contra el código real + este diseño detallado), las **5 migraciones 020–024 escritas y marcadas `NO APLICAR`**, y el **mapa de puntos de cobro** con el diff exacto por ruta. **Detenerse ahí** para revisión del auditor y evaluación punto a punto del fundador.

**ETAPA 2 (solo tras aprobación escrita):** reactivar magic-link + allowlist en la frontera del motor + implementar SOLO las RPC de consumo/otorgamiento/cortesía y cablear los puntos de cobro, con créditos de cortesía como única fuente. Pasarelas (RevenueCat/Stripe/Play), TOTP y dominio de correo quedan **después** de la validación del fundador. Suites verdes en clon limpio. Commits `Cuentas:`. No tocar `main`. No aplicar migraciones sin confirmación.

---

## 8. Preguntas abiertas para el auditor

1. **Frontera del organizador** (§2.1): ¿motor 100% cerrado, o "un sorbo" del organizador antes de pedir cuenta?
2. **Monto de cortesía:** ¿cuántos créditos de cortesía por invitado de beta? (p. ej. suficientes para 1 plan + 1 seguimiento + 1 mundo ≈ 10).
3. **Cobro al inicio vs. a la entrega:** ¿cobrar `plan_completo` al empezar la exploración o al entregar el plan? (El diseño propone **cobrar al entregar**, con refund como red; a confirmar.)
4. **Vinculación de invitados:** ¿se conservan las ideas de la beta abierta (vincular invitado→cuenta) o se parte de cero al cerrar la beta?
