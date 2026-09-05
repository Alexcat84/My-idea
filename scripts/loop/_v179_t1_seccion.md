### TAREA 1. LOS REGISTROS, LAS CORRECCIONES Y LA OPERACION DE CODIGO DE LA ESCALADA

#### 1.a. LA CORRECCION DECLARADA DE LA CAIDA DE LA 178, CON LAS TRES CIFRAS AL LADO

**EL TEXTO VIEJO NO SE BORRA Y EL REPORTE ARCHIVADO NO SE RETOCA**, que es lo que
el encargo manda y lo que `EJECUTOR.md` 8 exige: una correccion que tapa lo que
corrige no se puede auditar. `docs/loop/reportes/REPORTE_V178.md` sigue diciendo
en su **linea 349** lo que se publico.

| cifra | cuanto dice | de donde sale |
|---|---:|---|
| la PUBLICADA por la 178 (**CORRECCION DECLARADA**: es la que se corrige, no la que se afirma) | **16** | `docs/loop/reportes/REPORTE_V178.md:349`, localizada por el bloque H.6 de `scripts/loop/vuelta179_apertura.py` |
| la DEL FICHERO que esa frase cita | **18** | `docs/loop/SALIDA_V178_T1E_MUTACION.txt`, su linea que empieza por `CIFRA casos` |
| la DE MI RE-CORRIDA DE HOY | **18** | `docs/loop/SALIDA_V179_T1A_RECORRIDA_178.txt`, corrido en esta vuelta |

**Y UNA CUARTA MEDICION QUE NO DEPENDE DE NINGUNA DE LAS TRES:** el bloque H.6 de
la apertura conto las lineas del propio fichero que terminan en `CAE` y salieron
**18**. Cuatro caminos, una sola cifra, y la publicada no es ninguna de ellas.

**LA CAIDA ES MIA Y ASI QUEDA ESCRITA:** la frase de la 1.e de la 178 se tecleo
en vez de contarse del fichero que ella misma citaba. Es exactamente la especie
que `EJECUTOR.md` 1 nombra desde la vuelta 76.

#### 1.b. LA OPERACION DE CODIGO DE LA ESCALADA, QUE ES LA PIEZA QUE MANDA

**LA GUARDA DE LA PROSA QUE CITA UN FICHERO**, dentro de
`scripts/loop/cerrar_reporte.py` y junto a sus hermanas, con la misma forma que
ellas: **cuatro funciones PURAS** que reciben el texto y un lector.
`parrafos_fuera_de_cerca()`, `cifra_propia_del_arnes()`, `emparejar_citas()` y
`citas_de_arnes_que_no_calzan()`. El lector de disco, `lector_de_docs_loop()`, va
aparte a proposito: es la unica pieza que toca el disco, y por eso su arnes puede
tumbar a las otras cuatro sin tocar el repo.

**LO QUE HACE, Y LOS TRES MOTIVOS DE ROJO:** caza toda frase que publique una
cifra de casos y nombre un `SALIDA_V*.txt`, lee la cifra propia de ese fichero
(la linea que empieza por `CIFRA casos`, o su hermana `CIFRA casos que CAEN: X de
Y`, de donde el total es la segunda) y cae en rojo nombrando **la linea, la cifra
publicada y la del fichero** si no calzan, si el fichero no existe o si mide cero
bytes. Los dos ultimos por la letra del 5 sep, LA RUTA QUE PROMETE PRUEBA ES
CIFRA. **Los bloques cercados quedan fuera**, por el mismo motivo que la guarda de
la pareja: ahi va pegada la salida cruda y una cita que se retoca deja de ser una
cita.

**LA CORRIDA SOBRE `REPORTE_V178.md`, Y SE PUBLICA LO QUE SALIO**
(`docs/loop/SALIDA_V179_T1B_SOBRE_178.txt`). La tabla sale de contar ese fichero:

| que se cuenta | cuantos |
|---|---:|
| parejas cifra mas fichero que la guarda emparejo | **7** |
| de esas, las que CALZAN | **6** |
| de esas, las que NO calzan | **1** |
| cifras de casos que la guarda NO empareja con ningun fichero | **6** |

**LA GUARDA CAZA LA CAIDA DE LA 178 EN SU PRIMERA CORRIDA**, y lo digo con esas
palabras porque es lo que el encargo pide: **linea 349, fichero
`SALIDA_V178_T1E_MUTACION.txt`, cifra publicada 16, cifra del fichero 18**.

**Y LA PRIMERA VERSION DE ESTA GUARDA TENIA UN DEFECTO PROPIO, QUE SU PRIMERA
CORRIDA DESTAPO Y QUE ESCRIBO AQUI EN VEZ DE CALLARLO.** Cazaba **DOS**, no una:
acusaba tambien a la **linea 189**, donde la prosa dice *"pasa de 5 casos a 8,
los 8 pasan y los 8 caen"* y el fichero dice 8. La cifra que va con el fichero es
la **8**, y mi patron solo veia la palabra `casos`, que ahi solo acompana a la
**5**. Era un rojo inventado, que es justo lo que el docstring de la propia
guarda condena. **Se arreglo antes de seguir**, como el encargo manda: el patron
caza ahora tambien la forma `los N pasan`, y la ventana bajo de 400 a **120**
caracteres, elegida contando las siete parejas reales (32, 34, 36, 45, 51, 51 y
54) y no a ojo.

**EL CASO POSITIVO POR MUTACION**
(`scripts/loop/vuelta179_tarea1b_mutacion_citas.py`,
`docs/loop/SALIDA_V179_T1B_MUTACION.txt`). **25 casos, los 25 pasan y los 25
CAEN** al mutarles el valor esperado. **El caso que lo decide todo es el del
encargo y esta puesto:** un reporte fabricado que publica 16 junto a un fichero
fabricado que dice 18 sale **ROJO nombrando las dos cifras**; el mismo con 18 y
18 sale **VERDE**. Y estan tambien el fichero que no existe, el de cero bytes, el
parrafo con dos cifras y un solo fichero, la forma que no repite la palabra
`casos`, el bloque cercado y la ventana. **Nada sale del repo**: el lector es un
diccionario.

**Y LA GUARDA CAZO ESTE MISMO REPORTE AL CERRARLO, QUE ES COMO NACIO SU UNICA
EXENCION.** La tabla de la 1.a de aqui arriba publica **16** al lado de
`SALIDA_V178_T1E_MUTACION.txt`, y la guarda la acuso, con razon en su forma: la
cifra no calza. Pero la casa **OBLIGA** a escribirla, porque `EJECUTOR.md` 8 dice
que una correccion se declara **sin borrar el texto viejo**, ya que una
correccion que tapa lo que corrige no se puede auditar. Sin exencion, la guarda
acusaba al reporte por hacer exactamente lo que la doctrina manda. **La exencion
es de una sola palabra y hay que pedirla por escrito:** el parrafo tiene que
decir el literal **CORRECCION DECLARADA**, y entonces la cita se publica igual,
con sus dos cifras, pero no cuenta como rojo. **Sin esas palabras vuelve a ser
rojo**, y ese caso esta en el arnes.

#### 1.c. LOS DOS ARNESES DESTAPADOS ENTRAN EN LA NOMINA, Y LOS TRES DE HOY CON ELLOS

**LA CUENTA ENTERA CON SU RESTA COMPROBADA**, contada de
`docs/loop/SALIDA_V179_T1C_CUENTA.txt` por
`scripts/loop/vuelta179_tarea1c_cuenta_nomina.py`:

| que se cuenta | cuantos |
|---|---:|
| arneses que ve el censo | **163** |
| entradas de la nomina | **103** |
| del censo, FUERA de la nomina | **60** |
| de la nomina, INVISIBLES al censo | **0** |

**LA RESTA:** censo 163 menos nomina 103 es 60, y los que estan fuera son 60.
**CALZA.**

**LOS CINCO QUE ENTRAN, Y CADA UNO COMPROBADO EN DISCO, EN NOMINA Y EN CENSO:**
`vuelta150_2d_simular_op_c_05.py` y `vuelta160_tarea3b_caso_positivo.py`, que son
los dos que la vara arreglada de la 178 destapo, mas los tres que esta vuelta
escribe, `vuelta179_tarea1b_mutacion_citas.py`,
`vuelta179_tarea3_mutacion_triangulos.py` y
`vuelta179_tarea1d_mutacion_corte.py`. **La nomina no se poda** (`AUDITOR.md`
6.1): pasa de 98 a 103.

**Y EL ROJO QUE LA 178 ANUNCIO PARA LA 181 NO LLEGA A EXISTIR:**
`arneses_que_faltan()`, corrido hoy, **no nombra a nadie**.

#### 1.d. EL CORTE DEL DENOMINADOR, CABLEADO DONDE SE GENERA LA CIFRA

**No en una frase**, que es la letra del encargo.
`verificar_mutaciones_viejas.sello_de_corte()` es **PURA** y recibe el
denominador y el head; `corte_de_git()` es la unica que toca git y va aparte.
Cableado en **SIETE sitios** que publicaban un denominador de la nomina, contados
del propio fichero con `grep -c "sello_de_corte("`, que da **10** apariciones
menos las **3** de su definicion y sus dos menciones en comentario: el rojo y el
verde de la guarda del sujeto congelado, el total de su tabla de reparto, la
nomina entera de la cabecera de `main()`, la nomina entera del tramo, y las dos
cuentas de invisibles al censo, la de apertura y la recomputada al cierre.

**EL MOTIVO ESTA MEDIDO Y SE VE HOY MISMO EN ESTA VUELTA:** la 178 publico **15
de 92** siendo verdad, y al cerrar eran **15 de 98**. En esta vuelta pasa otra
vez, y por eso el corte sirve: al abrir la guarda decia **15 de 98**, y despues de
que la 1.c metiera los cinco de hoy dice **16 de 103**, porque uno de los dos
destapados es `NO DECIDIBLE`. **Las dos cifras son verdaderas y ahora cada una
dice contra que denominador se midio.**

**EL CASO POSITIVO POR MUTACION**
(`scripts/loop/vuelta179_tarea1d_mutacion_corte.py`,
`docs/loop/SALIDA_V179_T1D_MUTACION.txt`). **10 casos, los 10 pasan y los 10
CAEN**. Su caso que manda es el de la 178: el 92 y el 98 no se confunden aunque
el corte sea el mismo, y dos cortes distintos no se confunden aunque el numero
sea el mismo. **No se llama a git en ningun caso.**
