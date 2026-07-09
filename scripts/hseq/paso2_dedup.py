#!/usr/bin/env python3
"""Paso 2a: candidatos de dedup INTRA-dominio (jamas entre dominios).
Agrupa por titulo normalizado identico + fuzzy alto + sufijos numericos.
Escribe metadata/dedup_candidatos.json para revision; NO fusiona nada.

Paso 2b (--fusionar): lee metadata/dedup_decisiones.json (los candidatos
revisados, con "aprobar": true/false y "keeper" confirmado por grupo) y
ejecuta las fusiones: keeper conserva su contenido, absorbe los ids en
merged_originals + ids_alias, y toda referencia entrante se redirige.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import (CATEGORIAS, borrar_nodo, cargar_dominio, dir_metadata,
                         escribir_json, guardar_nodo, norm_titulo, similitud)
import json

UMBRAL_FUZZY = 0.90


def sin_sufijo(nid: str) -> str:
    return re.sub(r"_\d+$", "", nid)


def candidatos(cat: str) -> list[dict]:
    nodos = cargar_dominio(cat)
    grupos: dict[str, set[str]] = defaultdict(set)
    # 1) titulo normalizado identico  2) mismo id base sin sufijo numerico
    for nid, d in nodos.items():
        grupos["t:" + norm_titulo(d.get("titulo", nid))].add(nid)
        grupos["b:" + sin_sufijo(nid)].add(nid)
    vistos: set[frozenset] = set()
    out = []
    for miembros in grupos.values():
        if len(miembros) < 2:
            continue
        clave = frozenset(miembros)
        if clave in vistos:
            continue
        vistos.add(clave)
        orden = sorted(miembros, key=lambda i: -len(nodos[i].get("resumen_teorico", "")))
        out.append({
            "aprobar": None,
            "keeper": orden[0],
            "fusionar": orden[1:],
            "titulos": {i: nodos[i].get("titulo", "") for i in orden},
        })
    # 3) fuzzy de titulos entre pares aun no agrupados (solo pares sueltos)
    ids = sorted(nodos)
    ya = {i for g in out for i in [g["keeper"], *g["fusionar"]]}
    normt = {i: norm_titulo(nodos[i].get("titulo", i)) for i in ids}
    for a_i in range(len(ids)):
        a = ids[a_i]
        if a in ya:
            continue
        for b in ids[a_i + 1:]:
            if b in ya or abs(len(normt[a]) - len(normt[b])) > 15:
                continue
            if similitud(normt[a], normt[b]) >= UMBRAL_FUZZY:
                keeper, otro = sorted([a, b], key=lambda i: -len(nodos[i].get("resumen_teorico", "")))
                out.append({"aprobar": None, "keeper": keeper, "fusionar": [otro],
                            "titulos": {keeper: nodos[keeper].get("titulo", ""),
                                        otro: nodos[otro].get("titulo", "")}})
                ya |= {a, b}
                break
    return out


def fusionar(cat: str) -> None:
    ruta = dir_metadata(cat) / "dedup_decisiones.json"
    if not ruta.exists():
        print(f"{cat}: sin dedup_decisiones.json, nada que fusionar")
        return
    decisiones = json.load(open(ruta, encoding="utf-8"))
    nodos = cargar_dominio(cat)
    redir: dict[str, str] = {}
    hechas = 0
    for g in decisiones:
        if g.get("aprobar") is not True:
            continue
        keeper = g["keeper"]
        for viejo in g["fusionar"]:
            if viejo not in nodos or keeper not in nodos:
                continue
            k = nodos[keeper]
            k.setdefault("merged_originals", []).append(
                {"node_id": viejo, "titulo": nodos[viejo].get("titulo", ""),
                 "fuente": nodos[viejo].get("fuente", "")})
            k.setdefault("ids_alias", []).append(viejo)
            # heredar aristas del absorbido (se simetriza en paso 4)
            for campo in ("nodos_previos", "nodos_siguientes"):
                for r in nodos[viejo].get(campo) or []:
                    if r != keeper and r not in (k.get(campo) or []):
                        k.setdefault(campo, []).append(r)
            borrar_nodo(cat, viejo)
            del nodos[viejo]
            redir[viejo] = keeper
            hechas += 1
        guardar_nodo(cat, keeper, nodos[keeper])
    # redirigir referencias entrantes en todo el dominio
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
            guardar_nodo(cat, nid, d)
    print(f"{cat}: {hechas} fusiones ejecutadas | quedan {len(nodos)} nodos")


if __name__ == "__main__":
    modo_fusion = "--fusionar" in sys.argv
    for cat in CATEGORIAS:
        if modo_fusion:
            fusionar(cat)
        else:
            grupos = candidatos(cat)
            escribir_json(dir_metadata(cat) / "dedup_candidatos.json", grupos)
            print(f"{cat}: {len(grupos)} grupos candidatos -> metadata/dedup_candidatos.json")
    if not modo_fusion:
        print("\nSIGUIENTE: revisar candidatos (aprobar true/false, ajustar keeper),")
        print("guardarlos como metadata/dedup_decisiones.json y correr con --fusionar.")
