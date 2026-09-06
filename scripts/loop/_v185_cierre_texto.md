## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**LAS DOS TAREAS DEL ENCARGO CERRARON.** El tope era dos, por el regimen
temporal de `AUDITOR.md` 6.2, y son dos. **La TAREA 1 cierra con una PARADA
levantada en su `1.c` y la TAREA 2 con otra en su `2.a`, y las dos van
escritas con su medicion, no con una impresion.**

- rama, leida con `git rev-parse --abbrev-ref HEAD`: `pasada-unica`
- HEAD de apertura, sellado **antes de la primera operacion** en
  `docs/loop/SALIDA_V185_HEAD_APERTURA.txt`: **`5834632b`**
- HEAD del ultimo commit antes de cerrar, leido con `git rev-parse HEAD`
  **despues de la ultima operacion**: **`403e50c3`**
- commit del acta 185, localizado con `git log --grep` y no tecleado:
  **`5834632b`**
- commit de nacimiento del bloque de apertura, `git log --diff-filter=A`:
  **`2c72d81d`**

**GATE 0 VERDE ENTERO EN SU CICLO, EN LA APERTURA Y OTRA VEZ AL CIERRE.** Sus
salidas son `docs/loop/SALIDA_V185_GATE0_CMD1_APERTURA.txt` (**4859 bytes en disco y 4790 bytes normalizados a LF**)
y `docs/loop/SALIDA_V185_GATE0_CMD1_CIERRE.txt` (**4859 bytes en disco y 4790 bytes normalizados a LF**),
con motor **25/25** en la apertura y **25/25** al cierre, `tsc` **EXIT=0** y **EXIT=0**,
y web **1040 passed (1040)** y **1040 passed (1040)**. La apertura entera vive en
`docs/loop/SALIDA_V185_APERTURA.txt` (**26084 bytes en disco y 26084 bytes normalizados a LF**)
y **la sello el PRIMER commit de la vuelta**.

**EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA, ANTES DE LA PRIMERA
OPERACION**, que es donde `EJECUTOR.md` 1 lo manda desde la 178: **4 filas**
en la apertura y **4 filas** al cierre.

**EL ARCHIVO DE VEREDICTOS NO SE MOVIO, Y ESA ES LA PRUEBA INDEPENDIENTE DE
QUE ESTA VUELTA NO TOCO NINGUN VEREDICTO.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:
**3388 filas**, **A 551, B 72, C 5, D 2760**, **0 huecos y 0 duplicados**,
**4051967 bytes en disco y 4051967 bytes normalizados a LF**, y `sha256` **`ea6e850d331d14f0`**
**identico por las dos convenciones, disco `ea6e850d331d14f0` y LF `ea6e850d331d14f0`**.
Es el mismo que la apertura de esta vuelta midio y el mismo que las actas 179
a 185 publican.

## 4. LA GUARDA DEL COMMIT DE `dataset/`, CORRIDA EL DIA QUE SERVIA

`git status --porcelain` da **15 lineas** al cerrar la vuelta, y
`git diff --numstat -- dataset/` da **0 filas**. **Al ENTRAR, medido en el
bloque de apertura antes de la primera operacion, dio 0 filas tambien.**
**Ninguna perdida de catalogo que declarar**, y `dataset/` no se commitea en
esta vuelta.

**Y ESTA VUELTA NO TIENE LA `M dataset/metadata/master_graph.json` QUE LAS
ANTERIORES TRAIAN.** El arbol abrio limpio, con `git status --porcelain` en
cero lineas, cosa que el docstring del bloque de apertura predijo **antes** de
medirla y que sus bloques C, D, E y F midieron sin saber lo que habia escrito.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**LOS SIETE VAN EN SUS DOS SEDES Y AQUI SE LISTAN JUNTOS, QUE ES LO QUE LA
`5.7` DEL ACTA 185 PIDE.** Los cinco primeros nacen en el anexo de la TAREA 1
y los dos ultimos en el de la TAREA 2; **ninguno se tapa y ninguno cambia de
redaccion al repetirse aqui su titulo**.

- **`D.1`. ANADI UN CAMBIO MAS DE LOS TRES QUE LA `1.d` NOMBRA:** la
  procedencia de la novena columna en la prosa del tallador. No mueve ninguna
  celda, pero el encargo no lo pidio.
- **`D.2`. MI ARNES DE LA `1.b` SALIO EN ROJO EN SU PRIMERA CORRIDA Y LO
  REPARE YO EN VEZ DE TRAERLO.** Lei que la regla de detenerse protege a los
  arneses ya sellados y no al que estoy escribiendo. **La corrida en rojo va
  entera en el reporte.**
- **`D.3`. PUBLIQUE LA COLUMNA `quien lo sello` CON UNA NEGRITA COMPUTADA**,
  deducida de las celdas que tenia que reproducir. Nadie escribio esa regla de
  formato.
- **`D.4`. NO METI LOS DOS ARNESES NUEVOS EN LA NOMINA DE LA BATERIA.** Esta
  vuelta no es de bateria y su encargo no nombra la nomina. **La 189 empezara
  en rojo por esa via si nadie los mete antes.**
- **`D.5`. GUARDE EL REPORTE DE LA 184 QUE `cerrar_reporte.py` SI LLEGO A
  ESCRIBIR Y DESPUES RESTAURE EL ARBOL** con `git checkout`. Destruirlo habria
  perdido la evidencia; dejarlo habria hecho que el esqueleto pisara un texto
  sin otra sede.
- **`D.6`. NO PEGUE ENTERA LA SALIDA ROJA DEL CIERRE DE LA 184**, porque lleva
  dentro la marca de maquina que la pieza (2) busca en todo el texto. **La cito
  por su ruta con sus bytes y pego las lineas que deciden.** Es una desviacion
  de la letra del encargo.
- **`D.7`. CERRE EL REPORTE DE LA 185 SABIENDO QUE EL DE LA 184 NO CERRO.** Se
  puede leer que el orden del encargo hacia del cierre de la 184 una condicion
  previa. **La lectura contraria es defendible y por eso va marcado.**

## 6. LAS PREGUNTAS

**`P.1`. LA PIEZA (4) Y LA PIEZA (2) DE `piezas_que_faltan()`, ¿SE REPARAN
JUNTAS O POR SEPARADO?** La (4) es la copia gemela de la regla que la `1.c`
acaba de reparar. La (2) es otra especie: busca su marca **en todo el texto**,
y un reporte que **cita** una salida roja dentro de un bloque cercado la lleva
dentro sin estar sin tallar. **No se cual es prioridad y no me lo encargaron.**

**`P.2`. ¿QUE SE HACE CON LAS CIFRAS SIN PAREJA DEL REPORTE DE LA 184?** La
guarda `cifras_sin_pareja()` las caza y el encargo prohibe tocar ese texto. **O
se exime el texto ya escrito, o se reescribe, o la guarda aprende a mirar solo
lo nuevo.** No elijo yo.

**`P.3`. ¿LOS DOS ARNESES NACIDOS HOY ENTRAN EN LA NOMINA DE LA BATERIA, Y
QUIEN LOS METE?** La `5.6` del acta 185 ampara meterlos en su propia vuelta,
pero esta no es vuelta de bateria. **Medido hoy: `arneses_que_faltan()` da 2.**

## 7. PENDIENTES DE DOCTRINA

**`PD.1` SIGUE ABIERTA Y NO LA TOCO:** las cinco `D` con el diferenciador ya
presente el dia del veredicto, **1778, 2530, 2540, 3141 y 3232**, hoy con sus
cinco puestos escritos en el `R.47` y leidos del acta, no copiados del encargo.

**`PD.5` NUEVA. UNA MARCA DE MAQUINA CITADA DENTRO DE UN BLOQUE CERCADO SIGUE
SIENDO UNA MARCA DE MAQUINA.** La pieza (2) busca su marca en todo el texto y
`cifras_sin_pareja()` ya excluye los bloques cercados: **dos guardas del mismo
fichero tratan la cita al reves la una de la otra.** Hoy eso impide que un
reporte pueda citar entero el rojo de otro.

**`PD.6` NUEVA. UNA REGLA ESCRITA DOS VECES EN EL MISMO FICHERO.**
`rama_de_la_seccion9()` y la pieza (4) de `piezas_que_faltan()` llevan la misma
comparacion de vuelta ajena. **Reparar una y no la otra deja el instrumento
diciendo dos cosas distintas del mismo caso.** Es la PARADA de la `1.c` dicha
como doctrina.

**`PD.2`, `PD.3` Y `PD.4` QUEDARON CERRADAS POR EL ACTA 185** y no se reabren
aqui: estan registradas en el `R.47` con su estado leido del titulo del acta.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**`C.1`. ESCRIBI UN ARNES CUYA SALIDA SELLADA LLEVABA DENTRO EL MISMO DATO QUE
CAMBIA SOLO QUE LA REPARACION VENIA A QUITAR.** La primera version de
`scripts/loop/vuelta185_tarea1b_mutacion_sin_temporal.py` pegaba sus lineas de
entrada **crudas**, con el sufijo aleatorio del `mkdtemp` dentro. **Habria
hecho caer la bateria de la 189 por la misma averia que estaba reparando.** Lo
cace **releyendo mi propio fichero**, no un instrumento, y anadi `mostrar()`.
La prueba de que ya no pasa es que sus dos corridas seguidas dan la misma
salida byte a byte.

**`C.2`. MI PRIMER ARNES DE LA `1.b` FABRICO UN TEMPORAL QUE NO EXISTE Y SUS
DOS CASOS DE RUTA RELATIVA SALIERON EN ROJO.** La funcion bajo prueba estaba
bien; lo que estaba mal era **mi entrada tecleada**, que no es la cadena que
`os.path.relpath` produce. **Es exactamente la especie que esta casa castiga:
teclear en vez de medir.** La corrida en rojo va entera en el reporte y el
motivo queda escrito dentro del propio fichero, no en una nota aparte.

