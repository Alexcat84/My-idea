# -*- coding: utf-8 -*-
r"""CONTADOR DE MIS CLASES, VUELTA 203. Un solo uso, prefijo de guion bajo, FUERA
del censo y FUERA de la nomina congelada en 135: no fabrica maquinaria y no roza
la moratoria `AUDITOR.md` 6.3. Es el remedio de la caida propia `C.A1` (teclear
el resumen en vez de contarlo) que el acta 200 mando y el acta 201 estreno; la
201 no dejo su contador escrito, solo su salida, asi que este se escribe aqui.

NO LEE NI `clase` NI `razon` DEL ARCHIVO DE VEREDICTOS. Solo mira mi fichero de
clases y el sello, o sea que correrlo NO destapa nada y no toca la cuarta puerta.
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
MIS = os.path.join(LOOP, "_auditor_v203_mis_clases.txt")
SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V203.json")

FILA = re.compile(r"^(\d+)\s+([ABCD])\s+(\*?)")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    texto = io.open(MIS, encoding="utf-8").read()
    lineas = texto.split("\n")

    filas = []
    for l in lineas:
        m = FILA.match(l)
        if m:
            filas.append((int(m.group(1)), m.group(2), m.group(3) == "*"))

    reparto = {}
    for _p, c, _a in filas:
        reparto[c] = reparto.get(c, 0) + 1

    # LOS PUESTOS SELLADOS SE LEEN DEL SELLO Y DE LA CIEGA, NO SE TECLEAN.
    sello = json.load(io.open(SELLO, encoding="utf-8"))
    ciega = io.open(os.path.join(RAIZ, sello["ciega"]), encoding="utf-8").read()
    sellados = [int(x) for x in re.findall(r"^puesto_intra:\s*(\d+)",
                                           ciega, re.M)]

    mios = [p for p, _c, _a in filas]
    faltan = [p for p in sellados if p not in mios]
    sobran = [p for p in mios if p not in sellados]

    con_asterisco = sorted(p for p, _c, a in filas if a)

    # LOS DISCUTIBLES DEL PIE: todo numero que aparezca tras la ultima cabecera
    # `MIS DISCUTIBLES`. Se leen de ahi y se cotejan contra los asteriscos.
    corte = texto.rfind("MIS DISCUTIBLES")
    del_pie = sorted(int(x) for x in re.findall(r"\b(\d{1,4})\b", texto[corte:]))
    del_pie = [x for x in del_pie if x in sellados]

    print("CONTADOR DE MIS CLASES, VUELTA 203")
    print("  fichero: docs/loop/_auditor_v203_mis_clases.txt (%d bytes en disco)"
          % os.path.getsize(MIS))
    print("  filas con clase: %d" % len(filas))
    print("  REPARTO CONTADO: A %d  B %d  C %d  D %d"
          % (reparto.get("A", 0), reparto.get("B", 0),
             reparto.get("C", 0), reparto.get("D", 0)))
    print("  suma del reparto: %d" % sum(reparto.values()))
    print("  puestos SELLADOS (leidos del sello y de la ciega): %d" % len(sellados))
    print("  puestos MIOS distintos: %d" % len(set(mios)))
    print("  sellados SIN clase mia: %s"
          % (", ".join(str(x) for x in faltan) if faltan else "ninguno"))
    print("  clases mias FUERA del sello: %s"
          % (", ".join(str(x) for x in sobran) if sobran else "ninguna"))
    print("  discutibles con asterisco en las filas: %d -> %s"
          % (len(con_asterisco), con_asterisco))
    print("  discutibles listados al pie:            %d -> %s"
          % (len(del_pie), del_pie))
    print("  LAS DOS LISTAS DE DISCUTIBLES CALZAN: %s"
          % ("SI" if con_asterisco == del_pie else "NO"))
    return 0 if (not faltan and not sobran and con_asterisco == del_pie
                 and len(filas) == len(sellados)) else 1


if __name__ == "__main__":
    sys.exit(main())
