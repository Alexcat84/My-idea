Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la campana My Idea. Rama `pasada-unica`. FASE III, EJECUCION.
Esta vuelta **VUELVE A SER DE BATERIA** por `AUDITOR.md` `6.1`: la de la 183 esta
en **5 de 9** y **retoma en el TRAMO 6**, no desde el principio. El tope de esta
vuelta es **DOS SUB-TAREAS** por el regimen `6.2`, y esta medido: la 182 cerro su
propio reporte y la 183 **NO**, asi que la cuenta de "dos seguidas" **volvio a
cero**. Van dos tareas y no hay una tercera.

Antes de la primera operacion corre tu bloque de apertura entero y sellalo, con su
medicion del desfase de calibrado dentro, como en las cuatro vueltas anteriores.
Y **abre el reporte con la vuelta**: el de la 183 sigue **sin cerrar y sin
archivar**, y su archivado es el PASO 0 de esta, no un adorno del final.

---

## TAREA 1. LOS REGISTROS Y LAS DOS REPARACIONES DE CODIGO. BLOQUEANTE, Y ANTES DE TOCAR LA BATERIA

**(a) EL ACTA 184 ENTRA EN LA SERIE.** Con el numero que devuelve
`scripts/loop/serie_de_registros.py`, **computado y no tecleado**. Sus numerales,
contados del acta acotada y no de memoria: **siete adjudicaciones `5.1` a `5.7`**
(los siete discutibles marcados, los siete a favor), **la adjudicacion del punto
6** (la reparacion del arnes, que no lleva numeral `5.n` y por eso hay que
contarla aparte o el contador la pierde), **cero caidas propias del auditor**,
declaradas con todas las letras en su seccion 2, y **una caida del ejecutor**,
`E.1`, en su seccion 7. Si tu patron da cero caidas propias y el acta no lo
declarara, **haces PARADA en vez de escribir la entrada**, como ya hace el
instrumento de la 183. Caso positivo por mutacion, con el esperado mutado cayendo.
**La deuda de la serie se remide en esta vuelta y no se hereda del `R.45`.**

**(b) LA REPARACION DEL ARNES QUE PARO LA BATERIA. Es la adjudicacion del punto 6
del acta 184 y va escrita para ejecutarse sin decidir nada.**
`scripts/loop/vuelta165_tarea2_mutacion_censo.py`, caso
`A_el_patron_VIEJO_no_ve_dos_de_su_propia_nomina`:

1. **`esperadas` deja de teclearse y se computa** de la nomina real. Queda
   prohibido teclear un `5` encima del `2`: eso es resolver la discrepancia
   copiando, que `EJECUTOR.md` 2 prohibe.
2. **Queda prohibido tambien el otro camino**, cambiar el caso A para que mire una
   nomina fabricada: es **el unico de los trece que mira la nomina REAL** y los
   casos B y C ya cubren lo fabricado. Vaciarlo seria comprar el verde.
3. **Los dos ficheros que el auditor de la 165 nombro no se borran.** Se quedan
   con nombre propio y el caso pasa a exigir que sigan **DENTRO** del conjunto
   invisible, no que sean **TODO** el conjunto. Esa afirmacion no envejece porque
   la nomina solo crece.
4. **La cifra sale con su corte**, por banco `9.21`: el numero de invisibles lleva
   al lado el tamano de nomina y el `HEAD` sobre el que se conto, igual que ya
   hacen las salidas selladas de los tramos.
5. **Caso positivo por mutacion sobre variable computada**, y el arnes entero
   vuelve a correr: **todos sus casos tienen que CAER al mutar su esperado**. Si
   alguno deja de caer, la reparacion no vale y lo traes.

**(c) LA ESTIMACION DEL `--plan` SALE CON SU CORTE PEGADO, Y ES LA ESCALADA DE LA
RACHA DE REPORTE, QUE ESTA EN DOS.** El acta 184 levanta la caida `E.1`: el
reporte de la 183 publico **36,6 y 47,7 minutos** como estimacion "de hoy" cuando
la nomina ya era de **112** y el `--plan` de hoy dice **37,0 y 48,2**; la cifra
publicada era la de **111** entradas. En
`scripts/loop/vuelta183_bateria_por_tramos.py`, las dos lineas de `ESTIMACION`
pasan a llevar **en la misma linea** el tamano de nomina y el `HEAD` sobre el que
se computaron, de modo que **quien copie la estimacion copie su corte**. Funcion
**PURA** y **arnes propio** que **CAE** si la linea sale sin su corte o si el
corte no coincide con la nomina contada en esa corrida.

**(d) LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 184**, por
`AUDITOR.md` 1.2, porque **las tres discrepancias salieron fuera del marcado**.
Los **30 puestos** de `docs/loop/_auditor_v185_ciega_blind.txt` mas sus **30
vecinos deterministas**, con `vecinos()` importado y la vara importada de
`vuelta182_tarea3_diferenciador_movido.py`. **El cotejo de `sha256` contra
`docs/loop/SELLO_APERTURA_AUDITOR_V185.json` va ANTES de leer un solo puesto** (el
sello declara **38.747 bytes** y `sha256` `f81f1b32594221f1`); si no calzan, no
relees nada y lo dices. **Ninguna clase se vuelve a decidir**: lo que la vara no
ve, la salida no lo afirma.

**LO QUE (b) Y (c) ARRASTRAN SOBRE LA NOMINA, Y SE MIDE ANTES DE SEGUIR.** Los
arneses nuevos entran en la nomina en su misma vuelta por la regla del acta 176
punto 7.2, asi que la nomina sube de **112**. **Mide el reparto antes y despues**:
con tamano de tramo 13, los **ocho primeros tramos no se mueven** y el que crece
es el noveno, que es lo que ya paso al ir de 111 a 112. **Si el reparto moviera
las fronteras de los tramos 1 a 5, sus salidas selladas dejarian de ser del mismo
calibre: ahi te detienes y lo traes**, porque eso no lo decides tu.

## TAREA 2. LA BATERIA, DEL TRAMO 5 AL 9, Y EL CIERRE DEL REPORTE

**EL TRAMO 5 SE RE-CORRE PRIMERO**, ya con (b) puesto, porque su rojo era ese
arnes y una salida sellada en rojo no es del mismo calibre que ocho en verde. **Y
despues los tramos 6, 7, 8 y 9**, en orden, con
`python scripts/loop/vuelta183_bateria_por_tramos.py --tramo N`. Cual toca lo dice
`--siguiente` y no tu memoria.

**CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR, ANTES DE SEGUIR CON EL
SIGUIENTE.** Lo corrido queda corrido: si la vuelta se corta, la siguiente retoma
en el tramo que falte. **El reloj de cada tramo se mide al cerrarlo y se publica
medido**; la estimacion del `--plan` es estimacion, se dice como tal y **desde (c)
va con su corte**. **Una salida sellada que mide CERO BYTES no cuenta como
hecha.** La doble corrida y todas las demas guardas siguen enteras: lo unico que
cambio nunca fue una guarda, fue la cadencia.

**MIDE `git diff --numstat -- dataset/` AL ENTRAR Y AL SALIR DE CADA TRAMO** y
publica las dos cifras. El auditor midio hoy que `git status` marca
`M dataset/metadata/master_graph.json` **por final de linea y no por contenido**
(el `numstat` da cero filas): si en tu corrida ese `numstat` dejara de dar cero,
**eso si es catalogo sucio y paras**.

**SI OTRO ARNES CAE EN ROJO, TE DETIENES AHI Y LO TRAES CON SU SALIDA ENTERA**, sin
re-correrlo y sin arreglarlo tu, exactamente como hizo la 183 con el tramo 5. Esa
decision se le adjudico a favor y sigue siendo la buena.

**CUANDO LOS NUEVE TRAMOS TENGAN SALIDA SELLADA DEL MISMO CALIBRE:** corres
`--componer` para armar `docs/loop/SALIDA_V183_BATERIA.txt`, y **con esa pieza
cierras el reporte con `scripts/loop/cerrar_reporte.py`**, que es lo que lleva dos
vueltas sin conseguirse. **El cierre no se talla a mano ni se rellena la cabecera
sin su pieza**: si `cerrar_reporte.py` cae en rojo, publicas su rojo entero y lo
traes. **Y el reporte, una vez cerrado, se archiva en su propia vuelta.**

---

**MARCA TUS DISCUTIBLES ANTES DE SABER SI ACIERTAS**, como hizo la 183 con sus
siete: los siete se adjudicaron a favor y esa lista es lo que hizo la auditoria
util. Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
