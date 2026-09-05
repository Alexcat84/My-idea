## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**Todo hash de esta seccion sale de `git log` o `git rev-parse` corrido en esta
vuelta** (`EJECUTOR.md` 1, LA IDENTIDAD SE LEE DE GIT).

| | |
|---|---|
| rama | `pasada-unica` |
| sello de apertura, escrito ANTES de la 1.a operacion | `77621a68` (`SALIDA_V178_HEAD_APERTURA.txt`) |
| sello de cierre, escrito TRAS la ultima operacion | `38143ebe` (`SALIDA_V178_HEAD_CIERRE.txt`) |
| commits entre los dos sellos | **7** |
| rutas tocadas | **65** (`docs/loop/` 35, `scripts/loop/` 29, `docs/plan/` 1) |
| **el grafo entre los dos sellos** | **`git diff --numstat` sobre `dataset/`, `web/` y `engine/`: 0 filas** |

**LOS SIETE COMMITS, EN SU ORDEN:**

| hash | que cierra |
|---|---|
| `531efee1` | el bloque de apertura, corrido antes de la primera operacion, y el desfase del calibrado DENTRO de el |
| `72126b30` | el esqueleto del reporte, abierto al empezar con sus CINCO filas vacias |
| `09e5c4b4` | TAREA 1, los registros y las correcciones (bloqueante) |
| `3c22f94a` | TAREA 2, `OP-L-03` re-medido entero |
| `9c690d2d` | TAREA 3, los triangulos anotados con su regla |
| `e56a1dff` | TAREA 4, la columna `CONSUMIDA` de la vara |
| `38143ebe` | TAREA 5, lo que no entra y no se pierde |

Los commits posteriores a `38143ebe` son **el cierre de este reporte y su
archivado**, y por eso no estan en la cuenta de arriba: el sello de cierre se
escribe antes que ellos y no puede nombrarlos.

**EL MARCADOR, RECOMPUTADO AL CIERRE Y NO HEREDADO DE LA APERTURA**
(`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE):

| | total | A | B | C | D |
|---|---:|---:|---:|---:|---:|
| **marcador al cierre** | **3.388** | **551** | **72** | **5** | **2.760** |

Puestos de **1 a 3.388**, **0 huecos** y **0 duplicados**. **Identico al de la
177**, y esa es la cifra que las TAREAS 2 y 3 prometian no mover.

**GATE 0, EL CICLO ENTERO Y EN SU ORDEN, EN LAS DOS PUNTAS**, nunca `run_phase1`
suelto:

| paso | apertura | cierre |
|---|---|---|
| `run_phase1.py --reaplico-curaduria` | **GATE 0: OK**, exit 0 | **GATE 0: OK**, exit 0 |
| `etiquetas_de_cara.py --aplicar` | corrido, exit 0 | corrido, exit 0 |
| `sync_assets_web.py` | corrido, exit 0 | corrido, exit 0 |
| `git diff HEAD --numstat -- dataset/ web/ engine/` | **0 filas** | **0 filas** |
| `engine/run_all_tests.py` | **25/25** | **25/25** |
| `npx tsc --noEmit` | **exit 0, cero lineas** | **exit 0, cero lineas** |
| `pnpm test` | **82 (82) / 1.040 (1.040)** | **82 (82) / 1.040 (1.040)** |

**Y EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA, QUE ES LA CAIDA PROPIA QUE
LA 177 SE ANOTO Y QUE DESDE ESTA VUELTA ACUMULA.** El medidor corre DENTRO de
`scripts/loop/vuelta178_apertura.py`, antes de la primera operacion. Las dos
salidas, la de apertura y la de cierre, son **identicas byte a byte**: **505
bytes en disco y 498 bytes normalizados a LF** cada una, sha256 en disco
`9c1a246654108251` y sha256 normalizado a LF `7d683eea4700f18b` **las dos**. La
salida del conteo de aristas tambien sale identica en las dos puntas.

## 4. LA GUARDA DEL COMMIT, CORRIDA EN CADA COMMIT DE ESTA VUELTA

`scripts/loop/guarda_commit_dataset.py` salio **VERDE antes de cada uno de los
siete commits**, con **0 filas de `git diff --numstat -- dataset/`**, **0 ficheros
nombrados por `git status --porcelain -- dataset/`** y **0 blobs de arbol
divergentes de HEAD**. **`dataset/` no se toco en ninguna de las cinco tareas**, y
eso no es una promesa: es la cifra que la guarda imprime.

**Y NINGUNA TAREA ESCRIBIO EN LOS TRES FICHEROS QUE LA CAMPANA RESERVA.**
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` sale con el mismo sha256 normalizado a LF
antes y despues de la TAREA 3, comprobado por el propio instrumento;
`docs/plan/OPERACIONES.jsonl` y `scripts/loop/backlog_l03_vuelta14.py` salen con
`git diff --stat` **vacio**.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` LA VARA DEL CENSO EN 148 ES UNA ELECCION, Y LA MARCO.** El encargo dice
"menos los anteriores a la vara del censo" y no dice cual es la vara. Elegi **148**
porque es el unico numero con motivo escrito y citable: la letra de entrada en la
nomina es "desde la vuelta 148" y `vuelta164_tarea5_medir_pre148.py` midio lo
anterior con `CORTE = 148` y lo adjudico fuera. **Lo discutible es que con la vara
en 177 (o sea "la ultima de la nomina", con `>=` en vez de `>`) el resultado de
hoy seria CERO y no habria destapado nada**, y eso tambien encajaria con la frase
"es exactamente lo que tu hiciste a mano". **Elegi la lectura que destapa, no la
que calla**, y puede que el auditor prefiera la otra.

**`D.2` NO CABLEE LA GUARDA DEL SUJETO CONGELADO AL ROJO GLOBAL DE LA BATERIA.**
La guarda existe, corre sola y cae en rojo en su propio carril con **15 de 92**.
Cablearla pondria la bateria de la 181 en rojo por quince entradas cuyo estado
real hay que juzgar una a una. **Lo discutible es si "entra aqui y no se aplaza
otra vez" exigia el cableado y no solo el instrumento.**

**`D.3` LAS HUELLAS DE LA GUARDA DEL SUJETO CONGELADO SON MIAS Y NO SALEN DE
NINGUNA REGLA ESCRITA.** `SUJETO_FIJO`, `tempfile`, `mkdtemp`, `deepcopy`, `git
show`, `cat-file`, `sha256` y el literal `SUJETO CONGELADO` para el lado
congelado; los cinco ficheros vivos de la campana para el otro. **Son una lista
que yo compuse mirando lo que la nomina ya hace**, no una vara adjudicada, y por
eso los 8 `NO DECIDIBLE` pueden ser mas o menos con otra lista.

**`D.4` EL ROJO POR `--excluir` DE UN PUESTO INEXISTENTE LO ESTIRE YO.** El
encargo dice "CAE EN ROJO si un puesto PEDIDO no existe". Lo aplique tambien a
`--excluir`, con su motivo escrito en el fichero (el universo de los dos es el
mismo archivo). **Es una lectura ancha y la marco.**

**`D.5` EL AST DEL PAR DEL ACTA 176 SALE DIFIERE, ASI QUE EL CUARTO VEREDICTO NO
EXONERA SOLO EN ESE PAR.** Lo que exonera es la fila de los tipos de nodo, que
empatan exactamente (1.368 contra 1.368, 0 tipos distintos). **Lo traigo tal cual
en vez de redondearlo a "AST identico".**

**`D.6` LOS 24 LADOS `SIN MARCA DE NINGUNA DE LAS DOS` DE LA TAREA 3.** La mitad
de los lados de los triangulos no trae en su razon ninguna marca literal de
ninguna de las dos reglas. **Los declaro asi en vez de asignarles una a ojo**,
pero puede que el auditor considere que la anotacion queda a medias sin ellos.

## 6. LAS PREGUNTAS

**`P.1` LOS DOS ARNESES QUE LA VARA DEL CENSO DESTAPA: ¿ENTRAN EN LA NOMINA?**
`vuelta150_2d_simular_op_c_05.py` y `vuelta160_tarea3b_caso_positivo.py` estan en
el censo, no estan en la nomina y no son anteriores a la vara. Corridos hoy: **exit
0 los dos, 0 filas de numstat sobre `dataset/`**. La regla escrita desde la 148
dice que un arnes entra en la nomina. **No los meti porque eso decide lo que la
181 corre.** Mientras no entren, **la bateria de la 181 dara ROJO por esta cuenta,
y ese rojo sera correcto.**

**`P.2` ¿SE CABLEA LA GUARDA DEL SUJETO CONGELADO AL ROJO DE LA BATERIA, Y CUANDO?**
Con las cifras de hoy (75 congeladas, 2 casos declarados, 7 sujeto vivo, 8 no
decidibles) cablearla es un rojo de 15 entradas de golpe.

**`P.3` ¿LA CIFRA DE TRIANGULOS QUE VALE ES NUEVE O CINCO?** Sobre los mismos tres
actos, la 177 conto cinco y el instrumento cuenta nueve. **Publico las dos y no
resuelvo copiando.**

**`P.4` ¿QUE SE HACE CON LOS SIETE TRIANGULOS DE LOS ACTOS SIN LEER?** Estan
anotados con su regla y ninguno se toca. **Bloquean la fusion de cinco actos mas
por `P.10`**, y eso cambia lo que queda de `OP-L-03` mas todavia que la cifra de
pares.

## 7. PENDIENTES DE DOCTRINA

**`PD.1` LA CONVENCION DE BYTES, POR QUINTA ACTA.** Sigue sin fijar y es del
fundador. Lo que si esta adjudicado (acta 177, 7.11) ya es instrumento desde esta
vuelta: `cerrar_reporte.py` cae en rojo si el reporte publica una cifra de bytes o
un sha sin su pareja. **Y la guarda cazo a su autor en su primera corrida:
encontro CUATRO cifras sin pareja en este mismo reporte, las cuatro mias**, y
estan corregidas en `scripts/loop/_v178_arreglo_parejas.py`, que arregla el
borrador y el reporte a la vez para que no diverjan.

**`PD.2` LA REGLA DEL SUJETO CONGELADO YA TIENE INSTRUMENTO, PERO NO TIENE VARA
ADJUDICADA.** Las huellas con las que clasifica son mias (ver `D.3`). **Lo que
falta ya no es el instrumento, es la lista.**

**`PD.3` QUE CUENTA COMO "PAR" EN `OP-L-03`: EL ESCRITO O EL RESUELTO.** Esta
vuelta cambio la cuenta a **pares RESUELTOS distintos**, y eso mueve la cifra de la
177 de 9 a 8. **La regla no esta escrita en ningun sitio**: la deduje de que la
pregunta es "cuantas lecturas quedan".

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**`C.1` LA CIFRA DE TRIANGULOS DE LA 177 SE QUEDO CORTA, Y ES DE METODO.** Publique
CINCO y sobre los mismos tres actos hay NUEVE. **Mire los triangulos que tocaban
los pares que estaba leyendo en vez de enumerar todas las ternas del acto.** Los
cinco que nombre son correctos; los cuatro que faltan son reales.

**`C.2` LA CUENTA DE PARES REALES DE LA 177 CONTABA PARES ESCRITOS.** Publique 9 y
hoy salen 8, porque una pareja de `estrategia_de_innovacion_arenas` era la misma
una vez resuelta. **El registro de la 177 no se retoca**: dice lo que midio.

**`C.3` MIS DOS INSTRUMENTOS NUEVOS SALIERON CON UN DEFECTO CADA UNO, Y LOS CAZARON
SUS PROPIOS ARNESES EN LA PRIMERA CORRIDA.** `backlog_l03_resuelto.py` contaba
pares escritos y no resueltos, o sea inflaba por el mismo mecanismo que venia a
desinflar; y la columna `CONSUMIDA` buscaba la atribucion en la PRIMERA ventana de
la nota y devolvia vacio teniendo `OP-U-01` escrito unos cientos de caracteres mas
abajo. **En los dos se arreglo el instrumento y no el esperado del arnes.** Lo
cuento como caida mia porque los dos defectos salieron de mi mano, y lo cuento con
alegria porque los dos casos rojos funcionaron.

**`C.4` CINCO CIFRAS SIN PAREJA EN ESTE MISMO REPORTE, Y LA QUINTA LA ESCRIBIA LA
PROPIA GUARDA.** La guarda de la TAREA 1.e encontro CUATRO en el cuerpo, todas
mias, antes del cierre; estan corregidas en
`scripts/loop/_v178_arreglo_parejas.py`, que arregla el borrador y el reporte a la
vez para que no diverjan. **Y en la primera corrida de `cerrar_reporte.py` la
guarda cazo una QUINTA que no era del cuerpo: la escribia el generador de la
seccion 9 de ese mismo fichero**, que partia "N bytes en disco" y "N bytes
normalizados a LF" en dos lineas. **Una guarda que se estrena cazando a su autor
DOS VECES, la segunda dentro del instrumento que la lleva**, y por eso el cierre
de esta vuelta salio ROJO la primera vez y hubo que arreglar el generador antes de
volver a correrlo. Se arreglo el generador, no la guarda.
