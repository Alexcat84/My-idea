# -*- coding: utf-8 -*-
r"""_v206_cotejar_tramos.py . COMPUTO DE LA VUELTA 206, NO MAQUINARIA.

Prefijo de guion bajo: fuera del censo y fuera de la nomina (congelada en 135),
no anade guarda ni lector que se quede vigilando, muere con la vuelta.

QUE HACE: coteja MIS ONCE FILAS (medidas hoy contando los ficheros) contra LAS
ONCE FILAS DEL ACTA 205 DEL AUDITOR (leidas de docs/loop/ACTA_AUDITOR.md, que no
escribo). Si una discrepa, LA DECLARA; no la copia (`EJECUTOR.md` 2).

TRAE SU PRUEBA DE MUTACION (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR
MUTACION): `--mutar` altera UNA celda de mi lado y comprueba que el cotejo CAE.
Sin esa prueba, un cotejo que siempre dice VERDE no prueba nada.
"""
import hashlib
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")

RE_EXIT = re.compile(r"^EXITCODE DEL TRAMO (\d+): (\d+)\s*$", re.M)
RE_MIN = re.compile(r"^DURACION DEL TRAMO \(monotona, minutos\): ([0-9.]+)\s*$", re.M)
# LA FILA DEL ACTA: | n | disco | LF | lineas | sha | exitcode | minutos |
RE_FILA_ACTA = re.compile(
    r"^\|\s*(\d{1,2})\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*"
    r"([0-9a-f]{16})\s*\|\s*(\d+)\s*\|\s*([0-9.]+)\s*\|\s*$", re.M)


def mias():
    """MIS ONCE FILAS, CONTADAS DE LOS FICHEROS EN ESTA VUELTA."""
    filas = {}
    for n in range(1, 12):
        ruta = os.path.join(LOOP, "SALIDA_V205_BATERIA_TRAMO_%d.txt" % n)
        if not os.path.exists(ruta):
            continue
        crudo = io.open(ruta, "rb").read()
        lf = crudo.replace(b"\r\n", b"\n")
        texto = lf.decode("utf-8", "replace")
        ex = RE_EXIT.findall(texto)
        mi = RE_MIN.findall(texto)
        filas[n] = {
            "bytes_disco": len(crudo),
            "bytes_lf": len(lf),
            "lineas": lf.count(b"\n") + (0 if (not lf or lf.endswith(b"\n")) else 1),
            "sha256_lf": hashlib.sha256(lf).hexdigest()[:16],
            "exitcode": int(ex[-1][1]) if ex else None,
            "minutos": mi[-1] if mi else None,
        }
    return filas


def del_acta():
    """LAS ONCE FILAS DEL ACTA 205, LEIDAS DE SU TABLA. Se acota al bloque de la
    vuelta 205 para no barrer tablas de otras actas del mismo fichero."""
    texto = io.open(ACTA, encoding="utf-8", errors="replace").read().replace("\r\n", "\n")
    i = texto.rfind("# ACTA DEL AUDITOR, VUELTA 205")
    if i < 0:
        return {}, "el patron no encontro la cabecera del acta 205"
    bloque = texto[i:]
    j = bloque.find("## 3. LA RELECTURA CIEGA")
    if j > 0:
        bloque = bloque[:j]
    filas = {}
    for m in RE_FILA_ACTA.finditer(bloque):
        n = int(m.group(1))
        if 1 <= n <= 11 and n not in filas:
            filas[n] = {
                "bytes_disco": int(m.group(2)),
                "bytes_lf": int(m.group(3)),
                "lineas": int(m.group(4)),
                "sha256_lf": m.group(5),
                "exitcode": int(m.group(6)),
                "minutos": m.group(7),
            }
    return filas, None


CAMPOS = ["bytes_disco", "bytes_lf", "lineas", "sha256_lf", "exitcode", "minutos"]


def cotejar(a, b):
    """PURA. Devuelve la lista de discrepancias entre dos diccionarios de filas."""
    disc = []
    for n in sorted(set(a) | set(b)):
        if n not in a:
            disc.append("TRAMO %d: mi lado no lo tiene" % n)
            continue
        if n not in b:
            disc.append("TRAMO %d: el acta no lo tiene" % n)
            continue
        for c in CAMPOS:
            if str(a[n][c]) != str(b[n][c]):
                disc.append("TRAMO %d, campo %s: mio %s | acta %s"
                            % (n, c, a[n][c], b[n][c]))
    return disc


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    mutar = "--mutar" in sys.argv
    mis, acta_filas = mias(), None
    acta_filas, err = del_acta()
    print("EL COTEJO DE LAS ONCE FILAS: LAS MIAS DE HOY CONTRA LAS DEL ACTA 205")
    print("=" * 78)
    print("  CIFRA filas mias, contadas de los ficheros en esta vuelta: %d" % len(mis))
    if err:
        print("  %s" % err)
    print("  CIFRA filas leidas de la tabla del acta 205: %d" % len(acta_filas))
    if len(acta_filas) == 0:
        print("  EL PATRON NO ENCONTRO NINGUNA FILA EN EL ACTA. Eso no dice que no")
        print("  las haya: dice que mi patron no las vio, y asi se publica.")
    print("")

    disc = cotejar(mis, acta_filas)
    print("  CIFRA discrepancias: %d" % len(disc))
    for d in disc:
        print("      DISCREPANCIA: %s" % d)
    print("")
    print("  CIFRA suma de bytes de disco de los once (mia): %d"
          % sum(f["bytes_disco"] for f in mis.values()))
    print("  CIFRA suma de minutos de los once (mia): %.1f"
          % sum(float(f["minutos"]) for f in mis.values() if f["minutos"]))
    print("")

    if mutar:
        print("LA PRUEBA DE MUTACION, PORQUE UN COTEJO QUE SIEMPRE DICE VERDE NO PRUEBA")
        print("=" * 78)
        casos = 0
        caen = 0
        for n, campo, valor in [(1, "bytes_disco", 9556),
                                (3, "minutos", "11.3"),
                                (7, "sha256_lf", "427b396bd08b2fc9"),
                                (11, "exitcode", 0)]:
            copia = {k: dict(v) for k, v in mis.items()}
            copia[n][campo] = valor
            d = cotejar(copia, acta_filas)
            casos += 1
            cae = len(d) > len(disc)
            caen += 1 if cae else 0
            print("  MUTACION tramo %d campo %s -> %s : %s (%d discrepancia(s))"
                  % (n, campo, valor, "CAE" if cae else "NO CAE, Y ESO ES ROJO", len(d)))
        print("  CIFRA casos de mutacion: %d | CIFRA que CAEN: %d" % (casos, caen))
        if caen != casos:
            print("ROJO: alguna mutacion no tumbo el cotejo. El cotejo no vale.")
            return 1
        print("  VERDE: las %d mutaciones tumban el cotejo, o sea que muerde." % casos)
        print("")

    if disc:
        print("ROJO: hay discrepancias, y se DECLARAN. No se resuelven copiando.")
        return 1
    print("VERDE: las %d filas mias calzan al digito con las %d del acta 205."
          % (len(mis), len(acta_filas)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
