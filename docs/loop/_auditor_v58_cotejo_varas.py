# -*- coding: utf-8 -*-
# Cotejo fila a fila: mi cuadro propio contra SALIDA_V58_VARAS_TRAMO5.txt
import io, re

mias = {}
for l in io.open("docs/loop/_auditor_v58_varas_tramo5_propio.txt", encoding="utf-8"):
    if l.startswith("POR FORMA"):
        continue
    p = l.rstrip("\n").split("|")
    mias[int(p[0])] = (p[1], p[2], p[3], p[4], p[5])

FORMAS = ("TODAS DE ACUERDO", "UNA SOLA VARA", "CHOCAN", "CONTENIDO EMPATA", "EMPATE SIN VARA")
dif = 0
vistas = 0
for l in io.open("docs/loop/SALIDA_V58_VARAS_TRAMO5.txt", encoding="utf-8"):
    m = re.match(r"\s+(\d+)\s+(\S+)\s+(\S+)\s+(.*)$", l)
    if not m:
        continue
    n = int(m.group(1))
    if n not in mias:
        continue
    vistas += 1
    resto = m.group(4)
    forma_ej = next((f for f in FORMAS if f in resto), None)
    mia = mias[n]
    ok_m = (m.group(2) == mia[0] and m.group(3) == mia[1])
    ok_f = (forma_ej == mia[4])
    # los conteos del ejecutor: pares x/y en el resto
    nums = re.findall(r"(\d+)/(\d+)\s*", resto)
    mis1 = tuple(int(x) for x in re.findall(r"\d+", mia[2]))
    mis2 = tuple(int(x) for x in re.findall(r"\d+", mia[3]))
    ok_c = len(nums) >= 3 and all(int(nums[i][0]) == mis1[i] and int(nums[i][1]) == mis2[i] for i in range(3))
    if not (ok_m and ok_f and ok_c):
        dif += 1
        print("DIF acto", n, "| miembros ok:", ok_m, "| forma ej:", forma_ej, "mia:", mia[4], "| conteos ok:", ok_c)
print("filas cotejadas:", vistas, "| DISTINTAS:", dif)
