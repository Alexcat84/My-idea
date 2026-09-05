### TAREA 2 (BLOQUEANTE). EL SUJETO CONGELADO, RESUELTO Y CABLEADO

**EL ORDEN SE RESPETO Y ES LA MITAD DE LA TAREA:** primero declararon los trece,
despues se congelaron los cuatro, la guarda dio **0**, **y solo entonces se
cablea**. Cablear con 17 habria dejado la 181 en un rojo permanente, que es
degradacion silenciosa del `banco 9`.

**2.a. LOS TRECE QUE NO ABREN NADA VIVO DECLARAN SU SUJETO.** Instrumento:
`scripts/loop/vuelta180_tarea2a_declarar_sujeto.py`, salida
`docs/loop/SALIDA_V180_T2A_DECLARAR.txt`, exit **0**. **A quien le toca NO SE
TECLEA**: sale del registro `docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl`, contado
en la corrida, **17 filas**, de las cuales `LO NOMBRA SIN ABRIRLO` **11**, `ABRE
UN SUJETO YA CLAVADO` **2** y `ABRE FICHERO VIVO` **4**. Los `11 + 2 = 13`
declaran aqui.

**LA LINEA DE CADA UNO SE COMPONE DE SU PROPIA FILA**, no de una lista tecleada:
el fichero vivo que nombra y sus tres cifras (apariciones, llamadas que leen,
lecturas del fichero vivo) salen del registro. Va **dentro del docstring de
modulo**, y eso no es capricho: `anclaje_de()` busca las huellas de congelado en
el texto entero y las de sujeto vivo **solo en la maquina**, asi que declarar en
el docstring garantiza que **la maquina no cambia**. El propio instrumento lo
comprueba con `sin_docstring_de_modulo()` antes y despues de escribir, fichero a
fichero: **13 de 13 con la maquina identica**, y **13 de 13 parsean**.

**LAS LINEAS ANADIDAS POR FICHERO**, contadas de
`docs/loop/SALIDA_V180_T2_NUMSTAT.txt` con `git diff HEAD --numstat -- scripts/loop/`:
los trece salen **`1 0`** exactos, o sea **una linea anadida y CERO borradas** en
cada uno. Son `vuelta135_2e_mutacion_1.py`, `vuelta135_2e_mutacion_2.py`,
`vuelta145_2a_mutacion_ancla_unica.py`, `vuelta148_2d_mutacion_exencion.py`,
`vuelta150_5c_mutacion_ciclo.py`, `vuelta162_tarea2a_mutacion_puerta.py`,
`vuelta162_tarea2b_mutacion_excepcion.py`, `vuelta163_tarea4b_mutacion_re_sellado.py`,
`vuelta165_tarea6_mutacion_op_l_01.py`, `vuelta166_tarea2_mutacion_correccion.py`,
`vuelta166_tarea6_mutacion_guarda.py`, `vuelta177_tarea1b_mutacion_esperado_vivo.py`
y `vuelta179_tarea3_mutacion_triangulos.py`. **NINGUNA otra linea de esos trece se
toco.**

**2.b. LOS CUATRO QUE SI ABREN. Y AQUI LEVANTO UNA CORRECCION AL ENCARGO, MEDIDA
Y NO OPINADA.** El instrumento nuevo `scripts/loop/sujeto_congelado_de_git.py`
(nombre estable, sin numero de vuelta) lee un blob de git clavado por su commit y
**comprueba su `sha256` contra el que el arnes declara**, con dos candados en vez
de uno.

| arnes | que abria | que abre ahora | prueba de que ya no se mueve |
|---|---|---|---|
| `vuelta157_tarea4b_mutacion_tachado.py` | `io.open(LD).read()` sobre `docs/plan/LECTURAS_DIRIGIDAS.md` **VIVO** | blob `24bd395b0cde:docs/plan/LECTURAS_DIRIGIDAS.md`, `sha256 dda1cdd67042c733...` comprobado dentro | dos corridas, salida enmascarada identica, `sha 231f53052759b502` las dos, exit 0 y 0 |
| `vuelta160_tarea7c_mutacion_guarda_cita.py` | `shutil.copy` de **TRES ficheros VIVOS** a un temporal, en cada corrida | `volcar_blob` de los tres blobs clavados (`7dff83ab6a17`, `24bd395b0cde`, `2743bd88faed`), los tres con su `sha256` comprobado | dos corridas, `sha 558a488b8793407f` las dos, exit 0 y 0 |
| `vuelta150_2d_simular_op_c_05.py` | `json.load(open("dataset/metadata/master_graph.json"))` **VIVO** | blob `a34328b23a7d:dataset/metadata/master_graph.json`, `sha256 627cc662296f7f00...` comprobado | dos corridas, `sha c2951c5e99c94698` las dos, exit 0 y 0 |
| `vuelta174_tarea1b_mutacion_esqueleto.py` | **NADA VIVO, y esto es la correccion** | lo mismo que antes: un `REPORTE.md` **fabricado por el en un `tempfile.mkdtemp`** | dos corridas, `sha 09f85ae25297d0ec` las dos, exit 0 y 0 |

**LA CORRECCION, DECLARADA SIN BORRAR LO QUE CORRIGE** (`EJECUTOR.md` 8). El
encargo pone `vuelta174_tarea1b_mutacion_esqueleto.py` entre los cuatro que **si
abren**, nombrando `REPORTE.md`. **Medido, no abre ninguno vivo**, y la prueba la
da el propio registro de la 179 en su campo `evidencia.codigo`, linea 182:
`vivo -> os.path.join(tmp, "REPORTE.md") | io.open(vivo).read()`, donde `tmp` es
el `tempfile.mkdtemp(prefix="v174_mut_")` que el mismo fichero crea y borra. **Lo
que le faltaba era declararlo**, no congelarlo: la guarda buscaba la huella
`REPORTE.md` en la maquina, la encontraba en el nombre del fichero fabricado y no
podia distinguir un sujeto fabricado de uno vivo. **NO PARO POR ESTO**, porque no
hace falta decidir nada que el encargo no diga: el criterio del propio encargo es
*"un sujeto que no dependa de lo que el fichero vivo diga hoy"*, y este ya lo
cumplia; lo unico pendiente era la declaracion y la prueba, y las dos estan.

**LA PRUEBA DE ESTABILIDAD, CORRIDA:**
`scripts/loop/vuelta180_tarea2b_prueba_de_congelacion.py`, salida
`docs/loop/SALIDA_V180_T2B_CONGELACION.txt`, exit **0**. **4 arneses medidos, 4
estables**, y los **5 ficheros vivos** que tenian atribuidos **no se movieron ni
un byte** en las ocho corridas. **EL PRECIO VA DECLARADO Y NO ESCONDIDO:** la
comparacion enmascara toda ruta absoluta, porque tres de los cuatro imprimen su
temporal de sufijo aleatorio; el enmascarado tapa tambien las rutas del repo, asi
que esta prueba **no cazaria un cambio que solo afectara a una ruta impresa**. Lo
que si compara sin tapar es toda cifra, todo `sha256`, todo veredicto y el exit.

**Y UNA SEGUNDA MEDIDA INDEPENDIENTE:**
`scripts/loop/vuelta179_tarea4_juzgar_sujeto.py --solo-mirar`, corrido hoy sin
escribir el registro (`docs/loop/SALIDA_V180_T2B_RELECTURA.txt`), dice **"CIFRA
entradas que la guarda senala: 0"** al corte `HEAD 7aacaa474fcc`. El juez de la
179 reconoce `git cat-file` sobre un blob como sujeto clavado, asi que **los tres
congelados ya no son lecturas vivas para su propio metodo**, y el cuarto tampoco.

**2.c. EL CABLEADO, Y SOLO ENTONCES.** Las dos mediciones, cada una con su corte:

| medicion | corte | fichero contado | entradas que no cumplen | denominador |
|---|---|---|---:|---:|
| ANTES de la 2.a y la 2.b | HEAD `d3240915e994`, apertura de la 180 | `docs/loop/SALIDA_V180_APERTURA.txt`, bloque `H.7` | **17** | 103 |
| DESPUES de la 2.a | HEAD `7aacaa474fcc` | `docs/loop/SALIDA_V180_T2A_GUARDA_TRAS_DECLARAR.txt` | **4** | 103 |
| DESPUES de la 2.b | HEAD `7aacaa474fcc` | `docs/loop/SALIDA_V180_T2C_GUARDA_DESPUES.txt` | **0** | 104 |

**DA 0, ASI QUE SE CABLEA.** El cableado vive en `verificar_mutaciones_viejas.py`,
al cierre de la corrida y **recomputado ahi**, no heredado de la cabecera: nace
`hay_rojo_al_cierre()`, **PURA**, que decide el rojo global con sus **seis
piezas** en un solo sitio, y `main()` la llama. La cifra se imprime con su sello
de corte al lado. **La guarda entra al rojo tambien en modo `--tramo`**, como ya
hacia la mirada de la nomina sobre si misma, y esta comprobado corriendo
`--tramo 1 --tamano-tramo 2` (`docs/loop/SALIDA_V180_T2C_TRAMO_CABLEADO.txt`,
exit **0**): imprime **"CIFRA entradas cuyo SUJETO NO ESTA CONGELADO
(recomputado al cierre): 0, de 104"**.

**LA CONDICION SE EXTRAJO A UNA FUNCION PURA POR UN MOTIVO, Y NO ES DE ESTILO:**
mientras vivio dentro de un `if` de `main()`, la unica forma de probar que una
guarda estaba enchufada era correr la bateria entera y mirar el color. Ahora se le
quita una pieza a la vez.

**EL CASO POSITIVO POR MUTACION DEL CABLEADO**
(`scripts/loop/vuelta180_tarea2c_mutacion_cableado.py`, salida
`docs/loop/SALIDA_V180_T2C_MUTACION_CABLEADO.txt`, exit **0**), sobre un
directorio de arneses de mentira fabricado en un temporal y una nomina fabricada,
**sin leer ni un fichero de la campana**: **10 comprobaciones, 0 fallan.**

| caso | que prueba | resultado |
|---|---|---|
| A1 | un arnes que abre un fichero vivo y no lo declara **sale senalado** | 1 senalado |
| A2 | el MISMO con la linea de declaracion **deja de salir** | 0 senalados |
| B | las seis piezas vacias: **no hay rojo** | `False` |
| C | **solo** la pieza del sujeto congelado: **hay rojo** | `True` |
| **D, LA MUTACION** | la condicion **VIEJA** sobre el mismo escenario de C | `False`, **el caso CAE** |
| E, cinco veces | cada una de las otras cinco piezas **sola** enciende el rojo | `True` las cinco |

**2.d. NADA SE PODA DE LA NOMINA, Y LA RESTA VA COMPROBADA.** La nomina crece de
**103 a 105** con los dos arneses que esta vuelta escribe, y la cuenta se recompone
al cierre de la tarea:

| cifra | valor | corte |
|---|---:|---|
| arneses que el censo ve | **165** | HEAD `7aacaa474fcc` |
| entradas de la nomina | **105** | HEAD `7aacaa474fcc` |
| censo menos nomina | **60** | HEAD `7aacaa474fcc` |
| los que estan FUERA de la nomina | **60** | HEAD `7aacaa474fcc` |
| `arneses_que_faltan()` | **0** | HEAD `7aacaa474fcc` |
| entradas invisibles al censo | **0** | HEAD `7aacaa474fcc` |
| entradas con el sujeto sin congelar | **0** | HEAD `7aacaa474fcc` |

**LA RESTA CALZA: `165 - 105 = 60`, y fuera de la nomina son 60.** Los dos que
entran son `vuelta180_tarea1b_mutacion_etiqueta.py` (103 a 104) y
`vuelta180_tarea2c_mutacion_cableado.py` (104 a 105), cada uno con su motivo
escrito en la propia nomina. **Los otros dos ficheros nuevos de esta tarea NO son
arneses y por eso no entran**, y se dice cual es la vara y no una opinion: el
patron del censo es `vuelta<N>...<familia>...py` con familia en `mutacion`,
`caso_positivo` o `simular`, y ni `sujeto_congelado_de_git.py` (sin numero de
vuelta, es instrumento estable) ni `vuelta180_tarea2a_declarar_sujeto.py` ni
`vuelta180_tarea2b_prueba_de_congelacion.py` traen ninguna de las tres familias.
**Ninguno de los tres se publica como caso positivo por mutacion**: el primero es
un lector, el segundo una operacion de una sola corrida y el tercero una MEDICION
de estabilidad, y asi esta escrito en sus docstrings.
