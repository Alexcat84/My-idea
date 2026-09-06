### TAREA 2. LA BATERIA, DEL TRAMO 5 AL 9, Y EL CIERRE DEL REPORTE. LA BATERIA CERRO ENTERA. EL CIERRE, NO: PARADA

**LOS NUEVE TRAMOS TIENEN SALIDA SELLADA. OCHO EN VERDE Y EL NOVENO EN ROJO,
QUE SE TRAE SIN TOCAR.** La tabla sale de contar
`docs/loop/SALIDA_V183_BATERIA_TRAMO_<n>.txt` con
`scripts/loop/_v184_tallar_t2.py`, y no de recordar nada: los bytes con
`os.path.getsize` y con el mismo fichero normalizado a LF, las lineas contando
saltos, las entradas contando sus lineas `ENTRADA DEL TRAMO:`, el exitcode y
los minutos de las lineas que el propio tramo escribe al sellarse, y la nomina
de la linea `LAS <n> MUTACIONES VIEJAS` que cada tramo imprime.

| tramo | bytes disco | bytes LF | lineas | entradas | nomina del sello | exitcode | minutos | quien lo sello |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **1** | 9116 | 9116 | 120 | 13 | 112 | **0** | 2.1 | vuelta 183 |
| **2** | 7352 | 7352 | 114 | 13 | 112 | **0** | 3.8 | vuelta 183 |
| **3** | 7406 | 7406 | 114 | 13 | 112 | **0** | 3.7 | vuelta 183 |
| **4** | 7421 | 7421 | 114 | 13 | 112 | **0** | 1.0 | vuelta 183 |
| **5** | 7385 | 7385 | 114 | 13 | 113 | **0** | 0.9 | **vuelta 184** |
| **6** | 7428 | 7428 | 114 | 13 | 113 | **0** | 0.9 | **vuelta 184** |
| **7** | 7456 | 7456 | 114 | 13 | 113 | **0** | 0.5 | **vuelta 184** |
| **8** | 7407 | 7407 | 114 | 13 | 113 | **0** | 0.7 | **vuelta 184** |
| **9** | 6769 | 6769 | 105 | 9 | 113 | **1** | 0.4 | **vuelta 184** |

**CIFRA tramos con salida sellada no vacia: 9 de 9.** **CIFRA entradas que
los tramos dicen haber corrido, sumadas de sus lineas `ENTRADA DEL TRAMO:`:
113.** **CIFRA exitcodes distintos de cero: 1.** **Suma de los minutos
medidos: 14.0.** El tramo mas largo midio **3.8 minutos** y el mas corto **0.4**.

**LA ESTIMACION DEL `--plan` ES ESTIMACION Y DESDE LA TAREA 1.c VA CON SU
CORTE**, y por eso se puede cotejar sin ir a buscar el denominador: la de hoy
dice *"entre 37.3 y 48.6 (corte: HEAD ..., nomina de 113 entradas contada en
esta corrida)"*, y **la medicion de verdad, sumada de los nueve tramos, es
14.0 minutos**. La estimacion se paso por arriba por mas del doble, y **eso es
lo que pasa cuando se estima con la cifra de una bateria del auditor**: se
dice medido y no se disfraza.

**`git diff --numstat -- dataset/` SE MIDIO AL ENTRAR Y AL SALIR DE CADA UNO
DE LOS CINCO TRAMOS DE ESTA VUELTA, Y LAS DIEZ MEDICIONES DIERON CERO FILAS.**
Al cerrar la vuelta vuelve a dar **0 filas**. `git status` sigue marcando
`M dataset/metadata/master_graph.json` **por final de linea y no por
contenido**, que es lo que el acta 184 midio en su punto 3.1. **No hay catalogo
sucio y no hay parada por esa via.**

**EL TRAMO 5 SE RE CORRIO PRIMERO, YA CON LA REPARACION DE LA 1.b PUESTA**, y
paso de **exitcode 1** a **exitcode 0**. **Su rojo era ese arnes**, y con el
esperado computado en vez de tecleado el arnes vuelve a morder sin caducar.

**EL TRAMO 9 SALIO EN ROJO Y NO SE RE CORRIO NI SE ARREGLO.** El motivo,
literal de su propia salida sellada: **`NO REPRODUCIBLE: 1
(vuelta182_tarea2_mutacion_apertura_auditor.py)`**, cuya salida sellada
`SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` **cambia SOLO entre dos
corridas, en su linea 53**, y lo que cambia es **el sufijo aleatorio del
directorio temporal que esa misma linea imprime**:

```
  vuelta182_tarea2_mutacion_apertura_auditor.py exit 0  NO REPRODUCIBLE      2.9s
  NO REPRODUCIBLE: 1 (vuelta182_tarea2_mutacion_apertura_auditor.py)
         corrida 1:       | SELLO ESCRITO: ../../AppData/Local/Temp/v182_apertura_2yoa89kq/SELLO_APERTURA_AUDITOR_VARNES_LIMPIO.json (582 bytes)
         corrida 2:       | SELLO ESCRITO: ../../AppData/Local/Temp/v182_apertura_5ixwb87k/SELLO_APERTURA_AUDITOR_VARNES_LIMPIO.json (582 bytes)
ROJO: 0 con el ancla perdida, 0 que no mordieron y 1 cuya salida sellada NO SE REPITE.
```

**EL ARNES, CORRIDO SOLO, SALE `exit 0`: EL ROJO LO ENCIENDE LA DOBLE CORRIDA
DE LA BATERIA, QUE ES LA UNICA QUE LO MIRA.** Y **es su primera bateria**:
buscado su nombre en todas las `docs/loop/SALIDA_V*_BATERIA*.txt`, **el unico
fichero de bateria que lo contiene es el tramo 9 de hoy**. Se trae sin tocar,
que es lo que el encargo manda y lo que el acta 184 adjudico a favor cuando la
183 hizo lo mismo con su tramo 5.

**LA COMPOSICION, CORRIDA Y MEDIDA:** `docs/loop/SALIDA_V183_BATERIA.txt`
(**71753 bytes en disco y 71753 bytes normalizados a LF**, 1101 lineas, `sha256` LF `422a909ad6ffb167`),
con **113 entradas corridas**, **0 sin correr**, **0 repetidas** y **0
ajenas**, leido de `docs/loop/SALIDA_V184_COMPONER.txt` (**2539 bytes en disco y 2503 bytes normalizados a LF**).

**LA MIRADA DE LA BATERIA SOBRE SI MISMA, RECOMPUTADA AL CIERRE:** nomina
**113 entradas**, `arneses_que_faltan()` **0**, `nomina_invisible_al_censo()`
**0**, `guarda_del_sujeto_congelado()` **0**.

#### PARADA. EL CIERRE DEL REPORTE CAE EN ROJO Y NO LO ARREGLO YO

**LAS TRES PIEZAS DEL CIERRE ESTAN TALLADAS Y MEDIDAS**, y ninguna se teclea:

- la cabecera, `docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt` (**2435 bytes en disco y 2415 bytes normalizados a LF**),
  **exitcode 0**, con sus once filas de tabla;
- el cuerpo, `scripts/loop/_v184_cierre_texto.md` (**13982 bytes en disco y 13982 bytes normalizados a LF**),
  con sus **secciones 3 a 8** talladas por `scripts/loop/_v184_tallar_cierre.py`;
- la bateria, `docs/loop/SALIDA_V183_BATERIA.txt` (**71753 bytes en disco y 71753 bytes normalizados a LF**).

**Y AUN ASI `scripts/loop/cerrar_reporte.py` SALE EN ROJO, exitcode 1, POR UNA
GUARDA VIGENTE QUE CHOCA CON LA LETRA DEL ENCARGO.** El encargo nombra
`docs/loop/SALIDA_V183_BATERIA.txt` como la pieza con la que cerrar el reporte
**de la 184**; la guarda, nacida en la vuelta 182 como remedio del `E.1` del
acta 180, dice que **una corrida de otra vuelta no cierra este reporte** y mira
el numero que lleva el nombre del fichero. **Las dos son reglas escritas y
vigentes.** El rojo, entero:

**EL CORTE DEL ROJO QUE VIENE ABAJO, DICHO ANTES DE PEGARLO** (`EJECUTOR.md`
8, toda cifra con su fecha de corte): el intento se corrio **con la TAREA 1 ya
anexada y la TAREA 2 todavia no**, asi que la cifra de bytes que el propio rojo
mide de `docs/loop/REPORTE.md` es la de **ese** momento y no la del reporte
terminado, que crece justamente al anexar esta tarea. **No se retoca la cita:**
una cita que se retoca deja de ser una cita, y por eso lleva su corte al lado en
vez de un numero corregido.

```
==============================================================================
SE CIERRA EL REPORTE DE LA VUELTA 184, EN UN SOLO ACTO
==============================================================================

A) EL SUJETO, COMPROBADO ANTES DE TOCARLO
   docs/loop/REPORTE.md primera linea: # REPORTE DE LA VUELTA 184 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.
   CIFRA bytes: 16031 | saltos de linea: 230
   contiene '**EL VEREDICTO DE UNA LINEA: SIN E' -> SI (se esperaba SI)
   contiene 'PENDIENTE DE TALLAR AL CIERRE'      -> SI (se esperaba SI)
   contiene '\n## 3.'                            -> NO (se esperaba NO)
   contiene '\n## 9.'                            -> NO (se esperaba NO)

B) LAS TRES PIEZAS QUE VIENEN DE FUERA, MEDIDAS ANTES DE PEGARLAS
   docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt             2415 bytes, 11 filas de tabla
   scripts/loop/_v184_cierre_texto.md                     13982 bytes, sha256 050cdbb4ea99e11c
      ## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT
      ## 4. LA GUARDA DEL COMMIT DE `dataset/`, CORRIDA EL DIA QUE SERVIA
      ## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO
      ## 6. LAS PREGUNTAS
      ## 7. PENDIENTES DE DOCTRINA
      ## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA
   docs/loop/SALIDA_V183_BATERIA.txt                    71753 bytes
   CIFRA lineas no vacias de la bateria: 1009
   vuelta que lleva dentro el nombre del fichero: 183
   RAMA DE LA SECCION 9, decidida por rama_de_la_seccion9(): ROJO
      motivo: el fichero de bateria que se pasa es el de la vuelta 183 y se esta cerrando la 184. UNA CORRIDA DE OTRA VUELTA NO CIERRA ESTE REPORTE.

B.1) LOS NUMERALES DEL VEREDICTO, COTEJADOS CONTRA LO QUE EL CUERPO
     PERMITE CONTAR (vuelta 183, TAREA 1.c; escalada de AUDITOR.md 1.2)
   el veredicto, tal como se paso: 'LA VUELTA 184 CIERRA SUS DOS TAREAS, PONE EN CODIGO LAS DOS REPARACIONES QUE EL ACTA 184 ADJUDICO Y CORRE LA BATERIA HAS'
   CIFRA numerales hallados en el veredicto: 1
      'DOS'      -> 2 tareas
   LAS CUENTAS DEL CUERPO, CONTADAS Y NO TECLEADAS:
      caidas   -> 2
      tareas   -> 2
   CIFRA numerales que NO calzan: 0

ROJO, 1 motivo(s), y NO se escribe nada:
   el fichero de bateria que se pasa es el de la vuelta 183 y se esta cerrando la 184. UNA CORRIDA DE OTRA VUELTA NO CIERRA ESTE REPORTE.

```

**LO QUE NO HICE, Y ES LA MITAD QUE IMPORTA.** No copie ni renombre el fichero
a `SALIDA_V184_BATERIA.txt` para que la guarda pasara: **el nombre lo computa
el lanzador de su propio fichero**, que es justo lo que la 183 reparo y el acta
184 le adjudico a favor, y fabricar un nombre para que una guarda deje pasar es
comprar el verde. **Tampoco toque `cerrar_reporte.py`:** nadie me encargo
aflojar esa guarda, y `EJECUTOR.md` 4 y 5 lo prohiben. **Publico su rojo entero
y lo traigo.**

**CONSECUENCIA, DICHA SIN ADORNAR:** `docs/loop/REPORTE.md` **se queda con su
veredicto sin escribir y su cabecera sin tallar**, porque **el cierre no se
talla a mano**. Es la tercera vuelta seguida sin cerrar su propio reporte, y
**el motivo de esta no es que se cayera al final: es que una guarda vigente lo
impide y la decision no es mia.**

**Y LA COMPARACION DE LA CABECERA SE CORRE IGUAL, SALGA LO QUE SALGA**
(`EJECUTOR.md` 1: *"antes del commit, `--comparar docs/loop/REPORTE.md` tiene
que dar CABECERA IDENTICA AL TALLADOR, y su salida se cita en el reporte"*).
Corrida hoy, `docs/loop/SALIDA_V184_TALLADOR_COMPARAR.txt` (**3439 bytes en disco y 3405 bytes normalizados a LF**),
**exitcode 1**, dice:

```
  AUSENTE  | censo: nodos / vivos / deprecados | la fila no esta en el fichero
  AUSENTE  | Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | la fila no esta en el fichero
  AUSENTE  | aristas: `nodos_siguientes` / `nodos_previos` / suma / union | la fila no esta en el fichero
  AUSENTE  | motor | la fila no esta en el fichero
  AUSENTE  | web: ficheros / tests | la fila no esta en el fichero
  AUSENTE  | tsc | la fila no esta en el fichero
  AUSENTE  | aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | la fila no esta en el fichero
  AUSENTE  | desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | la fila no esta en el fichero
  AUSENTE  | identidad: rama y commit de apertura (leidos de git, no tecleados) | la fila no esta en el fichero
  filas cotejadas: 9 | DISTINTAS: 0 | ausentes: 9
  CABECERA: NO CALZA CON EL TALLADOR
```

**LAS NUEVE FILAS ESTAN AUSENTES Y NINGUNA ESTA DISTINTA, Y ESA DIFERENCIA ES
LA QUE IMPORTA.** *Ausente* significa que **la cabecera no se pego**, porque el
cierre cayo en rojo; *distinta* habria significado que **alguien la tecleo**.
**Cero distintas: ninguna celda de este reporte esta tecleada.**

#### LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

*(van aqui, y no en la seccion 5, porque la seccion 5 vive en
`scripts/loop/_v184_cierre_texto.md` y esa pieza no se pudo pegar. **Un reporte
sin discutibles no sirve para la relectura ciega**, asi que se anexan con la
tarea que si cerro en vez de perderse con la que no.)*

**`D.1`. COMPUSE LA BATERIA CON EL TRAMO 9 EN ROJO DENTRO.** El encargo dice
dos cosas que aqui se tocan: *"si otro arnes cae en rojo, te detienes ahi"* y
*"cuando los nueve tramos tengan salida sellada del mismo calibre, corres
`--componer`"*. **Me detuve** (no re corri el tramo 9 y no toque el arnes),
**pero si compuse**. Mi lectura de *mismo calibre* es la de `AUDITOR.md` 6.1
con sus palabras, *"nueve salidas selladas no valen si una es de otra HONDURA
que las demas"*: la hondura del tramo 9 es la de los otros ocho, mismo
protocolo y misma doble corrida. **Lo que cambia no es la hondura, es el
resultado.** La lectura contraria, la que el encargo aplico al tramo 5, dejaria
la bateria sin componer. **Elegi la que publica el rojo entero dentro de la
pieza, y lo marco.**

**`D.2`. EL ESQUELETO Y EL TALLADOR NOMBRAN EL ACTA DE LA VUELTA ANTERIOR Y NO
LA QUE ORDENA ESTA.** Las dos maquinas piden el acta de `VUELTA - 1`, o sea la
**183**, y el acta que encarga esta vuelta es la **184**, cuyo commit es
justamente el **HEAD de apertura** que la misma identidad publica. **No toque
la maquina**, porque el clon declarado dice que no se toca salvo el numero de
vuelta. **Lo digo en vez de dejar que la celda hable sola.**

**`D.3`. RENOMBRE UN CASO DEL ARNES DE LA 165 QUE EL ACTA 184 NOMBRA POR SU
NOMBRE.** El acta cita `A_el_patron_VIEJO_no_ve_dos_de_su_propia_nomina`; hoy
se llama `A_el_patron_VIEJO_no_ve_parte_de_su_propia_nomina` y ademas **se
partio en dos**, porque el nombre viejo lleva dentro la cifra que caduco.
**Mover una etiqueta que un acta cerrada nombra es una decision de alcance**, y
la tomo yo.

**`D.4`. EL ESPERADO COMPUTADO DEL CASO A RECOMPONE EL FILTRO DE LA FUNCION
BAJO PRUEBA.** `esperadas` se computa con la via directa sobre la nomina real,
y `nomina_invisible_al_censo()` hace lo mismo por dentro. **Se puede leer como
re implementacion del sujeto**, y entonces el caso probaria menos de lo que
parece. **Mi razon es que sigue cazando el orden, la nomina por defecto y
cualquier entrada que la funcion se coma**, y que el caso hermano, el de los dos
ficheros DENTRO del conjunto, es el que no envejece.

**`D.5`. LA RELECTURA AL DOBLE ENCONTRO UNA LESION EXACTA Y NO HICE NADA CON
ELLA.** Es el puesto **3.141**, y **es un VECINO, no del tramo de la ciega**.
El encargo dice *"ninguna clase se vuelve a decidir"*, asi que **no la toque** y
la dejo nombrada con su motivo en su salida. **Pero una lesion encontrada y no
registrada se puede perder**, y no se si le tocaba entrada propia.

**`D.6`. METI EL ARNES DE LA 1.c EN LA NOMINA DE LA BATERIA QUE LO ESTRENA.**
Corrio en el **TRAMO 9** de su propia bateria, el mismo dia que nacio. **La
regla me ampara** (acta 176 punto 7.2, reconfirmada por la `5.6` del acta 184)
y la medicion la respalda: sin el, `arneses_que_faltan()` daba **1** y los cinco
tramos que quedaban habrian cerrado en rojo. **Pero es la misma especie que la
`PD.3` del reporte de la 183 dejo abierta**, y hoy vuelve a pasar.

**`D.7`. ANEXE LOS DISCUTIBLES A LA TAREA 2 EN VEZ DE A LA SECCION 5.** La
seccion 5 no existe en este reporte porque el cierre cayo en rojo. **Preferi
que los discutibles existieran en un sitio raro a que no existieran**, pero
**es una sede que ninguna regla nombra**, y quien busque la seccion 5 no los va
a encontrar donde toca.

#### PENDIENTES DE DOCTRINA

**`PD.1` SIGUE ABIERTA Y NO LA TOCO:** las cinco `D` con el diferenciador ya
presente el dia del veredicto. Registrada y sin resolver desde el acta 182.

**`PD.2` NUEVA. EL CALIBRE DE UN TRAMO EN ROJO.** `AUDITOR.md` 6.1 define
*mismo calibre* por la **hondura** y el encargo de esta vuelta lo aplico al
**resultado**. Las dos lecturas son defendibles y llevan a sitios opuestos.
**Aplique la primera** y lo marque en la `D.1`. **No hay regla escrita que
elija.**

**`PD.3` NUEVA. UNA BATERIA QUE CRUZA DOS VUELTAS NO TIENE NOMBRE.** El
lanzador computa el numero de su propio fichero (bien), la bateria empezo en la
183 y acabo en la 184 (bien), y `cerrar_reporte.py` exige que la seccion 9 no
traiga una corrida de otra vuelta (bien). **Las tres reglas son buenas por
separado y juntas impiden cerrar el reporte.** Es la PARADA de arriba, dicha
como doctrina.

**`PD.4` NUEVA. UN ARNES QUE SE ESTRENA DENTRO DE LA BATERIA QUE LO ESTRENA.**
Heredada del reporte de la 183 y **hoy con consecuencia medida**: el arnes que
hizo caer el tramo 9 **no aparece en ninguna salida de bateria anterior a la de
hoy**. **Su primera bateria de verdad es esta, y en ella cayo.** Es lo que el
acta 184 anoto en su `5.6` sin convertirlo en regla.

#### MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**`C.1`. PUBLIQUE DOS SALIDAS DE ARNES CON EL DENOMINADOR VENCIDO Y HUBO QUE
RE CORRERLAS.** Corri los arneses de la 1.b y de la 1.c **antes** de meter el
nuevo en la nomina, o sea con la nomina en **112**, y sus salidas quedaron
escritas en disco con ese denominador. Al subir la nomina a **113** hubo que
volver a correrlos para que sus cifras fueran las del cierre. **Es la misma
especie que la caida `E.1` del acta 184**, la estimacion publicada con una
nomina vencida, **y la cometi el mismo dia que escribia su remedio**. Lo que la
salvo fue re correr antes de commitear, no un instrumento.

**`C.2`. EL CLON DE LA RELECTURA CORRIO UNA VEZ CON UNA FRASE QUE SE
CONTRADECIA CON SU PROPIO TITULO.** Su salida decia *"publica el reparto y LA
UNICA discrepancia"* debajo de una cabecera que decia **TRES**. La cace
**releyendo la salida**, no un instrumento, y se regenero antes del commit.
**Ningun fichero commiteado la lleva, pero estuvo a una orden de llevarla.**

