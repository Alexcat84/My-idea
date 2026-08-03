# Plan — Restructuración "TODO SEPARADO"

Estado: **propuesta v2, con las 6 decisiones cerradas (fundador + auditor).** Pendiente
de la calibración final antes de la primera línea. (Redactado 2026-08-03. Anula
parcialmente el frente "La idea completa" (`web-v2.1.0-beta`) y la Opción A de la Fase 3.)

Todo verificado en código (no de memoria); las rutas son `file:line` reales.

## 0. El modelo final

El **proyecto principal** ("Tu viaje" / Mi idea) ES el centro visual y conceptual, desde
su pantalla actual (que no se toca en esencia). Los **mundos** son adiciones, cada uno
**espejo TOTAL** de esa misma configuración con su etiqueta. **NO existe nivel
centralizado por encima.** Todo registro, medida y documento es **POR ESPACIO**, con
**UNA excepción global: el Expediente completo.**

**Principio:** gobernanza separada por espacio, **cero mezcla de medidas**. Cada espacio
se mide solo, con sus indicadores. **Paridad total:** lo que el core tiene, el mundo lo
tiene, scopeado (su análisis completo, su Gantt, su cumplimiento, su calendario, su modo
de fechas). Donde la infraestructura no exista por mundo, **se extiende** (jamás se
aligera la vista del mundo).

## 1. Decisiones cerradas (fundador + auditor, 2026-08-03)

- **D1** — Las barras cross-mundo del Análisis del núcleo **MUEREN** (`CumplimientoPorMundoBarras`):
  cada espacio se mide solo.
- **D2** — **PARIDAD TOTAL** (no análisis ligero): cada mundo es espejo del core en
  estructura y comportamiento. Donde falte infraestructura de fechas para los checklists
  de mundo (modo, línea base, cascada, a-mi-ritmo) **se extiende** — su propia tanda (§T3).
- **D3** — Un solo calendario personal por usuario que **crece con los mundos**; cada
  actividad con su etiqueta `[Espacio]` visible en el título.
- **D4** — **Todos** los documentos visibles en **todos** los espacios, en **dos
  recuadros**: arriba **"Reportes globales"** (el Expediente completo, etiquetado
  **Global**, siempre presente en todos lados); abajo **"Reportes de {espacio}"** (los del
  espacio actual: su plan, sus seguimientos/ciclos sueltos, su bitácora, su análisis/
  reporte), etiquetados con su nombre de cara.
- **D5** — Orden del Expediente **como hoy**: el proyecto principal completo primero, luego
  cada mundo desde su plan, y la **secuencia global** como capítulo de cierre (es EL
  documento global; su broche global es coherente).
- **D6** — Las dos tarjetas de acción adoptan el **formato de acceso** (la tarjeta entera
  es la entrada; el flujo de confirmación/ritual se abre al pulsar). Cambia la forma,
  jamás la función.

## 2. Qué ya sirve / qué falta (verificado)

**Ya sirve (reusa):**
- Bitácora por espacio (`bitacoraDeEspacio` + ruta `?dominio` + `BitacoraEspacio`).
- `analyticsDeMundo.universal` = misma forma que el core → Capas 1-2 verbatim.
- El **sugeridor de fechas** `sugerirFechasBase` es **agnóstico** y **ya se llama por-tramo
  incluyendo mundos** (`ManosALaObra.tsx:716-729`): cero trabajo.
- La **cascada** `mover-fecha` **ya filtra por `dominio`** (`route.ts:101-111`): cero trabajo.
- `fecha_base/_origen/_original` son **por ítem** con `dominio` (schema OK).
- `GanttCumplimiento` (UI) es **reutilizable tal cual** — solo necesita el dato `porEtapa`.
- El Expediente ya lista principal-primero + sección por mundo con plan+acciones+cómo te
  fue (`expediente.ts:333-356`); el "Reporte de {mundo}" ya se sirve (`route.ts:162-197`).

**Falta / hay que cambiar:**
- **Modo del camino es del PROYECTO ENTERO** (`projects.modo_camino`, migración 018): un
  mundo **no puede** tener modo distinto del core → **requiere migración** (§T3).
- **La baseline del plan de un mundo nunca se sella**: `confirmarBaseline` manda solo
  `core.plan_id` (`ManosALaObra.tsx:1129-1132`); `planBaselineVigente` solo mira
  `planesCore` (`analytics.ts:543`). El schema (`plans.baseline_confirmada_at` por plan)
  **ya lo permite**; falta el código.
- **El ritual/selector de modo está gated por `mostrarCore`** → no aparece en el hub del
  mundo. `hayFechas` solo mira ítems del core.
- **El cumplimiento del mundo carece de Gantt**: `cumplimientoPorDominio` (que alimenta
  `AnalyticsMundo.cumplimiento`) **no** calcula `porEtapa`, `pct*` ni `desviacionVsInicial`,
  y **a propósito ignora `baseline_confirmada_at`** (`analytics.ts:283-287`). La capa de
  cumplimiento del core está **inline** en `calcularAnalytics` (`:542-641`), **no
  extraída** (a diferencia de `capaUniversalDe`).
- Los 4 accesos + 2 tarjetas de acción viven **solo en el core** (aside `mostrarCore`,
  `ManosALaObra.tsx:1799-1971`); sin componente compartido; formatos distintos.
- El Análisis no recibe `dominio`; el Calendario in-app y el .ics son **CORE-ONLY**.
- El Expediente no lleva etiqueta "Global"; los docs core no llevan su etiqueta de espacio.

## 3. Las tandas (commits "Todo separado:")

### Tanda 0 — Gobierno (el banco lidera)
Re-enmienda BANCO §7.1: (a) "Tu avance" = **hitos reales del espacio, nada más**; (b)
**"no existe análisis global; cada espacio se mide solo; la única vista global es el
Expediente"**; (c) **paridad total** (el mundo es espejo del core, con su modo/fechas);
(d) el **calendario etiquetado**; (e) el porqué del fundador. Matriz: elimina el nivel
general; varas de Design pierden el nivel general y ganan calendario etiquetado + seis
tarjetas hermanas + paridad de fechas por mundo.

### Tanda 1 — Eliminar el nivel general (borrado limpio)
Muere `agregadoDeIdea`+tests, `IdeaCompleta.tsx`, `?vista=idea`+nav+entrada del cambiador,
el `agregado` de `/analisis`, y **"Tu proyecto completo"**+`NivelFila` en AnalisisProyecto.
- **BORDE B1 (verificado):** **NO borrar `ETIQUETAS_CICLO_PLAN`** (`analytics.ts:465`):
  `analyticsDeMundo` lo usa (`:445`), no solo el agregado.
- **B2:** `/analisis` y `Analytics.mundos` se quedan (5 consumidores); solo muere `agregado`.
- **D1 aquí:** quitar también `CumplimientoPorMundoBarras` (`AnalisisProyecto.tsx:340-351`)
  y su import (23). `NOMBRE_DOMINIO` se queda si lo usa el análisis de mundo (tanda 4); si
  no, muere con el bloque.

### Tanda 2 — "Tu avance" vuelve a solo hitos
Quitar `EstadisticasEspacio` y `BitacoraEspacio` de "Tu avance" (`ManosALaObra.tsx:1366,
1368` core; `:1589,1593` mundo). "Tu avance" = **solo `LineaAvance`**. Los componentes NO
se borran: se reubican en los accesos "Análisis de {espacio}" y "Mi bitácora de {espacio}".

### Tanda 3 — PARIDAD DE FECHAS POR MUNDO (infraestructura) ⚠️ la tanda de peso
Para que el mundo tenga su modo, su línea base, su cumplimiento y su Gantt como el core.

**3a. Migración — el modo del camino por ESPACIO** (única pieza de esquema que falta):
- Nueva tabla `project_modos(project_id, dominio, modo_camino text CHECK IN ('ritmo','fechas'),
  updated_at)` con `UNIQUE(project_id, dominio)` + RLS espejo de `project_nodes_own`.
  Cubre core y mundos uniformemente (el core **no** tiene fila en `project_unlocks`, por eso
  no sirve añadir la columna allí).
- **Backfill:** copiar `projects.modo_camino` existente a `project_modos(project_id, 'core', …)`.
  `projects.modo_camino` se deja como está (lectura de respaldo) y se deja de escribir; se
  puede retirar en una migración futura. **Contrato/dbContract + check plain-SQL** (regla de
  la casa: script paste-and-run con UNION ALL, sin funciones).
- **BORDE B4:** transición dual-read (leer `project_modos`; si no hay fila del core, caer a
  `projects.modo_camino`). Documentado, acotado.

**3b. Modo por espacio (código):**
- Ruta `modo/route.ts` acepta `{ dominio, modo_camino }` → upsert en `project_modos`.
- `/api/idea/[id]` devuelve los modos por dominio (mapa) en vez de un solo `modo_camino`.
- Front: `modoDe(dominio)` en IdeaView; `ManosALaObra` lee el modo del **espacio actual**.

**3c. Ritual + selector de modo en el hub del mundo:**
- Desbloquear el selector de modo y `RitualFechas` fuera de `mostrarCore`: renderizarlos
  para el **espacio actual** (core o mundo), con `hayFechas`/estado de modo **por dominio**.
- **BORDE B5 (cambio de comportamiento):** hoy el ritual del **core arrastra los tramos de
  mundo** (`gruposRitual` los incluye) y sella todo contra `core.plan_id`. Con paridad,
  **cada espacio corre SU propio ritual** scopeado a sí mismo: el ritual del core pasa a
  ser **core-only**, y cada mundo corre el suyo en su hub. Se debe reescribir `gruposRitual`/
  `confirmarBaseline` para sellar **el plan de cada espacio por separado** (y arreglar el
  filtro de `previos` por plan en `baseline/route.ts:74-78`).

**3d. Cumplimiento + Gantt por mundo (extracción):**
- **Extraer** `capaCumplimientoDe(items, planBaseline, chispa)` del bloque inline de
  `calcularAnalytics` (`analytics.ts:542-641`, incluido el constructor `porEtapa` de
  `:573-603`). Los tests de analytics del core **blindan** que la extracción no cambia su
  salida.
- Llamarla scopeada en `analyticsDeMundo` con el plan baseline **del mundo** +
  `mundo.unlocked_at` como día-0 → `AnalyticsMundo.cumplimiento` gana `porEtapa`, `pct*`,
  `desviacionVsInicial`, `replanificaciones`. Gate de política igual que el core: solo si
  el plan del mundo tiene `baseline_confirmada_at` (que 3a-3c ya permiten sellar).
- **BORDE B6:** los mundos existentes no tienen baseline sellada → su cumplimiento/Gantt
  aparece en cuanto el usuario corre el ritual del mundo (misma política que el core hoy).
  Sin ritual del mundo, el mundo está "a mi ritmo" y su análisis muestra las capas
  universales sin el Gantt (idéntico al core sin baseline). Esto **no** es "aligerar": es
  la misma regla de política, scopeada.

### Tanda 4 — Las vistas SCOPEABLES por espacio (los destinos)
- **Análisis por mundo COMPLETO:** `/analisis?dominio=X` devuelve un `Respuesta` desde
  `analyticsDeMundo`: `universal=m.universal`, `cumplimiento` = la `CapaCumplimiento`
  **completa** del mundo (de la tanda 3d, con Gantt), `realizada_at←m.completadoAt`,
  `cierre_motivo←m.cierreMotivo`, `titulos` del plan del mundo. `AnalisisProyecto` gana
  `dominio?`; **el Gantt del mundo se dibuja** (paridad). Etiqueta "Análisis de {espacio}".
  `MapaHitos` del mundo se alimenta de los hitos del espacio (`hitosDeEspacio`) para paridad
  (o se omite si se decide que "Tu avance" ya es su mapa — ver nota).
- **Bitácora por espacio:** cablear `BitacoraEspacio`/ruta `?dominio` al acceso, etiqueta.
- **Calendario por espacio:** el componente scopea al espacio (ver tanda 6) con su modo.
- **Documentos por espacio:** ver tanda 7.
- **Navegación:** cada `ir*` gana `dominio`; deep-link `?vista=analisis&dominio=X`, etc.;
  "Volver" coherente por espacio (patrón `?cara=`).

### Tanda 5 — Los 6 accesos/acciones UNIFORMES por espacio
- **Extraer `TarjetaAcceso`** (icono + título + descripción + botón): un solo formato.
- **El aside existe en CADA espacio** (generalizar `mostrarCore` → "el espacio actual"),
  con conteos/gates **del espacio**.
- **Seis tarjetas hermanas:** Mi bitácora · Tu calendario · Análisis · Tus documentos +
  (cierre) + (ciclo), etiquetadas con el nombre del espacio.
- **Las 2 tarjetas de acción** adoptan `TarjetaAcceso` (**D6**): core (Marcar realizada;
  Contar qué pasó) y mundo (cerrar el mundo con acta; el seguimiento del mundo). **Copy del
  mundo (paridad):** gana su promesa scopeada — *"¿La realidad cambió {mundo}? Cuéntame qué
  pasó y lo recalculo desde donde estás"* — **jamás "todo"** (backend ya scopeado).

### Tanda 6 — Calendario ETIQUETADO por espacio (D3, "lo nuevo importante")
- **Incluir ítems de mundo** (relajar `esCore`) en el Calendario in-app (`:96`), las
  descargas (`ManosALaObra.tsx:1077`) y el **feed webcal** (`feed/route.ts:40`).
- **Etiqueta visible:** `nombreEspacio?` en `TareaIcs`; **prefijar el SUMMARY en un solo
  sitio** (`ics.ts:86`): `[Calidad y Confianza] {texto}`. Poblar el nombre de cara.
- **Vista in-app** por espacio (cada actividad etiquetada; el calendario de un mundo muestra
  lo suyo, con su modo de fechas de la tanda 3).
- **Nivel 1 sano (B3):** el `UID` por ítem no se toca → los suscriptores actualizan, no
  duplican; el feed es uno por usuario y ahora crece con los mundos, cada uno etiquetado.

### Tanda 7 — Documentos etiquetados, dos recuadros (D4)
- **Panel en DOS recuadros:** arriba **"Reportes globales"** = el Expediente (etiquetado
  **Global**), presente en todos los espacios; abajo **"Reportes de {espacio}"** = plan,
  seguimientos/ciclos sueltos, bitácora y análisis/reporte del espacio actual, etiquetados.
- **Requiere:** `DocumentoIndice` con una etiqueta de espacio para el expediente ("Global")
  y para los docs core; exponer los **ciclos del mundo** (Tu Plan/Seguimiento del mundo)
  como docs sueltos del índice (hoy solo el "Reporte" empaquetado); `Descargas.tsx` scopea
  al espacio actual y renderiza el chip también para el Global.
- **D5:** el orden interno del Expediente queda como hoy (principal → mundos → secuencia
  global de cierre).

### Cierre — verificación
- **Tests que MUEREN:** el describe de `agregadoDeIdea` (`analytics.test.ts:599-660`).
- **Tests NUEVOS (puros, a mano):** la extracción `capaCumplimientoDe` (misma salida que el
  core — golden test) + `porEtapa` por mundo; el modo por espacio (contrato/migración); la
  baseline por dominio; el prefijo del ICS (idempotente, UID intacto) + calendario con
  ítems de mundo; el índice con etiqueta Global/específico + ciclos de mundo.
- **Gate re-capturado:** quitar `?vista=idea`/"Tu proyecto completo"; añadir por-espacio los
  6 accesos/acciones (core y un mundo), el **análisis de un mundo con su Gantt**, el modo/
  ritual de fechas en el hub de un mundo, el calendario etiquetado, y los documentos en dos
  recuadros. Dos viewports. **No corrido en vivo** (fundador/auditor).
- **Migración:** aplicar `project_modos` en Supabase + correr el check plain-SQL.
- **Tag:** `web-v2.2.0-beta` ("todo separado"). Merge a main con visto, por tanda.

## 4. Bordes y riesgos (para la calibración final)
- **B1** — `ETIQUETAS_CICLO_PLAN` no es huérfano (no borrar).
- **B2** — `/analisis` y `Analytics.mundos` se quedan; solo muere `agregado`.
- **B3** — ICS: `UID` estable → el prefijo no duplica (Nivel 1 sano); el feed crece con mundos (D3, confirmado).
- **B4** — Migración `project_modos`: transición dual-read del modo del core (backfill + fallback), acotada.
- **B5** — El ritual del core deja de arrastrar los mundos: cada espacio sella SU baseline.
  Cambio de comportamiento real; se prueba en el gate (ritual en el hub del mundo).
- **B6** — Cumplimiento/Gantt por mundo aparece tras sellar la baseline del mundo (misma
  política que el core). Sin baseline = "a mi ritmo", sin Gantt: es paridad, no aligeramiento.
- **B7** — Extraer `capaCumplimientoDe` es un refactor del analytics del core: los tests
  existentes del core deben pasar SIN cambios (golden) — es la red de seguridad.
- **B8** — Navegación vista×espacio multiplica el estado; "Volver" coherente con el patrón
  `?cara=`; deep-links en el gate.
- **B9** — UI no unit-testeable (vitest=node): accesos/aside/tarjetas/ritual del mundo se
  verifican en el **gate**; lo puro (cumplimiento extraído, ICS, índice, modo) lleva tests.
- **Alcance:** 8 tandas; la T3 (paridad de fechas) es la de peso y la única con migración.
  Checkpoint por tanda, merge con visto, como en Fase 3.

## 5. Nota abierta (menor, no bloquea)
- **MapaHitos por mundo (paridad):** el core lo tiene en su Análisis; el mundo tiene sus
  hitos en "Tu avance". ¿El Análisis del mundo repite un mapa de hitos (paridad estricta) o
  se apoya en "Tu avance"? *Propuesta: alimentar `MapaHitos` del mundo con `hitosDeEspacio`
  para paridad estricta; es barato y no rompe nada.* Se decide al implementar la tanda 4.
