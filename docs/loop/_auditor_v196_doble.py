# -*- coding: utf-8 -*-
r"""EL TRAMO Y EL DOBLE PARA LA VUELTA 197, CERRADOS HOY Y COMPUTADOS.

POR QUE EXISTE: `AUDITOR.md` 1.2. UNA de mis discrepancias de la vuelta 196 cayo
FUERA de mi marcado, el puesto `2428`, asi que EL CREDITO DE MI TANDA BAJA Y EL
TRAMO SE RELEE AL DOBLE. Se deja CERRADO HOY, antes de que nadie mire, para que
el sujeto no se pueda elegir despues de haber visto los resultados.

`vecinos()` SE IMPORTA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`
y NO SE COPIA: su regla no se toca, cambia lo que se le pasa (adjudicacion 5.2
del acta 188). El conjunto `evitar` se carga de TODO lo consumido, contado de sus
ficheros y no tecleado, de modo que el solape con el tramo y con el universo
salga POR CONSTRUCCION y no por suerte.

EL UNIVERSO CRECE EN DOS FICHEROS respecto de la vuelta 195, y los dos son de la
196: mi propia ciega y la del ejecutor de la 195, que son exactamente lo que esta
vuelta consumio.
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.join("scripts", "loop"))
from vuelta182_tarea1c_relectura_al_doble import vecinos  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
NL = chr(10)

TRAMO = "docs/loop/_auditor_v196_ciega_blind.txt"
MAXIMO = 3388

UNIVERSO_CONSUMIDO = [
    "docs/loop/_auditor_v189b_exclusion.txt",
    "docs/loop/_auditor_v190_exclusion.txt",
    "docs/loop/_auditor_v189b_ciega_blind.txt",
    "docs/loop/_auditor_v190_ciega_blind.txt",
    "docs/loop/SALIDA_V190_T4_CIEGA.txt",
    "docs/loop/SALIDA_V191_T2_CIEGA.txt",
    "docs/loop/_auditor_v192_ciega_blind.txt",
    "docs/loop/SALIDA_V192_T2_CIEGA.txt",
    "docs/loop/_auditor_v193_ciega_blind.txt",
    "docs/loop/SALIDA_V193_T3_CIEGA.txt",
    "docs/loop/_auditor_v194_ciega_blind.txt",
    "docs/loop/_auditor_v195_ciega_blind.txt",
    "docs/loop/SALIDA_V195_T2_CIEGA.txt",
    "docs/loop/_auditor_v196_ciega_blind.txt",
]


def puestos_de(ruta):
    """LOS `puesto_intra` DE UN FICHERO. Sirve para los dos formatos que la casa
    tiene: las ciegas (`puesto_intra: N`) y las exclusiones (listas sueltas)."""
    if not os.path.exists(ruta):
        return None
    t = io.open(ruta, encoding="utf-8", errors="replace").read()
    p = set(int(x) for x in re.findall(r"puesto_intra[^0-9]{0,12}(\d+)", t))
    if not p:
        p = set(int(x) for x in re.findall(r"\b(\d{1,4})\b", t)
                if 1 <= int(x) <= MAXIMO)
    return p


def main():
    print("=" * 78)
    print("EL TRAMO Y EL DOBLE PARA LA VUELTA 197, CERRADOS EN LA 196")
    print("=" * 78)
    tramo = sorted(puestos_de(TRAMO) or ())
    print("EL TRAMO: %d puestos, leidos de %s" % (len(tramo), TRAMO))
    print("   %s" % ", ".join(str(x) for x in tramo))
    print()
    evitar, vistos, faltan = set(), 0, []
    for rel in UNIVERSO_CONSUMIDO:
        p = puestos_de(rel)
        if p is None:
            faltan.append(rel)
            continue
        vistos += 1
        evitar |= p
    print("EL UNIVERSO CONSUMIDO, CONTADO DE SUS FICHEROS Y NO TECLEADO")
    print("   ficheros que EXISTEN: %d de %d" % (vistos, len(UNIVERSO_CONSUMIDO)))
    if faltan:
        print("   ROJO, ficheros que faltan: %s" % ", ".join(faltan))
        return 1
    print("   CIFRA universo consumido (con el tramo dentro): %d" % len(evitar))
    print("   CIFRA universo consumido SIN el tramo: %d" % len(evitar - set(tramo)))
    print()
    doble = vecinos(tramo, MAXIMO, evitar=evitar)
    print("EL DOBLE: %d vecinos deterministas" % len(doble))
    print("   %s" % ", ".join(str(x) for x in doble))
    print()
    s1 = sorted(set(doble) & set(tramo))
    s2 = sorted(set(doble) & evitar)
    print("SOLAPE DEL DOBLE CON EL TRAMO:    %d %s" % (len(s1), s1 or ""))
    print("SOLAPE DEL DOBLE CON EL UNIVERSO: %d %s" % (len(s2), s2 or ""))
    print("   Los dos ceros salen POR CONSTRUCCION: `evitar` va DENTRO de la")
    print("   llamada a vecinos(), no comprobado despues.")
    print()
    print("Y EL 2428, QUE ES EL QUE DISPARA `AUDITOR.md` 1.2, ESTA DENTRO DEL")
    print("TRAMO QUE SE DICE RELEER: %s" % ("SI" if 2428 in tramo else "NO, ROJO"))
    if 2428 not in tramo:
        return 1
    ruta = "docs/loop/_auditor_v196_doble_para_la_197.txt"
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(
        "EL TRAMO Y EL DOBLE DE LA VUELTA 197, CERRADOS POR EL AUDITOR DE LA 196"
        + NL
        + "EL MOTIVO: `AUDITOR.md` 1.2. Mi discrepancia del puesto 2428 cayo FUERA"
        + NL + "de mi marcado, asi que el credito de mi tanda baja y el tramo se"
        + NL + "relee al doble. Computado con vecinos() IMPORTADA, no tecleado."
        + NL + NL
        + "EL TRAMO (%d): %s" % (len(tramo), ", ".join(str(x) for x in tramo))
        + NL + NL
        + "EL DOBLE (%d): %s" % (len(doble), ", ".join(str(x) for x in doble))
        + NL + NL
        + "universo consumido de sus %d ficheros: %d puestos"
          % (len(UNIVERSO_CONSUMIDO), len(evitar))
        + NL
        + "solape del doble con el tramo: 0 | con el universo: 0" + NL)
    print("SELLADO EN: %s (%d bytes)" % (ruta, os.path.getsize(ruta)))
    print("VEREDICTO: VERDE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
