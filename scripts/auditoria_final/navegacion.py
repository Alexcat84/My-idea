# -*- coding: utf-8 -*-
"""NAVEGACION SIN IA sobre el 100 % del catalogo (auditoria final del 28 sep 2026, docs/ACTA_SANEAMIENTO_FINAL.md,
secciones 2 y 4). Las definiciones son las del acta, escritas antes de medir:

  - MURALLAS DE DOMINIO: ninguna arista (nodos_siguientes o nodos_previos) une nodos vivos de dos mundos distintos; un
    mundo solo toca el nucleo, por sus puentes.
  - PUENTES: todo mundo tiene al menos un puente al nucleo, y la LEY DEL ANCLA: ningun nodo del nucleo ancla mas de 2
    puentes del mismo mundo.
  - PUERTAS: todo mundo tiene al menos una puerta; toda puerta es un nodo vivo de su mundo con pregunta en la cache.
  - ALCANZABILIDAD: todo nodo vivo del nucleo se alcanza desde las semillas del nucleo por nodos_siguientes dentro del
    nucleo; todo nodo vivo de un mundo se alcanza desde las puertas de ese mundo por nodos_siguientes pasando por nodos
    del mundo o del nucleo (lo que recorre una sesion de mundo). Se informa ademas el alcance sin pasar por el nucleo.
  - JURISDICCION: toda entrada de dataset/metadata/jurisdiccion.json lleva pais y clase.
  - CERO ARISTAS A DEPRECADOS: ningun nodo vivo apunta a uno deprecado.

Sin IA y sin red: lee dataset/nodos y los ficheros de semillas. Uso:
    python scripts/auditoria_final/navegacion.py            # guarda: sale con 1 si algo falla
    python scripts/auditoria_final/navegacion.py --informe  # ademas imprime el informe en JSON
"""
import collections
import glob
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def cargar():
    nodos = {}
    for f in glob.glob(os.path.join(RAIZ, "dataset", "nodos", "*.json")):
        n = json.load(open(f, encoding="utf-8"))
        nodos[n["node_id"]] = n
    semillas_nucleo = json.load(open(os.path.join(RAIZ, "dataset", "metadata", "entry_seeds.json"), encoding="utf-8"))["seeds"]
    puertas = {d: [p["id"] for p in ps] for d, ps in json.load(
        open(os.path.join(RAIZ, "web", "lib", "assets", "packs_entry_seeds.json"), encoding="utf-8")).items()}
    cache = json.load(open(os.path.join(RAIZ, "engine", "preguntas_cache.json"), encoding="utf-8"))
    jur = json.load(open(os.path.join(RAIZ, "dataset", "metadata", "jurisdiccion.json"), encoding="utf-8"))["nodos"]
    return nodos, semillas_nucleo, puertas, cache, jur


def alcance(inicio, vivos, permitido):
    vistos = set()
    cola = [s for s in inicio if s in vivos and permitido(s)]
    vistos.update(cola)
    while cola:
        a = cola.pop()
        for s in vivos[a].get("nodos_siguientes", []):
            if s in vivos and permitido(s) and s not in vistos:
                vistos.add(s)
                cola.append(s)
    return vistos


def medir():
    nodos, semillas_nucleo, puertas, cache, jur = cargar()
    vivos = {k: n for k, n in nodos.items() if not n.get("deprecado")}
    dom = {k: n.get("dominio") for k, n in vivos.items()}
    mundos = sorted({d for d in dom.values() if d != "core"})
    r = {"vivos": len(vivos), "mundos": mundos, "fallos": []}

    # murallas y aristas a deprecados
    murallas, a_deprecados = [], []
    for k, n in vivos.items():
        for campo in ("nodos_siguientes", "nodos_previos"):
            for o in n.get(campo, []):
                if o in nodos and nodos[o].get("deprecado"):
                    a_deprecados.append(f"{k}.{campo} -> {o}")
                elif o in vivos and dom[o] != dom[k] and "core" not in (dom[o], dom[k]):
                    murallas.append(f"{k} ({dom[k]}) -> {o} ({dom[o]})")
    r["murallas_rotas"] = murallas
    r["aristas_a_deprecados"] = a_deprecados

    # puentes y ley del ancla (por mundo)
    # Un PUENTE es una arista del nucleo a un mundo (la misma definicion que engine/test_puentes_tejidos.py).
    puentes = collections.defaultdict(set)
    for k, n in vivos.items():
        if dom[k] != "core":
            continue
        for o in n.get("nodos_siguientes", []):
            if o in vivos and dom[o] != "core":
                puentes[dom[o]].add((k, o))
    r["puentes"] = {m: len(puentes[m]) for m in mundos}
    ancla = []
    for m in mundos:
        por_ancla = collections.Counter(a for a, _ in puentes[m])
        ancla += [f"{m}: {a} ancla {c}" for a, c in por_ancla.items() if c > 2]
    r["ley_del_ancla_rota"] = ancla

    # puertas
    puertas_mal = []
    for m in mundos:
        ps = puertas.get(m, [])
        if not ps:
            puertas_mal.append(f"{m}: sin puertas")
        for p in ps:
            if p not in vivos:
                puertas_mal.append(f"{m}: la puerta {p} no es un nodo vivo")
            elif dom[p] != m:
                puertas_mal.append(f"{m}: la puerta {p} es de {dom[p]}")
            elif not (cache.get(p) or {}).get("pregunta"):
                puertas_mal.append(f"{m}: la puerta {p} no tiene pregunta en la cache")
    r["puertas"] = {m: len(puertas.get(m, [])) for m in mundos}
    r["puertas_mal"] = puertas_mal

    # alcanzabilidad
    nucleo = {k for k in vivos if dom[k] == "core"}
    al = alcance(semillas_nucleo, vivos, lambda s: dom[s] == "core")
    r["alcance"] = {"core": {"vivos": len(nucleo), "alcanzados": len(al & nucleo), "sin_alcanzar": sorted(nucleo - al)}}
    for m in mundos:
        suyos = {k for k in vivos if dom[k] == m}
        con = alcance(puertas.get(m, []), vivos, lambda s, m=m: dom[s] in (m, "core"))
        solo = alcance(puertas.get(m, []), vivos, lambda s, m=m: dom[s] == m)
        r["alcance"][m] = {
            "vivos": len(suyos),
            "alcanzados": len(con & suyos),
            "sin_alcanzar": sorted(suyos - con),
            "alcanzados_sin_pasar_por_el_nucleo": len(solo & suyos),
        }

    # jurisdiccion
    r["jurisdiccion_sin_clase_o_pais"] = sorted(k for k, v in jur.items() if not v.get("clase") or not v.get("pais"))

    for clave in ("murallas_rotas", "aristas_a_deprecados", "ley_del_ancla_rota", "puertas_mal", "jurisdiccion_sin_clase_o_pais"):
        if r[clave]:
            r["fallos"].append(f"{clave}: {len(r[clave])} (p. ej. {r[clave][:3]})")
    for m in mundos:
        if r["puentes"][m] == 0:
            r["fallos"].append(f"{m}: sin puentes al nucleo")
    for esp, a in r["alcance"].items():
        if a["sin_alcanzar"]:
            r["fallos"].append(f"alcance {esp}: {len(a['sin_alcanzar'])} de {a['vivos']} sin alcanzar (p. ej. {a['sin_alcanzar'][:3]})")
    return r


def main():
    r = medir()
    if "--informe" in sys.argv:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    if r["fallos"]:
        print("ROJO: navegacion del catalogo", *r["fallos"], sep="\n  ")
        sys.exit(1)
    print(f"VERDE: navegacion del catalogo ({r['vivos']} vivos, {len(r['mundos'])} mundos): murallas, puentes, ley del ancla, "
          "puertas, alcanzabilidad 100 % en el nucleo y en cada mundo, jurisdiccion con pais y clase, 0 aristas a deprecados")


if __name__ == "__main__":
    main()
