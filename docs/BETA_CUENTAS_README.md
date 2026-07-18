# Beta con cuentas y créditos — el manual de operación (ETAPA 2)

Fase: identidad y créditos (rama `beta-identidad-creditos`, tag `web-v1.5.0-beta`).
Diseño: [CUENTAS_DISENO.md](CUENTAS_DISENO.md). Migraciones 020-024: **aplicadas**.
La beta corre 100% con cortesía (20 créditos por invitado); **ninguna pasarela activada**.

## 1. Cómo funciona (el resumen de una pantalla)

- **Libre sin login:** la web pública y el ORGANIZADOR (el gancho). La identidad
  invisible sigue existiendo solo para eso.
- **El login nace en "Iniciar La Exploración"**: magic link + allowlist (3.2).
  Al confirmar: los proyectos del anónimo se **adoptan** (la cookie del propio
  request es la prueba de posesión) y la cuenta recibe su **cortesía: 20
  créditos, una sola vez** (`beta_courtesy_log`).
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

### b) Entrar por primera vez

1. `https://my-idea-psi.vercel.app/login` → tu email → clic en el enlace del correo.
2. Al confirmar: cortesía 20 otorgada + destino `/ideas`.

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
- Las demás (`SUPABASE_*`, `ANTHROPIC_API_KEY`, `VUELO_DEV_PASSWORD`) no cambian.

## 3. Estado vivo vs dormido

| Pieza | Estado |
|---|---|
| Ledger 020-024 (RPCs atómicas, RLS, courtesy log, refund log) | **VIVO** |
| Cortesía 20 al primer login | **VIVO** |
| Los 5 puntos de cobro + 402 + idempotencia + refund | **VIVOS** (se pagan con cortesía) |
| Magic link + allowlist + adopción al login | **VIVO** |
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
