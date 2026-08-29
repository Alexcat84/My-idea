# -*- coding: utf-8 -*-
"""Genera docs/loop/SALIDA_V128_BATERIAS_CMP.txt: cmp -s por pares, una linea
por par, dentro de cada familia de la vuelta 128 (TAREA 1.d)."""
import filecmp
import itertools
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")

FAMILIAS = {
    "GATE0": ["SALIDA_V128_GATE0_CMD1_APERTURA.txt", "SALIDA_V128_OPS09REP3_GATE0_POST.txt",
              "SALIDA_V128_OPS10_GATE0_POST.txt", "SALIDA_V128_GATE0_CMD1_CIERRE.txt"],
    "CONTEO": ["SALIDA_V128_CONTEO_APERTURA.txt", "SALIDA_V128_OPS09REP3_CONTEO_POST.txt",
               "SALIDA_V128_OPS10_CONTEO_POST.txt", "SALIDA_V128_CONTEO_CIERRE.txt"],
    "MOTOR": ["SALIDA_V128_MOTOR_APERTURA.txt", "SALIDA_V128_OPS09REP3_MOTOR_POST.txt",
              "SALIDA_V128_OPS10_MOTOR_POST.txt", "SALIDA_V128_MOTOR_CIERRE.txt"],
    "WEB": ["SALIDA_V128_WEB_APERTURA.txt", "SALIDA_V128_OPS09REP3_WEB_POST.txt",
            "SALIDA_V128_OPS10_WEB_POST.txt", "SALIDA_V128_WEB_CIERRE.txt"],
    "TSC": ["SALIDA_V128_TSC_APERTURA.txt", "SALIDA_V128_OPS09REP3_TSC_POST.txt",
            "SALIDA_V128_OPS10_TSC_POST.txt", "SALIDA_V128_TSC_CIERRE.txt"],
    "DESFASE": ["SALIDA_V128_DESFASE_CALIBRADO_APERTURA.txt", "SALIDA_V128_DESFASE_CALIBRADO_CIERRE.txt"],
    "MARCADOR": ["SALIDA_V128_MARCADOR_APERTURA.txt", "SALIDA_V128_MARCADOR_CIERRE.txt"],
    "ETIQUETAS": ["SALIDA_V128_CICLO_ETIQUETAS_APERTURA.txt", "SALIDA_V128_OPS09REP3_CICLO_ETIQUETAS.txt",
                  "SALIDA_V128_OPS10_CICLO_ETIQUETAS.txt", "SALIDA_V128_CICLO_ETIQUETAS_CIERRE.txt"],
    "SYNC": ["SALIDA_V128_CICLO_SYNC_APERTURA.txt", "SALIDA_V128_OPS09REP3_CICLO_SYNC.txt",
             "SALIDA_V128_OPS10_CICLO_SYNC.txt", "SALIDA_V128_CICLO_SYNC_CIERRE.txt"],
    "NUMSTAT": ["SALIDA_V128_CICLO_NUMSTAT_APERTURA.txt", "SALIDA_V128_OPS09REP3_CICLO_NUMSTAT.txt",
                "SALIDA_V128_OPS10_CICLO_NUMSTAT.txt", "SALIDA_V128_CICLO_NUMSTAT_CIERRE.txt"],
}

etiquetas_lado = {
    "APERTURA": "APERTURA", "OPS09REP3": "OPS09REP3", "OPS10": "OPS10", "CIERRE": "CIERRE",
}


def lado_de(nombre):
    if "APERTURA" in nombre:
        return "APERTURA"
    if "OPS09REP3" in nombre:
        return "OPS09REP3"
    if "OPS10" in nombre:
        return "OPS10"
    if "CIERRE" in nombre:
        return "CIERRE"
    return nombre


def main():
    out = []
    resumen = {}
    for familia, archivos in FAMILIAS.items():
        idénticos = 0
        distintos = 0
        for a, b in itertools.combinations(archivos, 2):
            pa, pb = os.path.join(LOOP, a), os.path.join(LOOP, b)
            la, lb = lado_de(a), lado_de(b)
            if not os.path.exists(pa) or not os.path.exists(pb):
                out.append("%s: %s vs %s: FALTA FICHERO" % (familia, la, lb))
                continue
            igual = filecmp.cmp(pa, pb, shallow=False)
            out.append("%s: %s vs %s: %s" % (familia, la, lb, "IDENTICOS" if igual else "DISTINTOS"))
            if igual:
                idénticos += 1
            else:
                distintos += 1
        resumen[familia] = (idénticos, distintos)
    with open(os.path.join(LOOP, "SALIDA_V128_BATERIAS_CMP.txt"), "w", encoding="utf-8", newline="\n") as fh:
        for line in out:
            fh.write(line + "\n")
        fh.write("\n")
        for familia, (i, d) in resumen.items():
            fh.write("RESUMEN %s: %d IDENTICOS, %d DISTINTOS\n" % (familia, i, d))
    for line in out:
        print(line)
    print()
    for familia, (i, d) in resumen.items():
        print("RESUMEN %s: %d IDENTICOS, %d DISTINTOS" % (familia, i, d))


if __name__ == "__main__":
    main()
