### TAREA 3. EL LANZADOR DE LA BATERIA. CERRADA EN VERDE, Y LA BATERIA NO SE CORRE

**LA BATERIA NO SE CORRIO EN ESTA VUELTA, Y ESO NO ES UN HUECO SINO EL ENCARGO.**
La 189 la corrio entera y por `AUDITOR.md` 6.1 la siguiente cae en la **194**. Lo
que se hizo aqui es **arreglar su lanzador y probarlo con sus arneses**. De el se
corrieron **`--plan` y `--siguiente`**, que no escriben ninguna salida sellada de
tramo y no corren ningun arnes; **`--tramo` no se invoco ni una vez**.

**LOS FICHEROS, MEDIDOS EN DISCO POR LAS DOS CONVENCIONES:**

| fichero | bytes en disco | bytes en LF | lineas | `sha256` LF |
|---|---:|---:|---:|---|
| `scripts/loop/vuelta190_bateria_por_tramos.py` | 44857 | 44857 | 949 | `01e40dcf9ab20f9b` |
| `scripts/loop/vuelta190_tarea3b_mutacion_selladas_ajenas.py` | 14532 | 14532 | 283 | `25455d33314884b4` |
| `docs/loop/SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt` | 7489 | 7489 | 91 | `6a4f66f26dfbadbb` |
| `docs/loop/SALIDA_V190_T3_PLAN.txt` | 7229 | 7069 | 160 | `a45e5ce2636f8b7a` |
| `docs/loop/SALIDA_V190_T3_SIGUIENTE.txt` | 1555 | 1524 | 31 | `cf4c4a0a8f426272` |
| `docs/loop/SALIDA_V190_T3_COTEJO_CLON.txt` | 14332 | 14078 | 254 | `080e6ec950149ec9` |

**EL CLON, DECLARADO Y COTEJADO SALGA LO QUE SALGA.**
`scripts/loop/vuelta190_bateria_por_tramos.py` es clon declarado del de la 189, y
`scripts/loop/cotejar_clon_declarado.py` lo publica sin adornos: **docstring A 43
lineas y B 62; maquina A 706 y B 888; 184 lineas de maquina que difieren; 848
tokens que difieren; 165 SENTENCIAS DE CODIGO y 19 LITERALES DE TEXTO.** **Este
clon CAMBIA CODIGO y el cotejo lo dice**, que es exactamente el caso que la `4.8`
del acta 189 manda separar y cuya separacion en codigo **queda fuera de esta
vuelta y va nombrada en el encargo**.

#### (a) EL EXITCODE SEPARA, Y LA CIFRA SE DICE

La causa esta medida en la `4.4` y no supuesta: **los diez tramos de la 189
salieron con `exitcode 1` y en NUEVE de ellos no cayo ni un arnes**; la fuente era
siempre la guarda de nomina en deuda. **Un unico `1` para un arnes caido y para
una deuda declarada es degradacion silenciosa (banco 9).**

Desde la TAREA 2, `verificar_mutaciones_viejas.py` devuelve **0, 1 o 2** segun la
clase. El lanzador **lee ese codigo, lo NOMBRA en su salida sellada y lo PROPAGA a
su propio codigo de salida**, sin aplanarlo a 1:

| codigo | clase | donde se dice |
|---:|---|---|
| 0 | `VERDE` | `CIFRA clase del exitcode del tramo` (dentro de la salida sellada del tramo) |
| 1 | `ROJO POR FALLO` | idem, y `CIFRA clase del exitcode del lanzador` al terminar |
| 2 | `ROJO POR DEUDA DECLARADA` | idem |

**LOS TRES NOMBRES NO SE TECLEAN EN EL LANZADOR:** salen del diccionario
`CODIGO_DE_LA_CLASE` de `verificar_mutaciones_viejas.py`, para que las dos mitades
no puedan discrepar. **Y un codigo que nadie declaro no se traga:** sale como
`ROJO DE ESPECIE DESCONOCIDA`, que sigue siendo rojo y ademas dice que no se sabe
de que es, que es mas informacion que un `1` mudo.

#### (b) LA BATERIA RESTAURA SOLA LAS SALIDAS SELLADAS AJENAS QUE PISA

Es el **PASO 6** nuevo del tramo, y va **despues** del sellado a proposito: si
corriera antes, restauraria la salida del propio tramo, que es justo lo que acaba
de escribirse. La disciplina es la misma que la de `dataset/` porque es el mismo
problema: **se mide lo que se movio, se guarda el corte nuevo al lado, se restaura
el original, y SE VUELVE A MEDIR.** Restaurar sin remedir es prometer, no
comprobar.

- **QUE ES AJENA NO SE TECLEA:** sale de que el nombre del fichero lleve dentro un
  numero de vuelta distinto del de este lanzador, que a su vez se computa de
  `os.path.basename(__file__)`. **Una lista tecleada de ficheros a proteger seria
  proteger lo que uno se acuerda, no lo que hay.**
- **UNA SELLADA PROPIA PISADA NO ES ROJO:** lo que esta corrida escribe es suyo, y
  restaurarlo seria borrar el dia.
- **SI EL CORTE NUEVO INTERESA, SE ESCRIBE AL LADO CON NOMBRE NUEVO Y SU VUELTA,
  NUNCA ENCIMA**, y eso es una funcion (`nombre_del_corte_nuevo`) y no una
  costumbre. **La escritura va EN LF**, que es la convencion de la casa en disco.
- **Y SI AL REMEDIR QUEDA ALGUNA PISADA, EL TRAMO SALE EN ROJO** con esas
  palabras: *eso borra el registro de otra vuelta*.

**LAS TRES QUE LA 189 PISO, CLASIFICADAS POR ESTA VARA SIN ABRIRLAS NI TOCARLAS**
(bloque G del arnes): `SALIDA_V184_T1C_MUTACION_ESTIMACION.txt` (vuelta 184),
`SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt` (187) y
`SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt` (188). **Las TRES salen AJENAS
respecto de esta vuelta**, o sea que la restauracion automatica **las habria
cubierto a las tres**, que es lo que en la 189 tuvo que hacer una persona a mano,
en dos vueltas distintas y a dos personas distintas.

#### EL ARNES, CON EL CASO QUE EL ENCARGO PIDE CON ESAS PALABRAS

`scripts/loop/vuelta190_tarea3b_mutacion_selladas_ajenas.py`, **7 bloques, CIFRA
casos que CAEN 0, CIFRA mutaciones que NO cayeron 0, VEREDICTO VERDE**, contado de
`docs/loop/SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt`. **El caso que el encargo
pide es el bloque E: CAE si una salida sellada ajena se queda pisada.** Sobre un
escenario fabricado, restaurada del todo da `VERDE`, una pisada da `ROJO`, las dos
pisadas dan `ROJO`, y una **propia** pisada da `VERDE`. **Si los dos escenarios
dieran lo mismo, la guarda no estaria mirando nada.**

**Y EL ARNES ME CAZO A MI OTRA VEZ, Y SE DECLARA:** en su bloque F teclee a mano
los bytes esperados del fichero fabricado (**22 y 20**) y **los dos CAYERON**: son
**23 y 21**. Corregido no metiendo las cifras buenas, sino **cambiando el esperado
por una RELACION medida sobre el propio fichero** (`bytes del corte = bytes en
disco menos los retornos de carro`), que es lo que no se puede equivocar al contar
de cabeza. **Es la misma especie que esta casa persigue desde la vuelta 74, y me
mordio dentro de mi propio arnes.**

#### LO QUE `--plan` Y `--siguiente` DICEN HOY, CORRIDOS POR MI

- **`--plan`** (exit 0): guarda de la atribucion **VERDE, 0 literales de vuelta
  clavados**; **nomina 127**, tamano de tramo **13**, **10 tramos**, **suma de las
  entradas de todos los tramos 127**; estimacion **entre 41,9 y 54,6 minutos**
  para la nomina entera, **con su corte pegado en la misma linea**
  (`HEAD bbe8af367232, nomina de 127 entradas contada en esta corrida`).
- **`--siguiente`** (exit 0): **10 tramos del reparto, 0 con salida sellada no
  vacia, 10 que FALTAN, EL SIGUIENTE ES EL TRAMO 1.** **Cuenta desde cero**, que es
  lo que un clon con su propio numero de vuelta tiene que hacer, y **no hereda ni
  una salida sellada de la corrida de la 189**.

**GATE 0 AL CERRAR LA TAREA:** `GATE 0: OK`, motor **25/25**, `tsc` exit **0**, y
`git diff --numstat -- dataset/` en **0 filas**.
