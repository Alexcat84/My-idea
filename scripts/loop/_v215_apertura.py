# -*- coding: utf-8 -*-
r"""_v215_apertura.py . COMPUTO DE LA VUELTA 215, CON PREFIJO DE GUION BAJO,
FUERA DEL CENSO Y FUERA DE LA NOMINA (moratoria de AUDITOR.md 6.3).

QUE HACE: mide el estado del arbol ANTES DE LA PRIMERA OPERACION de la vuelta
(EJECUTOR.md 1, LA APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION) y lo sella.

IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5). git, shas y RAIZ se IMPORTAN
de _v213_apertura, que los importa de _v212_apertura, que a su vez importa
medir_en_disco de vuelta186_rutas_del_reporte.py, la sede unica de las dos
convenciones. Aqui NO se copia ni una linea de esas funciones: solo cambia LA
LISTA DE SEDES que esta vuelta va a nombrar y el numero de vuelta, que se
computa del propio nombre del fichero y no se teclea.

LA 215 SI ES VUELTA DE BATERIA (cadencia de cinco de AUDITOR.md 6.1, y el acta
214 adjudicacion 5.1 dice que son ONCE tramos y no nueve). Por eso esta apertura
lleva ADEMAS el bloque de LOS SELLOS VIEJOS: los once ficheros de tramo que hay
en el arbol AL ENTRAR, cada uno con su ultimo commit y su fecha LEIDOS DE git
log, que es lo que la TAREA 2.a manda publicar ANTES de correr nada.

LAS SEDES SON LAS QUE LA 215 VA A NOMBRAR: los tres ficheros de gobierno del
bucle, el expediente y el inventario del plan (que esta vuelta LEE y no
escribe), los dos bancos, el informe y el archivo de veredictos, el grafo
maestro y la vara del criterio de hecho.
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v213_apertura import git, shas, RAIZ  # noqa: E402
from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

RUTAS = [
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/REPORTE.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "docs/INTRA_DOMINIO_INFORME.md",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/INVENTARIO.jsonl",
    "docs/plan/08_VERIFICACION.md",
    "docs/plan/10_INVENTARIO.md",
    "docs/plan/00_INDICE.md",
    "docs/BANCO_DE_TEXTOS.md",
    "docs/plan/BANCO_DEL_PLAN.md",
    "dataset/metadata/master_graph.json",
]

SEDES_AUDITOR = [
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/PARA_ALEXIS.md",
]

# EL PATRON DE LOS SELLOS DE TRAMO. El nombre lo pone el lanzador con el numero
# de SU PROPIO fichero, el 183, y no con el de la vuelta que lo corre: por eso
# una corrida vieja y una fresca COMPARTEN NOMBRE. La cifra 183 no se teclea
# como afirmacion de vuelta: es parte del NOMBRE del fichero que hay en disco.
PATRON_SELLO = "SALIDA_V183_BATERIA_TRAMO_%d.txt"


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
    for sede in ["dataset/", "web/", "engine/", "docs/plan/", "docs/"]:
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
    out.append("LOS SELLOS DE TRAMO QUE HAY EN EL ARBOL AL ENTRAR, CON SU ULTIMO")
    out.append("COMMIT Y SU FECHA LEIDOS DE git log Y NO TECLEADOS (TAREA 2.a):")
    presentes = 0
    for n in range(1, 40):
        rel = "docs/loop/" + (PATRON_SELLO % n)
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            continue
        presentes += 1
        _, ident = git(["log", "-1", "--format=%h|%ad|%s", "--date=short",
                        "--", rel])
        trozos = ident.strip().split("|", 2)
        while len(trozos) < 3:
            trozos.append("(sin commit)")
        out.append("SELLO tramo " + str(n) + ": " + str(os.path.getsize(p))
                   + " bytes, ultimo commit " + trozos[0]
                   + ", fecha " + trozos[1]
                   + ", asunto (primeros 70) " + trozos[2][:70])
    out.append("CIFRA sellos de tramo presentes en el arbol AL ENTRAR: "
               + str(presentes))
    out.append("")
    for nombre in ("REPORTE_V214.md",):
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
