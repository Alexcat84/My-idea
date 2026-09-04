### TAREA 4, `OP-V-01` POR LA DECISION 5: HAY PRUEBA, Y LA FICHA NO VUELVE A PENDIENTE

**Salidas:** `docs/loop/SALIDA_V168_T4_OP_V_01.txt` y
`docs/loop/SALIDA_V168_T4_MUTACION_OP_V_01.txt`. **Instrumento:**
`scripts/loop/vuelta168_tarea4_op_v_01.py`.

**EL HASH NO SE RECIBIO DEL ENCARGO: SE BUSCO.** El encargo nombra `e966d896` y
ordena *"VERIFICALO TU TAMBIEN"*, asi que el instrumento recorre los commits que
tocan `docs/plan/OPERACIONES.jsonl` y compara la ficha contra la de su padre
hasta encontrar el que cambia el campo. Cifras de la seccion A de la salida:

| lo que se midio | cifra |
|---|---|
| commits que MUEVEN el estado de `OP-V-01` en toda la historia | **1**, `e966d896`, `LISTA -> HECHA` |
| commits que la HACEN NACER, contados aparte | **1**, `c891b3ff`, `(nace) -> LISTA` |
| hash del encargo contra hash medido | `e966d896` contra `e966d896`, **COINCIDEN** |
| los cinco puntos transversales en el cuerpo del commit medido | **5 de 5 PRESENTES** |

**LOS CINCO PUNTOS SE BUSCARON POR SU MARCA PROPIA Y NO POR SU ORDEN** (seccion
C): Gate 0 con su ciclo entero y `26 en OK`; las tres suites (`motor 25/25`,
`1.040 pasadas`, `tsc exitcode 0`); el vuelo `16 de 16` en la `corrida K`; la
`PRUEBA DE RUMBOS` `SIN DERIVA`; y el reindexado con `d70adc1d` y `42223fcc`.
**Si faltara uno, el instrumento paraba y la ficha volvia a pendiente**, que es
lo que la decision 5 manda. No falto ninguno.

**LO ESCRITO, Y ES CORTO A PROPOSITO** (seccion E). La ficha **YA TRAIA** la
corrida K y los dos sellos: los escribio el propio commit del fundador. Lo que
**no traia**, y es exactamente lo que el hallazgo 4.4 del acta 167 declaro no
haber verificado, es **que commit movio el estado**. Eso es lo que se adosa:
**1.711 caracteres anadidos, de 3.394 a 5.105; la nota vieja sigue ENTERA dentro
de la nueva (comprobado por el instrumento, no afirmado); 71 fichas antes y 71
despues; 18 claves, el esquema no crece; y el estado NO se movio.**

**Y LA NOTA DICE ALGO MAS, QUE ES LO QUE LE IMPIDE SER UN FALSO VERDE: LA FICHA
SIGUE SIN CALZAR CON EL INSTRUMENTO, Y SE DECLARA.** Escribir la prueba por cita
**no cambia** el veredicto de `vuelta150_3_relectura_expediente.py`, que en esta
misma vuelta sigue midiendo `OP-V-01` como **HECHA SIN NINGUNA PRUEBA** (medido
en la TAREA 5: `CIFRA fichas HECHA sin ninguna prueba: 1`). **Y EL INSTRUMENTO NO
SE TOCA PARA QUE CAMBIE.** Sus tres pruebas son grafo, codigo vivo y huella en
git con rutas `dataset/`, `web/` o `engine/`, y `e966d896` toca `docs/` y
`examples/`, medido con `git show --numstat`. **La prueba por cita es una CUARTA
via que la decision del fundador autoriza para esta ficha, no una de las tres.**
Aflojar el instrumento para que la fila se pusiera verde habria sido la
degradacion callada que el canon 9 del banco prohibe. **Marcado como
DISCUTIBLE.**

**EL CASO POSITIVO POR MUTACION: 16 casos pasan tal cual y los 16 caen al mutar
el esperado**, exit 0. El veredicto de los cinco puntos es variable computada:
alimentado con cuerpos fabricados, el mismo codigo da 5, 4, 3 y 0 segun lo que el
cuerpo traiga.

**UNA CIFRA MIA QUE ESTUVO MAL Y LA CAZO EL ARNES, declarada y no tapada:** puse
que habia **1** movimiento de estado y el arnes midio **2**. No era la ficha, era
mi vara: contaba el NACIMIENTO (`None -> LISTA`, en `c891b3ff`) como movimiento.
Se arreglo **en la fuente**, separando las dos poblaciones y publicando las dos,
que es mas exacto que antes y no mas laxo. El motivo queda escrito en el
comentario del instrumento.
