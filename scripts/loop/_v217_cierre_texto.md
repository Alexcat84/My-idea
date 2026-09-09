## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODAS SALEN DE `docs/loop/SALIDA_V217_T2_CIERRE.txt`, que las midio y las sello. NINGUNA SE TECLEA.**

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS

**CIFRA salidas selladas del ciclo: 18 | CIFRA que deberia haber: 18**
**CIFRA ausentes: 0 | CIFRA de cero bytes: 0**
**CIFRA salidas SIN exitcode dentro: 0**
**CIFRA peor exitcode de las dieciocho: 0**

**Las dos consolas existen y las sello el propio instrumento**, que es el
remedio de la `3.1` del acta 214, mantenido y sin aflojar por ninguna de sus dos
puertas.

### 3.2. EL MARCADOR, EL CENSO Y LAS SUITES

**CIFRA cifras cotejadas: 16 | CIFRA que NO calzan: 0** Las tres suites corren **solas**, fuera del ciclo, cada una con su
exitcode y sus bytes por las dos convenciones. **La tabla entera esta en la
TAREA 2 del anexo y no se repite aqui**, porque dos versiones de lo mismo es
exactamente lo que esta casa prohibe.

### 3.3. LAS SEDES, Y LA PRUEBA DE QUE ESTA VUELTA NO ESCRIBIO NI UNA FICHA

**CIFRA sedes cotejadas: 13 | CIFRA que se movieron: 0** Esa es la prueba medida de que esta vuelta **no movio ni un nodo,
ni un veredicto, ni un campo de estado**. `docs/loop/ACTA_AUDITOR.md` y
`docs/loop/PROMPT_SIGUIENTE.md`, que son sede del auditor, tambien quedan
quietas.

**Y LA MISMA PRUEBA POR LA OTRA VIA, LA QUE LA TAREA 1 EXIGIA:**

```
SHA256 DE docs/plan/OPERACIONES.jsonl AL ENTRAR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/OPERACIONES.jsonl AL SALIR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/08_VERIFICACION.md AL ENTRAR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
SHA256 DE docs/plan/08_VERIFICACION.md AL SALIR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
LOS CUATRO SHA COINCIDEN CON LOS DE LA ENTRADA: SI
```

### 3.4. LAS RUTAS QUE ESTE REPORTE CITA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y **su salida se cita en el
commit de cierre**. Va ademas **metido como guarda previa en los tres
compositores de esta vuelta**, que cuentan los guiones largos y los directorios
de dos tramos entre comillas inversas **antes de escribir**.

## 4. LO QUE SE TOCO, Y LO QUE NO

**LA CIFRA VA CON SU HUECO AL LADO, QUE ES LA OBLIGACION DE DICTADO NUEVA DEL
ENCARGO DE LA 217 Y NACE DE MI CAIDA DE LA 216:**

**CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA: 7 | CIFRA de esos con el prefijo que le toca: 7**
**CIFRA MEDIDA AHORA: 7 | CIFRA DEL HUECO QUE EL PROPIO CIERRE ANADE: 4 | CIFRA TOTAL DE LA VUELTA, LAS DOS JUNTAS: 11**
**Y LOS DEL HUECO LLEVAN EL PREFIJO IGUAL: 4 de 4, contado de sus propios nombres.**

Fuera del censo y fuera de la nomina, que sigue **CONGELADA EN 135**.

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`):

- **`git status --porcelain` al entrar: 1 linea(s)**, y era mi
  propio script de apertura sin rastrear. **LA CIFRA NO SE TECLEA: se lee de
  la linea `CIFRA lineas de status: 1` del sello de apertura.**
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0**

**LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE:** no corrio la
bateria (la 215 la corrio y la cadencia de cinco pone la siguiente en la
**220**); **no reparo `scripts/loop/vuelta150_4_tabla_por_fase.py` aunque lo
encontro en rojo**, porque la moratoria lo prohibe; no toco el lanzador; no podo
ni engordo la nomina; no escribio en `docs/loop/PROMPT_SIGUIENTE.md` ni en
`docs/loop/ACTA_AUDITOR.md`; y **no movio ni un campo de estado**, con los
cuatro `sha256` delante.

**LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA:** leida de `git log` sobre el
commit de apertura y sobre el de ahora mismo.

- **fecha del commit de apertura, leida de git log: 2026-09-09**
- **fecha del commit de ahora mismo, leida de git log: 2026-09-09**

## 5. LAS PARADAS

**NO TRAIGO NINGUNA PARADA, Y LO DIGO CON EL MOTIVO DELANTE.**

**LA UNICA QUE MI ENCARGO ME MANDABA TRAER NO SE DISPARO:** su letra dice *"SI
TU INSTRUMENTO SACA OTRO NUMERO, PARAS Y LO TRAES CON LAS DOS CIFRAS
DELANTE"*, y mi instrumento saca **las mismas cuatro cifras** que el encargo, con
**CIFRA descuadres contra las cifras del encargo: 0**. No hay nada que parar ahi.

**Y LAS CINCO CLAUSULAS QUE NO LLEGAN A CUBRE TAMPOCO SON PARADA:** ninguna da
**NO CUBRE**, las cinco estan en **A MEDIAS por trabajo pendiente medido y
nombrado**, y ninguna contradice una regla vigente ni una cifra publicada con su
corte. **Lo que hay no es algo que parar: es algo que subir, y sube nombrado en
la seccion de la propuesta.**

**LO QUE SI TRAIGO, Y NO ES PARADA SINO HALLAZGO CON SU CORRIDA:**
`scripts/loop/vuelta150_4_tabla_por_fase.py`, que es el arnes que mide las ocho
filas de la tabla POR FASE, **hoy cae en rojo con exitcode 1**, y la causa esta
medida: su `assert` exige OCHO filas y la correccion declarada de la vuelta 214
dejo **ONCE**. **No lo reparo: la moratoria lo prohibe y mi encargo dice que
esta vuelta es medicion y verificacion.** La corrida vive en ``docs/loop/SALIDA_V217_T1_CONTRASTE_V150.txt``.

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Los cinco son de la TAREA 1 y los cinco son LECTURAS MIAS de una clausula.**
Estan escritos enteros, con su duda y con lo que cambiaria si el auditor lee al
reves, en la **seccion `1.g` de la TAREA 1 del anexo**, y **no se repiten aqui a
proposito**: dos versiones de lo mismo es lo que esta casa prohibe. Sus rotulos,
para que se puedan citar: **`D.a`** la vara del ANTES de la clase, **`D.b`** que
es reubicar, **`D.c`** la anchura del detector del reparto, **`D.d`** el
universo de la clausula de las fusiones y **`D.e`** cuatro controles contra
cinco.

## 7. LAS PREGUNTAS Y LOS PENDIENTES DE DOCTRINA

**`P.1` LA CELDA DE `07 ADUANA` DICE CUATRO Y SU FASE DICE CINCO. CUAL MANDA?**
Medido hoy: la celda pide **CUATRO controles mecanicos corriendo en Gate 0**, y
**hay cuatro corriendo y los cuatro en verde**. Pero `docs/plan/07_ADUANA.md`
titula su tabla **LOS CINCO CONTROLES MECANICOS QUE LA ACOMPANAN** y la
verificacion de `OP-A-02` escribe *"los CINCO controles mecanicos corriendo"*. El
quinto, **la revision de toda nomina por el DOMINIO de sus miembros**, nacio el
13 ago 2026, **despues** de que se escribiera la celda, y **no corre**. **La
pregunta no la contesto yo:** o la celda quedo vieja y la cifra viva es cinco, o
el quinto control no es de esta celda.

**`P.2` UN ARNES QUE UNA CORRECCION DECLARADA DEJO EN ROJO, SE REPARA CUANDO?**
`scripts/loop/vuelta150_4_tabla_por_fase.py` medía las ocho filas y hoy no
arranca. **La moratoria prohibe repararlo y yo no lo he reparado.** La pregunta
es del fundador: **la auditoria integral lo autoriza, o la vara de las ocho
filas queda retirada y la sustituye la de las diecisiete clausulas de esta
vuelta.**

**PENDIENTES DE DOCTRINA: UNO, Y ES EL DE LA CLASE.** La clausula *"ningun nodo
de la clase con pasos alterados"* no dice **si protege el NUMERO de pasos o su
LETRA**. Medido hoy: por el numero, **6 de 6 quedan intactos**; por la letra,
**2 de 6 tienen texto distinto** al del grafo previo, y **ninguno de los commits
que los tocaron nombra una operacion de la fase 01**. **Registro lo mejor
sostenido, lo marco `D.a` y sigo**, que es lo que `EJECUTOR.md` 5 manda cuando
falta la regla.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**ES UNA, DE MI PROPIA SONDA, CAZADA DENTRO DE ESTA MISMA VUELTA Y NO PUBLICADA
COMO CIFRA BUENA EN NINGUN SITIO.**

**`C.1` MI MUTANTE SANO DE `03 FUSIONES` NO PODIA SUBIR NUNCA.** Lo fabrique
deprecando a mano los miembros sobrantes de cada acto y anadiendolos a los
`ids_alias` del superviviente. **Un nodo vive en mas de un acto**, asi que
deprecarlo por uno rompia el otro, y la sonda medía **un desorden fabricado por
mi mutante**, no un mundo sano: salio **NO CUBRE** y con el la comprobacion
entera. **Lo cazo mi propio instrumento cayendo en rojo antes de escribir nada.**
Corregido a construir el mundo sano **sin tocar el grafo**, dejando en el
inventario los actos que ya tienen un superviviente unico, **sube a CUBRE** y la
comprobacion pasa: **4 de 4 mutantes sanos suben.** **La version vieja queda
escrita en el codigo, con su motivo, y no se borra.**

**Y UNA SEGUNDA COSA QUE NO CUENTO COMO CAIDA Y DIGO POR QUE:** mi primera
corrida publicaba la clausula `02 DESTEJIDOS` idx 1 con **un solo detector**, el
estrecho. **No era una cifra falsa** y el veredicto no cambia, pero dejaba fuera
que **cuatro fichas nombran su bloque con otras palabras**. Se anadio el
detector **ANCHO** y ahora se publican **las dos cifras**, con el veredicto
saliendo de la estrecha, que es la que no afloja la vara. **Anadir una cifra al
lado no es corregir una falsa**, y por eso va aqui abajo y no arriba.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**NO PROPONGO LA PARADA FELIZ, Y LA CONDICION NO LA PUSE YO.** Mi encargo la
escribio antes de saber el resultado: *"si las DIECISIETE quedan en CUBRE con su
busqueda corrida y su cifra delante"*. **Medido hoy: 5 de 17 quedan en
A MEDIAS**, cada una con su fila, su indice y su cifra en la TAREA 1. **Por
tanto no propongo declarar la campana consumada.** Quien declara es el auditor;
yo propongo, que es lo que mi encargo manda.

**LO QUE SI DIGO, CON SU CIFRA DELANTE, PORQUE ES LO QUE LA MEDICION SOSTIENE:
NINGUNA DE LAS DIECISIETE DA NO CUBRE**, y **12 de 17 dan CUBRE**. Las
cinco que no cubren lo hacen **por trabajo del plan que no se ha ejecutado**, no
por un fallo del catalogo: **71 actos siguen sin fundir**, **7 menciones siguen
declarando un segundo libro**, y **1 de los 3 de Incoterms** quedo anotado como
trabajo post campana por adjudicacion del acta 120. **Ninguna de las tres es
maquinaria: es plan.**

**LO QUE PROPONGO, CON SU CIFRA DELANTE:**

1. **QUE LA VUELTA SIGUIENTE NO FABRIQUE NADA.** La moratoria aguanta y esta
   vuelta lo demuestra: **7 ficheros escritos en el arbol de scripts, los
   7 con su prefijo**, ninguno en el censo ni en la nomina.
2. **QUE LAS CINCO CLAUSULAS EN A MEDIAS SUBAN NOMBRADAS**, con su cifra, a la
   lista de la seccion 6 del acta, igual que subio la de `OP-I-01`.
3. **QUE EL ROJO DE `vuelta150_4_tabla_por_fase.py` SUBA NOMBRADO Y SIN
   REPARAR**, y que el fundador diga en la auditoria integral si se repara o si
   la vara de las ocho filas queda sustituida por la de las diecisiete
   clausulas.
4. **QUE LA `P.1` SE CONTESTE ANTES DE QUE NADIE TOQUE LA CELDA DE `07
   ADUANA`**, porque cambiarla sin contestarla seria reescribir una vara para
   que pase.

**Y EL MERGE NO SE PIDE: EL BUCLE NO FUNDE RAMAS.**
