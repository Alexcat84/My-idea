# -*- coding: utf-8 -*-
"""vuelta102_tarea1_prueba_mutacion_apertura.py . PRUEBA DE MUTACION del
arreglo de scripts/loop/verificar_apertura_sellada.py (TAREA 1.3 de la
vuelta 102, acta de la vuelta 101, "PRIMERA, DE REPORTE, Y ACUMULA": la
guarda se envenenaba con su propia salida de prueba).

Corre los tres casos que el encargo pide, y NADA MAS:

  (a) VERDE sobre la vuelta 101 DESPUES del arreglo, con
      docs/loop/SALIDA_V101_TAREA1_2_MUTACION_APERTURA.txt todavia presente
      en el arbol de trabajo (la guarda ya no se la come).
  (b) ROJO sobre la vuelta 100, que sigue siendo el caso negativo real, sin
      cambios de comportamiento.
  (c) ROJO si un fichero de apertura REAL (sin la palabra MUTACION en el
      nombre) se mueve a mano al SEGUNDO commit de la vuelta. Esto se prueba
      en una COPIA TEMPORAL de repositorio, construida desde cero con git
      init (nunca sobre el repo real): dos commits sinteticos, el primero
      "ACTA DE LA VUELTA 4 DEL AUDITOR" con un fichero de apertura ya
      sellado, el segundo que anade UN SEGUNDO fichero de apertura tarde.
      Prueba tambien, de paso, que un fichero con MUTACION en el nombre
      anadido en ese mismo segundo commit NO tumba la guarda (es la mitad
      que confirma que el arreglo no volvio a poner en riesgo el caso (a)).

USO:
  python scripts/loop/vuelta102_tarea1_prueba_mutacion_apertura.py

Sale con exit 0 solo si los tres casos dan el veredicto esperado; imprime
cada caso con su veredicto real y sale con exit 1 en cuanto alguno no calza.
"""
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_apertura_sellada.py")


def correr(args, cwd):
    r = subprocess.run([sys.executable] + args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def git(args, cwd, env=None):
    r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True, env=env)
    if r.returncode != 0:
        raise SystemExit("git %s fallo: %s" % (" ".join(args), r.stderr))
    return r.stdout


def caso_a(fallos):
    codigo, salida = correr([GUARDA, "--vuelta", "101"], RAIZ)
    ok = codigo == 0 and salida.startswith("VERDE")
    print("--- CASO (a): --vuelta 101 sobre el repo real, DESPUES del arreglo ---")
    print(salida.strip())
    if not ok:
        fallos.append("caso (a): se esperaba VERDE (exit 0) y salio exit %d" % codigo)
    else:
        print("CASO (a): OK (VERDE, exit 0)")
    print()


def caso_b(fallos):
    codigo, salida = correr([GUARDA, "--vuelta", "100"], RAIZ)
    ok = codigo == 1 and salida.startswith("ROJO")
    print("--- CASO (b): --vuelta 100 sobre el repo real, caso negativo sin cambios ---")
    print(salida.strip())
    if not ok:
        fallos.append("caso (b): se esperaba ROJO (exit 1) y salio exit %d" % codigo)
    else:
        print("CASO (b): OK (ROJO, exit 1)")
    print()


def caso_c(fallos):
    print("--- CASO (c): fichero de apertura movido al 2.o commit, en copia temporal ---")
    tmp = tempfile.mkdtemp(prefix="v102_tarea13_")
    try:
        env = dict(os.environ)
        env["GIT_AUTHOR_NAME"] = env["GIT_COMMITTER_NAME"] = "prueba-mutacion"
        env["GIT_AUTHOR_EMAIL"] = env["GIT_COMMITTER_EMAIL"] = "prueba@local"

        git(["init", "-q"], tmp, env)
        os.makedirs(os.path.join(tmp, "scripts", "loop"))
        os.makedirs(os.path.join(tmp, "docs", "loop"))
        shutil.copyfile(GUARDA, os.path.join(tmp, "scripts", "loop", "verificar_apertura_sellada.py"))

        # commit 0: EL ACTA de la vuelta "4", sin ningun fichero de apertura
        # (root commit propio, para que el commit 1 tenga un padre real).
        with open(os.path.join(tmp, "README_ACTA.txt"), "w") as f:
            f.write("acta sintetica\n")
        git(["add", "-A"], tmp, env)
        git(["commit", "-q", "-m", "ACTA DE LA VUELTA 4 DEL AUDITOR: acta sintetica de la prueba"], tmp, env)

        # commit 1: EL PRIMER commit de la vuelta "5", hijo directo del acta,
        # con el UNICO fichero de apertura que nace a tiempo.
        with open(os.path.join(tmp, "docs", "loop", "SALIDA_V5_HEAD_APERTURA.txt"), "w") as f:
            f.write("sello sintetico, sellado a tiempo\n")
        git(["add", "-A"], tmp, env)
        git(["commit", "-q", "-m", "VUELTA 5: apertura sellada"], tmp, env)

        # commit 2: UN SEGUNDO fichero de apertura real (sin MUTACION en el
        # nombre) que llega tarde, MAS un fichero de prueba de mutacion (con
        # MUTACION en el nombre) que llega en el mismo commit y NO debe
        # contarse como apertura.
        with open(os.path.join(tmp, "docs", "loop", "SALIDA_V5_TARDIO_APERTURA.txt"), "w") as f:
            f.write("fichero de apertura real que llego tarde\n")
        with open(os.path.join(tmp, "docs", "loop", "SALIDA_V5_TAREA_X_MUTACION_APERTURA.txt"), "w") as f:
            f.write("salida de una prueba de mutacion, no una medicion\n")
        git(["add", "-A"], tmp, env)
        git(["commit", "-q", "-m", "VUELTA 5: TAREA 1, segundo commit"], tmp, env)

        codigo, salida = correr(
            [os.path.join(tmp, "scripts", "loop", "verificar_apertura_sellada.py"), "--vuelta", "5"], tmp)
        print(salida.strip())
        ok = codigo == 1 and salida.startswith("ROJO") and "SALIDA_V5_TARDIO_APERTURA.txt" in salida \
            and "SALIDA_V5_TAREA_X_MUTACION_APERTURA.txt" not in salida
        if not ok:
            fallos.append("caso (c): se esperaba ROJO (exit 1) nombrando SALIDA_V5_TARDIO_APERTURA.txt "
                          "y SIN mencionar el fichero MUTACION; salio exit %d" % codigo)
        else:
            print("CASO (c): OK (ROJO, exit 1, nombra el tardio real y calla el de MUTACION)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print()


def main():
    fallos = []
    caso_a(fallos)
    caso_b(fallos)
    caso_c(fallos)
    if fallos:
        print("ROJO GENERAL, %d caso(s) no calzan:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE GENERAL: los tres casos (a), (b) y (c) dan el veredicto esperado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
