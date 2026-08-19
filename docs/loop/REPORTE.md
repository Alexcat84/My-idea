# REPORTE DE LA VUELTA 37 (ejecutor Opus 5). FASE III, rama `pasada-unica`

**`OP-D-04` CON SUS PASOS 1 Y 2 HECHOS, SU ACTO LEIDO ENTERO POR PRIMERA VEZ (21 DE 21 PARES), Y
LA FUSION EN PARADA CON TRES MOTIVOS MEDIDOS.** El destejido resulto **ya consumado** por el corte
de `OP-F-02`, las cuatro relecturas de `P.5` **no cambian ni una clase**, y las trece lecturas
dirigidas nuevas encontraron **el primer nodo puente TRIPLE del archivo**. **Cero nodos tocados:
ninguno se funde, ninguno se depreca, ninguno pierde un paso. El marcador no se movio.**

---

## 1. LO QUE ESTA VUELTA MOVIO, MEDIDO Y NO NARRADO

- **Hash de partida:** `be54bb7d` (el acta del auditor de las vueltas 34, 35 y 36).
- **Hash final:** `8096b16d`. **CINCO commits** (`a5f3c4ac` la apertura, `646d6878` la TAREA 1,
  `dd80b63f` los pasos 1 y 2, `75e65033` la medicion de `P.5`, `b1d0fa62` las relecturas y
  `8096b16d` el acto entero con la parada), **y el de este reporte hace SEIS.** Se dice con las dos
  cifras a proposito.
- **Rutas tocadas** (`git diff --stat a5f3c4ac..HEAD`, corrido hoy): **50 ficheros, 6.942
  insertadas, 6 borradas**. Por carpeta: `docs/loop` **32**, `scripts/loop` **10**, `docs` **4**,
  `docs/plan` **3**, `docs/loop/paradas` **1**. **Cero merges.** El hook corrio verde en los cinco.
- **`dataset/`: CERO ficheros tocados. `web/`: CERO ficheros tocados.** Medido con
  `git diff --name-only a5f3c4ac..HEAD` filtrado por carpeta: la lista sale **vacia**.
- **EL ARCHIVO DE VEREDICTOS SI SE TOCO, y aqui esta la cuenta exacta**, comparando el fichero de
  hoy contra el del commit de apertura registro por registro: **n 3.388 antes y despues, cero
  altas, cero bajas, CUATRO registros cambiados** (585, 823, 834 y 844), **los cuatro con SOLO el
  campo `razon` movido**, **los cuatro con la razon vieja LITERAL dentro de la nueva** (1.389 de
  4.639; 1.061 de 5.410; 900 de 3.749; 1.151 de 4.410) y **CERO cambios de clase**.

### EL ESTADO, APERTURA CONTRA CIERRE

**Las dos columnas son de dos corridas propias del MISMO instrumento**
(`scripts/loop/vuelta31_estado.py`, **sin tocarlo**): la de **APERTURA** corrida **antes de la
primera operacion** y commiteada antes de tocar nada (`a5f3c4ac`, salida
`SALIDA_V37_APERTURA.txt`), y la de **CIERRE** corrida **al cerrar** (`SALIDA_V37_CIERRE.txt`).

| | **APERTURA** | **CIERRE** |
|---|---:|---:|
| marcador: n / A / B / C / D | 3.388 / 575 / 83 / 8 / 2.722 | **3.388 / 575 / 83 / 8 / 2.722** |
| tasa de A | 17,0 % | **17,0 %** |
| huecos / duplicados / clases fuera de ABCD | 0 / 0 / 0 | **0 / 0 / 0** |
| grafo: ficheros / ids / vivos / deprecados | 3.853 / 3.853 / 3.538 / 315 | **identicos** |
| enlaces / claves distintas | 16.849 / 15 | **16.849 / 15** |
| familias Weinberg / Horowitz / Hugos / Coleman / Rackham (vivos) | 72 / 93 / 111 / 75 / 47 | **identicas** |
| operaciones / estados / dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| inventario | 672 | **672** |
| indice rojo declarado | 18 lineas, 0 ausentes | **18 lineas, 0 ausentes** |
| fronteras de `OP-F-04-COL` | 14 de 15 | **14 de 15** |

> **Y LA COMPARACION SE HIZO POR MAQUINA, no a ojo:** `difflib` sobre las dos salidas enteras da
> **84 lineas cada una y CUATRO lineas de diferencia, LAS CUATRO EL ROTULO** (*APERTURA* contra
> *CIERRE*, en la cabecera y en el pie). **No hay una sola cifra distinta entre el principio y el
> final de la vuelta**, y eso es exactamente lo que un modo de solo lectura tiene que producir.

### LA TASA POR DOMINIO, recomputada del archivo en esta vuelta

**Instrumento `scripts/loop/vuelta35_tasa_dominio.py`, REUTILIZADO y no reescrito** (medicion pura,
sin constantes de vuelta). Salida `SALIDA_V37_TASA_DOMINIO.txt`:

| dominio | n | A | tasa | B | C | D |
|---|---:|---:|---:|---:|---:|---:|
| **core** | 1.445 | 336 | **23,3 %** | 81 | 8 | 1.020 |
| quality | 844 | 126 | 14,9 % | 0 | 0 | 718 |
| health_safety | 192 | 45 | 23,4 % | 0 | 0 | 147 |
| entrega | 171 | 2 | 1,2 % | 0 | 0 | 169 |
| environmental | 170 | 29 | 17,1 % | 0 | 0 | 141 |
| compras | 155 | 1 | 0,6 % | 2 | 0 | 152 |
| franquicias | 148 | 18 | 12,2 % | 0 | 0 | 130 |
| exportacion | 130 | 15 | 11,5 % | 0 | 0 | 115 |
| risk_management | 106 | 0 | 0,0 % | 0 | 0 | 106 |
| seguridad_digital | 27 | 3 | 11,1 % | 0 | 0 | 24 |

**Identica a la de la vuelta 36 en las diez filas**, y tenia que serlo: ninguna clase se movio.

---

## 2. TAREA 1: EL AVISO DE CORTE SOBRE LA PROPUESTA DE LA VUELTA 35

**Hecha, y con el sello intacto.** `docs/loop/PROPUESTA_V35_RELECTURAS.json` recibe **un campo
nuevo y fechado**, `aviso_posterior`, que dice que las cinco relecturas se volcaron el **18 ago
2026** en la vuelta 36 por `scripts/loop/vuelta36_volcado_910.py` con el lote
`docs/loop/_lote_v36.jsonl`, y que **el 643 fue por su propio carril**,
`docs/loop/_lote_v36_643.jsonl`, como `LD-82`.

**Instrumento nuevo `scripts/loop/vuelta37_aviso_v35.py`, con cuatro guardas corridas hoy**
(salida `SALIDA_V37_AVISO_V35.txt`):

| guarda | resultado |
|---|---|
| 1. la propuesta y el lote son **el mismo conjunto de cinco** | `[277, 374, 452, 1571, 1575]` en los dos. **OK** |
| 2. el **643 NO esta** en la propuesta y su carril trae **solo al 643** | **OK** |
| 3. los seis puestos estan **HOY en clase `D`** en el archivo | **OK**, medidos uno por uno |
| 4. tras escribir: el campo `estado` **identico caracter a caracter** y las filas **identicas** | **OK**: `23.020` caracteres antes y despues |

**El diff del fichero lo confirma: 2 insertadas y 1 borrada**, y la borrada es solo la ausencia de
salto de linea final. **El campo `estado` sigue diciendo, literal, *PROPUESTA NO VOLCADA. Espera
decision del fundador (PARADA de la vuelta 35)*.** Es la figura del aviso de corte: **el sello se
conserva y el aviso se fecha.**

---

## 3. TAREA 2: `OP-D-04`, PASO POR PASO

### 3.1 PASO 1, LA FUENTE PRIMERO, verificada por corrida propia y no leida de su nota

**El encargo manda verificar que `OP-F-02` y `OP-F-03` estan ejecutadas antes de apoyarse en
ellas, y eso no se resuelve leyendo sus notas:** las dos declaran *QUEDA HECHA* con fecha 14 ago
2026, y la regla 2 dice que **una nota nunca es fuente de una cifra nueva.** Instrumento
`scripts/loop/vuelta37_fuente_primero.py`, salida `SALIDA_V37_OPD04_FUENTE.txt`:

| medicion de hoy contra el grafo | resultado |
|---|---|
| los **tres nodo propio** de `OP-F-02` | `escenarios_de_evolucion_de_la_ia` **6 pasos**, `critica_del_plan_con_ia` **5**, `ideacion_con_ia_en_la_sesion` **4**: **los tres vivos, los tres con los pasos que la nota declara, los tres en `INDICE_ROJO_DECLARADO.jsonl`** |
| Mollick en los tres origenes de `OP-F-02` | **fuera de los tres**, buscado sobre el fichero entero de cada nodo |
| la fuente de `brainstorming_divergente` | **UNA sola**, *Change by Design, Revised and U - Tim Brown*, que es la fijada en `01_FUENTES.md` |
| los **cuatro nodo propio** de `OP-F-03` | 4, 9, 4 y 8 pasos: **los cuatro vivos y los cuatro en el indice rojo** |
| **el cruce medido** | de los siete nodos de `OP-D-04`, **UNO** esta en la nomina de `OP-F-02` y **CERO** en la de `OP-F-03` (que tiene 21) |

> **LO QUE ESE ULTIMO NUMERO ANADE Y NO ESTABA ESCRITO:** el campo `depende_de` de `OP-D-04` nombra
> a `OP-F-03`, y **no comparten ni un nodo**. **Esa dependencia es de ORDEN DE FASE, no de nodo
> compartido**, y ahora esta medido en vez de supuesto.

### 3.2 PASO 2, EL DESTEJIDO: CONSUMADO, Y SIN NADA QUE CORTAR

**Es el hallazgo estructural de la vuelta.** El plan escribe cuatro frentes para
`brainstorming_divergente`, y dos de ellos, **la decision de fuente y el destejido, resultaron ser
el mismo bloque.** Instrumento `scripts/loop/vuelta37_destejido_opd04.py`, salida
`SALIDA_V37_OPD04_DESTEJIDO.txt`:

| medicion de hoy | resultado |
|---|---|
| costurados del acto sobre los **128 registros** de `docs/COSTURAS_INTERNAS.jsonl` | **1 de 7**; los otros seis sanos. La seccion 54.3 del informe declara **1 y 6**: **coincide** |
| corte registrado de esa unica costura | **el 5**, bloque **5 a 8**, `sim_bloque` 44,8 |
| frontera que `OP-F-02` publico en `01_FUENTES.md` | **1 a 4 / 5 a 8**: **el mismo sitio** |
| pasos de `brainstorming_divergente` hoy | **4**, exactamente el lado izquierdo del corte |
| los ocho pasos viejos, por `git` del **padre del commit de `OP-F-02`** (`2d96e3d3~1`) | **8**, tal como el registro de costuras dice |
| los **1 a 4** viejos contra el nodo de hoy | **4 de 4 IDENTICOS**, impresos uno al lado del otro |
| los **5 a 8** viejos contra `ideacion_con_ia_en_la_sesion` | **4 de 4 IDENTICOS**, y el destino **cuelga del cableado** |
| material perdido | **CERO**: 4 mas 4 igual a 8 |

> **DISCUTIBLE MARCADO 1, y lo marco antes de saber si acierto: NO volvi a correr
> `scripts/costuras_internas.py`.** Ese instrumento **se declara MAL CALIBRADO en su propia
> salida** desde la vuelta 34 (*INSTRUMENTO MAL CALIBRADO. No entrega nada*), y el encargo dice que
> **si una operacion NECESITA su cifra, eso es guarda en rojo y se para**. **Sostengo que
> `OP-D-04` no la necesita:** su frontera esta **publicada** en `01_FUENTES.md` y su corte esta
> **registrado con fecha** en `COSTURAS_INTERNAS.jsonl`, asi que la operacion se ejecuta sobre
> papel sellado y no sobre una medicion nueva. **Preguntar si hoy nacio una costura que nadie
> registro seria abrir alcance que ninguna operacion escribio.** Quien sostenga que un destejido
> exige medir las costuras del dia dira que aqui habia que parar.

### 3.3 `P.5`: LA MEDICION, y los tres gemelos salen los tres rancios

Instrumento `scripts/loop/vuelta37_p5_opd04.py`, **sucesor declarado** de
`vuelta35_pares_opd03.py` y `vuelta35_rancios.py`, que **junta las dos varas en uno** porque la
vuelta 35 tuvo que cruzar dos salidas a mano. Salida `SALIDA_V37_OPD04_P5.txt`.

| medicion | resultado |
|---|---|
| pares internos posibles de siete nodos | **21** |
| con veredicto en el archivo | **8** (234, 585, 586, 823, 834, 844, 885, 943) |
| **sin registro** | **13** |
| contraste contra la seccion 54.3 del informe | los **siete pares `A`** que atribuye al acto **son los siete `A` de hoy**; ademas aparece el **585 en `D`**, que el informe no lista |
| marcados por la **vara de fecha** | **4**: 585, 823, 834 y 844, los cuatro por lo mismo, `brainstorming_divergente` cambio el 2026-08-14 |
| confirmados por la **vara de texto** | **los 4**: de 8 a 4 pasos, y **el otro lado de cada par IDENTICO** |
| **RANCIOS de clase `A`** | **823, 834 y 844: EXACTAMENTE los tres gemelos** que la nota de la operacion manda al final |

### 3.4 LAS CUATRO RELECTURAS: **NINGUNA CAMBIA DE CLASE, y eso es el hallazgo**

**585 `D` a `D`, 823 `A` a `A`, 834 `A` a `A`, 844 `A` a `A`.** El marcador recomputado tras el
volcado da **n 3.388, A 575, B 83, C 8, D 2.722**, **identico** al que la guarda 4 del constructor
escribio **antes** de volcar.

**POR QUE NO CAE NINGUNA, y es medible:** **las tres razones de los gemelos habian localizado ellas
mismas el solape en los pasos 1 a 4 citando el banco `9.9`**, o sea en el lado que la cirugia iba a
dejar en pie. **Acertaron las tres.** Es lo contrario de lo que paso en `OP-D-03`, donde las cinco
razones rancias se apoyaban en material que las cirugias ya se habian llevado.

**LO QUE SI ENVEJECIO Y SE CORRIGE, con la vieja entera debajo en las cuatro:**

| puesto | lo que envejecio | lo que no |
|---:|---|---|
| **823** | *lo propio de `brainstorming_divergente` son el registro visual y **el bloque de IA entero***: el bloque **ya no esta** | el nucleo compartido, entero; y `brainstorming_efectivo` conserva su paso 3, la condicion social |
| **834** | solo la salvedad del `9.9` sobre **una juntura que ya no existe** | **todo lo demas**: ni una linea de contenido dejo de ser cierta. Es el caso mas limpio de los cuatro |
| **844** | solo la nota de costura | **los tres gestos propios** que listaba siguen los tres, y la vara se re-corrio hoy: el `9.6.2` **no** se cumple (cruza dos pasos), asi que decide el segundo polo del `9.22`, **linea en los dos sentidos** |
| **585** | la descripcion incluia **cuatro gestos de IA** que hoy no estan en el nodo | el argumento entero (*la sesion contra la disciplina mental*), que **nunca colgo de ese bloque** |

**El constructor del lote (`scripts/loop/vuelta37_build_lote_p5.py`) COPIA LA RAZON VIEJA DEL
ARCHIVO POR MAQUINA** y aborta si no queda literal dentro. **Ni una letra de la razon vieja se
tecleo.**

### 3.5 LAS TRECE LECTURAS DIRIGIDAS, `LD-83` a `LD-95`

**Guarda previa** (`scripts/loop/vuelta37_ld_opd04.py`, salida `SALIDA_V37_LD_OPD04.txt`):
**barrido de `docs/` entero por `LD-` mas digitos: el mas alto escrito es el 82**, asi que la tanda
arranca en el 83; **los trece buscados en las 3.388 filas de `docs/INTRA_DOMINIO_PARES.jsonl`:
ninguno esta en la cola**, asi que son lectura dirigida y **`n` no se mueve**; y **las 21 aristas
internas medidas en los dos sentidos y resueltas por alias (`P.1`): solo DOS pares tienen arista**,
y las dos la tienen en los dos sentidos.

| LD | par | clase | arista |
|---|---|:---:|---|
| **83** | `brainstorming_divergente` / `construir_sobre_ideas_ajenas` | **D** | madre e hijo, **ARISTA QUE FALTA** |
| **84** | `brainstorming_divergente` / `design_attitude_vs_decision_attitude` | **D** | no, y no se declara |
| **85** | `brainstorming_efectivo` / `generar_multiples_opciones` | **D** | no |
| **86** | `brainstorming_efectivo` / `pensamiento_convergente_divergente` | **D** | **ya puesta, en los dos sentidos** |
| **87** | `brainstorming_efectivo` / `design_attitude_vs_decision_attitude` | **D** | no |
| **88** | `reglas_brainstorming` / `generar_multiples_opciones` | **D** | no |
| **89** | `reglas_brainstorming` / `construir_sobre_ideas_ajenas` | **D** | no. **El solape mas fino de la tanda** |
| **90** | `reglas_brainstorming` / `pensamiento_convergente_divergente` | **D** | no |
| **91** | `reglas_brainstorming` / `design_attitude_vs_decision_attitude` | **D** | no. **Los dos del mismo libro** |
| **92** | `generar_multiples_opciones` / `construir_sobre_ideas_ajenas` | **D** | madre e hijo, **ya puesta en los dos sentidos** |
| **93** | `generar_multiples_opciones` / `design_attitude_vs_decision_attitude` | **A** | fusion, no enlace |
| **94** | `construir_sobre_ideas_ajenas` / `pensamiento_convergente_divergente` | **D** | no |
| **95** | `construir_sobre_ideas_ajenas` / `design_attitude_vs_decision_attitude` | **D** | no |

**SALDO: DOCE `D` y UNA `A`.** El `LD-86` cierra una observacion que el puesto **585** habia dejado
escrita el 10 ago 2026 y que nadie habia leido: *`pensamiento_convergente_divergente` es vecino del
racimo sin ser miembro, y la mesa tendra que mirarlo*. **Hoy esta leido.**

### 3.6 LA RESPUESTA DE `P.5`: dos triangulos, un colgado y **el primer puente TRIPLE**

Con **21 de 21** leidos (`scripts/loop/vuelta37_acto_opd04.py`, salida
`SALIDA_V37_OPD04_ACTO.txt`), **reparto 8 `A` y 13 `D`**:

| subconjunto **cerrado** (todos sus pares internos en `A`) | sus pares | que es |
|---|---|---|
| `brainstorming_divergente`, `brainstorming_efectivo`, `reglas_brainstorming` | **823, 834, 234** | **EL TALLER** |
| `generar_multiples_opciones`, `pensamiento_convergente_divergente`, `design_attitude_vs_decision_attitude` | **943, `LD-93`, 885** | **LA ALTERNANCIA** |
| `brainstorming_divergente`, `generar_multiples_opciones` | **844** | **el puente entre los dos** |
| `brainstorming_efectivo`, `construir_sobre_ideas_ajenas` | **586** | **el nodo colgado** |

**Y `P.10` da TRES NODOS PUENTE, cuando el archivo solo conocia el simple y el doble:**

| puente | sus `A` | las `D` que enfrentan a sus extremos |
|---|---|---|
| `brainstorming_divergente` | 823, 834, 844 | `LD-85` y `LD-88` |
| `brainstorming_efectivo` | 823, 234, 586 | `LD-83` y `LD-89` |
| `generar_multiples_opciones` | 844, 943, `LD-93` | `LD-84` y **585** |

> **`P.10` ya habia escrito que un puente doble no es un punto debil sino una costura. AQUI SON
> TRES, y son los mismos nodos que la operacion llama gemelos.**

### 3.7 LA PARADA DE LA FUSION, con sus tres motivos medidos

**MOTIVO 1: NO HAY SUPERVIVIENTE, ni escrito ni deducible.** Campo `superviviente` en **`null`**,
leido hoy. Especie de `9.3.1` **con su correccion del 18 ago 2026** (la prueba se hace **solo sobre
los pares `A`**): **POR ELEGIR**, y por el peor camino: **de los OCHO pares `A`, CERO nombran
ganador en su razon.** No hay **ni una victoria citable** de la que tirar. Y dos de esos ocho, el
**823** y el **834**, dicen literalmente que **no se pelea la clase porque la decision ya esta
tomada en otro sitio**, la mesa del racimo. **`P.8` desempata a contenido empatado; aqui el
contenido no ha hablado.**

**MOTIVO 2: TRES NODOS PUENTE, y `P.10` prohibe expresamente fundir la componente entera** (*el
cierre transitivo no lee: cuenta*). Su tercera salida, **fundir solo el cerrado y enlazar el
resto**, aqui da **DOS triangulos y por tanto DOS supervivientes**, y **la forma final de la
operacion no la escribe ninguna pagina**: la seccion **54.6** del informe lo dice desde el 11 ago
2026, *no dice si los siete deben quedar en uno, en dos o en cuatro*.

**MOTIVO 3: EL TRIANGULO DEL TALLER ES UN RACIMO MIXTO AL QUE LE FALTA UN MIEMBRO.** Medido hoy en
`docs/RACIMOS_MIEMBROS.jsonl`: el racimo **Las reglas del brainstorming** tiene **CUATRO** miembros
y el cuarto es **`brainstorming`, de `quality`**, fuera del acto. `MESA_RACIMOS.md` advierte que
**podar el lado del nucleo de un racimo mixto cambia el gradiente del mundo que lo acompana**, y
**`P.5` no da puerta para leerlo**: su alcance es el acto en operacion, **nunca fuera**. **Medido
tambien: ninguna operacion de la fase 06 nombra a estos nodos**, asi que esa mesa **no esta escrita
como operacion**.

**`docs/loop/paradas/2026-08-19-fusion-opd04.md`** trae las tres decisiones con sus opciones, el
cableado de `P.8` medido como contraste, y mi recomendacion.

**Y EL MODO CONTINUO MANDA DETENERSE AQUI Y ME DETENGO:** *cualquier operacion cuyo texto no
alcance para ejecutarse sin decidir detiene al ejecutor y convoca al auditor en la vuelta
siguiente*. **No se abrio `OP-D-05` ni ninguna otra.**

---

## 4. LAS GUARDAS DEL MODO CONTINUO, una por una y todas por corrida propia de hoy

| guarda que el encargo exige | resultado |
|---|---|
| **simulacion previa sobre copia en memoria** | **no aplica y se dice por que**: esta vuelta **no ejecuto ninguna operacion sobre nodos**. Los cuatro instrumentos que tocan algo escriben en `docs/`, y los tres que escriben en ficheros sellados **releen y verifican tras escribir** |
| **`Gate 0` en verde tras cada fase** | **exit 0, `GATE 0: OK`**, 20 `[OK]` y 0 `[FALLO]`, 3.853 compilados, 3.538 activos y 315 deprecados, simetria 0. Corrido **dos veces**, tras las relecturas y al cierre |
| **derivado byte igual** | **SI**, tras el **ciclo entero** (`run_phase1 --reaplico-curaduria`, `etiquetas_de_cara --aplicar` con 71, `sync_assets_web` con seis assets): `git status` sobre `dataset/` y `web/` sale **vacio** |
| **suites en verde** | **motor 25 de 25** (`engine/run_all_tests.py`, exit 0); **web 80 ficheros, 1.030 pasadas, 3 saltadas**, exit 0; **`tsc --noEmit` cero lineas**, exit 0 |
| **caso positivo de cada operacion** | **el destejido de `OP-D-04` lleva el suyo y es de la especie mas fuerte**: los ocho pasos viejos leidos por `git` del padre del commit de `OP-F-02` y comparados **uno a uno** contra los dos nodos de hoy, 4 de 4 y 4 de 4 identicos. **No es un conteo: es el texto** |
| **cero duplicadas o auto-aristas tras resolver** | **no aplica**: cero fusiones, cero redirecciones. El recomputo lo confirma por su lado, **1 auto-arista en todo el archivo** y es la conocida del 386 |
| **barrido del `9.10` en el mismo acto de cada volcado** | **corrido**, `scripts/loop/vuelta37_barrido_910.py`, **117 candidatos** listados sin truncar |
| **toda cifra publicada de una corrida de ESTA vuelta** | **si**. La unica excepcion declarada es el discutible 1 |
| **`costuras_internas.py` mal calibrado** | **no se necesito su cifra**: ver el discutible 1 |
| **verificador de mapas de destejido** | **3 tablas, 17 filas, 0 discrepancias, OK**, y el instrumento **declara en voz alta** que sin `--json` corre solo la vara 1 |
| **recomputo entero** | **actos 333**, nodos con al menos una `A` **845**, `A` crudas **575**, pares distintos del retrato **574**, y **las CUATRO comprobaciones del `08_VERIFICACION` OK** |

---

## 5. LAS CORRECCIONES DECLARADAS DE ESTA VUELTA, incluidas las mias

1. **UNA CIFRA MIA, MAL MEDIDA Y CORREGIDA SIN BORRAR EL TEXTO VIEJO.** El comentario que puse en
   `scripts/loop/vuelta37_aviso_v35.py` decia que el archivo guarda `puesto_intra` **como cadena**.
   **ES FALSO: contadas hoy las 3.388 lineas, las 3.388 lo traen ENTERO.** La causa esta escrita
   dentro del propio fichero: **la medicion que lo sostenia imprimia sus propios valores pasados
   por `str()`**, asi que todo salia cadena por construccion. **Un instrumento que mide su propia
   impresion no mide nada.** La comparacion del codigo se hace por `str()` en los dos lados y por
   eso funcionaba igual; **lo que estaba mal era la afirmacion, no el resultado.**
2. **DOS FALLOS DE CAMPO QUE LAS GUARDAS CAZARON EN VEZ DE CALLARSE**, y los dos quedan escritos en
   el docstring del instrumento que los sufrio: el archivo de veredictos nombra el puesto
   `puesto_intra` y no `puesto` (la guarda 3 lo canto con **seis AUSENTES**); y
   `INDICE_ROJO_DECLARADO.jsonl` nombra el nodo `id` y no `node_id` (**revento con `KeyError`** en
   vez de devolver una lista vacia y darla por buena).
3. **TRES AVISOS DE CORTE FECHADOS**, sin borrar nada, en las tres paginas que presentaban la
   costura de `brainstorming_divergente` **como viva**: `BANCO_DE_TEXTOS.md` seccion `9.9`,
   `INTRA_DOMINIO_INFORME.md` seccion 26.5 y `FICHA_SUBFUSION_GRADIENTE.md`. **Las tres salen
   REFORZADAS**: predijeron que el bloque 1 a 4 sobreviviria a la cirugia, y esta vuelta lo
   comprobo. **Es la primera vez que un ejemplar del `9.9` se verifica DESPUES de la cirugia que
   anticipaba.**
4. **LA NOTA DE `OP-D-04`**, con la vieja de **582 caracteres LITERAL dentro** de la nueva de
   **4.973**, y `estado`, `superviviente`, `nodos` y `eliminar` **sin tocar**, verificado releyendo
   el fichero tras escribir. **71 operaciones antes y despues.**

---

## 6. LOS DISCUTIBLES MARCADOS, todos ANTES de saber si acierto

1. **NO RE-CORRER `costuras_internas.py`** para el destejido. Detalle en 3.2. **Es el mas
   estructural**: si el auditor sostiene que un destejido exige medir las costuras del dia, esta
   vuelta debio parar en el paso 2.
2. **`LD-93`, la unica `A` de la tanda, y el mas fuerte de todos.** `generar_multiples_opciones`
   contra `design_attitude_vs_decision_attitude`. **Los entregables NO coinciden** (*un set de 3-5
   alternativas evaluadas* contra *mentalidad y proceso de trabajo del equipo*) y el `9.6.2` dice
   que **los entregables deciden mas rapido que los pasos**. **Lo que sostengo** es que esa senal
   esta escrita para detectar la **direccion** de un par madre e hijo, y **aqui no hay madre e
   hijo**: ninguno cabe dentro de un paso del otro, asi que aplica el `9.22`, que pesa **lineas** y
   no productos. **Quien de mas peso al entregable leera `D`, y entonces el triangulo de la
   alternancia deja de ser triangulo y la parada cambia de forma.**
3. **`LD-83`, `D` donde el `586` dio `A` con el mismo hijo.** Lo que los separa es medible: el paso
   2 de `brainstorming_efectivo` dice *por encima de generar ideas propias de forma aislada* y **eso
   ya cubre el no acaparar**; el paso 2 de `brainstorming_divergente` **no lo dice**. **Con una
   madre queda una linea fuera y con la otra quedan dos.** Quien sostenga que dos lineas siguen
   siendo lineas dira que este par tambien es `A`.
4. **`LD-91`, sin arista entre dos nodos del mismo libro.** El paso 2 de
   `design_attitude_vs_decision_attitude` se puede leer como linea madre de la sesion entera. **Lo
   que lo impide**, corrido hoy: `reglas_brainstorming` **no cabe entero dentro de ese paso**,
   porque su paso 1 y su paso 3 caen mas cerca del paso 3 de la otra.
5. **LAS TRES `A` QUE NO CAEN (823, 834, 844).** Las dos primeras se sostienen por la **regla
   `FAMILIA DECLARADA`** y no por la vara del contenido, y tras la cirugia
   `brainstorming_divergente` conserva **tres gestos propios de cuatro pasos**, que es mas de lo que
   tenia cuando la razon vieja lo llamo repeticion. **Lo que lo impide** es que la regla escrita
   manda **no pelear** la clase de un par de racimo declarado.
6. **DECLARAR LA PARADA EN VEZ DE FUNDIR EL TRIANGULO DE LA ALTERNANCIA.** Ese triangulo **no**
   tiene el problema del racimo mixto, asi que alguien puede decir que ahi si se podia fundir. **Lo
   que lo impide, y son dos cosas**: sus tres pares `A` **tampoco nombran ganador** (motivo 1 vale
   igual), y **uno de los tres es `LD-93`, lectura mia de hoy y sin auditar**. **Fundir sobre una
   lectura propia sin auditar es exactamente lo que la vuelta 36 pidio no volver a hacer.**
7. **CONTAR LAS LECTURAS DIRIGIDAS COMO CLASE DEL ACTO.** El instrumento del acto **junta dos
   fuentes**, el archivo y `LECTURAS_DIRIGIDAS.md`, porque una dirigida no existe en el archivo. Lo
   sostengo porque es lo que `OP-D-02` y `OP-D-03` hicieron con `LD-72` a `LD-81`. **Pero la
   consecuencia hay que decirla: `scripts/plan/recomputo_3388.py` NO lee ese fichero**, asi que
   **la `A` de `LD-93` no entra en el recomputo**. Aqui no cambia nada (los siete ya estaban en la
   misma componente por el 844 y el 586), **pero un dia una `A` dirigida unira dos componentes y el
   recomputo no lo vera.** Va como pendiente, abajo.

---

## 7. PENDIENTES DE DOCTRINA

1. **EL RECOMPUTO NO VE LAS LECTURAS DIRIGIDAS.** Medido hoy: `grep` de `LECTURAS_DIRIGIDAS` y de
   `LD-` sobre `scripts/plan/recomputo_3388.py` da **cero**. Las dirigidas **`A`** no entran en el
   cierre transitivo. **Hoy es inocuo y esta comprobado**; el dia que no lo sea, el censo de actos
   mentira en silencio. **Es del fundador**, y no bloquea.
2. **`P.5` NO ALCANZA AL CUARTO MIEMBRO DE UN RACIMO MIXTO.** Su alcance es el acto en operacion,
   *nunca fuera*, y aqui el acto contiene **tres cuartas partes de un racimo declarado**. **No hay
   pagina que diga que se hace con el cuarto.** Es el motivo 3 de la parada y **es del fundador**.
3. **EL ESTADO `HECHA` SIGUE SIN EXISTIR EN EL ESQUEMA** (pendiente heredado de la vuelta 36, vivo
   y medido hoy: **71 operaciones y las 71 en `LISTA`**). `OP-D-04` queda con sus pasos 1 y 2 hechos
   y **el campo dice `LISTA`**, igual que `OP-F-02` y `OP-F-03`, que estan enteras.
4. **QUE HACE EL PLAN CON UN ACTO QUE SE PARTE EN DOS** (heredado, y esta vuelta lo hace concreto):
   si la decision 1 de la parada sale por dos fusiones, **el acto 1 del cierre transitivo deja de
   ser un acto y pasa a ser dos**, y el inventario tiene una entrada `acto` con los siete miembros.
5. **PENDIENTES 5 A 9 DE LA VUELTA 36: siguen vivos y ninguno bloquea**, incluido el 6, la
   calibracion de `costuras_internas.py`.

---

## 8. PREGUNTAS QUE TRAIGO, porque no las puedo medir

1. **La `54.6` del informe dice que el acto de siete puede quedar en uno, en dos o en cuatro. La
   medicion de hoy dice que en `A` cerrada solo hay dos formas posibles: dos triangulos, o un
   nodo.** Falta saber si el fundador cuenta **`construir_sobre_ideas_ajenas`** como tercer nodo
   vivo o como material que viaja al superviviente del taller por el **586**.
2. **Si el auditor voltea `LD-93` a `D`**, el triangulo de la alternancia se rompe y quedan **dos
   pares `A` sueltos** (943 y 885) con `generar_multiples_opciones` de puente. **La parada seguiria
   siendo parada, pero la decision 1 cambiaria de opciones.** Lo digo antes de que se lea, no
   despues.

---

## 9. EL SALDO EN UNA TABLA

| | |
|---|---:|
| operaciones ejecutadas enteras | **0** |
| operaciones con pasos hechos | **1** (`OP-D-04`: pasos 1 y 2, mas el acto leido entero) |
| **nodos tocados** | **0** |
| veredictos releidos y volcados | **4** |
| de ellos, con cambio de clase | **0** |
| lecturas dirigidas nuevas | **13** (`LD-83` a `LD-95`): 12 `D`, 1 `A` |
| pares del acto leidos, de 21 | **21** |
| nodos puente encontrados | **3**, el primer triple del archivo |
| aristas declaradas para la fase 04 | **1** (`LD-83`) |
| avisos de corte fechados | **4** (la propuesta de la 35, mas tres paginas de doctrina) |
| **marcador al cierre** | **n 3.388, A 575, B 83, C 8, D 2.722** |
| **diferencia entre apertura y cierre** | **cuatro lineas, las cuatro el rotulo** |
| paradas declaradas | **1**, la fusion de `OP-D-04` |
