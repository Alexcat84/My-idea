# -*- coding: utf-8 -*-
r"""_v208_apertura.py . COMPUTO DE LA VUELTA 208, CON PREFIJO DE GUION BAJO,
FUERA DEL CENSO Y FUERA DE LA NOMINA (moratoria de AUDITOR.md 6.3).

QUE HACE: mide el estado del arbol ANTES DE LA PRIMERA OPERACION de la vuelta
(EJECUTOR.md 1, LA APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION) y lo sella.

IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5). `git` y `shas` se IMPORTAN
de `_v208_apertura`'s predecesor `_v207_apertura.py`, que a su vez importa
`medir_en_disco` de `vuelta186_rutas_del_reporte.py`, la sede unica de las dos
convenciones. Aqui NO se copia ni una linea de esas funciones: solo cambia LA
LISTA DE SEDES que esta vuelta va a nombrar y el numero de vuelta, que se
computa del propio nombre del fichero y no se teclea.

Y LA LINEA DE STATUS VA EN LA FORMA QUE LA GUARDA SABE LEER. La correccion
declarada al pie del sello de la 207 midio que `cerrar_reporte.py` busca el
literal `CIFRA lineas de status: <n>` con los dos puntos PEGADOS a la palabra
`status`, y que la coma de la 207 le rompia la coincidencia. Aqui se escribe ya
en esa forma, y la version con glosa va detras.
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v207_apertura import git, shas, RAIZ  # noqa: E402
from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402

NL = chr(10)
# EL NUMERO DE VUELTA SE COMPUTA DEL NOMBRE DEL FICHERO, NO SE TECLEA.
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

RUTAS = [
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/REPORTE.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/PENDIENTES.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/INTRA_DOMINIO_INFORME.md",
    "docs/BANCO_DE_TEXTOS.md",
    "docs/plan/BANCO_DEL_PLAN.md",
    "docs/plan/OP_L_03_LECTURAS.jsonl",
    "docs/plan/OP_L_03_TRIANGULOS.jsonl",
    "docs/plan/CORRECCIONES_A_APLICAR.md",
]

# LAS TRES SEDES DEL AUDITOR, que el encargo exige en 0 al cierre y de las que
# hay que DISTINGUIR el cero de ausencia del cero de fichero vacio.
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
    for nombre in ("REPORTE_V207.md",):
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
