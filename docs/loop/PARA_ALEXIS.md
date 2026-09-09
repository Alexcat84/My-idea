# PARA ALEXIS. CAMPAÑA CONSUMADA POR EL LADO DEL BUCLE (9 sep 2026)

**Escrito por decision del fundador, no por el auditor.** El bucle queda
DETENIDO y `docs/loop/PROMPT_SIGUIENTE.md` queda VACIO.

**NO SE PIDE EL MERGE.** La auditoria integral, con credencial y con el fundador
delante, va antes. Este documento es la base medida sobre la que esa auditoria
empieza.

---

## 1. LA DECISION, Y SU MOTIVO

> **DECISION DEL FUNDADOR (9 sep 2026): la Fase III se DECLARA AGOTADA POR EL
> LADO DEL BUCLE.** Las tres clausulas que quedan A MEDIAS de las 17 **NO se
> persiguen con mas vueltas**: suben **NOMBRADAS como HERENCIA DECLARADA** a la
> auditoria integral, que corre con credencial y con el fundador delante, y es
> la que decide si cubren, si se remiten o si piden trabajo.

**EL MOTIVO, ESCRITO POR EL FUNDADOR:** la lista de clausulas **crecio mientras
se cumplia**, de **14 a 17 en tres vueltas**, y **perseguir un blanco que se
mueve** es el patron que la parada del 7 sep ya nombro
(`paradas/2026-09-07-el-bucle-se-volvio-el-bucle.md`).

**LO QUE ESTO NO ES:** no es que las tres se den por buenas. Es que **dejan de
ser trabajo de bucle y pasan a ser materia de la integral**, que es la unica que
puede decidirlas.

---

## 2. EL INVENTARIO FINAL DE LAS 71 FICHAS, CON SUS PRUEBAS

**Medido en esta sesion**, no heredado, con la vara del expediente
(`scripts/loop/vuelta150_3_relectura_expediente.py --corte 97af7fef`), que es la
vara vigente del trabajo pendiente. **El campo `estado` NO se usa para esto:**
esta jubilado desde el 4 sep 2026 y asi lo declara `docs/plan/00_INDICE.md`.

| que | cuanto |
|---|---:|
| fichas en `docs/plan/OPERACIONES.jsonl` | **71** |
| fichas en el arbol de trabajo | **71** |
| **que CALZAN con el campo** | **31** |
| **que NO calzan** | **40** |

**LAS 40 QUE NO CALZAN, POR SU MOTIVO Y CONTADAS DE LA TABLA:**

| motivo | cuantas |
|---|---:|
| CONGELADO DECLARADO (la ficha habla de su estado) | **24** |
| CONGELADO EN SILENCIO (la ficha no dice nada de su estado) | **12** |
| **HECHA SIN NINGUNA PRUEBA** (el estado afirma mas que el repo) | **4** |

**LAS CUATRO QUE AFIRMAN MAS QUE EL REPO, NOMBRADAS:** `OP-V-01`, `OP-L-01`,
`OP-L-02` y `OP-L-03`. Las cuatro llevan `HECHA` en el campo y **ninguna de las
tres pruebas en el repo**. **No se tocan aqui:** el campo esta jubilado y la
reconciliacion ficha por ficha **es acto de la integral**, por la decision del 4
sep 2026.

**LA COBERTURA DE CADA PRUEBA, CONTADA POR LA VARA:**

| prueba | cuantas fichas |
|---|---:|
| **P1**, vara de grafo | **71** con veredicto computable, de ellas **20 con DESTINO CUMPLIDO** |
| **P2**, vara de codigo (el `id_op` presente en codigo vivo) | **20** |
| **P3a**, huella en git (mensaje mas rutas de `dataset/`, `web/`, `engine/`) | **59** |
| **P3b**, caso positivo o mutacion citado y presente en el arbol del corte | **4** |

**Y LA CUENTA QUE MAS IMPORTA PARA CERRAR:** **3 fichas en `LISTA` sin ninguna
de las tres pruebas**, de las cuales **1 es trabajo real**; y esa una **es una
MESA cuyo producto documental SI existe en disco**. **Que ese documento cubra lo
que la ficha describe es LECTURA, y esta vara no la hace.** Queda para la
integral, dicho por la propia vara y no por mi.

---

## 3. EL CIERRE INTEGRAL, MEDIDO EN LA ULTIMA VUELTA

Todo lo de esta seccion sale de `docs/loop/SALIDA_V220_CIERRE_INTEGRAL.txt`,
sellado por la vuelta 220.

**EL CICLO ENTERO DE GATE 0, LOS DOS LADOS:**

- **18 salidas selladas** de las 18 que deberia haber. **0 ausentes, 0 de cero
  bytes, 0 sin exitcode dentro.**
- **PEOR EXITCODE DE LAS DIECIOCHO: 0.**
- Las **dos consolas** del ciclo, selladas por el propio instrumento, las dos
  declarando **peor exitcode 0**.

**LAS TRES SUITES, CORRIDAS SOLAS Y CADA UNA CON SU EXITCODE:**

| suite | exitcode | bytes de su salida |
|---|---:|---:|
| motor | **0** | 1.131 |
| `tsc` | **0** | 24 |
| web | **0** | 336 |

**EL MARCADOR Y EL CENSO, RECOMPUTADOS CADA UNO CON SU COMANDO:**

- **MARCADOR:** n **3.388**, A **550**, B **71**, C **5**, D **2.762**, huecos **0**.
- **CENSO:** **3.853** nodos, **3.169** vivos, **684** deprecados.
- **ARISTAS:** siguientes **8.780**, previos **8.740**, suma **17.520**, union
  **9.914**.

**LAS TRECE CIFRAS, COTEJADAS CONTRA LO QUE LA 219 PUBLICO:** 13 cotejadas, **0
que no calzan**, 13 que debian quedarse quietas y se quedaron, **0 que debian
moverse**.

**LAS TRECE SEDES QUE LA VUELTA PUDO MOVER, COTEJADAS POR SU `sha256`:** 13
cotejadas, **0 que se movieron**. Ni el plan, ni los veredictos, ni el banco, ni
el grafo, ni el acta. Entre ellas `dataset/metadata/master_graph.json`
(`627cc662296f7f00`, 8.375.817 bytes) y `docs/plan/OPERACIONES.jsonl`
(`650578474361eb2b`, 517.181 bytes).

---

## 4. LAS TRES CLAUSULAS A MEDIAS, NOMBRADAS UNA A UNA

**El recuento de las 17 se publica CON LAS DOS CIFRAS, porque son dos mediciones
ciertas de cosas distintas:**

| veredicto | lo que el lector mide SIN la adjudicacion 4.5 | lo que la adjudicacion 4.5 deja |
|---|---:|---:|
| CUBRE | **14 de 17** | **15 de 17** |
| **A MEDIAS** | **3 de 17** | **2 de 17** |
| NO CUBRE | **0 de 17** | **0 de 17** |

**LAS TRES, CONTRA EL ARBOL, QUE ES LO QUE SUBE A LA INTEGRAL:**

### 4.1 `03 FUSIONES` indice 0. A MEDIAS

**LA CIFRA:** **71 actos sin fundir** por la lectura ancha, y **SEIS fusiones de
19 nodos** por la estrecha.

**POR QUE QUEDA:** su clausula pide *un superviviente por acto, el resto
DEPRECADO CON ALIAS*, y **las dos lecturas de acto dan cifras distintas**. Cual
de las dos manda **es doctrina, y la doctrina es del fundador**.

### 4.2 `07 ADUANA` indice 0. A MEDIAS

**LA CIFRA:** **el quinto control sin correr**, de los que su clausula pide
*corriendo en Gate 0*.

**POR QUE QUEDA, y viene con una divergencia pegada que sube nombrada y sin
tocar:** la **linea 30** de `docs/plan/08_VERIFICACION.md` dice **CUATRO**
controles y su ficha `OP-A-02` dice **CINCO**. **Es la tercera acta seguida que
la nombra y nadie la ha escrito**, porque escribir en esa pagina es sede del
fundador.

### 4.3 `05 SANEO` indice 1. A MEDIAS CONTRA EL ARBOL, CUBRE EN LA ARITMETICA

**ESTA ES LA TERCERA, Y ES LA MAS FACIL DE PERDER DE VISTA.** La adjudicacion
`4.5` del acta 219 la sube a **CUBRE**, acotando su punto de verificacion **por
correccion declarada** a los dos nodos que `OP-S-02` alcanza, por extension de la
decision del fundador del 28 ago 2026: *el contenido que la operacion no alcanza
se anota en la ficha y no se ejecuta, y el punto de verificacion se acota por
correccion declarada*.

**PERO ESA ESCRITURA NO ESTA EN EL PLAN.** El propio reporte de la 220 lo declara
en su `D.2`: la subida **se aplica solo sobre la tabla que el lector imprime, en
memoria**, y **el arbol sigue diciendo 14 mientras el reporte dice 15**. **La
divergencia la sostiene la prosa, no un fichero**, y el auditor dice por que no
la escribio: **`docs/plan/08_VERIFICACION.md` es sede del fundador.**

> **POR ESO SON TRES Y NO DOS: contra el arbol quedan tres. La tercera no espera
> trabajo, espera UNA FIRMA.**

---

## 5. LAS DOS PARADAS DE LA BATERIA DE LA VUELTA 220

**La bateria corrio ENTERA Y SOLA por sus once tramos**, sellados uno a uno en
esa vuelta: **11 hechos, 0 faltan, 0 de cero bytes**, **135 entradas exactamente
una vez**, **270 corridas** por la doble corrida, **13,6 minutos** de reloj y una
salida unica de **93.479 bytes**. **Y aun asi los once salen en ROJO POR FALLO**,
por dos motivos que el auditor **no reparo** porque la moratoria se lo prohibe.

### PARADA 1. SIETE ARNESES QUE NO MUERDEN

**Y no son nuevos: la lista es IDENTICA a la de la corrida anterior en 11 de 11
tramos.** Los siete, por su nombre:

- `vuelta160_tarea6b_mutacion_puerta.py`
- `vuelta165_tarea6_mutacion_op_l_01.py`
- `vuelta166_tarea2_mutacion_correccion.py`
- `vuelta168_tarea1_mutacion_nota.py`
- `vuelta168_tarea2_mutacion_reconstructor.py`
- `vuelta171_mutacion_busqueda_acta.py`
- `vuelta185_tarea1c_mutacion_bateria_continuada.py`

**Un mutante que no muere es una guarda que no muerde**, y esa es exactamente la
especie que el 7 sep 2026 quedo escrita como **CIFRA PUBLICADA**.

### PARADA 2. DOS ARNESES FUERA DE LA NOMINA, Y SON DOS REGLAS VIGENTES CHOCANDO

- `vuelta197_tarea2_mutacion_orden_del_turno.py`
- `vuelta199_tarea1_mutacion_guardas_revividas.py`

**LAS DOS REGLAS, LAS DOS ESCRITAS Y LAS DOS VIGENTES:** el fichero de la bateria
dice **desde la vuelta 148** que un arnes **entra en la nomina**; la moratoria
(`AUDITOR.md` 6.3, del 7 sep 2026) dice que la nomina queda **CONGELADA EN 135,
ni crece ni se poda**, y que **la poda se decide en la auditoria integral y no
antes**. **Los dos arneses nacieron entre una regla y la otra**, en las vueltas
197 y 199.

> **MIENTRAS LAS DOS ESTEN PUESTAS, ESTA BATERIA NO PUEDE SALIR EN VERDE.** No es
> un fallo del bucle: es **una contradiccion de doctrina**, y resolverla es del
> fundador.

**Y EL AUDITOR LO DIJO CONTRA SU PROPIO INTERES:** es la misma razon por la que
la bateria de la 215 tambien salio en rojo, y **el acta 219 la dio por corrida**.
El de la 220 **se declara corrido por el mismo criterio** y **marca como
discutible que ese criterio sea el bueno**.

---

## 6. LA COLA QUE LAS ACTAS FUERON NOMBRANDO

**Siete entradas, escritas en la seccion 6 del acta 219 con su linea, y ninguna
resuelta a proposito:**

| # | linea del acta | lo que sube |
|---:|---:|---|
| 1 | 78026 | la familia `C.1` del auditor en **NUEVE actas seguidas**, con TRES mediciones de fallo del remedio del fundador. **Sube con TRES OPCIONES concretas** |
| 2 | 78039 | **DOS divergencias**, ya no una, entre la pagina 08 del plan y lo adjudicado: la linea 30 (CUATRO controles contra los CINCO de `OP-A-02`) y la linea 28 (el punto de `05 SANEO` idx 1 acotado en la prosa y sin acotar en su texto) |
| 3 | 78044 | el carril del lanzador de la bateria **no distingue la vuelta de las salidas que mira**, y hoy responde que no falta ningun tramo; hermano del rotulo que dice VUELTA 183 sobre el contenido de la 215 |
| 4 | 78049 | `scripts/loop/vuelta150_4_tabla_por_fase.py` en rojo (*la tabla no trae ocho filas: 11*), y queda por decidir si se repara o si su vara de ocho filas se retira |
| 5 | 78053 | **la ciega no puede acertar lo que el archivo decide por BARRIDO DE FAMILIA**, por transitividad sobre veredictos de otros puestos: **NUEVE de los catorce fallos** del auditor son de esa especie |
| 6 | 78059 | las clausulas que quedan con su cifra, que son las de la seccion 4 de este documento |
| 7 | 78062 | el remedio de dictado de la `C.4`: **la pareja de bytes no es una regla de RUTAS, es una regla de CIFRAS DE BYTES**, vengan de una ruta o de un campo de texto |

---

## 7. QUE SIGUE, Y QUE NO

**LO QUE SIGUE: LA AUDITORIA INTEGRAL, CON CREDENCIAL Y CON EL FUNDADOR
DELANTE.** Es la que decide, sobre todo lo de arriba: si las tres clausulas
cubren, se remiten o piden trabajo; si la nomina de la bateria se poda; que se
hace con los siete arneses que no muerden; y **la reconciliacion ficha por ficha
del campo `estado`**, que el 4 sep quedo reservada a ese acto.

**LO QUE NO SE PIDE Y NO SE HACE: EL MERGE.** `pasada-unica` **no se ha fundido
con nada**, ni el bucle lo ha intentado nunca. **El merge es del fundador y viene
DESPUES de la integral**, no antes.

**Y UNA COSA QUE SE DICE EN VEZ DE CALLARLA:** el arbol de trabajo tiene ficheros
de la vuelta 220 **sin commitear** (salidas del turno y el sello de apertura del
auditor). **No se tocan aqui:** son de su turno, y el bucle esta **detenido, no
revertido**.
