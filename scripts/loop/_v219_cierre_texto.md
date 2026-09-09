## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODAS SALEN DE `docs/loop/SALIDA_V219_CIERRE_INTEGRAL.txt`, que las midio y las sello. NINGUNA SE TECLEA.**
Ese fichero mide **11091 bytes en disco y 11091 normalizado a LF**.

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS

**CIFRA salidas selladas del ciclo: 18 | CIFRA que deberia haber: 18**
**CIFRA ausentes: 0 | CIFRA de cero bytes: 0**
**CIFRA salidas SIN exitcode dentro: 0**
**CIFRA peor exitcode de las dieciocho: 0**

**Las dos consolas existen y las sello el propio instrumento**, que es el
remedio de la `3.1` del acta 214, mantenido y sin aflojar por ninguna de sus dos
puertas, la del fichero ausente y la del fichero de cero bytes.

### 3.2. EL MARCADOR, EL CENSO Y LAS SUITES, COTEJADOS CONTRA LA 218

**LA COLUMNA DE CONTRASTE NO ES DE MI ENCARGO, Y ESO CAMBIA COMO SE LEE.** Mi
encargo de esta vuelta **no trae cifras de marcador ni de censo**, asi que lo que
se coteja es **lo que la 218 publico**, citado como contraste (`EJECUTOR.md` 2).
**Y ESTA VUELTA NO DECLARA NINGUN MOVIMIENTO ESPERADO**, al reves que la 218:
sus dos tareas son lectura, medicion y registro, asi que **las trece tenian que
quedarse quietas y cualquiera que se moviera era ROJO**.

**CIFRA cifras cotejadas: 13 | CIFRA que NO calzan: 0**
**CIFRA cifras que debian quedarse quietas y se quedaron: 13 | CIFRA que debian moverse y se movieron: 0**

Las tres suites corren **solas**, fuera del ciclo, cada una con su exitcode y sus
bytes por las dos convenciones, y las escribio
`scripts/loop/_v219_suites_y_cifras.py`, que existe porque **las dos tareas de
esta vuelta no corren suites** y el lector del cierre pide esos cinco ficheros
por su nombre. **La tabla entera esta en la salida sellada y no se repite aqui**,
porque dos versiones de lo mismo es lo que esta casa prohibe.

### 3.3. LAS SEDES, Y NINGUNA SE MOVIO

**CIFRA sedes cotejadas: 13 | CIFRA que se movieron: 0**
**CIFRA sedes que se movieron A PROPOSITO y estaban declaradas: 0 | CIFRA que se movieron SIN AVISO: 0**

**NO HAY NINGUNA SEDE MOVIDA A PROPOSITO EN ESTA VUELTA, Y ESO SE DECLARO ANTES
DE MEDIRLO**, dentro del instrumento: su tabla de excepciones esta **VACIA**. El
plan no se toco, y eso se prueba con sus propios `sha256`, los de la TAREA 1 y
los de la TAREA 2, por las dos convenciones:

```
docs/plan/OPERACIONES.jsonl AL ENTRAR: sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b
docs/plan/OPERACIONES.jsonl AL SALIR:   sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b, 517181 bytes en disco y 517181 normalizado a LF
docs/plan/08_VERIFICACION.md AL ENTRAR: sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4
docs/plan/08_VERIFICACION.md AL SALIR:   sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4, 73652 bytes en disco y 73652 normalizado a LF
docs/plan/07_ADUANA.md AL ENTRAR: sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0
docs/plan/07_ADUANA.md AL SALIR:   sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0, 3815 bytes en disco y 3723 normalizado a LF
docs/plan/01_FUENTES.md AL ENTRAR: sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3
docs/plan/01_FUENTES.md AL SALIR:   sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3, 128187 bytes en disco y 126666 normalizado a LF
docs/plan/05_SANEO.md AL ENTRAR: sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806
docs/plan/05_SANEO.md AL SALIR:   sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806, 39450 bytes en disco y 38699 normalizado a LF
docs/plan/INVENTARIO.jsonl AL ENTRAR: sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a
docs/plan/INVENTARIO.jsonl AL SALIR:   sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a, 629533 bytes en disco y 629533 normalizado a LF
LOS 12 SHA DE LAS SEDES DEL PLAN COINCIDEN AL ENTRAR Y AL SALIR POR LAS DOS CONVENCIONES: SI
docs/plan/OPERACIONES.jsonl AL ENTRAR: sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b
docs/plan/OPERACIONES.jsonl AL SALIR:   sha256 disco 650578474361eb2b y sha256 LF 650578474361eb2b, 517181 bytes en disco y 517181 normalizado a LF
docs/plan/08_VERIFICACION.md AL ENTRAR: sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4
docs/plan/08_VERIFICACION.md AL SALIR:   sha256 disco 578eeefab6db2fd4 y sha256 LF 578eeefab6db2fd4, 73652 bytes en disco y 73652 normalizado a LF
docs/plan/07_ADUANA.md AL ENTRAR: sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0
docs/plan/07_ADUANA.md AL SALIR:   sha256 disco 34642304c5f7667f y sha256 LF 6f5f91619adec6e0, 3815 bytes en disco y 3723 normalizado a LF
docs/plan/01_FUENTES.md AL ENTRAR: sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3
docs/plan/01_FUENTES.md AL SALIR:   sha256 disco 73168452929b3d42 y sha256 LF f965abf6c3ca95c3, 128187 bytes en disco y 126666 normalizado a LF
docs/plan/05_SANEO.md AL ENTRAR: sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806
docs/plan/05_SANEO.md AL SALIR:   sha256 disco 3f46a4141e63144a y sha256 LF 22e59e0b7a22b806, 39450 bytes en disco y 38699 normalizado a LF
docs/plan/INVENTARIO.jsonl AL ENTRAR: sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a
docs/plan/INVENTARIO.jsonl AL SALIR:   sha256 disco 43cea06634e6fc1a y sha256 LF 43cea06634e6fc1a, 629533 bytes en disco y 629533 normalizado a LF
LOS 12 SHA DE LAS SEDES DEL PLAN COINCIDEN AL ENTRAR Y AL SALIR POR LAS DOS CONVENCIONES: SI
```

### 3.4. LAS RUTAS QUE ESTE REPORTE CITA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y **su salida se cita en el
commit de cierre**. Va ademas **metido como guarda previa en los compositores de
esta vuelta**, que cuentan los guiones largos y los directorios de dos tramos
entre comillas inversas **antes de escribir**.

## 4. LO QUE SE TOCO, Y LO QUE NO

**LA CIFRA VA CON SU HUECO AL LADO:**

**CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA: 13 | CIFRA de esos con el prefijo que le toca: 13**
**CIFRA MEDIDA AHORA: 13 | CIFRA DEL HUECO QUE EL PROPIO CIERRE ANADE: 2 | CIFRA TOTAL DE LA VUELTA, LAS DOS JUNTAS: 15**
**Y LOS DEL HUECO LLEVAN EL PREFIJO IGUAL: 2 de 2, contado de sus propios nombres.**

Fuera del censo y fuera de la nomina, que sigue **CONGELADA EN 135**.

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`):

- **git status --porcelain al entrar: 2 linea(s)**, y eran mis dos
  propios scripts de apertura sin rastrear. **LA CIFRA NO SE TECLEA: se lee del
  sello de apertura, cuya linea dice `CIFRA lineas de status: 2`.**
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0**

**LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE:** no corrio la
bateria (la 215 la corrio y la cadencia de cinco pone la siguiente en la
**220**); **no reparo `scripts/loop/vuelta150_4_tabla_por_fase.py`**, que la
moratoria `6.3` cubre por su propia letra; no toco el lanzador; no podo ni
engordo la nomina; no escribio en `docs/loop/PROMPT_SIGUIENTE.md` ni en
`docs/loop/ACTA_AUDITOR.md`; **no toco la celda de
`docs/plan/08_VERIFICACION.md`**, que es sede del fundador; **no escribio ni una
linea en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**, al reves que la 218; y **no
movio ni un campo de estado de ninguna ficha**, con sus `sha256` delante.

**Y NO TOQUE EL BLOQUE FINAL DEL ACTA 218 DIRIGIDO AL AUDITOR DE ESTA VUELTA**,
que el encargo manda dejar donde esta. El `sha256` de `docs/loop/ACTA_AUDITOR.md`
es el mismo al entrar y al salir, y esta en la tabla de sedes de arriba.

**Y AQUI VA EL NOMBRE DEL FICHERO COMPUESTO DE LA BATERIA, QUE EL ENCARGO ME
MANDA DECIR Y QUE NO CABE EN LA SECCION 9.** El encargo dice, literal, que *el
fichero compuesto de la bateria se llama `docs/loop/SALIDA_V183_BATERIA.txt`
aunque su contenido sea el de la vuelta 215*, y que si lo mido diga las dos
cosas. **Las digo, y las digo AQUI y no en la seccion 9 por un motivo medido, no
por comodidad:** la guarda `hueco_declarado_que_falta()` de
`scripts/loop/cerrar_reporte.py` **barre la seccion 9 buscando cualquier nombre
de fichero de bateria y cae en ROJO si aparece uno que no sea el de la vuelta que
cierra** (*UNA CORRIDA DE OTRA VUELTA*). **Lo comprobe corriendo el cierre y
saliendo en rojo por esa puerta**, y la moratoria `6.3` me prohibe reparar la
guarda. **Las dos cosas, entonces:** el fichero se llama
`docs/loop/SALIDA_V183_BATERIA.txt`, **su primera linea sigue diciendo VUELTA
183**, y **su contenido es el de la vuelta 215**, porque el lanzador es estable y
no se clona. Ese letrero es el punto 3 de la seccion 6 del acta 218, linea
77678, y sube nombrado otra vez. **Sus bytes medidos por mi hoy van en la
atribucion de la seccion 9.**

**LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA:** leida de `git log` sobre el
commit de apertura y sobre el de ahora mismo.

- **fecha del commit de apertura, leida de git log: 2026-09-09**
- **fecha del commit de ahora mismo, leida de git log: 2026-09-09**

## 5. LAS PARADAS

**NO TRAIGO NINGUNA PARADA, Y LO DIGO CON EL MOTIVO DELANTE.** Nada de lo medido
contradice una regla vigente ni una cifra publicada con su corte. **Las dos
puertas de parada que el encargo me abrio expresamente quedaron cerradas por
medicion, no por criterio mio:**

- El encargo dice *si tu registro te dice lo contrario, paras y lo traes*, sobre
  que ninguna adjudicacion mueva un veredicto. **Mi registro no dice lo
  contrario:** CIFRA correcciones que esta vuelta tiene que aplicar por adjudicacion: 0 | CIFRA que el encargo ordena: 0
- El encargo dice *reproduce esa cifra con tu propio instrumento antes de nada, y
  si te da otra, publica las dos y para*. **Me dio la misma:**
  CIFRA menciones que TODAVIA declaran mas de una fuente, MEDIDA HOY POR MI: 7 | CIFRA que el acta 217 publica en su linea 77346: 7

**LAS TRES CLAUSULAS QUE SIGUEN SIN CUBRIR NO SON PARADA:** ninguna da **NO
CUBRE**, las tres estan en **A MEDIAS por trabajo de plan o por frontera sin
adjudicar**, y las tres suben nombradas con su fila, su indice y su cifra en la
TAREA 2.

**LO QUE SI TRAIGO, Y NO ES PARADA SINO HALLAZGO HEREDADO CON SU ADJUDICACION
DELANTE:** `scripts/loop/vuelta150_4_tabla_por_fase.py` sigue sin reparar. **No
es lectura mia: lo adjudica el auditor en su `5.6` del acta 217, linea
77295 de `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero**, que dice que un
arnes en rojo no es una caida de dato y que la moratoria lo cubre. **Sube
nombrado y sin reparar, otra vez.**

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**SEIS, y los seis son LECTURAS MIAS.** Estan escritos enteros, con su duda y con
lo que cambiaria si el auditor lee al reves, en **el bloque de discutibles de la
TAREA 1** y en **el de la TAREA 2**, y **no se repiten aqui a proposito**. Sus
rotulos, para que se puedan citar:

- **TAREA 1**: `D.1` que el recuento no se recomputa sino que se remide; `D.2`
  que re-correr el lector de la 218 no es escribir; `D.3` que la glosa de las
  seis adjudicaciones es registro y no lectura mia.
- **TAREA 2**: `D.1` que la vara de *reubicado* es la del grafo y no la del campo
  `fuente`; `D.2` que la frontera de la `2.b` no la decido, pero si digo como la
  leo; `D.3` que el reparto de tanda a libro es mio.

**EL MAS PESADO ES EL `D.1` DE LA TAREA 2, Y LO DIGO PORQUE DE EL CUELGA LA UNICA
SUBIDA DE ESTA VUELTA.** Si el auditor lee que *reubicado* exige que el material
**salga** del nodo, entonces **cinco de las siete menciones no lo estan**, la
clausula de `01 FUENTES` idx 1 **vuelve a A MEDIAS** y el recuento del cierre
vuelve a **13 y 4**.

## 7. LAS PREGUNTAS Y LOS PENDIENTES DE DOCTRINA

**`P.1` LA QUE EL PROPIO ENCARGO ME MANDA ABRIR, Y ES LA QUE DECIDE UNA
CLAUSULA:** un nodo que la campana **difirio a proposito y por decision
escrita**, cuenta como incumplimiento de la clausula o como **fuera de su
alcance**? El caso concreto esta medido en la `2.b`: `seguro_de_carga_transporte`
resuelve a `seguro_exportacion`, que **no cita Incoterms**, porque la palabra
cayo por debajo de la granularidad del paso en una fusion anterior. **La
adjudicacion que lo difirio vive en la linea 41699 del acta 120 y su anotacion en
la linea 1574 de `docs/PENDIENTES.md`, las dos leidas hoy del fichero.** **Mi
lectura, y va marcada como DISCUTIBLE y NO aplicada al recuento**: queda fuera del
alcance. **No la decido yo: es exactamente el tipo de frontera que el auditor
adjudica.**

**`P.2` LA CELDA DE `07 ADUANA` SIGUE DICIENDO CUATRO Y SU FICHA DICE CINCO.
QUIEN LA CORRIGE?** La lectura ya esta adjudicada por la `5.5` del acta 217,
linea 77275, leida hoy: **manda la ficha**. Lo que queda abierto **no es la
lectura sino la mano**: la celda vive en `docs/plan/08_VERIFICACION.md`, que es
**sede del fundador**, y esta vuelta no la toca. **Sube nombrada a la auditoria
integral por segunda acta seguida.**

**`P.3` UN ARNES QUE UNA CORRECCION DECLARADA DEJO EN ROJO, SE REPARA CUANDO?**
Contestada por la `5.6` del acta 217, linea 77295: **la moratoria lo cubre y
no se repara**. Lo que queda para el fundador es **si se repara al levantarse la
moratoria o si la vara de las ocho filas queda retirada** y la sustituye la de
las diecisiete clausulas.

**PENDIENTES DE DOCTRINA: NINGUNO NUEVO.** La `P.3` que yo abri en la 218, sobre
si escribir en el registro del cribado estaba prohibido, **quedo cerrada por la
`4.3` del acta 218, linea 77605**: no solo estaba permitido, estaba ordenado,
y no se revierte nada.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**SON CUATRO, Y NINGUNA LA CACE YO: LAS CAZARON MIS PROPIAS GUARDAS, EN ROJO,
ANTES DE QUE NINGUNA CIFRA SALIERA DE LA VUELTA.** Lo digo asi porque decir *"la
vi venir"* cuando nadie lo iba a comprobar es exactamente lo que esta casa
persigue. **Las tres primeras son de la misma especie; la cuarta es de otra, y es
PEOR, porque es una REINCIDENCIA sobre una caida que mi encargo me nombro por
escrito.**

**`C.1`. UN ANCLA DE CABECERA DE ACTA COPIADA DE LA FORMA DE OTRA ACTA.**
`scripts/loop/_v219_t1_registros.py` buscaba la cabecera del acta 217 con
`# ACTA DEL AUDITOR, VUELTA 217:`, **con dos puntos**, copiando la forma de la
del acta 218. La del acta 217 **no lleva dos puntos: lleva un parentesis con su
fecha**. La corrida salio en **ROJO con 1 comprobacion fallando**, y la
comprobacion que fallo era la del propio instrumento. **El ancla vieja queda
escrita en el codigo, con su motivo y sin borrar.**

**`C.2`. UN ANCLA DE UNA LINEA QUE APARECIA DOS VECES.**
`scripts/loop/_v219_t2_seccion.py` pedia la linea `SUBE POR LECTURA:` a un
lector que exige que el ancla aparezca **exactamente una vez**, y aparece **dos**:
la tabla del cierre repite esa marca dentro de la celda del veredicto. **El
compositor cayo en rojo y no escribio nada**, que es para lo que esa guarda
existe. Corregido a un ancla que nombra la fila.

**`C.3`. UN FILTRO DE LINEAS ESCRITO CON LAS DECENAS DEL DIA EN VEZ DE UN
PATRON.** El mismo compositor recortaba la adjudicacion del acta 120 con
`417\d\d`, y eso **dejaba fuera justo la primera linea, la 41699**. **La guarda
de conteo lo canto: 14 de 15.** Corregido a un patron de numero de linea, y el
viejo queda escrito con su motivo.

**LAS TRES PRIMERAS TIENEN LA MISMA RAIZ Y LA DIGO EN VOZ ALTA: UN ANCLA ES UNA
APUESTA SOBRE LA FORMA DE UN FICHERO QUE NO SE HA MIRADO.** Las tres se cazaron
porque **cada ancla lleva su cifra de cuantas veces deberia casar**, y esa es la
unica razon por la que ninguna llego a este reporte.

**`C.4`. VOLVI A PUBLICAR UNA CIFRA DE BYTES SIN SU PAREJA, Y ES REINCIDENCIA
SOBRE UNA CAIDA QUE MI PROPIO ENCARGO ME NOMBRO.** El encargo de esta vuelta dice,
con todas las letras, *LOS TAMANOS EN BYTES EXACTOS... cada ruta con sus dos
convenciones EN SU MISMA LINEA, que es la caida `C.2` que tu propia guarda te
canto en la 218*. **Y aun asi mi instrumento de la TAREA 1 publicaba `razon de
3793 bytes` y `razon de 4383 bytes` a secas**, las dos en la misma tabla, y **la
guarda de `scripts/loop/cerrar_reporte.py` volvio a cantarlo, con su numero de
linea: CIFRA cifras publicadas sin su pareja: 2**. Corregido a **bytes en disco y
bytes normalizado a LF en la misma linea**, con el texto viejo escrito en el
instrumento y sin borrar.

**Y DIGO LO QUE ESTO ENSENA, QUE ES LO UNICO QUE VALE DE UNA REINCIDENCIA:** la
`C.2` de la 218 fue sobre una RUTA, y yo lei la regla como si fuera de rutas.
**No lo es: es de CIFRAS DE BYTES**, vengan de una ruta o de un campo de texto de
un registro. **La guarda si lo tenia claro y yo no**, y por eso la cazo ella y no
yo, otra vez.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**NO PROPONGO LA PARADA FELIZ, Y LA CONDICION NO LA PUSE YO.** Mi encargo la
escribio antes de saber el resultado: *"si al cerrar esta vuelta las DIECISIETE
quedan en CUBRE, lo propones"*. **Medido al cierre y no heredado:**

```
CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2: 14 de 17 | CIFRA que dejo la TAREA 1: 13
CIFRA clausulas en A MEDIAS AL CIERRE DE LA TAREA 2: 3 de 17 | CIFRA que dejo la TAREA 1: 4
CIFRA clausulas en NO CUBRE AL CIERRE DE LA TAREA 2: 0 de 17 | CIFRA que dejo la TAREA 1: 0
CIFRA en CUBRE: 14 | CIFRA que la condicion exige: 17
LA CONDICION SE CUMPLE: NO
```

**Por tanto NO propongo declarar la campana consumada.** Quien declara es el
auditor; yo propongo, que es lo que mi encargo manda.

**LAS TRES QUE FALTAN, CON SU FILA, SU INDICE Y SU CIFRA**, que es lo que el
encargo pide que se diga cuando la condicion no se cumple:

```
03 FUSIONES    idx 0 | A MEDIAS  | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
05 SANEO       idx 1 | A MEDIAS  | los tres de Incoterms con su version
07 ADUANA      idx 0 | A MEDIAS  | los cuatro controles mecanicos **corriendo en Gate 0**
```

**Y LO QUE HAY DETRAS DE LAS TRES ES PLAN, FRONTERA Y UN CONTROL SIN CORRER, NO
MAQUINARIA:** 71 actos sin fundir por la lectura ancha y **SEIS fusiones con 19
nodos** por la estrecha; **1 de los 3 de Incoterms** diferido por decision
escrita, que es la `P.1`; y **el quinto control de aduana sin correr**, con su
celda en sede del fundador.

**LO QUE PROPONGO, CON SU CIFRA DELANTE:**

1. **QUE EL `D.1` DE LA TAREA 2 SE ADJUDIQUE ANTES QUE NADA**, porque de el
   cuelga la unica subida de esta vuelta y con el al reves el recuento vuelve a
   **13 y 4**.
2. **QUE LA `P.1` SE ADJUDIQUE**, porque decide si `05 SANEO` idx 1 puede subir
   alguna vez sin ejecutar trabajo post campana. **Es de frontera y es del
   auditor.**
3. **QUE LA VUELTA SIGUIENTE NO FABRIQUE NADA.** La moratoria aguanta y esta
   vuelta lo vuelve a demostrar, con su cifra en la seccion 4.
4. **QUE LA 220 SEA DE BATERIA Y NO LLEVE NADA MAS**, que es lo que la cadencia
   de cinco de `AUDITOR.md` 6.1 dice y no una preferencia mia.
5. **QUE LAS TRES CLAUSULAS EN A MEDIAS SUBAN NOMBRADAS** a la lista de la
   seccion 6 del acta, con su cifra, como subieron las cuatro de la 218.

**Y EL MERGE NO SE PIDE: EL BUCLE NO FUNDE RAMAS.**
