# -*- coding: utf-8 -*-
"""APERTURA DEL AUDITOR DE LA VUELTA 188 (acta 188, sello V189).
Sella PRIMERO y solo eso; despues toca los tres prohibidos por sus funciones."""
import io, os, sys
sys.path.insert(0, os.path.join("scripts", "loop"))
from apertura_del_auditor import (sellar, git_log, git_status, leer_reporte,
                                  bitacora, puede_sellar)

sys.stdout.reconfigure(encoding="utf-8")
EX = io.open("docs/loop/_auditor_v189_exclusion.txt", encoding="utf-8").read().strip()
CRIT = ("muestra fresca de 30 puestos con semilla 1892 sobre todo el archivo, "
        "excluyendo los 351 puestos que las ciegas de las actas 183 a 187 y sus "
        "vecinos deterministas ya consumieron (docs/loop/_auditor_v189_exclusion.txt)")
ok, informe = sellar(criterio=CRIT, vuelta="189", muestra=30, semilla=1892, excluir=EX)
L = ["=" * 78, "APERTURA SELLADA DEL AUDITOR, ACTA 188, SELLO V189", "=" * 78]
L += ["   " + x for x in informe]
L.append("   VEREDICTO DEL SELLO: %s" % ("VERDE" if ok else "ROJO"))
if not ok:
    io.open("docs/loop/_auditor_v189_apertura_toques.txt", "w", encoding="utf-8",
            newline=chr(10)).write(chr(10).join(L) + chr(10))
    print(chr(10).join(L)); sys.exit(1)
L.append("")
L.append("--- AHORA SI: LOS TRES PROHIBIDOS, POR SUS FUNCIONES, QUE APUNTAN SU TOQUE")
gl = git_log("--oneline", "-40")
gs = git_status("--short")
rep = leer_reporte()
L.append("git log --oneline -40:")
L += ["   | " + x for x in gl.split(chr(10)) if x.strip()]
L.append("git status --short: %d lineas" % len([x for x in gs.split(chr(10)) if x.strip()]))
L += ["   | " + x for x in gs.split(chr(10)) if x.strip()][:40]
L.append("REPORTE.md leido: %d caracteres, %d lineas"
         % (len(rep), len(rep.split(chr(10)))))
L.append("")
L.append("BITACORA DEL TURNO: %s" % ", ".join(bitacora()))
sipuede, motivo = puede_sellar()
L.append("PUEDE SELLAR AHORA: %s (%s)" % ("SI" if sipuede else "NO", motivo))
io.open("docs/loop/_auditor_v189_apertura_toques.txt", "w", encoding="utf-8",
        newline=chr(10)).write(chr(10).join(L) + chr(10))
print(chr(10).join(L))
