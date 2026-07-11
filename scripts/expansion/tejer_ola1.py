# -*- coding: utf-8 -*-
"""Expansión v1.3 — OLA 1: dedup interno, aristas y tejido al core (RUNBOOK §3-§4).

Etapas (correr en orden, DESPUÉS de aplicar enriquecer_vs_crear):
  --dedup-candidatos   grupos de posibles duplicados INTERNOS de General
                       (título normalizado + fuzzy) -> metadata/dedup_candidatos.json
  --dedup-fusionar     aplica metadata/dedup_decisiones.json (aprobar/keeper)
  --aristas            resuelve refs de los nodos de General contra el censo
                       core+General; fantasmas -> rematch semántico con bandas
                       (auto>=0.70, revisión 0.50-0.70, poda<0.50) -> metadata/
  --aristas-aplicar    aplica veredictos de la banda revisión
  --tejer <Libro>      integra los nodos de UN libro a dataset/nodos:
                       copia, simetriza, y garantiza >=1 predecesor y >=1
                       sucesor en el grafo integrado (mejor vecino temático
                       si falta, registrado). Correr run_phase1.py después
                       de cada libro (Gate 0 entre libros, regla del runbook).

Los nombres de libro para --tejer son los prefijos de `fuente`:
  Traction | SPIN | Never Lose | Warranty | Essentials of Supply | Hard Thing | Co-Intelligence
"""
import json
import re
import sys
import unicodedata
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
NODOS = BASE / "books" / "General" / "nodos"
META = BASE / "books" / "General" / "metadata"
DATASET = BASE / "dataset" / "nodos"

UMBRAL_FUZZY = 0.90
BANDA_AUTO, BANDA_REV = 0.70, 0.50


def a_ascii(t):
    p = unicodedata.normalize("NFKD", t)
    p = "".join(c for c in p if not unicodedata.combining(c)).lower()
    p = re.sub(r"[^a-z0-9_]+", "_", p)
    return re.sub(r"_+", "_", p).strip("_")


def norm_titulo(t):
    return a_ascii(re.sub(r"\([^)]*\)", " ", t or ""))


def cargar(carpeta):
    return {f.stem: json.loads(f.read_text(encoding="utf-8"))
            for f in sorted(carpeta.glob("*.json")) if not f.name.startswith("_")}


def guardar(carpeta, nid, d):
    d["node_id"] = nid
    (carpeta / f"{nid}.json").write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def escribir(ruta, obj):
    ruta.parent.mkdir(exist_ok=True)
    ruta.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# --------------------------- dedup interno ---------------------------

def dedup_candidatos():
    nodos = cargar(NODOS)
    grupos = defaultdict(set)
    for nid, d in nodos.items():
        grupos["t:" + norm_titulo(d.get("titulo_concepto", nid))].add(nid)
        grupos["b:" + re.sub(r"_\d+$", "", nid)].add(nid)
    # fuzzy alto entre titulos
    ids = list(nodos)
    nts = {i: norm_titulo(nodos[i].get("titulo_concepto", "")) for i in ids}
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = nts[ids[i]], nts[ids[j]]
            if a and b and SequenceMatcher(None, a, b).ratio() >= UMBRAL_FUZZY:
                grupos["f:" + a].update({ids[i], ids[j]})
    vistos, out = set(), []
    for miembros in grupos.values():
        if len(miembros) < 2:
            continue
        clave = frozenset(miembros)
        if clave in vistos:
            continue
        vistos.add(clave)
        orden = sorted(miembros)
        out.append({"aprobar": None, "keeper": orden[0], "fusionar": orden[1:],
                    "titulos": {m: nodos[m].get("titulo_concepto", "") for m in orden},
                    "resumen_extracto": {m: nodos[m].get("resumen_teorico", "")[:150] for m in orden}})
    escribir(META / "dedup_candidatos.json", out)
    print(f"{len(out)} grupos candidatos -> {META/'dedup_candidatos.json'}")


def dedup_fusionar():
    decisiones = json.loads((META / "dedup_decisiones.json").read_text(encoding="utf-8"))
    nodos = cargar(NODOS)
    redir = {}
    hechas = 0
    for g in decisiones:
        if not g.get("aprobar"):
            continue
        keeper = g["keeper"]
        for otro in g["fusionar"]:
            if otro not in nodos or keeper not in nodos:
                continue
            k = nodos[keeper]
            k.setdefault("ids_alias", []).append(otro)
            for campo in ("nodos_previos", "nodos_siguientes"):
                for r in nodos[otro].get(campo) or []:
                    if r not in (k.get(campo) or []) and r != keeper:
                        k.setdefault(campo, []).append(r)
            merged = META / "merged_originals"
            merged.mkdir(exist_ok=True)
            (merged / f"{otro}.json").write_text(json.dumps(nodos[otro], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            (NODOS / f"{otro}.json").unlink()
            redir[otro] = keeper
            del nodos[otro]
            hechas += 1
            guardar(NODOS, keeper, k)
    # redirigir referencias
    for nid, d in nodos.items():
        cambio = False
        for campo in ("nodos_previos", "nodos_siguientes"):
            lista = d.get(campo) or []
            nueva = []
            for r in lista:
                r2 = redir.get(r, r)
                if r2 != nid and r2 not in nueva:
                    nueva.append(r2)
            if nueva != lista:
                d[campo] = nueva
                cambio = True
        if cambio:
            guardar(NODOS, nid, d)
    print(f"{hechas} fusiones | quedan {len(nodos)} nodos")


# --------------------------- aristas ---------------------------

def _texto(n):
    return " ".join([n.get("titulo_concepto", ""), n.get("resumen_teorico", "")[:300]])


def aristas():
    from sentence_transformers import SentenceTransformer, util
    nodos = cargar(NODOS)
    core = cargar(DATASET)
    censo = set(core) | set(nodos)
    # alias del core (fusiones historicas)
    alias = {}
    for nid, d in core.items():
        for a in d.get("ids_alias") or []:
            alias[a] = nid

    fantasmas = defaultdict(list)  # ref -> [(nid, campo)]
    exactas = 0
    for nid, d in nodos.items():
        for campo in ("nodos_previos", "nodos_siguientes"):
            for r in list(d.get(campo) or []):
                if r in censo:
                    exactas += 1
                    continue
                if r in alias:
                    lista = d[campo]
                    lista[lista.index(r)] = alias[r]
                    guardar(NODOS, nid, d)
                    exactas += 1
                    continue
                fantasmas[r].append((nid, campo))
    print(f"refs exactas/alias: {exactas} | fantasmas unicos: {len(fantasmas)}")

    modelo = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    objetivos = list(censo)
    corpus = [_texto((core | nodos)[t]) for t in objetivos]
    emb_c = modelo.encode(corpus, normalize_embeddings=True, show_progress_bar=False)
    emb_f = modelo.encode([f.replace("_", " ") for f in fantasmas], normalize_embeddings=True, show_progress_bar=False)

    out = []
    import numpy as np
    S = np.array(emb_f) @ np.array(emb_c).T
    for k, (ref, usos) in enumerate(fantasmas.items()):
        j = int(S[k].argmax())
        score = float(S[k][j])
        destino = objetivos[j]
        banda = "auto" if score >= BANDA_AUTO else ("revision" if score >= BANDA_REV else "poda")
        out.append({"fantasma": ref, "destino": destino, "score": round(score, 4),
                    "titulo_destino": (core | nodos)[destino].get("titulo_concepto", ""),
                    "banda": banda, "usos": [{"nodo": n, "campo": c} for n, c in usos],
                    "veredicto": None})
    escribir(META / "aristas_rematch.json", out)
    autos = sum(1 for o in out if o["banda"] == "auto")
    revs = sum(1 for o in out if o["banda"] == "revision")
    podas = sum(1 for o in out if o["banda"] == "poda")
    print(f"auto={autos} revision={revs} poda={podas} -> {META/'aristas_rematch.json'}")
    _aplicar_rematch(solo_auto=True)


def _aplicar_rematch(solo_auto):
    data = json.loads((META / "aristas_rematch.json").read_text(encoding="utf-8"))
    nodos = cargar(NODOS)
    aplicadas = podadas = 0
    for o in data:
        aplicar = (o["banda"] == "auto") if solo_auto else (o.get("veredicto") == "aprobado_revision")
        podar = (o["banda"] == "poda") if solo_auto else (o.get("veredicto") == "rechazado_revision")
        if not (aplicar or podar):
            continue
        for uso in o["usos"]:
            nid, campo = uso["nodo"], uso["campo"]
            if nid not in nodos:
                continue
            lista = nodos[nid].get(campo) or []
            if o["fantasma"] not in lista:
                continue
            if aplicar and o["destino"] != nid:
                lista[lista.index(o["fantasma"])] = o["destino"]
                aplicadas += 1
            else:
                lista.remove(o["fantasma"])
                podadas += 1
            guardar(NODOS, nid, nodos[nid])
        o["estado"] = "aplicado" if aplicar else "podado"
    escribir(META / "aristas_rematch.json", data)
    print(f"aristas: {aplicadas} redirigidas | {podadas} podadas ({'auto' if solo_auto else 'revision'})")


# --------------------------- tejido ---------------------------

def tejer(prefijo_libro):
    from sentence_transformers import SentenceTransformer
    import numpy as np
    nodos = cargar(NODOS)
    lote = {nid: d for nid, d in nodos.items() if prefijo_libro.lower() in d.get("fuente", "").lower()}
    if not lote:
        print(f"nada que tejer para '{prefijo_libro}'")
        return
    core = cargar(DATASET)
    print(f"tejiendo {len(lote)} nodos de '{prefijo_libro}' sobre core de {len(core)}")

    # 1. copiar al dataset (colision = abortar: el censo debio atraparla)
    for nid, d in lote.items():
        destino = DATASET / f"{nid}.json"
        if destino.exists():
            raise SystemExit(f"COLISION inesperada: {nid} ya existe en dataset/")
    integrado = core | lote

    # 2. limpiar refs que apunten fuera del grafo integrado (quedaron de
    #    otros libros aun no tejidos: se conservan en el archivo de General
    #    y entraran cuando su libro se teja; aqui se filtran al copiar)
    pend_meta = []
    for nid, d in lote.items():
        d = json.loads(json.dumps(d))  # copia
        for campo in ("nodos_previos", "nodos_siguientes"):
            lista = [r for r in (d.get(campo) or []) if r in integrado and r != nid]
            d[campo] = lista
        lote[nid] = d

    # 3. mejor vecino tematico si falta predecesor o sucesor EN EL INTEGRADO
    modelo = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    ids_core = list(core)
    emb_core = modelo.encode([_texto(core[i]) for i in ids_core], normalize_embeddings=True, show_progress_bar=False)
    conexiones = []
    for nid, d in lote.items():
        falta_prev = not d.get("nodos_previos")
        falta_sig = not d.get("nodos_siguientes")
        if not (falta_prev or falta_sig):
            continue
        e = modelo.encode([_texto(d)], normalize_embeddings=True)[0]
        S = np.array(emb_core) @ e
        orden = S.argsort()[::-1]
        if falta_prev:
            mejor = ids_core[int(orden[0])]
            d.setdefault("nodos_previos", []).append(mejor)
            conexiones.append({"nodo": nid, "campo": "nodos_previos", "vecino": mejor, "score": round(float(S[int(orden[0])]), 4)})
        if falta_sig:
            j = int(orden[1] if falta_prev else orden[0])
            mejor = ids_core[j]
            d.setdefault("nodos_siguientes", []).append(mejor)
            conexiones.append({"nodo": nid, "campo": "nodos_siguientes", "vecino": mejor, "score": round(float(S[j]), 4)})

    # 4. escribir lote + simetrizar (ambas direcciones, tocando el core real)
    for nid, d in lote.items():
        guardar(DATASET, nid, d)
        (NODOS / f"{nid}.json").unlink()
    tocados = set()
    grafo = cargar(DATASET)
    for nid in lote:
        d = grafo[nid]
        for sig in d.get("nodos_siguientes") or []:
            back = grafo[sig].setdefault("nodos_previos", [])
            if nid not in back:
                back.append(nid)
                tocados.add(sig)
        for prev in d.get("nodos_previos") or []:
            fwd = grafo[prev].setdefault("nodos_siguientes", [])
            if nid not in fwd:
                fwd.append(nid)
                tocados.add(prev)
    for t in tocados:
        guardar(DATASET, t, grafo[t])

    escribir(META / f"tejido_{a_ascii(prefijo_libro)}.json",
             {"nodos": sorted(lote), "conexiones_vecino_tematico": conexiones,
              "core_tocados_simetria": sorted(tocados)})
    print(f"tejidos {len(lote)} | conexiones por vecino: {len(conexiones)} | core tocados: {len(tocados)}")
    print("SIGUIENTE: python scripts/run_phase1.py (Gate 0 antes del proximo libro)")


if __name__ == "__main__":
    if "--dedup-candidatos" in sys.argv:
        dedup_candidatos()
    elif "--dedup-fusionar" in sys.argv:
        dedup_fusionar()
    elif "--aristas" in sys.argv:
        aristas()
    elif "--aristas-aplicar" in sys.argv:
        _aplicar_rematch(solo_auto=False)
    elif "--tejer" in sys.argv:
        i = sys.argv.index("--tejer")
        tejer(sys.argv[i + 1])
    else:
        print(__doc__)
