#!/usr/bin/env python3
"""Paso 3: reparar referencias rotas INTRA-dominio (exacto tras ASCII ->
alias -> fuzzy >= 0.90 -> poda con log). Paso 4 (--simetrizar): clausura
bidireccional (si A lista a B como siguiente, B lista a A como previo)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import (CATEGORIAS, a_ascii, cargar_dominio, dir_metadata,
                         escribir_json, guardar_nodo, similitud)

UMBRAL = 0.90


def reparar(cat: str) -> None:
    nodos = cargar_dominio(cat)
    ids = set(nodos)
    alias = {}
    for nid, d in nodos.items():
        for a in d.get("ids_alias") or []:
            alias[a] = nid
    log = {"reparadas": [], "podadas": []}
    for nid, d in nodos.items():
        cambio = False
        for campo in ("nodos_previos", "nodos_siguientes"):
            nueva = []
            for r in d.get(campo) or []:
                if r in ids:
                    dest = r
                else:
                    dest = alias.get(r) or (a_ascii(r) if a_ascii(r) in ids else None)
                    if dest is None:
                        mejor, score = None, 0.0
                        for cand in ids:
                            s = similitud(r, cand)
                            if s > score:
                                mejor, score = cand, s
                        dest = mejor if score >= UMBRAL else None
                    if dest:
                        log["reparadas"].append({"en": nid, "campo": campo, "de": r, "a": dest})
                    else:
                        log["podadas"].append({"en": nid, "campo": campo, "ref": r})
                        cambio = True
                        continue
                if dest != nid and dest not in nueva:
                    nueva.append(dest)
            if nueva != (d.get(campo) or []):
                d[campo] = nueva
                cambio = True
        if cambio:
            guardar_nodo(cat, nid, d)
    escribir_json(dir_metadata(cat) / "aristas_reparadas.json", log)
    print(f"{cat}: {len(log['reparadas'])} reparadas | {len(log['podadas'])} podadas (log en metadata/)")


def simetrizar(cat: str) -> None:
    nodos = cargar_dominio(cat)
    tocados = set()
    for nid, d in nodos.items():
        for sig in list(d.get("nodos_siguientes") or []):
            back = nodos[sig].setdefault("nodos_previos", [])
            if nid not in back:
                back.append(nid)
                tocados.add(sig)
        for prev in list(d.get("nodos_previos") or []):
            fwd = nodos[prev].setdefault("nodos_siguientes", [])
            if nid not in fwd:
                fwd.append(nid)
                tocados.add(prev)
    for nid in tocados:
        guardar_nodo(cat, nid, nodos[nid])
    print(f"{cat}: simetria cerrada ({len(tocados)} nodos completados)")


if __name__ == "__main__":
    for cat in CATEGORIAS:
        if "--simetrizar" in sys.argv:
            simetrizar(cat)
        else:
            reparar(cat)
