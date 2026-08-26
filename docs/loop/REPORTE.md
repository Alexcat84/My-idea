# REPORTE DE LA VUELTA 71: EL LOTE G DEL TRAMO UNICO DE `OP-U-02`, CINCO FUSIONES, CERO DECLARADOS Y CERO COLISIONES FABRICADAS

**Fase III, ejecucion continua. Rama `pasada-unica`. 26 ago 2026.**

**FECHA POR DOS RELOJES, CORRIDOS POR MI:** el reloj del sistema da **2026-08-26** y `git log -1
--date=format` sobre el ultimo commit da **2026-08-26 05:14**. **Toda cifra de este reporte tiene ese
corte.** La vuelta abrio con el arbol limpio en `2d22e7e6` y **no cruzo medianoche**.

**EL CONTADOR DE PARADA ENTRO A ESTA VUELTA EN UNO DE DOS** (acta 70, seccion 8). **Lo que este
reporte trae para ese contador va dicho de frente y no al final:** cero veredictos movidos, cero
colisiones fabricadas, y **una discrepancia con el acta que se declara en vez de copiarse** (seccion
2.1). **Las averias propias de la vuelta son SEIS y ninguna llego a una cifra publicada** (seccion 7).

---

## 1. LA CABECERA, TALLADA Y NO TECLEADA

**Generada entera con** `python scripts/loop/tallar_cabecera_reporte.py --vuelta 71` y **pegada sin
tocar una celda** ([`SALIDA_V71_CABECERA.txt`](SALIDA_V71_CABECERA.txt)). **La celda que no salga de
un instrumento no se escribe.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.214 / 639 / 17.612 | **3.853 / 3.204 / 649 / 17.639** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 350 / 201 | **551 / 360 / 191** |
| actos (componentes) | 62 | **57** |
| actos `CERRADOS` / `ABIERTOS` | 26 / 36 | **26 / 31** |
| nodos en `CERRADOS` / `ABIERTOS` | 61 / 166 | **61 / 151** |
| cola de costuras | 1.441 | **1.442** |
| colisiones de clase vigentes | 7 | **7** |
| auto-pares (los dos lados al mismo vivo) | 273 | **278** |
| duplicadas historicas: grupos / nodos | 911 / 721 | **902 / 714** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (227 igual a 227; 201 igual a 201) | **TODAS OK (212 igual a 212; 191 igual a 191)** |

**LA APERTURA SE MIDIO ANTES DE LA PRIMERA OPERACION** (regla 1): los seis instrumentos de apertura
corrieron con el arbol limpio en `2d22e7e6`, **antes de escribir nada**, y `git status --porcelain`
tras correrlos dio **CERO ficheros rastreados movidos** (solo las salidas nuevas, sin trackear).
**EL CIERRE SE RECOMPUTO AL CIERRE**, despues de que las cinco fusiones y `run_phase1` movieran el
arbol.

> **LA LECCION DEL `D12` DEL ACTA 70, APLICADA DESDE EL PRIMER MINUTO Y POR ESO SIN NOTA DE
> PROCEDENCIA:** el marcador de apertura se tallo con **`recomputar_marcador.py`**, que es el
> instrumento cuyo formato el tallador lee, **y no con `vuelta38_marcador.py`**. **Esta vuelta no
> tiene averia 7.3 equivalente y el fichero de apertura no lleva ninguna declaracion dentro**, porque
> no le hace falta.

**LA APERTURA DE HOY CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 70 PUBLICO** (marcador 551 / 72 / 5 /
2.760, grafo 3.853 / 3.214 / 639 con 17.612 enlaces, retrato 551 / 350 / 201, 62 componentes, 26 y 36
sobre 61 y 166, cola 1.441, colisiones 7, auto-pares 273, duplicadas 911/721, 71 `LISTA`, 672 entradas
y las cuatro comprobaciones en 227 y 201), **que es el contraste que la regla 2 permite**: entre las
dos vueltas nadie movio dato.

**LA ARITMETICA DEL SALTO ES COHERENTE ENTERA:** cinco actos fundidos son **menos 5 componentes** (62
a 57), **menos 15 nodos abiertos** (166 a 151), **menos 10 vivos** (3.214 a 3.204) y **mas 10
deprecados** (639 a 649). El retrato sube 10 colapsos y baja 10 pares distintos (201 a 191), que es
**un par interno por acto colapsando a auto-arista**, y los auto-pares suben exactamente esos **5**
(273 a 278). Las duplicadas bajan **9** por `P.16`. Los enlaces suben **27**.

> **LA COLA DE COSTURAS SUBE UNO Y NO SE DEJA COMO UN MAS UNO MUDO**, porque es el costo mas caro de
> este lote y **lo mide un instrumento, no una impresion**
> ([`SALIDA_V71_COLA_DELTA.txt`](SALIDA_V71_COLA_DELTA.txt)): **ENTRAN TRES y SALEN DOS**. Los tres
> que entran son **supervivientes de este lote** (`defensas_en_profundidad_3` con 7 pasos,
> `segmentos_de_clientes_problema_necesidad` con 6 y `traction_goal` con 7); los dos que salen son
> **absorbidos** que dejan de ser vivos. **Tres de los cinco supervivientes de esta vuelta quedan
> citados por la cola de costuras, y va MARCADO (`D6`).**

---

## 2. TAREA 1: EL REGISTRO DEL ACTA 70 Y LAS DOS CORRECCIONES DECLARADAS

`python scripts/loop/vuelta71_registrar_acta70.py`
([`SALIDA_V71_REGISTRO_ACTA70.txt`](SALIDA_V71_REGISTRO_ACTA70.txt)), adosado al final de
[`../plan/03_FUSIONES.md`](../plan/03_FUSIONES.md) **sin reescribir ni una linea de arriba**
(`git show --numstat` sobre `c1859ed5`: **`222 0`**).

### 2.1 **LA CAIDA DE CIFRA PUBLICADA, REGISTRADA, Y UNA DISCREPANCIA CON EL ACTA QUE SE DECLARA**

**Lo que queda registrado va primero porque es lo que mueve el contador de parada:** el cableado de
los `actos 34` y `36` se publico con el conteo **CRUDO** de las listas, la causa medida (los ids sin
pasar por el resolutor), la letra incumplida (`P.1` citada en el docstring del propio instrumento), lo
que **NO** se movio (ningun ganador cambia y el cableado no decidio en ninguno de los dos actos), y
**el contador en UNA TANDA de dos**.

> **Y AQUI VA LA DISCREPANCIA, DECLARADA EN VEZ DE RESUELTA COPIANDO** (regla 2: un acta previa se
> cita como contraste, y si discrepa de la medicion de hoy **la discrepancia se declara**).
>
> | | medido HOY por mi | lo que el acta 70 dice |
> |---|---|---|
> | **las cifras del instrumento** | **6 contra 4 y 2** y **4 contra 3 y 2**, re-corridas por mi en un worktree sobre `bf4f20f9` ([`SALIDA_V71_VARAS_34_36_PRE_FUSION.txt`](SALIDA_V71_VARAS_34_36_PRE_FUSION.txt)) | **las mismas**. **CALZA** |
> | **la SEDE de las celdas malas** | `docs/plan/03_FUSIONES.md` trae **CERO** ocurrencias de `6 contra 5 y 2` y de `5 contra 4 y 3`, contado por maquina. Viven en **`PLAN_V70_OPU02_LOTE_F.json`** (1 y 1) y en **`scripts/loop/_v70_lote_f.py`** (1 y 1), y en forma abreviada en la tabla 3.2 del reporte de la vuelta 70 (`6 contra 5` y `5 contra 4`) | *el registro del lote F en docs/plan/03_FUSIONES.md publica...* | **NO CALZA** |
>
> **QUE HAGO CON ESO, Y POR QUE:** **la correccion se adosa igual al registro**, que es lo que el
> encargo manda y **donde el registro queda**; **el plan ejecutado NO se re-sella** (carril del `D15`
> del acta 68), asi que la celda mala del plan **se queda entera y sin tachar**; y **la sede del
> reporte de la vuelta 70 desaparece sola** porque este fichero la sobrescribe. **La discrepancia va
> MARCADA (`D15`).**

### 2.2 **CORRECCION DECLARADA, PRIMERA: LAS DOS CELDAS DE CABLEADO**

**Adosada al final del registro, sin tachar ni reescribir lo de arriba**, con las cifras **leidas de
la columna `cab` del instrumento** y no copiadas del acta.

| acto | cableado, medido por mi | quien apunta | decidio? |
|---:|---|---|---|
| **34** | **6 contra 4 y 2** | `ciclo_de_culpa` | **NO**: `TODAS DE ACUERDO`, el contenido no empata |
| **36** | **4 contra 3 y 2** | `matriz_de_control_de_proceso` | **NO**: `CHOCAN`, decide la pieza declarada |

**LO QUE SE CORRIGE ES LA CIFRA, NO LA DECISION**, y por eso es una correccion y no una reapertura:
**los dos ganadores del cableado son los mismos con las cifras crudas y con las buenas**.

### 2.3 **CORRECCION DECLARADA, SEGUNDA: EL DEFECTO DE `--base` PASA DE `6` A `7`**

**Aplicada sobre `scripts/loop/vuelta65_colisiones_esperadas.py` por el mismo carril con que la vuelta
67 lo paso de `2` a `4` y la 70 de `4` a `6`.** **EL TEXTO VIEJO SE QUEDA ENTERO Y NO SE TACHA:** el
docstring conserva **las tres correcciones anteriores** y **las DOS llamadas viejas quedan citadas
verbatim en un comentario justo encima de la nueva**. **LA ARITMETICA NO SE TOCA**: la guarda sigue
**midiendo la base sobre el arbol** y cayendo en `ROJO` si la medida no calza con la declarada. **Es
el cuarto escalon del mismo carril: 2 por el acta 64, 4 por el acta 66, 6 por el acta 69 y 7 por el
acta 70.** **Y la correccion se probo sola:** la corrida de las esperadas de esta vuelta **no paso
`--base` a mano** y el instrumento midio **7** sobre el arbol y calzo.

### 2.4 **LA GUARDA DE CITAS: COPIADA POR EXTRACCION, NO IMPORTADA Y NO RETECLEADA**

**El acta 68 escribio la regla en su `D14` y las actas 69 y 70 la dejaron en pie:** importar vale
**dentro de la misma vuelta**; **copiar** es el carril que protege a los registradores **de vueltas
distintas**. El registrador del acta 70 es de otra vuelta que su ancestro, asi que **la maquina se
copio entera**, y **la copia la hace `scripts/loop/_v71_construir_registrador_acta.py` POR
EXTRACCION**, con **un assert por pieza**, y **despues comprueba que la maquina aparece LITERAL en el
destino**. **El registrador del lote `G`, que es de ESTA vuelta, si la importa.**

| mecanismo | medido en esta vuelta |
|---|---|
| **1. las citas se derivan por aguja** | **80 agujas** en el registro del acta y **16** en el del lote, **cero tecleadas** |
| **2. el texto nuevo se coteja antes de escribir** | **13** citas canonicas en el del acta y **12** en el del lote, **MALAS 0** en los dos |
| **la red ancha** (todo numero de 3 a 5 digitos en negrita) | **87** en el del acta (8 declarados) y **36** en el del lote (11 declarados) |
| **las agujas NEGATIVAS** | **3, y las tres de sustancia**: la linea de las cifras CRUDAS **NO** contiene la cifra buena (si estuvieran en la misma linea, la correccion citaria su propio error como remedio); la linea de la base **NO** dice `aritmetica`; y la linea de los actos que FUNDEN con su puerta **NO** nombra al `44`, que es el que cierra `DECLARADO`. **Las tres `OK`** |
| **cero citas muertas** | **80 de 80** y **16 de 16**, y la guarda MORDIO: la primera corrida cayo en `ROJO` con una aguja sin usar |
| **idempotencia** | **MUERDE en los dos** (`YA ADOSADA` y `YA ADOSADO` en la segunda corrida) |
| **re-cotejo tras adosar** | **`OK (80 de 80)`** y **`OK (16 de 16)`** |

> **LA MAQUINA NO CRECE EN ESTA VUELTA, Y VA DICHO PORQUE ES UNA ADJUDICACION APLICADA SOBRE SI
> MISMA:** la adjudicacion 3 del acta 69 congelo las tablas de los registradores. **Cero mecanismos
> nuevos, cero filas nuevas, cero columnas nuevas**, y `tabla_declarado` **se copia entera aunque este
> lote no la use**. **El unico cambio declarado dentro de una funcion copiada es el nombre del fichero
> del tallador**, y va con su assert.

---

## 3. TAREA 2: EL LOTE G, DECLARADO AL ABRIRLO Y ENTREGADO ENTERO

**EL LOTE ABRE EN EL `ACTO 38`, QUE ES EL PRIMERO DEL TRAMO SIN DUENO MEDIDO**, y **LOS DOS SALTOS VAN
DECLARADOS con su cita**: el `acto 31` trae `OP-F-04-WEI` y `OP-S-04` y el `acto 37` trae `OP-S-07` en
`duenos_cualquier_operacion`, **leidos hoy del fichero fijado del tramo**
([`SALIDA_V71_DUENOS_Y_RACIMOS.txt`](SALIDA_V71_DUENOS_Y_RACIMOS.txt)), y **ninguno de los dos esta en
la cola de fusiones de `OP-U-02`**, asi que saltarlos **no rompe el prefijo sin saltos** (adjudicacion
2 del acta 69).

**SE DECLARARON CINCO ACTOS Y 15 NODOS, Y SE ENTREGARON LOS CINCO.**

| acto | miembros | cierra | **FORMA medida** | superviviente |
|---:|---:|---|---|---|
| **38** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `segmentos_de_clientes_problema_necesidad` |
| **39** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `defensas_en_profundidad_3` |
| **40** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `traction_goal` |
| **41** | 3 | **FUNDIDO** | `TODAS DE ACUERDO` | `design_for_six_sigma_dfss` |
| **42** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `equipo_multifuncional_real` |

**ES EL SEGUNDO LOTE SEGUIDO SIN NINGUN `DECLARADO Y NO FUNDIDO`**, y **los motivos posibles ya no son
cuatro sino DOS** por la adjudicacion 4 del acta 70: **la guarda `1B` con dos o mas puertas** y **la
respuesta *DOS FAMILIAS* de `P.5`**. **Ninguno tiene sujeto aqui**, y los dos que quedaron sin sujeto
en todo el tramo (`P.10` y el `D` directo interno) **siguen sin el**, medido.

**LA GUARDA `1B` CORRE POR VACIO EN LOS CINCO ACTOS Y SE DICE EN VEZ DE CALLARSE:** **CERO puertas
dentro de cada acto**, medido con `varas_n_arias_del_tramo.py` contra el universo protegido de **256**
ids ([`SALIDA_V71_VARAS_N_ARIAS.txt`](SALIDA_V71_VARAS_N_ARIAS.txt)). **Es el segundo lote seguido en
el que la guarda no tiene ni un sujeto**, y **es la ultima vez que va a poder decirse**: el `acto 44`,
que trae DOS puertas, entra en el prefijo que viene.

**EL TOPE DEL PREFIJO NO ES ESTRUCTURAL SINO DE LOTE, Y SE DICE:** el siguiente sin dueno y sin puerta
es el **`acto 43`**, y el tope cae antes de el **porque el encargo fija CINCO actos**, no porque el
`43` tenga nada que lo impida. **Esta vuelta NO leyo el `acto 43`** y lo dice en vez de dejarlo
implicito: el dossier y las varas de este lote cubren **exactamente los cinco actos entregados**.

### 3.1 **`P.5` CONTESTADA ACTO POR ACTO, SOBRE EL TEXTO ESTABLE**

**El acto se leyo ENTERO** con `python scripts/loop/dossier_del_tramo.py --tramo
docs/loop/TRAMO_UNICO_OPU02_V64.jsonl --actos 38,39,40,41,42`
([`SALIDA_V71_DOSSIER_LOTE_G.txt`](SALIDA_V71_DOSSIER_LOTE_G.txt), **310 lineas**), con **todos sus
pares internos y su razon entera**.

| acto | libro | pares `A` | pares `D` | puentes | triangulos | puertas | **una familia o dos** |
|---:|---|---:|---:|---:|---:|---:|---|
| **38** | Blank (los 3) | 2 | 0 | 0 | 0 | 0 | **UNA**, y la declara el archivo: el **1216** mide que *la misma escala de cuatro niveles aparece ya en TRES etiquetados distintos en esta zona* |
| **39** | Reason (los 3) | 2 | 0 | 0 | 0 | 0 | **UNA**, y **no la contesta una lectura mia sino una DECISION APROBADA**: `INVENTARIO.jsonl` trae la familia `defensas_en_profundidad` con los TRES miembros y con la nota *DECISION 4 de la mesa de racimos, aprobada el 9 ago 2026: familia unica, fusion con alias* |
| **40** | Weinberg (los 3) | 2 | 0 | 0 | 0 | 0 | **UNA**, y el **824** cierra con *la familia de la meta de traccion llega a TRES nodos y dos pares leidos* |
| **41** | Juran (los 3) | 2 | 0 | 0 | 0 | 0 | **UNA**: los dos absorbidos son *las cinco letras de DMADV* contadas dos veces, dicho por las dos razones |
| **42** | Cooper (los 3) | 2 | 0 | 0 | 0 | 0 | **UNA**, y el **672** los llama *gemelos del mismo libro sobre el mismo problema* |

**MEDIDO** con `python scripts/loop/vuelta65_puentes_del_tramo.py --tramo ... --detalle`
([`SALIDA_V71_PUENTES_TRAMO.txt`](SALIDA_V71_PUENTES_TRAMO.txt)), **con los ids pasados por el
resolutor (`P.1`)**, y las puertas con `varas_n_arias_del_tramo.py`.

**LA RESPUESTA *DOS FAMILIAS* DE `P.5` NO SE USO EN NINGUN ACTO, Y SE DICE**, porque un motivo sellado
que no se usa se cuenta como usado si nadie lo dice. **El acto donde estuvo mas cerca de usarse es el
`39`**, donde **las dos razones coronan supervivientes distintos**, **y por eso va marcado (`D5`)**.

### 3.2 **LAS VARAS POR FORMA, CON SU LETRA Y MEDIDAS POR INSTRUMENTO**

`python scripts/loop/varas_n_arias_del_tramo.py --tramo ... --actos 38,39,40,41,42`
([`SALIDA_V71_VARAS_N_ARIAS.txt`](SALIDA_V71_VARAS_N_ARIAS.txt)). **Formas contadas por el instrumento
sobre los cinco actos: 4 `UNA SOLA VARA` y 1 `TODAS DE ACUERDO`.** **TODA CIFRA DE CABLEADO DE ESTA
TABLA SALE DE LA COLUMNA `cab` DEL INSTRUMENTO**, que es la regla que la adjudicacion 3 del acta 70
dejo escrita, **y ninguna sale de contar listas**.

| acto | pasos | condiciones | cableado (columna `cab`) | **la letra que decide** |
|---:|---|---|---|---|
| **38** | **apuntan a `segmentos_de_clientes_problema_necesidad`** (5 contra 4 y 4) | empatan los 3 en 2 | apunta a `customer_segments_hypothesis` (12 contra 5 y 4) | **UNA SOLA VARA BASTA**, y el cableado solo habla a contenido empatado. **Margen de cableado en contra: el mas ancho del lote por esta via** |
| **39** | **apuntan a `defensas_en_profundidad_3`** (4 contra 3 y 3) | empatan dos en 2 | apunta a `defensas_en_profundidad` (11 contra 3 y 2) | **UNA SOLA VARA BASTA**, y ademas **el contenido declarado por el archivo apunta al mismo nodo**: el **2283** declara la figura *el hermano que corrige al hermano* |
| **40** | **apuntan a `traction_goal`** (5 contra 4 y 3) | empatan los 3 en 2 | **EMPATA a tres bandas** (3, 3 y 3) | **UNA SOLA VARA BASTA**, y **el cableado ni siquiera podria desempatar si le tocara**. Unico acto del lote asi |
| **41** | **apuntan a `design_for_six_sigma_dfss`** (6 contra 5 y 5) | al mismo (4 contra 2 y 3) | al mismo (12 contra 3 y 3) | **TODAS DE ACUERDO: se funde a su lado.** Las tres cuentas al mismo sitio |
| **42** | **EMPATAN en 5** entre los otros dos, **no apuntan** | **apuntan a `equipo_multifuncional_real`** (3 contra 2 y 2) | apunta a `equipo_multifuncional` (5 contra 4 y 2) | **UNA SOLA VARA BASTA, Y ES LA DE CONDICIONES.** El superviviente es **el miembro mas pequeno del acto** por pasos y por cableado |

**EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN**, y eso vale tambien para el sufijo `_3` del
superviviente del `acto 39` y para la palabra `real` del rotulo del superviviente del `acto 42`, que
son rotulo y no contenido. **Ninguna vara se teclea:** las tres cuentas por miembro salen del
instrumento.

### 3.3 **LAS CINCO FUSIONES, EN CIFRAS DEL INSTRUMENTO**

`python scripts/loop/fundir_por_plan.py --plan docs/loop/PLAN_V71_OPU02_LOTE_G.json --ejecutar`
([`SALIDA_V71_FUSION_LOTE_G.txt`](SALIDA_V71_FUSION_LOTE_G.txt)), **precedida de la simulacion sobre
copia en memoria** ([`SALIDA_V71_FUSION_SIMULADA.txt`](SALIDA_V71_FUSION_SIMULADA.txt)).

| | acto 38 | acto 39 | acto 40 | acto 41 | acto 42 | **el lote** |
|---|---:|---:|---:|---:|---:|---:|
| absorbidos | 2 | 2 | 2 | 2 | 2 | **10** |
| pasos del superviviente | 5 a **6** | 4 a **7** | 5 a **7** | 6 a 6 | 4 a **7** | |
| condiciones | 2 a **3** | 2 a 2 | 2 a 2 | 4 a 4 | 3 a 3 | |
| piezas repartidas | 12 | 9 | 11 | 15 | 14 | **61** |
| de ellas `APPEND` / `CUBIERTO` / `INCISO` | 2 / 8 / **2** | 3 / 5 / **1** | 2 / 8 / **1** | 0 / 15 / 0 | 3 / 10 / **1** | **10 / 46 / 5** |
| perdidas selladas en campo propio | 5 | 5 | 6 | 7 | 7 | **30** |

**TOTAL: 10 nodos mueren (3.214 vivos a 3.204). Ficheros tocados: 58. Redirecciones sobre nodos
vivos: 51.**

**LAS GUARDAS DE CADA FUSION, LAS CUATRO Y TODAS VERDES EN LAS CINCO:** guarda 1 (miembros vivos y
nomina completa), guarda **1B** (ningun **absorbido** es semilla ni extremo de puente), guarda 2
(cobertura exacta de indices, cero olvidos) y guarda 3 (cero repetidos literales).

**LOS CINCO `INCISO` SE EXTRAJERON DEL NODO Y SE COMPROBARON VERBATIM**, y sus pasos resultantes estan
impresos por el generador y **leidos uno a uno antes de sellar el plan**, que es lo que la averia 7.1
de la vuelta 70 dejo como habito:

- **acto 38, al paso 2:** *Clasifica el problema en la escala: latente, pasivo, activo o con una
  solución casera**, y también cuando aún no existe y tú le muestras una visión***
- **acto 38, al paso 3:** *Identifica si tu producto es indispensable (must-have) o solo agradable de
  tener (nice-to-have)**, determinando la intensidad del dolor que causa el problema***
- **acto 39, al paso 1:** *Mapear todas las capas de defensa del sistema (barreras físicas, sistemas
  de protección, procedimientos)**, clasificándolas en las siete funciones defensivas***
- **acto 40, al paso 1:** *Define un objetivo de tracción cuantificable y significativo para tu etapa
  actual de negocio**, en números concretos como cantidad de clientes y tasa de crecimiento mensual***
- **acto 42, al paso 1:** *Asigna un líder de proyecto dedicado y dale autoridad real, no solo la
  responsabilidad**, y elígelo con espíritu emprendedor***

**CERO `INCISO` EN EL ACTO 41, Y ES POR LA PUNTUACION** (carril del `D5` del acta 66): **los SEIS
pasos de su superviviente terminan en punto**, comprobado leyendolos, y un `INCISO` con nexo de coma
detras de un punto cae en la guarda de la **JUNTURA ROTA**. **No se forzo ninguno.**

**`P.16`, QUIEN FABRICA LIMPIA, EN EL MISMO COMMIT:** la fusion fabrico **9** duplicadas y **las
limpio en la misma corrida**; **0 auto-aristas** que retirar; **guarda A** (cero auto-aristas nuevas)
**OK**, **guarda B** (cero duplicadas nuevas tras resolver) **OK**, **guarda C** (los campos que esta
operacion no redacta, intactos: **25 de 25**) y **guarda D** (los 10 absorbidos conservan su texto
**INTACTO**) **OK**. El pasivo del censo propio de la guarda **baja 9** (889 a 880).

**`reanclar_por_resolutor.py` corrido ENTRE la fusion y `run_phase1`**
([`SALIDA_V71_REANCLAJE.txt`](SALIDA_V71_REANCLAJE.txt)): **UNA referencia re-anclada, y NO es un
cero**. Es un **rumbo** (`nucleo_le_sirve_a_todo_el_mundo`) que apuntaba a
`customer_segments_hypothesis` y pasa a `segmentos_de_clientes_problema_necesidad`. **El fundidor
redirige el GRAFO y no `scripts/rumbos/banco_rumbos.json`, y por eso el reanclaje hace falta**: la
vuelta 70 publico que ese fichero no se tocaba y **esta vuelta SI lo toca**, con su cifra y su motivo.

### 3.4 **EL DIFF DE DUPLICADAS, POR INSTRUMENTO Y CON LA APERTURA SACADA DE `git`**

`python scripts/loop/diff_duplicadas_por_resolutor.py --antes <git show c1859ed5:...> --despues
docs/plan/ARISTAS_DUPLICADAS.jsonl`
([`SALIDA_V71_DIFF_DUPLICADAS.txt`](SALIDA_V71_DIFF_DUPLICADAS.txt)).

> **GRUPOS FABRICADOS DE VERDAD: `0`.** **RENOMBRADOS: `0`.** Hay **7 que DESAPARECEN**, y **los siete
> son de la misma especie y estan nombrados uno a uno en la salida**: un vivo que apuntaba a **DOS
> miembros del mismo acto en el mismo campo** y que tras la fusion **hereda el destino una sola vez**.
> **909 grupos resueltos a 902.**

**EL CORTE DE *ANTES* SALE DE `git show` SOBRE EL COMMIT DE LA TAREA 1** (`c1859ed5`), **anterior a la
fusion**, y el de *despues* es el fichero **tras recompilar el grafo con `run_phase1`**, que es la
leccion de la averia 7.5 de la vuelta 68.

### 3.5 **EL CENSO DE COLISIONES: ESTE LOTE NO FABRICA NINGUNA, Y SE PUBLICA IGUAL**

`python scripts/loop/vuelta65_colisiones_esperadas.py --plan docs/loop/PLAN_V71_OPU02_LOTE_G.json`
([`SALIDA_V71_COLISIONES_ESPERADAS.txt`](SALIDA_V71_COLISIONES_ESPERADAS.txt)), **corrido sobre el
arbol de antes y simulando en memoria, sin tocar un nodo**. **La base entro por el DEFECTO del
instrumento, que es lo que la correccion de la TAREA 1 dejo en `7`: no hizo falta pasarla a mano, y la
guarda la MIDIO sobre el arbol antes de usarla.**

| | |
|---|---:|
| linea base declarada **y MEDIDA sobre el arbol de antes** | **7** |
| **colisiones NUEVAS que la fusion fabricaria** | **0** |
| colisiones que desaparecerian | **0** |
| **ESPERADAS TRAS FUNDIR** | **7** |
| **MEDIDAS al cierre por el censo** | **7** |
| **`CALZA`** | **`SI`** |
| auto-pares, predichos y medidos | **5** nuevos predichos (273 a 278) y **278** medidos al cierre |

> **UN CENSO QUE SOLO SE PUBLICA CUANDO SALE MAL NO ES UN CENSO**, y por eso la tabla va entera aunque
> el delta sea cero. **Es el primer lote del tramo desde la vuelta 68 que no fabrica ninguna
> colision**, y **rompe la racha de tres vueltas seguidas fabricandolas** que el `D2` de la vuelta 70
> anoto como ritmo. **Las dos de la mesa `OP-M-03` y las CINCO de `OP-U-02` ya publicadas siguen
> vigentes con su duena y no se tocan.**

### 3.6 **GATE 0 CON SU CICLO DE TRES, Y NO DE CUATRO**

| paso | resultado |
|---|---|
| `python scripts/run_phase1.py --reaplico-curaduria` | **`GATE 0: OK`**, todos los chequeos en `[OK]`; universo **3.204 activos / 649 deprecados**; alcanzabilidad **100,0 por ciento** |
| `python scripts/etiquetas_de_cara.py --aplicar` | **71 etiquetas** re-aplicadas |
| `python scripts/sync_assets_web.py` | **6 assets** mas `manifest.json` |
| **una cuarta corrida** | **NO SE HIZO** |

**LAS TRES SUITES, CORRIDAS POR MI CON EL COMANDO BUENO:** motor **25/25**
([`SALIDA_V71_SUITE_MOTOR.txt`](SALIDA_V71_SUITE_MOTOR.txt)); web **80 ficheros, 1.030 pasadas, 3
saltadas** ([`SALIDA_V71_SUITE_WEB.txt`](SALIDA_V71_SUITE_WEB.txt)); `tsc --noEmit` **CERO lineas**
([`SALIDA_V71_TSC.txt`](SALIDA_V71_TSC.txt)). **Y el guardian de commit las volvio a correr en verde
en los tres commits de trabajo de esta vuelta.**

### 3.7 **EL REGISTRO EN `03_FUSIONES.md`** (`+473` lineas, `0` borradas)

`python scripts/loop/vuelta71_registro_lote_g.py`
([`SALIDA_V71_REGISTRO_LOTE_G.txt`](SALIDA_V71_REGISTRO_LOTE_G.txt)), **bajo la cabecera de tramo que
la vuelta 65 adoso** (derivada hoy por aguja) y **sin reescribir ni una linea de arriba** (`git show
--numstat` sobre `eacce4a3`: **`473 0`**).

**NINGUNA TABLA TECLEADA Y NINGUNA CITA TECLEADA:** el reparto pieza a pieza y las piezas por absorbido
de los **cinco** actos **se generan del plan sellado**; las de perdidas **se recortan de la salida del
tallador**; y las celdas de guardas, colisiones, censos y cuentas **se extraen por aguja**.
**Idempotencia MUERDE.**

**LA MAQUINA SE COPIO POR EXTRACCION Y NO A MANO**, con
`scripts/loop/_v71_construir_registro_lote.py`, que **comprueba que `tabla_reparto`,
`tabla_por_absorbido` y `tabla_declarado` aparecen LITERALES en el destino**. **UN SOLO cambio
declarado** (el fichero del tallador), y **el mapa de motivos ya venia VACIO del ancestro y no se
toca**.

### 3.8 **NINGUN RACIMO CENSADO TOCADO, Y DOS ENTRADAS DE INVENTARIO QUE SI SE DECLARAN**

**Medido hoy sobre [`../RACIMOS_MIEMBROS.jsonl`](../RACIMOS_MIEMBROS.jsonl): NINGUNO de los 15
miembros del lote esta en ninguna nomina de racimo** (32 lineas barridas). **Y el barrido sobre
`OPERACIONES.jsonl` devuelve CERO menciones de los 15 en cualquier campo.**

**PERO HAY DOS ENTRADAS DE INVENTARIO QUE SI TOCAN A DOS ACTOS, Y LAS DOS SE CITAN CON SU
CONSECUENCIA PUBLICADA.** La medicion entera esta en la seccion **4**, que no se repite aqui.

### 3.9 **LAS PERDIDAS DEL LOTE, CONTADAS POR MAQUINA Y NO DE MEMORIA**

`python scripts/loop/cuenta_agregada_de_perdidas.py --plan docs/loop/PLAN_V71_OPU02_LOTE_G.json`
([`SALIDA_V71_CUENTA_ATENUANTES.txt`](SALIDA_V71_CUENTA_ATENUANTES.txt)).

| | contado sobre el plan sellado |
|---|---:|
| **perdidas selladas en campo propio** | **30** |
| de ellas `DE PARAMETRO DE PASO` | **19** |
| de ellas `DE CONDICIONES` | **11** |
| **filas con `ATENUANTE DECLARADO`** | **5** |
| de ellas, de la **especie del pendiente 4** | **3** |
| de ellas, con **`ATENUANTE DECLARADO Y MEDIDO`** | **1** |
| **filas con DOS SEDES en el campo `donde`** | **4** |
| **filas que describen un atenuante SIN la frase sellada** | **NINGUNA**, medido |
| la aritmetica de **la lectura contraria** (una fila por SITIO, no por PIEZA) | **34** y no **30** |

> **TREINTA PERDIDAS ES LA CIFRA MAS ALTA DEL TRAMO** (la vuelta 70 sello 21) **y no se maquilla**:
> la causa esta medida y es el `acto 41`, que sella **SIETE** con **cero `APPEND` y cero `INCISO`**.
> **Donde no se repone nada, todo lo propio del absorbido se cubre o se pierde, y lo que se pierde se
> NOMBRA.** **Va marcado (`D12`).**
>
> **LA MITAD DE LA REGLA QUE OBLIGA A DECIR LO QUE SE EXCLUYE NO TIENE SUJETO EN ESTE LOTE, Y SE DICE
> ASI EN VEZ DE CALLARLO:** **cero filas** describen un atenuante sin llevar la frase sellada, o sea
> que **no hay ninguna exclusion que declarar**. **Es la segunda vuelta seguida sin sujeto**, y por eso
> el caso positivo que la ejerce a proposito (seccion 9) se vuelve a correr.

---

## 4. LAS DOS ENTRADAS DE INVENTARIO DEL LOTE, Y LA QUE LA LETRA DEL ACTA 70 NO CUBRE

**Sube a seccion propia porque una de las dos es el discutible mas fuerte del dia.**

| | `acto 39`, `defensas_en_profundidad` | `acto 41`, `design_for_six_sigma_dmadv` |
|---|---|---|
| **tipo de la entrada** | `familia_de_ids` | `familia_de_ids` |
| **`operaciones`** | **`OP-S-09`** | **`OP-S-09`** |
| **cobertura de la nomina del acto** | **3 de 3, LA NOMINA ENTERA** | **2 de 3** |
| **estado declarado** | *pendiente, se resuelve por continua o repite* | *pendiente, se resuelve por continua o repite* |
| **nota declarada** | *DECISION 4 de la mesa de racimos, aprobada el 9 ago 2026: familia unica, **fusion con alias*** | *DECISION 4 de la mesa de racimos, aprobada el 9 ago 2026: familia unica, fusion con alias* |
| **la letra del acta 70 lo cubre?** | **NO**: su adjudicacion 2 habla de una entrada *sobre PARTE de la nomina* | **SI**, es exactamente el caso adjudicado |
| **consecuencia para `OP-S-09`, publicada** | queda **UN id vivo**, `defensas_en_profundidad_3`, **con sufijo numerico**: le queda un **renombre con alias**, que es su tipo | queda **CERO ids vivos**: los dos mueren dejando alias, y la familia **se resuelve por REPITE**, una de sus dos salidas escritas |

**LO QUE HICE CON EL `ACTO 39` Y POR QUE, DICHO ENTERO:**

1. **Por el PRINCIPIO que la propia letra del acta 70 enuncia, que es de TIPO y no de cobertura:** una
   entrada `familia_de_ids` es **jurisdiccion sobre SU sujeto (la familia)**, no sobre el acto; el
   dueno del acto se mide en los dos campos `duenos_*` del fichero fijado (**VACIOS**, medido hoy) y
   en el campo `operaciones` de **la entrada DEL ACTO** (que nombra `OP-L-03` y `OP-U-02`).
2. **Porque la propia entrada declara su resolucion y esta operacion la ejecuta:** *familia unica,
   FUSION CON ALIAS*, aprobada por la mesa de racimos con fecha. **Fundir es lo que esa decision
   manda, no lo que la contradice.**
3. **Y la consecuencia queda publicada** para que `OP-S-09` no se la encuentre.

> **LO QUE NO HAGO: no estiro la letra.** **La cobertura de 3 de 3 es un caso que el acta 70 no
> resolvio**, y decir que si lo resolvio seria exactamente la especie de cosa que esta campana
> persigue. **Va MARCADO (`D1`) y va como pregunta 3.**

---

## 5. UNA MEDICION QUE NINGUNA VUELTA HABIA NOMBRADO: `OP-L-03` EN EL CAMPO `operaciones` DE TODOS LOS ACTOS

**Sube a seccion propia porque toca a los 47 actos del tramo y porque nadie la habia publicado.**

**Medido hoy:** las entradas de tipo `acto` de los cinco actos del lote traen en `operaciones` **no
solo `OP-U-02` sino tambien `OP-L-03`**. La vuelta 70 publico que *todas las entradas de tipo acto del
tramo nombran `OP-U-02`*, **que es cierto**, pero **no nombro la otra**.

| | medido hoy |
|---|---|
| **que es `OP-L-03`** | la **MESA** de la fase `09_LECTURAS_DIRIGIDAS`, estado `LISTA`, y su campo `bloquea_a` nombra a **`OP-U-01` y `OP-U-02`** |
| **su verificacion, primera linea** | *ningun acto se funde con un par interno sin veredicto* |
| **los actos de este lote** | **2 pares `A` leidos y 1 sin veredicto**, los cinco |
| **la letra en divergencia ya estaba adjudicada, y para la MISMA frase** | el acta 65 la resolvio para la ficha de `OP-U-02` con **cuatro varas** y con las palabras **NO ES PARADA** (registrado en `03_FUSIONES.md`), y su **correccion declarada esta aplicada sobre esa ficha**, leida hoy |
| **sobre la ficha de `OP-L-03`** | **la correccion NO esta aplicada**: su verificacion conserva la frase entera |

**POR QUE NO PARO, Y VA DICHO CON SU LETRA:** la vara tercera de aquella adjudicacion es literal y
vale aqui igual (*los actos del tramo tienen CERO pares en cola sin leer: lo que falta no es lectura
pendiente, es propuesta que la semejanza nunca hizo*), y **la lectura contraria anularia los siete
lotes ya ejecutados y auditados**. **NO INVENTO REGLA**: cito la que existe, **declaro que la ficha de
`OP-L-03` conserva el texto viejo**, lo marco (`D11`) y lo subo como **pregunta 4**.

---

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D1`. EL `ACTO 39` SE FUNDE PESE A UNA ENTRADA `familia_de_ids` QUE CUBRE LA NOMINA ENTERA Y NOMBRA
A `OP-S-09`, Y ES EL MAS FUERTE DEL DIA.** La adjudicacion 2 del acta 70 resolvio el caso de una
entrada asi **sobre PARTE de la nomina** (el `acto 34`, 2 de 3). **Esta cubre 3 de 3.** **Mi razon
para fundir:** el principio que esa letra enuncia es de **TIPO** (una `familia_de_ids` manda sobre su
familia, no sobre el acto), los dos campos `duenos_*` estan vacios, y **la propia entrada declara
*fusion con alias* como su resolucion aprobada**. **Leido al reves, el `acto 39` deberia haber cerrado
`DECLARADO`** y esta fusion habria que deshacerla. **Va como pregunta 3.** Miembros:
`defensas_en_profundidad_3`, `defensas_en_profundidad`, `defensas_en_profundidad_2`.

**`D2`. EL `ACTO 39` SE FUNDE CONTRA UN CABLEADO DE 11 A 2, Y MATA AL NODO CON EL INSTRUMENTO
NOMBRADO.** `defensas_en_profundidad` tiene **nueve previos y cuatro siguientes** y es el que trae
**las siete funciones defensivas** como taxonomia; el que sobrevive tiene **un previo y un
siguiente**. **La letra es clara** (el cableado solo habla a contenido empatado, y la vara de pasos
apunta) **y el banco tiene el ejemplar de *diez contra cinco, y pierde***. **Se puede sostener que
matar el nodo mejor conectado y con el instrumento propio del libro es mas caro que ganar un paso**, y
que la taxonomia entra como `INCISO` a un nodo que casi nadie alcanza.

**`D3`. EL `ACTO 38` SE FUNDE CONTRA UN CABLEADO DE 12 A 4.** `customer_segments_hypothesis` tiene
**doce** conexiones resueltas y el superviviente **cuatro**. **Mi razon:** la vara de pasos apunta (5
contra 4 y 4) y **las dos razones escritas apuntan al mismo nodo**. **Se puede sostener que un nodo con
doce caminos de entrada es un nodo que la gente alcanza, y que el costo de las redirecciones no lo
paga un paso de mas.**

**`D4`. EL `ACTO 42` ELIGE AL MIEMBRO MAS PEQUENO DEL ACTO POR LA SOLA VARA DE CONDICIONES.** El
superviviente tiene **4 pasos contra 5 y 5** y **cableado 2 contra 5 y 4**; gana porque la vara de
pasos **EMPATA** y la de condiciones apunta a el (3 contra 2 y 2). **Mi razon:** la de condiciones es
vara de contenido igual que la de pasos, y **el 672 declara que las dos piezas ejecutables del acto
son sus pasos 2 y 3**. **Se puede sostener que elegir al mas pequeno por una sola vara y con dos
cuentas en contra es forzar la letra**, y que el acto era un caso de `CHOCAN` de facto.

**`D5`. LAS DOS RAZONES DEL `ACTO 39` CORONAN SUPERVIVIENTES DISTINTOS.** El **2236** corona a
`defensas_en_profundidad` y el **2283** a `defensas_en_profundidad_3`; **el par que falta es
exactamente el que enfrentaria a los dos coronados**. **Mi razon:** ninguna razon escrita se desmiente
(cada una corona sobre SU par y las dos matan al mismo nodo), y es **la misma forma que el `acto 34`
del lote F**, que el acta 70 adjudico `A FAVOR` en su `D6`. **Leido al reves, eso es un `P.5` que
contesta DOS FAMILIAS** y el acto tendria que haber cerrado `DECLARADO`. **Es el sitio donde ese motivo
sellado estuvo mas cerca de usarse.**

**`D6`. TRES DE LOS CINCO SUPERVIVIENTES ENTRAN A LA COLA DE COSTURAS, Y ES EL COSTO MAS CARO DEL
LOTE.** Medido: `defensas_en_profundidad_3`, `segmentos_de_clientes_problema_necesidad` y
`traction_goal` **no estaban en la cola antes de la fusion y estan despues**
([`SALIDA_V71_COLA_DELTA.txt`](SALIDA_V71_COLA_DELTA.txt)). **Mi razon:** la cola **CITA, no juzga**
(su propio docstring), y el limite del acta de la vuelta 40 dice que **la cola global no es base de
lectura**. **Se puede sostener que tres citas nuevas de tres fusiones es la senal de que el reparto
esta metiendo repeticion interna donde antes habia repeticion entre nodos**, y que eso es exactamente
lo que la fase 04 va a tener que deshacer.

**`D7`. TRES NODOS DEL LOTE LLEGAN A SIETE PASOS** (`defensas_en_profundidad_3`, `traction_goal` y
`equipo_multifuncional_real`). Es el carril del `D8` del acta 67, del `D4` del acta 68, del `D2` del
acta 69 y del `D5` del acta 70 (*catalogo mas rico con solapes declarados*), **aplicado tres veces en
el mismo lote y por segunda vuelta seguida**. **Se puede sostener que dos vueltas seguidas con tres
nodos grandes cada una ya no es un caso sino una politica de hecho que nadie adjudico.**

**`D8`. NUEVE `APPEND` DE PASO EN UN LOTE, TRES DE ELLOS EN UN SOLO ACTO.** El `acto 39` recibe tres
(`el balance duro y blando`, `las funciones ausentes o debiles` y `el diseno de redundancia`) y el
`42` otros tres. **Mi razon:** los nueve son gestos que las razones nombran como propios, y uno de
ellos entra **porque la razon lo manda con esas palabras** (*el principio de redundancia se absorbe
como linea suya*). **Se puede sostener que tres `APPEND` en un acto de tres miembros es rehacer el
nodo, no repartirlo.**

**`D9`. DOS PIEZAS DE PASO SE MARCAN CONTRA UNA CONDICION DEL SUPERVIVIENTE Y NO CONTRA UN PASO**
(`CUBIERTO_COND`, en el `acto 42`). Los pasos 1 de los dos absorbidos describen **la composicion
multiarea del equipo**, y el superviviente la nombra **solo en su condicion 1**. **Mi razon:** la
marca existe en el generador exactamente para esto y **las dos sellan su perdida**. **Se puede
sostener que una condicion de activacion no cubre un paso**, y que las dos tenian que haber sido
`APPEND`.

**`D10`. LOS NEXOS DE LOS CINCO `INCISO` SON COSECHA PROPIA.** *, y también cuando*, *,
determinando*, *, *, *, en números concretos como*, *, y elígelo*. **El instrumento solo exige que el
TROZO sea verbatim; el nexo es mio.** **Los cinco resultantes estan impresos en la seccion 3.3 para
que se juzguen leyendolos**, y **los cinco se leyeron con sus tildes antes de sellar el plan**.

**`D11`. FUNDO CINCO ACTOS CUYA ENTRADA DE INVENTARIO NOMBRA A `OP-L-03`, CUYA VERIFICACION DICE QUE
NINGUN ACTO SE FUNDE CON UN PAR INTERNO SIN VEREDICTO.** Los cinco tienen **un par sin veredicto**.
**Mi razon:** es **la misma letra en divergencia** que el acta 65 adjudico con **cuatro varas** y con
las palabras **NO ES PARADA** para la ficha de `OP-U-02`, y **la lectura contraria anularia los siete
lotes ya ejecutados y auditados**. **Pero la correccion declarada esta aplicada sobre la ficha de
`OP-U-02` y NO sobre la de `OP-L-03`**, medido hoy. **Va como pregunta 4.**

**`D12`. EL `ACTO 41` SELLA SIETE PERDIDAS Y NO REPONE NI UNA PIEZA.** Cero `APPEND` y cero `INCISO`,
y el nodo no crece. **Mi razon:** las diez piezas de paso de los dos absorbidos son *las cinco letras
de DMADV* contadas dos veces y **estan todas dentro** del superviviente, y los seis pasos terminan en
punto, con lo que el `INCISO` cae en la juntura rota. **Se puede sostener que siete perdidas selladas
en un solo acto son siete piezas que se tiran**, y que al menos la del **alcance** (*descubrir las
necesidades ocultas del cliente*) merecia un `APPEND` aunque el nodo creciera a siete.

**`D13`. UNA PERDIDA SE SELLA SOBRE UN SUPUESTO QUE EL PROPIO ARCHIVO DECLARA DESMENTIDO.** El paso 2
de `defensas_en_profundidad_2` pide evaluar cada capa *de forma independiente* y el paso 2 del
superviviente pide **exactamente lo contrario**. **La selle como perdida con su motivo escrito**, para
que la fase 04 sepa que ahi hubo una correccion y no un olvido. **Se puede sostener que sellar como
perdida algo que el archivo dice que estaba mal infla la cuenta de perdidas con basura.**

**`D14`. DOS SALIDAS DE INSTRUMENTO SE TRANSCODIFICARON DE `cp1252` A `UTF-8`.** Las de
`reanclar_por_resolutor.py` y `run_phase1.py` salieron con la pagina de codigos de la consola y el
registrador las lee en `UTF-8`. **Transcodifique el fichero sin tocar una letra de su texto** (la
prueba es que la unica diferencia es la codificacion del acento de *Pasión*). **Se puede sostener que
tocar un fichero de salida despues de generarlo es exactamente lo que la regla 2 persigue**, aunque el
contenido sea identico. **Lo marco yo y va dicho en la averia 7.4.**

**`D15`. LA CORRECCION DE LAS CELDAS DE CABLEADO SE ADOSA A `03_FUSIONES.md` AUNQUE LAS CELDAS MALAS
NO VIVAN AHI.** Medido por maquina: esa pagina trae **CERO** ocurrencias de las dos cifras crudas;
viven en el plan sellado y en su modulo de contenido. **Mi razon:** el encargo manda adosar la
correccion al registro, **el registro es lo que queda**, y **un plan ejecutado no se re-sella** (acta
68 `D15`). **Se puede sostener que una correccion que no se pone donde vive el error deja el error
vivo**, y que lo debido era corregir el modulo `_v70_lote_f.py`. **Va como pregunta 2.**

---

## 7. LAS AVERIAS PROPIAS, CAZADAS ANTES DE UNA CIFRA PUBLICADA

**CERO de ellas llego a una cifra publicada ni a un dato movido**, y **las SEIS las cazo un instrumento
o una lectura**.

### 7.1 **EL MODULO DEL LOTE EXPONIA `LOTE` Y EL GENERADOR EXIGE `LOTE_G`**

El generador cayo en **`ROJO: el modulo _v71_lote_g no trae el lote G (trae [])`** y **no sello nada**.
Corregido renombrando la constante. **La cazo el instrumento, no un `exit` mudo.**

### 7.2 **LA CLAVE DEL LOTE ERA `tramo` Y EL GENERADOR PIDE `titulo`**

`KeyError: 'titulo'` **despues de imprimir las guardas y antes de escribir el plan**. Corregido, y
**con la duplicacion quitada**: el generador antepone el nombre del tramo por su cuenta.

### 7.3 **EL PLAN SE SELLO CON EL PREFIJO `OPU01`, QUE ES EL DEFECTO DEL GENERADOR**

El fichero salio como `PLAN_V71_OPU01_LOTE_G.json`, **con el nombre de la operacion equivocada dentro
del nombre**. **Lo vi al leer la linea `plan escrito` de la salida**, no al leer un `exit`: el
generador **acepto `--operacion OP-U-02` y sello bien el contenido**, pero **el prefijo del nombre es
un argumento aparte con defecto propio**. Borre el fichero equivocado y re-selle con
`--prefijo PLAN_V71_OPU02_LOTE_`. **Ningun plan con nombre equivocado quedo en el arbol**, comprobado
listando `docs/loop/PLAN_V71*`.

> **ES UNA TRAMPA DE INSTRUMENTO Y NO SOLO UN DESPISTE MIO, Y SE DICE:** un generador de nombre
> estable al que `--operacion` es **requerido** y que aun asi **nombra el fichero `OPU01` por
> defecto** puede sellar un plan cuyo NOMBRE miente sobre su operacion. **Va como pregunta 5.**

### 7.4 **DOS SALIDAS ESCRITAS CON LA PAGINA DE CODIGOS DE LA CONSOLA**

El registrador del lote cayo en **`UnicodeDecodeError`** al leer `SALIDA_V71_REANCLAJE.txt` y despues
`SALIDA_V71_GATE0.txt`: las dos traian el byte `0xf3` (`ó` en `cp1252`) porque la redireccion las
escribio con la codificacion de la consola y no en `UTF-8`. **Las cace corriendo el registrador, no
leyendo un `exit`.** Corregidas **transcodificando el fichero sin tocar su texto**, y **el barrido
por maquina se re-corrio AL CIERRE sobre las 43 salidas de la vuelta**: **CERO fuera de `UTF-8`**,
o sea que **solo esas dos** lo tenian. **Va marcado
(`D14`).**

### 7.5 **EL CONSTRUCTOR DEL REGISTRO SE RENOMBRO A SI MISMO LA LISTA DE `cambios`**

Al derivar el constructor del lote `G` del de la vuelta 70 aplique un renombrado general de
`SALIDA_V70_` a `SALIDA_V71_`, **y ese renombrado alcanzo tambien al literal `viejo` de la lista de
cambios declarados**, con lo que el `assert` de esa pieza cayo. **La cazo el assert del propio
constructor**, que es para lo que esta. Corregido devolviendo ese literal a su forma vieja, que es la
que tiene que casar contra el ancestro.

### 7.6 **CORRI EL INSTRUMENTO DE PUENTES SOBRE LOS 47 Y NO SOBRE LOS 11 QUE QUEDAN**

La primera corrida de `vuelta65_puentes_del_tramo.py` para la tabla del cierre fue **sobre el tramo
entero**, con lo que su resumen habria publicado *38 de 47 sin puente* como si fuera una medicion de
**lo que queda**. **Lo vi al ir a escribir la celda**, la re-corri con `--actos` sobre los **11**, y el
resumen ahora dice **11 mirados, 0 con puente, 11 sin puente**. **Es exactamente la especie de la
caida de reporte del acta 70** (una cifra de un universo publicada como si fuera la de otro), **y por
eso va dicha con esa palabra.**

---

## 8. PENDIENTES DE DOCTRINA Y PREGUNTAS

1. **EL SUBCONJUNTO CERRADO DE UN ACTO CON PUENTE** (heredado): siguen siendo **CATORCE** los actos
   declarados que esperan el cierre de la fase 03, **y esta vuelta no anadio ninguno**. **Ya no puede
   crecer por `P.10` en este tramo**, medido: **cero puentes en los 11 que quedan**.
2. **NUEVA: LA CORRECCION DECLARADA DE UNA CIFRA VA DONDE ESTA EL REGISTRO O DONDE ESTA EL ERROR?**
   Medido: las dos celdas malas del cableado **no viven en `03_FUSIONES.md`** sino en el plan sellado
   y en `scripts/loop/_v70_lote_f.py`. **La correccion se adoso al registro, como el encargo manda**,
   y **el plan no se re-sello** (acta 68 `D15`). **La pregunta concreta: el modulo de contenido de una
   vuelta pasada es un plan ejecutado a efectos del `D15`, o es un instrumento que si se corrige?**
   **No invente regla y lo traigo marcado (`D15`).**
3. **NUEVA, Y ES LA DE MAS PESO: LA FRONTERA DEL DUENO CUANDO LA `familia_de_ids` CUBRE LA NOMINA
   ENTERA.** La adjudicacion 2 del acta 70 resolvio el caso **de PARTE de la nomina**. El `acto 39`
   trae una entrada de esa especie con **3 de 3**, con `OP-S-09` en `operaciones` y con una decision
   de mesa aprobada que dice *familia unica, fusion con alias*. **La pregunta concreta: la frontera se
   lee por TIPO de entrada (y entonces el `39` esta bien fundido) o por COBERTURA (y entonces tenia
   que cerrar `DECLARADO`)?** **Fundi por el principio de tipo, publique la consecuencia para
   `OP-S-09` y lo traigo marcado (`D1`).**
4. **NUEVA: LA FICHA DE `OP-L-03` CONSERVA LA LETRA QUE EL ACTA 65 YA CORRIGIO EN `OP-U-02`.** Medido
   hoy: `OP-L-03` es la mesa de la fase 09, su `bloquea_a` nombra a `OP-U-02`, **su verificacion dice
   *ningun acto se funde con un par interno sin veredicto*** y **la correccion declarada NO esta
   aplicada sobre ella**. **La pregunta concreta: esa correccion se extiende a la ficha de `OP-L-03`,
   o hay algo en la mesa de lecturas dirigidas que la haga distinta?** **No pare, por la adjudicacion
   del acta 65 leida entera, y lo traigo marcado (`D11`).**
5. **NUEVA, Y ES DE INSTRUMENTO: `generar_plan_del_lote.py` NOMBRA EL FICHERO `OPU01` POR DEFECTO
   AUNQUE `--operacion` SEA REQUERIDO.** Medido en la averia 7.3: el contenido sale bien y **el
   NOMBRE miente**. **La pregunta concreta: el prefijo se deriva de `--operacion` en vez de tener
   defecto propio?** **No toque el instrumento** porque nadie lo encargo y porque es de nombre
   estable.
6. **LA MARCA PARA *YA LO DICE EL `APPEND` DE UN HERMANO*** (heredado): **esta vuelta la paga TRES
   veces**, contadas por maquina, **y una de ellas es dentro del MISMO nodo y no entre hermanos** (el
   `acto 40`, donde el descarte llega por el `APPEND` del paso 3 del propio absorbido). **El carril
   vigente alcanza, pero la especie se ensancho y se dice.**
7. **EL `INCISO` DE CONDICIONES SIGUE SIN EXISTIR** (heredado): **once perdidas `DE CONDICIONES`** en
   esta vuelta, **la cifra mas alta del tramo**, enrutadas a la fase 04 por el carril del acta 55,
   pregunta 5.
8. **EL ESQUEMA DE `OPERACIONES.jsonl`** (heredado): sigue pendiente y **esta vuelta no toco ninguna
   ficha** (`git diff --numstat` sobre el fichero: vacio), asi que no estreno ninguna clave.

---

## 9. RUTAS TOCADAS Y CENSOS AL CIERRE

**Del grafo (58 ficheros):** los **cinco supervivientes** (`segmentos_de_clientes_problema_necesidad`,
`defensas_en_profundidad_3`, `traction_goal`, `design_for_six_sigma_dfss`, `equipo_multifuncional_real`),
sus **diez absorbidos** (`customer_segments_hypothesis`, `problem_recognition_scale`,
`defensas_en_profundidad`, `defensas_en_profundidad_2`, `definir_meta_de_traccion`,
`moving_the_needle`, `design_for_six_sigma_dmadv`, `design_for_six_sigma_dmadv_2`,
`diseno_organizacional_equipos_innovacion`, `equipo_multifuncional`), los **redirigidos** (51
referencias sobre nodos vivos), mas `dataset/metadata/master_graph.json` y
`dataset/metadata/phase1_run_log.json`.

**Del registro:** `docs/plan/03_FUSIONES.md` (**`+222`** del acta 70 y **`+473`** del lote G, **cero
borradas en los dos**), `docs/plan/ARISTAS_DUPLICADAS.jsonl`, `docs/COSTURAS_INTERNAS.jsonl` y su
resumen, y `web/lib/assets/` por el `sync`. **`docs/plan/OPERACIONES.jsonl`, `docs/plan/INVENTARIO.jsonl`
y `docs/RACIMOS_MIEMBROS.jsonl` NO se tocaron** (`git diff --numstat` sobre los tres: vacio).
**`scripts/rumbos/banco_rumbos.json` SI SE TOCO**, con **una** referencia re-anclada, y va dicho
porque la vuelta 70 publico lo contrario para su lote.

**Instrumentos nuevos (SIETE, contados por maquina con `git diff --name-status --diff-filter=A
2d22e7e6..HEAD -- scripts/`): NINGUNO de nombre estable**, los siete son de vuelta:
`_v71_construir_registrador_acta.py`, `_v71_texto_acta70.py`, `vuelta71_registrar_acta70.py`,
`_v71_lote_g.py`, `_v71_construir_registro_lote.py`, `_v71_texto_lote_g.py` y
`vuelta71_registro_lote_g.py`. **Y UN SOLO instrumento de nombre estable se MODIFICO**, contado por la
misma via (`--diff-filter=M`): **`vuelta65_colisiones_esperadas.py`**, por la **CORRECCION DECLARADA**
de la `TAREA 1`. **Esta vuelta NO crea ningun instrumento de medida nuevo**, que es el carril que el
`D13` del acta 70 dejo abierto y que aqui no hace falta usar.

| censo al cierre | valor |
|---|---|
| **barrido de titulos** ([`SALIDA_V71_BARRIDO.txt`](SALIDA_V71_BARRIDO.txt)), **re-corrido AL CIERRE** | **470 ficheros**, `ROJO` **32** (**linea base heredada, EN SU SITIO**), **`AMBAR` 0**, `ROTULADO` **51**, `CENSO` **224**, `ILEGIBLE` **1** |
| **censo de plantillas talladas** ([`SALIDA_V71_CENSO_PLANTILLAS.txt`](SALIDA_V71_CENSO_PLANTILLAS.txt)) | **CERO TALLADOS** sobre **26** instrumentos de nombre estable |
| **estado de las operaciones** ([`SALIDA_V71_CIERRE.txt`](SALIDA_V71_CIERRE.txt)) | **71**, todas `LISTA`, **0** dependencias rotas, **672** entradas, enlaces **17.639** |
| **casos positivos** ([`SALIDA_V71_CASOS_POSITIVOS.txt`](SALIDA_V71_CASOS_POSITIVOS.txt)) | **SEIS, y los seis sobre sujetos que esta vuelta NO toca**: mesa **LAS NUEVE** sobre `OP-M-02-ACCLIMATE`; contrato de perdidas **LAS CUATRO**; varas **LAS TRES mitades**; promesas **LAS DOS mitades**; cuenta agregada **LAS CINCO mitades**; y el del generador, que compara **el ancestro sacado de `git` contra el fichero de hoy** |

> **EL `ROTULADO` SUBE DE 49 A 51 Y NO SE DEJA COMO UN NUMERO QUE CAMBIA SOLO:** son **los dos rotulos
> de los dos ficheros nuevos de esta vuelta** (`vuelta71_registrar_acta70.py` y
> `vuelta71_registro_lote_g.py`), **los dos EXTRAIDOS del ancestro y no tecleados**, que es el carril
> que la averia 7.4 de la vuelta 70 dejo escrito. **El `ROJO` no se mueve de su linea base de 32 y el
> `CENSO` no se mueve de 224.**

### 9.1 **LA TASA POR DOMINIO AL CIERRE, IDENTICA A LA DE APERTURA**

**Fundir no volteo ni un veredicto**, y por eso el marcador de cierre sale **identico** al de apertura,
las diez lineas.

| dominio | pares | `A` | tasa |
|---|---:|---:|---:|
| compras | 155 | 1 | 0,6 |
| core | 1.445 | 325 | 22,5 |
| entrega | 171 | 2 | 1,2 |
| environmental | 170 | 28 | 16,5 |
| exportacion | 130 | 15 | 11,5 |
| franquicias | 148 | 15 | 10,1 |
| health_safety | 192 | 43 | 22,4 |
| quality | 844 | 119 | 14,1 |
| risk_management | 106 | 0 | 0,0 |
| seguridad_digital | 27 | 3 | 11,1 |

**Corte de todas estas cifras: 26 ago 2026, puesto 3.388.**

---

## 10. LO QUE QUEDA DEL TRAMO, MEDIDO AL CIERRE

([`SALIDA_V71_TRAMO_CIERRE.txt`](SALIDA_V71_TRAMO_CIERRE.txt),
[`SALIDA_V71_PUERTAS_DE_LOS_QUE_QUEDAN.txt`](SALIDA_V71_PUERTAS_DE_LOS_QUE_QUEDAN.txt) y
[`SALIDA_V71_PUENTES_DE_LOS_QUE_QUEDAN.txt`](SALIDA_V71_PUENTES_DE_LOS_QUE_QUEDAN.txt))

| | |
|---|---:|
| actos del tramo unico | **47** |
| actos **FUNDIDOS**, medido sobre el grafo | **22** |
| actos **`DECLARADOS Y NO FUNDIDOS`** | **14** |
| **quedan sin destino** | **11 actos y 33 nodos** |
| **el siguiente del prefijo** | el acto **31**, **con dueno** (`OP-F-04-WEI`, `OP-S-04`) |
| **el primero SIN dueno** | el acto **43** |
| de los que quedan, **con dueno medido** | **2** (los actos **31** y **37**) |
| de los que quedan, **con nodo puente** | **0** |
| de los que quedan, **con par `D` interno** | **0** |
| de los que quedan, **con puerta dentro** | **4** |
| **actos declarados que esperan el cierre de la fase 03** | **14** |

> **LAS PUERTAS DE LOS QUE QUEDAN SE MIDEN CON SU SALIDA COMMITTEADA, Y ESA ES LA REGLA PRACTICA QUE
> ESTA VUELTA CUMPLE**: de los **11**, **CUATRO traen puerta**, y van nombradas una a una. El
> **`31`**: `captura_conocimiento_mercado` (y ademas tiene dueno). El **`44`: DOS**,
> `explotacion_tecnologias_disruptivas` y `tecnologias_disruptivas_oportunidad`. El **`46`**:
> `mitigacion_riesgos_ambientales`. El **`51`**: `metodo_valor_presente_neto`. **El `44` cerrara
> `DECLARADO` por la guarda `1B` cuando el prefijo lo alcance; el `46` y el `51` funden con su puerta
> sobreviviendo** (acta 54, pregunta 1), **por la adjudicacion 4 del acta 70**.
>
> **Y LAS FORMAS DE LOS 11 YA NO SON TODAS IGUALES, medido**: **8 `UNA SOLA VARA`, 1 `CONTENIDO
> EMPATA` (el `45`), 1 `CHOCAN` (el `31`) y 1 `TODAS DE ACUERDO` (el `53`)**. **Los 11 siguen siendo
> de tres miembros con dos pares `A` y uno sin veredicto, cero puentes y cero `D` internos.**

**NO SE FUNDIO NINGUN ACTO CON DUENO** (el `31` y el `37` quedan con los suyos), **no se toco la mesa
`OP-M-03` ni sus dos colisiones**, **las cinco colisiones de `OP-U-02` ya publicadas siguen vigentes
con su duena**, **no se toco el `acto 44` ni sus dos puertas**, y **las cinco fichas `OP-M-02`
consumidas no se ejecutaron**: lo consumado no se ejecuta ni se rehace.

---

## 11. CONDICIONES DE PARADA, RECORRIDAS

| condicion | se cumple? |
|---|---|
| doctrina nueva inventada | **NO**: los quince discutibles y los ocho pendientes quedan bajo letra citable (`P.1`, `P.5`, `P.8`, `P.10`, `P.16`, guarda `1B`, y actas 53, 54, 55, 61, 64, 65, 66, 67, 68, 69 y 70). **Lo que no tiene letra va como PREGUNTA, no como regla**: la frontera del dueno con nomina entera **sube como pregunta 3**, la ficha de `OP-L-03` **como pregunta 4** y el prefijo del generador **como pregunta 5**, y **ningun instrumento se toca** mas alla de la correccion encargada |
| contradiccion sin regla de correccion | **NO**: la letra de `OP-L-03` en divergencia **tiene adjudicacion escrita para su misma frase** (acta 65, con las palabras *NO ES PARADA*), y **se declara en vez de resolverse inventando** |
| decision de fundador | **NINGUNA SE TOMA**: el merge sigue siendo suyo |
| fallo tecnico repetido | **NO**: Gate 0 y las tres suites en verde |
| campana consumada | **NO**: quedan **11 actos y 33 nodos** del tramo, la mesa `OP-M-03` y las fases 04 en adelante |
| **cierre de la fase 03** (la parada de `AUDITOR.md`) | **NO SE CUMPLE TODAVIA**: quedan 11 actos, dos de ellos con dueno, y los **14** declarados siguen sin destino resuelto |
| credenciales | no hicieron falta |

---

## 12. HASH FINAL Y COMMITS

**Los commits de trabajo de esta vuelta, escritos en la rama `pasada-unica` y leidos hoy con
`git log --oneline`:**

| commit | que lleva |
|---|---|
| **`c1859ed5`** | **TAREA 1 entera**: el registro del acta 70 (`+222`, `0` borradas, 80 agujas, tres negativas de sustancia) **mas las DOS CORRECCIONES DECLARADAS** (las celdas de cableado con las cifras medidas por mi en worktree, y la linea base de 6 a 7) **y la APERTURA medida antes de la primera operacion, con el marcador tallado con `recomputar_marcador.py` desde el principio** |
| **`f188f1c3`** | **TAREA 2**: el lote G ejecutado (5 fusiones, 0 declarados, 10 nodos muertos, `P.16` limpio, **CERO colisiones fabricadas**, Gate 0 con su ciclo de tres y las tres suites en verde) |
| **`eacce4a3`** | **el registro del lote G** (`+473`, `0` borradas, 16 agujas, idempotencia mordiendo) **mas los censos de cierre, las puertas de los 11 medidas con su salida y los seis casos positivos** |

**EL HASH FINAL DE LA VUELTA ES EL DEL COMMIT QUE ESCRIBE ESTA MISMA LINEA, y por eso no se puede
escribir dentro de si mismo: un commit no puede contener su propio hash.** **Los TRES anteriores estan
arriba, ninguno de memoria**, y **la cadena entera queda escrita en esta cabecera**, que es lo que la
regla 7 pide y lo que el commit del reporte no podia contener. Es la misma via que las vueltas 65 a 70
usaron, la ultima de ellas en su commit `66ef6d38`.

**LAS GUARDAS DE CIERRE, RE-CORRIDAS TRAS ESTA EDICION** (regla 1: lo que la propia vuelta mueve, se
remide antes de publicar):

| guarda | comando | resultado |
|---|---|---|
| **la cabecera se talla, no se teclea** | `tallar_cabecera_reporte.py --vuelta 71 --comparar docs/loop/REPORTE.md` | **`CABECERA: IDENTICA AL TALLADOR`**, 14 filas cotejadas, DISTINTAS 0, ausentes 0 ([`SALIDA_V71_CABECERA_COMPARADA.txt`](SALIDA_V71_CABECERA_COMPARADA.txt)) |
| **las promesas de marcado, por maquina** | `comprobar_promesas_de_marcado.py --reporte docs/loop/REPORTE.md --plan docs/loop/PLAN_V71_OPU02_LOTE_G.json` | **4 promesas medidas, 4 CUMPLIDAS, 0 INCUMPLIDAS** ([`SALIDA_V71_PROMESAS.txt`](SALIDA_V71_PROMESAS.txt)) |
| **el barrido de titulos, re-corrido AL CIERRE** | `barrido_titulos_tallados.py` | **470 ficheros, `ROJO` 32** (linea base en su sitio), **`AMBAR` 0**, `ROTULADO` 51, `CENSO` 224 ([`SALIDA_V71_BARRIDO.txt`](SALIDA_V71_BARRIDO.txt)) |
| **la cuenta agregada de perdidas, por maquina** | `cuenta_agregada_de_perdidas.py --plan ...` | **30 perdidas, 5 con atenuante, 3 del pendiente 4, 1 con atenuante medido, 4 con dos sedes**, y **cero exclusiones que declarar** ([`SALIDA_V71_CUENTA_ATENUANTES.txt`](SALIDA_V71_CUENTA_ATENUANTES.txt)) |
| **el diff de los dos sellos del plan** | por maquina, con el primer sello guardado dentro del repo | **UNA sola linea distinta**, la del campo `colisiones_esperadas` ([`SALIDA_V71_DIFF_SELLOS.txt`](SALIDA_V71_DIFF_SELLOS.txt)) |

**Cero guiones largos y cero guiones medios**, contados por maquina sobre el fichero entero.
