### TAREA 3. EL ROJO DE LA BATERIA, ATACADO EN SU CAUSA. **CERRADA, Y LAS TRES CAUSAS DEL ROJO QUEDAN EN CERO, CERO Y CERO.**

**LO QUE ESTABA ROTO, MEDIDO EN EL BLOQUE `F` DEL SELLO DE APERTURA Y ANTES DE LA
PRIMERA OPERACION:** 6 arneses del censo fuera de la nomina, 3 entradas sin sujeto
congelado, y 1 arnes que no muerde. **Las tres cosas ponian en ROJO los diez tramos
de cualquier bateria**, y un rojo permanente y conocido apaga la bateria sola: si
siempre esta roja, nadie mira el rojo nuevo.

#### 3.a LOS SEIS ENTRAN EN LA NOMINA, Y LO RESERVADO ERA PODARLA, NO HACERLA CRECER

**LAS DOS CITAS VAN LEIDAS DE SUS FICHEROS Y NO DE MEMORIA.** De
`scripts/loop/verificar_mutaciones_viejas.py`, desde la vuelta 148: *"LO QUE ESTA
REGLA EXIGE ES SUJETO CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL FIN."*
De `AUDITOR.md` 6.1: *"LA NOMINA SIGUE CRECIENDO: NADIE LA PODA SIN EL FUNDADOR."*
**La opcion `c` que el fundador RECHAZO el 5 sep 2026 era JUBILAR ARNESES VIEJOS**,
que es exactamente lo contrario de anadir.

**LOS SEIS SE RECONTARON DEL INSTRUMENTO AL EMPEZAR** y salieron los mismos seis
que el encargo nombra. Los seis tenian ya **SUJETO CONGELADO comprobado por
`anclaje_de()` antes de entrar**, salvo uno, que lo recibe en la `3.c`.

| lo que se mide | apertura | cierre |
|---|---:|---:|
| entradas de la nomina | **127** | **135** |
| arneses que el censo reconoce | **193** | **195** |
| arneses del censo FUERA de la nomina | **6** | **0** |
| entradas SIN SUJETO CONGELADO | **3** | **0** |
| entradas que el censo NO VE | **0** | **0** |

**LA NOMINA CRECE DE 127 A 135 Y NO SE QUITA NI UNA ENTRADA.** Son los seis del
encargo mas los **dos que nacen hoy** (`3.g` y `4.c`), que entran en su misma
vuelta por la regla aplicada a si misma.

#### 3.b Y 3.c LOS QUE NO TENIAN SUJETO CONGELADO: NINGUNO NECESITO SER CASO DECLARADO

La regla ofrece dos salidas, **o se les congela el sujeto, o pasan a CASO
DECLARADO con su marca**. **Los CUATRO se resolvieron por la primera**, y ninguno
entro como caso declarado: `CASOS_DECLARADOS` sigue en **2** entradas, las mismas
de antes.

**Y LA DECLARACION NO ES UN SELLO DE GOMA: los cuatro se miraron uno a uno ANTES
de escribir nada, y en los cuatro la huella de vivo NO es una apertura del fichero
vivo.** Lo que cada uno hace de verdad va escrito en su propia declaracion, dentro
de su docstring:

| arnes | que ve la guarda | que es de verdad |
|---|---|---|
| `vuelta193_tarea4e_mutacion_sello_entre_procesos.py` | `REPORTE.md` | el argumento de `AP.apuntar("REPORTE.md")`, una CADENA que va a la bitacora del turno para comprobar si sobrevive entre procesos. Todo lo que abre en escritura vive en un `mkdtemp` |
| `vuelta186_tarea2c_mutacion_cierre_tardio.py` | `REPORTE.md` | una linea que el propio arnes IMPRIME para decir que no lo toca. Su sujeto de datos son cadenas fabricadas; lo unico que lee del disco es el codigo bajo prueba, cuyo `sha256` publica |
| `vuelta187_tarea4_mutacion_dos_convenciones.py` | `REPORTE.md` | siempre detras de `git show bb3aaad3:...`, o sea el BLOB de un commit fijo |
| `vuelta188_tarea4_mutacion_cobertura_parejas.py` | `REPORTE.md` | el valor de `RUTA_DEL_187`, que solo se usa detras de `git show` con `COMMIT_DEL_187` delante |

**NO SE TOCA NI UNA LINEA DE MAQUINA DE LOS CUATRO.** La declaracion va en el
docstring, que es donde la guarda busca la huella de congelado y donde esta casa
escribe lo que un fichero declara de si mismo. **La cadena que la guarda confunde
con un fichero no se cambia**: cambiarla para contentar a la guarda seria falsear
la prueba.

#### 3.d EL QUE NO MORDIA: DIAGNOSTICADO, REPARADO, Y CON SU CAUSA ESCRITA

`vuelta172_tarea5_mutacion_cierre.py` llevaba **desde la vuelta 188** sin morder, y
las baterias de la 189 y la 194 lo publicaban como `NO MORDIO` **sin
diagnosticarlo**. Corrido en esta vuelta, la causa sale sola: **su propio caso
verde fabricaba DOS secciones `## 9.`**, la del bucle y la de `CR.CAB_9`.

Eso era inofensivo hasta que **la TAREA 4.b de la vuelta 188 ensancho la pieza (3)
de `cerrar_reporte.py` para cazar SECCIONES DUPLICADAS**. Desde entonces
`A_con_las_cuatro_no_falta_ninguna` daba **1** en vez de **0** y
`A_y_no_nombra_ningun_codigo` devolvia **`['(3)']`** en vez de `[]`.

**NO ES QUE LA GUARDA ESTUVIERA MAL: ES QUE EL SUJETO DE MENTIRA DEL ARNES DEJO DE
SER UN REPORTE VALIDO Y NADIE LO RE APUNTO.** El arreglo es una linea (`tope = 9`
en las dos ramas) y va comentado en su sitio con su causa. **NO SE AFLOJA NINGUN
CASO:** la rama `secciones=False` sigue fabricando un reporte SIN la seccion 9 y la
pieza (3) sigue teniendo que cazarla.

| corrida | resultado |
|---|---|
| antes, en esta vuelta | `ROJO: fallos=2, casos que no caen=1`, exitcode **1** |
| despues | **`VERDE: los 17 casos pasan tal cual y los 17 caen al mutar el esperado`**, exitcode **0** |

#### 3.e NO SE PODA NADA

**No se quito ni una entrada.** La nomina solo crece: 127 a 135, y `CASOS_DECLARADOS`
sigue en 2.

#### 3.f LA BATERIA SOLO SOBRE LO TOCADO, Y EL ROJO SE APAGO

`scripts/loop/vuelta195_tarea3f_bateria_de_lo_tocado.py`. **NO ES LA BATERIA Y NO
SE CITA COMO TAL**: la cadencia de `AUDITOR.md` 6.1 pone la siguiente en la 199.

**LA LISTA DE LO TOCADO NO SE TECLEA A OJO: se computa de git** con
`git diff --name-only <apertura>..HEAD` filtrado por el censo, y se coteja contra
lo que la tarea declara haber tocado. **Se corre la UNION de las dos**, que es el
lado prudente. Salieron **12 arneses**, con las dos listas coincidiendo.

| lo que la corrida acotada encuentra | cifra |
|---|---:|
| arneses corridos, cada uno DOS veces | **12** |
| ANCLA PERDIDA | **0** |
| NO MORDIO | **0** |
| CASO DECLARADO | **0** |
| SIN REPRODUCIR | **0** |
| **CLASE DEL VEREDICTO** | **VERDE, exitcode 0** |

**Y LAS TRES CIFRAS QUE EL ENCARGO MANDA PUBLICAR SALGAN COMO SALGAN, medidas
sobre el repo de hoy y no sobre esta corrida acotada: arneses del censo FUERA de la
nomina 0, entradas SIN SUJETO CONGELADO 0, entradas que el censo NO VE 0.** **Las
tres son cero, y por eso no hay lista que publicar.**

**`dataset/` en 0 filas de `numstat` al entrar y 0 al salir**, y **la sede del
turno del auditor no se movio** (345 bytes, `sha256` LF `2e085e88795b9df2` por los
dos lados), que se remide en vez de creerse porque es la que
`vuelta192_tarea4_mutacion_cuarta_puerta.py` borraba antes de que la 194 lo
arreglara.

**Y ESTA CORRIDA CAZO UNA CAIDA MIA ANTES DE QUE SALIERA DE LA VUELTA.** En su
primera pasada, `vuelta195_tarea3g_mutacion_nomina_enchufada.py` salio **NO
REPRODUCIBLE**: escribia el nombre del temporal de `mkdtemp` en su salida sellada,
y ese nombre cambia en cada corrida. **Una salida sellada que cambia sola no se
puede cotejar con nada.** Corregido quitando el nombre y dejando escrito por que;
la segunda pasada da **0 sin reproducir**. **El cotejo de reproducibilidad de la
vuelta 141 hizo exactamente su trabajo sobre un arnes recien nacido.**

#### 3.g EL CASO POSITIVO POR MUTACION, Y PRUEBA EL CABLE Y NO SOLO LA MIRADA

`scripts/loop/vuelta195_tarea3g_mutacion_nomina_enchufada.py`, salida en
`docs/loop/SALIDA_V195_T3G_MUTACION_NOMINA_ENCHUFADA.txt`: **`CIFRA casos: 15 |
pasan: 15 | fallan: 0`**, **`CIFRA casos que caen al mutar el esperado: 15 de 15`**,
**`VEREDICTO: VERDE`**, contado de su propio fichero.

**POR QUE NO BASTABA CON LO QUE YA HABIA, Y ES LA MITAD QUE IMPORTA.**
`prueba_de_la_nomina()` ya comprobaba que `arneses_que_faltan()` VE a los que estan
fuera. **Lo que no estaba probado por nada es que ese ver MUEVA EL VEREDICTO**, y
la unica forma de saberlo era correr la bateria entera y mirar el color, que es lo
que la adjudicacion `4.4` del acta 190 llama inaceptable. Aqui el cable se prueba
**apagandolo y encendiendolo**: con la lista de faltantes hay `ROJO POR FALLO` y
codigo distinto de cero; con la lista vacia vuelve `VERDE` y codigo cero.

**Y LA TERCERA COSA, QUE ES LA QUE EL ENCARGO SUBRAYA: SER `CASO DECLARADO` NO ES
UNA PUERTA TRASERA PARA SALIRSE DE LA NOMINA.** `arneses_que_faltan()` no consulta
`CASOS_DECLARADOS`, y aqui se prueba en vez de leerse: un arnes declarado que no
este en la nomina **sigue saliendo como que falta**. **Una exencion de exitcode no
es una exencion de estar en la nomina.**

Ademas se prueba que **un hueco de censo es FALLO y no DEUDA** (la precedencia de
`clase_del_rojo()`), y que **la vara del censo sigue protegiendo a los anteriores**,
que no se afloja.

**Todo sobre un directorio de `mkdtemp` y nominas fabricadas en memoria**, sin
tocar `scripts/loop/` ni ningun dato de la campana, y con el temporal retirado al
salir (`P.16`).
