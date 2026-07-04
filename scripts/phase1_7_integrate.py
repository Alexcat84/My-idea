#!/usr/bin/env python3
"""
phase1_7_integrate.py - Fase 1.7: integracion del lote "New txt/" (409 nodos,
libros: Financial Intelligence for Entrepreneurs, The Founder's Dilemmas,
Venture Deals) al dataset principal (908 nodos).

Subcomandos (se ejecutan en orden; cada uno espera que el anterior ya haya
corrido y, cuando aplica, que exista el archivo de decisiones manuales
correspondiente en dataset/metadata/):

  --cluster            Paso 1a: detecta clusters de duplicados intra-lote
                        (titulo exacto, titulo fuzzy >= 88, o contenido
                        fuzzy >= 80) -> dataset/metadata/new_txt_clusters.json
  --merge              Paso 1b: aplica dataset/metadata/merge_decisions_v11.json
                        (escrito a mano tras revisar los clusters) sobre
                        "New txt/" en el sitio. Perdedores -> merged_originals_v11/
  --ghosts             Paso 2: analiza referencias fantasma del lote ya
                        deduplicado contra (a) ids del lote y (b) ids del
                        dataset principal. Auto-resuelve >=90 (rapidfuzz,
                        desempate por ratio literal) y escribe
                        dataset/metadata/ghost_report_v11.json con lo que
                        quedo sin resolver para decision manual.
  --apply-ghosts       Aplica las resoluciones automaticas + las manuales
                        (dataset/metadata/ghost_decisions_v11.json) sobre
                        "New txt/".
  --degree             Paso 3a (analisis): imprime los nodos del lote con
                        mayor grado interno (candidatos a hub) y los nodos
                        sin nodos_previos / sin nodos_siguientes (Paso 3b).
  --bridges            Aplica dataset/metadata/bridges_v11.json (puentes de
                        hub + enlaces oportunistas, escritos a mano) sobre
                        "New txt/" Y sobre dataset/nodos/ (bidireccional).
  --safeguard          Paso 4: agrega la frase de salvaguarda juridica a los
                        nodos de jurisdiccion especifica listados en
                        JURISDICTIONAL_NODES.
  --finalize           Paso 5: mueve los .json finales de "New txt/" a
                        dataset/nodos/, elimina la carpeta "New txt", y
                        mueve New txt/pipeline_new.py a scripts/archive/.

Uso:
  python scripts/phase1_7_integrate.py --cluster
  python scripts/phase1_7_integrate.py --merge
  python scripts/phase1_7_integrate.py --ghosts
  python scripts/phase1_7_integrate.py --apply-ghosts
  python scripts/phase1_7_integrate.py --degree
  python scripts/phase1_7_integrate.py --bridges
  python scripts/phase1_7_integrate.py --safeguard
  python scripts/phase1_7_integrate.py --finalize
"""
import collections
import json
import shutil
import sys
import unicodedata
from pathlib import Path

from rapidfuzz import fuzz

BASE = Path(__file__).resolve().parent.parent
BATCH_DIR = BASE / "New txt"
NODOS_DIR = BASE / "dataset" / "nodos"
METADATA_DIR = BASE / "dataset" / "metadata"
ARCHIVE_DIR = BASE / "scripts" / "archive"

MERGED_ORIGINALS_V11 = METADATA_DIR / "merged_originals_v11"

CLUSTERS_PATH = METADATA_DIR / "new_txt_clusters.json"
MERGE_DECISIONS_PATH = METADATA_DIR / "merge_decisions_v11.json"
PHASE1_7_LOG_PATH = METADATA_DIR / "phase1_7_log.json"

GHOST_REPORT_PATH = METADATA_DIR / "ghost_report_v11.json"
GHOST_DECISIONS_PATH = METADATA_DIR / "ghost_decisions_v11.json"

BRIDGES_PATH = METADATA_DIR / "bridges_v11.json"

REF_KEYS = ("nodos_previos", "nodos_siguientes")

TITLE_SIM_THRESHOLD = 88
CONTENT_SIM_THRESHOLD = 80
GHOST_AUTO_THRESHOLD = 90

# Nodos con jurisdiccion especifica de EE.UU. (Paso 4). Se verifican contra
# disco antes de aplicar; ids que no existan se ignoran silenciosamente
# (pueden haber sido renombrados/fusionados en el Paso 1).
JURISDICTIONAL_NODES = [
    # Lista dada por el usuario (estructura_corporativa_c_corp se fusiono en
    # seleccion_estructura_corporativa durante el Paso 1)
    "eleccion_83b",
    "crowdfunding_legal_exemptions_jobs_act",
    "cumplimiento_sarbanes_oxley",
    "seleccion_estructura_corporativa",
    "inversionistas_acreditados",
    "cumplimiento_inversionistas_acreditados",
    # Detectados adicionalmente por busqueda de terminos jurisdiccionales
    # (SEC, IRS, 83(b), 409A, Sarbanes, JOBS Act, C Corp/S Corp/LLC) con
    # limites de palabra para evitar falsos positivos (p.ej. 'convertirse')
    "compensacion_service_providers",
    "derechos_de_registro",
    "equity_crowdfunding",
    "exercise_period_opciones",
    "original_issue_discount_oid",
    "preparacion_due_diligence",
    "preparacion_para_salida_a_bolsa",
    "registration_rights_stock_consideration",
    "valuacion_409a",
    "vesting_acciones_fundadores",
    "vesting_dinamico",
]

JURISDICTIONAL_NOTE = (
    " Los detalles legales y fiscales de este tema varían según el país; "
    "antes de actuar, verifícalos con un profesional local."
)


# ---------------------------------------------------------------------------
# Utilidades comunes
# ---------------------------------------------------------------------------

def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)


def load_dir_nodes(directory):
    nodes = {}
    for path in sorted(directory.glob("*.json")):
        nodes[path.stem] = load_json(path)
    return nodes


def save_node_in(directory, node_id, data):
    with open(directory / f"{node_id}.json", "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)


def normalize_title(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().strip()
    s = s.replace("_", " ").replace("-", " ")
    while "  " in s:
        s = s.replace("  ", " ")
    return s.strip()


def dedupe_and_remove_self(node_id, values):
    seen = set()
    out = []
    for v in values:
        if v == node_id or v in seen:
            continue
        seen.add(v)
        out.append(v)
    return out


# ---------------------------------------------------------------------------
# --cluster : Paso 1a
# ---------------------------------------------------------------------------

def cmd_cluster():
    nodes = load_dir_nodes(BATCH_DIR)
    ids = sorted(nodes)
    titles = {nid: normalize_title(nodes[nid].get("titulo_concepto", "")) for nid in ids}
    resumenes = {nid: nodes[nid].get("resumen_teorico", "") or "" for nid in ids}

    adjacency = collections.defaultdict(set)
    edges = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            ta, tb = titles[a], titles[b]
            if not ta or not tb:
                continue
            reason = None
            if ta == tb:
                reason = "titulo_exacto"
            else:
                title_score = fuzz.ratio(ta, tb)
                if title_score >= TITLE_SIM_THRESHOLD:
                    reason = f"titulo_fuzzy({title_score:.0f})"
                else:
                    ra, rb = resumenes[a], resumenes[b]
                    if ra and rb:
                        content_score = fuzz.ratio(ra, rb)
                        if content_score >= CONTENT_SIM_THRESHOLD:
                            reason = f"contenido_fuzzy({content_score:.0f})"
            if reason:
                adjacency[a].add(b)
                adjacency[b].add(a)
                edges.append({"a": a, "b": b, "reason": reason})

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
        clusters.append(sorted(comp))

    clusters.sort(key=lambda c: (-len(c), c[0]))

    out = []
    for cluster in clusters:
        out.append({
            "members": [
                {"node_id": nid, "titulo_concepto": nodes[nid].get("titulo_concepto"),
                 "fuente": nodes[nid].get("fuente")}
                for nid in cluster
            ],
        })

    save_json(CLUSTERS_PATH, out)
    total = sum(len(c) for c in clusters)
    print(f"Clusters detectados: {len(clusters)} (cubren {total} nodos de {len(nodes)})")
    for c in out:
        print(f"  - {[m['node_id'] for m in c['members']]}")
    print(f"\nEscrito en {CLUSTERS_PATH.relative_to(BASE)}")


# ---------------------------------------------------------------------------
# --merge : Paso 1b (misma mecanica que phase1_6_merge.py --apply, pero
# operando sobre "New txt/" en el sitio, no sobre dataset/nodos/)
# ---------------------------------------------------------------------------

def merge_links(cluster_members, nodes_before):
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


def cmd_merge():
    if not MERGE_DECISIONS_PATH.exists():
        print(f"No existe {MERGE_DECISIONS_PATH.relative_to(BASE)}. Corre --cluster y decide primero.")
        sys.exit(1)

    decisions = load_json(MERGE_DECISIONS_PATH)
    nodes_before = load_dir_nodes(BATCH_DIR)

    MERGED_ORIGINALS_V11.mkdir(parents=True, exist_ok=True)

    log = {"merges": []}
    for decision in decisions:
        canonical_id = decision["canonical_id"]
        cluster_members = decision.get("cluster_members", decision["losers"] + [canonical_id])
        canonical_data = dict(decision["canonical_data"])
        canonical_data["node_id"] = canonical_id
        canonical_data.update(merge_links(cluster_members, nodes_before))
        save_node_in(BATCH_DIR, canonical_id, canonical_data)

        log["merges"].append({
            "cluster": cluster_members,
            "canonical_id": canonical_id,
            "losers": decision["losers"],
            "notes": decision.get("notes", ""),
        })

    for decision in decisions:
        canonical_id = decision["canonical_id"]
        for loser in decision["losers"]:
            if loser == canonical_id:
                continue
            loser_path = BATCH_DIR / f"{loser}.json"
            if loser_path.exists():
                loser_path.rename(MERGED_ORIGINALS_V11 / f"{loser}.json")

    # Redirigir referencias dentro del lote ya fusionado
    redirect_map = {}
    for decision in decisions:
        for loser in decision["losers"]:
            if loser != decision["canonical_id"]:
                redirect_map[loser] = decision["canonical_id"]

    nodes = load_dir_nodes(BATCH_DIR)
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
            save_node_in(BATCH_DIR, node_id, data)
            updated += 1

    existing_log = load_json(PHASE1_7_LOG_PATH) if PHASE1_7_LOG_PATH.exists() else {}
    existing_log["merges"] = log["merges"]
    save_json(PHASE1_7_LOG_PATH, existing_log)

    print(f"Fusiones aplicadas: {len(decisions)}")
    print(f"Nodos del lote con referencias redirigidas: {updated}")
    print(f"Nodos del lote tras fusion: {len(load_dir_nodes(BATCH_DIR))}")


# ---------------------------------------------------------------------------
# --ghosts : Paso 2 (analisis)
# ---------------------------------------------------------------------------

def build_candidate_strings(nodes):
    """Construye, por nodo, el conjunto de strings contra los que puede
    matchear un fantasma. Los fragmentos extraidos del parentesis del
    titulo (inner/outer) solo se agregan si tienen 2+ palabras: una sola
    palabra generica (p.ej. 'Equity', 'IPO', 'VC') dispara falsos positivos
    con token_set_ratio=100 contra cualquier fantasma que la contenga,
    sin importar el resto de las palabras."""
    cand = {}
    for nid, data in nodes.items():
        strings = {normalize_title(nid)}
        titulo = data.get("titulo_concepto", "")
        if titulo:
            strings.add(normalize_title(titulo))
            if "(" in titulo and ")" in titulo:
                inner = titulo[titulo.find("(") + 1: titulo.rfind(")")]
                if inner.strip() and len(normalize_title(inner).split()) >= 2:
                    strings.add(normalize_title(inner))
                outer = titulo[: titulo.find("(")]
                if outer.strip() and len(normalize_title(outer).split()) >= 2:
                    strings.add(normalize_title(outer))
        cand[nid] = strings
    return cand


def best_match(phantom, cand):
    p = normalize_title(phantom)
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


def cmd_ghosts():
    batch_nodes = load_dir_nodes(BATCH_DIR)
    main_nodes = load_dir_nodes(NODOS_DIR)
    all_nodes = {**main_nodes, **batch_nodes}
    existing_ids = set(all_nodes)

    phantoms = collections.Counter()
    for data in batch_nodes.values():
        for key in REF_KEYS:
            for ref in data.get(key, []):
                if ref not in existing_ids:
                    phantoms[ref] += 1

    cand = build_candidate_strings(all_nodes)

    auto_map = {}
    unresolved = {}
    for phantom, count in phantoms.most_common():
        scored = best_match(phantom, cand)
        top_nid, top_score, top_ratio = scored[0]
        single_token = len(normalize_title(phantom).split()) <= 1
        if top_score >= GHOST_AUTO_THRESHOLD and (not single_token or top_ratio >= 85):
            auto_map[phantom] = {"resolved_to": top_nid, "score": top_score, "ratio": top_ratio}
        else:
            unresolved[phantom] = {
                "refs": count,
                "candidatos": [
                    {"node_id": n, "score": s, "ratio": r,
                     "titulo": all_nodes[n].get("titulo_concepto", "")}
                    for n, s, r in scored[:3]
                ],
            }

    save_json(GHOST_REPORT_PATH, {
        "total_phantoms": len(phantoms),
        "total_refs": sum(phantoms.values()),
        "auto_resolved": auto_map,
        "unresolved": unresolved,
    })

    print(f"Fantasmas unicos: {len(phantoms)} (total refs: {sum(phantoms.values())})")
    print(f"Auto-resueltos (score>={GHOST_AUTO_THRESHOLD}): {len(auto_map)}")
    print(f"Sin resolver (requieren decision manual): {len(unresolved)}")
    print(f"\nEscrito en {GHOST_REPORT_PATH.relative_to(BASE)}")


def cmd_apply_ghosts():
    if not GHOST_REPORT_PATH.exists():
        print("No existe el reporte de fantasmas. Corre --ghosts primero.")
        sys.exit(1)
    report = load_json(GHOST_REPORT_PATH)
    resolve_map = {k: v["resolved_to"] for k, v in report["auto_resolved"].items()}

    manual_map = {}
    if GHOST_DECISIONS_PATH.exists():
        manual_map = load_json(GHOST_DECISIONS_PATH)
        resolve_map.update({k: v for k, v in manual_map.items() if v is not None})

    batch_nodes = load_dir_nodes(BATCH_DIR)
    main_nodes = load_dir_nodes(NODOS_DIR)
    existing_ids = set(batch_nodes) | set(main_nodes)

    removed_log = []
    updated = 0
    for node_id, data in batch_nodes.items():
        changed = False
        for key in REF_KEYS:
            values = data.get(key)
            if not isinstance(values, list):
                continue
            new_values = []
            for ref in values:
                if ref in existing_ids:
                    new_values.append(ref)
                    continue
                if ref in resolve_map:
                    new_values.append(resolve_map[ref])
                    changed = True
                elif ref in manual_map and manual_map[ref] is None:
                    changed = True
                    removed_log.append({"node": node_id, "key": key, "ref": ref})
                elif ref in report.get("unresolved", {}):
                    # sin decision manual todavia: se deja para no perder informacion silenciosamente
                    new_values.append(ref)
                else:
                    new_values.append(ref)
            deduped = dedupe_and_remove_self(node_id, new_values)
            if deduped != values:
                changed = True
                data[key] = deduped
        if changed:
            save_node_in(BATCH_DIR, node_id, data)
            updated += 1

    existing_log = load_json(PHASE1_7_LOG_PATH) if PHASE1_7_LOG_PATH.exists() else {}
    existing_log["ghosts_auto_resolved"] = report["auto_resolved"]
    existing_log["ghosts_manual"] = manual_map
    existing_log["ghosts_removed"] = removed_log
    save_json(PHASE1_7_LOG_PATH, existing_log)

    print(f"Nodos actualizados: {updated}")
    print(f"Referencias eliminadas sin resolver: {len(removed_log)}")

    # Reportar cuantos fantasmas siguen sin ninguna decision (ni auto ni manual)
    still_ghost = [p for p in report.get("unresolved", {}) if p not in manual_map]
    if still_ghost:
        print(f"ATENCION: {len(still_ghost)} fantasma(s) sin decision manual todavia (quedaron intactos): {still_ghost[:10]}{'...' if len(still_ghost) > 10 else ''}")


# ---------------------------------------------------------------------------
# --degree : Paso 3a/3b (analisis)
# ---------------------------------------------------------------------------

def cmd_degree():
    batch_nodes = load_dir_nodes(BATCH_DIR)
    existing_ids = set(batch_nodes)

    degree = collections.Counter()
    no_previos = []
    no_siguientes = []
    for nid, data in batch_nodes.items():
        prev = [r for r in data.get("nodos_previos", []) if r in existing_ids]
        sig = [r for r in data.get("nodos_siguientes", []) if r in existing_ids]
        degree[nid] += len(prev) + len(sig)
        if not data.get("nodos_previos"):
            no_previos.append(nid)
        if not data.get("nodos_siguientes"):
            no_siguientes.append(nid)
        for r in prev + sig:
            degree[r] += 1

    top = degree.most_common(20)
    print("--- Top 20 nodos por grado interno (candidatos a hub) ---")
    for nid, deg in top:
        print(f"  {deg:3d}  {nid}  ({batch_nodes[nid].get('titulo_concepto')})")

    print(f"\n--- Nodos sin nodos_previos ({len(no_previos)}) ---")
    for nid in no_previos:
        print(f"  {nid}  ({batch_nodes[nid].get('titulo_concepto')})  [fase={batch_nodes[nid].get('fase_proyecto')}]")

    print(f"\n--- Nodos sin nodos_siguientes ({len(no_siguientes)}) ---")
    for nid in no_siguientes:
        print(f"  {nid}  ({batch_nodes[nid].get('titulo_concepto')})  [fase={batch_nodes[nid].get('fase_proyecto')}]")


# ---------------------------------------------------------------------------
# --bridges : aplica puentes de hub + enlaces oportunistas (bidireccional)
# ---------------------------------------------------------------------------

def cmd_bridges():
    if not BRIDGES_PATH.exists():
        print(f"No existe {BRIDGES_PATH.relative_to(BASE)}. Escribelo a mano primero.")
        sys.exit(1)
    bridges = load_json(BRIDGES_PATH)

    batch_nodes = load_dir_nodes(BATCH_DIR)
    main_nodes = load_dir_nodes(NODOS_DIR)

    def add_edge(nodes_map, directory, node_id, key, target):
        data = nodes_map[node_id]
        values = data.get(key, [])
        if target not in values:
            values = values + [target]
            data[key] = dedupe_and_remove_self(node_id, values)
            save_node_in(directory, node_id, data)
            return True
        return False

    applied = []
    for link in bridges:
        src, dst = link["from"], link["to"]
        src_dir, src_map = (BATCH_DIR, batch_nodes) if src in batch_nodes else (NODOS_DIR, main_nodes)
        dst_dir, dst_map = (BATCH_DIR, batch_nodes) if dst in batch_nodes else (NODOS_DIR, main_nodes)
        if src not in src_map:
            print(f"ADVERTENCIA: id origen no encontrado, se omite: {src}")
            continue
        if dst not in dst_map:
            print(f"ADVERTENCIA: id destino no encontrado, se omite: {dst}")
            continue
        a = add_edge(src_map, src_dir, src, "nodos_siguientes", dst)
        b = add_edge(dst_map, dst_dir, dst, "nodos_previos", src)
        if a or b:
            applied.append({"from": src, "to": dst, "type": link.get("type", "bridge")})

    existing_log = load_json(PHASE1_7_LOG_PATH) if PHASE1_7_LOG_PATH.exists() else {}
    existing_log["bridges"] = applied
    save_json(PHASE1_7_LOG_PATH, existing_log)

    print(f"Puentes/enlaces aplicados: {len(applied)} de {len(bridges)} propuestos")


# ---------------------------------------------------------------------------
# --safeguard : Paso 4
# ---------------------------------------------------------------------------

def cmd_safeguard():
    batch_nodes = load_dir_nodes(BATCH_DIR)
    applied = []
    for node_id in JURISDICTIONAL_NODES:
        if node_id not in batch_nodes:
            print(f"(omitido, no existe en el lote: {node_id})")
            continue
        data = batch_nodes[node_id]
        resumen = data.get("resumen_teorico", "")
        if JURISDICTIONAL_NOTE.strip() in resumen:
            continue
        data["resumen_teorico"] = resumen.rstrip() + JURISDICTIONAL_NOTE
        save_node_in(BATCH_DIR, node_id, data)
        applied.append(node_id)

    existing_log = load_json(PHASE1_7_LOG_PATH) if PHASE1_7_LOG_PATH.exists() else {}
    existing_log["jurisdictional_safeguard"] = applied
    save_json(PHASE1_7_LOG_PATH, existing_log)

    print(f"Salvaguarda aplicada a {len(applied)} nodo(s): {applied}")


# ---------------------------------------------------------------------------
# --finalize : Paso 5
# ---------------------------------------------------------------------------

def cmd_finalize():
    batch_nodes = load_dir_nodes(BATCH_DIR)
    moved = 0
    for node_id, data in batch_nodes.items():
        dest = NODOS_DIR / f"{node_id}.json"
        if dest.exists():
            print(f"ATENCION: colision de nombre con dataset principal, no se sobreescribe: {node_id}")
            continue
        save_node_in(NODOS_DIR, node_id, data)
        moved += 1

    pipeline_script = BATCH_DIR / "pipeline_new.py"
    if pipeline_script.exists():
        ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
        pipeline_script.rename(ARCHIVE_DIR / "pipeline_new.py")

    shutil.rmtree(BATCH_DIR)

    existing_log = load_json(PHASE1_7_LOG_PATH) if PHASE1_7_LOG_PATH.exists() else {}
    existing_log["finalize_moved_count"] = moved
    save_json(PHASE1_7_LOG_PATH, existing_log)

    print(f"Nodos movidos a dataset/nodos/: {moved}")
    print("Carpeta 'New txt' eliminada. pipeline_new.py archivado en scripts/archive/.")


def main():
    args = sys.argv[1:]
    dispatch = {
        "--cluster": cmd_cluster,
        "--merge": cmd_merge,
        "--ghosts": cmd_ghosts,
        "--apply-ghosts": cmd_apply_ghosts,
        "--degree": cmd_degree,
        "--bridges": cmd_bridges,
        "--safeguard": cmd_safeguard,
        "--finalize": cmd_finalize,
    }
    if not args or args[0] not in dispatch:
        print(__doc__)
        sys.exit(1)
    dispatch[args[0]]()


if __name__ == "__main__":
    main()
