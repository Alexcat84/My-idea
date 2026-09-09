## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODAS SALEN DE `docs/loop/SALIDA_V218_CIERRE_INTEGRAL.txt`, que las midio y las sello. NINGUNA SE TECLEA.**

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS

**CIFRA salidas selladas del ciclo: 18 | CIFRA que deberia haber: 18**
**CIFRA ausentes: 0 | CIFRA de cero bytes: 0**
**CIFRA salidas SIN exitcode dentro: 0**
**CIFRA peor exitcode de las dieciocho: 0**

**Las dos consolas existen y las sello el propio instrumento**, que es el
remedio de la `3.1` del acta 214, mantenido y sin aflojar por ninguna de sus dos
puertas, la del fichero ausente y la del fichero de cero bytes.

### 3.2. EL MARCADOR, EL CENSO Y LAS SUITES, COTEJADOS CONTRA LA 217

**LA COLUMNA DE CONTRASTE NO ES DE MI ENCARGO, Y ESO CAMBIA COMO SE LEE.** Mi
encargo de esta vuelta **no trae cifras de marcador ni de censo**, asi que lo que
se cotea es **lo que la 217 publico**, citado como contraste (`EJECUTOR.md` 2). Y
**DOS de esas cifras TENIAN que moverse**, porque la TAREA 1.c las movio a
proposito: **las dos van escritas con su movimiento ANTES de medirlas**, y no
moverse habria sido rojo igual que moverse las otras.

**CIFRA cifras cotejadas: 13 | CIFRA que NO calzan: 0**
**CIFRA cifras que debian quedarse quietas y se quedaron: 11 | CIFRA que debian moverse y se movieron: 2**

Las tres suites corren **solas**, fuera del ciclo, cada una con su exitcode y sus
bytes por las dos convenciones. **La tabla entera esta en la salida sellada y no
se repite aqui**, porque dos versiones de lo mismo es lo que esta casa prohibe.

### 3.3. LAS SEDES, Y LA UNICA QUE SE MOVIO, DECLARADA ANTES DE MEDIRLA

**CIFRA sedes cotejadas: 13 | CIFRA que se movieron: 1**
**CIFRA sedes que se movieron A PROPOSITO y estaban declaradas: 1 | CIFRA que se movieron SIN AVISO: 0**

**LA QUE SE MOVIO ES `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, Y NO ES UN DESCUIDO:
ES LA TAREA 1.c.** Su motivo se escribio **dentro del instrumento y antes de
medir**, no despues de ver el resultado. **El plan no se toco**, y eso se prueba
con sus propios `sha256`, los de la TAREA 1 y los de la TAREA 2:

```
SHA256 DE docs/plan/OPERACIONES.jsonl AL ENTRAR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/OPERACIONES.jsonl AL SALIR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/08_VERIFICACION.md AL ENTRAR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
SHA256 DE docs/plan/08_VERIFICACION.md AL SALIR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
LOS SEIS SHA DEL PLAN COINCIDEN CON LOS DE LA ENTRADA: SI
LOS OCHO SHA DEL PLAN COINCIDEN CON LOS DE LA ENTRADA: SI
```

### 3.4. LAS RUTAS QUE ESTE REPORTE CITA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y **su salida se cita en el
commit de cierre**. Va ademas **metido como guarda previa en los cuatro
compositores de esta vuelta**, que cuentan los guiones largos y los directorios
de dos tramos entre comillas inversas **antes de escribir**.

## 4. LO QUE SE TOCO, Y LO QUE NO

**LA CIFRA VA CON SU HUECO AL LADO:**

**CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA: 10 | CIFRA de esos con el prefijo que le toca: 10**
**CIFRA MEDIDA AHORA: 10 | CIFRA DEL HUECO QUE EL PROPIO CIERRE ANADE: 2 | CIFRA TOTAL DE LA VUELTA, LAS DOS JUNTAS: 12**
**Y LOS DEL HUECO LLEVAN EL PREFIJO IGUAL: 2 de 2, contado de sus propios nombres.**

Fuera del censo y fuera de la nomina, que sigue **CONGELADA EN 135**.

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`):

- **`git status --porcelain` al entrar: 1 linea(s)**, y era mi
  propio script de apertura sin rastrear. **LA CIFRA NO SE TECLEA: se lee de
  la linea `CIFRA lineas de status: 1` del sello de apertura.**
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0**

**LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE:** no corrio la
bateria (la 215 la corrio y la cadencia de cinco pone la siguiente en la
**220**); **no reparo `scripts/loop/vuelta150_4_tabla_por_fase.py`**, que el
encargo verifico en rojo y que la moratoria `6.3` cubre por su propia letra; no
toco el lanzador; no podo ni engordo la nomina; no escribio en
`docs/loop/PROMPT_SIGUIENTE.md` ni en `docs/loop/ACTA_AUDITOR.md`; **no toco la
celda de `docs/plan/08_VERIFICACION.md`**, que es sede del fundador; y **no
movio ni un campo de estado de ninguna ficha**, con sus `sha256` delante.

**LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA:** leida de `git log` sobre el
commit de apertura y sobre el de ahora mismo.

- **fecha del commit de apertura, leida de git log: 2026-09-09**
- **fecha del commit de ahora mismo, leida de git log: 2026-09-09**

## 5. LAS PARADAS

**NO TRAIGO NINGUNA PARADA, Y LO DIGO CON EL MOTIVO DELANTE.** Nada de lo medido
contradice una regla vigente ni una cifra publicada con su corte.

**LAS CUATRO CLAUSULAS QUE SIGUEN SIN CUBRIR NO SON PARADA:** ninguna da **NO
CUBRE**, las cuatro estan en **A MEDIAS por trabajo de plan medido y nombrado**, y
las cuatro suben nombradas con su fila, su indice y su cifra en la TAREA 2.

**LO QUE SI TRAIGO, Y NO ES PARADA SINO HALLAZGO HEREDADO CON SU ADJUDICACION
DELANTE:** `scripts/loop/vuelta150_4_tabla_por_fase.py` sigue en rojo. **No lo
reparo, y esta vez no es lectura mia: lo adjudica el auditor en su `5.6` del acta
217, linea 77295 de `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero**, que
dice que un arnes en rojo no es una caida de dato y que la moratoria lo cubre.
**Sube nombrado y sin reparar, otra vez.**

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**SEIS, y los seis son LECTURAS MIAS.** Estan escritos enteros, con su duda y con
lo que cambiaria si el auditor lee al reves, en la **seccion `1.f` de la TAREA 1**
y en la **`2.e` de la TAREA 2**, y **no se repiten aqui a proposito**. Sus
rotulos, para que se puedan citar: **`D.1`** la clase que muevo de `B` a `D` en el
puesto 299, **`D.2`** la `D` del puesto 1249 que se sostiene con menos margen,
**`D.3`** el sitio donde escribo, que es el registro y no el plan, **`D.4`** cual
de las dos varas del ANTES manda en la clausula de la clase, **`D.5`** la lectura
contra el detector en las cuatro fichas de destejidos, y **`D.6`** que la `2.b`
no lleva caso rojo automatico.

**EL MAS PESADO ES EL `D.4`, Y LO DIGO PORQUE DE EL CUELGA UNA SUBIDA ENTERA.**
Si el auditor lee que el ANTES de esa clausula es el grafo previo a la campana y
no la vispera de la fase 01, la clausula de `01 FUENTES` idx 0 **vuelve a A
MEDIAS** y el recuento del cierre vuelve a **12 y 5**.

## 7. LAS PREGUNTAS Y LOS PENDIENTES DE DOCTRINA

**`P.1` LA CELDA DE `07 ADUANA` SIGUE DICIENDO CUATRO Y SU FICHA DICE CINCO.
QUIEN LA CORRIGE?** La pregunta de la 217 ya esta contestada por la `5.5` del
acta 217, linea 77275, leida hoy: **manda la ficha, la celda quedo vieja y la
clausula baja a A MEDIAS**. Lo que queda abierto **no es la lectura sino la
mano**: la celda vive en `docs/plan/08_VERIFICACION.md`, que es **sede del
fundador**, y esta vuelta no la toca. **Sube nombrada a la auditoria integral.**

**`P.2` UN ARNES QUE UNA CORRECCION DECLARADA DEJO EN ROJO, SE REPARA CUANDO?**
Contestada tambien, por la `5.6` del acta 217, linea 77295: **la moratoria lo
cubre y no se repara**. Lo que queda para el fundador es **si se repara al
levantarse la moratoria o si la vara de las ocho filas queda retirada** y la
sustituye la de las diecisiete clausulas.

**`P.3` LA QUE ABRO YO, Y ES DE FRONTERA:** el encargo prohibe escribir en el
plan y enumera sus sedes; **`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no esta entre
ellas**, y es donde la `5.7` del acta 217, linea 77304, manda la correccion
declarada con recomputo del marcador. **Escribi alli y lo declaro en voz alta.
Si el auditor lee que la prohibicion alcanzaba tambien al registro del cribado,
esas dos lineas se revierten y lo digo yo antes de que me lo digan.**

**PENDIENTES DE DOCTRINA: NINGUNO NUEVO.** El unico que la 217 levanto, si la
clausula de la clase protege el NUMERO de pasos o su LETRA, **quedo cerrado por
la `5.1` del acta 217, linea 77231**: protege la letra. Lo que esta vuelta
anade no es doctrina, es la lectura que esa adjudicacion encargo.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**SON DOS, Y LA PRIMERA ES EXACTAMENTE LA ESPECIE QUE EL ENCARGO DE ESTA VUELTA
VENIA A CAZAR, ASI QUE NO SE DISIMULA.**

**`C.1` ESCRIBI UNA LINEA DE ACTA DE MEMORIA EN VEZ DE LEERLA.** El primer
docstring de `scripts/loop/_v218_apertura.py` citaba la adjudicacion `6.5` del
acta 206 **en la linea 71455**. Leida del fichero, esa adjudicacion vive en la
**linea 72517**. **La cace yo, dentro de la propia vuelta, antes de que ese
numero llegara a ningun reporte ni a ningun commit de tarea**, y la version vieja
**queda escrita en el docstring con su motivo y no se borra**: una correccion que
tapa lo que corrige no se puede auditar. **La cuento como caida y no como
anecdota** porque la obligacion `6.6` que este encargo me pone encima dice
exactamente eso, que la linea se LEE y no se recuerda, y yo la recorde.

**`C.2` MI COMPOSITOR PARTIO UNA PAREJA DE BYTES EN DOS LINEAS Y PUBLICO UNA
CIFRA SIN SU PAREJA.** El parrafo del marcador de la seccion `1.d` escribia
*446 bytes* al final de una linea y *en disco y 426 normalizado a LF* al principio
de la siguiente, dos veces. **La guarda de `cerrar_reporte.py` la canto con su
numero de linea y el cierre salio en ROJO**, que es exactamente para lo que esa
guarda existe. Corregido a **una ruta por linea con sus dos convenciones al
lado**, y la version vieja queda escrita en el compositor con su motivo. **No la
cace yo: la cazo la guarda**, y eso se dice tal cual en vez de contarla como si
la hubiera visto antes.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**NO PROPONGO LA PARADA FELIZ, Y LA CONDICION NO LA PUSE YO.** Mi encargo la
escribio antes de saber el resultado: *"si al cerrar esta vuelta las DIECISIETE
clausulas quedan en CUBRE, con su busqueda corrida y su cifra delante, lo
propones"*. **Medido al cierre y no heredado:**

```
CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2: 13 de 17 | CIFRA que dejo la TAREA 1: 11
CIFRA clausulas en A MEDIAS AL CIERRE DE LA TAREA 2: 4 de 17 | CIFRA que dejo la TAREA 1: 6
CIFRA clausulas en NO CUBRE AL CIERRE DE LA TAREA 2: 0 de 17 | CIFRA que dejo la TAREA 1: 0
CIFRA en CUBRE: 13 | CIFRA que la condicion exige: 17
LA CONDICION SE CUMPLE: NO
```

**Por tanto NO propongo declarar la campana consumada.** Quien declara es el
auditor; yo propongo, que es lo que mi encargo manda.

**LAS CUATRO QUE FALTAN, CON SU FILA, SU INDICE Y SU CIFRA**, que es lo que el
encargo pide que se diga cuando la condicion no se cumple:

```
01 FUENTES     idx 1 | A MEDIAS  | **el material del segundo libro reubicado, no borrado**
03 FUSIONES    idx 0 | A MEDIAS  | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
05 SANEO       idx 1 | A MEDIAS  | los tres de Incoterms con su version
07 ADUANA      idx 0 | A MEDIAS  | los cuatro controles mecanicos **corriendo en Gate 0**
```

**Y LO QUE HAY DETRAS DE LAS CUATRO ES PLAN, NO MAQUINARIA:** 7 menciones que
todavia declaran un segundo libro, 71 actos sin fundir por la lectura ancha y
SEIS fusiones con 19 nodos por la estrecha, 1 de los 3 de Incoterms anotado como
trabajo post campana, y el quinto control de aduana sin correr.

**LO QUE PROPONGO, CON SU CIFRA DELANTE:**

1. **QUE LA VUELTA SIGUIENTE NO FABRIQUE NADA.** La moratoria aguanta y esta
   vuelta lo demuestra: **10 ficheros escritos en el arbol de scripts,
   los 10 con su prefijo**, ninguno en el censo ni en la nomina.
2. **QUE EL `D.4` SE ADJUDIQUE ANTES QUE NADA**, porque de el cuelga una subida
   entera y con el al reves el recuento vuelve a 12 y 5.
3. **QUE LA `P.3` SE CONTESTE**, y que si la respuesta es que el registro del
   cribado tambien estaba prohibido, **se revierta lo que escribi** en vez de
   dejarlo pasar por estar ya hecho.
4. **QUE LAS CUATRO CLAUSULAS EN A MEDIAS SUBAN NOMBRADAS** a la lista de la
   seccion 6 del acta, con su cifra, como subieron las seis de la 217.
5. **QUE LA 219 NO SEA DE BATERIA Y LA 220 SI**, que es lo que la cadencia de
   cinco de `AUDITOR.md` 6.1 dice y no una preferencia mia.

**Y EL MERGE NO SE PIDE: EL BUCLE NO FUNDE RAMAS.**
