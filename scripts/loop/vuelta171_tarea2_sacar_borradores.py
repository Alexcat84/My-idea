# -*- coding: utf-8 -*-
r"""vuelta171_tarea2_sacar_borradores.py . TAREA 2 DE LA VUELTA 171
(adjudicaciones 6.2 y 6.3 del acta 170).

LOS CINCO BORRADORES DE SECCION DE LA VUELTA 170 SALEN DE `docs/`, Y LAS TRES
LECTURAS DEL CONTADOR SE PUBLICAN AL LADO.

EL PROBLEMA, EN UNA LINEA: `docs/loop/_v170_t4_seccion.md` nombra `LD-139` y
`LD-154`, y `scripts/loop/vuelta48_contar_ld.py` barre `docs/` ENTERO excluyendo
por nombre solo `SALIDA_*`, los tres narrativos del bucle y los registros del
arnes. Un borrador de seccion de reporte no cae en ninguna de esas tres
exclusiones, asi que ENTRA en el universo y mueve el mayor. La cifra de 54
huecos que la vuelta 170 publico era cierta cuando la midio, y el commit que la
trajo la convirtio en otra.

POR QUE MOVER Y NO EXCLUIR POR NOMBRE (adjudicacion 6.3, y la cito porque es
suya y no mia): `vuelta48_contar_ld.py` ya excluye `REPORTE.md` por ser
NARRATIVO DEL BUCLE, y un fichero que es literalmente UNA SECCION DE ESE MISMO
REPORTE es de la misma especie y por el mismo motivo. **No es doctrina nueva: es
la exclusion que el instrumento ya tiene, leida sin hacerse el tonto con el
nombre del fichero.** Y se mueven en vez de excluirse porque anadir un patron
mas a la lista negra deja el agujero abierto para el siguiente nombre que a
alguien se le ocurra; sacarlos de `docs/` lo cierra para todos.

NO SE BORRA NADA Y NO SE EDITA NINGUNO: `git mv`, y el instrumento comprueba por
sha256 que los cinco ficheros llegan al destino byte a byte iguales.

LAS TRES LECTURAS QUE SE PUBLICAN, Y LA TERCERA ES LA QUE MANDA:
  (1) en `222ca6a7`, el corte donde la vuelta 170 midio sus 54 huecos, sobre un
      WORKTREE LIMPIO de ese commit (no sobre el arbol de hoy);
  (2) en HEAD, ANTES de mover;
  (3) en HEAD, DESPUES de mover.

LA GUARDA QUE PUEDE PARAR ESTA VUELTA (adjudicacion 6.2, literal): tras mover,
**el mayor de las HECHAS y el mayor del UNIVERSO tienen que dar los dos
`LD-138`**. Si no convergen, el instrumento sale en ROJO y la TAREA 3 no se
corre.

USO:
  python scripts/loop/vuelta171_tarea2_sacar_borradores.py
  python scripts/loop/vuelta171_tarea2_sacar_borradores.py --solo-medir
"""
import glob
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTADOR = os.path.join("scripts", "loop", "vuelta48_contar_ld.py")
CORTE_VIEJO = "222ca6a7"
PATRON = os.path.join(RAIZ, "docs", "loop", "_v170_t*_seccion.md")
DESTINO_REL = "scripts/loop"


def git(args, cwd=None):
    r = subprocess.run(["git"] + args, cwd=cwd or RAIZ, capture_output=True)
    return r.returncode, (r.stdout.decode("utf-8", errors="replace")
                          + r.stderr.decode("utf-8", errors="replace"))


def sha(ruta):
    return hashlib.sha256(io.open(ruta, "rb").read()).hexdigest()


def correr_contador(raiz):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, CONTADOR], cwd=raiz, capture_output=True, env=env)
    return r.returncode, (r.stdout.decode("utf-8", errors="replace")
                          + r.stderr.decode("utf-8", errors="replace"))


def leer(salida):
    """LAS CIFRAS SE EXTRAEN DE LA SALIDA, NO SE TECLEAN. Cae en rojo si alguna
    no se puede leer, en vez de rellenarla."""
    d = {}
    pares = [
        ("hechas", r"LECTURAS DIRIGIDAS HECHAS \(ids distintos con seccion propia\):\s*(\d+)"),
        ("hechas_desde", r"rango: LD-(\d+) a LD-\d+"),
        ("hechas_hasta", r"rango: LD-\d+ a LD-(\d+)"),
        ("universo_desde", r"rango del universo: LD-(\d+) a LD-\d+"),
        ("universo_hasta", r"rango del universo: LD-\d+ a LD-(\d+)"),
        ("sin_seccion", r"numeros nombrados sin seccion propia:\s*(\d+)"),
        ("huecos", r"huecos en el rango:\s*(\d+)"),
        ("universo_distintos", r"numeros distintos hallados = (\d+)"),
    ]
    faltan = []
    for clave, pat in pares:
        m = re.search(pat, salida)
        if not m:
            faltan.append(clave)
        else:
            d[clave] = int(m.group(1))
    m = re.search(r"numeros nombrados sin seccion propia:\s*\d+\n(.*?)\n=+\n5\. LOS HUECOS",
                  salida, re.S)
    d["nombres_sin_seccion"] = sorted(set(int(x) for x in re.findall(
        r"LD-(\d+) nombrado en", salida)))
    return d, faltan


def imprimir(etiqueta, d):
    print("   %-34s hechas %3d (LD-%02d a LD-%02d) | universo %3d distintos "
          "(LD-%02d a LD-%02d) | sin seccion %2d | huecos %2d"
          % (etiqueta, d["hechas"], d["hechas_desde"], d["hechas_hasta"],
             d["universo_distintos"], d["universo_desde"], d["universo_hasta"],
             d["sin_seccion"], d["huecos"]))
    print("   %-34s nombradas sin seccion: %s"
          % ("", ", ".join("LD-%d" % n for n in d["nombres_sin_seccion"]) or "ninguna"))


def main():
    solo_medir = "--solo-medir" in sys.argv
    print("=" * 78)
    print("VUELTA 171, TAREA 2: LOS CINCO BORRADORES SALEN DE docs/, Y LAS TRES LECTURAS")
    print("=" * 78)
    print("")
    rojos = []

    print("A) LOS CINCO FICHEROS, ANTES DE TOCARLOS")
    ficheros = sorted(glob.glob(PATRON))
    for p in ficheros:
        rel = os.path.relpath(p, RAIZ).replace(os.sep, "/")
        c, seg = git(["ls-files", "--error-unmatch", rel])
        print("   %-38s %6d bytes  sha256 %s  seguido por git: %s"
              % (rel, os.path.getsize(p), sha(p)[:16], "SI" if c == 0 else "NO"))
    print("   CIFRA ficheros: %d" % len(ficheros))
    nombrados = set()
    for p in ficheros:
        nombrados |= set(int(x) for x in re.findall(
            r"LD-(\d+)", io.open(p, encoding="utf-8").read()))
    print("   numeros LD que estos cinco nombran: %s"
          % ", ".join("LD-%d" % n for n in sorted(nombrados)))
    print("   el mayor que nombran: LD-%d" % max(nombrados))
    if len(ficheros) != 5:
        rojos.append("se esperaban 5 borradores y hay %d" % len(ficheros))
    print("")

    print("B) LECTURA 1: EL CORTE %s, SOBRE UN WORKTREE LIMPIO DE ESE COMMIT"
          % CORTE_VIEJO)
    tmp = tempfile.mkdtemp(prefix="v171_wt_")
    wt = os.path.join(tmp, "corte")
    c, o = git(["worktree", "add", "--detach", wt, CORTE_VIEJO])
    print("   git worktree add --detach ... %s -> exit %d" % (CORTE_VIEJO, c))
    d1 = None
    try:
        if c != 0:
            rojos.append("no se pudo crear el worktree de %s: %s" % (CORTE_VIEJO, o[:200]))
        else:
            c1, s1 = git(["rev-parse", "HEAD"], cwd=wt)
            print("   HEAD del worktree: %s" % s1.strip())
            sueltos = glob.glob(os.path.join(wt, "docs", "loop", "_v170_t*_seccion.md"))
            print("   borradores _v170_t*_seccion.md presentes en ese corte: %d"
                  % len(sueltos))
            cc, sal1 = correr_contador(wt)
            io.open(os.path.join(RAIZ, "docs", "loop",
                                 "SALIDA_V171_T2_CONTAR_LD_%s.txt" % CORTE_VIEJO),
                    "w", encoding="utf-8", newline="\n").write(sal1)
            d1, faltan = leer(sal1)
            if faltan:
                rojos.append("celdas ilegibles en la lectura 1: %s" % ", ".join(faltan))
            else:
                imprimir("(1) %s, worktree limpio" % CORTE_VIEJO, d1)
    finally:
        git(["worktree", "remove", "--force", wt])
        shutil.rmtree(tmp, ignore_errors=True)
    print("")

    print("C) LECTURA 2: HEAD, ANTES DE MOVER")
    c2, sal2 = correr_contador(RAIZ)
    io.open(os.path.join(RAIZ, "docs", "loop", "SALIDA_V171_T2_CONTAR_LD_ANTES.txt"),
            "w", encoding="utf-8", newline="\n").write(sal2)
    d2, faltan2 = leer(sal2)
    if faltan2:
        rojos.append("celdas ilegibles en la lectura 2: %s" % ", ".join(faltan2))
    else:
        imprimir("(2) HEAD, antes de mover", d2)
    print("")

    if rojos:
        print("ROJO, %d motivo(s), y NO se mueve nada:" % len(rojos))
        for r in rojos:
            print("   " + r)
        return 1

    if solo_medir:
        print("--solo-medir: no se mueve nada y no hay lectura 3.")
        return 0

    print("D) EL MOVIMIENTO, CON git mv Y SIN BORRAR NI EDITAR NADA")
    shas_antes = {os.path.basename(p): sha(p) for p in ficheros}
    for p in ficheros:
        rel = os.path.relpath(p, RAIZ).replace(os.sep, "/")
        nuevo = "%s/%s" % (DESTINO_REL, os.path.basename(p))
        c, o = git(["mv", rel, nuevo])
        print("   git mv %s %s -> exit %d %s" % (rel, nuevo, c, o.strip()[:80]))
        if c != 0:
            rojos.append("git mv fallo para %s" % rel)
    print("")

    print("E) NADA SE PERDIO Y NADA SE EDITO, COMPROBADO POR sha256")
    for nombre, sh in sorted(shas_antes.items()):
        destino = os.path.join(RAIZ, DESTINO_REL.replace("/", os.sep), nombre)
        origen = os.path.join(RAIZ, "docs", "loop", nombre)
        existe = os.path.exists(destino)
        igual = existe and sha(destino) == sh
        print("   %-26s en el destino: %s | sha256 identico: %s | queda en docs/: %s"
              % (nombre, "SI" if existe else "NO", "SI" if igual else "NO",
                 "SI" if os.path.exists(origen) else "NO"))
        if not igual:
            rojos.append("%s no llego al destino byte a byte" % nombre)
        if os.path.exists(origen):
            rojos.append("%s sigue en docs/loop/" % nombre)
    print("   CIFRA ficheros movidos con sha256 identico: %d de %d"
          % (sum(1 for n, s in shas_antes.items()
                 if os.path.exists(os.path.join(RAIZ, DESTINO_REL.replace("/", os.sep), n))
                 and sha(os.path.join(RAIZ, DESTINO_REL.replace("/", os.sep), n)) == s),
             len(shas_antes)))
    print("")

    print("F) LECTURA 3: HEAD, DESPUES DE MOVER")
    c3, sal3 = correr_contador(RAIZ)
    io.open(os.path.join(RAIZ, "docs", "loop", "SALIDA_V171_T2_CONTAR_LD_DESPUES.txt"),
            "w", encoding="utf-8", newline="\n").write(sal3)
    d3, faltan3 = leer(sal3)
    if faltan3:
        rojos.append("celdas ilegibles en la lectura 3: %s" % ", ".join(faltan3))
    print("")

    print("G) LAS TRES LECTURAS, UNA DEBAJO DE OTRA")
    if d1:
        imprimir("(1) %s, worktree limpio" % CORTE_VIEJO, d1)
    imprimir("(2) HEAD, antes de mover", d2)
    if not faltan3:
        imprimir("(3) HEAD, despues de mover", d3)
    print("")

    print("H) LA GUARDA DE LA 6.2: LAS DOS VARAS TIENEN QUE CONVERGER EN LD-138")
    if faltan3:
        rojos.append("no se puede comprobar la convergencia: lectura 3 ilegible")
    else:
        print("   el mayor de las HECHAS   -> LD-%d" % d3["hechas_hasta"])
        print("   el mayor del UNIVERSO    -> LD-%d" % d3["universo_hasta"])
        print("   convergen: %s" % ("SI" if d3["hechas_hasta"] == d3["universo_hasta"] else "NO"))
        print("   y dan LD-138: %s" % ("SI" if d3["hechas_hasta"] == 138
                                       and d3["universo_hasta"] == 138 else "NO"))
        if d3["hechas_hasta"] != d3["universo_hasta"]:
            rojos.append("PARADA: las dos varas NO convergen (hechas LD-%d, universo LD-%d)"
                         % (d3["hechas_hasta"], d3["universo_hasta"]))
        elif d3["hechas_hasta"] != 138:
            rojos.append("PARADA: convergen pero en LD-%d y no en LD-138"
                         % d3["hechas_hasta"])
    print("")

    if rojos:
        print("ROJO, %d motivo(s):" % len(rojos))
        for r in rojos:
            print("   " + r)
        print("LA TAREA 3 NO SE CORRE.")
        return 1
    print("VERDE: los cinco borradores estan fuera de docs/, las dos varas convergen")
    print("en LD-138, y la TAREA 3 puede correr.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
