# -*- coding: utf-8 -*-
"""vuelta129_tarea1h_casos_positivos.py . LOS DOS CASOS POSITIVOS POR
MUTACION que pide la TAREA 1.h de la vuelta 129 para
scripts/loop/verificar_cierre_sellado.py, corridos sobre una COPIA TEMPORAL
de repositorio construida desde cero con git init (nunca sobre el repo
real, "sin tocar los ficheros reales").

Construye una cadena sintetica: commit0 = acta ("ACTA DE LA VUELTA 128 DEL
AUDITOR: acta sintetica de la prueba"), commit1 = una operacion cualquiera,
commit2 = anade docs/loop/SALIDA_V129_HEAD_APERTURA.txt con el hash de
commit0 (asi es como sale de verdad: la apertura se mide con `git rev-parse
HEAD` ANTES de la primera operacion, asi que su contenido es el hash del
acta misma; ver docs/loop/SALIDA_V129_HEAD_APERTURA.txt real, que vale
a77f67f7... igual al acta a77f67f7 de la vuelta 128).

CASO (a): un commit que EXISTE en el repositorio (una rama lateral,
divergente de commit0, nunca fusionada) pero NO esta en la rama de trabajo.
Se escribe como cierre y tiene que dar ROJO nombrando "no esta en la rama".

CASO (b): el propio hash de la apertura (commit0) puesto como cierre. Pasa
las comprobaciones de existencia, rama y descendencia (un commit es
ancestro de si mismo), y tiene que caer ROJO SOLO por la ultima condicion,
"igual a la apertura".

USO:
  python scripts/loop/vuelta129_tarea1h_casos_positivos.py
"""
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_cierre_sellado.py")


def correr(args, cwd):
    r = subprocess.run([sys.executable] + args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def git(args, cwd, env=None):
    r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True, env=env)
    if r.returncode != 0:
        raise SystemExit("git %s fallo: %s" % (" ".join(args), r.stderr))
    return r.stdout


def rev(cwd, env, ref="HEAD"):
    return git(["rev-parse", ref], cwd, env).strip()


def main():
    fallos = []
    tmp = tempfile.mkdtemp(prefix="v129_tarea1h_")
    try:
        env = dict(os.environ)
        env["GIT_AUTHOR_NAME"] = env["GIT_COMMITTER_NAME"] = "prueba-mutacion"
        env["GIT_AUTHOR_EMAIL"] = env["GIT_COMMITTER_EMAIL"] = "prueba@local"

        git(["init", "-q"], tmp, env)
        git(["checkout", "-q", "-b", "principal"], tmp, env)
        os.makedirs(os.path.join(tmp, "scripts", "loop"))
        os.makedirs(os.path.join(tmp, "docs", "loop"))
        shutil.copyfile(GUARDA, os.path.join(tmp, "scripts", "loop", "verificar_cierre_sellado.py"))

        # commit0: EL ACTA de la vuelta 128 (sintetica).
        with open(os.path.join(tmp, "README_ACTA.txt"), "w") as f:
            f.write("acta sintetica\n")
        git(["add", "-A"], tmp, env)
        git(["commit", "-q", "-m", "ACTA DE LA VUELTA 128 DEL AUDITOR: acta sintetica de la prueba"], tmp, env)
        commit0 = rev(tmp, env)

        # commit1: una operacion cualquiera de la vuelta 129 sintetica.
        with open(os.path.join(tmp, "docs", "loop", "OPERACION1.txt"), "w") as f:
            f.write("operacion sintetica 1\n")
        git(["add", "-A"], tmp, env)
        git(["commit", "-q", "-m", "VUELTA 129: operacion sintetica 1"], tmp, env)

        # commit2: la apertura, con el hash de commit0 (asi sale en la vida
        # real: se mide ANTES de la primera operacion, asi que vale el hash
        # del acta misma).
        with open(os.path.join(tmp, "docs", "loop", "SALIDA_V129_HEAD_APERTURA.txt"), "w") as f:
            f.write(commit0 + "\n")
        git(["add", "-A"], tmp, env)
        git(["commit", "-q", "-m", "VUELTA 129: sello de apertura sintetico"], tmp, env)

        # rama lateral divergente desde commit0, con un commit que EXISTE
        # pero nunca se fusiona a "principal".
        git(["checkout", "-q", "-b", "lateral", commit0], tmp, env)
        with open(os.path.join(tmp, "LATERAL.txt"), "w") as f:
            f.write("commit de una rama lateral, nunca fusionada\n")
        git(["add", "-A"], tmp, env)
        git(["commit", "-q", "-m", "commit lateral, ajeno a la rama principal"], tmp, env)
        commit_lateral = rev(tmp, env)
        git(["checkout", "-q", "principal"], tmp, env)

        guarda_tmp = os.path.join(tmp, "scripts", "loop", "verificar_cierre_sellado.py")

        # CASO (a): commit_lateral EXISTE pero no esta en "principal".
        with open(os.path.join(tmp, "docs", "loop", "SALIDA_V129_HEAD_CIERRE.txt"), "w") as f:
            f.write(commit_lateral + "\n")
        codigo_a, salida_a = correr([guarda_tmp, "--vuelta", "129"], tmp)
        print("--- CASO (a): cierre = commit lateral %s (existe, ajeno a la rama) ---" % commit_lateral[:8])
        print(salida_a.strip())
        ok_a = codigo_a == 1 and salida_a.startswith("ROJO") and "no esta en la rama" in salida_a
        if not ok_a:
            fallos.append("caso (a): se esperaba ROJO nombrando 'no esta en la rama', salio exit %d" % codigo_a)
        else:
            print("CASO (a): OK (ROJO, exit 1, 'no esta en la rama')")
        print()

        # CASO (b): cierre = apertura (commit0).
        with open(os.path.join(tmp, "docs", "loop", "SALIDA_V129_HEAD_CIERRE.txt"), "w") as f:
            f.write(commit0 + "\n")
        codigo_b, salida_b = correr([guarda_tmp, "--vuelta", "129"], tmp)
        print("--- CASO (b): cierre = apertura, mismo hash %s ---" % commit0[:8])
        print(salida_b.strip())
        ok_b = codigo_b == 1 and salida_b.startswith("ROJO") and "IGUAL a" in salida_b
        if not ok_b:
            fallos.append("caso (b): se esperaba ROJO nombrando 'IGUAL a', salio exit %d" % codigo_b)
        else:
            print("CASO (b): OK (ROJO, exit 1, 'IGUAL a' la apertura)")
        print()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if fallos:
        print("ROJO GENERAL, %d caso(s) no calzan:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE GENERAL: los dos casos positivos (a) y (b) dan el veredicto ROJO esperado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
