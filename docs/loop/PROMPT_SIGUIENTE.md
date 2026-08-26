# ENCARGO DE LA VUELTA 79 (ejecutor Sonnet 5)

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Tu acta de referencia es `docs/loop/ACTA_AUDITOR.md`, **vuelta 78, desde la
linea 22702**. Todo lo que sigue sale de ahi, y cada cifra que esa acta publica
tiene su fichero `docs/loop/_auditor_v78_*` al lado para que la puedas contar
tu mismo en vez de creerme.

**LO PRIMERO, PORQUE CAMBIA COMO SE ESCRIBE ESTA VUELTA:** la racha de caidas
de reporte vuelve a **DOS TANDAS SEGUIDAS**, y ese es el numero exacto que el
fundador dejo escrito como gatillo de la **ESCALADA AUTOMATICA de la opcion
(b)** en `docs/loop/paradas/2026-08-26-racha-tramo-mecanico-DECISION.md`, linea
183. La escalada es la TAREA 2 y es **BLOQUEANTE**: no se lee un solo candidato
nuevo hasta que este verde. **La parada de esta especie pide TRES tandas: la
vuelta 79 es la ultima que hay.**

**Y LO SEGUNDO, PORQUE ES LA NOTICIA BUENA:** cero caidas de clase y cero de
cifra publicada en la vuelta 78. La racha que el acta 77 dejo en UNA, con el
aviso de que una sola mas era parada, **vuelve a CERO**. Las 25 aristas, la
reversion, las once disposiciones de la TAREA 3.2, las cuatro correcciones del
plan y las 24 escrituras del tramo 4 **se sostienen todas**, verificadas por
corrida propia del auditor.

---

## TAREA 1: LOS REGISTROS Y LAS CORRECCIONES DECLARADAS

### 1.1. Registra la caida de reporte de la vuelta 78, con su nombre

**UNA caida de reporte, DENTRO del marcado** (acta 78, seccion 3, D4 y seccion
7). No la vuelvas a medir: ya viene medida, y se cita como fuente.

> El reporte de la vuelta 78, seccion 3.2, publica **un criterio unico para las
> once aristas**: *"si el extremo ESCRITO en la arista esta condenado por una
> operacion sin ser su superviviente, la arista SE MUEVE; si el extremo escrito
> ES el superviviente declarado, o si ninguna operacion condena al extremo
> escrito, la arista SE QUEDA"*. **La fila 11 de su propia tabla dice que el
> hijo escrito NO esta en ninguna nomina, y aun asi SE MUEVE.** El criterio
> publicado no produce la decision publicada, y ademas no distingue la fila 11
> de la 4 ni de la 6, que tienen la misma forma y se quedaron.

**Cero caidas de clase y cero de cifra publicada.** Registralo tambien: la
racha de esa especie vuelve a cero.

### 1.2. Correccion declarada: el criterio real de la TAREA 3.2, escrito donde se pueda auditar

El criterio que de verdad decidio las once **existe y es bueno**, pero vive
solo en el docstring de `scripts/loop/vuelta78_tarea32_decision_once.py`, no en
el reporte. **Escribelo con el texto viejo delante y sin reescribirlo**, en
`docs/plan/04_ENLACES.md`, bajo las notas de `P.9.1` que ya estan ahi, como
CORRECCION DECLARADA de la vuelta 79. La linea que hay que dejar dicha, y que
el auditor adjudica por cita de `P.9` punto 2, es esta:

> **No es lo mismo que el companero de A caiga en el `eliminar` de una FUSION
> que en los `nodos` de un RENOMBRE_CON_ALIAS.** Una fusion **ya declara
> superviviente**: si el extremo escrito no es el condenado, el extremo escrito
> esta a salvo y la arista SE QUEDA (filas 2, 3 y 4). Un renombre **no mata a
> nadie y no declara ganador**: cual de los dos gemelos vivira sigue abierto,
> asi que la arista escrita sobre cualquiera de los dos SE MUEVE y espera
> (fila 11). **Y cuando el archivo remite la familia a mesa, manda la mesa**
> (fila 6, puesto 460).

Verificalo contra la ficha antes de escribirlo: `OP-M-05-APERTURA` tiene
`superviviente` `customer_validation` y `eliminar` de dos ids; `OP-S-09` es
`RENOMBRE_CON_ALIAS` con `superviviente` en `null`. **Corre tu propio comando y
cita su salida.**

### 1.3. Registra las cinco adjudicaciones del auditor

De la seccion 5 del acta 78, sin remedirlas:

1. **D1** (`diferencia_iso9001_iso9004 -> trilogia_de_juran`): **la arista se
   queda**, por banco 9.6.2. Cerrado.
2. **D2** (`conformidad_comercio_internacional -> sistema_gestion_calidad`):
   **se queda**, por banco 9.6.2, con el lado flojo declarado. Cerrado.
3. **D3**: **no es sobre-conexion por termino generico**, y tres de las cuatro
   se quedan. **La cuarta va a relectura conjunta** (TAREA 3.1).
4. **D4**: **las once disposiciones se confirman una a una.** Solo el criterio
   publicado se corrige (1.2).
5. **D5** (`requisitos_numericos_calidad_lotes -> critica_acceptable_quality_level`):
   **la abstencion se confirma y el PENDIENTE DE DOCTRINA queda DISUELTO por
   cita** de banco 9.6.2 (el hijo no ejecuta el paso: lo deroga, y su entregable
   literal es eliminar el AQL que el paso manda definir) y de banco 9.6.3
   (procedimiento en los dos lados: el par es sano y sigue caminos distintos).
   **Borra el pendiente de la seccion 7 del reporte y escribe en su lugar la
   cita.** No queda ninguna doctrina nueva pendiente.

---

## TAREA 2: LA ESCALADA AUTOMATICA DEL TALLADOR A LA FASE 04. **BLOQUEANTE**

Es la opcion (b) del fundador y se dispara sola por la racha de dos. No es
opinion del auditor: es la condicion escrita, y se cumple.

`scripts/loop/tallar_cabecera_reporte.py` existe y funciona, pero lee
`SALIDA_V<N>_MARCADOR_*.txt` y `SALIDA_V<N>_RECOMPUTO_*.txt`, que son salidas
**del cribado**, y la fase 04 no produce ninguna de las dos. Por eso desde que
el bucle entro al tramo mecanico todas las cifras del reporte volvieron a ser
frases tecleadas.

**Lo que hay que hacer, sin cambiar el nombre del fichero ni clonarlo por
vuelta** (esa disciplina ya esta escrita en su cabecera):

1. **Anade un modo de fase 04** que talle **las dos columnas** de la cabecera,
   apertura y cierre **por separado**, cada una leida de SU propia salida del
   dia: censo del grafo y las tres comprobaciones de `SALIDA_V<N>_GATE0_CMD1_*`,
   las cuatro cifras de aristas de `SALIDA_V<N>_CONTEO_*`, el motor de
   `SALIDA_V<N>_MOTOR_*`, la web de `SALIDA_V<N>_WEB_*`, el `tsc` de
   `SALIDA_V<N>_TSC_*` y el marcador de `SALIDA_V<N>_MARCADOR_*` si la vuelta lo
   produce. **Un lado no puede heredar del otro**, que es el bug que la vuelta
   56 pago.
2. **Que caiga en ROJO, sin escribir nada, si alguna celda no se puede leer.**
   Es la mecanica que el tallador ya tiene y no se toca.
3. **Que `--comparar docs/loop/REPORTE.md` funcione** en la fase 04, cotejando
   fila a fila y nombrando cada celda que difiera.
4. **CASO POSITIVO OBLIGATORIO, y hazlo con una vuelta vieja que ya sabemos que
   estaba mal**: talla la cabecera de la vuelta 78 con las salidas
   `SALIDA_V78_*` que ya estan en el repo y compara contra el `REPORTE.md` de
   la vuelta 78 archivado en `0ea71f3a`. **Debe salir identica**, porque esas
   cifras las verifique yo al digito. Si sale distinta en alguna celda, **paras
   y lo traes**: significaria que una de las dos mediciones esta mal y eso ya
   no es cosa del tallador.
5. **Usa el tallador en tu propio reporte de esta vuelta**, apertura y cierre,
   y dilo en el reporte con el comando escrito.

**Gate 0 con su ciclo de tres, motor, web y `tsc` en verde antes de pasar a la
TAREA 3.**

---

## TAREA 3: LA RELECTURA CONJUNTA Y LA RELECTURA AL DOBLE DEL TRAMO 4

### 3.1. Relectura conjunta de UNA arista, con el caso del auditor escrito

**`extraer_priorizar_hipotesis -> value_proposition_startup`** (escrita en el
tramo 4, fila 14 de las 191, sin veredicto del cribado).

**Mi caso, y lo verificas tu contra el grafo antes de decidir** (acta 78,
seccion 3, D3):

- El paso 1 de la madre es *"Lista todo lo que tiene que ser cierto sobre tu
  modelo de negocio, tu propuesta de valor y tu cliente"*. **La accion del paso
  es listar hipotesis.** La propuesta de valor es uno de los tres objetos sobre
  los que se listan, no la accion.
- El hijo (identificar problemas del segmento, definir que caracteristicas los
  resuelven, verificar el encaje hablando con clientes) **no ejecuta ese paso:
  es su insumo**, y el resumen de la propia madre lo dice: *"A partir de tu mapa
  de propuesta de valor y tu modelo de negocio, identifica todas las
  suposiciones"*.
- **Banco 9.6.2**, formulacion literal: *"la prueba de que el paso de la madre
  es un procedimiento es que existe el hijo que lo ejecuta"*. Aqui el hijo lo
  precede.
- **Y tu propio reporte descarta la misma especie ocho lineas mas abajo**:
  `timing_solicitud_referidos -> fase_adopt_ciclo_cliente`, *"el paso senalado
  nombra la fase Adopt solo como ejemplo parentetico"*.
- **Las otras tres del mismo hub se quedan**, y por que se quedan esta escrito
  en la tabla del acta: en las tres la accion del paso ES la propuesta de valor
  (revisarla, definirla, dejarla explicita).

**Decide con la vara, par a par, contra el grafo.** Si la reviertes, hazlo
**quitando las dos vistas a la vez** (la leccion de tu propia seccion 3.2) y
con correccion declarada y recomputo. Si la sostienes, escribe el argumento con
la cita del banco por numero: **mi caso es un caso, no una orden.**

### 3.2. Relectura al doble del tramo 4, por el credito rebajado

El credito de la tanda queda **REBAJADO** porque el hallazgo del par en dos
direcciones (TAREA 4) aparecio **fuera de los discutibles marcados**. Por
`AUDITOR.md` seccion 1.2, el tramo 4 se relee al doble. La vara, en dos
barridos, los dos con fichero de salida y **la tabla contada de su fichero**:

1. **Cruza las 24 aristas escritas del tramo 4 contra
   `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**, emparejando **sin direccion**.
   Publica par a par si el cribado lo habia leido y con que clase. **Mi corrida
   dice: 2 de las 30 leidas tienen veredicto (3205 D y 637 B), cero clase A,
   cero a revertir** (`docs/loop/_auditor_v78_treinta_tramo4.txt`). Si tu
   corrida da otra cosa, **declara la discrepancia en vez de copiar la mia**.
2. **Cruza las 24 contra la bolsa calibrada buscando el mismo par en la
   direccion contraria**, que es la vara nueva de la TAREA 4. Publica cuantas
   de las 24 tenian su reciproca propuesta y no leida. **Mi corrida dice: UNA,
   la fila 46, y ya la adjudique** (se queda como esta escrita). Confirma o
   discrepa.

---

## TAREA 4: LA GUARDA DEL PAR NO DIRIGIDO, ADJUDICADA POR CITA Y SIN DOCTRINA NUEVA

**El hallazgo, medido por el auditor** (acta 78, seccion 4): la bolsa filtrada
de 191 traia **el mismo par dos veces, una en cada direccion**:

| fila | par | paso |
|---:|---|---:|
| **1** | `necesidades_reales_vs_declaradas -> descubrir_necesidades_del_cliente` | 2 |
| **46** | `descubrir_necesidades_del_cliente -> necesidades_reales_vs_declaradas` | 3 |

El tramo 4 leyo la fila 1 y escribio la arista; **la fila 46 quedo resuelta sin
que nadie la mirara**, porque el campo `arista` del calibrador **no tiene
direccion** y al escribir en un sentido las dos filas se marcan. **Un par que
el instrumento propone en las dos direcciones es el caso exacto para el que el
banco 9.6.2 se escribio** (*"LA VARA TIENE DIRECCION"*, y se escribio aparte
*"porque se aplico al reves tres veces y ninguna de las tres se detecto al
escribirla"*).

**LA GUARDA, adjudicada por cita del banco 9.6.2 y de `AUDITOR.md` seccion 3
(el criterio del forastero: la fuente propone, la lectura confirma):**

1. **Antes de leer, la bolsa filtrada se agrupa por par NO DIRIGIDO.**
2. Cuando el mismo par aparece en las dos direcciones, **las dos filas se leen
   JUNTAS y la direccion se decide con 9.6.2 explicitamente**, con las dos
   opciones escritas en la razon y la descartada nombrada.
3. La fila hermana **no se cuenta como candidato aparte** en la cifra de bolsa
   restante.

**CASO POSITIVO OBLIGATORIO, con datos sinteticos que no toquen el grafo
real**: que la guarda agrupe un par propuesto en las dos direcciones, que
publique las dos filas juntas, y que no rompa el caso normal de un par
propuesto en una sola direccion.

**La direccion del par de la fila 1 ya esta adjudicada por el auditor y NO se
toca**: la madre conserva materia propia que el hijo no toca (la miopia de
marketing de Levitt y el rediseno de la propuesta de valor) y el hijo despliega
el paso 2 de la madre con 6 pasos de procedimiento. **La arista se queda como
esta escrita.**

---

## TAREA 5: EL TRAMO 5 DE `OP-E-01`

Solo si las TAREA 1 a 4 cerraron en verde.

1. **Recalibra la bolsa FRESCA** con los mismos umbrales
   (`--umbral-titulo 72 --umbral-contencion 0.45 --min-tokens 4`). **NO reuses
   `PASO_NODO_CALIBRADO_FILTRADO_V78.jsonl`**: el grafo se movio con las 24
   aristas del tramo 4, y mi corrida de hoy sobre el grafo final ya da **258**
   sin arista contra los 283 de la corrida de tu seccion 4.1
   (`docs/loop/_auditor_v78_bolsa_delta.txt`). **Sella y restaura
   `docs/plan/PASO_NODO_CALIBRADO.jsonl` si lo tocas.**
2. **Corre el filtro `P.9.1` ensanchado ANTES de leer nada**, con las tres
   varas ya vigentes (operaciones por `eliminar`, `superviviente` y `nodos` de
   `RENOMBRE_CON_ALIAS`; y los veredictos **A** con los dos extremos vivos) mas
   **la guarda del par no dirigido de la TAREA 4**. Publica la tabla de
   apartados **contada de su fichero**.
3. **Lee 30 candidatos** en orden de fichero, sin sorteo, con el criterio ya
   adjudicado y sin cambio: **veredicto del cribado PRIMERO**; el sufijo
   numerico y el racimo solo opinan cuando no hay veredicto; **cuando el paso
   que el calibrador senala no es el que calza, manda la lectura y se declara
   cual es el que calza** (acta 77, D1); y **cuando el paso solo NOMBRA un
   objeto en vez de mandar una accion sobre el, no hay jerarquia** (acta 78, D3,
   por banco 9.6.2). Dossier completo en fichero.
4. **Escribe las aristas sanas en LAS DOS VISTAS a la vez**
   (`nodos_siguientes` y `nodos_previos`), que es la leccion de la
   simetrizacion de tu propia seccion 3.2. **Chequeo de escalera exacto sobre
   las escritas**, contado de su fichero.
5. **Los no escritos van con su razon, uno a uno**, y los discutibles se marcan
   ANTES de saber si aciertan.
6. **Gate 0 con su ciclo de tres, motor, web y `tsc` en verde al cerrar**, y la
   cabecera del reporte **tallada con el instrumento de la TAREA 2**, no
   tecleada.

---

## LO QUE NO SE TOCA ESTA VUELTA

- `OP-E-02` sigue **HECHA** (vuelta 76). No se vuelve a abrir.
- `OP-E-03` sigue esperando a que `OP-E-01` termine entero.
- `OP-M-03-ENLACES`, `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES` y
  `OP-M-01-SEXTO` siguen esperando a la fase 06 por remision escrita.
- Las **diez aristas de la fase 04 que la vara de los A sigue tocando** quedan
  como observacion, no como parada: ninguna operacion las condena hoy, y las
  verifique una a una.
- **El merge a staging o a produccion no es del bucle.** La rama sigue siendo
  `pasada-unica`.

---

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
