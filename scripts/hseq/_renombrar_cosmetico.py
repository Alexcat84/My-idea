#!/usr/bin/env python3
"""Herramienta temporal (checkpoint 3, post-fusion): todo keeper
superviviente con sufijo numerico cuya base sin sufijo quedo libre tras
la fusion se renombra a la base limpia -- el sufijo viejo pasa a
ids_alias y todas las referencias del dominio se reescriben."""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import borrar_nodo, cargar_dominio, dir_metadata, escribir_json, guardar_nodo

RENOMBRES = {
    "environmental": {"deteccion_temprana_regulatoria_2": "deteccion_temprana_regulatoria"},
    "health_safety": {
        "plan_control_peligros_2": "plan_control_peligros",
        "recomendaciones_smart_2": "recomendaciones_smart",
        "jerarquia_controles_2": "jerarquia_controles",
    },
    "quality": {
        "concepto_variacion_estadistica_2": "concepto_variacion_estadistica",
        "distribucion_normal_probabilidad_2": "distribucion_normal_probabilidad",
        "inspeccion_automatizada_2": "inspeccion_automatizada",
        "trilogia_de_juran_2": "trilogia_de_juran",
    },
}

for cat, mapa in RENOMBRES.items():
    nodos = cargar_dominio(cat)
    # verificacion de seguridad: la base debe estar libre de verdad
    for viejo, nuevo in mapa.items():
        assert viejo in nodos, f"{cat}: {viejo} no existe"
        assert nuevo not in nodos, f"{cat}: {nuevo} ya existe, no se puede renombrar {viejo} sobre el"
        base_sin_sufijo = re.sub(r"_\d+$", "", viejo)
        assert base_sin_sufijo == nuevo, f"{cat}: {viejo} -> {nuevo} no es un sufijo numerico limpio"

    for viejo, nuevo in mapa.items():
        data = nodos.pop(viejo)
        alias = data.get("ids_alias") or []
        if viejo not in alias:
            alias.append(viejo)
        data["ids_alias"] = alias
        borrar_nodo(cat, viejo)
        guardar_nodo(cat, nuevo, data)
        nodos[nuevo] = data

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

    escribir_json(dir_metadata(cat) / "renombres_cosmeticos.json", mapa)
    print(f"{cat}: {len(mapa)} ids renombrados a su base limpia | {tocados} nodos con refs reescritas")
    for v, n in mapa.items():
        print(f"    {v} -> {n}")
