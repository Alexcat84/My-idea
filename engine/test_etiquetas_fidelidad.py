# -*- coding: utf-8 -*-
"""Las correcciones de FIDELIDAD de la etiqueta de cara (decision del fundador, 25 sep 2026).

dataset/metadata/etiquetas_de_cara_v1_fidelidad.json corrige etiquetas que decian lo
CONTRARIO o algo DISTINTO del concepto de su nodo. Esta guardia exige:
  1. que la lista sea la ULTIMA de scripts/etiquetas_de_cara.py (manda sobre las demas),
  2. que cada entrada tenga su motivo escrito en `_motivos`, y ningun motivo sobre,
  3. que cada etiqueta este aplicada en las DOS copias del grafo,
  4. que ninguna etiqueta corregida repita la de otro nodo vivo.

    python engine/test_etiquetas_fidelidad.py
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

from etiquetas_de_cara import GRAFOS, LISTAS  # noqa: E402

LISTA = BASE / "dataset" / "metadata" / "etiquetas_de_cara_v1_fidelidad.json"


def cargar(ruta):
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)


def main():
    fallos = []
    if not LISTAS or LISTAS[-1] != LISTA:
        fallos.append("la lista de fidelidad no es la ultima de LISTAS")
    datos = cargar(LISTA)
    motivos = datos.get("_motivos", {})
    lista = {k: v for k, v in datos.items() if not k.startswith("_")}
    if not lista:
        fallos.append("la lista de fidelidad esta vacia")
    for k in lista:
        if not str(motivos.get(k, "")).strip():
            fallos.append("sin motivo: %s" % k)
    for k in motivos:
        if k not in lista:
            fallos.append("motivo sin etiqueta: %s" % k)
    for ruta in GRAFOS:
        nodos = cargar(ruta)["nodos"]
        for k, etiqueta in lista.items():
            nodo = nodos.get(k)
            if nodo is None:
                fallos.append("%s: no existe %s" % (ruta.name, k))
            elif nodo.get("etiqueta_arbol") != etiqueta:
                fallos.append("%s: %s dice %r y la lista %r" % (ruta.parent.name, k, nodo.get("etiqueta_arbol"), etiqueta))
    nodos = cargar(GRAFOS[0])["nodos"]
    for k, etiqueta in lista.items():
        otros = [o for o, n in nodos.items() if o != k and not n.get("deprecado")
                 and str(n.get("etiqueta_arbol", "")).lower() == etiqueta.lower()]
        if otros:
            fallos.append("%s repite la etiqueta de %s" % (k, ", ".join(otros)))
    if fallos:
        print("ROJO: %d fallos" % len(fallos))
        for f in fallos:
            print("  " + f)
        return 1
    print("VERDE: %d etiquetas de fidelidad, con motivo y aplicadas en las dos copias del grafo" % len(lista))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
