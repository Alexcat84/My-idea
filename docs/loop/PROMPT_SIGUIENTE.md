# ENCARGO DE LA VUELTA 206 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

## LO QUE MANDA ESTA VUELTA, Y VA DELANTE PARA QUE NO SE DEDUZCA

**LA 205 CORRIO SU BATERIA ENTERA Y NO LA CERRO. ESTA VUELTA LA CIERRA Y NO LA
REPITE.** Los ONCE tramos estan sellados y committeados, ninguno de cero bytes,
del mismo calibre y sumando las 135 entradas de la nomina; lo que quedo cortado es
el CIERRE. **Mi adjudicacion `4.2` lo resuelve por `AUDITOR.md` 6.1**, *"una vuelta
cortada retoma en el tramo siguiente, no desde el principio"*. **NO VUELVAS A
CORRER NI UN TRAMO: tirarias 42.0 minutos de corrida sellada, que es exactamente lo
que el regimen por tramos vino a impedir.**

- **EL TOPE ES DE DOS SUB-TAREAS** (`AUDITOR.md` 6.2, mi adjudicacion `4.4`). El
  disparador de salida pide **DOS vueltas seguidas** que cierren su propio reporte:
  la 204 cerro y **la 205 no**, asi que la racha se corto y el tope vuelve a dos.
  **Este encargo trae DOS tareas y ninguna mas.**
- **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3): ninguna vuelta fabrica
  arneses, guardas ni lectores nuevos que se queden vigilando. **LA NOMINA SIGUE
  CONGELADA EN 135**, y la conte yo con `ast` sobre `VIEJAS`: son **135**, sobre un
  censo de **197**. **No la podes y no la crezcas.** Un fichero `_v206_*` con
  prefijo de guion bajo, fuera del censo y fuera de la nomina, es computo de una
  vuelta y no roza la moratoria (acta 199 `4.5`, acta 203 `4.6`, mi `4.1`).
- **NO SE MUEVE NINGUN CAMPO `estado`, NINGUNA CLASE Y NINGUN VEREDICTO.** Medido
  por mi al cerrar la 205: `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en **4054129**
  bytes de disco y **4054129** normalizado a LF, `sha256` LF **`0a77b5a35a962621`**;
  `docs/plan/OPERACIONES.jsonl` en **513043** y **513043**, `sha256` LF
  **`829c583eb779cab6`**. **Remidelos tu y publica las dos convenciones.**
- **`dataset/`, `web/`, `engine/` y `docs/plan/` en cero filas de `numstat`**, al
  entrar y al salir. Si corres el Gate 0, corre **el ciclo entero**, nunca
  `run_phase1.py` a secas. **AVISO MEDIDO, PARA QUE NO LO DENUNCIES COMO CAIDA:**
  `git status` marca `dataset/metadata/master_graph.json` como modificado y **no lo
  esta**; es el aviso de fin de linea de git. El fichero es identico en crudo al de
  HEAD, **8375817** bytes y `sha256` LF **`627cc662296f7f00`** en los dos.
- **LOS TAMANOS EN BYTES EXACTOS**, nunca redondeados, y los KB solo entre
  parentesis (`P.2`). **Detras de cada ruta va SU tamano al cierre.** **Cada cifra
  junto a su pareja en el MISMO renglon.**

## LA SEDE DEL AUDITOR NO SE ESCRIBE, Y SIGUE VIGENTE SIN CAMBIOS

**`docs/loop/PROMPT_SIGUIENTE.md`, `docs/loop/ACTA_AUDITOR.md` y
`docs/loop/PARA_ALEXIS.md` SON SEDE DEL AUDITOR.** El ejecutor **no los escribe, no
los reescribe, no los borra y no los reordena**. Si crees que tu encargo siguiente
deberia decir otra cosa, **lo propones en tu reporte**, en una seccion titulada
**`LO QUE PROPONGO PARA LA VUELTA SIGUIENTE`**. **Proponer es tuyo. Encargar es mio.**

**LA 205 LA CUMPLIO Y LO MEDI EN `git`, NO EN SU PALABRA:** la vuelta entera solo
toco `docs/loop/` y `scripts/loop/`, y las once cifras de bytes y `sha256` de sus
once mensajes de commit **calzan las once** con mi medicion. **Publica al cerrar el
`numstat` de las tres sedes del auditor contra tu HEAD de apertura, y las tres
tienen que dar 0**, distinguiendo que el cero de `PARA_ALEXIS.md` es **de ausencia
de fichero**.

## LO QUE MI ACTA 205 ADJUDICO, PARA QUE NO SE VUELVA A LEVANTAR

- **EL ROJO DE LA BATERIA ES ESTRUCTURAL Y NO ES TUYO** (mi `5.3`). Los once tramos
  dan `ROJO POR FALLO` con exitcode 1 por **una sola causa**: los **2** arneses del
  censo nacidos despues de la vara **148** que la nomina congelada en **135** no
  puede admitir, y son `vuelta197_tarea2_mutacion_orden_del_turno.py` y
  `vuelta199_tarea1_mutacion_guardas_revividas.py`. **No lo arregles, no lo saltes y
  no lo escondas: lo citas como estructural y sigues.**
- **EL ENVOLTORIO `_v205_bateria_en_su_nombre.py` QUEDA ADJUDICADO A FAVOR** (mi
  `4.1`): no es clon, importa el lanzador y solo le corrige el numero de vuelta.
  **Uselo tal cual para componer. No lo clones y no escribas otro.**
- **`--siguiente` DEL LANZADOR SIGUE MINTIENDO Y HOY NO SE TOCA** (mi `5.2`): computa
  su vuelta del nombre del fichero (lineas **91, 92, 96** de
  `scripts/loop/vuelta183_bateria_por_tramos.py`) y por eso responde **183** en
  cualquier vuelta, dando los once tramos de la 183 por sellados con cero que
  faltan. **Va a la auditoria integral, ya nombrado, para que la 211 no lo
  redescubra.** **Si lo corres, no creas su respuesta: mira los ficheros `V206`.**
- **LA VARA DE `cobertura` SIGUE DIFERIDA A LA INTEGRAL** (acta 203 `4.7`, acta 204
  `4.8`). **Acertar no autoriza a escribirla.**
- **EL PATRON DE `preguntas_del_reporte()` ES CODIGO Y HOY NO SE TOCA** (acta 204
  `4.4`), aunque este roto: casa con `^##\s+\d+\.\s+PREGUNTAS\b` y el articulo `LAS`
  le rompe la coincidencia, en `scripts/loop/_v203_reparto_de_actas_viejas.py` linea
  **196**. Va a la integral.
- **`OP-I-01`, `OP-L-01` Y `OP-L-02` NO SE CIERRAN.** No las levantes y no les toques
  el `estado`.
- **LA OPERACION DE CODIGO DE LA ESCALADA SIGUE ENCARGADA Y CON SU EJECUCION
  SUSPENDIDA** (acta 202 `4.6`, ratificada por la 203 `4.9`, la 204 `4.10` y por mi):
  se ejecuta en la **primera vuelta despues de que la moratoria se levante**.
  **PROPONLA otra vez en tu reporte para que la 207 la arrastre.**

## TAREA 1: CERRAR LA VUELTA 205, QUE ES LO QUE QUEDO A MEDIAS

**VA PRIMERA Y ES BLOQUEANTE.** Hasta que esto cierre, la bateria de la cadencia de
cinco **no esta declarada corrida** y la 210 heredaria el mismo agujero que la 205
heredo de la 200.

1. **COMPON LA SALIDA UNICA CON `--componer`**, por el envoltorio y no por el
   lanzador a pelo: `python scripts/loop/_v205_bateria_en_su_nombre.py --componer`.
   La compuesta se llama **`SALIDA_V205_BATERIA.txt`** y **no existe todavia**:
   lo verifique yo. **EL CALIBRE LO COTEJA `--componer`, NO TU OJO NI EL MIO**
   (`AUDITOR.md` 6.1, y es mi adjudicacion `4.3`). Yo mire el calibre con mi propio
   instrumento y me dio **una sola familia de secciones sobre los once**, pero **eso
   no sustituye a la herramienta**, y por eso te lo encargo en vez de darlo por
   hecho. **Si `--componer` sale ROJO, eso es un hallazgo y lo declaras con su
   salida; no lo tapas y no lo repites hasta que salga verde.**
2. **PUBLICA LA TABLA DE LOS ONCE TRAMOS EN TU REPORTE**, con **bytes de disco,
   bytes LF, lineas, `sha256` LF, exitcode y minutos**, medidos por ti en esta
   vuelta. **Las once filas ya las medi yo y estan en mi acta**: si alguna de las
   tuyas discrepa de la mia, **declara la discrepancia en vez de copiar la mia**.
3. **CIERRA EL REPORTE DE LA 205 CON `scripts/loop/cerrar_reporte.py` Y SUS CUATRO
   PIEZAS**, y **archivalo**. El esqueleto de la 205 sigue en **27 lineas** con
   **todas sus celdas en PENDIENTE** y su veredicto **sin escribir**: hoy se rellena.
   **Tu seccion 9 lleva LA BATERIA, que es la cuarta pieza y la razon de ser de
   aquella vuelta, y NO lleva hueco declarado.**
4. **EL VEREDICTO DE UNA LINEA DE LA 205 LO ESCRIBES TU, Y TIENE QUE DECIR LAS DOS
   COSAS:** que la bateria corrio **entera y en su propio nombre por primera vez
   desde la 194**, y que salio **ROJA por la causa estructural** de los 2 arneses
   fuera de la nomina congelada.

## TAREA 2: LA DEUDA DE REGISTROS, QUE LLEVA DOS VUELTAS ARRASTRANDOSE

**SON DOS Y SON LAS DOS SIGUIENTES DE LA COLA:** el registro del **acta 179** y el
del **acta 180**. La serie la corri yo con `scripts/loop/serie_de_registros.py` y
esta **VERDE**: **60** entradas, **0** colisiones, **0** huecos, mayor escrito
**R.68**, y **SIGUIENTE LIBRE R.69**. O sea que van en **`R.69`** (acta 179) y
**`R.70`** (acta 180), en `docs/PENDIENTES.md`, **por adicion pura y en su sede**.

- **DESDE `R.69`, UNA ENTRADA PUEDE PEGAR EL REPARTO MEDIDO SIN USARLO COMO
  NUMERAL** (acta 204 `4.6`): el numeral sigue `NO COMPUTABLE` y el reparto va
  debajo, **marcado como medicion y no como numeral**.
- **NO USES `preguntas_del_reporte()` PARA CONTAR LAS PREGUNTAS DE ESAS ACTAS**: su
  patron esta roto y ya esta declarado arriba. **Cuenta a mano y di como contaste.**
- **NUNCA PUBLIQUES UN NEGATIVO** (`EJECUTOR.md` 9). Si tu instrumento devuelve
  cero, la frase que escribes encima es **"el patron no encontro nada"**, nunca
  **"no existe"**. La 204 se estrello justo ahi y yo mismo estuve a punto en esta
  vuelta: mi primer conteo de la nomina me dio **0** porque lei `VIEJAS` como lista
  de cadenas cuando es **lista de tuplas**. **Un cero de tu instrumento no es un
  hecho del mundo.**

## EL CIERRE

Cierra tu propio reporte con `scripts/loop/cerrar_reporte.py` y sus cuatro piezas.
Toda cifra que publiques sale del instrumento corrido **en esta vuelta**; una nota
vieja o un acta previa se citan **como contraste**, y si discrepan de la medicion de
hoy **la discrepancia se declara en vez de resolverse copiando**. **Antes de declarar
una PARADA, mide su premisa EN POSITIVO y pega la medicion.**

**NO CORRAS NADA PESADO EN PARALELO CONTIGO MISMO, Y ESTO SALE MEDIDO DE LA 205**
(mi `5.4`): el tramo 3 publico **RUIDO DE CONCURRENCIA: 2 fichero(s)**, y los dos
eran `SALIDA_V205_APERTURA.txt` y `SALIDA_V205_HEAD_APERTURA.txt`, **escritos por ti
mismo mientras tu propio tramo 3 corria**. Ese tramo tardo **11.2 minutos** contra
una mediana de **2.8** en los otros diez. **La guarda mordio de verdad y tenia
razon.**

**Cuenta tus propias caidas UNA SOLA VEZ, EN UN SOLO SITIO Y CON UNA SOLA ETIQUETA.**

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice
una regla vigente, paras y lo traes. No adivines.
