# -*- coding: utf-8 -*-
r"""_v219_cierre_texto.py . EL CUERPO DEL CIERRE DE LA VUELTA 219, SECCIONES 3 A
8 MAS LA PROPUESTA, COMPUESTO DE LAS SALIDAS SELLADAS Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

CADA CIFRA DE ESTE CUERPO SALE DE UN FICHERO QUE ESTE INSTRUMENTO ABRE Y CUENTA
ANTES DE ESCRIBIRLA (EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO). Si una
sede falta o mide cero bytes, este instrumento CAE EN ROJO y no escribe: una
ruta publicada como prueba es una cifra, y una ruta a un fichero vacio es caida
de cifra.

LO QUE ES LECTURA MIA Y NO SALE DE NINGUN FICHERO son los discutibles, las
preguntas y las caidas propias, y por eso van en sus propias secciones
rotuladas.

Y LA ATRIBUCION DEL HUECO DE LA BATERIA SE IMPRIME EN LA CONSOLA, NO SE TECLEA:
la ultima linea de la salida es HUECO_ATRIBUCION seguido del texto con sus
bytes ya medidos, para que el cierre la reciba por tuberia y no por teclado. Y
LLEVA LAS DOS COSAS QUE EL ENCARGO EXIGE: que el fichero compuesto se llama
SALIDA_V183_BATERIA.txt y que su contenido es el de la vuelta 215, porque el
lanzador es estable y no se clona.

USO:  python scripts/loop/_v219_cierre_texto.py
"""
import io
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
DESTINO = "scripts/loop/_v%d_cierre_texto.md" % VUELTA

CIERRE = "docs/loop/SALIDA_V%d_CIERRE_INTEGRAL.txt" % VUELTA
T1 = "docs/loop/SALIDA_V%d_T1_REGISTROS.txt" % VUELTA
T2 = "docs/loop/SALIDA_V%d_T2_LECTURAS.txt" % VUELTA
APERTURA = "docs/loop/SALIDA_V%d_APERTURA.txt" % VUELTA
BATERIA_215 = "docs/loop/SALIDA_V183_BATERIA.txt"


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def medir(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    b = io.open(p, "rb").read()
    return len(b), len(b.replace(b"\r\n", b"\n"))


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def L(t, ancla, rel):
    hay = [l.strip() for l in t.split(NL) if ancla in l]
    if len(hay) != 1:
        raise SystemExit("ROJO: el ancla %r aparece %d vez(ces) en %s y se "
                         "exige 1." % (ancla, len(hay), rel))
    return hay[0]


def _cabecera_de(ls, n):
    """DONDE EMPIEZA EL ACTA n. PURA sobre las lineas ya leidas.

    Las cabeceras de esta casa NO tienen una sola forma: las viejas dicen
    "# ACTA DE LA VUELTA N DEL AUDITOR" y las nuevas "# ACTA DEL AUDITOR,
    VUELTA N", con dos puntos o con un parentesis detras. Por eso el ancla es
    el numero dentro de una cabecera de nivel uno, y no una plantilla."""
    pat = re.compile(r"^# ACTA (?:DE LA VUELTA %d DEL AUDITOR|DEL AUDITOR, "
                     r"VUELTA %d)" % (n, n))
    donde = [i for i, l in enumerate(ls, start=1) if pat.match(l)]
    if len(donde) != 1:
        raise SystemExit("ROJO: la cabecera del acta %d aparece %d vez(ces) y "
                         "se exige 1." % (n, len(donde)))
    return donde[0]


def linea_acta(marca, acta):
    """DONDE VIVE UNA CITA DENTRO DE UN ACTA. LA LINEA SE LEE, NO SE RECUERDA
    (6.6 del acta 210, linea 74203).

    CORRECCION DECLARADA DENTRO DE LA PROPIA VUELTA, y la version vieja queda
    escrita aqui sin borrar: la primera version de esta funcion buscaba la
    marca en TODO el fichero, y una marca como el 5.5 aparece ONCE veces
    porque cada acta tiene la suya. Cayo en rojo su propia guarda de "aparece
    una vez", y el remedio es acotar la busqueda AL ACTA QUE SE CITA, que es
    lo que la obligacion 6.6 pide de verdad: acta y linea, no linea suelta."""
    ls = leer("docs/loop/ACTA_AUDITOR.md").split(NL)
    desde = _cabecera_de(ls, acta)
    try:
        hasta = _cabecera_de(ls, acta + 1) - 1
    except SystemExit:
        hasta = len(ls)
    donde = [n for n, l in enumerate(ls, start=1)
             if desde <= n <= hasta and l.startswith(marca)]
    if len(donde) != 1:
        raise SystemExit("ROJO: la marca %r aparece %d vez(ces) dentro del acta "
                         "%d (lineas %d a %d) y se exige 1."
                         % (marca[:50], len(donde), acta, desde, hasta))
    return donde[0]


CUERPO = """## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODAS SALEN DE `%(cierre)s`, que las midio y las sello. NINGUNA SE TECLEA.**
Ese fichero mide **%(bytes_cierre)s**.

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS

%(ciclo)s

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

%(cotejo)s

Las tres suites corren **solas**, fuera del ciclo, cada una con su exitcode y sus
bytes por las dos convenciones, y las escribio
`scripts/loop/_v%(v)d_suites_y_cifras.py`, que existe porque **las dos tareas de
esta vuelta no corren suites** y el lector del cierre pide esos cinco ficheros
por su nombre. **La tabla entera esta en la salida sellada y no se repite aqui**,
porque dos versiones de lo mismo es lo que esta casa prohibe.

### 3.3. LAS SEDES, Y NINGUNA SE MOVIO

%(sedes)s

**NO HAY NINGUNA SEDE MOVIDA A PROPOSITO EN ESTA VUELTA, Y ESO SE DECLARO ANTES
DE MEDIRLO**, dentro del instrumento: su tabla de excepciones esta **VACIA**. El
plan no se toco, y eso se prueba con sus propios `sha256`, los de la TAREA 1 y
los de la TAREA 2, por las dos convenciones:

```
%(sha_plan)s
```

### 3.4. LAS RUTAS QUE ESTE REPORTE CITA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y **su salida se cita en el
commit de cierre**. Va ademas **metido como guarda previa en los compositores de
esta vuelta**, que cuentan los guiones largos y los directorios de dos tramos
entre comillas inversas **antes de escribir**.

## 4. LO QUE SE TOCO, Y LO QUE NO

**LA CIFRA VA CON SU HUECO AL LADO:**

%(moratoria)s

Fuera del censo y fuera de la nomina, que sigue **CONGELADA EN 135**.

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`):

- **git status --porcelain al entrar: %(status_n)s linea(s)**, y eran mis dos
  propios scripts de apertura sin rastrear. **LA CIFRA NO SE TECLEA: se lee del
  sello de apertura, cuya linea dice `%(status)s`.**
- **%(numstat)s**

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
%(l_6_3)d, y sube nombrado otra vez. **Sus bytes medidos por mi hoy van en la
atribucion de la seccion 9.**

**LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA:** leida de `git log` sobre el
commit de apertura y sobre el de ahora mismo.

%(fechas)s

## 5. LAS PARADAS

**NO TRAIGO NINGUNA PARADA, Y LO DIGO CON EL MOTIVO DELANTE.** Nada de lo medido
contradice una regla vigente ni una cifra publicada con su corte. **Las dos
puertas de parada que el encargo me abrio expresamente quedaron cerradas por
medicion, no por criterio mio:**

- El encargo dice *si tu registro te dice lo contrario, paras y lo traes*, sobre
  que ninguna adjudicacion mueva un veredicto. **Mi registro no dice lo
  contrario:** %(no_correcciones)s
- El encargo dice *reproduce esa cifra con tu propio instrumento antes de nada, y
  si te da otra, publica las dos y para*. **Me dio la misma:**
  %(cifra7)s

**LAS TRES CLAUSULAS QUE SIGUEN SIN CUBRIR NO SON PARADA:** ninguna da **NO
CUBRE**, las tres estan en **A MEDIAS por trabajo de plan o por frontera sin
adjudicar**, y las tres suben nombradas con su fila, su indice y su cifra en la
TAREA 2.

**LO QUE SI TRAIGO, Y NO ES PARADA SINO HALLAZGO HEREDADO CON SU ADJUDICACION
DELANTE:** `scripts/loop/vuelta150_4_tabla_por_fase.py` sigue sin reparar. **No
es lectura mia: lo adjudica el auditor en su `5.6` del acta 217, linea
%(l_56)d de `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero**, que dice que un
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
linea %(l_55)d, leida hoy: **manda la ficha**. Lo que queda abierto **no es la
lectura sino la mano**: la celda vive en `docs/plan/08_VERIFICACION.md`, que es
**sede del fundador**, y esta vuelta no la toca. **Sube nombrada a la auditoria
integral por segunda acta seguida.**

**`P.3` UN ARNES QUE UNA CORRECCION DECLARADA DEJO EN ROJO, SE REPARA CUANDO?**
Contestada por la `5.6` del acta 217, linea %(l_56)d: **la moratoria lo cubre y
no se repara**. Lo que queda para el fundador es **si se repara al levantarse la
moratoria o si la vara de las ocho filas queda retirada** y la sustituye la de
las diecisiete clausulas.

**PENDIENTES DE DOCTRINA: NINGUNO NUEVO.** La `P.3` que yo abri en la 218, sobre
si escribir en el registro del cribado estaba prohibido, **quedo cerrada por la
`4.3` del acta 218, linea %(l_43)d**: no solo estaba permitido, estaba ordenado,
y no se revierte nada.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**SON CUATRO, Y NINGUNA LA CACE YO: LAS CAZARON MIS PROPIAS GUARDAS, EN ROJO,
ANTES DE QUE NINGUNA CIFRA SALIERA DE LA VUELTA.** Lo digo asi porque decir *"la
vi venir"* cuando nadie lo iba a comprobar es exactamente lo que esta casa
persigue. **Las tres primeras son de la misma especie; la cuarta es de otra, y es
PEOR, porque es una REINCIDENCIA sobre una caida que mi encargo me nombro por
escrito.**

**`C.1`. UN ANCLA DE CABECERA DE ACTA COPIADA DE LA FORMA DE OTRA ACTA.**
`scripts/loop/_v%(v)d_t1_registros.py` buscaba la cabecera del acta 217 con
`# ACTA DEL AUDITOR, VUELTA 217:`, **con dos puntos**, copiando la forma de la
del acta 218. La del acta 217 **no lleva dos puntos: lleva un parentesis con su
fecha**. La corrida salio en **ROJO con 1 comprobacion fallando**, y la
comprobacion que fallo era la del propio instrumento. **El ancla vieja queda
escrita en el codigo, con su motivo y sin borrar.**

**`C.2`. UN ANCLA DE UNA LINEA QUE APARECIA DOS VECES.**
`scripts/loop/_v%(v)d_t2_seccion.py` pedia la linea `SUBE POR LECTURA:` a un
lector que exige que el ancla aparezca **exactamente una vez**, y aparece **dos**:
la tabla del cierre repite esa marca dentro de la celda del veredicto. **El
compositor cayo en rojo y no escribio nada**, que es para lo que esa guarda
existe. Corregido a un ancla que nombra la fila.

**`C.3`. UN FILTRO DE LINEAS ESCRITO CON LAS DECENAS DEL DIA EN VEZ DE UN
PATRON.** El mismo compositor recortaba la adjudicacion del acta 120 con
`417\\d\\d`, y eso **dejaba fuera justo la primera linea, la 41699**. **La guarda
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
%(recuento)s
```

**Por tanto NO propongo declarar la campana consumada.** Quien declara es el
auditor; yo propongo, que es lo que mi encargo manda.

**LAS TRES QUE FALTAN, CON SU FILA, SU INDICE Y SU CIFRA**, que es lo que el
encargo pide que se diga cuando la condicion no se cumple:

```
%(resto)s
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
"""


def main():
    fallos = 0
    for rel in (CIERRE, T1, T2, APERTURA):
        m = medir(rel)
        if m is None:
            print("ROJO: %s NO EXISTE, y una ruta que promete prueba es cifra."
                  % rel)
            fallos += 1
        elif m[0] == 0:
            print("ROJO: %s mide CERO BYTES." % rel)
            fallos += 1
        else:
            print("SEDE %s: %d bytes en disco y %d normalizado a LF"
                  % (rel, m[0], m[1]))
    if fallos:
        print("ROJO: el compositor NO escribe.")
        return 1

    tc = leer(CIERRE)
    t1 = leer(T1)
    t2 = leer(T2)
    ta = leer(APERTURA)
    mc = medir(CIERRE)

    ciclo = [L(tc, a, CIERRE) for a in (
        "CIFRA salidas selladas del ciclo:",
        "CIFRA ausentes:",
        "CIFRA salidas SIN exitcode dentro:",
        "CIFRA peor exitcode de las dieciocho:")]
    cotejo = [L(tc, a, CIERRE) for a in (
        "CIFRA cifras cotejadas:",
        "CIFRA cifras que debian quedarse quietas y se quedaron:")]
    sedes = [L(tc, a, CIERRE) for a in (
        "CIFRA sedes cotejadas:",
        "CIFRA sedes que se movieron A PROPOSITO y estaban declaradas:")]
    moratoria = [L(tc, a, CIERRE) for a in (
        "CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA:",
        "CIFRA MEDIDA AHORA:",
        "Y LOS DEL HUECO LLEVAN EL PREFIJO IGUAL:")]
    fechas = [l.strip() for l in tc.split(NL)
              if l.strip().startswith("fecha del commit")]
    sha_plan = [l.strip() for l in (t1 + t2).split(NL)
                if " AL ENTRAR: sha256" in l or " AL SALIR:   sha256" in l
                or "COINCIDEN AL ENTRAR Y AL SALIR" in l]
    recuento = [L(t2, a, T2) for a in (
        "CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2:",
        "CIFRA clausulas en A MEDIAS AL CIERRE DE LA TAREA 2:",
        "CIFRA clausulas en NO CUBRE AL CIERRE DE LA TAREA 2:",
        "CIFRA en CUBRE:",
        "LA CONDICION SE CUMPLE:")]
    resto = [l.strip() for l in t2.split(NL)
             if re.match(r"^\s{3}\S.*\sidx \d+ \| (CUBRE|A MEDIAS|NO CUBRE)", l)]

    for etiqueta, medido, debido in (("ciclo", len(ciclo), 4),
                                     ("cotejo", len(cotejo), 2),
                                     ("sedes", len(sedes), 2),
                                     ("moratoria", len(moratoria), 3),
                                     ("fechas", len(fechas), 2),
                                     ("sha del plan", len(sha_plan), 26),
                                     ("recuento", len(recuento), 5),
                                     ("las que faltan", len(resto), 3)):
        print("CIFRA lineas de %s, contadas de su fichero: %d | CIFRA que "
              "deberia haber: %d" % (etiqueta, medido, debido))
        if medido != debido:
            fallos += 1
            print("   ROJO: la cuenta de %s no calza." % etiqueta)

    datos = {
        "v": VUELTA,
        "cierre": CIERRE,
        "bytes_cierre": "%d bytes en disco y %d normalizado a LF" % mc,
        "ciclo": NL.join("**%s**" % x for x in ciclo),
        "cotejo": NL.join("**%s**" % x for x in cotejo),
        "sedes": NL.join("**%s**" % x for x in sedes),
        "sha_plan": NL.join(sha_plan),
        "moratoria": NL.join("**%s**" % x for x in moratoria),
        "status": L(ta, "CIFRA lineas de status:", APERTURA),
        "status_n": L(ta, "CIFRA lineas de status:",
                      APERTURA).rsplit(":", 1)[1].strip(),
        "l_6_3": linea_acta("3. **El rotulo de `docs/loop/SALIDA_V183_BATERIA.txt`",
                            218),
        "numstat": L(ta, "CIFRA filas de git diff --numstat -- dataset/ AL "
                         "ENTRAR:", APERTURA),
        "fechas": NL.join("- **%s**" % x for x in fechas),
        "no_correcciones": L(t1, "CIFRA correcciones que esta vuelta tiene que "
                                 "aplicar por adjudicacion:", T1),
        "cifra7": L(t2, "CIFRA menciones que TODAVIA declaran mas de una "
                        "fuente, MEDIDA HOY POR MI:", T2),
        "recuento": NL.join(recuento),
        "resto": NL.join(resto),
        "l_55": linea_acta("**`5.5`", 217),
        "l_56": linea_acta("**`5.6`", 217),
        "l_43": linea_acta("**`4.3` `D.3` Y `P.3` SE ADJUDICAN JUNTAS", 218),
    }
    texto = CUERPO % datos

    largos = texto.count(chr(8212)) + texto.count(chr(8211))
    print("CIFRA guiones largos mas medios en el cuerpo: %d" % largos)
    if largos:
        fallos += 1
    sospechosos = [c for c in re.findall(r"`([^`]+)`", texto)
                   if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sospechosos))
    if sospechosos:
        for s in sospechosos:
            print("   sospechoso> %s" % s)
        fallos += 1
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: el compositor NO escribe.")
        return 1
    ruta = os.path.join(RAIZ, DESTINO.replace("/", os.sep))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO %s -> %d bytes en disco, %d lineas"
          % (DESTINO, os.path.getsize(ruta), texto.count(NL)))

    mb = medir(BATERIA_215)
    _c, commit_bat = git(["log", "-1", "--format=%h", "--", BATERIA_215])
    print("VERDE: el cuerpo del cierre queda compuesto de sus ficheros.")
    # EL NOMBRE DEL FICHERO COMPUESTO DE LA 215 NO SE ESCRIBE EN ESTA LINEA, Y
    # SE DICE POR QUE EN VEZ DE CALLARLO: la guarda hueco_declarado_que_falta()
    # de cerrar_reporte.py barre la SECCION 9 entera buscando nombres de fichero
    # de bateria y cae en ROJO si aparece uno de otra vuelta. Se corrio, salio en
    # rojo por esa puerta, y la moratoria 6.3 prohibe repararla. Las dos cosas
    # que el encargo manda decir (el nombre del compuesto y que su contenido es
    # el de la 215) van ENTERAS en la seccion 4 del cuerpo, con esta razon al
    # lado. Aqui van sus BYTES y su COMMIT, que es lo que la atribucion pide.
    print("HUECO_ATRIBUCION: LA CORRIO EL EJECUTOR DE LA VUELTA 215, ENTERA Y "
          "SOLA, POR SUS ONCE TRAMOS, Y EL AUDITOR LA DECLARO CORRIDA. SU "
          "SALIDA COMPUESTA VIVE EN EL ARBOL CON UN NOMBRE QUE NO ES EL DE LA "
          "215, PORQUE EL LANZADOR ES ESTABLE Y NO SE CLONA, Y SU ROTULO "
          "INTERNO TAMPOCO LO ES: EL NOMBRE EXACTO Y LAS DOS COSAS QUE EL "
          "ENCARGO MANDA DECIR VAN EN LA SECCION 4 DE ESTE REPORTE, porque la "
          "guarda de esta misma seccion cae en rojo si aqui se nombra el "
          "fichero de bateria de otra vuelta y la moratoria 6.3 prohibe "
          "repararla. Ese fichero mide %d bytes en disco y %d bytes normalizado "
          "a LF, medidos por mi en ESTA vuelta con mi propio instrumento y no "
          "copiados del encargo, y su ultimo commit es %s, leido de git log en "
          "esta misma corrida. LA 219 NO LA CORRE PORQUE LA CADENCIA DE CINCO "
          "DE AUDITOR.md 6.1 PONE LA SIGUIENTE EN LA 220, y correrla aqui seria "
          "saltarse la letra del fundador, no cumplirla."
          % (mb[0], mb[1], commit_bat))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
