#!/usr/bin/env python3
"""
phase1_6_merge.py - Fase 1.6: fusion semantica de nodos duplicados.

Unica fase autorizada a modificar contenido teorico. Ver dataset/metadata/
merge_decisions.json para la fusion real aplicada (decidida a mano, nodo
por nodo, leyendo el contenido completo de cada cluster).

Paso 1 (este script, --cluster): normaliza titulos (NFKD, sin acentos,
lowercase) y construye un grafo de similitud entre nodos: arista si el
titulo es exactamente igual O rapidfuzz.ratio >= 92. Los componentes
conexos del grafo son los clusters candidatos a fusion. Escribe
dataset/metadata/merge_clusters.json para revision humana.

Paso 2 (este script, --apply): lee dataset/metadata/merge_decisions.json
(escrito a mano tras revisar los clusters) y aplica cada fusion:
  - crea/actualiza el nodo canonico con el contenido unificado
  - redirige en todo el dataset las referencias a los ids perdedores
  - mueve los JSON originales de los perdedores a
    dataset/metadata/merged_originals/
  - registra todo en dataset/metadata/phase1_6_log.json

Uso:
  python scripts/phase1_6_merge.py --cluster
  python scripts/phase1_6_merge.py --apply
"""
import collections
import json
import sys
import unicodedata
from pathlib import Path

from rapidfuzz import fuzz

BASE = Path(__file__).resolve().parent.parent
NODOS_DIR = BASE / "dataset" / "nodos"
METADATA_DIR = BASE / "dataset" / "metadata"
MERGED_ORIGINALS_DIR = METADATA_DIR / "merged_originals"

CLUSTERS_PATH = METADATA_DIR / "merge_clusters.json"
DECISIONS_PATH = METADATA_DIR / "merge_decisions.json"
LOG_PATH = METADATA_DIR / "phase1_6_log.json"

REF_KEYS = ("nodos_previos", "nodos_siguientes")
SIMILARITY_THRESHOLD = 92


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_all_nodes():
    nodes = {}
    for path in sorted(NODOS_DIR.glob("*.json")):
        nodes[path.stem] = load_json(path)
    return nodes


def normalize_title(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().strip()
    return s


def build_clusters(nodes):
    ids = sorted(nodes)
    titles = {nid: normalize_title(nodes[nid].get("titulo_concepto", "")) for nid in ids}

    adjacency = collections.defaultdict(set)
    edges = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            ta, tb = titles[a], titles[b]
            if not ta or not tb:
                continue
            if ta == tb:
                score = 100
            else:
                score = fuzz.ratio(ta, tb)
            if ta == tb or score >= SIMILARITY_THRESHOLD:
                adjacency[a].add(b)
                adjacency[b].add(a)
                edges.append({"a": a, "b": b, "score": round(score, 1), "exact_title": ta == tb})

    visited = set()
    clusters = []
    for nid in ids:
        if nid in visited or nid not in adjacency:
            continue
        stack = [nid]
        visited.add(nid)
        comp = []
        while stack:
            cur = stack.pop()
            comp.append(cur)
            for neigh in adjacency[cur]:
                if neigh not in visited:
                    visited.add(neigh)
                    stack.append(neigh)
        if len(comp) > 1:
            clusters.append(sorted(comp))

    clusters.sort(key=lambda c: (-len(c), c[0]))
    return clusters, edges


def cmd_cluster():
    nodes = load_all_nodes()
    clusters, edges = build_clusters(nodes)

    out = []
    for cluster in clusters:
        out.append({
            "members": [
                {"node_id": nid, "titulo_concepto": nodes[nid].get("titulo_concepto")}
                for nid in cluster
            ],
        })

    with open(CLUSTERS_PATH, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)

    total_nodes_in_clusters = sum(len(c) for c in clusters)
    print(f"Clusters encontrados: {len(clusters)} (cubren {total_nodes_in_clusters} nodos)")
    for c in out:
        titles = [m["titulo_concepto"] for m in c["members"]]
        print(f"  - {[m['node_id'] for m in c['members']]}: {titles}")
    print(f"\nEscrito en {CLUSTERS_PATH.relative_to(BASE)}")


# ---------------------------------------------------------------------------
# Paso 2: aplicar fusiones desde merge_decisions.json
# ---------------------------------------------------------------------------

def save_node(node_id, data):
    with open(NODOS_DIR / f"{node_id}.json", "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)


def dedupe_and_remove_self(node_id, values):
    seen = set()
    out = []
    for v in values:
        if v == node_id or v in seen:
            continue
        seen.add(v)
        out.append(v)
    return out


def merge_links(cluster_members, nodes_before):
    """Union deduplicada de nodos_previos/nodos_siguientes de todos los
    miembros del cluster, leida de los datos ORIGINALES (antes de fusionar).
    Elimina referencias a otros miembros del mismo cluster (se vuelven
    auto-referencias del nodo canonico tras la fusion)."""
    member_set = set(cluster_members)
    merged = {}
    for key in REF_KEYS:
        seen = set()
        out = []
        for member in cluster_members:
            for ref in nodes_before.get(member, {}).get(key, []):
                if ref in member_set or ref in seen:
                    continue
                seen.add(ref)
                out.append(ref)
        merged[key] = out
    return merged


def cmd_apply():
    if not DECISIONS_PATH.exists():
        print(f"No existe {DECISIONS_PATH.relative_to(BASE)}. Corre --cluster y decide primero.")
        sys.exit(1)

    decisions = load_json(DECISIONS_PATH)
    nodes = load_all_nodes()
    existing_ids = set(nodes)
    nodes_before = dict(nodes)  # snapshot previo a cualquier fusion, para computar enlaces

    MERGED_ORIGINALS_DIR.mkdir(parents=True, exist_ok=True)

    log = {"merges": []}
    redirect_map = {}

    for decision in decisions:
        canonical_id = decision["canonical_id"]
        losers = decision["losers"]

        for loser in losers:
            if loser != canonical_id:
                redirect_map[loser] = canonical_id

        log["merges"].append({
            "cluster": decision.get("cluster_members", losers + [canonical_id]),
            "canonical_id": canonical_id,
            "losers": [l for l in losers if l != canonical_id],
            "notes": decision.get("notes", ""),
        })

    # 1. Escribir/actualizar nodos canonicos con el contenido fusionado.
    #    nodos_previos/nodos_siguientes se calculan automaticamente por
    #    union de los miembros originales del cluster (no a mano).
    for decision in decisions:
        canonical_id = decision["canonical_id"]
        cluster_members = decision.get("cluster_members", decision["losers"] + [canonical_id])
        canonical_data = dict(decision["canonical_data"])
        canonical_data["node_id"] = canonical_id
        canonical_data.update(merge_links(cluster_members, nodes_before))
        save_node(canonical_id, canonical_data)
        existing_ids.add(canonical_id)

    # 2. Mover los JSON originales de los perdedores a merged_originals/
    for decision in decisions:
        canonical_id = decision["canonical_id"]
        for loser in decision["losers"]:
            if loser == canonical_id:
                continue
            loser_path = NODOS_DIR / f"{loser}.json"
            if loser_path.exists():
                dest = MERGED_ORIGINALS_DIR / f"{loser}.json"
                loser_path.rename(dest)
                existing_ids.discard(loser)

    # 3. Redirigir referencias en todo el dataset (recargar tras mover archivos)
    nodes = load_all_nodes()
    updated = 0
    for node_id, data in nodes.items():
        changed = False
        for key in REF_KEYS:
            values = data.get(key)
            if not isinstance(values, list):
                continue
            new_values = [redirect_map.get(v, v) for v in values]
            deduped = dedupe_and_remove_self(node_id, new_values)
            if deduped != values:
                changed = True
                data[key] = deduped
        if changed:
            save_node(node_id, data)
            updated += 1

    with open(LOG_PATH, "w", encoding="utf-8") as fh:
        json.dump(log, fh, ensure_ascii=False, indent=2)

    print(f"Fusiones aplicadas: {len(decisions)}")
    print(f"Nodos con referencias redirigidas: {updated}")
    print(f"Log escrito en {LOG_PATH.relative_to(BASE)}")


def main():
    if "--cluster" in sys.argv:
        cmd_cluster()
    elif "--apply" in sys.argv:
        cmd_apply()
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
