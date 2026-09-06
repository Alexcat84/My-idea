# ENCARGO DE LA VUELTA 183 (ejecutor). FASE III. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

**LA 183 ES VUELTA DE BATERIA, Y ESO MANDA SOBRE TODO LO DEMAS.** `AUDITOR.md`
6.1: la bateria corre **cada cinco, en vuelta propia, y esa vuelta no lleva
trabajo de plan al lado**. La 181 era la suya y se corto antes de lanzarla, y la
decision del fundador del 5 sep (PREGUNTA 4 de
`docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md`) la manda **por
tramos resumibles**. Su lanzador esta escrito y sin correr desde la 182.

**EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y NO ES INERCIA: ESTA MEDIDO.** El
regimen `6.2` devuelve el tope a cinco cuando **dos vueltas seguidas cierren su
propio reporte** con `scripts/loop/cerrar_reporte.py`. Mi acta 182, punto 8, lo
midio: **la 181 NO cerro el suyo** (su copia archivada dice *"SIN ESCRIBIR
TODAVIA"* en su linea 41, y `cerrar_reporte.py` nunca corrio sobre el) y **la 182
SI**. La cuenta va por **UNA**, no por dos. **Si la 183 cierra el suyo, seran dos
seguidas y el tope vuelve a cinco en la 184.**

---

## TAREA 1 (BLOQUEANTE, Y VA ANTES DE LA BATERIA). LOS REGISTROS Y LA ESCALADA

**1.a. EL ACTA 182 ENTRA EN LA SERIE DE REGISTROS.** Cabecera en
`docs/loop/ACTA_AUDITOR.md:63250`. El numero lo da
`scripts/loop/serie_de_registros.py` y **no se teclea**. Van sus adjudicaciones
(`5.D.1` a `5.D.7`, y `7.1` a `7.5`), su caida propia del auditor (`C.1`, punto
2) y **las dos del ejecutor** (`E.1`, que acumula, y `E.2`, que no). Con su caso
por mutacion, como el `R.43`.

**1.b. LA DEUDA DE OCHO REGISTROS SE DOCUMENTA COMO SALTO, Y NO SE RELLENA.**
Adjudicacion `7.4` de mi acta 182: las actas **173 a 180** no tienen entrada
propia y **no se inventan ocho registros de memoria**. Escribe **una sola linea
de constancia** en la serie, en su sitio, que diga el salto y sus dos extremos
(`R.42` cubre el acta 172, `R.43` el acta 181), con la cifra contada por el
instrumento y no tecleada.

**1.c. LA ESCALADA, Y ES LA PIEZA QUE NO SE PUEDE DEJAR PARA DESPUES.** La racha
de reporte llego a **DOS** (`AUDITOR.md` 1.2), asi que la operacion de codigo va
en esta vuelta como tarea bloqueante. **LA CAIDA QUE LA TRAE:** el veredicto de
una linea de la 182 dice *"LAS SEIS CAIDAS QUE COMETI"* y su seccion 8 lista
**siete** (`C.1` a `C.7`), y hasta el cierre de esa misma seccion dice *"NINGUNA
DE LAS SIETE SE TAPA"*.

**LA OPERACION, con la figura del tallador del 26 ago
(`docs/loop/paradas/2026-08-26-racha-hash-apertura-DECISION.md`): lo que se
teclea se coteja contra lo que se puede contar.**

- `scripts/loop/cerrar_reporte.py` gana una funcion **pura y con arnes propio**
  que recibe el texto del veredicto de una linea y el cuerpo del reporte, y
  **coteja los numerales del veredicto contra lo que el cuerpo permite contar**:
  como minimo **las caidas propias** (cabeceras `C.n` de la seccion 8) y **las
  tareas cerradas** (filas de la tabla de tareas).
- **Si un numeral del veredicto no calza con su cuenta, el cierre CAE EN ROJO y
  no escribe nada.** No avisa ni recomienda: no cierra.
- **Los numerales se leen tambien escritos con letra** (*"seis"*, *"siete"*), que
  es como el veredicto los escribe, o la guarda no muerde en el unico caso que la
  trae.
- **CASO POSITIVO POR MUTACION SOBRE VARIABLE COMPUTADA**, no sobre constante
  literal (`EJECUTOR.md` 1): el veredicto real de la 182 contra su cuerpo real
  tiene que **CAER**, y el mismo veredicto con *"siete"* tiene que **PASAR**; y la
  mutacion se corre cambiando el valor esperado para comprobar que el caso cae de
  verdad.

**1.d. EL HUECO DE LA SECCION 9 TIENE QUE DECIR SI EL FICHERO NO EXISTE O SI MIDE
CERO.** Adjudicacion `7.1` de mi acta 182, por extension citada del punto 3 de
`docs/loop/paradas/2026-09-05-la-bateria-sin-techo-DECISION.md`, que **nombra los
dos casos y no los confunde**. Hoy `cerrar_reporte.py:696` hace
`tam = os.path.getsize(ruta_bat) if existe else -1` y la seccion publica
`max(tam, 0)`, asi que **un fichero ausente sale como "0 bytes medidos con
`os.path.getsize`"**, que no es lo que paso: el cero sale de un `max`. El propio
instrumento ya imprime `NO EXISTE` en su consola. **Que la declaracion escrita
diga cual de los dos es**, con su arnes, y **sin cambiar las tres piezas que el
hueco ya exige** (nombre, medicion y atribucion).

**1.e. LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA**, encargada por
`AUDITOR.md:57` porque las seis discrepancias salieron **fuera del marcado**. El
tramo son **los 30 puestos de la seccion 9 de mi acta 182**, leidos del acta y no
tecleados; el doble, sus **30 vecinos deterministas**, como hizo la TAREA 1.c de
la 182, con la maquina importada y no copiada. **Es relectura MECANICA con la
vara: no vuelve a decidir la clase de ningun par**, y lo que la vara no vea, la
salida **no lo afirma**.

---

## TAREA 2. LA BATERIA DE MUTACIONES, ENTERA Y POR TRAMOS

`scripts/loop/vuelta183_bateria_por_tramos.py`, que la 182 dejo escrito, medido y
sin correr. Su reparto corrido hoy por mi da **109 entradas de nomina, tramo de
13, NUEVE tramos, y la suma de los tramos es 109**.

**COMO CORRE, Y ES LA LETRA DEL FUNDADOR:**

- **Cada tramo se commitea CON SU SALIDA SELLADA al terminar**, antes de seguir
  con el siguiente. **Lo corrido queda corrido.**
- **Una vuelta cortada RETOMA EN EL TRAMO SIGUIENTE**, no desde el principio, y
  cual toca lo dice `--siguiente`, no la memoria de nadie. Corrido hoy por mi:
  **9 tramos, 0 con salida sellada, 9 faltan, el siguiente es el TRAMO 1.**
- **La bateria se declara corrida cuando los NUEVE tienen salida sellada DEL
  MISMO CALIBRE.** Ocho no valen. Nueve de distinta hondura, tampoco.
- **UNA SALIDA SELLADA QUE MIDE CERO BYTES NO CUENTA COMO HECHA.** La del
  ejecutor salio en cero bytes en la 171, la 172 y la 173, y esa es media causa de
  este regimen.
- **La doble corrida no se afloja** (cotejo de reproducibilidad, vuelta 141), ni
  ninguna otra guarda: **lo unico que cambio es la cadencia.**
- **El reloj de cada tramo se mide al cerrarlo y se publica medido.** La
  estimacion del `--plan` (entre 4,3 y 5,6 minutos por tramo, entre 36,0 y 46,9 la
  nomina entera) **es estimacion y se dice como tal**: la medicion de verdad la da
  el tramo.

**Si un arnes cae en rojo, el ejecutor se detiene ahi y lo trae**, con su salida
entera. **Un rojo de bateria no se arregla de paso.**

---

## LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE

- **No se relee ningun par de los 543** ni se toca la cola de
  `docs/plan/08_VERIFICACION.md`. El TRAMO 1 de esa cola es el par **2.464** y se
  relee cuando haya vuelta de trabajo, no en la de bateria.
- **No se cablea el instrumento de vigencia de las ocho `A` rancias por `P.5`.**
  Esta adjudicado (`7.4`) y anotado para la primera vuelta de trabajo, **no para
  esta**.
- **No se toca el marcador, ni un veredicto, ni `dataset/`.** El `sha256` del
  archivo tiene que seguir siendo `ea6e850d331d14f0` al cerrar, y si no lo es, eso
  es lo primero que se declara.
- **No se poda la nomina de la bateria.** La opcion `c` de la parada del 5 sep
  quedo **RECHAZADA** por el fundador.

## EL CIERRE

Cierra el reporte con `scripts/loop/cerrar_reporte.py`, que es la mitad de lo que
devuelve el tope a cinco, y **archivalo en `docs/loop/reportes/` en esta misma
vuelta**, byte a byte y comprobado. La seccion 9 lleva **la bateria entera**, no
un hueco: esta vez si es su vuelta.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
