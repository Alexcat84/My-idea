### TAREA 5. EL FORMATO UNICO DEL COTEJO DE CIEGA. **CERRADA.** Los TRES cotejos que el acta nombraba como dejados fuera por formato (183, 184 y 190) **son exactamente los tres que se recuperan**.

**(a) EL FORMATO UNICO, EN `scripts/loop/cotejo_de_ciega.py`**, con nombre estable
y sin numero de vuelta, hermano de `aislador_de_ciega.py` y
`apertura_del_auditor.py`. Lleva **las cinco columnas que el encargo pide y todas
explicitas**: puesto, clase del lector, clase del archivo, si estaba en los
dudosos del lector, y COINCIDE o DISCREPA. **El veredicto no se le pasa: se
computa de las dos clases**, para que no se pueda teclear uno que las contradiga.

**Y LA REGLA QUE LO SOSTIENE ES EL DENOMINADOR: una fila POR CADA PUESTO
COTEJADO, no solo por las discrepancias.** El denominador va **declarado en la
cabecera Y recuperable contando las filas**, y `denominador()` **CAE EN ROJO si
las dos cifras no calzan**. Esa es la enfermedad exacta que la TAREA 5 de la 191
midio: dos de sus seis ficheros solo listaban discrepancias y por eso no se sabia
sobre cuantos pares se midio.

**Y NO ES UNA PLANTILLA QUE NADIE HA CORRIDO: LA TAREA 2 DE ESTA MISMA VUELTA ES
SU PRIMER USUARIO.** `docs/loop/SALIDA_V192_T2_COTEJO.txt` sale de el, y su guarda
corrida sobre esa salida da **declarado 30, filas contadas 30, VERDE**. Se
escribio antes que el resto de esta tarea porque la TAREA 2 necesitaba un cotejo
de todas formas, **y usarlo es la prueba de que sirve**.

**(b) EL LECTOR DE LOS FORMATOS VIEJOS,** en
`scripts/loop/lector_de_cotejos_viejos.py`, tambien de nombre estable, **con sus
CINCO parseadores declarados en el docstring ANTES de contar nada** y cada uno
escrito mirando UN fichero real y nombrado por el: `UNICO`, `COLUMNAS` (la tabla
ancha del 182), `TUBERIA` (la del 190 y la 191), `YO_ARCHIVO` (que cubre las tres
escrituras del 183, el 184, el 189b, el 190 y el 191) y `DISCREPA`, **que es la
regla de la 191 conservada a proposito** porque es la unica que lee ficheros sin
las dos clases, **y lo que recupera es el puesto y nada mas**.

**LAS DOS CIFRAS, PUBLICADAS JUNTAS, QUE ES LO QUE EL ENCARGO PIDE:**

| | recupera | de |
|---|---:|---:|
| ANTES, regla de la TAREA 5 de la 191 | **6** | **43** |
| DESPUES, este lector, sobre los candidatos de HOY | **9** | **46** |
| DESPUES, **cifra comparable**, sin los nacidos en esta vuelta | **8** | **43** |

**Y EL DENOMINADOR DE LAS DOS CIFRAS NO ES EL MISMO, Y ESO SE DICE EN VEZ DE
ESCONDERSE:** la 191 midio sobre **43** candidatos y hoy hay **46**, porque **esta
misma vuelta ha escrito tres ficheros con `COTEJO` en el nombre**
(`SALIDA_V192_T2_COTEJO.txt`, `SALIDA_V192_T5_MUTACION_FORMATO_COTEJO.txt` y
`_auditor_v192_cotejo_ciega.txt`). Comparar 9 contra 6 sin decir eso habria sido
inflar la mejora con mi propia basura.

**EL COTEJO CONTRA LOS SEIS, POR NOMBRE Y NO POR CIFRA**, leidos de
`SALIDA_V191_T5_MARCA_CONTRA_DIFICULTAD.txt` y no de la memoria:

- **SIGUEN DENTRO 5:** `SALIDA_V190_T4_COTEJO.txt`, `SALIDA_V191_T2_COTEJO.txt`,
  `_auditor_v182_cotejo_ciega.txt`, `_auditor_v189b_cotejo.txt`,
  `_auditor_v191_cotejo_ciega.txt`.
- **SALE 1:** `_auditor_v155_cotejo_t3.txt`, **y sale porque este lector es MAS
  ESTRECHO, no mas ancho**: exige las DOS clases Y el denominador, y ese fichero
  solo da el puesto de una discrepancia. **Que la cifra suba con un criterio mas
  estrecho es lo que hace que la subida signifique algo.**
- **ENTRAN 4 QUE NO ESTABAN:** `_auditor_v183_cotejo_ciega.txt`,
  `_auditor_v184_cotejo_ciega.txt`, `_auditor_v190_cotejo_ciega.txt` **y**
  `SALIDA_V192_T2_COTEJO.txt`.

**LOS TRES PRIMEROS SON EXACTAMENTE LOS TRES QUE EL ENCARGO NOMBRA** como *"tres
cotejos de ciega DE VERDAD (los del 183, 184 y 190) que quedan fuera por formato
y no por fondo"*. **Estaban fuera por formato y el formato es lo que se
arreglo.**

**Y CADA UNO PUBLICA DE DONDE SALE SU DENOMINADOR**, que es la mitad del asunto:
del `COTEJADOS: 30` del 183, del `COINCIDEN: 29 de 30` del 184, del `mis clases:
30 | destape: 30` del 190, del `CIFRA puestos mios: 30` del 189b, de la suma de
los dos declarados en el 191, y del conteo de filas en los que si traen
coincidencias.

**UNA CIFRA FALSA CAZADA ANTES DE PUBLICARLA, Y VA DECLARADA:** en la primera
corrida `_auditor_v191_cotejo_ciega.txt` salia con **39 filas y denominador 30**,
que es imposible. La causa esta medida: **ese fichero lista cada discrepancia DOS
VECES**, una en su tabla y otra en su bloque de detalle, y eran **9 duplicadas
sobre 30 puestos distintos**. Se anadio `deduplicar()`, que se queda con la
primera aparicion **y CUENTA cuantas quita, porque una fila descartada en
silencio es una cifra que nadie puede cotejar**; ahora publica **30 filas, 30 de
denominador, y las 9 repetidas dichas al lado**. Y se anadio un aviso que
**publica y no tapa** cualquier fichero con mas filas que denominador.

**(c) NO SE RE MIDE LA MARCA CONTRA LA DIFICULTAD EN ESTA VUELTA**, y el
instrumento lo dice en su propia salida. El universo nuevo **se usa cuando este
medido y declarado, no en el mismo acto en que se construye**: elegir el universo
y sacar la conclusion a la vez es justo lo que la TAREA 5 de la 191 evito bien y
la `4.4` del acta 192 adjudico A FAVOR. **Lo que queda para quien la mida: 8
ficheros comparables, 165 filas con las dos clases y 270 pares de denominador
sumado.**

**(d) LOS CASOS POSITIVOS POR MUTACION, DOS Y NO UNO, PORQUE SON DOS PIEZAS:**

- **Del formato:** `docs/loop/SALIDA_V192_T5_MUTACION_FORMATO_COTEJO.txt` (**disco
  2141 bytes | LF 2141 bytes**), **VERDE**. La mutacion que el encargo pide es la
  `B`: **un cotejo que SOLO lista las discrepancias**, que es la forma de dos de
  los seis ficheros de hoy, y `denominador()` **CAE** y dice que el declarado (3)
  y el contado (1) no calzan. Y hay cuatro mutaciones mas: sin la linea del
  denominador, sin la marca de formato, con la tabla vacia, y **con la cabecera
  mintiendo** (declara 30 y hay 3).
- **Del lector:** `docs/loop/SALIDA_V192_T5_MUTACION_LECTOR_VIEJOS.txt` (**disco
  1961 bytes | LF 1961 bytes**), **VERDE**. Prueba cada parseador sobre su formato,
  que `DISCREPA` recupera menos y **no se prefiere** cuando hay uno completo, las
  cuatro vias del denominador, y **la que importa: sin cabecera y solo con
  discrepancias, el denominador sale `None` y el motivo lo explica, en vez de
  estimarse**.

**LO QUE ESTE FORMATO NO PUEDE HACER, ESCRITO EN SU PROPIO DOCSTRING:** no
convierte en legible un cotejo viejo que no trae la informacion (un fichero que
nunca escribio la clase del lector no la tiene, y ningun lector la recupera), y
**no dice si el lector acerto**, sino si coincide con el archivo, que es otra
cosa: el archivo tambien se equivoca, y esta casa tiene correcciones declaradas
que lo prueban.
