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
  5. Simetrizacion de enlaces: cada arista "X antes de Y" debe vivir en
     ambos extremos (Y en nodos_siguientes de X, X en nodos_previos de Y)
  6. Recompilacion de dataset/metadata/master_graph.json
  7. Validador Gate 0 (sys.exit(1) si algun chequeo falla), incluyendo
     simetria de enlaces y alcanzabilidad dirigida desde
     dataset/metadata/entry_seeds.json

Todas las rutas son relativas al repo (BASE = carpeta padre de scripts/).
No modifica contenido teorico de los nodos: solo nombres de archivo,
node_id, nodos_previos y nodos_siguientes.

Uso:
  python scripts/run_phase1.py
"""
import argparse
import collections
import json
import sys
import unicodedata
from pathlib import Path

from rapidfuzz import fuzz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from etiquetas_de_cara import LISTAS as LISTAS_CURADURIA  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
NODOS_DIR = BASE / "dataset" / "nodos"
METADATA_DIR = BASE / "dataset" / "metadata"
MASTER_GRAPH_PATH = METADATA_DIR / "master_graph.json"
LOG_PATH = METADATA_DIR / "phase1_run_log.json"
ENTRY_SEEDS_PATH = METADATA_DIR / "entry_seeds.json"

MIN_DIRECTED_REACHABILITY_PCT = 99.5

REF_KEYS = ("nodos_previos", "nodos_siguientes")

# Hotfix v2.1.1: groundwork de dominios (motor v2.1 solo tiene "core", pero
# el interruptor de filtrado por dominio queda instalado desde ya en
# ruteador/brujula/cosecha). Todo nodo DEBE declarar "dominio" con un valor
# de esta lista; agregar aqui cuando exista un dominio nuevo real.
# Fase 3.6: dominios ampliados — los packs P1-HSEQ integrados por
# scripts/integrar_packs.py viven en el mismo dataset con su dominio propio.
# Fase v1.3.2: tres mundos nuevos (seguridad_digital, exportacion, franquicias).
# Fase v1.4: septimo pack risk_management.
# Extraccion 2026-08-07: octavo y noveno, compras y entrega. Esta lista es la
# que hace fallar el Gate cuando alguien integra un pack y se olvida de
# registrarlo aqui: el grafo sale perfecto y el Gate dice FALLIDO sin mas
# pista que "dominio invalido". Es intencional: mejor un Gate rojo que un
# dominio fantasma paseandose por el dataset.
DOMINIOS_PERMITIDOS = {
    "core", "quality", "health_safety", "environmental",
    "seguridad_digital", "exportacion", "franquicias", "risk_management",
    "compras", "entrega",
}

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
# Paso 5: Simetrizacion de enlaces
#
# REGLA SEMANTICA: un enlace es UNA arista dirigida "conviene saber X antes
# de Y", almacenada siempre en AMBOS extremos: Y debe aparecer en
# nodos_siguientes de X, y X debe aparecer en nodos_previos de Y. Nunca una
# sola vista. Si falta una de las dos, se completa aqui; el contenido
# teorico no se toca, solo se agregan entradas a las listas existentes
# (nunca se reordenan ni eliminan las ya declaradas).
# ---------------------------------------------------------------------------

def step5_symmetrize(log):
    nodes, _ = load_all_nodes()
    existing_ids = set(nodes)

    # Union de "antes -> despues" visto desde cualquiera de los dos extremos
    edges = set()
    for node_id, data in nodes.items():
        for after in data.get("nodos_siguientes") or []:
            if after in existing_ids and after != node_id:
                edges.add((node_id, after))
        for before in data.get("nodos_previos") or []:
            if before in existing_ids and before != node_id:
                edges.add((before, node_id))

    succ_needed = collections.defaultdict(set)
    pred_needed = collections.defaultdict(set)
    for a, b in edges:
        succ_needed[a].add(b)
        pred_needed[b].add(a)

    added_siguientes = 0
    added_previos = 0
    updated = 0

    for node_id, data in nodes.items():
        changed = False

        original_sig = dedupe_and_remove_self(node_id, data.get("nodos_siguientes") or [])
        sig_set = set(original_sig)
        new_sig = list(original_sig)
        for target in sorted(succ_needed.get(node_id, ())):
            if target not in sig_set:
                new_sig.append(target)
                sig_set.add(target)
                added_siguientes += 1
                changed = True
                log["symmetrize_added"].append(
                    {"node": node_id, "key": "nodos_siguientes", "added": target}
                )

        original_prev = dedupe_and_remove_self(node_id, data.get("nodos_previos") or [])
        prev_set = set(original_prev)
        new_prev = list(original_prev)
        for source in sorted(pred_needed.get(node_id, ())):
            if source not in prev_set:
                new_prev.append(source)
                prev_set.add(source)
                added_previos += 1
                changed = True
                log["symmetrize_added"].append(
                    {"node": node_id, "key": "nodos_previos", "added": source}
                )

        if new_sig != (data.get("nodos_siguientes") or []):
            data["nodos_siguientes"] = new_sig
            changed = True
        if new_prev != (data.get("nodos_previos") or []):
            data["nodos_previos"] = new_prev
            changed = True

        if changed:
            save_node(node_id, data)
            updated += 1

    return updated, added_siguientes, added_previos


def count_asymmetric_edges(nodes):
    """Cuenta cuantas aristas siguen sin la vista reciproca completa."""
    existing_ids = set(nodes)
    missing_previo = 0
    missing_siguiente = 0
    for node_id, data in nodes.items():
        sig = set(data.get("nodos_siguientes") or [])
        prev = set(data.get("nodos_previos") or [])
        for after in sig:
            if after in existing_ids:
                other = nodes[after]
                if node_id not in (other.get("nodos_previos") or []):
                    missing_previo += 1
        for before in prev:
            if before in existing_ids:
                other = nodes[before]
                if node_id not in (other.get("nodos_siguientes") or []):
                    missing_siguiente += 1
    return missing_previo, missing_siguiente


def compute_directed_reachability(nodes, seed_ids):
    """BFS dirigido hacia adelante (nodos_siguientes) desde seed_ids.
    Devuelve (alcanzados, total, porcentaje)."""
    existing_ids = set(nodes)
    seeds = [s for s in seed_ids if s in existing_ids]
    visited = set(seeds)
    stack = list(seeds)
    while stack:
        cur = stack.pop()
        for nxt in nodes[cur].get("nodos_siguientes") or []:
            if nxt in existing_ids and nxt not in visited:
                visited.add(nxt)
                stack.append(nxt)
    total = len(existing_ids)
    pct = round(len(visited) / total * 100, 2) if total else 0.0
    return len(visited), total, pct


# ---------------------------------------------------------------------------
# Paso 6: Compilacion de master_graph.json
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


def step6_compile_master_graph():
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

    indice_por_dominio = collections.defaultdict(list)
    for node_id, data in nodes.items():
        dominio = data.get("dominio", "sin_dominio")
        indice_por_dominio[dominio].append(node_id)
    for dominio in indice_por_dominio:
        indice_por_dominio[dominio].sort()

    stats = compute_graph_stats(nodes)
    stats["enlaces_rotos_en_grafo"] = broken

    master = {
        "version": "0.2.0",
        "total_nodos": len(nodes),
        "nodos": dict(sorted(nodes.items())),
        "indice_por_fase": dict(sorted(indice_por_fase.items())),
        "indice_por_dominio": dict(sorted(indice_por_dominio.items())),
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
# Paso 7: Validador Gate 0
# ---------------------------------------------------------------------------

def load_entry_seeds():
    if not ENTRY_SEEDS_PATH.exists():
        return []
    seeds = list(load_json(ENTRY_SEEDS_PATH).get("seeds", []))
    # Fase 3.6: los mundos integrados se entran por sus propias semillas
    # (packs/<dominio>/metadata/entry_seeds.json, rutas unlock/start), no por
    # las 20 puertas core del motor. Para el chequeo de alcanzabilidad el
    # universo tiene todas las puertas; el archivo del motor NO se toca.
    for pack_seeds in sorted(BASE.glob("packs/*/metadata/entry_seeds.json")):
        for seed in load_json(pack_seeds):
            if seed not in seeds and (NODOS_DIR / f"{seed}.json").exists():
                seeds.append(seed)
    return seeds


def step7_validate(master, parse_errors):
    stats = master["stats"]
    checks = []

    checks.append((
        "Enlaces rotos en dataset == 0",
        stats["enlaces_rotos_en_grafo"] == 0,
        stats["enlaces_rotos_en_grafo"],
    ))

    nodos_dominio_invalido = [
        node_id for node_id, data in master["nodos"].items()
        if data.get("dominio") not in DOMINIOS_PERMITIDOS
    ]
    checks.append((
        f"Todos los nodos tienen dominio valido ({sorted(DOMINIOS_PERMITIDOS)})",
        len(nodos_dominio_invalido) == 0,
        len(nodos_dominio_invalido) if nodos_dominio_invalido else 0,
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

    missing_previo, missing_siguiente = count_asymmetric_edges(master["nodos"])
    total_asymmetric = missing_previo + missing_siguiente
    checks.append((
        "Cero aristas con vista reciproca faltante (simetria)",
        total_asymmetric == 0,
        f"{total_asymmetric} (sin previo reciproco: {missing_previo}, sin siguiente reciproco: {missing_siguiente})",
    ))

    # --- El Gate aprende `deprecado` (cirugia de Calidad, ago 2026) ---------
    # Un deprecado sigue EN el grafo, con sus aristas intactas: el grafo
    # historico queda integro. Lo que pierde es la elegibilidad. Asi que:
    #   * no se le exige alcance (no es alcanzable por definicion: nadie lo
    #     ofrece), y por eso el porcentaje se mide sobre el universo ACTIVO;
    #   * no cuenta como huerfano;
    #   * pero NO puede ser semilla ni destino de un puente activo, porque eso
    #     seria una puerta que abre a un nodo que ya no se ofrece.
    nodos_todos = master["nodos"]
    deprecados = {k for k, n in nodos_todos.items() if n.get("deprecado")}
    activos = {k: v for k, v in nodos_todos.items() if k not in deprecados}
    checks.append((
        "Universo: activos / deprecados",
        True,
        f"{len(activos)} activos, {len(deprecados)} deprecados (siguen en el grafo)",
    ))

    # EL NODO FANTASMA CON NOMBRE, cero tolerancia (adoptado ago 2026 tras la
    # deprecacion de los programas de OSHA). Un nodo ACTIVO cuya UNICA entrada
    # esta deprecada sigue existiendo, con su titulo y su contenido, y NADIE
    # puede llegar a el por ningun camino. No es un huerfano historico: es una
    # baja causada por una deprecacion, y el efecto es DOMINO (al cerrar una
    # puerta se llevo por delante a tres nodos universales que estaban detras).
    #
    # Va aparte del porcentaje de alcanzabilidad a proposito: ese umbral existe
    # para el flotante historico y con 99.5% este caso PASABA. Aqui no se
    # tolera ni uno.
    fantasmas = []
    for nid, n in activos.items():
        entradas = [r for r in (n.get("nodos_previos") or []) if r in nodos_todos]
        if entradas and all(r in deprecados for r in entradas):
            fantasmas.append(nid)
    checks.append((
        "Ningun nodo ACTIVO cuya unica entrada este deprecada",
        not fantasmas,
        f"{len(fantasmas)} fantasmas" + (f": {fantasmas[:5]}" if fantasmas else ""),
    ))

    # ── TODO ACTIVO TIENE VECTOR EN EL INDICE SEMANTICO ─────────────────────
    #
    # LA CLASE QUE CIERRA (ago 2026): al revivir diez nodos deprecados de
    # seleccion, los diez EXISTIAN en el grafo, pasaban todos los chequeos, y la
    # brujula era INCAPAZ de encontrarlos: el indice se habia construido cuando
    # estaban deprecados, y build_semantic_index los excluye a proposito.
    #
    # No es un caso, es una clase: CUALQUIER cambio de estado de deprecado la
    # reproduce, y tambien la reproduce un nodo nuevo sin reindexar. Un nodo
    # ofrecible que el indice no conoce es invisible para el salto semantico y
    # para la prueba de rumbos, y ninguna de las dos se queja: simplemente no lo
    # devuelven nunca. Cero tolerancia.
    ruta_indice = BASE / "web" / "lib" / "assets" / "semantic_index.json"
    if ruta_indice.exists():
        con_vector = set(json.loads(ruta_indice.read_text(encoding="utf-8"))["ids"])
        sin_vector = sorted(set(activos) - con_vector)
        sobran = sorted(con_vector - set(activos))
        detalle = f"{len(sin_vector)} activos sin vector"
        if sin_vector:
            detalle += (f": {sin_vector[:5]} -> corre el reindex ANTES de usar esta copia: "
                        "python scripts/build_semantic_index_voyage.py && "
                        "python scripts/sync_assets_web.py")
        if sobran:
            detalle += f" | {len(sobran)} vectores de nodos que ya no son ofrecibles"
        checks.append(("Todo nodo ACTIVO tiene vector en el indice semantico",
                       not sin_vector, detalle))

    seeds = load_entry_seeds()
    seeds_deprecadas = sorted(set(seeds) & deprecados)
    checks.append((
        "Ninguna semilla de entrada esta deprecada",
        not seeds_deprecadas,
        f"{len(seeds_deprecadas)} deprecadas" + (f": {seeds_deprecadas[:5]}" if seeds_deprecadas else ""),
    ))

    # La otra mitad del requisito: ningun deprecado puede ser DESTINO de un
    # puente aprobado. Un puente es una puerta del core hacia un mundo; si su
    # destino ya no se ofrece, es una puerta que no abre. Cazado a mano en la
    # cirugia de Calidad (un puente apuntaba a medir_progreso_kpi tras
    # deprecarse), que es justo lo que este chequeo evita repetir.
    puentes_muertos = []
    for ruta_b in sorted(BASE.glob("packs/*/metadata/bridges_aprobados.json")):
        try:
            with open(ruta_b, encoding="utf-8") as fh:
                for x in json.load(fh).get("aprobados", []):
                    for extremo in ("core", "dominio"):
                        if x.get(extremo) in deprecados:
                            puentes_muertos.append(f"{ruta_b.parent.parent.name}:{x[extremo]}")
        except (OSError, json.JSONDecodeError):
            continue
    checks.append((
        "Ningun puente aprobado apunta a un nodo deprecado",
        not puentes_muertos,
        f"{len(puentes_muertos)} rotos" + (f": {puentes_muertos[:5]}" if puentes_muertos else ""),
    ))

    # La alcanzabilidad se mide sobre el universo ACTIVO: exigirsela a un
    # deprecado seria pedirle que sea alcanzable justo despues de sacarlo de
    # todos los caminos de oferta.
    seeds_vivas = [s for s in seeds if s not in deprecados]
    reached, total, pct = compute_directed_reachability(activos, seeds_vivas)
    checks.append((
        f"Alcanzabilidad dirigida >= {MIN_DIRECTED_REACHABILITY_PCT}% desde entry_seeds.json",
        bool(seeds_vivas) and pct >= MIN_DIRECTED_REACHABILITY_PCT,
        f"{pct}% ({reached}/{total} activos, semillas validas: {len(seeds_vivas)})",
    ))

    near_duplicates = find_near_duplicate_titles(master["nodos"], threshold=95)

    return checks, near_duplicates


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# EL AVISO DE LA CURADURIA REVERTIDA
#
# Este script recompila master_graph.json desde dataset/nodos/, y la curaduria
# de etiquetas de cara NO vive en los nodos: vive en dataset/metadata/
# etiquetas_de_cara_v1*.json y se aplica sobre las dos COPIAS del grafo. O sea,
# cada recompilacion la borra. Cazado el 2026-08-07 integrando compras y
# entrega: 71 etiquetas del core volvieron a su titulo de libro ("Canvas",
# "Pivotar", "SPIN", "DMAIC") y el grafo seguia siendo valido, asi que nada se
# quejo. Es la clase mas peligrosa de averia: degrada la VOZ sin romper la
# estructura, y el Gate solo mira la estructura.
#
# Aqui SOLO se avisa y se falla. Jamas se auto-aplica: eso creaeria una segunda
# fuente de curaduria, y el remache del e-bis de integrar_packs la prohibe.
# Quien recompila, reaplica.
#
# La lista de listas se IMPORTA de etiquetas_de_cara, que es quien la define.
# ---------------------------------------------------------------------------
def etiquetas_curadas():
    """El mapa node_id -> etiqueta que la curaduria manda. La ultima lista gana."""
    curadas = {}
    for ruta in LISTAS_CURADURIA:
        with open(ruta, encoding="utf-8") as fh:
            curadas.update({k: v for k, v in json.load(fh).items() if not k.startswith("_")})
    return curadas


def curaduria_revertida(nodos):
    """Los node_id cuya etiqueta en el grafo NO es la curada. Vacio = intacta."""
    return sorted(
        nid for nid, esperada in etiquetas_curadas().items()
        if nid in nodos and nodos[nid].get("etiqueta_arbol") != esperada
    )


def avisar_curaduria(nodos, reaplico):
    """Grita y devuelve el codigo de salida. 0 = nada que decir."""
    revertidas = curaduria_revertida(nodos)
    if not revertidas or reaplico:
        return 0
    rojo, fin = "\033[1;31m", "\033[0m"
    print(f"\n{rojo}{'=' * 70}")
    print("REVERTISTE LA CURADURIA DE ETIQUETAS")
    print(f"{'=' * 70}{fin}")
    print(f"  {len(revertidas)} etiquetas volvieron al titulo del libro al recompilar.")
    for nid in revertidas[:8]:
        print(f"    {nid}: '{nodos[nid].get('etiqueta_arbol')}'")
    if len(revertidas) > 8:
        print(f"    ... y {len(revertidas) - 8} mas")
    print(f"\n  {rojo}Corre esto antes de usar esta copia:{fin}")
    print("    python scripts/etiquetas_de_cara.py --aplicar")
    print("\n  (Si vienes de integrar_packs, su paso e-bis ya lo hace; ese flujo")
    print("   pasa --reaplico-curaduria para que este aviso no lo pare.)")
    return 2


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--reaplico-curaduria", action="store_true",
        help="quien llama reaplica las etiquetas justo despues (lo usa integrar_packs)")
    args = ap.parse_args()
    log = {
        "ascii_renames": [],
        "ascii_rename_collisions": [],
        "merge_redirects": [],
        "alias_redirects": [],
        "alias_unresolved_removed": [],
        "final_cleanup_removed": [],
        "symmetrize_added": [],
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

    print("=== Paso 5: Simetrizacion de enlaces ===")
    updated5, added_sig, added_prev = step5_symmetrize(log)
    print(f"  {updated5} nodo(s) actualizado(s). Vistas completadas: "
          f"{added_sig} en nodos_siguientes, {added_prev} en nodos_previos.")

    print("=== Paso 6: Compilacion de master_graph.json ===")
    master, parse_errors = step6_compile_master_graph()
    print(f"  {master['total_nodos']} nodos compilados.")

    with open(LOG_PATH, "w", encoding="utf-8") as fh:
        json.dump(log, fh, ensure_ascii=False, indent=2)
    print(f"  Log escrito en {LOG_PATH.relative_to(BASE)}")

    print("\n=== Paso 7: Validador Gate 0 ===")
    checks, near_duplicates = step7_validate(master, parse_errors)

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

    # El Gate mira la ESTRUCTURA; esto mira la VOZ. Va despues del OK a
    # proposito: un grafo puede estar impecable y sonar a manual otra vez.
    sys.exit(avisar_curaduria(master["nodos"], args.reaplico_curaduria))


if __name__ == "__main__":
    main()
