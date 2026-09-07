### TAREA 2. EL TAMANO DEL AGUJERO DE `cobertura`, MEDIDO Y NO TAPADO

**LO QUE ESTA TAREA NO HACE, Y VA DELANTE PARA QUE NO SE DEDUZCA:** no cierra
`OP-I-01`, no propone cerrarla, **no escribe ninguna vara** y **no toca ni un
campo `estado`**. La vara es codigo permanente y va a la auditoria integral por
el `4.7` del acta 203. Todo lo de abajo sale de
`docs/loop/SALIDA_V204_T2_COBERTURA.txt`.

**LA SEDE, RECONTADA HOY:** `docs/plan/INVENTARIO.jsonl` mide **584554 bytes en disco y 584554 normalizado a LF**,
con `sha256` **69666b73339f2afe** en disco y **69666b73339f2afe** normalizado a LF, y con **672
lineas no vacias, 0 que no parsean como JSON y 672 con la clave `cobertura`**,
todas de tipo cadena y **0 vacias**. El encargo decia 672 y **lo recontado
calza**.

**EL TEXTO DE LAS CUATRO CLAUSULAS, LEIDO HOY DE LA FICHA Y NO DE MEMORIA.**
`OP-I-01` vive en la **linea 44** de `docs/plan/OPERACIONES.jsonl`,
que mide **513043 bytes en disco y 513043 normalizado a LF**,
con `sha256` **829c583eb779cab6** en disco y **829c583eb779cab6** normalizado a LF.
Su `verificacion` trae 4 elementos: (1) *toda entrada lleva
su fecha_corte*, (2) *toda forma con cobertura incompleta va marcada
PROVISIONAL*, (3) *todo hueco va NOMBRADO, nunca rellenado*, (4) *el inventario
se recomputa entero con el disparador de 08_VERIFICACION*. Su `estado` sigue
siendo `LISTA` y **no se toco**.

#### CUANTAS FORMAS TOMA HOY EL CAMPO, AGRUPADAS POR SU FORMA

**LA VARA DE AGRUPACION SE DICE ANTES DE LA CIFRA:** se sustituye toda tira de
digitos por `N` y se agrupa por ese esqueleto, que es la unica manera de que
*"3 de 5"* y *"4 de 9"* cuenten como la MISMA forma. **BUSQUEDA POSITIVA Y CAMPO
DECLARADO: corre sobre el VALOR DEL CAMPO `cobertura`, nunca sobre la linea.**

- **CIFRA formas distintas del campo `cobertura`: 23.**
- **CIFRA valores literales distintos del campo `cobertura`: 77.**
- Las tres mayores concentran casi todo: **554** entradas dicen
  `N de N pares leidos; N en cola; N fuera de cola`, **53** dicen `N ids` y
  **18** son un numero pelado. **Once de las 23 formas tienen UNA sola entrada.**

#### CUANTAS QUEDARIAN FUERA DE CUALQUIER VARA RAZONABLE

Las varas candidatas **no se inventaron: salen de agrupar el campo antes de
escribir un solo patron**, que es lo contrario de fabricar una vara y buscarle
clientes. **Ninguna se propone como la buena.**

| vara candidata, sobre el campo `cobertura` | entradas |
|---|---:|
| V1 `N de N pares leidos; N en cola; N fuera de cola` | 555 |
| V2 `N ids` | 54 |
| V3 `N` a secas | 18 |
| V4 `N de N` | 569 |
| V5 `N ejemplar` o `N ejemplares` | 10 |
| V6 `puestos N a N, N pares leidos` | 6 |

**CAEN EN AL MENOS UNA: 657. NO CAEN EN NINGUNA: 15.** **Esa es la cifra que el
encargo pide, y va con su vara al lado**, porque un numero de agujero sin la vara
que lo mide no significa nada. Las 15 estan nombradas una a una en la salida: **4
de tipo `dominio` que dicen `SIN CRIBAR`, 10 de tipo `figura`** (entre ellas
`medio dominio exportacion`, `3 dominios medidos`, `15 reclasificadas`) **y 1 de
tipo `defecto`** que dice `4,2%, banda 0,7 a 20,2`.

**LA MISMA BUSQUEDA SOBRE EL FICHERO ENTERO, PUBLICADA AL LADO**, que es la
leccion de la `C.2` del acta 203: V3 da **18** sobre el campo y **0** sobre la
linea; V6 da **6** y **0**; V4 da **569** y **574**; V1 da **555** y **555**.
**Las dos columnas son ciertas y miden cosas distintas**, y por eso van las dos.

#### LA COINCIDENCIA QUE SALIO MEDIDA Y QUE SIRVE A QUIEN ESCRIBA LA VARA

**LAS 569 ENTRADAS QUE CAEN EN V4 SON EXACTAMENTE LAS 569 DE TIPO `acto` O
`racimo`**, o sea la poblacion que el paso 4 de `docs/plan/08_VERIFICACION.md`
nombra: **0 en V4 que no sean acto o racimo, 0 acto o racimo que no caigan en
V4**, comprobado por igualdad de conjuntos y no a ojo. Es la misma particion que
el `4.3` del acta 203 midio como **569 dentro del disparador y 103 fuera**. **El
agujero no esta repartido por el fichero: esta concentrado en las 103 de fuera**,
repartidas en 54 `familia_de_ids`, 20 `figura`, 19 `defecto` y 10 `dominio`. **Y
las 15 sin ninguna vara son un SUBCONJUNTO de esas 103, no una suma aparte:
comprobado, 15 de 15 estan fuera del disparador y 0 dentro.**

#### LA CLAUSULA 3, LA DE LOS HUECOS NOMBRADOS, MEDIDA IGUAL

**CADA BUSQUEDA DECLARA SU CAMPO, Y AHI ESTA LA MITAD DEL AGUJERO: la clausula no
dice en que campo se escribe el hueco.** `SIN CRIBAR` da **4** en `cobertura` y
**0** en `forma`, `estado` y `nota`. `hueco` da **114** en `nota` y **0** en los
otros tres. `nombrado` da **115** en `nota` y **0** en los otros tres. `HUECO` en
mayusculas da **5** en `nota`. **El literal que mas trae y el que menos difieren
en dos ordenes de magnitud sobre los mismos campos**, o sea que `hueco nombrado`
tampoco tiene forma comprobable.

#### LA CLAUSULA 2, LA DEL PROVISIONAL

`PROVISIONAL` da **1** en `forma`, **1** en `estado`, **1** en `nota` y **0** en
`cobertura`. **Y entradas cuyo campo `forma` sea EXACTAMENTE `PROVISIONAL`: 0**,
sobre **28** valores distintos de `forma`. **El agujero entero cabe en una
frase:** para comprobar *toda forma con cobertura incompleta va marcada
PROVISIONAL* haria falta saber que es `cobertura incompleta`, y `cobertura` es
texto libre con **23 formas distintas**, asi que **hoy no hay nada que
comparar**. **No es que la clausula se incumpla: es que no se puede medir**, que
es exactamente lo que el `4.3` del acta 203 adjudico.

#### LO QUE PROPONGO Y NO DECIDO, MARCADO COMO DISCUTIBLE

**`D.2` EL AGUJERO ES MAS PEQUENO DE LO QUE SU NOMBRE SUGIERE, Y ESO CAMBIA EL
COSTE DE LA VARA.** Con seis patrones sacados del propio campo, **657 de 672
entradas ya son comprobables a maquina y quedan 15**. Quien escriba la vara no se
enfrenta a 672 casos de texto libre sino a **una forma dominante de 554, dos
formas medianas de 53 y 18, y una cola de 15 que ninguna alcanza**. **NO ESCRIBO
LA VARA Y NO PROPONGO CUAL DE LAS SEIS ES**: dejo las cifras para que quien la
escriba sepa contra que.
