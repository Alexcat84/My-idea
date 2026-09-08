### TAREA 1. LOS REGISTROS DE LA VUELTA 207: `R.72`, LAS OCHO ADJUDICACIONES Y LA CORRECCION DECLARADA DE LA `4.1`

**LO QUE DEJO SELLADO, CON LAS DOS CONVENCIONES EN EL MISMO RENGLON:**

| salida sellada | bytes | exitcode |
|---|---|---:|
| `docs/loop/SALIDA_V208_SERIE_APERTURA.txt` | 9113 bytes en disco y 9025 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_SERIE_CIERRE.txt` | 9252 bytes en disco y 9163 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1_REGISTROS_SECO.txt` | 14269 bytes en disco y 14269 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1_REGISTROS.txt` | 14328 bytes en disco y 14328 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1_REGISTROS_IDEM.txt` | 14279 bytes en disco y 14279 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1D_CORRECCION_SECO.txt` | 3269 bytes en disco y 3269 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1D_CORRECCION.txt` | 3303 bytes en disco y 3303 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1D_CORRECCION_IDEM.txt` | 3287 bytes en disco y 3287 normalizado a LF | 0 |

#### 1.a. EL ACTA 207, LEIDA ENTERA Y CON SUS CIFRAS REMEDIDAS POR MI

**LAS CIFRAS DEL ENCARGO SON CONTRASTE Y LAS REMEDI. LAS SEIS CALZAN AL DIGITO.**

| cifra | el encargo, como contraste | mi medicion de hoy | calza |
|---|---:|---:|---|
| bytes del acta ANTES | 4793964 | 4793964 | SI |
| bytes del acta DESPUES, en disco | 4820516 | 4820516 | SI |
| bytes del acta DESPUES, normalizado a LF | 4820516 | 4820516 | SI |
| bytes anadidos | 26552 | 26552 | SI |
| lineas del fichero | 73081 | 73081 | SI |
| linea donde empieza la seccion del auditor | 72641 | 72641 | SI |

**Y LOS DOS `sha256` TAMBIEN**, leidos de mi sello de apertura:
sha256 disco **`0ca61c2ee053dd0d`** y sha256 LF **`0ca61c2ee053dd0d`**, los mismos
dos que el encargo publica.

**EL AVISO MEDIDO DEL ENCARGO LO COMPROBE ANTES DE RESTAR, NO DESPUES.** El
encargo avisa que el acento circunflejo se lo come el shell. Lo mire: en el mio
`git rev-parse 0d9e71a3~1` y `git rev-parse '0d9e71a3^'` devuelven **el mismo**
`bdfbe52555299a6740e8b44d2b2ed7805aeaf2c9`, que **NO** es el hijo
`0d9e71a3f6a540860452afbb4bfc1552f32f11f9`. **Los dos valores son distintos, que
es la condicion que el encargo pide comprobar**, y aun asi la resta la hice con
`~1`.

**LA ADICION PURA NO LA AFIRMO: LA MIDE `git`.**
`git show --numstat 0d9e71a3 -- docs/loop/ACTA_AUDITOR.md` da **442** lineas
anadidas y **0** borradas. El acta 207 abre en la linea **72641** de un fichero de
**73081** lineas, o sea **441** lineas de cuerpo; **la 442.a es la linea en blanco
de la 72640**, que es el separador, y lo digo en vez de dejar la resta coja.

#### 1.b. `R.72`, ESCRITA POR ADICION PURA Y CON EL NUMERO COMPUTADO

**EL NUMERO NO SE TECLEO.** `scripts/loop/serie_de_registros.py` corrido por mi al
entrar y al salir, recomputando la serie de sus DOS sedes:

| punta | entradas | en `PENDIENTES.md` | en `CORRECCIONES_A_APLICAR.md` | colisiones | huecos | mayor | siguiente libre |
|---|---:|---:|---:|---:|---:|---|---|
| AL ENTRAR (`SALIDA_V208_SERIE_APERTURA.txt`) | 63 | 62 | 1 | 0 | 0 | `R.71` | `R.72` |
| AL SALIR (`SALIDA_V208_SERIE_CIERRE.txt`) | 64 | 63 | 1 | 0 | 0 | `R.72` | `R.73` |

**LA PUNTA DE ENTRADA CALZA AL DIGITO CON EL CONTRASTE DEL ENCARGO** (63, 62, 1,
0 colisiones, 0 huecos, mayor `R.71`, siguiente libre `R.72`).

**LA ADICION ES PURA, Y LO MIDE `git`, NO YO:**
`git diff --numstat -- docs/PENDIENTES.md` da **140** lineas anadidas y **0
BORRADAS**. La sede pasa de **1171455** bytes en disco y **1171455** normalizado a
LF a **1180091** y **1180091**, o sea **8636** anadidos, y de **17040** a **17180**
lineas.

**Y LA GUARDA DEL TEXTO VIEJO SE CORRIO ENTERA:** las lineas del texto de ENTRADA
que NO estan, en orden, en el de SALIDA son **0**.

**LA SEGUNDA CORRIDA CRECE 0 BYTES, COMO EL ENCARGO PIDE.**
`SALIDA_V208_T1_REGISTROS_IDEM.txt` publica `NO SE ESCRIBE: la entrada ya estaba.
IDEMPOTENTE.` y la sede crece **0** bytes en disco y **0** bytes normalizado a LF,
leido de sus dos lineas `CIFRA crecimiento`. El `numstat` sigue en **140 / 0**
despues de la segunda corrida.

#### 1.c. LAS OCHO ADJUDICACIONES, POR SU NUMERO Y CON SU LINEA

**LA VARA DEL `4.1` DEL ACTA 202 LA CORRI YO, CON EL LECTOR IMPORTADO Y SIN
TOCARLE UNA LINEA, Y DA LO MISMO QUE EL ACTA PUBLICA.**

| acta | numerales COMPUTABLES de 4, medidos por mi | el acta 207 en su `7.1`, como contraste | calza |
|---|---:|---:|---|
| **206** | **1** | 1 | SI |
| **207** | **4** | 4 | SI |

**Sobre la 207 la vara saca las cuatro:** adjudicaciones **8**, hallazgos **5**,
caidas del auditor **4** y caidas del ejecutor **1**. **Sobre la 206 saca una
sola:** hallazgos **4**; adjudicaciones y caidas del ejecutor dan seccion hallada
con **0 claves**, y caidas del auditor no tiene seccion que la titule.
**Ninguna discrepancia con el contraste, asi que esto no sube a la `3.0`.**

**LAS OCHO, CON SU LINEA MEDIDA Y CON LO QUE CIERRAN:**

| clave | linea | cierra pendiente | que es |
|---|---:|---|---|
| `6.1` | 72858 | **`P.2`** | una evidencia que no lleva la cobertura al lado no cubre una mesa |
| `6.2` | 72879 | (ninguno) | `OP-L-01` no se cierra, y eso no es una parada |
| `6.3` | 72886 | **`P.3`** | las dos filas las escribe la vuelta 208, con el denominador recomputado primero |
| `6.4` | 72894 | **`PD.1`** | un punto de una vara sellada que aparece del otro lado se corrige por adicion declarada |
| `6.5` | 72906 | **el TOPE de sub-tareas** | vuelve a cinco: el disparador se cumplio |
| `6.6` | 72916 | (ninguno) | la moratoria se respeto, 11 de 11 con prefijo y nomina en 135 |
| `6.7` | 72921 | (ninguno) | la bateria no corre en la 208 |
| `6.8` | 72925 | **`P.1`** | el `3.0.a` no rompe la moratoria y el remedio es como titula el auditor |

**LAS CINCO QUE CIERRAN PENDIENTES QUEDAN DICHAS AL REGISTRARLAS**, dentro de
`R.72`, y el computo cae en rojo si alguna de las cinco no aparece entre las
medidas: `CIFRA de las cinco que cierran pendientes que NO estan entre las
medidas: 0`.

**UN CERO FALSO CAZADO ANTES DE PUBLICARLO, Y ESTE ES MIO.** `REG206.titulo_de()`
cuenta las caidas con `numeral(dato, 'viejas')`, o sea por la forma antigua
`CAIDA n`, y **el acta 207 escribe las suyas como `9.1` a `9.4` y `4.1`**. Corrido
tal cual, el titulo de `R.72` habria dicho **las 0 caidas propias del auditor**
sobre un acta que trae **cuatro**. Lo cace corriendolo, y **no toque el lector**:
le pase a la misma funcion importada el dato contado por la forma que esa acta usa.
**Las dos cuentas van juntas dentro de `R.72` y el titulo crudo queda escrito ahi
entero y sin tachar.** Va como `D.1`.

#### 1.d. LA CAIDA `4.1` DEL AUDITOR CONTRA MI, CORREGIDA POR CORRECCION DECLARADA

**EL AUDITOR TIENE RAZON Y NO LO CORRIJO COPIANDOLE** (`EJECUTOR.md` 2). Las dos
mediciones son mias y las dos dan **7**:

| via | cifra |
|---|---:|
| remedida por mi sobre la linea **41** de `docs/plan/OPERACIONES.jsonl` | **7** |
| leida de la **linea 21** de mi propia salida sellada `docs/loop/SALIDA_V207_T2_VARA.txt` | **7** |
| lo que el reporte de la 207 publicaba | 6 |

Esa linea 21, pegada entera y no parafraseada:
``   CIFRA elementos de `verificacion`: 7``.
**El instrumento midio bien; la transcripcion al reporte perdio uno.**

**LA COBERTURA NO CAMBIA, Y NO LO AFIRMO: LO COMPRUEBA EL COMPUTO.** De los
**7** elementos, **3** son clausulas (indices **0**, **1** y **2**) y **4** son
CORRECCIONES DECLARADAS (indices **3**, **4**, **5** y **6**). `V.12`, `V.13` y
`V.14` salen de `verificacion[0]`, `[1]` y `[2]`, que son justamente las tres
clausulas; **los cuatro que faltaban de contar son las CORRECCIONES DECLARADAS,
que nunca fueron puntos de la vara**. `CIFRA puntos de la vara que se mueven por
esta correccion: 0`. Si el reparto no hubiera sido ese, el computo caia en rojo y
no escribia nada.

**LA CORRECCION ES POR ADICION Y CON EL TEXTO VIEJO ENTERO ENCIMA.** El bloque se
inserta **debajo** del parrafo que falla, en `docs/loop/reportes/REPORTE_V207.md`,
que pasa de **50306** bytes en disco y **50306** normalizado a LF (sha256
`e0d67989e21687ce` por las dos) a **51699** y **51699** (sha256 `231b2df5d3414bf1`
por las dos). `git diff --numstat` da **26** anadidas y **0 BORRADAS**, y las
lineas del texto de entrada que faltan del de salida son **0**.
**Segunda corrida IDEMPOTENTE: 0 bytes de crecimiento.**

**Y LA FICHA SOLO SE LEYO:** `docs/plan/OPERACIONES.jsonl` entra y sale de esta
sub-tarea en **513043** bytes por las dos convenciones, con sha256
`829c583eb779cab6` por disco y `829c583eb779cab6` por LF.
