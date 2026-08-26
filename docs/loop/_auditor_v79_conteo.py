"""Auditor v79 (Opus 5): instrumento propio, escrito en esta vuelta.
Cuenta censo y aristas de master_graph.json en cualquier ref de git, o WORK.
union = |{(a,b) de nodos_siguientes} U {(a,b) de nodos_previos}|
Comprueba la clave contra node_id con assert (leccion del acta 77).
Ademas: conjuntos de aristas para diff por conjuntos, y duplicadas dentro de una lista.
"""
import json, sys, subprocess

def cargar(ref):
    if ref == "WORK":
        with open("dataset/metadata/master_graph.json", encoding="utf-8") as f:
            return json.load(f)
    b = subprocess.run(["git", "show", f"{ref}:dataset/metadata/master_graph.json"],
                       capture_output=True)
    if b.returncode != 0:
        raise SystemExit(f"ROJO: no se pudo leer {ref}: {b.stderr.decode(errors='replace')[:200]}")
    return json.loads(b.stdout.decode("utf-8"))

def medir(ref):
    N = cargar(ref)["nodos"]
    sig = prev = vivos = depre = auto = 0
    S, P = set(), set()
    dup_en_lista = 0
    for nid, n in N.items():
        assert n.get("node_id") == nid, f"clave != node_id: {nid}"
        if n.get("deprecado"):
            depre += 1
        else:
            vivos += 1
        s = n.get("nodos_siguientes") or []
        q = n.get("nodos_previos") or []
        sig += len(s); prev += len(q)
        if len(set(s)) != len(s): dup_en_lista += 1
        if len(set(q)) != len(q): dup_en_lista += 1
        for d in s:
            if d == nid: auto += 1
            S.add((nid, d))
        for d in q:
            if d == nid: auto += 1
            P.add((d, nid))
    return dict(ref=ref, nodos=len(N), vivos=vivos, depre=depre, sig=sig, prev=prev,
                suma=sig+prev, union=len(S | P), auto=auto, S=S, P=P,
                solo_S=len(S - P), solo_P=len(P - S), dup_en_lista=dup_en_lista)

if __name__ == "__main__":
    for ref in sys.argv[1:]:
        r = medir(ref)
        print(f"{r['ref']:>12} | nodos {r['nodos']} vivos {r['vivos']} depre {r['depre']} "
              f"| sig {r['sig']} prev {r['prev']} suma {r['suma']} union {r['union']} "
              f"| solo_sig {r['solo_S']} solo_prev {r['solo_P']} auto {r['auto']} "
              f"| nodos_con_duplicada_en_lista {r['dup_en_lista']}")
