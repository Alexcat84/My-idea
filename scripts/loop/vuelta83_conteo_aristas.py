"""vuelta83_conteo_aristas.py . Instrumento propio del ejecutor, vuelta 83.

Censo y aristas de dataset/metadata/master_graph.json, en el arbol de trabajo
(WORK) o en cualquier ref de git. Salida en el formato que
scripts/loop/tallar_cabecera_reporte.py --fase04 sabe leer con la expresion
regular "sig (\\d+) prev (\\d+) suma (\\d+) union (\\d+)".

union = |{(a,b) de nodos_siguientes} U {(a,b) de nodos_previos}|
Con --par A B, ademas comprueba una arista concreta en las DOS vistas
(A.nodos_siguientes trae a B, B.nodos_previos trae a A) y sus inversas.

USO:
  python scripts/loop/vuelta83_conteo_aristas.py WORK
  python scripts/loop/vuelta83_conteo_aristas.py WORK --par madre hijo
"""
import argparse
import json
import subprocess
import sys


def cargar(ref):
    if ref == "WORK":
        with open("dataset/metadata/master_graph.json", encoding="utf-8") as f:
            return json.load(f)
    b = subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % ref],
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
        if n.get("deprecado"):
            depre += 1
        else:
            vivos += 1
        s = n.get("nodos_siguientes") or []
        q = n.get("nodos_previos") or []
        sig += len(s)
        prev += len(q)
        if len(set(s)) != len(s):
            dup += 1
        if len(set(q)) != len(q):
            dup += 1
        for d in s:
            if d == nid:
                auto += 1
            S.add((nid, d))
        for d in q:
            if d == nid:
                auto += 1
            P.add((d, nid))
    linea = ("%12s | nodos %d vivos %d depre %d | sig %d prev %d suma %d union %d | "
             "solo_sig %d solo_prev %d auto %d | nodos_con_dup_en_lista %d"
             % (ref, len(N), vivos, depre, sig, prev, sig + prev, len(S | P),
                len(S - P), len(P - S), auto, dup))
    if par:
        a, b2 = par
        en_sig = b2 in (N.get(a, {}).get("nodos_siguientes") or [])
        en_prev = a in (N.get(b2, {}).get("nodos_previos") or [])
        inv1 = a in (N.get(b2, {}).get("nodos_siguientes") or [])
        inv2 = b2 in (N.get(a, {}).get("nodos_previos") or [])
        linea += ("\n%12s | PAR %s -> %s: en_sig_madre %s en_prev_hijo %s INVERSAS %s/%s"
                  % ("", a, b2, en_sig, en_prev, inv1, inv2))
    return linea


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("refs", nargs="+", help="WORK o un commit de git")
    ap.add_argument("--par", nargs=2, metavar=("MADRE", "HIJO"), default=None)
    a = ap.parse_args()
    for ref in a.refs:
        print(medir(ref, tuple(a.par) if a.par else None))


if __name__ == "__main__":
    main()
