# AUDITORÍA DE PARIDAD DE MUNDOS — My Idea
Pregunta del fundador: **¿los mundos ven el proyecto ACTUAL y reciben el mismo
trato que el core?** Verificación V1–V5 antes de arreglar nada; con este reporte
el auditor y el fundador deciden qué entra pre-beta y qué va al backlog.

- **Fecha:** 2026-07-15 · **Contra:** `main` = `3ac2edc`
- **Costo de la auditoría: $0.** La prueba viva de V1 ya estaba contenida en el
  último vuelo (su fase de mundos corre después del ciclo de seguimiento); el
  resto salió de leer el código y de reproducir consultas contra lo persistido.
- **Método:** nada se afirma sin evidencia — `archivo:línea` o resultado real.

## Resumen

| Verificación | Veredicto |
|---|---|
| V1 · Frescura del `estado_vivo` en los mundos | ✅ **Pasa** (probado en vivo) |
| V2 · La brecha ignora el avance del checklist | ⚠️ **Confirmado** |
| V3a · Los ítems de mundo nunca reciben fecha | ⚠️ **Confirmado** |
| V3b · El Análisis excluye los mundos | ⚠️ **Confirmado** |
| V4 · El follow puede tomar ítems de otro dominio | ⚠️ **Confirmado** (latente, alcanzable) |
| V5 · Trato visual y paridad de tracking | ✅ **Paridad** |

---

## V1 · FRESCURA — ✅ PASA (con un matiz de diseño)

`projects.estado_vivo` tiene **un solo punto de escritura**:
`app/api/session/[id]/plan/route.ts:304`. Esa ruta sirve a **core, mundos y
seguimientos por igual** → se reescribe tras **cada** plan. No quedó congelado en
la sesión inicial.

`world/[pack]/start/route.ts` lo lee (`:85`) y lo pasa a los tres sitios que
importan:
- la **brecha** (`:87`),
- el **mensaje de la sesión** (`"Contexto actual: …"`, `:117`),
- el **perfilSesion** del intérprete (`:125`).

**Prueba viva** (del último vuelo; sus mundos corren tras el seguimiento core).
`mensaje_entrada` reales de la base:

| Sesión | Creada | Contexto con que arrancó |
|---|---|---|
| seguimiento core | 16:59 | *(el ciclo que cambia la realidad)* |
| mundo `quality` | 17:02 | "costos actualizados $102-130… ha logrado **reducir costos de cemento en un 20%**… 12 macetas mensuales a **$250, manteniendo volumen tras el aumento**" |
| mundo `seguridad_digital` | 17:04 | "…tras reducir 20% el costo de cemento… pero **carece del desglose real de ventas por canal**" |
| mundo `risk_management` | 17:06 | "…**dos clientes mayoristas esperan respuesta** en modelo B2B" |

Los mundos ven la realidad post-seguimiento, y cada uno más fresco que el anterior.

**El matiz (diseño deliberado, no bug):** la **primera pregunta** del mundo es la
**cacheada de la semilla** que eligió la brecha — determinística, cero LLM
(`world/start:131-139`). No la del intérprete. Es una decisión de v1.3.2 que **el
vuelo cazó dos veces**: con un `estado_vivo` cargado de urgencias core, el
intérprete juzgaba la semilla "desalineada" y salía en el turno 0 — y el usuario
había pagado por explorar *ese* mundo. Desde el turno 2 el intérprete manda como
siempre. Conclusión: la pregunta no refleja el estado *textualmente*; lo refleja
la **puerta elegida**, que sí se escoge con el estado fresco.

## V2 · LA BRECHA Y EL AVANCE — ⚠️ CONFIRMADO

`evaluacionBrecha(pack, estadoVivo, tipoOferta, faseActual, cubiertos)`
(`lib/engine/evaluacionBrecha.ts`). **El checklist no es una entrada.** Decide por:
1. el mapa aprobado fase→semilla (`brecha_semillas.json`),
2. la cercanía de fase (`ORDEN_FASES`),
3. el solape de tokens con `estadoVivo + tipoOferta`.

**Un usuario con 80% ejecutado que abre un mundo: la brecha no lo sabe.** Solo ve
`fase_actual` (proxy grueso, sí actualizado por plan) y la prosa del
`estado_vivo`. No distingue "planificado" de "ejecutado", ni sabe **dónde está
atascado** — justo la señal que el bloque de realidad (Fase 4.0 §3) ya calcula
para el core y que aquí no llega.

## V3 · FECHAS DE MUNDO — ⚠️ DOS HALLAZGOS

**(a) El ritual de fechas es core-only.** `app/ui/ManosALaObra.tsx:812`:
`itemsCore = core?.etapas.flatMap(...)` → `RitualFechas items={itemsCore}`. Los
ítems de mundo **nunca reciben sugerencia de fecha**. El interruptor "recalcular
pendientes" filtra el mismo `itemsCore`: **no los ve**. Un mundo activado después
de confirmada la baseline core queda sin fechas de forma permanente.

**(b) El Análisis excluye los mundos.** `lib/analyticsEntrada.ts:54`
`.filter((i) => esCore(i.dominio))`, y los planes igual (`:40`). **No hay
cumplimiento de ítems de mundo**: aunque tuvieran fecha, no se contarían.

Consecuencia combinada: los mundos viven **fuera del sentido del tiempo**
(Fase 3.8) y fuera del bucle de tracking (Fase 4.0).

## V4 · EL BLOQUE DE REALIDAD POR DOMINIO — ⚠️ CONFIRMADO (distinto al previsto)

**No existe un follow de mundo.** El único follow (`follow/route.ts:136`) siempre
hace `crearSesion(..., "seguimiento", mensaje)` sin dominio → **core**. La premisa
"el follow de un mundo" no aplica hoy; el bloque core-only es coherente con eso.

**Pero hay un bug latente y alcanzable:** la consulta del follow **no filtra por
dominio** (`follow/route.ts:88-100`) y toma `ultimoPlanId = filas[0].plan_id` — el
ítem más reciente del proyecto, sea del dominio que sea. **Si el usuario explora
un mundo y luego pulsa "Contar qué pasó", el follow core compone su "mi avance
real" con el checklist del MUNDO**, mientras el bloque de realidad lleva
cumplimiento **core**: el mensaje y el bloque describirían dominios distintos.

**Honestidad sobre la evidencia:** se reprodujo la consulta exacta del follow
sobre los datos del vuelo y **no se manifestó** — a las 17:09:52 el ítem más
reciente era core (17:09:49), porque el vuelo encadena un seguimiento core justo
antes de ese follow. Fue **suerte del orden**, no diseño. El flujo real de la UI
(explorar un mundo → "Contar qué pasó") lo alcanza.

## V5 · TRATO VISUAL COMPLETO — ✅ PARIDAD (matiz menor)

- **El plan del mundo** (`ManosALaObra.tsx:1109`) usa **el mismo `<PlanDocumento>`**
  que el core → "Tu primera acción" siempre visible, acordeones, Entregable como
  subtítulo, prosa justificada y pasos uniformes.
- **El checklist del mundo** (`:1095`) usa **el mismo `<GrupoEtapas>`** que el core
  (`:1059`), que renderiza `<FilaItem>` → los 4 estados de un toque, "¿Cuándo lo
  hiciste?" y las notas. **Paridad de tracking completa.**
- Matiz menor: el plan de mundo no recibe `nodosFuente` → sin sidebar "Construido
  con tu recorrido". Discutible si es fallo: vive dentro de Manos a la Obra, no en
  la vista del plan.

---

## Lectura para la decisión (del ejecutor; la decisión es del fundador)

- **V4** es el único que **corrompe el dato que llega al motor** (le describe el
  dominio equivocado) y es barato: un filtro de dominio en la consulta del follow.
- **V3a/V3b** son un hueco de producto **coherente consigo mismo** (los mundos
  quedaron fuera del sentido del tiempo). Meterlos pide una decisión de diseño
  —¿una baseline por dominio? ¿cumplimiento por mundo en el Análisis?— no un
  parche.
- **V2** es el más profundo: darle el avance real a la brecha es fácil
  técnicamente, pero **cambia qué puerta elige** para el usuario. Merece criterio,
  no prisa.
