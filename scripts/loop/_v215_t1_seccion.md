### TAREA 1. LOS REGISTROS, Y LA LINEA DE CADA UNO LEIDA HOY

**LA FUENTE ES EL ACTA Y EL LECTOR ES UN INSTRUMENTO.**
`scripts/loop/_v215_t1_registros.py` abre `docs/loop/ACTA_AUDITOR.md`
(**76237** lineas hoy), localiza el acta de la vuelta 214 por su
cabecera en la **linea 75878**, y saca sus entradas numeradas con
`enumerate()`. **NINGUN NUMERO DE LINEA DE ESTA SECCION SE TECLEA**, que es lo
que manda el `6.6` del acta 210 y la letra de `EJECUTOR.md` 1.

#### 1.a. LAS NUEVE ADJUDICACIONES, CON SU LINEA Y CON LO QUE ME OBLIGAN A HACER

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V215_T1_REGISTROS.txt`: 9. FILAS QUE DEBERIA HABER,
CONTADAS POR EL PROPIO INSTRUMENTO SOBRE EL ACTA: 9.** **LAS DOS SE
ESCRIBEN JUNTAS**, por la obligacion de las filas.

| adjudicacion | linea del acta | titulo, VERBATIM del acta | que me obliga a hacer en esta vuelta (LECTURA MIA) |
|---|---:|---|---|
| **`5.1`** | **76149** | LA BATERIA SE DECLARA CORRIDA CON TODOS LOS TRAMOS DE SU REPARTO, Y HOY SON ONCE, NO NUEVE. ADJUDICADO, Y NO HACE FALTA DOCTRINA NUEVA. | CORRO ONCE TRAMOS Y NO PARO EN NUEVE. La bateria se declara corrida cuando los ONCE que el reparto compute tengan salida sellada del mismo calibre. NO reescribo el fichero del auditor: el nueve es la cifra a su corte y se corrige por declaracion. |
| **`5.2`** | **76159** | EL `--siguiente` NO ES SENAL DE ARRANQUE. ADJUDICADO A FAVOR DEL EJECUTOR. | NO USO EL CARRIL DE LA SENAL DE ARRANQUE PARA DECIDIR NADA. Corro tramo por tramo del 1 al 11 y commiteo cada salida al terminar, y publico ANTES el commit y la fecha de los sellos viejos. |
| **`5.3`** | **76166** | EL `2.117` CONTRA EL `3388`: MANDA EL CORTE, NO LA LETRA. ADJUDICADO, PENDIENTE CERRADO. | NO VUELVO A TRAER EL MARCADOR COMO PENDIENTE DE DOCTRINA. La clausula pide que ESA operacion no mueva el marcador, no afirma cuanto vale. PENDIENTE CERRADO, y esta vuelta no mueve el marcador. |
| **`5.4`** | **76174** | EL PUNTO 3 DE `OP-I-01`: UNA NEGATIVA SI SE PUEDE CITAR. ADJUDICADO CONTRA EL EJECUTOR. | MIDO EL PUNTO 3 DE `OP-I-01` CORRIENDO LA BUSQUEDA Y PUBLICANDO SU CERO CON EL COMANDO DELANTE. Lo que se prohibe es afirmar una busqueda NO CORRIDA, no publicar la que da cero. Va en la TAREA 4. |
| **`5.5`** | **76183** | EL PUNTO 4 DE `OP-I-01`: NO LO ADJUDICO, LO ENCARGO, Y DIGO POR QUE. | BUSCO LA SEDE QUE SI REGENERA LA VISTA HUMANA ANTES DE DECIR SI EL PUNTO 4 CUBRE. No la invento: publico la busqueda con su comando, y si la sede no existe eso tambien es un resultado. Va en la TAREA 4. |
| **`5.6`** | **76188** | LAS TRES FILAS VAN DENTRO DE LA TABLA. RESPONDIDA SU PREGUNTA 1. | REGISTRADA, no me da orden nueva. |
| **`5.7`** | **76193** | NO, NO NECESITABA NADA MAS. RESPONDIDA SU PREGUNTA 2. | REGISTRADA, no me da orden nueva. |
| **`5.8`** | **76198** | SUS TRES DISCUTIBLES, LOS TRES A SU FAVOR. | REGISTRADA, no me da orden nueva. |
| **`5.9`** | **76206** | SU `D.3` SE CONFIRMA Y NO LE PERJUDICA. | REGISTRADA, no me da orden nueva. |

**LAS CUATRO ULTIMAS (`5.6` a `5.9`) NO ME DAN ORDEN NUEVA Y LO DIGO EN VEZ DE
INFLARLAS:** dos responden preguntas de la 214, una adjudica sus tres discutibles
a su favor, y la `5.9` confirma su `D.3`. **Se registran porque el encargo manda
registrar LAS NUEVE, no solo las cinco que mandan.**

#### 1.b. EL HALLAZGO CONTRA MI PROPIO REPORTE DE LA 214, QUE ES LA CAIDA QUE ACUMULA

**FILAS ARMADAS: 2.** El acta trae dos entradas en su seccion 3 y
las dos van aqui, porque esconder la que me favorece seria elegir.

| hallazgo | linea del acta | titulo, VERBATIM del acta |
|---|---:|---|
| **`3.1`** | **76086** | LA SECCION 3.1 DE SU REPORTE, QUE ES LA DEL CICLO ENTERO DE GATE 0, SALIO PUBLICADA VACIA. Y ES CAIDA DE REPORTE QUE ACUMULA, PORQUE VIVE EN U |
| **`3.2`** | **76120** | UNA PRECISION MENOR QUE NO ES CAIDA Y LA DIGO PARA QUE NADIE LA CUENTE COMO TAL. |

**LO REGISTRO SIN ATENUARLO, PORQUE ES MIO Y ES EL UNICO QUE ACUMULA.** Mi
seccion 3.1 de la 214, la del ciclo entero de Gate 0, **salio publicada VACIA**:
sus dos filas decian que no habia fichero de consola y las tres columnas de
medicion salieron en blanco. **La causa esta medida y no supuesta: el fichero de
consola que mi compositor buscaba NUNCA EXISTIO**, ni en el arbol ni en la
historia, porque el ciclo imprime su consola por `stdout` y yo no la redirigi. **Y
lo que importa mas que la celda vacia: mi compositor escribio una fila en blanco
y siguio**, que es degradacion silenciosa, que es justo lo que el banco 9
prohibe.

**MI RACHA DE CAIDA DE REPORTE QUEDA EN UNO**, y el remedio de las dos mitades va
en la **TAREA 5** de esta vuelta, que es bloqueante: la consola se sella **desde
dentro del propio instrumento** y el compositor **CAE EN ROJO** si no la
encuentra, en vez de rellenar con un hueco.

#### 1.c. LA GUARDA DE ESTA TAREA, Y SU PRUEBA DE MUTACION

**Las cuatro comprobaciones viven en una funcion pura, `juzgar()`, para que se
puedan mutar sin tocar el acta**: que las adjudicaciones sean nueve, que sus
etiquetas vayan de `5.1` a `5.9` sin huecos ni repeticiones, que las cinco que el
encargo manda aplicar esten, y que el hallazgo `3.1` aparezca.

**`docs/loop/SALIDA_V215_T1_MUTANTES.txt`: 6 mutantes, CAEN 6, y el texto bueno pasa el
mismo juicio en 0 fallos.** El mutante `F` es el que de verdad me
importaba: **las dos listas vacias**, que es lo que devuelve un lector que no
encuentra nada, **cae con 4 fallos**. Un lector roto que no cae es exactamente la
enfermedad de mi `3.1`.
