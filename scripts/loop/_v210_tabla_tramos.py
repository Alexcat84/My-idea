# -*- coding: utf-8 -*-
r"""_v210_tabla_tramos.py . LAS DOS TABLAS DE LA TAREA 1, IMPRESAS DE LOS ONCE
FICHEROS SELLADOS Y DE `git log`, NUNCA TECLEADAS.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo, fuera de la
nomina (congelada en 135), no vigila nada y muere con la vuelta (moratoria de
`AUDITOR.md` 6.3).

POR QUE EXISTE, Y ES LETRA DE `EJECUTOR.md` 1: *"LA TABLA SE IMPRIME, NO SE
TECLEA"* y *"TODA TABLA O CIFRA DEL REPORTE CITA EL FICHERO DE SALIDA DEL QUE
SALE, Y SE RECONSTRUYE CONTANDO ESE FICHERO ANTES DE PUBLICARLA"*. Las dos
tablas que la TAREA 1 debe publicar son justo las que el tallador de cabecera no
alcanza, que es donde la casa lleva vueltas volviendo a teclear.

LAS DOS TABLAS:

  A. EL CALIBRE. Fila por tramo, con las dos convenciones de bytes, lineas,
     `sha256` LF, entradas corridas, el reparto de veredictos por arnes y las
     cifras de fallo recomputadas al cierre por el propio tramo. Es lo que hace
     comparables los once y lo que `AUDITOR.md` 6.1 llama DEL MISMO CALIBRE.

  B. LA FRESCURA. Fila por tramo con el commit que lo sello, LEIDO DE `git log`
     y no tecleado, y la vuelta que ese asunto nombra. Es la unica vara que
     queda cuando el nombre del fichero no la da: el lanzador computa su vuelta
     de su propio nombre, asi que sus salidas se llaman `V183` corra la vuelta
     que corra.

IMPORTAR NO ES CLONAR (acta 206, `6.5`): `medir`, `nombre_tramo`,
`nombre_de_la_compuesta` y `entradas_de_la_salida` salen del lanzador, que es su
sede unica y al que esta vuelta no le toca una linea; `vuelta_que_sello` sale de
`cerrar_reporte.py`, que es la sede de esa lectura desde la vuelta 185.

USO:  python scripts/loop/_v210_tabla_tramos.py
"""
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from vuelta183_bateria_por_tramos import (  # noqa: E402
    medir, nombre_tramo, nombre_de_la_compuesta, entradas_de_la_salida,
    LOOP, RAIZ)
from cerrar_reporte import vuelta_que_sello  # noqa: E402

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
PATRON_FILA = re.compile(r"^  (\S+\.py)\s+exit (-?\d+)\s+(.+?)\s+([\d.]+)s\s*$")


def uno(texto, patron, defecto="?"):
    m = re.findall(patron, texto)
    return m[0] if len(m) == 1 else defecto


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", errors="replace").strip()


def main():
    out = []
    w = out.append
    w("LAS DOS TABLAS DE LA TAREA 1 DE LA VUELTA %d, IMPRESAS DE LOS FICHEROS" % VUELTA)
    w("SELLADOS Y DE git log, NUNCA TECLEADAS.")
    w("")

    tramos = []
    for n in range(1, 12):
        ruta = os.path.join(LOOP, nombre_tramo(n))
        if not os.path.exists(ruta):
            w("ROJO: docs/loop/%s NO EXISTE (ausencia, no cero)." % nombre_tramo(n))
            return 1
        m = medir(ruta)
        if m["bytes_disco"] == 0:
            w("ROJO: docs/loop/%s mide CERO BYTES y no cuenta como hecho."
              % nombre_tramo(n))
            return 1
        texto = io.open(ruta, encoding="utf-8", errors="replace").read().replace(
            chr(13) + NL, NL)
        filas = [f for f in (PATRON_FILA.match(l) for l in texto.split(NL)) if f]
        clases = {}
        for f in filas:
            clases[f.group(3).strip()] = clases.get(f.group(3).strip(), 0) + 1
        asunto = git(["log", "-1", "--format=%s", "--", "docs/loop/" + nombre_tramo(n)])
        tramos.append({
            "n": n, "m": m, "texto": texto, "filas": filas, "clases": clases,
            "entradas": entradas_de_la_salida(ruta),
            "hash": git(["log", "-1", "--format=%H", "--",
                         "docs/loop/" + nombre_tramo(n)]),
            "asunto": asunto,
            "sello": vuelta_que_sello(asunto),
        })

    w("A. EL CALIBRE, FILA POR TRAMO. Cada celda sale del fichero de esa fila.")
    w("")
    w("| tramo | fichero sellado | bytes disco | bytes LF | lineas | sha256 LF | entradas | OK | CASO DECLARADO | NO MORDIO | ANCLA PERDIDA | NO REPRODUCIBLE | RUIDO | exitcode | minutos |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    tot = {"entradas": 0, "OK": 0, "CASO DECLARADO": 0, "NO MORDIO": 0}
    for t in tramos:
        x = t["texto"]
        fila = ("| %d | `%s` | %d | %d | %d | `%s` | %d | %s | %s | %s | %s | %s | %s | %s | %s |"
                % (t["n"], nombre_tramo(t["n"]), t["m"]["bytes_disco"],
                   t["m"]["bytes_lf"], t["m"]["lineas"], t["m"]["sha256_lf"][:16],
                   len(t["entradas"]),
                   t["clases"].get("OK", 0), t["clases"].get("CASO DECLARADO", 0),
                   t["clases"].get("NO MORDIO", 0),
                   uno(x, r"ANCLA PERDIDA  : (\d+)"),
                   uno(x, r"NO REPRODUCIBLE: (\d+)"),
                   uno(x, r"RUIDO DE CONCURRENCIA: (\d+) fichero"),
                   uno(x, r"EXITCODE DEL TRAMO %d: (-?\d+)" % t["n"]),
                   uno(x, r"DURACION DEL TRAMO \(monotona, minutos\): ([\d.]+)")))
        w(fila)
        tot["entradas"] += len(t["entradas"])
        for k in ("OK", "CASO DECLARADO", "NO MORDIO"):
            tot[k] += t["clases"].get(k, 0)
    w("")
    w("  CIFRA suma de entradas de los once tramos: %d" % tot["entradas"])
    w("  CIFRA suma de OK: %d" % tot["OK"])
    w("  CIFRA suma de CASO DECLARADO: %d" % tot["CASO DECLARADO"])
    w("  CIFRA suma de NO MORDIO: %d" % tot["NO MORDIO"])
    w("  CIFRA suma de las tres clases: %d"
      % (tot["OK"] + tot["CASO DECLARADO"] + tot["NO MORDIO"]))
    w("  CIFRA suma de bytes en disco de los once: %d"
      % sum(t["m"]["bytes_disco"] for t in tramos))
    w("  CIFRA suma de minutos de los once: %.1f"
      % sum(float(uno(t["texto"],
                      r"DURACION DEL TRAMO \(monotona, minutos\): ([\d.]+)", "0"))
            for t in tramos))
    w("  CIFRA tramos con RUIDO DE CONCURRENCIA distinto de cero: %d"
      % sum(1 for t in tramos
            if uno(t["texto"], r"RUIDO DE CONCURRENCIA: (\d+) fichero", "0") != "0"))
    w("  CIFRA tramos con exitcode distinto de 1: %d"
      % sum(1 for t in tramos
            if uno(t["texto"], r"EXITCODE DEL TRAMO %d: (-?\d+)" % t["n"], "?") != "1"))
    w("")

    w("  LOS NO MORDIO, UNO A UNO, CON EL TRAMO QUE LOS CAZO:")
    cuantos = 0
    for t in tramos:
        for f in t["filas"]:
            if f.group(3).strip() == "NO MORDIO":
                cuantos += 1
                w("      tramo %-2d  %-52s exit %s" % (t["n"], f.group(1), f.group(2)))
    w("  CIFRA entradas NO MORDIO, contadas de las filas: %d" % cuantos)
    w("  calza con la suma de la columna NO MORDIO (%d): %s"
      % (tot["NO MORDIO"], "SI" if cuantos == tot["NO MORDIO"] else "NO"))
    w("")

    w("B. LA FRESCURA. QUE COMMIT SELLO CADA TRAMO, LEIDO DE git log.")
    w("")
    w("| tramo | commit que lo sello | vuelta que nombra su asunto |")
    w("|---|---|---|")
    for t in tramos:
        w("| %d | `%s` | %s |" % (t["n"], t["hash"][:8],
                                  t["sello"] if t["sello"] is not None
                                  else "(el asunto no la nombra)"))
    compuesta = nombre_de_la_compuesta()
    a_c = git(["log", "-1", "--format=%s", "--", "docs/loop/" + compuesta])
    h_c = git(["log", "-1", "--format=%H", "--", "docs/loop/" + compuesta])
    w("| compuesta | `%s` | %s |" % (h_c[:8], vuelta_que_sello(a_c)))
    w("")
    de_la_vuelta = [t["n"] for t in tramos if t["sello"] == VUELTA]
    w("  CIFRA tramos cuyo commit nombra la VUELTA %d: %d de 11"
      % (VUELTA, len(de_la_vuelta)))
    w("  LOS TRAMOS: %s" % ", ".join(str(x) for x in de_la_vuelta))
    w("  CIFRA tramos cuyo commit nombra OTRA vuelta: %d"
      % sum(1 for t in tramos if t["sello"] != VUELTA))
    w("  POR QUE ESTA TABLA ES LA VARA Y NO EL NOMBRE DEL FICHERO: el lanzador")
    w("  computa su vuelta de os.path.basename(__file__), asi que sus salidas se")
    w("  llaman SALIDA_V183_* corra la vuelta que corra. El nombre no dice de que")
    w("  vuelta es la CORRIDA; el commit si.")
    w("")

    ruta_c = os.path.join(LOOP, compuesta)
    mc = medir(ruta_c)
    w("C. LA SALIDA UNICA, REMEDIDA AQUI Y NO COPIADA DE --componer:")
    w("  docs/loop/%s: %d bytes en disco y %d normalizado a LF, %d lineas, sha256 LF %s"
      % (compuesta, mc["bytes_disco"], mc["bytes_lf"], mc["lineas"],
         mc["sha256_lf"][:16]))
    w("")

    texto = NL.join(out) + NL
    destino = os.path.join(LOOP, "SALIDA_V%d_T1E_TABLAS.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
