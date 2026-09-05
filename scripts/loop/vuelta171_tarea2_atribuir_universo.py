# -*- coding: utf-8 -*-
r"""vuelta171_tarea2_atribuir_universo.py . LA SEGUNDA MITAD DE LA TAREA 2 DE LA
VUELTA 171: A QUIEN PERTENECE CADA FUENTE QUE MUEVE EL UNIVERSO DEL CONTADOR.

POR QUE HACE FALTA, Y NO ESTABA EN EL ENCARGO. La TAREA 2 movio los cinco
borradores a `scripts/loop/` (5 de 5, sha256 identico) y la lectura de despues
salio IGUAL que la de antes: universo hasta `LD-154`, 8 nombradas sin seccion,
64 huecos. O sea que **los cinco borradores no eran la unica fuente**, y el
encargo manda parar si las dos varas no convergen. Antes de traer la parada hay
que decir DE QUIEN es cada fuente, porque no es lo mismo un fichero que ya
estaba que uno que ha escrito esta misma vuelta.

QUE MIDE: corre `scripts/loop/vuelta48_contar_ld.py` sobre WORKTREES LIMPIOS de
los cortes que se le pasen, y sobre el arbol de hoy, y saca la nomina de
ficheros que nombran cada `LD` sin seccion propia en cada corte. La atribucion
sale de comparar las nominas, no de suponer.

De solo lectura sobre el repo (crea y destruye worktrees en el temporal del
sistema). No escribe nada dentro de `docs/` salvo sus propias salidas
`SALIDA_V171_T2_*`.

USO:
  python scripts/loop/vuelta171_tarea2_atribuir_universo.py 0caca89f 222ca6a7
"""
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTADOR = os.path.join("scripts", "loop", "vuelta48_contar_ld.py")


def git(args, cwd=None):
    r = subprocess.run(["git"] + args, cwd=cwd or RAIZ, capture_output=True)
    return r.returncode, (r.stdout.decode("utf-8", errors="replace")
                          + r.stderr.decode("utf-8", errors="replace"))


def correr_contador(raiz):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, CONTADOR], cwd=raiz, capture_output=True, env=env)
    return (r.stdout.decode("utf-8", errors="replace")
            + r.stderr.decode("utf-8", errors="replace"))


def nomina(salida):
    """{numero: [ficheros]} para las nombradas SIN seccion propia, leido de la
    seccion 4 de la salida del contador."""
    tramo = salida.split("4. LAS ENCARGADAS Y SIN HACER", 1)
    if len(tramo) < 2:
        return {}, {}
    cuerpo = tramo[1].split("5. LOS HUECOS", 1)[0]
    d = {}
    actual = None
    for linea in cuerpo.split("\n"):
        m = re.match(r"\s*LD-(\d+) nombrado en \d+ fichero", linea)
        if m:
            actual = int(m.group(1))
            d[actual] = []
            continue
        if actual is not None and linea.strip().startswith(("docs/", "scripts/")):
            d[actual].append(linea.strip())
    cifras = {}
    for clave, pat in (("hechas_hasta", r"rango: LD-\d+ a LD-(\d+)"),
                       ("universo_hasta", r"rango del universo: LD-\d+ a LD-(\d+)"),
                       ("hechas", r"HECHAS \(ids distintos con seccion propia\):\s*(\d+)"),
                       ("huecos", r"huecos en el rango:\s*(\d+)")):
        m = re.search(pat, salida)
        cifras[clave] = int(m.group(1)) if m else -1
    return d, cifras


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    cortes = [a for a in sys.argv[1:] if not a.startswith("-")]
    print("=" * 78)
    print("VUELTA 171, TAREA 2 (segunda mitad): A QUIEN PERTENECE CADA FUENTE")
    print("=" * 78)
    print("")

    lecturas = []
    tmp = tempfile.mkdtemp(prefix="v171_atr_")
    try:
        for i, corte in enumerate(cortes):
            wt = os.path.join(tmp, "c%d" % i)
            c, o = git(["worktree", "add", "--detach", wt, corte])
            if c != 0:
                print("ROJO: no se pudo crear el worktree de %s" % corte)
                return 1
            c2, real = git(["rev-parse", "HEAD"], cwd=wt)
            sal = correr_contador(wt)
            io.open(os.path.join(RAIZ, "docs", "loop",
                                 "SALIDA_V171_T2_CONTAR_LD_%s.txt" % corte),
                    "w", encoding="utf-8", newline="\n").write(sal)
            lecturas.append((corte + " (worktree limpio)", real.strip()[:8]) + nomina(sal))
            git(["worktree", "remove", "--force", wt])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    sal_hoy = correr_contador(RAIZ)
    lecturas.append(("el arbol de HOY, tras mover los cinco", "arbol") + nomina(sal_hoy))

    print("A) LAS CIFRAS DE CADA CORTE")
    for etiqueta, h, _d, cif in lecturas:
        print("   %-42s %-9s hechas %3d (hasta LD-%d) | universo hasta LD-%d | huecos %d"
              % (etiqueta, h, cif["hechas"], cif["hechas_hasta"],
                 cif["universo_hasta"], cif["huecos"]))
    print("")

    print("B) LAS NOMBRADAS SIN SECCION, CORTE A CORTE, CON SU FICHERO")
    todos = sorted(set(n for _e, _h, d, _c in lecturas for n in d))
    for n in todos:
        print("   LD-%d:" % n)
        for etiqueta, _h, d, _c in lecturas:
            fich = d.get(n)
            print("      %-42s %s" % (etiqueta, ", ".join(fich) if fich else "(no aparece)"))
    print("")

    print("C) LA ATRIBUCION, CONTADA Y NO SUPUESTA")
    if len(lecturas) < 2:
        print("   (hacen falta al menos dos cortes)")
        return 1
    base = lecturas[0]
    hoy = lecturas[-1]
    nuevas = sorted(set(hoy[2]) - set(base[2]))
    print("   corte base: %s" % base[0])
    print("   CIFRA nombradas sin seccion en la base: %d" % len(base[2]))
    print("   CIFRA nombradas sin seccion hoy:        %d" % len(hoy[2]))
    print("   CIFRA que NO estaban en la base:        %d (%s)"
          % (len(nuevas), ", ".join("LD-%d" % n for n in nuevas) or "ninguna"))
    print("")
    print("   y el fichero que las trae hoy, uno por uno:")
    por_fichero = {}
    for n in nuevas:
        for f in hoy[2][n]:
            por_fichero.setdefault(f, []).append(n)
    for f in sorted(por_fichero):
        print("      %-40s %s" % (f, ", ".join("LD-%d" % n for n in por_fichero[f])))
    print("")

    print("D) ESOS FICHEROS, ¿EXISTIAN EN EL CORTE BASE?")
    for f in sorted(por_fichero):
        c, o = git(["cat-file", "-e", "%s:%s" % (cortes[0], f)])
        existia = (c == 0)
        print("   %-40s en %s: %s" % (f, cortes[0], "SI" if existia else "NO EXISTIA"))
        if existia:
            c2, viejo = git(["show", "%s:%s" % (cortes[0], f)])
            nums = sorted(set(int(x) for x in re.findall(r"LD-(\d+)", viejo)))
            trae = [n for n in por_fichero[f] if n in nums]
            print("      %-37s los nombraba ya: %s"
                  % ("", ", ".join("LD-%d" % n for n in trae) or "ninguno"))
    print("")
    return 0


if __name__ == "__main__":
    sys.exit(main())
