#!/usr/bin/env python3
"""Gate 0 por dominio (equivalente a run_phase1.py del core). Exit code 0
solo si TODO pasa: 0 referencias rotas, simetria 100%, titulos unicos,
ids ASCII, dominio estampado correcto, alcanzabilidad dirigida >= 99.5%
desde metadata/entry_seeds.json. Uso:
    python scripts/hseq/run_phase1_dominio.py            # los tres dominios
    python scripts/hseq/run_phase1_dominio.py Quality    # uno solo
"""
import json
import sys
from collections import deque
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import CATEGORIAS, cargar_dominio, dir_metadata

UMBRAL_ALCANCE = 0.995


def validar(cat: str, clave: str) -> bool:
    nodos = cargar_dominio(cat)
    ids = set(nodos)
    errores = []
    rotas = sum(1 for d in nodos.values()
                for campo in ("nodos_previos", "nodos_siguientes")
                for r in (d.get(campo) or []) if r not in ids)
    if rotas:
        errores.append(f"{rotas} referencias rotas")
    asim = 0
    for nid, d in nodos.items():
        for s in d.get("nodos_siguientes") or []:
            if nid not in (nodos[s].get("nodos_previos") or []):
                asim += 1
        for p in d.get("nodos_previos") or []:
            if nid not in (nodos[p].get("nodos_siguientes") or []):
                asim += 1
    if asim:
        errores.append(f"{asim} aristas asimetricas")
    no_ascii = [i for i in ids if not i.isascii()]
    if no_ascii:
        errores.append(f"{len(no_ascii)} ids no-ASCII (ej {no_ascii[:2]})")
    mal_dom = [i for i, d in nodos.items() if d.get("dominio") != clave]
    if mal_dom:
        errores.append(f"{len(mal_dom)} nodos con dominio != '{clave}' (ej {mal_dom[:2]})")
    titulos = {}
    for i, d in nodos.items():
        titulos.setdefault((d.get("titulo_concepto") or "").strip().lower(), []).append(i)
    dups = {t: v for t, v in titulos.items() if len(v) > 1 and t}
    if dups:
        errores.append(f"{len(dups)} titulos duplicados (ej {list(dups.values())[0]})")
    seeds_path = dir_metadata(cat) / "entry_seeds.json"
    if not seeds_path.exists():
        errores.append("falta metadata/entry_seeds.json (semillas aprobadas)")
    else:
        seeds = [s for s in json.load(open(seeds_path, encoding="utf-8")) if s in ids]
        vistos, cola = set(seeds), deque(seeds)
        while cola:
            n = cola.popleft()
            for s in nodos[n].get("nodos_siguientes") or []:
                if s not in vistos:
                    vistos.add(s)
                    cola.append(s)
        alcance = len(vistos) / len(ids) if ids else 0
        if alcance < UMBRAL_ALCANCE:
            faltan = sorted(ids - vistos)[:5]
            errores.append(f"alcanzabilidad {alcance:.1%} < {UMBRAL_ALCANCE:.1%} (fuera: {faltan}...)")
    estado = "VERDE" if not errores else "ROJO"
    print(f"\n[{estado}] {cat}: {len(nodos)} nodos")
    for e in errores:
        print(f"    - {e}")
    return not errores


if __name__ == "__main__":
    solo = sys.argv[1] if len(sys.argv) > 1 else None
    ok = True
    for cat, clave in CATEGORIAS.items():
        if solo and cat != solo:
            continue
        ok = validar(cat, clave) and ok
    print("\nGATE 0 HSEQ:", "VERDE (los dominios validados pasan)" if ok else "ROJO")
    sys.exit(0 if ok else 1)
