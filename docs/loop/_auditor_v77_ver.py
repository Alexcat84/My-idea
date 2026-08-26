import json,sys
G=json.load(open("dataset/metadata/master_graph.json",encoding="utf-8"))["nodos"]
for nid in sys.argv[1:]:
    n=G.get(nid)
    if not n: print(f"### {nid}: NO EXISTE\n"); continue
    print(f"### {nid}  [{n.get('dominio')}] deprecado={n.get('deprecado')}")
    print(f"TITULO: {n.get('titulo_concepto')}")
    print(f"FUENTE: {n.get('fuente')}")
    print(f"RESUMEN: {n.get('resumen_teorico')}")
    print("PASOS:")
    for i,p in enumerate(n.get("pasos_accionables") or [],1):
        print(f"  {i}. {p if isinstance(p,str) else json.dumps(p,ensure_ascii=False)}")
    print(f"ENTREGABLE: {n.get('entregable_esperado')}")
    print(f"SIGUIENTES: {n.get('nodos_siguientes')}")
    print(f"PREVIOS: {n.get('nodos_previos')}")
    print()
