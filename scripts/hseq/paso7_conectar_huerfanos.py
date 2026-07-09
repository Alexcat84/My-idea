#!/usr/bin/env python3
"""Paso 7 (Gate 0, alcanzabilidad): conecta los nodos huerfanos al
componente alcanzable desde las semillas aprobadas, con la regla
mandatada: aristas nuevas INTRA-dominio justificadas una a una hacia el
vecino tematico mas cercano -- jamas inflar las semillas, jamas cruzar
dominios, jamas al bulto.

Cirugia minima: los huerfanos no se conectan uno por uno a ciegas; se
calcula la condensacion en SCCs del subgrafo huerfano y solo los
SCC-fuente (sin aristas entrantes desde otros huerfanos) reciben UNA
arista de entrada desde su mejor vecino tematico alcanzable (embedding,
mismo modelo del paso 6) -- el resto del cluster se vuelve alcanzable a
traves de las aristas internas que ya existian. Cada arista agregada
queda en metadata/aristas_conexion_gate0.json con {padre, hijo, score,
tamano_cluster_conectado} para auditoria una a una."""
import json
import sys
from collections import deque
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import CATEGORIAS, cargar_dominio, dir_metadata, escribir_json, guardar_nodo

MODELO = "paraphrase-multilingual-MiniLM-L12-v2"


def texto_nodo(d: dict) -> str:
    return f"{d.get('titulo_concepto', '')}. {(d.get('resumen_teorico') or '')[:200]}"


def alcanzables(nodos: dict, seeds: list) -> set:
    vistos, cola = set(s for s in seeds if s in nodos), deque(s for s in seeds if s in nodos)
    while cola:
        n = cola.popleft()
        for s in nodos[n].get("nodos_siguientes") or []:
            if s in nodos and s not in vistos:
                vistos.add(s)
                cola.append(s)
    return vistos


def sccs_fuente(nodos: dict, universo: set) -> list[set]:
    """SCCs del subgrafo inducido por `universo`, devolviendo solo las
    fuente (sin aristas entrantes desde otros SCCs del universo).
    Kosaraju iterativo."""
    grafo = {u: [s for s in (nodos[u].get("nodos_siguientes") or []) if s in universo] for u in universo}
    inverso = {u: [] for u in universo}
    for u, sigs in grafo.items():
        for s in sigs:
            inverso[s].append(u)
    # 1er pase: orden de finalizacion
    visitado, orden = set(), []
    for inicio in universo:
        if inicio in visitado:
            continue
        pila = [(inicio, iter(grafo[inicio]))]
        visitado.add(inicio)
        while pila:
            nodo, it = pila[-1]
            avanzo = False
            for s in it:
                if s not in visitado:
                    visitado.add(s)
                    pila.append((s, iter(grafo[s])))
                    avanzo = True
                    break
            if not avanzo:
                orden.append(nodo)
                pila.pop()
    # 2do pase sobre el inverso
    asignacion, visitado2 = {}, set()
    scc_id = 0
    for nodo in reversed(orden):
        if nodo in visitado2:
            continue
        cola = deque([nodo])
        visitado2.add(nodo)
        while cola:
            n = cola.popleft()
            asignacion[n] = scc_id
            for p in inverso[n]:
                if p not in visitado2:
                    visitado2.add(p)
                    cola.append(p)
        scc_id += 1
    miembros: dict[int, set] = {}
    for n, cid in asignacion.items():
        miembros.setdefault(cid, set()).add(n)
    con_entrada = set()
    for u, sigs in grafo.items():
        for s in sigs:
            if asignacion[u] != asignacion[s]:
                con_entrada.add(asignacion[s])
    return [m for cid, m in miembros.items() if cid not in con_entrada]


def descendientes(nodos: dict, raiz: str, universo: set) -> set:
    vistos, cola = {raiz}, deque([raiz])
    while cola:
        n = cola.popleft()
        for s in nodos[n].get("nodos_siguientes") or []:
            if s in universo and s not in vistos:
                vistos.add(s)
                cola.append(s)
    return vistos


def conectar(cat: str, modelo) -> None:
    from sentence_transformers import util
    import torch
    nodos = cargar_dominio(cat)
    seeds = json.load(open(dir_metadata(cat) / "entry_seeds.json", encoding="utf-8"))
    log = []
    ronda = 0
    while True:
        ronda += 1
        R = alcanzables(nodos, seeds)
        U = set(nodos) - R
        if not U:
            break
        assert ronda <= 5, f"{cat}: la conexion no converge (quedan {len(U)})"
        fuentes = sccs_fuente(nodos, U)
        ids_R = sorted(R)
        emb_R = modelo.encode([texto_nodo(nodos[i]) for i in ids_R],
                              normalize_embeddings=True, show_progress_bar=False)
        for fuente in fuentes:
            ids_F = sorted(fuente)
            emb_F = modelo.encode([texto_nodo(nodos[i]) for i in ids_F],
                                  normalize_embeddings=True, show_progress_bar=False)
            sim = util.cos_sim(emb_F, emb_R)  # [F, R]
            flat_idx = int(torch.argmax(sim))
            fi, ri = flat_idx // len(ids_R), flat_idx % len(ids_R)
            hijo, padre = ids_F[fi], ids_R[ri]
            score = float(sim[fi][ri])
            # agregar arista padre -> hijo, simetrica
            sig = nodos[padre].setdefault("nodos_siguientes", [])
            if hijo not in sig:
                sig.append(hijo)
            prev = nodos[hijo].setdefault("nodos_previos", [])
            if padre not in prev:
                prev.append(padre)
            guardar_nodo(cat, padre, nodos[padre])
            guardar_nodo(cat, hijo, nodos[hijo])
            log.append({
                "ronda": ronda, "padre": padre, "hijo": hijo, "score": round(score, 4),
                "titulo_padre": nodos[padre].get("titulo_concepto", ""),
                "titulo_hijo": nodos[hijo].get("titulo_concepto", ""),
                "tamano_cluster_conectado": len(descendientes(nodos, hijo, U)),
            })
    escribir_json(dir_metadata(cat) / "aristas_conexion_gate0.json", log)
    scores = [e["score"] for e in log]
    print(f"{cat}: {len(log)} aristas de conexion en {ronda - 1 if not (set(nodos) - alcanzables(nodos, seeds)) else ronda} ronda(s) | "
          f"score min={min(scores):.3f} medio={sum(scores)/len(scores):.3f} max={max(scores):.3f}" if scores else f"{cat}: 0 aristas necesarias")


if __name__ == "__main__":
    from sentence_transformers import SentenceTransformer
    modelo = SentenceTransformer(MODELO)
    for cat in CATEGORIAS:
        conectar(cat, modelo)
