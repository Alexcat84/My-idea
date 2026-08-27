"""Auditor v82 (Opus 5): instrumento propio, escrito y corrido en esta vuelta.
Censo y aristas de master_graph.json en cualquier ref de git, o WORK.
union = |{(a,b) de nodos_siguientes} U {(a,b) de nodos_previos}|
assert de la clave contra node_id. Ademas: comprueba una arista concreta
en las DOS vistas (madre.nodos_siguientes y hijo.nodos_previos).
"""
import json, sys, subprocess

def cargar(ref):
    if ref == "WORK":
        with open("dataset/metadata/master_graph.json", encoding="utf-8") as f:
            return json.load(f)
    b = subprocess.run(["git", "show", f"{ref}:dataset/metadata/master_graph.json"],
                       capture_output=True)
    if b.returncode != 0:
        raise SystemExit("ROJO: no se pudo leer " + ref)
    return json.loads(b.stdout.decode("utf-8"))

def medir(ref, par=None):
    N = cargar(ref)["nodos"]
    sig = prev = vivos = depre = auto = 0
    S, P = set(), set()
    dup = 0
    for nid, n in N.items():
        assert n.get("node_id") == nid, "clave != node_id: " + nid
        if n.get("deprecado"): depre += 1
        else: vivos += 1
        s = n.get("nodos_siguientes") or []
        q = n.get("nodos_previos") or []
        sig += len(s); prev += len(q)
        if len(set(s)) != len(s): dup += 1
        if len(set(q)) != len(q): dup += 1
        for d in s:
            if d == nid: auto += 1
            S.add((nid, d))
        for d in q:
            if d == nid: auto += 1
            P.add((d, nid))
    linea = (f"{ref:>12} | nodos {len(N)} vivos {vivos} depre {depre} | sig {sig} prev {prev} "
             f"suma {sig+prev} union {len(S|P)} | solo_sig {len(S-P)} solo_prev {len(P-S)} "
             f"auto {auto} | nodos_con_dup_en_lista {dup}")
    if par:
        a, b2 = par
        en_sig = b2 in (N.get(a, {}).get("nodos_siguientes") or [])
        en_prev = a in (N.get(b2, {}).get("nodos_previos") or [])
        inv1 = a in (N.get(b2, {}).get("nodos_siguientes") or [])
        inv2 = b2 in (N.get(a, {}).get("nodos_previos") or [])
        linea += f"\n{'':>12} | PAR {a} -> {b2}: en_sig_madre {en_sig} en_prev_hijo {en_prev} INVERSAS {inv1}/{inv2}"
    return linea

if __name__ == "__main__":
    par = ("descubrir_necesidades_del_cliente", "traduccion_necesidades_cliente")
    for ref in sys.argv[1:]:
        print(medir(ref, par))
