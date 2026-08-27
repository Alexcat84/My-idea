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
| ~~**`voz_del_cliente_voc`**~~ | ~~**3**~~ **0** | ~~724, 755, 827~~ **LIBERADOS EL 15 ago 2026 por la fusion de `OP-D-02`: los tres a `D`** |
| ~~**`producto_minimo_viable`**~~ | ~~**2**~~ | ~~592, 830~~ **LIBERADOS EL 15 ago 2026: ver la correccion declarada al final de esta seccion** |
| `lienzo_modelo_negocio` | 1 | 784 |
| ~~`ab_testing_optimizacion` + `split_testing_experimentos_ab`~~ | ~~1~~ | ~~738~~ **LIBERADO EL 15 ago 2026 (vuelta 34): el 738 paso de `B` a `D` tras el destejido de `ab_testing_optimizacion`, y con el se volteo tambien el `1061`, de `A` a `D`** |
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
| **CONGELADOS** | el **veredicto depende** de qué quede tras la cirugía | ~~**13**~~ ~~**10**~~ ~~**7**~~ **6** | ~~592,~~ 599, ~~724,~~ ~~738,~~ ~~755,~~ 784, 798, ~~827,~~ ~~830,~~ 831, 835, 851, ~~**494**~~ |
| **EN COLA** | el texto va a cambiar, se relee igual | ~~**19**~~ ~~**16**~~ ~~**13**~~ ~~**12**~~ **11** | los ~~trece~~ ~~diez~~ ~~siete~~ **seis** de arriba **más 361, ~~374,~~ 386, 392, 492 y 915** |

> **CORRECCION DECLARADA (15 ago 2026, vuelta 33 del bucle). TRES CONGELADOS SALEN DE LA LISTA, y
> las cifras viejas se quedan tachadas y no borradas.** El destejido de `producto_minimo_viable`
> (`OP-D-01` movimiento 1, vuelta 32: de 22 pasos a **6** y de 10 condiciones a **5**) **tumbo la
> causa de los tres**, y el volteo se ejecuto el 15 ago 2026 por el banco `9.10` con la
> adjudicacion del fundador:
>
> | puesto | contra que nodo | antes | ahora | arreglo que queda |
> |---:|---|:---:|:---:|---|
> | **494** | `principio_calidad_mvp` | **A** | **C** | **ENLACE MUTUO, dos aristas** (banco `9.22`, tercer ejemplar), **sin poner**: es fase 04 |
> | **592** | `mvp_catalogo_tecnicas` | **B** | **D** | **ARISTA QUE FALTA** hacia `mvp_catalogo_tecnicas`, sin poner |
> | **830** | `prueba_mvp_alta_fidelidad` | **B** | **D** | **ARISTA QUE FALTA** hacia `prueba_mvp_alta_fidelidad`, sin poner |
>
> **`producto_minimo_viable` sale entero del orden de la cirugia: no le queda ningun par
> congelado.** Los que siguen congelados por `voz_del_cliente_voc` (**724**, **755**, **827**)
> **no se mueven aqui**, y su suerte se decide en `OP-D-02`.
>
> **La cuenta EN COLA baja de 19 a 16 por los mismos tres**, y es aritmetica de la propia tabla
> (10 congelados mas los 6 de cola sin congelar). Y se dice lo que esta correccion **no** hace:
> **no toca el `851` ni el `835`**, que dependen de otras cirugias.
>
> **DISCREPANCIA DECLARADA Y NO RESUELTA COPIANDO, y es previa a esta vuelta:** el parrafo de la
> *Actualizacion del 13 ago 2026*, dos lineas mas abajo, **ya decia `Cola a 16`** cuando la tabla
> de arriba decia **19**. Que mi correccion aterrice tambien en 16 **es una coincidencia
> aritmetica, no una confirmacion**: las dos cifras cuentan cosas distintas y ninguna de las dos
> se recomputo hoy. **Queda anotado para quien audite; no lo arreglo yo, porque arreglarlo pide
> recontar la cola y eso es trabajo de la fase I, cerrada.**

> **SEGUNDA CORRECCION DECLARADA (18 ago 2026, vuelta 36): EL 374 SALE DE LA COLA, Y NO POR UNA
> CIRUGIA NUEVA SINO PORQUE YA SE RELEYO.** La cola dice *el texto va a cambiar, se relee igual*, y
> el texto del **374** ya cambio (`split_testing_experimentos_ab` paso de nueve pasos a cinco con
> `OP-F-04-RAC`) **y el par ya se releyo contra el texto de hoy** por `P.5`, dentro del acto de
> `OP-D-03`: **paso de `A` a `D`** el 18 ago 2026, con la razon vieja entera dentro de la nueva
> (`docs/loop/_lote_v36.jsonl`, marcador recomputado `n 3.388, A 576, B 83, C 8, D 2.721` en
> `docs/loop/SALIDA_V36_MARCADOR.txt`). **La cuenta EN COLA baja de 12 a 11 por ese solo par**, y
> es aritmetica de la propia tabla: los **seis** congelados mas los **cinco** de cola sin congelar
> que quedan (361, 386, 392, 492 y 915).
> 
> **LO QUE ESTA CORRECCION NO HACE, y va dicho:** los otros cuatro pares que `P.5` volteo el mismo
> dia (**277**, **452**, **1571** y **1575**) **no estaban en esta cola**, asi que la cuenta no
> baja por ellos. **Y la fila CONGELADOS no se mueve**: ninguno de los cinco estaba congelado.
> 
> **DISCREPANCIA QUE ESTA CORRECCION HEREDA Y NO TAPA:** el parrafo de la *Actualizacion del 13
> ago 2026* de mas abajo sigue nombrando al **374** entre *los TRES que estan en cola sin
> congelar*, y esa prosa es de su corte y no se reescribe. **La cuenta viva es la de la tabla.**

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

> **CORRECCION DECLARADA (26 ago 2026, vuelta 76, adjudicada por el auditor,
> acta de la vuelta 75 seccion 4.1).** *"El control los encuentra todos de una
> vez"* es FALSA y esta medida como falsa: el control cubre los racimos
> **censados en `docs/RACIMOS_MIEMBROS.jsonl`** (32 racimos, reconstruidos por
> el commit `d4d2652f` de las razones de `FRANJA_VEREDICTOS.jsonl`), o sea los
> racimos que el CRIBADO declaro. Un racimo del INFORME que nunca paso por
> franja, como *el lienzo de propuesta de valor* (seccion 14 del informe,
> remedido a SIETE miembros por cierre transitivo), **no esta en ese universo
> por construccion, no porque el control lo perdiera.** Las dos fuentes son
> distintas por construccion. Los tres ejemplares de la tabla de arriba ya
> estan resueltos: `value_stream_mapping_ambiental` y `analisis_flujo_de_valor`
> por la segunda salida (su racimo *Mapeo del flujo de valor* tiene
> `dominio_censado` literal `quality + environmental + nucleo`, que ES la
> declaracion transversal explicita); `desarrollo_value_proposition_usp` por
> la primera salida, la nomina se depura (informe seccion 33.2: *"CAE, y ni
> siquiera es del dominio... CERO SOLAPE"*, y 33.3 lo llama *"defecto de
> NOMINA, no de lectura"*). El texto viejo de arriba no se toca.

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
| **494** | `principio_calidad_mvp` | ~~**A**~~ **C** |
| **592** | `mvp_catalogo_tecnicas` | ~~B~~ **D** |
| **830** | `prueba_mvp_alta_fidelidad` | ~~B~~ **D** |

> **CORRECCION DECLARADA (15 ago 2026, vuelta 33): LA COLUMNA DECIA *clase hoy* Y HABIA DEJADO DE
> SER HOY.** Las tres clases se voltearon por el banco `9.10` tras el destejido, y **el encabezado
> `(22 pasos)` de esta seccion tambien envejecio: el nodo tiene SEIS pasos desde el 15 ago 2026**.
> La cabecera vieja se deja escrita porque describe el estado que motivo el orden de la cirugia.
> **El orden interno que este bloque prescribia se cumplio tal cual**: se destejio
> `producto_minimo_viable`, se midio que `principio_calidad_mvp` ya no tenia costura que destejer,
> y **solo entonces** se releyeron el 494, el 592 y el 830.

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
| **738** | `split_testing_experimentos_ab` | ~~B~~ **D** (15 ago 2026, vuelta 34) |
| **1061** | `optimizacion_embudo_get_customers` | ~~**A**~~ **D** (15 ago 2026, vuelta 34) |

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
| **2393** | `limitaciones_ltif_indicador`, de Reason, manda **implementar reporte y seguimiento de EVENTOS PRECURSORES, casi accidentes, fugas y fallas de equipo**, es decir que **el menor anuncia al grave**; `no_usar_triangulo_heinrich`, de Dekker, manda **investigar los incidentes menores y los accidentes graves como fenomenos con CAUSAS POTENCIALMENTE DISTINTAS** y **no asumir que la ausencia de menores garantiza ausencia de riesgo mayor**. **Fuentes distintas** | **INTER: frontera candidata** | **DOS DOCTRINAS LEGITIMAS Y OPUESTAS SOBRE EL MISMO DATO.** No es defecto de instruccion: ninguna de las dos omitio una condicion, **discrepan sobre si la frecuencia de lo menor predice lo grave**. Se anota y **NO se repone nada**. Leido **D** en el 2.393: la contradiccion no decide la clase (1632), y cada uno trae procedimiento propio, el reemplazo del LTIF por metricas de integridad de proceso en uno, el desacople causal en el otro. **QUEDA ESCRITA PARA QUE NINGUNA FUSION FUTURA LA BORRE**: si el racimo de la medicion se funde, el superviviente **tiene que conservar las dos posiciones con su contexto al lado**, no elegir una en silencio |
| **2473** | `economia_de_la_inspeccion`, de Juran, **se titula REGLA DE DEMING kp** y en su paso 5 ofrece elegir entre **ninguna inspeccion, MUESTREO o cien por ciento**; `punto_equilibrio_calidad_inspeccion`, de Deming, manda en su paso 5 **EVITAR LOS PLANES DE MUESTREO INTERMEDIOS** cuando p esta consistentemente de un lado del punto de equilibrio. **Fuentes distintas, y una de ellas CITA A LA OTRA** | **INTER: frontera candidata, con agravante de ATRIBUCION** | **No es una frontera normal: un nodo atribuye la regla a un autor y le anade una opcion que ese autor descarta.** Leido **A** en el 2.473 y la contradiccion **no decide la clase** (1632); sobrevive el de Deming por la vara. **ADJUDICADO: si algun dia se funden, el anadido del muestreo SE MARCA COMO AJENO AL AUTOR**, con la etiqueta *variante no atribuible a Deming*. **Una atribucion es una afirmacion de fuente y se verifica**: un lector no puede salir creyendo que Deming admite lo que Deming prohibe |
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

### AÑADIDO PARA LAS OPERACIONES DEL PLAN: EL CONTROL DE DENOMINACION VA DENTRO DE CADA FUSION (18 ago 2026)

**Adjudicado y escrito en el banco 9.28.** La cifra de perdidas de nombre que publica el
barrido **es una COTA INFERIOR**: su lista de marcadores es curada y **esta incompleta por
construccion**. Lo probo el puesto **2.477**, donde muere el nodo titulado *Critica a la
Gestion por Objetivos* y **el superviviente no nombra MBO**, sin que el barrido lo detectara.

> **PASO OBLIGATORIO AL ESCRIBIR CADA OPERACION DE FUSION:** comprobar si **algun id o
> titulo que muere lleva una denominacion buscable ausente del texto del superviviente**.
> Si la lleva, **la denominacion viaja como linea** al superviviente.

| | |
|---|---|
| `scripts/barrido_perdida_de_nombre.py` | **buscador de candidatos**, adelanta trabajo. **NO es censo** |
| **la operacion de fusion** | **el control real**: dos textos delante, sin lista de por medio |

**PRECISION DEL 18 ago 2026, del puesto 2.488: EL ACRONIMO ES DENOMINACION APARTE.** Quien
busca **MBO** no escribe *Gestion por Objetivos*. **El control de denominacion busca
tambien las siglas**, y cuando la sigla muere **viaja entre parentesis** en el titulo o en
la primera frase del superviviente. **Denominaciones a reponer al dia: Amalberti (2.250),
Taguchi (2.432) y MBO (2.488).**

**No hay ruta nueva:** el paso se hace **dentro de las operaciones que el plan ya tiene**,
al redactarlas, junto al reparto de perdidas.

---

## LOS TRECE RACIMOS DE IDS DE `health_safety`, para el recomputo (18 ago 2026)

**VIAJA AL RECOMPUTO.** El dominio esta **cerrado** (192 pares, 45 A, **23,4%**), y con el
cierre queda medido lo que el plan tiene que decidir. **Tabla completa con miembros,
cobertura y aristas: informe intra §80.4.** Reproducible con
`python scripts/racimos_health_safety.py`, de solo lectura.

| | |
|---|---:|
| racimos | **13** |
| miembros nominales | **74** (68 nodos distintos: `enfoque_situacional_vs_personal` esta en dos) |
| pares posibles dentro de los racimos | **194** |
| **leidos por la cola** | **74 (38%)**, con 29 A |
| **SIN LEER** | **120** |
| aristas ya puestas entre miembros | **20** |

> **LOS 120 PARES SIN LEER NO VUELVEN POR LA COLA.** El dominio esta cerrado: **se leen si
> el plan los encarga como lectura dirigida, o no se leen.** Esa es la decision, y la
> cifra para tomarla es esta.

---

## ANEXO: LOS 55 PARES EN A QUE YA TIENEN LA ARISTA PUESTA (18 ago 2026)

**VIAJA AL RECOMPUTO.** Son las A **donde el grafo ya habia cableado a los dos nodos** y
aun asi repiten. **Una de cada nueve A del archivo** (55 de 473).

> **QUE PASA AL FUNDIRLAS, adjudicado:** la arista interna **resuelve al superviviente por
> alias** y nace **AUTO-ARISTA**, el mismo mecanismo de las 27 del grafo vivo (informe
> §31.3). **No es trabajo manual: es carga de `OP-S-12`** (saneo mecanico) **con su guarda
> `OP-C-05`**, y **la simulacion P.7 lo reporta antes** de que la operacion se escriba
> lista.

| dominio | pares | los puestos |
|---|---:|---|
| **`core`** | **42** | 188, 194, 212, 237, 244, 261, 265, 282, 292, 302, 307, 325, 326, 334, 345, 361, 376, 378, 381, 404, 462, 508, 541, 544, 559, 562, 570, 609, 614, 635, 712, 782, 893, 1028, 1031, 1109, 1142, 1146, 1332, 1488, 1517, 1564 |
| `exportacion` | 4 | 1943, 1966, 1981, 2022 |
| `environmental` | 3 | 1792, 1865, 1917 |
| `health_safety` | 3 | 2255, 2303, 2309 |
| `quality` | 3 | 2420, 2432, 2458 |
| **TOTAL** | **55** | |

**Recomputable con el mismo criterio en cualquier momento:** una A cuenta aqui si
`res(nodo_b)` esta en los vecinos de `nodo_a` o al reves, **resolviendo alias**.

> **LO QUE ESTA LISTA SIGNIFICA, y no es lo obvio.** Un cable entre dos nodos **dice que
> alguien vio la relacion**; **no dice que hagan cosas distintas**. Es **la simetrica de la
> ARISTA QUE FALTA**: alli el grafo **no vio** una jerarquia real, aqui **vio un parentesco
> y lo cableo en vez de fundirlo.** **El 88% de las A no tienen ese cable**, asi que la
> mayoria de las fusiones no tocan el grafo; **estas 55 si, y por eso van contadas.**

**LO QUE LA TABLA DEL §80.4 DECIDE POR ADELANTADO:**

- **DOS racimos cerrados**, y los dos pequenos: **la deriva** (6 de 6 leidos, 3 A y 3 D) y
  **la gestion del error** (3 de 3, cero A). **Ahi la lectura ya no puede cambiar nada.**
- **EL ERROR COMO SINTOMA es el grande y el mas caro**: 9 miembros, **11 A sobre 14 pares
  leidos**, 39% de cobertura, y contiene al iman (`errores_como_consecuencia`, nueve A y
  tres D). **Con 22 pares sin leer, su forma final no esta fijada.**
- **CINCO racimos sin un solo cable interno** (la vieja y la nueva vision, la gestion del
  error, la medicion que corrompe, la cultura coordinadora, el aprendizaje
  organizacional). **Es la cosecha de enlace mas barata del dominio.**
- **La cobertura es baja donde hay mas aristas**: el error de mantenimiento va al 19% con
  **6 aristas**; la medicion que corrompe al 19% con **0**. **Donde hay aristas, el grafo
  ya resolvio parte del racimo.**

## BACKLOG POST-CAMPAÑA (decision del fundador, 14 ago 2026)

**Nacida de la parada de la fase 01 sobre `OP-S-07`/`OP-C-04`.** Las dos preguntas de
codigo que la parada trajo **no bloquean nada del plan**: ninguna operacion las ordena,
asi que se deciden DESPUES del merge, no dentro de la pasada.

| pregunta | recomendacion que viaja con ella |
|---|---|
| **el resolutor unico** | hoy hay TRES implementaciones (el `resolverId` de `graph.ts` en el motor, la guarda de Gate 0, y el instrumento del ejecutor). Una sola fuente en Python para los scripts, la guarda importable desde ahi, y un test de paridad contra el `TypeScript` para que las tres no puedan divergir sin que algo se caiga |
| **la guarda de gemelos dentro del Gate** | hoy el chequeo de gemelos no ve la divergencia que una operacion recien creo, porque compara contra el snapshot de antes del paso 6; hoy la caza la suite del motor, no el Gate. Meterla dentro del Gate es codigo nuevo |

> **CODIGO QUE NINGUNA OPERACION ORDENA: SE DECIDE TRAS EL MERGE.** Las dos quedan
> anotadas aqui para no perderlas, no para resolverlas ahora. La tercera pregunta de la
> misma parada (estado `ejecutada` para las operaciones del plan) **NO entra en este
> backlog: se decidio SIN estado nuevo**, el estado de verdad sigue siendo el repo y el
> commit por operacion es su registro de ejecucion.

## CANDIDATOS DE UNA PASADA POSTERIOR DE `OP-E-06`: LOS PUESTOS 581 Y 650 (adjudicacion 4.3 del acta de la vuelta 89)

**Los dos quedan FUERA de la bolsa V90** (`docs/plan/OP_E_06_REBASE_V90.jsonl`), y la
exclusion se declara con su motivo real: **se caen por como quedo cosechada su frase, no
por su contenido.**

| puesto | par | por que cae de `OP-E-06` (letra de la verificacion: "si una razon no lo dice, el par NO entra") |
|---:|---|---|
| **581** | `cumplimiento_magnuson_moss -> prohibicion_tie_in_sales` | la frase es un argumento METODOLOGICO citando el banco 9 (si la madre sabe enlazar a otros hijos, la falta es omision de grafo), y no dice que ninguno de los dos nodos desarrolle contenido del otro |
| **650** | (misma familia de `cumplimiento_magnuson_moss`) | su frase habla de que `prohibicion_tie_in_sales` es uno de los DOS que la madre no enlaza, aunque enlaza a tres de cinco: mismo argumento de familia, sin contenido propio del par |

> **LO QUE LA EXCLUSION CUESTA, medido por el auditor (acta 89, seccion 2.2):** por
> contenido, el par 581 es **tan canonico como el 530** (que si entro por 4.1): la madre
> `cumplimiento_magnuson_moss` tiene un paso, en una linea, que es exactamente la
> prohibicion de tie-in, y el grafo de hoy no la enlaza a `prohibicion_tie_in_sales`. La
> arista real probablemente existe; lo que falta es una LECTURA NUEVA del par, no de la
> frase ya cosechada, que declare el contenido y no solo el argumento de familia.

**RECOMENDACION QUE VIAJA CON ELLA:** una pasada posterior, fuera de `OP-E-06`, que relea
a mano los pares `cumplimiento_magnuson_moss -> prohibicion_tie_in_sales` (581) y su
hermano de familia (650) por CONTENIDO (no por frase cosechada), con el mismo criterio de
`OP-E-06` ("la frase dice quien desarrolla a quien"). **No bloquea nada de la fase 04**:
ninguna operacion vigente depende de estos dos puestos.

## TRES PARES DE LA BOLSA V90 SON ENLACE MUTUO (banco 9.22), NO ESCALERA: EXCLUIDOS DE `OP-E-06` (TAREA 4 de la vuelta 90)

Al leer la direccion de las 117 filas de `docs/plan/OP_E_06_REBASE_V90.jsonl` sobre el
campo `razon` completo de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (no sobre la `frase`
truncada a 200 caracteres de la cosecha), TRES citan LITERALMENTE "banco 9.22" con la
formula "CONTINUA en los dos sentidos": la doctrina del ENLACE MUTUO
(`docs/plan/04_ENLACES.md`, seccion "LAS CINCO C TAMBIEN SON DE ESTA FASE"), no la
escalera de una sola direccion que `OP-E-06` exige por su propia `verificacion` ("UNA
SOLA DIRECCION por arista, de la madre al hijo").

| puesto | par | razon (cita literal) |
|---:|---|---|
| **2082** | `preparar_candidato_validacion <-> validacion_con_franquiciados` | "Por la vara del banco 9.6.1, CONTINUA en los dos sentidos, banco 9.22: uno trae el trabajo con la red, el otro trae el entrenamiento del que pregunta." |
| **2084** | `control_responsabilidad_manual <-> gestion_responsabilidad_vicaria` | "Por la vara del banco 9.6.1, CONTINUA en los dos sentidos, banco 9.22: uno defiende con seguros y letreros, el otro defiende con la eleccion de las palabras." |
| **2112** | `capitalizacion_adecuada_del_franquiciador <-> estimacion_inversion_inicial_franquiciador` | "Por eso CONTINUA en los dos sentidos, banco 9.22." |

**QUEDAN FUERA de la bolsa escrita por `OP-E-06` en la vuelta 90** (114 de las 117 filas de
V90 se escriben; estas tres no). Forzar una sola direccion sobre un par que su propia
razon declara mutuo seria leer solo la mitad de la evidencia.

**RECOMENDACION QUE VIAJA CON ELLA (texto original de la vuelta 90, NO se borra, ver
correccion aditiva abajo):** los tres van a una operacion de ENLACE MUTUO (DOS ARISTAS
cada uno, como la seccion "LAS CINCO C" de `docs/plan/04_ENLACES.md` ya trata los pares
del banco 9.22), no a `OP-E-06`. **No bloquea nada de la fase 04.**

### CORRECCION ADITIVA (vuelta 91, TAREA 1): LA EXCLUSION DE `OP-E-06` SE RATIFICA; LA ETIQUETA "ENLACE MUTUO" NO SOSTIENE LA RELECTURA DIRIGIDA

**Origen:** acta de la vuelta 90 (`docs/loop/ACTA_AUDITOR.md`, adjudicacion 4.1, lineas
30788 a 30811), que mide los tres en clase **D** (no C) en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (linea 30626), los cinco enlaces mutuos vigentes
(201, 215, 494, 1077, 1240) en clase **C** (linea 30627), y el banco `9.22`
(`docs/BANCO_DE_TEXTOS.md` linea 2523) mandando *"el par es sano y se registra C, sano
con figura, no D"* (acta linea 30628). Ordena una **relectura dirigida contra el test de
las dos lineas del 9.22** antes de tocar la recomendacion (`docs/loop/PROMPT_SIGUIENTE.md`,
encargo de la vuelta 91, TAREA 1).

**LA RELECTURA DIRIGIDA, hecha en esta vuelta sobre el campo `razon` COMPLETO de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (no la frase truncada):**

**El test que exige el banco** (`docs/BANCO_DE_TEXTOS.md` linea 2539 a 2541): *"la
figura exige DOS LINEAS DISTINTAS, una en cada nodo"*, y solo cuando la vara da
**PROCEDIMIENTO en los dos sentidos sobre dos lineas distintas** es clase **C**
(tabla de la linea 2577 a 2580); si lo que hay es la formula **"cada uno trae lo
suyo"**, ese es el criterio de la **D**, fijado por el contraste del puesto **2091**
(banco linea 2594 a 2602, tambien clase D preguntando en los dos sentidos).

| puesto | linea EXPLICITA nombrada ("en UNA LINEA") en la razon | como justifica la razon el segundo sentido | sostiene el test de las dos lineas |
|---:|---|---|---|
| **2082** | UNA sola: paso de `validacion_con_franquiciados` (*"dice en UNA LINEA preparar al candidato explicandole que encontrara respuestas variadas"*) | *"uno trae el trabajo con la red, el otro trae el entrenamiento del que pregunta"*: formula de reparto, no una segunda linea nombrada con su paso | **NO** |
| **2084** | UNA sola: paso 2 de `gestion_responsabilidad_vicaria` (*"redactar el manual y el contrato diferenciando estandares de marca de aspectos operativos"*) | *"uno defiende con seguros y letreros, el otro defiende con la eleccion de las palabras"*: misma formula de reparto | **NO** |
| **2112** | UNA sola: paso 1 de `capitalizacion_adecuada_del_franquiciador` (*"estimar el presupuesto para desarrollar el sistema"*) | *"trae lo suyo, que es la pregunta que el otro no se hace"*: la formula LITERAL de la D | **NO** |

**VEREDICTO DE LA RELECTURA DIRIGIDA: NO SOSTIENE, los tres.** Cada razon nombra
**una sola linea explicita con su paso** (en un solo nodo del par) y justifica el
"segundo sentido" con la formula de reparto que el acta de la vuelta 90 nombra como la
de la D (*"cada uno trae lo suyo"*, `docs/loop/ACTA_AUDITOR.md` linea 30631), la misma
que el contraste del puesto 2091 deja fijada (`docs/BANCO_DE_TEXTOS.md` linea 2594 a
2602, tambien D preguntando en los dos sentidos), no con una segunda linea identificada
con su paso en el otro nodo. **La cita literal de "banco 9.22" en las tres razones es
cierta** (el ejecutor no la invento), **pero citar la doctrina no es lo mismo que
cumplir su test**, y el test es el que decide la clase.

**CONSECUENCIA, aplicando la regla del propio encargo ("si no sostiene, vuelven como
escalera de una sola direccion por la linea que su razon ya nombra"), leyendo la
direccion con la MISMA vara de `scripts/loop/vuelta90_tarea4_direccion_ope06.py`
("el que dice EN UNA LINEA es la MADRE; el que trae el procedimiento de esa linea es
el HIJO; arista MADRE -> HIJO"):**

| puesto | direccion (madre -> hijo), leida de la unica linea que la razon nombra |
|---:|---|
| **2082** | `validacion_con_franquiciados` -> `preparar_candidato_validacion` |
| **2084** | `gestion_responsabilidad_vicaria` -> `control_responsabilidad_manual` |
| **2112** | `capitalizacion_adecuada_del_franquiciador` -> `estimacion_inversion_inicial_franquiciador` |

**LA EXCLUSION DE `OP-E-06` NO SE TOCA: sigue siendo correcta** (ya ejecutada y
cerrada en la vuelta 90; esta correccion no reabre `OP-E-06` ni escribe aristas).
**LO QUE SE CORRIGE ES LA RECOMENDACION** de arriba: los tres **NO** son candidatos de
una operacion de ENLACE MUTUO de dos aristas cada uno. Son candidatos de **escalera de
una sola direccion**, por la direccion de la tabla de encima, en una pasada posterior
fuera de `OP-E-06` (la misma familia de pasada que los puestos 581 y 650 de mas arriba
en este documento). **No bloquea nada de la fase 04.**

## EL PUESTO 1098 DE `OP-E-07` TENIA UNA ARISTA QUE SU PROPIA RAZON PROHIBE: CORREGIDO (vuelta 92)

**Origen:** acta de la vuelta 91 (`docs/loop/ACTA_AUDITOR.md`, seccion 3.1, lineas 31290
a 31365, y adjudicacion 5.1, lineas 31438 a 31447). Es una CAIDA DE CLASE (mueve dato),
la unica de la tanda, encontrada por el auditor con un barrido propio que buscaba
formulas que NIEGAN la jerarquia (`no crea jerarquia`, `ninguno la expande`, `sin
jerarquia`) sobre las 88 razones de `OP-E-07`, y confirmada por el ejemplar ya
registrado del banco.

**LA FRASE, LITERAL, del campo `razon` de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, puesto
1098** (`customer_validation_sell_phase` contra `prueba_solucion_con_cliente`, clase D,
core; citada en `ACTA_AUDITOR.md` linea 31298 a 31304):

> "Queda anotada UNA LINEA COMPARTIDA que no crea jerarquia porque ninguno la expande:
> los dos preguntan como es el proceso interno de aprobacion de compra, y los dos lo
> dicen en un solo paso."

**QUE PASO, mecanicamente** (`ACTA_AUDITOR.md` linea 31311 a 31317): el criterio de
`extraer_direccion_automatica` leyo la palabra "trae" de la otra mitad de la razon
("prueba_solucion_con_cliente trae un procedimiento de entrevista que el otro no tiene
en ninguna forma") y le puso direccion, cuando esa formula es la de la clase D ("cada
uno trae lo suyo"), no la de madre e hijo. El par entro con direccion
`customer_validation_sell_phase -> prueba_solucion_con_cliente` cuando su propia razon
manda que SALGA.

**LA COMPROBACION SOBRE LOS PASOS DE LOS DOS NODOS** (`ACTA_AUDITOR.md` linea 31319 a
31330): `customer_validation_sell_phase` toca la linea compartida en su **paso 4**
("Confirma como es el proceso real de compra y de aprobacion dentro del negocio de tu
cliente") y `prueba_solucion_con_cliente` en su **paso 5** ("Pregunta como es el proceso
interno de aprobacion de compra de quien te compra"). Un paso en cada lado, ninguno
expande al otro.

**EL TEST DEL BANCO `9.6.2` que decide** (`docs/BANCO_DE_TEXTOS.md`, seccion que abre en
linea 1737, test en lineas 1771 a 1774): *"El hijo cabe entero dentro de UN paso de la
madre, y la madre conserva materia propia que el hijo no toca en ningun paso"*. Los seis
pasos de `prueba_solucion_con_cliente` no caben dentro de ningun paso de
`customer_validation_sell_phase`: no hay madre e hijo.

**EL EJEMPLAR YA REGISTRADO que hace esto adjudicable y no doctrina nueva**
(`docs/BANCO_DE_TEXTOS.md`, tabla de lineas 1776 a 1782, fila del puesto **2.195**): el
mismo nodo `capitalizacion_adecuada_del_franquiciador` ya tiene un veredicto escrito con
las mismas palabras, *"no era madre e hijo: linea compartida y procedimiento propio a
cada lado"*. El 1098 es ese mismo caso.

**LO QUE MANDA LA OPERACION, literal, del campo `verificacion` de `OP-E-07` en**
`docs/plan/OPERACIONES.jsonl` (linea 69): *"Si la razon tampoco lo dice, el par sale de
la cosecha y se anota por que"*, y *"los que salgan se cuentan y se nombran: un
descarte silencioso aqui seria un enlace perdido"*. El 1098 tenia que SALIR y se conto
como ENTRADO: es el reverso de la regla, un enlace inventado en vez de uno perdido.

**LA CORRECCION, ejecutada en la vuelta 92 (TAREA 2 y TAREA 3 del encargo,
`docs/loop/PROMPT_SIGUIENTE.md`):** se construyo un guarda de dos condiciones para
`extraer_direccion_automatica` (marca de madre positiva Y ausencia de negacion de
jerarquia), el puesto 1098 salio de `OP_E_07_DIRECCION_V91.jsonl` (queda en 87), su
arista se retiro de `dataset/nodos/` en las dos vistas, y el `ADDENDUM DE EJECUCION` de
`OP-E-07` se reescribio con el corte nuevo (1 SALE, 85 ESCRITA, 2 YA_ESTABA, 0
ESCALERA_ROTA).

**LO QUE NO SE TOCA, y es explicito** (`ACTA_AUDITOR.md` linea 31363 a 31365): el
marcador no se toca (la clase D del 1098 es correcta, lo que no sostenia era la
DIRECCION), `OP-E-06` no se reabre (contraprueba corrida por el auditor sobre sus 114
direcciones, un solo toque, el puesto 1160, leido entero y CONFIRMADO,
`ACTA_AUDITOR.md` linea 31367 a 31386), y los otros 85 de `OP-E-07` se quedan.

## LA RELECTURA CONJUNTA DEL PUESTO 1009 DE `OP-E-07`: RESUELTA, EL PAR SALE (vuelta 93)

**Origen:** acta de la vuelta 92 (`docs/loop/ACTA_AUDITOR.md`, seccion 4, lineas 31977
a 32106): el auditor discrepo de SU PROPIA adjudicacion de la vuelta 91 sobre el
puesto 1009 y la mando a RELECTURA CONJUNTA (`docs/loop/AUDITOR.md` seccion 1.3), con
la decision reservada al ejecutor de la vuelta 93. Este apartado registra esa
decision, sin borrar nada de lo que sigue.

**(a) LA RELECTURA CONJUNTA, RESUELTA: EL PAR SALE.** `scripts/loop/
vuelta93_tarea2_relectura_1009.py` (salida completa en `docs/loop/
SALIDA_V93_TAREA2_RELECTURA_1009.txt`) leyo la razon completa del puesto 1009
(`customer_discovery_phase2_problem_test` contra `fit_problema_solucion`, clase D,
core) contra la UNICA pregunta que `OP-E-07.verificacion` manda (`docs/plan/
OPERACIONES.jsonl` linea 69): *"la razon nombra cual de los dos nodos es la madre, si
o no"*. La razon dice:

> "`customer_discovery_phase2_problem_test` **prueba el problema**: disenar
> experimentos con clientes reales, prepararse para los contactos y las entrevistas,
> probar la comprension del problema y su importancia percibida, profundizar en
> perfiles y comportamientos, y capturar conocimiento competitivo durante las
> entrevistas. `fit_problema_solucion` **trae un procedimiento QUE ESA FASE NO
> TIENE**: identificar en cual de las tres fases esta el negocio, enviar en la fase I
> un flujo pequeno y constante de clientes frios por canales de traccion..., y no
> escalar la inversion en marketing hasta que la fuga sea baja. Por la vara del banco
> 9.6.1, CONTINUA. Y por el banco 9.9 se juzga hoy: el solape cae en sus tres primeros
> pasos, los encajes de Value Proposition Design, y **el bloque de traccion queda
> fuera**."

**CONTRASTE CONTRA LA VARA, los dos ejemplares ya adjudicados y escritos**
(`ACTA_AUDITOR.md` seccion 4.1, lineas 32026 a 32036): el puesto **1083**
(CONFIRMADO por el acta 91) dice *"trae un procedimiento que **LA MADRE** no
tiene"*: nombra a la madre, literal. El puesto **1098** (que CAYO en la vuelta 92)
dice *"trae un procedimiento de entrevista que **el otro** no tiene en ninguna
forma"*: no nombra a nadie, solo se refiere al otro nodo. El 1009 dice *"trae un
procedimiento que **esa fase** no tiene"*: es la misma forma que el 1098, no la del
1083. Ademas, ninguna linea del 1009 esta nombrada con su paso (numero u ordinal):
*"prueba el problema:"* introduce los CINCO pasos enteros del nodo, no una linea.
Y la propia razon declara que el bloque de traccion del hijo escrito queda FUERA del
solape, lo que hace fallar el test del banco `9.6.2` (`BANCO_DE_TEXTOS.md` lineas
1771 a 1774: *"el hijo cabe entero dentro de UN paso de la madre"*).

**VEREDICTO: la razon del 1009 NO NOMBRA cual nodo es la madre.** Por
`OP-E-07.verificacion` ("si la razon tampoco lo dice, el par sale de la cosecha y se
anota por que"), **EL PAR SALE**, con el mismo tratamiento que el 1098 en la vuelta
92: sale de `docs/plan/OP_E_07_DIRECCION_V92.jsonl` (queda en 86,
`scripts/loop/vuelta93_tarea3a_filtrar_1009.py`), su arista
(`customer_discovery_phase2_problem_test -> fit_problema_solucion`) se retira de
`dataset/nodos/` en las dos vistas (`scripts/loop/vuelta93_tarea3b_retirar_1009.py`),
y el diff de la union del grafo contra el cierre de la vuelta 92
(`85a250bee2495f4a23d89a4cf51338a5bcd8397e`) da EXACTAMENTE una borrada y cero
nuevas (`docs/loop/SALIDA_V93_DIFF_UNION.txt`). El `ADDENDUM DE EJECUCION` de
`OP-E-07` se reescribio con el corte nuevo (84 ESCRITA, 2 YA_ESTABA, 0
ESCALERA_ROTA, `scripts/loop/vuelta93_tarea4_reescribir_addendum.py`). **EL MARCADOR
NO SE TOCA**: la clase D del 1009 es correcta y no se discute (mismo criterio que el
acta 91 aplico al 1098); lo que se discutia era la DIRECCION.

**(b) LOS DOS DEFECTOS MEDIDOS DEL GUARDA DE LA VUELTA 92, REPARADOS EN LA VUELTA
93** (`scripts/loop/vuelta93_tarea3_guarda_direccion.py`; medidos por el auditor,
`ACTA_AUDITOR.md` seccion 3.1 y 3.2, lineas 31896 a 31976; reproducidos y reparados
por el ejecutor, `docs/loop/SALIDA_V93_TAREA3_VARA.txt`):

- **EL FALSO SALE, 3,7% sobre un TERCER CONJUNTO de 81 razones** (los pares de
  `docs/plan/COSECHA_RAZONES_D.jsonl` con senales "formula de la vara" o
  "procedimiento de esa linea", menos los 202 puestos de las dos bolsas oficiales;
  reconstruido por codigo propio en la vuelta 93, `scripts/loop/
  vuelta93_tarea3_guarda_direccion.py --tercer-conjunto`, tambien **81 filas**, sin
  discrepancia con la cifra del auditor). Tumbaba 3 pares SANOS (puestos **995**,
  **1007**, **1024**) porque sus razones nombran la linea con una preposicion que el
  guarda de la vuelta 92 no traia ("termina CON UNA LINEA", "cierra CON UNA LINEA",
  "empieza CON UNA LINEA"), y el 995 ademas cierra con "el paso nombra, el hijo
  ejecuta", la marca de madre mas limpia del catalogo, que el guarda tampoco conocia.
  **REPARADO**: se anadieron esas cuatro formulas a `MARCA_MADRE_POSITIVA`, cada una
  citada con el puesto que la motivo, con la misma lookahead negativa que excluye
  "linea compartida". Probado por mutacion (`docs/loop/SALIDA_V93_TAREA3_MUTACION.txt`,
  casos 4 y 5).
- **EL FALSO PASA AL REVES**: la alternativa "prueba el problema" (anadida en la
  vuelta 92 citando SOLO el puesto 1009) hacia PASAR el 1009, el 1411 y el 1557 sin
  merecerlo: es el UNICO sosten de los tres, y su formula es la de la clase D, no la
  de madre e hijo (ver apartado (a) arriba). **REPARADO**: la alternativa se retiro
  de la lista. Verificado que el 1397 (la cuarta aparicion de "prueba el problema" en
  las 3.388 razones) sigue PASANDO por otra marca ("paso 4") y no se ve afectado.
- **LA VARA, LOS TRES CASOS OBLIGATORIOS, los tres en verde**
  (`docs/loop/SALIDA_V93_TAREA3_VARA.txt`, EXIT 0): sobre las 88 de
  `OP_E_07_REBASE_V91.jsonl`, SALEN exactamente `{1009, 1098}`; sobre las 114 de
  `OP_E_06_DIRECCION_V90.jsonl`, el 1160 sigue PASA y 0 SALEN (OP-E-06 no se reabre);
  sobre el tercer conjunto de 81, los tres falsos SALE conocidos PASAN y ningun otro
  sale.
- **CABLEADO POR DEFECTO** (discutible 3 del reporte de la vuelta 92, CONFIRMADO por
  el acta 92 seccion 2.3): `extraer_direccion_automatica`
  (`scripts/loop/vuelta91_tarea4_direccion_ope07.py`) ahora llama al guarda ELLA
  MISMA antes de devolver (TAREA 3.e de la vuelta 93); una llamada futura a esa
  funcion, directa o via `main()`, ya no puede saltarse el guarda sin querer
  (verificado en `docs/loop/SALIDA_V93_TAREA3E_VERIFICACION_CABLEADO.txt`: una
  corrida fresca sobre la bolsa de 88 excluye 1098 y 1009 automaticamente, sin
  filtro aparte).

**(c) "ES UN HABITO" (puesto 1281): INVERIFICABLE, se queda declarado como tal.**
Aparece **UNA SOLA VEZ** en las 3.388 razones de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
(medido por conteo directo en esta vuelta). No hay un segundo puesto contra el que
probar si la formula generaliza o falla como marca de madre positiva: **es
INVERIFICABLE CONTRA OTRO PAR**. Se queda en la lista de `MARCA_MADRE_POSITIVA` (no
hay evidencia de que falle, solo falta evidencia de que generalice), pero la
declaracion de que no se puede probar queda escrita aqui, no callada.

**(d) OBSERVACION PARA ALEXIS, NO ES TRABAJO DEL BUCLE: LA DERIVA DE CONTENIDO**
(medida por el auditor, `ACTA_AUDITOR.md` seccion 4.4, lineas 32077 a 32106). De los
140 nodos que tocan los 87 pares de `OP-E-07` (bolsa previa a esta vuelta), **26**
tienen hoy `pasos_accionables` distintos de los que tenian en el commit del
encendido del bucle (`50f03099`), y eso afecta a **32** de los 87 pares. El ejemplar
es el propio `fit_problema_solucion`: en `50f03099` tenia 6 pasos (3 encajes de Value
Proposition Design mas 3 de traccion); hoy tiene 3 (el bloque de traccion se fue en
`cadc9977`, vuelta 53, LOTE A). **NO SE TOCA**: `OP-E-07.verificacion` decide por
escrito que la fuente es la razon y NO el par ("NO SE RELEE EL PAR: se lee su razon,
que ya esta escrita"), asi que una medicion de hoy no revoca esa eleccion de carril.
Es una pregunta de ALCANCE (si la cola de relectura post fusion tiene que crecer) y
esa decision es RESERVA DE FUNDADOR, no del bucle.

## LAS DOS RELECTURAS CONJUNTAS DE LA VUELTA 91 (1281 y 1992): RESUELTAS, LOS DOS PARES SALEN (vuelta 94)

**Origen:** acta de la vuelta 93 (`docs/loop/ACTA_AUDITOR.md`, secciones 5.1 y 5.2),
DOS discrepancias PROPIAS del auditor sobre direcciones que el ejecutor de la vuelta
91 confirmo en el acta 91 "por adjudicar la bolsa por muestreo en vez de barrerla con
instrumento". Las dos van a RELECTURA CONJUNTA (`docs/loop/AUDITOR.md` seccion 1.3),
decision reservada al ejecutor de esta vuelta. Este apartado registra esa decision,
sin borrar nada de lo que sigue.

**(a1) EL 1281** (`get_visual -> pensamiento_visual_modelos_negocio`,
`scripts/loop/vuelta94_tarea3_relectura_1281_1992.py`, salida completa en
`docs/loop/SALIDA_V94_TAREA3_RELECTURA.txt`). La razon completa
(`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, puesto 1281) compara "el habito general
contra su aplicacion a un artefacto": `get_visual` **es un habito de taller**
(mantener notas adhesivas, dibujar sin preocuparse por la calidad, explicar los
dibujos, intentar dibujar lo que cuesta explicar); `pensamiento_visual_modelos_
negocio` aplica ese habito al modelo de negocio y ANADE una narrativa de
presentacion. La razon dice, textual: *"la narrativa y el orden de presentacion son
lo que **ningun habito general trae**"*.

Medido con comando propio (barrido del "trae" en el segmento del hijo, desde su
primera mencion): hay **UNA SOLA** aparicion de "trae" en toda la razon, y esta
**dentro de "ningun habito general trae"**. La lookbehind vieja de `MARCA_HIJO`
(`(?<!no )`) solo tapaba "no trae" pegado y dejaba pasar esta forma: la deteccion
automatica de la vuelta 91 la leyo como marca de hijo cuando dice EXACTAMENTE LO
CONTRARIO (que el habito general NO TIENE la narrativa, no que el hijo la traiga de
la madre). Contraste contra la vara: el 1009 (que SALIO en la vuelta 93) fallaba
porque su razon nunca nombraba una linea con su paso; el 1281 tiene el mismo
defecto, y ademas su unico sosten en el guarda automatico es "es un habito"
(declarada INVERIFICABLE en la vuelta 93, ver seccion de arriba: aparece UNA SOLA
vez en las 3.388 razones). Y la propia razon declara que el hijo tiene contenido
(la narrativa) que "ningun habito general" tiene, lo que falla el test del banco
`9.6.2` ("el hijo cabe entero dentro de UN paso de la madre").

**VEREDICTO: la razon del 1281 NO NOMBRA cual nodo es la madre. EL PAR SALE.**

**(a2) EL 1992** (`seleccion_de_metodo_de_pago -> metodos_pago_electronico_
internacional`, direccion `B_MADRE`, fijada por `DIRECCION_MANUAL` en la vuelta 91,
`scripts/loop/vuelta91_tarea4_direccion_ope07.py` lineas 126 a 128). La razon dice:
*"seleccion_de_metodo_de_pago compara los cinco por seguridad, costo y
competitividad, y cierra con el contrato escrito y la consulta al banco"*: ninguna
cita de paso ni de linea. Medido con comando propio contra sus dos hermanos de la
misma madre y misma fuente: **el 1991 y el 1993 SI traen** *"dice en su paso 3, en
UNA LINEA"* (verificado literal en las dos razones); **el 1992 no trae la formula**.
El redactor escribio el paso numerado dos veces para esta misma madre, y no la
tercera. Ademas, la direccion del 1992 nunca salio de la razon: salio de un
comentario del ejecutor de la vuelta 91 en `DIRECCION_MANUAL`
("la comparacion general de los cinco metodos es la madre, la infraestructura de
uno de ellos, el hijo"), y `OP-E-07.verificacion` exige leer LA RAZON, no un
comentario ("se lee su razon, que ya esta escrita").

**VEREDICTO: la razon del 1992 NO NOMBRA cual nodo es la madre. EL PAR SALE.**

**(a3) LA EJECUCION, sobre las dos:** el guarda filtro `OP_E_07_DIRECCION_V93.jsonl`
(86 filas) y saco EXACTAMENTE `{1281, 1992}`
(`scripts/loop/vuelta94_tarea3_relectura_1281_1992.py`), escribiendo
`docs/plan/OP_E_07_DIRECCION_V94.jsonl` (84 filas). Las dos aristas se retiraron de
`dataset/nodos/` en las dos vistas
(`scripts/loop/vuelta94_tarea3b_retirar_1281_1992.py`; idempotencia probada, segunda
corrida `NO_ESTABA` en las dos, sha256 identico antes y despues,
`docs/loop/_v94_sha_antes_idem.txt`). El ciclo de tres se corrio entero: Gate 0 OK,
censo IGUAL (3.853 / 3.188 / 665), motor 25/25, web 80/1030 mas 3 skipped, tsc
limpio, guarda de `OP-C-05` VERDE (935 entradas que sobran ANTES y DESPUES), y el
diff de la union del grafo contra el cierre de la vuelta 93 (`352b8529`) dio
EXACTAMENTE DOS borradas (los dos pares nombrados arriba) y CERO nuevas
(`docs/loop/SALIDA_V94_DIFF_UNION.txt`). El `ADDENDUM DE EJECUCION` de `OP-E-07` se
reescribio con el corte nuevo (82 ESCRITA, 2 YA_ESTABA, 0 ESCALERA_ROTA). **EL
MARCADOR NO SE TOCA**: la clase D de los dos puestos es correcta y no se discute; lo
que se discutia era la DIRECCION.

## EL DEFECTO MEDIDO DE `MARCA_HIJO`: LA LOOKBEHIND ANGOSTA, REPARADA (vuelta 94)

**El defecto** (medido primero por el acta de la vuelta 93 sobre el puesto 1281, ver
seccion de arriba): `MARCA_HIJO` en `scripts/loop/vuelta91_tarea4_direccion_ope07.py`
es `(?<!no )trae\b(?!\s+lo\s+suyo)|desarrolla|RECORRE\s+EL\s+CAMINO`. La lookbehind
`(?<!no )` solo tapa "no trae" PEGADO (las tres letras inmediatas), y Python `re` no
soporta lookbehind de longitud variable, asi que una negacion a mas de dos palabras
de distancia ("ningun ... trae", "nadie ... trae", "sin ... traer") se le cuela
entera.

**LA REPARACION** (`scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py`,
`marca_hijo_presente_v94`): en vez de un lookbehind, una VENTANA de negacion de 60
letras antes de cada "trae" encontrado, buscando "no", "ningun", "ninguna", "nadie",
"jamas" o "sin". Si alguna aparece en la ventana, ese "trae" NO cuenta como marca de
hijo. "desarrolla" y "RECORRE EL CAMINO" se dejan igual: el defecto medido es
especifico de "trae".

**LA PRUEBA DE QUE NO ROMPE NADA** (`docs/loop/SALIDA_V94_TAREA4_SIN_CAMBIO.txt`):
las 84 direcciones VIGENTES de `OP-E-07` (post relectura conjunta de arriba),
recalculadas con el guarda y `MARCA_HIJO` reparados, dan **CERO cambios**: ninguna de
las 84 direcciones ya escritas se mueve.

**EL CASO ROJO POR MUTACION** (`docs/loop/SALIDA_V94_TAREA4_MUTACION.txt`), sobre una
entrada REAL, no un literal disfrazado: el segmento del hijo del puesto 1281
(`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`), que contiene el UNICO "trae" negado por
"ningun" que motivo la reparacion. `marca_hijo_presente_v94` da `False` sobre la
entrada real (el "trae" esta negado) y `True` al mutarla quitando la palabra
"ningun": el criterio SI depende de su entrada.

**LAS TRES VARAS OBLIGATORIAS, las tres en verde**
(`docs/loop/SALIDA_V94_TAREA4_VARA.txt`): sobre las 88 de `OP_E_07_REBASE_V91.jsonl`,
el guarda automatico SALE exactamente `{1009, 1098}` (el 1281 y el 1992 salen de
`OP-E-07`, pero NO por este guarda: el 1281 sale porque, reparado `MARCA_HIJO`, su
unica marca de hijo queda negada y `extraer_direccion_automatica` lo deja AMBIGUA
[verificado en `docs/loop/SALIDA_V94_TAREA4E_VERIFICACION_CABLEADO.txt`: una corrida
fresca sobre la bolsa de 88, fuera de `DIRECCION_MANUAL`, deja `AMBIGUA` exactamente
`{1009, 1098, 1281}`]; el 1992 sale por relectura conjunta de un `DIRECCION_MANUAL`,
no por el guarda); sobre las 114 de `OP_E_06_DIRECCION_V90.jsonl`, el 1160 sigue PASA
y 0 SALEN (`OP-E-06` no se reabre); sobre el tercer conjunto de 81, los tres falsos
SALE conocidos (995, 1007, 1024) PASAN.

**CABLEADO POR DEFECTO**: `extraer_direccion_automatica`
(`scripts/loop/vuelta91_tarea4_direccion_ope07.py`) ahora importa `guarda_direccion_
v94` y `marca_hijo_presente_v94` (import perezoso, mismo patron que la vuelta 93); la
constante `MARCA_HIJO` vieja se deja escrita sin borrar, documentando la forma
angosta, pero ya no se usa.

## LAS DOS FORMAS LIMPIAS ANADIDAS A `MARCA_MADRE_POSITIVA` (vuelta 94)

El guarda acertaba el veredicto de al menos dos de las 86 (hoy 84) POR LA RAZON
EQUIVOCADA: "trae el procedimiento de LA SEGUNDA" (puesto **960**, madre
`value_proposition_startup`) y "trae la forma de UNA DE SUS LINEAS" (puesto **1567**,
madre `brief_de_diseno`) son NOMBRAMIENTOS DE LA MADRE en toda regla (referencian un
ordinal o "una de sus lineas" que solo tiene sentido si la madre enumero varias), y
el guarda los dejaba pasar por casualidad, por una marca idiosincratica distinta que
si conocia ("dice tres lineas" para el 960, "escribe el encargo entero" para el
1567).

**ANADIDAS**, con la MISMA lookahead negativa que excluye "linea compartida":
`trae\s+(?:el\s+procedimiento|la\s+forma)\s+de\s+(?:la\s+(?:primera|segunda|tercera|
cuarta|quinta)|una\s+de\s+sus\s+l[ií]neas?(?!\s*compartid))`. Frecuencia en las
3.388 razones: **4** (puestos 960, 1567, y dos mas del mismo dominio,
`fase_activate_primera_impresion` y `fase_activate`), no un patron sobreajustado a
un solo caso.

**EFECTO SOBRE EL SOSTEN UNICO**: al ganar una segunda marca, el 960 y el 1567 salen
de la lista de "sosten unico" (antes cada uno solo tenia su marca idiosincratica; hoy
tienen dos).

## EL SOSTEN UNICO DE `OP-E-07`, RECONSTRUIDO (vuelta 94)

**Reproduccion independiente de la medicion del auditor** (acta 93,
`docs/loop/SALIDA_V94_TAREA1C_REPRODUCCION_86.txt`), sobre las 86 filas vigentes
ANTES de la relectura conjunta de esta vuelta (`OP_E_07_DIRECCION_V93.jsonl`), con la
lista de `MARCA_MADRE_POSITIVA` de la vuelta 93 (sin las dos formulas nuevas): **29 de
86** pasan el guarda por UNA SOLA alternativa, y **7 de esas 29** por una alternativa
con frecuencia <= 3 en las 3.388 razones. **SIN DISCREPANCIA**: coincide cifra por
cifra y puesto por puesto con la medicion del auditor (960, 1281, 1567, 1844, 1848,
1886, 1992).

**LA CIFRA VIGENTE HOY** (`docs/loop/SALIDA_V94_TAREA4_SOSTEN_UNICO.txt`), sobre las
84 filas que quedan tras la relectura conjunta de esta vuelta y con las dos formulas
nuevas de `MARCA_MADRE_POSITIVA`: **25 de 84** pasan por UNA SOLA alternativa (baja de
29: el 1281 y el 1992 salieron de la bolsa, y el 960 y el 1567 ganaron una segunda
marca), y **3 de esas 25** por frecuencia <= 3 (puestos **1844** "nombra el problema"
freq 1, **1848** "entre sus pasos" freq 1, **1886** "monta el marco" freq 2).

**LAS OCHO ALTERNATIVAS CON FRECUENCIA 1 EN TODO EL CATALOGO** (no solo las que
sostienen alguna fila vigente hoy), con el MISMO CRITERIO aplicado a "es un habito"
en la vuelta 93 (declarar INVERIFICABLE, no quitar): ninguna tiene un segundo puesto
en las 3.388 razones contra el que probar si generaliza o falla como marca de madre
positiva, asi que las OCHO son INVERIFICABLES CONTRA OTRO PAR, y se declaran aqui en
vez de que solo una lo lleve escrito:

| formula | puesto de origen | frecuencia en las 3.388 |
|---|---:|---:|
| `dice\s+(?:una\|dos\|tres)\s+lineas?` | 960 | 1 |
| `entre sus pasos` | 1848 | 1 |
| `el paso nombra,?\s*el hijo ejecuta` | 995 | 1 |
| `es un h[aá]bito` | 1281 | 1 |
| `es un repertorio` | 1196 | 1 |
| `nombra el problema` | 1844 | 1 |
| `escribe el encargo entero` | 1567 | 1 |
| `calcula dos indicadores` | 974 | 1 |

Ninguna se quita de `MARCA_MADRE_POSITIVA` (no hay evidencia de que fallen, solo
falta evidencia de que generalicen), salvo donde una relectura conjunta especifica
(como la del 1281, arriba) concluya que el par que sostienen SALE por otra razon.

## EL CENSO DE `DIRECCION_MANUAL` DE `OP-E-07` (vuelta 94)

`scripts/loop/vuelta91_tarea4_direccion_ope07.py`, diccionario `DIRECCION_MANUAL`:
**8 entradas** (1163, 1191, 1388, 1500, 1778, 1847, 1886, 1992), los OCHO puestos que
la deteccion automatica de la vuelta 91 no resolvio y se leyeron a mano sobre la
razon completa. De las 8, **7 siguen vivas** en la bolsa vigente de 84
(`docs/plan/OP_E_07_DIRECCION_V94.jsonl`); la octava, **1992**, SALIO esta vuelta por
relectura conjunta (ver seccion de arriba).

**TRES de las 7 vivas NO tienen lectura ciega de nadie todavia: 1163, 1191 y 1847.**
Las otras cuatro (1388, 1500, 1778, 1886) tienen su cita textual propia en el
comentario de `DIRECCION_MANUAL`, pero eso es la lectura del propio ejecutor de la
vuelta 91 que las escribio, no una lectura ciega independiente. Las tres sin lectura
quedan para la TAREA 5 de esta vuelta (si queda vuelta) o para una vuelta futura.

## LAS TRES LECTURAS CIEGAS QUE FALTABAN EN `DIRECCION_MANUAL`: LAS TRES CONFIRMADAS (vuelta 94, TAREA 5)

Mecanica: volcar los `pasos_accionables` de los dos nodos de cada par SIN la razon
(`docs/loop/SALIDA_V94_TAREA5_LECTURAS_CIEGAS.txt`), adjudicar a ciegas, y SOLO
DESPUES destapar la razon completa (`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`) y el
comentario de `DIRECCION_MANUAL`. Si alguna resultaba ser otro 1992 (direccion que
vive en el comentario y no en la razon), iba a relectura conjunta sin resolverse
sola. **NINGUNA DE LAS TRES lo es**: las tres razones nombran la madre EXPLICITAMENTE
(no solo el comentario), y las tres coinciden con mi lectura ciega.

**PUESTO 1163** (`analisis_de_cohortes <-> customer_retention_tactics`). Lectura
ciega: `analisis_de_cohortes` termina en un paso generico ("disena y ajusta tus
estrategias de retencion") mientras que `customer_retention_tactics` son puras
tacticas concretas de retencion (correos, programa de lealtad, notificaciones,
Dia 1 y 100 dias, llamadas antes de renovar): **A_MADRE** (`analisis_de_cohortes`
nombra la categoria en una linea, el otro la despliega en 6 tacticas). La razon,
destapada: *"analisis_de_cohortes dice en su **paso 5**, en **UNA LINEA**, disenar
y ajustar las estrategias de retencion... y `customer_retention_tactics` **trae el
catalogo de esa linea**"*. **COINCIDE**, y la razon nombra la madre con paso
numerado, no solo el comentario.

**PUESTO 1191** (`ingenieria_de_prompts_efectiva <-> prompting_alta_variacion`).
Lectura ciega: `ingenieria_de_prompts_efectiva` son 4 pasos GENERICOS de cualquier
prompt (rol, contexto, restricciones, iterar); `prompting_alta_variacion` es una
tecnica ESPECIALIZADA para generar ideas variadas (rol inusual, pedir ideas
distintas, analogias extremas, varias tandas, filtrar a mano): **A_MADRE**
(el marco general nombra las piezas de cualquier peticion, el otro especializa esas
piezas para un proposito distinto). La razon, destapada: *"ingenieria_de_prompts_
efectiva **describe las piezas** de cualquier peticion... **la madre** busca
precision, este busca dispersion"*. **COINCIDE**, y la razon usa LITERALMENTE la
palabra "la madre" para nombrarla (no "trae" ni "desarrolla", pero nombra
explicitamente igual que 1191 ya documentaba en el comentario de `DIRECCION_
MANUAL` de la vuelta 91): no es un 1992, porque el nombramiento esta EN LA RAZON,
no solo en el comentario del ejecutor.

**PUESTO 1847** (`diseno_para_el_medio_ambiente <-> eco_efectividad_2`). Lectura
ciega: `diseno_para_el_medio_ambiente` cierra con un paso que cita modelos de
inspiracion (biomimetica, cradle-to-cradle, ecologia industrial) en una linea;
`eco_efectividad_2` es exactamente uno de esos modelos con su procedimiento propio
(ciclo de vida completo, nutrientes biologicos/tecnicos, metas positivas de
diseno): **A_MADRE** (el marco cita el modelo, el modelo desarrolla su
procedimiento). La razon, destapada: *"diseno_para_el_medio_ambiente dice en su
**paso 4**, en **UNA LINEA**, buscar inspiracion... en modelos como CRADLE TO
CRADLE... y `eco_efectividad_2` **es uno de esos modelos con su procedimiento**"*.
**COINCIDE**, y la razon nombra la madre con paso numerado.

**CONCLUSION: las tres se quedan como estan, sin relectura conjunta.** Las tres
razones nombran la madre por escrito (dos con "paso N, en UNA LINEA", una con la
palabra literal "la madre"), y las tres coinciden con la lectura ciega independiente
de esta vuelta.

## VUELTA 95, TAREA 1: LOS CUATRO REGISTROS DEL ENCARGO (acta de la vuelta 94)

### (a) La caida de reporte del "8 aciertos": medicion y regla

El reporte de la vuelta 94 publico "8 aciertos... 7 mas 1" sobre
`docs/loop/SALIDA_V94_TAREA2A_BARRIDO.txt`. El acta de la vuelta 94 (`docs/loop/
ACTA_AUDITOR.md` lineas 33192 a 33214) lo tallo con `scripts/loop/
tallar_composicion_salida.py`: **14 filas, 11 en `docs/plan/04_ENLACES.md` y 3 en
OTRO fichero**, ninguna combinacion produce "8, todos en 04_ENLACES.md, 7 mas 1".
Yo lo reproduje EN ESTA VUELTA con el mismo instrumento (`docs/loop/
SALIDA_V95_TAREA1A_COMPOSICION_V94.txt`): **14 filas, 11 y 3, mismas
enumeraciones** (04_ENLACES.md: 704, 939, 1017, 1019, 1021, 1027, 1029, 1030,
1031, 1040, 1048; otro fichero: 327, 640, 748). Calza al digito con el acta.

**LA REGLA QUE SALE DE ELLA** (EJECUTOR.md regla 1, "LA TABLA SE CUENTA DE SU
FICHERO"): toda cifra que describa la composicion de un fichero de salida se
talla con instrumento y se pega con su comando; ninguna se cuenta a ojo.

**CORRECCION DECLARADA (TAREA 2.a de la vuelta 95), sin borrar la frase vieja:**
el "8 aciertos... 7 mas 1" del reporte de la vuelta 94 se sustituye por la cifra
real, tallada con el instrumento NUEVO `scripts/loop/tallar_barrido_cifras.py`
(que CORRE el barrido el mismo, con las mismas raices y patrones del primer
comando de `SALIDA_V94_TAREA2A_BARRIDO.txt`), corrido en esta vuelta
(`docs/loop/SALIDA_V95_TAREA2A_BARRIDO_TALLADO.txt`): **18 aciertos totales**
(por ocurrencia del patron, no por linea de grep: dos lineas de `04_ENLACES.md`
y una de `OPERACIONES.jsonl` traen dos ocurrencias cada una), **14 en
`docs/plan/04_ENLACES.md`, 3 en `docs/plan/OPERACIONES.jsonl`, 1 en
`docs/plan/03_FUSIONES.md`; 9 CON salvedad y 9 SIN salvedad** (ventana de 200
caracteres a cada lado). DISCUTIBLE: el conteo por OCURRENCIA (no por linea de
grep) y la inclusion de `OPERACIONES.jsonl` (que el `grep -rn docs/plan/
docs/BANCO_DE_TEXTOS.md` original SI barria por ser recursivo, aunque la salida
vieja no mostraba coincidencias ahi) son decisiones de diseno del instrumento
nuevo, declaradas en su docstring; se marcan para la relectura ciega.

### (b) Las cuatro adjudicaciones de los discutibles (acta de la vuelta 94, secciones 2.1 a 2.4)

**2.1** (`ACTA_AUDITOR.md` lineas 33109 a 33137): el sello de apertura de la
vuelta 94 se commiteo en `a4c89ab6` (el ULTIMO commit), no antes de la primera
operacion. El VALOR es correcto (`git rev-parse ce8767c9^` da `267365c88f...`,
el mismo hash), asi que **NO es caida de identidad**: es **INCUMPLIMIENTO DE
ENCARGO**, declarado por el propio ejecutor. De ahi nace la averia de instrumento
reparada en la TAREA 2.b de esta vuelta 95 (la fila de identidad de
`tallar_cabecera_reporte.py` imprimia un literal incondicional).

**2.2** (lineas 33139 a 33160): los seis `SALIDA_V94_*_APERTURA.txt` son byte
identicos a los `SALIDA_V93_*_CIERRE.txt`, verificado con `cmp` y con
`git diff --stat` sobre `dataset/` y `web/lib/assets/` (cero lineas). ADJUDICADO
SUFICIENTE, con el **CRITERIO NUEVO** escrito para que deje de ser discutible
cada vuelta: cuando el arbol de `dataset/`, `web/` y `scripts/` del commit de
apertura sea byte identico al del cierre de la vuelta anterior **y ese diff se
corra y se cite EN LA VUELTA**, las salidas del cierre anterior SON la medicion
de apertura, citadas con el comando del diff al lado.

**2.3** (lineas 33162 a 33169): abrir `OP-E-03` en la TAREA 6 de la vuelta 94
sin leer las 183 lecturas de par fue una eleccion de alcance CORRECTA y
CONFIRMADA (183 lecturas no caben detras de cinco tareas).

**2.4** (lineas 33171 a 33180): la entrada `1992: "B_MADRE"` de
`vuelta91_tarea4_direccion_ope07.py` sigue sin nota pese a que la salida vigente
(`OP_E_07_DIRECCION_V94.jsonl`) ya no trae el par. ADJUDICADO: no se borra, se
anota "SUPERADO por la TAREA 3 de la vuelta 94" al lado (EJECUTOR.md regla 8).
Ejecutado en la TAREA 4.b de esta vuelta 95.

### (c) El cribado de cita de linea sobre las 84 (acta de la vuelta 94, seccion 6, lineas 33309 a 33336)

Sobre `OP_E_07_DIRECCION_V94.jsonl` (84 filas vigentes), el auditor midio si la
razon de cada par cita un paso numerado o una linea explicita: **grupo A (cita
paso o linea): 57**; **grupo B (sin linea pero con forma de indice): 9** (872,
1023, 1111, 1388, 1500, 1536, 1634, 1778, 2018); **grupo C (ni una ni otra):
18** (886, 890, 896, 909, 910, 940, 947, 983, 993, 1020, 1057, 1083, 1086, 1191,
1196, 1220, 1844, 1886). **LOS CUATRO CAIDOS de esta operacion en tres vueltas
(1098, 1009, 1281, 1992) caen los CUATRO en el grupo C.** El **1083**, el
ejemplar CONFIRMADO de la casa ("que LA MADRE no tiene"), **tambien esta en C**:
el grupo C no es una lista de condenados, es la poblacion donde vive esta especie
de error. Cribado y lectura de las 18 en la TAREA 3 de esta vuelta 95.

### (d) La caida propia del auditor, declarada por el mismo (acta de la vuelta 94, seccion 7.1, lineas 33340 a 33346)

`docs/loop/_auditor_v93_grafo.py`, commiteado por el auditor en la vuelta 93
como instrumento, **no reproduce la salida que publico** (busca una clave
`nodes` que ese JSON no tiene y revienta al correrlo). La medicion en si era
correcta (rehecha por el auditor en la vuelta 94, mismo resultado), pero
commitear como instrumento un fichero que no es el que se corrio es el mismo
defecto que esta casa le exige al ejecutor. Se registra aqui como pide el
encargo, con el mismo trato.

## VUELTA 95, TAREA 3: EL CRIBADO DE CITA DE LINEA, RECONSTRUIDO, Y LA LECTURA DEL GRUPO C

**(a) Reconstruccion del cribado con codigo propio**
(`scripts/loop/vuelta95_tarea3a_cribado_cita_de_linea.py`,
`docs/loop/SALIDA_V95_TAREA3A_CRIBADO.txt`): una primera version de mis
patrones (sin numeros escritos como "tres" y sin conjugaciones de "enunciar")
dio 56/8/20, DISTINTO del acta. Con dos ajustes linguisticos declarados (numero
escrito en "dice N lineas", y prefijo en vez de palabra exacta para
"enumera"/"enuncia") la reconstruccion da **57/9/18, IDENTICO al acta de la
vuelta 94** (`ACTA_AUDITOR.md` lineas 33317 a 33321), misma enumeracion de B y
C. Se registra el primer intento fallido junto con el que calza, por
transparencia del proceso (EJECUTOR.md regla 8).

**(b) a (f) La lectura de las 18 filas del grupo C**
(`scripts/loop/vuelta95_tarea3_lectura_grupo_c.py`,
`docs/loop/SALIDA_V95_TAREA3_LECTURA_GRUPO_C.txt`), pasos primero y razon
despues, misma mecanica que el 1009/1281/1992. Tres ya resueltos sin releer
(1083 confirmado, 1191 por mandato explicito del encargo, 1886 por el acta de
la vuelta 93). De las 15 restantes:

**QUEDAN, la razon nombra la madre (11): 896, 909, 910, 940, 983, 993, 1020,
1057, 1086, 1196, 1220.** Once de once anclan a UN paso, fase o linea concreta
de un nodo que el otro desarrolla entero (formula canonica del banco 9.6.2,
"UNA LINEA... ES UN PROCEDIMIENTO NOMBRADO EN UNA LINEA"); el 1220 ademas dice
literalmente "es la MADRE".

**RELECTURA CONJUNTA, duda genuina, NO resueltos solo (4): 886, 890, 947,
1844.** Los cuatro comparan una clase entera de un nodo contra lo que el otro
"no tiene" o "asume", sin anclar a un paso, fase o linea unica y numerada (el
patron exacto que hizo salir al 1098, 1009, 1281 y 1992). **DISCUTIBLE
marcado**: mi primer barrido de este mismo grupo, con un criterio mas
estricto (exigir la palabra literal "madre"), habria dado ONCE candidatos a
SALIR en vez de cuatro; me aparte de ese criterio porque contradecia la
propia advertencia del encargo ("si lees las 18 buscando 18 bajas, las
encontraras y estaras equivocado") y porque el acta de la vuelta 93 ya habia
usado el criterio de ANCLA A UN PASO (no la palabra literal) para confirmar el
1886. Traigo la duda entera para que la mesa la revise, no la resuelvo sola:
ninguna arista se retira esta vuelta por esta via.

**CERO ARISTAS RETIRADAS en esta TAREA 3**: es un resultado legitimo, no una
falta de trabajo (el encargo lo dice explicito: "cada una se decide por su
razon", "el grupo C no es una lista de condenados").

## VUELTA 95, TAREA 4: LAS TRES DE HIGIENE

**(a)** `docs/plan/04_ENLACES.md`, fila 11: intervalo cerrado igual que la
fila 9 ("desde la vuelta 93 hasta la vuelta 94"), con CORRECCION DECLARADA al
lado remitiendo a la fila 12 (82 ESCRITA + 2 YA_ESTABA, cifra vigente desde
la vuelta 94). Sin borrar nada.

**(b)** `scripts/loop/vuelta91_tarea4_direccion_ope07.py`, entrada `1992` del
diccionario `DIRECCION_MANUAL`: anotado al lado "SUPERADO por la TAREA 3 de
la vuelta 94, el par salio de OP-E-07", sin borrar el comentario original de
la vuelta 91 (EJECUTOR.md regla 8).

**(c) La pisada de `DIFERENCIA_CONTRA_COLA.jsonl`.** Elegi: recuperar el
ensayo de agosto (387 filas, commit `88b3f7c6`) a un fichero de contraste con
nombre propio, `docs/plan/DIFERENCIA_CONTRA_COLA_ENSAYO_AGOSTO.jsonl`
(`wc -l` confirmado, 387). La salida vigente (`DIFERENCIA_CONTRA_COLA.jsonl`,
183 filas de la vuelta 94) sigue pisandose a proposito en cada corrida nueva
(es la costumbre correcta: solo debe existir UNA diferencia vigente por
dominio a la vez), y `scripts/plan/diferencia_contra_cola.py` ya trae
`--salida` para versionar si una vuelta futura necesita conservar dos
diferencias vigentes a la vez; se documento la decision en el docstring del
script.

**El SyntaxWarning de `scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py`,
DISCREPANCIA DECLARADA:** lo corri fresco (cache `__pycache__` borrado,
`python -W always::SyntaxWarning`, import directo con
`warnings.filterwarnings('error', category=SyntaxWarning)`, y `compile()`
sobre el fuente): NINGUNA de las tres corridas produce ningun SyntaxWarning.
El fichero tiene un solo commit en toda su historia (`d1d88d1a`, `git log`
confirmado) y ese commit YA trae el docstring principal como `r"""` desde el
primer caracter (linea 2); la unica linea con secuencias de escape sin
prefijo `r` (linea 8, `` `(?<!no )trae\b...` ``) vive DENTRO de ese docstring
ya crudo, asi que no genera advertencia. EL INSTRUMENTO MANDA (EJECUTOR.md
regla 2): no toco el fichero porque mi propia corrida no reproduce el defecto
que el encargo cita; declaro la discrepancia en vez de "arreglar" algo que no
esta roto. DISCUTIBLE marcado para la relectura ciega.

## VUELTA 95, TAREA 5: PARADA DELIBERADA, NO INTENTADA ESTA VUELTA

Las TAREAS 1 a 4 cerraron en verde (ningun ROJO, ninguna contradiccion con
regla vigente), asi que la condicion para abrir la TAREA 5 se cumplia. La leo
y decido PARAR antes de empezar el tramo, por la propia regla que el encargo
escribe: "Si el texto de la operacion no alcanza para leer sin decidir,
PARAS y la traes: eso no es un fracaso de la vuelta, es la regla."

**Por que para.** La nota de `OP-E-03` en `docs/plan/OPERACIONES.jsonl` dice
que la lectura pendiente es "clasificacion (A/B/C/D, veredictos contados
aparte de la tasa por dominio) ... del mismo tamano que OP-E-06/OP-E-07": es
el MISMO juicio completo del banco 9.6.1 (CONTINUA o D) mas la direccion del
9.6.2 para cada par nuevo, no la pregunta mas estrecha de la TAREA 3 de esta
vuelta (si la razon YA ESCRITA nombra la madre). La TAREA 3, con esa pregunta
mas estrecha y con precedente extenso de vueltas anteriores para calibrar
contra el, ya me dejo 4 de 15 en duda genuina. Abrir 40 pares NUEVOS con el
juicio completo, en la misma vuelta y despues de las TAREAS 1 a 4, es
exactamente la clase de lectura apurada que esta casa prohibe ("no adivines").

**Lo que SI deje listo para que la vuelta que la lea no empiece de cero:**
`docs/plan/OPERACIONES.jsonl` (OP-E-03) trae la verificacion completa (cinco
puntos) y la bolsa vigente (`docs/plan/DIFERENCIA_CONTRA_COLA.jsonl`, 183
filas de la vuelta 94, cuenta cuadrada sin fugas). No hace falta releer nada
de esta vuelta para abrir el primer tramo despues: el resolutor de ids, la
marca de LECTURA DIRIGIDA, el no entrar en cola ni mover el marcador, y el
conteo aparte de la tasa por dominio, los cinco puntos de la verificacion,
quedan citados aqui para la vuelta que la tome.

## VUELTA 96, TAREA 1: LOS REGISTROS DEL ACTA 95 (acta de la vuelta 95, `ACTA_AUDITOR.md` lineas 33446 a 34023)

### (1.1) La caida de reporte de la vuelta 95, con su nombre, su medicion y LA LETRA NUEVA al lado

**LA CAIDA, con su nombre.** `docs/loop/REPORTE.md` de la vuelta 95, linea 210,
publico en su lista de RUTAS TOCADAS el parentesis **"`docs/PENDIENTES.md`
(cinco secciones nuevas)"**, y las secciones eran **CUATRO**.

**LA MEDICION, que NO se rehace aqui porque ya viene hecha** (encargo de la
vuelta 96, TAREA 1.1, literal: *"No se vuelve a medir: ya viene medida"*). La
tallo el auditor con `scripts/loop/tallar_composicion_salida.py` sobre el diff
de la vuelta entera, y su salida vive en
`docs/loop/_auditor_v95_pendientes_tallado.txt`: **4 secciones de nivel 2 (##) y
4 subsecciones de nivel 3 (###)**, 8 filas casadas en total, con las dos
enumeraciones nominales impresas. El acta 95 (seccion 5, lineas 33854 a 33917)
probo ademas **siete criterios distintos y NINGUNO da cinco** (`##` 4, `###` 4,
las dos juntas 8, cualquier nivel 8, lineas que abren en negrita 17, lineas que
mencionan "VUELTA 95" 4, hunks del diff 1).

**LA LETRA NUEVA AL LADO, que es lo que cambia el trato.** Decision del fundador
del 27 ago 2026 (`docs/loop/paradas/2026-08-27-racha-parentesis-DECISION.md`,
recogida en `AUDITOR.md` seccion 4): la caida de reporte cuenta para la racha
**SOLO cuando la cifra vive en una TABLA, una CABECERA o una CONCLUSION**; si
vive en una **LISTA DE RUTAS** o en **PROSA DE ACOMPANAMIENTO**, se registra y
dispara la relectura al doble, **pero NO acumula**. Esta cifra vivia en la lista
de rutas tocadas.

**CONSECUENCIA, escrita entera:** la caida **SE REGISTRA** (aqui), **dispara la
relectura al doble** de su tramo, y **NO ACUMULA para la racha**, por letra
expresa de esa misma decision, que la nombra por su caso. La racha de reporte
que acumula queda por tanto **en CERO**, y la de clase o cifra publicada
tambien, con dos tandas limpias seguidas (acta 95, seccion 7).

### (1.2) LAS DOS CAIDAS PROPIAS DEL AUDITOR, cada una con su nombre

El acta 95 las declara ella misma en su seccion 6 (lineas 33919 a 33946), con el
mismo trato que las del ejecutor, y las dos quedan aqui verificadas por medicion
propia de la vuelta 96.

**(i) AFIRMO UNA BUSQUEDA QUE NO CORRIO** (acta 95, seccion 6 punto 2, y
adjudicacion 4.4, linea 33826). El encargo de la vuelta 95 mando arreglar *"el
SyntaxWarning de `scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py` (secuencia
de escape en la docstring)"*. **Ese warning no existe y nunca existio.**
Remedido hoy: `git log --format='%h %s' -- scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py`
da **UN SOLO commit en toda la historia del fichero** (`d1d88d1a`), y
`git show d1d88d1a:scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py | head -2`
muestra que **ese commit ya abre con la cadena cruda `r` mas tres comillas**,
identico a la cabecera de hoy. `AUDITOR.md` seccion 2 lo prohibe con esas
palabras: *"Prohibido afirmar una busqueda no corrida."* **El ejecutor gasto
tres vias en desmentirlo y tenia razon** (reporte de la vuelta 95, TAREA 4).

**(ii) UNA OMISION QUE MANDO UN PAR A LA MESA SIN NECESIDAD** (acta 95,
seccion 6 punto 3, y adjudicacion 4.1, linea 33773). El auditor dio al ejecutor
la linea **32695** del acta para resolver el **1886**, y no vio que **la misma
tabla, DOS FILAS MAS ARRIBA, ya resolvia el 1844**. Verificado hoy leyendo
`sed -n '32693,32697p' docs/loop/ACTA_AUDITOR.md`: la linea **32693** es la del
**1844** (*"encaje plausible en el paso 2"*, razon *"NOMBRA EL PROBLEMA ... TRAE
EL PROCEDIMIENTO"*, veredicto **COINCIDO**) y la **32695** es la del 1886.
**El 1844 QUEDA**, adjudicado por el acta 95 (4.1) por extension natural del
mismo trato dado al 1886, y **la relectura conjunta baja de CUATRO a TRES: 886,
890 y 947.** No es caida del ejecutor: la prudencia no lo es.

### (1.3) LA ETIQUETA DEL GRUPO C, CORREGIDA PARA LOS NUEVE, sin borrar el texto viejo

**EL TEXTO VIEJO, que NO se borra** (acta de la vuelta 94, y repetido en la
seccion 6 punto 1 del acta 95): el auditor publico las 18 razones del grupo C
como *"ni citan linea ni traen forma de indice"*.

**LA CORRECCION, medida con instrumento propio de ESTA vuelta** (`EJECUTOR.md`
regla 2, "EL INSTRUMENTO MANDA": el acta 95 se cita como CONTRASTE, no como
fuente). Instrumento: `scripts/loop/vuelta96_tarea1c_etiqueta_grupo_c.py`,
salida en `docs/loop/SALIDA_V96_TAREA1C_ETIQUETA_GRUPO_C.txt`, EXIT 0. La bolsa
de 18 **no se teclea**: se calcula importando `clasifica_razon()` de
`scripts/loop/vuelta95_tarea3a_cribado_cita_de_linea.py`. Tabla pegada entera de
ese fichero:

| pregunta | cuantas de las 18 |
|---|---:|
| mencionan la palabra "linea" en cualquier forma | 9 |
| lo hacen con la formula ESTRICTA "es/son UNA LINEA" (con determinante) | 6 |
| lo hacen con la formula ANCHA "es/son ... LINEA" (con o sin determinante) | 7 |
| anclan con "en ... linea" y NO con "es/son" | 1 |
| NO mencionan la palabra "linea" en ninguna forma | 9 |
| casan el patron A del acta 94 (tiene que ser 0) | 0 |

- **mencionan linea (9):** 896, 909, 910, 940, 983, 993, 1057, 1086, 1196
- **formula ESTRICTA (6):** 896, 910, 940, 993, 1057, 1196
- **formula ANCHA (7):** 896, 909, 910, 940, 993, 1057, 1196
- **"en ... linea" y no "es/son" (1):** 1086
- **no la mencionan (9):** 886, 890, 947, 1020, 1083, 1191, 1220, 1844, 1886

**LO QUE CALZA Y LO QUE NO, declarado y no resuelto copiando.** El **NUEVE**
del acta 95 calza al digito **y con la misma enumeracion**. Su **OCHO con la
formula literal "es/son UNA LINEA"** (896, 909, 910, 940, 993, 1057, 1086,
1196) **NO calza con mi medicion**: mi formula estricta da **SEIS** y la ancha
**SIETE**. La diferencia esta nombrada, par por par, y no es opinable:

- el **909** dice *"Sus dos referencias al mapa **son lineas**"*, plural y sin
  determinante: entra en la formula ANCHA (7) y no en la estricta (6);
- el **1086** dice *"cierra con TRES PREGUNTAS **en una sola linea**"*, que
  **NO es la formula "es/son"** sino un "en ... linea"; escapa al patron A del
  acta 94 solo por la palabra "sola" que se cuela en medio;
- el **983** dice *"... validacion suficiente**: UNA LINEA**"*, tras dos puntos,
  y el propio acta 95 ya lo contaba aparte de sus ocho.

**7 mas 1 mas 1 dan los 9. Todo queda contado y nada sobra.**

**LO QUE SE CORRIGE ES LA ETIQUETA, NO LA CONCLUSION.** La conclusion que el
auditor saco del grupo C **sigue en pie y esta medida** (acta 95, seccion 3.2):
el **1083**, el ejemplar CONFIRMADO de la casa, cae dentro de C bajo **las tres
varas** probadas (la del acta 18, la mas ancha 8, la mas estrecha 50), o sea que
**ninguna vara de este tipo separa confirmados de caidos**. Lo que era falso, y
queda corregido aqui, es la **ETIQUETA**: el grupo C no era "la poblacion que no
cita linea", era **la poblacion que el patron A del acta 94 dejo fuera**, y ese
patron casa *"EN una linea"* pero no *"ES una linea"*, que es como el redactor
escribe la mayoria de sus anclas.

**LA MECANICA DE ROJO DEL INSTRUMENTO, PROBADA POR MUTACION** (`EJECUTOR.md`
regla 1, "EL CASO ROJO SE PRUEBA POR MUTACION"):
`scripts/loop/vuelta96_tarea1c_prueba_mutacion.py`, salida en
`docs/loop/SALIDA_V96_TAREA1C_MUTACION.txt`, EXIT 0. Control sobre dato real
VERDE (18 filas, 0 fallos); mutacion (ii) del tamano esperado a 17 sobre el dato
real **CAE**; mutacion (i) sobre una copia EN MEMORIA del fichero de veredictos
sin la entrada del puesto 872 **CAE**; control de vuelta VERDE. **Y la tercera
guarda se DECLARA en vez de fabricarle un rojo que se apruebe solo:** la guarda
"esta en C y ademas casa el patron A" es una **TAUTOLOGIA** mientras el mismo
`clasifica_razon()` alimente las dos piezas, asi que **NO TIENE CASO ROJO
AUTOMATICO** y asi queda escrito en el propio instrumento.

**ADJUDICADO EN LA VUELTA 97, y el texto de arriba se queda entero.** El acta de
la vuelta 96, seccion **4.2** (`docs/loop/ACTA_AUDITOR.md` linea **34317**, leida
hoy), da la razon a esta discrepancia: **el "ocho" es del auditor y esta mal**, y
el propio auditor lo lleva a sus errores con nombre (seccion 6 punto 1, linea
**34457**). La correccion queda registrada en la seccion **VUELTA 97, TAREA 1**
apartado **(1.2)** de este mismo fichero, y **NO se remide**, porque ya viene
medida dos veces.

### (1.4) LAS ADJUDICACIONES DEL ACTA 95, cada una por su numero

Leidas hoy con `grep -n '^### ' docs/loop/ACTA_AUDITOR.md` sobre el tramo del
acta 95; la linea de cada una va al lado y sale de ese grep, no de memoria.

| num | linea | que adjudica | efecto sobre el trabajo |
|---|---:|---|---|
| **4.1** | 33773 | **EL 1844 SALE DE RELECTURA CONJUNTA Y QUEDA**, por extension natural del mismo trato dado al 1886 (misma regla, mismo fichero, misma tabla) | la relectura conjunta baja de **4 a 3**: quedan 886, 890 y 947 |
| **4.2** | 33795 | **LOS TRES QUE SIGUEN: CONFIRMADOS como duda genuina**, con la evidencia que faltaba (el 886 es el hermano vivo del 1009 caido: mismo hijo `fit_problema_solucion`, misma formula, madre casi gemela) | los tres van a **MESA DE FORMULA**, TAREA 2 de esta vuelta |
| **4.3** | 33816 | **Discutible 1** (la unidad de medida del barrido nuevo, por ocurrencia y no por linea, con `OPERACIONES.jsonl` dentro): **CONFIRMADO Y SUFICIENTE**, la unidad nueva es la buena | deja de ser discutible; queda escrita en el docstring del instrumento |
| **4.4** | 33826 | **Discutible 3** (el SyntaxWarning no reproducido): **EL EJECUTOR TIENE RAZON**, el auditor estaba equivocado | ver (1.2)(i); el fichero **no se toca** |
| **4.5** | 33835 | **Discutible 4** (la herencia de apertura por el criterio 2.2): **CONFIRMADO**, el criterio aguanta con la vara mas estricta (`web/` entero, no solo `web/lib/assets/`) | **deja de ser discutible** |
| **4.6** | 33843 | **Discutible 2** (la aplicacion del criterio a 15 razones nuevas): **CONFIRMADO Y RESUELTO POR MEDICION**, una vara mecanica que no vio el codigo del ejecutor reproduce sus dos listas exactas (11 y 4) | apartarse del criterio estricto fue **correcto**: el estricto habria sacado al 1083 |

## VUELTA 96, TAREA 2: LA MESA DE FORMULA DE LOS PARES 886, 890 Y 947. NO HAY VARA CITABLE: LOS TRES QUEDAN COMO ESTAN, Y LA DUDA QUEDA SELLADA AQUI

**Origen:** decision 2 del fundador, 27 ago 2026
(`docs/loop/paradas/2026-08-27-racha-parentesis-DECISION.md`), literal: *"los
pares 886, 890 y 947 van a MESA DE FORMULA en la reanudacion: los cinco
ejemplares de la formula (1083, 1009 y los tres) impresos enteros y juntos, la
vara que los separa escrita o declarada inexistente, y los tres adjudicados por
ella con correccion declarada; si no hay vara citable, los tres quedan como
estan y la duda va sellada a PENDIENTES."* **La mesa se sento entera. Este
apartado es la ultima de las cuatro ramas: la que la propia decision escribio
para el caso de que no hubiera vara.**

### (a) LOS CINCO EJEMPLARES, IMPRESOS ENTEROS Y JUNTOS

`scripts/loop/vuelta96_tarea2_mesa_de_formula.py`, salida completa en
`docs/loop/SALIDA_V96_TAREA2_MESA_DE_FORMULA.txt` (**152 lineas**, contadas del
fichero con `wc -l`), EXIT 0. De cada uno de los cinco: puesto, estado con el
sitio que lo dice, dominio, clase, los dos nodos **crudos y RESUELTOS por el
resolutor antes de cruzarse** (`P.1`, `BANCO_DEL_PLAN.md` linea 11; ninguno de
los diez ids cambio al resolverse, y se dice porque `P.1` obliga a decir siempre
si se resolvio), la direccion registrada en `OP_E_07_DIRECCION_V94.jsonl`, **la
razon COMPLETA sin recortar**, y los `pasos_accionables` **ENTEROS** de los dos
nodos. Los diez recuentos de pasos salen del fichero:

| puesto | estado | nodo A y sus pasos | nodo B y sus pasos |
|---:|---|---|---|
| 1083 | CONFIRMADO | `customer_discovery_cuatro_fases` (4) | `priorizar_elementos_a_validar` (5) |
| 1009 | CAIDO, YA SALIO | `customer_discovery_phase2_problem_test` (5) | `fit_problema_solucion` (3) |
| 886 | VIVO, a mesa | `customer_discovery_overview` (4) | `fit_problema_solucion` (3) |
| 890 | VIVO, a mesa | `checkpoints_validacion` (4) | `customer_validation` (5) |
| 947 | VIVO, a mesa | `customer_discovery` (5) | `product_market_fit` (6) |

**LA MECANICA DE ROJO de este instrumento, probada por mutacion** (mutacion C de
`docs/loop/SALIDA_V96_TAREA2_MUTACION.txt`): con un puesto inventado en la lista
de ejemplares, **CAE** y no imprime nada.

### (b) LA VARA CANDIDATA, ESCRITA, Y DE DONDE SALE CADA PIEZA

No se invento ninguna regla. La vara candidata sale entera de dos textos ya
escritos, citados literalmente en el docstring del instrumento:

- **banco `9.6.2`** (`docs/BANCO_DE_TEXTOS.md` linea 1737 y siguientes):
  *"COMO SE RECONOCE UN PAR MADRE E HIJO... El hijo CABE ENTERO DENTRO DE UN
  PASO DE LA MADRE, y la madre conserva materia propia que el hijo no toca en
  ningun paso."*
- **`OP-E-07.verificacion`** (`docs/plan/OPERACIONES.jsonl`, campo
  `verificacion`): *"NO SE RELEE EL PAR: se lee su razon, que ya esta escrita.
  Si la razon tampoco lo dice, el par sale de la cosecha y se anota por que."*

De las dos juntas sale la vara: **la razon tiene que SENALAR UN PASO, FASE O
LINEA UNICA** de uno de los dos nodos como el sitio donde el otro cabe entero.
Si la razon solo opone el nodo ENTERO contra lo que el otro *"no tiene"*,
*"asume"* o *"da por supuesto"*, no ha senalado madre: ha comparado dos clases.

- **T1, ANCLA SINGULAR** (decide): trece familias de designacion, cada una
  tomada de una forma que el expediente ya usa (paso numerado, paso ordinal,
  fase numerada u ordinal, "es/son ... linea", "en N lineas", dos puntos y UNA
  LINEA, "una de sus lineas", "termina/cierra/empieza con una linea", "entre
  sus pasos", "el paso nombra", "una de las N", la palabra "madre" literal, "es
  el indice").
- **T2, SIN RESIDUO DECLARADO** (se publica al lado, NO decide sola): la razon
  no declara ella misma que una parte del hijo *queda fuera* del solape. Se mide
  **literal y estrecho a proposito**, para que no se pueda ensanchar hasta
  atrapar a quien convenga.

### (c) LA PRUEBA: LA VARA SE CORRE CONTRA LAS DIECINUEVE ADJUDICACIONES YA PUBLICADAS, Y CONTRADICE TRES

`scripts/loop/vuelta96_tarea2_vara_de_la_mesa.py`, salida completa en
`docs/loop/SALIDA_V96_TAREA2_VARA.txt`, EXIT 0. **Una vara que tumba lo ya
adjudicado no separa nada: reordena.** Por eso se prueba antes de usarse, sobre
los quince pares que el expediente publico como QUEDA y los cuatro que publico
como SALE, cada uno con el sitio de su adjudicacion en la tabla. Cifras leidas
de ese fichero:

**EXPEDIENTE: 19 filas. CALZAN 16. CHOCAN 3, nominales: 1886, 1844 y 1009.**

**LAS TRES QUE CHOCAN, cada una con su nombre y su motivo:**

| puesto | publicado | la vara da | por que choca |
|---:|---|---|---|
| **1886** | QUEDA (acta 93, `ACTA_AUDITOR.md` linea 32695) | **SALE** | su razon **no trae NINGUNA** de las trece familias de ancla |
| **1844** | QUEDA (acta 95, adjudicacion 4.1, linea 33773) | **SALE** | su razon **no trae NINGUNA** de las trece familias de ancla |
| **1009** | SALE (vuelta 93) | **QUEDA** | su razon **si trae** un ordinal de fase, *"en la fase I"*, **pero esa fase es del HIJO**, no de la madre |

**Y LAS TRES CHOCAN POR LA MISMA RAIZ, que es lo que hace inutil seguir
afinando el patron.** El 1886 y el 1844 fueron adjudicados QUEDA **leyendo los
PASOS DE LOS NODOS**, no la razon: el acta 93 dice del 1886 *"encaje limpio
dentro del paso 1"* y la lectura ciega del acta 95 (seccion 3.3) dice del 1844
*"madre `productos_crudos`, ancla en su paso 2"*. Las dos son lecturas del PAR.
El 1009, en cambio, cayo **leyendo la RAZON**, que es el carril que
`OP-E-07.verificacion` manda. **Los dos carriles dan respuestas opuestas sobre
razones de la MISMA FORMA**, y el ejemplar esta a la vista en el fichero de la
mesa: la razon del **1844** dice *"`productos_crudos` NOMBRA EL PROBLEMA:
[tres cosas] ... `diagnostico_de_productos_crudos` TRAE EL PROCEDIMIENTO:
[cinco cosas]"*, y la del **1009** dice *"`customer_discovery_phase2_problem_test`
prueba el problema: [cinco cosas] ... `fit_problema_solucion` trae un
procedimiento que esa fase no tiene: [tres cosas]"*. **Misma forma, veredictos
opuestos.** Ningun patron sobre el texto de la razon puede separar dos frases
que tienen la misma forma.

**LA COMPARACION NO ES UNA TAUTOLOGIA, y esta probado en las dos direcciones**
(`docs/loop/SALIDA_V96_TAREA2_MUTACION.txt`, EXIT 0): sobre el dato real ya sabe
decir que NO (3 CHOCAN de 19); la **mutacion A1** voltea en memoria el veredicto
publicado del 1083, que hoy CALZA, y **pasa a CHOCAR**; la **mutacion A2**
voltea el del 1886, que hoy CHOCA, y **pasa a CALZAR**; la **mutacion B** mete
un puesto inventado y la mecanica de ROJO **CAE**; y el control vuelve a verde
con las mutaciones deshechas.

### (d) LA SEGUNDA VARA POSIBLE, LA QUE SI LOS SEPARARIA, Y POR QUE NO SE APLICA

**Se dice entera en vez de callarla**, porque callarla seria esconder que la
mesa tenia una salida y no se tomo. Si en vez de leer la RAZON se leyera el PAR
(el test de `9.6.2` aplicado a los `pasos_accionables` de hoy), los cinco SI se
separarian. **Esto es LECTURA MIA, declarada como tal, sobre el material impreso
en `SALIDA_V96_TAREA2_MESA_DE_FORMULA.txt`, y no es un instrumento:**

- **1083:** los cinco pasos del hijo (revisar el lienzo, las cinco variables
  criticas, enfocar recursos, priorizar cada lado, no validar todo a la vez)
  caben **enteros dentro de la fase 1 de la madre** (*"desarma tu idea en las
  nueve partes del lienzo"*), y la madre conserva sus fases 2, 3 y 4. **Cumple
  9.6.2. QUEDA**, igual que lo publicado.
- **1009:** el paso 1 del hijo solapa con la madre, pero sus pasos 2 y 3
  (product market fit y modelo de negocio escalable) **quedan por encima de una
  fase que solo prueba el problema**. No cabe en UN paso. **Falla 9.6.2. SALE**,
  igual que lo publicado.
- **886:** mismo hijo que el 1009. Sus tres pasos se reparten entre las fases
  **2, 3 y 4** de `customer_discovery_overview`. **No cabe en UN paso. Falla.**
- **947:** las seis evaluaciones del hijo cubren cosas que la madre no tiene en
  ningun paso (tamano de mercado, crecimiento predecible, decision formal con
  inversores). **No cabe en UN paso. Falla.**
- **890:** el mas dudoso de los cinco y se dice asi. El hijo fija umbrales de
  ventas, **retencion y referidos**, y por canal; el paso 3 de la madre solo
  habla de la proporcion de ventas y marketing. **Se reparte entre el paso 3 y
  el 5 y anade materia. Falla, pero por poco.**

**Y NO SE APLICA, por dos razones escritas, ninguna de ellas mia:**

1. **`OP-E-07.verificacion` dice literalmente lo contrario**: *"NO SE RELEE EL
   PAR: se lee su razon, que ya esta escrita."* Cambiar el carril de decision de
   esta operacion no es afinar una vara: es cambiar su criterio de verificacion.
2. **LA DERIVA DE CONTENIDO lo haria ademas poco fiable**, y ya esta medida y
   registrada en este mismo fichero (seccion de la vuelta 93, apartado **(d)**,
   medida por el auditor en el acta 92 seccion 4.4): de los 140 nodos que tocan
   los 87 pares de `OP-E-07`, **26** tienen hoy `pasos_accionables` distintos de
   los del encendido del bucle, y eso afecta a **32** de los 87 pares.
   **El ejemplar es justamente el nodo de esta mesa**: `fit_problema_solucion`
   tenia **6** pasos en `50f03099` (3 encajes de Value Proposition Design mas 3
   de traccion) y hoy tiene **3** (el bloque de traccion se fue en `cadc9977`,
   vuelta 53, LOTE A). **Las razones del 886 y del 1009 describen los seis
   pasos**, incluido el bloque de traccion que citan como lo valioso del par, y
   ese bloque **ya no esta en el nodo**. Leer el par hoy es leer un nodo
   distinto del que la razon describe.
   Y ese mismo apartado (d) ya dejo escrito que ampliar el carril es **una
   pregunta de ALCANCE y RESERVA DE FUNDADOR, no del bucle.**

### (e) LO QUE SE DECIDE, Y LO QUE NO

**NO HAY VARA CITABLE.** La unica que se puede escribir sin doctrina nueva
contradice tres adjudicaciones ya publicadas; la que si separaria exige cambiar
el criterio de verificacion escrito de la operacion, que es reserva de fundador.

**POR LA DECISION 2 DEL FUNDADOR, literal** (*"si no hay vara citable, los tres
quedan como estan y la duda va sellada a PENDIENTES"*):

> **EL 886, EL 890 Y EL 947 QUEDAN COMO ESTAN.** Siguen en
> `docs/plan/OP_E_07_DIRECCION_V94.jsonl` con su direccion registrada, sus
> aristas no se tocan, y **NINGUNA CIFRA DEL PLAN NI DEL MARCADOR SE MUEVE POR
> ESTA MESA.** La relectura conjunta queda **CERRADA SIN RETIRADAS**: de los
> cuatro que traia el acta 95, el 1844 salio de ella por la adjudicacion 4.1 y
> QUEDA, y estos tres quedan por falta de vara.

**CORRECCION DECLARADA, sin borrar el texto viejo.** El acta 95 (seccion 4.2,
linea 33795) escribio: *"Ninguna vara escrita hoy discrimina entre ellos, y por
eso los tres son duda genuina y no pereza."* **Esa frase queda RATIFICADA y
ahora esta MEDIDA, no solo afirmada**: la vara se escribio, se corrio contra las
19 adjudicaciones publicadas y contradijo 3. Lo que se corrige es el alcance de
la frase: el acta la dejo como impresion, y hoy es una medicion con fichero.

**LO QUE ESTA MESA SI DEJA GANADO, y no es poco:** el motivo de que no haya vara
ya no es *"nadie ha encontrado una"*, es **una causa nombrada y medida**: el
expediente decide unos pares leyendo la RAZON y otros leyendo los NODOS, y sobre
razones de la misma forma los dos carriles dan respuestas opuestas.

### (f) PENDIENTE DE DOCTRINA (`EJECUTOR.md` regla 5: no se para, se registra)

**LA PREGUNTA QUE NINGUNA REGLA ESCRITA CONTESTA HOY:** cuando la lectura ciega
del auditor (`AUDITOR.md` seccion 1.2, que **manda** imprimir primero los pasos
de los nodos y adjudicar sobre ellos) y el criterio de verificacion de la
operacion (`OP-E-07.verificacion`, que **manda** decidir por la razon y no
releer el par) apuntan a lados distintos, **cual manda**.

Las dos reglas estan vigentes, las dos se han aplicado, y **el expediente tiene
adjudicaciones publicadas de las dos clases**: el 1886 y el 1844 QUEDAN por
lectura de nodos, el 1009 y el 1098 SALIERON por lectura de razon. **No es una
contradiccion que se resuelva con las reglas de correccion existentes** (ninguna
de las cuatro adjudicaciones esta mal bajo la regla que la produjo), asi que no
se toca ninguna: **se registra la pregunta y se sigue**, como manda la regla 5.

**Lo mejor sostenido, mientras no haya doctrina:** cada operacion decide por SU
propio criterio de verificacion escrito (para `OP-E-07`, la razon), y la lectura
ciega del auditor sigue siendo control de calidad de la clase, no fuente de
direccion. **Es lo que ya se hace de hecho; lo que falta es que este escrito.**

**RESUELTO EN LA VUELTA 97, Y EL TEXTO DE ARRIBA NO SE BORRA** (`EJECUTOR.md`
regla 8: *"una correccion que tapa lo que corrige no se puede auditar"*). El acta
de la vuelta 96, seccion **4.5** (`docs/loop/ACTA_AUDITOR.md` linea **34381**,
leida hoy con `grep -n '^### 4\.'`), lo adjudica **POR EXTENSION CITABLE y NO
como doctrina nueva**, con esta letra: **manda el criterio escrito de la
operacion; la lectura ciega del auditor es control de la clase y detector de
discrepancia, NUNCA fuente de direccion.** Es lo mismo que este apartado dejo
escrito como "lo mejor sostenido", asi que **no cambia el trabajo**: lo que
faltaba era que estuviera escrito. La letra entera, con sus dos citas y con lo
que expresamente NO reabre, esta en la seccion **VUELTA 97, TAREA 1** apartado
**(1.3)** de este mismo fichero.

## VUELTA 96, TAREA 3: `OP-E-03` EMPIEZA A LEERSE. PRIMER TRAMO, 40 DE 183, CON SUS CINCO PUNTOS DE VERIFICACION CUMPLIDOS

**Origen:** encargo de la vuelta 96, TAREA 3, que recoge la parada deliberada y
bien puesta de la vuelta 95 (seccion "VUELTA 95, TAREA 5" de este mismo fichero:
el ejecutor leyo la nota de `OP-E-03`, vio que pedia el juicio COMPLETO del banco
`9.6.1` mas direccion, y paro en vez de abrirlo apurado al final de una vuelta ya
densa). **Esta vuelta lo abre con la vuelta entera por delante.**

### (a) LOS CINCO PUNTOS DE `OP-E-03.verificacion`, uno por uno, con lo que los cumple

Copiados literales del campo `verificacion` de la operacion
(`docs/plan/OPERACIONES.jsonl`, `id_op` `OP-E-03`), leidos hoy:

| punto de la verificacion | como se cumple, y donde se ve |
|---|---|
| *"se corre DESPUES del cierre de la cola del dominio, nunca antes"* | **REMEDIDO en esta vuelta**, no heredado: `docs/INTRA_DOMINIO_PARES.jsonl` **3.388 filas** y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` **3.388 filas**, contadas por el propio instrumento. Si no cuadran, cae en ROJO y no imprime nada |
| *"los ids pasan por el resolutor antes de comparar (regla P.1)"* | el resolutor se construye de `ids_alias` del grafo y se aplica a madre e hijo **antes** de cruzar contra la cola. Cada fila imprime el crudo al lado del resuelto cuando difieren, y una linea que dice si el resolutor movio algo. **En estas 40 no movio ninguno**, y se dice porque `P.1` obliga a declarar siempre si se resolvio |
| *"la cuenta cuadra sin fugas"* | ninguna de las 40 se repite dentro del tramo, ninguna resuelve a un par consigo mismo, y los **2.796 pares distintos de la cola tras resolver** se cruzan contra las 40: **cero coincidencias** |
| *"la diferencia se marca LECTURA DIRIGIDA: no entra en la cola y NO mueve el marcador del cribado"* | la marca va escrita en **cada** fila de la salida y en **cada** fila del JSONL (`marca`, `fuera_de_la_cola`, `mueve_el_marcador_del_cribado: false`). **El marcador no se toco**: sigue en A 551 / B 72 / C 5 / D 2.760, n 3.388, **remedido en esta vuelta** contando `INTRA_DOMINIO_VEREDICTOS.jsonl` por clase |
| *"sus veredictos se cuentan aparte de la tasa por dominio"* | la tabla por dominio se imprime **rotulada** como que NO entra en la tasa del banco `9.27`, y los veredictos viven en fichero propio, `docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl`, no en `INTRA_DOMINIO_VEREDICTOS.jsonl` |

### (b) LOS INSTRUMENTOS, Y QUE HACE CADA UNO

- `scripts/loop/vuelta96_tarea3_tramo1_opE03.py`: imprime el material entero de
  los 40 (par crudo y resuelto, el paso de la madre que el barrido caso con su
  texto, y los `pasos_accionables` ENTEROS de los dos nodos con titulo, fuente y
  entregable). Salida: `docs/loop/SALIDA_V96_TAREA3_TRAMO1_MATERIAL.txt`,
  **1.368 lineas** contadas con `wc -l`, EXIT 0. **No juzga nada.**
- `scripts/loop/vuelta96_tarea3_veredictos_tramo1.py`: recoge los veredictos de
  la lectura, los cruza uno a uno contra las filas reales del tramo y cuenta.
  Salida: `docs/loop/SALIDA_V96_TAREA3_VEREDICTOS.txt` y
  `docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl` (**40 filas**), EXIT 0.
- `scripts/loop/vuelta96_tarea3_prueba_mutacion.py`: las guardas, probadas.
  Salida: `docs/loop/SALIDA_V96_TAREA3_MUTACION.txt`, EXIT 0.

### (c) EL RESULTADO, TALLADO DE `SALIDA_V96_TAREA3_VEREDICTOS.txt`

Vara aplicada, citada y no inventada: banco **`9.6.1`** rama contenido manda
(*"Si lo que el hijo anade a lo que la madre ya dice CABE EN UNA LINEA, REPITE.
Si trae un PROCEDIMIENTO que la madre no tiene, CONTINUA"*), direccion por
**`9.6.2`**, y **`9.6.3`** para no dejar que el tamano del solape decida.

| clase | que significa | cuantas de 40 |
|---|---|---:|
| A | REPITE (lo que anade cabe en una linea) | 1 |
| B | DUDOSO (la vara no lo resuelve sola) | 1 |
| C | figura aparte | 0 |
| D | CONTINUA (trae procedimiento que el otro no tiene) | 38 |

- **A (1):** el par **12**, `human_error_como_sintoma` contra
  `preguntar_que_no_quien`, misma fuente (Dekker). Los pasos 1, 2 y 4 del segundo
  dicen con otras palabras lo que los pasos 1 y 2 del primero ya mandan; lo unico
  que anade es *"anota las condiciones de trabajo que rodeaban el momento"*, y
  **eso cabe en una linea**.
- **B (1):** el par **23**, `fit_problema_solucion` contra
  `value_proposition_startup`. El paso 3 del segundo ES el paso 2 del primero; lo
  que anade (identificar los problemas reales y definir que caracteristicas los
  resuelven) **es mas que una linea y menos que un procedimiento con logica
  propia**, y ademas son de fuentes distintas. **Se declara DUDOSO en vez de
  forzarlo.**
- **D (38):** el resto.

**LA DIRECCION (`9.6.2`), contada de la misma tabla:**

| resultado | cuantas |
|---|---:|
| direccion LEIDA y afirmada | **29** |
| direccion NO RESUELTA, declarada como tal | **11** (pares 11, 12, 15, 22, 23, 26, 32, 34, 35, 36, 37) |

**Las once no resueltas no son pereza y cada una dice por que en su razon**: en
unas el hijo hace algo ADYACENTE al paso y no lo ejecuta (11 construir no es
probar, 22 nombrar no es mandar ejecutar, 34 el MVP de alta fidelidad EMPIEZA
donde acaba el de baja, 35 definir la metrica no es afinar el motor, 36 coinciden
las personas y no la actividad, 37 el canal social no esta en ningun paso de la
madre); en otras **no hay madre e hijo en absoluto**, que es el caso 2.195 que el
propio banco `9.6.2` ya nombra (15 los dos lados del balance, 26 linea compartida
con procedimiento propio a cada lado, 32 el hijo REFUTA el paso en vez de
desarrollarlo); y en dos no hay pregunta de direccion porque el par no CONTINUA
(12 es A y 23 es B).

**POR DOMINIO, Y SE ROTULA: ESTA TABLA NO ENTRA EN LA TASA POR DOMINIO DEL BANCO
`9.27`**, se cuenta aparte como manda el punto 5 de la verificacion:

| dominio | pares del tramo | A | B | C | D |
|---|---:|---:|---:|---:|---:|
| core | 20 | 0 | 1 | 0 | 19 |
| environmental | 2 | 0 | 0 | 0 | 2 |
| franquicias | 2 | 0 | 0 | 0 | 2 |
| health_safety | 2 | 1 | 0 | 0 | 1 |
| quality | 14 | 0 | 0 | 0 | 14 |

### (d) LAS SEIS FIGURAS QUE LA LECTURA DESTAPA, y no son veredictos de par

Van enteras en `SALIDA_V96_TAREA3_VEREDICTOS.txt`. En corto, y las cuatro
primeras importan porque **la nota de la operacion dice que este barrido "ES
TAMBIEN UN DETECTOR DE GEMELOS"** y aqui se le ve haciendolo:

1. **Tres hijos de una misma linea, los tres de Crosby.** El paso 3 de
   `medicion_servicios` tiene TRES casas distintas en la bolsa:
   `make_certain_programa`, `programa_make_certain_3` y `programa_make_certain`
   (pares 2, 3 y 14). Los tres pares son D por separado. **La sospecha de gemelos
   es ENTRE LOS TRES HIJOS**, que es otra pregunta y otra operacion.
2. **Dos hijos de una misma linea, los dos de Blank.** El paso 3 de
   `waterfall_vs_agile_development` tiene dos:
   `desarrollo_de_clientes_customer_development` y `modelo_customer_development`
   (pares 13 y 20).
3. **Dos nodos de titulo casi identico, uno haciendo de madre y otro de hijo.**
   `estrategia_innovacion_producto` (madre del par 27) y
   `estrategia_de_innovacion_de_producto` (hijo del par 33), mismo libro
   (Cooper). **Es la forma que mas cuesta ver**, porque los dos papeles distintos
   disimulan el parecido.
4. **La familia de la capacidad de proceso, y el Gate 0 ya avisaba.**
   `capacidad_de_proceso`, `capacidad_del_proceso` y `capacidad_de_proceso_2`
   aparecen en los pares 8, 9, 18 y 25. El aviso informativo de Gate 0 **de esta
   misma vuelta** ya lista `capacidad_de_proceso <-> capacidad_del_proceso` con
   **97,6** de similitud de titulo. **La lectura corrobora el aviso desde otro
   camino**, y eso vale mas que cualquiera de los dos por separado.
5. **El barrido puede casar un paso con su propia refutacion.** Par 32: el paso
   *"Definir indices numericos de calidad de lote (AQL)"* de Juran quedo casado
   con `critica_acceptable_quality_level` de Crosby, que manda **eliminar** el
   AQL. **No es un defecto del barrido**: casa por vocabulario y el vocabulario no
   distingue desarrollar de refutar. Conviene tenerlo escrito **antes** de leer
   los 143 que quedan.
6. **Un par con la direccion INVERTIDA respecto a la etiqueta de la bolsa.** Par
   16: la bolsa etiqueta `madre=proceso_llamada_inicial_venta`, y la lectura da
   lo contrario (el flujo de ventas es la madre, y el guion de nueve pasos de la
   primera llamada cabe entero dentro de su paso 1). **Uno de 40, y es exactamente
   el error que el banco `9.6.2` nace para evitar**, asi que se cuenta y se nombra.

### (e) LAS GUARDAS, PROBADAS POR MUTACION, Y LA QUE SE DECLARA SIN PROBAR

`docs/loop/SALIDA_V96_TAREA3_MUTACION.txt`, EXIT 0. **Seis mutaciones y las seis
CAEN**, con el control en verde antes y despues:

| mutacion | que se muta | resultado |
|---|---|---|
| A | bolsa EN MEMORIA con un par que **si esta en la cola** | **CAE**, nombrando el par |
| B | corte del cribado esperado a 3389 sobre el dato real | **CAE** |
| C | una clase fuera de `{A,B,C,D}` | **CAE** |
| D | un veredicto renumerado a una fila que no existe | **CAE** |
| E | una direccion que nombra un nodo ajeno a esa fila | **CAE** |
| F | un veredicto que falta | **CAE**, nombrando la fila |

La mutacion **A** es la que mas importa: es la guarda que sostiene la
adjudicacion del 11 ago 2026 de esta operacion (*"una lectura que entra por dos
puertas se cuenta dos veces, y entonces la tasa por dominio del banco 9.27 deja
de significar nada"*), y ahora esta probado que dispara.

**Y LO QUE NO SE PRUEBA, DICHO EN VEZ DE FABRICARLE UN ROJO** (`EJECUTOR.md`
regla 1, parrafo final): **la CLASE A/B/C/D de cada par la pone la lectura y vive
en una TABLA A MANO. NO HAY CASO ROJO AUTOMATICO PARA ELLA.** No se le construye
una asercion que se apruebe sola, que es la caida 2 de la vuelta 89.

### (f) LO QUE QUEDA, Y EL RITMO MEDIDO

**143 de los 183 sin leer** (183 menos 40). El tramo siguiente empieza en la fila
41 y el instrumento ya lo acepta sin tocar codigo:
`--desde 40 --cuantos 40`. **CERO ARISTAS ESCRITAS O RETIRADAS por esta tarea**:
`OP-E-03` es LECTURA DIRIGIDA y su producto es el juicio, no el cableado; el
cableado de lo que estas lecturas habiliten es decision de otra operacion y de
otra vuelta.

## VUELTA 97, TAREA 1: LOS REGISTROS DEL ACTA 96 (acta de la vuelta 96, `ACTA_AUDITOR.md` lineas 34025 a 34536, leidas hoy)

**DE DONDE SALEN LAS LINEAS DE ESTA SECCION, para que se puedan volver a correr.**
Ninguna cita de linea esta tecleada de memoria (`EJECUTOR.md` regla 1, "LA CITA
LLEVA SU LINEA"). Los cortes del acta se leyeron HOY con
`grep -n '^# ACTA DE LA VUELTA 96\|^## [0-9]\.' docs/loop/ACTA_AUDITOR.md` y con
`grep -n '^### 4\.[1-6]' docs/loop/ACTA_AUDITOR.md`, y el final del acta con
`wc -l docs/loop/ACTA_AUDITOR.md`, que da **34536**: el acta 96 es la ultima del
fichero, asi que su cierre es el cierre del fichero.

**EL ESTADO DE LA TANDA ANTERIOR, tal como el acta lo escribe** (seccion 5, linea
**34434**): **CAIDAS DEL EJECUTOR EN ESTA TANDA: NINGUNA, DE NINGUNA ESPECIE**,
con las cinco especies en CERO (clase, cifra publicada, reporte, expediente,
incumplimiento de encargo). El acta lo llama *"la primera tanda de la campana sin
una sola caida"*. Se registra aqui sin adornarlo y sin rebajarlo, y **con el
freno delante**: la especie que cayo tres veces seguidas (la cuenta de piezas de
artefacto contada a ojo) se talla SIEMPRE, tambien las faciles.

### (1.1) LAS SEIS ADJUDICACIONES DEL ACTA 96, cada una por su numero, con su linea leida hoy y su efecto sobre el trabajo

| num | linea del acta | que adjudica | efecto sobre el trabajo |
|---|---:|---|---|
| **4.1** | 34274 | Discutible 1, LA VARA: **CONFIRMADO**, y probado en vez de opinado | **CIERRA la mesa.** Nada que rehacer |
| **4.2** | 34317 | Discutible 5, el "OCHO": **el ejecutor tiene razon**, la caida es del auditor | Correccion declarada, apartado **(1.2)** |
| **4.3** | 34356 | Discutibles 2, 4 y 6 (pares **26**, **16** y **23**): **CONFIRMADOS los tres** | **CIERRA** las tres clases del tramo 1. Nada que rehacer |
| **4.4** | 34367 | Discutible 3, las once direcciones no resueltas: **el umbral esta bien puesto** | **NO se toca el umbral** en el tramo de hoy |
| **4.5** | 34381 | El pendiente de doctrina: **NO ES PARADA**, adjudicado por extension citable | Marcado RESUELTO, apartado **(1.3)** |
| **4.6** | 34415 | La deriva de contenido: **citada bien**, y sigue **RESERVADA** | **NO se toca.** Sigue anotada para Alexis y sin encargar |

**LA 4.1, CON SU CIFRA (linea 34274).** El acta acepta la invitacion que el
reporte de la vuelta 96 le hizo (*"si el auditor construye una vara que las
reproduzca todas, mi conclusion cae"*) y construye **TRECE varas distintas**
sobre el texto de la razon, corridas contra las **19 adjudicaciones publicadas**.
Su veredicto, literal en la linea **34297**: **"NINGUNA DE LAS TRECE REPRODUCE
LAS DIECINUEVE."** La mejor llega a **17 de 19** (mejor que la del ejecutor, que
llego a 14 de 19) y **sigue contradiciendo dos adjudicaciones publicadas**, el
**1281** y el **1992**, con lo cual **cae por la misma vara con la que el ejecutor
descarto la suya**. Adjudicacion literal, linea **34307**: *"la conclusion 'NO HAY
VARA CITABLE' se sostiene, y ahora esta medida con trece intentos y no con uno"*.

**Y el segundo resultado de la 4.1, que es el que de verdad cierra la mesa:** las
**tres** varas que llegan a 17 dicen **QUEDA a los tres pares de la mesa** (886,
890 y 947). O sea que **el destino de los tres no depende de la vara elegida**.
Los tres **QUEDAN COMO ESTAN** y la duda queda sellada, que es la rama que la
decision 2 del fundador escribio.

**Lo que la 4.1 deja dicho sin llamarlo caida, y se registra igual porque es
material para quien vuelva sobre la mesa:** la vara que el ejecutor eligio **no
era la mas fuerte disponible** (14 de 19 contra 17 de 19). El acta explica por
que no es caida: *"el propio ejecutor marco esa eleccion como su discutible
numero 1 y pidio justo esta prueba"*.

**LA 4.3, CON LOS TRES PARES NOMBRADOS (linea 34356).** El auditor leyo los tres
a ciegas antes de destapar y **coincide en los tres**: el **26** es **D** y no A
(dos de las tres instrucciones que anade, la interdependencia hardware y software
y el cronograma estable, **no aparecen en ninguna forma en el otro nodo**, y el
`titulo_ratio` 91,7 es senal de titulo, que por banco `9.6.3` no decide); el
**16** lo leyo **invertido por su cuenta**, o sea que la direccion contraria a la
etiqueta de la bolsa se sostiene con dos lecturas independientes; y el **23** es
**B** porque *"ninguno contiene al otro"*.

**LA 4.4, QUE ES LA QUE MANDA SOBRE EL TRABAJO DE HOY (linea 34367).** El
ejecutor sospecho de si mismo (*"once de cuarenta es mucho"*) y nombro las cinco
que con un umbral mas laxo se afirmarian: **11, 22, 35, 36, 37**. El auditor
**leyo las cinco a ciegas y llego a NO RESUELTA en las cinco por su cuenta**, en
tres de ellas con el mismo argumento. Adjudicacion literal, linea **34374**: *"el
umbral esta bien puesto y no se toca"*. Su ejemplar zanjador es el **36** (PR a
los franquiciados contra referidos DE los franquiciados: comparten *"las personas
y nada mas"*). **CONSECUENCIA OPERATIVA, escrita aqui para que el tramo de hoy no
la olvide: NO se baja el umbral de direccion para que salgan menos no resueltas.
Si el tramo 2 da una proporcion parecida, es la bolsa, no la vara.**

**LA 4.6, Y LO QUE NO SE HACE CON ELLA (linea 34415).** La deriva de contenido
(**26** nodos de 140 y **32** pares de 87, medida por el auditor en el acta 92
seccion 4.4) queda **verificada en su atribucion y en su ejemplar**: el auditor
remidio `fit_problema_solucion` y da **6 pasos en el encendido** contra **3 hoy**.
Cierre literal, linea **34431**: *"la deriva sigue siendo lo que el acta 92 dijo:
ANOTADA para Alexis y NO encargada, porque roza el ALCANCE de la campana"*. **NO
se toca en esta vuelta**, y citarla como contraste con su fuente nombrada es la
forma correcta de usarla.

### (1.2) LA CORRECCION DECLARADA DEL "OCHO": ES UNA CAIDA DE ACTA DEL AUDITOR Y VA NOMBRADA COMO TAL, sin borrar el texto viejo

**QUIEN CAYO, CON SU NOMBRE.** No es una caida del ejecutor. Es una **CAIDA DE
ACTA DEL AUDITOR**, y el propio auditor la lleva a su seccion de errores con
nombre (`ACTA_AUDITOR.md` seccion 6 punto 1, linea **34457**, leida hoy).

**EL TEXTO VIEJO, QUE NO SE BORRA** (`EJECUTOR.md` regla 8): el acta de la vuelta
**95** publico que **OCHO** de las razones del grupo C llevaban *"la formula
literal es/son UNA LINEA"*, y enumero `[896, 909, 910, 940, 993, 1057, 1086, 1196]`.

**LA CORRECCION, adjudicada en la seccion 4.2 del acta 96 (linea 34317) y
literal en la linea 34350** (*"la discrepancia del ejecutor es CORRECTA. El
'ocho' es MIO y esta mal"*): de las **NUEVE** razones del grupo C que mencionan
la palabra "linea", **SEIS** llevan la formula **estricta** *"es/son UNA (sola)
LINEA"* y **SIETE** la **ancha** *"es/son ... linea"*, mas el **1086** (que ancla
con **EN** y no con **ES/SON**) y el **983** (que va tras dos puntos).

**LOS DOS SOBRANTES DEL OCHO, leidos en su texto por el auditor:** el **909** dice
*"sus dos referencias al mapa son lineas"*, plural y sin determinante, que no es
*"son UNA LINEA"*; y el **1086** dice *"cierra con tres preguntas en una sola
linea"*, que ancla con **EN**.

**LO QUE VUELVE LA CORRECCION INDISCUTIBLE, y lo dice el auditor de si mismo:**
su propia acta 95 diagnostica, dos parrafos antes, que el fallo del patron era
confundir *"EN una linea"* con *"ES una linea"*, **y acto seguido mete el 1086
(que es un "EN una linea") dentro del conjunto rotulado "formula literal es/son
UNA LINEA"**. Se contradijo dentro del mismo texto.

**NO SE REMIDE EN ESTA VUELTA, y se dice por que en vez de dejarlo implicito**
(encargo de la vuelta 97, TAREA 1.2, literal: *"NO SE REMIDE: ya viene medida dos
veces"*). Las dos mediciones existen y son independientes: la del ejecutor en la
vuelta 96 (`scripts/loop/vuelta96_tarea1c_etiqueta_grupo_c.py`, salida en
`docs/loop/SALIDA_V96_TAREA1C_ETIQUETA_GRUPO_C.txt`) y la del auditor con regex
propias y sin importar aquel codigo (`_auditor_v96_grupoc.py`). **Salieron
identicas, enumeraciones incluidas.** Correr una tercera no anade vara: anade
ruido.

**LO QUE NO CAMBIA:** la **CONCLUSION** que el auditor saco del grupo C sigue en
pie y no se toca. **Lo que cae es la ETIQUETA**, no el juicio.

### (1.3) EL PENDIENTE DE DOCTRINA DE LA VUELTA 96 APARTADO (f): QUEDA RESUELTO, y se marca como resuelto sin borrar su texto

**DONDE ESTA EL TEXTO VIEJO:** seccion "VUELTA 96, TAREA 2" apartado **(f)** de
este mismo fichero, **intacto**, con la marca de resuelto **anadida debajo** y
nada borrado.

**LA PREGUNTA QUE ABRIO:** cuando la lectura ciega del auditor (`AUDITOR.md`
seccion 1.2) y el criterio de verificacion de una operacion
(`OP-E-07.verificacion`) apuntan a lados distintos, **cual manda**.

**QUE HIZO BIEN EL EJECUTOR, y el acta lo dice expresamente (linea 34381):** no
paro. Registro lo mejor sostenido, lo marco PENDIENTE DE DOCTRINA y siguio, que
es literalmente lo que manda `EJECUTOR.md` regla 5.

**LA ADJUDICACION, Y SU CLASE: POR EXTENSION CITABLE, NO DOCTRINA NUEVA.** El
auditor esta obligado por `AUDITOR.md` seccion 3 a mirar primero si una regla ya
escrita lo cubre por extension natural, y encuentra que **la cubre su propio
protocolo**, con dos citas:

- **`AUDITOR.md` seccion 1.2** define la relectura ciega **por lo que produce**:
  *"Registra cuantos coinciden, cuantos discrepan, y la METRICA DE CREDITO"*. Es
  un **contador de coincidencia**, o sea un control de calidad. **En ningun punto
  dice que adjudique la direccion de un par.**
- **`AUDITOR.md` seccion 1.3** dice que pasa cuando discrepan y no deja hueco:
  las discrepancias van a relectura conjunta, *"el ejecutor verifica contra el
  grafo y **decide con la vara**"*. **La vara decide. La lectura ciega detecta.**

**LA LETRA, literal del acta linea 34402:** *"manda el criterio escrito de la
operacion. La lectura ciega del auditor es control de la clase y detector de
discrepancia, nunca fuente de direccion."*

**NO CAMBIA EL TRABAJO, y por eso no hay nada que rehacer.** Es exactamente "lo
mejor sostenido" que el ejecutor dejo escrito en el apartado (f). Lo unico que
faltaba era que estuviera escrito, y con esta adjudicacion lo esta.

**LO QUE EXPRESAMENTE NO REABRE, y se registra porque es la mitad util de la
adjudicacion:** las adjudicaciones ya publicadas por el carril de los **PASOS**
(el **1886** y el **1844**, actas 93 y 95) y por el carril de la **RAZON** (el
**1009** y el **1098**) **quedan como estan**. La adjudicacion **fija cual manda
de aqui en adelante**; no retrocede sobre lo publicado.

## VUELTA 97, TAREA 2: `OP-E-03`, SEGUNDO TRAMO. SESENTA PARES MAS, Y LA BOLSA QUEDA LEIDA HASTA LA FILA 100 DE 183

Filas **41 a 100** de `docs/plan/DIFERENCIA_CONTRA_COLA.jsonl`, leidas con
`python scripts/loop/vuelta96_tarea3_tramo1_opE03.py --desde 40 --cuantos 60`,
que es el instrumento de la vuelta 96 **sin tocarle una linea de codigo**, como el
encargo manda. Material entero en
`docs/loop/SALIDA_V97_TAREA2_TRAMO2_MATERIAL.txt`, **2.070 lineas** contadas del
fichero con `wc -l`, EXIT 0, y **60 filas** casadas por el tallador de
composicion (`docs/loop/SALIDA_V97_TAREA2_MATERIAL_COMPOSICION.txt`, EXIT 0).

**UNA HONESTIDAD SOBRE LA CABECERA DEL MATERIAL, dicha en vez de callada.** El
instrumento se llama `..._tramo1_...` y su cabecera imprime *"PRIMER TRAMO DE
LECTURA DIRIGIDA (vuelta 96, TAREA 3)"* tambien cuando se le pasa `--desde 40`:
ese rotulo es del fichero de la vuelta 96 y **no depende de los argumentos**. La
linea que si depende de ellos, y que es la que manda, dice *"Este tramo: filas 41
a 100 (60 pares)"* y es correcta. **No se corrigio el rotulo** porque el encargo
dice expresamente que el auditor probo que el instrumento acepta el salto **sin
tocar codigo**, y tocarlo aqui habria cambiado la vara a mitad de la medicion.

**LA LECTURA NO SE DEGRADO Y POR ESO NO SE PARO.** El encargo autoriza a parar a
mitad del tramo si la lectura se degrada, diciendolo con la cifra. Se leyeron los
**60** con el mismo detenimiento; no hubo parada y se dice para que el silencio
no tenga que interpretarse.

### (a) LOS CINCO PUNTOS DE `OP-E-03.verificacion`, REMEDIDOS EN ESTA VUELTA Y NO HEREDADOS DEL TRAMO 1

Salida en `docs/loop/SALIDA_V97_TAREA2_CINCO_PUNTOS.txt`. Cada cifra sale de
correr algo hoy, no de leer el reporte de la vuelta 96.

| punto de la verificacion | como se cumple HOY, con su medicion |
|---|---|
| **1.** se corre DESPUES del cierre de la cola, nunca antes | el instrumento **recuenta** las filas de los dos ficheros del cribado y cae en ROJO si no dan 3.388. Recontado aparte en esta vuelta: `INTRA_DOMINIO_PARES.jsonl` **3.388** e `INTRA_DOMINIO_VEREDICTOS.jsonl` **3.388** |
| **2.** los ids pasan por el RESOLUTOR antes de comparar (`P.1`) | madre e hijo se resuelven antes de cruzar nada. **En estas 60 el resolutor no movio ningun id**, y se declara igual **porque `P.1` obliga a declararlo siempre**, tambien cuando no cambia nada |
| **3.** la cuenta cuadra sin fugas | **cero** de las 60 esta ya en la cola tras resolver, contra los **2.796** pares distintos de la cola; **cero** repetidas dentro del tramo; los 60 puestos van del 41 al 100 y son **60 distintos** |
| **4.** se marca LECTURA DIRIGIDA, no entra en la cola y NO mueve el marcador | escrito en **las 60** filas del material y en **las 60** del JSONL, contadas: `marca` 60 de 60, `fuera_de_la_cola` 60 de 60, `mueve_el_marcador_del_cribado` false 60 de 60. Y verificado por fuera: `git diff --stat` de los dos ficheros del cribado y de `dataset/` da **VACIO** |
| **5.** los veredictos se cuentan APARTE de la tasa por dominio | viven en fichero propio, `docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl` (**60 filas** contadas), y la tabla por dominio va **rotulada** en su salida como que NO entra en la tasa del banco `9.27` |

### (b) LOS INSTRUMENTOS, Y QUE HACE CADA UNO

| instrumento | que hace | salida |
|---|---|---|
| `vuelta96_tarea3_tramo1_opE03.py --desde 40 --cuantos 60` | imprime el material entero (paso casado con su texto, y los `pasos_accionables` ENTEROS de los dos nodos). **De la vuelta 96, sin tocar** | `SALIDA_V97_TAREA2_TRAMO2_MATERIAL.txt` |
| `vuelta97_tarea2_veredictos_tramo2.py` | pone la tabla de los 60 veredictos y la cruza contra el material. **IMPORTA `construir_filas()` del hermano de la vuelta 96 en vez de copiarlo**: el armazon es literalmente el mismo codigo ya probado | `SALIDA_V97_TAREA2_VEREDICTOS.txt` y el JSONL |
| `vuelta97_tarea2_senal_de_la_bolsa.py` | **NUEVO.** Mide la senial objetiva de la bolsa por tramo y la cruza contra los veredictos de direccion ya escritos | `SALIDA_V97_TAREA2_SENIAL.txt` |
| `vuelta97_tarea2_prueba_mutacion.py` | muta las guardas y comprueba que CAEN | `SALIDA_V97_TAREA2_MUTACION.txt` |

### (c) EL RESULTADO, TALLADO DE `SALIDA_V97_TAREA2_VEREDICTOS.txt` Y NO TECLEADO

Las tres tablas se pegan enteras de ese fichero, que es quien las imprime
contando la tabla de veredictos (`EJECUTOR.md` regla 1, "LA TABLA SE CUENTA DE SU
FICHERO").

| clase | que significa | cuantas de 60 |
|---|---|---:|
| A | REPITE (lo que anade cabe en una linea) | 3 |
| B | DUDOSO (la vara no lo resuelve sola) | 1 |
| C | figura aparte | 0 |
| D | CONTINUA (trae procedimiento que el otro no tiene) | 56 |

Enumeraciones del mismo fichero: **A (3): 42, 88, 100. B (1): 47. C (0): ninguna.**

| direccion (banco `9.6.2`) | cuantas |
|---|---:|
| LEIDA y afirmada | 33 |
| NO RESUELTA, declarada como tal | 27 |

| dominio | pares del tramo | A | B | C | D |
|---|---:|---:|---:|---:|---:|
| core | 22 | 1 | 1 | 0 | 20 |
| environmental | 3 | 0 | 0 | 0 | 3 |
| exportacion | 3 | 0 | 0 | 0 | 3 |
| health_safety | 2 | 1 | 0 | 0 | 1 |
| quality | 29 | 1 | 0 | 0 | 28 |
| risk_management | 1 | 0 | 0 | 0 | 1 |

**ESTA TABLA POR DOMINIO NO ENTRA EN LA TASA DEL BANCO `9.27`** y va rotulada asi
en su propio fichero de salida.

**LOS TRES A, nombrados:** el **42** (`cultura_justa_2` contra
`preguntar_que_no_quien`, y es el segundo par del archivo en que este hijo sale A
contra una madre de Dekker, el primero fue el par 12 del tramo 1); el **88**
(`genchi_gembutsu_salir_del_edificio` de Ries contra `get_out_of_the_building` de
Blank, dos casas del mismo consejo en dos libros); y el **100**
(`desarrollar_metas_anuales` contra `metas_negocio_calidad`, donde la madre ya
barre las areas, ya exige meta medible con plazo y ya la mete en el plan de
negocio).

**EL UNICO B es el par 47** (`reporte_estado_miembro_equipo` contra
`variance_analysis`), y se declara DUDOSO en vez de forzarlo: **la direccion si se
lee**, lo que la vara no resuelve sola es la clase. Quitado lo que la madre ya
dice, al hijo le queda extender la comparacion a cronograma y calidad y calcular
la magnitud de la variacion: mas que una linea y menos que un procedimiento
propio.

**EL UMBRAL DE DIRECCION NO SE TOCO**, por adjudicacion expresa del acta 96
seccion 4.4 (`ACTA_AUDITOR.md` linea **34367**, leida hoy).

### (d) LA PROPORCION DE DIRECCIONES NO RESUELTAS SUBE, Y SE MIDE EN VEZ DE EXPLICARSE

**LA CIFRA, primero, sin suavizarla.** El tramo 1 dejo **11 de 40** sin direccion
(**27,5%**); el tramo 2 deja **27 de 60** (**45,0%**). **NO es "una proporcion
parecida"**, que es el caso que el encargo previo (*"Si el segundo tramo da otra
proporcion parecida, es la bolsa, no tu vara"*). Como la premisa de esa frase no
se cumple, **no se puede invocar su conclusion**, y en vez de invocarla se
construyo un instrumento que la ponga a prueba:
`scripts/loop/vuelta97_tarea2_senal_de_la_bolsa.py`, salida en
`docs/loop/SALIDA_V97_TAREA2_SENIAL.txt`, EXIT 0.

**LA SENIAL DE LA BOLSA POR TRAMO**, tabla pegada entera de ese fichero. Los ids
pasan por el resolutor antes de leer la fuente de cada nodo (`P.1`):

| tramo | filas | mediana de `titulo_ratio` | madre e hijo de la MISMA fuente |
|---|---:|---:|---:|
| tramo 1 (filas 1 a 40) | 40 | 84.3 | 33 de 40 (82.5%) |
| tramo 2 (filas 41 a 100) | 60 | 78.2 | 44 de 60 (73.3%) |
| sin leer (filas 101 a 183) | 83 | 76.2 | 62 de 83 (74.7%) |

**LA BOLSA VIENE ORDENADA DE MAS FUERTE A MAS DEBIL**, y eso no se sabia escrito
en ningun sitio: la mediana de `titulo_ratio` baja **84,3 a 78,2 a 76,2** tramo
tras tramo. **El tramo 2 no es una muestra equivalente al tramo 1: es un tramo mas
debil de la misma bolsa.**

**EL CRUCE, que es la parte que de verdad prueba algo**, porque parte las 60 filas
por lo que la lectura decidio (leido del JSONL, no de una lista tecleada) y mide
la senial OBJETIVA de cada mitad:

| grupo del tramo 2 | filas | mediana de `titulo_ratio` | madre e hijo de la MISMA fuente |
|---|---:|---:|---:|
| direccion LEIDA | 33 | 81.5 | 26 de 33 (78.8%) |
| direccion NO RESUELTA | 27 | 77.3 | 18 de 27 (66.7%) |

**Las filas que la lectura no resolvio son, medidas por fuera de la lectura, las
mas debiles de la bolsa.** Las dos afirmaciones que el instrumento comprueba salen
**VERIFICADAS** las dos, y las dos **podian salir en rojo** (su mutacion esta
probada en el apartado (f)).

**LO QUE ESTO NO PRUEBA, Y SE DICE AQUI CON TODAS LAS LETRAS PARA QUE NADIE LO LEA
DE MAS:** **no prueba que mi umbral sea el correcto.** Una vara demasiado estricta
aplicada a una bolsa que se debilita produciria exactamente estas dos mismas
seniales. Lo unico medido es que **la bolsa se debilita** y que **la senial
objetiva acompania a la lectura**. Si el umbral esta bien puesto lo adjudica el
auditor, no este fichero, y va **marcado como discutible** en el reporte.

### (e) LAS NUEVE FIGURAS QUE LA LECTURA DESTAPA, REGISTRADAS Y SIN ADJUDICAR

Mismo trato que las seis del tramo 1, por mandato del encargo (*"Si el tramo 2
destapa figuras nuevas, mismo trato"*): **se registran y no se adjudican**, porque
las sospechas de gemelos entre nodos son otra pregunta y otra operacion. Estan
impresas enteras en `SALIDA_V97_TAREA2_VEREDICTOS.txt`. Resumidas:

1. **LOS GEMELOS DE LA ESTRATEGIA DE INNOVACION, y esta vez el tramo trae LOS
   DOS.** `estrategia_de_innovacion_de_producto` es madre del par 45 y
   `estrategia_innovacion_producto` es hijo del par 84: ids que se diferencian en
   dos preposiciones, mismo libro (Cooper), y arenas estrategicas, metas
   vinculadas al negocio y asignacion de recursos en los dos. **Corrobora desde un
   segundo camino la figura que el tramo 1 ya registro.**
2. **LOS GEMELOS DEL TIEMPO DE CICLO.** `reduccion_de_tiempo_de_ciclo` (par 63) y
   `reduccion_tiempo_ciclo` (par 70): una preposicion de diferencia en el id, mismo
   libro, mismo titulo salvo dos palabras. **Misma especie que la familia de la
   capacidad de proceso del tramo 1.**
3. **LA FAMILIA CROSBY DE LOS 14 PASOS, REPARTIDA Y MAL EMPAREJADA.**
   `costo_de_calidad_3` ("Paso 4"), `fijacion_de_metas` ("Paso 10"),
   `dia_cero_defectos_2` y `eliminacion_causas_error_4` son capitulos del mismo
   programa, cuya madre `programa_mejora_calidad_14_pasos` **esta en la propia
   bolsa**. El `costo_de_calidad_3` sale en **tres filas seguidas** (81, 82, 83)
   con tres madres distintas y la misma senial 84,4, y **solo la del 83 es la
   suya**.
4. **LOS NODOS IMAN.** Un hijo que el barrido cuelga de varias madres sin serlo:
   `costo_de_calidad_3` (81, 82, 83), `optimizacion_caracteristicas_diseno` (56,
   72), `key_process_product_characteristics` (68, 90),
   `validar_modelo_negocio_hechos` (62, 69), y
   `recursos_apoyo_gubernamental_exportacion` de madre con el MISMO paso 3 (55,
   65). **Propiedad del barrido que conviene tener escrita antes de leer los 83 que
   quedan.**
5. **EL MISMO NODO DE MADRE EN UNA FILA Y DE HIJO EN OTRA, y son DOS casos
   distintos que no hay que confundir.** `pre_control_estadistico` (madre en 51,
   hijo en 60) **si es figura**, porque las dos filas son falsos amigos.
   `posicionamiento_por_tipo_de_mercado` (hijo en 92, madre en 52) **NO es
   figura**: las dos filas juntas dibujan una **cadena de tres niveles**, que es la
   forma sana que el caveat de la `9.6.1` ya nombra.
6. **EL TRIO DE SALIR DEL EDIFICIO, en dos libros.**
   `get_out_of_the_building` (Blank), `genchi_gembutsu_salir_del_edificio` (Ries) y
   `customer_discovery_get_out_of_building` (Blank, madre del par 46).
7. **EL FALSO AMIGO POR NOMBRE PROPIO COMPARTIDO:** "NDA" (44, donde la madre dice
   NUNCA pidas NDA a un VC y el hijo dice EXIGE NDA bidireccional al comprador),
   "Energy Star" (67) y "Business Model Canvas" (79). **El ejemplar mas limpio es
   el 95:** *espacios de oportunidad* de un analisis de mega-tendencias contra
   *costo de oportunidad* de un libro de finanzas.
8. **EL BARRIDO VUELVE A CASAR UN PASO CON SU REFUTACION, y ahora es una escuela
   contra otra.** El tramo 1 registro el AQL de Juran contra la critica de Crosby;
   aqui hay **dos** filas entre Juran y Deming con `pre_control_estadistico` en
   medio (51 y 60): PRE-Control centra el proceso entre los limites de
   ESPECIFICACION y el nodo de Deming manda **nunca** ajustar por si un punto cae
   dentro o fuera de especificacion. **No es un defecto del barrido: es material
   real de dos escuelas en tension**, y quien cablee esta zona tiene que saberlo.
9. **UN NODO DE QUINCE PASOS QUE PARECE DOS CASAS.** `causas_comunes_vs_especiales`
   (par 80): del paso 1 al 9 mecanica de control estadistico, del 10 al 15 cultura
   de no buscar culpables. **Sin adjudicar:** partir un nodo es otra pregunta.

### (f) LAS GUARDAS, PROBADAS POR MUTACION, Y LO QUE SE DECLARA SIN PROBAR

`scripts/loop/vuelta97_tarea2_prueba_mutacion.py`, salida en
`docs/loop/SALIDA_V97_TAREA2_MUTACION.txt`, EXIT 0. Cifras del pie **contadas por
el propio instrumento y no tecleadas**: **12 de 12 comprobaciones se comportan
como deben, 6 mutaciones que tenian que caer y 6 controles verdes.**

**LAS SEIS MUTACIONES, Y LAS SEIS CAEN:** (1) una clase pasa a `X`; (2) un puesto
aparece dos veces; (3) la direccion de un par nombra dos nodos de OTRA fila; (4)
se quita un veredicto de los 60; (5) `normaliza_fuente` se muta a constante y la
afirmacion 2 deja de sostenerse (los dos grupos pasan a 100,0%); (6) el
`titulo_ratio` del tramo 2 se sube a 99,0 y la afirmacion 1 deja de sostenerse.
**Control verde antes y despues**, con la tabla real y los datos reales.

**LO QUE SE DECLARA EN VEZ DE FABRICARLE UN ROJO QUE SE APRUEBE SOLO**
(`EJECUTOR.md` regla 1, "EL CASO ROJO SE PRUEBA POR MUTACION"): **la CLASE y la
DIRECCION de cada uno de los 60 pares son una TABLA A MANO y NO TIENEN CASO ROJO
AUTOMATICO.** No existe dentro del repo una segunda fuente independiente contra la
que contrastarlas, asi que **no hay nada que mutar**. Su control es la relectura
ciega del auditor, no un `assert`.

### (g) LO QUE QUEDA, Y LO QUE NO SE MOVIO

**CERO ARISTAS ESCRITAS O RETIRADAS.** `OP-E-03` es LECTURA DIRIGIDA y su producto
es el juicio, no el cableado. **Ninguna cifra del plan, del marcador ni de la tasa
por dominio se mueve por esta tarea**, y esta verificado y no supuesto:
`git diff --stat` de los dos ficheros del cribado y de `dataset/` da **VACIO**.

**QUEDAN 83 SIN LEER**, filas 101 a 183. La bolsa esta leida hasta la **100 de
183**. El instrumento acepta `--desde 100 --cuantos N` sin tocar codigo, y **el
tramo que venga es el mas debil de los tres** (mediana de `titulo_ratio` 76,2),
cosa que ahora esta medida y escrita en vez de descubrirse leyendo.
