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
- **APLICACIÓN DE LA CALIBRACIÓN: EN PAUSA hasta la corrida del fundador
  (decisión, 2026-08-06).** Las entregas de CD están completas y guardadas, pero
  **nada se aplica al front todavía**: el fundador corre su idea nueva paso a
  paso sobre main y, al llegar a cada pantalla, decide. El front que se prueba es
  el implementado, sin vestir. Nada de esto es función: aplicar después no cuesta
  más que aplicar ahora, y probar sobre lo ya conocido evita confundir un fallo
  de función con uno de calibración.
- **PREGUNTA ABIERTA del fundador sobre el diagrama de fechas (a resolver cuando
  su corrida llegue ahí):**
  1. **Los rombos de protección chocan con la notación PM**: el rombo ES el
     símbolo del hito, y en este producto los hitos ya tienen lenguaje propio
     (la línea de "Tu avance", el timeline de La Celebración). **El error es de
     origen: lo especifiqué yo en el brief de P4**, CD solo lo dibujó. Caminos:
     (a) que la protección use un segmento corto en su renglón (marca de
     duración, no de hito) y el rombo quede reservado; (b) mantener el rombo y
     declarar que en este gráfico jamás se dibujan hitos.
  2. **Pieza F (letras junto a las barras): el fundador la rechaza** ("para eso
     existen las leyendas"). Producción YA respeta su regla (leyenda numerada
     arriba, solo números en las barras): F es lo que rompería eso. Si algo se
     toma de F, sería solo la jerarquía tipográfica de la leyenda.
  3. **Pregunta de fondo:** ¿el carril de protección debe vivir en el diagrama
     del núcleo, o su casa natural es el registro del mundo? Lo aprobó como
     lectura, pero si al verlo genera "¿esto es de riesgos o son hitos?", el
     gráfico del núcleo podría quedarse limpio.
- **Tiempo y protección — VUELTA 1 ENTREGADA Y ELEGIDA (2026-08-06):** CD entregó
  las piezas A, B y C (2 opciones cada una, formato perfecto, vara pasada:
  `_entrega-claude-design/Entrega 20260805`). **Veredicto del fundador: A2 (la
  pregunta y su escalera) · B1 (el rango como dato del cajón) · C2 (documento de
  columnas suaves).** **VUELTA 2 ENTREGADA** (`Entrega-desing 20260729/entrega-tiempo-y-proteccion-v2`):
  el cierre de v1 completo (los 380 de A2/B1/C2 + notas de dos viewports + el
  rename de "línea base" hecho) y D, E, F con dos opciones cada una (CD perfila
  D2 con el matiz de mundo, E1, F1). **Vara pasada salvo dos guiones medios en
  las notas de D y F** (ninguno en pantallas). **Sin veredicto de D/E/F: la
  pieza F está cuestionada de raíz por el fundador (ver arriba).** Aplicación al
  front: EN PAUSA.
- **Scheduler + Protección + fases del Gantt — PAQUETE DE ENCARGO LISTO
  (ago 2026):** brief y prompt en `docs/calibracion-design/`
  (`BRIEF_TIEMPO_Y_PROTECCION.md` + `PROMPT_TIEMPO_Y_PROTECCION_CD.md`, seis
  piezas A-F con copy exacto y reglas duras). Archivos base para CD: esos dos +
  `REGLAS_Y_TOKENS.md` + canon 06/10/11/13 + `BRIEF_GANTT.md`; los pares del
  gate (07b/07c, 13/13b, 14..14e) se adjuntan tras la corrida del fundador.
- **Mundos de protección — encargo CONSOLIDADO (campaña cerrada en contenido,
  ago 2026; front funcional en producción, esto es calibración visual):**
  - **El carril y sus rombos** en el Gantt del núcleo: toggle "Ver protección",
    sub-fila anidada bajo la banda de su etapa (restricción ya fijada: DENTRO de
    la jerarquía de fase), rombos verde=hecha / contorno azul=pendiente, title
    con mundo y texto. Par del gate: `14c_proteccion_carril`.
  - **El registro** en el hub del mundo: filas con detección · severidad en
    palabras · camino · "Protege: #N · título"; el estado vacío honesto. Pares:
    `14_proteccion_registro` y `14b_proteccion_documentos` (dos recuadros + chip).
  - **Los chips bidireccionales** del detalle: "Protegida" en el ítem del núcleo,
    la detección + "Protege:" en la respuesta del mundo, el retiro dicho. Par:
    `14d_proteccion_chip`.
  - **El aviso de no-llego** en el ritual de fechas del mundo: ámbar espejo,
    jamás regaño. Par: `14e_proteccion_no_llega`.
  - Más las **fases visuales del Gantt** ya fichadas (abajo): calibrar una vez,
    heredar en las tres vistas, y vestir el carril sin deshacerlo.
- **Fases visuales en el Gantt (ficha del fundador, ago 2026):** el Gantt ya es
  **por fases en datos y geometría** (una barra = una etapa; un solo cálculo y un
  solo componente sirven a las tres vistas: Análisis del núcleo, análisis de
  mundo y PDF). **La vara de CD:** tratamiento visual de fase (títulos
  jerarquizados, bandas/separadores, numeración visible) **calibrado UNA vez y
  heredado por las tres vistas**, más cualquier adición visual que CD proponga
  sobre el frente. Restricción ya fijada para P4 de protección: el **carril de
  protección nace DENTRO de la jerarquía visual de fase** (anidado bajo la banda
  de su etapa), para que la calibración de CD lo vista sin deshacerlo.
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
- **ESTADO REAL (aclaración del fundador, 2026-08-06): NADA se ha corrido en
  vivo todavía.** La estrategia es construir la infraestructura sólida primero y
  hacer al final UNA corrida completa, ya solo en búsqueda de detalles. Los
  merges y tags de scheduler y protección salieron con auditoría de código y
  suites (904 verdes), no con vuelo/gate en vivo: la corrida única de abajo
  cubre TODO lo acumulado (scheduler F0..F4 + protección 2P + los pares nuevos
  del gate). El commit de cierre de protección en main dice "corrida del
  fundador hecha": quedó mal dicho y esta nota es la corrección del registro.
- **CORRIDA ÚNICA (todo lo acumulado) — instrucciones:**
  1. `cd web` y `pnpm dev` (puerto 3000, Supabase real con 033/034/035 aplicadas).
  2. **Vuelo:** `npx tsx scripts/vuelo.ts`. La fase nueva es la **2P**: snapshot
     vivo (y ausente en el mundo de mejora), el PAR de la pregunta anclada
     impreso para tu muestreo (DE/A), plan enlazado sin fallos del enlazador,
     registro sin puntajes, carril en la etapa del protegido, anclas con
     prioridad y no-llego. **Tu censo de costos** sale al final de esa fase:
     "CENSO DE COSTOS DE PROTECCION (por pieza)" con diagnóstico / anclaje /
     estimación / enlace y su total; la única alarma es la mención de sentido
     común si una pieza llega a $0.50+.
  3. **Gate:** `npx tsx scripts/gate_canon.ts` (dev corriendo). Los pares de la
     campaña: `14_proteccion_registro`, `14b_proteccion_documentos`,
     `14c_proteccion_carril`, `14d_proteccion_chip`, `14e_proteccion_no_llega`,
     en `web/examples/gate-canon/`.
  4. Con tu **"visto, mergea y etiqueta"**: merge del cierre a main + tag
     propuesto **`web-v2.4.0-beta`**.
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

- **`mundos-de-proteccion-sobre-lo-existente`** → **PROMOVIDA A CAMPAÑA.** La spec del
  fundador es **`docs/PLAN_MUNDOS_PROTECCION.md`** (5 ago 2026), que responde las
  cuatro preguntas que esta ficha dejó abiertas y añade las herramientas canónicas
  minadas del grafo. La ficha se conserva abajo como el origen de la decisión; **lo
  que manda es la spec**. Decisión futura del fundador: alimentar a **Riesgos Bajo Control, HSEQ
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

## Ficha del futuro mundo `Primer Equipo`

Dos conceptos de quality se deprecaron de la selección en la re-voz (ago 2026)
**no por malos, sino porque su concepto anclado es la estructura de equipo**:

- **Equipo de Mejora de Calidad** `equipo_mejora_calidad_2`
- **Involucramiento del Sindicato en Programas de Calidad** `involucramiento_sindical_calidad`

Reencuadrarlos a persona-sola habría sido escribir un nodo que la fuente no
escribió. Siguen en el grafo (nadie se borra) y **su minería propia podrá
renacerlos desde sus fuentes** cuando ese mundo exista.

## Campaña fichada: `re-voz-de-hseq` — PRIORIDAD ALTA, PRE-BETA

**Se dispara tras la fusión de Seguridad y Personas**, que ya está hecha. La
secuencia fusión-primero volvió a pagarse sola: el censo previo marcaba 57 nodos
con hallazgo y tras absorber 48, el paciente quedó en **49**.

**Censo post-fusión**: {'matriz_o_puntaje': 3, 'residuo_corporativo': 20, 'dato_local_cableado': 27}

**Por qué es prioridad alta y no puede esperar a después de la beta**, a
diferencia de la de quality: **27 de los hallazgos son DATO LOCAL CABLEADO, y casi
todos son OSHA** — un organismo de Estados Unidos citado como si fuera el marco
de todos. Para un usuario de cualquier otro país eso no es un defecto de estilo:
es una **deuda de credibilidad**. Un emprendedor en Bogotá o en Lima que lee
"según exige OSHA" descubre en dos clics que OSHA no le aplica, y con eso pierde
la confianza en el resto del mundo, no solo en ese nodo.

El trabajo: el método se conserva, el organismo se vuelve *"averigua qué
organismo regula esto en tu país"*. Mismo circuito de re-voz ya curtido, con las
barandas del taller (no las de la fábrica) y el guardián de rumbos vigilando.

## Campaña CERRADA: `re-voz-de-quality`

**Se dispara al CERRAR la cirugía de fusión de Calidad, no antes.** La secuencia
fusión-primero es aritmética: los nodos absorbidos ya no hay que re-vozarlos.

**El hallazgo que la origina** (cirugía de Calidad, 2026-08-07): los detectores
de las tres barandas sobre los **896** nodos de `quality` marcaron **209 (23%)**.
El censo los había muestreado con 10 nodos y dio 0/10; una muestra detecta lo
sistémico, no mide prevalencia. Verificado leyendo, no confiando en el patrón:
son reales.

| patrón | nodos |
|---|---:|
| "la gerencia" / "la alta dirección" | 149 |
| "el equipo" | 21 |
| "el departamento" | 17 |
| matriz o puntaje | 9 |
| dato local cableado | 4 |

Calidad está escrito en **voz de dirección corporativa**: *"justificar ante la
alta dirección"*, *"comparar con las expectativas de la gerencia"*. Eso viola la
lente de persona-sola-con-teléfono de la vara vigente.

**El trabajo**: regeneración-CON-ANCLAJE de los supervivientes que estén entre
los 209 marcados. Mismo fragmento de fuente, lente persona-sola, la gerencia
muere. Por lotes, con muestreo del fundador entre lote y lote. Cero invención:
lo que no esté en el fragmento no se escribe.

**EL PACIENTE REAL, tras la fusión** (2026-08-07): de los 209 marcados, **24 se
deprecaron** al fundirse y **185 sobrevivieron**. Ese es el lote a regenerar:

| patrón | nodos vivos |
|---|---:|
| residuo corporativo | 174 |
| matriz o puntaje | 8 |
| dato local cableado | 4 |

La secuencia fusión-primero se pagó sola: 24 nodos que habrían costado API ya
no existen como sujetos.

**Los datos ya están**: `packs/quality/poda/_revoz_lote.json` trae la lista
exacta de los 185 vivos, y `_poda_quality.json` la cita textual y el patrón de
cada uno. La campaña arranca sin volver a medir nada.

## REQUISITO DE TODA REGENERACIÓN: la prueba de rumbos

**Cualquier cosa que cambie el índice semántico corre `scripts/rumbos/prueba_rumbos.py`
antes de darse por hecha.** Sin excepción, y aunque el cambio "sea pequeño".

Qué la dispara:
- un reindex de Voyage (`build_semantic_index_voyage.py`)
- la re-voz de un pack (185 nodos regenerados = 185 embeddings nuevos)
- una fusión, una deprecación, un pack nuevo
- cualquier edición masiva de `resumen_teorico` o `titulo_concepto`

Ya está cableada como paso `d-bis` de `integrar_packs.py`, justo detrás del
reindex. Fuera de ese flujo, se corre a mano.

**Por qué**: Gate 0 dice que el grafo está sano, las suites que el código cumple,
el vuelo que el viaje corre. Ninguno dice si la brújula APUNTA BIEN. Una deriva
de puntería no rompe nada: manda a la persona equivocada al mundo equivocado, en
silencio, y se descubre en el recorrido de alguien.

La línea base vive committeada en `scripts/rumbos/linea_base_rumbos.json`. La
prueba sale con código 1 si algún rumbo cambia de estado.

## Al margen, sin acción: `matriz_probabilidad_impacto` (núcleo)

Anotado al re-anclar los puentes (ago 2026), **sin acción y sin urgencia**: el
núcleo tiene un nodo `matriz_probabilidad_impacto` que es doctrinalmente lo
contrario de la doctrina anti-matriz de la casa. Hoy es útil justo por eso: es el
ancla del **puente correctivo** hacia "Evalúa la gravedad sin autoengaño" del
mundo de Riesgos, y el antídoto se ancla en el punto de exposición.

Queda como **candidato a ojo en la eventual revisión del núcleo post-beta**, con
la misma vara que todo lo del núcleo: la telemetría es testigo obligado antes de
tocar nada. Si algún día se revisa, hay que mirar también su puente: sin el
ancla, el correctivo pierde su punto de exposición.

## Ficha: `re-voz-de-environmental` — REGISTRADA, SIN DISPARO

**El plan escalonado del censo está COMPLETO.** Esta ficha no es un pendiente
del ciclo: es el candidato natural del siguiente, y **el tablero es del
fundador**.

`environmental` cerró con **291 activos y 23 hallazgos** (7,9%), el más alto de
los cinco packs de este ciclo y por encima de la media del catálogo (6,6%). Su
fusión ya corrió; lo que queda es la voz.

No se dispara nada hasta que el fundador lo ponga en el tablero.

## FRENTE DE RECUPERACIÓN — abierto con evidencia, para la campaña del motor

**Demostrado experimentalmente (ago 2026), no supuesto.** La voz **no** cura la
puntería de la brújula.

**La evidencia**: se re-vozó el vecindario completo de tres rumbos que subían sin
llegar (13 rivales directos + su rama). Con todo el vecindario hablando igual de
bien, **los blancos no subieron: retrocedieron**, y los rivales —todos en el
lote— siguieron ganando.

| rumbo | blanco | rivales que ganan |
|---|---|---|
| *"nadie me ha pagado"* | 67 → **78** | `profit_vs_cash`, `cash_is_king` |
| *"por qué me comprarían"* | 82 → **83** | `necesidad_vs_deseo_en_ma` (¡fusiones y adquisiciones!) |
| *"le sirve a todo el mundo"* | 245 → **252** | `anticipar_consecuencias_negativas` |

**El diagnóstico**: la brújula se engancha a **palabras sueltas**. *"pagado"* la
lleva a las finanzas, *"me comprarían"* a M&A, *"está mal"* a las consecuencias
no intencionadas. Ninguna es un problema de contenido ni de voz.

Y el contraste lo cierra: los dos rumbos cuyo vecindario **no** competía por las
mismas palabras **sí** llegaron al top-10 con solo re-vozar.

### PRUEBA DE ACEPTACIÓN del frente

> **Los tres rumbos de arriba se ponen VERDES.** Están en el banco como
> `diagnostico: true`, fuera del marcador y con su expectativa escrita al lado.
> El día que el frente funcione, se quitan de diagnóstico y entran a la vara.

### LAS TRES VÍAS POR PROBAR, en orden de costo (adjudicadas ago 2026)

**(a) La asimetría de `input_type`.** Verificar que el corpus se embebió como
`document` y que las consultas van como `query`. Si no coinciden, **hay puntería
perdida gratis**, sin tocar un solo nodo. Es lo más barato que hay: se reporta al
abrir el frente.

**(b) Embeber y CONSULTAR las `condiciones_activacion` aparte**, con índice o
peso propio, para que **la situación compita contra la situación** en vez de
diluirse dentro del concepto. Hoy están dentro del mismo vector que el título y
el resumen, y ahí se pierden.

**(c) Un reordenador sobre el top-k de la búsqueda vectorial**, que lee consulta
y nodo juntos. Es la cura clásica del enganche léxico, y la más cara.

### PRUEBA DE ACEPTACIÓN, CERRADA Y CONGELADA

**LOS TRES RUMBOS REBELDES**, identificados por nombre contra la foto final de
`scripts/rumbos/_puestos_final.json`:

| rumbo | ancla | puesto de partida |
|---|---|---:|
| `nucleo_dicen_que_si_pero_no_compran` | `get_out_building_test_sell` | **67** |
| `nucleo_por_que_me_comprarian_a_mi` | `value_proposition_startup` | **82** |
| `nucleo_le_sirve_a_todo_el_mundo` | `customer_segments_hypothesis` | **245** |

Los otros dos rumbos de diagnóstico (`nucleo_validar_antes_de_gastar` y
`nucleo_sacar_algo_pequeno_primero`) **ya se pusieron verdes** tras la fusión y
la re-voz del núcleo: no son prueba, son trabajo hecho. El de hueco
(`nucleo_no_doy_abasto_solo`) no entra: **lo cierra el mundo 11, no el motor**.

**PASA la vía si**:

a) **los tres rebeldes quedan verdes**: ancla dentro del top-K con K=10, dominio
   correcto, sin frontera violada;
b) **el trinquete aguanta**: cero rojos en los 43 del marcador y ámbares menores
   o iguales a la línea base de 1;
c) **`nucleo_validar_antes_de_gastar` y `nucleo_sacar_algo_pequeno_primero` NO
   retroceden fuera del top-K**.

**Las tres condiciones son necesarias. Arreglar tres rompiendo otros no es
arreglar.**

**CÓMO SE MIDE**: se reportan **las dos cosas** en cada corrida, el marcador de
colores **y** los puestos exactos de las cinco anclas vía
`scripts/rumbos/puesto_de_blancos.py`. El puesto es la medida continua: bajar de
245 a 30 es progreso real aunque el color no cambie, y el marcador solo no lo
vería.

**ESTA VARA QUEDA CONGELADA.** No se renegocia después de ver resultados de
ninguna vía. Si una vía obliga a cambiarla, se para y se adjudica antes de
seguir.

### LA VARA CADUCA SI ENTRA CATÁLOGO NUEVO

Los puestos de partida (**67, 82 y 245**) se midieron el **8 de agosto de 2026**
sobre un catálogo de **3.521 nodos activos**. El puesto de un ancla es una
posición **RELATIVA**: si entran cientos de nodos nuevos (mundo 11, la garantía
honesta en el núcleo, la huella en Ambiente), esos puestos **se mueven solos por
dilución**, sin que nadie haya tocado el motor.

Por lo tanto:

a) Si el frente de recuperación se abre **ANTES** de integrar nodos nuevos, la
   vara vale tal como está congelada.
b) Si se integra catálogo nuevo primero, **la línea base se vuelve a medir ANTES
   de abrir ninguna vía**, y se anota junto a los números nuevos **el tamaño del
   catálogo sobre el que se midieron**. Los puestos viejos **NO** se comparan con
   los nuevos como si nada hubiera pasado.

**Recomendación del auditor: correr el frente primero.** Las tres vías son
experimentos cortos; la minería son días.

### Hipótesis original del auditor — CORREGIDA con el código en la mano

La hipótesis era *"embeber también las `condiciones_activacion`: es dato que ya
existe y sería un spike barato"*. **Parte de una premisa falsa**:
`scripts/build_semantic_index_voyage.py:56-62` ya las incluye en el texto que se
embebe, junto al título y el resumen. **Los tres rumbos rebeldes fallan con ellas
dentro.**

Eso no mata la intuición, la reorienta: si el campo escrito como situación ya
está en la mezcla y no basta, lo que queda por probar es **embeberlo aparte y
consultarlo aparte** — dos índices, o un campo con peso propio en la puntuación—
en vez de *añadirlo*. No lo diseño aquí.

Lectura completa del uso real del campo en
`docs/LECTURA_CONDICIONES_Y_DEPRECADOS.md`.

**Embeber también las `condiciones_activacion`.** Están escritas como
situaciones —*"Cuando el emprendedor está tratando de…"*, *"Si dudas entre pagar
más por mejores profesionales"*— y **se parecen mucho más a como escribe un
usuario** que el texto conceptual del resumen. Es dato que **ya existe** en los
3.511 nodos: sería un spike barato.

Nota mía sobre esa hipótesis, de este mismo ciclo: cuando se excluyó ese campo de
la cuarta baranda fue precisamente porque **describe la situación del lector en
tercera persona por diseño**. Ese es el argumento a favor: es el campo escrito
desde la situación, no desde el concepto.

Lo demás del frente vive en `docs/AUDITORIA_MOTOR.md`, archivada.

## DECISIÓN DE DISEÑO: las `condiciones_activacion` NO son compuerta, y así se quedan

**Adjudicada ago 2026, con el código leído.** No filtran: suman puntaje léxico en
cuatro sitios del motor y viajan al intérprete dentro de `resumenNodo`, que las
lee antes de elegir.

**El porqué, y es el argumento que la sostiene:**

> Cuando el motor decide, **todavía no sabe casi nada del usuario**. Filtrar por
> una condición que el usuario aún no ha declarado mataría nodos legítimos por
> falta de información, no por falta de encaje. Sumar puntaje y entregarle las
> condiciones al intérprete es lo correcto: pesa hacia quien encaja sin cerrarle
> la puerta a quien todavía no ha contado su situación.

**La advertencia queda registrada igual**: es un peso, no un muro. Si el catálogo
se quedara sin mejores candidatos, un nodo de escala corporativa se le ofrecería
igual a quien trabaja solo.

**Y la seguridad se compra con un guardián, no con un filtro**: el rumbo-trampa
`frontera_artesana_sola_no_corporativo` en el banco de rumbos. Una consulta de
artesana sola que **no debe devolver nodos de escala corporativa en el top-3**.
Si la política de escala empezara a estorbar, ese rumbo lo canta antes que un
usuario.

## EL SEGUNDO ÍNDICE (`engine/semantic_index.npz`) Y EL MOTOR DE CLI

**Estado: fósil vigilado, no retirado.**

**Sus datos**: generado **2026-07-08**, sentence-transformers, 384 dimensiones,
**1.266 vectores contra 3.521 activos**. Sin consumidores fuera del CLI, sin
prueba que lo ejercite, sin flujo que lo regenere.

**Por qué no se retiró**: en el CLI vive el port original y la documentación viva
de las rutas de la web.

**Por qué NO entra al Gate 0**: el Gate es la puerta del catálogo y no se ata a
un artefacto sin consumidores en la línea de ensamblaje. Obligaría a regenerarlo
en cada minería para nada, y **un guardián que cobra peaje por trabajo inútil se
acaba desactivando**.

**Qué se hizo en su lugar**: la brújula del CLI **se niega a operar** si el
índice no cubre a todos los activos. Cero tolerancia, aviso una vez por sesión
con el comando de regeneración, y sin lanzar: el motor sigue con navegación
local, el mismo respaldo que ya existe cuando falta la clave de Voyage en la web.

**CONDICIÓN DE RETIRO, fijada por adelantado**: el CLI y su índice se retiran
cuando **el último flujo que hoy solo existe ahí tenga puerto en la web**. Hasta
entonces vive, vigilado y honesto. **No se relitiga** sin que esa condición se
cumpla o sin evidencia nueva.

## Ficha: `huecos-de-contenido` — documentados sin inventarlos

Vacíos REALES del catálogo, encontrados midiendo y **no rellenados a mano**.
Material de minería futura: el día que se extraiga un libro que los cubra, ya
está dicho qué falta y por qué se supo.

- **El núcleo no tiene nodo de PRIMERA CONTRATACIÓN.** Cero aciertos en el
  barrido sobre los 1.721. El rumbo `nucleo_no_doy_abasto_solo` lo documenta: sin
  contenido, la brújula manda esa consulta a *"quemar las naves"*. El contenido
  natural es del futuro mundo **Primer Equipo**, cuya ficha ya está abierta y que
  heredó dos conceptos deprecados de quality. El día que ese mundo nazca, ese
  rumbo lo estrena.
- **`environmental` no tiene huella de carbono a ESCALA DE TALLER.** Los dos
  nodos que había (`evaluar_huella_carbono` y `medir_huella_carbono_corporativa`)
  eran **el mismo inventario corporativo formal** del mismo libro, con el mismo
  entregable, y se fundieron. Nadie cubre *"cuánto contamina lo que hago yo"* a
  escala de una persona con un taller.

Ninguno se inventa. **Un hueco documentado vale más que un nodo fabricado para
taparlo**: el nodo fabricado se ofrece, y lo que se ofrece se cree.

## DOCTRINA DE LA VÁLVULA (ago 2026)

> **El título mentía, los pasos no.**

**La válvula de `pasos_accionables` es la última palabra de toda fusión.** Un
índice de fusión propone por parecido de superficie —título, resumen, sigla,
vocabulario— y ese parecido es una **pista, no una prueba**. Lo que decide es si
el lector *hace* lo mismo en los dos sitios. Cuando el solape de pasos cae bajo
el umbral, la fusión **no se ejecuta y no se discute**: vuelve como duda para
adjudicación.

En el ciclo del censo revocó **tres** fusiones que el índice daba por hechas, y
las tres se conservaron como nodos propios. Las adjudicaciones, con el porqué de
cada par, en `packs/environmental/poda/DUDAS_DE_LA_VALVULA.md` y
`packs/exportacion/poda/DUDAS_DE_LA_VALVULA.md`.

Corolario: **una institución no es un concepto.** Dos nodos que citan la misma
sigla pueden pedir cosas opuestas al lector.

## POLÍTICA DEL NÚMERO HONESTO (ago 2026)

> **Un número honesto con su límite declarado vale más que uno redondo de
> memoria.**

Nace de una confesión propia: al cerrar el ciclo del censo no se pudo certificar
el costo total. Cada corrida imprimía lo suyo y lo escribía en un informe que la
corrida siguiente **pisaba**, así que al final solo quedaba la última tanda de
cada script. La suma habría tenido que salir del chat.

El arreglo: **`docs/COSTOS.jsonl`**, un libro de apéndice —una línea por corrida,
nunca se reescribe— que `revoz_pack.py` y `consolidar_pack.py` alimentan con
fecha, pack, operación y costo. `python scripts/libro_mayor.py` lo suma.

### LA FRONTERA DEL CICLO DE LA CURACIÓN DEL MOTOR

El libro tiene **66 corridas por $16,54**, y el ciclo de la curación del motor
reportó **$15,25 en 57 corridas**. La diferencia está explicada, y se deja
escrita para que nadie concluya después que el reporte mintió:

> **La primera corrida de este ciclo es la de `2026-08-08T16:08:53+00:00`**
> (environmental / consolidación / $0,03). Todo lo anterior son **9 filas que no
> le pertenecen**: la línea de apertura del libro ($0,00) y **8 filas rescatadas
> y marcadas `parcial`** ($1,29), que son del ciclo del censo y se recuperaron
> de informes que se pisaban unos a otros.

El libro **no se toca**: es un registro, y un registro al que se le quitan filas
deja de serlo. Lo que se corrige es el reporte, diciendo dónde empieza a contar.

Las filas rescatadas del ciclo viejo van marcadas **`parcial`** y el resumen lo
dice en voz alta: un total con filas dudosas se declara dudoso en vez de sonar
exacto. **El próximo ciclo cierra con total certificable.**

## Campaña del gradiente: el tablero vive en su auditoría

**Puntero, para que la decisión no viva solo ahí.** El tablero completo de la
campaña está en `docs/audits/AUD-08-Gradiente_Nucleo_Mundo.md`, y las fichas de
fusión que abrió, en `docs/FICHA_SUBFUSION_GRADIENTE.md`.

**DECISIÓN DEL FUNDADOR (ago 2026): el barrido INTRA-DOMINIO se hace y cierra el
100%** (el núcleo contra sí mismo y cada mundo contra sí mismo). Converge con la
pregunta **mundo contra mundo** y con la clase de huérfanos **por nombre libre**,
que quedó declarada NO MEDIDA: **son tres caras del mismo instrumento**, que es
`scripts/gradiente_pares.py` con otro emparejamiento.

**ORDEN FIJADO**: primero se agota la cola de 346, después la franja bajo el
umbral, y **el intra-dominio AL FINAL**, porque muchos de sus pares caerán solos
cuando las fusiones de la ficha se ejecuten. **El instrumento no se extiende
hasta llegar ahí.**

## Ficha permanente: `vigencia-del-marco-internacional`

Nace con el ciclo del censo (ago 2026). Los nodos de exportación que citan
**marcos versionados o tratados vigentes** —Incoterms, cartas de crédito,
códigos arancelarios, cláusula antidesviación, EAR— ganan nota de vigencia y
entran a revisión cuando el comercio cambie de rumbo.

**Las instituciones-de-libro jamás se omiten: se mantienen al día.** Incoterms
2020 no es un dato local ni un detalle de estilo: es el vocabulario acordado
entre países, y un catálogo que lo cite desactualizado miente con precisión.

### Entrada del gradiente (lote 7, puesto 53), sin tocar el nodo

`exportacion/proteccion_propiedad_intelectual_internacional` **cablea `uspto.gov`
y `stopfakes.gov`**, agencias de **un solo país**, en su paso 3.

**La frontera cae limpia dentro de la doctrina de esta ficha**, y por eso el nodo
se anota entero en vez de partirse:

- **PCT y Madrid Protocol (paso 2) son INTOCABLES**: son tratados multinacionales,
  el vocabulario acordado entre países, exactamente la clase de Incoterms.
- **Las dos URLs de agencias son la clase "ejemplar de un país"**, y piden el
  reencuadre *"averigua el de tu país"* cuando esta ficha despierte.

**El nodo no se toca desde el gradiente.** Queda aquí porque su revisión es de
vigencia de marco, no de profundidad.

### Entrada del cribado de la franja: `seguridad_digital`, y no es una entrada suelta

Viene de la adjudicación de la franja (`docs/FRANJA_INFORME.md`, apartado 4.6 y
sección 9.4). **Es el primer miembro de esta ficha que NO es de exportación**, y
por eso la anoto aquí en vez de abrirle ficha propia: la clase es la misma
(marco de un solo país cableado sin condición de país). **Si el auditor prefiere
ficha aparte, mudarla cuesta una línea.**

**El caso citado**: `seguridad_digital/getting_started_supply_chain_risk_management`,
cuyo paso 1 manda *identificar proveedores críticos con acceso a sistemas que
procesan **CUI***. CUI es una designación federal estadounidense y arrastra
detrás el NIST SP 800-171. Es la **tercera instancia registrada** en ese mundo,
después de los dos POA&M.

**Y al ir a contarla, el censo cambió el tamaño del problema.** Medido contra el
grafo, nodo por nodo:

> **20 de los 55 nodos de `seguridad_digital` cablean el marco federal
> estadounidense en sus pasos** (trece con CUI, cuatro con NIST, cuatro con
> SP 800, cuatro con POA&M, con solapes). **Más de un tercio del mundo.**

**Lo que eso significa para esta ficha**: en `seguridad_digital` el problema no
son tres nodos sueltos que se arreglan uno por uno, **es el encuadre entero del
mundo**. El cribado sólo vio los que la cola le puso delante. **Cuando esta
ficha despierte, en este mundo lo primero es el barrido, no la entrada suelta**,
igual que ya está escrito para la ficha hermana.

**Ningún nodo se toca desde aquí.**

### El bloque CONTRAMODELO más consistente del catálogo: la familia Magnuson-Moss

Registrado el **9 ago 2026**, y entra aquí porque esta ficha necesita tanto sus
miembros como sus contramodelos: sin contramodelo, la ficha no tiene vara.

**SEIS nodos del núcleo**, todos de *Businessperson's Guide to Federal Warranty
Law*, **condicionan por país de forma explícita** (el sexto se verificó el 10 ago
2026, leyendo la tanda 12 de costuras):

| nodo | primera `condiciones_activacion` |
|---|---|
| `cumplimiento_magnuson_moss` | *Si vendes, o piensas vender, productos a clientes en Estados Unidos.* |
| `regla_disponibilidad_previa_venta` | la misma línea, literal |
| `clasificacion_garantia_full_limited` | la misma línea, literal |
| `evitar_terminos_enganosos_garantia` | la misma línea, literal |
| `regla_divulgacion_garantia` | la misma línea, literal |
| `publicidad_garantia_conforme` | *vendes, o piensas vender, productos a clientes en Estados Unidos*, **y además** condiciona por el uso de la palabra *lifetime* y por el umbral de los 15 dólares |

**Y cuatro de los cinco lo repiten en el `resumen_teorico`** con la instrucción
de buscar la norma equivalente: *como es una ley de Estados Unidos, si vendes en
otro país conviene revisar la norma equivalente que aplique allí*.
`cumplimiento_magnuson_moss` lo repite además en su `entregable_esperado`, o sea
**tres veces en el mismo nodo**.

> **Este es el patrón que la ficha debería pedir para todo lo demás**: no se
> borra el marco nacional, se **condiciona** y se manda buscar el equivalente
> local. El lector de otro país no pierde el nodo, sabe qué hacer con él.

**Historia verificada contra git, porque la pregunta correspondía**: el nodo se
creó el **2026-07-11** (`722bfa5d`) ya con condición de país (*se vende a
consumidores finales en EE.UU.*), y el **2026-08-08** el commit `9e22a53f`
(*Regulación cerrada*) la reescribió a la forma explícita actual. **Nunca perdió
la condición: la ganó más fuerte.** No hay cambio de contenido que rastrear.

> **Corrección que esto obliga**, ya aplicada: el apartado 4.6 de
> `docs/FRANJA_INFORME.md` clasificaba `cumplimiento_magnuson_moss` como uno de
> los **dos casos duros de marco-país del núcleo**. Baja a contramodelo, el
> veredicto de la franja 1297 pasa de C a D, y cinco veredictos del cribado
> intra-dominio (157, 159, 162, 164 y 171) pasan de C a D. **La causa fue leer
> `pasos_accionables` sin leer `condiciones_activacion`.**

**Alcance del error, medido**: de los **52 nodos** implicados en los **33
veredictos** de la franja que citan la figura, **solo 4 llevan condición de
país**, y uno de ellos ya estaba listado como contramodelo. **El censo de la
figura se sostiene.**

#### Adjudicación provisional del auditor: es un CASO A ESCALA DE MUNDO

Con el conteo de arriba sobre la mesa (20 de 55 nodos: 13 con CUI, 4 con NIST, 4
con SP 800, 4 con POA&M, con solapes), **el auditor reclasifica el caso**. Deja
de ser *tres instancias sueltas de marco-país en un mundo* y pasa a ser
**un caso a escala de mundo**: cuando más de un tercio de los nodos comparten el
mismo encuadre nacional, el encuadre es del dominio, no de los nodos.

**Remedio candidato, provisional:**

> **UNA condición o declaración de marco a nivel de dominio, no veinte parches
> nodo a nodo.** Los principios viajan (la disciplina de identificar proveedores
> críticos, de evaluarlos antes de contratar, de tener plan de respuesta); **los
> artefactos de cumplimiento son de Estados Unidos** (CUI, NIST SP 800-171, el
> POA&M). Una sola declaración que separe las dos cosas cubre los veinte nodos y
> no deja veinte redacciones distintas de la misma advertencia.

**Es provisional en dos sentidos, y los dos importan:**

1. **La decisión final es del fundador**, y se toma en el barrido, no aquí.
2. **El remedio es candidato, no dictado.** Antes de escribirlo hay que ver los
   veinte nodos juntos: puede que unos pocos sí necesiten reencuadre propio (los
   que hacen del artefacto el objeto del nodo, no una mención), y esos no los
   cubre ninguna declaración de dominio.

**Sigue sin tocarse nada.** Esta entrada solo cambia de qué tamaño es el
problema y por dónde conviene agarrarlo.

## Ficha permanente hermana: `vigencia-de-herramientas-nombradas`

**Nace del lote 8 del gradiente (puesto 69).** Es **hermana** de la de arriba, no
una entrada suya, y conviene explicar por qué se abrió aparte: aquella se declara
a sí misma sobre **nodos de exportación que citan marcos versionados o tratados**,
y esto es **otra clase** (una herramienta comercial citada por su nombre, en un
nodo del **núcleo**). **Si el auditor prefiere una sola ficha, fundirlas cuesta
una línea.**

**El principio es el mismo que ya está escrito arriba**: un catálogo que cita algo
desactualizado **miente con precisión**.

### Entrada 1: `nucleo/seo_link_building`

Su paso 4 dice *"revisa tus enlaces y los de tu competencia con una herramienta
como **Open Site Explorer**"*. **Moz retiró esa herramienta.** El consejo sigue
siendo bueno; **el nombre propio ya no existe**.

**Clase del arreglo**: no es dato local ni profundidad. Es **una herramienta
nombrada que caducó**, y el reencuadre natural es **describir la capacidad en vez
del producto** (*"con una herramienta de análisis de enlaces"*), que además no
vuelve a caducar.

**El nodo no se toca desde el gradiente.**

### Entrada 2 (10 ago 2026): las DOS PRIMERAS herramientas declaradas MUERTAS, con evidencia

Salen de verificar las seis que nombra `nucleo/retargeting_display`, y son las
primeras que esta campaña puede declarar muertas en vez de anotarlas sin
verificar.

| herramienta | estado | evidencia |
|---|---|---|
| **Perfect Audience** | **MUERTA** | TrustRadius la lista como *(discontinued)*; comprada por Marin Software en 2014 y por SharpSpring en 2019, y descontinuada después |
| **The Deck** | **MUERTA** | **cerró en marzo de 2017**, anunciado por su fundador Jim Coudal; cubierto por TechCrunch y Daring Fireball |
| AdRoll | viva | plataforma de NextRoll, activa en 2026 |
| MixRank | viva | operando en 2026 |
| Adbeat | viva | activa en 2026 |
| BuySellAds | viva | operando en 2026 |

> **Las dos muertas viven en el mismo nodo y en pasos distintos**: `Perfect
> Audience` en el paso 1, entre los píxeles a instalar, y `The Deck` en el paso
> 4, entre las redes de nicho a evaluar. **Un lector que siga ese nodo hoy
> instalaría el píxel de una plataforma descontinuada y evaluaría una red que
> cerró hace nueve años.**
>
> **El nodo es sano como costura y está caducado como consejo.** Son dos
> preguntas distintas y las dos hay que contestarlas.

### Entrada 3 (10 ago 2026): cinco nombres más del lote grande, verificación PARCIAL

**El lote de veinticuatro no se pudo cerrar en esta pasada** y queda abierto a
propósito: la búsqueda web estuvo caída durante parte del trabajo y **no se
escribió nada de memoria**. Lo que sí quedó verificado con evidencia:

| nombre | estado | evidencia |
|---|---|---|
| **Alexa** (alexa.com, ranking web de Amazon) | **MUERTA** | Amazon la retiró el **1 de mayo de 2022**, anunciado en diciembre de 2021; las APIs cerraron en diciembre de 2022. **NO es una entrada nueva**: esta ficha ya la daba por retirada desde la entrada del lote 22, vía `nucleo/analisis_trafico_competitivo`. **Una sola herramienta muerta, TRES procedencias** (corregido en la entrada 4: escribí dos y son tres) |
| **oDesk** | **MUERTA como marca** | rebautizada **Upwork en mayo de 2015**; el dominio redirige |
| **Elance** | **MUERTA como marca** | fusionada en Elance-oDesk y **retirada tras el rebranding a Upwork** |
| **InnoCentive** | **VIVA, con dueño nuevo** | **adquirida por Wazoku en julio de 2020**; sigue operando dentro del grupo |
| **Guide to Greener Electronics** (Greenpeace) | **NO VERIFICABLE** | la última edición localizable es la de **2017**; no se encontró anuncio de discontinuación, así que no se declara muerta |

> **CORRECCIÓN DE LA CIFRA, recomputada del censo entero el 10 ago 2026**:
> escribí *cuatro muertas y cinco vivas de once verificadas* y **no conté
> `Compete`**, que la entrada del lote 22 ya daba por retirada junto con Alexa.
>
> | | |
> |---|---:|
> | **muertas** | **6**: Alexa, Compete, Perfect Audience, The Deck, oDesk, Elance |
> | **vivas** | **5**: AdRoll, MixRank, Adbeat, BuySellAds, InnoCentive |
> | **no verificables** | **1**: Guide to Greener Electronics |
> | **verificadas** | **12** |
>
> **Seis muertas de doce verificadas: la mitad.**
> **Los dieciocho que quedaban se verificaron el mismo día: ver la entrada 4,
> que cierra el lote y corrige esta cifra.** El censo entero no va en seis
> muertas de doce sino en **siete de treinta**, y el motivo de la diferencia es
> el hallazgo, no un error de suma.

> **Por qué esta ficha vale la pena aunque hoy tenga una sola entrada**: el
> catálogo nombra herramientas en más sitios, y **ninguna revisión las ha
> barrido**. La primera que apareció, apareció **de rebote**. Cuando se despierte,
> lo primero es **el barrido**, no la entrada suelta.

### Entrada 4 (10 ago 2026): EL LOTE CIERRA, y con él aparece una segunda forma de caducar

**Los dieciocho nombres que quedaban abiertos están verificados con evidencia y
el lote de veinticuatro queda cerrado.** El resultado no es el que la ficha
esperaba, y **el hallazgo no es la cuenta de muertas: es que hay DOS formas de
caducar y el censo solo estaba contando una.**

#### Las tres que no siguen tal como el catálogo las nombra

| nombre | estado | evidencia |
|---|---|---|
| **Visual Website Optimizer** | **MUERTA COMO MARCA** | Wingify la rebautizó **VWO en junio de 2014**. El producto vive; **el nombre que usa el catálogo no** |
| **Empty Miles Service** (VICS / GS1) | **NO VERIFICABLE**, con el dueño desaparecido | VICS firmó la fusión con GS1 US el **10 sep 2012** y la completó a final de año. **No encontré página viva del servicio ni anuncio de cierre**, así que no lo declaro muerto |
| **RentaGreenBox** | **NO VERIFICABLE, FUENTES EN CONFLICTO** | **Crunchbase la da por cerrada de forma permanente**; **Yelp muestra local activo en Huntington Beach a julio de 2026** y el sitio propio responde. **No lo fuerzo en ninguna dirección** |

#### Las quince vivas, y seis de ellas vivas de otra manera

| nombre | estado | evidencia |
|---|---|---|
| **GS1** | **VIVA, y mandando** | gobierna GTIN/EAN/UPC desde 1973 y conduce **Sunrise 2027**, la transición al código 2D en punto de venta |
| **EPCglobal** | **VIVA COMO ESTÁNDAR, no como organización aparte** | se constituyó **dentro de GS1 en 2005**; hoy es una iniciativa de GS1, no una entidad independiente |
| **Google Analytics** | **VIVO EL NOMBRE, MUERTA LA VERSIÓN** | **Universal Analytics dejó de recoger datos el 1 jul 2023**; en jul 2024 se cortaron el acceso y la API **y se borraron los datos**. Solo existe GA4 |
| **Energy Star** | **VIVO, Y CAMBIÓ DE CASA** | la EPA propuso eliminarlo en 2025, con cero dólares en el presupuesto FY2026; **sobrevivió mudándose al Departamento de Energía**, con acuerdo EPA/DOE de marzo de 2026 |
| **VMware** | **VIVO, MUERTA LA FORMA DE COMPRARLO** | Broadcom **terminó las licencias perpetuas en 2024** y pasó todo a suscripción por núcleo; **el hipervisor vSphere gratuito y los Essentials Kits se descontinuaron** |
| **Optimizely** | **VIVA, CON DUEÑO Y ALCANCE NUEVOS** | Episerver la compró en oct 2020 y **en ene 2021 rebautizó la empresa entera como Optimizely**; dejó de ser una herramienta de pruebas A/B para ser una suite |
| **Unbounce** | **VIVA, CON DUEÑO NUEVO** | controlada por Crest Rock Partners; **fusionada con Insightly en julio de 2024** |
| **Minitab** | **VIVO** | versión 22.4.0; entregas del Solution Center en feb, may y jul de 2026 |
| **Google Keyword Planner** | **VIVO** | dentro de Google Ads, sección Planificación; exige cuenta de Ads |
| **Google Trends** | **VIVO** | activo, con **API en alfa desde jul 2025** y panel Gemini en Explorar |
| **SEMrush** | **VIVA** | operando en 2026 |
| **SpyFu** | **VIVA** | operando en 2026 |
| **TrafficEstimate.com** | **VIVA** | sigue apareciendo en guías de herramientas de 2026 y su propio tráfico se mide |
| **EcoNation** | **VIVA, evidencia débil** | sitio propio activo con referencias de obra. **No consulté el registro mercantil belga**, y eso es lo que zanjaría la pregunta |
| **las plataformas generales** (Google, LinkedIn, Facebook, Amazon) | **VIVAS** | con una nota: **Facebook es Meta desde octubre de 2021** como empresa, aunque el producto conserve el nombre |

---

#### EL HALLAZGO: MUERTA y CAMBIADA son dos cosas distintas

**De las quince vivas, SEIS no están vivas como el catálogo las describe.** Y el
caso que lo enseña sin discusión posible es **Google Analytics**:

> **El nombre está perfectamente vivo. Todo lo que se escriba sobre la interfaz
> de Universal Analytics es papel mojado desde el 1 de julio de 2023, y desde
> julio de 2024 ni siquiera se pueden mirar los datos viejos.** Un nodo que diga
> *usa Google Analytics* sigue en pie; uno que describa dónde hacer clic dentro
> manda al lector a una pantalla que ya no existe.
>
> **Una herramienta institucional no muere: muta.** Y una instrucción escrita
> contra la forma vieja **caduca exactamente igual de mal** que una que nombra
> una empresa cerrada. **La diferencia es que la muerta se detecta abriendo el
> enlace y la mutada no**, porque el enlace abre perfectamente.

**Por eso el barrido no puede preguntar solo si la herramienta existe.** Tiene
que preguntar **si el paso que la usa sigue siendo ejecutable**, que es otra
pregunta y bastante más cara de contestar.

#### LA MORTALIDAD NO ES DEL CATÁLOGO: ES DEL TIPO DE HERRAMIENTA

**La cifra bajó mucho, y bajó por una razón que hay que decir en vez de
celebrarla.** La primera mitad del censo daba **seis muertas de doce, la mitad**.
Con el lote cerrado da **siete de treinta, el 23%**. **No es que el catálogo haya
mejorado: es que las doce primeras estaban sesgadas**, porque salieron de nodos
de marketing y de mercados de trabajo por encargo, que es justo donde se citan
productos comerciales de nicho por su nombre.

| | muertas | vivas | no verificables | total |
|---|---:|---:|---:|---:|
| **antes del lote** | 6 | 5 | 1 | **12** |
| **el lote** | **1** | **15** | **2** | **18** |
| **CENSO ENTERO** | **7** | **20** | **3** | **30** |

> **Las siete muertas son siete productos comerciales de nicho**: Alexa, Compete,
> Perfect Audience, The Deck, oDesk, Elance y el nombre Visual Website Optimizer.
> **Ninguna es un estándar, una institución ni un producto de una plataforma
> grande.**
>
> **Y al revés: de las siete institucionales o de plataforma grande** (GS1,
> EPCglobal, Energy Star, Google Analytics, Keyword Planner, Trends y las
> plataformas generales), **cero muertas y cuatro cambiadas de forma material.**
>
> **La regla de redacción que sale de aquí**: nombrar un producto comercial de
> nicho **es apostar**; nombrar un estándar o una institución **es seguro para el
> nombre y no lo es para el procedimiento**. **Las dos apuestas se pierden, solo
> que de maneras distintas.**

---

#### LAS SEIS CASAS DE LAS SIETE MUERTAS, verificadas contra el grafo

**Esto es lo que le sirve al barrido, y no la lista de nombres.** Las siete
muertas viven en **seis nodos**, cinco del núcleo y uno de franquicias:

| nodo | dominio | muertas que nombra | dónde |
|---|---|---|---|
| `analisis_trafico_competitivo` | core | **Alexa, Compete** | resumen y **paso 1**; Alexa además en el **paso 6** |
| `capturar_conocimiento_de_mercado` | core | **Alexa, Compete** | **solo en el resumen teórico** |
| `medicion_resultados_marketing_franquicia` | franquicias | **Alexa** | **paso 3**, junto a TrafficEstimate.com y Google Analytics |
| `retargeting_display` | core | **Perfect Audience, The Deck** | **pasos 1 y 4** |
| `seo_long_tail` | core | **oDesk, Elance** | **el mismo paso**, como par |
| `optimizacion_embudo_get_customers` | core | **Visual Website Optimizer** | un paso, junto a Optimizely y Unbounce, **que sí viven** |

> **DOS CORRECCIONES A LO QUE YO MISMO ESCRIBÍ HOY EN ESTA FICHA**, y las dos
> salen de contar bien en vez de suponer:
>
> 1. **Alexa vive en TRES nodos, no en dos.** Escribí *dos procedencias* esta
>    misma mañana. Falta `capturar_conocimiento_de_mercado`.
> 2. **Compete vive en DOS nodos, no en uno.** La entrada del lote 22 solo
>    registraba `analisis_trafico_competitivo`.
>
> **La causa de las dos es la misma**: busqué por subcadena. `Alexa` da diez
> aciertos en el grafo y **siete son *Osterwalder, Alexander***; `Elance` da tres
> y **dos son la palabra *freelance***. **Los nombres propios cortos hay que
> buscarlos con frontera de palabra**, y esa es la lección de instrumento.

#### EL CATÁLOGO YA CONTIENE SU PROPIO REMEDIO, y no lo sabe

**`capturar_conocimiento_de_mercado` y `analisis_trafico_competitivo` cuentan lo
mismo y lo escriben distinto**, y esa diferencia es exactamente el arreglo que
esta ficha viene proponiendo desde la entrada 1:

| | qué dice el paso |
|---|---|
| `analisis_trafico_competitivo`, paso 1 | *Buscar y comparar tráfico de competidores con herramientas como **Alexa o Compete*** |
| `capturar_conocimiento_de_mercado`, paso 3 | *Usar **herramientas de medición de tráfico web** y rankings de app stores* |

> **El segundo describe la capacidad y el primero nombra dos productos muertos.
> El segundo no caduca; el primero caducó en 2022.** No hay que inventar la
> redacción arreglada: **está escrita, en un nodo hermano, dentro del mismo
> dominio y con la misma fuente.**
>
> **Y hay una anomalía que conviene mirar**: el catálogo nombra **oDesk y
> Elance**, las dos marcas muertas, y **no nombra Upwork ni una sola vez**, que
> es la viva en la que las dos se fundieron. **Verificado: cero apariciones.**

#### DOS COSAS QUE NO CIERRO, y las dejo abiertas a propósito

1. **`Quantcast`: no revierto el veredicto anterior, pero queda marcado.** La
   entrada del lote 22 lo dio por vivo, y **la empresa lo está**. Pero el
   producto que el paso 6 pide, **Quantcast Measure**, aparece **como
   descontinuado en directorios de software y como activo en las páginas propias
   de Quantcast**. **Fuentes en conflicto: se queda como estaba, con la marca
   puesta.** Es, si se confirma, otro caso de *vivo el nombre y muerta la
   versión*.
2. **Un par de nodos casi gemelos apareció de rebote**, `captura_conocimiento_mercado`
   (7 pasos) y `capturar_conocimiento_de_mercado` (5 pasos), **mismo dominio y
   misma fuente**. **No lo juzgo aquí**: la cola del cribado intra ya lo tiene
   fichado en el **puesto 941** con semejanza 0,8051, y ahí se lee cuando le
   toque, en orden.

**Ningún nodo se toca desde esta ficha.** Lo que cambia es que el barrido ya
tiene sus seis casas, su orden de prioridad y su segunda pregunta.

### Entrada 3 (lote 22, puesto 340): el nodo que más herramientas nombra

`nucleo/analisis_trafico_competitivo` (*The Startup Owner's Manual* | *Traction*)
nombra **seis herramientas en ocho pasos**, y **no todas están muertas**. La lista
exacta, verificada contra el grafo:

| herramienta | dónde | estado |
|---|---|---|
| **Alexa** | pasos 1 y 6 | **RETIRADA** por Amazon en 2022 |
| **Compete** | paso 1 | **RETIRADA**, y antes que Alexa |
| Quantcast | paso 6 | sigue operando |
| MixRank | paso 5 | sigue operando |
| Adbeat | paso 5 | sigue operando |
| Quora | paso 3 | sigue operando |

> **PRECISIÓN, porque cambia el tamaño del arreglo**: el encargo agrupó *Alexa,
> Quantcast y MixRank*, y **de esas tres solo Alexa está muerta**. Las muertas son
> **Alexa y Compete**; las otras cuatro siguen vivas. **La reparación es
> quirúrgica, no una reescritura del nodo.**

**La ficha va por tres nodos y ocho menciones:**

| nodo | herramientas nombradas |
|---|---|
| `nucleo/seo_link_building` (P69) | Open Site Explorer |
| `nucleo/seo_estrategia_fat_head` (P145) | Open Site Explorer |
| `nucleo/analisis_trafico_competitivo` (P340) | Alexa, Compete, Quantcast, MixRank, Adbeat, Quora |

> **Los tres son del núcleo, y los tres aparecieron de rebote leyendo el
> gradiente.** Ninguno se buscó.

**Y el barrido gana un criterio que antes no tenía**: no basta con listar los
nombres propios, **hay que comprobar cuáles siguen vivos**. En este nodo, **cuatro
de seis lo están**. Un barrido que asuma que todo nombre propio caducó **rompería
consejos que funcionan**.

**Ningún nodo se toca: la reparación es de la pasada única.**

### Entrada 2 de herramientas (lote 13, puesto 145): Open Site Explorer, SEGUNDA vez

`nucleo/seo_estrategia_fat_head` **cita la misma herramienta muerta** que
`nucleo/seo_link_building` (entrada 1, puesto 69).

**Verificado contra el grafo: son exactamente dos nodos activos los que la
nombran, y los dos son del núcleo.**

> **Ya no es un caso suelto: es un patrón.** Una herramienta retirada por Moz
> sobrevive en **dos** sitios del catálogo, y **apareció las dos veces de rebote**,
> leyendo otra cosa.

**Confirma el primer acto de esta ficha, que ya estaba escrito**: cuando despierte,
**lo primero es el barrido**, no la entrada suelta. Dos apariciones accidentales en
un mismo barrido de gradiente son la mejor evidencia de que **nadie ha mirado el
resto**.

### Entrada 2 de marco-país (lote 9, puesto 85): el mundo quedó atrás del núcleo

Va aquí, junto al puesto 53, aunque su ficha natural sea la de marco: es la misma
clase de **ejemplar de un país** cableado.

`franquicias/obtencion_marca_registrada` está atado a un solo país en todo: la
base **TESS**, un abogado de **Thomson CompuMark**, la solicitud ante la
**USPTO**, y el propio título dice *"Marca Registrada **Federal**"*.

**Lo que lo hace distinto del puesto 53 es con qué contrasta.** Su par del núcleo,
`nucleo/marcas_registradas`, **ya está curado**: dice *"en Estados Unidos esto se
hace ante el USPTO; **averigua cuál es la oficina equivalente en tu país**"* y
*"presenta la solicitud ante la **oficina correspondiente en tu país**"*.

> **La campaña que curó al núcleo no pasó por los mundos.** No es que el nodo de
> pago sea más superficial: es que **el gratuito ya viajó y el de pago no**.

**Consecuencia para cuando esto despierte**: el barrido **no puede ser solo del
núcleo**. Lo que se curó una vez en `core` **hay que buscarlo otra vez en los
nueve mundos**, o la asimetría se repite en cada campaña de voz.

**El nodo no se toca desde el gradiente.**

### Entrada 3 de marco-país (lote 16, puesto 214): tercer miembro, y ya son dos mundos

`exportacion/screening_mercados_potenciales` cita el **U.S. Census Bureau** (paso
1) y el **U.S. Commercial Service** (paso 5) para elegir a qué mercados exportar.

**Con este van tres miembros medidos, de dos mundos distintos:**

| miembro | mundo | qué cablea |
|---|---|---|
| `proteccion_propiedad_intelectual_internacional` (P53) | exportacion | uspto.gov, stopfakes.gov |
| `obtencion_marca_registrada` (P85) | franquicias | TESS, Thomson CompuMark, USPTO, y *Federal* en el título |
| `screening_mercados_potenciales` (P214) | exportacion | Census Bureau, Commercial Service |

> **El barrido de los nueve mundos queda confirmado POR ACUMULACIÓN, no por
> doctrina.** No hizo falta argumentar que hacía falta: **tres hallazgos
> accidentales, en dos mundos distintos, lo demuestran solos.**

### Entrada 4, y es la forma MENOR: el nombre se quedó, el contenido ya viajó

`nucleo/regla_disponibilidad_previa_venta` (lote 18, puesto 250) conserva en su
**título** el nombre de la regla estadounidense (*Pre-Sale Availability Rule*, de
la *Businessperson's Guide to Federal Warranty Law*), **pero sus tres pasos ya
están universalizados**: revisa por qué canal vendes, coloca el texto de la
garantía visible junto al producto o en su página, prepara a quien te ayuda a
vender.

> **Es la forma menor de la clase, y el contrario exacto del puesto 85**: allí el
> mundo seguía cableado entero mientras el núcleo ya estaba curado; **aquí el
> contenido ya viajó y solo se quedó el nombre.**

**Consecuencia para el barrido**: hay que mirar **títulos además de pasos**. Un
barrido que solo lea `pasos_accionables` **no vería este caso.**

### CORRECCIÓN de la entrada 4, y el MODELO que la ficha buscaba (lote 21)

**La entrada 4 se registró como "forma menor" sin comprobar sus
`condiciones_activacion`. Comprobadas, el nodo NO es un miembro de esta ficha:**

`regla_disponibilidad_previa_venta` declara *"**Si vendes, o piensas vender,
productos a clientes en Estados Unidos**"*. **Está condicionado.** Su único residuo
es el nombre inglés de la regla en el título, que es **cosmético, no de válvula**.

**Y su hermano de libro lo confirma.** El puesto 306 llevó a
`nucleo/cumplimiento_magnuson_moss`, y está marcado **tres veces**:

| dónde | qué dice |
|---|---|
| `condiciones_activacion` | *"Si vendes, o piensas vender, productos a clientes en **Estados Unidos**"* |
| `resumen_teorico` | *"Esta es una ley federal **de Estados Unidos**... vendidos a clientes **en ese país**"* |
| `entregable_esperado` | *"...**si vendes a clientes en Estados Unidos**"* |

> **Los dos nodos de la ley de garantías, del mismo libro, están correctamente
> condicionados. NO son deuda: son EL MODELO.**

**Los miembros reales de esta ficha son TRES**, y lo que los separa del modelo es
exactamente lo que hay que arreglar:

| miembro | su condición | qué le falta |
|---|---|---|
| `proteccion_propiedad_intelectual_internacional` (P53) | *"si planea licenciar tecnología o formar joint ventures en el extranjero"* | **no nombra país alguno**, y cablea `uspto.gov` y `stopfakes.gov` |
| `obtencion_marca_registrada` (P85) | *"cuando se planea franquiciar y aún no se posee un trademark **federal**"* | **dice "federal" sin decir de qué país** |
| `screening_mercados_potenciales` (P214) | *"cuando se inicia la fase de selección de mercados"* | **genérica**, y cablea Census Bureau y Commercial Service |

> **EL REMEDIO YA EXISTE EN EL CATÁLOGO, aplicado dos veces y del mismo libro.** No
> hay que inventar cómo se arregla esta clase: hay que **copiar la condición
> honesta** que los nodos de garantías ya llevan.
>
> **Y eso cambia el costo de la ficha**: no es reescribir contenido, es **añadir la
> condición que dice a quién aplica.**

**El nodo no se toca desde el gradiente.**

Los tres nodos-frontera condicionales (EAR, antiboicot, cláusula antidesviación)
viven aquí también: su condición honesta —*"si tu producto lleva componentes de
EE.UU. o tu ruta lo toca"*— depende de acuerdos que cambian.

## DOCTRINA DE LA CLASE (ago 2026)

**"Los programas de tu estado no significan nada donde no hay estados con
programa."** Cuando un nodo describe algo subnacional de un país concreto, no
hay clase universal a la que reencuadrarlo: prometer un equivalente que en
varios países no existe es doblemente deshonesto. Deprecar de selección es la
única salida honesta.

**Y la ley de la lectura pagó su primer dividendo**: leer los 28 encontró 30. El
grep había perdido dos.

## DOCTRINA DE CAMPAÑA (re-voz de quality, cerrada ago 2026)

**Fusión primero, a toda escala.** La secuencia se pagó sola tres veces: 24
nodos del lote original se deprecaron antes de tocarlos, y otros 15 en la
ronda 2. Cada nodo fundido antes de re-vozar es API que no se gasta en texto
que va a desaparecer. Cuando el guardián delató la familia COQ a mitad de
campaña, la respuesta correcta no fue seguir: fue una skip-list y una ronda 2.

**Un ámbar por vecindario es síntoma de sub-fusión.** El rumbo guardián del
COPQ cayó sin que su nodo se tocara: lo desplazaron sus gemelos sin fundir, que
la re-voz volvió más coloquiales. Re-vozar un pack **mueve el vecindario
entero**. Un ámbar cuyo nodo esperado no cambió y aun así perdió el puesto es la
firma de que quedan duplicados. Al fundirlos, recuperó el top-10 exactamente
como se declaró de antemano.

**Las barandas del taller no son las de la fábrica.** La vara de la extracción
mide texto que nace; la del taller mide texto que se traduce. Aplicar la primera
a la segunda produjo el peor tipo de error: rechazar lo correcto (39 nodos
buenos de 40) y empujar a rellenar. Cada taller declara sus propias barandas.

**Dos conceptos murieron por la regla de cero invención, no por su calidad.**
`Equipo de Mejora de Calidad` e `Involucramiento del Sindicato` se deprecaron de
la selección porque el concepto ANCLADO es la estructura: la versión sin ella es
un nodo que la fuente no escribió. Quedan anotados para el futuro mundo **Primer
Equipo**, cuya minería propia podrá renacerlos desde sus fuentes.

## DOCTRINA del taller de re-voz (ago 2026)

**La vara de largo de la extracción, aplicada a lo existente, es presión de
invención.** Exigí 80-150 palabras a nodos que ya vivían con 55-75. Pedirle a
una reescritura de VOZ que alargue un texto es pedirle que invente, justo donde
está prohibido inventar. El largo se mide contra el original.

**Una baranda que caza lo correcto no es estricta: está rota.** Dos veces en esta
campaña. Metí *cuando*, *quién*, *cuánto* y *más* en la lista de tildes
obligatorias, cuando solo la llevan si son interrogativas o de cantidad: rechazó
39 nodos buenos de 40. Y puse `sab[ée]s` como voseo, cazando *sabes*, que es el
tú correcto: rechazó tres más.

**Una función que existe, se llama, no revienta y no hace nada** es la peor de
las averías. La corrección mecánica de tildes tenía un carácter de retroceso en
vez de un límite de palabra, porque el heredoc del shell come un nivel de
escapado. `re.sub` sin coincidencias devuelve el texto igual, en silencio.

**El plural no lleva la tilde del singular.** *Acción* pero *acciones*. Un
detector que no lo sabe reporta 525 fallos donde hay 284.

## DOCTRINA: la ortografía NO mueve la recuperación semántica

**Experimento controlado** (ago 2026), a raíz del único ámbar de la prueba de
rumbos. `proteger_fragiles_caja_dentro_de_caja` era el único nodo de compras y
entrega escrito **entero sin tildes**, y quedaba 14.º dentro de su propio mundo
para la consulta que debía ganar.

Se corrigieron **18 tildes** en título, resumen, pasos y condiciones. Nada de
contenido, el anclaje a fuente intacto. Se re-embebió solo ese nodo, con el mismo
`input_type` del corpus, y se volvió a correr la prueba completa.

| | puesto | score |
|---|---:|---:|
| antes | 14.º | 0,5140 |
| después | **15.º** | 0,5062 |

**Resultado negativo, y es doctrina igual.** En este espacio (voyage-4-lite,
multilingüe), la ortografía **no** mueve la recuperación: la diferencia cabe en el
ruido. La causa del puesto 14 es **semántica**, no ortográfica — los nodos que le
ganan hablan de empacar cosas concretas (flores, líquidos, relleno) y la consulta
pregunta *cómo empacar*, no *qué método de doble caja usar*.

**Lo que esto significa para `re-voz-de-quality`:** la ortografía impecable sigue
siendo obligatoria, pero **por la voz, no por la puntería**. El lector ve el
texto; la brújula, aparentemente, no lo nota. No se puede justificar una
regeneración con el argumento de que mejora la recuperación.

La corrección se conserva (el español correcto es correcto igual), y el rumbo
sigue en el banco vigilando ese nodo.

**Hallazgo al margen, sin acción**: ese nodo dice *"probarla **vos** mismo"* —
voseo, que desentona con el tú de la casa. No se tocó para no contaminar el
experimento. Va al lote de `re-voz`.

## Ficha post-beta: `densidad-de-quality`

**Marcada post-beta-con-telemetría**: informa, no receta, igual que el núcleo.

**El diagnóstico** (cirugía de Calidad, ago 2026). `ramaDe()` desde **cualquiera**
de las 7 semillas de quality alcanza el tope de 500 nodos. El pack está tan
conectado que "descartar la rama" descarta casi todo lo alcanzable:

| semilla rechazada | semillas que quedan fuera de su rama |
|---|---:|
| accion_correctiva · programa_mejora_calidad_14_pasos · costo_de_calidad · medicion_calidad | **0** |
| control_estadistico_de_procesos · trilogia_de_juran | 1 |
| mejora_continua_del_proceso | 3 |

**El efecto real**: cuando el usuario rechaza una puerta del mundo, la reelección
debería ofrecerle otra semilla fuera de esa rama. En 4 de las 7 no queda ninguna,
así que cae al vecino. La regla existe en el código y no se puede ejercer.

**La fusión no lo causó.** Medido contra el grafo anterior: la rama de
`medicion_calidad` ya se tragaba 6 de las 7 semillas; el test pasaba por **una**
de margen y la fusión se comió la séptima. Lo que hizo fue destaparlo.

**El test de guardia** ya está puesto (`reeleccionPuerta.test.ts`, describe "la
densidad del pack, fijada como está hoy"): fija el estado actual, así que el día
que alguien mejore la densidad el test lo canta en vez de dejarlo pasar.

**Por qué post-beta**: arreglarlo es podar aristas, y qué aristas sobran lo dice
el recorrido real de la gente, no el grafo mirándose a sí mismo.

## El NÚCLEO gana su TERCER argumento de espera (ago 2026)

Aprendido en quality, y es el más fuerte de los tres:

> **La fusión mueve el vecindario entero. Operar el corazón antes de la beta
> contaminaría la línea base que debe juzgarlo.**

Lo vimos con datos: al re-vozar y fundir quality, un nodo que nadie tocó perdió
su puesto porque sus vecinos cambiaron, y la densidad del pack pasó de dejar 3
puertas alternativas a no dejar ninguna. Si eso se hace en el núcleo **antes** de
que la beta corra, la telemetría que debía decidir qué se poda ya vendría medida
sobre un grafo movido por la propia poda.

Los tres argumentos, juntos: (1) el núcleo es el único validado por meses de uso
real; (2) cinco definiciones de *startup* pueden ser cinco nodos que sobran o
cinco puertas por las que entraron cinco personas distintas, y el censo no
distingue; (3) esta.

## Hecho recientemente (para no reabrirlo por error)

- **Calendario**: modo con-fechas + recordatorios + `.ics` universal (webcal) EN PRODUCCIÓN.
  El **Google Calendar Nivel 1 se RETIRÓ** a favor del webcal universal (no reabrir).
- **Catálogo congruente** (precios 10/5, Tus Números incluido, beta sin cortesía): EN PRODUCCIÓN.
- **Espacios** Fase 1+2 + las 3 caras (Plan · Manos a la obra · Tu avance): EN PRODUCCIÓN.
- **`ancla-de-puente-mal-rotulada`**: CERRADA (ago 2026). **La ley: un puente ancla en el
  NÚCLEO, siempre.** El acoplamiento mundo↔mundo queda prohibido como accidente; el día que
  valga será clase declarada con su regla de desbloqueo, jamás un anclaje del proponedor
  buscando sobre el master entero. Los 22 mal anclados se re-anclaron (0 podados: todos
  superaban el piso calibrado), el proponedor ya solo mira candidatos de dominio `core`, y la
  aserción pasó de "packs pendientes" a **todos los puentes en cada corrida**.
