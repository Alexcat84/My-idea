# -*- coding: utf-8 -*-
r"""archivar_reporte.py . LE DA NOMBRE DE FICHERO AL REPORTE DE UNA VUELTA QUE
YA CERRO, COPIANDOLO A docs/loop/reportes/REPORTE_V<N>.md.

NOMBRE ESTABLE A PROPOSITO, sin numero de vuelta, como
tallar_cabecera_reporte.py y verificar_apertura_sellada.py: la vuelta se pasa
con --vuelta y este fichero NO se clona cada vuelta.

POR QUE NACE (adjudicacion 6.4 del acta 169, y resuelve la D.1 y la pregunta
P.1 del reporte de la 169). docs/loop/REPORTE.md SE SOBRESCRIBE cada vuelta con
el esqueleto de la siguiente, asi que el reporte de una vuelta cerrada solo
vivia en el COMMIT que lo llevaba. Eso no es una perdida (git lo guarda entero)
pero si es una sede sin nombre: para leer el reporte de la 168 hay que saber
que su commit es 1eec382f. Este instrumento NO BORRA NADA, NO CAMBIA NINGUNA
REGLA Y NO CREA SEDE NUEVA: le pone nombre de fichero a la sede que ya existia.

LA DECISION DE DISENO, Y ES LA QUE HACE QUE ESTO SE PUEDA CORRER TARDE: el
texto NO se lee del arbol de trabajo, SE LEE DE GIT (git show <commit>:ruta).
Un archivador que copiase el arbol de trabajo solo podria correr en la ventana
exacta anterior al esqueleto, y si esa ventana se pierde el reporte queda sin
archivar para siempre. Leyendo de git, cualquier reporte de cualquier vuelta
pasada se puede archivar en cualquier momento, que es justo lo que hace falta
para ARCHIVAR HACIA ATRAS el de la 168.

COMO ELIGE EL COMMIT SI NO SE LE DA UNO: `git log -1 --format=%H -- <ruta>`,
o sea el ultimo commit que toco docs/loop/REPORTE.md. Corrido en la APERTURA de
una vuelta, ese commit es exactamente el del cierre de la vuelta anterior,
porque el esqueleto de la vuelta nueva todavia no ha escrito. Corrido mas
tarde, el automatismo apuntaria al esqueleto de la vuelta en curso, y por eso
existe --commit: para nombrarlo a mano cuando la ventana ya paso.

LA GUARDA, Y ES LA QUE PUEDE CAER: el texto recuperado tiene que EMPEZAR por
una cabecera "# REPORTE DE LA VUELTA <N>", con la MISMA N que se pidio. Si el
commit que se nombra lleva el reporte de otra vuelta, el instrumento CAE EN
ROJO y no escribe nada. Nunca archiva un reporte bajo un numero que no es el
suyo. Tambien cae si el destino ya existe con contenido DISTINTO: un archivo
que se pisa a si mismo en silencio no se puede auditar.

USO:
  python scripts/loop/archivar_reporte.py --vuelta 169
  python scripts/loop/archivar_reporte.py --vuelta 168 --commit 1eec382f
  python scripts/loop/archivar_reporte.py --vuelta 168 --commit 1eec382f --forzar

SALIDA: exit 0 si archiva (o si el destino ya estaba con contenido identico);
exit 1 en cualquier rojo, sin escribir nada.
"""
import argparse
import hashlib
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_REPORTE = "docs/loop/REPORTE.md"
DIR_ARCHIVO = os.path.join(RAIZ, "docs", "loop", "reportes")


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def normalizar(texto):
    return texto.replace("\r\n", "\n").replace("\r", "\n")


def sha(texto):
    return hashlib.sha256(normalizar(texto).encode("utf-8")).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    ap.add_argument("--commit", default=None,
                    help="commit del que leer el reporte; por defecto, el ultimo que toco la ruta")
    ap.add_argument("--forzar", action="store_true",
                    help="permite reescribir un destino que ya existe con contenido distinto")
    a = ap.parse_args()

    print("=" * 78)
    print("ARCHIVADOR DE REPORTES. Vuelta %d." % a.vuelta)
    print("El texto se lee de git, no del arbol de trabajo.")
    print("=" * 78)

    rojos = []

    commit = a.commit
    if commit is None:
        c, o = git(["log", "-1", "--format=%H", "--", RUTA_REPORTE])
        commit = o.strip()
        if c != 0 or len(commit) != 40:
            print("  ROJO: git log no trae ningun commit que toque %s" % RUTA_REPORTE)
            return 1
        print("  commit elegido solo (ultimo que toco la ruta): %s" % commit)
    else:
        c, o = git(["rev-parse", "--verify", "%s^{commit}" % commit])
        if c != 0 or len(o.strip()) != 40:
            print("  ROJO: %r no resuelve a ningun commit" % commit)
            return 1
        commit = o.strip()
        print("  commit nombrado a mano: %s" % commit)

    c, asunto = git(["log", "-1", "--format=%ad%x09%s", "--date=iso", commit])
    print("  asunto de ese commit: %s" % asunto.strip()[:150])

    c, texto = git(["show", "%s:%s" % (commit, RUTA_REPORTE)])
    if c != 0 or not texto.strip():
        print("  ROJO: %s no existe en el arbol de %s" % (RUTA_REPORTE, commit[:8]))
        return 1

    primera = normalizar(texto).split("\n", 1)[0]
    m = re.match(r"^#\s*REPORTE DE LA VUELTA\s+(\d+)\b", primera)
    if not m:
        rojos.append("la primera linea del texto recuperado no es una cabecera "
                     "'# REPORTE DE LA VUELTA <N>': %r" % primera[:90])
    else:
        vuelta_leida = int(m.group(1))
        print("  vuelta LEIDA de la cabecera del texto: %d" % vuelta_leida)
        if vuelta_leida != a.vuelta:
            rojos.append("el reporte que lleva %s es el de la VUELTA %d, no el de la %d: "
                         "no se archiva bajo un numero que no es el suyo"
                         % (commit[:8], vuelta_leida, a.vuelta))

    destino = os.path.join(DIR_ARCHIVO, "REPORTE_V%d.md" % a.vuelta)
    rel = os.path.relpath(destino, RAIZ).replace(os.sep, "/")
    ya_identico = False
    if os.path.exists(destino):
        viejo = io.open(destino, encoding="utf-8").read()
        if sha(viejo) == sha(texto):
            ya_identico = True
            print("  el destino %s YA EXISTE con contenido IDENTICO (sha256 %s)"
                  % (rel, sha(texto)[:12]))
        elif not a.forzar:
            rojos.append("el destino %s ya existe con contenido DISTINTO "
                         "(en disco sha256 %s, recuperado sha256 %s). "
                         "Se necesita --forzar para pisarlo."
                         % (rel, sha(viejo)[:12], sha(texto)[:12]))

    if rojos:
        print("")
        print("  ROJO, %d motivo(s), y NO se escribe nada:" % len(rojos))
        for r in rojos:
            print("     " + r)
        return 1

    if not ya_identico:
        if not os.path.isdir(DIR_ARCHIVO):
            os.makedirs(DIR_ARCHIVO)
        io.open(destino, "w", encoding="utf-8", newline="\n").write(normalizar(texto))
        print("  ESCRITO: %s" % rel)

    print("")
    print("  VERDE.")
    print("     vuelta            %d" % a.vuelta)
    print("     commit de origen  %s" % commit)
    print("     ruta de origen    %s" % RUTA_REPORTE)
    print("     destino           %s" % rel)
    print("     bytes             %d" % len(normalizar(texto).encode("utf-8")))
    print("     lineas            %d" % normalizar(texto).count("\n"))
    print("     sha256 (LF)       %s" % sha(texto))
    return 0


if __name__ == "__main__":
    sys.exit(main())
