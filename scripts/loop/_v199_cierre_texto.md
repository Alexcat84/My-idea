## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA FILA DE ABAJO CITA EL FICHERO DEL QUE SALE Y SE RECONSTRUYO CONTANDO ESE
FICHERO** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO, 26 ago 2026).

| que se cuenta | cuantos | de que fichero se cuenta |
|---|---:|---|
| casos del arnes de la TAREA 1 | **26 verdes, 0 rojos** | `SALIDA_V199_T1_GUARDAS_REVIVIDAS.txt` |
| casos de la mutacion del caso rojo de la TAREA 2 | **9 verdes, 0 rojos** | `SALIDA_V199_T2_MUTACION_SEDE.txt` |
| fallos del arnes reparado de la TAREA 2 | **0** | `SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` |
| casos del arnes del orden del turno, tras el cambio | **52 verdes, 0 rojos** | `SALIDA_V197_T2_MUTACION_ORDEN_DEL_TURNO.txt` |
| casos del computo de los ejemplares del banco | **5 verdes, 0 rojos** | `SALIDA_V199_T3_EJEMPLARES_DEL_BANCO.txt` |
| puestos que salen del universo de las ciegas | **109** | `_v199_ejemplares_del_banco_exclusion.txt` |
| pares elegidos por el aislador sin la lista y con ella | **61** y **51** | `SALIDA_V199_T3_CARRIL_CIEGA.txt` |
| pares reales de `OP-L-03`, con lectura y sin lectura | **18** y **0** | `SALIDA_V199_T4_LECTURA_DEL_PLAN.txt` |
| filas de `docs/plan/INVENTARIO.jsonl` contadas hoy | **672** | `SALIDA_V199_T4_LECTURA_DEL_PLAN.txt` |
| llamadas a `AP.olvidar_todo()` en el arnes de la TAREA 2 | **6** | `SALIDA_V199_APERTURA.txt`, bloque `H.1` |
| racha de cierres, contada del instrumento | **3**, vueltas 195, 196 y 197 | `SALIDA_V199_APERTURA.txt`, bloque `E` |
| entradas de la nomina de la bateria | **135**, y CALZA con el congelado | `SALIDA_V199_APERTURA.txt`, bloque `F` |
| arneses del censo fuera de la nomina, con vara 148 y sin vara | **1** y **61** | `SALIDA_V199_APERTURA.txt`, bloque `F` |

**LA CIFRA DE FUERA DE LA NOMINA VIAJA CON SU VARA Y SE PUBLICAN LAS DOS**
(adjudicacion `4.7` del acta 197). Y **el 1 con vara es NUEVO**: la 197 media 0.
**El que sobra es `vuelta197_tarea2_mutacion_orden_del_turno.py`**, escrito por la
197 y **nunca metido en la nomina porque `AUDITOR.md` 6.3 la congelo en 135**.
**Queda fuera por regla escrita, no por olvido**, y con el mismo motivo quedan
fuera los tres ficheros nuevos de esta vuelta.

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO EN ESTA PROSA.**
`docs/loop/SALIDA_V199_APERTURA.txt`, bloque `C`, publica las dos cifras del estado
del arbol con la redaccion exacta que la guarda coteja, y aqui se repiten LEIDAS de
ella:

`git status --porcelain` 1 linea al entrar, que era el propio bloque de apertura
todavia sin commitear.

`git diff --numstat -- dataset/` 0 filas al entrar.

**La apertura sellada no se toco al cierre ni una vez.**

**LO QUE SE TOCO:**

- `scripts/loop/apertura_del_auditor.py`, **que no se clona**: las dos guardas
  reencendidas y `_apuntar_sello()` extraida de `sellar()`.
- `scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py`: la redireccion de
  la sede que cubre sus seis llamadas.
- `scripts/loop/vuelta197_tarea2_mutacion_orden_del_turno.py`: sandbox completo y
  **tres casos anadidos**, de 49 a 52.
- `scripts/loop/`: el bloque de apertura y el esqueleto de esta vuelta, el arnes de
  la TAREA 1, la mutacion de la TAREA 2, el computo del banco, la lectura del plan,
  los dos parches de un solo uso y los cuatro cuerpos de tarea.
- `docs/loop/`: las salidas selladas de esta vuelta y el reporte.

**LO QUE NO SE TOCO, Y SE MIDE EN VEZ DE PROMETERSE:**

- **`dataset/` no se toco a mano.** El `numstat` contra `HEAD` sale con **0 filas**
  al entrar y **0 al salir**, y las dos cifras se publican:
  `SALIDA_V199_CICLO_NUMSTAT_APERTURA.txt` y `SALIDA_V199_CICLO_NUMSTAT_CIERRE.txt`
  traen solo el aviso de fin de linea de git, sin una sola fila.
- **Ningun veredicto se movio.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre en
  **4054129 bytes en disco y 4054129 normalizado a LF**, con `sha256 disco 0a77b5a35a962621 y sha256 LF 0a77b5a35a962621` (bloque `D` de la apertura), y **cierra en los mismos valores**.
- **Ningun `estado` del expediente se movio**, que es lo que la TAREA 4 dice con
  todas sus letras: `OP-L-01`, `OP-L-02`, `OP-L-03` y `OP-I-01` siguen en `LISTA`.
- **La nomina no se podo ni crecio:** 135 al entrar y 135 al salir.
- **La sede del turno del auditor no se movio:** `docs/loop/_TURNO_DEL_AUDITOR.json` mide 789 bytes en disco y 789 normalizado a LF, con `sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280`, al entrar y al salir, medido tres veces por tres instrumentos distintos.
- **La bateria no corrio, y no tocaba**: su vuelta es la 200. Seccion 9.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`P.2` EL COMPUTO DE LA TAREA 3 CONTRA LA MORATORIA.** `AUDITOR.md` 6.3 prohibe
fabricar lectores nuevos y **la TAREA 3 no esta entre sus dos excepciones**. Lo que
la salva, y es mi lectura y puedo estar equivocado, es que el propio encargo manda
que la lista se COMPUTE y no se teclee, y computar necesita codigo. Se hizo con el
minimo posible: prefijo `_`, fuera del censo, fuera de la nomina, no vigila a nadie.
**Si el fundador lo lee como maquinaria, se retira.** Lo mismo vale para
`_v199_t4_lectura_del_plan.py` y para `_v199_t2_mutacion_sede.py`.

**`P.5` EL BLOQUE DE APERTURA Y EL ESQUELETO SE CLONARON, Y ESO TAMBIEN ES
CODIGO NUEVO.** Los lei como instancias por vuelta de un procedimiento que otras
reglas obligan a correr (la apertura antes de la primera operacion, el esqueleto al
abrir), y no como maquinaria nueva. **Va marcado porque la frontera es fina.**

**`P.6` LA MITAD `1.a` SE PUSO EN DOS SITIOS Y SOLO UNO SE VE SOLO.** El encargo
decia *"REABRIR EL TURNO AL SELLAR, o no dejarlo cerrado para siempre"*, con una
`o`. **Puse las dos**, y la mutacion demuestra que **la del sello no se ve mientras
la de la carga este puesta**. Elegi ponerla igual porque el encargo la nombra
primero y porque protege el caso en que nadie escriba antes del sello. **Si el
auditor lee que sobra, sobra, y se quita sin perder ninguna cifra.**

**`P.7` LA VARA DE `sello_mas_reciente_en_disco()` ES LA VUELTA MAS ALTA.** Es la
unica que se puede sostener sin adivinar, pero **es una eleccion mia**: un sello de
una vuelta baja escrito despues no se veria. Los sellos que hay en disco hoy van del
190 al 198 sin hueco salvo el 194, medido en esta vuelta.

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` EL ARNES DEL AUDITOR DE LA 198 QUEDA CITADO Y NO CORRIDO.** Sus diez casos
estan escritos para salir verdes **sobre el agujero**, asi que ahora saldrian rojos,
y correrlo **pisaria `docs/loop/SALIDA_V198_GUARDA_MUERTA.txt`, que es su prueba
sellada**. Mi bloque `MUTACION TOTAL` reproduce sus cuatro medidas una a una. **No
esta en la nomina**, asi que la 200 no lo va a correr. **Si quiere que su arnes
quede invertido en vez de citado, lo decide el.**

**`P.3` LA LISTA DE EXCLUSION DEL BANCO ENVEJECE.** Son 109 al corte **2026-09-07**,
y el banco crece cada vuelta. El computo se puede volver a correr, pero **nadie ha
escrito que haya que correrlo**, y una lista vieja deja entrar al universo puestos
cuya clase ya esta publicada. **Si esto tiene que ser un paso fijo del sello de
apertura, es una linea de doctrina.**

**`P.4` LA EVIDENCIA DE `OP-I-01` PROMETE 323 ENTRADAS Y EL FICHERO TIENE 672.** No
es caida de nadie: la cifra de la ficha viaja con su corte, el `2026-08-11`, y el
fichero se movio despues. **Leo que necesita una CORRECCION DECLARADA por el carril
del banco `9.10`**, la misma via que `OP-L-01` uso en la vuelta 166 y `OP-L-03` en
la 72. **No la escribo yo**: tocar el expediente no esta en las cuatro sub-tareas de
este encargo, y una correccion de evidencia es adjudicacion.

**`P.8` `OP-L-02` SIGUE SIN DOCUMENTO Y ESO YA NO ES NUEVO.** Esta vuelta lo midio y
lo dice, que es lo que el encargo pedia. **Lo que nadie ha escrito es que se hace
con una ficha cuya evidencia entera es prosa**: ni se puede cerrar por lectura ni se
puede declarar incompleta sin recomputar. **Sigue en `LISTA` y sigue sin vara.**

## 7. PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Las cuatro sub-tareas se ejecutaron con reglas escritas, y lo que
no cabia en una regla vigente salio como pregunta en la seccion 6 en vez de
resolverse por mi cuenta. **La `P.2` es el caso mas cerca del borde**, y va marcada
como discutible y no como doctrina nueva porque **el propio encargo ordena la
tarea**: no invento una excepcion, leo una orden.

## 8. LO QUE LA 200 RECIBE

**LA 200 ES VUELTA DE BATERIA Y NO LLEVA NADA MAS**, por el encargo de esta vuelta:
*"LA VUELTA DE BATERIA SE CORRE EN LA 200, con la nomina CONGELADA en 135, para que
los remedios de las TAREAS 1 y 2 esten DENTRO cuando corra"*. **Los dos remedios
estan dentro:** `vuelta182_tarea2_mutacion_apertura_auditor.py` esta en la nomina
(linea 847 de `verificar_mutaciones_viejas.py`) y **ya no se lleva la sede por
delante**, y `apertura_del_auditor.py` es el modulo que media la nomina entera.

**LO QUE LA 200 SE VA A ENCONTRAR, Y SE DICE PARA QUE NO LO REDESCUBRA:**

- **la nomina mide 135 y CALZA con el congelado**, con `CASOS_DECLARADOS` en 2;
- **1 arnes del censo queda fuera de la nomina con la vara 148**, y es
  `vuelta197_tarea2_mutacion_orden_del_turno.py`. **La bateria no lo va a correr**,
  y eso es consecuencia del congelado y no un descuido de nadie;
- **los tres ficheros `_v199_*` de esta vuelta tampoco entran**, por el prefijo y
  por el congelado;
- **el siguiente libre de la serie es `R.60`**, con 0 colisiones, y **el acta 198
  todavia no esta registrada**: la registra quien la tome;
- **las cuatro fichas del plan siguen en `LISTA`**, con su saldo medido en la
  seccion 2 y las dos preguntas abiertas, `P.4` y `P.8`.

**Y SIGUEN FUERA, NOMBRADAS:** la guarda de codigo del hallazgo `5.3` del acta 194;
`acumulan()` que lea la tabla; el cotejo de clon declarado; las ocho actas sin
entrada propia en la serie (173 a 180); y **que hacer con las filas `B` del
archivo**.
