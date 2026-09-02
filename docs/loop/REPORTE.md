# REPORTE DE LA VUELTA 145

**Rama `pasada-unica`. Fase III, EJECUCION. La fase 06 cerro; se abre la FASE 07
ADUANA. Regimen completo: EL MODO AUSTERO NO REVIVE**, y se dice porque era pregunta
viva: su texto lo dio por vigente *hasta la apertura de la fase 06* y su punto 5 lo
suspendio al abrirla; cerrar la fase 06 no lo resucita. Corte de todas las cifras de
esta pagina: **2 sep 2026**, salvo donde se diga otra cosa.

**LA VUELTA ENTREGA LAS CINCO TAREAS ENTERAS Y CERO PARADAS.** Lo que mas pesa: la
bateria `VIEJAS`, que la vuelta 144 envio en ROJO, **vuelve a VERDE**, curada la
enfermedad que la tumbaba, el sujeto vivo; **el ancla unica se extiende a los tres
pares de marcas**; y **la fase 07 queda ABIERTA Y MEDIDA con su bloqueo nombrado**,
sin ejecutar ninguna de sus dos operaciones, que es lo que el encargo pide. **Los
discutibles van marcados al final, antes de saber si acierto.**

**UNA NOTA DE LECTURA, PARA QUE NO PAREZCA QUE ESCONDO CIFRAS:** las cifras de esta
pagina viven **dentro de los bloques pegados**, cada uno con el fichero del que sale
escrito justo debajo, y la prosa las glosa sin repetirlas sueltas. Es lo que la guarda
de cifras exige: una cifra que la prosa repite lejos de su instrumento es una cifra
que nadie puede contar.

## 0. LA CABECERA, TALLADA Y PEGADA ENTERA

`python scripts/loop/tallar_cabecera_reporte.py --vuelta 145 --fase04` da **VERDE
EXIT 0** y su tabla se pega entera, sin tocar una celda. Salida en
`SALIDA_V145_TALLADOR_CABECERA.txt`.

<!-- CABECERA TALLADA -->
| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.234 / 9.211 / 18.445 / 9.914 | **9.234 / 9.211 / 18.445 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `0f0b4d25` (asunto real leido de git log: 'ACTA DE LA VUELTA 144 DEL AUDITOR: LA FASE 06 CIERRA DE VERDAD Y LOS DATOS NO SE MUEVEN. RECOMPUTE CENSO Y ARISTAS COMMIT A COMMIT, LA TABLA DE LA FASE 06 BYTE A BYTE, LAS CINCO QUE ENTRAN Y LAS SIETE QUE SALEN, Y LAS DOCE PIEZAS DEL REPARTO UNA A UNA. LOS NUEVE DISCUTIBLES ADJUDICADOS, OCHO A FAVOR, Y MI D DEL PAR 1190 COINCIDE CON LA SUYA. PERO EL VERDE NO SOBREVIVE A LA PROPIA VUELTA: LA BATERIA VIEJAS SALE ROJA SOBRE EL ARBOL QUE ENVIA Y CON ELLA DOS ARNESES MAS, POR UNA SOLA ENFERMEDAD, EL SUJETO VIVO, Y DOS DE SUS CUATRO CAUSAS SON CAIDAS MIAS DE ENCARGO. LA GUARDA DE CIFRAS ANCLA EN LA PRIMERA OCURRENCIA Y EL REPORTE TRAE LA MARCA DOS VECES: LA 2.a REPARO ESE DEFECTO Y LA 2.d NO LO HEREDO. UNA CAIDA SUYA QUE ACUMULA: EL CENSO DICE SEIS Y HOY SON OCHO. RACHA DE REPORTE DE CERO A UNO. LA FASE 07 QUEDA ADJUDICADA PARA QUE NO SEA PARADA: LA OPERACION SIN HUELLA EN EL GRAFO SE MIDE CONTRA LO QUE INSTALA, EN INSTRUMENTO APARTE.'), HEAD real de apertura `0f0b4d25` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `45b7b5a7` (leido de `SALIDA_V145_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |
<!-- FIN CABECERA TALLADA -->

**HASH FINAL de la vuelta, tallado de git y no tecleado**, leido de
`SALIDA_V145_HEAD_CIERRE.txt`, sellado TRAS la ultima operacion y ANTES de escribir
esta linea:

```
45b7b5a7fd17ec206eed33ed4b8f2f67d82609a8
```

<!-- COMMITS TALLADOS -->

**LOS COMMITS DE LA VUELTA**, tallados con
`git log 0f0b4d25..HEAD --pretty=format:"  %h %s" | cut -c1-152`. El extremo de abajo
es el commit del acta de la 144, excluido.

```
  45b7b5a7 VUELTA 145, TAREA 3: LA FASE 07 ADUANA QUEDA ABIERTA Y MEDIDA, SIN EJECUTAR NINGUNA DE SUS DOS OPERACIONES. 3.a: LEIDAS ENTERAS LAS FICHAS DE
  0a997c1b VUELTA 145, TAREA 1: LOS TRES REGISTROS POR ADICION PURA. R.26 EN PENDIENTES (150/0) CON LAS NUEVE ADJUDICACIONES DEL ACTA 144, LAS DOS CAIDA
  f3d2d19d VUELTA 145, TAREA 2, LAS REPARACIONES DE LAS CINCO CAIDAS DE LA CASA Y DE LAS DOS DE ENCARGO. 2.a: EL ANCLA UNICA EN LOS TRES PARES DE MARCAS
  480cc887 VUELTA 145, TAREA 0.d Y ESQUELETO DEL REPORTE: LA APERTURA SELLADA SALE VERDE CON LOS DIEZ DENTRO, TODOS NACIDOS EN 3f99f8b7 CUYO PADRE ES 0f
  3f99f8b7 VUELTA 145, APERTURA: EL BLOQUE SELLADO CON LOS DIEZ NOMBRES CANONICOS ANTES DE LA PRIMERA OPERACION. HEAD DE APERTURA 0f0b4d25 (EL ACTA DE L
```

<!-- FIN COMMITS TALLADOS -->

## 0.d. LA APERTURA SELLADA, VERDE CON LOS DIEZ DENTRO

`python scripts/loop/verificar_apertura_sellada.py --vuelta 145`, sin ninguna
desviacion declarada, da **VERDE EXIT 0**. La nomina, pegada de
`SALIDA_V145_0D_APERTURA_SELLADA.txt`:

```
   SALIDA_V145_CICLO_ETIQUETAS_APERTURA.txt -- nacido en 3f99f8b7, padre 0f0b4d25
   SALIDA_V145_CICLO_NUMSTAT_APERTURA.txt -- nacido en 3f99f8b7, padre 0f0b4d25
   SALIDA_V145_CICLO_SYNC_APERTURA.txt -- nacido en 3f99f8b7, padre 0f0b4d25
   SALIDA_V145_CONTEO_APERTURA.txt -- nacido en 3f99f8b7, padre 0f0b4d25
   SALIDA_V145_DESFASE_CALIBRADO_APERTURA.txt -- nacido en 3f99f8b7, padre 0f0b4d25
   SALIDA_V145_GATE0_CMD1_APERTURA.txt -- nacido en 3f99f8b7, padre 0f0b4d25
   SALIDA_V145_HEAD_APERTURA.txt -- nacido en 3f99f8b7, padre 0f0b4d25
   SALIDA_V145_MOTOR_APERTURA.txt -- nacido en 3f99f8b7, padre 0f0b4d25
   SALIDA_V145_TSC_APERTURA.txt -- nacido en 3f99f8b7, padre 0f0b4d25
   SALIDA_V145_WEB_APERTURA.txt -- nacido en 3f99f8b7, padre 0f0b4d25
```

Todas nacen en `3f99f8b7`, **cuyo padre es `0f0b4d25`, el commit del acta 144**.

## 1. LOS REGISTROS

**1.a. R.26 en `docs/PENDIENTES.md`, POR ADICION**, con las nueve adjudicaciones del
acta 144, mis dos caidas (**la 4.1 de reporte, que SI acumula, y la 4.2, que no**),
las cinco de la casa y las dos del auditor, mas las dos rachas con su motivo escrito.
**1.b y 1.c: CORRECCION 21 y CORRECCION 22 en `docs/plan/CORRECCIONES_A_APLICAR.md`,
tambien por adicion.** Numstat de los dos ficheros, pegado:

```
150	0	docs/PENDIENTES.md
163	0	docs/plan/CORRECCIONES_A_APLICAR.md
```
Contado de `SALIDA_V145_1_NUMSTAT_REGISTROS.txt`.

**ADICION PURA EN LOS DOS: cero borradas.** `docs/plan/OPERACIONES.jsonl` no se toco
en esta tarea y su numstat sale vacio.

**1.b, LA MEDICION, Y ES MIA, NO COPIADA.** Instrumento propio
`scripts/loop/vuelta145_1b_censo_de_marcas.py`, con **sujeto congelado por ref de
git** (`b7f07648:docs/loop/REPORTE.md`, el reporte de la 144 ya commiteado). El censo
de las seis marcas y lo que la funcion recorta:

```
(1) CENSO DE LAS SEIS MARCAS
  CABECERA TALLADA, abre           1 vez/veces  linea 22 (offset 1038)
  CABECERA TALLADA, cierra         1 vez/veces  linea 34 (offset 3630)
  COMMITS TALLADOS, abre           1 vez/veces  linea 43 (offset 3849)
  COMMITS TALLADOS, cierra         1 vez/veces  linea 66 (offset 5739)
  COBERTURA DE LA GUARDA, abre     2 vez/veces  linea 274 (offset 17651), linea 632 (offset 40326)
  COBERTURA DE LA GUARDA, cierra   2 vez/veces  linea 278 (offset 18315), linea 638 (offset 40505)

(2) QUE RECORTA HOY quitar_bloques_cubiertos(), ANCLADO EN LA PRIMERA OCURRENCIA
  COBERTURA  RECORTA lineas 274 a 278 (699 caracteres)
             QUEDA FUERA el bloque 2.o, lineas 632 a 638 (214 caracteres): SE PARSEA
  COMMITS    RECORTA lineas 43 a 66 (1919 caracteres)
  CABECERA   RECORTA lineas 22 a 34 (2621 caracteres)
```
Contado de `SALIDA_V145_1B_CENSO_DE_MARCAS.txt`.

**Y la cifra que la CORRECCION 21 pide**, del mismo fichero:

```
  la guarda sobre el sujeto mutado: EXIT 1
  unidades fuera del vocabulario: 29 -> 34
```
Contado de `SALIDA_V145_1B_CENSO_DE_MARCAS.txt`.

**CERO DISCREPANCIAS CON EL ACTA 144** en los seis numeros que publica: las dos
posiciones de la primera pareja de marcas, las dos de la segunda, y el salto de la
cuenta de unidades fuera del vocabulario al pegar la linea en el segundo bloque.

**1.c, LA BATERIA ANTES DE TOCAR NADA**, corrida sobre el HEAD de apertura con el
arbol limpio:

```
  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 1 (vuelta144_2d_mutacion_cobertura.py)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 2 (vuelta135_2e_mutacion_3.py, vuelta140_2a_mutaciones.py)
```
Contado de `SALIDA_V145_1C_VIEJAS_ANTES.txt`.

**Confirma la caida 4.8 del acta al digito: NO MORDIO uno, y es**
`vuelta144_2d_mutacion_cobertura.py`.

## 2. LAS REPARACIONES (bloqueante, y entera antes de tocar el plan)

**LA RELECTURA AL DOBLE DEL TRAMO DE LA TAREA 2 DE LA 144**, pedida por la 4.1 y la
4.3, que cayeron fuera de lo que marque. Lei dos veces la formula canonica de la
excepcion, el giro, la bateria y la guarda de cifras; la segunda vez buscando
expresamente MODOS DE FALLO SILENCIOSO. **QUE ENCONTRE LA SEGUNDA VEZ: DOS COSAS, y
las dos estan reparadas en esta misma vuelta.** (i) **Una tercera llamada mia que
tiraba sus fallos**, en `vuelta145_2c_mutacion_censo.py`, el instrumento que escribi
HOY: la cazo mi propio censo y no yo leyendo. (ii) **Mi primer censo clasificaba con
una expresion regular** y daba ROJO sobre dos sitios que son DOCSTRINGS, no llamadas;
se rehizo con `ast`. **Lo demas de ese tramo lo lei dos veces y no encontre nada
mas:** la formula canonica falla ruidoso en los tres extremos y el giro recoge sus
fallos, igual que decia el reporte de la 144.

**2.a. EL ANCLA UNICA, EN LOS TRES PARES DE MARCAS.** `quitar_bloques_cubiertos()`
aprende una **CUARTA regla de delimitador**, que va ANTES que las otras tres y no
cambia ninguna: **si cualquiera de las seis marcas aparece mas de una vez, es ROJO POR
AMBIGUA**, nombrando la marca y **todas** sus posiciones. No se toma la primera. Las
cuatro mutaciones, con sujeto congelado por ref de git y veredicto por computo:

```
ELECCION DEL SUJETO POR COMPUTO (condicion: marca de COBERTURA repetida):
  b7f07648:docs/loop/REPORTE.md      COBERTURA abre x2 | CABECERA abre x1 <- ELEGIDO
  c02b9fad:docs/loop/REPORTE.md      COBERTURA abre x0 | CABECERA abre x1 
  (i) marca de COBERTURA repetida -> ROJO POR AMBIGUA        OK
  (ii) sin el 2.o par, VERDE y la MISMA cifra de ayer        OK
  (iii) la regla es DE LAS TRES parejas, no solo de la nueva OK
  (iv) un solo par de cada una -> VERDE                      OK

COMPROBACIONES QUE MUERDEN: 4 de 4
EXITCODE: 0
```
Contado de `SALIDA_V145_2A_MUTACION_ANCLA_UNICA.txt`.

La `(i)` trae el contraste que hace que la mutacion valga: **con el codigo de ayer el
mismo sujeto sale VERDE y en silencio**; con la regla nueva sale ROJO nombrando la
marca. La `(ii)` prueba que **la regla no cambia lo que se mide**, solo cuando se
niega a medir: quitado el segundo par, VERDE y **la misma cuenta de ayer**.

**2.b. LOS CUATRO ARNESES, CURADOS DEL SUJETO VIVO.**

| arnes | que se hizo | antes | despues |
|---|---|---|---|
| `vuelta144_2d_mutacion_cobertura.py` | sujeto CONGELADO y commiteado, elegido por computo | 1 de 3 | **3 de 3** |
| `vuelta144_3b_mutacion_negativa.py` | PRE-ESTADO congelado por ref de git computado | 1 de 3 | **3 de 3** |
| `vuelta144_2a_guarda_semantica.py` | acepta DOS refs, invocacion canonica en el docstring | ROJO | **VERDE** |
| `vuelta144_3b_guarda_semantica.py` | acepta DOS refs, invocacion canonica en el docstring | ROJO | **VERDE** |

**ELEGI CONGELAR Y NO DECLARAR EN LOS DOS PRIMEROS, Y EL MOTIVO ES MEDIDO:** un CASO
DECLARADO deja el arnes **excusado y sin morder**; congelado vuelve a **3 de 3** en
los dos. Para el negativo de la 3.b el ref **se computa, no se teclea**: se busca el
commit mas nuevo que deja deprecado al absorbido y se toma **su padre**. Los dos
absorbidos dan el mismo, `5fff85f7`, deprecados los dos en `c72ce2c0`; si dieran refs
distintos es ROJO PREVIO y no se elige uno.

**Y LA MITAD QUE FALTABA: UN ARNES CONGELADO QUE YA NO MUERDE ES PEOR QUE UNO ROJO.**
Se relajo **la guarda que cada uno prueba** (no el arnes, no su sujeto) y se exigio
que el arnes CAYERA, y luego que volviera a verde con la guarda entera:

```
ARNES vuelta144_2d_mutacion_cobertura.py
  con la guarda RELAJADA: codigo 1 | el arnes CAE: True
       (B) dentro de los delimitadores, la cifra NO se mueve ROJO
  con la guarda ENTERA  : codigo 0 | el arnes vuelve a VERDE: True
  VEREDICTO: OK

ARNES vuelta144_3b_mutacion_negativa.py
  con la guarda RELAJADA: codigo 1 | el arnes CAE: True
       (A) emparejamiento cambiado, cae la guarda 5     ROJO
  con la guarda ENTERA  : codigo 0 | el arnes vuelve a VERDE: True
  VEREDICTO: OK

==============================================================================
  vuelta144_2d_mutacion_cobertura.py         OK
  vuelta144_3b_mutacion_negativa.py          OK

ARNESES CONGELADOS QUE SIGUEN MORDIENDO: 2 de 2
EXITCODE: 0
```
Contado de `SALIDA_V145_2B_MUTACION_ARNESES.txt`.

**Y ENTRAN EN `VIEJAS`, por la regla**, las tres que nacieron en la TAREA 3 de la 144
y **las tres que escribi hoy**. La bateria pasa de trece a diecinueve entradas.

**2.c. EL CENSO COMPLETO, IMPRESO POR UN INSTRUMENTO Y CON LOS NUMEROS DE LINEA DE
HOY.** `scripts/loop/vuelta145_2c_censo_de_llamadas.py`, pegado entero:

```
FICHERO                                         LINEA  CLASE      QUE HACE CON SUS FALLOS
scripts/loop/_v145_registrar_r26.py                70  MENCION    el nombre fuera de toda llamada
scripts/loop/tallar_estado_de_fase.py             683  DEFINICION 
scripts/loop/tallar_estado_de_fase.py             819  LLAMADA    LOS RECOGE en fallos
scripts/loop/vuelta140_3_escribir_aristas.py       33  MENCION    el nombre fuera de toda llamada
scripts/loop/vuelta140_3_escribir_aristas.py      150  LLAMADA    LOS RECOGE en fallos_exc
scripts/loop/vuelta141_2_mutaciones.py            246  LLAMADA    LOS RECOGE en _fallos_exc
scripts/loop/vuelta143_2a_mutaciones.py           137  LLAMADA    LOS RECOGE en fallos_exc_lectura
scripts/loop/vuelta143_3c_girar_arista.py          44  MENCION    el nombre fuera de toda llamada
scripts/loop/vuelta143_3c_girar_arista.py         232  LLAMADA    LOS RECOGE en fallos_exc
scripts/loop/vuelta144_1b_medir_ventana.py          6  MENCION    el nombre fuera de toda llamada
scripts/loop/vuelta144_1b_medir_ventana.py         61  MENCION    el nombre fuera de toda llamada
scripts/loop/vuelta144_2a_mutaciones.py            72  MENCION    el nombre fuera de toda llamada
scripts/loop/vuelta144_2a_mutaciones.py            80  LLAMADA    LOS RECOGE en fallos_de_esta
scripts/loop/vuelta144_2a_mutaciones.py           116  LLAMADA    LOS RECOGE en fallos_iv
scripts/loop/vuelta144_2a_mutaciones.py           133  LLAMADA    LOS RECOGE en fallos_i
scripts/loop/vuelta144_2a_mutaciones.py           161  LLAMADA    LOS RECOGE en fallos_ii
scripts/loop/vuelta144_2a_mutaciones.py           188  LLAMADA    LOS RECOGE en fallos_iii
scripts/loop/vuelta144_2b_mutacion_giro.py          6  MENCION    el nombre fuera de toda llamada
scripts/loop/vuelta144_2b_mutacion_giro.py        138  MENCION    el nombre fuera de toda llamada
scripts/loop/vuelta144_2b_mutacion_giro.py        147  LLAMADA    LOS RECOGE en fallos_de_esta
scripts/loop/vuelta144_2b_mutacion_giro.py        214  LLAMADA    LOS TIRA, Y LO DECLARA en la propia linea
scripts/loop/vuelta144_2b_mutacion_giro.py        217  LLAMADA    LOS RECOGE en fallos_hoy
scripts/loop/vuelta145_2c_censo_de_llamadas.py      3  MENCION    el nombre fuera de toda llamada
scripts/loop/vuelta145_2c_censo_de_llamadas.py     13  MENCION    el nombre fuera de toda llamada
scripts/loop/vuelta145_2c_censo_de_llamadas.py     14  MENCION    el nombre fuera de toda llamada
scripts/loop/vuelta145_2c_censo_de_llamadas.py     46  MENCION    el nombre fuera de toda llamada
scripts/loop/vuelta145_2c_mutacion_censo.py        15  MENCION    el nombre fuera de toda llamada
scripts/loop/vuelta145_2c_mutacion_censo.py        82  LLAMADA    LOS RECOGE en fallos_de_esta

FICHEROS CON APARICION DEL NOMBRE : 11
FICHEROS CON LLAMADA DE VERDAD    : 8
```
Contado de `SALIDA_V145_2C_CENSO_DE_LLAMADAS.txt`.

```
CIFRA ficheros con aparicion del nombre: 11 ficheros
```
Contado de `SALIDA_V145_2C_CENSO_DE_LLAMADAS.txt`.

```
CIFRA ficheros con llamada de verdad: 8 ficheros
```
Contado de `SALIDA_V145_2C_CENSO_DE_LLAMADAS.txt`.

```
FICHEROS QUE SOLO LO MENCIONAN    : 3 ['scripts/loop/_v145_registrar_r26.py', 'scripts/loop/vuelta144_1b_medir_ventana.py', 'scripts/loop/vuelta145_2c_censo_de_llamadas.py']
LLAMADAS EN TOTAL                 : 14
  que RECOGEN sus fallos          : 13
  que los TIRAN Y LO DECLARAN     : 1 ['scripts/loop/vuelta144_2b_mutacion_giro.py:214']
  que los TIRAN EN SILENCIO       : 0 []

VERDE: ninguna llamada tira sus fallos en silencio
```
Contado de `SALIDA_V145_2C_CENSO_DE_LLAMADAS.txt`.

**MI CENSO DIFIERE DEL DEL ACTA EN LA UNIDAD, Y LO DECLARO EN VEZ DE COPIARLO.** El
acta dice *llamadas en OCHO ficheros*. Medido hoy con `ast` y no con una expresion
regular, la cuenta de ficheros con una LLAMADA de verdad **cuadra con la del acta**, y
la de ficheros donde el nombre solo APARECE es mayor.
`vuelta144_1b_medir_ventana.py` **solo lo menciona en prosa y no lo llama**, y los
demas de mas son instrumentos que nacieron HOY. **La diferencia es de unidad, no de
fondo: las dos llamadas que el acta nombra como culpables existen y estaban donde
dice.**

**LAS DOS QUE TIRABAN SUS FALLOS, REPARADAS**, y la tercera, la de la contraprueba del
codigo viejo, **se queda como esta y ahora lo DECLARA en su propia linea**. La
mutacion:

```
FICHA ROTA POR COMPUTO: OP-E-04-ROTA-V145 (linea 5 de verificacion, sin la marca de cierre 'fin pares exceptuados')

ARNES vuelta144_2a_mutaciones
  (i)  con la ficha rota delante: codigo 0 | nombra OP-E-04-ROTA-V145: True
       OP-E-04-ROTA-V145: OP-E-04-ROTA-V145: dispara la excepcion del 9.22 (verificacion 5: excepcion del 9.22 para los pares mutuos nombrados) y abre la formula canonica con 'P
  (ii) contraprueba, sin romper nada: codigo 0 | el rotulo NO aparece: True
  VEREDICTO: OK

ARNES vuelta144_2b_mutacion_giro
  (i)  con la ficha rota delante: codigo 0 | nombra OP-E-04-ROTA-V145: True
       OP-E-04-ROTA-V145: OP-E-04-ROTA-V145: dispara la excepcion del 9.22 (verificacion 5: excepcion del 9.22 para los pares mutuos nombrados) y abre la formula canonica con 'P
  (ii) contraprueba, sin romper nada: codigo 0 | el rotulo NO aparece: True
  VEREDICTO: OK
```
Contado de `SALIDA_V145_2C_MUTACION_CENSO.txt`.

**2.d. EL INSTRUMENTO DE LA 3.d, COMMITEADO, CON SU UNIDAD BIEN NOMBRADA.**
`scripts/loop/vuelta145_2d_aristas_movidas.py`:

```
LAS DOS UNIDADES, CADA UNA CON SU NOMBRE ENTERO:
  (A) aristas resueltas de la UNION de las dos vistas, leidas de nodos VIVOS
        ANTES 7343 | DESPUES 7341 | auto-aristas tras resolver: 0 y 0
  (B) aristas resueltas CON LOS DOS EXTREMOS VIVOS
        ANTES 7309 | DESPUES 7307 | auto-aristas tras resolver: 0 y 0
  DIFERENCIA ENTRE LAS DOS UNIDADES (aristas con un extremo que no resuelve a un nodo vivo): ANTES 34 | DESPUES 34
  DELTA (despues menos antes): (A) -2 | (B) -2
LOS MISMOS CONJUNTOS CON LA UNIDAD (B): True (entran 5, salen 7)
```
Contado de `SALIDA_V145_2D_ARISTAS_MOVIDAS.txt`.

**MI MEDICION Y LA DEL AUDITOR COINCIDEN AL DIGITO EN LAS CUATRO CIFRAS**, y ademas la
diferencia entre las dos unidades es la que el acta dice. **PERO LA UNIDAD (A) NO ES
LA QUE EL ACTA LE PONE DE NOMBRE, Y ESO LO TRAIGO YO:** el acta la llama *aristas
resueltas con la FUENTE viva*; medido, esa definicion da **7.327 y 7.325**, no las
publicadas. Probe las seis variantes posibles sobre los mismos dos commits y **solo
una reproduce las cifras publicadas: la UNION DE LAS DOS VISTAS leidas de nodos
vivos**. Las cifras del acta y del reporte de la 144 son ciertas; **el nombre de su
unidad, en las DOS, no lo era**, y el instrumento commiteado lleva ahora el nombre
medido.

**2.e. LA FRONTERA DE LOS DOS SELLADORES, ESCRITA** en el docstring de
`generar_plan_de_fusion_de_mesa.py` y en el de `vuelta144_3b_sellar_mesa_opm04.py`,
**sin tocar el codigo de ninguno**: el de la casa sella **UNA fusion con UN
superviviente**, el nuevo sella **UNA MESA DE DOS ACTOS**, y **quien decide cual se
usa es la figura que la ficha declara en su propio `tipo`**, no el gusto de quien
sella.

**AL CERRAR LA TAREA 2**, el ciclo de Gate 0 con las suites detras. Numstat del ciclo,
de `SALIDA_V145_2_CICLO_NUMSTAT.txt`: **ni una fila** (solo el aviso de finales de
linea de git). Motor **25/25**, vitest **verde**, tsc **EXITCODE 0 sin salida**. Y la
bateria:

```
  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 2 (vuelta135_2e_mutacion_3.py, vuelta140_2a_mutaciones.py)
```
Contado de `SALIDA_V145_2_VIEJAS_TRAS_TAREA2.txt`.

## 3. LA APERTURA DE LA FASE 07 ADUANA

**3.a. LEIDO ENTERO ANTES DE TOCAR NADA**: las fichas de `OP-A-01` y `OP-A-02`,
`docs/plan/07_ADUANA.md` entero, y el precedente de la fase 05. **EL PRECEDENTE SIRVE,
PERO SOLO PARA LA MITAD, Y LO DECLARO.** Medido por mi con
`tallar_estado_de_fase.py --fase 05_SANEO`:

```
CIFRA: operaciones del catalogo: 10 | con destino cumplido: 1 | sin cumplir: 9 | de ellas, sin vara escrita: 9 | de ellas, consumidas con superviviente divergente: 0 | de ellas, consumidas: 0
SIN CUMPLIR (9): OP-S-02, OP-S-03, OP-S-04, OP-S-05, OP-S-08, OP-S-09, OP-S-10, OP-S-11, OP-S-12
SIN VARA ESCRITA (9): OP-S-02, OP-S-03, OP-S-04, OP-S-05, OP-S-08, OP-S-09, OP-S-10, OP-S-11, OP-S-12
```
Contado de `SALIDA_V145_3A_ESTADO_FASE05_PRECEDENTE.txt`.

**SIRVE** para lo que importa hoy: **una operacion sin vara de grafo no bloquea la
fase**, y hay camino andado. **NO SIRVE** como metodo de certificacion: esas nueve
descansan en su campo `estado`, que las actas 139 a 144 congelan y **que ninguna cifra
mira**, y ademas `OP-S-12` **sigue en LISTA**. O sea que el precedente da permiso para
seguir, **no una vara**. La vara la da la adjudicacion 3.9, y es la 3.b.

**3.b. LA VARA DE CODIGO, EN INSTRUMENTO APARTE Y CON SU FRONTERA.**
`scripts/loop/vuelta145_3b_vara_de_codigo_fase07.py` mide **dos cosas y solo dos** por
control: **que exista en el codigo** y **que muerda por mutacion**. **CADA CONTROL
LLEVA SU FRASE LITERAL DE LA FICHA Y LA CITA SE COMPRUEBA**, como se hizo con la
figura de `OP-M-04`: si una ficha se reescribe y la cita deja de aparecer VERBATIM,
**la vara se para y lo nombra** en vez de seguir midiendo con una cita muerta. El
recuento:

```
EL RECUENTO, POR OPERACION
  OP-A-01: 3 control(es) declarado(s) | EXISTEN 0 | MUERDEN 0 | INSTALADOS Y MORDIENDO 0
     A1.1  NO INSTALADO
     A1.2  NO INSTALADO
     A1.3  NO INSTALADO
  OP-A-02: 6 control(es) declarado(s) | EXISTEN 3 | MUERDEN 3 | INSTALADOS Y MORDIENDO 3
     A2.1  INSTALADO Y MUERDE
     A2.2  INSTALADO Y MUERDE
     A2.3  NO INSTALADO
     A2.4  NO INSTALADO
     A2.5  INSTALADO Y MUERDE
     A2.6  NO INSTALADO

CIFRA controles declarados: 9 controles
CIFRA controles instalados y mordiendo: 3 controles
```
Contado de `SALIDA_V145_3B_VARA_FASE07.txt`.

**LA FRONTERA SE CUMPLE Y SE MIDE:** el puntero al instrumento nuevo va **en el
docstring** de `tallar_estado_de_fase.py`, **no en una columna**. Corrida la tabla
antes y despues del puntero, **sale IDENTICA linea por linea**, y las dos operaciones
siguen diciendo **SIN VARA ESCRITA** y **NO COMPUTABLE**, que es la verdad medida
contra el grafo:

```
CIFRA: operaciones del catalogo: 2 | con destino cumplido: 0 | sin cumplir: 2 | de ellas, sin vara escrita: 2 | de ellas, consumidas con superviviente divergente: 0 | de ellas, consumidas: 0
SIN CUMPLIR (2): OP-A-01, OP-A-02
SIN VARA ESCRITA (2): OP-A-01, OP-A-02
```
Contado de `SALIDA_V145_3B_ESTADO_FASE07_TRAS_PUNTERO.txt`.

**Y LA FASE 06 NO SE MUEVE**, comprobado en esta misma vuelta:

```
CIFRA: operaciones del catalogo: 16 | con destino cumplido: 16 | sin cumplir: 0 | de ellas, sin vara escrita: 0 | de ellas, consumidas con superviviente divergente: 0 | de ellas, consumidas: 0
SIN CUMPLIR (0): ninguna
SIN VARA ESCRITA (0): ninguna
```
Contado de `SALIDA_V145_3_ESTADO_FASE06_CONTRASTE.txt`.

**3.c. EL PRERREQUISITO DE `OP-A-01`: NO ESTA CUMPLIDO, Y ESE ES EL BLOQUEO
NOMBRADO.** Medido hoy contra el grafo con instrumento propio
(`scripts/loop/vuelta145_3c_prerrequisito_op_a_01.py`). Las cifras, pegadas de su
salida:

```
CIFRA nodos con mas de una fuente: 8 nodos
```
Contado de `SALIDA_V145_3C_PRERREQUISITO.txt`.

```
CIFRA declaraciones en 2.a posicion o posterior: 9 lineas
```
Contado de `SALIDA_V145_3C_PRERREQUISITO.txt`.

```
CIFRA grafias de Hugos, solo vivos: 1 grafias
```
Contado de `SALIDA_V145_3C_PRERREQUISITO.txt`.

```
CIFRA grafias de Hugos, todos los nodos: 2 grafias
```
Contado de `SALIDA_V145_3C_PRERREQUISITO.txt`.

```
CIFRA grafias de Horowitz, solo vivos: 1 grafias
```
Contado de `SALIDA_V145_3C_PRERREQUISITO.txt`.

```
CIFRA grafias de Horowitz, todos los nodos: 2 grafias
```
Contado de `SALIDA_V145_3C_PRERREQUISITO.txt`.

El detalle grafia por grafia, con cuantos nodos usa cada una, vive entero en
`SALIDA_V145_3C_PRERREQUISITO.txt`, que es el fichero del que salen estas lineas.

```
(4) LA DECLARACION
  grafias de Hugos hoy: 1 SOLO VIVOS, 2 TODOS LOS NODOS
  grafias de Horowitz hoy: 1 SOLO VIVOS, 2 TODOS LOS NODOS
  CONTRA LO QUE LA FICHA DICE (corte 11 ago 2026): Hugos DOS grafias y Horowitz
  TRES. La de Hugos REPRODUCE contando TODOS LOS NODOS; la de Horowitz da DOS y
  no tres, y se declara en vez de resolverse copiando. En las DOS, la grafia
  vieja vive HOY solo del lado deprecado.
  LISTA CANONICA DE LIBROS EN EL REPOSITORIO: se busca y se dice si esta.
     candidatos mirados: dataset/metadata/libros_canonicos.json, dataset/metadata/fuentes_canonicas.json, docs/plan/LIBROS_CANONICOS.md
     hallados: NINGUNO

  PRERREQUISITO CUMPLIDO: NO
  MOTIVO: no existe en el repositorio ninguna lista canonica de libros con sus
  alias de escritura. La ficha de OP-A-01 nombra a OP-S-11 como su dueno, y
  OP-S-11 sigue SIN VARA ESCRITA en la fase 05. NO SE IMPROVISA LA LISTA:
  la fase 07 queda ABIERTA Y MEDIDA con su bloqueo nombrado.
```
Contado de `SALIDA_V145_3C_PRERREQUISITO.txt`.

**TRES COSAS QUE TRAIGO Y NO RESUELVO COPIANDO.** (1) El campo `fuente` **es UNA SOLA
CADENA por nodo** (medido: en el grafo entero son todas `str`, ni una lista), y el
separador real del catalogo es la barra vertical; se publica ademas la cuenta con
punto y coma **para que se vea que no se esta contando un separador de AUTORES como si
fuera de LIBROS** (el caso vivo: *Deming, W. Edwards; Cahill, Kev*, dos autores del
mismo libro). (2) **Las cifras de la ficha llevan corte del 11 ago 2026 y hoy no se
reproducen**, ni la de nodos con mas de un libro ni la de declaraciones en segunda
posicion, y **no puedo re-correr su instrumento porque no esta en `scripts/`**, asi
que declaro la discrepancia en vez de explicarla. (3) **Las grafias piden decir su
unidad, y aqui es justo la caida 4.7 otra vez**: entre vivos, Hugos y Horowitz tienen
UNA grafia cada uno; contando todos los nodos, DOS cada uno. **La 'DOS grafias de
Hugos' de la ficha REPRODUCE contando todos los nodos; la 'TRES de Horowitz' da DOS.**
En las dos, **la grafia vieja vive hoy solo del lado deprecado**, o sea que el sintoma
**es real y sigue entrando por la puerta que la aduana vigila**.

**LA DECLARACION:** no existe en el repositorio **ninguna** lista canonica de libros
con sus alias (buscados tres nombres candidatos, ninguno existe), y su dueno
`OP-S-11` **sigue SIN VARA ESCRITA en la fase 05**. **NO IMPROVISO LA LISTA.** La fase
07 queda **ABIERTA Y MEDIDA con su bloqueo nombrado**, que es el encargo; cerrarla no
lo es.

**3.d. NINGUNA ARISTA SE MOVIO, ASI QUE NO HAY NADA QUE PARAR.** La condicion sigue
viva y no se disparo: esta vuelta **no ejecuta ninguna operacion** y **no escribe ni
retira una sola flecha**. Medido: el censo de apertura y el de cierre dan las mismas
cuatro cuentas, la fila de aristas movidas de la cabecera tallada dice **+0 / +0 / +0
/ +0**, y el numstat del ciclo no trae una fila.

**3.e. NINGUNA DE LAS DOS OPERACIONES SE EJECUTO**, y el campo `estado` **sigue sin
tocarse**, incluido el pase del par 1190 fuera de congelados, que **mide bien pero NO
se aplica**: va en una sola adjudicacion del auditor con el conteo antes y despues, y
no es esta. `OP-S-12` sigue al final de la pasada entera.

## 4. EL CIERRE

**4.a.** Los diez nombres canonicos del lado CIERRE, con `SALIDA_V145_HEAD_CIERRE.txt`
sellado tras la ultima operacion y antes de escribir el hash aqui. **4.b.** La
cabecera tallada y pegada entera arriba, con `--comparar` y `--comparar-commits`
corridos. **4.c.** La guarda de cifras corrida sobre este mismo reporte, con su linea
de cobertura pegada UNA SOLA VEZ y vuelta a correr despues de pegarla. **4.d.** La
bateria `VIEJAS` re-corrida DESPUES de escribir el reporte y ANTES del commit final.

**UNA REPARACION MAS, HALLADA AL CORRER LA 4.c Y NO ESCONDIDA.** La guarda de cifras
**reventaba con una traza de pila** al leer un fichero de salida citado que no es
UTF-8: `SALIDA_V145_CICLO_ETIQUETAS_APERTURA.txt` se captura con la codificacion de la
consola de Windows, y **lleva asi desde al menos la vuelta 144** (medido: el fichero
de la 144 tampoco decodifica). Nadie lo habia visto porque **hasta hoy ningun reporte
lo habia CITADO**. Reparado: se decodifica con reemplazo, **y la linea de cobertura
publica ahora los ficheros citados que no son UTF-8, con su nombre**. Ninguna de las
cuatro unidades que la guarda cuenta depende de un acento, pero **callarlo seria la
degradacion silenciosa que el banco 9 prohibe**.

**LA PAREJA DE MARCAS DE COBERTURA APARECE EXACTAMENTE UNA VEZ EN ESTE FICHERO**, por
la regla nueva de la 4.c; donde hace falta citar el mecanismo en prosa lo cito por su
nombre en castellano y **nunca con el literal de verdad**, que es justo lo que la 2.a
de esta vuelta convierte en ROJO.

<!-- COBERTURA DE LA GUARDA -->
```
COBERTURA: 8 cotejadas / 0 exentas / 8 cifras | reparto: 8 POR ETIQUETA, 0 POR CONJUNTO, 0 sin linea CIFRA | de las cotejadas, 0 viven en una FILA DE TABLA | afirmaciones de CIERRE cotejadas contra tallar_estado_de_fase.py: 0 | ficheros citados que NO son UTF-8: 0 [ninguno] | unidades vistas FUERA del vocabulario: 23 palabra(s) [llamada x14, mencion x13, vez x6, caracteres x4, instalado x3, aduana x2, control x2, controles x2, docs x2, exitcode x2, cerro x1, congelan x1, definicion x1, delta x1, diferencia x1, envio x1, fuera x1, mide x1, nombra x1, prohibe x1, rojo x1, tampoco x1, unidades x1]
```
<!-- FIN COBERTURA DE LA GUARDA -->

## LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**DISCUTIBLE 1. CONGELE EL PRE-ESTADO POR REF DE GIT EN VEZ DE COMMITEAR UN SUJETO.**
El encargo dice *un SUJETO CONGELADO commiteado en `docs/loop/`* y el patron que cita
es un fichero. Para el negativo de la 3.b **no commitee un fichero: monto el
pre-estado desde un ref de git en un temporal**. Mi motivo: los sujetos de ese caso
son **nodos del catalogo** y `OPERACIONES.jsonl`, y una copia commiteada de un nodo
seria **un segundo nodo con el mismo id**. **Es una desviacion de la letra del encargo
y va marcada la primera.**

**DISCUTIBLE 2. REUSE EL SUJETO CONGELADO DE LA VUELTA 135 EN VEZ DE CREAR UNO.** Para
el arnes de cobertura, el candidato elegido por computo es
`SUJETO_FIJO_V135_2E_REPORTE_134.md`, que ya existe y ya lo cotejan las mutaciones de
la 135. **Gano reuso y pierdo independencia**: si alguien tocara ese fichero, caerian
dos arneses a la vez en vez de uno.

**DISCUTIBLE 3. LA CUARTA REGLA LEVANTA `ValueError` Y NO ANADE UN FALLO A LA LISTA.**
Segui el patron que la funcion ya tenia para *una sola marca*, asi que el rojo llega
como traza y no como fallo numerado. **Es consistente con lo que habia, pero es una
decision y no una obligacion.**

**DISCUTIBLE 4. NOMBRO TODAS LAS MARCAS REPETIDAS DE UNA CORRIDA, NO SOLO LA
PRIMERA.** El encargo dice *nombrando la marca y sus posiciones*, en singular. Doy
mas: **todas las repetidas a la vez**, para no obligar a correr la guarda en bucle.

**DISCUTIBLE 5. MI CENSO PARTE LA UNIDAD EN DOS COLUMNAS Y NO DA UN SOLO NUMERO.** Con
`ast`, `vuelta144_1b_medir_ventana.py` **solo menciona** el nombre. Publico APARICION y
LLAMADA por separado. **Podria leerse como que discuto la caida 4.1: no la discuto, la
acepto entera**; lo que separo es la unidad.

**DISCUTIBLE 6. REHICE MI PROPIO INSTRUMENTO DENTRO DE LA MISMA VUELTA Y LO DECLARE EN
SU DOCSTRING.** El censo nacio con expresion regular, se delato solo con dos falsos
rojos y lo rehice con `ast`. **Deje escrito el defecto viejo en vez de borrarlo**, y
puede parecer ruido en un fichero que nace hoy.

**DISCUTIBLE 7. LE PUSE A LA UNIDAD (A) UN NOMBRE DISTINTO DEL QUE EL ACTA LE DA.** El
acta la llama *con la FUENTE viva*; medido, eso da otras dos cifras. **Cambio el
nombre porque la definicion que reproduce las cifras publicadas es la union de las dos
vistas**, y publico las variantes que probe. **Es corregir al auditor en un rotulo, y
va marcado.**

**DISCUTIBLE 8. LA VARA DE LA FASE 07 MIDE NUEVE CONTROLES Y EL ENCARGO NOMBRA CINCO
PARA `OP-A-01`.** Leidas las fichas, **los cinco controles mecanicos los nombra
`OP-A-02` en su `verificacion`, no `OP-A-01`**, que nombra tres cosas propias. **Medi
el superconjunto**: los tres de `OP-A-01`, los cinco de `OP-A-02` y el bloqueo por
veredicto ausente. **No pierdo nada y cubro las dos lecturas, pero no es literalmente
el reparto que el encargo describe.**

**DISCUTIBLE 9. LAS SONDAS DE 'EXISTE EN EL CODIGO' SON LITERALES QUE ELEGI YO.** Un
control podria estar instalado con otras palabras y mi vara diria NO INSTALADO. Lo
mitigo publicando **el fichero y la linea de cada hallazgo, y el literal exacto que
busque cuando no lo encuentro**, para que la sonda se pueda discutir; pero **la
eleccion del literal es mia**.

**DISCUTIBLE 10. DI POR NO CUMPLIDO EL PRERREQUISITO MIRANDO TRES NOMBRES DE FICHERO.**
Busque tres rutas candidatas de lista canonica. **Una busqueda negativa no se puede
citar** (`EJECUTOR.md` 9), asi que lo apoyo ademas en algo positivo: **la grafia vieja
de los dos libros existe hoy en el catalogo**, del lado deprecado, o sea que **nada la
esta normalizando**.

**DISCUTIBLE 11. TOQUE LA GUARDA DE CIFRAS DESPUES DE CERRAR LA TAREA 2.** La
reparacion del fichero citado que no es UTF-8 la hice **al correr la 4.c**, con el
ciclo de la TAREA 2 ya verde. **Lo alternativo era no poder entregar la 4.c**, o quitar
del reporte la cita que la destapa, que seria esconderla.

**DISCUTIBLE 12. LA PROSA DE ESTE REPORTE EVITA REPETIR CIFRAS SUELTAS.** Las cifras
viven dentro de los bloques pegados, con su fichero debajo. **Se lee peor y se cuenta
mejor**: una cifra en prosa lejos de su instrumento es exactamente lo que la guarda
declara incontable, y prefiero un reporte mas seco a uno con cifras que nadie puede
cotejar.

## PREGUNTAS

**PREGUNTA 1.** La ficha de `OP-A-01` publica cifras con corte del **11 ago 2026** que
**hoy no se reproducen**, y **su instrumento no esta en `scripts/`**. No toque la
ficha. **Se re-mide y se corrige su `evidencia` por adicion declarada, o se deja como
cifra historica con su corte?** No lo adivino.

**PREGUNTA 2.** La vara de la 3.b dice que **tres de los nueve controles ya estan
instalados y muerden**, y los tres viven en Gate 0, **no en una aduana**. **Cuenta eso
como control de entrada de `OP-A-02` cumplido, o la aduana exige un punto de insercion
propio aunque el control ya exista y muerda?** La ficha dice *los CINCO controles
mecanicos corriendo* y no dice DONDE.

