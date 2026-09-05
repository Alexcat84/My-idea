### TAREA 4. LAS DOS PENDIENTES BARATAS, Y UNA CAIDA MIA QUE DECLARO DELANTE

**LA CAIDA VA PRIMERA, PORQUE ES MIA Y PORQUE LA CAUSE PROBANDO LA 4.b.** Corri
`scripts/loop/vuelta180_esqueleto_reporte.py` **entero** para ver la guarda nueva
en su sitio, **prediciendo que el paso 0 lo pararia**. No lo paro, y tenia razon
en no pararlo: el paso 0 pregunta por el reporte que va a pisar, leyo **180** de
la cabecera, lanzo el archivador, el archivador saco el texto **de git**, lo
guardo en `docs/loop/reportes/REPORTE_V180.md`, la guarda salio **VERDE con
razon**, y el esqueleto reescribio `docs/loop/REPORTE.md` con sus cinco filas
vacias, borrando del arbol las secciones de las TAREAS 1, 2 y 3.

**EL DANO, MEDIDO: CERO**, y la medicion esta en
`docs/loop/SALIDA_V180_T4B_ARCHIVO_PREMATURO.txt`. `docs/loop/REPORTE.md` se
restauro con `git checkout HEAD -- docs/loop/REPORTE.md` desde el commit de cierre
de la TAREA 3, y los dos `sha256` cotejados **calzan byte a byte**:
`4836dc51e19092efd56d164d945eaeac4605a96ce95ca6195971c6949a9c9563` el del arbol y
el de `HEAD`, con **3 filas que dicen CERRADA** dentro, contadas del texto. El
archivo prematuro `docs/loop/reportes/REPORTE_V180.md`,
32.854 bytes en disco y 32.854 bytes normalizados a LF, **no seguido por git**,
salia como `??`, **se retiro**, y se dice por que: era el
archivo de un reporte a medias, y dejarlo haria que el
`archivar_reporte.py --vuelta 180` del cierre encontrara su destino **ya
existente con contenido distinto**, o sea rojo.

**LO QUE ESTO ENSENA Y NO SE TAPA:** la guarda del paso 0 protege **el reporte
anterior**, no el de la vuelta en curso. Corriendo el esqueleto a mitad de vuelta,
lo que se pierde del arbol es el trabajo de esa misma vuelta, y **el paso 0 lo
deja pasar en verde porque el archivador lo guarda antes**. La costumbre de
commitear por tarea es lo que hizo que aqui no se perdiera nada.

**4.a. EL DOCSTRING DE `scripts/loop/paso0_archivar_anterior.py`.** La linea vieja
y la nueva, las dos, y **la vieja no se borra de este reporte** ni del propio
fichero, que la conserva escrita dentro de una CORRECCION DECLARADA
(`EJECUTOR.md` 8):

| | texto |
|---|---|
| **la linea vieja** (`git show HEAD:...`, lineas 2 y 3) | `ARCHIVADOR ENCHUFADO, Y LA NEGATIVA A ESCRIBIR SI EL REPORTE ANTERIOR NO ESTA ARCHIVADO.` |
| **la linea nueva** (lineas 2 y 3 de hoy) | `ARCHIVADOR ENCHUFADO, Y LA NEGATIVA A ESCRIBIR SI **EL REPORTE QUE SE VA A PISAR** NO ESTA ARCHIVADO.` |

**Y NO ES LA UNICA FRASE QUE MENTIA.** Tambien decian la pregunta vieja la
clausula `(a)` (*"para la vuelta anterior"*), el bloque `USO` (*"exigir_archivado(N
- 1)"*) y **el nombre del parametro**, que era `vuelta_anterior` y hoy es
`vuelta_del_reporte_a_pisar`. **Un nombre de parametro es texto que describe la
maquina**, y ese mentia igual. `git diff --numstat`: **44 lineas mas y 12 menos**
en ese fichero. **LA MAQUINA NO CAMBIA**: todos los llamadores pasan el numero en
posicion, ninguno por nombre, comprobado con `grep` sobre `scripts/`.

**LA GUARDA QUE HACE VISIBLE LA DIFERENCIA, FABRICADA.** Hoy las dos preguntas
coinciden y por eso en corrida no se ve nada. El caso fabricado pone el arbol en
la **172** con `VUELTA - 1` en **173**:

| pregunta | resultado | clausula |
|---|---|---|
| la BUENA, el reporte que se va a pisar (172) | **VERDE**, deja escribir | ninguna |
| la VIEJA, la vuelta anterior (173) | **ROJO**, lo impide | `(b) no existe` |

**Y LA CONTRAPRUEBA VA AL LADO, QUE ES LO QUE IMPIDE UN ROJO PERMANENTE:** con las
dos preguntas coincidiendo, **las dos dan VERDE**. Sin eso, el caso de arriba no
distinguiria una guarda que mira de una que dice ROJO siempre.

**UNA MEDICION QUE NO ES UN CASO Y SE DECLARA COMO TAL:** preguntar por el numero
equivocado produce un **FALSO ROJO, nunca un falso verde**, porque la clausula
`(d)` coteja siempre contra el fichero del arbol. O sea que la mentira del texto
**nunca pudo destruir un reporte**; lo que podia era bloquear una escritura
legitima. Va medido en el caso `A5`.

**4.b. LA GUARDA QUE FALTABA EN LA DEPENDENCIA DEL `D.4` DE LA 174.** Nace
`scripts/loop/guarda_de_la_fuente_del_clon.py`, **nombre estable y sin numero de
vuelta**, que es la unica forma de que no se pierda en el proximo clon. Comprueba
tres cosas y **CAE EN ROJO nombrando la ruta y la funcion**: `(a)` que la fuente
exista, `(b)` que **defina** la funcion, buscada en su **arbol de sintaxis** y no
con un `in` sobre el texto, y `(c)` que el fichero parsee. **Lo que NO hace, dicho
en vez de insinuado:** no compara los dos cuerpos, que es otra pregunta y tiene
otro instrumento, `cotejar_clon_declarado.py`.

Va **enchufada** en `scripts/loop/vuelta180_esqueleto_reporte.py` como **PASO
0.0**, antes del paso 0, con la fuente y la funcion declaradas en dos constantes
del propio esqueleto. Corrida contra la fuente de verdad
(`scripts/loop/vuelta174_esqueleto_reporte.py`,
**13.918 bytes en disco y 13.918 bytes normalizados a LF**, 273 lineas y 2
funciones definidas) sale **VERDE**.

**EL CASO POSITIVO POR MUTACION DE LAS DOS LETRAS**
(`scripts/loop/vuelta180_tarea4_mutacion_texto_y_clon.py`, salida
`docs/loop/SALIDA_V180_T4_MUTACION.txt`, exit **0**): **17 comprobaciones, 0
fallan**, todas sobre ficheros fabricados en un temporal que se retira.

| caso | que prueba | resultado |
|---|---|---|
| A1 | el dia en que las dos preguntas difieren, la maquina responde a la buena | VERDE / ROJO `(b)` |
| A2 | el parametro se llama por lo que la maquina hace, leido con `inspect.signature` | pasa |
| A3 | el docstring dice la frase nueva, **declara** la correccion y **conserva la vieja** | pasa, las tres |
| A4 | la contraprueba: coincidiendo, las dos dan VERDE | pasa |
| A5 | el numero equivocado da falso ROJO, nunca falso verde | pasa |
| B1 a B6 | fuente presente, **borrada**, sin la funcion, rota, solo mencionada en un comentario, y la vuelta al verde | pasan las seis |
| C | la guarda apuntada a la fuente de verdad del esqueleto de hoy | VERDE |

**LA B5 MERECE UNA LINEA:** una **mencion** de la funcion en un comentario **no
cuenta** como definirla. Un `in` sobre el texto la habria dado por buena, y esa es
justo la forma en que esta guarda podria haber dejado de mirar sin que nadie lo
notara.

**LA NOMINA CRECE DE 106 A 107** con
`vuelta180_tarea4_mutacion_texto_y_clon.py`. Recontada al cerrar esta tarea: censo
**167**, nomina **107**, `167 - 107 = 60` y fuera de la nomina **60**;
`arneses_que_faltan()` **0**, invisibles **0**, sujetos sin congelar **0**.
`guarda_de_la_fuente_del_clon.py` **no entra**, por la misma vara de siempre: su
nombre no trae ninguna de las tres familias del censo.
