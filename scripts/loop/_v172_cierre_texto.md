## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**LOS DOS EXTREMOS SE LEEN DE LOS SELLOS Y NO SE TECLEAN.** Apertura `002e0517`,
de `docs/loop/SALIDA_V172_HEAD_APERTURA.txt`, sellado **antes de la primera
operacion**; cierre `24dda21e`, de `docs/loop/SALIDA_V172_HEAD_CIERRE.txt`,
sellado **tras la ultima**. **LOS COMMITS DE LA VUELTA, LEIDOS DE
`git log 002e0517..24dda21e`: OCHO.**

| # | commit | que cierra |
|---:|---|---|
| 1 | `ad3cea43` | la apertura, el bloque ENTERO |
| 2 | `99d54005` | TAREA 1.a, el reporte de la 171 cerrado |
| 3 | `20b11348` | TAREA 1.b, el acta 171 al `R.41` |
| 4 | `45fb75f5` | TAREA 1 cerrada (1.c, archivador y esqueleto) |
| 5 | `96940490` | TAREA 2 |
| 6 | `24bd395b` | TAREA 3 |
| 7 | `680f74ab` | TAREA 4.a y 4.b |
| 8 | `24dda21e` | TAREA 5 |

**Y HAY UN COMMIT ANTES DE LA APERTURA QUE TAMBIEN ES DE ESTA VUELTA Y SE DICE:**
`002e0517`, la suciedad de la apertura (el `SALIDA_V172_AUDITOR_BATERIA.txt` de
cero bytes que el auditor dejo suelto), commiteado por la regla 3 de
`EJECUTOR.md` **antes de tocar nada**. Es el HEAD de apertura, asi que **queda
fuera del rango por definicion**, no por olvido.

**EL GRAFO NO SE MOVIO, PROBADO Y NO CREIDO:**
`git diff 002e0517 24dda21e --numstat -- dataset/ web/ engine/` sale con **0
filas**. Las **74 rutas** que la vuelta toca son **40 de `docs/loop/`, 30 de
`scripts/loop/`, 2 de `docs/plan/`, 1 de `docs/loop/reportes/` y 1 de `docs/`**.
**Cero nodos tocados, cero aristas movidas, cero clases movidas**, y la cabecera
de arriba lo confirma por otro camino: **+0 / +0 / +0 / +0** en las cuatro cifras
de aristas.

**EL COMMIT QUE LLEVA ESTE REPORTE NO SE NOMBRA AQUI**, porque se crea despues de
escribirlo. Y **este cierre lo escribe la propia vuelta 172**, que es la primera
en tres que lo hace: la 170 y la 171 lo dejaron sin cerrar.

## 4. LA PARADA, Y ES UNA, PERO NO DETIENE NINGUNA TAREA

**LA BATERIA SALE ROJA POR MIS PROPIOS ARNESES, Y NO LO ARREGLO YO.**

El encargo, en su 4.b, dice con esas palabras: *"Con las tres entradas nuevas la
nomina tiene que dar 78 y su ultima vuelta representada tiene que ser la 171."*
**Eso es exactamente lo que hice, y lo mide la funcion pura del propio
instrumento: 78 entradas, ultima vuelta 171, nomina invisible al censo 0.**

**PERO `arneses_que_faltan()` SIGUE DEVOLVIENDO 3, Y LOS TRES SON MIOS**, nacidos
en esta misma vuelta:
`vuelta172_tarea1b_mutacion_registro.py`,
`vuelta172_tarea2a_mutacion_exclusion.py` y
`vuelta172_tarea3_mutacion_numeracion.py`. **Y hay un cuarto desde la TAREA 5**,
`vuelta172_tarea5_mutacion_cierre.py`. El veredicto de la bateria cuenta esa
lista como **ROJO**.

**EL CHOQUE, DICHO EN UNA LINEA:** la regla escrita en el propio
`verificar_mutaciones_viejas.py` dice que *"una mutacion entra en la vuelta
SIGUIENTE a la que nace, no mas tarde"*, o sea que los mios entran en la **173**;
**pero la comprobacion marca como FUERA todo arnes con vuelta mayor que la ultima
de la nomina, y eso incluye a los recien nacidos.** Las dos cosas no pueden ser
ciertas a la vez en la vuelta en que un arnes nace.

**LOS DOS PRECEDENTES, MEDIDOS Y NO RECORDADOS, Y NO DICEN LO MISMO:**

| vuelta | metio sus PROPIOS arneses en la nomina | resultado |
|---|---|---|
| 170 | **SI** (`vuelta170_tarea1a_mutacion_registro.py` y `vuelta170_tarea2a_mutacion_aislador.py` estan en `VIEJAS` y la ultima vuelta representada era la 170) | la bateria del auditor salio **VERDE**, con `faltan` en **0** |
| 171 | **NO** (escribio tres y no metio ninguno) | el acta 171 dice que la bateria **saldria ROJA**, y su seccion 4.3 lo mide |

**POR QUE NO LO ARREGLO METIENDO LOS MIOS:** porque eso daria **81 entradas y
ultima vuelta 172**, y **contradice al digito la cifra que el encargo publica**.
`EJECUTOR.md` 5 dice que si algo contradice una regla vigente **se para y se
trae, y no lo arreglo yo**. **Asi que la bateria se corre, se publica su rojo
entero con su texto en la seccion 9, y la decision sube.**

**LO QUE NO ES:** no es una parada de trabajo. **Las cinco tareas del encargo
estan cerradas**, la bateria corrio entera y sola, y su salida esta pegada
completa. Lo unico que queda en el aire es **si la nomina debe llevar tambien los
arneses de la vuelta que corre**, que es una linea de doctrina y no un arreglo.

**Y LA PREGUNTA CONCRETA, PARA QUE SE PUEDA CONTESTAR EN UNA LINEA:** ¿la nomina
de la bateria se cierra con los arneses de la vuelta ANTERIOR (y entonces
`arneses_que_faltan()` tiene que dejar de contar a los de la vuelta en curso), o
se cierra con los de la vuelta EN CURSO (y entonces la 4.b de este encargo pedia
78 cuando tenia que pedir 82)? Va como `P.1`.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Los marco ahora, con la relectura ciega del auditor por delante y sin saber
como va a adjudicarlos.** Esta vez si son ciegos, y lo digo porque en el reporte
de la 171 que cerre en la TAREA 1.a **no lo eran** y ahi va escrito.

- **`D.1` LAS GLOSAS DEL `R.41` NO AFIRMAN EN PASADO, Y ESO CAMBIA LA FORMA DE
  UNA ENTRADA DE LA SERIE.** El campo se llama **VIA PREVISTA**, las siete glosas
  de tarea dicen *"VA A EJECUTARSE EN LA TAREA n ... Y AL ESCRIBIR ESTA LINEA
  TODAVIA NO HA CORRIDO"*, y la confirmacion medida se anexa al cierre.
  **Discutible: puede que la forma correcta fuera escribir la entrada AL FINAL de
  la vuelta, cuando ya se sabe, en vez de cambiar el tiempo verbal; y puede que
  cambiar la forma de una entrada de la serie sea doctrina y no ejecucion.**
- **`D.2` TRAIGO UNA DISCREPANCIA CON EL ACTA EN VEZ DE RESOLVERLA.** El acta 171
  dice que el paso 0 sale ROJO **por la clausula (d)**; con
  `vuelta_anterior=171`, que es lo que el esqueleto de esta vuelta llama, sale
  **por la (b)**. Reproduje la del acta con **su** parametro,
  `exigir_archivado(170)`, y ahi si sale la (d). **Publico las dos. Discutible:
  puede que lo esperado fuera decir simplemente que reproduce, y que separar dos
  lecturas de dos preguntas distintas sea hilar de mas.**
- **`D.3` ESCRIBI UN INSTRUMENTO QUE EL ENCARGO NO PIDE.**
  `scripts/loop/anexar_tarea_al_reporte.py`, de nombre estable. El motivo es que
  anexar la fila de cada tarea al cerrarse **era un paso a mano**, la misma
  especie que la TAREA 5 viene a matar. **Discutible: el encargo trae tope de
  cinco tareas y esto es codigo de mas; puede que tocara traerlo como propuesta
  en vez de escribirlo.**
- **`D.4` SAQUE EL CRITERIO DE EXCLUSION DEL CONTADOR A UNA FUNCION PURA.** Sin
  eso no habia nada que un arnes pudiera llamar y la 2.a no se podia probar por
  mutacion. **Discutible: es un cambio de forma en un instrumento viejo que el
  encargo no manda tocar, y un refactor dentro de una tarea de contenido es
  precisamente lo que suele colar cambios sin guarda.**
- **`D.5` ESTRENE LA ETIQUETA DE VIA `NO SE CORRIO`.** El vocabulario de la casa
  trae `EJECUTADA`, `SIN TOCAR NADA` y `AL FUNDADOR`. **Discutible: estrenar una
  palabra es exactamente lo que hizo el `D.5` de la vuelta 170 y se le pidio
  cuenta; puede que lo correcto fuera dejar la via vieja tachada y sin
  sustituto.**
- **`D.6` LE PUSE PARAMETRO AL CORTE DE LA 2.c.** Estaba clavado en 138 y al
  correr el instrumento DESPUES de la TAREA 3 salia ROJO por diseno. **Discutible:
  un rojo que molesta no siempre es un rojo mal puesto, y puede que lo correcto
  fuera dejarlo clavado y no volver a correrlo.**
- **`D.7` TOQUE UNA SEGUNDA FILA DE `docs/plan/00_INDICE.md` QUE EL ENCARGO NO
  NOMBRA.** La de *"lecturas dirigidas hechas"* llevaba **82 con corte 5 sep
  2026** y mi TAREA 3, del mismo dia, la movio a **98**; dejarla habria puesto dos
  cifras distintas con la misma fecha para la misma vara, **y la habria creado
  yo**. **Discutible: el encargo nombra una fila y toque dos.**
- **`D.8` NO METI MIS PROPIOS ARNESES EN LA NOMINA Y DEJE LA BATERIA EN ROJO.**
  Esta explicado entero en la seccion 4. **Discutible: puede que la lectura buena
  del encargo fuera "78 al meter los tres de la 171, y despues los tuyos
  tambien", y que yo haya elegido la letra por encima del sentido.**

## 6. LAS PREGUNTAS

- **`P.1`** ¿La nomina de la bateria se cierra con los arneses de la vuelta
  ANTERIOR o con los de la vuelta EN CURSO? Es la de la seccion 4 y es la unica
  que deja algo en rojo.
- **`P.2`** ¿Una entrada de la serie `R.n` se escribe al ABRIR la vuelta, con
  glosas en futuro y confirmacion anexada al cierre (lo que hice), o al CERRARLA,
  con glosas en pasado y ya medidas? Las dos evitan la caida del `R.40`; solo una
  puede ser la forma de la casa.
- **`P.3`** El `PD.1` de la vuelta 171 sigue abierto y hoy es lo unico que separa
  las dos varas del contador: **¿un registro fiel que CITA un encargo cuenta como
  encargo?** Medido hoy, los dos numeros que lo sostenian (`LD-139` y `LD-154`)
  **ya no cuentan**, porque la TAREA 3 les dio seccion propia; **pero la pregunta
  sigue viva** para el proximo encargo que una entrada `R.n` glose.

## 7. PENDIENTES DE DOCTRINA

- **`PD.1` NO HAY REGLA SOBRE CUANDO ENTRA EN LA BATERIA EL ARNES QUE NACE HOY.**
  El fichero dice *"en la vuelta SIGUIENTE a la que nace"* y su comprobacion los
  cuenta como FUERA desde el minuto uno. **La vuelta 170 metio los suyos y salio
  verde; la 171 no metio ninguno y quedo roja.** La regla que falta es de una
  linea y cierra el rojo de esta vuelta.
- **`PD.2` NO HAY VOCABULARIO ESCRITO DE VIAS PARA LA SERIE `R.n`.** La casa usa
  `EJECUTADA`, `SIN TOCAR NADA` y `AL FUNDADOR`, y hoy hicieron falta dos que no
  estaban: **`NO SE CORRIO`** (para la correccion del `R.40`) y **`VIA
  PREVISTA`** (para una entrada escrita antes de que la tarea corra). Las dos
  describen hechos y ninguna regla escrita las prohibe, **pero estrenar
  vocabulario dos veces en una vuelta es justo lo que la 170 hizo una vez y se le
  cazo**.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

- **`CAIDA 1`. LA PRIMERA CORRIDA DEL BLOQUE DE APERTURA MURIO CON
  `SyntaxError` Y NO ESCRIBIO NI UN FICHERO.** Al generar
  `scripts/loop/vuelta172_apertura.py` se me colo **un salto de linea de verdad
  donde tenia que ir su escape**, y el fichero no compilaba. **Ninguna cifra
  salio de ahi: no escribio ninguna salida.** Lo arregle usando `chr(10)` en vez
  del escape y volvi a correr, **y la segunda corrida sigue estando antes de la
  primera operacion sobre el registro**. Va declarada tambien en el mensaje del
  commit `ad3cea43`, antes de que nadie la cazara.
- **`CAIDA 2`. UNA GUARDA MIA MIDIO EL FICHERO ENTERO EN VEZ DE MI PROPIO
  CAMBIO.** La comprobacion anti guiones de la TAREA 2.b miraba
  `docs/PENDIENTES.md` **completo** y salio ROJA **despues de escribir**, porque
  esa pagina **ya traia 54 guiones largos de antiguo**, ninguno mio. Revertí con
  `git checkout`, apunte la guarda **al DELTA** (que yo no anada ninguno) mas una
  segunda que mira **solo mi bloque**, y volvi a correr. **La guarda no se
  aflojo: se reapunto**, que es lo mismo que la vuelta 170 hizo con su `CAIDA 2`.
- **`CAIDA 3`. PISE UNA SALIDA QUE ERA EVIDENCIA.** Al ponerle el parametro
  `--corte` al instrumento de la 2.c **lo volvi a correr con `--corte 138`
  DESPUES de la TAREA 3 y sobreescribi
  `docs/loop/SALIDA_V172_T2C_ATRIBUCION.txt`**, que era la medicion de la guarda
  **previa** a la TAREA 3. **No se perdio nada porque estaba commiteada** y la
  restaure con `git checkout 96940490 --`. **Lo que ensena es que una salida
  commiteada es la unica que aguanta**, y que un instrumento que se puede
  re-correr sobre su propio fichero de salida deberia negarse a pisarlo.
- **`CAIDA 4`. UN MARCADOR DE UNA LETRA ROMPIO UN FICHERO GENERADO.** El primer
  andamio que escribia el texto del `R.41` usaba **la letra `Q` como marcador de
  comilla**, y `Q` aparece en `AQUI` y en `QUE`, asi que el clon salio sin
  compilar. **Lo cazo `py_compile` y nada se commiteo roto**; el marcador paso a
  `~C~` y el andamio quedo como
  `scripts/loop/_v172_construir_registrador.py`, que **reproduce el fichero byte
  a byte**. Va declarada aunque no llegara a publicarse ninguna cifra.
