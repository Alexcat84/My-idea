# Fase 3.3 (bucle de checklist) + Fase 3.5 (mundos HSEQ) — reporte de implementación

Fecha: 2026-07-10 · Rama: `staging` · Commits: `9ae5462..e91f164` (11 commits)
Suites al cierre: **web 215/215 · python 12/12 · tsc limpio**

## Qué se construyó

### Fase 3.3 — el bucle de checklist (el corazón de la retención)

| Pieza | Dónde | Nota |
|---|---|---|
| Migración 015 `checklist_items` | `supabase/migrations/my_idea_015_checklist_items.sql` | Un ítem por paso accionable del plan; checker actualizado |
| Derivador determinístico | `web/lib/engine/checklist.ts` | Patch verbatim; cero LLM, el parser es el notario |
| Wiring en la persistencia | ruta del plan → `guardarPlan` (ahora devuelve `plan_id`) → `insertarChecklist` | Solo planes `inicial\|completo\|seguimiento`; organizador y reporte jamás |
| Rutas | `GET/PATCH /api/project/[id]/checklist` | GET agrupa por plan/etapa + resumen por dominio; PATCH valida contra `CHECKLIST_ESTADO` |
| Composer | `web/lib/engine/seguimientoComposer.ts` | Patch verbatim; 3 tarjetas → mensaje "qué ha pasado" |
| Puerta avanzada | `web/lib/engine/puertaAvanzada.ts` | Port función por función de `candidatos_seguimiento` (2366) y `seleccionar_puerta_avanzada` (2398) |
| **El hueco portado** | `POST /api/project/[id]/follow` | `modo_seguir` (línea 2801) por fin en la web; sesión `seguimiento`, mensaje compuesto auditable en `sessions.mensaje_entrada`, plan resultante deriva SU checklist → bucle encadenado |
| Vuelo | FASE 2f en `web/scripts/vuelo.ts` | Ciclo completo contra Supabase real (pendiente de correr, ver "Para encender") |

### Fase 3.5 — mundos HSEQ detrás de flags

| Pieza | Dónde | Nota |
|---|---|---|
| Migración 016 | `my_idea_016_mundos.sql` | `project_unlocks` + `sessions.dominio` + `plans.dominio`; checker actualizado |
| Canon comercial | `web/lib/precios.ts` + `packs_catalog.json` | Organizador 0 · Plan 5 · Seguimiento 2 · Tus Números 2 · Activar mundo 3 · Seguimiento de mundo 2 (créditos 3/2 en catálogo, copy de producción Paso 6) |
| El muro en 4 capas | `dominiosDesbloqueados()` en db.ts; lista en `EstadoRecorrido` | Sucesores del turno (intérprete niveles 1-2), brújula de saltos, brújula dirigida, cosecha del plan, puerta avanzada |
| Rutas | `POST .../world/[pack]/unlock` y `/start` | Unlock stub idempotente con créditos del catálogo; start exige unlock (403) y plan core (409), `evaluacionBrecha` determinística (cero LLM) elige la semilla |
| Semillas horneadas | `web/lib/assets/packs_entry_seeds.json` | Las 7×3 aprobadas en P1-HSEQ con titulo/fase/condiciones (Vercel solo despliega `web/`) |
| Línea de ensamblaje | `scripts/integrar_packs.py` | **NO ejecutada** — se niega sin `bridges_aprobados.json` ×3 (verificado); secuencia a-f completa |
| Vuelo | FASE 2g | Muro 403, 404 fuera de catálogo, unlock idempotente; el ciclo positivo se autodetecta post-integración |

## Correcciones al plan (verificación previa, regla de la casa)

1. **Policies RLS**: el patch proponía `USING (project_id IN (SELECT ...))`; la forma real de `my_idea_001` es `EXISTS (... p.user_id = (SELECT auth.uid()))`. Mandó 001, como el propio plan instruía. (015 y 016 la espejan exactamente.)
2. **Segunda bomba dormida**: además de `recorrido.ts:239` (citada por el plan, exacta), la cosecha del plan en `planRedactor.ts:76` también llamaba `dominioPermitido` sin la lista. Ambas corregidas y cubiertas por `mundos.test.ts`.
3. **Paridad de `visitados`**: el port web derivaba `visitados` solo de la ruta de la sesión; `modo_seguir` usa `cubiertos ∪ ruta`. Sin el fix, el seguimiento re-ofrecería nodos ya cubiertos. Nuevo campo `nodosCubiertosPrevios` en el estado (verificado en vivo por la FASE 2f: la puerta avanzada debe caer fuera de lo cubierto).
4. **`packs_catalog.json`**: el patch mostraba forma de objeto; se conservó la forma array con `clave` (los consumidores existentes — MundosAddOn, /api/packs/interes — ya la usan). Contenido (copy + créditos) tomado del patch + tu actualización de precios.
5. **CHECKs de 016 como `ADD CONSTRAINT` nombrado** (no inline en `ADD COLUMN`): así los parsea el test de contrato y se pueden relajar por nombre.
6. **Formato de puentes**: `bridges_propuestos.json` usa `{core, dominio, score}` — `integrar_packs.py` lee ese contrato (el patch no lo especificaba).
7. **Test Python espejo de `candidatos_seguimiento`**: no existe en `engine/` (verificado) — se escribió el unitario web con puntajes a mano.

## Decisiones que debes conocer

- **El follow cobra 1 arranque** del límite diario (mismo perfil de costo que `session/start`). El world/start también.
- **Tolerancia pre-migración**: `crearSesion`/`guardarPlan` omiten `dominio` cuando es `core`, y los arranques degradan a solo-core si `project_unlocks` no existe — nada revienta entre el deploy del código y la aplicación de 015/016. **Excepción**: generar un plan SÍ requiere la 015 (el checklist se inserta al persistir) — aplicar pronto.
- **world/start pre-integración responde 503** («Este mundo se está preparando») — el mundo existe comercialmente, su contenido llega con la línea de ensamblaje.

## Para encender (en orden)

1. **TÚ**: aplicar 015 y 016 en el SQL Editor de Supabase (proyecto My-idea) y correr `my_idea_check_migraciones.sql` → 016 filas ✓.
2. **YO** (avísame): correr el vuelo completo (`npx tsx scripts/vuelo.ts` con dev server) → 9/9 → tags `web-v0.3.0` y `web-v0.4.0-mundos`.
3. **TÚ** (cuando quieras, bloquea solo la integración): aprobar 10-15 puentes por dominio → `bridges_aprobados.json` ×3. Regla: máx 2-3 por nodo core; `calidad_de_ejecucion_proceso_innovacion` está sobre-representado (16/60) — descartarlo salvo 1-2 pares excepcionales.
4. **YO**: `python scripts/integrar_packs.py --ejecutar` → Gate 0 verde → reporte de costos reales de caché parcial + índice Voyage → el vuelo exigirá entonces el ciclo positivo completo de mundos.

## Costos de esta fase

Implementación: $0 en APIs (todo determinístico/unitario). Los costos reales llegan con el vuelo (≈2 sesiones completas + 1 de mundo) y con la línea de ensamblaje (c: caché parcial ≈1554+~40 nodos; d: índice Voyage ~2805 nodos — se reportarán al ejecutar).
