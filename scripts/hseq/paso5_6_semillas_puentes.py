#!/usr/bin/env python3
"""Paso 5: sugerir 12 semillas de entrada por dominio (decision final humana:
el usuario aprueba 5-8 y se guardan en metadata/entry_seeds.json).
Paso 6 (--puentes): proponer los 20 mejores puentes core<->dominio por
afinidad semantica (sentence-transformers si esta disponible; si no, fuzzy
de titulo+resumen). SOLO propuesta en metadata/bridges_propuestos.json;
ninguna arista se escribe al master graph."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import (CATEGORIAS, RAIZ, cargar_dominio, dir_metadata,
                         escribir_json, norm_titulo, similitud)

FUNDACIONALES = ["principio", "programa", "sistema", "fundament", "introducc",
                 "liderazgo", "mejora_continua", "eco_efect", "peligro", "calidad_"]


def sugerir_semillas(cat: str) -> None:
    nodos = cargar_dominio(cat)
    entrantes = {i: 0 for i in nodos}
    for d in nodos.values():
        for r in d.get("nodos_siguientes") or []:
            if r in entrantes:
                entrantes[r] += 1
    def puntaje(nid):
        d = nodos[nid]
        p = entrantes[nid] * 2 + len(d.get("nodos_siguientes") or [])
        fase = str(d.get("fase_proyecto", "")).lower()
        if any(k in fase for k in ("1", "inicial", "temprana", "descubr")):
            p += 3
        if any(k in nid for k in FUNDACIONALES):
            p += 4
        return p
    top = sorted(nodos, key=puntaje, reverse=True)[:12]
    print(f"\n== {cat}: candidatas a semilla (aprobar 5-8, guardar en metadata/entry_seeds.json) ==")
    for nid in top:
        print(f"  {nid}  <- {nodos[nid].get('titulo','')[:70]}")


def _texto(d: dict) -> str:
    return f"{d.get('titulo','')}. {d.get('resumen_teorico','')[:400]}"


def proponer_puentes(cat: str) -> None:
    dominio = cargar_dominio(cat)
    core = {}
    for f in (RAIZ / "dataset" / "nodos").glob("*.json"):
        core[f.stem] = json.load(open(f, encoding="utf-8"))
    pares = []
    try:
        from sentence_transformers import SentenceTransformer, util  # type: ignore
        m = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
        cids, dids = sorted(core), sorted(dominio)
        ec = m.encode([_texto(core[i]) for i in cids], normalize_embeddings=True, show_progress_bar=False)
        ed = m.encode([_texto(dominio[i]) for i in dids], normalize_embeddings=True, show_progress_bar=False)
        sim = util.cos_sim(ec, ed)
        import torch
        flat = sim.flatten()
        k = min(200, flat.numel())
        vals, idxs = torch.topk(flat, k)
        for v, ix in zip(vals.tolist(), idxs.tolist()):
            pares.append({"core": cids[ix // len(dids)], "dominio": dids[ix % len(dids)],
                          "score": round(v, 4)})
        metodo = "embeddings"
    except ImportError:
        for cid, cd in core.items():
            tc = norm_titulo(cd.get("titulo", cid))
            for did, dd in dominio.items():
                s = similitud(tc, norm_titulo(dd.get("titulo", did)))
                if s >= 0.55:
                    pares.append({"core": cid, "dominio": did, "score": round(s, 4)})
        metodo = "fuzzy (instalar sentence-transformers para mejor senal)"
    # deduplicar dejando el mejor par por nodo de dominio, top 20
    mejores: dict[str, dict] = {}
    for p in sorted(pares, key=lambda x: -x["score"]):
        mejores.setdefault(p["dominio"], p)
    top = sorted(mejores.values(), key=lambda x: -x["score"])[:20]
    escribir_json(dir_metadata(cat) / "bridges_propuestos.json",
                  {"metodo": metodo, "nota": "Seleccion final humana de 10-15; NO escritos al master.",
                   "candidatos": top})
    print(f"{cat}: {len(top)} puentes propuestos ({metodo}) -> metadata/bridges_propuestos.json")


if __name__ == "__main__":
    for cat in CATEGORIAS:
        if "--puentes" in sys.argv:
            proponer_puentes(cat)
        else:
            sugerir_semillas(cat)
