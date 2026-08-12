# Pendientes — My Idea

Lista viva de lo que queda por hacer. Se actualiza al cerrar o abrir frentes.
(Última actualización: agosto 2026.)

## 0b. La cirugía de costuras se ordena por PARES LIBERADOS (12 ago 2026)

**El dato que cambia la prioridad**, contado del archivo del cribado intra: hay
**nueve pares congelados por seis nodos costurados**. Un par congelado es una
lectura que no se puede emitir hasta que el nodo se opere, porque el veredicto
caería sobre un texto que va a cambiar (banco 9.4 y 9.9).

**Orden propuesto, de más a menos pares liberados:**

| nodo a operar | pares que libera | puestos |
|---|---:|---|
| **`voz_del_cliente_voc`** | **3** | 724, 755, 827 |
| **`producto_minimo_viable`** | **2** | 592, 830 |
| `lienzo_modelo_negocio` | 1 | 784 |
| `ab_testing_optimizacion` + `split_testing_experimentos_ab` | 1 | 738 |
| `preguntas_ipo_dolor_cliente` | 1 | 798 |
| `key_partners_hypothesis` + `asociaciones_clave` | 1 | 599 |
| **`estrategia_crecimiento_clientes`** | **1** | 831 |
| **`producto_unico_superior`** (va a cura acoplada) | **1** | 835 |

> **`voz_del_cliente_voc` vale por tres y `producto_minimo_viable` por dos**: los
> dos primeros movimientos de la cirugía liberan cinco de los nueve.
>
> **Y el criterio se puede seguir aplicando**: cada nodo costurado que entre a un
> par nuevo sube en la lista. La cuenta se rehace del jsonl, no de memoria.

**Actualización del 12 ago 2026: la cuenta subió a ONCE pares por OCHO nodos**, y
va a seguir subiendo mientras la cirugía no arranque, porque los nodos costurados
son grandes y por eso entran a muchos pares.

**LAS DOS CUENTAS, separadas y nombradas** (regla aprobada el 13 ago 2026, banco
§9.9). La cola es siempre más ancha: **todo congelado está también en cola**.

| cuenta | qué significa | hoy | lista |
|---|---|---:|---|
| **CONGELADOS** | el **veredicto depende** de qué quede tras la cirugía | **13** | 592, 599, 724, 738, 755, 784, 798, 827, 830, 831, 835, 851, **494** |
| **EN COLA** | el texto va a cambiar, se relee igual | **19** | los trece de arriba **más 361, 374, 386, 392, 492 y 915** |

**Actualización del 13 ago 2026**: el **915** entra en cola sin congelar, y es el primero donde el test de POSICIÓN y el de DEPENDENCIA se contradicen (ver informe §37.1). Cola a **16**.

**Los TRES que están en cola sin congelar**, y por qué: en el **361** el nodo chico
**es** el bloque 1 a 5 del grande; en el **374** el solape cae entero en el bloque
1 a 5 y el destejido se lleva el 6 a 9; en el **386** el solape cae entero en el
bloque de Cooper, que es el que sobrevive. **En los tres, lo que sobrevive es justo
donde el solape vive**, así que el veredicto es invariante.

**Actualización del 13 ago 2026**: la cola pasa a **14** (los once congelados más
361, 374 y 386). Y el **386** confirma quién va primero en la cirugía:
`voz_del_cliente_voc` es **el nodo que más pares congela** (tres: 724, 755, 827),
y además resultó **costura confirmada con gemelo declarado**, o sea **cura
acoplada**: destejer y fundir son el mismo acto, porque el gemelo cubre justo la
mitad que la cirugía deja en pie.

**Actualización del 13 ago 2026 (R19): la cola es MÁS ANCHA que la cuenta de
congelados, y el 361 es el primero que las separa.** `key_partners_hypothesis`
resultó ser **costura confirmada con gemelo declarado**, o sea **cura acoplada**
(séptimo ejemplar de la ficha). Su par **entra a la cola porque el texto va a
cambiar**, pero **no queda congelado**: el nodo chico **es** el bloque 1 a 5 del
grande, así que cualquier destejido plausible lo deja contenido igual y el
veredicto no depende de la cirugía.

> **La regla que esto propone, pendiente del visto del auditor**: un par entra a
> la **cola** cuando su texto va a cambiar; queda **congelado** solo cuando **el
> veredicto depende de qué sobreviva**. Hoy la cuenta va **once congelados, doce
> en cola**. Se releen **después** de operar sus nodos, y
sus razones ya llevan escrito qué hay que salvar en cada caso.

> **Dos avisos para quien la ejecute.** El **827** tiene los **dos** nodos
> costurados, así que necesita las dos cirugías antes. Y el **341**, aunque no
> está congelado, **manda que los dos mapas del racimo de experiencia se reúnan en
> uno**: destejer por separado ahí no arregla, aplaza (ficha, CURA CONJUNTA).

---

## 0. Despliegues de staging APAGADOS en Vercel (12 ago 2026)

**Qué se hizo:** `web/vercel.json` lleva ahora
`"git": { "deploymentEnabled": { "staging": false } }`. Vercel deja de construir un
preview por cada push a `staging`. **Motivo:** el frente del cribado empuja muchas
veces al día y cada push disparaba un despliegue que nadie mira.

**Por qué en `web/` y no en la raíz, que es lo que pedía el encargo:** el proyecto de
Vercel está enlazado desde `web/` (existe `web/.vercel/project.json`, y la app Next
vive ahí; no hay `package.json` en la raíz). **Vercel lee el `vercel.json` del Root
Directory del proyecto**, así que un archivo en la raíz no se leería y el apagado no
tendría efecto. Se deja **un solo archivo**, el que Vercel lee, por la regla de fuente
única.

**Cómo se revierte, en una línea:** borrar la clave `git` de `web/vercel.json` (o
poner `"staging": true`) y commitear. También se puede reactivar desde el panel de
Vercel sin tocar el repo, pero entonces el archivo y el panel dirían cosas distintas:
**mejor revertir aquí.**

**Ojo:** `main` no se toca. Los despliegues de producción siguen igual.

---

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


## Ficha permanente: `campos-sucios-dataset`

**DESPIERTA el 11 ago 2026.** Estaba dormida desde el gradiente, donde solo tenía
notas cosméticas sueltas (un id en inglés, un gemelo cirílico). **La despierta el
defecto de los tokens de fuente que salió de la tanda 17 de costuras, y al medirlo
entero resultó ser mucho más grande de lo que la nota anunciaba.**

**Todas las cifras de esta ficha están recontadas del grafo el 11 ago 2026**, sobre
`dataset/metadata/master_graph.json`: **3.835 nodos en disco, 314 deprecados, 3.521
activos.**

---

### 1. EL HALLAZGO: el campo `fuente` no guarda el título de la obra, guarda el NOMBRE DEL ARCHIVO

**Esto no se sabía, y explica de golpe tres defectos que parecían distintos.**

**La firma es inconfundible y son tres marcas juntas:**

| marca | qué se ve | ejemplo real del grafo |
|---|---|---|
| **truncado a 31 caracteres exactos** | el título se corta a mitad de palabra | `Juran's Quality Handbook_ The C` |
| **guion bajo donde iba `:` o `.`** | el saneado de nombre de archivo | `Co-Intelligence_ Living and Wor`, `Reason, J. T_` |
| **código de documento desnudo** | ni siquiera hay título | `OSHA3885`, `SMALL_BUSINESS` |

> **Las tres son la misma avería: alguien guardó el nombre del fichero PDF en vez
> del título de la obra.** `OSHA3885` y `OSHA3886` **son números de publicación
> reales de OSHA**, o sea nombres de archivo; `SMALL_BUSINESS` es otro. Y el corte
> a **31 caracteres exactos** no lo produce una persona: **lo produce un programa.**

#### La medición, con vivos y deprecados separados

| defecto | nodos en disco | de esos, deprecados | **VIVOS** |
|---|---:|---:|---:|
| **título truncado a 31 caracteres** | **1.212** | 93 | **1.119** |
| **código de documento desnudo** | **102** | 32 | **70** |
| **UNIÓN (no se solapan)** | **1.314** | 125 | **1.189** |

**1.314 de 3.835 nodos, el 34,3% del catálogo, declaran una fuente que no es el
título de la obra.**

**Las diez grafías truncadas, con su peso:**

| grafía tal cual está en el campo | nodos |
|---|---:|
| `Juran's Quality Handbook_ The C - Joseph A. Defeo` | **570** |
| `The Green to Gold Business Play - Daniel C. Esty` | **242** |
| `Managing the Risks of Organizat - Reason, J. T_` | 112 |
| `The Field Guide to Understandin - Dekker, Sidney;` | 91 |
| `The Hard Thing About Hard Thing - Ben Horowitz` | 60 |
| `Co-Intelligence_ Living and Wor - Ethan Mollick` | 51 |
| `Change by Design, Revised and U - Tim Brown` | 43 |
| `The Field Guide to Understandin - Dekker, Sidney` | 27 |
| `Essentials of Supply Chain Mana - Michael H. Hugos` | 17 |
| `Guia de empaque para transporte` | 1 |

**Los tres códigos desnudos, todos de `health_safety`:**

| token | en disco | deprecados | **vivos** |
|---|---:|---:|---:|
| `SMALL_BUSINESS` | 51 | 4 | **47** |
| `OSHA3886` | 27 | **20** | **7** |
| `OSHA3885` | 24 | 8 | **16** |
| | **102** | **32** | **70** |

> **CORRECCIÓN DE MI PROPIA CIFRA, y va aquí porque la escribí hace un día.** En
> la tanda 17 escribí que los 102 eran *de los 283 nodos de `health_safety`, más
> de un tercio del dominio*. **Está mal por partida doble**: mezclé el conteo en
> disco (102) con el de activos (283). Los números reales son
> **102 de 332 en disco, el 30,7%**, y **70 de 283 activos, el 24,7%**. **No es
> más de un tercio ni por una base ni por la otra.**
>
> El error es el mismo de siempre: **dividir dos cifras que no se cuentan sobre la
> misma población.**

### 2. LA MISMA OBRA ESCRITA DE VARIAS MANERAS: once libros, 1.178 nodos

**Consecuencia directa de lo anterior**, porque unas extracciones truncaron y otras
no. **Once obras** aparecen con dos o tres grafías **que no añaden ninguna
información**:

| obra | grafías | nodos | en qué se diferencian |
|---|---:|---:|---|
| *The Startup Owner's Manual* | **3** | **234** | *Steve Blank* / *Blank, Steve* / sin autor |
| *Venture Deals* | 2 | 142 | con y sin *Brad Feld* |
| *Essentials of Supply Chain Management* | 2 | 135 | una **truncada** |
| *The Founder's Dilemmas* | 2 | 130 | con y sin *Wasserman, Noam* |
| *The Field Guide to Understanding...* | 2 | 118 | **solo un punto y coma final** |
| *The Hard Thing About Hard Things* | **3** | 106 | una **truncada**, otra sin autor |
| *Financial Intelligence for Entrepreneurs* | 2 | 86 | con y sin autores |
| *A Project Manager's Book of Forms* | 2 | 67 | con y sin autora |
| *Change by Design* | 2 | 56 | con y sin *Tim Brown* |
| *Business Model Generation* | **3** | 55 | *(Osterwalder)* / *- Osterwalder* / *- Osterwalder, Alexander* |
| *The Art of Thought* | 2 | 49 | *Wallas, Graham* / *Graham Wallas* |
| | | **1.178** | |

> **Lo que esto rompe, y no es teórico**: cualquier conteo por libro hecho con
> igualdad de cadena **cuenta once obras como veintiséis**. El caso de Dekker es el
> más ridículo de todos: **118 nodos partidos en dos grupos por un punto y coma.**

#### DOS COSAS QUE NO SON ESTE DEFECTO, y las separo para que nadie las arregle por error

1. **La citación por capítulo SÍ añade información y no se toca.** *Edwards et al.*
   (30 grafías), *DeMarco y Lister* (13), *Hubbard* (10), *Lindstrom* (7),
   *Rushton* (3), *Muller* (3) y la *Guía FedEx* (2) citan capítulo o sección.
   **Eso es buena práctica, no suciedad**, aunque tenga el mismo efecto de romper
   los conteos por cadena.
2. **`OSHA3885` y `OSHA3886` NO son dos grafías de un documento: son dos
   documentos distintos.** Mi primera agrupación automática los juntó porque
   normalizaba por prefijo. **Es un artefacto de mi propio análisis y lo declaro
   antes de que se convierta en un arreglo equivocado.**

### 3. LO QUE YA ESTABA ANOTADO Y SIGUE EN PIE, verificado hoy

**La sección B.2 de `docs/AUDITORIA_MOTOR.md` sigue siendo exacta**, recontada:

| clave anómala | nodos | qué es |
|---|---:|---|
| `fuentes_adicionales` | **4** | `arquetipos_de_cliente`, `composicion_board_directors`, `definicion_startup`, `preferencia_de_liquidacion` |
| `fase_проekto` | **1** | `crosby_habilidad_transmision`, **gemelo cirílico** |
| `fase_project` | **1** | `mapa_flujo_trabajo_cliente`, gemelo en inglés |

> **PRECISIÓN sobre las otras dos claves que un barrido ingenuo marcaría**:
> `ids_alias` (**309** nodos) y `merged_originals` (**269**) **no son suciedad**:
> están declaradas y son del consolidador. Su problema es otro, y está en la
> sección B.3 de la auditoría: **nadie las lee.** No se tocan desde aquí.

**Y la nota cosmética que abrió esta ficha sigue viva**: hay ids del núcleo escritos
en inglés (`quality_audit` frente a `quality/auditoria_calidad`). **No lleva cifra
porque no la he medido**, y medirla exige decidir antes qué cuenta como id inglés.

---

### 4. EL REMEDIO CANDIDATO: una tabla de mapeo, un commit

> **UNA TABLA DE MAPEO de grafía a título canónico, aplicada en la pasada única, en
> UN commit.** El campo `fuente` tiene **129 grafías distintas** en todo el
> catálogo: **la tabla cabe en una pantalla** y la sustitución es mecánica.

**Cómo se construye, en orden y sin ambigüedad:**

1. **Los 102 códigos desnudos** se resuelven a mano: son tres, y **`OSHA3885` y
   `OSHA3886` son publicaciones identificables por su número**.
2. **Las diez truncadas** se completan al título real. **No se pueden reconstruir
   por programa**, porque los últimos caracteres se perdieron: hay que mirar el
   original.
3. **Las once obras con varias grafías** se colapsan a una sola forma, y **la forma
   canónica se decide una vez**: título más autor, con un solo criterio de orden
   del nombre.
4. **Las citas por capítulo se conservan tal cual**, y lo que se canoniza es solo su
   prefijo de obra.

**Y el remedio que impide la reincidencia, que es lo que la auditoría ya pedía
para las claves**: **una lista blanca de fuentes en el Gate 0**. Si un nodo nuevo
declara una `fuente` que no está en la tabla, **el gate lo para**. Sin eso, la
próxima extracción vuelve a meter nombres de archivo.

> **Prioridad, dicha con honestidad**: esto **no rompe nada hoy**. El lector no ve
> el campo `fuente` y el motor no lo usa para decidir. **Lo que rompe es todo
> trabajo de análisis que agrupe por obra**, y esta campaña ya tropezó con ello
> dos veces: en el racimo de la apertura de Customer Validation y en la tanda 17
> de costuras. **Es barato, es de higiene, y cada análisis que se haga antes de
> arreglarlo hay que hacerlo con la tabla en la mano.**

---


---

### Entrada del cribado de costuras (11 ago 2026): NAFTA, y la ficha mide por fin lo que dice su nombre

**Sale de la tanda 21 de costuras, del nodo `exportacion/certificado_de_origen_coo`.
Su paso 3 dice, literal y verificado contra el grafo:**

> *Determinar si aplica un tratado de libre comercio (**FTA/NAFTA/CAFTA-DR**) que
> reduzca aranceles*

**NAFTA se extinguió el 1 de julio de 2020**, sustituido por el **USMCA** (T-MEC en
México, CUSMA en Canadá). El nodo manda comprobar si aplica un tratado que **lleva
cinco años sin existir**.

#### CHOCA CON EL ENCARGO Y LO TRAIGO: esta no es la segunda medición, es la PRIMERA

**El encargo dice que la primera medición de esta ficha es el caso COC de las
fusiones. Verificado, no lo es.** El caso COC vive en
`docs/FICHA_SUBFUSION_GRADIENTE.md` sección 5 y **trata de otra cosa por completo**:
es el duo `evaluacion_gestion_riesgos` contra `plan_de_gestion_de_riesgos`, y su
hallazgo es que **al fusionarlos el superviviente no puede conservar el id**,
porque choca con `nucleo/plan_gestion_riesgos`. **Es un problema de nombres y
alias en una fusión, no de vigencia de un marco.**

**Y al ir a comprobarlo salió algo mejor que la corrección.** Esta ficha tiene dos
entradas previas y **ninguna de las dos mide vigencia**:

| entrada previa | qué mide de verdad |
|---|---|
| gradiente lote 7, `proteccion_propiedad_intelectual_internacional` | **alcance geográfico**: cablea `uspto.gov` y `stopfakes.gov`, agencias de un país |
| franja, `seguridad_digital` | **alcance geográfico**: artefactos de cumplimiento de un país |

> **La ficha se llama `vigencia-del-marco-internacional` y sus dos entradas son de
> ALCANCE, no de VIGENCIA.** Su texto fundacional dice *Incoterms 2020 no es un
> dato local: un catálogo que lo cite desactualizado miente con precisión*, o sea
> que **nació apuntando al eje temporal y se llenó del eje geográfico.**
>
> **NAFTA es la PRIMERA entrada que mide lo que el nombre promete: un marco que
> caducó.**

#### LA MEDICIÓN, y no es un nodo: son ocho

**Recontado del grafo el 11 ago 2026:**

| término | nodos vivos que lo nombran |
|---|---:|
| **NAFTA** | **8** |
| USMCA | **0** |
| T-MEC | **0** |
| CUSMA | **0** |
| TLCAN | **0** |

> **El catálogo nombra ocho veces un tratado extinto y CERO veces su sustituto.**

**Y dos de los ocho lo llevan en sitios que no son un paso cualquiera:**

| nodo | dónde está NAFTA |
|---|---|
| **`nafta_free_trade_agreements`** | **en el ID del nodo**, y en el título: *Aprovechamiento de NAFTA y Tratados de Libre Comercio* |
| **`certificado_de_origen_tratados_libre_comercio`** | **en el TÍTULO**: *Certificado de Origen y Tratados de Libre Comercio (**NAFTA**, Rules of Origin, RVC)*, y en el resumen, y en un paso |
| `certificado_de_origen_coo` | paso 3 |
| `documentacion_exportacion` | la lista de documentos |
| `regla_de_minimis` | el porcentaje, *7% para NAFTA* |
| `reglas_origen_sectoriales` | dos pasos, con el método de trazabilidad automotriz |
| `foreign_trade_zones` | mención |
| `import_regulations_foreign_governments` | mención |

> **El del id es el caro, y engancha con la DECISION 4 de la mesa de racimos**:
> renombrar `nafta_free_trade_agreements` **exige alias**, igual que las 36
> parejas de sufijo. **Un id que muere sin alias rompe todo lo que apuntaba a él.**
>
> **CAFTA-DR sí sigue vigente**, así que de la lista del paso 3 solo NAFTA está
> muerto. **La reparación es quirúrgica, no una reescritura del dominio.**

#### EL SEGUNDO HALLAZGO, y es peor que el primero: Incoterms sin año

**Al medir el otro marco que la ficha nombra en su texto fundacional:**

| | |
|---|---:|
| nodos vivos que nombran **Incoterms** | **11** |
| de esos, los que citan **una versión** (2010, 2020...) | **0** |

> **La ficha nació diciendo que citar Incoterms desactualizado miente con
> precisión. La medición dice algo distinto y peor: el catálogo NO CITA NINGUNA
> VERSIÓN, once veces.**
>
> **Y para Incoterms eso importa de verdad**, porque las reglas cambiaron entre
> 2010 y 2020: **DAT desapareció y se convirtió en DPU**, y las coberturas de
> seguro de CIP se movieron. **Un nodo que dice *usa Incoterms* sin año no está
> desactualizado: está indeterminado**, que es más difícil de detectar y de
> arreglar.

#### EL PUNTERO JURISDICCIONAL NO SALVA DE ESTO, y conviene decirlo

**`certificado_de_origen_coo` tiene el puntero**, literal en su resumen: *esta
mecánica refleja la normativa de EE.UU. y los acuerdos vigentes a la fecha de la
fuente; verifica el acuerdo y la regulación vigente en tu jurisdicción antes de
actuar.*

> **Y aun así manda buscar NAFTA.** El puntero avisa de que **la jurisdicción**
> puede ser otra; **no avisa de que el tratado nombrado ya no existe en ninguna
> jurisdicción.** Son dos averías distintas y el puntero solo cubre una.
>
> **Es el mismo límite que la ficha de herramientas ya midió con otras palabras**:
> *la muerta se detecta abriendo el enlace; la mutada no, porque el enlace abre.*
> Aquí: **el puntero se lee y no dice nada, porque lo que caducó no es la
> jurisdicción sino el nombre.**

**Ningún nodo se toca.** La ficha queda **despierta y con dos mediciones**, con
las cifras corregidas en la adjudicación de abajo: **seis nodos citan un tratado
extinto** y **doce un marco sin versión**.

---

### ADJUDICADO PARA EL PLAN (11 ago 2026): `exportacion` es el PRIMER BARRIDO DE VIGENCIA

**La decision se sostiene. La evidencia que yo di para ella NO, y la corrijo
antes de usarla.**

#### TRES CORRECCIONES A LO QUE ESCRIBI AYER

**Las tres son mias y las tres salen de recontar el grafo en vez de leer mi
propia salida de ayer.**

> **1. `export.gov` esta en TRES nodos, no en cuatro.** Escribi *cuatro nodos,
> cinco menciones*. Lo real: **3 nodos y 4 menciones**, porque
> `calculo_de_aranceles_importacion` lo nombra **dos veces** y yo lei dos lineas
> de salida como dos nodos.
>
> **2. LA INTERSECCION QUE CITE ES VACIA.** Escribi que *tres de esos cuatro
> nodos estan tambien en la lista de NAFTA o de Incoterms sin version*. **Es
> falso: la interseccion entre los nodos de `export.gov` y los de NAFTA o
> Incoterms no tiene ni un elemento.** Son conjuntos disjuntos.
>
> **3. La cifra de NAFTA mezclaba dos cosas distintas.** Dije 8 nodos. Lo exacto:
> **6 nodos lo NOMBRAN en su texto**, y otros **2 solo lo llevan en una ARISTA**
> que apunta al id `nafta_free_trade_agreements`. **Apuntar al nodo no es citar el
> tratado**, y mezclarlos infla la cifra.

**Y la correccion 3 deja un dato util que no tenia**: `foreign_trade_zones` e
`import_regulations_foreign_governments` **apuntan por arista a
`nafta_free_trade_agreements`**. Cuando la DECISION 4 renombre ese id, **esas dos
aristas se rompen si no lleva alias.** Es la prueba concreta de por que el alias
no es opcional.

#### LA EVIDENCIA REAL, y es mas fuerte que la que yo habia dado

**Recontado del grafo, sobre nodos VIVOS:**

| averia | nodos vivos |
|---|---:|
| citan **NAFTA** en su texto | **6** |
| citan **Incoterms** sin ninguna version, EN SU TEXTO | **3** |
| cablean **`export.gov`** | **3** |
| **UNION de las tres** | **12** |

> **CORRECCION DECLARADA, 12 ago 2026. LAS DOS FILAS QUE CAMBIAN SON LA DE INCOTERMS
> Y LA DE LA UNION.** La cifra de **12** sumaba **los 3 que lo CITAN en su texto mas 9
> que solo lo llevan en una arista o en el id**.
>
> **ES EL MISMO ERROR QUE ESTA MISMA ADJUDICACION HABIA CORREGIDO TRES PARRAFOS MAS
> ARRIBA PARA NAFTA**: *apuntar al nodo no es citar el tratado, y mezclarlos infla la
> cifra*. **Se corrigio la fila de NAFTA y no la de al lado.**
>
> **LOS TRES, remedidos sobre el grafo y nombrados**, los tres de `exportacion` y los
> tres **sin version**: `incoterms_reglas_comerciales_internacionales`,
> `terminos_de_venta_incoterms` y `seguro_de_carga_transporte`. **Los dos primeros lo
> llevan tambien en el id.**
>
> **LA DECISION DE FONDO NO SE MUEVE, Y HAY QUE DECIRLO ASI DE CLARO.** La union baja
> de **21 a 12 nodos**, **con solape cero entre las tres averias**, y **los 12 de 12
> siguen siendo de `exportacion`**, que era el argumento. **El argumento sobrevive
> entero: solo cambia el tamano.**

> **LOS VEINTIUNO SON DE `exportacion`. Los 21 de 21.** Ni un solo nodo de otro
> dominio esta tocado por ninguna de las tres averias de vigencia.
>
> **Eso adjudica el barrido mejor que mi solapamiento inventado.** No hace falta
> que un nodo acumule dos averias: **hace falta que el dominio las acumule todas,
> y las acumula en exclusiva.**

**Por eso `exportacion` va primero, y con este orden dentro:**

1. **`nafta_free_trade_agreements`**, porque el tratado extinto le da **el id y el
   titulo**, y porque **dos aristas dependen de ese id**: es el unico de los 21
   que exige alias, o sea que es el que hay que resolver antes de mover nada.
2. **`certificado_de_origen_tratados_libre_comercio`**, que lo lleva en el titulo
   y lo repite **cuatro veces**.
3. **Los otros cuatro que lo nombran** en resumen o pasos.
4. **Los doce de Incoterms**, que no piden reescritura sino **anadir el ano**, y
   que se hacen de una pasada porque la decision es una sola.
5. **Los tres de `export.gov`**, que solo piden cambiar el dominio por `trade.gov`.

> **Ninguna de las cinco toca la doctrina de un nodo.** Son nombres, versiones y
> direcciones. **Por eso el barrido de vigencia es el mas barato de todos los
> frentes abiertos, y por eso conviene hacerlo antes que el destejido.**

---

### MEDICION DE `franquicias` (11 ago 2026), para decidir si entra al barrido

**Encargo del fundador: medir, no leer, y sin adjudicar.** Mismo instrumento que
se uso para `exportacion`, corrido sobre las cinco casas de texto de los nodos
vivos.

| | `franquicias` | `exportacion` |
|---|---:|---:|
| nodos vivos | **195** | **141** |
| **(a) cablean marco legal de UN SOLO PAIS** | **31** (15,9%) | **42** (29,8%) |
| **(b) nombran organismo o portal** | 12 (6,2%) | 34 (24,1%) |
| **(c) citan norma con version o fecha** | 10 (5,1%) | 3 (2,1%) |

**DONDE CONDICIONA, por la doctrina del marco (*la condicion honesta se copia A LA
PUERTA*):**

| | `franquicias` | `exportacion` |
|---|---:|---:|
| **EN LA PUERTA**, con el pais nombrado en `condiciones_activacion` | **2** de 31 | **5** de 42 |
| **EN LA DESPEDIDA**, solo en `resumen_teorico` | 4 | 23 |
| **EN NINGUN SITIO** | **25** (80,6%) | 14 (33,3%) |
| ejecutan el marco en pasos o entregable **sin condicion en la puerta** | **25** | 36 |

**LAS FAMILIAS DEL MARCO EN `franquicias`**, y ninguna es multinacional:

| familia | nodos |
|---|---:|
| documento de divulgacion (**FDD** / UFOC) | **23** |
| regla federal (**FTC 436**, PMPA) | 9 |
| **registro o ley estatal** | 9 |
| items numerados del FDD (Item 8, 19, 23) | 6 |
| cifra legal en dolares | 2 |
| agencia o base de datos de un pais (USPTO, TESS) | 1 |

**LOS 31, con su columna de donde condiciona:**

| id | familias | donde |
|---|---|---|
| `comprender_definicion_legal_franquicia` | FTC 436, cifra legal | **PUERTA** |
| `cumplimiento_ftc_rule_436` | FTC 436, FDD, estatal, cifra legal | **PUERTA** |
| `calculo_roi_franquiciado_2` | FDD, Item | DESPEDIDA |
| `cumplir_leyes_estatales_franquicia` | FDD, estatal | DESPEDIDA |
| `eleccion_abogado_franquicias` | FDD | DESPEDIDA |
| `registro_estatal_franquicia` | FTC 436, FDD, estatal | DESPEDIDA |
| `alternativa_business_opportunity_licensing` | FTC 436, estatal | **NINGUNO** |
| `alternativa_trademark_licensing` | FTC 436 | **NINGUNO** |
| `calificacion_prospectos_award` | FDD | **NINGUNO** |
| `cinco_categorias_costos_franquicia` | FDD, estatal | **NINGUNO** |
| `concepto_de_advances` | FDD | **NINGUNO** |
| `decision_fpr` | FDD, Item | **NINGUNO** |
| `decision_marca_comun_branding` | estatal | **NINGUNO** |
| `desarrollar_manual_operaciones` | FDD | **NINGUNO** |
| `diseno_programa_capacitacion_franquicia` | FDD | **NINGUNO** |
| `elaboracion_fdd` | FTC 436, FDD, Item | **NINGUNO** |
| `estimacion_inversion_inicial_franquiciador` | FDD | **NINGUNO** |
| `estructura_proveedores_aprobados_designados` | FDD | **NINGUNO** |
| `estructuras_combinadas_franquicia` | estatal | **NINGUNO** |
| `exenciones_legales_franquicia` | FTC 436 (y PMPA) | **NINGUNO** |
| `financial_performance_representations` | FTC 436, FDD, Item | **NINGUNO** |
| `ingresos_por_rebates` | FDD, Item | **NINGUNO** |
| `los_tres_grandes_criterios` | FDD | **NINGUNO** |
| `multiples_compradores_influyentes` | estatal | **NINGUNO** |
| `obtencion_marca_registrada` | agencia de un pais (USPTO, TESS) | **NINGUNO** |
| `preparar_fdd` | FTC 436, FDD | **NINGUNO** |
| `proceso_venta_franquicias` | FDD | **NINGUNO** |
| `programas_compra_franquicia` | FDD, Item | **NINGUNO** |
| `propuesta_valor_franquicia` | FDD | **NINGUNO** |
| `proteccion_propiedad_intelectual_franq` | FDD | **NINGUNO** |
| `revision_legal_marketing` | FDD, estatal | **NINGUNO** |

> **EL PEOR CASO MEDIDO, `obtencion_marca_registrada`.** Su puerta dice *"aun no
> se posee un trademark **federal**"*: **nombra la federacion como si hubiera una
> sola.** Sus pasos mandan buscar en la base **TESS del gobierno de EE.UU.** y
> presentar ante la **USPTO**, sin condicion. **Es el unico del dominio que
> condiciona con un adjetivo en vez de con un pais.**

> **LO QUE LA MEDICION DICE, sin adjudicar:** `franquicias` cablea marco de un solo
> pais en **la mitad de proporcion** que `exportacion`, pero **su fraccion muda es
> mas del doble**: 80,6% contra 33,3%. La doctrina mide **donde se actua**, no
> cuanto se cita. **La decision es del fundador.**

**SENALES DESCARTADAS a proposito, y por que** (van aparte para que nadie las
sume): 14 nodos mas dan positivo por **moneda de ilustracion** (*"vender tu
negocio en $10M"*), **doctrina juridica general** (responsabilidad vicaria, no
competencia, secreto comercial) o **dato de mercado de un pais** (*"mas de 3.000
franquiciadores activos en EE.UU."*). **Ninguna de las tres es marco legal de un
solo pais** y contarlas subiria la cifra de 31 a 45 sin que haya nada que reparar.

### EL PAR DE NAFTA: los tres encargos caen sobre los mismos dos nodos

**Del puesto 1955 del cribado y de la relectura R41.**
`certificado_de_origen_tratados_libre_comercio` y `nafta_free_trade_agreements`
**son a la vez** el par que el cribado manda **fundir**, los numeros **1 y 2 de la
lista de este barrido**, y **el ejemplar escrito de la DECISION 4**, la del alias.

> **Por el TOQUE UNICO del banco 9.4, los tres van en UN SOLO ACTO.** Hacerlos por
> separado significa **reparar la vigencia de un nodo que la fusion va a borrar
> despues.**

**Medido contra el grafo, y es la parte util:** el id que este barrido manda matar
por llevar un tratado extinto, `nafta_free_trade_agreements`, **es tambien el que
la fusion puede matar**. Si la fusion va **hacia**
`certificado_de_origen_tratados_libre_comercio`, **el mismo acto cierra los tres
encargos**. Con dos condiciones verificadas:

1. **El alias es obligatorio**: `foreign_trade_zones` lleva ese id en
   `nodos_previos` e `import_regulations_foreign_governments` en
   `nodos_siguientes`, y **hoy ninguno de los dos nodos tiene `ids_alias`.**
2. **Las cinco perdidas se reponen**: *obtenido en su totalidad*; la conservacion
   por el periodo que exija la aduana; las cuatro reglas del articulo 401; los dos
   porcentajes (60 por transaccion, 50 por costo neto); y **los nombres de los
   formularios**, sin los cuales el paso de completar el certificado no dice que
   papel llenar.

**No se adjudica la direccion de la fusion.** Queda medido que **una de las dos
cierra los tres encargos y la otra no**, y va a la mesa.

---

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

**EL CENSO PASA A CUATRO COLUMNAS**, porque tres no alcanzaban para decir lo que
se encontro. **`CAMBIADA` es columna, no matiz de `viva`:**

| | muertas | **CAMBIADAS** | vivas sin cambio | no verificables | total |
|---|---:|---:|---:|---:|---:|
| **antes del lote** | 6 | 0 | 5 | 1 | **12** |
| **el lote** | **1** | **6** | **9** | **2** | **18** |
| **entrada 5, `export.gov`** | 0 | **1** | 0 | 0 | **1** |
| **entrada 6, del par 176** | **2** | 0 | 0 | 0 | **2** |
| **CENSO ENTERO** | **9** | **7** | **14** | **3** | **33** |

**Las seis CAMBIADAS, con su evidencia y con lo que cambio:**

| nombre | que cambio | evidencia |
|---|---|---|
| **Google Analytics** | **la version**, y rompe el paso | Universal Analytics dejo de recoger datos el **1 jul 2023**; acceso y API cortados en jul 2024 **y datos borrados** |
| **VMware** | **la forma de comprarlo**, y rompe el paso | Broadcom **termino las perpetuas en 2024**, todo a suscripcion por nucleo; **descontinuados el hipervisor vSphere gratuito y los Essentials Kits** |
| **Energy Star** | **la casa**: de la EPA al DOE | propuesto para eliminacion en 2025 con cero dolares en el presupuesto FY2026; **acuerdo EPA/DOE de marzo de 2026** |
| **EPCglobal** | **el estatuto**: de organizacion a iniciativa | constituida **dentro de GS1 en 2005**; hoy es una iniciativa de GS1 |
| **Optimizely** | **dueno y alcance** | Episerver la compro en oct 2020 y **rebautizo la empresa entera como Optimizely en ene 2021**; de herramienta A/B a suite |
| **Unbounce** | **dueno** | controlada por Crest Rock Partners; **fusionada con Insightly en jul 2024** |

> **PRECISION SOBRE DONDE CAE LA FRONTERA, y la digo porque la columna se puede
> leer mal.** El criterio que selecciona exactamente estas seis es **cambio
> material documentado dentro del lote**. Con un criterio **mas estricto**, que el
> cambio rompa el paso que la usa, **solo Google Analytics y VMware califican**;
> las otras cuatro cambiaron de casa, de estatuto o de dueno sin que el lector
> tenga que hacer nada distinto. Con un criterio **mas laxo**, cambio de dueno,
> **entraria tambien `InnoCentive`** del lote anterior, adquirida por Wazoku en
> 2020. **La cifra queda en seis como esta dictada, y queda escrito cual es su
> borde por si el auditor lo quiere mover.**

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

---

#### LAS DOS REGLAS QUE ESTE LOTE DEJA ESCRITAS

**Se escriben como reglas y no como comentario porque el barrido va a usarlas,
y porque las dos salieron de datos, no de opinion.**

> **REGLA DE DETECCION**: **la muerta se detecta abriendo el enlace; la mutada
> no, porque el enlace abre.**
>
> De ahi que **el barrido no pueda preguntar solo si la herramienta existe**.
> Tiene que preguntar **si el paso que la usa sigue siendo ejecutable**, que es
> otra pregunta y bastante mas cara de contestar. Una herramienta institucional
> **no muere: muta**, y la instruccion escrita contra la forma vieja **caduca
> exactamente igual de mal** que la que nombra una empresa cerrada.

> **REGLA DE MORTALIDAD POR TIPO**: **muere el producto comercial de nicho; el
> estandar y la institucion no mueren, mutan.**
>
> **Las siete muertas son siete productos comerciales de nicho** (Alexa, Compete,
> Perfect Audience, The Deck, oDesk, Elance y el nombre Visual Website
> Optimizer): **ninguna es un estandar, una institucion ni un producto de
> plataforma grande.** De las **siete institucionales o de plataforma grande**
> (GS1, EPCglobal, Energy Star, Google Analytics, Keyword Planner, Trends y las
> plataformas generales), **cero muertas y cuatro cambiadas.**
>
> **Nombrar un producto comercial de nicho es apostar. Nombrar un estandar o una
> institucion es seguro para el NOMBRE y no lo es para el PROCEDIMIENTO. Las dos
> apuestas se pierden, solo que de maneras distintas.**

---

#### EL REMEDIO DE LA CASA: el patron espejo del marco-pais

**La ficha hermana de arriba resolvio el marco-pais con una regla de sitio: la
condicion se copia A LA PUERTA, donde se actua. Este lote permite escribir su
espejo, y el espejo no es de sitio sino de GRADO DE COMPROMISO.**

**Primero hay que separar dos usos que hoy se tratan igual y no lo son:**

| uso | que es | como se arregla |
|---|---|---|
| **herramienta-EJEMPLO** | el nodo ensena una **capacidad** y nombra un producto solo para ilustrarla. El paso sigue teniendo sentido si el producto desaparece | **se vuelve mencion generica con ejemplos vivos**: se nombra la capacidad y los productos van detras, como ejemplos y no como instruccion |
| **herramienta-OBJETO** | el nodo trata **sobre esa herramienta**. Sin ella no queda nodo | **no se generaliza: se le pone FICHA DE VIGENCIA**, con fecha de verificacion, y se revisa en cada pasada |

> **EL EJEMPLAR ESTA EN EL PROPIO CATALOGO, y por eso este remedio no hay que
> inventarlo.** Dos nodos hermanos, mismo dominio, misma fuente y mismo tema,
> escriben el mismo paso de las dos maneras:
>
> | | como lo dice |
> |---|---|
> | `analisis_trafico_competitivo`, paso 1 | *Buscar y comparar trafico de competidores con herramientas como **Alexa o Compete*** |
> | `capturar_conocimiento_de_mercado`, paso 3 | *Usar **herramientas de medicion de trafico web** y rankings de app stores* |
>
> **El segundo no caduca. El primero caduco en 2022.** La redaccion arreglada
> **esta escrita**, en un nodo hermano, y **lo unico que hace falta es
> copiarla**.

**Por que este remedio es hermano del de marco-pais y no otra cosa**: los dos
tratan **una dependencia que el nodo no declara**. Alli la dependencia es de
**jurisdiccion** y el remedio es **declararla en la puerta**. Aqui la dependencia
es de **un producto de un tercero** y el remedio es **no contraerla**, o
declararla con fecha si es inevitable. **En los dos casos el nodo miente por
omision, y en los dos el arreglo es barato porque no toca la doctrina.**

> **ANOMALIA ANOTADA, que es el argumento de este remedio en una linea**: el
> catalogo nombra **oDesk y Elance**, las dos marcas muertas, **y no nombra
> Upwork ni una sola vez** (verificado: cero apariciones en el grafo). **La
> marca viva en la que las dos se fundieron no esta.** Un nodo que dijera
> *plataformas de trabajo por encargo* seguiria de pie; el que nombra las dos
> marcas manda al lector a dos sitios que ya no existen.

---

#### EN CONFLICTO DECLARADO, sin arbitro

**Dos nombres se quedan sin veredicto a proposito. No es que falte trabajo: es
que las fuentes se contradicen y forzar una lectura seria inventar.**

| nombre | una fuente dice | la otra dice | estado |
|---|---|---|---|
| **Quantcast** (el producto **Quantcast Measure**, paso 6 de `analisis_trafico_competitivo`) | **descontinuado**, segun directorios de software | **activo**, segun las paginas propias de Quantcast y su documentacion de ayuda | **EN CONFLICTO DECLARADO** |
| **RentaGreenBox** | **cerrada de forma permanente**, segun Crunchbase | **local activo en Huntington Beach a julio de 2026**, segun Yelp, y el sitio propio responde | **EN CONFLICTO DECLARADO** |

> **El veredicto anterior de `Quantcast` NO se revierte.** La entrada del lote 22
> lo dio por vivo y **la empresa lo esta**; lo que esta en duda es el producto
> concreto que el paso pide. **Queda marcado, no cambiado.**
>
> **Ninguno de los dos se cuenta como muerto ni como vivo sin cambio en la tabla
> de arriba**: los dos van en `no verificables`, que es exactamente para lo que
> existe esa columna. **Si el conflicto se resuelve, se resuelve con evidencia
> nueva y se anota la fecha.**

---

**Ningún nodo se toca desde esta ficha.** Lo que cambia es que el barrido ya
tiene **sus seis casas, su orden de prioridad, su segunda pregunta y sus dos
remedios escritos**.

---

### Entrada 5 (11 ago 2026): `export.gov`, la primera del cierre de costuras

**Sale de la tanda 22, la ultima del instrumento, del nodo
`exportacion/evaluacion_preparacion_empresa_exportar`, cuyo ultimo paso dice:**

> *Realiza la evaluacion formal de preparacion exportadora en
> **export.gov/begin/assessment.asp***

| nombre | estado | evidencia |
|---|---|---|
| **export.gov** | **CAMBIADA**: cambio de casa | El sitio de la International Trade Administration **migro a `trade.gov`**. Lo que queda de export.gov vive como **archivo en `legacy.export.gov`**; la ITA activa esta en trade.gov |

> **Es la misma clase que `Energy Star`**, que sobrevivio mudandose de la EPA al
> DOE: **el servicio existe y la puerta por la que el nodo manda entrar ya no.**
>
> **Y el detalle de la URL delata la edad sin necesidad de buscar nada**: termina
> en **`.asp`**, una extension de pagina que hace anos que no se emite. **La
> propia direccion lleva su fecha escrita.**

#### Y NO ES UN NODO, SON CUATRO, recontado del grafo

| nodo | como lo cablea |
|---|---|
| `evaluacion_preparacion_empresa_exportar` | `export.gov/begin/assessment.asp` |
| `calculo_de_aranceles_importacion` | **dos veces**: en el resumen y en un paso, *la base de datos de aranceles en export.gov* |
| `reglas_de_origen_fta_2` | `export.gov/fta` |

> **Cinco menciones en cuatro nodos, todas del dominio `exportacion`.** Ninguna
> apunta a trade.gov.

**Y engancha con la ficha hermana de vigencia**: **tres de estos cuatro nodos
estan tambien en la lista de NAFTA o de Incoterms sin version.** El dominio
`exportacion` acumula las tres averias a la vez, **la herramienta mudada, el
tratado extinto y el marco sin version**, y eso lo convierte en **el candidato
natural del primer barrido de vigencia**, por delante de los demas.

---

---

### Entrada 6 (11 ago 2026): `Delicious` y `Social Mention`, las dos MUERTAS

**Salen del puesto 176 del cribado intra, del par `targeting_blogs_channel`
contra `targeting_blogs_traccion`**, que la relectura R2 acaba de sostener como
fusión. **Los dos nodos mandan encontrar blogs de nicho con estas herramientas.**

| nombre | estado | evidencia |
|---|---|---|
| **Delicious** (delicious.com, marcadores sociales) | **MUERTA** | **Pinboard la compró en junio de 2017** por 35.000 dólares y **la puso en solo lectura el 15 de junio de 2017**: la API dejó de funcionar y no se pueden añadir ni editar marcadores. Se conserva **como archivo**, un museo de enlaces del pasado |
| **Social Mention** (socialmention.com) | **MUERTA** | El sitio original **está caído en su mayor parte y sin mantenimiento**. **Salvedad anotada**: hoy existe una herramienta con ese nombre servida por **BrandMentions**, que es otra empresa; **el nombre sobrevive, el sitio que el nodo cablea no** |

> **Las dos están en el paso 1 de su nodo, que es el peor sitio posible**: es el
> paso que dice **cómo encontrar los blogs**. Un lector que empiece por ahí
> **empieza por dos herramientas que no le van a devolver nada**.
>
> **`Delicious` es además el caso más limpio de la clase MUERTA de todo el
> censo**: no cambió de dueño ni de casa ni de nombre. **Está congelada desde
> 2017 y se declara a sí misma museo.**

**Reparto entre los dos nodos, verificado**: `Delicious` aparece en **uno** de los
dos (`targeting_blogs_channel`) y `Social Mention` en **los dos**. **Tres
menciones muertas en dos nodos que además van a fusionarse**, así que **el
arreglo y la fusión son la misma operación**: al escribir el nodo superviviente
del par 176, las dos herramientas salen solas.

> **Y eso da la regla de orden que el plan necesita**: **cuando un nodo con
> herramienta muerta está en un par que va a fusionarse, el arreglo de vigencia
> NO se hace aparte.** Se hace al redactar el superviviente, o se hace dos veces.

---

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

### PRIMERA MEDICIÓN DE LA FICHA (13 ago 2026): la densidad no es la que parece

**La ficha llevaba dormida desde la cirugía de Calidad. El barrido nuevo
`paso_contra_nodo.py` le da su primera medición, y sale al revés de lo esperado.**

| | quality | núcleo |
|---|---:|---:|
| nodos vivos | 792 | 1.618 |
| candidatos paso-contra-nodo | **323** | 298 |
| de esos, **SIN arista** | **296** | 229 |
| candidatos por cada 100 nodos | **40,8** | 18,4 |

> **Quality tiene la MITAD de nodos que el núcleo y MÁS candidatos**, y más del
> doble por nodo.

**LO QUE ESTO CAMBIA EN EL DIAGNÓSTICO, y es lo importante.** La ficha decía que
quality está *tan conectado* que `ramaDe()` desde cualquier semilla se traga todo.
Sigue siendo cierto. **Pero el barrido mide lo contrario en el otro plano**: hay
**296 relaciones madre-hijo de contenido que el grafo NO tiene cableadas.**

> **Los dos hechos juntos dicen algo que ninguno decía solo: las aristas de
> quality son MUCHAS y no son las que hacen falta.** El pack está lleno de enlaces
> que conectan todo con todo, y **le faltan justo los que codifican la jerarquía**
> (este paso lo desarrolla este nodo).
>
> **Por eso `ramaDe()` no discrimina**: no discrimina porque las aristas que tiene
> no significan jerarquía. **La densidad no es exceso de estructura: es ruido de
> estructura.**

**Lo que la ficha gana con esto**: deja de ser un problema de *demasiadas
aristas* y pasa a ser uno de *aristas equivocadas*. **El arreglo ya no es podar el
grafo: es añadir las 296 que faltan y volver a medir `ramaDe()` con ellas
puestas.** Sigue siendo post-beta, pero ahora tiene una hipótesis medible.

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

---

## MESA PENDIENTE: EL RACIMO DEL PIVOTE

**Convocada el 13 ago 2026, desde el tramo 843 a 848 del cribado intra.**

**Lo medido**: el censo dice **cinco miembros**, la lectura levanta **siete**
(entran `pivote_o_proceder`, que repite en el 268 con un miembro de la nómina, y
`decision_pivote_perseverar`; queda fuera `war_room_pivot_proceed`, que monta la
sala y no decide). **21 pares posibles, 10 en cola, 5 leídos, 11 que nunca
entraron, dos aristas internas entre siete.**

**El saldo de los leídos**: dentro de Blank ya está resuelto, la misma puerta
contada dos veces **repite** (268 A) y puertas distintas del proceso son **sanas**
(594 D, 598 D). **El cruce entre libros no**: 771 y 843, los dos en **B**.

### LA RECOMENDACIÓN DEL AUDITOR, registrada y sin adjudicar

> **El catálogo se organiza por lo que el lector HACE, no por la biblioteca.**
>
> **UN NODO POR PUERTA** como opción por defecto. **Nodo por libro solo donde los
> libros discrepen de verdad**, y en ese caso se llama **FRONTERA DECLARADA** y se
> escribe como tal, no como dos nodos que se ignoran.

> **Lo que la mesa tiene que hacer con esto**: mirar los dos pares en B (771 y
> 843) y decidir si Ries y Blank **discrepan** sobre cómo decidir un pivote, o si
> solo **entran por sitios distintos** a la misma puerta. Si es lo segundo, la
> recomendación los resuelve a los dos de una vez.

---

## ARREGLOS MECÁNICOS DEL GRAFO (13 ago 2026)

### 1. LAS 27 AUTO-ARISTAS

**Medido**: 27 nodos vivos se listan a sí mismos en sus `nodos_previos` o
`nodos_siguientes`. Al resolver alias, el enlace vuelve al propio nodo.

| qué | cómo |
|---|---|
| **arreglo** | una pasada que borra el propio id de las dos listas de cada nodo. **Mecánico, sin criterio** |
| **guarda** | validación en **Gate 0**: ningún nodo puede citarse a sí mismo como previo o siguiente |
| **por qué importa** | no rompe nada visible, **pero hace que un aislado deje de parecer aislado**. Es un falso negativo silencioso, y ya alcanzó a una medición (banco §9.14) |

### 2. TRES RACIMOS CON MIEMBROS DE OTRO DOMINIO

Encontrado al leer los nueve pares dirigidos (informe §33).

| racimo | miembro | su dominio real |
|---|---|---|
| el lienzo de propuesta de valor (`core`) | `desarrollo_value_proposition_usp` | **franquicias** |
| Mapeo del flujo de valor (`quality`) | `value_stream_mapping_ambiental` | **environmental** |
| Mapeo del flujo de valor (`quality`) | `analisis_flujo_de_valor` | **core** |

> **Un racimo con miembros de tres dominios no es una familia: es un grupo de
> nombres parecidos.** No es mecánico: pide decidir si la nómina se depura o si
> esos racimos se declaran explícitamente transversales.

**CONTROL MECÁNICO NUEVO, adoptado el 13 ago 2026**: **revisar TODA nómina por el
DOMINIO de sus miembros.** Es una pasada de lectura sobre
`docs/RACIMOS_MIEMBROS.jsonl` cruzada con el grafo, sin criterio: **lista los
racimos cuyos miembros no comparten dominio.**

> **Los tres casos ya hallados son la muestra, no el censo.** El control los
> encuentra todos de una vez, y cada uno se resuelve igual: **o la nómina se
> depura, o el racimo se declara transversal de forma explícita.** Lo que no puede
> quedar es un racimo que **parece** de un dominio y no lo es.

---

## LA BOLSA DEL PASO CONTRA NODO: 624 candidatos, una sola clase

**Medido el 13 ago 2026** con `scripts/paso_contra_nodo.py` y una **muestra pineada
de 24** (pin en `docs/PIN_SORTEO_PASO_NODO.txt`, informe §40).

| | |
|---|---:|
| candidatos **sin arista** | **624** |
| leidos en la muestra | 24 |
| **JERARQUIA SANA** (arista que falta) | **19** |
| **MADRE QUE REPITE** (poda) | **0** |
| FALSO POSITIVO | 5 |

> **CERO PODAS EN VEINTICUATRO LECTURAS.** La bolsa **no es una mezcla de dos
> clases de arreglo: es UNA, y es la barata.** Eso simplifica el plan: no hay que
> triar entre enlazar y podar, hay que **enlazar**.

> ## **CORRECCION DECLARADA, 12 ago 2026: ESTA GLOSA SE RETIRA ENTERA.**
>
> **LA BOLSA SI ES UNA MEZCLA DE DOS CLASES.** Remedido con el instrumento calibrado
> con la senal del verbo y con **46 lecturas pineadas en dos muestras disjuntas**:
>
> | | publicado | **medido** |
> |---|---:|---:|
> | candidatos sin arista | 624 | **477** |
> | lecturas | 24 | **46** |
> | **jerarquia sana** | 19 | **32, 69,6%** |
> | **MADRE QUE REPITE** | **0** | **7, 15,2%** |
> | falso positivo | 5 | 7, 15,2% |
> | proyeccion de aristas | 489, banda 376 a 586 | **332, banda 263 a 386** |
> | **pares gemelos proyectados** | **no se contemplaban** | **73, banda 36 a 135** |
>
> **Y LA MEDIDA EXACTA DE LA DISCREPANCIA, porque no todo se explica con el tamano de
> la muestra:** el techo al 95% de un **0 de 24** es **11,7%**, y lo medido es
> **15,2%**. **No son compatibles del todo, pero por poco.** Quedan **dos explicaciones
> abiertas** y no se puede elegir entre ellas con lo que hay: **o la muestra vieja tuvo
> mala suerte, o la clase MADRE QUE REPITE no se aplico igual al leerla.** Se escribe
> como pregunta abierta y no como conclusion.
>
> **LO QUE SI QUEDA CERRADO Y ES REGLA, y vale para todo el archivo:**
>
> > **UN CERO SOBRE 24 LECTURAS NO ES UN CERO: ES UN TECHO.** Se escribe *no vi ninguno
> > en 24, techo 11,7%*, **nunca** *no hay*. Es el banco **9.21** aplicado a la clase
> > vacia: **la cifra lleva su corte, y el cero lleva su banda.**

**PROYECCION, declarada como proyeccion**: aplicando la tasa de cada estrato a su
tamano salen **489** jerarquias sanas. El intervalo de Wilson al 95% sobre 19 de
24 va de 60% a 94%, o sea **entre 376 y 586 aristas que faltan**.

### CALIBRACION PARA UNA CORRIDA FUTURA: el modo de fallo es EL VERBO

**No se aplica a la lista ya emitida**, que se lee como esta. Es para el dia que
el instrumento vuelva a correr.

> **En cuatro de los cinco falsos positivos, el paso y el hijo comparten el
> SUSTANTIVO y cambian el VERBO**: leer contra disenar, monitorear contra lograr,
> listar contra definir, comprar contra certificar. **El instrumento mide
> vocabulario y no accion.**

> **La correccion que esto sugiere**: extraer el verbo principal del paso y el del
> titulo del hijo, y **penalizar el candidato cuando los verbos pertenecen a
> familias distintas** (observar contra construir, listar contra definir). No se
> toca el umbral: se anade una senal.

---

## LA CURA ACOPLADA MAYOR: el primer destejido del plan viene con gemelo costurado

**Registrado el 13 ago 2026, puesto 494 del cribado intra.**

`producto_minimo_viable` es **el emblema de la avería** (22 pasos, cinco
narraciones, bloque 80,2, el más alto del archivo) y es **el primer destejido del
plan**. Su gemelo, `principio_calidad_mvp`, **también es costura confirmada** (14
pasos, tres narraciones).

> **No son dos movimientos: son TRES.** Destejer el emblema, destejer al pariente,
> **y solo entonces decidir si lo que queda se funde.** Hacerlo en otro orden
> obliga a rehacer.

**Y el par queda CONGELADO por dependencia directa**: si el destejido de
`principio_calidad_mvp` conserva su narración de **la calidad** (pasos 1 a 5), el
par deja de repetir; si conserva la del **conjunto mínimo** (11 a 14), sigue
repitiendo. **No se puede saber antes de la cirugía.**

**Precedente exacto**: el puesto **341** (`blueprint_de_experiencia` contra
`customer_journey_mapping`), donde los dos estaban costurados y el solape era mapa
contra mapa. **Es la segunda vez que aparece esta forma, y ésta cae sobre el nodo
que abre el plan.**

### PROPUESTO: el barrido de confirmadas contra las A

**Van DOCE ejemplares de cura acoplada encontrados de uno en uno**, cuando una
relectura los cruza. El del puesto 492 **se podía declarar desde el 673** y no se
declaró.

> **Un barrido que cruce las costuras confirmadas contra todas las A del archivo
> diría cuántas hay de una vez**, en vez de irlas encontrando. Es de solo lectura
> y no adjudica nada: **cambia el goteo por una cifra.**

> **CORRIDO EL 13 ago 2026, y la cifra esta en la seccion 45 del informe: 17
> costuras con gemelo, VIGENTE AL PUESTO 1050.** Corregida a **18** el mismo dia
> por el puesto 1061. **Y de ahi salio la regla del banco 9.21**: toda cifra de
> cruce lleva su fecha de corte, y **este barrido se repite UNA SOLA VEZ, al
> cierre del cribado**; entre medias el goteo sigue par por par sobre esta base.

---

## `brainstorming_divergente`: EL NODO DE MAS FRENTES DEL CATALOGO

**Lo levanto el barrido de confirmadas del 13 ago 2026, y nadie lo habia contado
junto.** No es un pendiente nuevo: **son cuatro pendientes viejos que resultaron
ser el mismo nodo.**

### LOS CUATRO FRENTES, cada uno ya registrado por su lado

| frente | que pide | donde vive hoy |
|---|---|---|
| **1. DECISION DE FUENTE** | es el **injerto de Mollick**: el nodo lleva atribucion de un libro que no es de donde salio su contenido | ficha de campos sucios y censo de injertos |
| **2. DESTEJIDO** | es **costura CONFIRMADA**: tiene repeticion interna verificada | ficha de sub-fusion, tabla de confirmadas |
| **3. TRES GEMELOS** | `brainstorming_efectivo` (823), `reglas_brainstorming` (834) y `generar_multiples_opciones` (844): **su cura acoplada es de CUATRO nodos en un solo acto** | barrido de confirmadas, informe seccion 45 |
| **4. RACIMO DE CUATRO LIBROS** | el racimo del brainstorming cruza fuentes distintas, o sea que la fusion toca la atribucion de mas de un miembro | informe, racimo del brainstorming |

### EL ORDEN ES PROPIO Y NO ES NEGOCIABLE

> **1. LA FUENTE PRIMERO.** Mientras no este decidido de que libro es este nodo,
> cualquier fusion escribe la atribucion equivocada en el superviviente. **Y el
> superviviente es el que se queda: el error se vuelve permanente.**
>
> **2. EL DESTEJIDO DESPUES.** Con la fuente ya fijada, se le quita la repeticion
> interna. **Antes no**, porque el destejido decide que bloques sobreviven y esos
> bloques son los que van a cargar la atribucion.
>
> **3. LOS TRES GEMELOS AL FINAL, y los tres en un solo acto.** Solo con el nodo
> ya destejido se puede ver que le queda propio frente a cada gemelo. **Fundir
> antes de destejer obliga a decidir el destino de material que la cirugia iba a
> quitar de todos modos.**

**POR QUE SE ESCRIBE EL ORDEN Y NO SOLO LA LISTA: cualquier otro orden obliga a
rehacer.** Fundir antes de destejer se rehace; destejer antes de decidir la
fuente se rehace; tocar un gemelo antes que los otros dos deja al nodo con dos
formas distintas a la vez.

> **Es el unico nodo del catalogo con los cuatro frentes encima.** Y por eso es
> tambien **el mejor candidato a piloto**: lo que se aprenda aqui sirve para
> todas las curas acopladas que vienen detras, porque ninguna es mas dificil que
> esta.

---

## REGISTRO DE MESAS (abierto el 14 ago 2026)

**Una MESA es una decision que no se puede tomar mirando un par**: hace falta la
familia entera delante. Este registro las lista con su nomina medida y su
dependencia, si tiene.

> **REGLA QUE LAS GOBIERNA, adjudicada el 14 ago 2026:**
> **NINGUNA MESA SE SIENTA ANTES QUE LA MESA DE LA QUE DEPENDE.**
> El registro de dependencias vive en el informe, seccion 13.

### MESA 1: LAS PUERTAS Y EL PORTAFOLIO, unidas

**ADJUDICADO el 14 ago 2026: dejan de ser dos mesas.** Motivo escrito por el
fundador: **dos mesas que comparten franja deciden dos veces lo mismo o se
contradicen.**

> **La medicion respalda la adjudicacion**: la nomina unida tiene **doce aristas
> internas y OCHO cruzan la frontera vieja.** El grafo ya las trataba como una
> sola familia.

**NOMINA CERRADA: DIECISEIS miembros, cero candidatos fuera.**

| procedencia | nodos |
|---|---|
| puertas (6) | `sistema_stage_gate`, `stage_gate_system`, `estructura_gates`, `sistema_gates_go_kill`, `asignacion_recursos_en_gates`, `sistema_gestion_recursos_en_gates` |
| portafolio (7) | `portfolio_management`, `gestion_portafolio_formal`, `revision_portafolio_periodica`, `gestion_portafolio_dos_niveles`, `gestion_de_portafolio_gates_go_kill`, `gestion_portafolio_foco`, `equipos_dedicados_de_proyecto` |
| **los tres que arrastra `sistema_gates_go_kill`** | `requisitos_gates_con_dientes` (801), `gates_go_kill_decision_points` (1038), `estructura_de_gates` (765) |

| medida | cuantas |
|---|---:|
| pares posibles | 120 |
| en cola | 21 |
| leidos | **18** |
| **en A** | **15** |
| B / D | 1 / 2 |
| pendientes | 3 (1366, 1399, 1524) |
| **nunca encolados** | **99** |

> **Quince pares en A entre dieciseis nodos: el bloque de repeticion mas grande
> medido.** Y la reserva, con su cifra: **la mesa se sienta sabiendo el 15% de sus
> pares.**
>
> **LO QUE ESTA ADJUDICACION DEROGA**: el orden que fijaba el cruce 2 del informe,
> *primero las puertas y luego el portafolio*, **ya no aplica**. No hay dos mesas
> que ordenar.

### MESA 2: EL RACIMO DEL PIVOTE

Ver la ficha de mas arriba. **Nomina de siete, sin cambios**: el puesto 1140 salio
**D** y `actualizar_modelo_de_negocio_pivot_o_proceed` **no entra** (ocho
veredictos y los ocho D).

### MESA 3: LA JUNTA ASESORA

**Cuatro miembros**: `formalize_advisory_board`, `formalizar_junta_asesora`,
`identificar_junta_asesores`, `identificar_consejo_asesores`.

> **TIENE UNA MESA COLGANDO DE ELLA**, y es la primera dependencia registrada del
> plan: **el par 1190 no se puede decidir hasta que esta mesa decida el 367.**
> Detalle en el informe, seccion 13.

### MESA 4: LA APERTURA DE CUSTOMER VALIDATION

**Levantada en la relectura R32, puesto 549.** `filosofia_customer_validation`
contra `introduccion_validacion_clientes`, y con **`earlyvangelists_ventas_tempranas`**
dentro por la A del puesto 1096.

> **Lo que decide: si el catalogo quiere UNA puerta de entrada a Customer
> Validation o dos.** Medido: `filosofia_customer_validation` **repite con quien
> abre la etapa** (dos A) **y jerarquiza con quien la ejecuta** (cinco lecturas
> sanas en el tramo 1101-1200).

---

## ORDEN DE LA PASADA: LAS CIRUGIAS SE ORDENAN POR CONGELADOS LIBERADOS

**Adjudicado el 14 ago 2026.** El criterio de orden no es el tamano del nodo ni
lo averiado que este: es **cuantos pares desbloquea su destejido.**

> **La medicion que lo obliga: OCHO de los QUINCE congelados cuelgan de TRES
> nodos.** No estan repartidos por el catalogo, **estan amontonados**. Hacer esas
> tres primero libera mas de la mitad del inventario; hacerlas tarde deja ocho
> pares parados a la vez.

### LAS TRES PRIMERAS, en orden, con los pares que libera cada una

#### 1. `producto_minimo_viable` (22 pasos) libera TRES

| par | contra que nodo | clase hoy |
|---:|---|:---:|
| **494** | `principio_calidad_mvp` | **A** |
| **592** | `mvp_catalogo_tecnicas` | B |
| **830** | `prueba_mvp_alta_fidelidad` | B |

> **VA PRIMERA, y no solo por la cuenta.** El **494 es la CURA ACOPLADA MAYOR**:
> los dos nodos estan costurados, asi que es un **acto de tres**, destejer uno,
> destejer el otro y solo entonces decidir la fusion. **Y `principio_calidad_mvp`
> tiene catorce pasos**, o sea que el segundo destejido tampoco es pequeno.
>
> **El orden interno es obligatorio**: destejer `producto_minimo_viable`, destejer
> `principio_calidad_mvp`, resolver el **494**, y **solo despues** mirar el 592 y
> el 830, que se leen contra lo que haya quedado.

#### 2. `voz_del_cliente_voc` (10 pasos) libera TRES

| par | contra que nodo | clase hoy |
|---:|---|:---:|
| **724** | `voice_of_customer_estrategico` | B |
| **755** | `dia_en_la_vida_del_cliente` | B |
| **827** | `ganar_comprension_del_cliente` | B |

> **Los tres son B**, o sea que **los tres esperan exactamente lo mismo**: saber
> que queda del nodo para poder clasificarlos. **Es la cirugia mas limpia de las
> tres**: un solo destejido, sin gemelo costurado enfrente, y tres pares que se
> resuelven detras en una sola sentada.

#### 3. `ab_testing_optimizacion` (15 pasos) libera DOS

| par | contra que nodo | clase hoy |
|---:|---|:---:|
| **738** | `split_testing_experimentos_ab` | B |
| **1061** | `optimizacion_embudo_get_customers` | **A** |

> **VA TERCERA porque es la mas enredada de las tres.** El **1061 es el TERCER
> ACTO DE TRES del archivo**, costurada contra costurada, y el **738 tiene los DOS
> nodos averiados con el solape cruzando las dos junturas**. **Los dos pares
> dependen de dos destejidos, no de uno.**

### LO QUE QUEDA DETRAS, y por que no ordena la pasada

**Los siete congelados restantes cuelgan de un nodo cada uno** (599, 784, 798,
831, 835, 851 y el 1190). **Ninguno gana nada por ir antes que otro**, asi que se
hacen cuando toque su familia.

> **EXCEPCION, y es la unica del inventario: el 1190 no depende de una cirugia
> sino de OTRA MESA.** Espera a que la mesa de la junta asesora decida el 367. Va
> en el registro de dependencias del informe, seccion 13, no aqui.

### LA REGLA QUE ESTE ORDEN FIJA

> **Cuando varias cirugias estan disponibles, va primero la que libera mas pares
> congelados.** Y si dos empatan, va primero **la que no tenga gemelo costurado
> enfrente**, porque esa se puede cerrar en un acto y la otra necesita tres.

---

## CORRECCION A LA FICHA DE `brainstorming_divergente`: la cura es de CINCO, no de cuatro

**Encontrado el 14 ago 2026 en la relectura R33, puesto 586.**

La ficha del **NODO DE MAS FRENTES** dice que su cura acoplada es de **cuatro
nodos en un solo acto**, contando sus tres gemelos directos: `brainstorming_efectivo`
(823), `reglas_brainstorming` (834) y `generar_multiples_opciones` (844).

> **Medido hoy con la nomina cerrada: la familia es de CINCO.**
> `construir_sobre_ideas_ajenas` repite con `brainstorming_efectivo` (puesto 586),
> que es uno de los tres gemelos, **asi que por el banco 9.20 es candidato al mismo
> racimo.** Cinco pares en la cola, **los cinco leidos y los cinco en A**: es un
> **sub-puro de cinco** con una sola arista interna.
>
> **Y arrastra un sexto candidato**, `pensamiento_convergente_divergente`, por la
> A del puesto 943.

**POR QUE EL BARRIDO NO LO DIO, y no es un fallo suyo:** el barrido de las A
contesta **quien es gemelo de un nodo**. Una cura acoplada **fusiona una familia**,
y una familia es el **cierre transitivo** de esa relacion. **Son dos preguntas
distintas y la ficha uso la respuesta de la primera para la segunda.**

> **Lo que cambia en el plan**: el acto mas caro del inventario **crece de cuatro
> nodos a cinco, y puede ser de seis**. El orden escrito en la ficha, fuente
> primero, destejido despues y los gemelos al final, **no cambia**; lo que cambia
> es cuantos nodos entran en el ultimo paso.

---

## DOS NOTAS AL ORDEN DE LA PASADA (14 ago 2026)

### 1. LA TERCERA CIRUGIA NO TERMINA EN TRES DESTEJIDOS: TERMINA EN UNA FUSION

**El acto 2 del cierre transitivo, el de las pruebas A/B, tiene SEIS nodos y TRES
costuras.** El plan lo escribio como **tres destejidos**. **Falta el final.**

> **El puesto 643 emparejo a los DOS NODOS SANOS del acto**, `split_testing` y
> `test_ab_precio`, **y salio A.** O sea que **la repeticion de ese acto no esta
> solo dentro de las costuras: esta tambien entre los nodos limpios.**
>
> **Destejer las tres costuras NO cierra el acto.** Despues de las tres cirugias
> **queda una fusion sobre seis nodos**, y esa fusion habria hecho falta aunque
> ninguno estuviera costurado.

**EL TERCER PUESTO DEL ORDEN QUEDA ASI:**

| paso | que es |
|---:|---|
| 3a | destejer `ab_testing_optimizacion` |
| 3b | destejer `optimizacion_embudo_get_customers` |
| 3c | destejer `split_testing_experimentos_ab` |
| **3d** | **FUNDIR: decidir cuantos nodos quiere el catalogo entre los SEIS**, con los tres ya destejidos |

> **Es el unico puesto del orden con cuatro movimientos.** Y el cuarto no es
> opcional: **sin el, el acto queda con seis nodos limpios que siguen diciendo lo
> mismo.**

### 2. REMEDIR SIEMPRE RESTA, y las formas viejas sin remedir sobrecuentan

**Patron observado el 14 ago 2026, con dos casos y ninguno en contra.**

| figura | como se declaro | como quedo al remedir |
|---|---|---|
| el **racimo del capital de trabajo** (puesto 203) | **TRES nodos**: el conjunto mas sus dos mitades | **NO es racimo**: el conjunto **jerarquiza** con las dos mitades (191 D, 203 C). Su unica A esta con un nodo que no estaba en la figura |
| el **racimo del brainstorming** (ficha del nodo de mas frentes) | **CUATRO nodos** por gemelos directos | **SIETE** por cierre transitivo, **pero la direccion fue al reves**: ahi remedir SUMO |

> **El patron no es que remedir siempre resta en NUMERO: es que remedir siempre
> resta en CERTEZA.** En el 203 quito masa a la figura; en el brainstorming se la
> anadio. **Lo que las dos remediciones tienen en comun es que la figura escrita
> era falsa en su tamano**, y en las dos el error venia de **contar por cercania de
> tema en vez de por evidencia**.

**LO QUE ESTO DEJA DICHO PARA EL INVENTARIO:**

> **Toda forma vieja que no se haya remedido es sospechosa de estar mal
> dimensionada**, en cualquiera de las dos direcciones. **Las figuras declaradas
> por parecido** (mismo tema, mismo libro, nombres parecidos) **sobrecuentan**; las
> declaradas **por gemelo directo** cuando el arreglo es una fusion **subcuentan**,
> por el banco 9.24.
>
> **La regla practica**: antes de sentar una mesa, **remedir su nomina con el
> barrido de las A y con el cierre transitivo**, y escribir la cobertura al lado
> (banco 9.26). **Las dos remediciones hechas hasta hoy cambiaron el tamano de la
> mesa; ninguna lo dejo igual.**

---

## EL RETRATO DE LAS A: la pasada tiene DOS mesas, no diez (16 ago 2026)

**Pieza del inventario. Fecha de corte: VIGENTE AL PUESTO 1.400**, como manda el
banco 9.21. Recomputado entero del archivo, banco 9.10.

| medida | cifra |
|---|---:|
| pares en clase A | **326** |
| **nodos tocados por alguna A** | **466** |
| **componentes conexas** de la relacion gemelo | **175** |
| de dos nodos | **121** |
| de tres | 29 |
| de cuatro | 9 |
| de cinco | 7 |
| de seis | 4 |
| de siete | 3 |
| **de nueve** | **1**, el acto de Customer Discovery |
| **de doce** | **1**, el nucleo conexo de la mesa unida |

### LO QUE ESTO LE DICE AL PLAN, y hay que decirlo entero

> **LA PASADA NO TIENE DIEZ MESAS. TIENE DOS MESAS Y UN MONTON DE DECISIONES DE
> PAR.**

**Ciento veintiuna de las 175 componentes son parejas sueltas: el 69 por ciento.**
Una pareja suelta no necesita mesa. Necesita **una decision de dos nodos**: cual
sobrevive, o si se funden, o si se enlazan. Se resuelve leyendo dos fichas.

| forma | cuantas | que cuesta |
|---|---:|---|
| **pareja suelta** (2 nodos) | **121** | una decision, dos fichas delante |
| racimo chico (3 o 4) | 38 | una decision con contexto |
| racimo mediano (5 a 7) | 14 | **una sesion**, no una mesa |
| **mesa de verdad** (9 y 12) | **2** | **sesion larga, con nomina y orden escritos** |

> **Y LA SEGUNDA LECTURA, que es la que ahorra trabajo: NO HAY UNA TERCERA MESA
> ESCONDIDA.** El salto de tamano es limpio, de siete a nueve y de nueve a doce, y
> **las dos componentes grandes son exactamente las dos que el ejercicio ya tiene
> escritas**: el acto de Customer Discovery y la mesa unida de puertas y
> portafolio. **El mapa completo de las A no revela ninguna familia grande que no
> estuviera ya en el registro de mesas.**

**QUE SE HACE CON ESTO:**

> 1. **El registro de mesas no crece por descubrimiento.** Puede crecer porque el
>    fundador decida sentar una, no porque aparezca una que nadie habia visto.
> 2. **El grueso del trabajo de la pasada es en lote**, no en sesion: 121 decisiones
>    de par que se pueden agrupar por libro o por tema y despachar seguidas.
> 3. **La cifra es PROVISIONAL y va a crecer**, porque faltan 1.988 pares por leer.
>    Lo que no se espera que cambie es la FORMA: la cola ya entrego sus pares mas
>    parecidos, y lo que viene detras, por el 9.19, es jerarquia sin cablear.

> **La cobertura al lado, como manda el 9.26**: este retrato se toma sobre **1.400
> pares leidos de 3.388**, el 41,3 por ciento de la cola. **Es una forma
> PROVISIONAL como todas**, y la reserva concreta es que una sola A futura entre
> dos componentes grandes las une en una sola. **Ninguna de las dos mesas escritas
> se toco entre si hasta hoy.**

---

## CONTRADICCIONES INTERNAS (17 ago 2026)

**ADJUDICACION DEL FUNDADOR, y cierra el pendiente de doctrina del puesto 1632:**

> **LA CONTRADICCION NO DECIDE LA CLASE.** La clase la decide **continua-o-repite**
> y nada mas. Donde dos nodos se contradicen y ninguno desarrolla al otro, **la D
> se queda**. Lo que cambia es que la contradiccion **se anota aqui** en vez de
> perderse en la razon de un puesto.

**MOTIVO ESCRITO, del fundador:** *una frontera necesita dos doctrinas legitimas*.
Dos autores pueden mandar cosas opuestas y los dos tener razon en su contexto: eso
es una **frontera**. Pero **una sola fuente no se contradice a si misma**: si dos
nodos de la misma guia chocan, lo que hay es un **defecto de instruccion**, un
umbral o una condicion que uno de los dos omitio al extraerse. **Y el puesto 1642
lo prueba**: la condicion que faltaba, *la bolsa nunca es el contenedor unico*,
**existia en un tercer nodo de la misma familia.**

### LA TABLA, con sus dos columnas

| puesto | los dos nodos | **tipo** | que se hace |
|---:|---|---|---|
| **1632** | `elegir_sobre_o_caja_tamano` contra `evitar_materiales_blandos_contenedor_final`, **misma fuente** | **INTRA: defecto de instruccion** | **REPUESTO**: la condicion existe en `empacar_liquidos_doble_barrera` (puesto 1642), *nunca en bolsa o sobre como unico contenedor*. Verificar contra el original y reponerla en el nodo del umbral |
| **1714, 1741, 1765** | el **piso de cinco centimetros** de relleno contra **reducir el relleno excesivo** | **INTRA: defecto de instruccion** | falta el umbral: `tratar_packaging_costo_marca` dice *sin bajar de la proteccion minima* y **no la define**. La definicion existe en `aplicar_regla_fija_de_colchon_de_relleno`: cinco centimetros y la prueba de la sacudida. **Verificar contra el original y reponer** |
| **1726** | la **cinta en H** sobre la misma cara donde la etiqueta debe quedar sin cinta encima | **INTRA: defecto de instruccion** | ningun nodo dice donde va la etiqueta cuando la H ya esta puesta. **No hay tercer nodo que lo resuelva: hay que ir al original** |
| **1733 y 1679** | la **copia interior** y la **cara grande y plana** suponen caja; el nodo del umbral admite **sobre o bolsa** | **INTRA: defecto de instruccion** | misma raiz que el 1632. Se resuelve con la misma reposicion |
| **1643** | `evitar_materiales_blandos_contenedor_final` contra `revisar_necesidades_de_empaque`, **fuentes distintas** | **INTER: frontera candidata** | una guia admite bolsa plastica como envoltorio y la otra la descarta como contenedor final. **Dos doctrinas legitimas**: se anota como frontera y NO se repone nada |
| **1365, 1425, 1527, 1629** | leer la senal contra forzar el si; la competencia entre muchos contra el unico que dice que si; habilitadores contra obstaculos; cobrar por rapidez contra pagarla | **INTER: frontera candidata** | ya leidos como D con esa lectura. Quedan aqui como el precedente de la columna |
| **2094** | `combinar_crecimiento_corporativo_y_franquicia` manda **recursos dedicados a los DOS canales**, propio y franquiciado; `estrategia_multicanal_expansion` manda **recursos EXCLUSIVAMENTE a la franquicia** hasta lograr caja excedente. **Misma fuente** | **INTRA: defecto de instruccion** | falta la **condicion de momento**: uno describe el regimen y el otro el lanzamiento, pero **ninguno lo dice**. La condicion podria estar en `franquicia_mas_crecimiento_corporativo_hibrido`, que si ordena la secuencia. **Verificar contra el original y reponer el momento en el nodo que lo omitio**. Leido D en el 2094: la contradiccion no decide la clase (1632) |
| **2283** | `defensas_en_profundidad_2` manda **evaluar la integridad de cada capa defensiva DE FORMA INDEPENDIENTE**; `defensas_en_profundidad_3` manda **evaluar si existen DEPENDENCIAS OCULTAS entre capas que se asumen independientes**, y ademas **revisar si la confianza en las multiples defensas genero complacencia**, que es el reverso del *disenar redundancia entre capas* del `_2`. **Misma fuente**, Reason, *Managing the Risks of Organizational Accidents* | **INTRA: defecto de instruccion** | falta la **condicion de orden**: la evaluacion por capa separada solo es valida **despues** de haber descartado las dependencias ocultas, y **ninguno de los dos lo dice**. **No hay tercer nodo del catalogo que lo resuelva**: `defensas_en_profundidad` aporta las siete funciones y `modelo_barreras_defensas` la prueba de papel contra realidad, pero **ninguno ordena los dos pasos**. **Hay que ir al original.** Leido **A** en el 2.283, con `defensas_en_profundidad_3` como superviviente: **la contradiccion no decidio la clase** (1632), la decidio la vara, **y la coincidencia de que el que corrige sea tambien el que sobrevive es eso, una coincidencia, no un criterio** |

### COMO SE USA

> **INTRA-FUENTE**: se busca la condicion o el umbral que falta **primero dentro
> del catalogo** (otro nodo de la misma familia suele tenerlo) y, si no aparece,
> **se verifica contra el documento original**. Es trabajo de extraccion, no de
> cribado, y **no cambia ninguna clase**.
>
> **INTER-FUENTE**: se anota como **frontera candidata** y se lleva a la mesa del
> dominio. **Tampoco cambia la clase.** Lo que decide es si el catalogo quiere
> conservar las dos doctrinas con su contexto al lado, o elegir una.


---

## ADVERTENCIA DE DISENO PARA LA ADUANA: el vocabulario no discrimina (18 ago 2026)

**VIAJA AL RECOMPUTO. La sesion del plan la recoge; el cribado solo la mide y la
entrega.**

> **LA ADUANA NO PUEDE APOYARSE EN VOCABULARIO PARA DECIDIR SI DOS NODOS DICEN LO MISMO.**

**LA MEDICION, del barrido de direccion (informe §76.3).** Se implemento una prueba de
cobertura lexica sobre los 46 pares del archivo cuya A **elige direccion**: que fraccion
de los pasos del nodo que muere aparece, por vocabulario, dentro del que sobrevive.

| | |
|---|---:|
| pares medidos | **46** |
| marcados **SOSPECHOSO** por la prueba | **34** |
| de esos, **realmente al reves** | **1** |
| **precision** | **3%** |

**POR QUE FALLA, y no es un defecto del umbral.** Este catalogo **repite ideas con
palabras distintas**. Dos ejemplos medidos, los dos del mismo racimo y los dos siendo
**el mismo paso**:

| un nodo dice | el otro dice | palabras en comun |
|---|---|---:|
| *historial de pequenos cambios y ajustes acumulados en procedimientos operativos* | *brecha entre procedimiento escrito y practica real* | **1** (procedimiento) |
| *el desempeno puntual se ha vuelto la norma a costa de margenes de seguridad* | *metas de eficiencia local que compiten con la seguridad* | **1** (seguridad) |

**Subir el umbral no arregla nada**: bajarlo mete ruido y subirlo pierde estos casos, que
son **la mayoria del corpus doctrinal**.

### LO QUE ESTO EXIGE DEL DISENO

1. **El indice semantico de la aduana necesita la prueba que el script ya define**, no el
   solape de palabras: **que fraccion de los PASOS de un nodo esta EJECUTADA por el otro**,
   medida sobre significado y no sobre forma. `scripts/barrido_direccion.py` deja la
   funcion `cobertura()` escrita con su umbral y **con su tasa de acierto en la cabecera**,
   para que se reemplace el comparador y se conserve la forma de la prueba.
2. **La aduana tiene que poder distinguir POSTURA de PASO DE TRABAJO.** Es la leccion del
   puesto 2.371: *aceptar que el error es inevitable* y *ir a buscar que decidio la
   empresa antes del incidente* comparten casi todo el vocabulario y **no son lo mismo**.
   Un indice que no separe las dos cosas fundira politicas con protocolos.
3. **Y tiene que poder distinguir LA CASA DEL EJEMPLO** (figura EL CASO NO ES LA CASA,
   informe §78.3). La senal es barata y **no esta en los pasos, esta en el entregable**:
   si el entregable **lleva dentro un dato del caso** (una fecha, un lugar, una empresa),
   el nodo es ilustracion. **Hay 10 nodos con id `caso_`, `estudio_`, `case_` o
   `ejemplo_` en el grafo y 8 sin cribar todavia.**

> **EL RESUMEN EN UNA LINEA: la deduplicacion de este catalogo se verifica leyendo. Lo
> que la maquina puede hacer es ORDENAR LA COLA, que es lo que ya hace, y NO decidir el
> veredicto.**
