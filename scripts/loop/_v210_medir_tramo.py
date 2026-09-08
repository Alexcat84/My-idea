# -*- coding: utf-8 -*-
r"""_v210_medir_tramo.py . LAS CIFRAS DE UN TRAMO DE LA BATERIA, LEIDAS DE SU
FICHERO SELLADO PARA QUE EL MENSAJE DEL COMMIT NO SE TECLEE.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo, fuera de la
nomina (congelada en 135), no vigila nada y muere con la vuelta. NO ES UN ARNES
NI UNA GUARDA NI UN LECTOR NUEVO en el sentido de la moratoria de `AUDITOR.md`
6.3: no se queda mirando nada ni entra en ninguna nomina. Es lo que el encargo
de la 210 llama, con estas palabras, "todo tu computo va con prefijo `_v210_*`".

IMPORTAR NO ES CLONAR (acta 206, adjudicacion `6.5`). `medir`, `nombre_tramo` y
`entradas_de_la_salida` se IMPORTAN del lanzador
`scripts/loop/vuelta183_bateria_por_tramos.py`, que es su sede unica y al que
esta vuelta NO le toca una linea. Aqui no se copia ni una de esas funciones.

POR QUE ESTAS CIFRAS Y NO OTRAS: son las que `EJECUTOR.md` 1 exige que el commit
de cada tramo publique (las dos convenciones de bytes, el `sha256`, el exitcode
y el reloj) y las que hacen comparable el CALIBRE de un tramo con el de sus diez
hermanos (entradas corridas y el reparto de sus veredictos).

USO:  python scripts/loop/_v210_medir_tramo.py 1
"""
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from vuelta183_bateria_por_tramos import (  # noqa: E402
    medir, nombre_tramo, entradas_de_la_salida, LOOP, RAIZ)

NL = chr(10)
PATRON_FILA = re.compile(r"^  (\S+\.py)\s+exit (-?\d+)\s+(.+?)\s+([\d.]+)s\s*$")


def uno(texto, patron):
    m = re.findall(patron, texto)
    return m[0] if len(m) == 1 else None


def main():
    n = int(sys.argv[1])
    ruta = os.path.join(LOOP, nombre_tramo(n))
    if not os.path.exists(ruta):
        print("ROJO: %s NO EXISTE (ausencia, no cero)." % nombre_tramo(n))
        return 1
    m = medir(ruta)
    texto = io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    entradas = entradas_de_la_salida(ruta)
    filas = [PATRON_FILA.match(l) for l in texto.split(NL)]
    filas = [f for f in filas if f]
    clases = {}
    for f in filas:
        clases[f.group(3).strip()] = clases.get(f.group(3).strip(), 0) + 1

    r = subprocess.run(["git", "log", "-1", "--format=%H %s", "--",
                        "docs/loop/" + nombre_tramo(n)],
                       cwd=RAIZ, capture_output=True)
    ultimo = r.stdout.decode("utf-8", errors="replace").strip()

    print("TRAMO %d, MEDIDO DE SU PROPIO FICHERO SELLADO Y NO TECLEADO" % n)
    print("  fichero: docs/loop/%s" % nombre_tramo(n))
    print("  CIFRA bytes en disco: %d" % m["bytes_disco"])
    print("  CIFRA bytes normalizado a LF: %d" % m["bytes_lf"])
    print("  CIFRA lineas: %d" % m["lineas"])
    print("  CIFRA sha256 (LF): %s" % m["sha256_lf"])
    print("  CIFRA sha256 (LF), primeros 16: %s" % m["sha256_lf"][:16])
    print("  CIFRA entradas que el tramo dice haber corrido: %d" % len(entradas))
    print("  CIFRA filas de veredicto por arnes: %d" % len(filas))
    print("  EL REPARTO DE VEREDICTOS, CONTADO DE LAS FILAS:")
    for k in sorted(clases):
        print("      %-22s %d" % (k, clases[k]))
    for etiqueta, patron in (
            ("ANCLA PERDIDA", r"ANCLA PERDIDA  : (\d+)"),
            ("NO MORDIO", r"NO MORDIO      : (\d+)"),
            ("NO REPRODUCIBLE", r"NO REPRODUCIBLE: (\d+)"),
            ("CASO DECLARADO", r"CASO DECLARADO : (\d+)"),
            ("RUIDO DE CONCURRENCIA", r"RUIDO DE CONCURRENCIA: (\d+) fichero"),
            ("FUERA DE LA NOMINA", r"que se quedan FUERA de la nomina \(recomputado al cierre\): (\d+)"),
            ("INVISIBLES AL CENSO", r"CIFRA entradas de la nomina que el censo NO VE \(recomputado al cierre\): (\d+)"),
            ("SUJETO NO CONGELADO", r"CIFRA entradas cuyo SUJETO NO ESTA CONGELADO \(recomputado al cierre\): (\d+)"),
            ("TIEMPO segundos", r"CIFRA TIEMPO TOTAL de la bateria, en segundos: ([\d.]+)"),
            ("EXITCODE DEL TRAMO", r"EXITCODE DEL TRAMO %d: (-?\d+)" % n),
            ("DURACION minutos", r"DURACION DEL TRAMO \(monotona, minutos\): ([\d.]+)"),
            ("INICIO UTC", r"INICIO \(reloj de pared, UTC\): (\S+)"),
            ("FIN UTC", r"FIN \(reloj de pared, UTC\): (\S+)")):
        print("  CIFRA %-22s %s" % (etiqueta + ":", uno(texto, patron)))
    v = re.findall(r"^VEREDICTO DE ESTA CORRIDA: (.+)$", texto, re.M)
    print("  CLASE DEL VEREDICTO: %s" % (v[0] if len(v) == 1 else "(no unica: %d)" % len(v)))
    print("  ultimo commit que toco el fichero, ANTES de este: %s" % ultimo[:110])
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
