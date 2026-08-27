"""Auditor v80: vuelca los textos completos de un nodo, para la relectura ciega."""
import json, sys, textwrap
G = json.load(open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
for nid in sys.argv[1:]:
    n = G.get(nid)
    if n is None:
        print(f"### {nid}: NO EXISTE"); continue
    print("="*78)
    print(f"### {nid}   [deprecado={bool(n.get('deprecado'))}] dominio={n.get('dominio')}")
    print(f"TITULO: {n.get('titulo_concepto')}")
    print(f"FUENTE: {n.get('fuente') or n.get('libro') or '(sin campo fuente)'}")
    for campo in ("resumen_teorico","resumen","descripcion"):
        if n.get(campo):
            print(f"\n{campo.upper()}:"); print(textwrap.fill(str(n[campo]), 76)); break
    pasos = n.get("pasos_accionables") or n.get("pasos") or []
    print(f"\nPASOS ({len(pasos)}):")
    for i,p in enumerate(pasos,1):
        t = p if isinstance(p,str) else (p.get("texto") or p.get("paso") or json.dumps(p,ensure_ascii=False))
        print(textwrap.fill(f"  {i}. {t}", 76, subsequent_indent="     "))
    ent = n.get("entregable_esperado") or n.get("entregable")
    print(f"\nENTREGABLE: {textwrap.fill(str(ent),76,subsequent_indent='  ') if ent else '(ninguno)'}")
    print(f"\nnodos_siguientes ({len(n.get('nodos_siguientes') or [])}): {n.get('nodos_siguientes')}")
    print(f"nodos_previos ({len(n.get('nodos_previos') or [])}): {n.get('nodos_previos')}")
