Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la vuelta 189 en la rama `pasada-unica`, FASE III. **ESTA ES
UNA VUELTA DE BATERIA**, por `AUDITOR.md` 6.1: la bateria **entera y sola**, por
tramos, con su doble corrida, su reloj y su salida sellada, **y nada de trabajo
de plan al lado**. Solo lleva DOS tareas y la segunda es la bateria.

Abre con tu bloque de apertura sellado ANTES de la primera operacion (HEAD real,
`git status --porcelain`, `git diff --numstat -- dataset/` al entrar, y el
desfase del calibrado medido AHI y no al cierre), y **talla el esqueleto del
reporte en la apertura y en su propio commit**, como hizo la 188.

---

## TAREA 1. LOS REGISTROS. BLOQUEANTE.

El **acta del auditor de la vuelta 189** (cabecera `# ACTA DEL AUDITOR, VUELTA
189`, cubre la vuelta 188) entra en la serie con el numero que devuelve
`scripts/loop/serie_de_registros.py`, **computado y no tecleado**. Lleva:

- **DIEZ adjudicaciones**, `4.1` a `4.10`, y ademas la adjudicacion de la
  seccion 5 (la bateria corre entera). Las seis primeras (`4.1` a `4.6`) son los
  seis discutibles del ejecutor y **las seis van A FAVOR**.
- **TRES preguntas contestadas** (`4.7`, `4.8`, `4.9`).
- **DOS caidas propias del auditor**, `C.1` y `C.2`, **las dos de metodo y
  ninguna de racha**, y **CERO caidas del ejecutor**. Registra el cero **como
  cero y no lo omitas**.
- **UNA correccion declarada del auditor sobre su propia sede** (`4.9`): el acta
  188 escribio "de `LD-01` hasta `LD-98`" y la cifra buena, medida hoy, es **68
  etiquetas distintas con maximo `LD-154`**. **El texto viejo no se borra.**
- **La racha de reporte queda CORTADA y vuelve a 0** por la adjudicacion `4.10`,
  y eso **cambia** lo que decia el acta 188 (que la mantenia en 2). El registro
  lo dice con las dos cifras, la vieja y la nueva.

Con **caso positivo por mutacion** sobre un acta FABRICADA y su esperado mutado
cayendo, y con **la PARADA conservada entera**: un estado que el registrador no
sepa leer sigue siendo PARADA.

**Y UNA COSA MAS, QUE SALE DE LA `C.2` DEL ACTA Y ES DEL PROPIO REGISTRADOR:
HAZLO IDEMPOTENTE.** Hoy `scripts/loop/vuelta188_tarea1a_registrar_acta188.py`,
**re corrido**, no detecta que el acta ya esta registrada y **escribe una entrada
nueva duplicada con el numero siguiente**. El auditor lo cazo re corriendolo, y
tuvo que revertir a mano una `R.51` fantasma de 196 lineas en
`docs/PENDIENTES.md`. **Un instrumento que el auditor tiene mandato de re correr
y que muta el registro al re correrse es una trampa.** El registrador de esta
vuelta **comprueba primero si el acta que se le pide ya tiene entrada** (por su
cabecera literal, no por el numero) y, si la tiene, **sale sin escribir y
diciendolo con su cifra**. Con su caso positivo por mutacion: un registro que ya
existe y se intenta escribir dos veces **CAE**.

---

## TAREA 2. LA BATERIA DE MUTACIONES, ENTERA, POR TRAMOS Y SOLA.

**PRIMERO EL CLON, Y ES BLOQUEANTE DE LA BATERIA.**
`scripts/loop/vuelta183_bateria_por_tramos.py` **NO se corre tal cual**. Motivo
medido por el auditor en esta vuelta, y esta escrito entero en la seccion 5 de
su acta:

- La nomina paso de **121 a 125** entradas, asi que el reparto **ya no da NUEVE
  tramos sino DIEZ** (`CIFRA entradas de la nomina: 125`, `CIFRA tramos: 10`,
  nueve de 13 y uno de 8).
- Su `--siguiente` dice hoy **`CIFRA tramos CON salida sellada no vacia: 9`,
  `CIFRA tramos que FALTAN: 1`, `EL SIGUIENTE ES EL TRAMO 10`**, porque cuenta
  las salidas `SALIDA_V183_BATERIA_TRAMO_n.txt` de la corrida de la 183/184.
- **Correrlo tal cual haria un solo tramo de diez y declararia la bateria
  corrida habiendo corrido 8 arneses de 125.** Un verde comodo del tamano de la
  guarda entera.

**LA ADJUDICACION DEL AUDITOR, QUE NO SE RE LITIGA:** la bateria de la 189
**corre ENTERA sobre la nomina de hoy y NO hereda ni una salida sellada de la
corrida 183/184**. `AUDITOR.md` 6.1 dice "la bateria entera"; "una vuelta cortada
retoma en el tramo siguiente" habla de **una vuelta que se corto**, y la del
183/184 **cerro**; y **"DEL MISMO CALIBRE"** lo cierra, porque nueve salidas de
hace cinco vueltas y una de hoy no son del mismo calibre. **Y NO SE BORRA NADA:
las nueve salidas de la 183 se quedan donde estan.**

**COMO:** escribe `scripts/loop/vuelta189_bateria_por_tramos.py`, **clon
declarado** de `vuelta183_bateria_por_tramos.py`, cotejado con
`scripts/loop/cotejar_clon_declarado.py` y con la salida del cotejo pegada en el
reporte. El fichero ya computa su numero de vuelta de
`os.path.basename(__file__)` y trae `literales_de_vuelta_clavados()`, asi que el
clon **escribe `SALIDA_V189_BATERIA_TRAMO_n.txt` solo y su `--siguiente` cuenta
desde cero**. **Comprueba las dos cosas antes de lanzar nada**, con `--plan` y
con `--siguiente`, y pega las dos salidas.

**DESPUES LA BATERIA, TRAMO A TRAMO:**

1. `--plan` primero, y **publica el reparto computado, no tecleado**: cuantas
   entradas, cuantos tramos y de que tamano cada uno, con el corte de HEAD.
2. Cada tramo se corre con `--tramo N`, **se sella su salida y SE COMMITEA antes
   de pasar al siguiente**. Si la vuelta se corta, la siguiente **retoma en el
   tramo que diga `--siguiente`**, no desde el principio.
3. **Doble corrida** de cada arnes, con el cotejo de reproducibilidad: el mismo
   `sha256` normalizado a LF las dos veces. Un arnes que cambia solo entre dos
   corridas del mismo dia sobre el mismo sujeto es **PARADA**, y se trae.
4. **La doble corrida EXCLUYE explicitamente cualquier arnes que ya haya salido
   en rojo en esa misma vuelta**, y **lo dice en su salida** con el nombre del
   excluido, la ruta de su salida en rojo y el motivo. Una exclusion muda seria
   peor que el problema.
5. **Un arnes ya sellado que cae en rojo detiene AL ARNES, no a la vuelta**: te
   detienes ahi, lo traes con su salida entera, **sin re correrlo y sin
   arreglarlo**. Un arnes que **nace hoy** y sale en rojo si se repara, y su
   corrida en rojo se conserva entera con el motivo dentro del propio fichero.
6. **El reloj:** publica la estimacion del `--plan` **como estimacion** y, al
   cerrar cada tramo, **la medicion de verdad**, que es la que manda.
7. `--componer` al final, y **la bateria se declara corrida cuando LOS DIEZ
   tramos tienen salida sellada DEL MISMO CALIBRE**. **Una salida sellada que
   mide CERO BYTES no cuenta como hecha.**

**NADA MAS ENTRA EN ESTA VUELTA.** Ni cribado, ni recomputo, ni operaciones del
plan, ni las mesas anotadas, ni podar la nomina (la opcion `c` que el fundador
RECHAZO el 5 sep). **La nomina sigue creciendo y nadie la poda sin el fundador.**

---

## LO QUE VA A LA VUELTA 190 Y NO A ESTA, PARA QUE NO SE CUELE NI SE PIERDA

Queda escrito aqui **para que la 190 no tenga que redescubrirlo**, y **no se
toca en la 189**:

1. **LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 189**, encargada por
   `AUDITOR.md` 1.2 porque la discrepancia del **puesto 2422** cayo FUERA de los
   dudosos marcados. 30 puestos mas 30 vecinos deterministas, con `vecinos()`
   importada y su parametro `evitar`, solape del universo en cero, y **ninguna
   clase se vuelve a decidir**.
2. **`P.1` EN CODIGO:** la `guarda_del_sujeto_congelado()` **separa en su salida**
   las entradas `NO DECIDIBLE` que traen motivo escrito dentro de su propio
   arnes de las que no lo traen. La lista de exentos **NO se abre**: el auditor
   adjudico que `NO DECIDIBLE` se queda como esta y que la deuda sigue visible.
3. **`P.2` EN CODIGO:** el cotejo de clon declarado **separa el clon que ANADE
   codigo del que CAMBIA codigo**, publica las dos cifras (sentencias del
   original que sobreviven identicas, y sentencias nuevas del clon) y **solo cae
   en rojo cuando alguna del original no sobrevive**.
4. **`D.4`, la condicion que el auditor le puso al aprobarlo:** la excepcion
   mecanica del caso decisivo **publica siempre su lista, aunque este vacia**.
5. **LA SEDE DE `OP-L-02`, QUE ES UNA MEDICION NO CORRIDA Y NO UNA PARADA.** Su
   `verificacion` habla de "las tres nominas afectadas" y de "cada grupo del
   backlog", y **nadie ha buscado todavia si esas tres nominas tienen sede en el
   repo**. Se busca, con el comando escrito y su salida pegada. **Si la hay, la
   ficha se resuelve contra ella. Si no la hay en ninguna parte, ENTONCES es
   PARADA y se trae al fundador**, porque inventarle una sede es cambiar el
   alcance de la campana.

---

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
