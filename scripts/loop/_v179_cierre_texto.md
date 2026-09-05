## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**Todo hash de esta seccion sale de `git log` o `git rev-parse` corrido en esta
vuelta** (`EJECUTOR.md` 1, LA IDENTIDAD SE LEE DE GIT).

| | |
|---|---|
| rama | `pasada-unica` |
| sello de apertura, escrito ANTES de la 1.a operacion | `74cad47d` (`SALIDA_V179_HEAD_APERTURA.txt`) |
| sello de cierre, escrito TRAS la ultima operacion | `2037f785` (`SALIDA_V179_HEAD_CIERRE.txt`) |
| commits entre los dos sellos | **6** |
| rutas tocadas | **57** (`docs/loop/` 32, `scripts/loop/` 22, `docs/plan/` 3) |
| **el grafo entre los dos sellos** | **`git diff --numstat` sobre `dataset/`, `web/` y `engine/`: 0 filas** |

**LOS SEIS COMMITS, EN SU ORDEN:**

| hash | que cierra |
|---|---|
| `02af60ee` | el bloque de apertura, corrido entero antes de la primera operacion, con el desfase del calibrado DENTRO de el |
| `047b10b1` | el esqueleto del reporte, abierto al empezar con sus CINCO filas vacias |
| `d4a1028c` | la TAREA 1: la correccion declarada, la guarda de la escalada, la nomina y el corte del denominador |
| `8bd3bd3e` | la TAREA 2: los diez pares reales de `OP-L-03`, leidos |
| `09e0d2df` | las TAREAS 3 y 4: los triangulos partidos por su fuente y las del sujeto congelado juzgadas |
| `2037f785` | la TAREA 5: las cinco que no entran, nombradas y medidas |

**EL CICLO DE GATE 0 CORRIO ENTERO Y EN SU ORDEN EN LAS DOS PUNTAS**, nunca
`run_phase1` suelto: `run_phase1.py --reaplico-curaduria`, `etiquetas_de_cara.py
--aplicar`, `sync_assets_web.py`, `git diff HEAD --numstat`,
`engine/run_all_tests.py`, `npx tsc --noEmit` y `pnpm test`. **Las siete piezas
salieron verdes en las dos puntas**, y la tabla de la cabecera de arriba lo
publica columna a columna.

**LA GUARDA DE `dataset/` CORRIO ANTES DE CADA COMMIT** y salio **VERDE** en los
seis, con **0 filas de numstat y 0 blobs divergentes**. **`dataset/` no se toco en
ninguna de las cinco tareas.**

### 3.1 EL COTEJO DE MIS CLONES, PEGADO Y NO AFIRMADO

Desde la vuelta 178 **ningun reporte escribe CLON DECLARADO sin pegar la salida
del instrumento**. La mia vive en `docs/loop/SALIDA_V179_COTEJO_MIS_CLONES.txt` y
esto es lo que dice, contado de ese fichero:

| clon | fichero entero | solo la maquina | AST sin docstring | sentencias de codigo | literales de texto |
|---|---|---|---|---:|---:|
| `vuelta178_cierre.py` contra `vuelta179_cierre.py` | DIFIERE | **IDENTICO** | **IDENTICO** | 0 | 0 |
| `vuelta178_esqueleto_reporte.py` contra `vuelta179_esqueleto_reporte.py` | DIFIERE | DIFIERE | DIFIERE | **0** | **57** |
| `vuelta178_apertura.py` contra `vuelta179_apertura.py` | DIFIERE | DIFIERE | DIFIERE | **174** | **104** |

**LO QUE ESA TABLA DICE, Y NO LO SUAVIZO:** el clon del cierre es un clon de
verdad, con la maquina y el arbol de sintaxis identicos. El del esqueleto tambien:
**cero sentencias de codigo** y 57 literales de texto, que son las cinco filas de
tarea y la prosa. **El de la apertura NO es un clon en el sentido estrecho: cambia
174 sentencias de codigo**, porque su bloque H se reescribio entero para medir los
sujetos de ESTE encargo. **Eso estaba declarado en su docstring antes de correr el
cotejo**, y el cotejo lo confirma en vez de desmentirlo.

## 4. LA GUARDA DEL COMMIT, CORRIDA EN CADA COMMIT DE ESTA VUELTA

`scripts/loop/guarda_commit_dataset.py` corrio antes de cada uno de los seis
commits y salio **VERDE** en los seis: **0 filas de `git diff --numstat` sobre
`dataset/` y 0 ficheros con blob distinto del de HEAD**. El guardian del hook
(`motor` y `web`) tambien salio verde en los seis, y su salida esta en la consola
de cada commit.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**D.1. LA VENTANA DE 120 CARACTERES DE LA GUARDA NUEVA.** La elegi contando las
siete distancias reales de `REPORTE_V178.md` (32, 34, 36, 45, 51, 51 y 54) y
poniendo el doble largo de la mayor. **Es una vara que yo fije, no una que el
banco tenga escrita.** Una frase legitima mas larga que 120 caracteres entre su
cifra y su fichero se escaparia sin decir nada. **Prefiero que se escape a que
acuse en falso**, y esa preferencia tambien es mia y no del banco.

**D.2. EL EMPAREJAMIENTO POR CERCANIA.** Cada fichero se casa con la cifra que
tiene mas cerca en su parrafo, y cada cifra se gasta una sola vez. **Sobre el
sujeto real acierta las siete**, pero es una heuristica: un parrafo escrito al
reves la engana.

**D.3. EL `D` DEL PAR 4 DE `OP-L-03`** (`creacion_option_pool` contra
`employee_pool_esop`). El archivo da **dos senales contrarias** por dos terceros
distintos, y resuelvo a favor de la frontera del puesto 1193 declarando que el
otro tercero esta a caballo. **Es la unica de las diez lecturas donde tuve que
elegir entre dos cosas escritas**, y la elijo yo.

**D.4. EL `A` DEL PAR 10** (`evaluacion_` contra `explotacion_tecnologias_
disruptivas`). Los dos repiten con el mismo tercero, pero **el analisis IOTA de
`explotacion_` es lo mas cerca que hay en las diez de un procedimiento propio**.
Si el auditor lo lee como procedimiento, esto es `D`.

**D.5. EL METODO DE LA TAREA 4 NO SIGUE LA HUELLA A TRAVES DE FUNCIONES.** Un
arnes que salga `LO NOMBRA SIN ABRIRLO` y que llame a un tercero que si abre se
me escaparia. **Publico todas las lineas de cada arnes para que el ojo llegue
donde la maquina no**, pero la clasificacion mecanica tiene ese techo.

**D.6. LA TERCERA CASILLA QUE ME INVENTE EN LA TAREA 4**, `ABRE UN SUJETO YA
CLAVADO`, **no estaba en el encargo**, que pedia tres. La anadi porque sin ella
acusaba en falso a dos arneses que hacen exactamente lo que la regla pide.
**Anadir una casilla que el encargo no pide es una decision mia.**

## 6. LAS PREGUNTAS

**P.1. EL CABLEADO DE LA GUARDA DEL SUJETO CONGELADO.** Con los 17 veredictos
delante: cablearla hoy al rojo global pondria la bateria de la 181 en rojo por
**17**, de los cuales **13 no abren nada vivo**. Lo barato parece ser al reves,
que los 13 declaren su sujeto primero y despues se cablee con 4 pendientes de
verdad. **No lo decido yo.**

**P.2. LA ETIQUETA `(vuelta 177)` DE `clases_por_par()`.** Esta rota, esta medida
(5 lados mal de 15) y **el encargo prohibe tocar ese campo**. Queda como PARADA en
la seccion 3.f de la TAREA 3. **Hace falta que alguien autorice cambiarla para que
lea la vuelta del registro en vez del literal.**

**P.3. LA CONDICION `EL PAR TIENE PUESTO` NO PUEDE DAR QUE SI.** Medida en la
TAREA 2: un par real esta definido como el que no esta en el archivo, asi que
nunca trae puesto. **La distincion del punto 7.8 del acta 178 es correcta y su
rama del `SI` es inalcanzable mientras el archivo no tenga huecos.** Vale la pena
saber si eso es lo que se queria.

**P.4. EL ARCHIVO SE CONTRADICE CONSIGO MISMO EN LA FAMILIA DEL OPTION POOL.**
`pool_opciones_empleados` sale `A` con los dos lados de una frontera que el propio
archivo declaro. **No lo toco** (modo de cierre), pero queda nombrado.

## 7. PENDIENTES DE DOCTRINA

**PD.1. NO HAY REGLA ESCRITA PARA LA CADENA DE REPITE.** Use la transitividad
(`a` REPITE con `t` y `b` REPITE con `t`, luego `a` REPITE con `b`) en cinco de
las diez lecturas, apoyandome en `banco 9.3`, que dice que una direccion de fusion
no sobrevive a su familia. **Pero `9.3` dice que hay que MIRAR la familia, no que
la transitividad decida.** Registro lo mejor sostenido y lo marco.

**PD.2. NO HAY REGLA PARA EL SUJETO CLAVADO POR SHA.** `HUELLAS_DE_CONGELADO` ya
incluye `git show` y `cat-file`, pero la guarda los mira **en el texto entero** y
no **en la llamada**, y por eso los dos de la 135 salen `NO DECIDIBLE`. La casilla
que invente en la TAREA 4 no existe en ninguna doctrina escrita.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**C.1. LA GUARDA DE LA ESCALADA INVENTABA UN ROJO EN SU PRIMERA CORRIDA.** Sobre
`REPORTE_V178.md` cazaba **dos** y solo una era real: acusaba a la linea 189, donde
la cifra que va con el fichero es la **8** y mi patron solo veia la palabra
`casos`, que ahi acompana a la **5**. **La cazo su propia corrida contra el sujeto
real, no un arnes.** Arreglada antes de seguir.

**C.2. DOS ESPERADOS MIOS MAL PUESTOS EN EL ARNES DE LOS TRIANGULOS.** Esperaba 6
y 6 lados por fuente sobre el registro fabricado y son **7 y 5**. **El codigo
estaba bien y mis dos numeros estaban mal**, y la prueba de mutacion los cazo
porque el esperado equivocado coincidia con el valor mutado.

**C.3. UNA COMPROBACION MUERTA QUE PARECIA VIVA.** El patron del sujeto clavado
de la TAREA 4 se escribio con dos `\b` que quedaron guardados como **caracteres de
retroceso**, y **no podia dar verdadero nunca**. Lo destape al preguntarme por que
salian cero clavados teniendo el `sha` delante en la propia linea de la prueba.
**Es exactamente la especie que el banco 9 llama degradacion silenciosa.**

**C.4. LA AGUJA DE LA TAREA 5 ESTABA EN MAYUSCULAS.** El instrumento salio en ROJO
nombrandola. **Eso no es una caida del instrumento sino de mi aguja**, y lo cuento
aqui porque la primera version del fichero prometia cinco medidas y solo podia dar
cuatro.

**C.5. MI PRIMER CRITERIO DE `TIENE PUESTO` MEDIA OTRA COSA.** Preguntaba si algun
EXTREMO aparece en algun puesto, no si el PAR lo tiene, y con esa vara los diez
salian `SI` cuando la respuesta es `NO`. **Habria mandado los diez veredictos al
fichero equivocado.**

**C.6. LA GUARDA NUEVA CAZO ESTE MISMO REPORTE AL CERRARLO, Y NO ERA UN FALSO
ROJO NI ERA CORRECTO DEJARLO.** La tabla de la TAREA 1.a publica **16** al lado
de `SALIDA_V178_T1E_MUTACION.txt`, porque `EJECUTOR.md` 8 obliga a declarar la
correccion **sin borrar el texto viejo**. La guarda acusaba al reporte por hacer
lo que la doctrina manda. **Se le anadio su unica exencion**, que hay que pedir
por escrito diciendo el literal **CORRECCION DECLARADA** en el parrafo, con sus
cuatro casos nuevos por mutacion, incluido el que comprueba que **sin esas
palabras vuelve a ser rojo**. **La cazo la propia guarda contra su propio
reporte, no un arnes**, que es la segunda vez en esta vuelta que eso pasa.

**C.7. LA QUE VIENE DE LA VUELTA PASADA Y ES LA QUE ABRE ESTE REPORTE:** la 178
publico **16** donde su fichero decia **18**. Corregida en la TAREA 1.a con las
tres cifras al lado y sin retocar el reporte archivado.
