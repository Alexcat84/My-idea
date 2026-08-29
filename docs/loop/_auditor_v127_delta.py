import json, os, subprocess, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def conj(nodos):
    alias = {}
    for nid, n in nodos.items():
        if n.get("deprecado"): continue
        for x in (n.get("ids_alias") or []): alias[x] = nid
    def res(x):
        v=set()
        while x in alias and x not in v: v.add(x); x=alias[x]
        return x
    def vivo(i):
        n=nodos.get(i); return n is not None and not n.get("deprecado")
    def pres(o,d):
        return d in (nodos[o].get("nodos_siguientes") or []) or o in (nodos[d].get("nodos_previos") or [])
    s=set(); crudo=set()
    for muere,n in nodos.items():
        if not n.get("deprecado"): continue
        sup=res(muere)
        if sup==muere or not vivo(sup): continue
        for campo,dr in (("nodos_siguientes","sig"),("nodos_previos","prev")):
            for x in (n.get(campo) or []):
                otro=res(x)
                if otro==sup or not vivo(otro): continue
                o,d=(sup,otro) if dr=="sig" else (otro,sup)
                if pres(o,d): continue
                s.add((o,d))
                nx=nodos.get(x)
                if nx is not None and nx.get("deprecado"):
                    crudo.add((muere,x) if dr=="sig" else (x,muere))
    return s, crudo
work=json.load(open(os.path.join(RAIZ,"dataset","metadata","master_graph.json"),encoding="utf-8"))["nodos"]
r=subprocess.run(["git","show","7150339f:dataset/metadata/master_graph.json"],cwd=RAIZ,capture_output=True)
prev=json.loads(r.stdout.decode("utf-8"))["nodos"]
sw,cw=conj(work); sp,cp=conj(prev)
print("resueltas: antes %d, hoy %d, DESAPARECIDAS: %r, APARECIDAS: %r" % (len(sp),len(sw),sorted(sp-sw),sorted(sw-sp)))
print("crudas ambos muertos: antes %d, hoy %d, DESAPARECIDAS: %r" % (len(cp),len(cw),sorted(cp-cw)))
