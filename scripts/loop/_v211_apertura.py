# -*- coding: utf-8 -*-
r"""_v211_apertura.py . COMPUTO DE LA VUELTA 211, CON PREFIJO DE GUION BAJO,
FUERA DEL CENSO Y FUERA DE LA NOMINA (moratoria de AUDITOR.md 6.3).

QUE HACE: mide el estado del arbol ANTES DE LA PRIMERA OPERACION de la vuelta
(EJECUTOR.md 1, LA APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION) y lo sella.

IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5). `git`, `shas` y `RAIZ` se
IMPORTAN de `_v210_apertura`, que los importa de `_v209_apertura`, que a su vez
importa `medir_en_disco` de `vuelta186_rutas_del_reporte.py`, la sede unica de
las dos convenciones. Aqui NO se copia ni una linea de esas funciones: solo
cambia LA LISTA DE SEDES que esta vuelta va a nombrar y el numero de vuelta,
que se computa del propio nombre del fichero y no se teclea.

LA 211 NO ES VUELTA DE BATERIA (la cadencia de cinco de AUDITOR.md 6.1 pone la
siguiente en la 215), asi que aqui NO va la lista de los once tramos: esta
vuelta no los pisa y medirlos seria ruido.

LAS SEDES SON LAS QUE LA 211 VA A NOMBRAR: las dos del campo `estado`
(OPERACIONES.jsonl), las tres que nombra la evidencia de OP-I-01
(INVENTARIO.jsonl, 10_INVENTARIO.md y AUDITOR.md), la vara de su criterio de
hecho (08_VERIFICACION.md) y las dos que la medicion del 1357 va a contar
(02_DESTEJIDOS.md y master_graph.json).
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v210_apertura import git, shas, RAIZ  # noqa: E402
from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

RUTAS = [
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/REPORTE.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/INVENTARIO.jsonl",
    "docs/plan/10_INVENTARIO.md",
    "docs/plan/08_VERIFICACION.md",
    "docs/plan/02_DESTEJIDOS.md",
    "dataset/metadata/master_graph.json",
    "docs/loop/SALIDA_MARCADOR_AUDITOR_V210.json",
]

SEDES_AUDITOR = [
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "PARA_ALEXIS.md",
]


def main():
    out = []
    out.append("APERTURA DE LA VUELTA %d, MEDIDA ANTES DE LA PRIMERA OPERACION"
               % VUELTA)
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
    out.append("CIFRA lineas de status: " + str(len(lineas)))
    out.append("  (la misma cifra, con su glosa: medidas con git status --porcelain)")
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
        igual = "COINCIDEN" if m[0] == m[1] else "NO COINCIDEN"
        out.append("CIFRA " + ruta + ": " + str(m[0])
                   + " bytes en disco y " + str(m[1])
                   + " bytes normalizado a LF (" + igual
                   + "), sha256 disco " + sd + " y sha256 LF " + sl)
    out.append("")
    out.append("LAS TRES SEDES DEL AUDITOR, AL ENTRAR, CON EL CERO DISTINGUIDO:")
    for ruta in SEDES_AUDITOR:
        p = os.path.join(RAIZ, ruta.replace("/", os.sep))
        if not os.path.isfile(p):
            out.append("CIFRA " + ruta
                       + ": 0 filas POR AUSENCIA DE FICHERO (no existe en disco)")
            continue
        _, ns = git(["diff", "--numstat", "--", ruta])
        filas = [l for l in ns.split(NL) if l.strip()]
        out.append("CIFRA " + ruta + ": " + str(len(filas))
                   + " filas de git diff --numstat, FICHERO PRESENTE ("
                   + str(os.path.getsize(p)) + " bytes en disco)")
    out.append("")
    for nombre in ("REPORTE_V210.md",):
        p = os.path.join(RAIZ, "docs", "loop", "reportes", nombre)
        out.append("CIFRA docs/loop/reportes/" + nombre + " existe al entrar: "
                   + ("SI" if os.path.isfile(p) else "NO"))
    texto = NL.join(out) + NL
    destino = os.path.join(RAIZ, "docs", "loop", "SALIDA_V%d_APERTURA.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    io.open(os.path.join(RAIZ, "docs", "loop",
                         "SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA),
            "w", encoding="utf-8", newline=NL).write(head.strip() + NL)
    sys.stdout.write(texto)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
