# -*- coding: utf-8 -*-
"""Re-embebe con Voyage SOLO los nodos que la auditoria final corrigio (docs/ACTA_SANEAMIENTO_FINAL.md, seccion 5) y
comprueba despues que el indice sigue coherente. Reutiliza texto_nodo y embeber_textos de
scripts/build_semantic_index_voyage.py: una sola version del texto que se embebe y de la llamada.

Coherencia que se comprueba (y si algo falla, no se escribe nada):
  - todo nodo vivo del grafo tiene vector, y ningun id del indice queda duplicado;
  - todos los vectores tienen la dimension del indice;
  - los vectores nuevos son los de los nodos pedidos (y solo esos cambian);
  - el vector nuevo de cada nodo queda mas cerca de su vector viejo que de cualquier otro (sigue tratando de lo mismo).

    python scripts/auditoria_final/reembeber.py <tanda.json> [<tanda.json> ...]          # dice que haria
    python scripts/auditoria_final/reembeber.py <tanda.json> [...] --yes                 # llama a Voyage y escribe
"""
import json
import math
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
import build_semantic_index_voyage as bsi  # noqa: E402

INDICE = os.path.join(RAIZ, "web", "lib", "assets", "semantic_index.json")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")


def ids_de_tandas(rutas):
    ids = []
    for r in rutas:
        for e in json.load(open(r, encoding="utf-8")):
            for k in ("node_id", "desde", "hacia"):
                if e.get(k) and e.get("veredicto", e.get("operacion")) not in ("QUITAR", "TEJER", "RECABLEAR"):
                    ids.append(e[k])
    return sorted(set(ids))


def _cos(a, b):
    da = math.sqrt(sum(x * x for x in a)); db = math.sqrt(sum(x * x for x in b))
    return sum(x * y for x, y in zip(a, b)) / (da * db) if da and db else 0.0


def reembeber(ids, grafo, indice, embeber):
    """Devuelve (indice_nuevo, informe). `embeber(textos) -> vectores` se inyecta: en la prueba es un falso."""
    vivos = [k for k, n in grafo.items() if not n.get("deprecado")]
    pedidos = [i for i in ids if i in grafo and not grafo[i].get("deprecado")]
    vectores = embeber([bsi.texto_nodo(grafo[i]) for i in pedidos])
    pos = {k: j for j, k in enumerate(indice["ids"])}
    nuevos_ids = list(indice["ids"])
    nuevos_emb = [list(v) for v in indice["embeddings"]]
    for i, v in zip(pedidos, vectores):
        if i in pos:
            nuevos_emb[pos[i]] = list(v)
        else:
            nuevos_ids.append(i)
            nuevos_emb.append(list(v))
    nuevo = {**indice, "ids": nuevos_ids, "embeddings": nuevos_emb}
    fallos = []
    if len(set(nuevos_ids)) != len(nuevos_ids):
        fallos.append("ids duplicados en el indice")
    faltan = sorted(set(vivos) - set(nuevos_ids))
    if faltan:
        fallos.append("nodos vivos sin vector: %s" % faltan[:5])
    dim = indice["dimension"]
    if any(len(v) != dim for v in nuevos_emb):
        fallos.append("vectores con otra dimension que %d" % dim)
    cambiados = [k for k, v_old, v_new in zip(indice["ids"], indice["embeddings"], nuevos_emb) if list(v_old) != v_new]
    ajenos = sorted(set(cambiados) - set(pedidos))
    if ajenos:
        fallos.append("cambiaron vectores que no se pidieron: %s" % ajenos[:5])
    # Una correccion de voz no cambia de que trata el nodo: su vector nuevo tiene que quedar mas cerca de SU vector
    # viejo que de cualquier otro del indice viejo.
    no_propios = []
    for i, v in zip(pedidos, vectores):
        if i not in pos:
            continue
        mejor = max(range(len(indice["ids"])), key=lambda j: _cos(v, indice["embeddings"][j]))
        if indice["ids"][mejor] != i:
            no_propios.append(i)
    if no_propios:
        fallos.append("nodos cuyo vector nuevo no queda junto al suyo viejo: %s" % no_propios[:5])
    return nuevo, {"pedidos": len(pedidos), "cambiados": len(cambiados), "fallos": fallos}


def main():
    rutas = [a for a in sys.argv[1:] if not a.startswith("--")]
    grafo = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
    indice = json.load(open(INDICE, encoding="utf-8"))
    ids = ids_de_tandas(rutas)
    print("nodos a re-embeber: %d" % len(ids))
    if "--yes" not in sys.argv:
        print("No se llamo a Voyage. Para hacerlo: --yes (necesita VOYAGE_API_KEY en el .env raiz).")
        return
    motivo = bsi.credencial_ausente()
    if motivo:
        print("NO:", motivo)
        sys.exit(1)

    def embeber(textos):
        vectores = []
        for k in range(0, len(textos), bsi.BATCH_SIZE):
            v, _ = bsi.embeber_textos(textos[k:k + bsi.BATCH_SIZE], "document")
            vectores += v
        return vectores

    nuevo, informe = reembeber(ids, grafo, indice, embeber)
    print(json.dumps(informe, ensure_ascii=False))
    if informe["fallos"]:
        print("NO SE ESCRIBE: el indice no quedaria coherente.")
        sys.exit(1)
    json.dump(nuevo, open(INDICE, "w", encoding="utf-8"))
    print("escrito:", INDICE, "- despues: python scripts/sync_assets_web.py")


if __name__ == "__main__":
    main()
