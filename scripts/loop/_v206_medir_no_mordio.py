# -*- coding: utf-8 -*-
r"""_v206_medir_no_mordio.py . COMPUTO DE LA VUELTA 206, NO MAQUINARIA.

MIDE EN POSITIVO la premisa de una PARADA antes de declararla: cuantas entradas
de la nomina NO MORDIERON en la bateria de la 205, tramo por tramo, leidas de las
lineas que el propio arnes escribio en cada salida sellada.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")

P_BLOQUE = re.compile(r"^\s+NO MORDIO\s*:\s*(\d+)\s*\((.*?)\)\s*$", re.M)
P_ANCLA = re.compile(r"^\s+ANCLA PERDIDA\s*:\s*(\d+)\s*\((.*?)\)\s*$", re.M)
P_REPRO = re.compile(r"^\s+NO REPRODUCIBLE:\s*(\d+)\s*\((.*?)\)\s*$", re.M)
P_FALLO = re.compile(r"^\s+CIFRA de FALLO:\s*(.+)$", re.M)
P_LINEA = re.compile(r"^\s{2}(\S+\.py)\s+exit (-?\d+)\s+NO MORDIO", re.M)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("LA PREMISA, MEDIDA EN POSITIVO ANTES DE DECLARAR NADA")
    print("=" * 78)
    total_nm = 0
    nombres = []
    familias = set()
    for n in range(1, 12):
        ruta = os.path.join(LOOP, "SALIDA_V205_BATERIA_TRAMO_%d.txt" % n)
        t = io.open(ruta, encoding="utf-8", errors="replace").read().replace("\r\n", "\n")
        nm = P_BLOQUE.search(t)
        an = P_ANCLA.search(t)
        rp = P_REPRO.search(t)
        fa = P_FALLO.findall(t)
        marcadas = P_LINEA.findall(t)
        c = int(nm.group(1)) if nm else None
        total_nm += c or 0
        if nm and c:
            nombres.extend([x.strip() for x in nm.group(2).split(",") if x.strip()])
        print("  TRAMO %-2d | NO MORDIO %s | ANCLA PERDIDA %s | NO REPRODUCIBLE %s"
              % (n, nm.group(1) if nm else "EL PATRON NO ENCONTRO NADA",
                 an.group(1) if an else "EL PATRON NO ENCONTRO NADA",
                 rp.group(1) if rp else "EL PATRON NO ENCONTRO NADA"))
        print("           | lineas de entrada marcadas NO MORDIO: %d %s"
              % (len(marcadas), [m[0] for m in marcadas]))
        for f in fa:
            print("           | CIFRA de FALLO: %s" % f.strip())
            familias.add(f.strip())
    print("")
    print("  CIFRA total de entradas que NO MORDIERON en los once tramos: %d" % total_nm)
    print("  CIFRA nombres distintos: %d" % len(set(nombres)))
    for x in sorted(set(nombres)):
        print("      NO MORDIO: %s" % x)
    print("")
    print("  CIFRA familias distintas de la linea CIFRA de FALLO: %d" % len(familias))
    for f in sorted(familias):
        print("      FAMILIA: %s" % f)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
