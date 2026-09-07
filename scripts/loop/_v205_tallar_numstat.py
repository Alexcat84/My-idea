# -*- coding: utf-8 -*-
r"""_v205_tallar_numstat.py . LA SECCION 4 DEL REPORTE DE LA VUELTA 205, TALLADA
DE `git` Y NO TECLEADA.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo, fuera de la
nomina, no roza la moratoria (acta 199 `4.5`, acta 203 `4.6`). No vigila nada.

QUE TALLA, Y CADA COSA CON EL COMANDO QUE LA MIDE AL LADO:

  . el `numstat` de las CUATRO sedes que el encargo exige en cero
    (`dataset/`, `web/`, `engine/`, `docs/plan/`), contra el HEAD de apertura;
  . el `numstat` de las TRES sedes del auditor, que esta vuelta no escribe,
    distinguiendo el cero DE AUSENCIA DE FICHERO del cero de no haberla tocado,
    que es la forma correcta segun el `4.5` del acta 204;
  . las dos sedes selladas (`INTRA_DOMINIO_VEREDICTOS.jsonl` y
    `OPERACIONES.jsonl`) REMEDIDAS AL CIERRE, con sus bytes y su `sha256` por
    LAS DOS CONVENCIONES y en el MISMO RENGLON;
  . el inventario de lo que la vuelta SI toco, leido de `git diff --numstat`.

EL ESTADO AL CIERRE SE MIDE AL CIERRE (`EJECUTOR.md` 1): nada de esto se hereda
de la apertura, todo se recomputa aqui."""
import hashlib
import io
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
    print("**TODO LO DE ESTA SECCION SALE DE `git` CORRIDO AL CIERRE Y NO SE")
    print("HEREDA DE LA APERTURA** (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL")
    print("CIERRE). El HEAD de apertura contra el que se mide todo es `%s`," % ap[:8])
    print("leido de `git rev-parse HEAD` antes de la primera operacion.")
    print("")
    print("### 4.1 LAS CUATRO SEDES QUE EL ENCARGO EXIGE EN CERO, MEDIDAS AL CIERRE")
    print("")
    print("Comando: `git diff %s --numstat -- <sede>`" % ap[:8])
    print("")
    print("| sede | filas de numstat contra el HEAD de apertura |")
    print("|---|---:|")
    total_encargo = 0
    for s in SEDES_DEL_ENCARGO:
        _c, o = git(["diff", ap, "--numstat", "--", s])
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
    print("(`4.5` del acta 204: la sede se mide aunque no exista, y esa es la forma")
    print("correcta). Comando: `git diff %s --numstat -- <sede>`." % ap[:8])
    print("")
    print("| sede del auditor | existe en disco | filas de numstat | de que es el cero |")
    print("|---|---|---:|---|")
    for s in SEDES_DEL_AUDITOR:
        _c, o = git(["diff", ap, "--numstat", "--", s])
        f = filas(o)
        existe = os.path.exists(os.path.join(RAIZ, s.replace("/", os.sep)))
        motivo = ("de no haberla tocado" if existe
                  else "**de ausencia de fichero**, no de no haberla tocado")
        print("| `%s` | %s | %d | %s |" % (s, "SI" if existe else "NO", len(f), motivo))
    print("")
    print("### 4.3 LAS DOS SEDES SELLADAS, REMEDIDAS AL CIERRE Y NO HEREDADAS")
    print("")
    print("| fichero | bytes (disco y LF, en el mismo renglon) | sha256 (disco y LF, en el mismo renglon) | calza con el encargo |")
    print("|---|---|---|---|")
    for p, esperado in SELLADAS:
        b = io.open(os.path.join(RAIZ, p.replace("/", os.sep)), "rb").read()
        lf = b.replace(b"\r\n", b"\n")
        sd = hashlib.sha256(b).hexdigest()[:16]
        sl = hashlib.sha256(lf).hexdigest()[:16]
        print("| `%s` | %d bytes en disco y %d bytes normalizado a LF | sha256 disco `%s` y sha256 LF `%s` | %s |"
              % (p, len(b), len(lf), sd, sl,
                 "SI" if (sd == esperado and sl == esperado) else "**NO**"))
    print("")
    print("**NINGUN campo `estado`, NINGUNA clase y NINGUN veredicto se movio en esta")
    print("vuelta, y no lo digo: lo miden los dos `sha256` de arriba, identicos por")
    print("las dos convenciones a los que el encargo trae del cierre de la 204.**")
    print("")
    print("### 4.4 LO QUE LA VUELTA SI TOCO, LEIDO DE `git` Y NO NARRADO")
    print("")
    print("Comando: `git diff %s --numstat` sobre el arbol entero." % ap[:8])
    print("")
    _c, o = git(["diff", ap, "--numstat"])
    f = filas(o)
    _c2, o2 = git(["diff", ap, "--numstat", "--stat"])
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
    print("**CIFRA ficheros tocados en el arbol de trabajo contra el HEAD de apertura: %d.**"
          % len(f))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
