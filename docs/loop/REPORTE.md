# REPORTE DE LA VUELTA 38 (ejecutor Opus 5). FASE III, rama `pasada-unica`

**LAS TRES LECTURAS DEL CUARTO MIEMBRO HECHAS Y LAS TRES `D`; LOS DOS SUPERVIVIENTES ELEGIDOS POR
`P.8` POR LECTURA DE CONTENIDO; LOS DOS PLANES SELLADOS CON SU SIMULACION Y SU CASO POSITIVO. CERO
NODOS TOCADOS Y EL MARCADOR QUIETO.** La simulacion se gano el sueldo dos veces: **el enlace que la
`DECISION 3` del fundador pide no hay que escribirlo, la fusion lo pone sola**, y **las veinte
aristas que las dos fusiones dejarian cojas las escribe `run_phase1` en su paso 5**, con precedente
medido y no supuesto.

> **EL REPORTE ABRE PIDIENDO VERIFICACION COMPLETA** de las tres lecturas y de las dos elecciones,
> como manda la TAREA 3 del encargo. **Y trae una PARADA DE DOCTRINA que el ejecutor no resuelve**
> (seccion 7): la regla `FAMILIA DECLARADA` alcanza a los tres pares de la tanda y dice que no se
> peleen. **Si esa regla gobierna, las dos fusiones no se ejecutan.**

---

## 1. LO QUE ESTA VUELTA MOVIO, MEDIDO Y NO NARRADO

- **Hash de partida:** `f734ab67` (la decision del fundador sobre `OP-D-04`).
- **Hash final:** `1b2f3dd5`, **commit unico de la vuelta**, con el hook verde (motor y web). **La
  vuelta entera cabe en un commit porque no toca nodos**: no hay tramo que proteger contra una
  sesion que se caiga. **El hash se anade aqui despues de commitear**, que es la unica forma de
  citarlo sin inventarlo.
- **Rutas tocadas** (`git diff --cached --stat` contra `f734ab67`, corrido hoy con este reporte ya
  dentro): **26 ficheros, 4.043 insertadas, 366 borradas**. Por carpeta: `docs/loop` **15**,
  `scripts/loop` **9**, `docs/plan` **2**. **Cero merges.** **Las 366 borradas son UNA sola cosa: el
  reporte de la vuelta 37, que se sobrescribe por mandato de la regla 7.**
- **`dataset/`: CERO ficheros tocados. `web/`: CERO ficheros tocados.** Medido con
  `git status --porcelain dataset/ web/`: la salida sale **vacia**.
- **EL ARCHIVO DE VEREDICTOS NO SE TOCO.** Medido con la misma orden sobre
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `docs/INTRA_DOMINIO_PARES.jsonl`,
  `docs/RACIMOS_MIEMBROS.jsonl` y `docs/plan/OPERACIONES.jsonl`: **cero lineas de salida, los
  cuatro intactos.** **Ni un veredicto se emitio, ni una razon se reescribio.** Las tres lecturas
  de esta vuelta son **dirigidas**: viven en `docs/plan/LECTURAS_DIRIGIDAS.md` y no entran en la
  cola.

### APERTURA CONTRA CIERRE, con la salvedad dicha en vez de escondida

**LA APERTURA NO SE MIDIO POR SEPARADO, y se declara.** `EJECUTOR.md` regla 1, tercer parrafo,
manda medirla **antes de la primera operacion**, y esta vuelta abrio corriendo la guarda de
lecturas sin haber corrido antes `scripts/loop/vuelta31_estado.py`. **No se disfraza y no se
inventa una columna.**

**LO QUE SI SE PUEDE PROBAR, y es lo que hace que la falta no contamine ninguna cifra:** el
instrumento del estado lee `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `dataset/`,
`docs/plan/OPERACIONES.jsonl` y `docs/plan/INVENTARIO.jsonl`, **y los cuatro estan intactos contra
`f734ab67`**, medido arriba con `git status --porcelain`. **Un fichero que no cambio no puede dar
dos lecturas distintas**, asi que la corrida del cierre vale tambien como apertura, **y se publica
en UNA sola columna a proposito**: publicar dos columnas identicas sacadas de una sola corrida
seria exactamente la especie de la caida de la vuelta 28.

**Corrida de cierre:** `python scripts/loop/vuelta31_estado.py`, salida entera en
`docs/loop/SALIDA_V38_CIERRE.txt`.

| | **medido al cierre, 19 ago 2026** |
|---|---:|
| marcador: n / A / B / C / D | **3.388 / 575 / 83 / 8 / 2.722** |
| tasa de A | **17,0 %** |
| huecos / duplicados / clases fuera de ABCD | **0 / 0 / 0** |
| grafo: ficheros / ids / vivos / deprecados | **3.853 / 3.853 / 3.538 / 315** |
| enlaces / claves distintas | **16.849 / 15** |
| familias Weinberg / Horowitz / Hugos / Coleman / Rackham (vivos) | **72 / 93 / 111 / 75 / 47** |
| operaciones / estados / dependencias rotas | **71, todas `LISTA`, 0** |
| inventario | **672** |

**EL MARCADOR RECOMPUTADO POR SEGUNDA VIA Y POR OTRO INSTRUMENTO**
(`scripts/loop/vuelta38_marcador.py`, salida `docs/loop/SALIDA_V38_MARCADOR.txt`): **n 3.388, A
575, B 83, C 8, D 2.722**, y la suma de clases cuadra con `n`. **Identico al de la vuelta 37, que
es lo que tenia que dar: esta vuelta no emitio ni un veredicto.**

**TASA POR DOMINIO Y VARA POR TRAMO: NO APLICAN Y SE DICE POR QUE.** Las dos son cifras de tramo de
cribado, y **esta vuelta no corrio ningun tramo**: sus tres lecturas son dirigidas y estan fuera de
cola. **Publicar una tasa de tramo sin tramo seria repetir la de la vuelta anterior con fecha de
hoy**, que es lo que la regla 2 prohibe.

---

## 2. TAREA 1: LAS TRES LECTURAS DIRIGIDAS `LD-96` A `LD-98`. **LAS TRES `D`**

**Van enteras en `docs/plan/LECTURAS_DIRIGIDAS.md`, UNDECIMA TANDA.** Aqui va el saldo, no la
lectura.

**LA GUARDA CORRIO ANTES DE ESCRIBIR UNA LINEA** (`scripts/loop/vuelta38_ld_racimo.py`, salida
`docs/loop/SALIDA_V38_LD_RACIMO.txt`), y devolvio las cinco cosas que hacian falta: el racimo es
**mixto** por medicion (`brainstorming` de `quality`, los tres del taller de `core`); los tres
pares **sin veredicto** sobre 3.388 filas; los tres **fuera de cola** sobre 3.388 filas, asi que
**`n` no se mueve**; los cuatro nodos **vivos e impresos ENTEROS** antes de decidir nada; y las
tres aristas **buscadas en los dos sentidos y resueltas por alias** (`P.1`).

**LA NUMERACION, con su salvedad.** El barrido de `docs/` da hoy **98** como `LD` mas alto, pero
vive en `docs/loop/PROMPT_SIGUIENTE.md`: **es el encargo reservando los numeros, no una lectura
escrita.** El mas alto **escrito como lectura** sigue siendo el **95**.

| lectura | par | clase | arista |
|---|---|:---:|---|
| **`LD-96`** | `brainstorming` contra `brainstorming_divergente` | **D** | no hay, y **no se declara** |
| **`LD-97`** | `brainstorming` contra `brainstorming_efectivo` | **D** | **ya puesta en los dos extremos** |
| **`LD-98`** | `brainstorming` contra `reglas_brainstorming` | **D** | no hay, y **no se declara** |

**LA VARA, citada y no aludida:** `9.6.1` (la linea o el procedimiento) con **la direccion del
`9.6.2`**, la precision del `9.6.3` (el tamano del solape no decide), los **dos polos del `9.22`**
con su caso corriente, y el `67.6` para separar linea de procedimiento. **El criterio de la arista
que falta es el del 15 ago 2026** en `docs/plan/02_DESTEJIDOS.md`: bloque contra linea, no linea
contra linea.

**LA FIGURA QUE DECIDE LAS TRES, dicha una vez:** `brainstorming` es de Juran, tiene **siete** pasos
contra cuatro, cuatro y cinco, y **no es otra lista de reglas: es el protocolo de conduccion de la
sala**, con su antes (formular, comunicar, calentar), su durante (turnos, registro, corte por
fatiga) y **su despues (procesar y desduplicar), que ninguno de los tres del taller tiene**. La
vara devuelve **PROCEDIMIENTO en un solo sentido** en los tres pares, que es el caso corriente del
`9.22`: madre e hijo, el par **CONTINUA**.

**LO QUE LAS TRES `D` DECIDEN, por la tabla que el fundador escribio:** el racimo mixto **queda
decidido** y el cuarto miembro **se ENLAZA** al superviviente del taller. **No hubo `A`, asi que no
se escribio `PARA_ALEXIS.md` por esa via**, y la TAREA 2 procedio.

---

## 3. TAREA 2: LAS DOS ELECCIONES DE `P.8`, POR LECTURA DE CONTENIDO

**Van enteras en `docs/plan/02_DESTEJIDOS.md`, seccion `OP-D-04` ESTADO AL 19 ago 2026 (vuelta
38), y en el campo `eleccion_p8` de cada plan sellado.**

| triangulo | superviviente | decidio | el cableado |
|---|---|---|---|
| **EL TALLER** | **`reglas_brainstorming`** | **el contenido** | **VA EN CONTRA**: 13 de `brainstorming_efectivo` contra 11 del elegido |
| **LA ALTERNANCIA** | **`pensamiento_convergente_divergente`** | **el contenido** | **coincide**: 5 contra 3 y contra 2 |

**EL TALLER, en tres lineas.** `reglas_brainstorming` es el unico que cubre **los cinco momentos**
de la sesion (enunciado del problema, inmersion, reglas, captura visual, calentamiento); tiene
**dos piezas unicas** que ningun otro miembro del triangulo trae (la inmersion de campo y el
calentamiento nombrado); y **entrega mas lejos**, con las ideas *agrupadas por tema*.
`brainstorming_efectivo`, que gana el cableado, **no tiene ni un paso de captura** y aun asi promete
en su entregable una sesion documentada. `brainstorming_divergente` tiene **cero piezas unicas**.

> **TRECE CONTRA ONCE Y PIERDE EL TRECE.** Es la forma dura de `P.8`, la misma del acto II del
> racimo del pivote. **Y aqui ir contra el cableado cuesta CERO aristas, medido**: las trece de
> `brainstorming_efectivo` son reciprocas las trece y se redirigen solas.

**LA ALTERNANCIA, en dos lineas.** El triangulo se llama LA ALTERNANCIA y **solo uno de los tres
tiene los dos movimientos**: el embudo que estrecha y el descarte de ideas prometedoras no estan en
ninguno de los otros dos. Ademas es el unico cuya disciplina **se repite en el tiempo** (`67.6`) y
el unico cuyo entregable es un **documento que dura**. **El cableado coincide, y se declara que NO
fue lo que decidio.**

**LAS DOS TABLAS DE PERDIDAS (`P.13`), impresas desde los planes** con
`scripts/loop/vuelta38_tabla_perdidas.py` (salida `docs/loop/SALIDA_V38_PERDIDAS.txt`):

| | piezas | VIAJA | VIVE DENTRO | YA NO APLICA |
|---|---:|---:|---:|---:|
| el taller | **14** | 9 | 4 | 1 |
| la alternancia | **11** | 8 | 2 | 1 |

**LA FILA QUE MAS ENSENA es `P.13` en estado puro:** la regla *construir sobre las ideas de otros*
es la unica del triangulo que el superviviente no dice, asi que **la LINEA viaja**; pero **el
PROCEDIMIENTO de esa linea vive en `construir_sobre_ideas_ajenas`, que queda VIVO fuera de la
fusion** y que `P.10` manda enlazar. **Injertarlo tambien seria fabricar la repeticion nueva contra
la que `P.13` avisa.**

---

## 4. LOS DOS PLANES SELLADOS, Y EL CASO POSITIVO DE `P.7`

**`docs/loop/PLAN_V38_OPD04_TALLER.json`** y **`docs/loop/PLAN_V38_OPD04_ALTERNANCIA.json`**, los
dos con `estado` **SELLADO Y SIN EJECUTAR**, porque la `DECISION 2` del fundador manda que la
fusion espere el acta.

**NO ESTAN TECLEADOS.** Los escribe `scripts/loop/vuelta38_sellar_planes.py`, que **lee los textos
de origen de `dataset/nodos/`** (viajan verbatim), **deriva los pasos finales de los grupos** (no
se escriben dos veces) y **aborta sin escribir si un origen queda sin colocar o colocado dos
veces**. La prosa argumentada vive aparte, en `scripts/loop/vuelta38_bloques.py`, **para que se vea
de un vistazo que parte del plan esta medida y que parte esta escrita por un humano**.

**LA SIMULACION PREVIA DE `P.7` CORRIO SOBRE COPIA EN MEMORIA** y devolvio las seis cosas de la
regla (`scripts/plan/simular_fusion.py`, salidas `SALIDA_V38_SIM_TALLER.txt` y
`SALIDA_V38_SIM_ALTERNANCIA.txt`):

| | el taller | la alternancia |
|---|---:|---:|
| redirecciones de entradas vivas | **17** | **5** |
| deprecados que nombran y **no se tocan** | 0 | **1**, `fase_entender_modelo_negocio` |
| duplicadas **nuevas** que la fusion fabrica | **1** | **1** |
| auto aristas | **0** | **0** |
| aristas que quedarian declaradas en un solo extremo | **16** | **4** |

**EL CASO POSITIVO, y son dos, no uno.**

**UNO. EL ENLACE DEL CUARTO MIEMBRO YA ESTA PUESTO, y no se ve leyendo.** La `DECISION 3` manda
enlazar `brainstorming` al superviviente del taller si las tres lecturas dan `D`. **No hay que
escribir esa arista:** `brainstorming` nombra hoy a `brainstorming_efectivo` en sus
`nodos_previos`, ese nodo muere, la entrada se redirige, y el bloque 6 de la simulacion lo imprime
resuelto: **`reglas_brainstorming -> brainstorming`**.

**DOS. LA PREMISA DE LA RECIPROCIDAD SE FUE A MIRAR EN VEZ DE DEDUCIRSE, y por eso no cayo.** El
ejecutor de fusiones de la casa redirige a los vecinos y **no le escribe al superviviente las
aristas del absorbido**. Leido asi, las dos fusiones dejarian **20** aristas cojas en un grafo cuya
tasa de reciprocidad medida hoy es **99,59 por ciento** (15.448 de 15.511,
`scripts/loop/vuelta38_reciprocidad_post.py`). **Pero no las deja**: quien las escribe es
`scripts/run_phase1.py` en su **paso 5**, y el precedente esta **medido**, no supuesto, en el log de
la fusion de `OP-D-02` (**commit `72c718ea`**, `phase1_run_log.json`, `symmetrize_added` con las dos
aristas que gano `voz_del_cliente_voc`). **Los dos planes llevan por eso un bloque
`simetrizacion_esperada` con la lista entera y su guarda**: el dia de la ejecucion,
`symmetrize_added` tiene que traer **exactamente** 16 entradas para `reglas_brainstorming` y 4 para
`pensamiento_convergente_divergente`, **ni una mas ni una menos**.

**EL VERIFICADOR DE MAPAS CORRIO Y ESTA VERDE** (`scripts/loop/verificar_mapas_destejido.py` con
los cinco planes sellados, salida `docs/loop/SALIDA_V38_VERIFICADOR_MAPAS.txt`):

```
5 tabla(s), 31 fila(s), 0 discrepancia(s).
  vara 1 (todo numero citado en el motivo pertenece a su fila): CORRIDA
  vara 2 (la particion de la tabla calza celda a celda con el plan sellado): CORRIDA sobre 5 plan(es)
VERIFICADOR DE MAPAS DE DESTEJIDO: OK
```

---

## 5. CORRECCIONES DECLARADAS

**UNA, y va con el texto viejo entero delante, en `docs/plan/02_DESTEJIDOS.md`.** El estado de
`OP-D-04` publicado en la vuelta 37 decia **FUSION EN PARADA, TRES MOTIVOS MEDIDOS**. Los tres
estan resueltos y **por dos vias distintas que no se confunden**: el motivo 2 (la forma final) lo
resolvio **el fundador** el 19 ago 2026; los motivos 1 (no hay superviviente) y 3 (el racimo mixto
sin su cuarto miembro) los resuelve **esta vuelta, por lectura**. **El texto viejo no se borra: la
correccion va debajo, con su tabla de correspondencia.**

**UN INSTRUMENTO TOCADO, y va dicho con su motivo dentro del codigo.**
`scripts/loop/vuelta33_tabla_mapa.py` gana **una cabecera alterna para las tablas de condiciones**.
El motivo es una averia real y no una preferencia: `verificar_mapas_destejido.py` reconoce las
tablas de particion **por su cabecera**, la de *paso del resultado*, y compara su particion contra
`grupos_pasos`. **Una tabla de CONDICIONES publicada con esa misma cabecera se leeria como tabla de
pasos, no encontraria plan que calce y daria discrepancia por construccion.** Hasta hoy no se noto
porque las condiciones se habian publicado en prosa. **La cura es de una linea y no afloja ninguna
vara.**

---

## 6. LOS DISCUTIBLES MARCADOS, marcados ANTES de saber si acierto

**DOS, y el primero es el que puede tumbar la vuelta entera.**

**DISCUTIBLE 1, el `LD-96`** (`brainstorming` contra `brainstorming_divergente`). **Los cuatro
pasos del nodo de Tim Brown caben todos dentro del de Juran**, y lo que conserva de propio son dos
calificativos: *sin distracciones* y *post-its o pizarra*. Lo marco **`D`** porque la vara del
`9.6.2` **tiene direccion** y preguntar que anade el nodo compacto al nodo largo es la pregunta
invertida que esa regla prohibe. **Quien lo lea al reves dira `A`, y trae el argumento mas duro de
todos:** el puesto **823** ya lee `A` a este mismo nodo contra `brainstorming_efectivo`, y su razon
releida el 19 ago 2026 dice que **lo propio de `brainstorming_divergente` son TRES gestos de
taller**; **contra Juran no conserva ninguno de los tres, porque Juran los tiene los tres.** **Si
cae a `A`, la regla del fundador manda PARAR y las dos fusiones no se ejecutan.**

**DISCUTIBLE 2, el `LD-98`** (`brainstorming` contra `reglas_brainstorming`). **Cuatro de los cinco
pasos alineados y en el mismo orden**, que es la cuenta del puesto 2080. Lo marco **`D`**, y **digo
el punto exacto que lo puede tumbar: la clase de la inmersion previa.** La leo **LINEA** porque es
un puntero cuyos procedimientos viven fuera y estan cableados como sus `nodos_previos`. **Si se lee
PROCEDIMIENTO, hay procedimiento en los dos sentidos y el par puede ser `C` con enlace mutuo**; y
quien cuente los cuatro pasos alineados como el 2080 dira **`A`**. **Dato en contra que se escribe:**
el puesto **834** lee `A` a `reglas_brainstorming` contra `brainstorming_divergente` conservandole
sus tres piezas propias, y **dos de esas tres las tiene tambien Juran**.

**Y DOS DECISIONES DEL PLAN QUE NO SON LECTURAS PERO SE DISCUTEN IGUAL, marcadas aqui para que el
auditor las mire:**

- **EL ORDEN DEL NODO DEL TALLER.** Los cinco pasos del superviviente **conservan su orden relativo
  entre si**, y lo que viaja entra **a la cabeza** (el grupo y la sala) y **a la cola** (generar en
  sesiones separadas). **Es la opcion que no mueve nada del superviviente**, pero deja el acto de
  generar despues del calentamiento y de la captura, que es discutible como procedimiento.
- **EL TITULO Y LA ETIQUETA NO CAMBIAN.** El nodo resultante del taller es **la sesion entera** y
  sigue llamandose *Reglas de Brainstorming Efectivo*, con etiqueta *Organiza tu Lluvia de Ideas*.
  **`P.8` avisa que una cabeza que vale para todo no puede llamarse como una sola de sus partes.**
  No lo cambio porque cambiar un titulo no me lo pidio nadie, **pero lo dejo marcado.**

---

## 7. PARADA DE DOCTRINA: **LA REGLA `FAMILIA DECLARADA` ALCANZA A LAS TRES LECTURAS**

**Se trae y no se arregla (`EJECUTOR.md` regla 5), y esta medida**
(`scripts/loop/vuelta38_familia_declarada.py`, salida `docs/loop/SALIDA_V38_FAMILIA_DECLARADA.txt`).

**LA REGLA, tal como esta escrita** en `docs/INTRA_DOMINIO_INFORME.md` linea 26, generalizada el 11
ago 2026 **a TODO racimo declarado**: *un par cuyos DOS nodos pertenecen a un racimo ya declarado
lleva razon `familia declarada` y NO pelea la clase; se registra con la clase que la silueta
indique, sin argumentarla, porque la decision ya esta tomada en otro sitio*.

**LO MEDIDO HOY:**

| | |
|---|---|
| nomina del racimo *Las reglas del brainstorming* | **CUATRO** miembros: los tres del taller y `brainstorming` |
| los tres pares de la tanda, son intra nomina? | **LOS TRES** |
| pares intra nomina ya escritos | **TRES, y los tres `A`** (puestos 823, 834 y 234). **Dos citan la regla por su nombre** |
| operaciones de la fase `06_MESAS` que nombran a algun miembro | **CERO**, sobre las 71 de `docs/plan/OPERACIONES.jsonl` |

**EL CHOQUE, sin adornarlo:** las tres lecturas de esta vuelta **argumentan la clase de tres pares
que la regla dice que no se argumentan**, y los otros tres pares de la misma nomina estan escritos
`A`. **La regla se apoya en que la decision ya esta tomada EN OTRO SITIO, y ese otro sitio no existe
para este racimo**, medido hoy. **Es exactamente el hueco que la autorizacion del fundador viene a
llenar, y por eso las lecturas se escribieron; pero esa autorizacion se redacto como excepcion al
ALCANCE DE `P.5` y no dice una palabra sobre `FAMILIA DECLARADA`.**

**LO QUE ESTA EN JUEGO:** si `FAMILIA DECLARADA` gobierna, los tres pares se registran con la clase
de su familia, que es **`A`**, y entonces la condicion del fundador (*si alguna da `A`, el bucle
PARA*) **se cumple por doctrina y no por lectura**, y **las dos fusiones no se ejecutan**. Si
gobierna la autorizacion posterior y especifica, las tres son `D` y la fusion sigue. **El ejecutor
no elige entre las dos.**

**POR QUE NO SE PARO LA VUELTA AQUI, y va dicho para que se pueda discutir:** porque **detenerse no
habria costado menos que seguir**. Las dos tareas del encargo **no tocan ni un nodo**: escriben
lecturas y sellan planes. **Si la parada se resuelve a favor de `FAMILIA DECLARADA`, lo unico que
sobra es documentacion, y ni una sola linea de `dataset/` hay que deshacer.** El coste de haber
seguido es cero; el de haber parado con la vuelta a medias habria sido volver a medirlo todo.

---

## 8. PENDIENTES DE DOCTRINA

1. **`FAMILIA DECLARADA` contra las lecturas autorizadas del cuarto miembro.** La parada de la
   seccion 7. **No hay regla escrita que ordene una autorizacion especifica posterior frente a una
   regla general anterior**, y la campana ya la necesita dos veces.
2. **UNA OPERACION CON DOS SUPERVIVIENTES.** `docs/plan/OPERACIONES.jsonl` tiene **UN** campo
   `superviviente` por operacion y `OP-D-04` produce **DOS**. Sigue en `null`, **medido hoy**, y
   **no se toco**: escribir uno seria mentir por omision y escribir los dos seria estrenar un
   formato. **Ninguna pagina dice cual.**
3. **LA CLASE DE UN PUNTERO CON CASA PROPIA.** El `LD-98` se decide sobre si la inmersion previa es
   linea o procedimiento, y la regla practica del `67.6` **no dice que pasa cuando el paso nombra
   una actividad cuyo procedimiento vive en otro nodo YA CABLEADO como vecino**. Se resolvio como
   **puntero, o sea linea**, y queda **marcado como pendiente**, no como doctrina.

---

## 9. LO QUE PIDE ESTA VUELTA, en el orden en que sirve

1. **VERIFICACION COMPLETA de las tres lecturas** `LD-96` a `LD-98`, con los dos discutibles
   delante. **La lectura ciega de `LD-96` es la que decide si la vuelta 39 ejecuta o no.**
2. **VERIFICACION COMPLETA de las dos elecciones de `P.8`**, y en particular del taller, **donde el
   contenido va contra el cableado por 13 a 11**.
3. **ADJUDICACION DE LA PARADA DE DOCTRINA** de la seccion 7. **Es la unica que puede detener la
   ejecucion aunque las tres lecturas se confirmen.**
4. **Si el acta confirma las tres lecturas y las dos elecciones**, la vuelta 39 ejecuta las dos
   fusiones con `P.16`, corre el ciclo de Gate 0 y las suites, comprueba que el enlace del cuarto
   miembro llego solo, comprueba que `symmetrize_added` trae **exactamente** las 16 y las 4
   declaradas, enlaza los tres que quedan por `P.10` con `P.9`, cierra `OP-D-04` y retoma el modo
   continuo.

**`docs/loop/PROMPT_SIGUIENTE.md` NO se escribe en esta vuelta: el turno es del auditor.**
