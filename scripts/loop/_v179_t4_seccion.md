### TAREA 4. LAS DEL SUJETO CONGELADO, JUZGADAS UNA A UNA, Y NADA CABLEADO

#### 4.a. NO SON QUINCE AL CERRAR, Y LA CULPA ES MIA, Y ESTA MEDIDA

El encargo habla de **quince** (7 `SUJETO VIVO` y 8 `NO DECIDIBLE`), y **quince
eran al abrir**: el bloque H.10 de `scripts/loop/vuelta179_apertura.py` lo midio
antes de la primera operacion y dio **15 de 98**. **Al juzgarlas son 17 de 103**,
y el motivo es la TAREA 1.c de esta misma vuelta, que metio cinco arneses en la
nomina: dos de ellos salen senalados
(`vuelta150_2d_simular_op_c_05.py` y `vuelta179_tarea3_mutacion_triangulos.py`).

**LAS DOS CIFRAS SON VERDADERAS Y CADA UNA LLEVA SU CORTE**, que es exactamente
para lo que la TAREA 1.d cableo el sello: **15 de 98 al corte de apertura,
`74cad47d42e7`**, y **17 de 103 al corte de la corrida de esta tarea,
`8bd3bd3e8864`**. Sin el corte, las dos cifras se contradirian sin manera de
saber cual mira que.

#### 4.b. COMO SE JUZGO, Y ES MECANICO Y NO A OJO

`scripts/loop/vuelta179_tarea4_juzgar_sujeto.py` parsea cada arnes con `ast`,
busca las llamadas que **leen de disco** y mira si dentro aparece la huella de un
fichero vivo, **resolviendo tambien las asignaciones simples** (si el arnes hace
`RUTA = os.path.join(...)` y despues `io.open(RUTA)`, eso cuenta como abrir).

**Y HAY UNA TERCERA CASILLA QUE NO ESTABA EN EL ENCARGO Y QUE HUBO QUE ANADIR
PORQUE MI PRIMERA VERSION ACUSABA EN FALSO.** Leer `git show
<sha de 40>:docs/loop/REPORTE.md` **no es leer el `REPORTE.md` vivo**: es leer un
blob clavado por su huella, que no se mueve nunca mas. Mi primera corrida
clasificaba `vuelta135_2e_mutacion_1.py` y `_2.py` como **ABRE FICHERO VIVO**
teniendo el `sha` delante en la propia linea de la prueba. **Se arreglo antes de
escribir el registro**, y de paso destapo un defecto propio: el patron se habia
escrito con dos `\b` que quedaron guardados como caracteres de retroceso y **la
comprobacion no podia dar verdadero nunca**. Estaba muerta y parecia viva.

**LO QUE ESTE METODO NO PUEDE, Y SE DICE EN VEZ DE PRESUMIR:** no sigue la huella
a traves de funciones auxiliares ni de modulos importados. Por eso cada fila del
registro publica **todas las lineas** donde la huella aparece, abra o no, para
que el ojo pueda mirar donde la maquina no llega. **Marcado DISCUTIBLE.**

#### 4.c. LOS DIECISIETE, REPARTIDOS

| veredicto de la lectura | arneses |
|---|---:|
| `ABRE FICHERO VIVO` | **4** |
| `ABRE UN SUJETO YA CLAVADO` | **2** |
| `LO NOMBRA SIN ABRIRLO` | **11** |
| **total** | **17** |

**Y EL CRUCE CONTRA LO QUE LA GUARDA DICE, QUE ES LO QUE MIDE SI LA GUARDA
ACIERTA:**

| la guarda dice | la lectura dice | arneses |
|---|---|---:|
| `NO DECIDIBLE` | `ABRE FICHERO VIVO` | **3** |
| `NO DECIDIBLE` | `ABRE UN SUJETO YA CLAVADO` | **2** |
| `NO DECIDIBLE` | `LO NOMBRA SIN ABRIRLO` | **4** |
| `SUJETO VIVO` | `ABRE FICHERO VIVO` | **1** |
| `SUJETO VIVO` | `LO NOMBRA SIN ABRIRLO` | **7** |

**LO QUE ESE CRUCE DICE, Y ES LA CIFRA QUE IMPORTA PARA DECIDIR EL CABLEADO: de
17 senalados, solo 4 abren de verdad un fichero vivo.** Los otros **13** o leen
un sujeto ya clavado (**2**) o solo nombran el fichero sin abrirlo (**11**). **La
guarda no se equivoca en su carril**, porque `NO DECIDIBLE` significa
literalmente que el arnes no deja claro cual es su sujeto, y eso es cierto en los
nueve; **pero 7 de los 8 que llama `SUJETO VIVO` no abren nada vivo.**

#### 4.d. LOS CUATRO QUE SI ABREN, NOMBRADOS

| arnes | que abre | la guarda decia |
|---|---|---|
| `vuelta157_tarea4b_mutacion_tachado.py` | `LECTURAS_DIRIGIDAS.md`, con `io.open` sobre la ruta viva | `SUJETO VIVO` |
| `vuelta160_tarea7c_mutacion_guarda_cita.py` | copia `LECTURAS_DIRIGIDAS.md` e `INTRA_DOMINIO_VEREDICTOS.jsonl` vivos a un temporal | `NO DECIDIBLE` |
| `vuelta174_tarea1b_mutacion_esqueleto.py` | `REPORTE.md` | `NO DECIDIBLE` |
| `vuelta150_2d_simular_op_c_05.py` | `master_graph.json` | `NO DECIDIBLE` |

**El caso de `vuelta160_tarea7c` merece su linea**: copia el fichero vivo a un
temporal y trabaja sobre la copia, lo cual parece congelado y no lo es. **El
resultado sigue dependiendo de lo que el fichero vivo diga hoy**, porque la copia
se hace en cada corrida. Por eso `tmp` y `tempfile` **no** cuentan como marca de
clavado en este instrumento, y eso va escrito en su codigo con su motivo.

**LOS DOS QUE LEEN UN SUJETO YA CLAVADO** son `vuelta135_2e_mutacion_1.py` y
`_2.py`, los dos por `git show e12e4c362fe734ff:docs/loop/REPORTE.md`. **No les
falta nada de fondo:** lo unico que les falta es **declararlo** con el literal que
la guarda busca, para dejar de salir `NO DECIDIBLE`.

#### 4.e. EL REGISTRO, Y LO QUE NO SE HIZO

`docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl`, **17 filas**, una por arnes, con el
nombre, los dos veredictos, el fichero que abre, **la linea del codigo** como
evidencia, y **que haria falta** para arreglarlo. **20.939 bytes en disco y 20.939
normalizados a LF.**

**Y LO QUE NO SE HIZO ES TAN PARTE DEL ENCARGO COMO LO QUE SI:**

- **NINGUN ARNES SE ARREGLO.** Cero ficheros de `scripts/loop/` tocados por este
  instrumento.
- **LA GUARDA NO SE CABLEO** al rojo global de la bateria. Sigue corriendo sola en
  su carril con `--sujeto-congelado`.
- **NADA SE BORRO DE LA NOMINA** (`AUDITOR.md` 6.1): sigue en **103** al corte
  `8bd3bd3e8864`.

**LA RECOMENDACION PARA EL CABLEADO, CON LOS VEREDICTOS DELANTE Y NO ANTES**, que
es lo que el encargo pedia dejar preparado: cablearla hoy pondria la bateria de la
181 en rojo por **17**, de los cuales **13 no abren nada vivo**. **Lo barato es al
reves**: primero que los **13** declaren su sujeto, que no cuesta codigo nuevo
sino una linea por arnes, y despues cablear con **4** pendientes de verdad. **No
lo decido yo**, y va como pregunta.
