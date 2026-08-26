"""VUELTA 76: compara nodos_siguientes/nodos_previos del master_graph.json
en el commit de apertura 62d4f28e contra el estado actual del arbol de
trabajo, tras la reversion de 1.3.a. Cuenta pares nuevos y borrados, y
comprueba simetria (mismo conjunto en ambas listas)."""
import json
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BASE = "62d4f28e"


def cargar_commit(commit, ruta):
    salida = subprocess.run(
        ["git", "show", f"{commit}:{ruta}"], cwd=RAIZ, capture_output=True, check=True
    )
    return json.loads(salida.stdout.decode("utf-8"))


def cargar_actual(ruta):
    with open(RAIZ / ruta, encoding="utf-8") as f:
        return json.load(f)


def aristas(master):
    sig = set()
    prev = set()
    for nid, n in master["nodos"].items():
        for h in n.get("nodos_siguientes") or []:
            sig.add((nid, h))
        for m in n.get("nodos_previos") or []:
            prev.add((m, nid))
    return sig, prev


def main():
    ruta = "dataset/metadata/master_graph.json"
    base = cargar_commit(BASE, ruta)
    actual = cargar_actual(ruta)

    sig_base, prev_base = aristas(base)
    sig_act, prev_act = aristas(actual)

    nuevas_sig = sig_act - sig_base
    borradas_sig = sig_base - sig_act
    nuevas_prev = prev_act - prev_base
    borradas_prev = prev_base - prev_act

    print(f"nodos_siguientes: {len(nuevas_sig)} nuevas, {len(borradas_sig)} borradas")
    print(f"nodos_previos:    {len(nuevas_prev)} nuevas, {len(borradas_prev)} borradas")
    print(f"SIMETRIA (mismo conjunto en ambas vistas): {nuevas_sig == nuevas_prev}")
    print()
    print(f"LAS {len(nuevas_sig)} ARISTAS NUEVAS (madre -> hijo), orden alfabetico:")
    for m, h in sorted(nuevas_sig):
        print(f"  {m} -> {h}")
    if borradas_sig:
        print(f"\nARISTAS BORRADAS ({len(borradas_sig)}):")
        for m, h in sorted(borradas_sig):
            print(f"  {m} -> {h}")


if __name__ == "__main__":
    main()
