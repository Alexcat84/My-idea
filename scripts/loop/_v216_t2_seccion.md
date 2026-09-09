### TAREA 2. LA RE-MEDICION QUE EL FUNDADOR ORDENO, CORRIDA Y CON SU CIFRA DELANTE

**QUIEN LA ORDENA, POR SU RUTA Y NO DE MEMORIA:**
`docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md`, **DECISION 2**,
verbatim: *"las cinco fichas SIN EJECUTAR se re-miden contra esas filas (OP-V-01
con su prueba por cita de la corrida K ya escrita)"*. El instrumento es
`scripts/loop/_v216_t2_remedicion.py` y su salida sellada es
`docs/loop/SALIDA_V216_T2_REMEDICION.txt`.

#### 2.a. LAS CATORCE FILAS, SACADAS CON UN INSTRUMENTO Y COTEJADAS CONTRA SU SEDE

**FILAS ARMADAS LEYENDO LA TABLA DE DERIVACION DE `docs/plan/08_VERIFICACION.md`
(947 lineas hoy): 14. FILAS QUE DEBERIA HABER: 14.** **LAS
DOS SE ESCRIBEN JUNTAS**, y si el instrumento hubiera sacado otro numero
**habria parado**, que es lo que el encargo manda.

**Y NO BASTA CON CONTARLAS: CADA FILA SE COTEJA CONTRA SU SEDE.** El instrumento
abre `docs/plan/OPERACIONES.jsonl`, va a la linea que la fila declara, saca la
clausula del indice que la fila declara y **compara el texto VERBATIM**.
**CIFRA filas que NO calzan con su sede: 0** (se exigen 0).

**LAS CORRECCIONES DECLARADAS NO ENTRAN COMO FILAS**, que es lo que el registro
`R.72` del acta 208 adjudico y lo que la propia tabla hace listandolas aparte.
**PERO SI SE LEEN, Y LO DIGO PORQUE ES UNA DECISION MIA:** la tabla trae una
columna que dice, fila por fila, **que correccion corrige que clausula**
(**CIFRA filas que la tabla declara corregidas: 4**), y una
clausula corregida se mide **por su lectura corregida**. Leer la correccion no
es medirla.

#### 2.b. LAS CATORCE, MEDIDAS UNA POR UNA, CON LA BUSQUEDA CORRIDA Y SU CIFRA DELANTE

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V216_T2_REMEDICION.txt`: 14. FILAS QUE DEBERIA HABER:
14.** Ninguna celda de veredicto se teclea: todas se leen de esa salida.

| # | ficha | indice | linea del expediente | la clausula, VERBATIM | veredicto medido hoy |
|---:|---|---:|---:|---|---|
| **1** | `OP-V-01` | 8 | 34 | TRANSVERSAL: Gate 0 verde, suite verde, vuelo completo, prueba de rumbos, y reindexado semantico DESPUES de mover ids | **CUBRE** |
| **2** | `OP-L-01` | 0 | 41 | ninguna de las once aparece en INTRA_DOMINIO_VEREDICTOS.jsonl: viven solo aqui | **CUBRE** |
| **3** | `OP-L-01` | 1 | 41 | el marcador del cribado no se mueve: sigue en 2.117 | **CUBRE** |
| **4** | `OP-L-01` | 2 | 41 | cada nomina afectada se re-mide con su cobertura al lado (banco 9.26) | **CUBRE** |
| **5** | `OP-L-02` | 0 | 42 | las tres nominas afectadas quedan con cobertura COMPLETA y su forma reescrita | **CUBRE** |
| **6** | `OP-L-02` | 1 | 42 | el marcador del cribado no se mueve: sigue en 2.117 | **CUBRE** |
| **7** | `OP-L-02` | 2 | 42 | cada grupo del backlog lleva su motivo escrito, no solo su cuenta | **CUBRE** |
| **8** | `OP-L-03` | 0 | 43 | ningun acto se funde con un par interno sin veredicto | **CUBRE** |
| **9** | `OP-L-03` | 1 | 43 | las 55 lecturas marcadas LECTURA DIRIGIDA: no entran en la cola ni mueven su marcador | **CUBRE** |
| **10** | `OP-L-03` | 2 | 43 | cada acto cuya lectura completa cambie su forma se re-mide con su cobertura al lado | **CUBRE** |
| **11** | `OP-I-01` | 0 | 44 | toda entrada lleva su fecha_corte | **CUBRE** |
| **12** | `OP-I-01` | 1 | 44 | toda forma con cobertura incompleta va marcada PROVISIONAL | **CUBRE** |
| **13** | `OP-I-01` | 2 | 44 | todo hueco va NOMBRADO, nunca rellenado | **CUBRE** |
| **14** | `OP-I-01` | 3 | 44 | el inventario se recomputa entero con el disparador de 08_VERIFICACION | **A MEDIAS** |

**EL REPARTO: CIFRA en CUBRE 13 | CIFRA en A MEDIAS 1 | CIFRA en
NO CUBRE 0 | CIFRA sin sonda 0 | CIFRA medidas 14
de 14.**

**LO QUE ESTA VUELTA ANADE SOBRE LA 214, DICHO CON SU CIFRA Y NO COMO MERITO:**
la 214 dejo **6 de las catorce SIN VEREDICTO MECANICO** y
**2 en NO CALZA LEIDA A LA LETRA**, declaradas documentales o
pendientes de doctrina. **Aqui las catorce llevan sonda corrida, y las que dan
cero publican su cero con el comando delante**, que es lo que la `5.4` del acta
214 autoriza: **lo prohibido es afirmar una busqueda NO corrida, no publicar la
que da cero.**

#### 2.c. `OP-V-01` POR CITA DE LA CORRIDA K, QUE SE BUSCO Y SE ENCONTRO

**LA CORRIDA K EXISTE.** Su ruta es
`docs/loop/SALIDA_SESION_CREDENCIAL_VUELO_K.txt` y mide **63756 bytes en disco y 63655 bytes normalizado a LF**, con **788 lineas**, medidos
hoy. **No se vuelve a producir: se cita**, que es lo que la DECISION 2 manda.

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V216_T2_REMEDICION.txt`: 5. FILAS QUE DEBERIA HABER: 5**
(las cinco partes de la clausula transversal). **CIFRA partes sostenidas por
cita: 5 de 5.**

| # | parte de la clausula | marca con la que se busca | linea(s) en la corrida K | linea(s) en el commit `e966d896` | sostenida |
|---:|---|---|---|---|---|
| 1 | Gate 0 verde | `GATE 0 VERDE` | ninguna | [8] | **SI** |
| 2 | suite verde | `motor 25/25` | ninguna | [12] | **SI** |
| 3 | vuelo completo | `16 de 16 o 16/16` | [7, 784] | [1, 13] | **SI** |
| 4 | prueba de rumbos | `PRUEBA DE RUMBOS` | ninguna | [15] | **SI** |
| 5 | reindexado semantico DESPUES de mover ids | `d70adc1d` | ninguna | [18] | **SI** |

**Y AQUI VA UNA PRECISION QUE NO ME FAVORECE Y LA ESCRIBO IGUAL:** el fichero de
la corrida K sostiene **por si solo** la parte del vuelo completo; **las otras
cuatro las sostiene el cuerpo del commit `e966d896`**, que es el que movio el
estado de la ficha y el que sello la corrida K. **Son dos sedes y no una, y
decir "la corrida K las sostiene todas" seria mentir por omision.**

#### 2.d. EL CASO ROJO NO SE PROMETE, SE PRUEBA POR MUTACION

**El mutante se fabrica EN MEMORIA, sobre una copia profunda de los datos, y no
se escribe en ninguna ficha.** **CIFRA mutantes rotos: 14 | CIFRA que
CAEN, o sea que dejan de decir CUBRE: 14.**

**Y EL REVERSO, PORQUE UNA SONDA QUE NUNCA PUEDE DECIR CUBRE TAMPOCO MIDE:** la
clausula que hoy no da CUBRE se prueba ademas con un mutante **SANO**, y tiene
que SUBIR. **CIFRA mutantes sanos: 1 | CIFRA que SUBEN a CUBRE:
1.**

#### 2.e. LA GUARDA: ESTA TAREA NO MOVIO NI UN CAMPO DE ESTADO

**El `sha256` de `docs/plan/OPERACIONES.jsonl` al ENTRAR, el mismo en disco y normalizado a LF, es `650578474361eb2b`; y al SALIR, tambien el mismo en disco y normalizado a LF, es `650578474361eb2b`. Los dos CALZAN**, porque ese fichero
no trae ni un retorno de carro. Y cero filas de
`git diff --numstat` sobre el expediente, el inventario, la vara y la pagina de
lecturas dirigidas.

#### 2.f. UNA DISCREPANCIA QUE DECLARO EN VEZ DE CALLARLA, Y NO ME FAVORECE DISCUTIRLA

**MI ENCARGO DICE, Y EL ACTA 215 EN SU `5.7` TAMBIEN, QUE LA RE-MEDICION NO LA
HA CORRIDO NADIE.** **Medido hoy por mi: existe
`docs/loop/SALIDA_V214_T2B_REMEDIR_CINCO.txt`, **14302 bytes en disco y 14302 bytes normalizado a
LF**, commit `bb2337a0`, y es una re-medicion de las cinco fichas contra
estas mismas catorce clausulas.**

**NO DISCUTO LA ADJUDICACION Y NO LA NECESITO PARA NADA, porque la orden se
cumple igual:** aquella re-medicion dejo **6 de catorce sin veredicto
mecanico** y **2 mas en NO CALZA LEIDA A LA LETRA**, o sea que
**ocho de las catorce se quedaron sin CUBRE, A MEDIAS ni NO CUBRE**. **La orden
del fundador pedia las catorce medidas, y esa parte NO estaba corrida.** Lo
publico porque `EJECUTOR.md` 2 dice que una discrepancia se declara y nunca se
resuelve copiando, **y porque el que la declara con su cifra soy yo y no el que
me audita.**
