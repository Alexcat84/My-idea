# REPORTE DE LA VUELTA 157 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

**EL VEREDICTO DE UNA LINEA: LAS NUEVE TAREAS ENTREGADAS, LA BLOQUEANTE VACIA 62
DE LAS 113 DEL SACO, Y HAY UNA PARADA QUE NO ES MIA NI ES DE NADIE: LOS DOS
GUARDAS DEL CIERRE QUE BUSCAN "EL ACTA DE LA VUELTA N MENOS 1" NO PUEDEN CORRER,
PORQUE EL ACTA 156 NO EXISTE.** El auditor numero la suya **157** auditando mi
vuelta **156**, asi que para mi vuelta **157** el acta de apertura se llama
**157** y no **156**. No lo arreglo yo: es una guarda y la traigo.

## 0. LA IDENTIDAD, LEIDA DE GIT Y NO TECLEADA

Todo lo de esta tabla sale de `git rev-parse` y `git log` corridos en esta
vuelta, y los dos hashes estan sellados en fichero.

| | valor | de donde sale |
|---|---|---|
| rama | `pasada-unica` | `git rev-parse --abbrev-ref HEAD` |
| commit de apertura | `abb2fe4e` | `docs/loop/SALIDA_V157_HEAD_APERTURA.txt` |
| commit de cierre (antes del commit del reporte) | `60a79cf8` | `docs/loop/SALIDA_V157_HEAD_CIERRE.txt` |
| commits del corredor | 8 | `git rev-list --count abb2fe4e..HEAD` |
| intrusos en el corredor | 0 | los 8 son mios, uno por tarea |
| hashes admitidos | 0 (ninguno) | el encargo lo declara con su rotulo |

**Y UNA CAIDA MIA, LA PRIMERA Y LA DECLARO YO:** la apertura **la medi antes de
la primera operacion** (fue mi primera lectura del repo, `git rev-parse HEAD` con
el arbol limpio), **pero NO la selle en `SALIDA_V157_HEAD_APERTURA.txt` hasta el
cierre.** El valor no depende de mi memoria y por eso no contamina nada: `git
rev-parse 23004b4d^` da `abb2fe4e`, o sea que el padre de mi primer commit ES la
apertura. **Pero el sello llego tarde y eso se dice.**

## LA PARADA, Y VA PRIMERO PORQUE BLOQUEA DOS GUARDAS DEL CIERRE

**QUE PASA, MEDIDO Y NO SUPUESTO.** `scripts/loop/tallar_cabecera_reporte.py` y
`scripts/loop/verificar_apertura_sellada.py` localizan la apertura de la vuelta N
buscando en `git log` un commit que empiece por `ACTA DE LA VUELTA <N-1> DEL
AUDITOR` o `ACTA DEL AUDITOR, VUELTA <N-1>` (las dos lo tienen cableado como
`vuelta - 1`, lineas 836 y 266 de cada fichero). **Para mi vuelta 157 buscan el
acta 156, y el acta 156 NO EXISTE:** contado por mi con `git log --grep`, hay
**0 commits** con cada uno de los dos patrones. Las actas de la rama van **145,
146, 147, 149, 151, 153, 155, 157**.

**LO CONFIRMO CORRIENDO LA MISMA GUARDA CON EL INDICE CORRIDO, que es lo unico
que separa un instrumento roto de un indice desplazado**
(`docs/loop/SALIDA_V157_T9_APERTURA_SELLADA_158.txt`): con `--vuelta 158` la
guarda **encuentra el acta y deja de quejarse de ella**, y solo falla porque no
hay ficheros `SALIDA_V158_*_APERTURA.txt`. **La guarda esta sana. Lo que se
corrio es el indice.**

**QUE NO HAGO, Y POR QUE.** No parcheo ninguna de las dos. Son guardas, el
encargo no me autoriza a tocarlas, y por la regla 5 del EJECUTOR esto se escribe
como **PARADA** y no se arregla aqui. **Y no fabrico los ficheros de apertura
que faltan:** medirlos ahora y llamarlos apertura seria exactamente la caida de
las vueltas 28 y 29, medir tarde y publicar como si fuera temprano.

**QUE HAGO EN SU LUGAR, Y ES LA OTRA REGLA VIGENTE:** no publico tabla de
cabecera tallada, porque no hay tallador que la produzca, y **toda cifra de este
reporte va PEGADA del fichero de salida del que sale**. Es la letra del 26 ago
2026: si no existe fichero que contar, la tabla no se publica.

  - `tallar_cabecera_reporte.py --fase04 --vuelta 157`: **ROJO exit 1, 40 celdas
    no se pudieron leer**, salida `docs/loop/SALIDA_V157_T9_CABECERA.txt`.
  - `verificar_apertura_sellada.py --vuelta 157`: **ROJO exit 1, 1 cosa no
    cuadra**, salida `docs/loop/SALIDA_V157_T9_APERTURA_SELLADA.txt`.

**LAS OTRAS DOS GUARDAS DEL CIERRE SI CORREN Y LAS DOS SALEN VERDES**, y una de
ellas nacio hoy:

  - `verificar_cifras_del_reporte.py` sobre este reporte: **VERDE exit 0**, con
    `COBERTURA: 18 cotejadas / 0 exentas / 18 cifras` y `0 sin linea CIFRA`,
    salida `docs/loop/SALIDA_V157_T9_CIFRAS_REPORTE.txt`.
  - `verificar_re_sellado.py` sobre este reporte: **VERDE exit 0**, con
    `CIFRA re selladas SIN declarar en el reporte: 0`, salida
    `docs/loop/SALIDA_V157_T9_RE_SELLADO.txt`.
  - `verificar_mutaciones_viejas.py`, corrida **SOLA y sin nada al lado**:
    **VERDE exit 0**, salida `docs/loop/SALIDA_V157_T5_BATERIA.txt`. Se vuelve a
    correr sola al final del cierre y su segunda salida es
    `docs/loop/SALIDA_V157_T9_BATERIA_FINAL.txt`.

## 1. MIS CAIDAS, ANTES QUE NADA

**CAIDA 1, EL SELLO DE APERTURA TARDIO.** Ya esta arriba, en la seccion 0.

**CAIDA 2, DE INSTRUMENTO, CAZADA ANTES DE PUBLICAR.** Mi primer contador de
aristas del cierre dio **9742** para la union de las dos vistas, donde el archivo
publica 9914. **No publique el 9742 como discrepancia:** fui a mirar la
definicion, vi que contaba PARES NO ORDENADOS mientras que la union del archivo
es DIRIGIDA (las entradas de `nodos_previos` se dan la vuelta antes de unir), lo
arregle y dio **9914** con `solo_sig 1174` y `solo_prev 1134`. **El 9742 queda
escrito dentro de la propia salida** (`docs/loop/SALIDA_V157_T9_MARCADOR_CIERRE.txt`)
para que se vea de donde salio y con que vara.

**CAIDA 3, DE SEDE, Y LA CAZO MI PROPIA GUARDA DE ADITIVIDAD.** En la TAREA 1
puse la adjudicacion 6.7 DENTRO del docstring de `p3b_caso_positivo`, y
`git diff --numstat` canto **1 borrado**: ese docstring cierra con tres comillas
pegadas a su ultima linea de texto, asi que insertar dentro obligaba a re
escribir esa linea. **La guarda mordio, revertí y baje el bloque un renglon**, a
comentario inmediatamente debajo del docstring, dentro de la misma funcion.
Resultado final: **borrados 0 en los seis .py**.

## 2. TAREA 1, LAS DIEZ ADJUDICACIONES DEL ACTA 157

```
CIFRA adjudicaciones escritas en esta corrida: 13 operaciones
```

Pegado de `docs/loop/SALIDA_V157_T1_ADJUDICACIONES.txt`, corrido en esta vuelta.

```
CIFRA lineas del registro de citas: 154 linea(s)
```

Pegado de `docs/loop/SALIDA_V157_T1_ADJUDICACIONES.txt`, corrido en esta vuelta.

```
CIFRA ficheros de codigo tocados: 6 fichero(s)
```

Pegado de `docs/loop/SALIDA_V157_T1_ADJUDICACIONES.txt`, corrido en esta vuelta.

```
CIFRA borrados totales en los seis .py: 0
CIFRA entradas del registro con el texto viejo comprobado como PREFIJO: 154
CIFRA entradas cuya `razon` CRECIO: 1 (LD-OPC05-097)
```

Las tres lineas de arriba salen del mismo `docs/loop/SALIDA_V157_T1_ADJUDICACIONES.txt`.

Las diez donde el encargo manda: **6.1 y 6.2** en la razon de `LD-OPC05-097` y en
`vuelta156_tarea2a_pasos_con_hijo.py`; **6.3, 6.4, 6.6 y 6.8** en
`vuelta152_registro_de_citas_opc05.py`; **6.5** en la guarda de OP-C-05 de
`run_phase1.py`; **6.6** tambien en el registro; **6.7** en la funcion de la P3b;
**6.9** en `verificar_mutaciones_viejas.py`; **6.10** en
`verificar_cifras_del_reporte.py`. **La aditividad se midio, no se prometio:**
`numstat` con borrados 0 para los `.py` y assert de prefijo literal sobre las 154
razones del JSONL, no solo sobre la tocada.

## 3. TAREA 2, LA BLOQUEANTE: EL LOTE 1 DEL SACO

### 3.a LA NOMINA, RECOMPUTADA

```
CIFRA entradas con via LECTURA_DIRIGIDA: 122
CIFRA lecturas dirigidas CON puntero de paso: 6
CIFRA lecturas dirigidas SIN puntero de paso: 116
CIFRA de esas sin puntero que YA estan en D: 3 (LD-OPC05-002, LD-OPC05-040, LD-OPC05-097)
CIFRA todavia en C SIN puntero: 113
CIFRA todavia en C CON puntero: 6
CIFRA lecturas del lote 1: 66
```

Las siete cifras de arriba estan contadas en
`docs/loop/SALIDA_V157_T2A_NOMINA.txt`, que es la salida de esa tarea.

**Da 6 y 60, que es lo que el encargo declara, asi que se pudo leer.** Las
sesenta sin puntero van de `LD-OPC05-004` a `LD-OPC05-067`, tambien computado.

### 3.b EL VEREDICTO

```
CIFRA lecturas dirigidas por clase: {"C": 57, "D": 65}
CIFRA reclasificadas de C a D en este lote: 62
CIFRA que sostienen C en este lote: 4
CIFRA que ya estaban escritas: 0
```

Las cuatro cifras de arriba estan contadas en
`docs/loop/SALIDA_V157_T2_LOTE1.txt`, que es la salida de esa tarea.

**NINGUNA SALIO A.** No hay candidato a fusion, no se toco una arista y `n` no se
movio. El limite de la 6.1 sigue vigente y no se cruzo.

**LAS CUATRO QUE SOSTIENEN C, con sus dos lineas nombradas en la razon**, que es
lo que la 6.4 exige:

  - **`LD-OPC05-027`** (`cierre_segun_complejidad_venta` contra
    `metodologia_spin_selling`). LINEA 1, en SPIN paso 1: *diagnosticar si tu
    venta es pequena o grande*, expandida por los pasos 1 a 3 de cierre. LINEA 2,
    en cierre paso 3: *minimizar el cierre y enfocar el esfuerzo en las etapas de
    indagacion SPIN*, expandida por los pasos 2 y 3 de SPIN.
  - **`LD-OPC05-038`** (`control_estadistico_de_procesos` contra
    `plan_de_control`). LINEA 1, en plan de control paso 2: *el estandar que
    activara una accion, idealmente un limite de control de una carta*, expandida
    por los diez pasos del SPC. LINEA 2, en SPC paso 9: *definir instrucciones de
    interpretacion y accion*, expandida por los diez pasos del plan de control.
  - **`LD-OPC05-049`** (`decision_pivotar_o_proceder` contra
    `lienzo_modelo_negocio`). LINEA 1, en la decision paso 4: *toma un Canvas
    nuevo y busca game changers*, expandida por los doce pasos del lienzo. LINEA
    2, en el lienzo paso 12: *usar el lienzo como base para pivotar o validar*,
    expandida por los seis pasos de la decision.
  - **`LD-OPC05-122`** (`error_proofing_servicio` contra `metodologia_6s`), la
    que el acta 155 ya sostuvo a ciegas. LINEA 1, en error proofing paso 4:
    *simplificar el trabajo*, expandida por los seis pasos de 6S. LINEA 2, en 6S
    paso 6: *Safety*, expandida por los diez pasos de error proofing.

**LOS DOS AVISOS DEL ENCARGO, CONTESTADOS.** `LD-OPC05-046` **CAE A D**, y con
ello **queda revocada esa parte de la adjudicacion 6.3 del acta 155**, que lo
sostuvo en C por el 9.6.3, o sea POR SER SANO: bajo la 6.4 sano sin figura es D,
y ademas sus dos direcciones apuntan a la misma linea (el sistema que recolecta,
analiza y difunde). `LD-OPC05-122` **se sostiene**, y con sus dos lineas
nombradas.

### 3.c LA VARA, DECLARADA CON SUS LIMITES ANTES DE APLICARLA

Vive entera en el docstring de
`scripts/loop/vuelta157_tarea2_lote1_veredictos.py`. En corto: **una direccion
cuenta cuando la LINEA del nodo X es una ACCION y el nodo Y es el COMO SE HACE
esa accion**; mencionar al otro como contexto, precondicion o diagnostico **no
cuenta**; hacen falta **las dos** direcciones sobre **dos lineas distintas**; y si
las dos direcciones apuntan a la misma linea, **no es esta figura**, que es cita
literal del 9.22 y es la comprobacion que mas casos separo en este lote.

### 3.d LAS GUARDAS, MEDIDAS (misma salida)

```
C.1 PREFIJO: las 154 razones del registro conservan su texto viejo ENTERO
C.3 CLASES MOVIDAS: 62, y todas de C a D
C.4 FRONTERA, sha256 de dataset/ DESPUES: 1330ccb9c46c03d371cb1ecf7911c83bbb4b14db71a878b3405738000c90e9d8
    EL REGISTRO CAMBIA, EL GRAFO NO: sha256 IDENTICO y censo IDENTICO
C.5 CIFRA n, veredictos del cribado DESPUES: 3388
```

Las cuatro lineas de arriba estan contadas en
`docs/loop/SALIDA_V157_T2_LOTE1.txt`, que es la salida de esa tarea. **La guarda
C.2 no se pega aqui porque su fichero no la publica como linea `CIFRA` y una
cifra que no se puede contar de su fichero no se publica:** lo que dice, y vive
en esa misma salida, es que la coleccion de pares del registro es la misma antes
y despues, sin uno de mas ni uno de menos.

Gate 0 al terminar el lote, con el ciclo entero y en su orden:

```
CIFRA comprobaciones de Gate 0 que pasan: 26 comprobaciones
```

Pegado de `docs/loop/SALIDA_V157_T2D_CONTEO_GATE0.txt`, corrido en esta vuelta.

```
CIFRA comprobaciones de Gate 0 que fallan: 0 comprobaciones
```

Pegado de `docs/loop/SALIDA_V157_T2D_CONTEO_GATE0.txt`, corrido en esta vuelta.

### 3.e EL COTEJO CON LA CIEGA DEL AUDITOR, LEIDA DESPUES

Selle la lectura primero contra los nodos y solo despues abri
`docs/loop/_auditor_v157_mis_adjudicaciones.txt`, cuyo sha1 comprobe con
`git hash-object`: **`c3b1ceca60a7832346335b948dbad53c97610939`**, o sea el
`c3b1ceca` que el encargo declara.

**Y AQUI CORRIJO UNA CIFRA DEL ENCARGO, CONTANDOLA:** el encargo dice que
**cinco** de sus diez casos caen en mi lote (007, 019, 043, 055, 067). Son
**SEIS**: **`031` tambien esta**, porque es una de las seis con puntero de paso y
la nomina computada lo incluye. **Coincidimos en las seis, las seis en D.**

## 4. TAREA 3, LA INFERENCIA INVALIDA

Salida: `docs/loop/SALIDA_V157_T3_PASO1_JURAN.txt`. Lo medi yo, no lo copie:

```
CIFRA veredicto (1): VIVO
CIFRA pasos del candidato: 4
CIFRA veredicto (3): NO HAY ARISTA
CIFRA filas del calibrado con juran_rcca_metodo de madre: 2
CIFRA filas del calibrado que nombran a desperdicio_cronico_vs_esporadico: 0
CIFRA condiciones del contraejemplo que se cumplen: 4 de 4
```

`desperdicio_cronico_vs_esporadico` esta **VIVO** y sus cuatro pasos (monitorear,
diferenciar el pico esporadico del nivel cronico, accion correctiva, proyecto de
mejora) **despliegan el paso 1 de juran** (definir el problema: identificar si es
esporadico o cronico), **sin arista en ninguna de las dos vistas y sin fila en el
calibrado**. **Hay hijo, y la vara no lo veia.** La correccion por adicion vive en
la 6.2, en la razon de `LD-OPC05-097` y en el docstring del instrumento: *ningun
hijo adjudicado* es **una ausencia bajo la vara declarada**, no una prueba de
linea. **La clase no se mueve.**

## 5. TAREA 4, EL TACHADO

Salidas `docs/loop/SALIDA_V157_T4B_MUTACION_TACHADO.txt` (exit 0) y
`..._MUTADO.txt` (exit 1), y `docs/loop/SALIDA_V157_T4C_TACHADO.txt`.

```
CIFRA pares que recoge el lector VIEJO: 122
CIFRA pares que recoge el lector NUEVO: 122
CIFRA pares que recoge el lector VIEJO sobre el texto tachado: 121
coincidencias del patron VIEJO en la fila 97: 0
clase que le asigna (la ULTIMA escrita en la celda): 'D'
CIFRA filas tachadas en esta corrida: 3
CIFRA clases movidas por el tachado: 0 (ninguna)
```

Las tres condiciones que el encargo pide: **el lector viejo pierde la fila
tachada** (0 coincidencias), **el nuevo la recupera con la clase buena** (D), y
**el conteo sobre el fichero SIN tachar sale identico** (122 y 122, mismas claves
y mismas clases). **El caso rojo se probo por mutacion de su propia expectativa:**
con `--mutar` sale **exit 1**. Solo entonces las tres filas (002, 040 y 097)
recibieron su `~~C~~ D`, y Gate 0 lo vio en **26 de 26 en OK**.

## 6. TAREA 5, EL ROJO QUE NOMBRABA AL CULPABLE EQUIVOCADO

Salidas `docs/loop/SALIDA_V157_T5C_MUTACION_RUIDO.txt` (exit 0),
`..._MUTADO.txt` (exit 1) y `docs/loop/SALIDA_V157_T5_BATERIA.txt`.

```
CIFRA mutaciones en la nomina VIEJAS (contadas, no tecleadas): 23
CIFRA inestables (rojo del script)       : 0 (ninguno)
CIFRA ruido de concurrencia (aparte)     : 1 (_vecino_de_otro.txt)
CIFRA inestables que le cuelga al script : 1 (_vecino_de_otro.txt)
```

**El sujeto no es inventado.** La mitad (B) del caso importa la version **VIEJA**
de `correr_dos_veces` con `git show` del **commit de apertura leido de git log**,
y sobre EL MISMO escenario le cuelga `_vecino_de_otro.txt` a un script que no lo
escribe. La nueva sale limpia y lo nombra **aparte**, bajo RUIDO DE
CONCURRENCIA. **Y las 23 siguen siendo 23.**

**La bateria, corrida SOLA y sin nada al lado**, como manda la regla que el
auditor rompio y declaro:

```
  ANCLA PERDIDA  : 0 (ninguna)
  NO MORDIO      : 0 (ninguna)
  NO REPRODUCIBLE: 0 (ninguna)
  CASO DECLARADO : 2 (vuelta135_2e_mutacion_3.py, vuelta140_2a_mutaciones.py)
```

Las cuatro lineas de arriba estan pegadas de
`docs/loop/SALIDA_V157_T5_BATERIA.txt`, que es la salida de esa corrida. **La
linea nueva de RUIDO DE CONCURRENCIA sale ahi mismo y no la pego como cifra
porque esa salida no la publica como linea `CIFRA`:** dice que no aparecio
ningun fichero ajeno mientras la bateria corria, que es lo que se espera de una
corrida sola.

## 7. TAREA 6, EL RE SELLADO EN SILENCIO

Nace `scripts/loop/verificar_re_sellado.py`, con nombre estable y sin numero de
vuelta. Salidas `docs/loop/SALIDA_V157_T6B_MUTACION_RE_SELLADO.txt` (exit 0) y
`..._MUTADO.txt` (exit 1).

```
estado             : RE SELLADO
commit de su tarea : f95e4ee9f8d3
numstat contra HEAD: +7/-7
CIFRA lineas CIFRA cuyo VALOR cambio: 1
CIFRA filas sin declarar: 1 (SALIDA_V156_T4C_CIFRAS.txt)
CIFRA filas sin declarar: 0
```

Las seis lineas de arriba estan contadas en
`docs/loop/SALIDA_V157_T6B_MUTACION_RE_SELLADO.txt`, que es la salida de ese
caso. La linea CIFRA que se movio es `salidas selladas del tallador`, que pasa
de 52 a 55, y el valor viejo va sin su unidad a proposito para que no se lea
como una cifra que este reporte afirme: la afirma el fichero, no yo.

El sujeto del caso es **el fichero que el auditor pillo**. Las cuatro
comprobaciones: el sujeto esta re sellado de verdad; el reporte que calla deja
**1** fila sin declarar; el que trae la linea computada deja **0**; y un fichero
**SIN RE SELLAR** elegido por computo **no es acusado**.

**Y LA GUARDA MORDIO EN SU PRIMERA CORRIDA REAL, SOBRE ESTE MISMO REPORTE.**
Corrida contra `docs/loop/REPORTE.md`
(`docs/loop/SALIDA_V157_T9_RE_SELLADO.txt`) salio **ROJO exit 1** porque este
reporte cita `SALIDA_V156_T4C_CIFRAS.txt` y ese fichero cambio despues del
commit de su tarea sin que yo lo dijera. **Lo declaro con la linea que la propia
guarda computo, no con una narracion:**

```
RE SELLADO DECLARADO: SALIDA_V156_T4C_CIFRAS.txt numstat +7/-7, lineas CIFRA con valor cambiado: 1 (CIFRA salidas selladas del tallador)
```

No fui yo quien lo re sello: lo re sello la vuelta 156, y es exactamente el caso
que la 6.10 nombra. **Lo que cambia hoy es que ya no se puede citar en silencio.**

**EL LIMITE DE LA VARA, DECLARADO ANTES DE QUE NADIE LO DESCUBRA:** solo ve
lineas con el rotulo `CIFRA`. En ese mismo fichero el auditor nombro **dos**
cambios y esta guarda ve **uno**, porque el otro no lleva rotulo. **Lo que la
guarda garantiza no es ver todas las cifras movidas: es que un fichero que
cambio no pase en silencio**, porque el `numstat` cuenta el fichero entero.

## 8. TAREA 7, EL COSTE DE LAS NUEVE, Y SALE PEOR QUE UN COSTE

```
CIFRA fichas con al menos una cita que la bateria no cubre: 4
CIFRA salidas distintas sin respaldo en la bateria: 9
CIFRA ficheros .py barridos: 998
CIFRA salidas con productor identificado: 7 de 9
CIFRA de esas con productor identificado y corrido: 7
CIFRA de las corridas que TODAVIA MUERDEN (exit 0): 5
CIFRA de las corridas que ESCRIBEN en docs/loop/: 0
CIFRA segundos de UNA corrida de todas: 40.04 segundos
CIFRA segundos que anadirian al cierre de cada vuelta: 80.07 segundos
```

Las nueve cifras de arriba estan contadas en
`docs/loop/SALIDA_V157_T7_COSTE_P3B.txt`, que es la salida de esa tarea.

**TRES HALLAZGOS QUE LA VUELTA 156 NO PODIA VER PORQUE SOLO CONTABA:**

  1. **LA CORRESPONDENCIA SALIDA-SCRIPT NO ES MECANICA.**
     `SALIDA_V96_TAREA3_MUTACION.txt` NO la escribe `vuelta96_tarea3_mutacion.py`
     (no existe) sino `vuelta96_tarea3_prueba_mutacion.py`. Por eso aqui el
     productor **se busca por el texto que imprime cada salida**, barriendo 998
     `.py`. La regla de nombre de la 156 no solo sobre estima: **no sirve para
     encontrar al productor**.
  2. **DOS DE LAS NUEVE NO TIENEN PRODUCTOR IDENTIFICABLE:**
     `SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt` y `SALIDA_V136_3D_MUTACION.txt`.
     Y **las 7 identificadas son SEIS scripts distintos**, porque `V93` y `V94`
     comparten productor (`vuelta93_tarea3_guarda_direccion.py`).
  3. **DOS DE LAS SIETE NO MUERDEN HOY**, con su veredicto pegado:
     `vuelta96_tarea3_prueba_mutacion.py` exit 1, *ROJO, alguna guarda no se
     comporta*; y `vuelta97_tarea2_prueba_mutacion.py` exit 1, *10 de 12
     comprobaciones se comportan como deben*.

**NO METO NINGUNA EN LA BATERIA.** La cifra se publica y se trae, que es lo que
la 6.7 manda. Y la P3b de esas cuatro fichas queda declarada junto a la funcion
como **PROXY SIN RESPALDO EFECTIVO**, escrito en la TAREA 1.

## 9. TAREA 8, LAS DOS ESPECIES DE D

**Esta tarea mide: no reclasifica nada y no abre un fichero para escribir.**

`"el registro"` era ambiguo (el acta nombra puestos del CRIBADO, la discusion
nace en el REGISTRO DE CITAS) y **no lo adivine: medi los dos.**

```
A) REGISTRO DE CITAS DE OP-C-05
CIFRA filas en clase D: 96
CIFRA MADRE E HIJO    :     6  (6.2 por ciento)
CIFRA SANO Y DISTINTO :    20  (20.8 por ciento)
CIFRA AMBIGUA         :     1  (1.0 por ciento)
CIFRA SIN MARCA       :    69  (71.9 por ciento)

B) ARCHIVO DEL CRIBADO
CIFRA filas en clase D: 2760
CIFRA MADRE E HIJO    :    72  (2.6 por ciento)
CIFRA SANO Y DISTINTO :    21  (0.8 por ciento)
CIFRA AMBIGUA         :     2  (0.1 por ciento)
CIFRA SIN MARCA       :  2665  (96.6 por ciento)

C) CIFRA de los cinco puestos del acta que esta vara clasifica como MADRE E HIJO: 1 de 5
```

Las once cifras de arriba estan contadas en
`docs/loop/SALIDA_V157_T8_DOS_ESPECIES_D.txt`, que es la salida de esa tarea.

**LA CALIBRACION SE DELATA SOLA Y LA PUBLICO ASI.** De los cinco puestos que el
acta 157 nombra como madre e hijo (316, 478, 1424, 1494, 2066), esta vara lexica
solo clasifica **uno**, el **478**, y por la marca *casa propia*. Los otros cuatro
salen **SIN MARCA**. **La discrepancia se declara y no se arregla retocando las
marcas hasta que salga:** es el LIMITE 1 que el instrumento declara antes de
correr, y es la prueba de que **la cifra de MADRE E HIJO es una COTA INFERIOR y
no un total**. El acta lee; esta vara solo cuenta palabras. **El residuo se
publica en SIN MARCA en vez de repartirse.**

## 10. TAREA 9, EL CIERRE RECOMPUTADO AL CIERRE

**EL CICLO ENTERO Y EN SU ORDEN, NUNCA `run_phase1` SUELTO:**
`--reaplico-curaduria` (`docs/loop/SALIDA_V157_T9_GATE0.txt`),
`etiquetas_de_cara --aplicar` (`..._T9_ETIQ.txt`, **71 etiquetas**),
`sync_assets_web` (`..._T9_SYNC.txt`, **seis assets**) y despues el `numstat`.

```
CIFRA filas de numstat: 0 filas
```

La cifra de arriba esta contada en `docs/loop/SALIDA_V157_T9_NUMSTAT.txt`, que es
la salida de ese `git diff`.

**GATE 0, CON SU CONTEO HECHO SOBRE SU PROPIO FICHERO:**

```
CIFRA comprobaciones de Gate 0 que pasan: 26 comprobaciones
```

Pegado de `docs/loop/SALIDA_V157_T9_CONTEO_GATE0.txt`, corrido en esta vuelta.

```
CIFRA comprobaciones de Gate 0 que fallan: 0 comprobaciones
```

Pegado de `docs/loop/SALIDA_V157_T9_CONTEO_GATE0.txt`, corrido en esta vuelta.

```
```
CIFRA pares bidireccionales citados: 154 pares
```

Pegado de `docs/loop/SALIDA_V157_T9_CONTEO_GATE0.txt`, corrido en esta vuelta.

```
CIFRA pares bidireccionales huerfanos: 0 pares
```

Pegado de `docs/loop/SALIDA_V157_T9_CONTEO_GATE0.txt`, corrido en esta vuelta.

```
CIFRA pares excluidos por declarante deprecado: 3 pares
```

Pegado de `docs/loop/SALIDA_V157_T9_CONTEO_GATE0.txt`, corrido en esta vuelta.

```
CIFRA pares del universo ensanchado: 157 pares
```

Pegado de `docs/loop/SALIDA_V157_T9_CONTEO_GATE0.txt`, corrido en esta vuelta.

```
CIFRA veredicto de Gate 0: OK
```

Pegado de `docs/loop/SALIDA_V157_T9_CONTEO_GATE0.txt`, corrido en esta vuelta.

Ese fichero cuenta a su vez `docs/loop/SALIDA_V157_T9_GATE0.txt`, que es la
salida cruda del ciclo.

**LAS TRES SUITES:**

```
CIFRA motor: 25/25
```

Sale de `docs/loop/SALIDA_V157_T9_MOTOR.txt`, los 25 `engine/test_*.py` corridos
uno a uno.

```
 Test Files  80 passed (80)
      Tests  1030 passed | 3 skipped (1033)
```

Sale de `docs/loop/SALIDA_V157_T9_WEB.txt`, con vitest corrido DESDE `web/` y
exit 0.

```
CIFRA lineas de tsc: 0
```

Sale de `docs/loop/SALIDA_V157_T9_TSC.txt`, exit 0.

**EL ESTADO DEL ARCHIVO, RECOMPUTADO AL CIERRE:**

```
CIFRA n, filas del archivo: 3388
CIFRA marcador clase A: 551
CIFRA marcador clase B: 72
CIFRA marcador clase C: 5
CIFRA marcador clase D: 2760
CIFRA huecos: 0
CIFRA duplicados: 0
CIFRA nodos: 3853
CIFRA vivos: 3169
CIFRA deprecados: 684
CIFRA aristas nodos_siguientes: 8780
CIFRA aristas nodos_previos: 8740
CIFRA suma de las dos vistas: 17520
CIFRA union DIRIGIDA de las dos vistas: 9914
CIFRA solo_sig: 1174
CIFRA solo_prev: 1134
CIFRA lineas del registro de citas: 154
CIFRA via CRIBADO clase B: 1
CIFRA via CRIBADO clase D: 31
CIFRA via LECTURA_DIRIGIDA clase C: 57
CIFRA via LECTURA_DIRIGIDA clase D: 65
```

Las veintiuna cifras de arriba estan contadas en
`docs/loop/SALIDA_V157_T9_MARCADOR_CIERRE.txt`, que las cuenta de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, de `dataset/metadata/master_graph.json` y
de `docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl`.

**EL EXPEDIENTE, CON EL RELOJ PARADO EN LA APERTURA:**

```
CIFRA fichas del expediente: 71 operaciones
```

Pegado de `docs/loop/SALIDA_V157_T9_EXPEDIENTE.txt`, corrido en esta vuelta.

```
CIFRA fichas que no calzan: 36 operaciones
```

Pegado de `docs/loop/SALIDA_V157_T9_EXPEDIENTE.txt`, corrido en esta vuelta.

```
CIFRA fichas congeladas declaradas: 24 operaciones
```

Pegado de `docs/loop/SALIDA_V157_T9_EXPEDIENTE.txt`, corrido en esta vuelta.

```
CIFRA fichas congeladas en silencio: 12 operaciones
```

Pegado de `docs/loop/SALIDA_V157_T9_EXPEDIENTE.txt`, corrido en esta vuelta.

```
CIFRA fichas HECHA sin ninguna prueba: 0 operaciones
```

Pegado de `docs/loop/SALIDA_V157_T9_EXPEDIENTE.txt`, corrido en esta vuelta.

```
CIFRA fichas en LISTA sin ninguna prueba: 7 operaciones
```

Pegado de `docs/loop/SALIDA_V157_T9_EXPEDIENTE.txt`, corrido en esta vuelta.

Esa corrida va con `--corte abb2fe4e`, o sea con el reloj de git parado en la
apertura.

**EL ESTADO DE LAS FASES**, cada una con su `--fase` exacto y su fichero propio,
porque una salida mutilada no es una salida:

  - `03_FUSIONES`: **16 del catalogo, 12 cumplidas, 4 sin cumplir**, en
    `docs/loop/SALIDA_V157_T9_FASE_03_FUSIONES.txt`.
  - `06_MESAS`: **16 del catalogo, 16 cumplidas, 0 sin cumplir**, en
    `docs/loop/SALIDA_V157_T9_FASE_06_MESAS.txt`.
  - `08_VERIFICACION`: **1 del catalogo, 0 cumplidas, 1 sin cumplir**, en
    `docs/loop/SALIDA_V157_T9_FASE_08_VERIFICACION.txt`.
  - `09_LECTURAS_DIRIGIDAS`: **3 del catalogo, 0 cumplidas, 3 sin cumplir**, en
    `docs/loop/SALIDA_V157_T9_FASE_09_LECTURAS_DIRIGIDAS.txt`.

## LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

1. **LAS CUATRO QUE SOSTUVE EN C, Y LA MAS FLOJA ES LA `027`.** En `027` la
   segunda pata es delgada: `metodologia_spin_selling` expande *minimizar el
   cierre y enfocar en la indagacion* en solo dos pasos, y uno de ellos remite a
   *capitulos posteriores*. **Ademas su paso 1 y el paso 1 de cierre son casi la
   misma linea**, o sea que el par tambien tiene duplicacion. Si el auditor lee
   que eso lo mete en la comprobacion separadora del 9.22, **la 027 cae a D y no
   discuto**.
2. **LA `122`, POR SU PATA ANCHA.** Sostengo que el paso 6 de 6S (*Safety*) lo
   expande `error_proofing_servicio`, pero **practicas seguras abarca mas que a
   prueba de errores** (equipo de proteccion, ergonomia). Si el auditor lo lee
   como dos materias distintas, la segunda linea cae y con ella la C.
3. **MI CRITERIO DE QUE MENCIONAR NO ES EXPANDIR.** Es MIO, lo declare antes de
   aplicarlo y **es lo que decide 017, 030 y 056**, tres casos donde la ida es
   limpia y la vuelta es una mencion. Si el auditor sostiene que una linea que
   NOMBRA al otro nodo basta para contar la direccion, **esas tres vuelven a C** y
   mi lote pierde tres.
4. **LA CALIBRACION 1 DE 5 DE LA TAREA 8.** Mi vara lexica solo caza uno de los
   cinco puestos que el acta nombra. **Publico la cifra igual y la llamo cota
   inferior, pero es posible que una vara tan floja no sirva para decidir nada**,
   y en ese caso la cuenta que la 6.6 pedia sigue sin estar hecha de verdad.
5. **LA PARADA PODRIA NO SER PARADA.** Leo que dos guardas del cierre bloqueadas
   contradicen una regla vigente y por eso paro y no arreglo. **Si el auditor lee
   que esto es un simple desfase de indice que el ejecutor podia corregir sin
   tocar doctrina** (por ejemplo haciendo que las dos guardas busquen el acta mas
   reciente en vez de la N menos 1), entonces mi parada sobra y lo que falto fue
   trabajo.
6. **EL SELLO DE APERTURA TARDIO.** Lo declaro como caida mia en la seccion 0.
   Puede que el auditor lo lea como caida de reporte y no solo de procedimiento,
   porque una regla dice literalmente que la apertura se mide antes de la primera
   operacion y yo la medi pero no la selle.

## LAS PREGUNTAS

1. **EL SACO, QUE ES LA UNICA DEUDA DE LECTURA QUE QUEDA.** Contado al cierre de
   su propio fichero (`docs/loop/SALIDA_V157_T9_SACO_RESTANTE.txt`):

   ```
   CIFRA todavia en clase C: 57
   CIFRA de esas, LEIDAS en el lote 1 y sostenidas en C: 4
   CIFRA de esas, NO leidas todavia: 53
   CIFRA de las no leidas, CON puntero de paso: 0
   CIFRA nomina del lote 2 (todas las no leidas): 53
   ```

   **El lote 2 son 53, de `LD-OPC05-068` a `LD-OPC05-121`, y ninguna trae puntero
   de paso: el saco pequeno se agoto entero en el lote 1.** Confirmo que el
   criterio de la 6.4 se aplica igual en el segundo lote, o hay algo que el
   primero enseno y hay que cambiar?
2. **LAS DOS SALIDAS DE LA P3b SIN PRODUCTOR.** `SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt`
   y `SALIDA_V136_3D_MUTACION.txt` **no las escribe ningun `.py` del repo que yo
   pueda identificar por su texto**. Se busca su productor, se retira la cita de
   la ficha, o se declara que esas dos citas son artefactos huerfanos?
3. **LAS DOS QUE NO MUERDEN.** `vuelta96_tarea3_prueba_mutacion.py` y
   `vuelta97_tarea2_prueba_mutacion.py` salen **exit 1 hoy**. Sostienen la P3b de
   `OP-E-03`. **No las toco** porque el modo de cierre me lo prohibe y el encargo
   no lo pide. Se arreglan, se declaran como casos declarados, o se retira la P3b
   de esa ficha?

## PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Donde tuve que interpretar (que cuenta como direccion en la
6.4, que es "el registro" en la 6.6, donde vive el bloque de la 6.7) lo hice
**por extension de una regla escrita o midiendo las dos lecturas posibles**, y lo
marque como discutible en vez de inventar doctrina.

## EL MURO, Y NO SE PASA

Sigo el orden escrito en modo continuo y **paro donde el acta 149, 3.10 manda**:
la fase 08 no cierra sin una **sesion con credencial y con el fundador delante**,
medido hoy en `docs/loop/SALIDA_V157_T9_FASE_08_VERIFICACION.txt`, y la unica que
le queda sin cumplir es **`OP-V-01`, sin vara escrita**. **La unica deuda de LECTURA que le queda
al bucle es el saco, y son 57.** Cuando el lote 2 lo vacie no quedara trabajo que
un bucle pueda hacer solo. **El merge no se pide ni se hace: es del fundador y
solo suyo. La campana NO esta consumada.**
