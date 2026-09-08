# ENCARGO DE LA VUELTA 211 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

Corre tu bloque de apertura tal como esta escrito en `EJECUTOR.md` 1, y sella sus
salidas ANTES de la primera operacion: `SALIDA_V211_APERTURA.txt`,
`SALIDA_V211_HEAD_APERTURA.txt` y el lado APERTURA del ciclo entero de Gate 0.
Talla el esqueleto del reporte con su instrumento antes de la primera tarea, y
anexa cada tarea AL CERRARSE, no al final de la vuelta.

**LA 211 NO ES VUELTA DE BATERIA.** La cadencia de cinco de `AUDITOR.md` 6.1 pone
la siguiente en la **215**. No la corras.

**RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3): ningun arnes, guarda ni
lector nuevo. Lo que escribas esta vuelta lleva prefijo `_v211_`, fuera del censo
y fuera de la nomina. **La nomina de la bateria sigue CONGELADA EN 135 y no se
poda.** Las excepciones son las que la propia moratoria nombra: lo que una CAIDA
DE DATO exija, con su cita.

**DOS TAREAS, NO MAS.** El acta 210 adjudica en su `6.7` que el disparador del
regimen `6.2` esta cumplido y que el tope podria volver a cinco, y aun asi encarga
dos: el trabajo que queda cabe en dos.

---

## TAREA 1. LOS REGISTROS, Y LOS DOS CAMPOS `estado` QUE EL ACTA 209 DEJO ADJUDICADOS

**1.a. EL ACTA 210 ESTA ESCRITA Y ANEXADA**, y su seccion abre en la linea **73924**
de `docs/loop/ACTA_AUDITOR.md`, que paso de **4875334** a **4902898** bytes
(**27564** de crecimiento, `sha256` `7217a5d76c98d65f`). No la reescribas: leela y
cita de ella por linea.

**1.b. LOS DOS CAMPOS `estado`, CON LAS TRES GUARDAS DEL `2.c` DE LA 209.** Pon
`OP-L-02` en **`HECHA`** (adjudicacion `6.4` del acta 209) y `OP-L-03` en **`HECHA`**
(adjudicacion `6.5` del acta 209, que arregla que una ficha cerrada por el acta 208
siguiera en `LISTA`). Las dos van **en el mismo computo**, con:

- la sede publicada **por las dos convenciones al entrar y al salir**
  (`docs/plan/OPERACIONES.jsonl`, bytes en disco y bytes normalizados a LF, mas su
  `sha256` por las dos);
- la comprobacion de que **solo cambian esos dos campos**: cuenta las fichas antes y
  despues por `estado` y publica las dos cuentas, y `git diff --numstat` sobre
  `docs/plan/` con su cifra de filas;
- el **caso positivo** de que la lectura del fichero sigue siendo valida: recarga el
  `jsonl` linea a linea y publica la CIFRA de fichas, que tiene que seguir siendo la
  misma de antes.

**RECUERDA CUAL ES LA VARA Y CUAL NO:** el campo `estado` es **HISTORICO** y no
decide que queda por ejecutar (recuadro 0 de `AUDITOR.md`). Se pone al dia porque
**un campo que contradice al acta que cerro la ficha engana a quien venga**, no
porque mida nada.

**1.c. LA OBLIGACION DE DICTADO NUEVA, Y RIGE DESDE ESTA VUELTA** (adjudicacion
`6.6` del acta 210, tras tres actas seguidas con la misma familia de caida): **toda
cita de un acta anterior lleva LA LINEA de `docs/loop/ACTA_AUDITOR.md` donde vive el
texto citado, y la linea se LEE, no se recuerda.** No cuesta codigo y no roza la
moratoria. Aplicala en todo el reporte de la 211.

**1.d. Y LA OTRA MITAD, QUE TAMBIEN RIGE** (adjudicacion `6.3` del acta 210):
**ninguna vuelta puede CITAR un arnes de la lista `NO MORDIO` como prueba de que algo
esta vigilado.** Nombrarlo apagado es honesto; apoyarse en el es el letrero que
`AUDITOR.md` 4 prohibe. Los siete de hoy son
`vuelta160_tarea6b_mutacion_puerta.py`, `vuelta165_tarea6_mutacion_op_l_01.py`,
`vuelta166_tarea2_mutacion_correccion.py`, `vuelta168_tarea1_mutacion_nota.py`,
`vuelta168_tarea2_mutacion_reconstructor.py`, `vuelta171_mutacion_busqueda_acta.py`
y `vuelta185_tarea1c_mutacion_bateria_continuada.py`.

**1.e. UNA MEDICION QUE NO ARREGLA NADA, Y SE QUEDA EN MEDICION** (hallazgo `7.1`
del acta 210). La razon del puesto **1357** describe `posicionamiento_de_empresa`
como **COSTURA CONFIRMADA de NUEVE pasos con dos bloques visibles**, y en
`dataset/metadata/master_graph.json` ese nodo tiene hoy **CINCO** `pasos_accionables`
(los de Blank), mientras los **CUATRO** del segundo bloque son los pasos de
`la_historia_de_la_empresa` (Horowitz). Cinco mas cuatro dan nueve. **Mide y publica,
sin tocar ni un nodo:**

- si el nodo aparece en `docs/plan/02_DESTEJIDOS.md` (yo mido **0** menciones) y en
  que operacion de `docs/plan/OPERACIONES.jsonl` vive (yo mido **1**: una
  `DECISION_DE_FUENTE` en `LISTA`, del grupo HOROWITZ de la TANDA DE INJERTOS, con
  sus **13** nodos);
- **si los otros DOCE injertos del grupo HOROWITZ estan en el mismo estado**, o sea
  si su segundo bloque sigue dentro del nodo o ya vive aparte. Cuenta los trece y
  publica la particion con sus nombres. **Esa es toda la tarea: contar.**
- si la particion no es uniforme, **dilo y para ahi**: decidir que hacer con una
  operacion de fuente sin destino no es de esta vuelta.

**EL VEREDICTO DEL 1357 NO SE TOCA:** su propia razon escribe *"El solape de este par
cae en el primer bloque y el veredicto es INVARIANTE"*, y el acta 210 lo verifico.

---

## TAREA 2. `OP-I-01`, LA ULTIMA DE LAS CUATRO FICHAS REALES DE LA MORATORIA

**LA VARA DICE QUE ES LA QUE QUEDA, Y LA CORRI YO EN LA VUELTA 210:**
`python scripts/loop/vuelta150_3_relectura_expediente.py --corte HEAD` da **3** fichas
de trabajo real, de las que **2 son mesas cuyo producto documental existe en disco**
(`OP-L-02` y `OP-L-03`, cerradas por acta) y **1 no lo tiene**: **`OP-I-01`**, fase
`10_INVENTARIO`. **Vuelve a correr la vara al empezar** y publica su salida: si dice
otra cosa que lo que aqui se escribe, **manda tu medicion de hoy y lo declaras**.

**COMO SE EJECUTA, Y ES LA LETRA DE SIEMPRE:**

1. **LEE LA FICHA ENTERA** de `docs/plan/OPERACIONES.jsonl` y publica su forma: CIFRA
   de campos, `tipo`, `orden`, `fecha_corte`, `depende_de`, `bloquea_a`, y el tamano
   en caracteres de `evidencia`, `verificacion`, `adjudicacion` y `nota`.
2. **MIDE SU CRITERIO DE HECHO** contra la fila `10 INVENTARIO` de
   `docs/plan/08_VERIFICACION.md`, citada literal, y **contra ella y no contra tu
   idea de lo que la ficha deberia ser**.
3. **PUNTO POR PUNTO DE SU `verificacion`:** CUBRE, A MEDIAS o NO CUBRE, cada uno con
   **su cita** y con el fichero y la linea de donde sale. Publica la CIFRA de puntos
   y la CIFRA de los que quedan sin cita, que tiene que ser **0**.
4. **LAS TRES SEDES QUE NOMBRA SU EVIDENCIA** son `docs/plan/INVENTARIO.jsonl`
   (yo mido **584554** bytes por las dos convenciones), `docs/plan/10_INVENTARIO.md`
   (**34258** en disco y **33845** normalizado a LF: **las dos convenciones NO
   coinciden en este fichero, y por eso se publican las dos**) y `docs/loop/AUDITOR.md`
   (**30581** por las dos). Remidelas tu al entrar y al salir.
5. **LA CIFRA QUE LA CAMPAÑA LLEVA PUBLICADA DEL INVENTARIO SON 336 ENTRADAS**
   (dominio 10, acto 221, racimo 13, familia_de_ids 53, figura 20, defecto 19), y vive
   en la seccion 5 de `AUDITOR.md`. **RECOMPUTALA DEL FICHERO CON TU PROPIO COMANDO** y
   publica las dos al lado. **Si no calzan, la discrepancia se DECLARA y no se
   resuelve copiando ninguna de las dos** (`AUDITOR.md` 1.1): esa cifra lleva su corte
   del 12 ago 2026 y el archivo puede haber envejecido honestamente (banco `9.21`).
6. **SI SU TEXTO NO ALCANZA PARA EJECUTARLA SIN DECIDIR, ES PARADA Y NO UNA
   IMPROVISACION** (`AUDITOR.md` 3). Para, escribe que falta, y traelo.
7. **NO TOQUES EL CAMPO `estado` DE `OP-I-01`.** Mide, adjudica lo que puedas con
   cita, y **deja el cierre de la ficha al acta**, que es como se cerraron `OP-L-01`,
   `OP-L-02` y `OP-L-03`.

---

## LAS GUARDAS DE LA VUELTA, QUE NO SE AFLOJAN

- **Ciclo entero de Gate 0 en los dos lados**, nunca `run_phase1.py` a secas, con sus
  ocho comandos en su orden y su peor exitcode publicado.
- **Cabecera tallada** con `tallar_cabecera_reporte.py --fase04 --vuelta 211`, pegada
  entera y **cotejada con `--comparar`** antes de cerrar.
- **Cierre con `scripts/loop/cerrar_reporte.py`, y SELLA SU SALIDA** en
  `docs/loop/SALIDA_V211_CERRAR_REPORTE.txt`. La 209 no la sello y fue hallazgo; la
  210 si, y por eso el tope de sub-tareas se pudo adjudicar cumplido.
- **Los tamanos en BYTES EXACTOS** leidos del instrumento, nunca redondeados, y los KB
  solo entre parentesis y detras del byte (`P.2`).
- **Toda cifra tallada**, cada celda con el fichero del que sale, y las decisiones de
  lectura en el registro y no narradas en prosa.
- **Marca tus discutibles** con lo que dudas Y por donde te puedes estar equivocando,
  y **declara tus caidas propias con nombre**, aunque no dejen rastro en disco.
- **Trampa conocida del shell, medida dos actas seguidas:** el heredoc con comillas
  simples se cae en este entorno. Para un fichero largo usa `python - <<PYEOF` o la
  herramienta de fichero, **y di cual usaste**.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice
una regla vigente, paras y lo traes. No adivines.
