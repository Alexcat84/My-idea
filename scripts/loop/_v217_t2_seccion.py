# -*- coding: utf-8 -*-
r"""_v217_t2_seccion.py . EL CUERPO DE LA TAREA 2 DEL REPORTE DE LA VUELTA 217,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: cada tabla dice de que fichero
sale, cuantas filas armo y cuantas deberia haber, y se reconstruye contando ese
fichero antes de publicarla. La sede es
docs/loop/SALIDA_V217_T2_CIERRE.txt.

USO:  python scripts/loop/_v217_t2_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
SALIDA = "docs/loop/SALIDA_V%d_T2_CIERRE.txt" % VUELTA
DESTINO = "scripts/loop/_v%d_t2_seccion.md" % VUELTA


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def linea_con(texto, marca):
    for l in texto.split(NL):
        if marca in l:
            return l.strip()
    return None


def main():
    t = leer(SALIDA)
    ls = t.split(NL)
    b = io.open(os.path.join(RAIZ, SALIDA.replace("/", os.sep)), "rb").read()
    fallos = 0

    consolas = [l.strip() for l in ls if l.strip().startswith("CONSOLA ")]
    suites = [l.strip() for l in ls if l.strip().startswith("SUITE ")]
    cotejos = [l.strip() for l in ls if l.strip().startswith("COTEJO ")]
    sedes = [l.strip() for l in ls if l.strip().startswith("SEDE ")]
    tocados = [l.strip() for l in ls if l.strip().startswith("TOCADO ")]
    hueco = [l.strip() for l in ls if l.strip().startswith("DEL HUECO ")]
    ciclo = [l.strip() for l in ls if l.strip().startswith("SALIDA docs/loop/")]

    print("LO QUE ESTE COMPOSITOR CUENTA DE SU FICHERO, ANTES DE PUBLICAR NADA:")
    print("  SALIDA: %s -> %d bytes en disco y %d normalizado a LF"
          % (SALIDA, len(b), len(b.replace(b"\r\n", b"\n"))))
    for nombre, filas, esperado in (("salidas del ciclo", ciclo, 18),
                                    ("consolas", consolas, 2),
                                    ("suites", suites, 3),
                                    ("cotejos", cotejos, 16),
                                    ("sedes", sedes, 13),
                                    ("tocados", tocados, None),
                                    ("del hueco", hueco, 4)):
        print("  CIFRA filas de %-20s contadas del fichero: %2d | CIFRA que "
              "deberia haber: %s" % (nombre, len(filas), esperado
                                     if esperado is not None
                                     else "(la que salga: es la medicion)"))
        if esperado is not None and len(filas) != esperado:
            fallos += 1
    if fallos:
        print("ROJO: el compositor NO escribe. Fallos: %d" % fallos)
        return 1

    def L(m):
        x = linea_con(t, m)
        if x is None:
            raise SystemExit("ROJO: falta en la salida la linea %r" % m)
        return x

    filas_consola = []
    for l in consolas:
        m = re.match(r"CONSOLA (\S+)\s+(\S+) \| (\d+) bytes en disco y (\d+) "
                     r"normalizado a LF \| peor exitcode que declara: (.+)$", l)
        if m:
            filas_consola.append(m.groups())
    filas_suite = []
    for l in suites:
        m = re.match(r"SUITE (\S+)\s+(\S+) \| EXITCODE (\S+) \| (\d+) bytes en "
                     r"disco y (\d+) normalizado a LF$", l)
        if m:
            filas_suite.append(m.groups())
    filas_cotejo = []
    for l in cotejos:
        m = re.match(r"COTEJO (.+?)\s+\| LA MIA (\S+)\s+\| la del encargo "
                     r"(\S+)\s+\| CALZA: (\S+)$", l)
        if m:
            filas_cotejo.append(m.groups())
    print("  CIFRA filas de consola parseadas: %d de %d | de suite: %d de %d | "
          "de cotejo: %d de %d"
          % (len(filas_consola), len(consolas), len(filas_suite), len(suites),
             len(filas_cotejo), len(cotejos)))
    if (len(filas_consola) != 2 or len(filas_suite) != 3
            or len(filas_cotejo) != 16):
        print("ROJO: alguna fila de la salida no se deja leer entera.")
        return 1

    texto = """### TAREA 2. EL CIERRE INTEGRAL, MEDIDO DE SUS FICHEROS Y NO TECLEADO

**EL INSTRUMENTO ES `scripts/loop/_v%(v)d_t2_cierre.py` Y SU SALIDA SELLADA ES
`%(salida)s`, %(b)d bytes en disco y %(blf)d normalizado a LF.** Todas las
tablas de abajo se cuentan de ese fichero.

#### 2.a.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, CON SU CONSOLA SELLADA DESDE DENTRO

**%(lciclo)s**
**%(lausentes)s**
**%(lsinec)s**
**%(lpeor)s**

**EL REMEDIO DE LA 215 SE MANTIENE Y NO SE AFLOJA:** el ciclo sella su propia
consola desde dentro, en el nombre exacto que el compositor busca, y cae en rojo
por sus dos puertas, la del fichero **ausente** y la del fichero de **cero
bytes**.

**FILAS ARMADAS LEYENDO `%(salida)s`: %(nc)d. FILAS QUE DEBERIA HABER: 2.**

| lado | fichero de la consola | bytes, por las dos convenciones | peor exitcode que declara |
|---|---|---|---:|
%(tconsola)s

#### 2.a.2. LAS TRES SUITES SOLAS, CADA UNA CON SU EXITCODE Y SUS BYTES

**FILAS ARMADAS: %(ns)d. FILAS QUE DEBERIA HABER: 3.**

| suite | fichero | exitcode | bytes, por las dos convenciones |
|---|---|---:|---|
%(tsuite)s

#### 2.a.3. EL MARCADOR Y EL CENSO, RECOMPUTADOS CON SU COMANDO Y COTEJADOS SIN COPIAR

**LOS DOS COMANDOS, ESCRITOS ANTES DE SU RESULTADO:**
`python scripts/recomputar_marcador.py 3388` y
`python scripts/loop/vuelta83_conteo_aristas.py WORK`.

**FILAS ARMADAS: %(nco)d. FILAS QUE DEBERIA HABER: 16. LA COLUMNA DE LA
IZQUIERDA ES MIA Y LA DE LA DERECHA ES LA DEL ENCARGO**, y van separadas porque
son de autores distintos.

| cifra | LA MIA, recomputada hoy | la del encargo, del auditor | calzan |
|---|---:|---:|---|
%(tcotejo)s

**%(ldif)s**

#### 2.a.4. LAS SEDES, Y LA PRUEBA MEDIDA DE QUE ESTA VUELTA NO ESCRIBIO NI UNA FICHA

**%(lsedes)s**
**%(lvia)s**

```
%(tsedes)s
```

#### 2.a.5. LA MORATORIA, Y LA CIFRA CON SU HUECO AL LADO

**LA OBLIGACION DE DICTADO NUEVA DEL ENCARGO DE LA 217 SE CUMPLE AQUI, Y NACE DE
MI CAIDA DE LA 216:** aquella publico **16** ficheros escritos donde el auditor
conto **18**, porque el instrumento corre **antes** de que el cierre escriba los
suyos. La regla que el encargo fija es publicar **las dos cifras juntas**, la
medida y la que el propio cierre anade, y el hueco no se estima: **se nombra
fichero a fichero**.

**%(ltoc)s**

**%(lhueco)s**
**%(lpref)s**

```
%(ttocados)s
%(thueco)s
```

#### 2.a.6. LA FECHA, MEDIDA Y NO SUPUESTA

**%(lfap)s**
**%(lfci)s**

**%(lfallos)s**
""" % {
        "v": VUELTA,
        "salida": "`" + SALIDA + "`" if False else SALIDA,
        "b": len(b), "blf": len(b.replace(b"\r\n", b"\n")),
        "lciclo": L("CIFRA salidas selladas del ciclo:"),
        "lausentes": L("CIFRA ausentes:"),
        "lsinec": L("CIFRA salidas SIN exitcode dentro:"),
        "lpeor": L("CIFRA peor exitcode de las dieciocho:"),
        "nc": len(filas_consola),
        "tconsola": NL.join(
            "| **%s** | `%s` | **%s** bytes en disco y **%s** bytes normalizado a LF | %s |"
            % (a, b2, c, d, e) for a, b2, c, d, e in filas_consola),
        "ns": len(filas_suite),
        "tsuite": NL.join(
            "| **%s** | `%s` | **%s** | **%s** bytes en disco y **%s** bytes normalizado a LF |"
            % (a, b2, c, d, e) for a, b2, c, d, e in filas_suite),
        "nco": len(filas_cotejo),
        "tcotejo": NL.join("| %s | **%s** | %s | %s |" % g for g in filas_cotejo),
        "ldif": L("CIFRA cifras cotejadas:"),
        "lsedes": L("CIFRA sedes cotejadas:"),
        "lvia": L("CIFRA sedes cuya quietud se midio por sha256"),
        "tsedes": NL.join(sedes),
        "ltoc": L("CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA:"),
        "lhueco": L("CIFRA MEDIDA AHORA:"),
        "lpref": L("Y LOS DEL HUECO LLEVAN EL PREFIJO IGUAL:"),
        "ttocados": NL.join(tocados),
        "thueco": NL.join(hueco),
        "lfap": L("fecha del commit de apertura, leida de git log:"),
        "lfci": L("fecha del commit de ahora mismo, leida de git log:"),
        "lfallos": L("CIFRA comprobaciones que fallan:"),
    }

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
