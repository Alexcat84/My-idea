# REPORTE DE LA VUELTA 60 (20 ago 2026, ejecutor Opus 5)

**LA FECHA DE ARRIBA ESTA MEDIDA Y NO SUPUESTA, y se dice primero porque es la caida que esta vuelta
venia a corregir:** `date` del sistema y `git log -1 --date=format:'%Y-%m-%d'` dan **los dos**
`2026-08-20`, y el instrumento que escribio la correccion **cae en ROJO si los dos relojes no
coinciden**.

**EL TRAMO 5 QUEDA CERRADO.** Los treinta y tres actos que faltaban se ejecutan **en dos lotes
enteros**, B y C, y el tramo cierra con **47 fundidos y 3 declarados de 50**. **LA TAREA 1 VA ENTERA
EN SUS DOS PARTES.** **EL HALLAZGO DE LA VUELTA VUELVE A SALIR DE CORRER UNA GUARDA Y NO DE LEERLA,
y esta vez el cazado soy yo:** el diff del censo de duplicadas que corri publico **una fabricada que
no existia**, y la verificacion contra el grafo (regla 9) la desmonto antes de que tocara un nodo.
**P.16 tenia razon y el que estaba mal era mi diff.**

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `d6e98e97` (el commit del acta 59), **arbol limpio y todo pusheado; la regla 3 se cumplio POR VACIO y se dice asi en vez de darla por cumplida** |
| **hash final** | `5ce3300a` (el registro del tramo) mas este mismo commit, que solo escribe este reporte, **pusheados a `origin/pasada-unica`** |
| **commits de la vuelta** | **5 hasta aqui**, leidos de `git log --oneline d6e98e97..HEAD` al escribir esto: `7938d4b4` (apertura medida), `852d9412` (TAREA 1 entera), `02384c6a` (LOTE B), `aed86a79` (LOTE C), `5ce3300a` (el registro del cierre del tramo 5), **mas este** |
| **arbol al cierre** | limpio tras este commit |

---

## 0. LA APERTURA Y EL CIERRE, LA TABLA TALLADA POR INSTRUMENTO (regla 1)

**NINGUNA CELDA ESTA TECLEADA:** sale entera de
`python scripts/loop/tallar_cabecera_reporte.py --vuelta 60`
([`SALIDA_V60_TALLAR_CABECERA.txt`](SALIDA_V60_TALLAR_CABECERA.txt)). **Las dos columnas se leen de
ficheros DISTINTOS.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.326 / 527 / 17.396 | **3.853 / 3.295 / 558 / 17.449** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 223 / 328 | **551 / 254 / 297** |
| actos (componentes) | 134 | **103** |
| actos `CERRADOS` / `ABIERTOS` | 81 / 53 | **50 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 171 / 240 | **109 / 240** |
| cola de costuras | 1.467 | **1.460** |
| colisiones de clase vigentes | 0 | **0** |
| auto-pares (los dos lados al mismo vivo) | 201 | **232** |
| duplicadas historicas: grupos / nodos | 946 / 747 | **935 / 741** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (411 igual a 411; 328 igual a 328) | **TODAS OK (349 igual a 349; 297 igual a 297)** |

**LA APERTURA CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 59 MIDIO POR CORRIDA PROPIA**, y eso es
contraste, no fuente. Instrumentos de apertura corridos **ANTES de la primera operacion y con el
arbol limpio** (`git status --porcelain` VACIO, comprobado y no supuesto):
[`SALIDA_V60_APERTURA.txt`](SALIDA_V60_APERTURA.txt),
[`SALIDA_V60_MARCADOR_APERTURA.txt`](SALIDA_V60_MARCADOR_APERTURA.txt),
[`SALIDA_V60_RECOMPUTO_APERTURA.txt`](SALIDA_V60_RECOMPUTO_APERTURA.txt),
[`SALIDA_V60_COLA_APERTURA.txt`](SALIDA_V60_COLA_APERTURA.txt),
[`SALIDA_V60_COLISIONES_APERTURA.txt`](SALIDA_V60_COLISIONES_APERTURA.txt) y
[`SALIDA_V60_DUPLICADAS_APERTURA.txt`](SALIDA_V60_DUPLICADAS_APERTURA.txt). **Las tres que reescriben
sus ficheros salieron IDEMPOTENTES**, verificado por `git status`, que no listo **ni un fichero
rastreado modificado**.

**LA MEDICION DE CIERRE SE RE-CORRIO DESPUES DE ESCRIBIR EL REGISTRO DEL TRAMO**, por si aquella
escritura movia algo, y **las tres salidas dan `diff` VACIO contra las publicadas**: la cabecera de
arriba es la ULTIMA medicion y no una heredada.

**LAS CELDAS QUE SE MUEVEN EN 31 O EN 62 SON LAS QUE LOS DOS LOTES PREDECIAN**, una por acto fundido
o dos por acto: vivos bajan 31, deprecados suben 31, colapsos suben 31, pares distintos bajan 31,
actos bajan 31, `CERRADOS` bajan 31, nodos en `CERRADOS` bajan 62 y auto-pares suben 31. **Son 15 del
lote B mas 16 del lote C**, y los dos deltas de deprecados se midieron por separado al ejecutar cada
lote (**+15 sobre +15 esperado** y **+16 sobre +16 esperado**).

**LAS TRES CELDAS QUE NO SE MUEVEN ASI, MEDIDAS Y NO SUPUESTAS:**

1. **LOS ENLACES SUBEN 53 (17.396 a 17.449).** Cada superviviente hereda los vecinos del que muere y
   la fusion dedupica por literal, asi que el saldo no es multiplo de nada.
2. **LA COLA BAJA 7 (1.467 a 1.460).** Es el efecto de los pasos que se adosan y se apilan en los
   supervivientes, que cambia su cuenta de pasos y saca a siete nodos del corte de la cola.
3. **LAS DUPLICADAS BAJAN 11 (946 a 935 grupos), Y EL DIFF ESTA CORRIDO POR INSTRUMENTO, NO A OJO.**
   **CERO grupos fabricados en los tres cortes.** Esto tiene historia y va en la seccion 4, porque
   es el hallazgo de la vuelta.

**TASA POR DOMINIO AL CIERRE**, leida de
[`SALIDA_V60_MARCADOR_CIERRE.txt`](SALIDA_V60_MARCADOR_CIERRE.txt): compras 0,6 (n 155) | core 22,5
(n 1.445) | entrega 1,2 (n 171) | environmental 16,5 (n 170) | exportacion 11,5 (n 130) |
franquicias 10,1 (n 148) | health_safety 22,4 (n 192) | quality 14,1 (n 844) | risk_management 0,0
(n 106) | seguridad_digital 11,1 (n 27). **IDENTICA a la de la apertura al digito, y no es
casualidad: fundir no voltea veredictos.** Lo sostiene la medicion previa del tramo: **100
combinaciones simuladas y CERO que fabriquen colision**
([`SALIDA_V58_COLISIONES_ESPERADAS_TRAMO5.txt`](SALIDA_V58_COLISIONES_ESPERADAS_TRAMO5.txt)).

---

## 1. TAREA 1.1: **LA FECHA, CORREGIDA POR MEDICION Y NO POR OTRO TECLEO**

La nota de ratificacion de `docs/plan/03_FUSIONES.md` (linea **2469**) decia **21 ago 2026** y la
fecha buena es **20 ago 2026**. **CORRECCION DECLARADA, con el texto viejo CITADO y no borrado**, en
la linea **2471**.

**Y LA FECHA BUENA NO ESTA TECLEADA**, que es el punto entero: corregir una fecha supuesta escribiendo
otra fecha a mano habria repetido la especie de la caida un renglon mas abajo. Nace
**`scripts/loop/vuelta60_correccion_fecha.py`**, que **la MIDE con git** y escribe la linea el mismo
([`SALIDA_V60_CORRECCION_FECHA.txt`](SALIDA_V60_CORRECCION_FECHA.txt)):

| lo que mide | como |
|---|---|
| los **6 commits del ejecutor** de la vuelta 59 (`c9927b19`, `fd7de724`, `956f9e3d`, `39d495b2`, `6b6607bb`, `02d0bf00`) | `git log --date=format:'%Y-%m-%d'`, y **los seis dan `2026-08-20`**; si el rango abarcara mas de un dia, ROJO |
| el commit que **escribio la linea** | buscado por su asunto dentro del rango: `956f9e3d`, de `2026-08-20 13:48:45` |
| **hoy, POR DOS RELOJES** | ultimo commit del arbol y reloj del sistema; **si no coinciden, ROJO y no se fecha nada a ojo** |

**Es idempotente por negativa:** la segunda corrida dice *ROJO (por idempotencia): la linea YA dice
20 ago 2026* y no reescribe. **Comprobado, no supuesto.**

**EL CAMPO `fecha` DEL PLAN SELLADO DEL LOTE A NO SE REEDITA**, como el encargo manda, y queda
declarado en el registro del tramo (seccion 5). **PERO EL ARREGLO SI SE PUSO DONDE MUERDE:** ese
campo estaba **TALLADO A MANO** en la cabecera del generador de planes, asi que cualquier plan
sellado despues heredaba la misma fecha falsa. Pasa a `datetime.date.today()`, y **los planes B y C
nacieron con `2026-08-20`**, comprobado leyendo los tres ficheros.

## 2. TAREA 1.2: **EL ROJO NUEVO, APAGADO POR LA VIA DE REFORMULAR, Y LA ELECCION DECLARADA**

`scripts/loop/vuelta59_planes.py` llevaba **`TRAMO 5` tallado en la CABECERA (linea 1)** aunque su
print de titulo si estaba curado. El encargo daba dos vias y **se eligio REFORMULAR, no rotular como
procedencia**, con este motivo: **aqui el numero NO nombraba a un ancestro, nombraba al sujeto de
hoy**, que es justo lo que `--tramo` puede cambiar; un rotulo de procedencia habria sido **falso**.

**LA ARITMETICA NO SE TOCO, y esta medido de dos formas:** `git diff` da **17 lineas anadidas y 2
quitadas, TODAS de docstring**; y al intentar regenerar el plan del lote A **la guarda mordio en los
16 actos** (*alguno de los dos miembros YA esta deprecado*), que prueba que el motor sigue vivo y que
un plan ya fundido no se puede rehacer.

**BARRIDO RE-CORRIDO AL CIERRE**
([`SALIDA_V60_BARRIDO_TITULOS.txt`](SALIDA_V60_BARRIDO_TITULOS.txt)):

```
RESUMEN: 376 ficheros barridos, 184 con hallazgo, 192 limpios | ROJO 32, AMBAR 35, CENSO 213, ILEGIBLE 1
```

**ROJO baja de 33 a 32** y `vuelta59_planes.py` ya no sale. **Los 35 AMBAR quedan EN COLA**, como el
encargo ordena. **LOS SEIS FICHEROS NUEVOS DE ESTA VUELTA NO SALEN EN EL BARRIDO**, comprobado uno a
uno y no supuesto: `vuelta60_correccion_fecha.py`, `vuelta60_cotejo_insumo.py`,
`diff_duplicadas_por_resolutor.py`, `registrar_cierre_de_tramo.py`, `_v60_lote_b.py` y
`_v60_lote_c.py`.

---

## 3. TAREA 2: **LOS DOS LOTES ENTEROS, Y EL TRAMO 5 CERRADO**

**Las tablas salen enteras de**
`python scripts/loop/tallar_planes_del_tramo.py --vuelta 60 --prefijo PLAN_V59_OPU01_LOTE_ --prefijo PLAN_V60_OPU01_LOTE_`
([`SALIDA_V60_TALLAR_PLANES.txt`](SALIDA_V60_TALLAR_PLANES.txt)).

| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **A** | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17 | **16** | **16** | **97** | 24 | 59 | **14** | **3** |
| **B** | 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33 | **15** | **15** | **90** | 30 | 55 | **5** | **1** |
| **C** | 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 | **16** | **16** | **101** | 24 | 70 | **7** | **0** |
| **los tres** | | **47** | **47** | **288** | **78** | **184** | **26** | **4** |

| la forma, leida del motivo sellado | cuantos | los actos |
|---|---:|---|
| **UNA SOLA VARA de contenido no empatada, y BASTA** | **18** | 4, 6, 9, 16, 21, 22, 23, 24, 25, 26, 27, 28, 30, 36, 37, 44, 45, 46 |
| **TODAS LAS VARAS de contenido de acuerdo** | **10** | 8, 12, 14, 17, 18, 19, 31, 39, 48, 50 |
| **EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO** | **6** | 2, 5, 10, 15, 20, 38 |
| **CONTEOS QUE CHOCAN CON LA PIEZA DECLARADA, y decide la declarada** | **4** | 11, 35, 42, 47 |
| **LA PIEZA DECLARADA GANA A UN CONTEO de contenido** | **2** | 7, 33 |
| **LA PUERTA SOBREVIVE, con el choque registrado** | **2** | 1, 43 |
| **LOS TRES CONTEOS EMPATAN y decide LA PIEZA DECLARADA, que esta de UN SOLO LADO** | **2** | 32, 40 |
| **EL CONTENIDO EMPATA y LA PIEZA DECLARADA Y EL CABLEADO COINCIDEN** | **1** | 49 |
| **LA PIEZA DECLARADA GANA A LOS DOS CONTEOS de contenido** | **1** | 3 |
| **UNA FIGURA CON NOMBRE del informe vence al conteo (EL CASO NO ES LA CASA)** | **1** | 41 |
| **suma** | **47** | |

**CUATRO FORMAS SE LE ENSENARON AL TALLADOR y ninguna vieja se toco ni se renombro.** **Tres de las
cuatro nombran formas que YA EXISTEN en la letra vigente** y solo cambian la frase de cabecera. **LA
CUARTA ES FORMA NUEVA Y VA DICHA:** hasta este tramo **ninguna fusion se habia decidido por una
FIGURA CON NOMBRE del informe** en vez de por una vara de las actas, y por eso lleva etiqueta propia
en vez de colarse dentro de una existente.

**LOS TRES DECLARADOS DEL TRAMO, Y NO SON EL MISMO CASO:**

| acto | lote | especie | por que no lo rompe ninguna vara |
|---:|:---:|---|---|
| **13** | A | `EMPATE SIN VARA` | los tres conteos al digito y **propio declarado A LOS DOS LADOS** (heredado de la vuelta 59) |
| **29** | B | `CONTEOS QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA` | pasos 4 contra 5 y condiciones 3 contra 2 **CHOCAN**, y la pieza declarada esta **a los dos lados**: **LAS DOS VIAS DE DESEMPATE ESCRITAS FALLAN A LA VEZ**, y es el primer ejemplar |
| **34** | B | `EMPATE SIN VARA` | los tres conteos al digito y **UNA linea propia por lado, una contra una**: ni la rama NO ADOPTADA de la cantidad lo romperia |

**LA MESA PASA DE TRECE ACTOS A QUINCE.**

**LAS GUARDAS DE LOS DOS LOTES, TODAS MEDIDAS Y NINGUNA AFIRMADA:**

| guarda | LOTE B | LOTE C |
|---|---|---|
| cotejo del insumo fijado contra los nodos de HOY | **50 actos mirados, 34 vivos, 16 ya fundidos, DESCALCES 0** | (el mismo, corrido una vez para el tramo entero) |
| plan generado | **15 fichas TODAS en verde** | **16 fichas TODAS en verde** |
| `1B`, cobertura exacta, incisos verbatim, junturas | **las cuatro OK** | **las cuatro OK** |
| `P.16` antes de fundir, con el instrumento arreglado | **NINGUNA** | **NINGUNA** |
| simulacion sobre copia | **verde, 4 guardas OK en los 15 actos, CERO escrituras** | **verde, 4 guardas OK en los 16 actos, CERO escrituras** |
| delta de deprecados | **+15 sobre +15: OK** | **+16 sobre +16: OK** |
| reanclar entre la fusion y `run_phase1` | **NADA QUE RE-ANCLAR** | **NADA QUE RE-ANCLAR** |
| `Gate 0` con el ciclo de tres | **OK** | **OK** |
| suite del motor | **25 de 25** | **25 de 25** |
| suite web | **80 ficheros, 1.030 pasadas, 3 saltadas** | **80 ficheros, 1.030 pasadas, 3 saltadas** |
| `tsc --noEmit` | **CERO lineas** | **CERO lineas** |
| censo de colisiones con esperadas | **0 esperadas, 0 medidas, `CALZA: SI`** (201 a 216 auto-pares) | **0 esperadas, 0 medidas, `CALZA: SI`** (216 a 232 auto-pares) |
| duplicadas fabricadas, por instrumento | **CERO** | **CERO**, con **1 renombrado nombrado** |
| caso positivo | **LAS SEIS GUARDAS MUERDEN** | **LAS SEIS GUARDAS MUERDEN** |

El caso positivo va sobre **el acto 37 del tramo 3**, y que esta vuelta no lo toca esta **comprobado
contra la nomina del tramo 5** (100 ids, ninguno de los dos dentro) y contra el grafo (los dos
miembros siguen vivos), **no supuesto**.

**UN ROJO DE LA GENERACION, CAZADO POR LA GUARDA Y DECLARADO:** el plan del acto 42 apuntaba el
`INCISO` de *la tabla de area exponencial* al **paso 2** del absorbido y el trozo vive en el **paso
3**. La guarda del inciso verbatim **paro sin escribir nada** y se corrigio el indice. **La
aritmetica no se toco.**

---

## 4. EL HALLAZGO: **EL DIFF DEL CENSO DENUNCIO UNA FABRICADA QUE NO EXISTIA, Y EL EQUIVOCADO ERA YO**

Tras el lote C, mi diff del censo de duplicadas publico **un grupo NUEVO**:
`control_mantener_ganancias | nodos_siguientes | ciclo_shewhart_pdsa`. Con la vuelta 59 recien
salida de cazar tres defectos en `P.16`, la lectura facil era *`P.16` fallo otra vez*.

**SE VERIFICO CONTRA EL GRAFO ANTES DE TOCAR NADA (regla 9) Y ERA FALSO.** La cadena, medida:

1. `control_mantener_ganancias.nodos_siguientes` valia `['ciclo_pdsa', 'pdsa_shewhart_cycle']` **en
   la apertura**, leido con `git show 7938d4b4:`.
2. `ciclo_pdsa` esta **deprecado** y lo reclama como alias **`pdsa_shewhart_cycle`**, que era el
   absorbido del acto 35. **O sea que las DOS entradas YA resolvian hoy al mismo nodo**: la duplicada
   **ya existia** en la apertura.
3. Lo que la fusion hizo fue **RENOMBRARLE EL DESTINO**, de `pdsa_shewhart_cycle` a
   `ciclo_shewhart_pdsa`.

**`P.16` NO FALLO: acerto.** Su segundo arreglo de la vuelta 59 comprueba exactamente esto (*si las
entradas YA COMPARTIAN resolucion hoy, es duplicada VIEJA*) y por eso dijo `NINGUNA`. **El
instrumento equivocado era mi diff**, que comparaba **el rotulo crudo** `(nodo, campo, destino)` y
no puede distinguir un renombrado de una fabricacion.

**Y NO ERA LA PRIMERA VEZ, y esto es lo que lo convierte en especie en vez de tropiezo:** la vuelta
59 se topo con lo mismo y **lo resolvio A MANO**, emparejando con el ojo los cinco grupos que
aparecian con los cinco que desaparecian.

Nace **`scripts/loop/diff_duplicadas_por_resolutor.py`**, de **nombre estable**, que hace ese
emparejamiento **por maquina**: resuelve **nodo y destino** por la cadena de alias antes de comparar,
**separa RENOMBRADOS de FABRICADOS** y cae en ROJO solo con los segundos. Corrido en los tres cortes:

| corte | grupos ya resueltos | renombrados | **FABRICADOS** |
|---|---|---:|---:|
| lote B contra la apertura ([`SALIDA_V60_DIFF_DUPLICADAS_B.txt`](SALIDA_V60_DIFF_DUPLICADAS_B.txt)) | 943 a 938 | 0 | **0** |
| lote C contra el lote B ([`SALIDA_V60_DIFF_DUPLICADAS_C.txt`](SALIDA_V60_DIFF_DUPLICADAS_C.txt)) | 938 a 935 | **1**, nombrado | **0** |
| el cierre contra la apertura ([`SALIDA_V60_DIFF_DUPLICADAS_VUELTA.txt`](SALIDA_V60_DIFF_DUPLICADAS_VUELTA.txt)) | 943 a 935 | **1**, nombrado | **0** |

**SE PUBLICA ADEMAS UNA DIFERENCIA QUE NADIE HABIA MIRADO:** el censo por rotulo crudo dice **946**
grupos en la apertura y **ya resueltos son 943**. Los tres de diferencia son grupos que **el rotulo
separaba y el resolutor junta**. **La cifra 946 de la cabecera sigue siendo la del instrumento del
censo y no se toca**; lo que se anade es que **contada por resolutor son 943**, y se dice en vez de
elegir en silencio cual de las dos publicar.

**EL CARRIL DEL `D7` NO SE USO Y SE DICE POR QUE:** el encargo lo dejaba adjudicado *si el censo del
cierre destapa una fabricada*. **No la destapo.** `retirar_entrada_redundante.py` **no se corrio**,
no se escribio ni un nodo despues de cerrar los lotes, y **no hizo falta re-medir el cierre por esa
causa**.

---

## 5. EL REGISTRO DEL CIERRE DEL TRAMO 5, Y LO QUE NO SE PUDO PUBLICAR

Nace **`scripts/loop/registrar_cierre_de_tramo.py`**, de **nombre estable** (la cadena de clones
`vuelta56` a `vuelta57` muere ahi), **sucesor declarado** con la maquina del ancestro copiada. Anade
tres cosas y **cada una por un motivo medido**:

1. **UN TRAMO PUEDE REPARTIRSE ENTRE VARIAS VUELTAS.** El 5 lo abrio la 59 y lo cerro la 60. **Y por
   eso `tallar_planes_del_tramo.py` pasa a aceptar `--prefijo` REPETIBLE:** con un prefijo unico el
   registro habria publicado **31 fusiones donde hay 47**. El contraste esta corrido: sobre la vuelta
   59 imprime **lo mismo al digito**, salvo la linea que ahora **nombra el fichero de cada lote**.
2. **LA SECCION DE PERDIDAS ES OPCIONAL Y DECLARA SU FALTA** en vez de tumbar el registro entero.
3. **`--nota`** para las correcciones que el encargo manda anotar en el cierre.

**Es idempotente:** la segunda corrida dice *YA ESTA* y no escribe.

**LA TABLA DE PERDIDAS NO SALE, Y LA CULPA ES DEL INSTRUMENTO, NO DEL TRAMO.** Las dos mitades, las
dos medidas:

- **CONTABA DE MAS, y SI se corrigio.** De **SEIS** apariciones del token `PERDIDA NOMBRADA` en los
  lotes B y C, **CINCO** viven en frases que dicen que la perdida **SE REPONE** (lote B actos 20, 28,
  31, 32; lote C acto 36). **Sin corregirlo, la tabla de arriba habria publicado 5 perdidas en el
  lote B y 1 en el C, y las dos son falsas.** Contraste corrido: **con la correccion, el lote A de la
  59 sigue dando 3**, la cifra que ya publico.
- **SIGUE CONTANDO DE MENOS, y NO se corrigio porque hacerlo a ojo seria inventar.** Solo ve las
  perdidas con token. En estos dos lotes hay **al menos cuatro sin el**, y van nombradas: el matiz
  *sin recurrir a esquemas motivacionales artificiales* (B, acto 26), el matiz *o trabajador* (C,
  acto 36), la mitad de `Concerns, Options, Consequences` que vive solo en el titulo del absorbido
  (C, acto 37), y la instancia `arruga`, tambien solo en el titulo (C, acto 41).

**Y EL TALLADOR CAYO EN ROJO sobre el acto 19 del lote B**, el unico con perdida y token, porque su
nota nombra a la vez un paso y una condicion. **Eso es la guarda funcionando:** el instrumento esta
escrito para caer en ROJO antes que clasificar en silencio.

**HALLAZGO APARTE, MEDIDO, Y QUE NO ES DE ESTA VUELTA:** corrido el tallador **sin ningun cambio
mio** (`git stash`) sobre el lote A de la vuelta 59, **sus tres perdidas salen las tres en ROJO**, y
**la vuelta 59 nunca llego a correrlo** (no existe `SALIDA_V59_TALLAR_PERDIDAS.txt`). **La cifra 3
que aquella vuelta publico sigue en pie**; lo que no existe, y no existia, es su clasificacion por
especie.

---

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

| | que hice | por que se puede discutir |
|---|---|---|
| **D1** | **FUNDI el acto 32 (lote B) aunque el cuadro de varas lo imprima como `EMPATE SIN VARA`**, por pieza declarada de un solo lado | Es **la primera vez de la campana en que un empate sin vara impreso se funde**. Lo sostengo con la letra del propio plan (*la forma impresa es medicion de los tres conteos y NO adjudicacion, porque el cuadro no conoce la pieza declarada*) y con acta 54 pregunta 4; pero **quien lea la fila del cuadro sin la razon al lado leera lo contrario**, y el 13 y el 34 se declararon con la misma etiqueta impresa |
| **D2** | **DECLARE el acto 29 (lote B)**, primer ejemplar en que **las dos vias de desempate fallan a la vez** | Un lector puede decir que **el cableado deberia entrar** (12 contra 3, la diferencia mas ancha del acto) cuando la pieza declarada esta a los dos lados. No lo aplique porque `P.8` dice que el cableado **solo habla a contenido EMPATADO**, y aqui el contenido **choca**; pero esa lectura estrena doctrina y la dejo sin usar |
| **D3** | **FUNDI el acto 40 (lote C), segundo `EMPATE SIN VARA` impreso**, mientras el 34 se declaraba | La diferencia que uso es **de redaccion de la razon**: en el 34 escribe *NINGUNO DOMINA*, no nombra superviviente y da **una linea por lado**; en el 40 **si nombra superviviente** y llama al propio del otro **LINEA A REPONER**. Es una distincion fina y **quien no la admita dira que los dos casos son el mismo y que uno de los dos esta mal** |
| **D4** | **FUNDI el acto 41 (lote C) CONTRA el conteo de pasos**, por la figura **EL CASO NO ES LA CASA** | Es **la unica fusion del tramo decidida por una figura del INFORME y no por una vara de las ACTAS**. La razon la cita con su numero (78.2, par 2.335) y `P.8` alcance de rol; pero **una figura del informe no esta en la lista de varas** que la cabecera del plan enumera, y un lector estricto dira que el conteo de pasos mandaba |
| **D5** | **FUNDI el acto 43 (lote C) hacia la PUERTA, contra lo que la razon declara** | Es el carril del acta 54 pregunta 1 y el choque queda en el motivo, y a diferencia del acto 1 del lote A **aqui los conteos SI acompanan a la guarda**; pero la razon dice literalmente *Sobrevive medicion_calidad_2, el mas operativo, POR ELEGIR*, y en una fusion **por elegir** la guarda esta eligiendo |
| **D6** | **NOMBRE dos perdidas de nombre que el instrumento NO PUEDE reponer** (`Options`/`Consequences` en el acto 37, `arruga` en el 41) porque viven **solo en el titulo del absorbido** | Es la misma figura que el acta 59 dejo abierta con `TAGUCHI` (`D6` de aquella vuelta), y **esta es su segunda y tercera aparicion sin que exista regla**. Un lector estricto puede decir que **un acto cuya perdida de nombre no se puede reponer no estaba listo para fundirse** |
| **D7** | **CORREGI DOS INSTRUMENTOS DE CONTEO DE PERDIDAS en la misma vuelta en que corro sus cifras** | Las dos correcciones estan medidas y contrastadas contra el lote A (que sigue dando 3); pero **cambiar el instrumento que va a contar mis propias cifras, el mismo dia, es exactamente la forma en que un conteo se acomoda a quien lo corre**. La alternativa era publicar 5 y 1, que son falsas |
| **D8** | **NO CORRI `retirar_entrada_redundante.py`**, porque el censo no destapo ninguna fabricada | El carril estaba **adjudicado** por el encargo para ese caso y no se uso. Lo digo por si el auditor esperaba verlo corrido: **no habia nada que limpiar**, y correrlo sin causa habria sido escribir sobre el grafo por gusto |
| **D9** | **APENDE 3 pasos y 2 condiciones en el acto 38 (lote C)**, o sea **5 de 6 piezas viajan enteras** | Es el reparto mas ancho del tramo. Lo sostengo porque es fusion mutua decidida **por cableado** y las lineas son complementarias; pero **un nodo que crece de 4 a 7 pasos y de 2 a 4 condiciones en una sola fusion** es candidato a la poda de la fase 04, y no lo marque como solape |

---

## 7. PENDIENTES DE DOCTRINA

- **1, PARA LA MESA, con QUINCE actos** (los trece heredados **mas el 29 y el 34 de este tramo**). La
  rama de **la cantidad como vara** sigue **NO ADOPTADA** y **no se uso en ningun acto** de estos dos
  planes, **ni siquiera donde habria decidido** (acto 29, dos propios contra tres; acto 38, tres
  contra dos).
- **2 (INCISO), 3, 4, 5 y 7: HEREDADOS SIN CAMBIO.** No se pagan hoy.
- **NUEVO, y es el `D6` de la vuelta 59 convertido en serie:** **la perdida de nombre que vive SOLO
  en el `titulo_concepto` del absorbido no la puede reponer este ejecutor**, porque su contrato no
  toca ese campo y no hay trozo verbatim en ningun paso. Van **tres ejemplares** (`TAGUCHI`,
  `Options`/`Consequences`, `arruga`). **No propongo regla**: propongo que la mesa decida si el
  contrato del ejecutor se amplia o si esa clase de acto se declara.
- **NUEVO, y no pide doctrina sino instrumento:** el tallador de perdidas **solo cuenta las que
  llevan el token**. Cuatro de este tramo no lo llevan.
- **HEREDADO Y SIN PAGAR:** los **35 `AMBAR`** del barrido siguen en cola, como el encargo ordena.

## 8. PREGUNTAS PARA EL AUDITOR

1. **`EMPATE SIN VARA` impreso: cuando se funde y cuando se declara?** (`D1` y `D3`.) Esta vuelta
   funde dos (32 y 40) y declara dos (29 y 34) **con la misma etiqueta en el cuadro**. La linea que
   trace es *la razon reconoce el propio de un solo lado*, pero **la trazo yo**.
2. **Una FIGURA DEL INFORME es vara?** (`D4`.) `EL CASO NO ES LA CASA` decidio el acto 41 contra un
   conteo de pasos, y esa figura **no esta en la lista de varas** de la cabecera del plan.
3. **Un acto cuya perdida de nombre vive solo en el titulo se funde igual?** (`D6`.) Tercera
   aparicion sin regla.
4. **Puede el mismo ejecutor corregir el instrumento que cuenta sus cifras, en la misma vuelta?**
   (`D7`.) Las alternativas eran publicar cifras falsas o dejar el registro sin tabla.
5. **El acto 43: la guarda puede resolver una fusion que la razon declara POR ELEGIR?** (`D5`.)
6. **Hay que declarar solape en el acto 38?** (`D9`.) Cinco de seis piezas viajan enteras.

## 9. MIS PROPIOS MANEJOS Y TROPIEZOS, declarados

- **PUBLIQUE UNA DUPLICADA FABRICADA QUE NO EXISTIA** y la desmonte yo mismo verificando contra el
  grafo antes de tocar un nodo. **El instrumento equivocado era el mio, no `P.16`.** Coste: cero
  escrituras, un instrumento nuevo. Esta entero en la seccion 4.
- **RAZONE MAL UNA REVERSION Y LA DESHICE.** Acote la clasificacion del tallador de perdidas a la
  frase, **la revert creyendo que rompia el lote A de la vuelta 59**, y al comprobarlo corriendo el
  instrumento **sin ningun cambio mio** (`git stash`) resulto que aquellos tres actos **ya salian
  ROJO antes** y que la vuelta 59 **nunca corrio ese tallador**. La cota se re-aplico. **El
  razonamiento equivocado queda escrito dentro del propio instrumento**, no borrado.
- **EL PLAN DEL ACTO 42 APUNTABA EL INCISO AL PASO EQUIVOCADO** y lo paro la guarda, no yo.
- **La trampa del `vitest`, ya conocida y esquivada otra vez:** con `--reporter=basic` revienta al
  crear el servidor; sin la bandera corre limpio. **Es de entorno, no del codigo.**
- **CORRI LAS SUITES CUATRO VECES** (dos por lote, mas las dos del guardian de commit) y **el `Gate
  0` dos veces enteras**. Ninguna cifra se heredo entre lotes.

## 10. LO QUE QUEDA, DICHO SIN ADORNO

**EL TRAMO 5 ESTA CERRADO Y SU REGISTRO ESCRITO.** Quedan **50 actos `CERRADOS`** en el grafo, que es
de donde sale el **tramo 6** cuando el encargo lo abra; **su abridor NACE ESTABLE**, que es lo que el
acta 58 (pregunta 4) dejo dicho y lo que `vuelta58_tramo5_nomina.py` todavia no cumple (sigue en la
lista de los 32 `ROJO`). **Los 35 `AMBAR` del barrido siguen sin pagar.** **La mesa acumula QUINCE
actos.** **Nada de esta vuelta quedo a medias:** los dos lotes fueron enteros, con sus guardas en
verde, y el registro del tramo salio por maquina.
