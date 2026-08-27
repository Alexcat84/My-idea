# -*- coding: utf-8 -*-
"""_v87_volcar_tramo12.py . Vuelca las 8 fichas (madre e hijo de cada una de
las 4 unidades frescas de la cola de OP-E-01, TRAMO 12) desde
dataset/nodos/*.json, para leer el texto crudo ANTES de decidir (AUDITOR.md
seccion 1.2, misma disciplina)."""
import io
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
FILTRO = RAIZ / "docs" / "loop" / "SALIDA_V87_TRAMO12_FILTRO_P91_GUARDA_CADENA.txt"
NODOS = RAIZ / "dataset" / "nodos"

RE_UNIDAD = re.compile(r"^\s*(\d+):\s*(.+?)\s*->\s*(.+?)\s*\(paso\s*(.+?),\s*dominio\s*(.+?)\)\s*\|\s*(.+)$")


def leer_frescas():
    texto = io.open(FILTRO, encoding="utf-8").read()
    lineas = texto.splitlines()
    i = 0
    while i < len(lineas) and not lineas[i].startswith("CABEZA DE LA BOLSA FILTRADA"):
        i += 1
    while i < len(lineas) and not RE_UNIDAD.match(lineas[i]):
        i += 1
    unidades = []
    while i < len(lineas) and lineas[i].strip():
        m = RE_UNIDAD.match(lineas[i])
        if m:
            idx, madre, hijo, paso, dominio, resto = m.groups()
            unidades.append({"idx": int(idx), "madre": madre, "hijo": hijo,
                             "paso": paso, "dominio": dominio, "resto": resto})
        i += 1
    return unidades


def cargar_nodo(nid):
    ruta = NODOS / (nid + ".json")
    if not ruta.exists():
        return None
    return json.load(open(ruta, encoding="utf-8"))


def volcar_nodo(n, etiqueta):
    if n is None:
        print("  [%s] NODO NO ENCONTRADO" % etiqueta)
        return
    print("  [%s] %s (dominio %s)" % (etiqueta, n["node_id"], n.get("dominio")))
    print("    TITULO: %s" % n.get("titulo_concepto"))
    print("    RESUMEN: %s" % (n.get("resumen_teorico") or "")[:600])
    print("    PASOS:")
    for i, p in enumerate(n.get("pasos_accionables") or [], 1):
        print("      %d. %s" % (i, p))
    print("    ENTREGABLE: %s" % n.get("entregable_esperado"))
    print("    nodos_siguientes: %s" % (n.get("nodos_siguientes") or []))
    print("    nodos_previos: %s" % (n.get("nodos_previos") or []))


def main():
    unidades = leer_frescas()
    print("UNIDADES FRESCAS VOLCADAS: %d" % len(unidades))
    print()
    for u in unidades:
        print("=" * 90)
        print("UNIDAD %d: %s -> %s (paso %s, dominio %s)" % (u["idx"], u["madre"], u["hijo"], u["paso"], u["dominio"]))
        print("  filtro dice: %s" % u["resto"])
        print("=" * 90)
        volcar_nodo(cargar_nodo(u["madre"]), "MADRE")
        print()
        volcar_nodo(cargar_nodo(u["hijo"]), "HIJO")
        print()


if __name__ == "__main__":
    main()
