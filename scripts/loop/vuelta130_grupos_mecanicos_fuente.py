# -*- coding: utf-8 -*-
"""vuelta130_grupos_mecanicos_fuente.py . TAREA 3.b(ii) y (iii) de la vuelta
130: sobre el censo de vuelta130_censo_fuente.py (separador `|` unicamente,
129 grafias distintas en primera posicion), agrupa MECANICAMENTE lo que se
puede agrupar sin decidir nada:

  (1) GRAFIAS TRUNCADAS: una grafia es prefijo estricto de otra (la mas
      larga es la candidata a canonica).
  (2) GRAFIAS QUE SOLO DIFIEREN en espacios, mayusculas o puntuacion final
      (comparadas por una forma normalizada: minusculas, espacios
      colapsados, puntuacion final quitada).

Lo que NO cae en ninguno de los dos grupos se lista APARTE, sin tocar
(SALIDA_V130_3B_SIN_AGRUPAR.txt): pide decision, y la decision es del
auditor.

AVISO MEDIDO (encargo de la vuelta 130, contraste del auditor con separador
`;` solo): con ese separador el prefijo estricto daba 32 pares y varios NO
eran la misma obra, sino una obra y una cadena de dos obras unidas por `|`.
Con el separador de esta vuelta (`|` unicamente, sin partir por `;`) esa
contaminacion no puede ocurrir: ninguna grafia en primera posicion aqui es
una cadena de dos libros, asi que un prefijo estricto entre dos elementos de
ESTE censo si es candidato solido a truncamiento de la MISMA obra.

Salidas:
  docs/loop/SALIDA_V130_3B_GRUPOS_MECANICOS.txt
  docs/loop/SALIDA_V130_3B_SIN_AGRUPAR.txt

Uso:
  python scripts/loop/vuelta130_grupos_mecanicos_fuente.py
"""
import glob
import json
import os
import re
import sys
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def cargar_censo():
    censo = Counter()
    for p in sorted(glob.glob(os.path.join(NODOS, "*.json"))):
        d = json.loads(open(p, encoding="utf-8").read())
        if d.get("deprecado"):
            continue
        fu = d.get("fuente")
        if not fu:
            continue
        primera = fu.split("|")[0].strip()
        censo[primera] += 1
    return censo


def normalizar(g):
    g2 = g.lower().strip()
    g2 = re.sub(r"\s+", " ", g2)
    g2 = re.sub(r"[.,;:]+$", "", g2).strip()
    return g2


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    censo = cargar_censo()
    grafias = sorted(censo.keys())

    usadas = set()
    grupos_prefijo = []
    for i, a in enumerate(grafias):
        if a in usadas:
            continue
        miembros = [a]
        for b in grafias:
            if b == a or b in usadas:
                continue
            if a != b and (b.startswith(a) or a.startswith(b)):
                if b not in miembros:
                    miembros.append(b)
        if len(miembros) > 1:
            for m in miembros:
                usadas.add(m)
            canonica = max(miembros, key=len)
            grupos_prefijo.append((canonica, miembros))

    restantes = [g for g in grafias if g not in usadas]
    norm_a_grafias = {}
    for g in restantes:
        norm_a_grafias.setdefault(normalizar(g), []).append(g)

    grupos_normalizacion = []
    sin_agrupar = []
    for norm, miembros in norm_a_grafias.items():
        if len(miembros) > 1:
            canonica = max(miembros, key=len)
            grupos_normalizacion.append((canonica, miembros))
            for m in miembros:
                usadas.add(m)
        else:
            sin_agrupar.append(miembros[0])

    with open(os.path.join(RAIZ, "docs", "loop", "SALIDA_V130_3B_GRUPOS_MECANICOS.txt"), "w", encoding="utf-8") as fh:
        fh.write("GRUPOS POR PREFIJO ESTRICTO (candidata canonica = la mas larga):\n")
        for canonica, miembros in grupos_prefijo:
            fh.write("  CANONICA: %s\n" % canonica)
            for m in sorted(miembros, key=len):
                fh.write("    %d\t%s\n" % (censo[m], m))
        fh.write("\nTOTAL grupos por prefijo: %d\n" % len(grupos_prefijo))
        fh.write("\nGRUPOS POR NORMALIZACION (espacios/mayusculas/puntuacion final):\n")
        for canonica, miembros in grupos_normalizacion:
            fh.write("  CANONICA: %s\n" % canonica)
            for m in sorted(miembros, key=len):
                fh.write("    %d\t%s\n" % (censo[m], m))
        fh.write("\nTOTAL grupos por normalizacion: %d\n" % len(grupos_normalizacion))

    with open(os.path.join(RAIZ, "docs", "loop", "SALIDA_V130_3B_SIN_AGRUPAR.txt"), "w", encoding="utf-8") as fh:
        for g in sorted(sin_agrupar):
            fh.write("%d\t%s\n" % (censo[g], g))

    print("grafias totales: %d" % len(grafias))
    print("grupos por prefijo: %d" % len(grupos_prefijo))
    print("grupos por normalizacion: %d" % len(grupos_normalizacion))
    print("sin agrupar: %d" % len(sin_agrupar))
    print("suma de verificacion: %d (prefijo, miembros) + %d (norm, miembros) + %d (sin agrupar) = %d, contra %d grafias" % (
        sum(len(m) for _, m in grupos_prefijo),
        sum(len(m) for _, m in grupos_normalizacion),
        len(sin_agrupar),
        sum(len(m) for _, m in grupos_prefijo) + sum(len(m) for _, m in grupos_normalizacion) + len(sin_agrupar),
        len(grafias),
    ))


if __name__ == "__main__":
    raise SystemExit(main())
