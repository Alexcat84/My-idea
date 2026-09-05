### TAREA 4. LA CEGUERA DE LA VARA: SE ANADE UNA COLUMNA, NO UNA EXCLUSION

**LA VARA ES DEL FUNDADOR Y SU VEREDICTO NO SE TOCA.** Sigue imprimiendo **LAS
SEIS** fichas en LISTA sin prueba, y la cifra vieja sigue publicandose entera. Lo
que se anade es **una columna** y **una segunda cifra al lado de la primera**.

#### 4.a. LA COLUMNA, Y COMO SE MIDE CADA MITAD

Instrumento: `scripts/loop/vuelta150_3_relectura_expediente.py`, corrido con
`--corte HEAD` en esta vuelta. Salida: `docs/loop/SALIDA_V178_T4_VARA.txt`.

| id_op | fase | tipo | depende_de medido | consumida por |
|---|---|---|---|---|
| `OP-L-01` | 09_LECTURAS_DIRIGIDAS | MESA | (vacio) | no |
| `OP-L-02` | 09_LECTURAS_DIRIGIDAS | MESA | OP-D-01=LISTA, OP-D-02=LISTA, OP-D-03=LISTA | no |
| `OP-L-03` | 09_LECTURAS_DIRIGIDAS | MESA | OP-D-01=LISTA a OP-D-06=LISTA | no |
| `OP-I-01` | 10_INVENTARIO | MESA | (vacio) | no |
| `OP-M-02-MEDIOS` | 03_FUSIONES | FUSION DE MESA | OP-M-02=HECHA | **SI, por `OP-U-01`** |
| `OP-M-02-ADMIT` | 03_FUSIONES | FUSION DE MESA | OP-M-02=HECHA, OP-M-02-MEDIOS=LISTA | **SI, por `OP-U-01`** |

**LAS DOS MITADES DE LA COLUMNA SE MIDEN DE SITIOS DISTINTOS, y eso se dice en la
propia salida:**

- **SI ESTA CONSUMIDA sale del GRAFO**, por el resolutor de `P.1` y no leyendo un
  acta: una ficha esta consumida cuando tiene **dos o mas nodos** y **todos
  resuelven a UN SOLO NODO VIVO**, o sea que la fusion que la ficha describe **ya
  ocurrio**. `OP-M-02-MEDIOS` resuelve a `estrategia_multicanal_bienvenida` y
  `OP-M-02-ADMIT` a `fase_admit_celebracion`, y los dos destinos viven.
- **POR CUAL se lee de la propia ficha**, y **se declara que viene de ahi**,
  porque **el grafo guarda el resultado y no quien lo hizo**. Si la ficha no
  nombra a nadie, la columna dice **CONSUMIDA SIN DECIR POR QUIEN** en vez de
  inventar un culpable.

#### 4.b. LA CUENTA PUBLICA LAS DOS, NUNCA SOLO EL CUATRO

La vara imprime ahora, con estas palabras: **"6 en LISTA sin prueba, de las cuales
4 son TRABAJO REAL y 2 estan CONSUMIDAS por otras fichas"**, con las dos nombradas
y con su destino vivo al lado. Y en el bloque de cifras finales:

| cifra | valor |
|---|---|
| fichas en LISTA sin ninguna prueba (la de siempre, **intacta**) | **6** |
| de esas, CONSUMIDAS por otra ficha (nueva) | **2** |
| de esas, TRABAJO REAL (nueva) | **4** |

**PODAR LA CIFRA DE LA VARA SIN EL FUNDADOR ES LO QUE LA CASA RESERVA**, y por eso
el **6** sigue ahi y las seis filas se siguen imprimiendo enteras.

#### 4.c. EL COTEJO DE ANTES Y DESPUES, PARA QUE NADIE TENGA QUE CREERME

`docs/loop/SALIDA_V178_T4_COTEJO_VARA.txt`. **La version vieja se saca de git**
(`git show 77621a68:scripts/loop/vuelta150_3_relectura_expediente.py` a
`scripts/loop/_v178_vara_vieja_copia.py`), **no de una copia a mano**, y las dos se
corren con `--corte HEAD` en esta misma vuelta.

| medicion | valor |
|---|---|
| lineas de la salida VIEJA | **234** |
| lineas de la salida NUEVA | **248** |
| lineas que la vieja tiene y la nueva NO | **8** |
| lineas que la nueva anade | **22** |

**Y LAS OCHO QUE "SE PIERDEN" SON LAS MISMAS OCHO QUE VUELVEN CON LA COLUMNA
PUESTA**: la cabecera de la tabla, su separador y las seis filas. **NI UN
VEREDICTO, NI UNA CLASIFICACION Y NI UNA CIFRA VIEJA CAMBIAN.** Las 37 filas de
"las que no calzan", las 24 congeladas declaradas, las 12 en silencio, la 1 HECHA
sin prueba y el 6 de LISTA sin prueba salen **identicas**.

**Y UN CAMBIO ADITIVO QUE DECLARO EN VOZ ALTA:** la vara llamaba a `main()` a
nivel de modulo, asi que **importarla la corria**, y su caso positivo por mutacion
no podia llamar a sus funciones puras sin arrastrar la vara entera detras. Se le
puso la guarda `if __name__ == "__main__"`. **Corrida como programa hace
exactamente lo mismo que antes**, y el cotejo de arriba lo demuestra.

#### 4.d. EL CASO POSITIVO POR MUTACION, SOBRE UN EXPEDIENTE FABRICADO

`scripts/loop/vuelta178_tarea4_mutacion_consumidas.py`,
`docs/loop/SALIDA_V178_T4_MUTACION.txt`. **11 casos, los 11 pasan y los 11 CAEN**
al mutarles el esperado. **Nada sale del repo**: ni `docs/plan/OPERACIONES.jsonl`,
ni `dataset/nodos/`, ni el grafo.

| el caso | resultado |
|---|---|
| dos nodos que resuelven a un solo VIVO, con su atribucion escrita | CONSUMIDA, y nombra `OP-Z-99` |
| **la misma ficha SIN el alias** | **NO consumida** |
| una ficha de un solo nodo, aunque su nota lo afirme | no consumida |
| consumida pero sin nombrar a nadie | consumida, y lo declara sin inventar culpable |
| dos nodos que colapsan a un destino DEPRECADO | no consumida |

**LA MUTACION QUE MANDA ES LA DEL ALIAS**: si quitarlo no cambiara la respuesta,
la columna no estaria midiendo contra el grafo, estaria leyendo un acta.

**Y ESTE ARNES TAMBIEN TUMBO UN DEFECTO REAL EN SU PRIMERA CORRIDA**, igual que el
de la TAREA 2: la atribucion se buscaba en **la primera ventana** de la nota y
devolvia lista vacia **teniendo la respuesta escrita unos cientos de caracteres
mas abajo**, en la misma nota. La primera corrida de la columna sobre el
expediente real decia *"SI, PERO LA FICHA NO DICE POR QUIEN"* en las dos, y la
ficha si lo decia: `OP-U-01`. Se arreglo la funcion, y el caso del arnes pone la
atribucion **a 400 caracteres de la marca a proposito** para que no pueda volver a
pasar.
