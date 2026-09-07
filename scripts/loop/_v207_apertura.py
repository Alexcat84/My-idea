# -*- coding: utf-8 -*-
r"""_v207_apertura.py . COMPUTO DE LA VUELTA 207, CON PREFIJO DE GUION BAJO,
FUERA DEL CENSO Y FUERA DE LA NOMINA (encargo 207, punto 2.e y la moratoria de
AUDITOR.md 6.3).

QUE HACE: mide el estado del arbol ANTES DE LA PRIMERA OPERACION de la vuelta
(EJECUTOR.md 1, LA APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION) y lo sella.

LAS DOS CONVENCIONES SE IMPORTAN, NO SE COPIAN: `dos_convenciones` y
`medir_en_disco` viven en `vuelta186_rutas_del_reporte.py`, que es la sede unica.
IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5).
"""
import hashlib
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)

RUTAS = [
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/REPORTE.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/PENDIENTES.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/INTRA_DOMINIO_INFORME.md",
    "docs/BANCO_DE_TEXTOS.md",
]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def shas(ruta):
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    if not os.path.isfile(p):
        return None, None
    crudo = io.open(p, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return (hashlib.sha256(crudo).hexdigest()[:16],
            hashlib.sha256(lf).hexdigest()[:16])


def main():
    out = []
    out.append("APERTURA DE LA VUELTA 207, MEDIDA ANTES DE LA PRIMERA OPERACION")
    out.append("")
    _, head = git(["rev-parse", "HEAD"])
    _, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
    _, asunto = git(["log", "-1", "--format=%s"])
    _, fecha = git(["log", "-1", "--format=%ad", "--date=iso"])
    out.append("CIFRA HEAD de apertura: " + head.strip())
    out.append("CIFRA rama de apertura: " + rama.strip())
    out.append("CIFRA fecha del commit de apertura: " + fecha.strip())
    out.append("ASUNTO del commit de apertura (primeros 120): "
               + asunto.strip()[:120])
    out.append("")
    _, st = git(["status", "--porcelain"])
    lineas = [l for l in st.split(NL) if l.strip()]
    out.append("CIFRA lineas de status, medidas con git status --porcelain: "
               + str(len(lineas)))
    for l in lineas:
        out.append("  status> " + l)
    out.append("")
    for sede in ["dataset/", "web/", "engine/", "docs/plan/"]:
        _, ns = git(["diff", "--numstat", "--", sede])
        filas = [l for l in ns.split(NL) if l.strip()]
        out.append("CIFRA filas de git diff --numstat -- " + sede
                   + " AL ENTRAR: " + str(len(filas)))
    out.append("")
    out.append("LAS DOS CONVENCIONES DE CADA SEDE QUE LA VUELTA VA A NOMBRAR:")
    for ruta in RUTAS:
        m = medir_en_disco(RAIZ, ruta)
        if m is None:
            out.append("CIFRA " + ruta + ": NO EXISTE (ausencia, no cero)")
            continue
        sd, sl = shas(ruta)
        out.append("CIFRA " + ruta + ": " + str(m[0])
                   + " bytes en disco y " + str(m[1])
                   + " bytes normalizado a LF, sha256 disco " + sd
                   + " y sha256 LF " + sl)
    out.append("")
    p = os.path.join(RAIZ, "docs", "loop", "reportes", "REPORTE_V206.md")
    out.append("CIFRA docs/loop/reportes/REPORTE_V206.md existe al entrar: "
               + ("SI" if os.path.isfile(p) else "NO"))
    texto = NL.join(out) + NL
    destino = os.path.join(RAIZ, "docs", "loop", "SALIDA_V207_APERTURA.txt")
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
