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
#
# EL DEPRECADO ES ARCHIVO, TAMBIEN EN EL RECIPROCADO (decision del fundador,
# 15 ago 2026, opcion a de docs/loop/paradas/2026-08-15-cableado-deprecado-y
# -costuras.md). LA AVERIA QUE ESTO CIERRA, medida en la vuelta 33: una fusion
# depreca al absorbido CONSERVANDO su cableado (eso es lo que la hace
# auditable) y redirige a los vivos que lo nombraban. Acto seguido, este paso
# leia las listas del absorbido, veia aristas "sin la vista reciproca" y
# DEVOLVIA el id del muerto a los tres vivos de los que se acababa de quitar:
# la redireccion de toda fusion duraba hasta la siguiente corrida del Gate.
# Desde hoy, una arista cuya UNICA declaracion vive en un nodo deprecado no se
# reciproca: el deprecado conserva su cableado tal cual, y no se lo escribe a
# nadie.
# ---------------------------------------------------------------------------

def aristas_a_simetrizar(nodes):
    """Las aristas que este paso completa y que el Gate exige simetricas.

    Una arista entra si LA DECLARA UN NODO VIVO, en cualquiera de sus dos
    vistas. Las que solo viven en las listas de un deprecado quedan fuera.

    LA LECTURA ES POR DECLARACION, NO POR ORIGEN TOPOLOGICO, y la diferencia
    importa: si se leyera por el extremo "antes", una arista declarada por un
    vivo hacia un deprecado seguiria escribiendo el id del muerto dentro del
    vivo, que es exactamente el sintoma que la decision manda cerrar.

    Funcion PURA a proposito, como las tres barandas del alias: recibe el
    diccionario de nodos y devuelve el conjunto, para que los fixtures la
    prueben con grafos sinteticos sin recompilar nada
    (engine/test_gate_deprecado_reciproco.py).
    """
    existing_ids = set(nodes)
    edges = set()
    for node_id, data in nodes.items():
        if data.get("deprecado"):
            continue
        for after in data.get("nodos_siguientes") or []:
            if after in existing_ids and after != node_id:
                edges.add((node_id, after))
        for before in data.get("nodos_previos") or []:
            if before in existing_ids and before != node_id:
                edges.add((before, node_id))
    return edges


def step5_symmetrize(log):
    nodes, _ = load_all_nodes()

    # Union de "antes -> despues" visto desde cualquiera de los dos extremos,
    # DECLARADA POR UN VIVO (ver el recuadro de arriba).
    edges = aristas_a_simetrizar(nodes)

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
    """Cuenta cuantas aristas siguen sin la vista reciproca completa.

    MIDE EXACTAMENTE EL MISMO CONJUNTO QUE `aristas_a_simetrizar` COMPLETA, y
    eso no es una comodidad: un Gate que exigiera simetria en aristas que el
    paso 5 ya no simetriza se pondria rojo por su propia politica, y la salida
    barata seria aflojar la comprobacion. Las dos leen la misma funcion.

    Lo que el chequeo deja de exigir queda dicho para que nadie lo descubra
    tarde: las aristas cuya UNICA declaracion vive en un nodo deprecado. Esas
    se conservan como estan (archivo), simetricas o no.
    """
    edges = aristas_a_simetrizar(nodes)
    missing_previo = 0
    missing_siguiente = 0
    for antes, despues in edges:
        if antes not in (nodes[despues].get("nodos_previos") or []):
            missing_previo += 1
        if despues not in (nodes[antes].get("nodos_siguientes") or []):
            missing_siguiente += 1
    return missing_previo, missing_siguiente


# ---------------------------------------------------------------------------
# LAS TRES BARANDAS DEL ALIAS (cirugia de metadata, ago 2026)
#
# El alias es la promesa de la historia: un id viejo tiene que llevar al nodo
# que hoy lo representa. Se limpiaron ocho auto-alias y un alias con dos
# duenos, y el Gate no los veia. Ahora si.
#
# Se dejan como funciones PURAS a proposito: reciben el diccionario de nodos y
# devuelven las violaciones, para que los fixtures las prueben con grafos
# sinteticos sin recompilar nada.
# ---------------------------------------------------------------------------

def alias_auto(nodos):
    """Nodos que llevan su PROPIO id dentro de su ids_alias.

    No es cosmetico. `mapaDeAlias` en graph.ts lo filtra, y por eso nadie se
    colgaba, pero un auto-alias es una entrada x -> x que cualquier caminador
    sin guarda convierte en bucle, y ademas compite por el mismo alias con el
    dueno legitimo (ver `alias_con_dos_duenos`).
    """
    return sorted(nid for nid, n in nodos.items() if nid in (n.get("ids_alias") or []))


def alias_con_dos_duenos(nodos):
    """alias -> los nodos que lo reclaman, cuando son mas de uno.

    LA AVERIA QUE ESTO EVITA es silenciosa: el mapa se construye recorriendo
    los nodos y el ULTIMO en escribir gana, asi que la resolucion depende del
    ORDEN de serializacion del grafo. Cazado con `jerarquia_controles`, que
    ganaba el dueno correcto por estar en el indice 2877 contra el 2217 del
    otro. Un dato que esta bien de suerte es un dato que esta mal.
    """
    duenos = collections.defaultdict(list)
    for nid, n in nodos.items():
        for a in n.get("ids_alias") or []:
            duenos[a].append(nid)
    return {a: sorted(d) for a, d in sorted(duenos.items()) if len(d) > 1}


def gemelos_divergentes(nodos_dataset, nodos_web):
    """node_id -> que difiere entre las dos copias del grafo.

    POR QUE ESTE CHEQUEO EXISTE: 71 `etiqueta_arbol` vivieron divergentes entre
    dataset/metadata/master_graph.json y web/lib/assets/master_graph.json
    durante toda una serie de commits. La web servia la forma curada y el
    dataset la vieja, y NINGUN guardian comparaba los dos artefactos: cada uno
    era valido por su cuenta. Es la regla de transito fotografiada, dos gemelos
    y nadie que los mirara juntos.

    Se comparan CAMPOS, no bytes: el orden de las claves y el formato son cosa
    del serializador y no dicen nada.
    """
    dif = {}
    for nid in sorted(set(nodos_dataset) | set(nodos_web)):
        a, b = nodos_dataset.get(nid), nodos_web.get(nid)
        if a is None or b is None:
            dif[nid] = "solo en " + ("dataset" if b is None else "web")
            continue
        campos = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
        if campos:
            dif[nid] = ",".join(campos)
    return dif


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


INDICE_ROJO_DECLARADO_PATH = BASE / "docs" / "plan" / "INDICE_ROJO_DECLARADO.jsonl"


def indice_rojo_declarado():
    """Los ids que una operacion de la FASE III declaro al crearlos, {id: (operacion, fecha)}.

    Decision del fundador, 14 ago 2026: la opcion B extendida. SOLO las
    operaciones de la pasada escriben aqui, una linea por id, al crear un
    nodo. El chequeo del indice semantico (aqui y en
    engine/test_aviso_curaduria.py) resta EXACTAMENTE estos ids de los
    activos sin vector: cualquier OTRO id sin vector sigue siendo rojo que
    para. Al cierre de la FASE III esta lista tiene que quedar VACIA, con
    el reindexado hecho y Gate 0 entero en verde (docs/plan/08_VERIFICACION.md)."""
    if not INDICE_ROJO_DECLARADO_PATH.exists():
        return {}
    declarados = {}
    with open(INDICE_ROJO_DECLARADO_PATH, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            entrada = json.loads(linea)
            declarados[entrada["id"]] = (entrada["operacion"], entrada["fecha"])
    return declarados


def step7_validate(master, parse_errors, nodos_dataset_al_empezar=None):
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
    # EL CHEQUEO SE AGREGA SIEMPRE, PASE O FALLE. La primera version lo envolvia
    # en `if ruta_indice.exists()`, y sin el archivo el chequeo NO ENTRABA en la
    # lista: el Gate salia verde sin el. Es la misma trampa silenciosa en su
    # forma extrema, porque sin indice no hay diez nodos invisibles, hay 3.521.
    #
    #   "Un chequeo AUSENTE y un chequeo VERDE se ven igual en el resumen."
    #
    # Y esa es justamente la enfermedad que este chequeo vino a curar, asi que no
    # podia padecerla.
    REMEDIO = ("corre el reindex ANTES de usar esta copia: "
               "python scripts/build_semantic_index_voyage.py && "
               "python scripts/sync_assets_web.py")
    ruta_indice = BASE / "web" / "lib" / "assets" / "semantic_index.json"
    if not ruta_indice.exists():
        checks.append(("Todo nodo ACTIVO tiene vector en el indice semantico", False,
                       f"NO HAY INDICE en {ruta_indice}: los {len(activos)} activos estan "
                       f"sin vector -> {REMEDIO}"))
    else:
        con_vector = set(json.loads(ruta_indice.read_text(encoding="utf-8"))["ids"])
        faltan_vector = sorted(set(activos) - con_vector)
        rojo_declarado = indice_rojo_declarado()
        declarados = [nid for nid in faltan_vector if nid in rojo_declarado]
        sin_vector = [nid for nid in faltan_vector if nid not in rojo_declarado]
        sobran = sorted(con_vector - set(activos))
        detalle = f"{len(sin_vector)} activos sin vector"
        if sin_vector:
            detalle += f": {sin_vector[:5]} -> {REMEDIO}"
        if sobran:
            detalle += f" | {len(sobran)} vectores de nodos que ya no son ofrecibles"
        if declarados:
            detalle += (f" | {len(declarados)} ROJO DECLARADO "
                        f"({INDICE_ROJO_DECLARADO_PATH.relative_to(BASE)}):")
            for nid in declarados:
                operacion, fecha = rojo_declarado[nid]
                detalle += f"\n      {nid} ({operacion}, {fecha})"
        checks.append(("Todo nodo ACTIVO tiene vector en el indice semantico",
                       not sin_vector, detalle))

    # ── LAS TRES BARANDAS DEL ALIAS ─────────────────────────────────────────
    auto = alias_auto(nodos_todos)
    checks.append((
        "Ningun nodo lleva su propio id en su ids_alias (auto-alias)",
        not auto,
        f"{len(auto)} auto-alias" + (f": {auto[:5]}" if auto else ""),
    ))

    dos = alias_con_dos_duenos(nodos_todos)
    checks.append((
        "Ningun alias es reclamado por dos nodos distintos",
        not dos,
        f"{len(dos)} con dos duenos" + (
            f": {[f'{a} <- {d}' for a, d in list(dos.items())[:3]]}" if dos else ""),
    ))

    # Los dos artefactos del grafo tienen que decir lo MISMO. Ver la nota larga
    # de `gemelos_divergentes`: la divergencia de 71 etiquetas vivio meses
    # porque cada copia era valida por separado.
    # EL ORDEN DEL REMEDIO IMPORTA Y POR ESO VA ESCRITO. Recompilar borra la
    # curaduria de etiquetas (vive en dataset/metadata/, no en los nodos), asi
    # que tras un recompile la copia ATRASADA es la del dataset. Sincronizar a
    # secas empujaria esa copia vieja sobre la buena de la web: el remedio
    # arreglaria el sintoma y estropearia la voz. Primero se reaplica, despues
    # se sincroniza.
    REMEDIO_SYNC = ("ANTES de usar esta copia, EN ESTE ORDEN: "
                    "python scripts/etiquetas_de_cara.py --aplicar && "
                    "python scripts/sync_assets_web.py")
    #
    # SE COMPARA EL SNAPSHOT DE ANTES DEL PASO 6, no el recien compilado. Es la
    # unica forma de que el chequeo signifique algo: el paso 6 recompila desde
    # los nodos y por diseno NO reaplica la curaduria, asi que comparar el
    # intermedio pondria el Gate en rojo SIEMPRE, y un chequeo que siempre
    # grita se acaba desactivando. La pregunta honesta es la que vivio en HEAD:
    # los dos artefactos que se sirven, tal como estaban, ¿decian lo mismo?
    ruta_web = BASE / "web" / "lib" / "assets" / "master_graph.json"
    if nodos_dataset_al_empezar is None:
        checks.append(("Los dos master_graph (dataset y web) dicen lo mismo", True,
                       "sin snapshot: el chequeo no aplica en esta invocacion"))
    elif not ruta_web.exists():
        checks.append(("Los dos master_graph (dataset y web) dicen lo mismo", False,
                       f"NO EXISTE {ruta_web} -> {REMEDIO_SYNC}"))
    else:
        nodos_web = load_json(ruta_web)["nodos"]
        gemelos = gemelos_divergentes(nodos_dataset_al_empezar, nodos_web)
        detalle = f"{len(gemelos)} nodos divergentes"
        if gemelos:
            muestra = [f"{k} ({v})" for k, v in list(gemelos.items())[:3]]
            detalle += f": {muestra} -> {REMEDIO_SYNC}"
            # EL FALSO ROJO SE DELATA SOLO (TAREA 5 de la vuelta 150). El
            # REMEDIO_SYNC de arriba dice QUE correr; esto dice ademas SI el rojo
            # es de verdad o es el ciclo a medias, y CUAL de los dos comandos
            # falta. No afloja el check: `not gemelos` sigue siendo la condicion.
            sys.path.insert(0, str(BASE / "scripts" / "loop"))
            from diagnostico_ciclo_a_medias import diagnosticar
            detalle += diagnosticar(gemelos, nodos_dataset_al_empezar, nodos_web)
        checks.append(("Los dos master_graph (dataset y web) dicen lo mismo",
                       not gemelos, detalle))

    # ── OP-C-04: LAS DOS GUARDAS DE LA FASE 0 ───────────────────────────────
    # Son las que hacen PERMANENTES a OP-S-07 y a OP-S-06. Sin ellas, las dos
    # limpiezas duran hasta la proxima integracion.
    #
    # 1) AUTO ARISTA **CON RESOLUCION**, y la resolucion no es un detalle: es
    #    toda la guarda. Un chequeo LITERAL (id == id) daba CERO sobre el grafo
    #    que tenia VEINTISIETE nodos citandose a si mismos, porque ninguna de
    #    las 33 aristas era directa: el nodo no se citaba por su id, citaba un
    #    id que era su propio alias. Una guarda asi pasa verde el dia de la
    #    reparacion y sigue pasando verde si manana vuelve a entrar una.
    #    "ES UNA GUARDA QUE NO GUARDA" (nota de OP-S-07).
    #
    #    MIDE SOBRE VIVOS, y los deprecados quedan FUERA, con motivo escrito
    #    (correccion declarada del 14 ago 2026, decision del fundador, camino A):
    #    un nodo deprecado es REGISTRO HISTORICO, no superficie del producto, y
    #    exigirle la misma guarda que a un vivo no protege a ningun usuario. Su
    #    censo (81 enlaces en 59 nodos deprecados, particionados en 33 reciprocas
    #    literales mas 48 alias contra alias inertes) vive en la nota de OP-S-07,
    #    no aqui.
    alias_de = {}
    for _nid, _n in nodos_todos.items():
        for _a in _n.get("ids_alias") or []:
            if _a != _nid:
                alias_de[_a] = _nid

    def _resolver(nid):
        """Copia fiel de resolverId (web/lib/engine/graph.ts). Las dos
        resoluciones tienen que decir lo mismo o la guarda vigila otro grafo."""
        n = nodos_todos.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid
        visto = {nid}
        cur = nid
        ultimo_real = nid if n is not None else None
        while cur in alias_de:
            cur = alias_de[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = nodos_todos.get(cur)
            if c is None:
                continue
            ultimo_real = cur
            if not c.get("deprecado"):
                return cur
        return ultimo_real

    auto_aristas = []
    for nid, n in activos.items():
        for campo in ("nodos_previos", "nodos_siguientes"):
            for dest in n.get(campo) or []:
                if dest in nodos_todos and _resolver(dest) == nid:
                    auto_aristas.append(f"{nid}.{campo} -> {dest}")
    checks.append((
        "Ningun nodo VIVO se cita a si mismo tras RESOLVER (auto-arista via alias)",
        not auto_aristas,
        f"{len(auto_aristas)} auto-aristas" + (
            f": {auto_aristas[:5]}" if auto_aristas else ""),
    ))

    # 2) LISTA BLANCA DE CLAVES DEL NODO. Es lo que impide que vuelva
    #    `fase_проekto`, la clave con п, р y о CIRILICAS que convivia con un
    #    `fase_proyecto` correcto en el mismo nodo: dos strings que se ven
    #    IDENTICOS en pantalla, la averia mas dificil de diagnosticar que existe.
    #
    #    LA LISTA NO SE REESCRIBE AQUI: se importa de scripts/expansion/
    #    validar_esquema.py, que ya la tiene con su adjudicacion de
    #    `merged_originals` argumentada dentro. Dos listas blancas divergentes
    #    serian exactamente el defecto de los dos master_graph que el chequeo de
    #    gemelos de mas arriba vino a curar.
    sys.path.insert(0, str(BASE / "scripts" / "expansion"))
    from validar_esquema import CAMPOS_PERMITIDOS

    claves_renegadas = []
    for path in sorted(NODOS_DIR.glob("*.json")):
        try:
            datos = load_json(path)
        except json.JSONDecodeError:
            continue  # ya lo reporta el chequeo de parseo
        for clave in sorted(set(datos) - CAMPOS_PERMITIDOS):
            claves_renegadas.append(
                f"{path.stem}.{clave.encode('unicode_escape').decode('ascii')}")
    checks.append((
        "Ninguna clave de nodo fuera de la lista blanca del esquema",
        not claves_renegadas,
        f"{len(claves_renegadas)} renegadas" + (
            f": {claves_renegadas[:5]}" if claves_renegadas else ""),
    ))

    # ── OP-C-05 (FASE 0): DOS ENTRADAS QUE RESUELVEN AL MISMO DESTINO ────
    # Es la guarda que hace PERMANENTE a OP-S-12, igual que las dos de arriba
    # hacen permanentes a OP-S-06 y a OP-S-07. Su nota lo dice con esas
    # palabras: "una limpieza sin guarda se deshace sola". OP-S-12 retiro 925
    # entradas duplicadas sobre nodos vivos en la vuelta 148 (commit a34328b2)
    # y hasta hoy no habia nadie defendiendolas: la proxima fusion volvia a
    # dejar una por acto, que es el mecanismo que la propia ficha de OP-S-12
    # describe ("la cola larga de a una confirma el mecanismo: cada fusion deja
    # una").
    #
    # SE ENCIENDE AHORA Y NO ANTES, con la letra de su ficha: "SE ENCIENDE
    # DESPUES DEL SANEO FINAL: encenderla antes para el trabajo, porque el
    # grafo de hoy la falla 1.056 veces y eso NO es una regresion, es el estado
    # conocido". Su depende_de es ['OP-S-12'] y se cumplio en la vuelta 148.
    #
    # RESUELVE, NO COMPARA LITERAL, y la resolucion es toda la guarda: las
    # entradas duplicadas son todas DISTINTAS COMO TEXTO (el id nuevo mas su
    # alias), asi que un chequeo literal daba VERDE sobre las 925. Medido en la
    # vuelta 150 con instrumento propio (scripts/loop/vuelta150_medir_opc05.py)
    # sobre el arbol de a34328b2~1, o sea el grafo de justo ANTES de OP-S-12:
    # el conteo literal de vuelta83_conteo_aristas.py dice
    # `nodos_con_dup_en_lista 0` y esta guarda, resolviendo, dice 925 entradas
    # que sobran en 888 grupos de 702 nodos. Cero contra 925 es la diferencia
    # entre una guarda que guarda y una que no.
    #
    # POR CAMPO Y POR SEPARADO, que es el CASO DE BORDE de su verificacion:
    # "el mismo destino en nodos_previos y en nodos_siguientes NO debe fallar",
    # porque eso no es una duplicada sino ida y vuelta. Por eso el diccionario
    # se vacia en cada `campo` y nunca se cruzan las dos listas: hoy hay 307
    # nodos vivos con un destino en las dos listas y ninguno es un fallo.
    #
    # CORRECCION DECLARADA (2026-09-02, vuelta 152, TAREA 4; hallazgo del acta
    # 151, caida 4.4. LA FRASE DE ARRIBA NO SE BORRA: esta se anade debajo).
    # LA UNIDAD DE ESA CIFRA ESTABA MAL. El 307 es correcto, pero NO cuenta
    # nodos: cuenta DESTINOS. Re medido en la vuelta 152 con instrumento propio
    # (scripts/loop/_v152_tarea4_correccion_307.py, salida en
    # docs/loop/SALIDA_V152_T4_CORRECCION_307.txt): son 307 DESTINOS repartidos
    # sobre 255 NODOS VIVOS. Un nodo puede traer mas de un destino en las dos
    # listas a la vez, y por eso los dos cardinales no coinciden.
    #
    # Y VA CON SU REGLA AL LADO, porque esta cifra vive DENTRO del codigo de una
    # guarda de Gate 0 y hasta hoy eso no tenia casillero: por la DECISION DEL
    # FUNDADOR del 2 sep 2026 (PREGUNTA 2, en
    # docs/loop/paradas/2026-09-02-opc05-bidireccionales-DECISION.md), una cifra
    # falsa en el codigo o el docstring de una guarda de scripts/ CUENTA COMO
    # CIFRA PUBLICADA desde esa fecha, SIN RETROACTIVIDAD. Esta, por ser
    # anterior, se corrige por declaracion y NO ACUMULA.
    #
    # MIDE SOBRE VIVOS, y los deprecados quedan fuera. NO ES UNA DECISION
    # NUEVA: es el criterio ya escrito y adjudicado para OP-C-04 el 14 ago 2026
    # (decision del fundador, camino A), que la propia ficha de OP-C-05 cita
    # como su patron ("OP-C-04, el mismo patron ya adoptado para las
    # auto-aristas via alias"), y es tambien el universo sobre el que OP-S-12
    # midio y opero (3.521 vivos al 11 ago 2026). Un nodo deprecado es registro
    # historico, no superficie del producto. Su censo, medido en la vuelta 150:
    # 330 entradas que sobran contando vivos y deprecados juntos, o sea 330
    # sobre deprecados, y quedan declaradas aqui en vez de calladas.
    #
    # LO QUE ESTA GUARDA NO CUBRE, DICHO EN VOZ ALTA. La ficha de OP-C-05 trae
    # una SEGUNDA mitad, la LISTA BLANCA: "la guarda falla ante cualquier
    # arista bidireccional SALVO las de la lista blanca", con dos entradas (los
    # dos enlaces mutuos de OP-E-05, por LD-41 y LD-43). ESA MITAD NO SE
    # ENCIENDE AQUI, y el motivo esta medido, no supuesto: hoy hay 153 pares
    # bidireccionales tras resolver entre nodos vivos, y en el grafo anterior a
    # la campana (merge-base con main, 36b57d78) ya habia 83. Encenderla como
    # esta escrita pondria Gate 0 en rojo 153 veces y chocaria con la
    # verificacion 2 de su propia ficha ("el grafo saneado por OP-S-12 pasa en
    # verde"). Meter 153 pares en la lista blanca chocaria con su adjudicacion
    # ("cada entrada CITA SU LECTURA: una entrada sin su C del 9.22 detras no
    # es una excepcion, es un agujero"). NO SE ADIVINA cual de las dos cede:
    # queda como PARADA declarada en el reporte de la vuelta 150 y en el estado
    # de la ficha, que NO pasa a HECHA.
    duplicadas_resueltas = []
    for _nid in sorted(activos):
        _n = activos[_nid]
        for _campo in ("nodos_previos", "nodos_siguientes"):
            _por_destino = {}
            for _dest in _n.get(_campo) or []:
                if _dest not in nodos_todos:
                    continue  # referencia rota: la caza el chequeo de enlaces
                _por_destino.setdefault(_resolver(_dest), []).append(_dest)
            for _destino, _entradas in sorted(_por_destino.items()):
                if len(_entradas) > 1:
                    duplicadas_resueltas.append(
                        f"{_nid}.{_campo} -> {_destino} (por {_entradas})")
    checks.append((
        "OP-C-05: ninguna lista de aristas de un nodo VIVO tiene dos entradas que RESUELVAN al mismo destino",
        not duplicadas_resueltas,
        f"{len(duplicadas_resueltas)} lista(s) con duplicada tras resolver" + (
            f": {duplicadas_resueltas[:5]}" if duplicadas_resueltas else ""),
    ))
    # ── OP-C-05, SEGUNDA MITAD: EL REGISTRO DE CITAS ───────────────────
    # CORRECCION DECLARADA (2026-09-02, vuelta 152, TAREA 6.c). EL COMENTARIO
    # DE ARRIBA QUE DICE "LO QUE ESTA GUARDA NO CUBRE" NO SE BORRA: describia
    # con exactitud el estado hasta el 2 sep 2026, y taparlo impediria auditar
    # por que la mitad estuvo apagada setenta vueltas. Lo que sigue es lo que
    # cambio.
    #
    # LA DECISION DEL FUNDADOR (2 sep 2026, PREGUNTA 1, opcion c con atajo de
    # registro, en docs/loop/paradas/2026-09-02-opc05-bidireccionales-DECISION.md):
    # LA LISTA BLANCA DEJA DE SER UNA LISTA A MANO Y PASA A SER UN REGISTRO DE
    # CITAS. La guarda ya no pregunta "esta en la lista?", pregunta "tiene este
    # par un VEREDICTO DE LECTURA REGISTRADO CON CITA?". UN PAR SIN CITA ES
    # ROJO. Asi las tres letras de la ficha dejan de chocar: L1 se reescribe
    # como registro, y L2 (el grafo saneado pasa en verde) y L3 (cada entrada
    # cita su lectura) quedan intactas y se cumplen las dos a la vez.
    #
    # DE DONDE SALEN LAS CITAS, y son solo dos vias mas la lectura:
    #   CRIBADO           el par existe en docs/INTRA_DOMINIO_VEREDICTOS.jsonl
    #                     con clase D, B o C. La C es el enlace mutuo legitimo
    #                     del banco 9.22. La cita es el puesto.
    #   P.10              declaracion sellada de nodo puente, declarado y NO
    #                     fundido.
    #   LECTURA_DIRIGIDA  lo que no cubran las dos, leido por P.5 y escrito en
    #                     docs/plan/LECTURAS_DIRIGIDAS.md.
    # El registro se construye con scripts/loop/vuelta152_registro_de_citas_opc05.py
    # y vive en docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl. ESTA GUARDA NO LO
    # CONSTRUYE: LO EXIGE. Si el registro no existe, es ROJO, no verde por
    # omision (banco 9, fallar ruidoso).
    #
    # P.1 NO ES OPCIONAL Y LA DIFERENCIA ESTA MEDIDA: resolviendo alias salen
    # 153 pares, sin resolver 147, y esas SEIS solo aparecen tras resolver. Una
    # guarda que no resolviera daria verde creyendo el registro completo.
    _registro_ruta = BASE / "docs" / "plan" / "REGISTRO_DE_CITAS_OPC05.jsonl"
    _citados = set()
    _registro_existe = _registro_ruta.exists()
    if _registro_existe:
        with _registro_ruta.open(encoding="utf-8") as _fh:
            for _linea in _fh:
                if not _linea.strip():
                    continue
                _e = json.loads(_linea)
                _p = _e.get("par") or []
                if len(_p) == 2:
                    _citados.add(tuple(sorted(_p)))
    # CORRECCION DECLARADA (2026-09-02, vuelta 154, TAREA 2; hallazgo del acta
    # 153, seccion 4, FUERA de lo marcado. NADA DEL COMENTARIO DE ARRIBA SE
    # BORRA: describia con exactitud lo que la guarda hacia hasta hoy, y taparlo
    # impediria auditar por que estuvo verde sobre un universo incompleto.)
    #
    # LA CIFRA QUE SE CORRIGE, Y ES CIFRA PUBLICADA POR LA CUARTA SEDE QUE EL
    # FUNDADOR CREO EL 2 SEP 2026: donde el bloque de arriba y la nota de
    # OP-C-05 dicen "153 pares bidireccionales entre vivos tras resolver, 153
    # con cita, 0 SIN CITA", lo cierto es ~~153 pares, 0 sin cita~~ 154 PARES,
    # Y UNO ESTABA SIN CITA. El "0 sin cita" era FALSO, y lo era porque la
    # guarda contaba con una vara mas estrecha que la declarada.
    #
    # QUE HACIA MAL: recorria los nodos ACTIVOS y de cada uno leia SOLO su lista
    # `nodos_siguientes`. La FUENTE no hacia falta resolverla (el nodo de
    # partida ya es vivo por construccion), pero `nodos_previos` NO SE LEIA
    # NUNCA. Una arista declarada solo por ese lado era invisible.
    #
    # LA VARA QUE SE DECLARA, Y NO ES NUEVA: LOS DOS CAMPOS, sobre FUENTES
    # VIVAS. Esta escrita en tres sitios del repo, los tres re leidos en la
    # vuelta 154 antes de tocar nada:
    #   - la cabecera del reporte CUENTA `nodos_previos` (8.740) y su union de
    #     9.914 sale de los dos campos, no de uno;
    #   - `aristas_a_simetrizar` (arriba, en este mismo fichero) admite una
    #     arista "si LA DECLARA UN NODO VIVO, EN CUALQUIERA DE SUS DOS VISTAS",
    #     que es EXACTAMENTE esta vara, y la comprobacion de simetria de Gate 0
    #     ya la usa;
    #   - `web/lib/engine/planRedactor.ts` linea 96 recorre
    #     `[...nodos_siguientes, ...nodos_previos]` juntos como vecinos.
    # Mas P.1, que manda resolver antes de contar.
    #
    # LAS FUENTES DEPRECADAS SIGUEN FUERA, y no es un estrechamiento nuevo: es
    # el criterio ya adjudicado el 14 ago 2026 (decision del fundador, camino A)
    # que el bloque de arriba cita y que esta ficha hereda de OP-C-04. LO QUE
    # ESO DEJA FUERA SE NOMBRA EN VEZ DE CALLARSE (banco 9, fallar ruidoso):
    # con fuentes deprecadas admitidas saldrian 157 pares y 4 sin cita, o sea
    # TRES pares mas que esta guarda no mira, medidos en la vuelta 154
    # (scripts/loop/vuelta154_tarea2a_universo_bidireccionales.py):
    # `asignacion_recursos_en_gates <-> sistema_gates_go_kill`,
    # `formalizar_junta_asesora <-> identificar_consejo_asesores` y
    # `revision_portafolio_periodica <-> sistema_gates_go_kill`. Los tres solo
    # existen si se admite como declarante a un nodo deprecado.
    #
    # `nodos_previos` DECLARA LA ARISTA EN SENTIDO CONTRARIO y por eso se
    # invierte al meterla: "B es previo mio" es la direccion B hacia A. Meterla
    # como A hacia B invertiria la mitad del universo y la guarda contaria pares
    # que no existen.
    _dirigidas = set()
    for _nid in sorted(activos):
        for _campo in ("nodos_siguientes", "nodos_previos"):
            for _dest in activos[_nid].get(_campo) or []:
                if _dest not in nodos_todos:
                    continue
                _a, _b = _resolver(_nid), _resolver(_dest)
                if (_a and _b and _a != _b
                        and _a in activos and _b in activos):
                    if _campo == "nodos_previos":
                        _dirigidas.add((_b, _a))
                    else:
                        _dirigidas.add((_a, _b))
    _bidireccionales = sorted({tuple(sorted(_p)) for _p in _dirigidas
                               if (_p[1], _p[0]) in _dirigidas})
    # ADJUDICACION 6.9 DEL ACTA 155 (2026-09-03, vuelta 156): EL HUECO DE LA
    # VARA SE CUENTA Y SE PUBLICA CADA VEZ QUE ESTA GUARDA HABLE. Mismo
    # recorrido que el de arriba, con UNA sola diferencia: no se exige que el
    # nodo de PARTIDA este vivo. Los dos EXTREMOS siguen teniendo que resolver a
    # nodos vivos, asi que lo unico que se afloja es QUIEN declara la arista.
    # Es la vara 4 de la tabla del acta 153, seccion 4.1. NINGUNA CIFRA VA
    # TECLEADA: el 157 y el 3 salen de este computo, no de una constante.
    _dirigidas_con_deprecadas = set()
    for _nid in sorted(nodos_todos):
        for _campo in ("nodos_siguientes", "nodos_previos"):
            for _dest in nodos_todos[_nid].get(_campo) or []:
                if _dest not in nodos_todos:
                    continue
                _a, _b = _resolver(_nid), _resolver(_dest)
                if (_a and _b and _a != _b
                        and _a in activos and _b in activos):
                    if _campo == "nodos_previos":
                        _dirigidas_con_deprecadas.add((_b, _a))
                    else:
                        _dirigidas_con_deprecadas.add((_a, _b))
    _bidi_con_deprecadas = sorted({tuple(sorted(_p)) for _p in _dirigidas_con_deprecadas
                                   if (_p[1], _p[0]) in _dirigidas_con_deprecadas})
    _fuera_por_fuente_deprecada = sorted(set(_bidi_con_deprecadas) - set(_bidireccionales))
    _sin_cita = [f"{_a} <-> {_b}" for _a, _b in _bidireccionales
                 if (_a, _b) not in _citados]
    checks.append((
        "OP-C-05: todo par bidireccional entre nodos VIVOS tiene su veredicto de lectura REGISTRADO CON CITA",
        _registro_existe and not _sin_cita,
        (f"{len(_bidireccionales)} par(es) bidireccional(es) tras resolver, "
         f"{len(_bidireccionales) - len(_sin_cita)} con cita, {len(_sin_cita)} SIN CITA"
         + ("" if _registro_existe else " (Y EL REGISTRO NO EXISTE: docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl)")
         + (f" [FUERA DE ESTA VARA, decision del fundador del 14 ago 2026, camino A: {len(_fuera_por_fuente_deprecada)} par(es) mas que solo existen si se admite como declarante a un nodo DEPRECADO, o sea {len(_bidi_con_deprecadas)} con ellos: {[f'{_x} <-> {_y}' for _x, _y in _fuera_por_fuente_deprecada]}]" if _fuera_por_fuente_deprecada else "")
         + (f": {_sin_cita[:5]}" if _sin_cita else "")),
    ))
    # CORRECCION DECLARADA POR ADICION (2026-09-03, vuelta 156, TAREA 1,
    # ADJUDICACION 6.9 DEL ACTA 155). NADA DE LOS COMENTARIOS DE ARRIBA SE
    # BORRA: siguen describiendo con exactitud lo que esta guarda mira y lo que
    # deja fuera.
    #
    # LA PREGUNTA QUE SE CONTESTA (pregunta 4 de la vuelta 154): si los TRES
    # pares que solo existen admitiendo como declarante a un nodo DEPRECADO
    # habia que leerlos y meterlos en el registro.
    #
    # LA ADJUDICACION: NO SE LEEN. Quedan fuera por la DECISION DEL FUNDADOR DEL
    # 14 AGO 2026, CAMINO A, que no es del bucle para revocarla, y leerlos
    # meteria en el registro veredictos de pares que la vara declarada no mira.
    # SE QUEDAN FUERA Y SE QUEDAN NOMBRADOS AQUI DENTRO, que es lo minimo que el
    # banco 9 pide, y SU CUENTA SE PUBLICA CADA VEZ QUE ESTA GUARDA HABLE: no
    # solo en este comentario, sino en la linea de detalle del check, para que
    # el universo que la vara deja fuera no sea nunca invisible desde la salida.
    # Los tres pares son los ya nombrados arriba, y la cuenta es 157 menos 154.
    #
    # COMO SE CUENTA, Y SE COMPUTA, NO SE TECLEA: el mismo recorrido de arriba
    # pero SIN exigir que el nodo de partida este vivo (vara 4 de la tabla del
    # acta 153, seccion 4.1, medida en la vuelta 154 con
    # scripts/loop/vuelta154_tarea2a_universo_bidireccionales.py). Los dos
    # EXTREMOS siguen teniendo que resolver a nodos VIVOS: lo unico que se
    # afloja para contar el hueco es QUIEN declara la arista.
    # CORRECCION DECLARADA POR ADICION (2026-09-03, vuelta 157, TAREA 1,
    # ADJUDICACION 6.5 DEL ACTA 157). NADA DE LOS COMENTARIOS DE ARRIBA SE
    # BORRA, Y EN PARTICULAR NO SE BORRA EL BLOQUE DE LA 6.9 DEL ACTA 155 QUE
    # ESTA JUSTO ENCIMA: esta adjudicacion lo CONFIRMA, no lo enmienda.
    #
    # QUE SE PREGUNTO. El ejecutor de la vuelta 156 marco como DISCUTIBLE 2 la
    # segunda mitad de aquella 6.9: el encargo mandaba la adjudicacion A LOS
    # COMENTARIOS, y el ejecutor ademas cambio LA LINEA DE DETALLE DEL CHECK
    # para que publicara el hueco, leyendo que "su cuenta se publica cada vez
    # que la guarda hable" no lo puede cumplir un comentario, porque un
    # comentario no habla cada vez. Lo marco por si sobraba.
    #
    # LA ADJUDICACION: SE QUEDA, Y NO SOBRA. El ejecutor leyo bien la letra: esa
    # frase es LA LINEA DEL CHECK y no el comentario. El auditor lo comprobo en
    # su propia corrida de Gate 0 del 3 sep 2026: la linea publica 154 pares,
    # 154 con cita y 0 sin cita, y nombra LOS TRES excluidos y el 157 del
    # universo ensanchado, TODO COMPUTADO Y NADA TECLEADO. NO SE REVIERTE.
    #
    # LO QUE ESTO DEJA ESCRITO PARA EL QUE VENGA DETRAS: cuando una adjudicacion
    # mande "publicar" una cuenta, la sede es LA SALIDA DE LA GUARDA y no su
    # comentario. Un comentario deja constancia; solo la salida publica.
    # ── FIN OP-C-05 ────────────────────────────────────────────

    # ── OP-A-01 (FASE 07 ADUANA): LOS TRES CONTROLES DE SU `verificacion` ────
    # Ejecutada en la vuelta 146, TAREA 3.b, con su simulacion previa sobre
    # copia en memoria (scripts/loop/vuelta146_3b_simular_op_a_01.py) y su caso
    # rojo por mutacion sobre variable computada
    # (scripts/loop/vuelta146_3c_mutacion_aduana.py).
    #
    # EL ALCANCE SON LAS TRES ENTRADAS DE SU FICHA Y NI UNA MAS. Su PRERREQUISITO
    # esta CUMPLIDO: la lista canonica de libros existe
    # (docs/plan/OP_S_11_MAPEO_PROPUESTO.md) y su duena OP-S-11 esta HECHA con
    # corte 2026-08-29. Que la vuelta 145 dijera lo contrario es su caida 4.1, y
    # la guarda que impide repetirla es scripts/loop/
    # verificar_ausencias_del_reporte.py (CORRECCION 23).
    #
    # 3) EL SEGUNDO LIBRO Y LOS PASOS, LA MITAD SANA. La entrada 3 dice "Gate 0
    #    rechaza un nodo cuyo segundo libro no aparece en ningun paso". Un nodo
    #    que declara mas de un libro y NO TIENE NI UN paso no puede tener un paso
    #    donde aparezca su segundo libro: ese caso es MECANICO y no puede dar un
    #    falso rojo. LA OTRA MITAD (decidir si el MATERIAL de un paso concreto
    #    viene del segundo libro) PIDE UNA ATRIBUCION POR PASO QUE EL ESQUEMA NO
    #    TIENE: `pasos_accionables` es texto libre sin campo de fuente. NO SE
    #    ADIVINA (EJECUTOR.md 11) y no se fabrica una heuristica de parecido, que
    #    decidiria por semejanza lo que solo decide una lectura. Queda PENDIENTE
    #    DE DOCTRINA, dicho aqui, en la vara de la fase 07 y en el reporte.
    fuentes_por_nodo = {}
    for path in sorted(NODOS_DIR.glob("*.json")):
        try:
            datos = load_json(path)
        except json.JSONDecodeError:
            continue  # ya lo reporta el chequeo de parseo
        if datos.get("deprecado"):
            continue
        fu = datos.get("fuente")
        decl = [x.strip() for x in str(fu).split(" | ") if x.strip()] if isinstance(fu, str) else []
        if len(decl) > 1:
            fuentes_por_nodo[datos.get("node_id") or path.stem] = (
                decl, len(datos.get("pasos_accionables") or []))

    # 1) LA COMPROBACION POSICIONAL (BANCO_DEL_PLAN.md P.2: "el orden dentro del
    #    campo fuente lleva informacion; el primero es de donde salio el nodo, y
    #    lo que viene detras es lo que se le pego"). La nota de la ficha dice para
    #    que le sirve a la ADUANA: "el plan repara 67 nodos una vez; la aduana
    #    impide que entre el sesenta y ocho, y para eso le basta con mirar el
    #    ORDEN del campo fuente". Se coteja contra la NOMINA ADJUDICADA, ENTERA Y
    #    EN ORDEN, para que anadirle en silencio un segundo libro a un nodo ya
    #    adjudicado caiga igual que un nodo nuevo sin adjudicar.
    ruta_nomina = BASE / "dataset" / "metadata" / "aduana_fuente_multiple.json"
    try:
        nomina_aduana = {
            x["node_id"]: list(x["fuente"])
            for x in load_json(ruta_nomina).get("adjudicados", [])
        }
        nomina_legible = True
    except (OSError, json.JSONDecodeError, KeyError, TypeError):
        nomina_aduana, nomina_legible = {}, False

    posicional_fallos = []
    if not nomina_legible:
        posicional_fallos.append(
            "no se pudo leer dataset/metadata/aduana_fuente_multiple.json: "
            "sin nomina el control posicional no mide nada")
    else:
        for nid, (decl, _n_pasos) in sorted(fuentes_por_nodo.items()):
            if nid not in nomina_aduana:
                posicional_fallos.append(
                    f"{nid} declara {len(decl)} fuentes y NO esta en la nomina adjudicada")
            elif nomina_aduana[nid] != decl:
                posicional_fallos.append(
                    f"{nid} declara {decl} y la nomina adjudicada dice {nomina_aduana[nid]}")
    checks.append((
        "OP-A-01: todo nodo VIVO con MAS DE UNA fuente pasa la comprobacion posicional",
        not posicional_fallos,
        f"{len(fuentes_por_nodo)} con fuente multiple, {len(posicional_fallos)} sin adjudicar"
        + (f": {posicional_fallos[:5]}" if posicional_fallos else ""),
    ))

    # 2) EL CAMPO FUENTE CONTRA LA LISTA CANONICA DE LIBROS. NO SE REIMPLEMENTA:
    #    se llama a scripts/loop/verificar_fuente_canonico.py, que YA es el
    #    criterio de HECHO de la fase 08 y ya muerde por mutacion. Dos versiones
    #    de la misma comprobacion serian exactamente la averia de los dos
    #    master_graph que el chequeo de gemelos vino a curar. Este cableado es
    #    ademas el control A2.4 que OP-A-02 exige CORRIENDO (adjudicacion 3.15
    #    del acta 145: "OP-A-02 no los posee: los exige corriendo, y Gate 0 es la
    #    puerta").
    sys.path.insert(0, str(BASE / "scripts" / "loop"))
    from verificar_fuente_canonico import verificar as _verificar_fuente_canonico

    canonico_ok, canonico_incump = _verificar_fuente_canonico()
    checks.append((
        "OP-A-01 / OP-A-02 (A2.4): el campo `fuente` resuelve contra la lista CANONICA de libros",
        canonico_ok,
        f"{len(canonico_incump)} incumplimiento(s)" + (
            f": {[(n, g) for n, g, _m in canonico_incump[:5]]}" if canonico_incump else ""),
    ))

    # 3) LA NOMINA NO SE MUEVE EN SILENCIO (vuelta 147, TAREA 3.d; discutible 5
    #    del reporte 146, adjudicado A FAVOR CON RESERVA SERIA en el acta 146,
    #    3.5). El check (1) de aqui arriba mide LOS NODOS contra la nomina; este
    #    protege LA NOMINA contra la que aquel mide, que hasta hoy no la
    #    protegia nadie: bastaba volver a correr el sellador para que un nodo sin
    #    adjudicar entrase y Gate 0 volviese a verde con el `numstat` tapandolo.
    #    NO SE REIMPLEMENTA NADA: se llama a
    #    scripts/loop/verificar_nomina_sellada.py, que es donde vive el criterio
    #    entero con su frontera escrita.
    from verificar_nomina_sellada import verificar as _verificar_nomina_sellada

    nomina_ok, nomina_fallos, _nomina_detalle = _verificar_nomina_sellada()
    checks.append((
        "OP-A-01: la nomina adjudicada de la aduana no se movio sin declararse",
        nomina_ok,
        f"{len(nomina_fallos)} sin declarar" + (
            f": {nomina_fallos[:3]}" if nomina_fallos else ""),
    ))

    sin_pasos_con_dos_libros = sorted(
        nid for nid, (decl, n_pasos) in fuentes_por_nodo.items() if n_pasos == 0)
    checks.append((
        "OP-A-01: ningun nodo declara un SEGUNDO libro sin tener ni un paso donde pueda aparecer",
        not sin_pasos_con_dos_libros,
        f"{len(sin_pasos_con_dos_libros)} sin pasos" + (
            f": {sin_pasos_con_dos_libros[:5]}" if sin_pasos_con_dos_libros else ""),
    ))
    # ── FIN OP-A-01 ─────────────────────────────────────────────────────────

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

    # El snapshot de los DOS artefactos tal como llegan, antes de que el paso 6
    # recompile. Ver la nota del chequeo de gemelos en step7_validate.
    nodos_al_empezar = (load_json(MASTER_GRAPH_PATH)["nodos"]
                        if MASTER_GRAPH_PATH.exists() else None)

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
    checks, near_duplicates = step7_validate(master, parse_errors, nodos_al_empezar)

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
