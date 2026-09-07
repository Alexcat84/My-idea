# -*- coding: utf-8 -*-
"""EL COTEJO DE LA CIEGA 196. Mis clases contra el archivo, POR LA CUARTA PUERTA
(AP.leer_veredictos con destapar_sujeto=True), ya con las clases declaradas."""
import io, os, re, sys
sys.path.insert(0, os.path.join("scripts", "loop"))
import apertura_del_auditor as AP
sys.stdout.reconfigure(encoding="utf-8")
NL = chr(10)

mias = {}
disc = set()
for l in io.open("docs/loop/_auditor_v196_mis_clases.txt", encoding="utf-8"):
    m = re.match(r"^(\d+)\s*\|\s*([ABCD])\s*\|(.*?)\|", l)
    if m:
        mias[int(m.group(1))] = m.group(2)
        if m.group(3).strip():
            disc.add(int(m.group(1)))

filas = AP.leer_veredictos(destapar_sujeto=True)
arch = {}
for f in filas:
    p = f.get("puesto_intra")
    if p in mias:
        arch[p] = f.get("clase")

QUEMADOS = {654, 719}
print("=" * 78)
print("COTEJO DE LA CIEGA DE LA VUELTA 196")
print("=" * 78)
print("sujeto sellado: %d puestos | mis clases: %d | filas del archivo halladas: %d"
      % (len(AP.puestos_sellados()), len(mias), len(arch)))
print("bitacora del turno: %s" % ", ".join(AP.bitacora()))
print()
coin = []
disc_l = []
for p in sorted(mias):
    if arch.get(p) == mias[p]:
        coin.append(p)
    else:
        disc_l.append(p)
print("MIS CLASES:    A %d | B %d | C %d | D %d"
      % tuple(sum(1 for v in mias.values() if v == c) for c in "ABCD"))
print("EL ARCHIVO:    A %d | B %d | C %d | D %d"
      % tuple(sum(1 for v in arch.values() if v == c) for c in "ABCD"))
print()
print("COINCIDEN: %d de %d" % (len(coin), len(mias)))
print("DISCREPAN: %d -> %s" % (len(disc_l), ", ".join(str(x) for x in disc_l)))
print()
print("SIN LOS DOS QUEMADOS (654, 719), que salen del credito por declaracion:")
c2 = [p for p in coin if p not in QUEMADOS]
d2 = [p for p in disc_l if p not in QUEMADOS]
print("   COINCIDEN: %d de %d | DISCREPAN: %d" % (len(c2), len(mias) - 2, len(d2)))
print()
print("LAS DISCREPANCIAS, UNA A UNA, CON MI MARCADO DELANTE:")
dentro, fuera = [], []
for p in disc_l:
    marca = "DENTRO de mi marcado" if p in disc else "FUERA de mi marcado"
    (dentro if p in disc else fuera).append(p)
    print("   %-5s yo %s | archivo %s | %s%s"
          % (p, mias[p], arch.get(p), marca,
             "  [QUEMADO]" if p in QUEMADOS else ""))
print()
print("REPARTO: DENTRO %d -> %s" % (len(dentro), ", ".join(str(x) for x in dentro) or "-"))
print("         FUERA  %d -> %s" % (len(fuera), ", ".join(str(x) for x in fuera) or "-"))
fuera_limpio = [p for p in fuera if p not in QUEMADOS]
print("         FUERA sin quemados %d -> %s"
      % (len(fuera_limpio), ", ".join(str(x) for x in fuera_limpio) or "-"))
print()
print("MIS DISCUTIBLES QUE ACERTE (marcados y coincidentes): %s"
      % ", ".join(str(p) for p in sorted(disc) if p in coin))
print("MIS DISCUTIBLES MARCADOS: %d" % len(disc))
io.open("docs/loop/_auditor_v196_cotejo_tabla.txt", "w", encoding="utf-8",
        newline=NL).write(NL.join(
    "%d|%s|%s|%s" % (p, mias[p], arch.get(p), "DISCUTIBLE" if p in disc else "")
    for p in sorted(mias)) + NL)
