"""Auditor v79: vuelca el texto ENTERO de un nodo desde el grafo. Para la relectura ciega."""
import json, sys
G = json.load(open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
for nid in sys.argv[1:]:
    n = G.get(nid)
    if n is None:
        print(f"### {nid} : NO EXISTE"); continue
    print("=" * 78)
    print(f"### {nid}   [{'DEPRECADO' if n.get('deprecado') else 'vivo'}]  dominio={n.get('dominio')}")
    print(f"TITULO   : {n.get('titulo_concepto')}")
    print(f"ETIQUETA : {n.get('etiqueta_arbol')}")
    print(f"FUENTE   : {n.get('fuente') or n.get('libro') or n.get('procedencia')}")
    print(f"RESUMEN  : {n.get('resumen_teorico') or n.get('resumen')}")
    pasos = n.get("pasos") or n.get("pasos_accionables") or []
    print(f"PASOS ({len(pasos)}):")
    for i, p in enumerate(pasos, 1):
        print(f"   {i}. {p if isinstance(p,str) else json.dumps(p, ensure_ascii=False)}")
    print(f"ENTREGABLE: {n.get('entregable_esperado')}")
    print(f"MADRES ({len(n.get('nodos_previos') or [])}): {n.get('nodos_previos')}")
    print(f"HIJOS  ({len(n.get('nodos_siguientes') or [])}): {n.get('nodos_siguientes')}")
