# Pendientes — My Idea

Lista viva de lo que queda por hacer. Se actualiza al cerrar o abrir frentes.
(Última actualización: agosto 2026.)

## 1. Campaña "Espacios" — Fase 3 (COMPLETA, en staging)

**Plan y contrato: `docs/PLAN_ESPACIOS_FASE3.md`** (Opción A "dentro de Tu avance";
garantías de fuente única / partición exacta / sin doble conteo / ruido cero).
Las 5 tandas cerradas; tandas 1-4 en main, tanda 5 en staging (pendiente del visto
para main + tag de la campaña).

- **T1 — la fuente etiquetada** ✓: `EntradaBitacora.dominio` ("core" | mundo | null
  no-derivable), partición exacta, estampado de `payload.dominio` en los writes.
- **T2 — estadísticas por espacio** ✓: `analyticsDeMundo` pintado en "Tu avance"
  (core y cada mundo), tiles reusados, test de no doble conteo.
- **T3 — bitácora por espacio** ✓: filtro en servidor con `bitacoraDeEspacio`, reuso
  de `LineaBitacora`/`BitacoraPapel`, descarga .md/PDF scopeada.
- **T4 — Análisis global + etiquetas + ruido cero** ✓: "Tu proyecto completo" (suma
  declarada), etiqueta de espacio como DATO estructural (murió el sufijo de texto).
- **T5 — documentos por espacio** ✓: "Reporte de {mundo}" (plan+seguimientos+avance+
  cómo te fue+secuencia, del mismo armador), Expediente completado por-mundo (acciones
  + cómo te fue), etiqueta de espacio en los documentos.

## 1b. "La idea completa" (nivel general) — ANULADA por "Todo separado"

El frente "La idea completa" (tag `web-v2.1.0-beta`) fue **anulado** por el veredicto
"todo separado": muere el nivel general (no hay análisis ni medida global; la única vista
global es el Expediente). Se elimina en la tanda 1 de la restructuración. (El plan
`docs/PLAN_IDEA_COMPLETA.md` queda como archivo histórico.)

## 1c. Restructuración "TODO SEPARADO" (COMPLETA — T0..T7, cerrada 2026-08-04)

**Plan/contrato: `docs/PLAN_TODO_SEPARADO.md`** (aprobado por fundador y auditor, 6
decisiones cerradas). Cada espacio se mide/registra/documenta solo; el mundo es espejo
TOTAL del core (su análisis con Gantt, su calendario, su modo de fechas y línea base);
única vista global = Expediente. **Cerrada con el veredicto del fundador y el tag
`web-v2.2.0-beta`.** Matriz de las 8 tandas — **todas ✓, en producción (main):**

- **T0 gobierno** ✓ · **T1 eliminar nivel general** ✓ (murió "La idea completa",
  `IdeaCompleta.tsx` borrado, barras cross-mundo muertas) · **T2 "Tu avance"→solo hitos** ✓.
- **T3 paridad de fechas por mundo** ✓ (migración `project_modos` aplicada; B5 no-arrastre;
  `capaCumplimientoDe` extraída con golden; hub del mundo con su modo/ritual; Gantt del mundo).
- **T4 vistas scopeables** ✓ (Análisis del mundo con su Gantt; los cuatro accesos del espacio).
- **T5 seis tarjetas hermanas** ✓ (`TarjetaAcceso` único, contrato que lo blinda).
- **T6 calendario etiquetado `[Espacio]`** ✓ (feed que crece con los mundos; UID intacto).
- **T7 documentos en dos recuadros** ✓ ("Reportes globales" + "Reportes de {espacio}").
- **Cierre** ✓: corrida única del fundador (vuelo `faseTodoSeparado` 16/16 + gate del frente
  entero) + veredicto visual; merge de cierre + tag `web-v2.2.0-beta`.

Notas de método (para memoria): la migración `project_modos` la aplicó el fundador; B5
bendecido (cada espacio sella SU baseline, el core no arrastra); golden test antes de
extraer `capaCumplimientoDe`. **Pendiente SOLO la calibración visual de Design (§2).**

## 1d. Campaña "SCHEDULER INTELIGENTE" (COMPLETA — F0..F4, cerrada 2026-08-05)

**Visión original del fundador (PM):** un programador de fechas que entienda la
complejidad de cada tarea y sugiera fechas que respiran según la capacidad real del
usuario. **Spec:** `docs/SCHEDULER_INTELIGENTE.md`. **Plan de ejecución:**
`docs/PLAN_SCHEDULER_INTELIGENTE.md`. Cadencia: checkpoint por fase, merge con visto,
commits `Scheduler:`. **Anclajes verificados contra main 943ce0d** (planRedactor conoce
pasos+entregable; project_modos es la casa de la capacidad; diaDominante/cadenciaReal
son la capa 3 embrionaria). Matriz de fases:

- **F0 — SPIKE de estimación: PUERTA ABIERTA.** Corrido en vivo (`pnpm run spike` y
  `spike -- items`), reportes en `web/examples/spike_estimacion.md` y `_items.md`.
  **97.2% exacta-o-adyacente en las DOS granularidades**, costo real $0.31. El
  hallazgo del spike: a nivel CONCEPTO la distribución se apelmaza arriba
  (0S/8M/5L/23XL) porque el nodo es un bundle; a nivel ÍTEM (la unidad real que ve
  el usuario, la que produce `derivarChecklist`) reparte de verdad (9S/23M/1L/3XL).
  **Afinamiento decidido:** producción usa **MAYORÍA-DE-3** (tres corridas batch,
  banda = voto mayoritario; empates → la banda MAYOR de las empatadas, conservador;
  mismo criterio para `espera_externa`).
- **F1 — la estimación nace con el plan: HECHA** (staging `98bdee9`, migración 033
  **aplicada**). Al nacer TODO plan nuevo (core y mundo) corre el lote de
  mayoría-de-3 después del plan; el prompt validado vive en `lib/prompts.ts` como
  `SYSTEM_ESTIMACION_BANDA` con su procedencia (criterios de banda palabra por
  palabra del spike; solo cambia el empaquetado a lote con id). Motor puro en
  `lib/engine/estimacion.ts`. **Fallback declarado:** la estimación que falla deja
  los ítems sin banda y el plan JAMÁS se bloquea; el fallo deja síntoma en
  `sessions.decisiones` (`estimacion_banda` con el conteo, o `estimacion_fallida`).
  El detalle muestra el **rango honesto** (~1 h / ~2-4 h / una jornada / varios días)
  con corrección del usuario → evento `banda_corregida {de, a}` (telemetría del
  multiplicador de F4). Planes viejos sin banda: sin sección de esfuerzo, cero
  invención. 732/732 tests. **EN PRODUCCIÓN** (main `a307d1f`; migración 033
  aplicada por el fundador).
- **F2 — capacidad + empaquetado (el corazón): HECHA** (staging `e97ae8f`, sin
  migración: la 033 ya trajo `capacidad_semanal`). `lib/empaquetado.ts` puro:
  HORAS_MEDIA {S:1,M:3,L:8,XL:16}, etapas=PUERTAS (la N+1 abre la semana siguiente
  a la última de la N), reparto por horas acumuladas dentro de la etapa (el
  desborde y la tarea más grande que una semana salen del mismo cálculo), entrega
  en el día dominante de SU semana, destacada al lunes de la primera semana de su
  etapa. **Dos decisiones declaradas:** se planifica con el PISO del chip (mismo
  criterio conservador de la mayoría-de-3) y la primera etapa arranca en la semana
  siguiente al ancla (en la semana 0 el lunes de la destacada caería en el pasado).
  El ritual de cada espacio pregunta las horas (chips, default 5-10, replanifica a
  la vista, evento `capacidad_semanal` {de,a}) y se edita después desde la cinta de
  fechas activas; las horas nuevas entran en el siguiente "Recalcular pendientes",
  nunca a espaldas del usuario. Sin bandas no se pregunta y manda el sugeridor
  viejo. Vuelo con el assert de la TUBERÍA (empaquetado → /baseline → feed .ics,
  una S y una XL de la misma etapa en semanas distintas, UID estable); gate con el
  par 07b/07c (el mismo plan con 20+ y con 2-5). 769/769 tests.
  **EN PRODUCCIÓN** (main `d808a99`).
- **F3 — esperas externas: HECHA** (staging `89cdab6`, sin migración). La tarea con
  `espera_externa` se dispara temprano (inicio = lunes de la primera semana de su
  etapa) y entrega con colchón (`LEAD_ESPERA_SEMANAS = 1`, constante nombrada con
  su porqué y su criterio de revisión: los `completed_at` reales, no la intuición).
  **La espera NO consume capacidad** (el tiempo de terceros no empuja a las tareas
  hermanas), pero **sí manda en la puerta**: una etapa cierra cuando cierra su
  tarea más tardía de verdad, colchón incluido. El detalle lo dice en persona sin
  colgarle la demora al usuario, con un test que vigila que el copy no derive al
  reproche. Gate `13b`. 780/780 tests. **EN PRODUCCIÓN** (main `8f3a3f3`).
  Decisión propia bendecida: la destacada con espera conserva su lunes y corre de
  semana; `espera_externa` NO se abre al PATCH (contención de superficie,
  revisable con la telemetría de la beta).
- **F4 — multiplicador personal: HECHA** (staging `c1f1aa4`, sin migración).
  `factorPorBanda` compara lo que las tareas tardaron de verdad (tiempo desde el
  cierre de la anterior) contra lo que su banda prometía con esa capacidad, **por
  espacio**, **mín. 3 muestras**, **sin muestras → factor 1 (cero invención)**, y
  se aplica **SOLO en los recálculos**. Decisiones escritas en el código: la
  primera cumplida no da muestra; las tareas con espera externa se excluyen (F3 ya
  les puso colchón); manda la **mediana** (una vacación no reescribe una banda);
  el factor se acota a **[0.5, 4]** con el criterio del clamp de
  `cadenciaRealSemanas`. Las muestras salen del checklist **completo** del espacio,
  no del ciclo vigente. 793/793 tests. **EN PRODUCCIÓN** (main `0475e33`).
  Decisiones propias bendecidas: el historial COMPLETO del espacio como memoria que
  sobrevive a los ciclos, y el borde de capacidad-vigente resuelto por el lado
  barato del error (subir la capacidad deja el recálculo conservador hasta que
  entren muestras nuevas).
- **CIERRE: HECHO.** La **doctrina del scheduler** queda escrita en **BANCO §7.1**
  (bandas como rangos honestos corregibles; empaquetado determinístico auditado con
  aritmética a mano; capacidad por espacio planificada con su piso; las esperas no
  consumen capacidad pero mandan en las puertas; aprendizaje con mediana acotada que
  solo re-fecha lo que el usuario pide; el sugeridor simple vivo como fallback;
  **cero invención** como razón de todo lo anterior). Las piezas visuales van al
  encargo de Design (§2). Tag **`web-v2.3.0-beta`**. El sugeridor viejo queda como
  **fallback documentado, jamás muere**.
  **Lo único que sigue del fundador:** vuelo y gate en vivo de las fases que no los
  han tenido (§3), y la ficha `mundos-de-proteccion-sobre-lo-existente` del backlog
  (§5), que espera su propia mini campaña.

## 2. Claude Design (encargos)

- **Centro de créditos v4** (alta industria, modelo de consumible): brief y prompt v2
  listos (`docs/calibracion-design/BRIEF_CREDITOS.md`, `PROMPT_CREDITOS_CD.md`).
  Esperando opciones de CD.
- **Espacios + La idea completa (encargo ACUMULADO, front funcional ya en su sitio):**
  `docs/calibracion-design/BRIEF_ESPACIOS.md` listo (dos niveles de navegación
  explícitos). Calibración visual de CD sobre las superficies del frente **tras "todo
  separado"** (el nivel general SE ELIMINA del encargo):
  - hub + **cambiador** de espacios (pestañas-fichero, la activa levantada);
  - las **3 caras** (Plan · Manos a la obra · **Tu avance = solo la línea de hitos**);
  - **las seis tarjetas hermanas** por espacio (Mi bitácora · Tu calendario · Análisis ·
    Tus documentos · Marcar realizada/Cerrar · Contar qué pasó), mismo formato de tarjeta;
  - el **Análisis por mundo** (con su Gantt) y el **modo de fechas/ritual en el hub del
    mundo** (paridad total);
  - el **calendario etiquetado** (`[Espacio]` en cada actividad) y los **documentos en dos
    recuadros** (Global + del espacio);
  - las **varas previas** que quedan: chips de etiqueta en la bitácora global y las fichas
    de Reporte por mundo. (Muere del encargo: la banda "Lo general" y el desglose "Tu
    proyecto completo".)
  - **Estado del frente: COMPLETO Y EN PRODUCCIÓN (tag `web-v2.2.0-beta`).** La
    restructuración "todo separado" (T3c-2..T7) está entera y funcional; este encargo
    queda **consolidado como la SPEC VISUAL pendiente** — la calibración de CD sobre TODOS
    sus pares del frente, capturados por el gate (§3): hub + su **modo/ritual** de fechas
    del mundo, **Análisis del mundo con su Gantt**, los **cuatro accesos** scopeados, las
    **seis tarjetas hermanas** (`TarjetaAcceso` uniforme), el **calendario etiquetado**
    `[Espacio]`, y los **documentos en dos recuadros**. El front no espera a Design: lo que
    CD calibre se aplica encima. Pares en `web/examples/gate-canon/` (`espacios_*`).
- **Scheduler Inteligente — las tres superficies nuevas (front funcional YA en
  producción, `web-v2.3.0-beta`; esto es calibración visual, no función):**
  - **La pregunta de capacidad**, dentro del ritual de fechas de cada espacio:
    *"¿Cuántas horas por semana puedes darle a este espacio?"* con cuatro chips
    (2 a 5 · 5 a 10 · 10 a 20 · Más de 20) y la línea que explica que se planifica
    con el piso. Lo que se juega: es **la premisa** del calendario entero y hoy es
    un bloque más del ritual; merece leerse como la pregunta que manda. Su gemela
    reducida vive en la cinta de "fechas activas" ("Le das 5 a 10 horas por
    semana · cambiar"). Pares del gate: `07b_capacidad_20mas` y `07c_capacidad_2a5`
    (el MISMO plan con dos capacidades: la comparación es el punto).
  - **El rango de esfuerzo en el detalle de la tarea**: la sección "Esfuerzo" con
    su valor en rango (`~1 h`, `~2-4 h`, `una jornada`, `varios días`), su píldora
    "corregir" y los cuatro chips de corrección. Regla que no se toca: **jamás un
    número de horas exacto**, y sin banda la sección **no existe** (nada de
    placeholders). Par del gate: `13_detalle`.
  - **El copy del colchón de esperas**, en esa misma sección cuando la tarea
    depende de terceros ("· depende de terceros" junto al rango, y la explicación
    de que la fecha ya trae el colchón y el tiempo ajeno no se le cuenta al
    usuario). Lo que se juega: que se lea como un aviso útil y **no como una
    disculpa ni un regaño**. Par del gate: `13b_detalle_espera`.
- **NOTA (no pedido) — el "viernes compartido" del sugeridor de fechas:** en modo
  fechas, todos los ítems regulares de una etapa caen el mismo día (el viernes de su
  semana): es **doctrina** (la fecha es el compromiso de entrega de la etapa, no una
  agenda diaria — BANCO §7.1). Si en la beta el fundador ve confusión con ese día
  compartido, la palanca es **de presentación (CD)** —agrupar, un encabezado de
  "entrega de la etapa", lo que sea visual— **jamás del sugeridor** (escalonar sería
  precisión inventada). Se anota aquí para tenerlo a mano; NO es un encargo abierto.
  **Precisado por el scheduler (F2):** con el empaquetado, los ítems de una etapa
  siguen cayendo **siempre en el día de cierre** (nada de agenda diaria), pero la
  **semana** puede cambiar si el trabajo no cabe en la capacidad declarada. El día
  compartido sigue siendo doctrina; la semana compartida ya no.
- **PDF Expediente · interiores (DIFERIDO post-beta):** el diseño YA existe
  (`_entrega-claude-design/Entrega-desing 20260729/entrega2/pdf-expediente-interiores/`:
  Tus Números, un mundo, "Cómo te fue", "La secuencia de tu viaje"). **Cuando sea el
  momento: pedirle a CD regenerar esas 4 páginas en HTML LIMPIO (sin imágenes
  embebidas / blobs)** para poder implementarlas; las HTML entregadas están pesadas y
  no se pueden leer bien tal cual.

## 3. Verificación en vivo (necesita `pnpm dev` + Supabase real; la corre el fundador/auditor)

- **Vuelo de dinero** (`web/scripts/vuelo_beta.ts`): la contabilidad nueva del Catálogo
  congruente (siembra 30 → plan −10 → Tus Números 0 → mundo −5 → seguimiento −5 →
  seguimiento de mundo −5 = 5). **NO corrido en vivo.**
- **Gate** (`web/scripts/gate_beta.ts`): capturas en dos viewports de `/creditos`, el
  cambiador, el hub y las **3 caras**, **más (Fase 3 T4-T5)** la **bitácora global con
  etiquetas** (`?vista=bitacora`), el Análisis del núcleo (`?vista=analisis`) y los
  **reportes por mundo** (`?vista=documentos`). **NO corrido en vivo** → verificar al
  ejecutarlo (la siembra del mundo con plan y las esperas nuevas).
- **Vuelo y gate del SCHEDULER (F0..F4), corrida del fundador.** El vuelo gana dos
  asserts que solo viven en vivo: la **tubería del calendario** (empaquetado →
  `/baseline` → feed `.ics`: una S y una XL de la misma etapa en semanas distintas,
  con UID estable) y que el plan de **SEGUIMIENTO nace estimado** (si sale 0 bandas,
  el mensaje apunta a `sessions.decisiones`). El gate añade `07b_capacidad_20mas` /
  `07c_capacidad_2a5` (el mismo plan con dos capacidades: **si las dos capturas se
  parecen, el empaquetado no está haciendo nada**) y `13b_detalle_espera` (el copy
  del colchón). El gate siembra bandas y la espera por service role, a propósito:
  no depende de lo que la estimación en vivo decida ese día.
- **Gate — "todo separado" (T3c-2/T4), pares nuevos del ESPACIO** (referencia para el
  encargo de Design; el run en vivo y el veredicto los da el fundador). Al ejecutar
  `gate_beta` se generan en `web/examples/gate-canon/` (tracked en staging, excluidos del
  release a main por patrón):
  - `espacios_hub_mundo_ritual` — el hub del mundo con **su** modo/ritual de fechas
    scopeado (T3c-2, paridad con el núcleo).
  - `espacios_analisis_mundo` — el **Análisis del mundo** a pantalla completa con **su
    Gantt** (`porEtapa`) sellado (T4a, el "pair B"): quality activada en el pasado, su
    baseline sellada, 1/1/1 de 3 a mano.
  - `espacios_bitacora_mundo` · `espacios_calendario_mundo` · `espacios_documentos_mundo`
    — los otros **tres accesos scopeados** del espacio (T4b), misma tarjeta que el núcleo.
  Vara para Design: los **cuatro accesos del espacio** con formato de tarjeta UNIFORME (la
  vara de las seis hermanas de T5 llega después; aquí no hay formato nuevo que deshacer).
- **Veredicto visual del fundador** sobre el conjunto de Espacios y sobre el centro de
  créditos (cuando pruebe en producción).
- **Auditoría**: Catálogo congruente y Espacios quedan en revisión del auditor.

## 4. Pasarelas y cuenta — ETAPA 3 (dormido a propósito)

- **Compra con dinero** (RevenueCat / Stripe / Play): la compra "se abre pronto"; el
  catálogo de packs muestra el estado deshabilitado hasta la ETAPA 3.
- **Siembra manual de créditos** (mientras): el fundador otorga créditos desde Supabase
  (`otorgar_creditos`, origen `siembra_beta`) — documentado en `docs/BETA_CUENTAS_README.md §2.f`.
- **2FA/TOTP + dominio de correo propio**: dormido (anclas listas).

## 5. Backlog / afinar

- **`mundos-de-proteccion-sobre-lo-existente`** (ficha de diseño registrada 2026-08-05;
  **NO implementar**: alcance, copy y murallas se deciden en su propia mini campaña
  **post-F4**). Decisión futura del fundador: alimentar a **Riesgos Bajo Control, HSEQ
  y Seguridad Digital** con el **snapshot del plan vigente del núcleo** (títulos de las
  actividades + sus estados) como insumo de su entrevista/diagnóstico, para que el plan
  del mundo se aplique **SOBRE las actividades reales** del usuario y no sobre una idea
  contada de nuevo. Es el modelo PM del fundador: el **risk register se levanta sobre la
  WBS**, no al lado. Frontera de la ficha: los mundos de **mejora/expansión** (Calidad,
  Exportación, Franquicias, Medio Ambiente) **quedan como están** (el plan del núcleo
  como contexto narrativo, que es lo correcto para ellos). Lo que esa mini campaña
  tendrá que decidir y por eso NO se toca ahora: qué se manda exactamente (¿solo títulos
  y estados, o también fechas y bandas?), qué ve el usuario de ese traspaso (nada
  silencioso), el efecto en el costo del diagnóstico, y la muralla de que un mundo de
  protección **sin** plan de núcleo siga funcionando.
- **Ajustes visuales de Espacios** que salgan de la prueba del fundador (grosor del eje y
  tamaño de nodos de "Tu avance", cuánto se "levanta" la pestaña activa, el segmentado).
- **Varas de Design de la Fase 3** (calibración visual, front funcional ya en su sitio):
  las estadísticas por espacio (T2), la bitácora por espacio (T3), los chips de etiqueta
  en la bitácora global (T4), el desglose "Tu proyecto completo" del Análisis (T4) y las
  fichas de Reporte por mundo en Documentos (T5). Encargo a CD si el fundador quiere pulir.
- **Píldora-humana** en las fechas: backlog post-beta (de la fidelidad al canon).
- La **decoración de papel** de los interiores del Expediente (ver §2, ligado al pedido a CD).
- **`cumplimiento-desglose-core-multiciclo`** (analytics): la fila "core" de
  `cumplimientoPorDominio` cuenta ítems de cualquier ciclo, mientras los tiles globales
  cuentan solo el plan baseline vigente. No es doble conteo; criterio distinto que puede
  no cuadrar con varios ciclos. Arreglo NO es de una línea (pasar el id del baseline a
  `cumplimientoPorDominio`). Nombrado en `docs/PLAN_ESPACIOS_FASE3.md §6`; **jamás
  arreglar "de paso"**.

## Hecho recientemente (para no reabrirlo por error)

- **Calendario**: modo con-fechas + recordatorios + `.ics` universal (webcal) EN PRODUCCIÓN.
  El **Google Calendar Nivel 1 se RETIRÓ** a favor del webcal universal (no reabrir).
- **Catálogo congruente** (precios 10/5, Tus Números incluido, beta sin cortesía): EN PRODUCCIÓN.
- **Espacios** Fase 1+2 + las 3 caras (Plan · Manos a la obra · Tu avance): EN PRODUCCIÓN.
