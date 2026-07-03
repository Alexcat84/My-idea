# -*- coding: utf-8 -*-
"""
fix_spiderweb.py - Fase 1.2: Resolucion de nodos fantasma
Estrategia de 3 capas:
  Capa A: matching automatico (fuzzy) contra node_ids Y titulos de conceptos
  Capa B: candidatos ambiguos que requieren revision (humana o via Claude)
  Capa C: fantasmas sin candidato razonable (eliminar referencia o crear nodo)

Salidas (en reports/):
  alias_map_auto.json     -> fantasma: nodo_real (aplicable automaticamente)
  review_candidates.json  -> fantasma: [candidatos con score] (revisar)
  unresolved.json         -> fantasmas sin match (con conteo de referencias)
  fix_report.md           -> reporte legible

Uso:
  python3 fix_spiderweb.py           # solo analiza y genera reportes
  python3 fix_spiderweb.py --apply   # ademas aplica alias_map_auto sobre dataset_clean/
"""
import os
import sys
import json
import shutil
import unicodedata
import collections
from pathlib import Path
from rapidfuzz import fuzz

AUTO_THRESHOLD = 90
REVIEW_THRESHOLD = 72

BASE = Path(__file__).resolve().parent.parent
DATASET = BASE / "dataset" / "nodos"
REPORTS = BASE / "reports"
CLEAN = BASE / "dataset_clean" / "nodos"


def normalize(s: str) -> str:
    """lowercase, sin acentos, solo [a-z0-9_], espacios y guiones -> _"""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    out = []
    for c in s:
        if c.isalnum():
            out.append(c)
        elif c in " -_/":
            out.append("_")
    s = "".join(out)
    while "__" in s:
        s = s.replace("__", "_")
    # Espacios en vez de guiones bajos para que token_set_ratio tokenice bien
    # (permite matchear con orden de palabras distinto: 'verificacion wallas'
    #  vs 'wallas etapa verificacion')
    return s.strip("_").replace("_", " ")


def load_nodes():
    nodes = {}
    for f in sorted(DATASET.glob("*.json")):
        with open(f, encoding="utf-8") as fh:
            nodes[f.stem] = json.load(fh)
    return nodes


def build_candidate_strings(nodes):
    """Para cada nodo real: strings contra los que se puede matchear un fantasma."""
    cand = {}
    for nid, data in nodes.items():
        strings = {normalize(nid)}
        titulo = data.get("titulo_concepto", "")
        if titulo:
            strings.add(normalize(titulo))
            # Titulos tipo "Lienzo de Modelo de Negocio (Business Model Canvas)":
            # extraer tambien el contenido del parentesis como string separado
            if "(" in titulo and ")" in titulo:
                inner = titulo[titulo.find("(") + 1 : titulo.rfind(")")]
                if inner.strip():
                    strings.add(normalize(inner))
                outer = titulo[: titulo.find("(")]
                if outer.strip():
                    strings.add(normalize(outer))
        cand[nid] = strings
    return cand


def best_match(phantom, cand):
    """Devuelve lista [(nid, score, ratio)] ordenada por (score, ratio) desc.
    score = token_set_ratio (tolera orden de palabras distinto)
    ratio = similitud literal, usado como desempate para preferir el nodo
            cuyo nombre se parece mas de cerca al fantasma."""
    p = normalize(phantom)
    scored = []
    for nid, strings in cand.items():
        best_ts, best_r = 0, 0
        for s in strings:
            ts = fuzz.token_set_ratio(p, s)
            r = fuzz.ratio(p, s)
            if (ts, r) > (best_ts, best_r):
                best_ts, best_r = ts, r
        scored.append((nid, best_ts, best_r))
    scored.sort(key=lambda x: (-x[1], -x[2]))
    return scored


def collect_phantoms(nodes):
    existing = set(nodes)
    refs = collections.Counter()
    for data in nodes.values():
        for key in ("nodos_previos", "nodos_siguientes"):
            for t in data.get(key, []):
                if t not in existing:
                    refs[t] += 1
    return refs


def apply_alias_map(nodes, alias_map):
    """Aplica el alias map sobre una copia del dataset. Deduplica y elimina self-links."""
    if CLEAN.exists():
        shutil.rmtree(CLEAN.parent)
    CLEAN.mkdir(parents=True)
    fixed_links = 0
    for nid, data in nodes.items():
        new = dict(data)
        for key in ("nodos_previos", "nodos_siguientes"):
            seen, out = set(), []
            for t in data.get(key, []):
                t2 = alias_map.get(t, t)
                if t2 != t:
                    fixed_links += 1
                if t2 == nid or t2 in seen:
                    continue
                seen.add(t2)
                out.append(t2)
            new[key] = out
        with open(CLEAN / f"{nid}.json", "w", encoding="utf-8") as fh:
            json.dump(new, fh, ensure_ascii=False, indent=2)
    return fixed_links


def graph_stats(nodes):
    existing = set(nodes)
    total = broken = 0
    in_deg = collections.Counter()
    for data in nodes.values():
        for key in ("nodos_previos", "nodos_siguientes"):
            for t in data.get(key, []):
                total += 1
                if t not in existing:
                    broken += 1
                elif key == "nodos_siguientes":
                    in_deg[t] += 1
    no_in = sum(1 for n in existing if in_deg[n] == 0)
    return total, broken, no_in


def main():
    apply_flag = "--apply" in sys.argv
    REPORTS.mkdir(exist_ok=True)

    nodes = load_nodes()
    phantoms = collect_phantoms(nodes)
    cand = build_candidate_strings(nodes)

    total0, broken0, noin0 = graph_stats(nodes)
    print(f"Nodos: {len(nodes)} | Enlaces: {total0} | Rotos: {broken0} | Fantasmas unicos: {len(phantoms)}")

    alias_map, review, unresolved = {}, {}, {}
    for phantom, count in phantoms.most_common():
        scored = best_match(phantom, cand)
        top_nid, top_score, top_ratio = scored[0]
        single_token = len(normalize(phantom).split()) <= 1
        # Auto solo si: score alto Y (fantasma multi-palabra O similitud literal alta).
        # Fantasmas de una sola palabra ('pivote', 'brainstorm') son demasiado
        # ambiguos para resolver sin revision, salvo match literal casi exacto.
        if top_score >= AUTO_THRESHOLD and (not single_token or top_ratio >= 85):
            alias_map[phantom] = top_nid
        elif top_score >= REVIEW_THRESHOLD:
            review[phantom] = {
                "refs": count,
                "candidatos": [
                    {"node_id": n, "score": s, "ratio": r,
                     "titulo": nodes[n].get("titulo_concepto", "")}
                    for n, s, r in scored[:3] if s >= REVIEW_THRESHOLD - 10
                ],
            }
        else:
            unresolved[phantom] = {
                "refs": count,
                "mejor_candidato": {"node_id": top_nid, "score": top_score},
            }

    auto_link_hits = sum(phantoms[p] for p in alias_map)
    review_link_hits = sum(phantoms[p] for p in review)
    unresolved_link_hits = sum(phantoms[p] for p in unresolved)

    with open(REPORTS / "alias_map_auto.json", "w", encoding="utf-8") as fh:
        json.dump(alias_map, fh, ensure_ascii=False, indent=2, sort_keys=True)
    with open(REPORTS / "review_candidates.json", "w", encoding="utf-8") as fh:
        json.dump(review, fh, ensure_ascii=False, indent=2)
    with open(REPORTS / "unresolved.json", "w", encoding="utf-8") as fh:
        json.dump(unresolved, fh, ensure_ascii=False, indent=2)

    lines = [
        "# Reporte fix_spiderweb (Fase 1.2)",
        "",
        f"- Nodos reales: {len(nodes)}",
        f"- Enlaces totales: {total0}, rotos: {broken0} ({broken0/total0*100:.1f}%)",
        f"- Fantasmas unicos: {len(phantoms)}",
        "",
        "## Resolucion por capas",
        f"- Capa A (auto, score >= {AUTO_THRESHOLD}): {len(alias_map)} fantasmas, recuperan {auto_link_hits} enlaces",
        f"- Capa B (revision, {REVIEW_THRESHOLD}-{AUTO_THRESHOLD}): {len(review)} fantasmas, afectan {review_link_hits} enlaces",
        f"- Capa C (sin match, < {REVIEW_THRESHOLD}): {len(unresolved)} fantasmas, afectan {unresolved_link_hits} enlaces",
    ]

    if apply_flag:
        fixed = apply_alias_map(nodes, alias_map)
        clean_nodes = {f.stem: json.load(open(f, encoding="utf-8")) for f in CLEAN.glob("*.json")}
        total1, broken1, noin1 = graph_stats(clean_nodes)
        lines += [
            "",
            "## Resultado tras aplicar Capa A (dataset_clean/)",
            f"- Enlaces corregidos: {fixed}",
            f"- Rotos: {broken0} -> {broken1} ({broken1/total1*100:.1f}%)",
            f"- Nodos sin enlaces entrantes: {noin0} -> {noin1}",
        ]
        print(f"Aplicado. Rotos {broken0} -> {broken1}. Sin entrantes {noin0} -> {noin1}.")

    with open(REPORTS / "fix_report.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(lines[6:]))
    print(f"\nReportes en: {REPORTS}")


if __name__ == "__main__":
    main()
