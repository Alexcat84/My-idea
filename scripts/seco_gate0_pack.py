# -*- coding: utf-8 -*-
"""El SECO de una integracion con el Gate 0 de grafo completo (leccion del mundo 11, 28 sep 2026).

El seco del importador (`scripts/importar_forja.py`) solo miraba aristas rotas y reciprocas, y `integrar_packs.py
--dry-run` solo mira prerequisitos: ninguno mide el GRAFO. La primera corrida real del mundo 11 se paro en Gate 0 con
259 componentes y hubo que deshacerla. Este script teje EN MEMORIA el pack y sus puentes aprobados sobre el catalogo
de `dataset/nodos` y corre las mismas funciones de `scripts/run_phase1.py` que usa Gate 0:

  * componentes conexos <= 2 y cobertura del componente principal >= 99 por ciento;
  * alcanzabilidad dirigida >= MIN_DIRECTED_REACHABILITY_PCT desde todas las semillas (las del motor, las de los
    packs integrados y las del pack nuevo);

y ademas la vara del mundo: 100 por ciento de sus nodos alcanzables y ninguno aislado. No escribe nada, no llama a
ninguna API y no lee el `.env`.

    python scripts/seco_gate0_pack.py primer_equipo          (sale con 1 si algo falla)
"""
import copy
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import run_phase1 as gate  # noqa: E402


def tejer(catalogo, pack, puentes):
    """El catalogo con los nodos del pack y los puentes aprobados tejidos reciprocos, en copias."""
    nodos = copy.deepcopy(catalogo)
    nodos.update(copy.deepcopy(pack))
    for pz in puentes:
        c, m = pz["core"], pz["dominio"]
        if c in nodos and m in nodos:
            if m not in nodos[c].setdefault("nodos_siguientes", []):
                nodos[c]["nodos_siguientes"].append(m)
            if c not in nodos[m].setdefault("nodos_previos", []):
                nodos[m]["nodos_previos"].append(c)
    return nodos


def medir(nodos, semillas, dominio):
    activos = {i: n for i, n in nodos.items() if not n.get("deprecado")}
    stats = gate.compute_graph_stats(activos)
    alcanzados, total, pct = gate.compute_directed_reachability(activos, semillas)
    vistos, pila = set(), [s for s in semillas if s in activos]
    while pila:
        x = pila.pop()
        if x in vistos:
            continue
        vistos.add(x)
        pila.extend(t for t in activos[x].get("nodos_siguientes") or [] if t in activos)
    mundo = [i for i, n in activos.items() if n.get("dominio") == dominio]
    aislados = sorted(i for i in mundo if not [r for k in gate.REF_KEYS for r in activos[i].get(k) or [] if r in activos])
    return {
        "nodos": len(activos),
        "componentes": stats["componentes_conexos"],
        "cobertura_pct": stats["cobertura_componente_principal_pct"],
        "alcance_pct": pct,
        "mundo_nodos": len(mundo),
        "mundo_alcance_pct": round(sum(1 for i in mundo if i in vistos) / len(mundo) * 100, 2) if mundo else 0.0,
        "mundo_no_alcanzados": sorted(i for i in mundo if i not in vistos),
        "mundo_aislados": aislados,
    }


def leer_carpeta(carpeta):
    return {n["node_id"]: n for n in (json.loads(p.read_text(encoding="utf-8")) for p in sorted(carpeta.glob("*.json")))}


def main():
    dominio = sys.argv[1] if len(sys.argv) > 1 else "primer_equipo"
    raiz = BASE / "packs" / dominio
    catalogo = leer_carpeta(gate.NODOS_DIR)
    pack = leer_carpeta(raiz / "nodos")
    meta = raiz / "metadata"
    puentes = json.loads((meta / "bridges_aprobados.json").read_text(encoding="utf-8")).get("aprobados") or []
    semillas_pack = json.loads((meta / "entry_seeds.json").read_text(encoding="utf-8"))
    semillas = list(gate.load_entry_seeds()) + [s for s in semillas_pack if s in pack]
    r = medir(tejer(catalogo, pack, puentes), semillas, dominio)
    checks = [
        ("Componentes conexos <= 2", r["componentes"] <= 2, r["componentes"]),
        ("Cobertura del componente principal >= 99%", r["cobertura_pct"] >= 99.0, r["cobertura_pct"]),
        ("Alcanzabilidad dirigida >= %s%%" % gate.MIN_DIRECTED_REACHABILITY_PCT,
         r["alcance_pct"] >= gate.MIN_DIRECTED_REACHABILITY_PCT, r["alcance_pct"]),
        ("Mundo %s: 100%% alcanzable desde sus puertas" % dominio, r["mundo_alcance_pct"] == 100.0,
         "%s%% (%d nodos; fuera %s)" % (r["mundo_alcance_pct"], r["mundo_nodos"], r["mundo_no_alcanzados"][:10])),
        ("Mundo %s: ningun nodo aislado" % dominio, not r["mundo_aislados"], r["mundo_aislados"][:10]),
    ]
    print("SECO DEL GATE 0 DE GRAFO, %s tejido en memoria sobre el catalogo (%d nodos activos, %d puentes, %d semillas)"
          % (dominio, r["nodos"], len(puentes), len(semillas)))
    for nombre, ok, valor in checks:
        print("  %s  %s: %s" % ("OK  " if ok else "FALLA", nombre, valor))
    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
