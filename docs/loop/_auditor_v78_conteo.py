"""Auditor v78: instrumento propio. Cuenta nodos y aristas de master_graph.json
en cualquier ref de git (o WORK = arbol de trabajo).
union dirigida unica = |{(madre,hijo) de nodos_siguientes} U {(madre,hijo) de nodos_previos}|
Comprueba la clave del fichero (node_id) con assert, leccion del acta 77 seccion 6.2.
"""
import json, sys, subprocess

def cargar(ref):
    if ref == "WORK":
        return json.load(open("dataset/metadata/master_graph.json", encoding="utf-8"))
    b = subprocess.run(["git", "show", f"{ref}:dataset/metadata/master_graph.json"],
                       capture_output=True)
    return json.loads(b.stdout.decode("utf-8"))

def medir(ref):
    N = cargar(ref)["nodos"]
    sig = prev = vivos = depre = auto = 0
    ps, pp = set(), set()
    for nid, n in N.items():
        assert n.get("node_id") == nid, f"clave distinta de node_id: {nid}"
        if n.get("deprecado"):
            depre += 1
        else:
            vivos += 1
        s = n.get("nodos_siguientes") or []
        q = n.get("nodos_previos") or []
        sig += len(s); prev += len(q)
        for d in s:
            if d == nid: auto += 1
            ps.add((nid, d))
        for d in q:
            if d == nid: auto += 1
            pp.add((d, nid))
    return dict(ref=ref, total=len(N), vivos=vivos, depre=depre, siguientes=sig,
                previos=prev, suma=sig + prev, union=len(ps | pp), auto=auto,
                solo_sig=len(ps - pp), solo_prev=len(pp - ps), ps=ps, pp=pp)

if __name__ == "__main__":
    for ref in sys.argv[1:]:
        r = medir(ref)
        print(f"{r['ref']:>12}  nodos {r['total']} vivos {r['vivos']} depre {r['depre']} | "
              f"sig {r['siguientes']} prev {r['previos']} suma {r['suma']} union {r['union']} "
              f"| solo_sig {r['solo_sig']} solo_prev {r['solo_prev']} auto {r['auto']}")
