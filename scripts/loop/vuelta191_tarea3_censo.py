# -*- coding: utf-8 -*-
r"""vuelta191_tarea3_censo.py . EL CENSO DE LAS DOS CONVENCIONES DE `lineas`,
SELLADO ANTES Y DESPUES DEL ARREGLO.

POR QUE EXISTE, Y ES UNA REGLA DE LA CASA Y NO UN CAPRICHO: `EJECUTOR.md` 1, **LA
TABLA SE CUENTA DE SU FICHERO**. La cifra de ANTES del arreglo no se puede pedir
al instrumento del arreglo una vez arreglado, porque **ya no existe el estado que
la produjo**. Aqui se reconstruye del unico sitio donde ese estado sigue vivo:
**git**.

COMO. Saca los `scripts/loop/*.py` del commit que se le pida a un directorio
temporal y corre sobre ellos **EL DETECTOR DE HOY**, el mismo que corre sobre el
arbol de trabajo. Dos estados del sujeto, UN SOLO instrumento: si se corrieran dos
detectores distintos, la diferencia no seria del arreglo sino de la vara.

QUE ESCRIBE, Y LAS DOS RUTAS PROMETEN PRUEBA Y POR ESO SE MIDEN:
  . `docs/loop/SALIDA_V191_T3_CENSO_ANTES.txt`
  . `docs/loop/SALIDA_V191_T3_CENSO_DESPUES.txt`

LO QUE NO HACE: no arregla nada, no toca ningun fichero del repo y no corre
ningun script sacado de git. Solo LEE.

USO:
  python scripts/loop/vuelta191_tarea3_censo.py --commit HEAD
"""
import argparse
import io
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dos_convenciones_de_lineas as DC   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def informe(titulo, filas, extra=()):
    L = []
    w = L.append
    w("=" * 78)
    w(titulo)
    w("=" * 78)
    w("")
    for l in extra:
        w(l)
    if extra:
        w("")
    w("LA VARA, LA MISMA EN LOS DOS CENSOS:")
    w("   `len(texto.split(NL))` cuenta TROZOS y da UNO DE MAS. NO calza con wc -l.")
    w("   `texto.count(NL)` cuenta SALTOS y SI calza con wc -l.")
    w("   `len(texto.splitlines())` calza cuando el texto termina en salto.")
    w("   `len(texto.split(NL)) - 1` es la SPLIT ya corregida y SI calza.")
    w("   ROJO es una cosa sola: contar por SPLIT y por ninguna de las que calzan.")
    w("")
    reparto = {}
    for _n, v, _s in filas:
        reparto[v] = reparto.get(v, 0) + 1
    w("A) EL REPARTO")
    w("   CIFRA ficheros .py censados: %d" % len(filas))
    for v in (DC.ROJO, DC.VERDE_PAREJA, DC.VERDE_CALZA, DC.NO_APLICA):
        w("   %-64s %d" % (v, reparto.get(v, 0)))
    w("")
    rojos = [(n, s) for n, v, s in filas if v == DC.ROJO]
    w("B) LOS FICHEROS EN ROJO, NOMBRADOS UNO A UNO CON SUS SITIOS")
    if not rojos:
        w("   (ninguno)")
    for n, s in rojos:
        w("   %s -> %d sitio(s) SPLIT sin corregir, 0 que calcen" % (n, len(s["split"])))
        for i, t in s["split"]:
            w("      LINEA %-5d %s" % (i, t))
    w("   CIFRA ficheros en ROJO: %d" % len(rojos))
    w("")
    tot = {"split": 0, "count": 0, "splitlines": 0, "split_corregido": 0}
    for _n, _v, s in filas:
        for k in tot:
            tot[k] += len(s[k])
    w("C) LOS SITIOS, QUE ES EL TAMANO DEL ASUNTO")
    for k in ("split", "count", "splitlines", "split_corregido"):
        w("   CIFRA sitios %-16s %d" % (k, tot[k]))
    w("")
    w("VEREDICTO: %s" % ("ROJO, %d fichero(s)" % len(rojos) if rojos
                         else "VERDE, ninguno en rojo"))
    return NL.join(L) + NL


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", default="HEAD")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    c, sha = git(["rev-parse", a.commit])
    sha = sha.strip()
    c, asunto = git(["log", "-1", "--format=%s", sha])
    asunto = asunto.strip()

    # ---------------------------------------------------------------- ANTES
    tmp = tempfile.mkdtemp(prefix="v191_censo_antes_")
    try:
        c, lista = git(["ls-tree", "--name-only", "%s:scripts/loop" % sha])
        nombres = [l.strip() for l in lista.splitlines()
                   if l.strip().endswith(".py")]
        for n in nombres:
            c2, blob = git(["show", "%s:scripts/loop/%s" % (sha, n)])
            if c2 != 0:
                continue
            io.open(os.path.join(tmp, n), "w", encoding="utf-8",
                    newline=NL).write(blob)
        filas_antes = DC.censo(tmp)
        texto = informe(
            "CENSO DE LAS DOS CONVENCIONES DE `lineas`, ANTES DEL ARREGLO",
            filas_antes,
            extra=["EL SUJETO: `scripts/loop/*.py` del commit %s" % sha[:8],
                   "   asunto: %s" % asunto[:120],
                   "   sacados con `git show` a un directorio temporal y LEIDOS,",
                   "   nunca corridos.",
                   "EL INSTRUMENTO: el detector de HOY, el mismo que corre sobre el",
                   "   arbol de trabajo. Dos estados del sujeto, UNA sola vara.",
                   "CIFRA ficheros .py sacados de git: %d" % len(nombres)])
        ruta = os.path.join(LOOP, "SALIDA_V191_T3_CENSO_ANTES.txt")
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
        print(texto)
        print("ESCRITO: docs/loop/SALIDA_V191_T3_CENSO_ANTES.txt (%d bytes)"
              % len(texto.encode("utf-8")))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # -------------------------------------------------------------- DESPUES
    filas_desp = DC.censo(os.path.join(RAIZ, "scripts", "loop"))
    texto = informe(
        "CENSO DE LAS DOS CONVENCIONES DE `lineas`, DESPUES DEL ARREGLO",
        filas_desp,
        extra=["EL SUJETO: `scripts/loop/*.py` del ARBOL DE TRABAJO de hoy.",
               "EL INSTRUMENTO: el mismo detector que el censo de ANTES."])
    ruta = os.path.join(LOOP, "SALIDA_V191_T3_CENSO_DESPUES.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: docs/loop/SALIDA_V191_T3_CENSO_DESPUES.txt (%d bytes)"
          % len(texto.encode("utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
