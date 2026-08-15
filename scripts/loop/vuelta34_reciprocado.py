# -*- coding: utf-8 -*-
"""vuelta34_reciprocado.py - LA MEDICION del cableado del deprecado, ANTES de tocar codigo.

ESTRICTAMENTE DE SOLO LECTURA. No escribe ni un nodo. Mide sobre dataset/nodos,
que es la fuente, no sobre el grafo compilado.

POR QUE EXISTE. La decision del fundador del 15 ago 2026 (opcion a de la parada
docs/loop/paradas/2026-08-15-cableado-deprecado-y-costuras.md) manda quitar en la
simetrizacion de fase 0 el RECIPROCADO DE ARISTAS QUE NACEN EN NODOS DEPRECADOS.
Antes de cambiar una linea del instrumento sellado hay que saber A CUANTO ALCANZA
el cambio, y eso se mide, no se supone (EJECUTOR.md regla 2).

QUE CUENTA, con la definicion escrita para que se pueda discutir:

  ARISTA NACIDA EN UN DEPRECADO = la arista cuya UNICA declaracion vive en las
  listas de un nodo deprecado. Si un nodo VIVO tambien la declara (en cualquiera
  de los dos sentidos), la arista NO nace en el deprecado: nace en el vivo, y el
  cambio no la toca.

  La lectura por DECLARACION, y no por origen topologico, es la que resuelve el
  problema que la decision nombra: si se leyera por origen (el extremo 'antes'),
  una arista declarada por un vivo hacia un deprecado seguiria escribiendo el id
  del deprecado dentro del vivo, que es exactamente el sintoma de la caida 6.1
  de la vuelta 33.

Uso: python scripts/loop/vuelta34_reciprocado.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")


def cargar():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
            fuera[d["node_id"]] = d
    return fuera


def aristas_por_declarante(G):
    """(a, b) -> conjunto de nodos que la declaran, en cualquiera de los dos campos."""
    fuera = {}
    for nid, d in G.items():
        for otro in (d.get("nodos_siguientes") or []):
            if otro in G and otro != nid:
                fuera.setdefault((nid, otro), set()).add(nid)
        for otro in (d.get("nodos_previos") or []):
            if otro in G and otro != nid:
                fuera.setdefault((otro, nid), set()).add(nid)
    return fuera


def main():
    G = cargar()
    dep = {k for k, v in G.items() if v.get("deprecado")}
    print("GRAFO LEIDO DE dataset/nodos: %d nodos, %d vivos, %d deprecados"
          % (len(G), len(G) - len(dep), len(dep)))
    print("=" * 78)

    decl = aristas_por_declarante(G)
    solo_dep = {ar: quien for ar, quien in decl.items() if quien <= dep}
    print("\n--- CENSO DE ARISTAS ---")
    print("  aristas distintas (union de las dos vistas): %d" % len(decl))
    print("  aristas cuya UNICA declaracion vive en un deprecado: %d" % len(solo_dep))
    tocan_vivo = {ar for ar in solo_dep if not ({ar[0], ar[1]} <= dep)}
    print("  ... de esas, las que tocan a un VIVO en el otro extremo: %d" % len(tocan_vivo))
    print("  ... y las que son de deprecado a deprecado: %d" % (len(solo_dep) - len(tocan_vivo)))

    print("\n  LAS QUE TOCAN A UN VIVO, una por linea (son las que el cambio deja")
    print("  de escribir dentro de un nodo vivo):")
    for a, b in sorted(tocan_vivo):
        quien = "el deprecado %s" % sorted(solo_dep[(a, b)])[0]
        lado = "%s (dep=%s) -> %s (dep=%s)" % (a, a in dep, b, b in dep)
        print("    %-72s declarada por %s" % (lado, quien))

    print("\n--- LOS CUATRO NODOS DE LA CAIDA 6.1 DE LA VUELTA 33 ---")
    for nid in ("enfoque_mercado_voc", "homework_frontend_loading",
                "procesamiento_paralelo_con_espirales", "ventaja_competitiva_producto"):
        d = G.get(nid)
        if d is None:
            print("  %s AUSENTE" % nid)
            continue
        print("  %s  (deprecado=%s)" % (nid, bool(d.get("deprecado"))))
        for campo in CAMPOS:
            print("     %-18s %s" % (campo, d.get(campo) or []))

    print("\n--- QUE PASA HOY CON enfoque_mercado_voc ---")
    vivos_que_lo_nombran = sorted(
        nid for nid, d in G.items()
        if not d.get("deprecado") and nid != "enfoque_mercado_voc"
        and any("enfoque_mercado_voc" in (d.get(c) or []) for c in CAMPOS))
    muertos_que_lo_nombran = sorted(
        nid for nid, d in G.items()
        if d.get("deprecado") and nid != "enfoque_mercado_voc"
        and any("enfoque_mercado_voc" in (d.get(c) or []) for c in CAMPOS))
    print("  nodos VIVOS que lo nombran   : %d %s" % (len(vivos_que_lo_nombran), vivos_que_lo_nombran))
    print("  nodos MUERTOS que lo nombran : %d %s" % (len(muertos_que_lo_nombran), muertos_que_lo_nombran))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
