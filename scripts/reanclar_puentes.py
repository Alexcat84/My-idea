#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""reanclar_puentes.py - Re-ancla al NUCLEO los puentes que anclaron en otro pack.

LA LEY (adjudicada ago 2026): un puente conecta MUNDO -> CORAZON y ancla SIEMPRE
en el nucleo. El acoplamiento mundo<->mundo queda prohibido como accidente.

De donde salieron los mal anclados: el proponedor (paso5_6_semillas_puentes)
cargaba TODO dataset/nodos/ como candidatos, y ahi viven tambien los packs ya
integrados. Nada le impedia anclar un puente de entrega en un nodo de quality y
llamarlo "core". Salieron 22 asi. Esa fabrica ya esta cerrada; esto repara lo
que produjo.

EL PISO DE "ANCLA DIGNA", calibrado y no elegido a ojo: se mide el coseno de los
puentes que SI estan bien anclados, en el mismo espacio de embeddings, y se toma
su percentil 10. Un ancla nueva que supere el piso es al menos tan afin como el
10% mas flojo de lo que ya se acepto en produccion. Lo que no lo supere se PODA
con motivo escrito: mejor puerta ausente que puerta muerta.

EL TOPE por ancla se respeta como siempre: ningun nodo del nucleo sostiene mas de
2 puentes del mismo pack, contando los que ya tenia.

Uso:
  python scripts/reanclar_puentes.py --dry-run
  python scripts/reanclar_puentes.py --aplicar
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
TOPE_POR_ANCLA = 2
PERCENTIL_PISO = 10
# Los mundos recien publicados van primero: sus puertas estan parcialmente
# muertas y son las que un usuario puede topar hoy.
PRIORIDAD = ["compras", "entrega"]


def cargar():
    import numpy as np
    g = json.loads((BASE / "dataset" / "metadata" / "master_graph.json").read_text(encoding="utf-8"))["nodos"]
    idx = json.loads((BASE / "web" / "lib" / "assets" / "semantic_index.json").read_text(encoding="utf-8"))
    E = np.array(idx["embeddings"], dtype=np.float32)
    E /= np.linalg.norm(E, axis=1, keepdims=True)
    return g, idx["ids"], E, {n: i for i, n in enumerate(idx["ids"])}


def main():
    import numpy as np
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--aplicar", action="store_true")
    args = ap.parse_args()

    g, ids, E, pos = cargar()
    core = [n for n in ids if g[n].get("dominio", "core") == "core"]
    Ec = E[[pos[n] for n in core]]

    rutas = sorted((BASE / "packs").glob("*/metadata/bridges_aprobados.json"))
    packs = {p.parent.parent.name: json.loads(p.read_text(encoding="utf-8")) for p in rutas}

    # 1. El piso, calibrado contra lo que ya se acepto.
    buenos = []
    for pack, b in packs.items():
        for x in b["aprobados"]:
            c, d = x["core"], x["dominio"]
            if g.get(c, {}).get("dominio", "core") == "core" and c in pos and d in pos:
                buenos.append(float(E[pos[c]] @ E[pos[d]]))
    buenos.sort()
    piso = buenos[len(buenos) * PERCENTIL_PISO // 100]
    print(f"  {len(buenos)} puentes bien anclados: mediana {buenos[len(buenos)//2]:.3f}, "
          f"p{PERCENTIL_PISO} {piso:.3f} <- PISO")

    orden = PRIORIDAD + sorted(k for k in packs if k not in PRIORIDAD)
    informe = {"piso": round(piso, 4), "tope_por_ancla": TOPE_POR_ANCLA, "cambios": [], "podados": []}

    for pack in orden:
        b = packs.get(pack)
        if not b:
            continue
        malos = [x for x in b["aprobados"] if g.get(x["core"], {}).get("dominio", "core") != "core"]
        if not malos:
            continue
        # las anclas que YA sostienen puentes buenos de este pack
        usadas = Counter(x["core"] for x in b["aprobados"]
                         if g.get(x["core"], {}).get("dominio", "core") == "core")
        # se re-ancla de mejor a peor: el mas afin escoge primero
        candidatos = []
        for x in malos:
            nid = x["dominio"]
            s = Ec @ E[pos[nid]] if nid in pos else np.zeros(len(core))
            candidatos.append((x, s))
        candidatos.sort(key=lambda t: -float(t[1].max()) if len(t[1]) else 0)

        for x, s in candidatos:
            elegido, score = None, 0.0
            for i in np.argsort(-s):
                nid_core = core[i]
                if usadas[nid_core] >= TOPE_POR_ANCLA:
                    continue
                elegido, score = nid_core, float(s[i])
                break
            if elegido is None or score < piso:
                informe["podados"].append({
                    "pack": pack, "nodo_del_mundo": x["dominio"], "ancla_vieja": x["core"],
                    "dominio_del_ancla_vieja": g.get(x["core"], {}).get("dominio"),
                    "motivo": (f"el mejor candidato del nucleo puntua {score:.3f}, por debajo del "
                               f"piso {piso:.3f} (el p10 de los puentes ya aceptados). Mejor puerta "
                               f"ausente que puerta muerta.") if elegido else
                              "no queda ancla del nucleo libre bajo el tope de 2",
                })
                x["_podar"] = True
                continue
            informe["cambios"].append({
                "pack": pack, "nodo_del_mundo": x["dominio"],
                "ancla_vieja": x["core"], "dominio_viejo": g.get(x["core"], {}).get("dominio"),
                "ancla_nueva": elegido, "score": round(score, 4),
                "titulo_nuevo": g[elegido].get("titulo_concepto"),
            })
            x["reanclado_de"] = x["core"]
            x["core"] = elegido
            x["score"] = round(score, 4)
            usadas[elegido] += 1

        b["aprobados"] = [x for x in b["aprobados"] if not x.pop("_podar", False)]

    print(f"\n  re-anclados {len(informe['cambios'])}, podados {len(informe['podados'])}")
    for c in informe["cambios"]:
        print(f"   {c['pack']:<16} {c['nodo_del_mundo'][:34]:<34} {c['dominio_viejo']} -> core "
              f"{c['ancla_nueva'][:30]} ({c['score']})")
    for c in informe["podados"]:
        print(f"   PODADO {c['pack']}: {c['nodo_del_mundo']} — {c['motivo'][:70]}")

    if not args.aplicar:
        print("\n  --dry-run: nada escrito. Para aplicar: --aplicar")
        return

    for p in rutas:
        pack = p.parent.parent.name
        b = packs[pack]
        b["nota"] = b.get("nota", "") + (
            " | 2026-08-07: puentes RE-ANCLADOS al nucleo (ley del ancla). "
            "Los que anclaban en otro pack eran un accidente del proponedor, "
            "que buscaba candidatos sobre el master entero.")
        p.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    (BASE / "docs" / "_reanclaje_puentes.json").write_text(
        json.dumps(informe, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n  Escrito. Informe en docs/_reanclaje_puentes.json")


if __name__ == "__main__":
    main()
