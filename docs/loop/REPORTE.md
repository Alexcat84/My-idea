# REPORTE DE LA VUELTA 62 (20 ago 2026, ejecutor Opus 5)

**LO PRIMERO, PORQUE ES LO QUE LA VUELTA ENTREGA Y ES MAS DE LO QUE EL ENCARGO PEDIA: EL LOTE A DEL
TRAMO 6 SE EJECUTO ENTERO, Y EL LOTE B TAMBIEN. EL TRAMO 6 QUEDA CERRADO CON 21 ACTOS FUNDIDOS DE 21
Y CERO DECLARADOS, Y CON EL, EL UNIVERSO DE `OP-U-01` QUEDA AGOTADO.** El encargo permitia entregar
solo lo que cerrara entero (acta 58, pregunta 6) y **cerro entero el tramo**.

**LA FECHA DE ARRIBA ESTA MEDIDA POR DOS RELOJES Y NO SUPUESTA:** `date` del sistema da `2026-08-20`
y `git log -1 --date=format:'%Y-%m-%d'` da `2026-08-20`. Es la misma medicion que el campo `fecha` de
los dos planes sellados, que la lee del reloj y no de una constante.

**LAS DOS RACHAS ESTABAN EN CERO Y EL FRENO VA DELANTE.** Los sitios donde esta vuelta tuvo un `ROJO`
o un `AMBAR` propio estan dictados **con las DOS mitades en la misma frase**, cayo Y como quedo, y
van nombrados uno a uno en la seccion 7.

**EL HALLAZGO DE LA VUELTA NO ES DE FONDO SINO DE INSTRUMENTO, Y SALE DE SIMULAR, NO DE LEER:
`registrar_cierre_de_tramo.py`, que es de NOMBRE ESTABLE y se estreno hace dos vueltas, llevaba TRES
BLOQUES DE SU PLANTILLA TALLADOS A MANO CON LAS CIFRAS DEL TRAMO 5.** Corrido tal cual habria
publicado en el registro del tramo 6 que se miraron **50 actos con 34 vivos y 16 ya fundidos** (aqui
son **21, 21 y 0**), la casilla **`0 / 50`** en un tramo de **21**, y una nota afirmando que el lote A
ya estaba fundido al tomar la apertura, **que es falso en un tramo que abre y cierra en la misma
vuelta**. **Se cazo en la corrida `--simular`, antes de escribir una linea**, y va en la seccion 5.

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `d9fd6a54` (el commit del acta 61), **arbol limpio y todo pusheado; la regla 3 se cumplio POR VACIO y se dice asi en vez de darla por cumplida** (`git status --porcelain` VACIO, comprobado) |
| **hash final** | **el commit de este reporte**, pusheado a `origin/pasada-unica`, mas el que escribe esta celda, porque el commit del reporte no puede contener su propio hash |
| **commits de la vuelta** | **5**, leidos de `git log --format=%h d9fd6a54..HEAD`: `fdbaf979` (apertura medida), `dcb20469` (TAREA 1 entera), `7a467818` (LOTE A), `01fb303f` (LOTE B mas el registro del tramo), el de este reporte, **mas el que escribe esta celda** |
| **arbol al cierre** | limpio tras el commit del reporte |

---

## 0. LA APERTURA Y EL CIERRE, LA TABLA TALLADA POR INSTRUMENTO (regla 1)

**NINGUNA CELDA ESTA TECLEADA:** sale entera de
`python scripts/loop/tallar_cabecera_reporte.py --vuelta 62`
([`SALIDA_V62_TALLAR_CABECERA.txt`](SALIDA_V62_TALLAR_CABECERA.txt)). **Las dos columnas se leen de
ficheros DISTINTOS.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.295 / 558 / 17.449 | **3.853 / 3.274 / 579 / 17.486** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 254 / 297 | **551 / 275 / 276** |
| actos (componentes) | 103 | **82** |
| actos `CERRADOS` / `ABIERTOS` | 50 / 53 | **29 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 109 / 240 | **67 / 240** |
| cola de costuras | 1.460 | **1.456** |
| colisiones de clase vigentes | 0 | **0** |
| auto-pares (los dos lados al mismo vivo) | 232 | **253** |
| duplicadas historicas: grupos / nodos | 935 / 741 | **928 / 735** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (349 igual a 349; 297 igual a 297) | **TODAS OK (307 igual a 307; 276 igual a 276)** |

**LA APERTURA CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 61 MIDIO POR CORRIDA PROPIA**, y eso es
contraste, no fuente. Instrumentos de apertura corridos **ANTES de la primera operacion y con el
arbol limpio**: [`SALIDA_V62_APERTURA.txt`](SALIDA_V62_APERTURA.txt),
[`SALIDA_V62_MARCADOR_APERTURA.txt`](SALIDA_V62_MARCADOR_APERTURA.txt),
[`SALIDA_V62_RECOMPUTO_APERTURA.txt`](SALIDA_V62_RECOMPUTO_APERTURA.txt),
[`SALIDA_V62_COLA_APERTURA.txt`](SALIDA_V62_COLA_APERTURA.txt),
[`SALIDA_V62_COLISIONES_APERTURA.txt`](SALIDA_V62_COLISIONES_APERTURA.txt),
[`SALIDA_V62_DUPLICADAS_APERTURA.txt`](SALIDA_V62_DUPLICADAS_APERTURA.txt) y
[`SALIDA_V62_BARRIDO_APERTURA.txt`](SALIDA_V62_BARRIDO_APERTURA.txt). **Las tres que reescriben sus
ficheros salieron IDEMPOTENTES**, verificado por `git status`, que no listo **ni un fichero rastreado
modificado**.

**LA MEDICION DE CIERRE SE RE-CORRIO DESPUES DE ESCRIBIR EL REGISTRO DEL TRAMO**, por si aquella
escritura movia algo, y **las cuatro salidas dan `diff` VACIO contra las de antes** (estado,
marcador, recomputo y cola). **La cabecera de arriba es la ULTIMA medicion, no una heredada.**

**LAS CELDAS QUE SE MUEVEN EN 21 O EN 42 SON LAS QUE LOS DOS LOTES PREDECIAN**, una por acto fundido
o dos por acto: vivos bajan 21, deprecados suben 21, colapsos suben 21, pares distintos bajan 21,
actos bajan 21, `CERRADOS` bajan 21, nodos en `CERRADOS` bajan 42 y auto-pares suben 21. **Son 11 del
lote A mas 10 del lote B**, y los dos deltas de deprecados se midieron por separado al ejecutar cada
lote (**+11 sobre +11 esperado** y **+10 sobre +10 esperado**).

**LAS TRES CELDAS QUE NO SE MUEVEN ASI, MEDIDAS Y NO SUPUESTAS:**

1. **LOS ENLACES SUBEN 37** (17.449 a 17.486). Cada superviviente hereda los vecinos del que muere y
   la fusion dedupica por literal, asi que el saldo no es multiplo de nada.
2. **LA COLA BAJA 4** (1.460 a 1.456). Es el efecto de los pasos que se adosan y se apilan en los
   supervivientes, que cambia su cuenta de pasos y saca a cuatro nodos del corte de la cola.
3. **LAS DUPLICADAS BAJAN 7 (935 a 928 grupos), Y EL DIFF ESTA CORRIDO POR INSTRUMENTO, NO A OJO.**
   **CERO grupos fabricados en los tres cortes**, y **cero renombrados**. Detalle en la seccion 4.

**TASA POR DOMINIO AL CIERRE**, leida de
[`SALIDA_V62_MARCADOR_CIERRE.txt`](SALIDA_V62_MARCADOR_CIERRE.txt): compras 0,6 (n 155) | core 22,5
(n 1.445) | entrega 1,2 (n 171) | environmental 16,5 (n 170) | exportacion 11,5 (n 130) | franquicias
10,1 (n 148) | health_safety 22,4 (n 192) | quality 14,1 (n 844) | risk_management 0,0 (n 106) |
seguridad_digital 11,1 (n 27). **IDENTICA a la de la apertura al digito, y no es casualidad: fundir
no voltea veredictos.** Lo sostiene la medicion previa del tramo: **42 combinaciones simuladas y CERO
que fabriquen colision** ([`SALIDA_V61_COLISIONES_ESPERADAS_TRAMO6.txt`](SALIDA_V61_COLISIONES_ESPERADAS_TRAMO6.txt)).

---

## 1. TAREA 1: **LOS REGISTROS Y LA CORRECCION DEL `%d`**

### 1.1 Las adjudicaciones del acta 61, registradas donde el patron de la campana las pone

Van al final de [`docs/plan/03_FUSIONES.md`](../plan/03_FUSIONES.md), **adosadas y SIN reescribir una
sola linea de las secciones de arriba**, que es la via que esa pagina ya uso dos veces: las tres
adjudicaciones del acta 52 (**linea 1250**) y la del acta 57 sobre el acto 25 (**linea 2475**), **las
dos cotejadas HOY** abriendo el fichero, no recordadas.

| | lo registrado | la vara |
|---|---|---|
| **a** | **EL TRAMO ES UN PREFIJO CON TOPE DE CINCUENTA, NO UN MINIMO**, y por eso **un tramo corto POR AGOTAMIENTO es un tramo**. Con su consecuencia pegada: **el tramo 6 es EL ULTIMO de `OP-U-01`**. Y con su limite: **no autoriza cortar por debajo de cincuenta habiendo actos libres detras** | acta 61, `D1` (linea **15824**) y pregunta 1 (linea **15881**); la vara es la **linea 360** de la propia pagina |
| **b** | **UNA GUARDA PUEDE CRECER EN UN SUCESOR DECLARADO** con dos condiciones: enumerada en el docstring y marcada discutible. **No cubre crecer callando** | acta 61, `D2` (**15839**) y pregunta 2 (**15887**) |
| **c** | **`SELLO_FIJO` NO NECESITA FUENTE EXTERNA: BASTA LA GUARDA**, porque su sujeto vive DENTRO del fichero; `PROCEDENCIA` si la necesita porque el suyo vive FUERA | acta 61, `D3` (**15847**) y pregunta 3 (**15890**) |
| **d** | **LOS 29 VIVOS DE LOS TRAMOS 1 A 5 SON COSA JUZGADA**: quince por la via de la mesa, catorce sin cola pendiente. Prefijo de las guardas y nada mas | acta 61, pregunta 4 (**15893**) |
| **e** | **ENTRE UN ANCESTRO QUE MIENTE EN EL TITULO Y UN SUCESOR DECLARADO QUE NO, EL SUCESOR** | acta 61, `D5` (**15861**) y pregunta 5 (**15900**) |
| **f** | `D4`, `D6` y `D7`, **registrados sin desarrollo porque no crean carril** | acta 61, lineas **15856**, **15867** y **15873** |

**UN ROJO PROPIO DE ESTA MISMA TAREA, Y SE DICTA CON LAS DOS MITADES:** **CUATRO de las citas de
linea salieron mal a la primera** (las de `D4`, `D6`, `D7` y la de *Doctrina nueva: NO*, tecleadas
como 15855, 15868, 15874 y 15938); **Y QUEDARON ARREGLADAS antes del commit** porque se corrio un
`sed` sobre el acta imprimiendo cada linea citada y se compararon una a una: las buenas son **15856,
15867, 15873 y 15953**. **Es exactamente la especie que la regla 1 persigue**, y la caza no fue una
lectura sino una medicion.

### 1.2 **LA CORRECCION DEL AVISO QUE IMPRIMIA `%d` SIN INTERPOLAR**

Es el **hallazgo propio del auditor** (acta 61, seccion 6): la **linea 267** de
`scripts/loop/abrir_tramo_de_opu01.py` imprimia el `AVISO` con los **dos `%d` sin argumentos**.
**QUEDA ARREGLADA con nota fechada y el texto viejo citado entero dentro del propio fichero.**

**EL CASO POSITIVO ESTA CORRIDO, NO AFIRMADO**
([`SALIDA_V62_CASO_POSITIVO_AVISO.txt`](SALIDA_V62_CASO_POSITIVO_AVISO.txt)), **y trae las dos
mitades en la misma salida**:

| mitad | como se midio | que imprime |
|---|---|---|
| **como estaba** | corriendo **el fichero del commit `d9fd6a54`**, extraido con `git show`, con el mismo comando | `se pidio el tramo %d y el medido es el %d` |
| **como queda** | `--tramo-numero 6` sobre el censo que **ya ve el tramo 6 fijado**, asi que el medido es el **7** y el camino se alcanza | `se pidio el tramo 6 y el medido es el 7` |

**LA SALIDA DE PRUEBA NO SE PUBLICA Y SE BORRO TRAS MEDIRLA**, con el contraste anotado: daba **`diff`
VACIO** contra [`TRAMO6_V61.jsonl`](TRAMO6_V61.jsonl). **CERO cifras publicadas dependen de ese
camino**, y por eso es correccion y no caida, tal como el encargo lo dice.

**BARRIDO RE-CORRIDO TRAS LA CORRECCION: `diff` VACIO contra el de la apertura**, 380 barridos, `ROJO`
32, `AMBAR` 0, `ROTULADO` 34, `CENSO` 214, `ILEGIBLE` 1, y **el abridor no sale en ninguna lista**.

---

## 2. TAREA 2: **EL TRAMO 6 ENTERO, EN DOS LOTES**

### 2.1 **LAS TABLAS, TALLADAS DE LOS PLANES SELLADOS**

Salen enteras de
`python scripts/loop/tallar_planes_del_tramo.py --vuelta 62 --prefijo PLAN_V62_OPU01_LOTE_`
([`SALIDA_V62_TALLAR_PLANES.txt`](SALIDA_V62_TALLAR_PLANES.txt)).

| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas selladas |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **A** | 1 a 11 | **11** | **11** | **69** | 14 | 45 | **10** | **12** |
| **B** | 12 a 21 | **10** | **10** | **65** | 13 | 46 | **6** | **6** |
| **los 2** | | **21** | **21** | **134** | **27** | **91** | **16** | **18** |

| la forma, leida del motivo sellado | cuantos | los actos |
|---|---:|---|
| **UNA SOLA VARA de contenido no empatada, y BASTA** | **11** | 1, 3, 5, 6, 10, 12, 14, 16, 18, 19, 21 |
| **TODAS LAS VARAS de contenido de acuerdo** | **5** | 4, 8, 11, 13, 17 |
| **EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO** | **4** | 2, 7, 9, 15 |
| **LA PUERTA SOBREVIVE, con el choque registrado** | **1** | 20 |
| **suma** | **21** | |

**CERO ACTOS DECLARADOS, Y ES EL PRIMER TRAMO DE LA CAMPANA QUE CIERRA ASI. EL MOTIVO ESTA MEDIDO Y
NO ES MERITO:** el cuadro de varas fijado **no trae ni un `CHOCAN` ni un `EMPATE SIN VARA`**, y esas
son **las dos unicas figuras que declaran**. **LA MESA SE QUEDA EN QUINCE ACTOS.** **La rama de LA
CANTIDAD COMO VARA sigue NO ADOPTADA y no se uso en ningun acto de estos dos planes.**

**LAS TRES FORMAS DE LA TABLA SON LAS DE LA LETRA VIGENTE Y NINGUNA ES NUEVA**, y la cuarta (`LA
PUERTA SOBREVIVE`) ya la estreno el tramo 5. **EL CABLEADO SE DICE TAMBIEN CUANDO NO ENTRA:** en los
actos **1, 5, 16 y 18** apunta al lado contrario del que gana o con ventaja ancha, y **queda escrito
en el motivo sellado** en vez de callarse, porque por `P.8` solo habla a contenido EMPATADO.

### 2.2 **EL UNICO CHOQUE DE PUERTA DEL TRAMO: EL ACTO 20**

`mantenimiento_sistema_cui` es **puerta** (extremo de puente aprobado, leido del dossier, que lo marca
`PUERTA: TIENE QUE SOBREVIVIR`, y de la columna `puerta` del cuadro de varas). **Y LAS DOS VIAS
APUNTABAN AL OTRO LADO:**

| via | a quien apunta |
|---|---|
| **la vara de contenido** | pasos 6 contra 5 hacia `getting_started_maintenance` |
| **la pieza declarada** | la razon del puesto **3364** escribe *SUPERVIVIENTE POR DOMINANCIA: `getting_started_maintenance`* |
| **la guarda `1B`** | **prohibe absorber la puerta**, y el unico candidato limpio del acto es el otro |

Por **acta 54, pregunta 1**, registrada en `03_FUSIONES.md`, **LA GUARDA RESTRINGE Y EL CONTENIDO
ELIGE ENTRE LO PERMITIDO**: aqui lo permitido es uno solo, **LA PUERTA SOBREVIVE**, y **el choque
queda escrito en el motivo sellado**. **Y LA CONSECUENCIA VA DICHA, porque es la parte que podia
perderse:** el paso con el que la razon daba la dominancia (*sanitizar o destruir equipos con CUI
antes de retirarlos de las instalaciones*, **la unica linea que nombra CUI en toda la comparacion**)
**es justo el que tuvo que viajar de `APPEND`, y viajo**.

### 2.3 **EL CONTRATO `CAMPO PROPIO v1`, ESTRENADO: LAS PERDIDAS YA NO VIVEN EN LA PROSA**

Nace **`scripts/loop/generar_plan_del_lote.py`**, de **nombre estable** (ni vuelta, ni tramo, ni lote
en el nombre), **sucesor declarado** de `vuelta59_planes.py` (**sha1 del ancestro `fda28294196f`,
medido hoy**), que queda intacto y re-corrible.

**LA MAQUINA NO SE RETECLEA, Y ESO ES COMPROBABLE:** se **extrae** de las lineas 387 a 621 del
ancestro con `scripts/loop/_v62_construir_generador.py`, que lleva **un `assert` por cada cambio** y
es **IDEMPOTENTE** (re-corrido sobre su propia salida da `diff` VACIO, comprobado).

| lo que cambia | es aritmetica? |
|---|---|
| **1.** el contenido editorial entra por `--contenido` y este fichero no conoce ningun tramo | **no** |
| **2.** el campo `perdidas` va **SIEMPRE**, aunque vacio | **no**: es el contrato |
| **3.** **las perdidas se validan AL SELLAR**, no solo al tallar: especie fuera de las tres, o clave que falta, es `ROJO` y el plan **no se escribe** | **SI, ES UNA GUARDA QUE CRECE, Y VA COMO DISCUTIBLE `D1`** |
| **4.** la raiz declara `contrato_de_perdidas` | **no** |

**LA MITAD UTIL DEL CONTRATO, MEDIDA SOBRE LOS 21 ACTOS: NUEVE DECLARAN CERO PERDIDAS con la lista
vacia y DOCE SELLAN AL MENOS UNA.** Lista vacia es **una declaracion**; campo ausente es que el plan
no lo dice, **y eso es `ROJO`**.

**LAS 18 PERDIDAS, TALLADAS POR CAMPO** con `tallar_perdidas_del_plan.py`
([`SALIDA_V62_TALLAR_PERDIDAS.txt`](SALIDA_V62_TALLAR_PERDIDAS.txt)): **14 `DE PARAMETRO DE PASO` y 4
`DE CONDICIONES`**. Ninguna `DE NOMBRE`, y se dice: **este tramo no tuvo ni una perdida de
denominacion**, que es la especie que la vuelta 60 dejo como serie abierta.

**Y UNA DE LAS 18 ES LA QUE EL PROPIO ARCHIVO DEJO PENDIENTE:** la razon del puesto **3064** habia
marcado *PERDIDA NOMBRADA CANDIDATA, no verificada* (**reconociendo logros**, del acto 16). **Aqui
queda sellada en el campo con su especie, su sitio y su destino**, en vez de seguir siendo una nota en
prosa.

### 2.4 **LAS GUARDAS DE LOS DOS LOTES, TODAS MEDIDAS Y NINGUNA AFIRMADA**

| guarda | LOTE A | LOTE B |
|---|---|---|
| cotejo del insumo fijado contra los nodos de HOY | **21 mirados, 21 VIVOS, 0 ya fundidos, DESCALCES 0** | **10 mirados, 10 VIVOS, 0 ya fundidos, DESCALCES 0** |
| plan generado | **11 fichas TODAS en verde** | **10 fichas TODAS en verde** |
| `1B`, cobertura exacta, incisos verbatim, junturas | **las cuatro OK** | **las cuatro OK** |
| `P.16` antes de fundir, por el resolutor | **NINGUNA** | **NINGUNA** |
| simulacion sobre copia | **verde, 4 guardas OK en los 11 actos, CERO escrituras** | **verde, 4 guardas OK en los 10 actos, CERO escrituras** |
| delta de deprecados | **+11 sobre +11: OK** | **+10 sobre +10: OK** |
| reanclar entre la fusion y `run_phase1` | **NADA QUE RE-ANCLAR** | **NADA QUE RE-ANCLAR** |
| `Gate 0` con el ciclo de tres | **OK**, simetrizacion 0 | **OK**, simetrizacion 0 |
| suite del motor | **25 de 25** | **25 de 25** |
| suite web | **80 ficheros, 1.030 pasadas, 3 saltadas** | **80 ficheros, 1.030 pasadas, 3 saltadas** |
| `tsc --noEmit` | **CERO lineas** | **CERO lineas** |
| censo de colisiones con esperadas | **0 esperadas, 0 medidas, `CALZA: SI`** (232 a 243 auto-pares) | **0 esperadas, 0 medidas, `CALZA: SI`** (243 a 253 auto-pares) |
| duplicadas fabricadas, por instrumento | **CERO**, 0 renombrados | **CERO**, 0 renombrados |
| caso positivo heredado | **LAS SEIS GUARDAS MUERDEN** | **LAS SEIS GUARDAS MUERDEN** |
| caso positivo del contrato | **LAS CUATRO PRUEBAS EN VERDE** | **LAS CUATRO PRUEBAS EN VERDE** |

**LOS DOS CASOS POSITIVOS VAN SOBRE EL ACTO 37 DEL TRAMO 3**, que esta **DECLARADO** y que esta vuelta
**no toca**, comprobado **contra la nomina fijada del tramo 6** (42 ids, **ninguno de los dos
dentro**) y contra el grafo (los dos miembros siguen vivos), **no supuesto**.

### 2.5 **EL CASO POSITIVO NUEVO, Y POR QUE NO BASTABA EL HEREDADO**

Nace **`scripts/loop/caso_positivo_del_contrato_de_perdidas.py`**, de **nombre estable**. El heredado
prueba **las seis guardas del EJECUTOR de fusiones**, y **ninguna de las seis sabe nada de perdidas**:
la guarda nueva vive en el GENERADOR y muerde **antes**, al sellar.

| prueba | esperado | medido |
|---|---|---|
| **especie desconocida** (`DE COLOR`) al sellar | `ROJO`, sin escribir | **`ROJO`, exit 1, plan no escrito** |
| **clave que falta** (`enrutada_a`) al sellar | `ROJO`, sin escribir | **`ROJO`, exit 1, plan no escrito** |
| **la MISMA perdida bien formada** | **tiene que PASAR** | **exit 0, sella, 1 perdida en el campo** |
| **campo ausente** con el contrato declarado, visto por el tallador | `ROJO`, sin tabla | **`ROJO`, exit 1** |

**LA TERCERA PRUEBA ES LA QUE IMPIDE QUE ESTO SEA UN SELLO DE GOMA:** una guarda que solo sabe decir
rojo no es una guarda, es un freno de mano. **Muerde y no sobremuerde.**

---

## 3. `Gate 0`, EL CICLO DE TRES Y LAS SUITES

| | |
|---|---|
| `Gate 0` (`python scripts/run_phase1.py --reaplico-curaduria`) | **`GATE 0: OK`** las dos veces, simetrizacion **0** |
| `etiquetas_de_cara.py --aplicar` | **71 etiquetas re-aplicadas** cada vez |
| `sync_assets_web.py` | **6 assets sincronizados**, manifest escrito |
| suite del motor | **25 de 25** |
| suite web | **80 ficheros, 1.030 pasadas, 3 saltadas** |
| `tsc --noEmit` | **CERO lineas** |
| barrido de titulos al cierre | **387 barridos, `ROJO` 32, `AMBAR` 0, `ROTULADO` 34, `CENSO` 214, `ILEGIBLE` 1** |

**LOS SIETE FICHEROS NUEVOS DE ESTA VUELTA NO SALEN EN NINGUNA LISTA DEL BARRIDO**, comprobado uno a
uno por `grep` sobre la salida y no supuesto: `generar_plan_del_lote.py`,
`caso_positivo_del_contrato_de_perdidas.py`, `_v62_lote_a.py`, `_v62_lote_b.py`,
`_v62_construir_generador.py`, `_v62_corregir_registrador.py` y `_v62_registrar.py`.

---

## 4. LAS DUPLICADAS, POR INSTRUMENTO Y EN LOS TRES CORTES

| corte | grupos ya resueltos | renombrados | **FABRICADOS** |
|---|---|---:|---:|
| lote A contra la apertura ([`SALIDA_V62_DIFF_DUPLICADAS_A.txt`](SALIDA_V62_DIFF_DUPLICADAS_A.txt)) | 935 a 933 | 0 | **0** |
| lote B contra el lote A ([`SALIDA_V62_DIFF_DUPLICADAS_B.txt`](SALIDA_V62_DIFF_DUPLICADAS_B.txt)) | 932 a 928 | 0 | **0** |
| el cierre contra la apertura ([`SALIDA_V62_DIFF_DUPLICADAS_VUELTA.txt`](SALIDA_V62_DIFF_DUPLICADAS_VUELTA.txt)) | 934 a 928 | 0 | **0** |

**LOS SEIS GRUPOS QUE DESAPARECEN VAN NOMBRADOS UNO A UNO** en la salida del corte de la vuelta, y
todos son de nodos que murieron en estas mismas fusiones.

**SE REPITE LA DIFERENCIA QUE LA VUELTA 60 DESTAPO, y se dice en vez de elegir en silencio cual
publicar:** el censo **por rotulo crudo** dice **935** grupos en la apertura y **por resolutor** salen
**934** en un corte y **935** en otro, segun contra que fichero se compare. **La cifra 935 de la
cabecera es la del instrumento del censo y no se toca**; lo que se anade es que **contada por
resolutor puede diferir en uno o dos grupos que el rotulo separa y el resolutor junta**.

---

## 5. EL HALLAZGO: **UN INSTRUMENTO DE NOMBRE ESTABLE CON LA PLANTILLA TALLADA A MANO**

`registrar_cierre_de_tramo.py` nacio en la vuelta 60 **de nombre estable**, que es la direccion
correcta. **Pero su plantilla llevaba dentro las cifras del tramo 5 tecleadas**, y eso en un
instrumento estable **no envejece: miente en el tramo siguiente sin que nadie teclee nada ese dia.**

| lo que habria publicado en el tramo 6 | lo que es verdad | como se corrige |
|---|---|---|
| *50 actos mirados, 34 vivos, 16 ya fundidos, DESCALCES 0*, apuntando a la salida de la vuelta 60 | **21, 21, 0** | el bloque se arma de los ficheros que entran por **`--cotejo`**; **sin ninguno, DECLARA su falta** |
| la casilla **`0 / 50`** del tamano del tramo | **`0 / 21`** | el tamano **se suma** de los fundidos y los vivos de la salida del `--fijado` |
| *el lote A ya estaba fundido cuando se tomo la apertura* | **falso**: el tramo abre y cierra en la misma vuelta | se **mide**, leyendo las vueltas de los planes que el tallador hallo |

**Y DOS MAS DE LA MISMA ESPECIE, cazadas por la misma corrida:** el recorte de la `TABLA 1` buscaba la
marca **entera** (que llevaba dentro la cuenta de lotes) y **el registro caia en `ROJO` sin escribir**;
y la rama de la tabla de perdidas **solo conocia las marcas del tallador VIEJO**, asi que **habria
publicado una FALTA DE TABLA que no existe**. **Se reconocen las dos, la vieja primero.**

**SE ANADE ADEMAS `--abre`**, porque **el registro no tenia forma de ABRIR con una declaracion**, solo
de anadir al final con `--nota`, y el encargo pide que el registro del tramo 6 **abra** declarando
`TRAMO FINAL POR AGOTAMIENTO`. **Sin el argumento, el registro sale exactamente como antes.**

**LAS SEIS CORRECCIONES SE APLICAN CON `scripts/loop/_v62_corregir_registrador.py`, que lleva un
`assert` por cada una**, y **el texto viejo queda citado entero dentro del instrumento**.

**Y HAY UNA SEXTA, EN OTRO INSTRUMENTO, DE LA MISMA FAMILIA:** `tallar_planes_del_tramo.py` contaba
las perdidas **solo por el token en la prosa**, asi que **la `TABLA 1` de este reporte habria dicho
`perdidas nombradas 0` mientras el campo sella DIECIOCHO**. Es **exactamente la mitad que su propia
correccion de la vuelta 60 dejo escrita como no arreglada**. Ahora, **si el plan declara el contrato,
la cuenta sale del campo**.

**EL CONTRASTE ESTA CORRIDO Y NO AFIRMADO** ([`SALIDA_V62_CONTRASTE_TRAMO5.txt`](SALIDA_V62_CONTRASTE_TRAMO5.txt)):
sobre los planes del tramo 5, que **no** declaran el contrato, esta version da **A 3, B 1, C 0 y los
tres 4**, que son **las cifras que aquel registro publico**, y **la unica diferencia del `diff` es el
rotulo de la cabecera**.

---

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

| | que hice | por que se puede discutir |
|---|---|---|
| **D1** | **HICE CRECER UNA GUARDA en un sucesor declarado**: el generador valida las perdidas AL SELLAR, cosa que el ancestro no hacia | Es la figura que el acta 61 (`D2`) adjudico **con dos condiciones**, y las dos se cumplen (enumerada en el docstring, marcada aqui). Pero **es la primera vez que se usa esa adjudicacion**, y quien la lea estrecha dira que una guarda nueva es guarda nueva, no copia |
| **D2** | **CORREGI SEIS SITIOS DE DOS INSTRUMENTOS QUE CUENTAN LAS CIFRAS DE ESTA MISMA VUELTA, EL MISMO DIA** | Es el `D7` de la vuelta 60 otra vez, y lo digo igual: **cambiar el instrumento que va a contar mis propias cifras es la forma en que un conteo se acomoda a quien lo corre**. La alternativa era publicar *50 actos mirados* y *perdidas 0*, que son falsas. El contraste sobre el tramo 5 esta corrido y da identico |
| **D3** | **EJECUTE EL TRAMO ENTERO en una vuelta**, cuando el encargo pedia el lote A | El encargo decia que el tamano del lote lo decide el plan que se selle, y que **si no cabe entero se entregue lo que cierre**. Cerro todo. Pero **21 actos en una vuelta es el ritmo mas alto de la campana desde el tramo 3**, y quien mida el riesgo por actos por vuelta dira que era mejor parar en el lote A |
| **D4** | **FUNDI EL ACTO 20 HACIA LA PUERTA contra la vara Y contra la razon a la vez** | Es el carril del acta 54 pregunta 1 y el choque queda en el motivo; pero **a diferencia del acto 1 del tramo 5, aqui la razon NO dice POR ELEGIR: dice DOMINANCIA con nombre propio**, y un lector estricto puede decir que una razon que nombra por dominancia pesa mas que una que solo elige |
| **D5** | **APENDE 3 pasos en el acto 8 (5 a 8) y 3 en el acto 18 (6 a 9)** | Son los dos repartos mas anchos del tramo. Los sostengo porque cada pieza es un gesto que el superviviente no hace en ningun grado; pero **un nodo que crece de 6 a 9 pasos en una sola fusion es candidato a la poda de la fase 04**, y lo declaro como solape en la nota del plan en vez de marcarlo pieza a pieza |
| **D6** | **NOMBRE 18 PERDIDAS, cuando el tramo 5 entero nombro 4** | La diferencia no es que este tramo pierda mas: es que **el contrato nuevo hace visible lo que la prosa no contaba**. Pero quien compare las dos cifras sin leer el contrato dira que este tramo se fundio peor, y **el numero por si solo no distingue una perdida nueva de una perdida que antes no se veia** |
| **D7** | **DECIDI el superviviente del acto 1 por la cuenta de CONDICIONES (2 contra 3) contra un cableado de 7 contra 3** | Es `P.8` al pie: el cableado solo habla a contenido EMPATADO. Pero **la diferencia de cableado es la mas ancha del lote A**, y quien lea el acto por su peso en el grafo dira que sobrevivio el nodo mas pobre |
| **D8** | **DECIDI el acto 5 igual, por pasos 5 contra 6, hacia un nodo con CERO siguientes** | Mismo carril que el `D7` y misma objecion, agravada: `planificacion_gobierno_organizaciones_familiares` **no tiene ni un nodo siguiente**, asi que la fusion mueve el acto a un nodo que el grafo casi no toca |
| **D9** | **MARQUE `CUBIERTO` con perdida sellada en vez de `INCISO` en once sitios**, casi siempre porque el paso del superviviente cierra en punto | Es la letra de la politica del reparto (*de `CUBIERTO` con la perdida NOMBRADA cuando el paso resultante no se lee limpio*). Pero **la puntuacion del superviviente no es una razon de contenido**, y un lector puede decir que el criterio deberia ser si la pieza cabe, no si el punto estorba |

---

## 7. MIS PROPIOS ROJOS Y TROPIEZOS, declarados con las dos mitades

1. **LAS CUATRO CITAS DE LINEA DEL REGISTRO DE ADJUDICACIONES SALIERON MAL** y **quedaron arregladas
   antes del commit** por medicion, no por relectura (seccion 1.1).
2. **EL CASO POSITIVO NUEVO CAYO EN ROJO EN SU PRIMERA CORRIDA, 2 de 4 pruebas**, porque fabricaba la
   mentira sobre **el acto 1 del tramo 6, que esta vuelta acababa de fundir**, asi que **la guarda de
   miembros vivos se disparaba ANTES que la de perdidas y el rojo no era el que se buscaba**; **Y
   QUEDO ARREGLADO** apuntandolo a una nomina de mentira de una sola fila sobre el acto 37 del tramo
   3, con las dos comprobaciones corridas.
3. **LA CABECERA DE `_v62_lote_a.py` ENCENDIO UN `AMBAR` EN EL BARRIDO** (de 0 a 1) por tallar
   `TRAMO 6`; **Y QUEDO ARREGLADA** por la via de **REFORMULAR**, la misma que la vuelta 60 eligio
   para el ancestro, y el barrido volvio a `AMBAR` 0.
4. **EL REGISTRO DEL TRAMO CAYO EN `ROJO` SIN ESCRIBIR** en su primera simulacion, porque el recorte
   de la `TABLA 1` ya no casaba tras mi propia correccion del rotulo; **Y QUEDO ARREGLADO** buscando
   por el prefijo de la marca.
5. **MANEJOS SIN CIFRA DE POR MEDIO, declarados igual:** tres intentos de parche por `heredoc` que
   murieron en su propio `assert` **sin escribir nada** (dos por el escapado de `\n` y uno porque el
   fichero tenia saltos `CRLF` y mi comparacion asumia `LF`); el andamio de correccion del registrador
   dejo **una asignacion muerta duplicada** que **quite antes de correrlo de verdad**; y
   `registrar_cierre_de_tramo.py` quedo **normalizado a saltos `LF`**, que es lo que el repositorio
   guarda, y lo digo porque tocar los saltos de un fichero rastreado es un acto y no un accidente.

---

## 8. PENDIENTES DE DOCTRINA

- **1, PARA LA MESA, con QUINCE actos**, los mismos que el acta 60 conto. **Este tramo no anade
  ninguno**, y el motivo esta medido: sin `CHOCAN` y sin `EMPATE SIN VARA` no hay de que declarar.
- **2 (`INCISO`), 3, 4, 5 y 7: HEREDADOS SIN CAMBIO.** No se pagan hoy.
- **LA SERIE DE LA PERDIDA DE NOMBRE que vive solo en el titulo: NO CRECE.** Este tramo no tuvo ni una
  perdida `DE NOMBRE`, y se dice porque la ausencia tambien es medicion.
- **NUEVO, Y ES DE INSTRUMENTO, NO DE DOCTRINA:** el hallazgo de la seccion 5 dice que **un nombre
  estable no basta para que un instrumento no envejezca**: `registrar_cierre_de_tramo.py` tenia el
  nombre bien y la plantilla tallada. **Queda como pregunta al auditor**, no como regla escrita por
  mi.

---

## 9. PREGUNTAS PARA EL AUDITOR

1. **UN NOMBRE ESTABLE NO BASTA. ¿Hace falta una vara para las PLANTILLAS de los instrumentos
   estables?** El barrido de titulos caza el numero en el TITULO, pero `registrar_cierre_de_tramo.py`
   lo llevaba en el CUERPO de su plantilla de salida, y ahi no lo mira nadie. Lo traigo como pregunta
   y no como regla porque escribir la vara seria doctrina nueva.
2. **¿ES SUFICIENTE EL CARRIL DE LA PUERTA cuando la razon nombra al otro POR DOMINANCIA?** (`D4`).
   El acta 54 pregunta 1 se escribio sobre un acto donde la razon decia *POR ELEGIR*. Aqui dice
   dominancia con nombre. Lo funde igual, y lo pregunto.
3. **LAS 18 PERDIDAS DEL TRAMO 6 CONTRA LAS 4 DEL TRAMO 5: ¿es comparable esa cifra entre tramos?**
   (`D6`). Mi lectura es que **no**, porque los instrumentos que las cuentan son distintos, y que
   compararlas seria leer una mejora de instrumento como un empeoramiento de fusion.
4. **¿SE PUEDE CERRAR UN TRAMO ENTERO EN UNA VUELTA cuando el encargo pedia un lote?** (`D3`). El
   encargo decia *entrega lo que cierre entero y dilo primero*, y cerro todo. Lo pregunto por si la
   lectura correcta era *no mas de lo pedido*.
5. **EL UNIVERSO DE `OP-U-01` QUEDA AGOTADO. ¿Cual es la siguiente operacion?** El `00_INDICE` manda,
   pero lo pregunto en vez de elegirla yo: **la campana entra en terreno que ninguna vuelta ha
   pisado**, y elegir la siguiente operacion no es una medicion.

---

## 10. LO QUE QUEDA, DICHO SIN ADORNO

- **`OP-U-01` esta AGOTADO.** Los **29** actos vivos de los tramos 1 a 5 son **cosa juzgada** (acta
  61, pregunta 4): quince por la via de la mesa, catorce sin cola pendiente. **No queda ningun tramo
  por abrir.**
- **La mesa sigue con QUINCE actos** mas la serie del titulo con tres ejemplares.
- **Las fases 04 en adelante siguen enteras**, y **18 perdidas de este tramo estan enrutadas a la 04**
  con su especie, su sitio y su destino escritos en el plan sellado, no en una nota.
- **NINGUNA CONDICION DE PARADA SE CUMPLE.** El merge sigue siendo decision del fundador y este bucle
  no funde ramas.
