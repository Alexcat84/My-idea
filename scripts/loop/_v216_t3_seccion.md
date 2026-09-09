### TAREA 3. LA CONSECUENCIA, MEDIDA, Y LAS DOS VARAS LADO A LADO

**EL INSTRUMENTO ES `scripts/loop/_v216_t3_dos_varas.py` Y SU SALIDA SELLADA
ES `docs/loop/SALIDA_V216_T3_DOS_VARAS.txt`.** Todas las tablas de abajo se pegan enteras de ese fichero.
**NINGUNA CELDA SE TECLEA.**

#### 3.a. LAS CATORCE CLAUSULAS, REPARTIDAS FICHA POR FICHA

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V216_T3_DOS_VARAS.txt`: 5. FILAS QUE DEBERIA HABER: 5**
(las cinco fichas). **Y las clausulas repartidas son 14, contra las 14
que la TAREA 2 midio: LA SUMA SE COMPRUEBA CONTRA SI MISMA.**

| ficha | linea del expediente | clausulas suyas | en CUBRE | NO en CUBRE | cuales |
|---|---:|---:|---:|---:|---|
| `OP-V-01` | 34 | **1** | **1** | 0 | ninguna |
| `OP-L-01` | 41 | **3** | **3** | 0 | ninguna |
| `OP-L-02` | 42 | **3** | **3** | 0 | ninguna |
| `OP-L-03` | 43 | **3** | **3** | 0 | ninguna |
| `OP-I-01` | 44 | **4** | **3** | 1 | indice 3 en A MEDIAS |

#### 3.b. LA VARA DEL EXPEDIENTE, CORRIDA CON EL HASH DE MI APERTURA

**EL COMANDO, CON MI HASH Y NO CON OTRO:**
`scripts/loop/vuelta150_3_relectura_expediente.py --corte c7a0651c1e00de6ae296c71aaac52b71e798fa52`, leido del
sello `docs/loop/SALIDA_V216_HEAD_APERTURA.txt` y **no tecleado**. Su salida
cruda vive en `docs/loop/SALIDA_V216_T3_EXPEDIENTE.txt`.

**FILAS ARMADAS: 5. FILAS QUE DEBERIA HABER: 5.** **LA COLUMNA DE LA
IZQUIERDA ES MIA Y LA DE LA DERECHA ES LA DEL ENCARGO**, y van separadas para
que se pueda auditar cual es cual.

| cifra | LA MIA, medida hoy | la del encargo, del auditor | calzan |
|---|---:|---:|---|
| no calzan | **40** | 40 | SI |
| congeladas declaradas | **24** | 24 | SI |
| congeladas en silencio | **12** | 12 | SI |
| en LISTA sin prueba | **3** | 3 | SI |
| en HECHA sin prueba | **4** | 4 | SI |

**CIFRA celdas que NO calzan con la cifra del encargo: 0.** Las
cinco calzan una a una. **Lo digo con las dos columnas delante y no con una
sola**, porque publicar solo la mia cuando coincide es indistinguible de
copiarla.

**Y LA CIFRA DEL AUDITOR NO SE TOMA DEL ENCARGO Y YA: SE LEE DE SU ACTA, CON SU
LINEA**, porque una cifra citada de un encargo no es una cifra leida.

- ANCLAJE fichas que no calzan                   | linea 76665 | cifra suya 40
- ANCLAJE fichas en HECHA sin ninguna prueba     | linea 76666 | cifra suya 4

**LAS CUATRO FICHAS EN HECHA SIN NINGUNA PRUEBA SIGUEN IGUAL, Y VAN NOMBRADAS.**
**FILAS ARMADAS: 4. FILAS QUE DEBERIA HABER: 4.**

- HECHA SIN PRUEBA> OP-V-01 (fase 08_VERIFICACION, pruebas positivas: ninguna)
- HECHA SIN PRUEBA> OP-L-01 (fase 09_LECTURAS_DIRIGIDAS, pruebas positivas: ninguna)
- HECHA SIN PRUEBA> OP-L-02 (fase 09_LECTURAS_DIRIGIDAS, pruebas positivas: ninguna)
- HECHA SIN PRUEBA> OP-L-03 (fase 09_LECTURAS_DIRIGIDAS, pruebas positivas: ninguna)

#### 3.c. LAS DOS VARAS, LADO A LADO, SIN MAQUILLAR QUE MIDAN LO MISMO

**LA VARA NO SABE DE LAS CATORCE FILAS NUEVAS, Y ESO NO ES UN FALLO SUYO.** La
del expediente mide **P1, P2 y P3**: grafo, codigo vivo y huella en git. La de
las catorce filas mide **clausulas de verificacion**. **Son dos varas distintas
midiendo cosas distintas**, y una ficha puede salir en HECHA SIN NINGUNA PRUEBA
teniendo **todas sus clausulas en CUBRE**. **ESO NO ES UNA CONTRADICCION Y NO LO
MAQUILLO.** Cambiar la vara seria fabricar maquinaria y la moratoria lo prohibe.

**FILAS ARMADAS: 5. FILAS QUE DEBERIA HABER: 5.** **CIFRA de las
CUATRO en HECHA sin prueba que NO aparecen en lo leido: 0** (se
exigen 0), que es la guarda que impide publicar esta tabla a medio leer.

| ficha | VARA 1, la del expediente (P1 P2 P3) | VARA 2, las catorce clausulas |
|---|---|---|
| `OP-V-01` | estado `HECHA`, pruebas positivas ninguna, HECHA SIN NINGUNA PRUEBA: el estado afirma mas que el repo | 1 de 1 clausulas en CUBRE |
| `OP-L-01` | estado `HECHA`, pruebas positivas ninguna, HECHA SIN NINGUNA PRUEBA: el estado afirma mas que el repo | 3 de 3 clausulas en CUBRE |
| `OP-L-02` | estado `HECHA`, pruebas positivas ninguna, HECHA SIN NINGUNA PRUEBA: el estado afirma mas que el repo | 3 de 3 clausulas en CUBRE |
| `OP-L-03` | estado `HECHA`, pruebas positivas ninguna, HECHA SIN NINGUNA PRUEBA: el estado afirma mas que el repo | 3 de 3 clausulas en CUBRE |
| `OP-I-01` | estado `LISTA` SIN NINGUNA PRUEBA, o sea que su estado CALZA con el repo: consumida por otra ficha: no | 3 de 4 clausulas en CUBRE |

**LO QUE ESTA TABLA DICE, EN UNA FRASE Y SIN ADORNO:** las cuatro fichas que la
vara del expediente marca como **HECHA SIN NINGUNA PRUEBA** tienen hoy **todas
sus clausulas en CUBRE**; y la unica que **no** tiene todas sus clausulas en
CUBRE, `OP-I-01`, es justamente la que **si** calza con la vara del expediente,
porque su estado `LISTA` es exactamente lo que el repo dice de ella.

**Y UNA CORRECCION DECLARADA DE MI PROPIO COMPOSITOR, QUE NO TAPA LO QUE
CORRIGE:** su primera version leia CUALQUIER fila con forma de tabla de la
salida de la vara, y por eso cogia para `OP-I-01` la fila de la tabla de
DESBLOQUEADAS, cuya tercera celda es el TIPO y no el estado: publicaba
*estado MESA* cuando la ficha esta en `LISTA`. **La cifra era falsa por mi
compositor y no por el instrumento**, se acoto la lectura a la tabla por su
propia cabecera, y **la version vieja queda escrita en el codigo y no se borra**.

#### 3.d. LO QUE PROPONGO, QUE NO ES LO QUE DECLARO

**LA CONDICION LA ESCRIBI ANTES DE SABER EL RESULTADO**, que es lo que el
encargo manda: *"si las CATORCE clausulas quedan en CUBRE con su busqueda
corrida y su cifra delante, y si el cierre integral sale limpio, entonces la
campana esta consumada EN LO QUE EL BUCLE PUEDE CONSUMAR"*.

**CIFRA clausulas en CUBRE: 13 | CIFRA que la condicion exige: 14 | CIFRA
que NO estan en CUBRE: 1.**

- NO CUBRE LA CONDICION> clausula 14, ficha OP-I-01, indice 3, linea 44 del expediente, veredicto A MEDIAS

**LA PRIMERA MITAD DE LA CONDICION NO SE CUMPLE, Y POR ESO NO PROPONGO LA PARADA
FELIZ.** **PROPONGO ESTO EN SU LUGAR, con la cifra delante:** el plan queda
**agotado en trece de sus catorce clausulas**, y la que falta, `OP-I-01` indice
3, **no falta por pereza de esta vuelta**: le falta **la sede que la cumpliria**,
y esa sede **no existe en el repo** (**0 ficheros escriben la vista humana**,
busqueda corrida en la TAREA 2). **Fabricarla es maquinaria nueva y la moratoria
de `AUDITOR.md` 6.3 lo prohibe**, asi que **sube NOMBRADA**, que es donde el
propio auditor ya la puso en el punto 3 de su seccion 6.

**LO QUE ESTA TAREA NO HACE, DICHO PARA QUE NO SE BUSQUE:** no declara la
campana consumada, no escribe `docs/loop/PARA_ALEXIS.md` y **no pide ningun
merge**. Quien declara es **EL AUDITOR**, por la `4.2` del acta 203, **linea
71543**, ratificada por el fundador el 9 sep 2026. **Y EL BUCLE NO FUNDE RAMAS.**

**LA GUARDA DE LA PROHIBICION QUE NO SE NEGOCIA:** `sha256` LF de
`docs/plan/OPERACIONES.jsonl` **igual al entrar y al salir**, y **cero filas** de
`git diff --numstat` sobre el expediente. **CIFRA comprobaciones que fallan en
esta tarea: 0.**
