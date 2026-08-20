# REPORTE DE LA VUELTA 52 (20 ago 2026, ejecutor Opus 5)

**LA TAREA 1 ENTERA, sus CINCO puntos, cada uno tratado por su especie. DE LA TAREA 2, TRES ACTOS
FUNDIDOS con el CARRIL DEL FILO estrenado y CINCO ACTOS DECLARADOS. Y EL HALLAZGO DE LA VUELTA
SALE DE LA PROPIA REPARACION QUE EL ENCARGO ORDENO: el encargo mandaba anadirle al instrumento de
las puertas el caso de MAS DE UNA PUERTA con alguna obligada a morir, y nombraba DOS actos. LA
VARA REPARADA ENCUENTRA TRES, Y EL TERCERO TIENE UNA SOLA PUERTA. Lo que eso desmiente no es una
cifra sino la frase del instrumento viejo: un acto con una sola puerta SE SALVA si la lectura
elige a ese nodo. Cuando esa unica puerta es el CENTRO de la estrella, la lectura NO PUEDE
elegirlo. La cuenta de puertas nunca fue lo que decide.**

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `7eb940ee` (el acta de la vuelta 51), **arbol limpio y todo pusheado** |
| **commits de la vuelta** | **4**: `ee10eee1` (TAREA 1), `6ecb5d75` (lote A), `1996efd7` (lote B) y el del cierre |
| **arbol al cierre** | limpio tras el commit del cierre |

---

## 0. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (regla 1)

**Corrida ANTES de tocar nada**, con `python scripts/loop/vuelta31_estado.py APERTURA_V52`
([`SALIDA_V52_APERTURA.txt`](SALIDA_V52_APERTURA.txt)). **El arbol estaba limpio y todo pusheado
en `7eb940ee`, asi que la regla 3 se cumplio por vacio, y se dice asi en vez de darla por
cumplida.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 566 / 77 / 8 / 2.737 | **563 / 75 / 7 / 2.743** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| tasa de `A` | 16,7 | **16,6** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.492 / 361 / 17.011 | **3.853 / 3.489 / 364 / 17.011** |
| retrato: `A` crudas / colapsos / pares distintos | 566 / 57 / 509 | **563 / 60 / 503** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| actos `CERRADOS` / `ABIERTOS` | 247 / 53 | **244 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 518 / 240 | **509 / 240** |
| cola de costuras | 1.489 | **1.488** |
| duplicadas tras resolver (grupos) / auto-aristas | 1.001 / 0 | **1.000 / 0** |
| colisiones de clase vigentes | 0 | **0** |
| mixtos del tramo 1 pendientes de `P.12` | 21 | **18** |

**El cierre esta RECOMPUTADO al cierre**, DESPUES del ultimo movimiento
([`SALIDA_V52_CIERRE.txt`](SALIDA_V52_CIERRE.txt),
[`SALIDA_V52_MARCADOR_CIERRE.txt`](SALIDA_V52_MARCADOR_CIERRE.txt),
[`SALIDA_V52_RECOMPUTO_CIERRE.txt`](SALIDA_V52_RECOMPUTO_CIERRE.txt),
[`SALIDA_V52_COLA_CIERRE.txt`](SALIDA_V52_COLA_CIERRE.txt),
[`SALIDA_V52_DUPLICADAS_CIERRE.txt`](SALIDA_V52_DUPLICADAS_CIERRE.txt)), **no copiado de la
apertura.**

**EL MOVIMIENTO DEL MARCADOR CUADRA AL DIGITO CON LOS SEIS VOLTEOS**, y se dice porque es la
comprobacion que la vuelta 51 no hizo: **menos 3 en `A`** (los puestos 502, 251 y 281), **menos 2
en `B`** (el 266 y el 243), **menos 1 en `C`** (el 246) y **mas 6 en `D`**.

**UNA SOLA FAMILIA DE LIBRO SE MUEVE:** `Coleman`, de **74 vivos y 72 unicos** a **73 y 71**,
porque `regalos_estrategicos_sorpresa` es suyo. Las otras cuatro quedan quietas (`Weinberg`
68/66, `Horowitz` 91/89, `Hugos` 111/111, `Rackham` 46/46). **UN SOLO DOMINIO SE MUEVE:** `core`,
de `A 332` (23,0 por ciento) a **`A 329`** (22,8), porque los tres actos fundidos son los tres de
`core`.

---

## 1. TAREA 1: LOS CINCO PUNTOS, CADA UNO POR SU ESPECIE

**Instrumentos: `scripts/loop/vuelta52_correcciones_tarea1.py` (once sustituciones, todas
idempotentes al re-correrlas:
[`SALIDA_V52_CORRECCIONES_T1_IDEMPOTENCIA.txt`](SALIDA_V52_CORRECCIONES_T1_IDEMPOTENCIA.txt)) y
`scripts/loop/vuelta52_fotos_fechadas.py` (seis, tambien idempotentes).**

| | la especie | lo que se toco |
|---|---|---|
| **1.1** | **CONTADOR QUE NO CUADRA CON SU PROPIA CADENA** | filas **246**, **247** y **248** de `RECOMPUTO_3388.md`: ocho, cinco y ocho tachados contra contadores que decian siete, cuatro y siete. **Cuadrados con tachado (`~~SIETE~~ OCHO`, `~~CUATRO~~ CINCO`, `~~SIETE~~ OCHO`) y con la nota fechada de la vuelta 51 ADOSADA**, sin reescribir ninguna nota vieja |
| **1.2** | **CIFRA QUE NACIO MAL** (copiada de otra corrida) **y ROTULO** | los cinco declarados del registro de la vuelta 51: **`~~4, 21, 23, 27 y 28~~ 3, 19, 21, 25 y 26`**, que es lo que imprime la salida que la propia celda cita. Y **`~~25~~ 51` combinaciones de acto y superviviente viable de los 25 actos MIXTOS** |
| **1.3** | **ROTULO ENVEJECIDO, la cifra se queda** | la fila *los declarados 29, 32 y 36* del registro de la vuelta 49: **`~~hoy~~ 26, 28 y 32 AL ABRIR LA VUELTA 49`**, cifras intactas |
| **1.4.a** | **FOTO FECHADA tratada como TABLA VIGENTE** | el apendice **95.1** de `INTRA_DOMINIO_INFORME.md`: rotulo fechado al checkpoint del bucle vuelta 4, **cadena CERRADA** y la medicion de hoy DENTRO de la nota como contraste |
| **1.4.b** | **FOTO FECHADA, verificada por git ANTES de fechar** | las dos tablas *al cerrar la vuelta* (lineas 1790 y 1837): rotulo `~~medido hoy~~ MEDIDO AL CERRAR LA VUELTA 19 / 20`, cadena cerrada, contraste dentro de la nota |
| **1.5** | **INSTRUMENTO CON UNA DICOTOMIA QUE NO ALCANZA** | `vuelta48_puertas_en_el_lote.py` reparado con el texto viejo entero delante en el docstring; **de dos categorias a CUATRO** |

### LA VERIFICACION POR GIT DE 1.4.b, que es lo que el encargo pedia ANTES de fechar

**Se escribio un instrumento propio para eso** (`scripts/loop/vuelta52_marcador_por_git.py`), que
**no hace checkout y por eso no puede ensuciar el arbol**: lee
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` del objeto de git con `git show` y cuenta con la misma
aritmetica que `recomputar_marcador.py`. **Corrido sobre los ONCE commits que van del inicio de
la vuelta 19 al final de la 21** ([`SALIDA_V52_MARCADOR_POR_GIT.txt`](SALIDA_V52_MARCADOR_POR_GIT.txt)):

| commit | asunto | `A` / `B` / `C` / `D` |
|---|---|---:|
| `7b21a8d0` | Vuelta 19 TAREA 2.B, la FASE II medida al cierre | **583 / 89 / 7 / 2.709** |
| `1bfab1c4` | Vuelta 20 TAREA 2, la FASE II medida al cierre | **583 / 89 / 7 / 2.709** |
| (los otros nueve) | de `26c15781` a `8fe604ef` | **583 / 89 / 7 / 2.709** en los once |

**CALZA CON LA PRIMERA CIFRA DE CADA CADENA, que es la que hoy esta tachada.** O sea: **la cifra
nacio BIEN y lo que fallo fue el mantenimiento.** Las cuatro correcciones posteriores (582, 581,
576 y 575) **se le aplicaron a una foto restando de la cifra anterior en vez de re-medir**, y por
eso la `B` y la `C` de esas cadenas se quedaron congeladas mientras la `A` y la `D` bajaban. **Se
fecha, se cierra la cadena, y no se borra nada.**

### LA REPARACION DE 1.5 Y EL HALLAZGO QUE TRAE

**El instrumento viejo tenia DOS categorias**, SALVABLE (*una sola puerta*) e IMPOSIBLE (*todos
los miembros son puerta*), **y su rotulo se desmentia a si mismo**: imprimia dos puertas en la
misma linea bajo el rotulo que dice una sola. **El reparado tiene CUATRO** y la vara escrita
entera: un candidato a superviviente es **LIMPIO** si ninguno de sus absorbidos es puerta, y el
acto es SALVABLE si tiene al menos un candidato limpio.

| | apertura, instrumento viejo | apertura, **instrumento reparado** |
|---|---:|---:|
| actos con al menos una puerta dentro | 31 | **31** |
| SALVABLES | 29 | **26** |
| IMPOSIBLES POR NOMINA | 2 | **2** |
| **IMPOSIBLES POR ESTRUCTURA** | (no existia) | **3** |
| SIN RECETA | (no existia) | **0** |

**LOS TRES IMPOSIBLES POR ESTRUCTURA, y el encargo nombraba DOS**
([`SALIDA_V52_PUERTAS_REPARADO.txt`](SALIDA_V52_PUERTAS_REPARADO.txt)):

| miembros | puertas | por que ninguna eleccion lo salva |
|---|---:|---|
| `decision_cuando_fundar`, `evaluacion_capacidades_fundador`, `tres_preguntas_carrera` | **2** | `decision_cuando_fundar` es el CENTRO, no es viable, y los dos candidatos viables lo absorben |
| `enfoque_paso_a_paso_investigacion_mercado`, `evaluacion_mercados_objetivo`, `screening_mercados_potenciales` | **2** | misma figura exacta |
| **`calcular_peso_dimensional_antes_cotizar`, `conocer_limites_peso_tamano_courier`, `medir_paquete_redondeando_hacia_arriba`** | **1** | **EL QUE EL ENCARGO NO NOMBRABA.** Su UNICA puerta es el CENTRO de la estrella: no es viable como superviviente y los dos candidatos la absorben |

> **LA LECCION: LA CUENTA DE PUERTAS NO ES LO QUE DECIDE.** Lo que decide es si alguna puerta
> esta OBLIGADA A MORIR por la estructura del acto. El caso `c` que el encargo describe (*mas de
> una puerta*) es un sintoma frecuente, no la causa.

---

## 2. TAREA 2: LOS TRES ACTOS FUNDIDOS Y EL CARRIL DEL FILO

### LA GUARDA NUEVA DE COLISIONES, CUMPLIDA AL DIGITO EN LOS DOS LOTES

**La cuenta fija del encargo viejo esta RETIRADA** (acta 51, pregunta 2c): el censo esperado es
el que la simulacion imprime, por PAR RESUELTO.

| lote | **predicho** antes de tocar un nodo | **medido** sobre el archivo entero tras ejecutar | tras `P.16` |
|---|---:|---:|---:|
| **A** (el equity) | **3**: 1 dentro, 2 fuera | **3, las mismas tres** | **0** |
| **B** (regalos y habitos) | **3**: 2 dentro, 1 fuera | **3, las mismas tres** | **0** |

**Ninguna colision real fuera de la prediccion. Ninguna guarda en rojo. Ninguna condicion de
parada.**

### LOS TRES ACTOS, con el CONTENIDO eligiendo y NUNCA el conteo de caracteres

| lote | superviviente | absorbe | el mixto, `CONTINUA` contra el | **que eligio al superviviente** |
|---|---|---|---|---|
| **A** | `criterios_equity_split` | `split_igual_vs_desigual` | `teoria_equidad_split_equity` (871) | el margen mas ancho del tramo: 8 pasos contra 4, 3 condiciones contra 2, cableado 20 contra 4 |
| **B** | `regalos_estrategicos_personalizados` | `regalos_estrategicos_sorpresa` (el centro) | `sorprender_cliente_estrategico` (1348) | **las tres varas de conteo EMPATAN** y el resumen queda en 433 contra 428. Decide el **MATERIAL PROPIO** del puesto 799 (*resistir la tentacion de comercializar masivamente el artefacto exclusivo, que no esta en ningun otro nodo*) contra el otro viable, al que el 251 declara **repetido** |
| **B** | `gestion_de_habitos_mentales_para_pensar` | `formacion_de_habitos_de_pensamiento` (el centro) | `formacion_de_habitos_de_trabajo_creativo` (333) | pasos y condiciones EMPATADOS y **el resumen apunta al OTRO (557 contra 424) y NO desempata**. Decide el **PADRE DECLARADO** del puesto 261, que llama al elegido *la version larga* del centro |

**En los tres muere el CENTRO de la estrella. Ningun veredicto `A` de los tres escribe la formula
*Sobrevive X***, medido hoy ([`SALIDA_V52_VIABLES.txt`](SALIDA_V52_VIABLES.txt)), **asi que esta
vuelta no registra ningun choque nuevo de letra contra aritmetica.**

**Guardas, por acto y en los tres:** miembros vivos y nomina completa, **`1B` POR VACIO en los
tres** (ninguno de sus nueve miembros es puerta, medido con el instrumento reparado), cobertura
exacta de indices sin olvidos, cero repetidos literales, **cero auto-aristas y cero duplicadas
NUEVAS**, los cinco campos que la operacion no redacta intactos, y **los tres absorbidos con su
texto INTACTO**. El pasivo historico de duplicadas baja de 1.001 a 1.000 grupos porque `P.16`
limpia lo que la propia sustitucion toca.

### EL CARRIL DEL FILO, ESTRENADO: **TRES RELECTURAS, TODAS EN EL MISMO ACTO Y TODAS ANTES DE SELLAR**

| par resuelto | del filo | contraste | veredicto de la relectura |
|---|---|---|---|
| `criterios_equity_split` contra `reparto_inicial_equity` | **266 `B`** | 754 `D` | **CONDICION DE TEXTO.** El vesting y las clausulas de recompra son doctrina propia del par y NO existen en el superviviente; el unico roce es dejarlo por escrito, que es lo que el 754 llama *el unico roce* |
| `criterios_equity_split` contra `timing_equity_split` | **246 `C`** | 688 `D` | **CONDICION DE TEXTO.** El COMO contra el CUANDO, la misma lectura que el propio 246 escribio. **Y la FIGURA que el `C` congelaba (el racimo del reparto de equity) YA ESTA REGISTRADA y remedida a seis**, asi que la fusion no se lleva por delante ningun registro pendiente |
| `gestion_de_habitos_mentales_para_pensar` contra `ruptura_de_habitos_para_estimulo` | **243 `B`** | 563 `D` | **CONDICION DE TEXTO.** `ruptura` tiene CINCO pasos y **solo DOS caben** en el paso 3 del superviviente; los otros tres (dieta de informacion, experiencias nuevas, alternancia de modos) no estan en ningun paso |

**LAS TRES SALIERON CONDICION DE TEXTO Y NINGUNA PREGUNTA DE POLITICA, y de eso dependia que los
actos se pudieran fundir.** Si alguna hubiera destapado politica viva, el acto se habria detenido
y declarado, que es lo que el encargo manda.

### UNA COLISION CON UNA FORMA QUE NINGUN CARRIL ESCRITO CUBRE

**En el par `gestion_de_habitos_mentales_para_pensar` contra `ruptura_de_habitos_para_estimulo`
el veredicto ARRASTRADO es una `D` (el 563) y el DIRECTO es una `B` (el 243)**, que es **al reves
de los dos carriles**: el del `A` arrastrado (acta 49, pregunta 1) y el del filo (acta 51,
pregunta 2, que habla de un arrastrado `B` o `C`).

**Lo que si es mecanico es el disparador de `08_VERIFICACION.md`:** un par vuelve a la cola de
relectura post fusion cuando uno de sus dos nodos **muere o cambia de texto**, y aqui pasan las
dos cosas. **El `B` entra en la cola por su propio pie, se relee, y la relectura sostiene la `D`
por su cuenta.** **Se movio el `B` directo y no la `D` arrastrada, y eso es lectura mia: va
marcado (`D3`).**

### UN MOTIVO NUEVO DE **CUBIERTO CON PERDIDA NOMBRADA**, declarado para poder discutirlo

**En el acto de los habitos, dos piezas del absorbido NO viajaron de `APPEND` aunque no estan
dichas literalmente en el superviviente**, y el motivo no existia escrito: **anadirlas habria
metido dentro del nodo vivo el gesto que un veredicto `D` declara CONTRARIO al suyo.** El puesto
**333** dice que el paso 3 del superviviente (*programar rupturas deliberadas de rutina*) **va
justo en direccion contraria** a *repetir la rutina durante varias semanas*. **La fusion no puede
fabricar una contradiccion dentro del nodo que deja vivo.** Las dos lineas (*la repeticion
durante semanas* y *el segundo aliento*) **siguen vivas en el mixto que sobrevive**, y eso es
parte del motivo. Va marcado (`D5`).

### EL REPARTO, pieza por pieza

| acto | piezas | enteras | de INCISO | ya dichas | perdidas NOMBRADAS |
|---|---:|---:|---:|---:|---:|
| equity | 5 | 1 | 0 | 4 | **0** |
| regalos | 10 | 7 | 2 | 1 | **0** |
| habitos | 6 | 2 | 1 | 3 | **2**, las dos con la linea a salvo en el mixto vivo |

---

## 3. LOS CINCO ACTOS DECLARADOS Y NO FUNDIDOS, cada uno con su especie

| el acto | especie | por que no se funde |
|---|---|---|
| `mission_and_operations_planning`, `proceso_sop_mop`, `sop_colaborativo` | **PREGUNTA DE POLITICA** | **La escribe el propio veredicto 703**: *la mesa tiene que decidir si el catalogo quiere un procedimiento con dos contextos o dos nodos*. El encargo lo manda declarar. **A la mesa** |
| `founder_ceo_succession_process`, `identificacion_necesidad_sucesion_ceo`, `sucesion_iniciada_por_fundador` | **EL CONTENIDO NO ELIGE, y ademas la receta no tiene carril** | pasos EMPATADOS (4 y 4), cableado EMPATADO (3 y 3), el resumen retirado por mandato, **una vara para cada uno** (condiciones 2 contra 1 a favor de uno; PADRE DECLARADO a favor del otro, el 612 registra que su paso 3 es un nodo entero). **Y ademas**: los dos `A` del acto declaran a los dos viables CONTENIDOS ENTEROS en el centro que muere, asi que **la lectura honesta del mixto sale `ENTRA` y no `CONTINUA`, y la receta ratificada no tiene carril para un `ENTRA`** |
| los **TRES** imposibles por puerta (actos 8, 15 y 13 de la apertura) | **IMPOSIBLE POR ESTRUCTURA** | ninguna eleccion que la receta permita deja vivas a sus puertas. **La guarda `1B` los rechaza siempre** |

**Y LOS CINCO DECLARADOS DE SIEMPRE SIGUEN DECLARADOS, ninguno se toca**, identificados por sus
miembros. **Al cerrar la vuelta 52 son los actos 2, 16, 18, 22 y 23**, leidos del bloque *actos
de FUSION PURA vivos* de [`SALIDA_V52_TRAMO1_CIERRE.txt`](SALIDA_V52_TRAMO1_CIERRE.txt), corrida
DESPUES del ultimo movimiento.

---

## 4. EL CASO POSITIVO: LAS TRES GUARDAS PUESTAS A FALLAR A PROPOSITO

**Escrito y corrido ANTES de ejecutar nada** (`scripts/loop/vuelta52_caso_positivo.py`,
[`SALIDA_V52_CASO_POSITIVO.txt`](SALIDA_V52_CASO_POSITIVO.txt)). **Una guarda que sale verde y
nunca se ha visto salir roja no prueba nada, y esta campana lo sabe de primera mano.**

| guarda | la mentira que se le puso delante | resultado |
|---|---|---|
| **`1B`** | un plan cuyo absorbido es `domina_lo_que_compras`, que es puerta | **exit 1, `guarda 1B: ROJO`, aborta sin escribir** |
| **cobertura** | un plan que se olvida del paso 3 del absorbido | **exit 1, `faltan ['3']`, aborta sin escribir** |
| **colisiones** | el censo contra una cuenta esperada FALSA de 7 | **`MEDIDA: 0 | CALZA: NO`** |

**Los planes de mentira se borran al terminar y el ejecutor se llama SIEMPRE en modo simular.**

---

## 5. EL BARRIDO `9.10` DEL CIERRE, CORRIDO DESPUES DEL ULTIMO MOVIMIENTO

**Con las cifras viejas DE HOY** (`--viejo 566,77,8,2737 --retrato 57,509 --puestos
502,266,246,251,281,243`, [`SALIDA_V52_BARRIDO_910_CIERRE.txt`](SALIDA_V52_BARRIDO_910_CIERRE.txt),
163 candidatos listados). **VEINTE celdas corregidas**
([`SALIDA_V52_CORRECCIONES_910.txt`](SALIDA_V52_CORRECCIONES_910.txt)):

| la celda | decia | **medido al cierre** |
|---|---:|---:|
| `RECOMPUTO_3388.md` **246**, `A` crudas **y su contador** | 566, contador OCHO | **563, contador NUEVE** |
| **247**, colapsos **y su contador** | 57, contador CINCO | **60, contador SEIS** |
| **248**, pares distintos **y su contador** | 509, contador OCHO | **503, contador NUEVE** |
| **528**, el checkpoint `ii` en sus dos parentesis | 509 igual a 509 | **503 igual a 503, sigue OK** |
| **1079**, total de la tabla por dominio | 566 (16,7 %) | **563 (16,6 %)** |
| `INTRA_DOMINIO_INFORME.md` **100.1**, las CUATRO filas | 566 / 77 / 8 / 2.737 | **563 / 75 / 7 / 2.743** |
| **100.1**, tercera nota adosada | | **sin reescribir las dos de la vuelta 50 ni la de la 51** |

**LOS TRES CONTADORES SE CUADRARON EN EL MISMO ACTO, que es la regla que la vuelta 51 dejo sin
cumplir y que esta vuelta cumple de entrada** (`D7` de la vuelta 50, adjudicado). **Y las cuatro
filas del 100.1 se movieron, no dos**, porque los seis volteos salen de tres clases distintas.

### UNA DIVERGENCIA QUE EL BARRIDO SACA Y QUE **NO ES DE ESTA VUELTA**, corregida y declarada

**La tabla POR DOMINIO de `RECOMPUTO_3388.md` mantenia vigente su fila de TOTAL y NO sus filas
por dominio.** Medido **en la APERTURA de esta vuelta, ANTES de la primera operacion**:

| fila | publicaba | **en la apertura de la 52** | **al cierre** |
|---|---:|---:|---:|
| `core` | 344 (23,8 %) | **332** | **329 (22,8 %)** |
| `quality` | 126 (14,9 %) | **123** | **123 (14,6 %)** |
| `health_safety` | 45 (23,4 %) | **43** | **43 (22,4 %)** |

**La divergencia es ANTERIOR a esta vuelta y ninguna vuelta la habia visto, porque el barrido
busca de forma LEXICA las cifras que se le pasan y estas nunca se le pasaron.** **Se corrigen las
tres con tachado y nota fechada**, y la suma de la columna se comprobo hoy contra el total: 329
mas 123 mas 43 mas 2 mas 29 mas 1 mas 18 mas 0 mas 15 mas 3 son **563**. **Tomar ese alcance es
mio y va marcado (`D7`).**

---

## 6. GATE 0 Y LAS SUITES

**Corridos tras la TAREA 1, tras cada lote y otra vez al cierre. Todos exit 0.**

| que | como salio |
|---|---|
| **Gate 0**, ciclo de **TRES** comandos | `run_phase1 --reaplico-curaduria` con **`GATE 0: OK`**; `etiquetas_de_cara --aplicar` con **71** etiquetas; `sync_assets_web` con **6** assets |
| **suite del motor** | **25 de 25** |
| **suite web** | **80** ficheros, **1.030** pasadas y **3** saltadas |
| `tsc --noEmit` | **CERO** lineas |
| duplicadas / auto-aristas **NUEVAS** | **CERO** y **CERO** en los dos lotes |
| las cuatro comprobaciones de `08_VERIFICACION` | **TODAS OK** al cierre (749 igual a 749; 503 igual a 503) |
| censo de colisiones **al cierre** | **CERO** |
| **hook guardian** | verde en todos los commits |

---

## 7. CORRECCIONES DECLARADAS SOBRE MI PROPIO TRABAJO

1. **MI PRIMERA VERSION DEL PLAN DEL LOTE A PUSO EN `miembros` LOS TRES DEL ACTO Y NO SOLO LA
   PARTE A**, y ademas escribio la marca de condicion como `CUBIERTO_COND:2` en el diccionario de
   condiciones, donde el instrumento espera `CUBIERTO:2`. **La simulacion salio en ROJO con dos
   fallos y no escribio nada**, que es exactamente lo que se le pide. Corregido y re-simulado en
   verde antes de ejecutar. **Se cuenta como lo que es: la guarda funcionando, no un acierto mio.**
2. **LA NOTA QUE ESCRIBI PARA EL APENDICE 100.1 DECIA *cuatro volteos de `A`, uno de `B` y uno de
   `C`, y un sexto de `B`*, QUE SON SIETE Y SON SEIS.** Detectado al releer antes de escribir el
   fichero, y corregido a **tres de `A`, dos de `B` y uno de `C`**, con la resta contra la
   apertura escrita al lado (menos 3, menos 2, menos 1, mas 6) para que la cuenta se pueda
   comprobar sin salir de la celda. **La misma nota decia *sus seis volteos* de la vuelta 51,
   que fueron CINCO**; corregido tambien.
3. **EL ANCLA DE LA NOTA DE 1.4.a NO EXISTIA EN EL FICHERO** tal como la escribi (partia una linea
   por donde no se parte). El instrumento **salio en ROJO diciendo *el texto viejo aparece 0
   veces* y no escribio nada**; se re-ancla sobre una cadena verificada unica.
4. **Ficheros tocados que el encargo no nombraba, declarados:** `docs/COSTURAS_INTERNAS.jsonl` y
   `docs/COSTURAS_INTERNAS_RESUMEN.md` (los reescribe `scripts/costuras_internas.py` al correrse),
   `docs/plan/ARISTAS_DUPLICADAS.jsonl` (lo reescribe el instrumento de duplicadas),
   `dataset/metadata/*` y `web/lib/assets/manifest.json` (los reescribe el ciclo de Gate 0).
   **Mismo alcance que las vueltas 48 a 51.**

---

## 8. LOS DISCUTIBLES MARCADOS, para la relectura ciega

**Marcados ANTES de saber si acierto. Son ONCE.**

| # | el discutible | por que lo marco |
|---:|---|---|
| **D1** | **Ejecute 3 de 21 lecturas `P.12`, declare 5 actos mas, y NO abri el tramo 2.** | Es el discutible mayor y es de alcance. Quedan **18** mixtos. **De los 13 mixtos sin mirar, ONCE tienen su par mixto en `D` y dos en `B`. Si el auditor lee que esas once eran mecanicas una vez fijada la receta, esto es una caida de reparto y la marco yo.** Lo que consumio la vuelta fue la TAREA 1 entera (cinco puntos, dos instrumentos nuevos), el caso positivo y las tres relecturas del filo |
| **D2** | **Declare el acto de la sucesion del CEO en vez de fundirlo con `identificacion_necesidad_sucesion_ceo`**, que es a quien apunta la unica vara de conteo que no empata (condiciones 2 contra 1). | **Un lector puede decir que el contenido SI eligio y que yo lo tape con una objecion de doctrina.** Mi motivo es que con ese superviviente la lectura del mixto sale `ENTRA` y la receta no tiene carril; pero **elegir cuando una vara basta y cuando no es mio** |
| **D3** | **En la colision del `243` movi el `B` DIRECTO y no la `D` ARRASTRADA.** | **Ningun carril escrito cubre un arrastrado `D` contra un directo `B`.** Me apoye en que el `B` esta en la cola de relectura por el disparador mecanico y en que la relectura sostiene la `D`. **Si el auditor lee que el carril del `A` se generaliza (el arrastrado se voltea a la clase del directo), entonces habria que haber bajado el 563 a `B` y mi volteo va al reves** |
| **D4** | **En el acto de los regalos mantuve `CONTINUA` aunque, TRAS la fusion, las cinco lineas del mixto estan todas dentro del superviviente.** | Me apoye en que el veredicto DIRECTO del par resuelto (**1348**) es `D` y en que **un `D` directo no lo tumba la aritmetica de una fusion**. **Pero la lectura honesta del texto resultante es que el mixto ya no anade nada, y eso apunta a `ENTRA`.** Es la misma tension que me hizo declarar el acto de la sucesion, y aqui la resolvi al otro lado **porque alli el par es `B` y aqui es `D`** |
| **D5** | **El motivo NUEVO de CUBIERTO con perdida nombrada** (no meter en el superviviente el gesto que un `D` declara contrario al suyo) **es mio.** | **Ninguna regla escrita lo dice.** De el cuelgan las **dos** perdidas nombradas del acto de los habitos. **Un lector puede decir que una perdida nombrada sigue siendo una perdida y que el `APPEND` era obligatorio** |
| **D6** | **Declare el acto 13 como IMPOSIBLE POR PUERTA aunque el encargo solo nombraba dos y aunque tiene UNA sola puerta.** | El encargo describe el caso `c` como *MAS DE UNA PUERTA*. **Yo lei que lo que decide es que alguna puerta este obligada a morir, no cuantas hay.** Si el auditor lee la letra del encargo, este acto no era del caso `c` y bloquearlo es alcance tomado por mi cuenta |
| **D7** | **Corregi TRES filas por dominio de `RECOMPUTO_3388.md` que el encargo no nombraba** (`core`, `quality`, `health_safety`). | Lo hice porque la fila de TOTAL de esa misma tabla si se mantiene vigente y **dejar tres filas contradiciendo el total que yo acababa de corregir seria publicar una contradiccion a sabiendas**. **Pero dos de las tres ni siquiera las movio esta vuelta**, y corregir cifras ajenas envejecidas es alcance |
| **D8** | **En 1.4.b fecho el rotulo y cierro la cadena dejando VISIBLE el `575 / 83 / 8 / 2.722`**, que no es ni la cifra de la foto (`583 / 89 / 7 / 2.709`, hoy tachada) ni la de hoy. | Es lo que el encargo manda al pie (*fecha el rotulo y cierra la cadena con nota*) **y deja la celda publicando un numero que no es de nadie.** La alternativa era restaurar el 583 destachandolo, y eso **borra** la historia de las cuatro correcciones. **Lo marco porque la celda queda rara y lo digo en vez de que se note** |
| **D9** | **El `INCISO` del acto de los habitos se adosa DETRAS DE UN PUNTO**, asi que el paso resultante queda como dos frases y la segunda sin punto final. | El instrumento concatena `paso + nexo + inciso` sin tocar la puntuacion. **Elegi un nexo que se lee como frase nueva (`Asocia ademas el habito a`) en vez de perder la pieza.** Un lector puede decir que un paso a dos frases no es un inciso |
| **D10** | **En el acto de los regalos marque los pasos 1 y 3 del absorbido como `INCISO` y no como `APPEND`.** | *Su entorno cercano* y *el nombre del destinatario* los lei como **parametro** de gestos que el superviviente ya tiene (investigar intereses, disenar el regalo). **Si el auditor los lee como gestos distintos, son dos pasos que faltan** |
| **D11** | **Para elegir superviviente en los regalos lei *material propio declarado unico en una razon* como CONTENIDO que gana a un empate de tres varas de conteo.** | **`P.8` no dice que el material propio pese mas que el conteo**; el encargo si dice que el material propio cuenta como contenido y que el resumen no desempata. **Pero el orden entre ellos lo puse yo** |

---

## 9. PENDIENTES DE DOCTRINA

1. **LA RECETA `P.12` NO TIENE CARRIL PARA UN `ENTRA`.** Su condicion de viabilidad exige dejar
   un mixto fuera, o sea da por supuesto que todo mixto `CONTINUA`, y el instrumento de fundir
   solo sabe absorber la PARTE `A`. **Medido en el acto de la sucesion del CEO**, donde los dos
   veredictos `A` declaran a los dos viables contenidos ENTEROS en el centro que muere.
2. **LA REGLA DE LA CLIQUE TRATA UNA `B` COMO SI FUERA UNA `D`.** Su motivo escrito habla de
   nodos *que el archivo declaro DISTINTOS*, que es lo que dice una `D` y **no** lo que dice una
   `B` (*no lo doy por sano ni por repetido*). **Afecta al acto de la sucesion y a los otros tres
   mixtos con par en `B` del tramo.**
3. **NO HAY CARRIL PARA UNA COLISION CON ARRASTRADO `D` Y DIRECTO `B` O `C`.** Los dos carriles
   adjudicados cubren el arrastrado `A` y el arrastrado del filo. **Aparecio una vez esta vuelta
   y se resolvio releyendo, que es lo mejor sostenido, no lo escrito.**
4. **QUIEN CONTESTA UNA PREGUNTA DE POLITICA DE CATALOGO.** Heredado y sin cambio: sigue sin
   estar escrito quien decide si el catalogo quiere *un procedimiento con dos contextos o dos
   nodos*. **Afecta al acto del S&OP y a los otros tres mixtos con par en `B`.**
5. **NO HAY REGLA SOBRE QUE HACER CON UNA PIEZA CUYO `APPEND` FABRICARIA UNA CONTRADICCION.**
   Esta vuelta la marco CUBIERTO con perdida nombrada y lo declara como motivo nuevo (`D5`).
6. **HEREDADOS Y SIN CAMBIO HOY**: el `INCISO` para condiciones **sigue sin existir** en el
   instrumento; el esquema de `OPERACIONES.jsonl` **sigue sin distinguir ejecutada de pendiente**
   (71 en `LISTA`, medido hoy); y el campo `orden` de la fase 03 **sigue sin ser su criterio de
   orden**.

---

## 10. LO QUE ESTA VUELTA NO HIZO, DICHO EN VEZ DE CALLADO

1. **NO hizo 18 de las 21 lecturas `P.12` pendientes.** Tres hechas y ejecutadas, cinco actos
   declarados con su especie, **trece mixtos sin mirar en absoluto**. **Es el incumplimiento
   mayor de la vuelta.** La cuenta entera de los 18 que quedan, para que no haga falta
   derivarla: **3 bloqueados por la vara de las puertas** (ninguna lectura los salva), **2 ya
   declarados** (el del S&OP por politica y el de la sucesion por doctrina) y **13 sin mirar**,
   que son los que de verdad esperan lectura.
2. **NO abrio el tramo 2** de 50 actos: no hubo cuerda.
3. **NO toco los cinco declarados de siempre.** Al cerrar son los actos 2, 16, 18, 22 y 23.
4. **NO ejecuto las tres aristas** de los `CONTINUA` ni la poda de sus solapes: son de la fase 04
   y quedan **declaradas** con id resuelto (`P.9`). **En el acto del equity la arista ya existia
   en los dos sentidos**, asi que alli no hay arista que declarar sino solo poda.
5. **NO resolvio las 1.000 duplicadas** ni el alias durmiente `modelo_spin_2`: son de `OP-S-12`.
6. **NO leyo los cuatro mixtos con par en `B` mas alla de sus razones.** Dos de ellos (el del
   S&OP y el de la sucesion) quedan declarados; **los otros dos (el del mapa de influencia y el
   de la investigacion del cliente) no se miraron en absoluto.**
7. **NO reparo la receta** para que sepa que hacer con un `ENTRA`: eso es doctrina y va al
   auditor.

---

## 11. LAS PREGUNTAS PARA EL AUDITOR

1. **Un mixto que, TRAS la fusion, queda entero dentro del superviviente: `ENTRA` o `CONTINUA`?**
   (`D2`, `D4`, pendiente 1.) Esta vuelta lo resolvio **al reves en dos actos** y con un criterio
   que declaro: **cuando el par mixto es `D` mantuve `CONTINUA`** (un `D` directo no lo tumba la
   aritmetica) **y cuando es `B` declare el acto**. Si el criterio no vale, uno de los dos esta
   mal y no se cual.
2. **Si el `ENTRA` existe, quien sobrevive?** La receta excluye al centro por no dejar mixto
   fuera, y en el acto de la sucesion el centro es el unico que el contenido sostiene (8 pasos
   contra 4 y 4, 5 condiciones contra 2 y 1, cableado 14 contra 3 y 3).
3. **La regla de la clique debe distinguir `B` de `D`?** (Pendiente 2.) Su motivo escrito habla
   de nodos *declarados distintos*, y una `B` no declara eso.
4. **Una colision con arrastrado `D` y directo `B`: que carril?** (`D3`, pendiente 3.) Esta
   vuelta movio el `B`. La alternativa era bajar la `D`.
5. **El acto 13 (una sola puerta, y es el centro) es del caso `c`?** (`D6`.) De la respuesta
   depende si son dos imposibles por estructura o tres, y si el instrumento reparado esta bien
   reparado.
6. **Corregir las filas por dominio envejecidas era del barrido o era alcance?** (`D7`.) Dos de
   las tres no las movio esta vuelta.
7. **El `575 / 83 / 8 / 2.722` que queda visible en las dos fotos fechadas: se deja, se destacha
   el 583, o se tacha entero?** (`D8`.) Hoy la celda publica un numero que no es de ninguna
   corrida.
