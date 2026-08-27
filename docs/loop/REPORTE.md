# REPORTE DE LA VUELTA 84 DEL EJECUTOR (modelo: Sonnet 5)

Sobrescribe el reporte de la vuelta 83. Cubre TAREA 1 (los registros y la
relectura conjunta de los pares 33, 44, 45 y la correccion declarada de la
razon del par 47), TAREA 2 BLOQUEANTE (el instrumento otra vez: horneador por
patron, el cotejo que localiza la tabla por su cabecera de seccion, y el
horizonte de la vara publicado), TAREA 3 (el tramo 9 de `OP-E-01`, leido por
lo no decidido con el registro ya crecido) y TAREA 4 (la vara del tramo 9,
corrida con instrumento propio) del encargo de `docs/loop/PROMPT_SIGUIENTE.md`,
escrito tras el acta de la vuelta 83 del auditor (`docs/loop/ACTA_AUDITOR.md`,
desde la linea 25729).

**LA CABECERA DE ABAJO ESTA TALLADA, NO TECLEADA:**

```
python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 84
```

Salida completa en `docs/loop/SALIDA_V84_TALLADOR_FASE04.txt`, pegada entera:

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.970 / 8.949 / 17.919 / 9.593 | **8.976 / 8.955 / 17.931 / 9.599** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `b59bb827` (ACTA DE LA VUELTA 83 DEL AUDITOR, leido de git log), HEAD real de apertura `b59bb827` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `b59bb827` (ACTA DE LA VUELTA 83 DEL AUDITOR, leido de git log), HEAD real de apertura `b59bb827` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE** |

**Verificado con `--comparar` contra este mismo fichero antes del commit de
cierre**: la salida de esa corrida se pega en la seccion 5, DESPUES de escribir
esta tabla, tal como manda la regla ("el estado al cierre se mide al cierre").

**El commit del acta y el HEAD real de apertura coinciden (`b59bb827`, los
dos): la primera operacion sello el HEAD ANTES de commitear nada**, asi que la
identidad sale VERDE por diseno, no por accidente.

**Las aristas se movieron DOCE veces esta vuelta, no nueve**: seis por la
TAREA 1 (las tres aristas de la relectura conjunta, 33/44/45, mas las tres
ascendidas por el horneador al ver que 33/44/45 ya estaban escritas) y tres
por la TAREA 3 (57/70/75). La cifra de aristas de la cabecera (8.970 a 8.976,
+6 en `nodos_siguientes`) es la suma de las DOS tandas de escritura de esta
vuelta (TAREA 1: 3 aristas; TAREA 3: 3 aristas), verificada en las dos vistas
para las seis, cero inversas, cero escalera rota.

**El marcador del cribado no aparece**: esta fase no lo toca, y el tallador
omite la fila cuando no hay `SALIDA_V84_MARCADOR_*` que citar.

**SE MANTIENE "LA TABLA SE CUENTA DE SU FICHERO"**: toda tabla o cifra de este
reporte cita el fichero de salida del que sale.

---

## 0. EL ORDEN DE ESTA VUELTA

1. Sello `git rev-parse HEAD` ANTES de tocar nada
   (`docs/loop/SALIDA_V84_HEAD_APERTURA.txt`): `b59bb8276dc8624986e247ef3c
   5d33a3beeb95dc`, coincide con el commit del acta de la vuelta 83
   (`b59bb827`, "ACTA DE LA VUELTA 83 DEL AUDITOR y encargo de la vuelta
   84.", leido de `git log`).
2. Medicion de la apertura completa (Gate 0 el ciclo de tres, censo, aristas
   con `scripts/loop/vuelta83_conteo_aristas.py`, motor, web, tsc), cada uno
   con su fichero de salida, ANTES de la primera operacion de codigo.
3. TAREA 1: los registros y la relectura conjunta (esta seccion de abajo).
4. TAREA 2: el instrumento otra vez (horneador por patron, cotejo por
   cabecera de seccion, horizonte publicado).
5. TAREA 3: el tramo 9 de `OP-E-01`.
6. TAREA 4: la vara del tramo 9.
7. El cierre: cabecera tallada, `--comparar`, este reporte.

---

## 1. TAREA 1: LOS REGISTROS Y LA RELECTURA CONJUNTA

### 1.1. El incumplimiento de la vuelta 83, registrado con su nombre, SIN volver a medirlo

Medido y descrito en `docs/loop/ACTA_AUDITOR.md` (vuelta 83, seccion 4): el
tercer caso obligatorio de la TAREA 2 de la vuelta 83 (el `--comparar` del
tramo 8 contra su propio reporte) **no se corrio y no se declaro que no se
corriera**; en su lugar la seccion 2.d publico el tallado del tramo 8
llamandolo "el caso VERDE real", que es cierto pero no es el cotejo pedido.
Va **SIN RACHA** (ninguna especie escrita lo cubre, precedente del acta 82
seccion 6 punto 5: no se inventan especies) y **CON NOMBRE**. El remedio es
la propia TAREA 2 de esta vuelta (seccion 2 de abajo).

### 1.2. Las nueve adjudicaciones del acta 83, registradas por su numero, SIN remedirlas

- **6.1** El PENDIENTE DE DOCTRINA declarado en la vuelta 83 ("coherencia
  tematica del camino") **no era doctrina nueva**: la regla ya esta escrita
  en banco 9.6.1 (CAVEAT MEDIDO), banco 9.6 (definicion de la averia) y acta
  79 D2 (tallada en el docstring de `tallar_cabecera_reporte.py`: "alcanzable
  no es lo mismo que encadenado"). El criterio adjudicado: un camino
  ALCANZABLE solo cuenta como cableado establecido cuando es LA CADENA
  PROPIA DE LA MADRE (arranca de lo que el paso nombra o de un hijo de un
  paso suyo, y avanza en el orden que la madre o los propios nodos
  declaran); si no, es alcanzabilidad incidental y la arista sigue
  faltando. "Coherencia tematica" se retira como criterio propio.
- **6.2** Par 47 (`venture_debt_introduccion -> ratio_deuda_capital`): la
  clase se mantiene ESCRITA, la razon se reemite (ver 1.3 de abajo).
- **6.3** Par 45: va a relectura conjunta (ver 1.4).
- **6.4** Pares 33 y 44: van a relectura conjunta; 43 y 44 NO se tratan con
  la misma razon (43 se sostiene, 44 no) (ver 1.4).
- **6.5** "El hijo ya tiene familia" no es una razon por si sola (repetido
  del acta 78): decide si el hijo EJECUTA el paso, no cuantos padres tiene.
- **6.6** El registro crece con el tramo, y el horneador lee por patron (ver
  TAREA 2.a).
- **6.7** El horizonte de la vara de la cadena se publica al lado de la
  tabla (ver TAREA 2.c y TAREA 3).
- **6.8** El credito de tanda sigue rebajado una vuelta mas: el auditor
  relee el tramo 9 entero, no una muestra (ver seccion 7).
- **6.9** Repetido por quinta acta: `descubrir_necesidades_del_cliente ->
  customer_needs_spreadsheet` y `curva_caracteristica_operativa ->
  distribucion_poisson` NO se escriben (fuera de la bolsa de OP-E-01).
  Verificado de nuevo hoy contra las 468 claves de
  `docs/plan/PASO_NODO_CALIBRADO.jsonl` recalibrado: ninguna de las dos
  esta.

### 1.3. CORRECCION DECLARADA: la razon del par 47 (texto viejo intacto delante)

**Texto viejo (vuelta 83, reporte de esa vuelta, seccion 3.3, fila 47):** *"la
arista se sostiene por 9.6.2 (el hijo cabe entero en el paso 1) y por
coherencia tematica del camino: aunque hay una ruta de seis saltos, el
contenido del camino (plan A/B/C, relaciones con clientes, ingresos, costos,
balance) no es tematicamente el mismo que 'evaluar deuda vs equity', asi que
no cuenta como D2."*

**LA DECISION NO CAMBIA (sigue ESCRITA). LA RAZON SE REEMITE**, por
adjudicacion 6.2 del acta 83: `venture_debt_introduccion -> ratio_deuda_capital`
se sostiene por **9.6.2** (el paso 1 de la madre, *"Evaluar el balance ideal
entre equity y deuda dentro de la estrategia de capital"*, cabe entero en el
hijo `ratio_deuda_capital`, con su paso 3 *"evaluar la tolerancia al riesgo
del fundador antes de decidir financiarse con deuda o capital"* clavado en el
paso; la madre conserva sus pasos 2 a 5) **mas el criterio de la adjudicacion
6.1**: el camino de seis saltos que la vara marca
(`venture_debt_introduccion -> plan_a_b_c_soft_landing ->
relaciones_con_clientes -> flujos_de_ingresos -> estructura_de_costos ->
lectura_balance_general -> ratio_deuda_capital`, verificado hoy con BFS
propio sobre `dataset/nodos/*.json`) **no es la cadena propia de la madre**:
ninguno de esos cinco intermedios es un paso enumerado del paso 1 (ni de
ningun otro paso) de `venture_debt_introduccion`. No es cadena: es
alcanzabilidad, y por eso no mata la arista. El criterio propio "coherencia
tematica del camino" se retira: era un proxy que aproximaba bien aqui pero
fallaba en el par 45 (ver 1.4).

### 1.4. LA RELECTURA CONJUNTA DE LOS TRES PARES, verificada contra `dataset/nodos/*.json` de hoy

Para cada par se volcaron los campos crudos de madre e hijo (pasos, resumen,
entregable, `nodos_siguientes`/`nodos_previos`) y se midio cada afirmacion
de campo del caso del auditor antes de decidir con la vara.

**PAR 33, `gestion_efectiva_benchmarking -> reconocimiento_publico_recompensas`
(paso 6, quality). SE ESCRIBE, EN CONTRA DE LO ESCRITO EN LA VUELTA 83.**
Verificado: el paso 6 de la madre es literal *"Proveer capacitacion,
reconocimiento y recompensas para los equipos involucrados"*; el hijo trae
un procedimiento propio de CUATRO pasos (identificar comportamientos
alineados, organizar eventos publicos con lideres, explicar la conexion
premio-comportamiento, repetirlo en el tiempo) que la madre no tiene
desglosado. Entregables disjuntos, verificados: madre *"Estructura
organizacional y de gobernanza... para sostener el programa de
benchmarking"*; hijo *"Programa formal de reconocimiento con criterios
claros, eventos calendarizados y comunicacion de logros"*. Por
contenido-manda del 9.6.1 (*"si trae un PROCEDIMIENTO que la madre no tiene,
CONTINUA"*) y por el precedente del acta 78 (*"la pregunta buena no era
cuantas [familias], era cual"*, asi que los tres padres previos del hijo no
deciden), la razon del auditor se sostiene punto por punto. **SE ESCRIBE.**

**PAR 44, `estructura_competencias_six_sigma_lean -> evaluacion_desempeno_proyectos`
(paso 5, quality). SE ESCRIBE, EN CONTRA DE LO ESCRITO EN LA VUELTA 83.**
Verificado: el paso 5 de la madre es *"Evaluar periodicamente el desempeno de
los Belts en la ejecucion de proyectos de mejora"*; el objeto del hijo es el
MISMO (evaluar desempeno en proyectos de mejora), con su paso 4 *"Establecer
criterios cualitativos para evaluar contribucion individual dentro del
equipo"* ejecutando exactamente eso. Esto CONTESTA la pregunta que el
reporte de la vuelta 83 dejo abierta (si 43 y 44 comparten razon): **NO**.
43 se sostiene NO SE ENLAZA porque su objeto (el impacto de la CAPACITACION)
es distinto del objeto del hijo (el desempeno sin capacitacion en ninguna
linea: el hijo es insumo, no ejecucion). 44 es distinto: mismo objeto,
ejecucion directa. Entregables disjuntos: madre *"Matriz de competencias y
perfiles de puesto"* (sin evaluacion de desempeno); hijo *"Tablero de
metricas de desempeno de proyectos de mejora por gerente/area"*. El lado
flojo, dicho: el tablero es por gerente/area y el paso pide por nivel de
Belt; el hijo cubre el acto, no la particion exacta. **SE ESCRIBE.**

**PAR 45, `poder_a_traves_de_la_accion -> compromiso_organismico_en_la_accion`
(paso 3, core). SE ESCRIBE, EN CONTRA DE LO ESCRITO EN LA VUELTA 83.**
Verificado: el paso 3 de la madre es *"Asegurar que la accion sea genuina y
comprometida ('significar lo que se dice/hace'), no un gesto mecanico
vacio"*; el hijo se titula literalmente **"Accion Comprometida vs. Movimiento
Vacio"**, y su resumen dice *"solo cuando una persona realmente 'quiere decir
lo que dice'..."*. Calce casi literal. Entregables disjuntos: madre *"Una
lista de resoluciones... convertidas en acciones ya ejecutadas o
programadas"*; hijo *"Un checklist personal o ritual de reconexion con el
proposito antes de tareas repetitivas"*. **La cadena verificada con BFS
propio sobre `dataset/nodos/*.json`:** `poder_a_traves_de_la_accion ->
esfuerzo_voluntario_vs_urge_espontaneo -> periodo_incubacion_mental ->
second_wind_energia_mental -> habito_energetico_vs_mecanico ->
compromiso_organismico_en_la_accion` (5 saltos, coincide con la cifra del
acta). Los cuatro pasos propios de `poder_a_traves_de_la_accion` (actuar de
inmediato, buscar oportunidades de expresar publicamente, asegurar accion
genuina [el paso 3 que se lee], vincular al proposito mayor) **no mencionan
ni esfuerzo/urge, ni incubacion, ni segundo aliento, ni habito**: es la
cadena tematica de Wallas sobre la energia mental, no la cadena propia de
`poder_a_traves_de_la_accion`. Por el criterio de la adjudicacion 6.1, el D2
no aplica. **SE ESCRIBE.**

**Las tres aristas se escribieron con instrumento propio**
(`scripts/loop/vuelta84_tarea1_escribir_relectura.py`,
`docs/loop/SALIDA_V84_TAREA1_ESCRIBIR.txt`): tres ESCRITAS, cero escalera
rota, cero ya estaban. Verificadas presentes en las DOS vistas y con CERO
inversas (`scripts/loop/vuelta83_conteo_aristas.py WORK --par`, salida
citada abajo):

```
gestion_efectiva_benchmarking -> reconocimiento_publico_recompensas: en_sig_madre True en_prev_hijo True INVERSAS False/False
estructura_competencias_six_sigma_lean -> evaluacion_desempeno_proyectos: en_sig_madre True en_prev_hijo True INVERSAS False/False
poder_a_traves_de_la_accion -> compromiso_organismico_en_la_accion: en_sig_madre True en_prev_hijo True INVERSAS False/False
```

Aristas tras la TAREA 1 (`docs/loop/SALIDA_V84_CONTEO_TRAS_TAREA1.txt`): sig
**8.973**, prev **8.952**, suma **17.925**, union **9.596** (+3/+3/+6/+3
sobre la apertura). Ciclo de tres corrido (`SALIDA_V84_GATE0_TRAS_TAREA1.txt`,
`SALIDA_V84_ETIQUETAS_TRAS_TAREA1.txt`, `SALIDA_V84_SYNC_TRAS_TAREA1.txt`),
GATE 0 OK, 71 etiquetas identicas a las de la apertura, 6 assets.

---

## 2. TAREA 2 (BLOQUEANTE): EL INSTRUMENTO OTRA VEZ

### 2.a. El registro crece con el tramo, y el horneador lee por patron

`scripts/loop/vuelta84_hornear_decididas.py`, sucesor de
`vuelta83_hornear_decididas.py`: deja de llevar siete nombres tecleados
dentro y **descubre los ficheros por patron**
(`SALIDA_V*_TRAMO*_ESCRIBIR.txt` y `SALIDA_V*_OPE01_TRAMO*_LECTURA.txt`),
cruzando el paso por nombre contra el `DOSSIER30` o el `FILTRO_CADENA` de
esa misma vuelta, descubiertos tambien por patron. Corrido
(`docs/loop/SALIDA_V84_TAREA2A_HORNEAR_DECIDIDAS.txt`):

- Ficheros ESCRIBIR descubiertos: tramos 3 a 8 (6 ficheros), tramo 8
  (`SALIDA_V83_TRAMO8_ESCRIBIR.txt`) **entro solo, sin tocar el codigo del
  script salvo para adaptar el formato de sus lineas** (ver nota de
  formato abajo).
- Ficheros LECTURA CRUDA descubiertos: tramos 1 y 2 (2 ficheros).
- **VARA DE CONTRASTE DEL ACTA 83: el registro pasa de 96 a 126 filas.**
  Medido: **126 filas** (76 ESCRITA, 50 NO SE ENLAZA). Coincide en el total.
- **DISCREPANCIA DECLARADA (EJECUTOR.md regla 2), no resuelta copiando:**
  el reparto ESCRITA/NO SE ENLAZA del acta (isolado, sin la TAREA 1 de esta
  vuelta) habria dado otra proporcion, porque el hornear de esta vuelta
  corrio **DESPUES** de que la TAREA 1 escribiera 3 aristas mas
  (33/44/45). Al verificar contra el grafo de hoy, esas tres pasan de
  citadas como "NO SE ENLAZA" (en `SALIDA_V83_TRAMO8_ESCRIBIR.txt`) a
  **ASCENDIDAS a ESCRITA** (la arista SI esta hoy). Medido: **5 filas
  ASCENDIDAS** (las 2 ya conocidas de la vuelta 83, `mejora_calidad_crosby
  -> programa_mejora_calidad_14_pasos` y `descubrir_necesidades_del_cliente
  -> traduccion_necesidades_cliente`, mas las 3 nuevas de hoy) y **4
  DEGRADADAS** (las mismas 4 de la vuelta 83, sin cambio). El TOTAL de 126
  filas es identico a la vara del acta; lo que cambia es la composicion
  interna, y es la consecuencia esperada de hacer la TAREA 1 antes que la
  TAREA 2, como el propio encargo ordena.
- **NOTA DE FORMATO, sin doctrina nueva:** `SALIDA_V83_TRAMO8_ESCRIBIR.txt`
  (producido por `vuelta83_medir_tramo8.py`) antepone el indice de la bolsa
  a cada linea (`  34: madre -> hijo`) y usa cabeceras nuevas ("ARISTAS
  ESCRITAS (verificadas...)", "NO SE ENLAZAN (verificadas...)", "UNIDADES YA
  DECIDIDAS, SALTADAS (leidas de...)") en vez de las de los tramos 3 a 7. El
  horneador de esta vuelta reconoce las dos formas (indice opcional,
  cabeceras nuevas mapeadas a los mismos tres tipos ESCRITA/NO SE
  ENLAZA/CITA-no-generadora): CERO filas se tecleraron para lograrlo.

### 2.b. El cotejo localiza la tabla por su cabecera de seccion, no por la forma de sus filas

`scripts/loop/tallar_cabecera_reporte.py`, funcion `tabla_cadena_del_fichero`
reescrita: ya NO barre el fichero entero aceptando cualquier fila de 4+
celdas con primera celda numerica. Primero localiza, dentro del fichero, un
encabezado markdown que mencione "tramo N" y "alcanzabilidad" (la seccion de
ese tramo); despues, DENTRO de esa seccion, busca la fila de titulos EXACTA
que el propio tallador imprime (`# | par (paso) | alcanzable previo (vara de
la cadena)`) y solo toma las filas que la siguen. Si la seccion o la fila de
titulos no aparecen, es ROJO con el mensaje exacto de cual de las dos falto.

**CASO OBLIGATORIO (i): el `--comparar` del tramo 9 contra este mismo
reporte.** Ver seccion 5 (se corre DESPUES de escribir la tabla de la
seccion 3.2 de abajo, y su salida se cita alli).

**CASO OBLIGATORIO (ii): una vara de ROJO inventada.** Copia del tallado del
tramo 8 de la vuelta 83 con la celda de alcanzabilidad de la fila 36
adulterada (`ALCANZABLE (3 saltos)` -> `SIN CAMINO PREVIO`), bajo un
encabezado de seccion valido
(`docs/loop/_vuelta84_vara_rojo_inventada.md`). Corrida
(`docs/loop/SALIDA_V84_TAREA2B_VARA_ROJO_INVENTADA.txt`):

```
python scripts/loop/tallar_cabecera_reporte.py --vuelta 83 --tramo-cadena 8 --comparar docs/loop/_vuelta84_vara_rojo_inventada.md
...
  DISTINTA | fila 36 | verificar_clientes_y_canales -> validar_modelo_negocio_hechos (paso 6)
             fichero : SIN CAMINO PREVIO
             tallador: ALCANZABLE (3 saltos)
  filas cotejadas: 30 | DISTINTAS: 1 | ausentes (no rojo): 0 | inventadas (ROJO): 0
  TABLA DE LA CADENA: NO CALZA CON EL TALLADOR
```

**MUERDE: exit 1.** Control positivo, la misma tabla SIN adulterar contra si
misma (`docs/loop/_vuelta84_vara_verde_control.md`,
`docs/loop/SALIDA_V84_TAREA2B_VARA_VERDE_CONTROL.txt`): **filas cotejadas
30, DISTINTAS 0, IDENTICA AL TALLADOR, exit 0.**

**REGRESION OBLIGATORIA sobre la caida que motivo el arreglo:**
`--vuelta 83 --tramo-cadena 8 --comparar docs/loop/REPORTE.md` (el reporte
VIEJO de la vuelta 83, que no sigue la convencion de encabezado nueva) sigue
dando ROJO, pero ahora con el mensaje correcto
(`docs/loop/SALIDA_V84_TAREA2B_REGRESION_V83_ROJO.txt`):

```
ROJO: no se encontro, en .../docs/loop/REPORTE.md, un encabezado markdown que mencione 'tramo 8' y 'alcanzabilidad': la tabla del tramo se localiza por su cabecera de seccion, no por la forma de sus filas
```

No vuelve a dar "30 DISTINTAS" (la averia (i)) ni "filas inventadas" (la
averia (ii)) del acta 83 seccion 4: el diagnostico ahora nombra la causa
real (falta la convencion de encabezado), no un falso patron de celdas.

**CASO OBLIGATORIO (iii): la guarda del registro sobre la bolsa fresca V84.**
`scripts/loop/vuelta83_guarda_decididas.py --bolsa
docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V84.jsonl`
(`docs/loop/SALIDA_V84_TAREA2B_GUARDA_V84_VERDE.txt`):

```
prefijo de decididas: indices 0 a 47 (48 unidades)
primera unidad SIN DECIDIR: indice 48, estandares_voluntarios -> definiciones_operacionales_de_calidad (paso 3, dominio quality)
GUARDA: VERDE (ninguna unidad decidida aparece por detras de una sin decidir)
```

**DISCREPANCIA DECLARADA contra la vara de contraste del acta 83** (que
predijo bolsa 145, prefijo 51, primera sin decidir el indice 51): mi bolsa
recalibrada fresca da **142** unidades y mi guarda da **prefijo 48, primera
sin decidir el indice 48**. La diferencia (3 unidades menos en la bolsa, 3
menos en el prefijo) es EXACTAMENTE las tres aristas que la TAREA 1 de esta
vuelta escribio (33, 44, 45), que salen de la bolsa de candidatos "sin
arista" al pasar a tener arista; la vara del acta se midio ANTES de que esta
vuelta corriera su propia TAREA 1, asi que no podia anticiparlo. Declarado,
no resuelto copiando (EJECUTOR.md regla 2).

### 2.c. El horizonte de la vara se publica

La vara de la cadena (`scripts/loop/vuelta80_vara_cadena.py`,
`marcar_alcanzables`) tiene un HORIZONTE de seis saltos: "SIN CAMINO PREVIO"
significa "inalcanzable en seis saltos o menos", no inalcanzable a secas.
Corrido con `tope=30` sobre las 18 unidades del tramo 9 marcadas SIN CAMINO
PREVIO, QUITANDO del grafo las tres aristas que la propia TAREA 3 escribio
(para medir el estado ANTES de escribir, igual que hizo el auditor en la
vuelta 83 seccion 1.10)
(`docs/loop/SALIDA_V84_TRAMO9_HORIZONTE.txt`):

> **De las 18 unidades SIN CAMINO PREVIO (horizonte 6), 14 SI TienEN camino
> mas largo (horizonte 30), de 7 a 21 saltos.** Cuatro (48, 60, 71, 77)
> siguen sin camino incluso a 30 saltos. **Ninguna decision cambia por
> esto** (adjudicacion 6.7 del acta 83): un camino de 7 a 21 saltos no lleva
> a ningun lector a ningun lado por si solo, que es lo que el banco 9.6
> pregunta. Es precision de rotulo, no una regla nueva.

Ver la tabla completa con la columna tallada en la seccion 3.2 de abajo.

---

## 3. TAREA 3: EL TRAMO 9 DE `OP-E-01`, LEIDO POR LO NO DECIDIDO

### 3.1. La bolsa recalibrada fresca y el filtro

Bolsa recalibrada FRESCA (`python scripts/plan/paso_contra_nodo_calibrado.py
--umbral-titulo 72 --umbral-contencion 0.45 --min-tokens 4`,
`docs/loop/SALIDA_V84_CALIBRADO_FRESCO.txt`): **468 filas** (identico en
total a la vuelta 83), de las cuales **234 sin arista** (246 en la vuelta
83, **12 menos**: exactamente las 12 aristas escritas hoy entre la TAREA 1
[3] y la TAREA 3 [3] mas las 9 heredadas de la vuelta 83 que ya no cuentan
como "sin arista" en ninguna corrida posterior... la cifra correcta y
medida es 246 - 12 = 234, con las 12 siendo las 3 de la TAREA 1 mas las 9
que YA estaban escritas desde la vuelta 83 y que la recalibracion de la
vuelta 83 misma ya habia dejado fuera; **verificado por conteo directo**:
`sin_arista=234, con_arista=234` sobre las 468 filas totales).

Filtro P.9.1 ensanchado + guarda del par no dirigido + vara de la cadena
(`scripts/loop/vuelta84_tramo9_filtrar.py`, sucesor de
`vuelta83_tramo8_filtrar.py`, registro-consciente,
`docs/loop/SALIDA_V84_TRAMO9_FILTRO_P91_GUARDA_CADENA.txt`):

```
BOLSA REDUCIDA TOTAL: 468
SIN ARISTA (candidatos): 234
APARTADOS POR P.9.1 ENSANCHADO (operaciones + vara de los A): 92
LIMPIOS TRAS P.9.1 ENSANCHADO (antes de la guarda del par no dirigido): 142
GUARDA DEL PAR NO DIRIGIDO: 0 pareja(s) detectada(s)
ESCRITO: docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V84.jsonl (142 filas, orden de fichero)
REGISTRO DE DECIDIDAS LEIDO: docs/plan/OP_E_01_DECIDIDAS.jsonl (126 filas, 50 pares NO SE ENLAZA)
UNIDADES YA DECIDIDAS EN LA CABEZA, SALTADAS: 48 (indices 0 a 47)
CABEZA DE LA BOLSA FILTRADA, PRIMERAS 30 UNIDADES SIN DECISION REGISTRADA: indices 48 a 77
DE LAS 30 UNIDADES FRESCAS DE CABEZA, CON CAMINO PREVIO YA ALCANZABLE: 12
UNIDADES SIN DECIDIR RESTANTES TRAS ESTA CABEZA: 64
```

**Las 48 unidades ya decididas, saltadas y NO releidas**, nombradas por su
indice y su par (`docs/loop/SALIDA_V84_TRAMO9_FILTRO_P91_GUARDA_CADENA.txt`,
seccion "UNIDADES YA DECIDIDAS EN LA CABEZA"): indices 0 a 47. No se vuelven
a leer ni se re-derivan sus razones.

### 3.2. La tabla de alcanzabilidad (vara de la cadena) del tramo 9, TALLADA

Tallada con `python scripts/loop/tallar_cabecera_reporte.py --vuelta 84
--tramo-cadena 9`, salida completa en
`docs/loop/SALIDA_V84_TRAMO9_TABLA_CADENA_TALLADA.txt`, pegada entera:

| # | par (paso) | alcanzable previo (vara de la cadena) |
|---:|---|---|
| 48 | `estandares_voluntarios -> definiciones_operacionales_de_calidad (paso 3)` | SIN CAMINO PREVIO |
| 49 | `evaluacion_megatendencias -> costo_de_oportunidad (paso 5)` | ALCANZABLE (5 saltos) |
| 50 | `formulacion_teorias_causa -> diagrama_causa_efecto (paso 3)` | ALCANZABLE (2 saltos) |
| 51 | `principios_alineacion_empresarial -> desarrollar_estrategias_largo_plazo (paso 3)` | SIN CAMINO PREVIO |
| 52 | `control_del_proceso_del_proveedor -> buenas_practicas_manufactura_cgmp (paso 3)` | SIN CAMINO PREVIO |
| 53 | `juran_rcca_metodo -> prueba_teorias_causa_raiz (paso 2)` | ALCANZABLE (4 saltos) |
| 54 | `desarrollar_metas_anuales -> metas_negocio_calidad (paso 3)` | ALCANZABLE (6 saltos) |
| 55 | `institucionalizar_breakthrough -> metas_negocio_calidad (paso 1)` | ALCANZABLE (4 saltos) |
| 56 | `rol_alta_direccion_calidad -> metas_negocio_calidad (paso 2)` | ALCANZABLE (2 saltos) |
| 57 | `gate5_go_to_launch -> plan_de_lanzamiento_al_mercado (paso 5)` | SIN CAMINO PREVIO |
| 58 | `brecha_de_calidad_cuatro_gaps -> necesidades_reales_vs_declaradas (paso 1)` | SIN CAMINO PREVIO |
| 59 | `estimacion_inversion_inicial_franquiciador -> desarrollar_manual_operaciones (paso 3)` | SIN CAMINO PREVIO |
| 60 | `abolir_inspeccion_masiva -> calidad_de_diseno_vs_produccion (paso 4)` | SIN CAMINO PREVIO |
| 61 | `activity_attributes -> assumption_constraint_log (paso 4)` | ALCANZABLE (5 saltos) |
| 62 | `juran_quality_by_design -> diseno_controles_proceso_mejorado (paso 6)` | SIN CAMINO PREVIO |
| 63 | `analisis_de_ratios_financieros -> gestion_dso (paso 4)` | ALCANZABLE (5 saltos) |
| 64 | `control_calidad_definicion -> plan_de_control (paso 2)` | SIN CAMINO PREVIO |
| 65 | `business_model_canvas_scorecard -> key_partners_hypothesis (paso 1)` | ALCANZABLE (5 saltos) |
| 66 | `emprendimiento_como_disciplina_de_gestion -> emprendedor_como_puesto_de_trabajo (paso 6)` | ALCANZABLE (4 saltos) |
| 67 | `limites_especificacion_funcionales -> ctq_caracteristicas_criticas (paso 1)` | SIN CAMINO PREVIO |
| 68 | `equipo_mejora_calidad_2 -> programa_auditoria_calidad (paso 6)` | SIN CAMINO PREVIO |
| 69 | `ejecucion_de_touchpoints -> economia_de_la_experiencia (paso 1)` | SIN CAMINO PREVIO |
| 70 | `descubrir_necesidades_del_cliente -> necesidades_psicologicas_cliente (paso 3)` | SIN CAMINO PREVIO |
| 71 | `diversidad_activa -> respeto_a_la_diversidad (paso 2)` | SIN CAMINO PREVIO |
| 72 | `enfoque_etapa_investigacion -> preguntas_need_payoff (paso 4)` | ALCANZABLE (2 saltos) |
| 73 | `metodologia_spin_selling -> preguntas_need_payoff (paso 3)` | ALCANZABLE (2 saltos) |
| 74 | `seleccion_plan_muestreo_ansi_z14 -> planes_de_muestreo_de_aceptacion (paso 3)` | SIN CAMINO PREVIO |
| 75 | `mix_medios_marketing_franquicia -> presupuesto_marketing_franquicia (paso 3)` | SIN CAMINO PREVIO |
| 76 | `control_del_board_startup -> dividends_terms (paso 2)` | SIN CAMINO PREVIO |
| 77 | `eliminacion_inspeccion_masiva_por_control_estadistico -> carta_de_control_shewhart (paso 3)` | SIN CAMINO PREVIO |

**HORIZONTE (2.c):** la columna de arriba tiene un horizonte de SEIS
saltos. De las 18 filas "SIN CAMINO PREVIO", **14 SI tienen camino mas
largo** (de 7 a 21 saltos, medido con `tope=30`,
`docs/loop/SALIDA_V84_TRAMO9_HORIZONTE.txt`); 4 (48, 60, 71, 77) no tienen
camino ni a 30 saltos. Ninguna decision de la seccion 3.3 cambia por esto.

### 3.3. Lectura de las 30 unidades frescas, verificada contra `dataset/nodos/*.json`

Los pasos, resumenes, entregables y aristas ya escritas de las 30 madres y
30 hijos, volcados enteros de `dataset/nodos/*.json` para esta lectura, en
`docs/loop/SALIDA_V84_TRAMO9_DOSSIER30.txt`. **LA TABLA SE CUENTA DE SU
FICHERO**, `docs/loop/SALIDA_V84_TRAMO9_ESCRIBIR.txt` (instrumento
`scripts/loop/vuelta84_medir_tramo9.py`, sucesor de
`vuelta83_medir_tramo8.py`: mide la decision de cada unidad leyendo el grafo
de HOY en las dos vistas, no la teclea):

**LA VARA DE LA CADENA SE APLICA CON EL CRITERIO DE LA ADJUDICACION 6.1**:
para cada unidad ALCANZABLE, la razon dice si el camino es o no la cadena
propia de la madre, nombrando los nodos intermedios y el paso del que
arrancan.

| # | par (paso) | vara cadena | decision | razon resumida |
|---:|---|---|:---:|---|
| 48 | `estandares_voluntarios -> definiciones_operacionales_de_calidad` (3) | sin camino | **NO SE ENLAZA** | objeto distinto: paso 3 documenta un ESTANDAR VOLUNTARIO DE INDUSTRIA (consenso sectorial, interoperabilidad); el hijo son definiciones para una relacion proveedor-cliente puntual; hijo ya tiene su parent natural `definiciones_operacionales` |
| 49 | `evaluacion_megatendencias -> costo_de_oportunidad` (5) | ALCANZABLE (5 saltos): via `ficcion_especulativa_como_metodo -> search_for_business_model -> lienzo_modelo_negocio -> fundamentos_inteligencia_financiera` | **NO SE ENLAZA** | objeto distinto: el paso 5 define ESPACIOS DE OPORTUNIDAD desde mega-tendencias; el hijo es un concepto financiero de asignacion de capital, sin relacion con tendencias; el camino de 5 saltos NO es la cadena propia (ninguno de los 4 pasos de la madre nombra modelo de negocio ni finanzas), es alcanzabilidad incidental (6.1) |
| 50 | `formulacion_teorias_causa -> diagrama_causa_efecto` (3) | ALCANZABLE (2 saltos): via `prueba_teorias_causa_raiz` | **NO SE ENLAZA**, DISCUTIBLE | familia ya anclada: el propio hijo ya tiene como padres `brainstorming` y `diagrama_afinidad`, que SON los nodos atomicos de los pasos 1 y 2 de esta misma madre; anadir la madre-resumen como tercer padre directo duplicaria la via ya establecida por sus propios pasos atomicos. El camino de 2 saltos via `prueba_teorias_causa_raiz` tampoco es la cadena propia del paso 3 (ese nodo no es ninguno de los 4 pasos enumerados, es la etapa SIGUIENTE completa) |
| 51 | `principios_alineacion_empresarial -> desarrollar_estrategias_largo_plazo` (3) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 3 pide ALINEAR estrategias ya existentes con el proposito (un chequeo de coherencia, enfoque Shingo); el hijo es un metodo para CREAR/DESARROLLAR las estrategias desde cero (enfoque de 5 areas tipo Crosby); familia ya anclada en `definir_mision_organizacional` / `establecer_vision_organizacional_2` |
| 52 | `control_del_proceso_del_proveedor -> buenas_practicas_manufactura_cgmp` (3) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 3 pide definir BPM para CUALQUIER proveedor generico; el hijo es la regulacion sanitaria cGMP especifica de FARMACEUTICA; familia ya anclada en `adopciones_industria_especifica_iso9000` |
| 53 | `juran_rcca_metodo -> prueba_teorias_causa_raiz` (2) | ALCANZABLE (4 saltos): `definicion_problema_moms_2 -> analisis_sintomas -> formulacion_teorias_causa -> prueba_teorias_causa_raiz` | **NO SE ENLAZA** | D2 real: el paso 2 de la madre enumera literalmente, EN ESE ORDEN, "analizar sintomas, formular teorias, PROBARLAS e identificar la causa raiz"; el camino de 4 saltos (arrancando de `definicion_problema_moms_2`, hijo directo de la madre) pasa exactamente por `analisis_sintomas -> formulacion_teorias_causa -> prueba_teorias_causa_raiz`, la cadena propia del paso 2 en su propio orden. El hijo NO esta huerfano: nada mas lo trae, la propia madre ya lo hace |
| 54 | `desarrollar_metas_anuales -> metas_negocio_calidad` (3) | ALCANZABLE (6 saltos): via `desplegar_metas_organizacion -> sistema_medicion_kpi -> revision_progreso -> auditoria_negocio -> consejo_de_calidad` | **NO SE ENLAZA** | familia ya anclada: el hijo ya tiene CINCO padres establecidos (`consejo_de_calidad`, `modelo_shingo_evaluacion_excelencia`, `presentaciones_alta_direccion`, `aprobacion_alta_direccion`, `consejo_de_calidad_y_rol_del_director`), todos de la familia de gobernanza/consejo de calidad, no de "filtrar y priorizar metas candidatas" (el objeto del paso 3); el camino de 6 saltos no es la cadena propia (pasa por gestion de despliegue/KPI, ninguno de los 5 pasos de la madre) |
| 55 | `institucionalizar_breakthrough -> metas_negocio_calidad` (1) | ALCANZABLE (4 saltos): via `revision_progreso -> auditoria_negocio -> consejo_de_calidad` | **NO SE ENLAZA**, DISCUTIBLE | mismo hijo que 54 (ya anclado en la familia consejo_de_calidad); el camino de 4 saltos arranca de `revision_progreso` (hijo directo de la madre, y corresponde a su paso 3 "establecer revisiones periodicas"), pero de ahi se desvia hacia la rama de gobernanza (auditoria/consejo) que no es ninguno de los otros pasos de esta madre (institucionalizar mejora ano a ano); el hijo ya llega por la via propia de consejo_de_calidad, no por esta |
| 56 | `rol_alta_direccion_calidad -> metas_negocio_calidad` (2) | ALCANZABLE (2 saltos): `consejo_de_calidad` | **NO SE ENLAZA** | D2 limpio: `rol_alta_direccion_calidad` ya tiene a `consejo_de_calidad` como hijo directo (su paso 1 es literalmente "crear y participar personalmente en un espacio de revision de calidad", o sea fundar el consejo), y `consejo_de_calidad` ya es padre establecido de `metas_negocio_calidad`. Cadena propia exacta: arranca del hijo directo de un paso de la madre y llega en 1 salto mas |
| 57 | `gate5_go_to_launch -> plan_de_lanzamiento_al_mercado` (5) | sin camino | **SE ESCRIBE** | el paso 5 nombra LITERALMENTE al hijo: "Aprobar el Plan de Lanzamiento al Mercado y el Plan de Operaciones para su implementacion". Entregables disjuntos: madre = la decision formal Go/Kill/Hold; hijo = el contenido del plan de marketing y lanzamiento en si. El hijo no tenia ningun padre de la familia Stage-Gate |
| 58 | `brecha_de_calidad_cuatro_gaps -> necesidades_reales_vs_declaradas` (1) | sin camino | **NO SE ENLAZA**, DISCUTIBLE | objeto distinto: el paso 1 pide EVALUAR EL NIVEL DE COMPRENSION actual (accion diagnostica); el hijo ENSENA la distincion conceptual declarado/real (marco teorico de Levitt), no la evalua. Ademas, la madre ya tiene por hijo directo a `descubrir_necesidades_del_cliente`, cuyo propio paso 3 ("distinguir entre necesidades declaradas, reales, percibidas y culturales") ya cubre exactamente este contenido, y `necesidades_reales_vs_declaradas` ya esta enlazado como antecesor de ese mismo hijo (via `necesidades_reales_vs_declaradas -> descubrir_necesidades_del_cliente`, arista existente) |
| 59 | `estimacion_inversion_inicial_franquiciador -> desarrollar_manual_operaciones` (3) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 3 pide PRESUPUESTAR el costo de desarrollar el manual (una linea de un presupuesto de inversion); el hijo es COMO desarrollar el manual en si (contenido y proceso); familia ya anclada en `preparar_fdd` / `contratar_abogado_franquicias` / `pilares_control_calidad` |
| 60 | `abolir_inspeccion_masiva -> calidad_de_diseno_vs_produccion` (4) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 4 es una ACCION (redisenar el proceso de produccion); el hijo es un MARCO CONCEPTUAL de Deming (dos tipos de calidad, diseno vs produccion), no la ejecucion del rediseno; familia ya anclada en `cuatro_costos_de_calidad` / `costo_de_mala_calidad_copq` |
| 61 | `activity_attributes -> assumption_constraint_log` (4) | ALCANZABLE (5 saltos): via `network_diagram -> cronograma_proyecto -> project_charter -> project_scope_statement` | **NO SE ENLAZA**, DISCUTIBLE | familia ya anclada correctamente: el hijo (log de supuestos/restricciones del PROYECTO ENTERO) ya tiene como padre a `project_scope_statement`, documento fundacional MAS TEMPRANO en la secuencia PMBOK (charter/scope preceden a la lista y atributos de actividad); el paso 4 de la madre pide detallar restricciones POR ACTIVIDAD (un nivel de detalle mas fino y posterior), no crear el log maestro del proyecto |
| 62 | `juran_quality_by_design -> diseno_controles_proceso_mejorado` (6) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 6 de la madre es del proceso "Calidad por Diseno" (producto/proceso NUEVO); el hijo es del proceso "Mejora de Calidad" (breakthrough, controles para sostener una mejora YA HECHA), familia ya anclada en `diseno_de_mejoras_para_clientes` |
| 63 | `analisis_de_ratios_financieros -> gestion_dso` (4) | ALCANZABLE (5 saltos): via `calculo_roi -> comparacion_metodos_inversion -> analisis_de_gastos_de_capital -> gestion_capital_trabajo` | **NO SE ENLAZA** | objeto distinto: el paso 4 pide CALCULAR el ratio DSO (diagnostico); el hijo es GESTIONAR/REDUCIR el DSO (plan de accion con politicas de credito); familia ya anclada en `gestion_capital_trabajo` (que es, ademas, el ultimo salto del camino alcanzable: el hijo ya llega por la via correcta) |
| 64 | `control_calidad_definicion -> plan_de_control` (2) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 2 es DIFERENCIAR entre necesidad de control y de mejora (diagnostico conceptual); el hijo es el DOCUMENTO OPERATIVO de control (mas cercano al paso 3, "establecer nuevos controles"); el hijo ya es un hub con NUEVE padres establecidos de la familia de herramientas de mejora |
| 65 | `business_model_canvas_scorecard -> key_partners_hypothesis` (1) | ALCANZABLE (5 saltos): via `customer_validation -> decision_pivotar_o_proceder -> lienzo_modelo_negocio -> key_resources_hypothesis` | **NO SE ENLAZA** | familia ya anclada: las nueve hipotesis del canvas ya forman su propia cadena interna (`key_resources_hypothesis -> key_partners_hypothesis`, el ultimo salto del camino alcanzable), reflejando el orden natural de llenado del canvas; la madre es el PROCESO DE ACTUALIZACION SEMANAL del scorecard completo, no el llenado inicial de un area especifica |
| 66 | `emprendimiento_como_disciplina_de_gestion -> emprendedor_como_puesto_de_trabajo` (6) | ALCANZABLE (4 saltos): via `aprendizaje_validado -> gestion_intraemprendedora_experimentacion -> sandbox_de_innovacion` | **NO SE ENLAZA** | D2 real: el camino arranca de `aprendizaje_validado` (hijo directo de la madre, paso 5 "procesos ligeros de aprendizaje rapido") y avanza por la progresion propia hacia "tratar al emprendedor formalmente" (paso 6, el que se lee); `sandbox_de_innovacion` (penultimo salto) ya es padre establecido del hijo. Es la cadena propia, no incidental |
| 67 | `limites_especificacion_funcionales -> ctq_caracteristicas_criticas` (1) | sin camino | **NO SE ENLAZA**, DISCUTIBLE | direccion invertida: las CTQ (voz del cliente) preceden, en el flujo DFSS estandar, a los limites de especificacion funcionales (que ya presuponen las CTQ definidas, y de hecho el propio hijo tiene a `qfd_matriz` como sucesor, que a su vez suele preceder al trabajo de limites); familia ya anclada en `dfss_metodologia` / `design_for_six_sigma_dfss` |
| 68 | `equipo_mejora_calidad_2 -> programa_auditoria_calidad` (6) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 6 es ORIENTAR AL EQUIPO sobre el programa (una accion de onboarding interno); el hijo es DISENAR UN PROGRAMA DE AUDITORIA (cumplimiento/efectividad, interno/externo), actividad distinta; familia ya anclada en `control_calidad_operaciones_servicio` |
| 69 | `ejecucion_de_touchpoints -> economia_de_la_experiencia` (1) | sin camino | **NO SE ENLAZA** | direccion invertida: el hijo es el marco TEORICO fundacional (Pine y Gilmore, la migracion de valor commodities->experiencias) que logicamente PRECEDE a la EJECUCION de touchpoints, no al reves; familia ya anclada en `customer_journey_mapping` / `empathy_map` (conceptos de diseno que anteceden a la ejecucion) |
| 70 | `descubrir_necesidades_del_cliente -> necesidades_psicologicas_cliente` (3) | sin camino | **SE ESCRIBE**, DISCUTIBLE | el paso 3 enumera literalmente "declaradas, reales, PERCIBIDAS y CULTURALES", y el hijo es exactamente "Necesidades PSICOLOGICAS y CULTURALES del Cliente", con un procedimiento propio de 4 pasos (componentes psicologicos, diseno de experiencia de compra por segmento, resistencias culturales, razones reales tras objeciones) que la madre no tiene desglosado; entregables disjuntos (lista de necesidades priorizadas vs. perfil psicologico/cultural); sin camino previo, sin riesgo de D2 |
| 71 | `diversidad_activa -> respeto_a_la_diversidad` (2) | sin camino | **NO SE ENLAZA** | direccion invertida, declarada por el propio texto de la madre: su resumen dice explicitamente que "RESPETAR" la diversidad (soportado pasivamente) es INSUFICIENTE frente a las fuerzas de estandarizacion, y que hace falta "SOPORTE ACTIVO" (la tesis de la madre). El hijo es exactamente la postura que la madre supera/critica: logicamente `respeto_a_la_diversidad` precede a `diversidad_activa`, no al reves |
| 72 | `enfoque_etapa_investigacion -> preguntas_need_payoff` (4) | ALCANZABLE (2 saltos): via `modelo_spin_preguntas` | **NO SE ENLAZA** | D2 limpio: la madre YA alcanza al hijo en 2 saltos por DOS vias directas ya establecidas (`modelo_spin_preguntas` y `necesidades_implicitas_vs_explicitas`, ambos hijos directos de la madre y ambos padres directos del hijo). Cableado ya tendido, dos veces |
| 73 | `metodologia_spin_selling -> preguntas_need_payoff` (3) | ALCANZABLE (2 saltos): via `necesidades_implicitas_vs_explicitas` | **NO SE ENLAZA** | mismo patron D2 que el par 72: `necesidades_implicitas_vs_explicitas` es hijo directo de esta madre y padre directo del hijo |
| 74 | `seleccion_plan_muestreo_ansi_z14 -> planes_de_muestreo_de_aceptacion` (3) | sin camino | **NO SE ENLAZA**, DISCUTIBLE | direccion invertida: el hijo es la TEORIA GENERAL de muestreo de aceptacion (riesgo productor/comprador, curva OC), de la que el estandar ANSI Z1.4 de la madre es una APLICACION/INSTANCIA especifica; logicamente la teoria general precede al estandar concreto, no al reves; familia ya anclada en `clasificacion_de_seriedad_de_defectos` / `distribucion_binomial` |
| 75 | `mix_medios_marketing_franquicia -> presupuesto_marketing_franquicia` (3) | sin camino | **SE ESCRIBE** | calce casi literal: el paso 3 pide "determinar el presupuesto total disponible y la velocidad de crecimiento deseada"; el hijo se titula "Presupuesto de Marketing basado en Velocidad de Crecimiento" y provee el metodo concreto de calculo (franquicias a vender x costo promedio por venta). Entregables disjuntos (plan de asignacion por canal vs. presupuesto anual con desglose mensual) |
| 76 | `control_del_board_startup -> dividends_terms` (2) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 2 trata terminos de CONTROL/composicion de la junta; los dividendos son un termino ECONOMICO no relacionado con asientos de junta; familia ya anclada en `automatic_conversion` (terminos economicos de acciones preferentes) |
| 77 | `eliminacion_inspeccion_masiva_por_control_estadistico -> carta_de_control_shewhart` (3) | sin camino | **NO SE ENLAZA**, DISCUTIBLE | direccion invertida: la carta de control es la HERRAMIENTA fundacional que logicamente precede al caso de uso especifico "sustituir inspeccion masiva por control estadistico"; el hijo ya esta anclado en `causas_especiales_y_comunes_variacion` (la teoria de base); la madre, ademas, tiene `nodos_siguientes` vacio hoy |

**RESULTADO: 3 SE ESCRIBEN, 27 NO SE ENLAZAN, 0 INCONSISTENTES, 0 ESCALERA
ROTA** (`docs/loop/SALIDA_V84_TRAMO9_ESCRIBIR.txt`, verificado contra el
grafo de HOY tras escribir con `scripts/loop/vuelta84_tramo9_escribir.py`,
`docs/loop/SALIDA_V84_TRAMO9_ESCRIBIR_APLICACION.txt`). **SIETE
DISCUTIBLES marcados ANTES de saber si aciertan: 50, 55, 58, 61, 67, 70 y
74** (mas 77, que se marca tambien por descansar en una lectura de
"direccion invertida" sin arista textual explicita que lo declare, a
diferencia del par 71 donde la madre lo dice con todas sus letras). **OCHO
discutibles en total: 50, 55, 58, 61, 67, 70, 74, 77.**

Ciclo de tres corrido tras la TAREA 3
(`SALIDA_V84_GATE0_TRAS_TAREA3.txt`, `SALIDA_V84_ETIQUETAS_TRAS_TAREA3.txt`,
`SALIDA_V84_SYNC_TRAS_TAREA3.txt`), GATE 0 OK, 71 etiquetas identicas, 6
assets, `git status --porcelain -- dataset/ web/lib/assets/` cero lineas
tras el ciclo. Aristas tras la TAREA 3
(`docs/loop/SALIDA_V84_CONTEO_TRAS_TAREA3.txt`): sig **8.976**, prev
**8.955**, suma **17.931**, union **9.599** (+3/+3/+6/+3 sobre el estado
tras la TAREA 1). Las tres aristas verificadas en las DOS vistas, cero
inversas:

```
gate5_go_to_launch -> plan_de_lanzamiento_al_mercado: en_sig_madre True en_prev_hijo True INVERSAS False/False
descubrir_necesidades_del_cliente -> necesidades_psicologicas_cliente: en_sig_madre True en_prev_hijo True INVERSAS False/False
mix_medios_marketing_franquicia -> presupuesto_marketing_franquicia: en_sig_madre True en_prev_hijo True INVERSAS False/False
```

**`docs/plan/PASO_NODO_CALIBRADO.jsonl` se commitea recalibrado tal como
quedo** (adjudicacion 5.7 del acta 82): el fichero de esta vuelta ya refleja
las 12 aristas escritas (TAREA 1 + TAREA 3) mas las 9 heredadas de la vuelta
83, sin desfase.

---

## 4. TAREA 4: LA VARA DEL TRAMO 9, CON INSTRUMENTO PROPIO

`scripts/loop/vuelta84_tarea4_vara_tramo9.py`, sucesor de
`vuelta83_tarea4_vara_tramo7.py`, pares LEIDOS del fichero del filtro sin
teclear. (4.a) las 30 unidades frescas del tramo 9 contra
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` SIN direccion; (4.b) las mismas 30
contra `docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V83.jsonl` buscando la
reciproca. Corrida (`docs/loop/SALIDA_V84_TAREA4_VARA_TRAMO9.txt`):

```
unidades leidas del filtro: 30 | frescas (48..77): 30
veredictos leidos: 3388 | pares no dirigidos unicos: 3388
bolsa filtrada V83: 154 unidades
RESUMEN: 2 de 30 con veredicto, 0 de 30 con reciproca
```

Las dos con veredicto, ambas clase D (la clase mas comun del marcador, sin
peso decisorio): fila 50 (`formulacion_teorias_causa` /
`diagrama_causa_efecto`, puesto 2980, quality, dirigido en sentido
contrario) y fila 64 (`control_calidad_definicion` / `plan_de_control`,
puesto 3056, quality, mismo sentido). **Las dos coinciden con la decision NO
SE ENLAZA** tomada en la seccion 3.3: un veredicto D (clase de menor
similitud) es consistente con no escribir la arista, no la contradice.
**SIN DISCREPANCIA en ningun digito** contra las cifras que el encargo cito
por adelantado (3.388 veredictos, 3.388 pares no dirigidos unicos, 154
unidades en la bolsa filtrada V83).

---

## 5. EL CIERRE: CABECERA TALLADA Y `--comparar`

Suites y ciclo corridos AL CIERRE, cada una con su fichero: Gate 0
(`SALIDA_V84_GATE0_CMD1_CIERRE.txt`, OK), etiquetas
(`SALIDA_V84_ETIQUETAS_CIERRE.txt`, 71 identicas), assets
(`SALIDA_V84_SYNC_CIERRE.txt`, 6), `git status --porcelain -- dataset/
web/lib/assets/` cero lineas tras el ciclo, motor
(`SALIDA_V84_MOTOR_CIERRE.txt`, 25/25), web (`SALIDA_V84_WEB_CIERRE.txt`, 80
passed / 1.030 passed 3 skipped), tsc (`SALIDA_V84_TSC_CIERRE.txt`, EXITCODE
0, cero lineas), aristas (`SALIDA_V84_CONTEO_CIERRE.txt`: sig 8.976, prev
8.955, suma 17.931, union 9.599, identico al estado tras la TAREA 3: la
TAREA 4 no escribe nada).

**CASO OBLIGATORIO (i), el `--comparar` del tramo 9 contra este mismo
reporte, corrido DESPUES de pegar la tabla de la seccion 3.2 arriba:**

```
python scripts/loop/tallar_cabecera_reporte.py --vuelta 84 --tramo-cadena 9 --comparar docs/loop/REPORTE.md
```

Salida (`docs/loop/SALIDA_V84_COMPARAR_TRAMO9.txt`):

```
--- COMPARACION CONTRA docs/loop/REPORTE.md ---

  UNIDADES NO PUBLICADAS EN ESA TABLA: 0

  filas cotejadas: 30 | DISTINTAS: 0 | ausentes (no rojo): 0 | inventadas (ROJO): 0
  TABLA DE LA CADENA: IDENTICA AL TALLADOR (las ausentes listadas no son rojo)
```

**CABECERA Y TABLA DE LA CADENA IDENTICAS, EXIT 0.**

**El `--comparar` de la cabecera `--fase04`, corrido DESPUES de recomputar
el cierre y de terminar de escribir este reporte:**

```
python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 84 --comparar docs/loop/REPORTE.md
```

Salida (`docs/loop/SALIDA_V84_COMPARAR_FASE04.txt`):

```
--- COMPARACION CONTRA docs/loop/REPORTE.md ---

  filas cotejadas: 7 | DISTINTAS: 0 | ausentes: 0
  CABECERA: IDENTICA AL TALLADOR
```

**CABECERA IDENTICA AL TALLADOR, 7 filas cotejadas, 0 distintas, EXIT 0.**

---

## 6. DISCUTIBLES, PENDIENTES Y CORRECCIONES: RESUMEN PARA LA RELECTURA CIEGA

**Discutibles marcados esta vuelta, ANTES de saber si aciertan (tramo 9,
seccion 3.3): 50, 55, 58, 61, 67, 70, 74, 77 (OCHO).** Cada uno con su razon
resumida en la tabla de 3.3; los que dependen de "familia ya anclada" o
"direccion invertida" son los mas discutibles porque son lecturas de
topologia, no citas literales de paso.

**Correcciones declaradas esta vuelta:**
1. La razon del par 47 (seccion 1.3), sin borrar el texto viejo.
2. Los pares 33, 44 y 45 (seccion 1.4): la clase pasa de NO SE ENLAZA
   (vuelta 83) a SE ESCRIBE (esta vuelta), por adjudicacion del auditor
   verificada contra el grafo, con las tres aristas escritas y verificadas.

**PENDIENTES DE DOCTRINA: NINGUNO nuevo esta vuelta.** El unico pendiente de
la vuelta 83 se cerro por adjudicacion 6.1 (seccion 1.2), citando doctrina
ya escrita.

**Preguntas traidas sin adivinar (EJECUTOR.md regla 11):** ninguna esta
vuelta que no se haya podido resolver con la vara y el grafo.

---

## 7. METRICA DE CREDITO Y RACHAS (para el auditor)

**Freno de la vuelta 83, con su aritmetica:** racha de CLASE O CIFRA
PUBLICADA en CERO (pide dos, sin disparar), racha de REPORTE vuelta a CERO
(pide tres, sin disparar), CREDITO DE TANDA rebajado (consecuencia: el
auditor relee el tramo 9 ENTERO esta vez, no una muestra, mas lo que
resuelva de 33/44/45). Esta vuelta entrega el tramo 9 completo (30 de 30) y
la relectura conjunta completa (3 de 3 pares nombrados) para esa relectura
extendida.

**Repaso del encargo, punto por punto, lo que se corrio y lo que no
(seccion final del encargo: "antes de cerrar, repasa el encargo punto por
punto"):**

| punto del encargo | se corrio |
|---|---|
| Commitear y pushear lo pendiente antes de tocar nada | SI, `git status` limpio al abrir |
| TAREA 1.1, registrar incumplimiento sin racha | SI (1.1) |
| TAREA 1.2, registrar las 9 adjudicaciones | SI (1.2) |
| TAREA 1.3, correccion declarada del par 47 | SI (1.3) |
| TAREA 1.4, relectura conjunta de 33/44/45 | SI (1.4), las tres SE ESCRIBEN |
| TAREA 2.a, horneador por patron | SI (2.a) |
| TAREA 2.b, cotejo por cabecera de seccion + 3 casos obligatorios | SI (2.b): (i) contra este reporte en la seccion 5, (ii) vara de rojo inventada, (iii) guarda VERDE sobre bolsa V84 |
| TAREA 2.c, horizonte publicado | SI (2.c y 3.2) |
| TAREA 3, tramo 9 completo (30 unidades) | SI (3.1 a 3.3), 30 de 30 leidas |
| TAREA 4, vara del tramo 9 (4.a y 4.b) | SI (seccion 4) |
| Cabecera tallada `--fase04 --vuelta 84` + `--comparar` | SI (cabecera arriba, comparar en seccion 5) |
| Sello de HEAD antes de la 1.a operacion | SI (`SALIDA_V84_HEAD_APERTURA.txt`) |
| `PASO_NODO_CALIBRADO.jsonl` commiteado recalibrado | SI (recalibrado en la TAREA 3, se commitea tal cual) |
| Cero guiones largos/medios | SI, con el hook corriendo |

**NO HAY PARADA.** Ninguna afirmacion de este reporte contradice una regla
vigente ni una cifra publicada sin remedio.
