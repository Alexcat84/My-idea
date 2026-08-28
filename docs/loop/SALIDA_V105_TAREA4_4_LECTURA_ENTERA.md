# VUELTA 105, TAREA 4.4: LECTURA ENTERA A CIEGAS DE LOS SIETE SATELITE

Los 7 puestos que la TAREA 4.3 clasifico SATELITE (`docs/loop/SALIDA_V105_TAREA4_3_RE_BARRIDO.txt`):
**20, 21, 38, 66, 87, 91, 93**. Los pares **20** y **93** los cierra la TAREA 3 (relectura conjunta
con el auditor, `correccion_v105` ya aplicada, los dos SE MUEVEN). Este fichero cubre los
**cinco restantes: 21, 38, 66, 87, 91**, cada uno con los dos nodos enteros leidos hoy y el banco
**9.6.2** y **9.6.3** enteros. SATELITE no es sinonimo de que se mueva (encargo, 4.4): dos de los
cinco SOSTIENEN.

## 21 — `build_measure_learn` (paso 0) -> `value_proposition_canvas`

Paso: "Generar una hipotesis clara **a partir de** los Canvas de Value Proposition y Business
Model." El complemento de origen nombra el Canvas como **insumo ya construido**; el hijo describe
como **construir** ese Canvas (plantilla, dibujar Customer Profile y Value Map, iterar hasta el
Fit, comunicar, usar como scoreboard). Primer brazo del 9.6.2 falla: el hijo es el procedimiento
que PRODUCE el insumo, no el acto de generar una hipotesis a partir de el. Entregables sin
relacion: "ciclo completo de Build-Measure-Learn" contra "Canvas completo". **SE MUEVE.**
`correccion_v105`.

## 38 — `obtencion_compromiso` (paso 4) -> `enfoque_etapa_investigacion`

Paso: "Pon tu esfuerzo de mejora en las etapas de investigacion **Y** demostracion de capacidad,
no en el cierre" (dos etapas nombradas). El hijo cubre SOLO investigacion, y su propia tesis
("las etapas de Demostracion... fluyen naturalmente") dice explicitamente que NO hace falta
invertir esfuerzo en la otra mitad que el paso tambien nombra. Primer brazo del 9.6.2 falla.
Comparten precursor comun (`cuatro_etapas_llamada_de_ventas`) sin relacion madre-hijo: 9.6.3, SANO.
Entregables distintos: lista de avances validos por etapa contra checklist de tiempo en preguntas.
**SE MUEVE.** `correccion_v105`.

## 66 — `cultura_justa_3` (paso 3) -> `cultura_de_aprendizaje`

Paso: "Balancear la necesidad de accountability **con** la proteccion al aprendizaje
organizacional" (un acto de EQUILIBRIO entre dos fuerzas). El hijo desarrolla solo el lado del
aprendizaje (mecanismos de analisis de datos, reformas, medicion, revision institucionalizada);
cero lineas sobre accountability, sanciones o la tension entre los dos. Primer brazo del 9.6.2
falla: no desarrolla el balance, solo uno de los dos platillos. Libros distintos (Dekker contra
Reason); `cultura_de_aprendizaje` declara a `cultura_justa` (componente hermano, no
`cultura_justa_3`) entre sus previos: dos componentes PARES del modelo de Reason, no madre-hijo.
9.6.3: raiz comun (cultura de seguridad), procedimiento propio a cada lado, SANO. Entregables sin
relacion: politica de justicia con accountability contra proceso de revision de lecciones
aprendidas. **SE MUEVE.** `correccion_v105`.

## 87 — `emprendedor_como_puesto_de_trabajo` (paso 2) -> `contabilidad_innovacion_pivote`

Paso: "Evalua ese trabajo **con** la contabilidad de innovacion, no con las metricas tradicionales
de un puesto operativo." El hijo ES el metodo nombrado: documentar hipotesis de salto de fe,
medir metricas accionables por iteracion, comparar contra predicciones, evitar exito declarado por
metricas de vanidad. Evaluar CON la contabilidad de innovacion exige desplegarla: mismo patron
canonico que la linea que tarda varios pasos en ejecutarse (9.6.2). La madre conserva materia
propia (crear el puesto, reentrenar tras exito, ampliar el sandbox) que el hijo no toca. La senal
de entregables APOYA en vez de contradecir: el entregable de la madre incluye explicitamente "su
propia forma de medir resultados", que es exactamente lo que el hijo entrega (reporte de metricas
accionables). **SOSTIENE.** Sin correccion.

## 91 — `gestion_de_portafolio_gates_go_kill` (paso 2) -> `tipos_criterios_gate`

Paso: "Establecer gates o puntos de decision formales **con** criterios visibles de Go/Kill." El
hijo desarrolla exactamente la taxonomia de esos criterios (must-meet, go/kill, should-meet;
checklist, umbral financiero, scorecard; consistencia entre gates; ajuste por tipo de proyecto):
es la elaboracion directa de "criterios visibles" que el paso nombra. No se confunde con el paso 3
de la propia madre (evaluar con los SEIS criterios especificos del portafolio, un contenido
distinto: estrategico, ventaja competitiva, etc.). La madre conserva materia propia (embudo,
evaluacion con los seis criterios, decisiones de matar, balance del portafolio) que el hijo no
toca. Entregables con solape directo: el entregable de la madre nombra "gates definidos, criterios
de evaluacion documentados" como parte de si mismo, y eso es exactamente lo que el hijo entrega.
**SOSTIENE.** Sin correccion.

## RESUMEN

De los 5 leidos aqui: **3 SE MUEVEN** (21, 38, 66), **2 SOSTIENEN** (87, 91). Sumados a los 2 de la
TAREA 3 (20, 93, los dos MUEVEN): de los 7 SATELITE totales, **5 se mueven y 2 sostienen**.
Recomputo con `scripts/loop/contar_cierre_efectivo.py`
(`docs/loop/SALIDA_V105_TAREA4_4_CIERRE_EFECTIVO.txt`): **clase A 3, B 2, C 1 (par 111), D 177;
direccion leida y afirmada 74, NO RESUELTA 109 (59,6%); invertidas 2 (pares 16, 114).** LA CIFRA
VIGENTE AL CIERRE DE ESTA VUELTA ES **74 / 109 (59,6%)**.
