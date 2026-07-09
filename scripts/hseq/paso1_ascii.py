#!/usr/bin/env python3
"""Paso 1: ids 100% ASCII. Translitera ids no-ASCII (misma regla del core),
renombra archivos, reescribe TODAS las referencias del dominio, y conserva
el id original en `ids_alias`. Corre por dominio, idempotente."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import (CATEGORIAS, a_ascii, borrar_nodo, cargar_dominio,
                         dir_metadata, escribir_json, guardar_nodo)

for cat in CATEGORIAS:
    nodos = cargar_dominio(cat)
    mapa: dict[str, str] = {}
    for viejo in sorted(nodos):
        nuevo = a_ascii(viejo)
        if nuevo == viejo:
            continue
        # colision post-transliteracion: sufijo incremental (dedup lo juntara)
        candidato, n = nuevo, 2
        while candidato in nodos or candidato in mapa.values():
            candidato = f"{nuevo}_{n}"
            n += 1
        mapa[viejo] = candidato
    if not mapa:
        print(f"{cat}: 0 ids a transliterar")
        continue
    # renombrar nodos
    for viejo, nuevo in mapa.items():
        data = nodos.pop(viejo)
        alias = data.get("ids_alias") or []
        if viejo not in alias:
            alias.append(viejo)
        data["ids_alias"] = alias
        borrar_nodo(cat, viejo)
        guardar_nodo(cat, nuevo, data)
        nodos[nuevo] = data
    # reescribir referencias en todo el dominio
    tocados = 0
    for nid, data in nodos.items():
        cambio = False
        for campo in ("nodos_previos", "nodos_siguientes"):
            lista = data.get(campo) or []
            nueva = [mapa.get(r, r) for r in lista]
            if nueva != lista:
                data[campo] = nueva
                cambio = True
        if cambio:
            guardar_nodo(cat, nid, data)
            tocados += 1
    escribir_json(dir_metadata(cat) / "ascii_renombrados.json", mapa)
    print(f"{cat}: {len(mapa)} ids transliterados | {tocados} nodos con refs reescritas")
    for v, n in mapa.items():
        print(f"    {v} -> {n}")
print("\nVerificacion: correr run_phase1_dominio.py despues del paso 4.")
