# ENCARGO DE LA VUELTA 205 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

## LO QUE MANDA ESTA VUELTA, Y VA DELANTE PARA QUE NO SE DEDUZCA

**ESTA ES LA VUELTA DE BATERIA Y NO LLEVA NADA MAS.** `AUDITOR.md` 6.1, decision del
fundador del 5 sep 2026: la bateria corre **CADA CINCO VUELTAS, EN UNA VUELTA PROPIA QUE NO
LLEVA NADA MAS**: *"la bateria entera, su doble corrida, su reloj y su salida sellada. Nada
de trabajo de plan al lado."* La 200 es la anterior de la cadencia y **le toca a la 205**.

- **NO HAY TAREA DE REGISTROS EN ESTA VUELTA, Y NO ES UN OLVIDO MIO.** `AUDITOR.md` 1.4 pone
  los registros en la TAREA 1 de un encargo corriente, y **6.1 es posterior y mas
  especifica**: la vuelta de bateria no lleva trabajo de plan al lado. **La deuda de
  registros queda en 2** (actas **179** y **180**) **y la arrastra la 206.**
- **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3): **ninguna vuelta fabrica arneses,
  guardas ni lectores nuevos QUE SE QUEDEN VIGILANDO**. Un fichero `_v205_*` con prefijo de
  guion bajo, fuera del censo y fuera de la nomina, **es un computo de una vuelta y no roza
  la moratoria** (acta 199 `4.5`, acta 203 `4.6`). **LA NOMINA SIGUE CONGELADA EN 135**, y la
  conte yo con `ast` sobre `VIEJAS`: son **135** hoy. **No la podes y no la crezcas.**
- **NO SE MUEVE NINGUN CAMPO `estado`, NINGUNA CLASE Y NINGUN VEREDICTO.** Al cerrar la 204,
  medido por mi: `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en `sha256` **`0a77b5a35a962621`** por
  las dos convenciones, y `docs/plan/OPERACIONES.jsonl` en **`829c583eb779cab6`** por las dos,
  con **513043** bytes en disco y **513043** normalizado a LF. **Remidelos tu y publica las
  dos.**
- **`dataset/`, `web/`, `engine/` y `docs/plan/` en cero filas de `numstat`**, al entrar y al
  salir. Si corres el Gate 0, corre **el ciclo entero**, nunca `run_phase1.py` a secas.
- **LOS TAMANOS EN BYTES EXACTOS**, nunca redondeados, y los KB solo entre parentesis
  (`P.2`). **Detras de cada ruta va SU tamano al cierre**; el intermedio se dice sin nombrar
  la ruta. **Cada cifra junto a su pareja en el MISMO renglon.**
- **CON LA RACHA DE CIERRES POR ENCIMA DE DOS EL TOPE ES CINCO SUB-TAREAS.** La corri yo con
  protocolo del sello (medi **2443 bytes** y `sha256` LF `4469a54a3417f36b`, corri, restaure
  con `git checkout --`, remedi identico y `git status` en **0** filas) y **da 6**, con las
  vueltas **199, 200, 201, 202, 203 y 204**. **Este encargo trae UNA sola tarea, y es la
  bateria.**

## LA SEDE DEL AUDITOR NO SE ESCRIBE, Y SIGUE VIGENTE SIN CAMBIOS

**`docs/loop/PROMPT_SIGUIENTE.md`, `docs/loop/ACTA_AUDITOR.md` y `docs/loop/PARA_ALEXIS.md`
SON SEDE DEL AUDITOR.** El ejecutor **no los escribe, no los reescribe, no los borra y no los
reordena**. Si crees que tu encargo siguiente deberia decir otra cosa, **lo propones en tu
reporte**, en una seccion titulada **`LO QUE PROPONGO PARA LA VUELTA SIGUIENTE`**. **Proponer
es tuyo. Encargar es mio.**

**LA 204 LA CUMPLIO ENTERA Y LO MEDI EN `git`, NO EN SU PALABRA:** el `numstat` de las tres
sedes entre `59d32eee` y el commit de cierre real `e48d272f` da **0, 0 y 0**, y la vuelta
entera solo toco `docs/loop/`, `scripts/loop/`, `docs/loop/reportes/` y `docs/PENDIENTES.md`.
**Publica al cerrar el mismo `numstat` contra tu HEAD de apertura, y las tres tienen que dar
0**, distinguiendo que el cero de `PARA_ALEXIS.md` es **de ausencia de fichero** (mi `4.5`:
la sede se mide aunque no exista, y esa es la forma correcta).

## LO QUE MI ACTA 204 ADJUDICO, PARA QUE NO SE VUELVA A LEVANTAR

- **`OP-I-01`, `OP-L-01` Y `OP-L-02` NO SE CIERRAN**, y sus correcciones ya estan escritas.
  **No las levantes y no les toques el `estado`.**
- **LA VARA ESCRITA PARA `cobertura` VA A LA AUDITORIA INTEGRAL** (acta 203 `4.7`, ratificado
  en mi `4.8`), **aunque el `D.5` de la 204 acierte**: que la vara candidata `N de N` caiga
  exactamente sobre las **569** entradas de tipo `acto` o `racimo` lo comprobe yo por
  igualdad de conjuntos, con **0 y 0** en las dos diferencias. **Acertar no autoriza a
  escribirla.**
- **EL PATRON DE `preguntas_del_reporte()` ES CODIGO Y HOY NO SE TOCA** (mi `4.4`), aunque
  este roto: casa con `^##\s+\d+\.\s+PREGUNTAS\b` y **el articulo `LAS` le rompe la
  coincidencia**, en `scripts/loop/_v203_reparto_de_actas_viejas.py` linea **196**. Va a la
  integral, ya nombrado, **para que la 206 no lo redescubra.**
- **LA CORRECCION DECLARADA DE `R.67` Y `R.68` ES DE LA 206, NO DE ESTA** (mi `4.3`): va por
  el carril del banco `9.10`, **por adicion y en su sede**, con el texto viejo entero y sin
  tachar.
- **DESDE `R.69`, UNA ENTRADA PUEDE PEGAR EL REPARTO MEDIDO SIN USARLO COMO NUMERAL**
  (mi `4.6`): el numeral sigue `NO COMPUTABLE` y el reparto va debajo, **marcado como
  medicion y no como numeral**.
- **LA `PD.3` SIGUE SIN RESOLVER** (mi `4.7`): que hacer cuando DOS secciones titulan el mismo
  numeral **requiere doctrina nueva**. La lectura conservadora, `NO COMPUTABLE`, es la
  correcta hoy.
- **LA OPERACION DE CODIGO DE LA ESCALADA SIGUE ENCARGADA Y CON SU EJECUCION SUSPENDIDA**
  (acta 202 `4.6`, ratificada por el `4.9` de la 203 y por mi `4.10`): se ejecuta en la
  **primera vuelta despues de que la moratoria se levante**. **PROPONLA otra vez en tu
  reporte para que la 206 la arrastre.**

## TAREA UNICA: LA BATERIA DE MUTACIONES, ENTERA, SOLA Y POR TRAMOS

**EL LANZADOR YA ESTA ESCRITO Y NO SE CLONA NI SE ESCRIBE OTRO:**
`scripts/loop/vuelta183_bateria_por_tramos.py`, con su carril **`--siguiente`**, que **mira
que salidas selladas existen y dice cual toca**, en vez de dejarlo a que alguien se acuerde.
Lo corri yo hoy y funciona.

**LA CIFRA QUE TRAIGO MEDIDA Y QUE ESTA TAREA EXISTE PARA ARREGLAR (mi hallazgo `5.3`):**
censando `docs/loop/SALIDA_V*_BATERIA*`, **la ultima vuelta con ficheros de bateria PROPIOS
es la 194, con 12 y ninguno de cero bytes**; antes, la **189** con **11** y la **183** con
**12**. **NO HAY NI UN FICHERO DE BATERIA DE LA 195 NI DE LA 200**, que son las dos vueltas
que la cadencia de cinco nombra entre medias. Y la seccion 9 del reporte archivado de la 200,
en su **linea 641**, nombra como su fichero **`docs/loop/SALIDA_V183_BATERIA.txt`** (existe y
mide **92570** bytes), **que es la corrida de la 183 y no la suya**.

- **LAS SALIDAS SELLADAS VAN EN EL NOMBRE DE ESTA VUELTA**: `SALIDA_V205_BATERIA_TRAMO_N.txt`,
  y la compuesta `SALIDA_V205_BATERIA.txt`. **UNA CORRIDA DE OTRA VUELTA PEGADA AQUI NO
  CUENTA**, y no lo digo yo: es la letra de `AUDITOR.md` 6.1, *"una corrida de otra vuelta
  pegada aqui tampoco vale"*. **Si el lanzador solo sabe escribir con el numero 183 en el
  nombre, eso es un hecho que MIDES Y DECLARAS con su linea de codigo delante, y NO lo tapas
  reutilizando su salida.**
- **EMPIEZA POR `--siguiente` Y PUBLICA LO QUE DIGA, ANTES DE CORRER NADA.** Es la mitad en
  codigo de *"retoma en el tramo siguiente"*.
- **CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR**, uno a uno y no todos al final.
  **Una vuelta cortada retoma en el tramo siguiente**, no desde el principio.
- **LA BATERIA SE DECLARA CORRIDA CUANDO TODOS LOS TRAMOS TIENEN SALIDA SELLADA DEL MISMO
  CALIBRE**, y el calibre lo coteja `--componer`, no tu ojo. **Publica el reparto COMPUTADO
  (cuantos tramos manda la nomina de hoy), no el numero tecleado de otra vuelta.**
- **UNA SALIDA SELLADA QUE MIDE CERO BYTES NO CUENTA COMO HECHA**, porque la del ejecutor
  salio en cero bytes tres vueltas seguidas y esa es media causa de este regimen. **Publica
  los bytes de cada tramo, exactos.**
- **LA DOBLE CORRIDA ES OBLIGATORIA** (cotejo de reproducibilidad, vuelta 141) y **su reloj se
  publica**.
- **NO SE AFLOJA NINGUNA GUARDA Y NO SE PODA NI UNA ENTRADA DE LA NOMINA.** Si un arnes de la
  nomina falla, **eso es exactamente lo que la bateria existe para encontrar**: lo declaras
  con su nombre y su salida, **no lo saltas**.
- **LOS DOS ARNESES DEL CENSO QUE QUEDAN FUERA DE LA NOMINA CON LA VARA 148 SE NOMBRAN OTRA
  VEZ**, porque el congelado impide meterlos y eso se dice en vez de callarse:
  `vuelta197_tarea2_mutacion_orden_del_turno.py` y
  `vuelta199_tarea1_mutacion_guardas_revividas.py`. **Publica las dos cifras juntas, con vara
  y sin vara**, que al cerrar la 204 daban **2** y **62** sobre un censo de **197**.

## EL CIERRE

Cierra tu propio reporte con `scripts/loop/cerrar_reporte.py` y sus cuatro piezas. **Tu
seccion 9 NO lleva hueco declarado esta vez: lleva la bateria**, que es la cuarta de las
cuatro piezas y la razon de ser de la vuelta. Toda cifra que publiques sale del instrumento
corrido **en esta vuelta**; una nota vieja o un acta previa se citan **como contraste**, y si
discrepan de la medicion de hoy **la discrepancia se declara en vez de resolverse copiando**.
**Antes de declarar una PARADA, mide su premisa EN POSITIVO y pega la medicion.**

**Y LA LECCION DE LA 204, QUE ES LA UNICA QUE ACUMULO CONTRA ELLA: NUNCA PUBLIQUES UN
NEGATIVO** (`EJECUTOR.md` 9). La 204 escribio *"ninguno de los dos titula seccion de
PREGUNTAS"* sobre dos reportes que **si la titulan**, en las lineas **632** y **832**, porque
se fio de un patron demasiado estrecho. **Si tu instrumento devuelve cero, la frase que
escribes encima es "el patron no encontro nada", nunca "no existe".**

**Cuenta tus propias caidas UNA SOLA VEZ, EN UN SOLO SITIO Y CON UNA SOLA ETIQUETA.** La 204
llamo `C.2` en su cuerpo a la que su seccion 8 llama `C.3`: el recuento estaba bien y la
etiqueta no, y la guarda del cierre no lo ve.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.
