# -*- coding: utf-8 -*-
"""Genera docs/loop/SALIDA_V136_BATERIAS_CMP.txt: cmp -s por familia,
APERTURA vs CIERRE (TAREA 1.d de la vuelta 136). Adaptado de
vuelta135_baterias_cmp.py, mismo filecmp de bytes, shallow=False, sin
aflojarlo."""
import filecmp
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")

FAMILIAS = {
    "GATE0": ("SALIDA_V136_GATE0_CMD1_APERTURA.txt", "SALIDA_V136_GATE0_CMD1_CIERRE.txt"),
    "CONTEO": ("SALIDA_V136_CONTEO_APERTURA.txt", "SALIDA_V136_CONTEO_CIERRE.txt"),
    "MOTOR": ("SALIDA_V136_MOTOR_APERTURA.txt", "SALIDA_V136_MOTOR_CIERRE.txt"),
    "WEB": ("SALIDA_V136_WEB_APERTURA.txt", "SALIDA_V136_WEB_CIERRE.txt"),
    "TSC": ("SALIDA_V136_TSC_APERTURA.txt", "SALIDA_V136_TSC_CIERRE.txt"),
    "DESFASE": ("SALIDA_V136_DESFASE_CALIBRADO_APERTURA.txt", "SALIDA_V136_DESFASE_CALIBRADO_CIERRE.txt"),
    "MARCADOR": ("SALIDA_V136_MARCADOR_APERTURA.txt", "SALIDA_V136_MARCADOR_CIERRE.txt"),
    "ETIQUETAS": ("SALIDA_V136_CICLO_ETIQUETAS_APERTURA.txt", "SALIDA_V136_CICLO_ETIQUETAS_CIERRE.txt"),
    "SYNC": ("SALIDA_V136_CICLO_SYNC_APERTURA.txt", "SALIDA_V136_CICLO_SYNC_CIERRE.txt"),
    "NUMSTAT": ("SALIDA_V136_CICLO_NUMSTAT_APERTURA.txt", "SALIDA_V136_CICLO_NUMSTAT_CIERRE.txt"),
}


def main():
    out = []
    resumen = {}
    for familia, (a, b) in FAMILIAS.items():
        pa, pb = os.path.join(LOOP, a), os.path.join(LOOP, b)
        if not os.path.exists(pa) or not os.path.exists(pb):
            out.append("%s: APERTURA vs CIERRE: FALTA FICHERO" % familia)
            resumen[familia] = (0, 0)
            continue
        igual = filecmp.cmp(pa, pb, shallow=False)
        out.append("%s: APERTURA vs CIERRE: %s" % (familia, "IDENTICOS" if igual else "DISTINTOS"))
        resumen[familia] = (1, 0) if igual else (0, 1)

    with open(os.path.join(LOOP, "SALIDA_V136_BATERIAS_CMP.txt"), "w", encoding="utf-8", newline="\n") as fh:
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
    print("EXITCODE: 0")


if __name__ == "__main__":
    main()
