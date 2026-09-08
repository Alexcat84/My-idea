# -*- coding: utf-8 -*-
r"""_v210_apertura.py . COMPUTO DE LA VUELTA 210, CON PREFIJO DE GUION BAJO,
FUERA DEL CENSO Y FUERA DE LA NOMINA (moratoria de AUDITOR.md 6.3).

QUE HACE: mide el estado del arbol ANTES DE LA PRIMERA OPERACION de la vuelta
(EJECUTOR.md 1, LA APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION) y lo sella.

IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5). `git`, `shas` y `RAIZ` se
IMPORTAN de `_v209_apertura`, que los importa de `_v208_apertura`, que a su vez
importa `medir_en_disco` de `vuelta186_rutas_del_reporte.py`, la sede unica de
las dos convenciones. Aqui NO se copia ni una linea de esas funciones: solo
cambia LA LISTA DE SEDES que esta vuelta va a nombrar y el numero de vuelta,
que se computa del propio nombre del fichero y no se teclea.

ESTA ES LA VUELTA DE BATERIA, asi que la lista de sedes lleva ademas LOS ONCE
FICHEROS DE TRAMO Y LA SALIDA UNICA DE LA BATERIA TAL COMO ESTAN AL ENTRAR, que
son los que esta vuelta va a pisar y cuya frescura solo prueba el commit.
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v209_apertura import git, shas, RAIZ  # noqa: E402
from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

RUTAS = [
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/REPORTE.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/PENDIENTES.md",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "scripts/loop/vuelta183_bateria_por_tramos.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "docs/loop/SALIDA_MARCADOR_AUDITOR_V209.json",
]

# LAS SEDES QUE ESTA VUELTA VA A PISAR. El lanzador computa su vuelta de su
# propio nombre, asi que sus salidas se llaman V183 corra la vuelta que corra:
# lo que hay AL ENTRAR es la corrida VIEJA, y por eso se mide aqui, antes de
# tocarla, con el commit que la sello leido de git y no tecleado.
BATERIA = ["docs/loop/SALIDA_V183_BATERIA.txt"] + [
    "docs/loop/SALIDA_V183_BATERIA_TRAMO_%d.txt" % n for n in range(1, 12)]

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
        out.append("CIFRA " + ruta + ": " + str(m[0])
                   + " bytes en disco y " + str(m[1])
                   + " bytes normalizado a LF, sha256 disco " + sd
                   + " y sha256 LF " + sl)
    out.append("")
    out.append("LAS SEDES DE LA BATERIA TAL COMO ESTAN AL ENTRAR, ANTES DE PISARLAS,")
    out.append("CON LA VUELTA QUE LAS SELLO LEIDA DEL ASUNTO DE SU ULTIMO COMMIT:")
    for ruta in BATERIA:
        p = os.path.join(RAIZ, ruta.replace("/", os.sep))
        if not os.path.isfile(p):
            out.append("CIFRA " + ruta + ": NO EXISTE (ausencia, no cero)")
            continue
        m = medir_en_disco(RAIZ, ruta)
        sd, sl = shas(ruta)
        _, asu = git(["log", "-1", "--format=%s", "--", ruta])
        _, hsh = git(["log", "-1", "--format=%H", "--", ruta])
        mv = re.search(r"\bVUELTA\s+(\d+)", asu.strip())
        out.append("CIFRA " + ruta + ": " + str(m[0])
                   + " bytes en disco y " + str(m[1])
                   + " bytes normalizado a LF, sha256 disco " + sd
                   + " y sha256 LF " + sl)
        out.append("  ultimo commit " + hsh.strip()[:8] + ", vuelta que lo sello: "
                   + (mv.group(1) if mv else "(el asunto no la nombra)"))
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
    for nombre in ("REPORTE_V209.md",):
        p = os.path.join(RAIZ, "docs", "loop", "reportes", nombre)
        out.append("CIFRA docs/loop/reportes/" + nombre + " existe al entrar: "
                   + ("SI" if os.path.isfile(p) else "NO"))
    texto = NL.join(out) + NL
    destino = os.path.join(RAIZ, "docs", "loop", "SALIDA_V%d_APERTURA.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
