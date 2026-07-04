#!/usr/bin/env python3
"""
run_phase1.py - Orquestador reproducible de la Fase 1 de saneamiento del grafo.

Pasos (en orden, idempotente):
  1. Normalizacion ASCII de nombres de archivo en dataset/nodos/
  2. Redireccion de referencias a nodos fusionados (duplicados eliminados
     historicamente por scripts/archive/phase1_5_merge.py)
  3. Aplicacion de los alias maps restantes (capa B, capa C, auto) generados
     por fix_spiderweb.py / resolve_capa_b.py / resolve_capa_c.py
  4. Limpieza final de cualquier referencia rota sin resolver
  5. Recompilacion de dataset/metadata/master_graph.json
  6. Validador Gate 0 (sys.exit(1) si algun chequeo falla)

Todas las rutas son relativas al repo (BASE = carpeta padre de scripts/).
No modifica contenido teorico de los nodos: solo nombres de archivo,
node_id, nodos_previos y nodos_siguientes.

Uso:
  python scripts/run_phase1.py
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
MASTER_GRAPH_PATH = METADATA_DIR / "master_graph.json"
LOG_PATH = METADATA_DIR / "phase1_run_log.json"

REF_KEYS = ("nodos_previos", "nodos_siguientes")

# Mapa de fusion de duplicados, tal como quedo definido en
# scripts/archive/phase1_5_merge.py. Se mantiene aqui como fuente de verdad
# reproducible para poder redirigir las referencias que ese script nunca
# redirigio cuando elimino los nodos duplicados.
MERGE_CLUSTERS = {
    "producto_minimo_viable": [
        "mvp_minimo_viable",
        "producto_minimo_viable_mvp",
        "minimum_viable_product_discovery",
        "minimum_viable_product_mvp",
    ],
    "lienzo_modelo_negocio": [
        "business_model_canvas_hcd",
        "business_model_canvas_ideo",
        "business_model_canvas_refresher",
    ],
}

# Alias maps generados por fix_spiderweb.py / resolve_capa_b.py / resolve_capa_c.py
ALIAS_MAP_FILES = [
    "alias_map_capa_b.json",
    "alias_map_capa_c.json",
    "alias_map_auto.json",
]


# ---------------------------------------------------------------------------
# Utilidades comunes
# ---------------------------------------------------------------------------

def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_node(node_id, data):
    with open(NODOS_DIR / f"{node_id}.json", "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)


def load_all_nodes():
    """Carga todos los nodos del dataset. Devuelve (nodes, parse_errors)."""
    nodes = {}
    parse_errors = []
    for path in sorted(NODOS_DIR.glob("*.json")):
        try:
            nodes[path.stem] = load_json(path)
        except json.JSONDecodeError as e:
            parse_errors.append({"file": path.name, "error": str(e)})
    return nodes, parse_errors


def ascii_id(s: str) -> str:
    """NFKD + elimina diacriticos (n~ -> n) + lowercase + solo [a-z0-9_]."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    out = []
    for c in s:
        if c.isalnum() and ord(c) < 128:
            out.append(c)
        elif c in " -_":
            out.append("_")
    s = "".join(out)
    while "__" in s:
        s = s.replace("__", "_")
    return s.strip("_")


def dedupe_and_remove_self(node_id, values):
    seen = set()
    out = []
    for v in values:
        if v == node_id or v in seen:
            continue
        seen.add(v)
        out.append(v)
    return out


def rewrite_refs(node_id, data, key, transform):
    """Aplica transform(ref) -> nuevo_ref_o_None a data[key]. None = eliminar.
    Devuelve True si hubo cambios. Siempre deduplica y quita auto-referencias."""
    values = data.get(key)
    if not isinstance(values, list):
        return False
    original = list(values)
    new_values = []
    for ref in values:
        result = transform(ref)
        if result is not None:
            new_values.append(result)
    deduped = dedupe_and_remove_self(node_id, new_values)
    data[key] = deduped
    return deduped != original


# ---------------------------------------------------------------------------
# Paso 1: Normalizacion ASCII
# ---------------------------------------------------------------------------

def step1_ascii_normalize(log):
    files = sorted(NODOS_DIR.glob("*.json"))
    existing_ids = {p.stem for p in files}
    rename_map = {}

    for path in files:
        old_id = path.stem
        if all(ord(c) < 128 for c in old_id):
            continue
        new_id = ascii_id(old_id)
        if not new_id:
            continue
        if new_id in existing_ids and new_id != old_id:
            # El destino ASCII ya existe: probable duplicado (posible fosil
            # con el mismo contenido bajo otro nombre). No renombramos con un
            # sufijo que ocultaria el choque; lo dejamos para revision manual.
            log["ascii_rename_collisions"].append({
                "old_id": old_id, "target_id": new_id,
                "note": "el id destino ya existe en disco; posible duplicado, no renombrado",
            })
            continue
        path.rename(NODOS_DIR / f"{new_id}.json")
        existing_ids.discard(old_id)
        existing_ids.add(new_id)
        rename_map[old_id] = new_id
        log["ascii_renames"].append({"old_id": old_id, "new_id": new_id})

    if not rename_map:
        return rename_map

    for path in sorted(NODOS_DIR.glob("*.json")):
        node_id = path.stem
        data = load_json(path)
        changed = False

        if data.get("node_id") in rename_map:
            data["node_id"] = rename_map[data["node_id"]]
            changed = True

        for key in REF_KEYS:
            if rewrite_refs(node_id, data, key, lambda r: rename_map.get(r, r)):
                changed = True

        if changed:
            save_node(node_id, data)

    return rename_map


# ---------------------------------------------------------------------------
# Paso 2: Redireccion de nodos fusionados
# ---------------------------------------------------------------------------

def build_merge_redirect_map():
    redirect = {}
    for canonical, dupes in MERGE_CLUSTERS.items():
        for dupe in dupes:
            redirect[dupe] = canonical
    return redirect


def step2_redirect_merged(log):
    redirect_map = build_merge_redirect_map()
    nodes, _ = load_all_nodes()
    updated = 0

    for node_id, data in nodes.items():
        changed = False
        for key in REF_KEYS:
            def transform(ref, _key=key):
                target = redirect_map.get(ref, ref)
                if target != ref:
                    log["merge_redirects"].append(
                        {"node": node_id, "key": _key, "from": ref, "to": target}
                    )
                return target

            if rewrite_refs(node_id, data, key, transform):
                changed = True
        if changed:
            save_node(node_id, data)
            updated += 1

    return updated, redirect_map


# ---------------------------------------------------------------------------
# Paso 3: Aliases restantes (capa B, capa C, auto)
# ---------------------------------------------------------------------------

def load_alias_maps():
    combined = {}
    sources = {}
    for fname in ALIAS_MAP_FILES:
        path = METADATA_DIR / fname
        if not path.exists():
            continue
        for k, v in load_json(path).items():
            if k in combined:
                continue  # ya resuelto por un mapa de mayor prioridad
            combined[k] = v
            sources[k] = fname
    return combined, sources


def resolve_target(target, redirect_chain, existing_ids, max_hops=10):
    """Sigue redirect_chain (renombres ASCII + fusiones paso 2) hasta hallar
    un nodo existente en disco, o devuelve None si la cadena no llega a
    ningun nodo real."""
    current = target
    seen = set()
    for _ in range(max_hops):
        if current in existing_ids:
            return current
        if current in seen:
            return None
        seen.add(current)
        nxt = redirect_chain.get(current)
        if nxt is None:
            return None
        current = nxt
    return None


def step3_apply_remaining_aliases(log, redirect_chain):
    alias_map, alias_sources = load_alias_maps()
    nodes, _ = load_all_nodes()
    existing_ids = set(nodes)
    updated = 0

    for node_id, data in nodes.items():
        changed = False
        for key in REF_KEYS:
            def transform(ref, _key=key):
                if ref in existing_ids:
                    return ref
                if ref not in alias_map:
                    return ref  # sigue roto; lo maneja el paso 4
                candidate = alias_map[ref]
                resolved = resolve_target(candidate, redirect_chain, existing_ids)
                if resolved is not None:
                    log["alias_redirects"].append({
                        "node": node_id, "key": _key, "from": ref,
                        "alias_target": candidate, "resolved_to": resolved,
                        "via": alias_sources.get(ref),
                    })
                    return resolved
                log["alias_unresolved_removed"].append({
                    "node": node_id, "key": _key, "ref": ref,
                    "alias_target": candidate, "via": alias_sources.get(ref),
                })
                return None

            if rewrite_refs(node_id, data, key, transform):
                changed = True
        if changed:
            save_node(node_id, data)
            updated += 1

    return updated


# ---------------------------------------------------------------------------
# Paso 4: Limpieza final de referencias rotas restantes
# ---------------------------------------------------------------------------

def step4_cleanup_remaining(log):
    nodes, _ = load_all_nodes()
    existing_ids = set(nodes)
    updated = 0

    for node_id, data in nodes.items():
        changed = False
        for key in REF_KEYS:
            def transform(ref, _key=key):
                if ref in existing_ids:
                    return ref
                log["final_cleanup_removed"].append(
                    {"node": node_id, "key": _key, "ref": ref}
                )
                return None

            if rewrite_refs(node_id, data, key, transform):
                changed = True
        if changed:
            save_node(node_id, data)
            updated += 1

    return updated


# ---------------------------------------------------------------------------
# Paso 5: Compilacion de master_graph.json
# ---------------------------------------------------------------------------

def compute_graph_stats(nodes):
    existing_ids = set(nodes)
    adjacency = collections.defaultdict(set)
    incoming = collections.Counter()

    for node_id, data in nodes.items():
        for key in REF_KEYS:
            for ref in data.get(key, []):
                if ref in existing_ids:
                    adjacency[node_id].add(ref)
                    adjacency[ref].add(node_id)
        for ref in data.get("nodos_siguientes", []):
            if ref in existing_ids:
                incoming[ref] += 1

    visited = set()
    components = []
    for node_id in existing_ids:
        if node_id in visited:
            continue
        stack = [node_id]
        visited.add(node_id)
        comp = []
        while stack:
            cur = stack.pop()
            comp.append(cur)
            for neigh in adjacency[cur]:
                if neigh not in visited:
                    visited.add(neigh)
                    stack.append(neigh)
        components.append(comp)

    components.sort(key=len, reverse=True)
    main_size = len(components[0]) if components else 0
    total = len(existing_ids)
    coverage_pct = round(main_size / total * 100, 2) if total else 0.0
    sin_entrantes = sum(1 for n in existing_ids if incoming[n] == 0)

    return {
        "componentes_conexos": len(components),
        "tamano_componente_principal": main_size,
        "cobertura_componente_principal_pct": coverage_pct,
        "nodos_sin_enlaces_entrantes": sin_entrantes,
    }


def step5_compile_master_graph():
    nodes, parse_errors = load_all_nodes()
    existing_ids = set(nodes)

    broken = 0
    for data in nodes.values():
        for key in REF_KEYS:
            for ref in data.get(key, []):
                if ref not in existing_ids:
                    broken += 1

    indice_por_fase = collections.defaultdict(list)
    for node_id, data in nodes.items():
        fase = data.get("fase_proyecto", "otra")
        indice_por_fase[fase].append(node_id)
    for fase in indice_por_fase:
        indice_por_fase[fase].sort()

    stats = compute_graph_stats(nodes)
    stats["enlaces_rotos_en_grafo"] = broken

    master = {
        "version": "0.2.0",
        "total_nodos": len(nodes),
        "nodos": dict(sorted(nodes.items())),
        "indice_por_fase": dict(sorted(indice_por_fase.items())),
        "stats": stats,
    }

    with open(MASTER_GRAPH_PATH, "w", encoding="utf-8") as fh:
        json.dump(master, fh, ensure_ascii=False, indent=2)

    return master, parse_errors


def find_exact_title_duplicates(nodes):
    """Grupos de nodos con titulo_concepto EXACTAMENTE igual (fallo duro).
    Tras la fusion semantica de Fase 1.6, cada concepto debe existir como un
    unico nodo: si dos ids distintos comparten titulo exacto, son fosiles
    (duplicados) que deberian haberse fusionado."""
    by_title = collections.defaultdict(list)
    for node_id, data in nodes.items():
        by_title[data.get("titulo_concepto")].append(node_id)
    return {title: sorted(ids) for title, ids in by_title.items() if len(ids) > 1}


def normalize_title(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower().strip()


def find_near_duplicate_titles(nodes, threshold=95):
    """Pares de nodos con titulo_concepto distinto pero muy similar
    (similitud >= threshold, excluyendo los ya exactos). Chequeo
    informativo: no falla el Gate 0, solo se reporta para revision manual
    futura (candidatos a una proxima ronda de fusion semantica)."""
    ids = sorted(nodes)
    titles = {nid: normalize_title(nodes[nid].get("titulo_concepto", "")) for nid in ids}
    pairs = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            ta, tb = titles[a], titles[b]
            if not ta or not tb or ta == tb:
                continue
            score = fuzz.ratio(ta, tb)
            if score >= threshold:
                pairs.append((a, b, round(score, 1)))
    pairs.sort(key=lambda p: -p[2])
    return pairs


# ---------------------------------------------------------------------------
# Paso 6: Validador Gate 0
# ---------------------------------------------------------------------------

def step6_validate(master, parse_errors):
    stats = master["stats"]
    checks = []

    checks.append((
        "Enlaces rotos en dataset == 0",
        stats["enlaces_rotos_en_grafo"] == 0,
        stats["enlaces_rotos_en_grafo"],
    ))

    non_ascii_files = [
        p.name for p in NODOS_DIR.glob("*.json")
        if not all(ord(c) < 128 for c in p.stem)
    ]
    checks.append((
        "Archivos con nombre no-ASCII == 0",
        len(non_ascii_files) == 0,
        len(non_ascii_files),
    ))

    files_on_disk = len(list(NODOS_DIR.glob("*.json")))
    checks.append((
        "Nodos en master_graph.json == archivos en disco",
        master["total_nodos"] == files_on_disk,
        f"{master['total_nodos']} vs {files_on_disk}",
    ))

    checks.append((
        "Componentes conexos <= 2",
        stats["componentes_conexos"] <= 2,
        stats["componentes_conexos"],
    ))

    checks.append((
        "Cobertura del componente principal >= 99%",
        stats["cobertura_componente_principal_pct"] >= 99.0,
        stats["cobertura_componente_principal_pct"],
    ))

    checks.append((
        "Todos los JSON parsean sin error",
        len(parse_errors) == 0,
        len(parse_errors),
    ))

    duplicate_titles = find_exact_title_duplicates(master["nodos"])
    checks.append((
        "Cero grupos con titulo_concepto exacto duplicado",
        len(duplicate_titles) == 0,
        duplicate_titles if duplicate_titles else 0,
    ))

    near_duplicates = find_near_duplicate_titles(master["nodos"], threshold=95)

    return checks, near_duplicates


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    log = {
        "ascii_renames": [],
        "ascii_rename_collisions": [],
        "merge_redirects": [],
        "alias_redirects": [],
        "alias_unresolved_removed": [],
        "final_cleanup_removed": [],
    }

    print("=== Paso 1: Normalizacion ASCII ===")
    rename_map = step1_ascii_normalize(log)
    print(f"  {len(rename_map)} archivo(s) renombrado(s).")
    if log["ascii_rename_collisions"]:
        print(f"  ATENCION: {len(log['ascii_rename_collisions'])} colision(es) de renombrado "
              f"detectada(s) (posibles duplicados, no renombrados). Ver log.")

    print("=== Paso 2: Redireccion de nodos fusionados ===")
    updated2, merge_redirect_map = step2_redirect_merged(log)
    print(f"  {updated2} nodo(s) actualizado(s).")

    print("=== Paso 3: Aliases restantes (capa B / capa C / auto) ===")
    redirect_chain = {**rename_map, **merge_redirect_map}
    updated3 = step3_apply_remaining_aliases(log, redirect_chain)
    print(f"  {updated3} nodo(s) actualizado(s).")

    print("=== Paso 4: Limpieza final de referencias rotas ===")
    updated4 = step4_cleanup_remaining(log)
    print(f"  {updated4} nodo(s) actualizado(s).")

    print("=== Paso 5: Compilacion de master_graph.json ===")
    master, parse_errors = step5_compile_master_graph()
    print(f"  {master['total_nodos']} nodos compilados.")

    with open(LOG_PATH, "w", encoding="utf-8") as fh:
        json.dump(log, fh, ensure_ascii=False, indent=2)
    print(f"  Log escrito en {LOG_PATH.relative_to(BASE)}")

    print("\n=== Paso 6: Validador Gate 0 ===")
    checks, near_duplicates = step6_validate(master, parse_errors)

    all_ok = True
    print("\n--- Resumen Gate 0 ---")
    for name, ok, value in checks:
        status = "OK" if ok else "FALLO"
        if not ok:
            all_ok = False
        print(f"  [{status}] {name} (valor: {value})")

    print("\n--- Estadisticas del grafo ---")
    print(json.dumps(master["stats"], ensure_ascii=False, indent=2))

    print(f"\n--- Warning informativo: pares de titulo con similitud >= 95 ({len(near_duplicates)}) ---")
    if near_duplicates:
        for a, b, score in near_duplicates:
            print(f"  [{score}] {a}  <->  {b}")
    else:
        print("  Ninguno.")

    if not all_ok:
        print("\nGATE 0: FALLIDO")
        sys.exit(1)

    print("\nGATE 0: OK")


if __name__ == "__main__":
    main()
