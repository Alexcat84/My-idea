# -*- coding: utf-8 -*-
"""El cotejo byte a byte de las TRES copias del reporte de la 179. Se corre
DESPUES del archivo definitivo y escribe FUERA del reporte, que es lo unico que
rompe la circularidad."""
import hashlib
import io
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
COMMIT = sys.argv[1]


def sha(b):
    return hashlib.sha256(b).hexdigest()


arb = io.open("docs/loop/REPORTE.md", "rb").read()
arc = io.open("docs/loop/reportes/REPORTE_V179.md", "rb").read()
git = subprocess.run(["git", "show", COMMIT + ":docs/loop/REPORTE.md"],
                     capture_output=True).stdout
print("EL COTEJO BYTE A BYTE DE LAS TRES COPIAS DEL REPORTE DE LA VUELTA 179")
print("(el arbol, el archivo, y lo que git guarda en el commit del cierre %s)" % COMMIT)
print("")
print("| copia | bytes en disco | bytes normalizados a LF | sha256 (LF) |")
print("|---|---:|---:|---|")
for n, b in ((("el arbol, `docs/loop/REPORTE.md`"), arb),
             (("el archivo, `docs/loop/reportes/REPORTE_V179.md`"), arc),
             (("git, `%s:docs/loop/REPORTE.md`" % COMMIT), git)):
    lf = b.replace(chr(13).encode(), b"")
    print("| %s | %d | %d | `%s` |" % (n, len(b), len(lf), sha(lf)[:16]))
lfs = {sha(b.replace(chr(13).encode(), b"")) for b in (arb, arc, git)}
print("")
print("CIFRA sha256 distintos entre las tres: %d" % len(lfs))
print("LAS TRES CALZAN BYTE A BYTE NORMALIZADO A LF: %s" % ("SI" if len(lfs) == 1 else "NO"))
print("FIN")
sys.exit(0 if len(lfs) == 1 else 1)
