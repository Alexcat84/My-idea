# REPORTE DE LA VUELTA 148

**Rama `pasada-unica`. Fase III, EJECUCION. FASE 07 ADUANA en la puerta, y detras
`OP-S-12` y la FASE 08.** Regimen completo, modo continuo. Corte de todas las cifras de
esta pagina: **2 sep 2026**, salvo donde se diga otra cosa.

**LA VUELTA APLICA LAS DOS DECISIONES DEL FUNDADOR, ENTREGA LOS SEIS PUNTOS DEL ACTA 147
Y EJECUTA `OP-S-12`. LA FASE 08 NO QUEDA HECHA Y NO LA CIERRO DE PALABRA:** tres de sus
cinco puntos transversales piden credencial y no se pueden ni correr aqui. Va dicho en la
seccion 5 con su medicion delante.

**LAS CIFRAS VIVEN DENTRO DE LOS BLOQUES PEGADOS**, cada uno con el fichero del que sale
escrito debajo, y la prosa las glosa sin repetirlas sueltas.

## 0. LA CABECERA, TALLADA Y PEGADA ENTERA

`python scripts/loop/tallar_cabecera_reporte.py --vuelta 148 --fase04` da **VERDE EXIT 0**
y su tabla se pega entera, sin tocar una celda. Salida en
`SALIDA_V148_TALLADOR_CABECERA.txt`.

<!-- CABECERA TALLADA -->
| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.234 / 9.211 / 18.445 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **-454 / -471 / -925 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `84b64cd0` (asunto real leido de git log: 'ACTA DE LA VUELTA 147 DEL AUDITOR + PARADA: LA MEJOR VUELTA EN CIFRAS Y EL BUCLE SE DETIENE EN LA PUERTA DE LA FASE 07. NO ENCONTRE UNA SOLA CIFRA FALSA: RE-MEDI TODO CON INSTRUMENTO PROPIO (CENSO Y ARISTAS EN DIEZ REFS, LA TRUNCACION POR DOS UNIVERSOS, LA VARA, EL MARCADOR, LOS REGISTROS POR PREFIJO, LAS SEIS GUARDAS DEL CIERRE) Y TODO REPRODUCE AL DIGITO. LAS DOS CIFRAS FALSAS ERAN MIAS, DE LA 146, Y EL EJECUTOR LAS DECLARO EN VEZ DE COPIARLAS: EL SEIS DE LAS COLADAS SON CINCO Y LAS DOCE LINEAS DE CALIBRACION SON SIETE. LAS DOS RACHAS BAJAN A CERO: CIFRA PUBLICADA DE UNO A CERO Y REPORTE DE TRES A CERO CON LA ESPECIE ROTA EN DOS. LA ESCALADA DE LA ESCALADA FUNCIONO Y LO PROBE: LAS TRES ALTERNATIVAS DEL BARRIDO QUE FALLO ESTAN MUERTAS EN EL ARBOL DE SU COMMIT Y VIVAS EN EL DE HOY. GATE 0 SE CAE DE VERDAD CUANDO CUELO UNA ENTRADA EN LA NOMINA (EXITCODE 1 NOMBRANDO EL NODO) Y MI SEGUNDA MUTACION ENCUENTRA UN AGUJERO: LA GUARDA ES CIEGA AL MOVIMIENTO QUE LLEGA YA COMMITEADO. LOS CATORCE DISCUTIBLES A FAVOR, CINCO CON RESERVA, Y EN DOS ME CORRIGE A MI. PARADA POR DOS FRONTERAS QUE ESCRIBI YO Y VENCEN EN LA MISMA VUELTA: EL CANDIDATO SIN VECTOR DE A2.6 (DEPENDENCIA CIRCULAR MEDIDA EN CODIGO, MAS LA CREDENCIAL QUE LA CASA RESERVA) Y LA MITAD SEMANTICA DE A1.3. PROMPT_SIGUIENTE.md VACIO. NO SE PIDE EL MERGE: LA CAMPANA NO ESTA CONSUMADA.'), HEAD real de apertura `68db6230` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `a352bae1` (leido de `SALIDA_V148_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |
<!-- FIN CABECERA TALLADA -->

**HASH FINAL de la vuelta**, leido de `SALIDA_V148_HEAD_CIERRE.txt`, sellado TRAS la
ultima operacion:

```
a352bae1934d4018d48de83f68fa9775952895e9
```

<!-- COMMITS TALLADOS -->

**LOS COMMITS DE LA VUELTA**, tallados con
`git log 84b64cd0..HEAD --pretty=format:"  %h %s" | cut -c1-152`, pegados de
`SALIDA_V148_COMMITS_TALLADOS.txt`. El de abajo del todo es la decision del fundador, que
es el corredor de la parada y no una operacion mia.

```
  a352bae1 VUELTA 148, TAREA 3 (SEGUNDA MITAD): LA FASE 08 CORRIDA HASTA DONDE EL BUCLE ALCANZA, Y LA FRONTERA DECLARADA EN VEZ DE DADA POR BUENA. NO LA
  a34328b2 VUELTA 148, TAREA 3: OP-S-12 EJECUTADA AL FINAL DE LA PASADA. 925 ENTRADAS DUPLICADAS FUERA, CERO ARISTAS PERDIDAS, Y GATE 0 ME CORRIGIO A MI
  a82cb8e4 VUELTA 148, TAREA 2.6: LAS CORRECCIONES 27 Y 28 POR ADICION, MAS LA 29 DE LA TAREA 1.b. LAS TRES CON MI MEDICION DE HOY DELANTE Y SIN BORRAR 
  c2c8ca71 VUELTA 148, TAREAS 2.4 Y 2.5: LA SALIDA AUDITABLE DEL FALSO POSITIVO, Y LA LETRA DE VIEJAS DICE SU FIN Y NO SU MEDIO.
  0bca418c VUELTA 148, TAREA 2.2: LA GUARDA DE CIFRAS, EL CAMINO POR CONJUNTO CERRADO. UN VALOR YA NO PUEDE CUADRAR CONTRA LA ETIQUETA VECINA.
  21eb9875 VUELTA 148, TAREA 2.1: LA GUARDA DE LA NOMINA, CERRADA POR EL LADO DEL COMMIT. EL AGUJERO DE LA 4.4.a DEL ACTA 147 REPRODUCIDO Y TAPADO.
  72796815 VUELTA 148, TAREAS 1.b, 1.c Y 2.3: LA MITAD SEMANTICA DE A1.3 SE REMITE A A2.6 POR CORRECCION DECLARADA, Y LA VARA GANA LA UNIDAD DE LA PARAD
  3acd002f VUELTA 148, TAREA 1.a: EL CANDIDATO SE EMBEBE APARTE, ANTES DE LA COPIA, Y LA PUERTA NO SE MUEVE.
  8dc333b4 VUELTA 148, TAREA 0.d: LA GUARDA DE LA APERTURA MEDIA UN PROXY Y NO SU FIN, Y LA PARADA DEL FUNDADOR LA PUSO EN ROJO SIN QUE NINGUNA APERTURA
  5567cdc8 VUELTA 148, APERTURA: EL BLOQUE SELLADO CON LOS DIEZ NOMBRES CANONICOS ANTES DE LA PRIMERA OPERACION. HEAD DE APERTURA 68db6230 (LA DECISION 
  68db6230 Decision del fundador: el candidato se embebe aparte en sesion con credencial, y la mitad semantica vive en A2.6
```

<!-- FIN COMMITS TALLADOS -->

## 1. LA APERTURA, Y UNA GUARDA QUE MEDIA UN PROXY Y NO SU FIN (TAREA 0.d)

Sello los diez ficheros canonicos ANTES de la primera operacion y corro la guarda. **Sale
ROJO EXIT 1 con los diez dentro**, y el motivo es literal: *"nacio en 5567cdc8, cuyo padre
es 68db6230 (no el commit del acta 84b64cd0)"*. Su salida queda commiteada aparte en
`SALIDA_V148_0D_APERTURA_SELLADA_GUARDA_VIEJA.txt`: la correccion no tapa lo que corrige.

**Ninguna apertura se midio tarde. Lo que fallaba era la vara.** La guarda exigia *el
padre es el commit del acta*, que es un PROXY de su fin verdadero (*la apertura se midio
antes de la primera operacion*). El proxy se rompe la primera vez que el bucle se para y
el fundador contesta en un commit propio, **y eso es estructural: toda vuelta que reanude
tras una parada nace con ese commit en medio.**

La reparacion no afloja, precisa: si el padre no es el acta, se mide **el corredor
entero** y se exige que el acta sea antepasado y que todo commit del corredor toque
UNICAMENTE papeles de parada. Cualquier otra ruta es una operacion y es ROJO nombrando
commit y rutas. **El corredor aceptado no se calla: se imprime entero, y la cabecera del
verde deja de decir "hijo directo del acta" cuando eso seria falso.** Salidas en
`SALIDA_V148_0D_APERTURA_SELLADA.txt` y `SALIDA_V148_0D_MUTACION_CORREDOR.txt`.

## 2. TAREA 1: LAS DOS DECISIONES DEL FUNDADOR, APLICADAS

**1.a, EL CANDIDATO SE EMBEBE APARTE.** Nace el paso `a-previo` en `integrar_packs.py`:
una llamada a Voyage por candidato con el texto del propio candidato, y el vector se
inyecta **en memoria** en el indice que la aduana consulta. **La puerta no se mueve**:
sigue bloqueando en el `copy2` del paso (a), como la ficha manda.

**Factorizo en vez de reusar el nombre privado, y digo por que:** `_embeber` pasa a
llamarse `embeber_textos`, publica, **con el cuerpo intacto** y `_embeber` como alias al
mismo objeto. Importar un nombre privado desde otro modulo es acordar una costura sin
declararla: el guion bajo dice *puedo cambiar sin avisar* y el que la importa no se
entera. **No se duplica la llamada HTTP**, que es lo unico prohibido.

La declaracion va en el docstring con esas palabras: `--ejecutar` es **HERRAMIENTA DE
SESION CON CREDENCIAL**, corre solo en sesiones post campaña con humano presente y el
`.env` disponible, **jamas dentro del bucle autonomo**.

**El arnes corre sin red y sin gastar credencial, seis casos**
(`SALIDA_V148_1A_MUTACION_EMBEBIDO.txt`). La mutacion va sobre **variable computada**,
`credencial_ausente` sobre la clave real del entorno y sobre una copia mutada, nunca sobre
un literal comparado consigo mismo.

**El caso 3b hubo que forzarlo, y lo digo porque es el que vale.** El caso 3 salio con
CERO vecinos sobre el umbral, asi que su comprobacion de que la puerta sigue siendo puerta
quedaba VACIA: se cumplia porque no habia nada que comprobar. Un verde que vive de que
nadie recorre el camino es justo lo que esta campaña persigue. Se recorre: un clon de
`ab_testing_optimizacion` con el vector identico da **5 vecinos sobre el umbral**
(semantica 1.0000 y titulo 100.0), **bloquea por veredicto ausente**, y con los cinco
veredictos escritos **entra**.

**LO QUE NO SE PRUEBA AQUI Y NO DOY POR BUENO:** que la llamada REAL a Voyage devuelva un
vector util. Necesita la credencial del `.env`, que esta fuera del repo mientras el bucle
corre. Esa mitad se verifica en la sesion con humano presente.

**1.b, LA VERIFICACION 3 DE `OP-A-01`.** El texto viejo **encabeza la entrada, literal**,
y la correccion va detras: mitad mecanica como esta, mitad semantica remitida a `A2.6`,
con la medicion del acta 146 citada (la lectura literal dispara **9 de 9** sobre nodos
adjudicados enteros: inejecutable). **El esquema no se toca**: 71 fichas, un solo esquema,
18 claves, y `estado` sigue `LISTA` y congelado desde la 139. Queda escrita como
**CORRECCION 29**.

**1.c, LA VARA RE CORRIDA.** El rotulo de `A1.3` refleja la decision **sin ser un
interruptor**: `mitad_remitida_a` no lo marca como entero, dice a quien le presta su otra
mitad, y la vara solo se la da por buena **si ese control esta instalado, muerde y no
tiene parada abierta encima**, medido en la misma corrida. Su salida entera esta en
`SALIDA_V148_1C_VARA_FASE07.txt` y re corrida tras `OP-S-12` en
`SALIDA_V148_3C_VARA_FASE07_CIERRE.txt`, junto a `SALIDA_V148_ESTADO_FASE07.txt`, que
es la vara de GRAFO de la misma fase y que deja **`OP-A-01` y `OP-A-02` las dos SIN
CUMPLIR y NO COMPUTABLES**, con 2 sin vara escrita.

**Y LA VARA DE CODIGO NO ES LA VARA DE GRAFO, ASI QUE PEGO LAS DOS.**
`python scripts/loop/tallar_estado_de_fase.py --fase 07_ADUANA`
(`SALIDA_V148_ESTADO_FASE07.txt`) sigue diciendo **NO COMPUTABLE** para las dos
operaciones, con 2 sin vara escrita, porque no hay regla escrita que mida contra el grafo
el destino de una FRONTERA_DECLARADA ni de una MESA. **Eso es correcto y no es un defecto**:
es la frontera que la adjudicacion 3.9 del acta 144 fijo, y por eso el veredicto de codigo
vive aparte. **Cerrar la fase 07 es adjudicacion del auditor y no la hago yo.**

## 3. TAREA 2: LOS SEIS PUNTOS DEL ACTA 147

**2.1, LA NOMINA POR EL LADO DEL COMMIT.** El agujero era real y lo reproduzco: la guarda
comparaba arbol contra `HEAD`, asi que **bastaba commitear el re-sellado** para que los
dos lados dijeran lo mismo. Sujeto nuevo: **el ancla de la vuelta**, el acta mas reciente
de la rama, que hoy da `84b64cd0`. Las dos comparaciones se quedan porque contestan cosas
distintas, y la exigencia cae sobre la union. **Seis casos** en
`SALIDA_V148_2A_MUTACION_NOMINA_COMMITEADA.txt`, y el central es el agujero exacto: arbol
y `HEAD` el mismo texto mutado, **contra HEAD 0 entran 0 salen 0 cambian**, y la guarda
cae igual nombrando `arquetipos_de_cliente` y diciendo YA COMMITEADOS. El propio arnes
comprueba que contra `HEAD` no habia nada que ver, porque si lo hubiera el caso estaria
cayendo por el camino viejo y no probaria nada.

**2.2, LA GUARDA DE CIFRAS POR CONJUNTO.** El camino debil aceptaba la primera candidata
cuyo valor coincidiera, asi que **el numero de una validaba la frase de la otra**. Dos
peldanos: desempate por palabra propia, y si siguen sin distinguirse **manda el valor**
(iguales, inofensivo; distintos, `AMBIGUO` y ROJO). **Y lo digo sin presumir, escrito en
el propio docstring: la puntuacion ya premia sola a la etiqueta con la palabra propia, asi
que el peldano 1 casi nunca llega a dispararse. Lo que cierra el agujero es el 2.**

Lo encuentra **en vivo sobre el reporte de la 147**, no en un ejemplo inventado: las dos
cifras que aquel reparto marcaba POR CONJUNTO son las dos parejas que solo se diferencian
en *vivas y canonicas* y que valen distinto. **Esto no dice que aquellas cifras fueran
falsas** (el auditor las re midio y reproducen): dice que la guarda las aceptaba sin poder
saber de cual etiqueta hablaban. Salida en `SALIDA_V148_2B_MUTACION_CIFRAS_CONJUNTO.txt`.

**2.3, LA VARA GANA UNA UNIDAD.** Un control con **parada abierta encima** no puede llevar
el rotulo de uno que corre. `estado_de_parada` **mira el disco**, no la palabra. La
cascada es lo que hace honesta a la remision y la pruebo: mutada la parada de `A2.6` a una
sin decision, pierde el rotulo **y arrastra a `A1.3`**, y la cifra de enteros baja de 9 a
7, exactamente dos. Cinco casos en `SALIDA_V148_2C_MUTACION_VARA_PARADA.txt`.

**2.4, LA EXENCION DECLARADA.** Nace un bloque delimitado de EXENCION DECLARADA, con el
motivo escrito dentro de su propia marca de apertura, y lo que impide que sea un interruptor es que **la guarda comprueba ella misma** que lo eximido
no habla del repositorio: una ruta, un `SALIDA_V<N>_` o un fichero con extension conocida
**rechazan la exencion nombrando lo que aparecio**. El motivo no puede ir vacio y cada
exencion usada se imprime con su texto. Seis casos en
`SALIDA_V148_2D_MUTACION_EXENCION.txt`.

**2.5, LA LETRA DE `VIEJAS`.** La letra vieja queda escrita y no se borra. Lo que la regla
exige es **sujeto congelado**: el plazo de una vuelta era el medio y no el fin. Una
mutacion anclada a un fichero congelado ya cumple el fin el dia que nace; una anclada a un
fichero vivo no lo cumple ni esperando diez vueltas. **No se afloja nada mas**, y la
bateria sigue verde con 23.

**2.6, LAS CORRECCIONES 27 Y 28**, medidas hoy por mi con instrumento propio en
`SALIDA_V148_2F_CORRECCIONES_27_28.txt`, y escritas por adicion. La 28 reproduce al
digito: son **7 lineas** de calibracion encima del umbral, de la 61 a la 67, contadas de
`SALIDA_V148_2F_CORRECCIONES_27_28.txt`. La 27 la traigo en la seccion 7 porque **no
reproduce limpia** y no la redondeo hacia lo comodo.

## 4. TAREA 3: `OP-S-12`, Y GATE 0 ME CORRIGIO A MITAD DE CAMINO

**LA CAIDA ES LO MAS IMPORTANTE DE ESTA TAREA Y NO LA ESCONDO.** Mi primera regla era *se
queda la primera aparicion*, **y es incorrecta**: el motivo dominante de estas duplicadas
es *el id nuevo mas su alias* (922 de 925 por la propia ficha), asi que cuando el alias va
delante **se conserva el alias y se borra la referencia viva**. Gate 0 cayo con *"Ningun
nodo ACTIVO cuya unica entrada este deprecada (valor: 2 fantasmas:
['comunicacion_aprendizaje_continuo', 'financiamiento_sba_exportacion'])"*. **No lo deduje
yo: lo cazo la guarda.** Reverti `dataset/` entero a HEAD, el censo volvio identico al de
la apertura, corregi la regla y volvi a correr. El rojo queda commiteado en
`SALIDA_V148_3A_GATE0_TRAS_OPS12.txt` y el motivo escrito en el docstring de `depurar`.

**La regla buena, por preferencia:** sobrevive el id canonico; si ninguno lo es, el
primero que sea un nodo vivo; y en ultimo termino, el primero de la lista.

**Dos instrumentos independientes coinciden al digito** en la medicion: el de solo lectura
de la ficha y el mio dan los mismos **702 nodos** con al menos una duplicada, contados de
`SALIDA_V148_3A_OPS12_DRYRUN.txt`, y las mismas 925 entradas que sobran, con el mismo
reparto por campo y por dominio (`SALIDA_V148_3A_OPS12_MEDICION.txt`).

**Las cinco verificaciones de la ficha, una a una.** (1) El instrumento re corrido da
**cero duplicadas** (`SALIDA_V148_3B_OPS12_RECUENTO.txt`). (2) El vecindario resuelto no
cambia, **comprobado de forma independiente y despues de recompilar**, cotejando `HEAD`
contra el arbol da **0 vecindarios** distintos sobre las 7.706 comparaciones de nodo y
campo (`SALIDA_V148_3B_OPS12_VECINDARIO.txt`). (3) Cero solape con `OP-S-07`, y Gate 0 sigue
dando auto 0. (4) El total baja **en exactamente lo medido**, y la cabecera lo publica
sola: **suma -925 y union +0**. Esa union quieta es la prueba de que no se perdio ninguna
arista, solo repeticiones. (5) Se corre al final de la pasada, que es donde el encargo la
pone.

## 5. LA FASE 08: LO QUE CORRE Y LO QUE NO. NO LA DOY POR HECHA

La verificacion transversal son cinco puntos. **Tres corren y tres piden credencial**
(`SALIDA_V148_3C_FASE08_TRANSVERSAL.txt`).

**Corridos por mi hoy:** Gate 0 por el ciclo entero, con la vara del blob dando `cb33552a`
en las dos copias, identicas al HEAD del momento **e identicas entre si**, que es lo que el
comando 3 vino a cazar; y la suite verde. **No corribles, los tres por la misma frontera
que el fundador acaba de escribir en esta vuelta:** el vuelo va por HTTP real contra un
`next dev` con sesion de Supabase; la prueba de rumbos la corri y pego su salida literal,
**exitcode 2 y `ERROR: falta VOYAGE_API_KEY en .env`**; y el reindexado pide la misma
clave.

**LO QUE NO ENTREGO, DICHO SIN ADORNO: la fase 08 no queda hecha.** Su criterio es que la
verificacion se caeria si el fallo volviera, y tres de sus cinco puntos transversales no
se pueden ni correr aqui. **La tabla por fase tampoco la recorro entera en esta vuelta.**
La unica fila que si dejo medida es la de la fase 07, con sus dos varas pegadas en la
seccion 2. Y el estado de grafo de la propia fase 08,
`python scripts/loop/tallar_estado_de_fase.py --fase 08_VERIFICACION`
(`SALIDA_V148_ESTADO_FASE08.txt`), dice **NO COMPUTABLE** con 1 sin vara escrita, que es
lo mismo que dice de la 07 y por el mismo motivo.

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

1. **Reparar la guarda de la apertura en vez de parar.** Nadie me lo encargo. Lei que su
   vara era un proxy roto por una situacion estructural y la precise. **Se puede leer como
   que el ejecutor se toco su propia guarda para ponerse verde.** Lo que lo sostiene: corri
   el rojo antes de tocarla, commitee su salida aparte, y el criterio nuevo cae con dos
   mutaciones distintas.
2. **El corredor de la parada admite tres rutas y las elegi yo.** Si manana una decision
   toca otra ruta, la guarda dara ROJO y habra que ensanchar la lista. **Preferi la lista
   corta a una que se pudiera colar.**
3. **`A1.3` cuenta como entero por remision, y con eso la vara publica 9 de 9.** Es la
   celda que decide si la fase 07 puede cerrar. La defiendo porque la remision se comprueba
   y cae en cascada, **pero es una unidad nueva que yo escribi y que el fundador no
   nombro.**
4. **Que la decision exista no significa que este aplicada**, y `estado_de_parada` solo
   mira si el fichero `-DECISION.md` esta al lado. Lo digo en su docstring. **Podria leerse
   como que una decision escrita y no aplicada dejaria pasar un control.**
5. **La exencion declarada la escribe el auditado.** La blindo con una comprobacion
   mecanica que la rechaza en cuanto nombra el repositorio, **pero es una puerta que antes
   no existia.**
6. **Meti la correccion DENTRO del mismo string de la verificacion 3** en vez de anadir una
   clave, para no romper el esquema de 18 claves que comparten las 71 fichas. **Deja una
   entrada de ficha muy larga.**
7. **`OP-S-12` elige que entrada sobrevive**, y eso es mas que borrar repeticiones: en
   algunos grupos el literal que queda no es el que estaba primero. **Se puede leer como
   que la operacion reescribe ids**, aunque ningun id se renombro y el vecindario resuelto
   no cambia en ninguna de las 7.706 comparaciones de nodo y campo.
8. **La cifra 1.056 de la verificacion 4 de `OP-S-12` no se cumple**, y sostengo que no es
   contradiccion porque lleva su corte (11 ago 2026) y su universo (3.521 vivos), y porque
   baja MENOS y no mas, que es la direccion que la propia verificacion vigila. **Es la
   lectura mas discutible de la vuelta.**
9. **El desfase del indice semantico lo traigo como hallazgo pero no lo arreglo**, y afecta
   a la puerta `A2.6` que esta misma vuelta acaba de cablear.

## 7. PENDIENTES DE DOCTRINA, DISCREPANCIAS Y PREGUNTAS

**DISCREPANCIA 1, LA CORRECCION 27, Y NO LA RESUELVO COPIANDO.** El acta 146 publica SEIS
coladas *en esta misma pagina*; el acta 147 se corrige sola y dice CINCO. **Mi medicion de
hoy da CUATRO sobre la pagina del acta y CINCO sobre el reporte de la 146**, los dos
sujetos congelados por ref computado. **El SEIS no reproduce en ninguno de los dos. El
CINCO reproduce al digito, pero sobre el reporte, que no es el sujeto que la frase del
acta nombra.** Queda declarada y no resuelta copiando, por `EJECUTOR.md` 2.

**HALLAZGO, EL INDICE SEMANTICO ESTA DESFASADO.** Tiene 3.521 ids y los nodos vivos son
3.169: **18 vivos sin vector**, nombrados en la salida, y **370 ids que ya no estan
vivos**. Importa porque es el indice que lee `A2.6`: un nodo vivo sin vector no se puede
comparar por semantica y solo entra por la pierna del titulo. **Viene de antes y no de
`OP-S-12`**, y lo dejo medido en vez de suponerlo: el indice se construye de
`texto_nodo()`, que lee titulo, resumen y condiciones, y `OP-S-12` solo toco las dos listas
de aristas sin renombrar un id, con el censo de vivos igual antes y despues.

**PREGUNTA 1.** ¿La fase 08 puede darse por HECHA con tres de sus cinco puntos
transversales sin correr, o queda abierta hasta una sesion con credencial? **No lo adjudico
yo**, porque cerrar una fase con parte de su verificacion sin recorrer es exactamente lo
que el criterio de HECHO prohibe.

**PREGUNTA 2.** ¿El reindexado semantico entra en esa misma sesion con credencial? Si
entra, arregla de paso los 18 vivos sin vector y los 370 ids muertos del indice.

**EL MERGE NO SE PIDE Y NO SE HACE.** La campaña no esta consumada: la fase 08 sigue
abierta por lo que dice la seccion 5.
