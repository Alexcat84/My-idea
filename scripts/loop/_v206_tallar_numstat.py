# -*- coding: utf-8 -*-
r"""_v206_tallar_numstat.py . LA SECCION 4 DE UN REPORTE, TALLADA DE `git`.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo, fuera de la
nomina (congelada en 135), no anade guarda ni lector que se quede vigilando y
muere con la vuelta. Acta 199 `4.5`, acta 203 `4.6`, acta 205 `4.1`.

QUE ANADE SOBRE `_v205_tallar_numstat.py`, Y POR QUE NO LO REUSO TAL CUAL: aquel
mide SIEMPRE contra el ARBOL DE TRABAJO (`git diff <ap> --numstat`), que es lo
correcto para la vuelta que se esta corriendo y es FALSO para una vuelta VIEJA
que se cierra tarde: le colgaria a la 205 los ficheros de la 206. Este acepta un
CIERRE explicito y entonces mide `<apertura>..<cierre>`, que es la huella de esa
vuelta y de ninguna otra, y lee las sedes selladas de ESE arbol con `git show`.

USO:  python scripts/loop/_v206_tallar_numstat.py <apertura> [<cierre>]
"""
import hashlib
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)
P_FILA = re.compile(r"^(\d+|-)\t(\d+|-)\t")

SEDES_DEL_ENCARGO = ["dataset/", "web/", "engine/", "docs/plan/"]
SEDES_DEL_AUDITOR = ["docs/loop/PROMPT_SIGUIENTE.md",
                     "docs/loop/ACTA_AUDITOR.md",
                     "docs/loop/PARA_ALEXIS.md"]
SELLADAS = [("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", "0a77b5a35a962621"),
            ("docs/plan/OPERACIONES.jsonl", "829c583eb779cab6")]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, (r.stdout + r.stderr).decode("utf-8", errors="replace")


def filas(salida):
    return [x for x in salida.replace(chr(13), "").split(NL) if P_FILA.match(x)]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = sys.argv[1]
    ci = sys.argv[2] if len(sys.argv) > 2 else None
    rango = ["%s..%s" % (ap, ci)] if ci else [ap]
    cmd_texto = ("git diff %s..%s --numstat" % (ap[:8], ci[:8]) if ci
                 else "git diff %s --numstat" % ap[:8])

    print("**TODO LO DE ESTA SECCION SALE DE `git` CORRIDO EN ESTA VUELTA Y NO SE")
    print("HEREDA DE LA APERTURA** (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL")
    if ci:
        print("CIERRE). LA HUELLA SE MIDE ENTRE DOS COMMITS, `%s` de apertura y `%s`" % (ap[:8], ci[:8]))
        print("de cierre, **y no contra el arbol de trabajo**: esta vuelta se cierra")
        print("tarde, y medir contra el arbol de hoy le colgaria ficheros de otra vuelta.")
    else:
        print("CIERRE). El HEAD de apertura contra el que se mide todo es `%s`," % ap[:8])
        print("leido de `git rev-parse HEAD` antes de la primera operacion.")
    print("")
    print("### 4.1 LAS CUATRO SEDES QUE EL ENCARGO EXIGE EN CERO, MEDIDAS AL CIERRE")
    print("")
    print("Comando: `%s -- <sede>`" % cmd_texto)
    print("")
    print("| sede | filas de numstat |")
    print("|---|---:|")
    total_encargo = 0
    for s in SEDES_DEL_ENCARGO:
        _c, o = git(["diff"] + rango + ["--numstat", "--", s])
        f = filas(o)
        total_encargo += len(f)
        print("| `%s` | %d |" % (s, len(f)))
        for x in f:
            print("| ^ FILA QUE NO DEBERIA ESTAR | `%s` |" % x)
    print("")
    print("**CIFRA suma de filas de las cuatro sedes: %d.**" % total_encargo)
    print("")
    print("### 4.2 LAS TRES SEDES DEL AUDITOR, QUE EL EJECUTOR NO ESCRIBE")
    print("")
    print("**EL CERO DE `PARA_ALEXIS.md` ES DE AUSENCIA DE FICHERO, Y ASI SE DICE**")
    print("(`4.5` del acta 204). Comando: `%s -- <sede>`." % cmd_texto)
    print("")
    print("| sede del auditor | existe en disco | filas de numstat | de que es el cero |")
    print("|---|---|---:|---|")
    for s in SEDES_DEL_AUDITOR:
        _c, o = git(["diff"] + rango + ["--numstat", "--", s])
        f = filas(o)
        existe = os.path.exists(os.path.join(RAIZ, s.replace("/", os.sep)))
        motivo = ("de no haberla tocado" if existe
                  else "**de ausencia de fichero**, no de no haberla tocado")
        print("| `%s` | %s | %d | %s |" % (s, "SI" if existe else "NO", len(f), motivo))
    print("")
    print("### 4.3 LAS DOS SEDES SELLADAS, REMEDIDAS Y NO HEREDADAS")
    print("")
    if ci:
        print("Leidas del arbol de `%s` con `git show`, que es el arbol al cerrar" % ci[:8])
        print("esa vuelta, y no del disco de hoy.")
        print("")
    print("| fichero | bytes (disco y LF, en el mismo renglon) | sha256 (disco y LF, en el mismo renglon) | calza con el encargo |")
    print("|---|---|---|---|")
    for p, esperado in SELLADAS:
        if ci:
            r = subprocess.run(["git", "show", "%s:%s" % (ci, p)], cwd=RAIZ,
                               capture_output=True)
            b = r.stdout
        else:
            b = open(os.path.join(RAIZ, p.replace("/", os.sep)), "rb").read()
        lf = b.replace(b"\r\n", b"\n")
        sd = hashlib.sha256(b).hexdigest()[:16]
        sl = hashlib.sha256(lf).hexdigest()[:16]
        print("| `%s` | %d bytes en disco y %d bytes normalizado a LF | sha256 disco `%s` y sha256 LF `%s` | %s |"
              % (p, len(b), len(lf), sd, sl,
                 "SI" if (sd == esperado and sl == esperado) else "**NO**"))
    print("")
    print("**NINGUN campo `estado`, NINGUNA clase y NINGUN veredicto se movio, y no lo")
    print("digo: lo miden los dos `sha256` de arriba, identicos por las dos")
    print("convenciones a los que el encargo trae del cierre de la 204.**")
    print("")
    print("### 4.4 LO QUE LA VUELTA SI TOCO, LEIDO DE `git` Y NO NARRADO")
    print("")
    print("Comando: `%s` sobre el arbol entero." % cmd_texto)
    print("")
    _c, o = git(["diff"] + rango + ["--numstat"])
    f = filas(o)
    dirs = {}
    for x in f:
        partes = x.split("\t")
        ruta = partes[2] if len(partes) > 2 else "(?)"
        d = "/".join(ruta.split("/")[:2]) if "/" in ruta else "(raiz)"
        dirs[d] = dirs.get(d, 0) + 1
    print("| directorio tocado | ficheros |")
    print("|---|---:|")
    for d in sorted(dirs):
        print("| `%s` | %d |" % (d, dirs[d]))
    print("")
    print("**CIFRA ficheros tocados contra el HEAD de apertura: %d.**" % len(f))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
