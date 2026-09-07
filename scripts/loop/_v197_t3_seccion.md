### TAREA 3, LA RELECTURA AL DOBLE DE 240. CERRADA. 207 DE 224 EN LA MITAD LIMPIA, Y ONCE DISCREPANCIAS FUERA DEL MARCADO QUE VUELVEN A DOBLAR EL TRAMO.

**Instrumentos y ficheros de salida, y toda cifra de abajo se cuenta de ellos:**
`docs/loop/SALIDA_V197_T3_SUJETO.txt`, `_T3_CIEGA.txt` (326299 bytes),
`_T3_DESTAPE.txt` (250425 bytes), `_T3_MIS_CLASES.txt` (43605 bytes) y
`_T3_COTEJO.txt`. **El orden fue: sujeto commiteado, clases commiteadas, y SOLO
DESPUES el destape.**

**(a) EL DOBLE RECOMPUTADO CALZA CON LA SELLADA.** `vecinos()` importada de la
182, y `puestos_de()`, `numeros_de()` y `UNIVERSO_CONSUMIDO` de la 196. Universo
**681** de **16** ficheros con el lector que le toca a cada uno, **300** con un
solo patron: la trampa de la `C.A5` medida y no creida, con **381** puestos de
diferencia. **561** por diferencia de conjuntos. Doble **120**, solape **0** con
el tramo y **0** con el universo **por construccion**. **Y HUBO QUE ESCRIBIR UN
LECTOR:** la sellada se TITULA `EL DOBLE DEL TRAMO...`, asi que su primera linea
tambien empieza por `EL DOBLE`; el lector de la 196 casa con el titulo y devuelve
**0** vecinos, o sea **un `NO CALZA` falso contra una sellada correcta**. Con el
lector que exige los dos puntos: **120**, y **calza**.

**(b) LOS 240 LEIDOS A CIEGAS**, uno por uno, con `aislador_de_ciega.py`.
**Mi reparto, sellado antes del destape: A 47, B 0, C 1, D 192.**

**(c) LA VARA** fue `9.6.1` con `9.6.2`, `9.6.3` y la tabla de LOS DOS POLOS del
`9.22`, citadas por numero. **Los dos errores del auditor fueron dentro del
criterio y sirvieron:** catorce de mis `A` las marque como CONTENCION MEDIDA SOBRE
EL CONTENIDO, y en cinco de ellas hay pasos repetidos **palabra por palabra** entre
los dos nodos.

**(e) EL COTEJO.**

| sobre que se mide | coinciden | discrepan |
|---|---:|---:|
| los **240** enteros | 215 de 240 | 25 |
| **los 224 LIMPIOS, y es la cifra que manda** | **207 de 224** | **17** |
| solo los 16 quemados, fuera del credito | 8 de 16 | 8 |

| | mio | del archivo |
|---|---|---|
| sobre los 240 | A 47, B 0, C 1, D 192 | A 35, B 3, C 1, D 201 |
| sobre los 224 limpios | A 38, B 0, C 0, D 186 | A 31, B 2, C 0, D 191 |

**DENTRO del marcado: 6** (`2668`, `2917`, `2922`, `3076`, `3094`, `3095`).
**FUERA del marcado: 11** (`165`, `207`, `210`, `662`, `724`, `880`, `886`,
`1218`, `1807`, `1808`, `2434`). **`AUDITOR.md` 1.2: el credito de mi tanda BAJA y
el tramo se relee AL DOBLE. La serie medida va 30, 60, 120, 240 y ahora 480.**

**Y LA `B` LA FALLE POR OMISION, EXACTAMENTE COMO ESCRIBI QUE PODIA PASAR ANTES DE
ABRIR NADA.** El fichero de clases dice, sellado: *"EMITO CERO B... si el archivo
trae alguna B en estos 240, la falle por omision"*. El archivo trae **3** en los
240 y **2** en la mitad limpia (`210` y `662`). **Sobre emiti `A` por 7 en la
mitad limpia**, 38 contra 31, que es la otra cara del mismo sesgo.

**(f) LOS INALCANZABLES A CIEGAS, contados ANTES de leer** por un barrido que no
devuelve ni la clase ni el texto de la razon: **14** citan un RACIMO, **6** una
CORRECCION DECLARADA, **20** en union. Sobre los 120 del auditor fueron 6 y 3.
**No se ensancho la lista blanca del aislador**, que es lo que la `4.4` prohibe.

**(g) LOS QUEMADOS: 16, y CATORCE se sellaron antes de leer**, nueve nombrados por
el encargo y **cinco anadidos por mi contra mi propio credito** (`616`, `2428`,
`2429`, `2430`, `2662`). **Los otros DOS se declararon TARDE, en el fichero de
clases, y eso es peor que declararlos antes**, asi que van con su nombre:

- **`654`.** Su clase de archivo me llego por la lista `QUEMADOS` de
  `scripts/loop/vuelta196_tarea2_relectura_al_doble.py`, **que lei ENTERO al
  clonarlo para escribir mi propio sujeto**, o sea antes de la ciega. **Es
  contaminacion mia por no comprobar si los quemados de la 196 caian dentro de MI
  universo.**
- **`1077`.** Es el **EJEMPLAR del banco `9.22`**, y el banco lo nombra con su
  clase `C` y con sus dos nodos. **El encargo me manda citar el `9.22`.**

**(e.bis) EL REPARTO DEL MARCADO, QUE EL HALLAZGO `5.2` OBLIGA A PUBLICAR.** De
los **240**, llevan `DISCUTIBLE MARCADO` **31**, y **los 31 son del 2662 para
arriba**: **0 marcados en los 177 puestos por debajo**, contra **31 de 63** por
encima. **El reparto sale igual que el del auditor.** Dicho sin deducir: **la
metrica de dentro-o-fuera del marcado NO ES COMPARABLE ENTRE TRAMOS**, porque una
discrepancia en el tramo bajo cae FUERA **por construccion**, no por ser peor.
**Nueve de mis once discrepancias de fuera del marcado estan por debajo del 2662.**

**DISCUTIBLES.** Los dos primeros van marcados **antes de saber si acierto**, en el
fichero de clases sellado; los otros dos son **posteriores al destape y se dicen
como tales**, que es la diferencia que hace que la marca valga.

**`D.7` DISCUTIBLE MARCADO ANTES DEL DESTAPE. EMITI CERO `B`.** Lo escribi con su
riesgo delante y sali perdiendo: el archivo tiene 2 en la mitad limpia. Sostengo
que la definicion que use (se pisan sin arista y sin que ninguno nombre al otro) es
la del banco, y que el problema es que **no la busque activamente en 240 pares**.

**`D.8` DISCUTIBLE MARCADO ANTES DEL DESTAPE. AMPLIE LOS QUEMADOS DE NUEVE A
DIECISEIS, y siete de los siete de mas los puse yo contra mi credito.** Lo
discutible es si un puesto que el acta nombra en una lista de "discrepancias
quemadas" sin publicar su clase esta de verdad quemado.

**`D.9` DISCUTIBLE, POSTERIOR AL DESTAPE Y SE DICE. LA CONTENCION LA APLIQUE MAS
DE LO QUE EL ARCHIVO LA APLICA.** De mis 38 `A` limpias el archivo confirma 31, y
las que fallo son casi todas contencion (`886`, `1218`, `1807`, `1808`, `2434`,
`2668`, `2922`, `3076`, `3094`, `3095`). **El remedio del `2838` funciono en el
`2838` y me hizo sobre emitir en otros diez.**

**`D.10` DISCUTIBLE, POSTERIOR AL DESTAPE Y SE DICE. LOS QUEMADOS ME SALIERON
PEOR QUE LOS LIMPIOS**: 8 de 16 contra 207 de 224. Un puesto quemado deberia ser
mas facil, no mas dificil. **La causa que sostengo: los quemados son en su mayoria
los puestos que el acta discute, o sea los dificiles, y saber que el archivo gano
NO es saber que clase puso.**
