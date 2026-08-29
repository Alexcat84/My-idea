# -*- coding: utf-8 -*-
"""vuelta130_tabla_mapeo_propuesto.py . TAREA 3.b(iv) de la vuelta 130:
genera docs/plan/OP_S_11_MAPEO_PROPUESTO.md (fichero NUEVO, aditivo puro)
desde el censo y los grupos mecanicos de esta misma vuelta (no se teclea:
se corre e imprime, EJECUTOR.md "la tabla se imprime, no se teclea").

Uso:
  python scripts/loop/vuelta130_tabla_mapeo_propuesto.py
"""
import glob
import json
import os
import re
import sys
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "plan", "OP_S_11_MAPEO_PROPUESTO.md")


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


def agrupar(censo):
    grafias = sorted(censo.keys())
    usadas = set()
    grupos_prefijo = []
    for a in grafias:
        if a in usadas:
            continue
        miembros = [a]
        for b in grafias:
            if b == a or b in usadas:
                continue
            if b.startswith(a) or a.startswith(b):
                miembros.append(b)
        if len(miembros) > 1:
            for m in miembros:
                usadas.add(m)
            canonica = max(miembros, key=len)
            grupos_prefijo.append((canonica, miembros, "MECANICO: prefijo estricto (truncamiento)"))

    restantes = [g for g in grafias if g not in usadas]
    norm_a_grafias = {}
    for g in restantes:
        norm_a_grafias.setdefault(normalizar(g), []).append(g)
    grupos_norm = []
    sin_agrupar = []
    for norm, miembros in norm_a_grafias.items():
        if len(miembros) > 1:
            canonica = max(miembros, key=len)
            grupos_norm.append((canonica, miembros, "MECANICO: espacios/mayusculas/puntuacion final"))
            for m in miembros:
                usadas.add(m)
        else:
            sin_agrupar.append(miembros[0])

    return grupos_prefijo + grupos_norm, sin_agrupar


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    censo = cargar_censo()
    grupos, sin_agrupar = agrupar(censo)

    filas = []
    for canonica, miembros, motivo in grupos:
        for m in sorted(miembros, key=len):
            filas.append((m, canonica, motivo))
    for g in sorted(sin_agrupar):
        filas.append((g, g, "SIN AGRUPAR (pide decision)"))
    filas.sort(key=lambda f: f[0].lower())

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("# OP-S-11: tabla de mapeo PROPUESTA del campo `fuente`\n\n")
        fh.write("**PROPUESTA MEDIDA, escrita en la vuelta 130 (TAREA 3.b). NO se ha "
                 "aplicado a ningun nodo: OP-S-11 sigue LISTA, sin tocar, y esta tabla "
                 "no cambia su estado. La adjudica el auditor.**\n\n")
        fh.write("Separador elegido para identificar declaraciones dentro de `fuente`: "
                 "**` | ` (pipe) unicamente**, medido y argumentado en "
                 "`scripts/loop/vuelta130_censo_fuente.py` "
                 "(`docs/loop/SALIDA_V130_3B_CENSO_FUENTE.txt`). El `;` NO se usa como "
                 "separador de declaraciones: en los 264 nodos vivos que lo traen, junta "
                 "coautores del mismo libro, listas de capitulos del mismo libro, o (en "
                 "un punado de casos del dominio `risk_management`) dos citas academicas "
                 "pegadas sin ambiguedad de autoria; partir por `;` fabricaria grafias que "
                 "son apellidos sueltos o fragmentos de titulo, no declaraciones nuevas. "
                 "Corte del catalogo: 2026-08-29, 3.184 nodos vivos con `fuente`, "
                 "129 grafias distintas en primera posicion con este separador.\n\n")
        fh.write("| grafia | canonica propuesta | motivo |\n")
        fh.write("|---|---|---|\n")
        for g, canonica, motivo in filas:
            fh.write("| %s | %s | %s |\n" % (
                g.replace("|", "\\|"), canonica.replace("|", "\\|"), motivo))
        fh.write("\nTOTAL filas: %d (%d grafias en grupos mecanicos, %d sin agrupar), "
                  "contra %d grafias del censo.\n" % (
                      len(filas),
                      sum(len(m) for _, m, _ in grupos),
                      len(sin_agrupar),
                      len(censo),
                  ))

    print("escrito: %s, %d filas" % (SALIDA, len(filas)))


if __name__ == "__main__":
    raise SystemExit(main())
