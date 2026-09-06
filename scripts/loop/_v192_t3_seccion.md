### TAREA 3. LOS DOS `SUJETO VIVO` DE LA 191. **CERRADA, Y CON UNA CORRECCION DE LA PREMISA DEL ENCARGO:** los dos `SUJETO VIVO` **NO entran en la nomina**, y los que SI entran traen otra deuda.

**(a) LA GUARDA, CORRIDA POR MI, CON SU COMANDO PUBLICADO.**
`VMV.guarda_del_sujeto_congelado_separada(nomina=[(n, True) for n in los_doce])`,
con `VMV` importado y no copiado y la nomina pasada **por parametro**, sin tocar
`VIEJAS`. Los doce se descubren por patron (`^vuelta191_.*\.py$`) y no se
teclean: **salen doce**, como el acta 192 dice.

**LA MEDICION DE APERTURA CALZA CON EL ACTA, Y ESO VA PRIMERO.** El bloque `H.4`
del sello de apertura de esta vuelta, corrido **ANTES de la primera operacion**,
dio **`sujeto_vivo 2` y `sin_motivo 6`**, exactamente lo que el acta 192 publica.
**La medicion del auditor era correcta y lo digo antes de decir lo demas.** Los
dos vivos que nombra son los que nombra: `vuelta191_tarea1a_registrar_acta191.py`
y `vuelta191_tarea3_arreglar_lineas.py`.

**LO QUE NO CALZA ES LA CONSECUENCIA, Y ESO SI ES UNA CIFRA FALSA DEL ACTA.** El
titulo del hallazgo `5.1` dice que los dos *"ENTRAN EN LA NOMINA DE LA BATERIA A
LA VUELTA SIGUIENTE"*. **Eso no se cree: se corre.** La regla de entrada es
`VMV.PATRON_ARNES`, leida del fichero:
`^vuelta(\d+).*(?:mutacion|caso_positivo|simular).*\.py$`. **Exige que el NOMBRE
contenga `mutacion`, `caso_positivo` o `simular`, y ninguno de los dos `SUJETO
VIVO` lo contiene.** Medido:

| | cifra | cuales |
|---|---:|---|
| ficheros `vuelta191_*.py` | **12** | |
| de esos, que el CENSO ve | **3** | `..._tarea3_mutacion_lineas.py`, `..._tarea4_mutacion_veredicto.py`, `..._tarea6_mutacion_bloque_tallado.py` |
| que `arneses_que_faltan()` RECLAMA hoy | **3** | los mismos tres |
| con `SUJETO VIVO` **y** reclamados | **0** | ninguno |

**CORRECCION DECLARADA CONTRA EL ACTA 192, sin borrar lo que corrige:** los dos
`SUJETO VIVO` **no llegan a la nomina por la regla del propio fichero**. La
urgencia que el encargo le pone (*"BLOQUEANTE, Y LO ES POR LA BATERIA DE LA
194"*) **no se sostiene por esa via**. Lo arreglo igual, porque la `4.4` del acta
191 dice que `SUJETO VIVO` es FALLO y el encargo me prohibe dejarlo, **pero la
cifra vieja se queda donde esta y esta correccion va al lado**.

**Y LA URGENCIA SI EXISTE, POR OTRA PUERTA, Y ESA LA TRAIGO YO.** De los TRES que
si entran, **DOS son `NO DECIDIBLE SIN MOTIVO ESCRITO`**
(`vuelta191_tarea3_mutacion_lineas.py`, que nombra `LECTURAS_DIRIGIDAS.md` viva
en su linea 183 y ademas la mide con `wc -l` en la 192; y
`vuelta191_tarea6_mutacion_bloque_tallado.py`, que **abre `docs/loop/REPORTE.md`
vivo** en su linea 108 y se lo pasa a `--comparar`). **Ese es el que puede no
reproducir en la 194**, y **la confirmacion empirica ya esta en el acta 192**:
de los tres arneses que el auditor re corrio, el de la TAREA 3 no reprodujo.

**(b) LOS DOS ARREGLADOS, CADA UNO POR SU CARRIL, PORQUE NO SON EL MISMO CASO.**
Tratarlos igual habria tapado la diferencia:

- **`vuelta191_tarea3_arreglar_lineas.py` ERA UN FALSO POSITIVO, Y ESTA MEDIDO
  ANTES DE DECLARARLO.** Sus seis apariciones de `REPORTE.md` estan **todas
  dentro de literales de `CAMBIOS`, que son patrones de parcheo**: el texto que
  ese fichero busca y sustituye dentro de OTROS scripts. El instrumento cuenta
  sus aperturas de fichero (**6**) y **cuantas nombran el reporte (0)**, y **si
  alguna lo nombrara, PARA y no declara nada**. Carril: la declaracion en el
  propio arnes. **`SUJETO VIVO` -> `CONGELADO`.**
- **`vuelta191_tarea1a_registrar_acta191.py` TIENE EL SUJETO VIVO DE VERDAD:** un
  registrador **tiene que leer el acta de hoy**, y congelarlo lo romperia.
  **Declararlo `CONGELADO` habria sido mentir, y esa mentira es peor que el
  fallo.** Carril: escribir el motivo en cada aparicion, **mas una huella de
  congelado que sea VERDAD Y UTIL y no un literal puesto para enganar a la
  guarda**: ahora **publica el `sha256` LF del acta que acaba de leer**, asi que
  una corrida suya que lea otra acta se puede detectar. **`SUJETO VIVO` -> `NO
  DECIDIBLE CON MOTIVO ESCRITO`**, o sea deuda declarada y no fallo.

**LOS DOS COMPILAN** (`py_compile`, comprobado) y **NINGUNO DE LOS DOS SE HA
CORRIDO**: correrlos pisaria salidas selladas de la 191, y el anclaje se decide
leyendo el TEXTO. Bytes: el primero pasa de **15046 en disco y 15046 en LF** a
**15977 en disco y 15977 en LF**; el segundo, de **78744 en disco y 78744 en LF**
a **79940 en disco y 79940 en LF**.

**UNA CAIDA MIA, CAZADA SIMULANDO Y ANTES DE ESCRIBIR NADA:** mi primer parche
usaba `replace(..., 1)` y el registrador tiene **la misma linea de `p.append`
DOS veces**. Con una sola aparicion sin marca, `motivo_del_sujeto_vivo()` devuelve
False para el fichero entero. La simulacion lo enseño (`motivo escrito: no`) y
`insertar_motivos()` pasa a ir **linea a linea sobre todas las apariciones**, y es
idempotente. **Ninguna cifra falsa salio de aqui porque el modo `--simular` corre
antes de escribir.**

**(c) LOS SEIS `sin_motivo`, NOMBRADOS Y DIAGNOSTICADOS UNO A UNO, Y NO
ARREGLADOS**, que es lo que el encargo pide con esas palabras:

| arnes | sujeto vivo de verdad? | que le falta |
|---|---|---|
| `vuelta191_apertura.py` | **SI.** Un sello de apertura mide el arbol vivo: abre el reporte, el acta y el archivo | solo el motivo escrito, en 9 de sus 11 apariciones |
| `vuelta191_esqueleto_reporte.py` | **SI, y es el que mas.** No solo lee `REPORTE.md`: **lo ESCRIBE** | el motivo, en 7 de sus 14 apariciones |
| `vuelta191_tarea2_relectura_al_doble.py` | **SI, pero SOLO EN LECTURA**: abre el archivo de veredictos y mide su `sha256` al entrar y al salir | solo el motivo, en su unica aparicion (linea 19, la constante `ARCHIVO`) |
| `vuelta191_tarea3_mutacion_lineas.py` | **SI**, y ademas **entra en la nomina**: nombra `LECTURAS_DIRIGIDAS.md` viva y le corre `wc -l` | el motivo, y **es de los dos que de verdad amenazan la 194** |
| `vuelta191_tarea5_marca_contra_dificultad.py` | **SI, SOLO EN LECTURA**: no escribe ni una fila del archivo y lo mide al entrar y al salir | el motivo, en la primera de sus dos apariciones |
| `vuelta191_tarea6_mutacion_bloque_tallado.py` | **SI**, y ademas **entra en la nomina**: **abre `docs/loop/REPORTE.md` vivo** y se lo pasa a `--comparar` | el motivo, y **es el otro que de verdad amenaza la 194** |

**NINGUNO SE ARREGLA AQUI**, porque el encargo lo prohibe expresamente: *"no los
arregles a ciegas"*. **Cuatro de los seis solo necesitan escribir el motivo; dos
necesitan que alguien decida si su sujeto puede congelarse**, y esa decision no
la tomo yo en esta vuelta.

**(d) LA NOMINA NO SE TOCA.** Sigue en **127 entradas**: no se poda, no se
adelanta y no se le anade nada. La opcion `c` que el fundador RECHAZO el 5 sep
2026 sigue rechazada, y quien mete a alguien en la nomina es la regla del
fichero.

**(e) EL CASO POSITIVO POR MUTACION, EN SU PROPIO FICHERO DE NOMBRE ESTABLE:**
`scripts/loop/guarda_de_entrada_a_la_nomina.py`, **VERDE** con **13 casos** y
**cinco mutaciones que caen de verdad**
(`docs/loop/SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt`,
**disco 2433 bytes | LF 2433 bytes**). La guarda **cruza lo que ninguna de las dos guardas viejas
cruzaba**: `guarda_del_sujeto_congelado_separada()` mira **la nomina de hoy**, o
sea los que ya entraron, y cuando muerde ya es tarde; `arneses_que_faltan()` mira
**quien va a entrar** pero no mira su anclaje. **La pregunta nueva es el cruce: de
los que el censo RECLAMA, cual tiene el sujeto vivo.**

**Y VIVE EN SU PROPIO FICHERO A PROPOSITO, CON SU CIFRA:** medido en esta vuelta,
**42 entradas de la nomina nombran `verificar_mutaciones_viejas.py`**. La `4.7`
del acta 192 acaba de adjudicar que mover un fichero que la nomina nombra antes
de una bateria pone en riesgo la corrida; si eso vale con CUATRO entradas, vale
mas con CUARENTA Y DOS. **Aqui se importa de alla y no se toca ni un byte de
alla.**

**LO QUE LA GUARDA DICE HOY: VERDE CON DEUDA DECLARADA**, que no es verde a
secas. **FALLO 0** (ningun reclamado sale `SUJETO VIVO`), **DEUDA 2** (los dos de
arriba), **LIMPIO 1**. Y su ceguera va escrita en su propio docstring y probada
por la mutacion `D`: **no ve al que YA esta en la nomina**, para eso esta la otra.
