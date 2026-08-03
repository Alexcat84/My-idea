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
- **Partición exacta, sin inventar pertenencia.** Cada entrada de bitácora se asigna a
  **exactamente un** espacio cuando su dominio es derivable. Una entrada
  **no-derivable** (evento de ítem cuyo ítem ya no existe y que no estampó dominio)
  **NO se asigna a core**: se muestra **solo en la bitácora global**, con **etiqueta
  neutra**, y queda **ausente de todas las específicas**. Inventar pertenencia está
  **prohibido** (addendum). Fórmula de partición: **unión de las específicas = global −
  {no-derivables listadas explícitamente}**. **Sin migración** (reversible).
- **Sin doble conteo.** El universal global sigue siendo core-only; el "proyecto
  completo" se presenta como **"core y N mundos"** con el avance de cada nivel por
  separado y la suma **declarada**, nunca un número mezclado.
- **Ruido cero.** Las etiquetas de espacio y los desgloses por mundo **solo aparecen
  cuando el proyecto tiene ≥1 mundo**. Un proyecto solo-core se ve idéntico a hoy.

## 4. Las tandas (commits "Espacios Fase 3:")

### Tanda 1 — La fuente etiquetada (bitácora dominio-aware) + tests

**Gobierno primero (antes de pintar):** la ENMIENDA del BANCO §7.1 ya está hecha ("Tu
avance" = hitos + estadísticas + bitácora del espacio; las métricas globales viven en
Análisis). El banco lidera; la pantalla lo sigue en las tandas 2-3.

- `web/lib/bitacoraCliente.ts`: `EntradaBitacora` gana **`dominio: string | null`**
  (`null` = **no-derivable**, NO core). `construirBitacora` resuelve el dominio con
  esta PRIORIDAD, sin inventar:
  1. `payload.dominio` si está (eventos nuevos, ver estampado abajo).
  2. JOIN a `checklist_items.dominio` por `payload.item` (mientras el ítem exista).
  3. `payload.mundo` directo (eventos de mundo).
  4. **core** para eventos intrínsecamente de proyecto (`modo_camino`, `realizada`) y
     los hitos de core (chispa/orden/plan). Esto NO es invención: esos eventos SON del
     viaje entero por naturaleza.
  5. Si nada resuelve (evento de ítem, sin `payload.dominio`, ítem borrado) → **`null`
     (no-derivable)**.
  - Corregir los **dos hitos que hoy agrupan sin mirar dominio**: "Tus Números"
    (`:148-151`) y "línea base sellada" (`:143-145`) → leer `plan.dominio`.
- **Estampar `payload.dominio` al ESCRIBIR** los eventos de ítem (los que hoy solo
  guardan `payload.item`): `checklist/route.ts` (`:319,325,346,361,371`) y
  `mover-fecha/route.ts` (`:121`) ya tienen el ítem a mano → añadir su `dominio` al
  payload. Así los eventos NUEVOS son auto-descriptivos y **el borde no-derivable queda
  solo ARQUEOLÓGICO** (filas viejas pre-estampado cuyo ítem además se borró). Verificado
  (exploración): hoy los eventos de ítem llevan `payload.item` (derivable por JOIN
  mientras el ítem exista), los de mundo `payload.mundo`, los de proyecto nada (core por
  naturaleza). **Sin migración** (payload es jsonb).
- Helper puro nuevo `bitacoraDeEspacio(entradas, dominio): EntradaBitacora[]` — filtra
  por espacio (core = `esEspacioCore`); **nunca incluye entradas `dominio: null`**.
- La **bitácora global** muestra TODAS las entradas, incluidas las `null`, estas con
  **etiqueta neutra** (sin espacio inventado).
- Tests (`bitacoraCliente.test.ts`): **partición exacta** con la fórmula *unión de
  específicas = global − {no-derivables}*, declarando la lista de no-derivables
  explícita; y que una entrada de ítem con ítem borrado y sin `payload.dominio` cae a
  `null` (no a core) y solo aparece en la global.
- **Sin migración, sin cambio de contrato de API.** Solo el lector, el estampado en los
  writes y un helper.

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

## 6. Riesgos y decisiones nombradas
- **Borde `bitacora-no-derivable`** (ítem borrado, sin `payload.dominio`): NO cae a
  core. Va **solo a la bitácora global con etiqueta neutra**, ausente de todas las
  específicas; el test de partición lo declara explícito (unión de específicas = global
  − {no-derivables}). Con el **estampado de `payload.dominio` en los writes** (tanda 1)
  el borde queda **arqueológico**: solo filas viejas cuyo ítem además se borró. Estampar
  las filas históricas requeriría migración + backfill; no se hace ahora (reversible).
- **`cumplimiento-desglose-core-multiciclo`** (inconsistencia NOMBRADA, `analytics.ts`):
  la fila "core" de `cumplimientoPorDominio` (`:288`) cuenta ítems core con fecha de
  **cualquier ciclo**, mientras los tiles globales de cumplimiento (`aTiempo/adelantadas/
  tardias`) cuentan solo el **plan baseline vigente** (`:484`). **No es doble conteo**;
  es un criterio distinto que puede no cuadrar si hubo varios ciclos. **Disposición:** el
  arreglo NO es de una línea (habría que pasarle el id del baseline vigente a
  `cumplimientoPorDominio` para acotar la fila core, y los mundos no comparten ese
  concepto) → va al **backlog nombrado** (`PENDIENTES.md §5`), **jamás arreglado "de
  paso" sin decirlo**. En la tanda 4, el desglose por-espacio se rotula con qué mide (sin
  cambiar el conteo), para no confundir mientras el arreglo espera.
- **Fetch de analytics en el hub**: hoy solo lo pide `AnalisisProyecto`. Si el peso
  molesta, se cachea en `IdeaView` y se pasa por props.
