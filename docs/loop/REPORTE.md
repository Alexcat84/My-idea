# REPORTE DE LA VUELTA 36 (ejecutor Opus 5). FASE III, rama `pasada-unica`

**`OP-D-03` CERRADA CON SU DESTEJIDO HECHO Y SIN FUSION, Y NO POR RENUNCIA: PORQUE EL ACTO
DEJO DE EXISTIR.** Los seis pares `A` del acto se volcaron a `D` (cinco por `P.5`, uno por la
lectura dirigida `LD-82`), el acto se quedo con **cero pares `A`** y **desaparecio del censo**.
**Cero nodos tocados: ninguno se funde, ninguno se depreca, ninguno pierde un paso.**

---

## 0. VUELTAS 34 Y 35 SIN ACTA, Y LA 36 TAMPOCO LA TIENE

**ESTA SECCION ABRE EL REPORTE POR ORDEN DEL ENCARGO, y lo que trae esta MEDIDO HOY, no
recordado.** Antes de leer una sola cifra de esta vuelta hay que saber que **el bucle lleva TRES
vueltas sin auditor**, y que las dos primeras **fallaron por motivos distintos**.

| medicion de hoy | resultado |
|---|---|
| ultima cabecera de `docs/loop/ACTA_AUDITOR.md` (`grep` sobre las cabeceras, corrido hoy) | **`ACTA DE LA VUELTA 33`**, linea **7152** |
| `git log -1 -- docs/loop/ACTA_AUDITOR.md` | **`4d33534c`, 2026-08-15 10:35:28**, el acta de la **33** |
| `docs/loop/PARA_ALEXIS.md` | **NO EXISTE** (comprobado hoy) |
| `docs/loop/loop.log`, ultimas ocho lineas | ver abajo |

**LAS DOS CAIDAS, LEIDAS DEL `loop.log` DE HOY Y NO DE UN ACTA, Y NO SON LA MISMA:**

```
[2026-08-15 13:12:43] VUELTA 1 : AUDITOR (claude-fable-5)
[2026-08-15 13:30:52] auditor listo (USD 12.429116), 1089s, intento 1 de 7
[2026-08-15 13:30:53] VUELTA 2 : EJECUTOR (claude-opus-5)
[2026-08-15 13:57:14] ejecutor listo (USD 9.542621500000001), 1581s, intento 1 de 7
[2026-08-15 13:57:15] VUELTA 2 : AUDITOR (claude-fable-5)
[2026-08-15 13:57:19] auditor: fallo instantaneo (probable limite de uso), 4s, costo "0", intento 1 de 7
[2026-08-15 13:57:19] fallo instantaneo (probable limite de uso); espero 30 minutos y reintento
[2026-08-18 23:13:55] VUELTA 1 : EJECUTOR (claude-opus-5)
```

1. **EL AUDITOR DE LA VUELTA 34 CORRIO 1.089 SEGUNDOS, GASTO 12,43 DOLARES Y NO ESCRIBIO NADA.**
   Es **el auditor mudo**, y es exactamente la especie que el fundador acaba de instrumentar en
   `orquestador.sh` con el sexto parametro TESTIGO (commit `3a7d1549`).
2. **EL AUDITOR DE LA VUELTA 35 NO LLEGO A CORRER: fallo a los 4 segundos** con *probable limite
   de uso*, costo cero. **El orquestador anuncio los 30 minutos de espera y ese reintento NUNCA
   APARECE EN EL LOG:** la linea siguiente es del **18 de agosto** y **soy yo**. **Es una especie
   DISTINTA de la que el parche cubre, y el parche no la habria cazado**, porque el fallo
   instantaneo ya estaba contemplado; lo que fallo fue **que el proceso no volvio**.

> **QUE HIZO CADA UNA, para que la verificacion tenga lista de trabajo:**
>
> | vuelta | lo que hizo | estado |
> |---:|---|---|
> | **34** | reciprocado de deprecados fuera de `Gate 0` (**caso positivo 23 de 23 ANTES del Gate y 22 de 23 DESPUES**, cifra vieja conservada en `SALIDA_V34_PLAN_DECLARADO.txt` linea 10), `costuras_internas.py` **recalibrado** (`SALIDA_V34_COSTURAS_RECALIBRADO.txt`, umbrales pareja 80 y bloque 44, y **la puerta sigue roja**), **pasos 1 y 3 del orden interno de `OP-D-03`**, y las lecturas dirigidas **`LD-75` a `LD-81`** (medidas hoy en `LECTURAS_DIRIGIDAS.md`: 5, 4, 3, 2, 3, 2 y 5 apariciones) | **SIN AUDITAR** |
> | **35** | la **medicion de `P.5`** sobre el acto de `OP-D-03` (cinco pares rancios y no dos, dos varas independientes) y **las cinco relecturas escritas, selladas y NO volcadas** | **SIN AUDITAR** |
> | **36** | esta: el volcado de las cinco, `LD-82`, y el cierre de `OP-D-03` | **SIN AUDITAR** |

> ### PETICION EXPLICITA, Y ES LO QUE ESTE REPORTE PIDE ANTES QUE NADA
>
> **VERIFICACION COMPLETA DE LAS VUELTAS 34, 35 Y 36 ANTES DE REANUDAR EL MODO CONTINUO.** Y el
> motivo no es de forma: **esta vuelta volco SEIS veredictos apoyandose en criterios y en
> instrumentos que escribio la vuelta 34, que nadie ha leido.** El criterio del `738` sostiene
> cinco de los seis volcados; el instrumento `vuelta34_leer_opd03.py` imprimio los nodos de la
> sexta. **Si la 34 tuviera un fallo de fondo, esta vuelta lo habria propagado seis veces.**
>
> **La regla nueva del auditor (`AUDITOR.md` seccion 1, paso 0, HUECO DE ACTA) ya obliga a esto.**
> Se dice igual, porque la regla es del 15 de agosto y **todavia no ha corrido ni una vez.**

**EL ENCARGO MANDABA DETENERSE AQUI Y ME DETENGO: la TAREA 3 se cumplio.** No se siguio el modo
continuo, no se abrio `OP-D-04`, no se leyo un solo par de la cola.

---

## 1. LO QUE ESTA VUELTA MOVIO, MEDIDO Y NO NARRADO

- **Hash de partida:** `3a7d1549` (la decision del fundador que trajo el encargo).
- **Hash final:** `97552714`. **TRES commits** (`10615460` la apertura, `c8c4e0b3` la TAREA 1,
  `97552714` la TAREA 2), **y el de este reporte hace CUATRO.** Se dice con las dos cifras a
  proposito: la vuelta 33 recibio una caida de reporte por esta cuenta exacta.
- **Rutas tocadas** (`git diff --stat 10615460..HEAD`, corrido hoy): **41 ficheros, 4.360
  insertadas, 30 borradas**. Por carpeta: `docs/loop` **27**, `scripts/loop` **6**, `docs/plan`
  **5**, mas `docs/PENDIENTES.md`, `docs/INTRA_DOMINIO_INFORME.md` y
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`. **Cero merges.** El hook corrio verde en los tres.
- **`dataset/`: CERO ficheros tocados. `web/`: CERO ficheros tocados.** Medido con
  `git diff --name-only 10615460..HEAD` filtrado por carpeta.
- **EL ARCHIVO DE VEREDICTOS SI SE TOCO, y aqui esta la cuenta exacta**, comparando el fichero de
  hoy contra el del commit de apertura registro por registro: **n 3.388 antes y despues, cero
  altas, cero bajas, SEIS puestos cambiados** (277, 374, 452, 643, 1571, 1575), **los seis de `A`
  a `D`**, **los seis con la razon vieja LITERAL dentro de la nueva**, y **CERO puestos con
  cualquier otro campo movido**.

### EL ESTADO, APERTURA CONTRA CIERRE

**Las dos columnas son de dos corridas propias del MISMO instrumento**
(`scripts/loop/vuelta31_estado.py`, **sin tocarlo**): la de **APERTURA** corrida **antes de la
primera operacion** y commiteada antes de tocar nada (`10615460`, salida
`SALIDA_V36_APERTURA.txt`), y la de **CIERRE** corrida **al cerrar** (`SALIDA_V36_CIERRE.txt`).

| | **APERTURA** | **CIERRE** |
|---|---:|---:|
| marcador: n / A / B / C / D | 3.388 / **581** / 83 / 8 / **2.716** | 3.388 / **575** / 83 / 8 / **2.722** |
| tasa de A | 17,1 % | **17,0 %** |
| huecos / duplicados / clases fuera de ABCD | 0 / 0 / 0 | **0 / 0 / 0** |
| grafo: ficheros / ids / vivos / deprecados | 3.853 / 3.853 / 3.538 / 315 | **identicos** |
| enlaces / claves distintas | 16.849 / 15 | **16.849 / 15** |
| familias Weinberg / Horowitz / Hugos / Coleman / Rackham (vivos) | 72 / 93 / 111 / 75 / 47 | **identicas** |
| operaciones / estados / dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| inventario | 672 | **672** |
| indice rojo declarado | 18 lineas, 0 ausentes | **18 lineas, 0 ausentes** |
| fronteras de `OP-F-04-COL` | 14 de 15 | **14 de 15** |

> **Y LA COMPARACION SE HIZO POR MAQUINA, no a ojo:** `difflib` sobre las dos salidas enteras da
> **84 lineas cada una y CUATRO lineas de diferencia**, de las cuales **dos son el rotulo**
> (*APERTURA* contra *CIERRE*). **Las dos que importan son la `A` y la `D`.** Todo lo demas del
> estado de la campana esta quieto al digito.

### LA TASA POR DOMINIO, recomputada del archivo en esta vuelta

**Instrumento `scripts/loop/vuelta35_tasa_dominio.py`, REUTILIZADO y no reescrito** (es una
medicion pura, sin constantes de vuelta), corrido **dos veces**, una por volteo. Salidas
`SALIDA_V36_TASA_DOMINIO.txt` y `SALIDA_V36_TASA_DOMINIO_B.txt`:

| dominio | n | A al abrir | A tras las cinco | **A al cierre** |
|---|---:|---:|---:|---:|
| **core** | 1.445 | 342 (23,7 %) | 337 (23,3 %) | **336 (23,3 %)** |
| quality | 844 | 126 | 126 | **126** |
| health_safety | 192 | 45 | 45 | **45** |
| environmental | 170 | 29 | 29 | **29** |
| franquicias | 148 | 18 | 18 | **18** |
| exportacion | 130 | 15 | 15 | **15** |
| entrega | 171 | 2 | 2 | **2** |
| compras | 155 | 1 | 1 | **1** |
| risk_management | 106 | 0 | 0 | **0** |
| seguridad_digital | 27 | 3 | 3 | **3** |

> **LOS SEIS VOLTEOS SON LOS SEIS DE `core`, y los otros nueve dominios quedan identicos al
> digito.** Y **la tasa de `core` se mueve por primera vez en la campana**: 342 de 1.445 es 23,67
> y 336 de 1.445 es 23,25, **y ya no redondean al mismo sitio**. La correccion de la vuelta 34
> tuvo que explicar que el 23,7 no significaba *no paso nada*; **esta no lo necesita.**

**LA VARA POR TRAMO NO SE MUEVE:** es cifra del cribado, y **esta vuelta no leyo ningun par de la
cola**. `n` sigue en **3.388**.

---

## 2. TAREA 1: LAS CINCO RELECTURAS VOLCADAS, Y NO SE REESCRIBIO UNA LETRA

**LA DECISION QUE LO AUTORIZA, citada con su linea:**
`docs/loop/paradas/2026-08-15-p5-rancios-opd03-DECISION.md`, ultimo parrafo: *DECISION DEL
FUNDADOR (15 ago 2026): 1) se vuelcan las cinco relecturas*.

**EL INSTRUMENTO NUEVO (`scripts/loop/vuelta36_volcado_910.py`) ES SUCESOR DECLARADO DEL DE LA
VUELTA 34, Y CAMBIA EN UNA SOLA COSA, dicha en su cabecera** (`EJECUTOR.md` regla 2): aquel
**construia las razones dentro del script**; este **NO ESCRIBE NI UNA LETRA DE RAZON**, las lee de
`docs/loop/PROPUESTA_V35_RELECTURAS.json`.

> **POR QUE ESE CAMBIO Y NO OTRO:** reescribir el texto aqui **seria volcar OTRA cosa que la que
> el fundador aprobo.** La propuesta se sello el 15 de agosto y se aplica tal cual.

**LAS SEIS GUARDAS SE VOLVIERON A CORRER HOY Y NO SE HEREDARON DE LA PROPUESTA** (una guarda verde
el 15 no dice nada del 18). Salida entera en `SALIDA_V36_VOLCADO.txt`, y las seis verdes:

| guarda | resultado |
|---|---|
| 1. los seis nodos tienen HOY los pasos que las razones afirman | **6 de 6 OK** (5, 7, 5, 4, 5, 5) |
| 2. cada puesto sigue registrado y sigue en `A` | **5 de 5** |
| 3. **la razon vieja DEL ARCHIVO DE HOY, literal dentro de la sellada** | **5 de 5** (573, 664, 569, 1.574 y 1.452 caracteres dentro de 4.657, 3.721, 4.652, 4.945 y 4.823) |
| 4. las aristas internas, en LOS DOS SENTIDOS contra el grafo | **5 de 5 sin arista** |
| 5. el `643` **NO** entra en este lote | **OK**, va por su propio carril |
| 6. el marcador esperado, contrastado con la cifra del encargo | **coinciden**, y el script **aborta** si no |

> **LA GUARDA 3 ES LA QUE DE VERDAD IMPORTA Y POR ESO SE NOMBRA:** es la que **prueba que la
> propuesta se sello contra ESTE archivo y no contra otro.** Si alguien hubiera tocado esas cinco
> razones desde el 15 de agosto, **la guarda cae y el volcado no ocurre.**

**MARCADOR RECOMPUTADO CON EL INSTRUMENTO** (`SALIDA_V36_MARCADOR.txt`): **n 3.388, A 576, B 83,
C 8, D 2.721**, **exactamente la cifra que el encargo fijaba.** No hubo parada.

### EL BARRIDO DEL `9.10`, EN EL MISMO ACTO

**Instrumento sucesor propio** (`vuelta36_barrido_910.py`, cifras viejas `A 581 / B 83 / C 8 /
D 2.716`): **98 candidatos, listados sin ocultar ninguno** (`SALIDA_V36_BARRIDO_910.txt`).

**CORREGIDOS:**

| documento | que se corrigio |
|---|---|
| `INTRA_DOMINIO_INFORME.md` **100.1** | cuarto tachado en `A` y `D`, y **el cuarto volteo escrito con su tabla de cinco filas** |
| `INTRA_DOMINIO_INFORME.md` **100.2** | `core` de **342 a 337**, tasa de **23,7 a 23,3** |
| `INTRA_DOMINIO_INFORME.md` **100.6** | total de `A` a **576**, con el contador de fusiones mutuas **verificado de nuevo y quieto en veintiocho** |
| `RECOMPUTO_3388.md` | correccion declarada nueva **con el instrumento RE CORRIDO ENTERO**, y su `jsonl` de componentes **reescrito por el propio instrumento** |
| `PENDIENTES.md` | cola de **12 a 11**: sale el **374**, y no por una cirugia nueva sino **porque ya se releyo** |
| `02_DESTEJIDOS.md` | el acto pasa de **SEIS pares `A` a UNO** |
| `LECTURAS_DIRIGIDAS.md` | la tabla de la respuesta de `P.5` y **la conclusion de las DOS FAMILIAS CERRADAS**, reescrita con el texto de hoy |

**NO CORREGIDOS, y dicho por que:** las tablas de tramo del cribado y las filas de checkpoints
cerrados, **que son la foto de su propio corte**; y las salidas viejas de `docs/loop`, **que se
contrastan y no se maquillan.**

**EL RECOMPUTO, RE CORRIDO** (`SALIDA_V36_RECOMPUTO_3388.txt`): A crudas **581 a 576**, pares
distintos del retrato **580 a 575**, nodos con al menos una `A` **851 a 847**, actos **335 a
334**, CERRADAS **281 sobre 604 a 280 sobre 600**, ABIERTAS quietas en **54 sobre 247**. **Las
cuatro comprobaciones del `08_VERIFICACION.md` dan OK las cuatro.**

> **LAS DOS CIFRAS RARAS VAN EXPLICADAS Y NO ESCONDIDAS.** **Primera:** cinco `A` menos quitan
> solo **cuatro** nodos, porque el `643` seguia en `A` y sostenia a dos. **Segunda:** los actos
> **BAJAN** quitando cinco cuando la vuelta 34 los **SUBIO** quitando una. No es contradiccion:
> aquella **corto la arista que unia dos mitades y una componente se partio en dos**; esta **hace
> desaparecer la mitad del embudo entera.**

---

## 3. TAREA 2: `LD-82`, EL `643`, Y ES OTRA ESPECIE

**Y LO PRIMERO QUE HAY QUE DECIR ES QUE NO ES LA SEXTA DE UNA TANDA UNIFORME.**

| | las cinco de la TAREA 1 | **el `643`** |
|---|---|---|
| por que se relee | **el texto cambio bajo el veredicto** | **`P.5` manda leer el ACTO ENTERO** antes de fundirlo |
| estaba rancio | **si**, las cinco | **NO**: sus dos nodos no cambiaron una coma (`SALIDA_V35_RANCIOS.txt` lo puso en **AL DIA**) |
| la razon vieja, contra el texto de hoy | **afirma cosas falsas** | **describe el texto de hoy con exactitud** |
| que cambia | **el texto** | **EL CRITERIO** |

> **Eso va escrito dentro de la propia razon volcada, no solo aqui.** Presentarla como la sexta de
> una tanda uniforme **seria mentir por omision.**

**LOS DOS NODOS IMPRESOS ENTEROS ANTES DE DECIDIR** (`SALIDA_V36_NODOS_ENTEROS.txt`, con el
instrumento sellado `vuelta34_leer_opd03.py` **reutilizado y no reescrito**), y la arista buscada
**EN LOS DOS SENTIDOS** contra el grafo compilado **con el resolutor de alias aplicado antes de
comparar** (`P.1`): **no hay ninguna.**

### LA VARA QUE DECIDE NO ES LA HEREDADA, Y ESO ES A PROPOSITO

**Las cinco de la TAREA 1 se decidieron con el criterio del `738`** (*la mecanica compartida no
basta, el objeto decide*), **y ese criterio lo escribio la vuelta 34, que nadie ha auditado.**
Colgar un sexto veredicto de la misma vara heredada, **y sola**, seria **encadenar seis lecturas a
un criterio sin auditar.**

**Asi que el `643` se midio primero con una vara que no depende de aquella: LA CONTENCION.** Un
par REPITE cuando el contenido de uno **vive dentro** del otro. **La tabla no esta tecleada: es la
salida del instrumento** (`python scripts/loop/vuelta36_ld_643.py`, salida
`SALIDA_V36_LD_643.txt`), y la correspondencia se declara **solo donde el GESTO es el mismo**:

```
  split_testing    pasos 4 | compartidos 2 | PROPIOS 2 (50 por ciento propio)
  test_ab_precio   pasos 5 | compartidos 2 | PROPIOS 3 (60 por ciento propio)

  CONTIENE split_testing a test_ab_precio? NO
  CONTIENE test_ab_precio a split_testing? NO
```

**Lo propio de `split_testing`:** el reparto **equitativo** del trafico control contra retador, y
**la significancia estadistica por encima del 95 %**. **Lo propio de `test_ab_precio`:** el canal
real, **las multiples rondas para afinar el precio optimo**, y **quedarse con la ganadora**, que
el otro **no tiene como paso**.

### LO QUE DE VERDAD DECIDE ESTA DENTRO DE LA PROPIA RAZON VIEJA, Y JUEGA CONTRA SU CLASE

**Aquella cierra diciendo, con estas palabras**, que lo propio de `test_ab_precio` son las rondas
multiples *que el general no pide*, y que lo propio de `split_testing` es el umbral del 95 %,
*que es lo que impide declarar ganador a un ruido, y es **LO MAS CARO DE PERDER DE LOS DOS***.

> **UNA `A` LLEVA A FUNDIR, Y FUNDIR ES QUE UNO DE LOS DOS MUERA.** Si lo mas caro de perder vive
> en un lado y la busqueda iterativa del optimo vive en el otro, **la fusion tendria que
> conservarlos los dos**, y esa **no es la forma de un par que repite.** **La razon vieja nombro
> el motivo para no fundir y clasifico `A` igual.**

**LOS ENTREGABLES, que el `9.6.2` dice que deciden mas rapido que los pasos**, leidos hoy:
*resultados comparativos de conversion entre variantes con significancia estadistica* contra *un
precio o modelo de monetizacion validado*. **Dos productos distintos.**

**LA PRUEBA DE MADRE E HIJO DEL `9.6.2` SE CORRIO Y NO SE CUMPLE:** la regla pide que **el hijo
quepa entero dentro de UN paso de la madre**, y **tres de los cinco pasos de `test_ab_precio` no
tienen casa en ningun paso de `split_testing`**. El precio aparece alli como **una palabra dentro
de un parentesis**, no como una linea que sea un procedimiento nombrado.

**VEREDICTO: `D`, los dos sanos, SIN ARISTA DECLARADA.** Volcado por el mismo carril
(`_lote_v36_643.jsonl`), razon vieja **literal dentro de la nueva** (1.093 caracteres dentro de
8.456), **marcador recomputado n 3.388, A 575, B 83, C 8, D 2.722**, exacto a la cifra escrita
**antes** de correr el instrumento.

**Y SU BARRIDO, EN EL MISMO ACTO, CON UN SEGUNDO INSTRUMENTO SUCESOR** (`vuelta36_barrido_910_b.py`,
cifras viejas `A 576 / D 2.721`): **41 candidatos**. **Se corrigieron incluso las celdas que yo
mismo habia escrito en el commit anterior de esta misma vuelta**, porque **una cifra escrita hace
media hora envejece igual que una de hace un mes: el `9.10` no da plazo de gracia.**

---

## 4. `OP-D-03` CERRADA, Y EL ACTO DESAPARECE

**El cierre lo escribio un instrumento** (`scripts/loop/vuelta36_cerrar_opd03.py`) **y no mi mano**,
con una guarda que **ABORTA si quedara un solo par `A` vivo dentro del acto**. Corrida hoy:
**cero.** Nota vieja **literal dentro de la nueva** (2.283 a 5.200 caracteres), **71 operaciones,
ninguna alta ni baja, una sola nota tocada.**

| | antes (15 ago) | tras las cinco | **al cierre** |
|---|---|---|---|
| pares `A` dentro del acto | **6** | 1, el `643` | **CERO** |
| componentes que deja | DOS, cerradas | UNA, cerrada | **NINGUNA** |
| actos del censo | 335 | 334 | **333** |
| CERRADAS | 281 sobre 604 | 280 sobre 600 | **279 sobre 598** |
| nodos con al menos una `A` | 851 | 847 | **845** |

> **LA RESPUESTA DE `P.5` PARA ESTE ACTO, EN SU TERCERA VERSION: ni una familia de seis, ni dos
> familias, ni un par. NINGUNA.** El acto existia **porque los nodos repetian**, y lo que repetia
> **eran los bloques que `OP-F-04-WEI`, `OP-F-04-RAC` y el propio paso 1 de esta operacion se
> llevaron.** Eso no es un fracaso de la operacion: **es el destejido haciendo su trabajo.**

**LO QUE EL CIERRE NO HACE, y va dicho porque callarlo seria peor:** no toca un solo nodo; no fija
`superviviente` ni `eliminar` (**sin fusion no hay superviviente que fijar**); y **no cambia el
estado de la operacion**, que sigue en `LISTA` **igual que `OP-D-01` y `OP-D-02`, que tambien
estan ejecutadas**. El esquema no tiene otro estado y **la casa registra el hecho consumado en la
nota.**

---

## 5. LAS GUARDAS OBLIGATORIAS, todas por corrida propia de hoy

| guarda | resultado |
|---|---|
| `run_phase1.py --reaplico-curaduria` | **exit 0**, `GATE 0: OK`, **20 `[OK]` y 0 `[FALLO]`**, 3.853 compilados, 3.538 activos, 315 deprecados, **alcanzabilidad 100 % (3.538/3.538)** |
| `etiquetas_de_cara.py --aplicar` | **71 etiquetas** |
| `sync_assets_web.py` | **verde**, manifiesto escrito, **seis assets** |
| **el derivado sale BYTE IGUAL** | `git status` **no lista ni `dataset/metadata` ni `web/lib`** despues del ciclo entero |
| suite del motor (`engine/run_all_tests.py`) | **25 de 25** |
| suite web (`npx vitest run`) | **80 ficheros, 1.030 pasadas, 3 saltadas** |
| `npx tsc --noEmit` | **cero lineas** |
| verificador de mapas, con los TRES planes | **3 tablas, 17 filas, 0 discrepancias, exit 0**, corrido **dos veces** (`SALIDA_V36_VERIFICADOR_MAPAS.txt` y `_B.txt`) |

> **ESTA VUELTA NO ANADIO NINGUNA TABLA DE PARTICION**, y por eso el verificador sigue contando
> **3 tablas y 17 filas**, las mismas que la 35. Lo que se pego en `LECTURAS_DIRIGIDAS.md` es un
> **bloque de salida de instrumento**, no una tabla tecleada.

---

## 6. CORRECCIONES DECLARADAS DE ESTA VUELTA

1. **La conclusion de las DOS FAMILIAS CERRADAS de la vuelta 34 queda VOLTEADA, no en suspenso.**
   La vuelta 35 la habia dejado en suspenso porque el volcado no era suyo; hoy el volcado ocurrio
   y **el dibujo se rehizo con el texto de hoy**. Texto viejo conservado entero.
2. **Una correccion mia que corrige a otra correccion mia de la misma tarde.** En el commit
   `c8c4e0b3` escribi que *el acto tiene hoy UN solo par `A`, el 643*; **unas horas despues el
   `643` dio `D` y son cero.** La cifra vivio menos de una tarde. **No se borra: se tacha y se
   fecha**, porque el `9.10` no distingue entre una tabla vieja de un mes y una de media hora.
3. **La cifra de la fila `core` de `RECOMPUTO_3388.md` (344) NO se reescribe**, y va dicho: es la
   foto del 13 de agosto y **reescribirla fabricaria una corrida que nunca existio**. Lo que se
   corrige es el **total** y la **correccion declarada** que lo explica.
4. **El apartado `b. Actos: 335` de `RECOMPUTO_3388.md` no se remide, se le pone AVISO DE CORTE.**
   Ese apartado dice de si mismo *se cita aqui con su corte, no se remide*, asi que **no es una
   tabla envejecida por la regla vigente**; pero un lector podia tomarlo por vigente, y ahora
   apunta al dato de hoy.
5. **La `PROPUESTA_V35_RELECTURAS.json` conserva su campo `estado` diciendo *PROPUESTA NO
   VOLCADA*.** **No lo toque a proposito:** es el sello de la vuelta 35 y **lo que dice era cierto
   el dia que se escribio**. Que hoy este volcada consta en el archivo, en el lote y en este
   reporte. **Va marcado como discutible.**

---

## 7. PENDIENTES DE DOCTRINA

1. **NUEVO Y ES DE ESTA VUELTA: el esquema de `OPERACIONES.jsonl` no distingue una operacion HECHA
   de una pendiente.** Las **71** estan en `LISTA`, **incluidas `OP-D-01`, `OP-D-02` y ahora
   `OP-D-03`, las tres ejecutadas**. Hoy eso **solo se lee en la nota**, y la nota es prosa. **No
   invente un estado nuevo** porque la regla 5 lo prohibe.
2. **NUEVO: que hace el plan con una operacion cuyo acto se disolvio.** `OP-D-03` cierra sin
   fusion, pero **ninguna pagina dice si un acto disuelto se archiva, se borra del inventario o se
   queda como acto de cero.** El inventario sigue contando **556 actos** y no lo toque.
3. **NUEVO: la figura que esta operacion deja, propuesta y NO adoptada: UN ACTO PUEDE MORIR DE SU
   PROPIO DESTEJIDO.** Queda escrita en `02_DESTEJIDOS.md` como propuesta. **Ninguna pagina la
   tiene, y no la adopto yo.**
4. **NUEVO, y es de bucle mas que de plan: el orquestador no cubre las DOS especies de caida.** El
   parche del fundador caza al **auditor mudo**; la caida de la vuelta 35 fue **fallo instantaneo
   seguido de un reintento que nunca ocurrio**. **Un proceso que anuncia una espera y no vuelve no
   deja sintoma en ningun sitio salvo un hueco de tres dias en el log.**
5. **SIGUE VIVO (era el 4 de la vuelta 35): que umbral acompana a `MIN_BLOQUE = 2`.** No se toco.
6. **SIGUE VIVO (era el 5 de la 35): contra que nodos se recalibra la puerta de costuras**, si los
   dos historicos ya no son reproducibles.
7. **SIGUE VIVO (era el 6 de la 35): un verificador que mide media vara si no le pasan un
   argumento.**
8. **SIGUE VIVO (era el 7 de la 35): hasta donde atras alcanza el barrido del `9.10`.** **Esta
   vuelta lo volvio a tocar sin resolverlo:** decidi corregir lo vigente y dejar los checkpoints
   fechados, **por precedente y no por regla escrita.**
9. **SIGUE VIVO (era el 8 de la 35): los nodos propios de esta pasada escritos sin acentos.**
10. **CERRADO por la decision del fundador del 15 ago 2026** (era el 1 de la vuelta 35, *hasta
    donde llega `P.5` hacia atras*): el alcance esta escrito en `BANCO_DEL_PLAN.md`, **dentro del
    acto en operacion y nada mas.** Se anota como cerrado **para que la cuenta no arrastre un
    pendiente muerto.**
11. **CERRADO tambien** (era el 3 de la 35, *que hace una operacion cuyo acto se disuelve*):
    **el fundador lo contesto para este caso** (`D` cierra la operacion sin fusion). **Queda
    abierto lo general, que es el pendiente 2 de arriba.**

---

## 8. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

| # | que | por que es discutible |
|---:|---|---|
| **d1** | **El `643` leido `D`. ES EL DISCUTIBLE DE LA VUELTA ENTERA** | **es el UNICO par del acto donde el objeto de un nodo esta NOMBRADO DENTRO del objeto del otro:** `split_testing` lista *precio* entre sus cuatro variables y su condicion de activacion dice *precio* con todas sus letras. **Quien lo lea `A` tiene una frase literal del catalogo de su lado**, y la razon vieja la escribio mejor que nadie: *no es una tecnica distinta, es la misma con una de sus cuatro variables*. Lo sostengo con la contencion medida y con que la propia razon vieja nombro el motivo para no fundir. **Pero este par se lee al reves sin forzar nada** |
| **d2** | **Voltear un veredicto cuya razon vieja es EXACTA sobre el texto de hoy** | las otras cinco cayeron porque el texto se movio; **esta cae solo por criterio.** Un auditor puede decir que **eso es re cribar**, y que re cribar es justo lo que el fundador acaba de acotar al fijar el alcance de `P.5`. **Lo sostengo con que `P.5` manda leer el acto ENTERO y el fundador lo mando explicitamente**, pero **la frontera entre releer y re cribar la cruza este par** |
| **d3** | **No declarar `ARISTA QUE FALTA` en el `643`** | el ejemplar del **755** declaro arista **sin madre e hijo**, porque lo compartido cubria tres pasos del superviviente. **Aqui cubre dos de cuatro, que es la mitad**, y esta al filo. Lo resuelvo por el lado del **827** (linea contra linea con cableado propio) **y lo marco** |
| **d4** | **Apoyar cinco de los seis volcados en el criterio del `738`** | lo escribio la vuelta 34, **que nadie audito**. **Lo digo yo antes que el auditor**, y es la razon por la que el `643` se midio con una segunda vara que no depende de aquella. **Las cinco no tienen esa segunda vara** |
| **d5** | **Cerrar `OP-D-03` dejando el estado en `LISTA`** | un auditor puede decir que una operacion cerrada **tiene que verse en el estado y no en la prosa de una nota de 5.200 caracteres**. Lo sostengo con que **el esquema no tiene otro estado** y con que las dos operaciones ya ejecutadas estan igual. **Pero es un cierre que no se ve contando estados** |
| **d6** | **No tocar el campo `estado` de `PROPUESTA_V35_RELECTURAS.json`**, que sigue diciendo *NO VOLCADA* | quien lo lea suelto **creera que sigue sin volcarse**, y eso es exactamente **la especie de papel que envejece** que persigue el `9.10`. Lo sostengo con que **es el sello de otra vuelta** y con que era cierto el dia que se escribio. **Pero es un fichero de estado, no un acta fechada** |
| **d7** | **No corregir las tablas de tramo del cribado que citan el `277`, el `374` y el `452` como `A`** | son **fotos de su corte** por el precedente de las vueltas 33 y 34, **pero el precedente no es regla escrita** (es el pendiente 8). **Contadas en el barrido, son decenas de lineas** |
| **d8** | **Reutilizar `vuelta34_leer_opd03.py` para imprimir los nodos del `643`** | es instrumento de la vuelta sin auditar. Lo sostengo con que **duplicarlo habria sido peor**, pero **hereda lo que aquel tenga mal**. Es el mismo discutible que la 35 marco como su `d10` |
| **d9** | **Declarar yo la correspondencia paso a paso del `643`** | el script hace **la aritmetica**, pero **quien dice que el paso 3 de uno hace pareja con el paso 4 del otro soy yo**. Lo mitigo imprimiendo **el texto de los dos pasos al lado de cada fila**, para que se discuta mirandolo. **Pero no es una medicion ciega** |
| **d10** | **Proponer la figura del acto que muere de su propio destejido** | la escribo **como propuesta y no adoptada**, pero **la escribo en un documento de plan y no en un cajon**. Un auditor puede decir que **una figura propuesta dentro del plan ya pesa** |
| **d11** | **Contar TRES commits y decir que el reporte hace cuatro** | la vuelta 33 cayo por esta cuenta. **Escribo las dos cifras a proposito**; si el auditor cuenta *commits de trabajo* dira que son **dos** |

---

## 9. PREGUNTAS

1. **El `643` esta bien leido?** Es la pregunta de la vuelta y **la traigo yo, no espero a que me
   la hagan.** Recomiendo **verificarla contra los dos nodos impresos**, no contra mi razonamiento.
2. **Una operacion cerrada deberia verse en el estado?** Recomiendo **si**, y que se anada un
   estado al esquema. **No lo hice yo** porque inventar vocabulario es inventar reglas.
3. **Que se hace con un acto disuelto en el inventario?** Sigue contando **556 actos** y `OP-D-03`
   ya no tiene componente. **No lo toque.**
4. **Y la de bucle, otra vez y ahora con dos especies medidas: por que el auditor lleva TRES
   vueltas sin correr?** La 34 corrio mudo, **la 35 fallo a los 4 segundos y el reintento de 30
   minutos nunca aparecio en el log**, y la 36 es esta. **El parche del fundador cubre la primera
   especie. La segunda sigue descubierta.**
