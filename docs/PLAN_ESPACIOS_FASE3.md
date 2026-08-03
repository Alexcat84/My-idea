# Plan — Campaña "Espacios", Fase 3 (bitácora, reporte, documentos y estadísticas POR ESPACIO)

Estado: **propuesta, pendiente del visto del fundador y del auditor.** 0 líneas de
código hasta la aprobación. (Redactado 2026-08-03.)

## 0. Qué es la Fase 3 y qué ya está en producción

Un proyecto = el **core** ("Tu viaje") + cada **mundo** desbloqueado, y cada uno es
un **espacio** con su propio HUB. Ya en producción (Fase 1+2 + las 3 caras):

- Navegación de **dos niveles**: `CambiadorEspacios` (pestañas-fichero entre
  espacios) → `SelectorCara` (las 3 caras dentro de un espacio: **Plan · Manos a la
  obra · Tu avance**).
- El hub de core (`?vista=manos`) y el de un mundo (`?vista=mundo&dominio=X`) caen en
  la misma rama de render (`IdeaView.tsx:854`); los distingue la prop
  `soloDominio` (`IdeaView.tsx:937`).
- La cara **"Tu avance"** ya es per-espacio: `LineaAvance` con `hitosDeEspacio`
  (core: `hitosCore`; mundo: `hitosDeEspacio({espacio:"mundo",…})`).

Lo que **falta** (esta fase), literal del backlog (`docs/PENDIENTES.md §1`):

1. Documentos por espacio (plan + seguimientos filtrados por dominio, .md/PDF).
2. Estadísticas por espacio (dibujar `analyticsDeMundo`, ya calculado).
3. Etiquetas de espacio en bitácora/expediente, con **ruido cero** (solo si ≥1 mundo).
4. Addendum: bitácora y reporte POR ESPACIO como **vistas filtradas de la fuente
   única** ("una fuente, muchas lecturas": nunca registros paralelos). **Partición
   exacta**: cada entrada de la global aparece en exactamente una específica.
5. Análisis del proyecto **sin doble conteo**: "Tu proyecto completo: core y N
   mundos"; el avance de cada nivel es el suyo, el del proyecto es la **suma declarada**.

Fuera de alcance de esta fase (siguen como están):

- **Interiores decorados del PDF Expediente**: DIFERIDOS a CD (`PENDIENTES.md §2`).
- **ETAPA 3 = pasarelas de pago**: dormida a propósito.

## 1. Enfoque — Opción A: todo dentro de "Tu avance", sin navegación nueva

El propio código marca el seam: `ManosALaObra.tsx:1770-1772` dice *"En el hub de un
mundo no va — su documentación/estadística/bitácora propias llegan en la Fase 3."*

**Decisión: NO añadir una 4ª cara ni páginas nuevas.** Las estadísticas y la bitácora
de un espacio son la extensión natural de **"Tu avance"** (que ya es la superficie
histórica/resumen per-espacio). Encajan así:

- **Core** — `ManosALaObra.tsx:1354` (hoy `cara === "avance" && <LineaAvance hitos={hitosCore}/>`):
  debajo del riel se añaden **estadísticas del core** y **bitácora del core**.
- **Mundo** — `ManosALaObra.tsx:1557-1569` (el bloque `cara === "avance"` del hub):
  debajo del riel se añaden **estadísticas de ese mundo** y **bitácora de ese mundo**.

La vista GLOBAL de "Análisis del proyecto" (`?vista=analisis`, `AnalisisProyecto.tsx`)
y "Mi bitácora" (`?vista=bitacora`, `Bitacora.tsx`) **se conservan tal cual** como
lectura del proyecto entero. La Fase 3 añade las lecturas por-espacio en el hub y
mejora la global (tanda 4), sin romper la navegación de dos niveles.

Alternativa descartada (Opción B): páginas `?vista=analisis&dominio=X` dominio-aware.
Más disruptiva: obliga a renderizar el aside en el hub de mundo, parsear `dominio` en
los gates y arreglar los "Volver" que hoy siempre regresan al core
(`IdeaView.tsx:613,656`). No se elige.

## 2. Lo que YA existe (el motor está casi todo hecho)

Verificado en el código (esta fase es sobre todo *pintar*, no *calcular*):

- **Estadísticas por mundo:** `analytics.ts:440` `analyticsDeMundo(entrada, dominio):
  AnalyticsMundo` — capa universal completa (ritmo, racha, X/N, series) + cumplimiento
  por dominio, contando **desde el unlock del mundo**, no desde la chispa de la idea.
  `calcularAnalytics` (`analytics.ts:467`) ya emite `analytics.mundos[]` (`:590`). El
  endpoint `GET /api/project/[id]/analisis` **ya devuelve** todo eso. **Hoy no se
  dibuja** la capa universal por mundo (solo un desglose de cumplimiento en barras,
  `AnalisisProyecto.tsx:293-304`). No hace falta endpoint nuevo.
- **Bitácora etiquetada:** `bitacoraCliente.ts:construirBitacora` ya resuelve el
  dominio de cada entrada (mapa `dominioDe` desde `checklist_items.dominio`, `payload.mundo`
  directo en eventos de mundo, y core por defecto en eventos de proyecto). Pero
  `EntradaBitacora` (`:70-80`) **hoy NO expone `dominio`** — el mundo solo va embebido
  como sufijo de texto (" · en {mundo}"). Una bitácora por-espacio es un **filtro**
  sobre eso.
- **Sin doble conteo, por diseño:** el `universal` global es **solo core**
  (`analytics.ts:476-478`, filtra `esItemCore`); los mundos viven en carriles
  separados (`porDominio` y `Analytics.mundos[]`). Ningún lugar suma core + mundos en
  un solo total → una tarea de mundo **nunca** se cuenta dos veces. Contracara: el
  total global **excluye** las tareas de mundo, así que "core + N mundos" hay que
  **declararlo** como suma, no fundirlo.

## 3. Garantías (para el auditor)

- **Una fuente, muchas lecturas.** Cero tablas/registros paralelos. Toda vista
  por-espacio es un **filtro** de la bitácora/analytics únicos.
- **Partición exacta.** Cada entrada de bitácora se asigna a **exactamente un**
  espacio, derivado en el lector. La unión de las específicas = la global, sin
  solapes. **Sin migración** (reversible). Borde documentado y aceptado: si un
  `checklist_item` se borra, su entrada de ítem cae a **core** por defecto (sigue
  siendo una partición válida; es un evento raro en beta).
- **Sin doble conteo.** El universal global sigue siendo core-only; el "proyecto
  completo" se presenta como **"core y N mundos"** con el avance de cada nivel por
  separado y la suma **declarada**, nunca un número mezclado.
- **Ruido cero.** Las etiquetas de espacio y los desgloses por mundo **solo aparecen
  cuando el proyecto tiene ≥1 mundo**. Un proyecto solo-core se ve idéntico a hoy.

## 4. Las tandas (commits "Espacios Fase 3:")

### Tanda 1 — La fuente etiquetada (bitácora dominio-aware) + tests
- `web/lib/bitacoraCliente.ts`: añadir `dominio: string` (y `espacio: "core" | pack)
  a `EntradaBitacora`; `construirBitacora` ya conoce el dominio de cada entrada — solo
  emitirlo. Corregir los **dos hitos que hoy agrupan sin mirar dominio**: "Tus Números"
  (`:148-151`) y "línea base sellada" (`:143-145`) → leer `plan.dominio` (ya disponible).
- Helper puro nuevo `bitacoraDeEspacio(entradas, dominio): EntradaBitacora[]`
  (filtro por espacio; core = `esEspacioCore`).
- Tests (`bitacoraCliente.test.ts` o nuevo): **partición exacta** (unión de específicas
  = global; cada entrada en exactamente un espacio) y el borde (ítem borrado → core).
- **Sin migración, sin cambio de API.** Solo el lector y un helper.

### Tanda 2 — Estadísticas por espacio (pintar lo ya calculado)
- Componente nuevo `web/app/ui/EstadisticasEspacio.tsx`: la **capa universal** (ritmo,
  racha, X/N vigente, series) para un espacio dado. Reusa las piezas visuales de
  `AnalisisProyecto.tsx` (mismos tiles), sin recalcular.
- Wiring: `ManosALaObra` necesita el analytics. Cargar `GET /api/project/[id]/analisis`
  una vez en el hub (o subir el fetch a `IdeaView`) y pasar el slice: core → `universal`
  global (que ya es core-only); mundo → `analytics.mundos.find(m => m.dominio === X).universal`.
- Render: bajo el `LineaAvance` en las dos ramas de "Tu avance" (core `:1354`, mundo `:1557`).

### Tanda 3 — Bitácora por espacio (vista filtrada en el hub)
- Render de la bitácora filtrada bajo las estadísticas en "Tu avance", usando
  `bitacoraDeEspacio` (tanda 1). Reusar el render de `Bitacora.tsx` (o una versión
  compacta) con las entradas ya filtradas — sin fetch nuevo si se reusa el de la
  bitácora global; core muestra lo del core, cada mundo lo suyo.

### Tanda 4 — Análisis global sin doble conteo + etiquetas de espacio
- `AnalisisProyecto.tsx` (la vista global `?vista=analisis`): encabezar **"Tu proyecto
  completo: core y N mundos"**; el avance del proyecto = **suma declarada** de los
  niveles, cada uno mostrado por separado. Pintar la **capa universal por mundo** (que
  ya se calcula en `analytics.mundos[]` y hoy no se dibuja).
- **Etiquetas de espacio** (nombres de cara) en bitácora global y expediente, con
  **ruido cero** (solo si ≥1 mundo). Un proyecto solo-core no cambia.

### Tanda 5 — Documentos por espacio
- `web/app/api/project/[id]/documentos/route.ts`: hoy `esCore(dominio)` filtra a
  core-only en ciclos (`:85`) y acciones del expediente (`:226`); el Expediente ya crea
  **una sección `## {mundo}` por mundo** con su plan (`expediente.ts:305-315`). Se
  completa: **plan y seguimientos por espacio** (filtrados por dominio) descargables, y
  la sección de cada mundo gana **sus acciones** y **su "cómo te fue"** (stats del mundo).
- Los **interiores decorados del PDF** siguen diferidos a CD (`PENDIENTES.md §2`);
  aquí solo el contenido/estructura, no la decoración de papel.

### Cierre — verificación
- Extender `web/scripts/vuelo_beta.ts`: un proyecto core + 1 mundo; asertar que la
  bitácora/estadísticas por-espacio parten exacto y que el global no dobla conteo.
- Extender `web/scripts/gate_beta.ts`: capturas de "Tu avance" con stats + bitácora en
  core y en un mundo (dos viewports).
- Suites verdes en clon limpio (`pnpm vitest run` + `python engine/run_all_tests.py`).
- Tag menor; autopush a `origin/staging` por tanda. **Merge a main solo con
  autorización explícita del fundador.**

## 5. Archivos que se tocan (referencia)
- **Lib (puro, testeado):** `web/lib/bitacoraCliente.ts` (+ `.test.ts`), helper
  `bitacoraDeEspacio`. Sin tocar `analytics.ts` (ya calcula todo).
- **UI:** nuevo `web/app/ui/EstadisticasEspacio.tsx`; `web/app/ui/ManosALaObra.tsx`
  (las dos ramas de "Tu avance"); `web/app/ui/AnalisisProyecto.tsx` (tanda 4);
  posible fetch de analytics en `web/app/idea/[id]/IdeaView.tsx`.
- **API:** `web/app/api/project/[id]/documentos/route.ts` (tanda 5). Sin endpoints
  nuevos (analytics y bitácora ya existen).
- **Scripts:** `web/scripts/vuelo_beta.ts`, `web/scripts/gate_beta.ts`.
- **Migración:** **ninguna.**

## 6. Riesgos y decisiones abiertas
- **Borde de partición** (ítem borrado → core): aceptado y documentado; alternativa
  futura sería estampar `payload.dominio`/columna en `project_bitacora` al escribir
  (requeriría migración + backfill). No se hace ahora para mantener la fase reversible.
- **Inconsistencia menor de cumplimiento** (`analytics.ts`): la fila "core" de
  `porDominio` cuenta ítems core de **cualquier ciclo**, mientras los tiles globales
  cuentan solo el plan baseline vigente. No es doble conteo; se anota para que el
  desglose por espacio use el mismo criterio y no confunda.
- **Fetch de analytics en el hub**: hoy solo lo pide `AnalisisProyecto`. Si el peso
  molesta, se cachea en `IdeaView` y se pasa por props.
