# -*- coding: utf-8 -*-
r"""_v218_t2_seccion.py . EL CUERPO DE LA TAREA 2 DEL REPORTE DE LA VUELTA 218,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO. Ninguna celda se teclea: las
filas se leen de docs/loop/SALIDA_V218_T2_LECTURAS.txt y el compositor DICE
cuantas armo y cuantas deberia haber.

USO:  python scripts/loop/_v218_t2_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
SALIDA = "docs/loop/SALIDA_V%d_T2_LECTURAS.txt" % VUELTA
DESTINO = "scripts/loop/_v%d_t2_seccion.md" % VUELTA

DISCUTIBLES = [
    ("D.4", "`01 FUENTES` idx 0, CUAL de las dos varas del ANTES manda",
     "Publico **CUBRE**, y la subida entera descansa en una eleccion mia: **el "
     "ANTES de una clausula de `OP-F-01` es la VISPERA DE LA FASE 01, no el "
     "grafo previo a la campana**. Contra la vispera, **6 de 6** miembros son "
     "identicos byte a byte; contra el grafo previo, **2 de 6** tienen texto "
     "distinto. Mi motivo: la clausula verifica lo que la fase 01 hizo, y "
     "cobrarle a la fase 01 dos reescrituras de voz del **8 ago 2026**, cinco "
     "dias antes de que la fase existiera, seria medirla con lo que otro "
     "movio. **Si el auditor lee que el ANTES es el grafo previo y punto, esta "
     "clausula vuelve a A MEDIAS** y el recuento vuelve a 12 y 5."),
    ("D.5", "`02 DESTEJIDOS` idx 1, la lectura contra el detector",
     "Publico **CUBRE**. Las cuatro fichas que la regla estrecha no ve tienen "
     "su perdida **escrita en el bloque del que proviene**, y cada una con su "
     "linea de la pagina 02 leida del fichero. **La duda que dejo escrita**: "
     "para `OP-D-01` perdida 1 la respuesta no es una frase sino **una tabla**, "
     "la del reparto por origen de la linea 209, y para `OP-D-03` perdida 1 la "
     "respuesta es **donde vive hoy** el material y no donde se escribio la "
     "regla. **Si el auditor lee que la clausula exige la frase y no el hecho**, "
     "estas dos no cuentan y la clausula se queda en A MEDIAS."),
    ("D.6", "que la 2.b no lleva caso rojo automatico",
     "Lo digo yo antes de que me lo pregunten. **La maquina localiza el ancla y "
     "publica su linea verbatim; el juicio de si esa linea contesta la pregunta "
     "es MIO.** No fabrico un mutante que se apruebe solo sobre una tabla a "
     "mano, que es la caida que la casa lleva cazada desde la vuelta 89. **Lo "
     "que si es maquina y si cae en rojo: las 13 anclas se buscan en el fichero "
     "y una que no aparezca es fallo.**"),
]


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def medir(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    b = io.open(p, "rb").read()
    return len(b), len(b.replace(b"\r\n", b"\n"))


def L(texto, marca):
    for l in texto.split(NL):
        if marca in l:
            return l.strip()
    raise SystemExit("ROJO: falta la linea %r" % marca)


def bloque(texto, desde, hasta):
    ls = texto.split(NL)
    i = next(n for n, l in enumerate(ls) if desde in l)
    j = next(n for n, l in enumerate(ls) if n > i and hasta in l)
    return ls[i + 1:j]


def main():
    print("LA SEDE QUE ESTE CUERPO CITA COMO PRUEBA, MEDIDA ANTES DE CITARLA:")
    m = medir(SALIDA)
    if m is None or m[0] == 0:
        print("   ROJO: %s no existe o mide cero bytes" % SALIDA)
        return 1
    print("   %-52s %7d bytes en disco y %7d normalizado a LF"
          % (SALIDA, m[0], m[1]))
    t = leer(SALIDA)

    clase = [l.rstrip() for l in t.split(NL) if "igual al previo:" in l]
    print("CIFRA filas de la clase armadas leyendo la salida: %d | CIFRA que "
          "deberia haber: 6" % len(clase))
    if len(clase) != 6:
        return 1

    anclas = [l.rstrip() for l in t.split(NL)
              if re.match(r"^\s+linea \d+ de docs/plan/02_DESTEJIDOS\.md:", l)]
    print("CIFRA lineas de ancla armadas leyendo la salida: %d | CIFRA que "
          "deberia haber: 13" % len(anclas))
    if len(anclas) != 13:
        return 1

    tabla = [l for l in t.split(NL) if re.match(r"^\| \d+ \| ", l)]
    print("CIFRA filas de la tabla de las diecisiete armadas leyendo la salida: "
          "%d | CIFRA que deberia haber: 17" % len(tabla))
    if len(tabla) != 17:
        return 1

    resto = bloque(t, "LAS QUE SIGUEN SIN CUBRIR, CON SU FILA",
                   "CIFRA clausulas que siguen sin cubrir")
    print("CIFRA filas de las que siguen sin cubrir: %d | CIFRA que deberia "
          "haber: 4" % len(resto))
    if len(resto) != 4:
        return 1

    pasos = [l.rstrip() for l in t.split(NL)
             if l.strip().startswith("commit ") and "pasos que ESTE commit" in l]
    print("CIFRA filas de atribucion por commit armadas: %d | CIFRA que deberia "
          "haber: 8" % len(pasos))
    if len(pasos) != 8:
        return 1

    texto = """### TAREA 2. LAS DOS LECTURAS QUE CIERRAN DOS DE LAS SEIS CLAUSULAS

**LO QUE SE CORRIO, Y SU RUTA CON SUS BYTES:**
``%(salida)s``, **%(bd)d bytes en disco y %(bl)d normalizado a LF**, exitcode 0.

**ES LECTURA Y NO INSTRUMENTO NUEVO**, que es lo que el encargo pide y lo que la
moratoria protege: los lectores se **IMPORTAN** y lo unico propio de esta vuelta
son las dos preguntas y sus anclas.

#### 2.a. LOS DOS NODOS DE LA CLASE CON TEXTO DISTINTO, LEIDOS

**LA VARA DEL ANTES SE PARTE EN DOS Y LAS DOS SE PUBLICAN, PORQUE LA RESPUESTA
DEPENDE DE CUAL SE USE Y ESO NO SE ESCONDE:**

```
%(varas)s
```

**LA CLASE, MIEMBRO A MIEMBRO** (%(nclase)d filas leidas del fichero, 6 que
deberia haber):

```
%(clase)s
```

```
%(cifras)s
```

**LA ATRIBUCION NO ES UN PROXY, Y ESA ERA LA OBJECION.** Mi razon de la 217
decia que el asunto de un commit es un proxy y no una lectura, y tenia razon.
**Aqui no se lee el asunto: se recorre el historial del fichero de cada nodo y se
mide QUE PASOS cambia cada commit**, uno por uno (%(npasos)d filas leidas del
fichero, 8 que deberia haber):

```
%(pasos)s
```

**QUE DICE HOY Y QUE DECIA ANTES, LOS DOS NODOS, PASO POR PASO**, esta entero en
la salida sellada y **no se repite aqui a proposito**: son 15 pasos con sus dos
versiones y duplicarlos seria dos versiones de lo mismo. La muestra que fija la
especie, y es la especie de las quince: donde antes decia *Analizar el territorio
actual cubierto y su compatibilidad con **los** objetivos*, hoy dice *con **tus**
objetivos*. **Es reescritura de VOZ, no de contenido.**

**MI VEREDICTO, CON LA LECTURA DETRAS:** las dos alteraciones entran por dos
commits del **8 ago 2026**, `4542e482` y `f0364e94`, de la curaduria de packs y
del catalogo de hallazgos. **El primer commit de la rama que nombra una operacion
`OP-F` es del 13 ago 2026**, cinco dias despues. **Ninguno de los ocho commits
que tocaron los dos ficheros cambia un paso y ademas nombra una operacion de la
fase 01: la cifra es CERO.** Y contra la vispera de la fase 01 los **6 de 6**
miembros son identicos byte a byte. **La clausula sube a CUBRE, y sube por
lectura.**

#### 2.b. LAS CUATRO FICHAS DE `02 DESTEJIDOS`, LEIDAS UNA A UNA

**LA PREGUNTA ES UNA SOLA POR PERDIDA:** esta escrita en el bloque del que
proviene, si o no, con su linea de `docs/plan/02_DESTEJIDOS.md`. **Las lineas se
LOCALIZAN en el fichero y no se teclean.**

```
%(fichas)s
```

**LAS TRECE LINEAS QUE CONTESTAN, CON SU NUMERO LEIDO DEL FICHERO**
(%(nanclas)d lineas de ancla armadas, 13 que deberia haber):

```
%(anclas)s
```

```
%(cuenta)s
```

**MI VEREDICTO, CON LA LECTURA DETRAS: LAS CUATRO DAN SI.** `OP-D-01` tiene el
reparto **por origen y con su motivo de perdida** en la tabla impresa desde el
plan sellado, y sus tres narraciones ausentes **con su fecha y su operacion**;
`OP-D-02` tiene la evaluacion preliminar y el analisis competitivo **con sus dos
origenes nombrados**, y el bloque de Coleman **entero y verbatim**; `OP-D-03`
tiene los tres materiales **comprobados donde viven hoy**, uno por nodo vivo; y
`OP-D-07` tiene los cinco pasos del punto brillante **uno a uno y verbatim, con
el numero que tenian y el que tienen**. **Con las 5 que la regla estrecha ya veia
son 9 de 9, y la clausula sube a CUBRE por lectura y no por detector**, que es lo
que el banco `9.6.2` manda cuando dice que la direccion se verifica leyendo y no
contando palabras.

#### 2.c. EL RECUENTO, RECOMPUTADO AL CIERRE Y NO HEREDADO

**EL ESTADO AL CIERRE SE MIDE AL CIERRE** (`EJECUTOR.md` 1). La TAREA 1 dejo 11 y
6, esta tarea mueve DOS, y el recuento se rehace:

```
%(recuento)s
```

**LA TABLA ENTERA AL CIERRE** (%(ntabla)d filas leidas del fichero, 17 que
deberia haber):

%(tabla)s

**LAS QUE SIGUEN SIN CUBRIR, CON SU FILA, SU INDICE Y SU CIFRA** (%(nresto)d
lineas leidas del fichero, 4 que deberia haber):

```
%(resto)s
```

#### 2.d. ESTA TAREA SOLO LEE, Y SE PRUEBA CON LOS OCHO SHA

```
%(sha)s
```

#### 2.e. LOS DISCUTIBLES DE ESTA TAREA, MARCADOS ANTES DE SABER SI ACIERTO

**Son lectura mia y por eso van aparte** (`EJECUTOR.md` 7). **Tres.**

| # | sobre que | que decidi y cual es la duda |
|---|---|---|
%(disc)s
""" % {
        "salida": SALIDA, "bd": m[0], "bl": m[1],
        "varas": NL.join([
            L(t, "VARA 1 DEL ANTES, EL GRAFO PREVIO A LA CAMPANA:"),
            L(t, "primer commit que nombra OP-F:"),
            L(t, "su padre, LA VISPERA:")]),
        "nclase": len(clase),
        "clase": NL.join(x.strip() for x in clase),
        "cifras": NL.join([
            L(t, "CIFRA miembros con TEXTO distinto contra el GRAFO PREVIO:"),
            L(t, "CIFRA miembros con TEXTO distinto contra LA VISPERA"),
            L(t, "CIFRA miembros con el NUMERO de pasos alterado")]),
        "npasos": len(pasos),
        "pasos": NL.join(x.strip() for x in pasos),
        "fichas": NL.join([l.strip() for l in t.split(NL)
                           if re.match(r"^\s+OP-D-\d+ \| linea \d+", l)]
                          + [L(t, "CIFRA perdidas declaradas por las cuatro")]),
        "nanclas": len(anclas),
        "anclas": NL.join(x.strip() for x in anclas),
        "cuenta": NL.join([
            L(t, "CIFRA anclas buscadas:"),
            L(t, "CIFRA fichas leidas:"),
            L(t, "CIFRA fichas que contestan SI a la pregunta:"),
            L(t, "CIFRA fichas de la fase 02: 9 |")]),
        "recuento": NL.join([
            L(t, "CIFRA clausulas que esta tarea mueve:"),
            L(t, "CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2:"),
            L(t, "CIFRA clausulas en A MEDIAS AL CIERRE DE LA TAREA 2:"),
            L(t, "CIFRA clausulas en NO CUBRE AL CIERRE DE LA TAREA 2:"),
            L(t, "CIFRA en CUBRE:"),
            L(t, "LA CONDICION SE CUMPLE:")]),
        "ntabla": len(tabla),
        "tabla": NL.join(["| # | fila | idx | veredicto | la clausula, VERBATIM |",
                          "|---:|---|---:|---|---|"] + tabla),
        "nresto": len(resto),
        "resto": NL.join(x.strip() for x in resto),
        "sha": NL.join([l.strip() for l in t.split(NL)
                        if l.startswith("SHA256 DE docs/plan/")]
                       + [L(t, "LOS OCHO SHA DEL PLAN COINCIDEN")]),
        "disc": NL.join("| **%s** | %s | %s |" % (a, b, c)
                        for a, b, c in DISCUTIBLES),
    }

    mayores = [l for l in texto.split(NL)
               if l.startswith("## ") and not l.startswith("### ")]
    print("CIFRA encabezados de nivel dos en el cuerpo del anexo: %d | CIFRA "
          "que deberia haber: 0" % len(mayores))
    if mayores:
        return 1
    largos = texto.count(chr(8212)) + texto.count(chr(8211))
    print("CIFRA guiones largos mas medios en el cuerpo: %d" % largos)
    if largos:
        print("ROJO: el compositor NO escribe.")
        return 1
    sospechosos = [c for c in re.findall(r"`([^`]+)`", texto)
                   if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sospechosos))
    if sospechosos:
        for s in sospechosos:
            print("   sospechoso> %s" % s)
        return 1
    ruta = os.path.join(RAIZ, DESTINO.replace("/", os.sep))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO %s -> %d bytes en disco, %d lineas"
          % (DESTINO, os.path.getsize(ruta), texto.count(NL)))
    print("VERDE: el cuerpo de la TAREA 2 queda compuesto de su fichero.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
