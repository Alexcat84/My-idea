# -*- coding: utf-8 -*-
"""LOS TRES PROHIBIDOS, ABIERTOS POR LA PUERTA QUE LOS APUNTA. Despues del sello."""
import io, os, sys
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import apertura_del_auditor as AP
NL = chr(10)
sys.stdout.reconfigure(encoding="utf-8")

log = AP.git_log("--oneline", "-14")
est = AP.git_status("--porcelain")
rep = AP.leer_reporte()

io.open(os.path.join(RAIZ, "docs", "loop", "_auditor_v195_reporte_copia.txt"),
        "w", encoding="utf-8", newline=NL).write(rep)
print("BITACORA DEL TURNO: %s" % ", ".join(AP.bitacora()))
print("SELLO EN DISCO V195: %s" % AP.sello_en_disco("195"))
print("=" * 70)
print("GIT LOG --oneline -14")
print(log)
print("=" * 70)
print("GIT STATUS --porcelain (%d lineas)" % len([l for l in est.split(NL) if l.strip()]))
print(est)
print("=" * 70)
print("REPORTE.md: %d bytes leidos, %d lineas por split" % (len(rep), len(rep.split(NL))))
