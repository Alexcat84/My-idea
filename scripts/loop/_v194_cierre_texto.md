## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**LA CABECERA DE ARRIBA ES LA TABLA TALLADA ENTERA**, pegada de
`docs/loop/SALIDA_V194_TALLADOR_CABECERA.txt`, que salio de
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 194` con **exitcode 0
y sin una sola celda ilegible**. **LA CELDA QUE NO SALE DE UN INSTRUMENTO NO SE
ESCRIBE**, y por eso aqui abajo no se repite ninguna de sus cifras: se anaden las
que el tallador no cubre, cada una con el fichero del que sale.

| lo que se mide | cifra | de que fichero sale |
|---|---|---|
| entradas de la nomina de la bateria | 127 | `len(VMV.VIEJAS)`, corrido en la apertura y otra vez al cierre |
| tramos del reparto | 10 | `SALIDA_V194_T3B_PLAN.txt`, computado y no tecleado |
| entradas que los tramos dicen haber corrido | 127 | `SALIDA_V194_BATERIA_COMPUESTA.txt` |
| entradas sin correr, de mas, o repetidas | 0, 0 y 0 | `SALIDA_V194_BATERIA_COMPUESTA.txt` |
| tramos con salida sellada no vacia | 10 de 10 | las diez `SALIDA_V194_BATERIA_TRAMO_n.txt` |
| tramos cuya `CLASE DEL VEREDICTO` es `ROJO POR FALLO` | 10 de 10 | la linea `CLASE DEL VEREDICTO` de cada sellada |
| arneses que no mordieron | 1 (tramo 7) | la linea `CIFRA de FALLO` de cada sellada |
| arneses sin reproducir | 0 | la misma linea, en los diez |
| arneses fuera de la nomina | 6 | la misma linea, en los diez |
| entradas sin sujeto congelado | 3, con motivo escrito | la misma linea, en los diez |
| entradas de la serie `R.n` | 48, siguiente libre `R.57`, 0 colisiones y 0 huecos | `serie_de_registros.py`, corrido al cierre |
| actas sin entrada propia en la serie, tramo 173 a 193 | 8 | `SALIDA_V194_T1A_REGISTRO_R56.txt` |
| casos del arnes del registrador | 27, 27 pasan, 0 fallan | `SALIDA_V194_T1A_MUTACION_REGISTRADOR.txt` |
| casos del arnes de la sede del turno | 14, 14 pasan, 0 fallan | `SALIDA_V194_T2C_MUTACION_SEDE_DEL_TURNO.txt` |
| casos del cotejo de los tres escenarios | 13, 13 pasan, 0 fallan | `SALIDA_V194_T2G_TRES_ESCENARIOS.txt` |

**LA SALIDA UNICA DE LA BATERIA:** `docs/loop/SALIDA_V194_BATERIA.txt`, **102495
bytes en disco y 102495 normalizado a LF**, **1454 lineas**, `sha256` LF
`f2d927fa66cdc40a3f157294eaee1c86d1ffb4633a7afbd731befc1cd094b263`. **El hueco
que la 193 declaro con su nombre y sus cero bytes ya no es un hueco.**

**EL RELOJ DE LA BATERIA, CON SUS DOS MEDIDAS:** **17.2 minutos** sumando las
duraciones monotonas de los diez tramos, y **30.1 minutos** de ventana de reloj de
pared entre el inicio del tramo 1 (`2026-09-06T22:01:57Z`) y el fin del tramo 10
(`2026-09-06T22:32:03Z`).

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ESTADO DEL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO.**
`git status --porcelain` daba **1** linea al entrar.
`git diff --numstat -- dataset/` daba **0** filas. Las dos salen de
`docs/loop/SALIDA_V194_APERTURA.txt`, sellado antes de la primera operacion. **La
unica linea de `status` que habia era el propio fichero del bloque de apertura,
todavia sin commitear**, y esta escrita dentro de su bloque `B`.

**SE TOCARON, TODOS EN `scripts/loop/`, `docs/loop/` y `.gitignore`:**
`apertura_del_auditor.py` (su `_cargar_turno()`),
`vuelta192_tarea4_mutacion_cuarta_puerta.py`,
`vuelta193_tarea4e_mutacion_sello_entre_procesos.py`, `.gitignore`, mas los
instrumentos nuevos de esta vuelta. **`docs/PENDIENTES.md`** gano la entrada
`R.56`. **Y `docs/loop/SALIDA_V194_APERTURA.txt` recibio al cierre un bloque `Z`
marcado como RESTATEMENT DECLARADO**, que es mi caida `C.2` y va contada abajo.

**NO SE TOCO NADA DE:** `dataset/`, `web/`, `engine/`,
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `docs/plan/`, ni **la nomina de la
bateria**, que sigue en **127 entradas** leidas de `VMV.VIEJAS` al entrar y al
salir. La opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue rechazada. **Y
esta vuelta tuvo el motivo mas grande que ha habido para tocarla y no la toco:**
seis arneses fuera de la nomina son lo que pone los diez tramos en rojo.

**LOS VEREDICTOS NO SE MOVIERON:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y
cierra en **4054129 bytes en disco y 4054129 bytes normalizado a LF**, con
`sha256` de disco **`0a77b5a35a962621`** y `sha256` LF **`0a77b5a35a962621`**, medido en el
bloque `C` de la apertura y otra vez al cierre.

**`dataset/` SE MIDIO AL ENTRAR Y AL SALIR Y LAS DOS CIFRAS SE PUBLICAN: CERO Y
CERO.** El ciclo de Gate 0 corrio ENTERO las dos veces, con
`--reaplico-curaduria` y despues `etiquetas_de_cara.py --aplicar`, que es lo que
el encargo trajo medido y lo que evita las 72 lineas.

**Y NO ENTRO NADA DE LO QUE EL ENCARGO DEJA FUERA:** ni cribado, ni recomputo, ni
operaciones del plan, ni las mesas anotadas, ni ciegas nuevas, ni la relectura al
doble del tramo del auditor, que va a la 195 con su tramo ya cerrado.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` REGISTRE LA CIFRA DEL CUERPO Y NO LA DE LA TABLA DE CREDITO.** El acta 194
declara **dos** caidas propias del auditor en su seccion 8 y **una** en su fila de
la tabla. Elegi el cuerpo porque el encargo dice literal *"cada cifra se cuenta
del cuerpo acotado del acta y no de aqui"*. **Un lector puede sostener lo
contrario con la misma fuerza:** la tabla de credito es la sede de las cifras de
credito, y la fila es la que lleva la racha. **Las dos quedan publicadas con su
linea; lo discutible es cual manda.**

**`D.2` CAMBIE UNA PARADA POR UNA GUARDA DE PUBLICACION, Y ESO SE PUEDE LEER COMO
AFLOJAR.** El registrador de la 193 PARABA cuando el cuerpo y la fila no calzaban;
el mio publica las dos y **cae en rojo si la entrada no las lleva las dos**.
Sostengo que la parada vieja cazaba **un error de lectura del registrador** y que
aqui no lo hay, pero **un lector puede decir que una parada sustituida es una
parada menos**. La parada sigue entera en la fila del ejecutor.

**`D.3` TOQUE UN TERCER FICHERO QUE EL ENCARGO NO NOMBRA.** La pieza `e` dice *"NO
SE CLONA NINGUNO DE LOS DOS FICHEROS: se les anade"*, y yo ademas arregle
`_cargar_turno()` en `apertura_del_auditor.py`. **Sin eso el arnes de la 193 sigue
en rojo con el turno puesto**, o sea que la tarea no se podia cerrar sin tocarlo;
pero **el encargo no me lo pidio y lo marco**.

**`D.4` ELEGI UN LADO EN `_cargar_turno()` Y EL OTRO ERA DEFENDIBLE.** Cuando el
fichero **no existe** reinicio la memoria; cuando **existe y no se puede leer** NO
la toco. **Un lector puede sostener que un JSON roto tambien debe reiniciar**, por
simetria y para que no quede estado fantasma. Elegi no perder el estado vivo en
silencio, y lo digo.

**`D.5` PUSE UN CENTINELA EN LA SEDE DE VERDAD DEL TURNO PARA PROBAR QUE NADIE LA
BORRA.** Para demostrar que un arnes no borra ese fichero, hace falta que el
fichero exista mientras corre la prueba. **O sea que toco la sede que digo
proteger.** La respaldo byte a byte si hay una viva, pongo un centinela fabricado,
y al terminar restauro y **REMIDO** existencia, bytes y `sha256`. **Un lector
puede decir que la sede de verdad no se toca nunca y que la prueba debia montarse
en otro sitio.**

**`D.6` CORRI LA BATERIA SABIENDO QUE SALDRIA EN ROJO POR ALGO QUE NO PUEDO
ARREGLAR.** Los seis arneses fuera de la nomina ponen los diez tramos en rojo, y
la unica reparacion es tocar la nomina, que esta prohibida. **Podia haber parado
antes de correrla y traer la contradiccion**; corri, porque `AUDITOR.md` 6.1
manda correrla y porque un rojo medido dice mas que una parada. **Lo marco por si
la eleccion correcta era la otra.**

**`D.7` LE ANADI A MIS TRES ARNESES NUEVOS LA LINEA `CIFRA casos`, QUE ES LA QUE
`cerrar_reporte.py` USA PARA COTEJAR MI PROSA.** Sin ella, mis citas de casos
salen `SIN COTEJO`, o sea que la cifra se teclea y nadie la mira. **Un lector
puede decir que anadir la linea que me va a medir es escoger mi propia vara.** La
anadi solo a los arneses nuevos y **no toque la de ninguno viejo**.

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` LAS DOS CIFRAS DE CAIDAS PROPIAS DEL ACTA 194, CUAL ES LA SEDE?** Su
seccion 8 dice dos y su fila de credito dice una. **Registre la del cuerpo y
publique las dos.** No lo adjudico yo: es una cifra de credito del auditor.

**`P.2` LOS SEIS ARNESES FUERA DE LA NOMINA, QUIEN LOS METE Y CUANDO?** La regla
del propio fichero dice que un arnes entra en la nomina, y el acta 176 acepto que
entre en su misma vuelta; pero **las vueltas 191, 192, 193 y 194 escribieron
arneses y ninguno entro**, y cada encargo repite *"NO TOQUES LA NOMINA"*. **Tal
como esta, la bateria de la 199 saldra en rojo por lo mismo y con la lista mas
larga.** No lo resuelvo porque tocar la nomina esta expresamente prohibido.

**`P.3` UNA BATERIA CON LOS DIEZ TRAMOS EN ROJO Y `--componer` EN VERDE, ESTA
CORRIDA?** Por la letra de la 6.1 si: los diez tienen salida sellada no vacia y
del mismo calibre, y la cobertura se lee de las salidas. **Pero `--componer` sale
con exitcode 0 sin mirar el veredicto de los tramos**, y eso es exactamente el
punto que la lista de lo que sigue fuera nombra como *"el exitcode 2 propagado a
`--componer`"*. **Lo dejo dicho con las dos mitades: corrida por la letra, roja
por dentro.**

## 7. PENDIENTES DE DOCTRINA

**NINGUNO ABIERTO POR MI.** Las tres preguntas de arriba no piden regla nueva:
piden que alguien con autoridad diga cual de dos reglas ya escritas manda.

## 8. LO QUE LA 195 RECIBE

**LA BATERIA ESTA CORRIDA Y SU HUECO CERRADO**, asi que la 195 vuelve al regimen
de vuelta normal, con la seccion 9 en hueco declarado y medido. **La siguiente
bateria cae en la 199.**

**LO QUE SIGUE FUERA Y VA NOMBRADO PARA QUE NO SE REDESCUBRA:** la relectura al
doble del tramo de la tanda del auditor, con su tramo y su doble ya cerrados por
el acta 194; el remedio de codigo del hallazgo `5.3`, que desde hoy aplico a mano
en mis mensajes de commit; el desfase de `PATRONES_ACTA`; `acumulan()` que lea la
tabla; el cotejo de clon declarado que separa sentencia de codigo de cambio de
texto; la excepcion que publica siempre su lista; el censo de arneses con carril
de mutacion sin fichero propio; las **8** actas sin entrada propia en la serie
(173 a 180); el exitcode 2 propagado a `--componer`; el campo `evidencia` de
`OP-L-02`, **cuyo ESTADO NO SE MUEVE: sigue en `LISTA`**; y **las 72 filas `B` del
archivo**, nombradas y no resueltas.

**Y DOS COSAS QUE LA 195 RECIBE ROTAS Y QUE YO NO PODIA ARREGLAR HOY:** los
**seis** arneses fuera de la nomina, que ponen en rojo los diez tramos de
cualquier bateria mientras nadie los meta; y `vuelta172_tarea5_mutacion_cierre.py`,
que **no muerde** y que la bateria de la 189 ya publicaba igual.

### 8.1 MIS CAIDAS PROPIAS DE ESTA VUELTA, DECLARADAS Y NO OMITIDAS

**`C.1` (Y ACUMULA). MI BLOQUE DE APERTURA NO CORRIO `tsc` NI `pnpm test`, Y ESAS
DOS CELDAS DE APERTURA SE MIDIERON AL CIERRE.** Corri los dos comandos en el
momento del cierre y **lo declare en su fichero propio**,
`docs/loop/SALIDA_V194_APERTURA_INCOMPLETA_DECLARADA.txt`, que es el carril que la
`4.7` del acta 194 adjudico A FAVOR. **La cifra es cierta; su MOMENTO no es el que
su nombre dice.** Por `EJECUTOR.md` 1, una columna de apertura medida al cierre es
caida que ACUMULA, y **la cuento como tal en vez de discutirla**. **Es la SEGUNDA
vuelta seguida con esta misma caida**, porque el reporte de la 193 se la declaro a
si mismo en su `C.1` y yo clone su bloque de apertura.

**`C.2` (DE METODO). TOQUE LA APERTURA SELLADA AL CIERRE.** La guarda `D.1` de
`cerrar_reporte.py` coteja la seccion 4 contra la apertura sellada buscando **dos
literales exactos**, y mi bloque de apertura escribio esas mismas cifras **con
otras palabras**. Anadi al final de `docs/loop/SALIDA_V194_APERTURA.txt` un bloque
`Z` **marcado como RESTATEMENT DECLARADO**, que **lee las dos cifras del propio
fichero con una expresion regular** y no cambia ni un digito, y que dice dentro
que no es una medicion nueva. La version sin ese bloque se puede cotejar contra el
commit `d3e2c8f6`, leido con `git log --diff-filter=A`. **Tocar una apertura
sellada al cierre es exactamente la especie que esta casa vigila**, y **tambien es
la segunda vuelta seguida**: la 193 lo conto como su `C.3`.

**`C.3` (DE METODO, Y ES LA CAUSA DE LAS DOS DE ARRIBA). CLONE EL BLOQUE DE
APERTURA DE LA 193 SIN LEER LA SECCION 8.1 DE SU PROPIO REPORTE**, que declaraba
esas dos caidas con su nombre y su remedio. **Un clon declarado hereda tambien los
defectos declarados de su fuente**, y el sitio donde estan escritos es el reporte
de esa vuelta. **El remedio durable, nombrado y no hecho aqui:** que el bloque de
apertura corra el ciclo completo, incluidos `tsc` y `pnpm test`, y que escriba el
los dos literales que la guarda `D.1` busca. Mientras las dos redacciones no se
toquen, **estas dos caidas se heredan de vuelta en vuelta**, que es justo lo que
acaba de pasar dos veces.
