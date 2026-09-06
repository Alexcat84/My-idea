### TAREA 1. LOS REGISTROS Y LA DEUDA DE LECTURA

**1.a. EL ACTA 181, CITADA CON SU LINEA.** Instrumento
`scripts/loop/vuelta182_tarea1_registros.py`, salida
`docs/loop/SALIDA_V182_T1A_REGISTRO_ACTA_181.txt` (**8.504 bytes**). Cabecera del
acta 181 en la **62907** y la del acta 180 en la **62449**, las dos localizadas y
no tecleadas. **42 agujas buscadas, 42 halladas, 0 no halladas**, contadas de ese
fichero.

**R.43 ESCRITO**, con el numero que devuelve `serie_de_registros.siguiente_libre()`
y no tecleado. Instrumento `scripts/loop/vuelta182_tarea1a_registrar_acta181.py`,
salida `docs/loop/SALIDA_V182_T1A_REGISTRO_R43.txt` (**2.910 bytes**). Titulo con
sus tres numerales contados del acta acotada (lineas 62907 a 63249): **5
adjudicaciones `7.n`**, **1 caida propia del auditor** (`C.1`, linea 62932) y **1
del ejecutor** (`E.2`, linea 63078). `docs/PENDIENTES.md` pasa de **843.961** a
**850.711 bytes**. Caso por mutacion **VERDE**
(`docs/loop/SALIDA_V182_T1A_MUTACION_REGISTRO.txt`, **1.607 bytes**): 4 actas
fabricadas, el esperado mutado **CAE**, y el prefijo viejo `6.` sobre un acta que
numera `7.n` da **CERO**.

> **CAIDA MIA, Y VA DELANTE.** En el docstring del bloque de apertura, en el del
> esqueleto y en dos mensajes de commit escribi que la adjudicacion `6.8` del acta
> 180 dice, con esas palabras, *"El tope vuelve a cinco en la 182"*. **NO ESTA EN
> EL ACTA:** esa frase literal es del **reporte de la 181**
> (`docs/loop/reportes/REPORTE_V181.md:21`), o sea prosa mia. Lo que el acta 180
> escribe esta en su punto 10, **linea 62893**: *"EL TOPE: DOS SUB-TAREAS EN LA
> 181, POR MI ADJUDICACION 6.8, y vuelve a cinco en la 182"*. **La sustancia
> coincide; la atribucion y el literal no.** El texto viejo no se borra: vive en
> los commits `c85f0c4d` y `afa8ecc5`.

> **DEUDA MEDIDA Y NO CALLADA.** La ultima entrada de la serie antes de esta
> registraba el acta de la vuelta **172** (`R.42`). **Las actas 173 a 180 no
> tienen entrada propia.** Se cuenta en la seccion G de la salida y **no se
> inventan ocho registros que nadie encargo**.

**1.b. LOS DOS PENDIENTES DEL ACTA 180.**

**EL `E.1`**, sobre `scripts/loop/cerrar_reporte.py` (**38.947 a 43.563 bytes**).
Tres causas medidas y **cuatro piezas** de remedio: el patron no casaba con
`SALIDA_V180_HUECO_BATERIA` y daba `None`; con `None` la guarda de vuelta ajena se
saltaba en silencio; la rama se elegia solo por si el fichero traia lineas; y **una
corrida no es cualquier fichero con lineas, tiene que llamarse como una corrida**.
La decision sale de `main()` y pasa a ser `rama_de_la_seccion9()`, pura y con arnes
propio: **9 casos, 9 calzan, 4 en que la logica vieja y la viva difieren**, y las
dos mutaciones **CAEN**
(`docs/loop/SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt`, **5.573 bytes**).

> **EL ARNES CAZO QUE MI PRIMER REMEDIO ERA INCOMPLETO.** Con solo tres piezas
> salia VERDE en sus nueve casos **y su propia seccion C publicaba que el caso real
> de la 180 seguia saliendo `CORRIDA`**. Esa salida queda entera en
> `docs/loop/SALIDA_V182_T1B_ARNES_REMEDIO_INCOMPLETO.txt` (**5.293 bytes**) y el
> parche a medias en `SALIDA_V182_T1B_REMEDIO_E1_PRIMERA_PASADA.txt` (**867
> bytes**). De ahi salio la pieza (d). **Hoy el caso de la 180 sale `HUECO` y
> `hueco_declarado_que_falta()` SI corre.**

**LA `P.1`**, primero el esperado y despues el nombre, que es parte de la
adjudicacion `6.6` (acta 180, **linea 62818**). Caia con **exit 1 fallando 1 de
6**; hoy sale **exit 0 con 7 de 7**. **Tres mitades**, y solo la primera estaba
encargada: el escenario historico se reconstruye de `git ls-tree` y `git show` en
vez de copiar `docs/loop/reportes/` **de hoy**; la comprobacion deja de preguntar
por el repo de hoy; y el bloque E deja de correr contra el arbol vivo y pasa a ser
**conducta sobre dos escenarios fabricados** (muerde cuando falta el archivo, deja
de morder cuando esta). **La segunda y la tercera aparecieron al medir y son la
misma especie que el `6.6` adjudica.** Salidas:
`SALIDA_V182_T1B_REMEDIO_P1.txt` (**2.337 bytes**),
`SALIDA_V182_T1B_REMEDIO_P1_MITAD_C.txt` (**1.395 bytes**) y
`SALIDA_V182_T1B_DECLARAR_CONGELADO_P1.txt` (**1.897 bytes**).

Renombrado con `git mv` a
`scripts/loop/vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py`. **Censo 168 a
169**, **nomina 108 a 109**. Entra en la nomina porque **la regla de entrada es el
SUJETO CONGELADO y no el plazo de una vuelta**, y eso lo dice el propio fichero de
la bateria desde la 148. `anclaje_de()` lo dejaba en **NO DECIDIBLE** por cinco
apariciones de `REPORTE.md` en la maquina; cuatro eran prosa de `print` y el nombre
de un temporal y **se quitaron**, y la que queda es un `git show` de un blob
clavado, **declarada con su motivo y nombrando su linea**. Hoy: **CONGELADO**,
`guarda_del_sujeto_congelado()` **0**, `arneses_que_faltan()` **0**,
`nomina_invisible_al_censo()` **0**.

**1.c. LA RELECTURA AL DOBLE**, encargada por la `7.2` del acta 181
(`ACTA_AUDITOR.md:63171`) por `AUDITOR.md:57`. Instrumento
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, salida
`docs/loop/SALIDA_V182_T1C_RELECTURA_AL_DOBLE.txt` (**9.452 bytes**). El tramo son
los **30 puestos** que la seccion 8 del acta lista, leidos del acta en su
**linea 63210**; el doble son **30 vecinos deterministas** (el siguiente puesto
libre de cada uno), **solape con el tramo 0**, **60 releidos en total**. De los 60:
**3 declaran diferenciador**, **1 tiene lesion exacta** (el **2.464**) y **0 tienen
un nodo muerto**. La maquina **se importa** del instrumento de la TAREA 3.

> **LO QUE ESTA RELECTURA NO ES, Y SE DICE PARA NO VENDERLA DE MAS:** no vuelve a
> decidir la clase de ningun par. **Es la relectura MECANICA del tramo con la vara
> nueva de esta vuelta**, que es la unica que se puede correr sobre 60 pares sin
> inventarse nada. Lo que la vara no ve, esta salida **no lo afirma**.
