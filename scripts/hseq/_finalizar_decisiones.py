#!/usr/bin/env python3
"""Herramienta temporal: aplica las decisiones de revision (manual, basada
en similitud real de contenido, no solo coincidencia de titulo/id) sobre
dedup_candidatos.json y escribe dedup_decisiones.json por dominio."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import CATEGORIAS, dir_metadata

APROBADOS = {
    "environmental": {"manufactura_celular", "deteccion_temprana_regulatoria_2"},
    "health_safety": {"plan_control_peligros_2", "programa_proteccion_respiratoria", "recomendaciones_smart_2",
                      "jerarquia_controles_2"},
    "quality": {
        "concepto_variacion_estadistica_2", "consejo_de_calidad_3", "distribucion_normal_probabilidad_2",
        "especificacion_requisitos_proveedores", "niveles_calidad_muestreo_aql_lql_aoql",
        "inspeccion_automatizada_2", "requisitos_numericos_calidad_lotes", "seis_sigma_servicios",
        "trilogia_de_juran_2",
    },
}
# Para el keeper trilogia_de_juran_2 y consejo_de_calidad_3, el candidatos.json
# tiene DOS entradas (agrupadas por titulo Y por id-base); usamos la de mayor
# tamano (3 vias) y omitimos el duplicado de 1 via para no procesarlo dos veces.
GRUPOS_A_OMITIR_POR_DUPLICADO = {
    ("quality", "trilogia_de_juran_2", 1),  # omitir la version de 1 solo miembro
}

for cat in CATEGORIAS:
    grupos = json.load(open(dir_metadata(cat) / "dedup_candidatos.json", encoding="utf-8"))
    vistos_keeper = set()
    salida = []
    for g in grupos:
        keeper = g["keeper"]
        if keeper in APROBADOS[cat]:
            tam = len(g["fusionar"])
            if (cat, keeper, tam) in GRUPOS_A_OMITIR_POR_DUPLICADO:
                continue
            if keeper in vistos_keeper:
                continue  # ya se proceso una version mas completa de este keeper
            vistos_keeper.add(keeper)
            g["aprobar"] = True
        else:
            g["aprobar"] = False
        salida.append(g)
    ruta = dir_metadata(cat) / "dedup_decisiones.json"
    ruta.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")
    aprobados = [g for g in salida if g["aprobar"]]
    nodos_removidos = sum(len(g["fusionar"]) for g in aprobados)
    print(f"{cat}: {len(salida)} grupos | {len(aprobados)} aprobados ({nodos_removidos} nodos se fusionaran) | {len(salida)-len(aprobados)} rechazados")
