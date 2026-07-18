# Diseño — Sistema de cuentas y créditos de My Idea (ETAPA 1)

**Estado:** entregable de diseño de ETAPA 1. **Decisiones del fundador locked.** Migraciones **escritas y NO aplicadas**; pasarelas **no activadas**; puntos de cobro **no cableados en vivo** (diffs preparados, abajo). Doble freno: esto llega hasta el borde de lo reversible y se detiene ahí.
**Rama:** `cuentas-y-creditos`. No toca `main` ni `staging`.
**Antecede:** [`docs/CUENTAS_PLAN.md`](CUENTAS_PLAN.md) (plan aprobado en arquitectura por el auditor).
**Referencia probada:** The Original I Ching (`referencia/iching-app/`, en `.gitignore`).

---

## 0. Decisiones del fundador (locked)

1. **Web libre, motor autenticado.** La página web pública (landing, precios, guía, legal) no tiene muro. El motor con sus packs exige cuenta real. Son dos cosas distintas; al motor se entra desde la web.
2. **El organizador es gratis y sin login** (el gancho freemium). El **login y la cuenta nacen al pulsar "Iniciar La Exploración"** — el primer acto que cuesta créditos. La cuenta nace en el primer valor pagado, no antes.
3. **Cortesía = 20 créditos** por invitado de beta (alcanza un ciclo completo con holgura: plan 5 + números 2 + un par de seguimientos + activar uno o dos mundos).
4. **Cobrar a la entrega, con verificación de saldo al inicio.** Se valida saldo suficiente antes de arrancar (rechazo limpio si no alcanza); el crédito se descuenta **cuando la generación se completa con éxito**; si el sistema falla a mitad, **cero cobro**. El refund cubre el caso raro de fallo *tras* el cobro.
5. **Créditos de cortesía atados al `user_id` con `origen='cortesia'` inmutable.** Persisten intactos cuando llegue el cobro real y conviven con los comprados.

---

## 1. Mecanismos del I Ching, verificados contra el código real

`R` reutilizable tal cual · `A` reutilizable adaptado · `N` no aplica.

| Mecanismo | Archivo real | Veredicto | Adaptación en My Idea |
|-----------|--------------|-----------|-----------------------|
| Ledger de saldo `query_credits` | `021_consumable_tokens.sql` | **A** | `credit_accounts` (migr. 020) |
| Consumo atómico `consume_token` (UPDATE con guard, −1 si no alcanza) | `032_atomic_token_consumption.sql` | **R** | `consumir_creditos` (021) |
| Grant idempotente `grant_tokens_idempotent` (dedup+grant en 1 tx) | `039_atomic_webhook_grant.sql` | **R** | `otorgar_creditos_idempotente` (023) |
| Tabla de idempotencia de webhook | `005_revenuecat_webhook_idempotency.sql` | **R** | `revenuecat_webhook_events` (023) |
| Refund `refund_token` + log | `072_refund_token.sql` | **R** | `reembolsar_creditos` (024) |
| Cortesía única `init_free_user` + `user_trial_log` | `022_user_trial_log.sql` | **A** | `otorgar_cortesia` + `beta_courtesy_log` (022) |
| Postura de seguridad (SECURITY DEFINER + search_path + REVOKE/GRANT service_role; RLS deny-all internas) | `024`, `035`, `060` | **R** | todas las RPC 021–024 |
| Bridge de compra `sync-billing` → grant idempotente | `apps/web/.../account/sync-billing/` | **A** | ETAPA 2/b |
| 2FA/TOTP + replay guard | `016`, `011`, `030` | **A** | ETAPA 2/d (refinamiento) |
| Product IDs sagrados; tiers por `last_pack` | `token-packs.ts`, `credits.ts` | **N** | My Idea define los suyos |

> **Discrepancia confirmada (verificar-antes-de-construir):** el prompt situaba la lógica atómica en `024`/`022`; la real está en **`032`** (consumo) y **`039`** (grant idempotente). El diseño se basa en las correctas.

---

## 2. La frontera: web libre / motor autenticado

- **Web pública** — `/`, `/precios`, `/guia`, `/privacy`, `/terms`: abierta, sin muro. No cambia.
- **El organizador** (`/api/organizer`, `/api/organizer/stream`): **gratis y sin login** (precio 0). Es el gancho.
- **El motor con packs** — a partir de **"Iniciar La Exploración"** (`/api/session/start`) y todo lo que sigue (`/api/session/*`, `/api/project/*`, `world/*`, `report`): **exige cuenta real** (magic-link + allowlist, ya existentes en `web/app/api/auth/magic-link/route.ts`, tabla `beta_allowlist` migr. 008).

**Efecto en `proxy.ts` (ETAPA 2, no ahora):** la web pública queda intacta; el gate de auth real se aplica en la frontera del motor en lugar de acuñar el invitado invisible. Las ideas creadas como invitado se vinculan a la cuenta real al autenticarse (el propio `proxy.ts` ya lo anticipa: *"vincularse… conservando sus ideas"*).

---

## 3. El ledger (migración 020)

Dos tablas + blindaje + idempotencia (esquema exacto en `supabase/migrations/my_idea_020_creditos_ledger.sql`):

- **`credit_accounts`** — `user_id` (PK→auth.users), `creditos_total`, `creditos_usados`, `total_comprado`, `ultimo_pack`, `updated_at`. CHECK no-negativo.
- **`credit_transactions`** — caja de vidrio: `delta`, `saldo_resultante`, `tipo` (`grant|consumo|refund`), `concepto`, `origen` (`cortesia|revenuecat`), `idempotency_key` (**UNIQUE parcial** → una acción aplica una sola vez), `created_at`.
- **RLS:** `credit_accounts`/`credit_transactions` legibles solo por su dueño (`user_id = (SELECT auth.uid())`); **ninguna** policy de escritura → solo las RPC service-role mutan.

Tablas internas (`beta_courtesy_log`, `revenuecat_webhook_events`, `credit_refund_log`): RLS **deny-all**.

---

## 4. Las RPCs atómicas (migraciones 021–024)

Todas `SECURITY DEFINER`, `SET search_path=public`, `REVOKE` de public/anon/authenticated, `GRANT` solo a `service_role`. La app las llama con la **service-role key desde el servidor**, nunca desde el cliente.

| RPC | Migr. | Devuelve | Núcleo |
|-----|-------|----------|--------|
| `consumir_creditos(user, concepto, monto, idem?)` | 021 | saldo o **−1** | UPDATE atómico `WHERE creditos_total >= monto`; idempotente por clave |
| `otorgar_creditos(user, monto, origen, idem?, pack?)` | 021 | saldo | suma (ON CONFLICT); idempotente |
| `otorgar_cortesia(user, monto=20)` | 022 | saldo | otorga **una vez** vía `beta_courtesy_log` |
| `otorgar_creditos_idempotente(event_hash, tipo, user, monto, pack)` | 023 | `granted`\|`already_processed` | dedup + grant en 1 tx (webhook) |
| `reembolsar_creditos(user, monto, motivo?)` | 024 | saldo | +total, −usados (piso 0); `credit_refund_log` |

---

## 5. Modelo de cobro: verificar al inicio, descontar a la entrega

Materializa la decisión 4. **La verificación** (¿alcanza el saldo?) ocurre en el acto que *inicia* la unidad facturable; **el descuento** ocurre cuando esa unidad se *entrega* con éxito. Un fallo a mitad no cobra. La idempotencia (clave por sesión) impide doble cobro en reintentos.

| Unidad facturable | Acto que la inicia → **verifica** saldo | Ruta de entrega → **descuenta** | Concepto (`precios.ts`) | Créditos | `idempotency_key` |
|-------------------|------------------------------------------|----------------------------------|--------------------------|----------|--------------------|
| Plan core (1ª vez) | `session/start` ("Iniciar La Exploración") | `session/[id]/plan` (al persistir el plan) | `plan_completo` | **5** | `plan:{sessionId}` |
| Seguimiento core | `project/[id]/follow` | `session/[id]/plan` (esSeguimiento) | `seguimiento` | **2** | `plan:{sessionId}` |
| Activar mundo | `world/[pack]/unlock` (instantáneo) | *el mismo unlock* | `mundo_activar` | **3** | `unlock:{projectId}:{pack}` |
| Seguimiento de mundo | inicio del follow del mundo | `session/[id]/plan` (dominio=pack, esSeguimiento) | `mundo_seguimiento` | **2** | `plan:{sessionId}` |
| Tus números | `project/[id]/report` | *la misma respuesta del reporte* | `tus_numeros` | **2** | `report:{reportId}` |
| Organizador | — | — | `organizador` | **0** | — |

**Regla de concepto en `session/[id]/plan`** (resuelve la unidad por la sesión): `core + inicial/completo → plan_completo(5)` · `core + seguimiento → seguimiento(2)` · `pack + inicial → 0` (ya cubierto por `mundo_activar`) · `pack + seguimiento → mundo_seguimiento(2)`.

**Carrera rara (verificó al inicio, otra pestaña gastó antes de la entrega):** al descontar, `consumir_creditos` devuelve −1 pese a que la generación ya se produjo. Política: **entregar y registrar** (nunca castigar al usuario ni cobrar de más), coherente con la regla sagrada. Es el único caso de entrega sin cobro y queda en la bitácora.

---

## 6. Cableado de los puntos de cobro — **diff preparado, NO aplicado**

Estos son los cambios que ETAPA 2 aplicará (el "cableado vivo"). Aquí quedan **preparados y sin aplicar** (aplicarlos ahora, con las RPC aún inexistentes, rompería las rutas). Todos consumen vía una capa fina `web/lib/creditos.ts` (nueva, ETAPA 2) que envuelve las RPC con la service-role key: `verificarSaldo(user, monto)`, `cobrar(user, concepto, monto, idemKey)`, `reembolsar(...)`, `otorgarCortesia(user)`.

### 6.1 `web/lib/precios.ts` — sin cambios
Ya es el canon (`plan_completo 5, seguimiento 2, tus_numeros 2, mundo_activar 3, mundo_seguimiento 2, organizador 0`). Las rutas leen de aquí; nada hardcodeado.

### 6.2 `web/app/api/session/start/route.ts` — verificar al inicio (plan_completo)
Tras el fusible/límite (donde hoy dice *"Pre-beta: fusible global ANTES de cobrar creditos"*), y **solo para sesiones core no-seguimiento**:
```ts
// ETAPA 2: la Exploración cuesta plan_completo; verificar (no cobrar) al inicio.
const saldo = await verificarSaldo(user.id, PRECIOS.plan_completo);
if (!saldo.alcanza) {
  return NextResponse.json(
    { error: `Te quedan ${saldo.creditos} créditos; iniciar la exploración cuesta ${PRECIOS.plan_completo}.` },
    { status: 402 }
  );
}
```

### 6.3 `web/app/api/project/[id]/follow/route.ts` — verificar al inicio (seguimiento)
Mismo patrón, tras el fusible (línea ~82), con `PRECIOS.seguimiento` (o `mundo_seguimiento` si el follow es de un mundo).

### 6.4 `web/app/api/session/[id]/plan/route.ts` — descontar a la entrega
Dos toques:
- **Antes de abrir el stream** (línea ~143): repetir la verificación de saldo por el concepto resuelto (core inicial→5, core seguimiento→2, pack→0/2). 402 limpio si no alcanza.
- **Tras `guardarPlan` con éxito** (línea ~239), antes del `enviar("done", …)`:
```ts
// ETAPA 2: cobrar a la entrega, idempotente por sesión. Pack inicial = 0 (ya cobrado en unlock).
const monto = montoDelPlan(dominioSesion, recorrido.esSeguimiento); // 5 | 2 | 0
if (monto > 0) {
  const saldo = await cobrar(user.id, conceptoDelPlan(dominioSesion, recorrido.esSeguimiento), monto, `plan:${sessionId}`);
  // saldo === -1 (carrera): el plan ya está guardado → entregar y registrar, nunca cobrar de más.
}
```
El evento `done` incluye `creditos_restantes` para que la UI refresque el saldo (patrón del I Ching: `remainingCredits` en la respuesta).

### 6.5 `web/app/api/project/[id]/world/[pack]/unlock/route.ts` — verificar + descontar (instantáneo)
El unlock es instantáneo (no hay generación que pueda fallar a mitad): verificar y descontar juntos, idempotente por `unlock:{projectId}:{pack}`. Hoy inserta `creditos_pagados: entrada.creditos_activar` (stub); ETAPA 2 antepone el `cobrar(...)` real y mantiene el registro.

### 6.6 `web/app/api/project/[id]/report/route.ts` — descontar a la entrega (tus_numeros)
Verificar `PRECIOS.tus_numeros` al inicio; descontar al entregar el reporte, idempotente por `report:{reportId}`. (Las regeneraciones del mismo reporte no re-cobran: misma clave.)

### 6.7 UI (ETAPA 2)
Saldo visible; en 402, mensaje en palabras de persona *("Te quedan X créditos; esto cuesta Y")*; refresco de saldo tras cada cobro con el `creditos_restantes` de la respuesta.

---

## 7. RevenueCat como puente único (ETAPA 2/b — pasarelas, NO ahora)

```
Compra (web: Stripe vía RevenueCat · APK: Play vía RevenueCat)
  → webhook → POST /api/account/sync-billing
  → verificar firma (REVENUECAT_WEBHOOK_SECRET)
  → event_hash = hash(payload)
  → otorgar_creditos_idempotente(event_hash, tipo, user, monto, pack)  // 'granted' | 'already_processed'
```
El mismo endpoint sirve web y APK sin rehacerse. Los product IDs de My Idea se definen desde cero (no se heredan los del I Ching). **Nada de esto se activa en ETAPA 1 ni en el paso (a) de ETAPA 2.**

---

## 8. Seguridad (heredada del I Ching)

- Toda RPC de créditos: `SECURITY DEFINER` + `SET search_path=public`, ejecutable **solo por `service_role`**.
- Tablas internas (`beta_courtesy_log`, `revenuecat_webhook_events`, `credit_refund_log`): RLS **deny-all**.
- `credit_accounts`/`credit_transactions`: RLS `own` (cada quien ve solo lo suyo).
- El webhook verifica firma antes de tocar la DB.
- La service-role key vive solo en el servidor; el cliente jamás llama a las RPC.

---

## 9. Migraciones (numeradas 020–024, `NO APLICAR`)

| Archivo | Contenido |
|---------|-----------|
| `my_idea_020_creditos_ledger.sql` | `credit_accounts` + `credit_transactions` + RLS |
| `my_idea_021_creditos_rpc_consumo.sql` | `consumir_creditos` + `otorgar_creditos` |
| `my_idea_022_creditos_cortesia.sql` | `beta_courtesy_log` + `otorgar_cortesia` (20) |
| `my_idea_023_creditos_revenuecat.sql` | `revenuecat_webhook_events` + `otorgar_creditos_idempotente` |
| `my_idea_024_creditos_refund.sql` | `credit_refund_log` + `reembolsar_creditos` |

Al aplicarse (ETAPA 2) se añadirá su bloque `UNION ALL` a `my_idea_check_migraciones.sql` (SQL plano de pegar-y-correr, sin RPC), verificando presencia de cada tabla y función. **No se toca ese archivo en ETAPA 1** para no reportar en rojo lo aún no aplicado.

---

## 10. Aristas (cómo se resuelve cada una)

| Arista | Resolución |
|--------|-----------|
| Reembolso | `reembolsar_creditos` compensa cobros que no entregaron; verificación pre-refund en la ruta (si el resultado sí quedó persistido, no se reembolsa). |
| Idempotencia | webhook `event_hash UNIQUE`; acciones del motor con `idempotency_key` (índice único parcial) → reintentos no doble-cobran. |
| Saldo insuficiente | RPC devuelve `−1`; ruta responde 402 con mensaje humano. |
| Fusible existente | intacto (`lib/rateLimit.ts`), respaldo agregado independiente del saldo. |
| Migración de invitados | ideas del invitado se vinculan a la cuenta real; `origen='cortesia'` persiste. |
| Concurrencia | atomicidad del UPDATE con guard; **test de doble-consumo concurrente** en ETAPA 2. |
| Cortesía repetida | `beta_courtesy_log` (PK) bloquea re-otorgar aunque se borre `credit_accounts`. |

---

## 11. Qué NO se hizo (el doble freno)

- ❌ **Ninguna migración aplicada** (las 020–024 abren con `-- NO APLICAR`).
- ❌ **Ninguna pasarela activada** (RevenueCat/Stripe/Play): esquema definido, endpoint y claves en ETAPA 2/b.
- ❌ **Ningún punto de cobro cableado en vivo**: los diffs del §6 están preparados, no aplicados (las rutas siguen intactas).
- ❌ **`proxy.ts` sin tocar**: la web sigue abierta hasta ETAPA 2.
- ❌ **TOTP/dominio de correo**: ETAPA 2/d.

## 12. Plan de pruebas para ETAPA 2 (paso a: cortesía)

1. `otorgar_cortesia` da 20 una vez; segunda llamada no re-otorga (verificar `beta_courtesy_log`).
2. `consumir_creditos` descuenta exacto y devuelve saldo; **−1** cuando no alcanza (402 en la ruta).
3. **Concurrencia:** dos `consumir_creditos` simultáneos con saldo para uno solo → uno gana, el otro −1 (nunca saldo negativo).
4. Idempotencia: reintento de `session/[id]/plan` con la misma `idempotency_key` no doble-cobra.
5. Cobro a la entrega: fallo simulado a mitad → cero cobro; fallo tras cobro → `reembolsar_creditos` restituye.
6. Suites verdes en clon limpio; sin tocar `main`. Commits `Cuentas:`.

---

**ETAPA 2 requiere aprobación escrita del fundador.** Este documento y las migraciones se detienen en el borde de lo reversible.
