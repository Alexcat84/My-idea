### TAREA 4. EL CENSO DE LO QUE QUEDA DEL PLAN, MEDIDO Y NO NARRADO

**NINGUNA FICHA SE CIERRA Y NINGUN `estado` SE MUEVE.** Lo que esta tarea produce
es **el mapa de lo que queda**, para que el fundador decida el orden. Todo sale
de `docs/loop/SALIDA_V204_T4_CENSO.txt` y de
`docs/loop/SALIDA_V204_T4_VARA.txt`.

#### LAS DOS LECTURAS, CORRIDAS HOY Y PUBLICADAS JUNTAS

**LA PRIMERA, EL CAMPO `estado`, QUE ES LA QUE `AUDITOR.md` 0 PROHIBE COMO VARA**
y que va aqui porque el encargo pide las dos: `docs/plan/OPERACIONES.jsonl` mide
**513043 bytes en disco y 513043 normalizado a LF**, `sha256` LF
**829c583eb779cab6**, con **71 lineas no vacias, 42 en `LISTA` y 29 en `HECHA`**.
El encargo decia 42 y 29 y **lo recontado calza**.

**LA SEGUNDA, LA VARA DEL TRABAJO PENDIENTE, QUE ES LA QUE MANDA.** Corrida con
`scripts/loop/vuelta150_3_relectura_expediente.py --corte 59d32eee...`, **con un
COMMIT y nunca una fecha**, y ese commit es mi HEAD de apertura **leido de
`docs/loop/SALIDA_V204_HEAD_APERTURA.txt` y no tecleado**. Su salida mide
**18759 bytes en disco y 18468 normalizado a LF**, `sha256` LF
**26aceea650da798e**.

| cifra de la vara | mi corrida sobre `59d32eee` | el encargo, corrido por el auditor sobre `c4ffc221` |
|---|---:|---:|
| fichas del expediente | 71 | 71 |
| fichas que no calzan | 37 | 37 |
| congeladas declaradas | 24 | 24 |
| congeladas en silencio | 12 | 12 |
| `HECHA` sin ninguna prueba | 1 | 1 |
| en `LISTA` sin ninguna prueba | 6 | 6 |
| de esas, consumidas por otra ficha | 2 | 2 |
| de esas, TRABAJO REAL | 4 | 4 |

**LAS OCHO CALZAN AL DIGITO, Y ESO SE MIDIO EN VEZ DE MIRARSE:** el computo
cuenta cuantas de las ocho difieren y da **0**. Son **corridas distintas sobre
commits distintos**, y coinciden.

#### EL CRUCE, QUE ES EL PUNTO DEL ENCARGO Y NO LA SUMA

- El campo dice que quedan **42 fichas en `LISTA`**, o sea trabajo por hacer.
- La vara dice que de las 71 hay **37 que NO CALZAN**, y que de esas solo **4 son
  TRABAJO REAL**.
- **El campo `estado` sobreestima el trabajo pendiente en 38 fichas**, y por eso
  `AUDITOR.md` 0 lo prohibe como vara.
- **Y en el otro sentido el campo tambien miente, por exceso de confianza:
  1 ficha esta en `HECHA` sin ninguna prueba en el repo.**

**LA SALVEDAD VA PEGADA A LA RESTA PARA QUE NADIE LA LEA SOLA:** `TRABAJO REAL`
es la etiqueta de la vara, **no un sinonimo de lo unico que queda por hacer**. La
vara llega ahi por un camino escrito: de las 42 en `LISTA`, **24** salen por
congelada declarada, **12** por congelada en silencio, **6** quedan sin ninguna
prueba y **2** de esas estan consumidas por otra ficha. **La resta es aritmetica
sobre las dos cifras publicadas, no una afirmacion de que las otras 38 esten
hechas.** **NINGUNA DE LAS DOS CIFRAS SE CORRIGE CON LA OTRA: SE PUBLICAN LAS
DOS.**

#### LAS TRECE QUE NADIE HA MIRADO NUNCA, NOMBRADAS UNA A UNA

**Las filas se LEEN de la tabla de la vara, fila a fila, y no se teclean:** el
computo lee **61 filas**, de las que **12 son congeladas en silencio** y **1 es
`HECHA` sin ninguna prueba**, y **12 mas 1 son 13**.

| id_op | fase | estado | pruebas que dan positivo | motivo |
|---|---|---|---|---|
| `OP-F-01` | 01_FUENTES | LISTA | P3a | CONGELADO EN SILENCIO |
| `OP-C-01` | 00_CODIGO | LISTA | P2+P3a | CONGELADO EN SILENCIO |
| `OP-C-02` | 00_CODIGO | LISTA | P2+P3a | CONGELADO EN SILENCIO |
| `OP-C-03` | 00_CODIGO | LISTA | P2+P3a | CONGELADO EN SILENCIO |
| `OP-A-01` | 07_ADUANA | LISTA | P2+P3a | CONGELADO EN SILENCIO |
| `OP-A-02` | 07_ADUANA | LISTA | P2+P3a | CONGELADO EN SILENCIO |
| `OP-M-02-PROG` | 03_FUSIONES | LISTA | P1+P3a | CONGELADO EN SILENCIO |
| `OP-M-02-ASSESS` | 03_FUSIONES | LISTA | P1 | CONGELADO EN SILENCIO |
| `OP-M-02-ACTIVATE` | 03_FUSIONES | LISTA | P1 | CONGELADO EN SILENCIO |
| `OP-M-02-ACCOMPLISH` | 03_FUSIONES | LISTA | P1 | CONGELADO EN SILENCIO |
| `OP-M-03-I` | 03_FUSIONES | LISTA | P1+P3a | CONGELADO EN SILENCIO |
| `OP-M-03-II` | 03_FUSIONES | LISTA | P1+P3a | CONGELADO EN SILENCIO |
| `OP-V-01` | 08_VERIFICACION | **HECHA** | **ninguna** | **HECHA SIN NINGUNA PRUEBA: el estado afirma mas que el repo** |

**QUE SIGNIFICAN LAS DOS ETIQUETAS, DICHO Y NO SUPUESTO.** `CONGELADO EN
SILENCIO` es una ficha en `LISTA`, con alguna huella en el repo, cuyo **propio
texto no dice nada de su estado**: no significa que este mal, significa que
**nadie la ha mirado y escrito nunca**. `HECHA SIN NINGUNA PRUEBA` significa que
**el estado afirma mas que el repo**: ninguna de las tres pruebas, de grafo, de
codigo y de git, da positivo.

**EL REPARTO POR FASE DE LAS TRECE, CONTADO Y NO A OJO:** **6** en
`03_FUSIONES`, **3** en `00_CODIGO`, **2** en `07_ADUANA`, **1** en
`01_FUENTES` y **1** en `08_VERIFICACION`.

#### LA GUARDA

`docs/plan/OPERACIONES.jsonl` sale con **513043 bytes en disco y 513043
normalizado a LF**, `sha256` LF **829c583eb779cab6**, **identico al de entrada**,
y **0 de las 71 fichas cambian de `estado`**. El `numstat` de `docs/plan/` sigue
en **0 filas**.

#### LO QUE PROPONGO Y NO DECIDO, MARCADO COMO DISCUTIBLE

**`D.4` LA TRECE NO SON UN BLOQUE HOMOGENEO, Y EL ORDEN IMPORTA.** Seis de las
trece son de `03_FUSIONES` y **cuatro de esas seis son hermanas del mismo tronco
`OP-M-02-*`**, con lo que **una sola lectura las cubriria a las cuatro**. Y
`OP-V-01` **no es del mismo genero que las otras doce**: las doce afirman de
menos y ella afirma **de mas**, que es el unico caso del expediente en que el
campo va por delante del repo. **PROPONGO, SIN DECIDIRLO**, que si la 205 toma
este trabajo empiece por `OP-V-01` sola y siga por el tronco `OP-M-02-*` en
bloque. **El orden lo decide el fundador, y esto es una propuesta con su cifra
delante, no un encargo.**
