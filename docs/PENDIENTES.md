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

### Hipótesis del auditor para ese día — CORREGIDA con el código en la mano

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

Las filas rescatadas del ciclo viejo van marcadas **`parcial`** y el resumen lo
dice en voz alta: un total con filas dudosas se declara dudoso en vez de sonar
exacto. **El próximo ciclo cierra con total certificable.**

## Ficha permanente: `vigencia-del-marco-internacional`

Nace con el ciclo del censo (ago 2026). Los nodos de exportación que citan
**marcos versionados o tratados vigentes** —Incoterms, cartas de crédito,
códigos arancelarios, cláusula antidesviación, EAR— ganan nota de vigencia y
entran a revisión cuando el comercio cambie de rumbo.

**Las instituciones-de-libro jamás se omiten: se mantienen al día.** Incoterms
2020 no es un dato local ni un detalle de estilo: es el vocabulario acordado
entre países, y un catálogo que lo cite desactualizado miente con precisión.

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
