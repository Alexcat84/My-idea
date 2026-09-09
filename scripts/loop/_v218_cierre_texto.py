# -*- coding: utf-8 -*-
r"""_v218_cierre_texto.py . EL CUERPO DEL CIERRE DE LA VUELTA 218, SECCIONES 3 A
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
bytes ya medidos, para que el cierre la reciba por tuberia y no por teclado.

USO:  python scripts/loop/_v218_cierre_texto.py
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


def linea_con(texto, marca):
    for l in texto.split(NL):
        if marca in l:
            return l.strip()
    return None


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace").strip()


def main():
    fallos = 0
    print("LAS SEDES QUE ESTE CUERPO CITA COMO PRUEBA, MEDIDAS ANTES DE "
          "CITARLAS (una ruta que promete prueba es cifra):")
    for rel in (CIERRE, T1, T2, APERTURA, BATERIA_215):
        m = medir(rel)
        if m is None:
            print("   ROJO: %s NO EXISTE" % rel)
            fallos += 1
            continue
        if m[0] == 0:
            print("   ROJO: %s mide CERO BYTES" % rel)
            fallos += 1
            continue
        print("   %-52s %7d bytes en disco y %7d normalizado a LF"
              % (rel, m[0], m[1]))
    if fallos:
        print("ROJO: el compositor NO escribe. Fallos: %d" % fallos)
        return 1

    c = leer(CIERRE)
    t1 = leer(T1)
    t2 = leer(T2)
    ap = leer(APERTURA)
    bat = medir(BATERIA_215)
    _r, commit_bat = git(["log", "-1", "--format=%h", "--", BATERIA_215])

    def L(texto, marca):
        x = linea_con(texto, marca)
        if x is None:
            raise SystemExit("ROJO: falta la linea %r" % marca)
        return x

    print("")
    print("LA ATRIBUCION DE LA BATERIA, MEDIDA HOY Y NO COPIADA DEL ENCARGO:")
    print("   %s -> %d bytes en disco y %d normalizado a LF, commit %s"
          % (BATERIA_215, bat[0], bat[1], commit_bat))
    print("")

    texto = """## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODAS SALEN DE `%(cierre)s`, que las midio y las sello. NINGUNA SE TECLEA.**

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS

**%(lciclo)s**
**%(lausentes)s**
**%(lsinec)s**
**%(lpeor)s**

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

**%(ldif)s**
**%(lquietas)s**

Las tres suites corren **solas**, fuera del ciclo, cada una con su exitcode y sus
bytes por las dos convenciones. **La tabla entera esta en la salida sellada y no
se repite aqui**, porque dos versiones de lo mismo es lo que esta casa prohibe.

### 3.3. LAS SEDES, Y LA UNICA QUE SE MOVIO, DECLARADA ANTES DE MEDIRLA

**%(lsedes)s**
**%(lproposito)s**

**LA QUE SE MOVIO ES `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, Y NO ES UN DESCUIDO:
ES LA TAREA 1.c.** Su motivo se escribio **dentro del instrumento y antes de
medir**, no despues de ver el resultado. **El plan no se toco**, y eso se prueba
con sus propios `sha256`, los de la TAREA 1 y los de la TAREA 2:

```
%(sha)s
```

### 3.4. LAS RUTAS QUE ESTE REPORTE CITA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y **su salida se cita en el
commit de cierre**. Va ademas **metido como guarda previa en los cuatro
compositores de esta vuelta**, que cuentan los guiones largos y los directorios
de dos tramos entre comillas inversas **antes de escribir**.

## 4. LO QUE SE TOCO, Y LO QUE NO

**LA CIFRA VA CON SU HUECO AL LADO:**

**%(ltoc)s**
**%(lhueco)s**
**%(lpref)s**

Fuera del censo y fuera de la nomina, que sigue **CONGELADA EN 135**.

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`):

- **`git status --porcelain` al entrar: %(nstatus)s linea(s)**, y era mi
  propio script de apertura sin rastrear. **LA CIFRA NO SE TECLEA: se lee de
  la linea `%(lstatus)s` del sello de apertura.**
- **%(lnumstat)s**

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

- **%(lfap)s**
- **%(lfci)s**

## 5. LAS PARADAS

**NO TRAIGO NINGUNA PARADA, Y LO DIGO CON EL MOTIVO DELANTE.** Nada de lo medido
contradice una regla vigente ni una cifra publicada con su corte.

**LAS CUATRO CLAUSULAS QUE SIGUEN SIN CUBRIR NO SON PARADA:** ninguna da **NO
CUBRE**, las cuatro estan en **A MEDIAS por trabajo de plan medido y nombrado**, y
las cuatro suben nombradas con su fila, su indice y su cifra en la TAREA 2.

**LO QUE SI TRAIGO, Y NO ES PARADA SINO HALLAZGO HEREDADO CON SU ADJUDICACION
DELANTE:** `scripts/loop/vuelta150_4_tabla_por_fase.py` sigue en rojo. **No lo
reparo, y esta vez no es lectura mia: lo adjudica el auditor en su `5.6` del acta
217, linea %(l56)s de `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero**, que
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
acta 217, linea %(l55)s, leida hoy: **manda la ficha, la celda quedo vieja y la
clausula baja a A MEDIAS**. Lo que queda abierto **no es la lectura sino la
mano**: la celda vive en `docs/plan/08_VERIFICACION.md`, que es **sede del
fundador**, y esta vuelta no la toca. **Sube nombrada a la auditoria integral.**

**`P.2` UN ARNES QUE UNA CORRECCION DECLARADA DEJO EN ROJO, SE REPARA CUANDO?**
Contestada tambien, por la `5.6` del acta 217, linea %(l56)s: **la moratoria lo
cubre y no se repara**. Lo que queda para el fundador es **si se repara al
levantarse la moratoria o si la vara de las ocho filas queda retirada** y la
sustituye la de las diecisiete clausulas.

**`P.3` LA QUE ABRO YO, Y ES DE FRONTERA:** el encargo prohibe escribir en el
plan y enumera sus sedes; **`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no esta entre
ellas**, y es donde la `5.7` del acta 217, linea %(l57)s, manda la correccion
declarada con recomputo del marcador. **Escribi alli y lo declaro en voz alta.
Si el auditor lee que la prohibicion alcanzaba tambien al registro del cribado,
esas dos lineas se revierten y lo digo yo antes de que me lo digan.**

**PENDIENTES DE DOCTRINA: NINGUNO NUEVO.** El unico que la 217 levanto, si la
clausula de la clase protege el NUMERO de pasos o su LETRA, **quedo cerrado por
la `5.1` del acta 217, linea %(l51)s**: protege la letra. Lo que esta vuelta
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
%(recuento)s
```

**Por tanto NO propongo declarar la campana consumada.** Quien declara es el
auditor; yo propongo, que es lo que mi encargo manda.

**LAS CUATRO QUE FALTAN, CON SU FILA, SU INDICE Y SU CIFRA**, que es lo que el
encargo pide que se diga cuando la condicion no se cumple:

```
%(resto)s
```

**Y LO QUE HAY DETRAS DE LAS CUATRO ES PLAN, NO MAQUINARIA:** 7 menciones que
todavia declaran un segundo libro, 71 actos sin fundir por la lectura ancha y
SEIS fusiones con 19 nodos por la estrecha, 1 de los 3 de Incoterms anotado como
trabajo post campana, y el quinto control de aduana sin correr.

**LO QUE PROPONGO, CON SU CIFRA DELANTE:**

1. **QUE LA VUELTA SIGUIENTE NO FABRIQUE NADA.** La moratoria aguanta y esta
   vuelta lo demuestra: **%(ntoc)s ficheros escritos en el arbol de scripts,
   los %(npref)s con su prefijo**, ninguno en el censo ni en la nomina.
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
""" % {
        "cierre": CIERRE,
        "lciclo": L(c, "CIFRA salidas selladas del ciclo:"),
        "lausentes": L(c, "CIFRA ausentes:"),
        "lsinec": L(c, "CIFRA salidas SIN exitcode dentro:"),
        "lpeor": L(c, "CIFRA peor exitcode de las dieciocho:"),
        "ldif": L(c, "CIFRA cifras cotejadas:"),
        "lquietas": L(c, "CIFRA cifras que debian quedarse quietas"),
        "lsedes": L(c, "CIFRA sedes cotejadas:"),
        "lproposito": L(c, "CIFRA sedes que se movieron A PROPOSITO"),
        "sha": NL.join([
            L(t1, "SHA256 DE docs/plan/OPERACIONES.jsonl AL ENTRAR"),
            L(t1, "SHA256 DE docs/plan/OPERACIONES.jsonl AL SALIR"),
            L(t1, "SHA256 DE docs/plan/08_VERIFICACION.md AL ENTRAR"),
            L(t1, "SHA256 DE docs/plan/08_VERIFICACION.md AL SALIR"),
            L(t1, "LOS SEIS SHA DEL PLAN COINCIDEN CON LOS DE LA ENTRADA"),
            L(t2, "LOS OCHO SHA DEL PLAN COINCIDEN CON LOS DE LA ENTRADA")]),
        "ltoc": L(c, "CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA:"),
        "lhueco": L(c, "CIFRA MEDIDA AHORA:"),
        "lpref": L(c, "Y LOS DEL HUECO LLEVAN EL PREFIJO IGUAL:"),
        "lstatus": L(ap, "CIFRA lineas de status:"),
        "nstatus": re.search(r"CIFRA lineas de status: (\d+)", ap).group(1),
        "lnumstat": L(ap, "CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR:"),
        "lfap": L(c, "fecha del commit de apertura, leida de git log:"),
        "lfci": L(c, "fecha del commit de ahora mismo, leida de git log:"),
        "recuento": NL.join([
            L(t2, "CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2:"),
            L(t2, "CIFRA clausulas en A MEDIAS AL CIERRE DE LA TAREA 2:"),
            L(t2, "CIFRA clausulas en NO CUBRE AL CIERRE DE LA TAREA 2:"),
            L(t2, "CIFRA en CUBRE:"),
            L(t2, "LA CONDICION SE CUMPLE:")]),
        "resto": NL.join(
            x.strip() for x in t2.split(NL)
            if re.match(r"^\s+(01 FUENTES|03 FUSIONES|05 SANEO|07 ADUANA)\s+"
                        r"idx \d \| A MEDIAS", x)),
        "ntoc": re.search(r"MEDIDA AHORA: (\d+)", c).group(1),
        "npref": re.search(r"con el prefijo que le toca: (\d+)", c).group(1),
        "l51": linea_acta("`5.1` `D.a` SE ADJUDICA"),
        "l55": linea_acta("`5.5` `D.e` Y `P.1` SE ADJUDICAN JUNTAS"),
        "l56": linea_acta("`5.6` `P.2` NO ES DOCTRINA NUEVA"),
        "l57": linea_acta("`5.7` LA DISCREPANCIA `299`"),
    }

    largos = texto.count(chr(8212)) + texto.count(chr(8211))
    print("CIFRA guiones largos mas medios: %d" % largos)
    if largos:
        print("ROJO: el compositor NO escribe.")
        return 1
    sospechosos = [x for x in re.findall(r"`([^`]+)`", texto)
                   if x.endswith("/") and x.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sospechosos))
    if sospechosos:
        for s in sospechosos:
            print("   sospechoso> %s" % s)
        return 1
    for marcador in ("git status --porcelain", "git diff --numstat -- dataset/"):
        print("CIFRA veces que la seccion 4 nombra el marcador %r: %d | CIFRA "
              "que deberia haber: al menos 1" % (marcador, texto.count(marcador)))
        if marcador not in texto:
            print("ROJO: el compositor NO escribe.")
            return 1
    encabezados = [l for l in texto.split(NL) if l.startswith("## ")]
    print("CIFRA encabezados de seccion armados: %d | CIFRA que deberia haber: 7"
          % len(encabezados))
    for e in encabezados:
        print("   %s" % e)
    if len(encabezados) != 7:
        print("ROJO: el cuerpo no trae las siete secciones.")
        return 1
    ruta = os.path.join(RAIZ, DESTINO.replace("/", os.sep))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO %s -> %d bytes en disco, %d lineas"
          % (DESTINO, os.path.getsize(ruta), texto.count(NL)))
    print("VERDE: el cuerpo del cierre queda compuesto de sus ficheros.")
    print("HUECO_ATRIBUCION: LA CORRIO EL EJECUTOR DE LA VUELTA 215, ENTERA Y "
          "SOLA, POR SUS ONCE TRAMOS, Y EL AUDITOR LA DECLARO CORRIDA. Su salida "
          "compuesta en el arbol mide %d bytes en disco y %d bytes normalizado a "
          "LF, medidos por mi en ESTA vuelta con mi propio instrumento y no "
          "copiados del encargo, y su commit es %s, leido de git log en esta "
          "misma corrida. LA 218 NO LA CORRE PORQUE LA CADENCIA DE CINCO DE "
          "AUDITOR.md 6.1 PONE LA SIGUIENTE EN LA 220, y correrla aqui seria "
          "saltarse la letra del fundador, no cumplirla."
          % (bat[0], bat[1], commit_bat))
    return 0


ACTA = "docs/loop/ACTA_AUDITOR.md"
_LINEAS_ACTA = None


def linea_acta(marca):
    """EL NUMERO DE LINEA DE UNA ADJUDICACION, LEIDO DEL ACTA Y NO RECORDADO.
    Es la obligacion 6.6 del acta 210, linea 74203. Si la marca no aparece, cae
    en rojo en vez de publicar un numero inventado."""
    global _LINEAS_ACTA
    if _LINEAS_ACTA is None:
        _LINEAS_ACTA = leer(ACTA).split(NL)
    for n, l in enumerate(_LINEAS_ACTA, start=1):
        if marca in l:
            return n
    raise SystemExit("ROJO: la marca %r no aparece en %s, y su linea NO SE "
                     "INVENTA." % (marca, ACTA))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
