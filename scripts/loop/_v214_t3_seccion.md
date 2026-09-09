### TAREA 3. LA VUELTA 215, PREPARADA, Y DOS TRAMPAS MEDIDAS QUE LE ESPERAN

**DONDE VA ESTA PROPUESTA Y POR QUE NO EN OTRO SITIO.**
`docs/loop/PROMPT_SIGUIENTE.md`, `docs/loop/ACTA_AUDITOR.md` y
y el PARA_ALEXIS.md que vive junto a ellos **son sede del auditor y el ejecutor
no los escribe**;
si cree que el encargo siguiente deberia decir otra cosa, **lo propone en su
reporte, que es su sede**. Adjudicacion `4.2` del acta 203, leida hoy en la
**linea 71543** de `docs/loop/ACTA_AUDITOR.md`, y **ratificada por el fundador**
en su decision del 9 sep 2026. **Por eso esta tarea no escribe una sola linea
fuera de este reporte.**

#### 3.a LA BATERIA: EL REPARTO SE COMPUTA, Y NO DA NUEVE

**Corrido por mi en esta vuelta con el carril `--plan`, que NO toca la nomina, NO
corre ningun arnes y NO escribe ninguna salida de bateria.** Salida:
`docs/loop/SALIDA_V214_T3_PLAN_BATERIA.txt`.

| que | cuanto |
|---|---:|
| entradas de la nomina | **135** |
| tamano de tramo | **13** |
| **tramos que el reparto da** | **11** |
| suma de las entradas de todos los tramos | **135** |

**LA NOMINA CALZA CON LA MORATORIA: 135, CONGELADA**, y la suma de los
tramos reproduce esa misma cifra, o sea que el reparto cuadra consigo mismo.

**PARADA 1: EL ENCARGO Y `AUDITOR.md` 6.1 DICEN NUEVE, Y EL INSTRUMENTO CUENTA
11.** No lo arreglo yo (`EJECUTOR.md` 5: se escribe como PARADA y no se
repara). **La letra vigente dice, con estas palabras, que la bateria SE DECLARA
CORRIDA CUANDO LOS NUEVE TRAMOS TIENEN SALIDA SELLADA DEL MISMO CALIBRE.** El
**NUEVE** era cierto en su corte, cuando la nomina era menor; **con la nomina
congelada en 135 el reparto da 11**, y **la practica ya se movio
sin que la letra la siguiera**: la ultima bateria, la de la **vuelta 210**,
corrio **11** tramos y sus propios commits lo dicen. **Si la 215 se cine a
la letra y para en nueve, deja DOS TRAMOS sin correr y declara corrida una bateria
que no lo esta.** La cifra que manda es la que el instrumento computa, pero
**cambiar la letra de `AUDITOR.md` no es mio**: lo subo.

**PARADA 2, Y ES LA QUE DE VERDAD PUEDE FABRICAR UN FALSO VERDE: EL CARRIL
`--siguiente` DICE HOY QUE NO FALTA NINGUN TRAMO.** Corrido por mi, salida en
`docs/loop/SALIDA_V214_T3_SIGUIENTE.txt`:

- **tramos del reparto: 11**
- **tramos CON salida sellada no vacia: 11**
- **tramos que FALTAN: 0**

**Y no es que la bateria de la 215 este hecha: es que las salidas que ese carril
mira son las de la vuelta 210 y siguen en el arbol.** El motivo,
medido y no supuesto: **el lanzador nombra sus salidas con el numero que computa
de SU PROPIO fichero**, que es el **183**, no con el de la vuelta que lo corre.
Asi que `SALIDA_V183_BATERIA_TRAMO_N.txt` es el mismo nombre para toda corrida, y
**ni `--siguiente` ni `--componer` pueden distinguir una corrida fresca de la
anterior**. Lo comprobe en el propio `componer()`: cotejea **cobertura** (que
ninguna entrada de la nomina se quede sin correr, que no sobre ninguna y que no
se repita) y **que ninguna salida mida cero bytes**, pero **no mira la fecha ni el
commit de los sellos**.

**LOS ONCE SELLOS QUE HOY VE ESE CARRIL, CON SU CABECERA Y SU COMMIT, LEIDOS POR
MI:**

| tramo | cabecera de la salida, leida de su primera linea | ultimo commit que la toco | bytes |
|---:|---|---|---:|
| 1 | CORRIDA DEL TRAMO 1 DE 11, BATERIA DE LA VUELTA 183 | `ca702058 2026-09-08` | 9544 |
| 2 | CORRIDA DEL TRAMO 2 DE 11, BATERIA DE LA VUELTA 183 | `4895fb06 2026-09-08` | 7795 |
| 3 | CORRIDA DEL TRAMO 3 DE 11, BATERIA DE LA VUELTA 183 | `3fa5b035 2026-09-08` | 8050 |
| 4 | CORRIDA DEL TRAMO 4 DE 11, BATERIA DE LA VUELTA 183 | `a9a8fff9 2026-09-08` | 7862 |
| 5 | CORRIDA DEL TRAMO 5 DE 11, BATERIA DE LA VUELTA 183 | `274a0aed 2026-09-08` | 8274 |
| 6 | CORRIDA DEL TRAMO 6 DE 11, BATERIA DE LA VUELTA 183 | `fc68e550 2026-09-08` | 8205 |
| 7 | CORRIDA DEL TRAMO 7 DE 11, BATERIA DE LA VUELTA 183 | `3d79c288 2026-09-08` | 7893 |
| 8 | CORRIDA DEL TRAMO 8 DE 11, BATERIA DE LA VUELTA 183 | `97185bc4 2026-09-08` | 7848 |
| 9 | CORRIDA DEL TRAMO 9 DE 11, BATERIA DE LA VUELTA 183 | `ed74786d 2026-09-08` | 8525 |
| 10 | CORRIDA DEL TRAMO 10 DE 11, BATERIA DE LA VUELTA 183 | `08e9acdd 2026-09-08` | 8472 |
| 11 | CORRIDA DEL TRAMO 11 DE 11, BATERIA DE LA VUELTA 183 | `7dfbfdf7 2026-09-08` | 6273 |

**LO QUE PROPONGO, Y ES BARATO:** que la 215 **NO use `--siguiente` como senal de
arranque**, y corra **`--tramo 1` a `--tramo 11` uno a uno**, cada uno
**commiteado con su salida sellada al terminar**, que es lo que la letra manda de
todas formas; y que **antes de empezar publique el commit de los sellos viejos**,
para que la corrida nueva se distinga de la de la vuelta 210 en el
propio reporte. **`--componer` va al final y es el que coteja el calibre.**
**No propongo tocar el lanzador: rige la moratoria.**

#### 3.b EL CIERRE INTEGRAL, CON SUS INSTRUMENTOS COMPROBADOS UNO A UNO

**Todo lo que la `3.b` del encargo pide es SIN CREDENCIAL y tiene instrumento
vivo. Comprobados hoy, existencia y bytes, porque una ruta que promete prueba es
cifra:**

| que pide el encargo | instrumento | existe |
|---|---|---|
| el ciclo entero de Gate 0, los ocho comandos | `scripts/loop/_v205_ciclo_gate0.py` | **SI**, 4359 bytes en disco y 4359 bytes normalizados a LF |
| la bateria por tramos | `scripts/loop/vuelta183_bateria_por_tramos.py` | **SI**, 35327 bytes en disco y 35327 bytes normalizados a LF |
| la vara del trabajo pendiente | `scripts/loop/vuelta150_3_relectura_expediente.py` | **SI**, 60262 bytes en disco y 60262 bytes normalizados a LF |
| el inventario de las 71 contra sus pruebas | `scripts/loop/_v213_t2_cierre_fase_iii.py` | **SI**, 16687 bytes en disco y 16687 bytes normalizados a LF |
| el marcador y el censo, recomputados | `scripts/loop/vuelta159_tarea9_marcador_cierre.py` | **SI**, 7948 bytes en disco y 7948 bytes normalizados a LF |
| las tres suites, dentro del ciclo de Gate 0 | `engine/run_all_tests.py` | **SI**, 2535 bytes en disco y 2457 bytes normalizados a LF |
| el cierre del reporte | `scripts/loop/cerrar_reporte.py` | **SI**, 114466 bytes en disco y 114466 bytes normalizados a LF |
| el tallador de la cabecera | `scripts/loop/tallar_cabecera_reporte.py` | **SI**, 100077 bytes en disco y 100077 bytes normalizados a LF |
| el barrido de rutas del reporte | `scripts/loop/vuelta186_rutas_del_reporte.py` | **SI**, 5887 bytes en disco y 5887 bytes normalizados a LF |

**CIFRA instrumentos comprobados: 9 | CIFRA ausentes o de cero bytes:
0.**

**EL ORDEN QUE PROPONGO, y el motivo de cada sitio:** la **bateria primero y
sola**, porque `AUDITOR.md` 6.1 dice que su vuelta **no lleva nada mas** y porque
es lo que lleva vueltas cayendose; el **cierre integral despues**, con el ciclo
entero de Gate 0 **en sus dos lados**, las tres suites (que ya van dentro de ese
ciclo, comandos 7, 8a y 8b), el **inventario de las 71 contra sus pruebas** y el
**marcador y el censo recomputados**. **La vara del expediente se corre con el
reloj de git congelado en el HEAD de apertura de la 215**, no en un ancestro.

#### 3.c LA `PARA_ALEXIS.md`: SU CONDICION, Y QUIEN LA ESCRIBE

**LA CONDICION, ESCRITA ANTES DE SABER SI SE CUMPLE:** la 215 escribe la parada
de **campaña consumada** **solo si** los **11** tramos de la bateria
tienen salida sellada **fresca** y del mismo calibre, el ciclo entero de Gate 0
sale en **peor exitcode 0 por los dos lados**, las tres suites salen verdes, el
inventario de las 71 cuadra contra sus pruebas y el marcador y el censo
recomputados calzan. **Si algo no da verde, se dice CUAL y la 215 NO escribe esa
parada**, tal como el encargo ordena.

**Y EN ESA PARADA VA DECLARADO QUE LA AUDITORIA INTEGRAL CON CREDENCIAL Y CON EL
FUNDADOR DELANTE ES EL PASO SIGUIENTE. NO SE PIDE EL MERGE: el merge es del
fundador y viene despues de esa auditoria.** El bucle no funde ramas.

**UNA PRECISION QUE NO ES MENOR, Y LA DIGO PORQUE ME TOCA A MI DECIRLA:
`PARA_ALEXIS.md` ES SEDE DEL AUDITOR.** Cuando el encargo dice *"la 215 escribe
el `PARA_ALEXIS.md`"*, quien lo escribe es **el auditor de la 215**, no su
ejecutor. **El ejecutor de la 215 lo PROPONE en su reporte**, igual que yo estoy
proponiendo esto aqui. Si el ejecutor de la 215 lo escribiera, romperia la misma
adjudicacion `4.2` que el fundador acaba de ratificar.

**Y LO QUE LA 215 NO PUEDE DECLARAR CONSUMADO SIN MIRARLO, PORQUE ESTA VUELTA LO
DEJA ABIERTO:** los **puntos 3 y 4 de `OP-I-01` siguen en A MEDIAS** (TAREA 1), y
las **dos discrepancias de la `2.b`**, el marcador contra su cifra vieja y la
cifra once, **siguen sin doctrina que las resuelva**. **Ninguna de las tres es NO
CUBRE y ninguna la levanta el bucle por su cuenta, pero una parada de campaña
consumada que no las nombre estaria consumando por encima de ellas.**
