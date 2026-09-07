# -*- coding: utf-8 -*-
"""COTEJO DE LA CIEGA DEL AUDITOR 197. Corre DESPUES de declarar las clases."""
import io, re, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
NL = chr(10)

MIAS = "docs/loop/_auditor_v197_mis_clases.txt"
DEST = "docs/loop/_auditor_v197_ciega_reveal.txt"
# LOS QUEMADOS SALEN DE _auditor_v197_contaminacion.txt Y NO SE TECLEAN AQUI.
CONT = "docs/loop/_auditor_v197_contaminacion.txt"

t = io.open(MIAS, encoding="utf-8").read()
mias = {int(p): c for p, c in re.findall(r"^(\d+)\s+([ABCD])\s", t, re.M)}

d = io.open(DEST, encoding="utf-8").read()
arch = {}
puesto = None
for l in d.split(NL):
    m = re.match(r"^puesto_intra:\s*(\d+)", l)
    if m:
        puesto = int(m.group(1)); continue
    m = re.match(r"^\s*clase:\s*([ABCD])\s*$", l)
    if m and puesto is not None:
        arch[puesto] = m.group(1)

ct = io.open(CONT, encoding="utf-8").read()
quemados = sorted(set(int(x) for x in re.findall(r"^\s+(\d+)\s+->\s+[ABCD]\s", ct, re.M)))

print("=" * 78)
print("COTEJO DE LA CIEGA, AUDITOR DE LA VUELTA 197")
print("=" * 78)
print("CIFRA mis clases: %d" % len(mias))
print("CIFRA clases del archivo leidas del destape: %d" % len(arch))
print("CIFRA quemados leidos de la declaracion de contaminacion: %d -> %s"
      % (len(quemados), ", ".join(str(q) for q in quemados)))
faltan = sorted(set(mias) - set(arch))
print("CIFRA puestos sin clase en el destape: %d %s" % (len(faltan), faltan or ""))

def tabla(nombre, puestos):
    ok = [p for p in puestos if mias[p] == arch[p]]
    no = [p for p in puestos if mias[p] != arch[p]]
    print("")
    print("-- %s: n=%d" % (nombre, len(puestos)))
    print("   CIFRA coinciden: %d de %d" % (len(ok), len(puestos)))
    print("   CIFRA discrepan: %d -> %s" % (len(no), ", ".join(str(p) for p in no) or "(ninguna)"))
    print("   reparto mio    : %s" % sorted(Counter(mias[p] for p in puestos).items()))
    print("   reparto archivo: %s" % sorted(Counter(arch[p] for p in puestos).items()))
    return no

todos = sorted(set(mias) & set(arch))
limpios = [p for p in todos if p not in quemados]
d_todos = tabla("LOS 120 ENTEROS", todos)
d_limpios = tabla("LOS LIMPIOS, SIN LOS QUEMADOS, Y ES LA CIFRA QUE MANDA", limpios)
d_quem = tabla("SOLO LOS QUEMADOS, publicados y FUERA del credito", sorted(quemados))

print("")
print("=" * 78)
print("LAS DISCREPANCIAS, UNA POR UNA")
print("=" * 78)
print("%-8s %-6s %-8s %s" % ("puesto", "mia", "archivo", "quemado"))
for p in d_todos:
    print("%-8d %-6s %-8s %s" % (p, mias[p], arch[p], "SI" if p in quemados else "no"))
print("")
print("CIFRA discrepancias totales: %d" % len(d_todos))
print("CIFRA discrepancias limpias: %d" % len(d_limpios))
print("CIFRA discrepancias quemadas: %d" % len(d_quem))
