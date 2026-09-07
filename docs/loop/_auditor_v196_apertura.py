# -*- coding: utf-8 -*-
"""APERTURA DEL AUDITOR 196: git log, git status y REPORTE.md POR LAS FUNCIONES
QUE APUNTAN SU TOQUE, despues del sello. No se toca ninguno de los tres a mano."""
import io, os, sys
sys.path.insert(0, os.path.join("scripts", "loop"))
import apertura_del_auditor as AP
sys.stdout.reconfigure(encoding="utf-8")
NL = chr(10)
log = AP.git_log("--oneline", "-14")
est = AP.git_status("--porcelain")
rep = AP.leer_reporte()
io.open("docs/loop/_auditor_v196_gitlog.txt", "w", encoding="utf-8", newline=NL).write(log)
io.open("docs/loop/_auditor_v196_gitstatus.txt", "w", encoding="utf-8", newline=NL).write(est or "(limpio)" + NL)
print("=" * 78)
print("GIT LOG (por AP.git_log)")
print("=" * 78)
print(log)
print("=" * 78)
print("GIT STATUS --porcelain (por AP.git_status): %d lineas"
      % len([l for l in est.split(NL) if l.strip()]))
print("=" * 78)
print(est if est.strip() else "(limpio)")
print("=" * 78)
print("REPORTE.md (por AP.leer_reporte): %d bytes, %d lineas"
      % (os.path.getsize("docs/loop/REPORTE.md"), len(rep.split(NL))))
print("BITACORA DEL TURNO: %s" % ", ".join(AP.bitacora()))
