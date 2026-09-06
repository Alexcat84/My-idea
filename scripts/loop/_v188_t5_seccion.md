### TAREA 5. LA RELECTURA AL DOBLE, LOS DOS REMEDIOS PEQUENOS Y EL CIERRE. CERRADA

#### 5.a LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 188

**POR QUE:** `AUDITOR.md` 1.2. La discrepancia del auditor (**el puesto 1202**)
cayo **FUERA del discutible de clase marcado**: el reporte de la 187 marco el
**2464**. **Fue una sola y estaba en sus propios dudosos, y el credito baja igual
porque la letra no distingue.** Salida:
`docs/loop/SALIDA_V188_T5A_RELECTURA_AL_DOBLE.txt`, exitcode **0**.

**EL COTEJO DEL `sha256` FUE ANTES DE LEER UN SOLO PUESTO, COMPUTADO Y NO
COPIADO:**

| | el sello `V189` dice | medido hoy | |
|---|---|---|:-:|
| bytes de la ciega | **41098** | **41098** | **CALZA** |
| `sha256`, normalizado a LF, de la ciega | `4dbbedc0ac89951e979866454b5d7be4b9406c65ba47c664fdf89b51b098df3c` | el mismo | **CALZA** |
| bytes del destape | **34030** | **34030** | **CALZA** |
| `sha256`, normalizado a LF, del destape | `9267fbf46cbad22f1782d9813cea0ff426ed6da4838f2d7532ae588b566410e5` | el mismo | **CALZA** |

**Los dos calzan, y solo entonces se leyo.**

**EL TRAMO Y SU DOBLE.** `docs/loop/_auditor_v189_ciega_blind.txt` trae **30
puestos distintos**. `vecinos()` se **importa** de
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, **no se copia**. El
archivo trae **3388 filas**, maximo puesto **3388**, y el grafo **3853 nodos**.
`docs/loop/_auditor_v189_exclusion.txt` mide
**1648 bytes en disco y 1648 bytes normalizados a LF** y lista **351 puestos
distintos**, que es lo que el encargo dice.
**60 puestos releidos en total, que es el doble exacto.**

**EL REMEDIO DEL `D.2`, ADJUDICADO A FAVOR Y AUN ASI ARREGLADO, Y SU CONTRASTE.**
El acta 188 contesta mi `P.3`: **el solape se le exige AL UNIVERSO**, porque la
exclusion existe para que nadie relea lo ya leido y los 60 se leen todos. Va
**por parametro y de forma aditiva**: `vecinos()` recibe un conjunto `evitar`
opcional. **Y aqui esta la cifra que prueba que hacia falta:**

- **SIN `evitar`** (la conducta de la 187): 30 vecinos, y su **solape con la
  exclusion es 30**.
- **CON `evitar`**: 30 vecinos, y **el cero sale por construccion**.

**LOS TRES SOLAPES DEL UNIVERSO, QUE ES LO QUE EL ACTA EXIGE:**

- **el UNIVERSO contra el TRAMO: 0**
- **el UNIVERSO contra `docs/loop/_auditor_v188_ciega_blind.txt`: 0**
- **el UNIVERSO contra la EXCLUSION de 351 puestos: 0**
- **`CIFRA solapes que NO dan 0: 0`.**

**LAS CIFRAS DE LA RELECTURA MECANICA, Y NINGUNA CLASE SE VOLVIO A DECIDIR:**
**60 releidos**, **4 declaran diferenciador**, **0 con LESION EXACTA**, **0 con
algun nodo muerto**. Reparto por clase contado del archivo: **A 12, D 48**.

**LA CIFRA QUE EL ACTA PIDE APARTE, Y QUE SOLO SE CUENTA.** De los 60 releidos,
**6 tienen en su razon evidencia DE FAMILIA y no del par** (una `NOTA DE NOMINA`,
un racimo, un cumulo o unos hermanos): los puestos **415, 670, 1202, 1792, 2783 y
3148**. **Repartidos: 5 de los 30 del TRAMO y 1 de los 30 vecinos.** **Solo se
cuenta y se publica: no se interpreta y no se adjudica**, y si resulta que la
salida ciega no lleva la carta que decide una parte de los pares, **eso es un
hallazgo del fundador y no mio**.

**EL PUESTO 1202, MIRADO CON LA MISMA VARA Y PUBLICADO APARTE.** Esta **dentro**
del universo releido y **dentro del tramo** de la ciega.
`diferencias_venta_pequena_venta_grande` contra
`riesgo_tecnicas_cierre_venta_compleja`, dominio `core`, clase que **el archivo
dice hoy: `A`**. **La vara ve: declara diferenciador `no`, LESION EXACTA `no`,
los dos nodos vivos `SI`, cobertura `0.00`**, y su motivo es *"la razon no declara
ningun diferenciador"*. **Su razon SI lleva evidencia de familia**, y es la
`NOTA DE NOMINA` que el acta nombra: cita el banco `9.20` y `9.10` y dice que
`riesgo_tecnicas_cierre_venta_compleja` **es el centro del racimo del cierre en
venta grande y llevaba CUATRO `A` contra hermanos**, los puestos **274, 321, 432 y
1004**. **Lo que la vara no ve, no lo afirmo: la vara no ve aqui nada que decida
la clase, y ninguna clase se ha movido.**

**ARNES DEL PARAMETRO, Y NACE EN ESTA VUELTA:**
`scripts/loop/vuelta188_tarea5a_mutacion_vecinos_evitar.py`. Salida:
`docs/loop/SALIDA_V188_T5A_MUTACION_VECINOS_EVITAR.txt`, **`CIFRA casos: 20 |
pasan: 20`**, **`CIFRA casos que CAEN al mutar su esperado: 20 de 20`**, **`CIFRA
fallos: 0`**, **`VEREDICTO: VERDE`**, exitcode **0**. Su caso (A) es el que el
encargo pide con nombre: el arnes lleva dentro **una copia CONGELADA de la version
anterior al parametro**, declarada como tal, y exige que las dos den la **misma**
salida sobre **siete** tramos, incluidos los bordes (pegado al techo, pegado al
suelo, uno solo, denso, archivo diminuto y vacio). **Sin `evitar` la conducta es
la de antes, y eso no se afirma: se coteja.**

#### 5.b LOS PUESTOS DEL DISCUTIBLE DE CLASE, PARA QUE EL AUDITOR PUEDA LEERLOS A CIEGAS

**`docs/loop/DISCUTIBLES_DE_CLASE_V188.txt` esta escrito**, mide
**10 bytes en disco y 10 bytes normalizados a LF**, su `sha256` normalizado a
LF es `7f3c48b9b2a06c3c`, y **dentro dice
`(ninguno)` y nada mas**: sin la clase, sin la razon, sin el nombre de los nodos y
sin una palabra de contexto.

**Y EL `(ninguno)` ES UNA MEDICION Y NO UN HUECO: esta vuelta NO MARCA NINGUN
DISCUTIBLE DE CLASE, porque no ha decidido ninguna clase y no ha movido ningun
veredicto.** Mis seis discutibles son **todos de metodo** y van marcados en la
seccion 7 de este reporte.

#### 5.c EL ESQUELETO SE TALLO EN LA APERTURA. ES LA `C.1`, Y ESTA DESCARGADA

**LOS TRES COMMITS, EN SU ORDEN Y LEIDOS DE GIT:**

| que es | commit | que deja en el arbol |
|---|---|---|
| apertura | `2b309654` | el sello entero, con el ciclo de Gate 0 dentro |
| **esqueleto, en SU PROPIO COMMIT** | `b24ae22e` | **el reporte de la 188 con sus cinco filas ABIERTA, SIN CERRAR** |
| tarea 1 | `31f716b5` | la `R.50` y la primera fila anexada |

**Desde el segundo commit ya hay reporte parcial en el arbol**, que es exactamente
lo que `EJECUTOR.md` 1 protege. **El remedio costo un commit**, tal como el acta
188 lo midio contra la vuelta 186.

**Y AQUI VA UNA HONESTIDAD PEQUENA SOBRE UNA RUTA.**
`docs/loop/SALIDA_V188_ESQUELETO.txt` guarda **la SEGUNDA corrida** del esqueleto,
no la que escribio: la segunda salio en **ROJO** y no escribio nada, porque la
guarda del `PASO 0.c` hizo su trabajo (en el arbol ya estaba el reporte de la 188,
que aun no tiene commit ni archivo). **Es la idempotencia funcionando.** El
fichero lo declara en su primera linea, porque **una ruta publicada como evidencia
de una corrida es CIFRA** y decir que es la corrida que escribio seria falso.

#### 5.d LA NOMINA Y LA DOBLE CORRIDA CON EXCLUSION POR ROJO

`scripts/loop/vuelta188_tarea3c_nomina.py`, salida
`docs/loop/SALIDA_V188_T3C_NOMINA.txt`:

- **`CIFRA censo: 185 | CIFRA nomina AHORA: 125 | VARA_DEL_CENSO: 148`**. La
  nomina **abrio la vuelta en 121** y cierra en **125**: **crece, no se poda**.
- **`arneses_que_faltan(): ultima vuelta 188, FALTAN 0`.**
- **`nomina_invisible_al_censo(): 0`.**
- **`CIFRA de esos que estan dentro: 6 de 6`.**
- **`CIFRA arneses registrados como ROJOS de esta vuelta: 0`** y **`CIFRA arneses
  EXCLUIDOS de la doble corrida: 0`**, con la exclusion vacia **declarada con esas
  palabras** en vez de callada.
- **`CIFRA paradas: 0`**: los **seis** dan **el mismo `sha256` en las dos
  corridas**.
- **`CIFRA filas de git diff --numstat -- dataset/` despues de la doble corrida:
  0`.**

**Y LA CORRIDA SALE `VEREDICTO: ROJO` POR UNA SOLA COSA, QUE SE DECLARA ENTERA EN
VEZ DE ESCONDERSE:** **`guarda_del_sujeto_congelado(): 3 entradas sin
congelar`**, y son `vuelta186_tarea2c_mutacion_cierre_tardio.py`,
`vuelta187_tarea4_mutacion_dos_convenciones.py` y
`vuelta188_tarea4_mutacion_cobertura_parejas.py`, las tres `NO DECIDIBLE` por
nombrar `REPORTE.md`. **Dos de las tres son heredadas y no son nuevas: el reporte
de la 187 cerro con esas mismas dos y su corrida tambien salio `ROJO` por eso**
(`docs/loop/SALIDA_V187_T5A_NOMINA.txt` linea 87). **La tercera es mia y es
deliberada:** el caso decisivo de la escalada **tiene** que medir contra el disco
vivo, porque esa es la fuente que la guarda usa en produccion. **No se le pone la
marca `SUJETO CONGELADO` porque seria falsa**, y una declaracion falsa para
apagar una guarda es peor que la guarda encendida.

**LA QUE SI SE ARREGLO, PORQUE ERA ARREGLABLE:**
`vuelta188_tarea2_mutacion_pata_documental.py` **ahora si declara `SUJETO
CONGELADO`, y es cierto**: sus llamadas a disco van todas contra un temporal
propio que se limpia, y los nombres de ficheros vivos aparecen solo como texto
dentro de fichas fabricadas.

**Y UNA PARADA DE VERDAD QUE ESTA VUELTA ENCONTRO EN SU PROPIO ARNES, CON SU
CORRIDA EN ROJO PEGADA.** La primera doble corrida saco **`CIFRA paradas: 1`**:
`vuelta188_tarea2_mutacion_pata_documental.py` **cambiaba sola** entre dos
corridas del mismo dia sobre el mismo sujeto: su `sha256` normalizado a LF fue
`6e056e2b9d049861` y luego `edd65316f5312cd4`. **Eso es PARADA por la respuesta del acta 188 a la
`P.2`.** La causa, medida: **imprimia el nombre del directorio temporal**, que
`mkdtemp` fabrica distinto cada vez. **Es la misma enfermedad que tumbo a
`vuelta182_tarea2_mutacion_apertura_auditor.py` en la vuelta 184.** Como es **un
arnes que nace en esta vuelta y no habia sellado ninguna salida**, por la
adjudicacion `5.2` del acta 186 su rojo es parte de escribirlo: **se reparo, el
motivo quedo escrito dentro del propio fichero, y las dos corridas en rojo se
conservan enteras** en
`docs/loop/SALIDA_V188_T3C_NOMINA_EN_ROJO.txt` y
`docs/loop/SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL_EN_ROJO_CAMBIA_SOLA.txt`. Tras
la reparacion, las dos corridas dan `ae804ea4e2894cce` **las dos**.

**Y LOS DOS DE LA 186 SE MOVIERON, CON CAUSA CONOCIDA Y AHORA VISIBLE.**
`SALIDA_V186_T2A_MUTACION_PIEZA4.txt` y
`SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt` mueven **4 lineas cada una** contra
su version anterior, y **las cuatro son el sello del sujeto**: esta vuelta cambio
`scripts/loop/cerrar_reporte.py`. **Es exactamente el caso que la `3.b` vino a
hacer legible**, y ahora la propia salida lo dice en vez de dejarlo a que alguien
lo deduzca.

#### 5.e LOS CLONES DECLARADOS DE ESTA VUELTA, COTEJADOS

`docs/loop/SALIDA_V188_COTEJO_DE_CLONES.txt`. **No se afirma que ningun diff salga
vacio: se publica lo que salio.**

- `vuelta187_esqueleto_reporte.py` -> `vuelta188_esqueleto_reporte.py`:
  **exitcode 0**. `CIFRA lineas de maquina que difieren: 83`, `CIFRA SENTENCIAS DE
  CODIGO: 0`, `CIFRA LITERALES DE TEXTO: 83`, `CIFRA tipos de nodo que NO empatan:
  0`. **Es lo que un clon declarado promete: cambia el texto, no el codigo.**
- `vuelta187_tarea5a_nomina.py` -> `vuelta188_tarea3c_nomina.py`: **exitcode 0**.
  `CIFRA lineas de maquina que difieren: 141`, `CIFRA SENTENCIAS DE CODIGO: 94`,
  `CIFRA LITERALES DE TEXTO: 47`, `CIFRA tipos de nodo que NO empatan: 34`. **Y
  esas 94 sentencias nuevas se declaran y no se disimulan: son la exclusion por
  rojo de la `C.3`**, que es codigo que el original no tenia. **Un clon que anade
  una funcion nueva no es un clon identico, y decirlo es la mitad del cotejo.**
