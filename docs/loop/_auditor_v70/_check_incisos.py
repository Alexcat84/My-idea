# -*- coding: utf-8 -*-
# Sonda del auditor v70: trozos INCISO verbatim y pasos de supervivientes.
import json, subprocess

Gpre = json.loads(subprocess.run(
    ['git', 'show', 'bf4f20f9:dataset/metadata/master_graph.json'],
    capture_output=True, text=True, encoding='utf-8').stdout)['nodos']
Gpost = json.load(open('dataset/metadata/master_graph.json', encoding='utf-8'))['nodos']

def tx(n):
    return json.dumps(n, ensure_ascii=False)

pruebas = [
    ('acto32', 'encontrar_grandes_problemas_mercados_emergentes',
     'mercados en fase embrionaria o de rápido crecimiento'),
    ('acto34', 'ciclo_de_culpa',
     "patrones repetitivos de 'culpar y entrenar' tras incidentes"),
    ('acto35a', 'comunidad_tribu_marca', 'físicos o digitales'),
    ('acto35b', 'marcador_visual_marca', 'físicos o digitales'),
    ('acto36a', 'matriz_de_control_de_proceso',
     'unidad de medida, sensor, frecuencia y tamaño de muestra'),
    ('acto36b', 'matriz_de_control_de_proceso',
     'cobertura de variables críticas y velocidad de respuesta'),
    ('acto36c', 'control_mantener_ganancias',
     'cobertura de variables críticas y velocidad de respuesta'),
]
for tag, nid, tz in pruebas:
    print(tag, nid[:44], '->', 'VERBATIM' if tz in tx(Gpre[nid]) else 'NO')

print('--- pasos supervivientes pre->post ---')
for s in ['atacar_mercados_establecidos_con_problema',
          'wallas_intimacion_fringe_consciousness', 'ciclo_de_culpa_2',
          'construccion_tribu_de_marca', 'plan_de_control']:
    print(s, len(Gpre[s]['pasos_accionables']), '->', len(Gpost[s]['pasos_accionables']))

print('--- resultantes del reporte presentes en el grafo post ---')
res = [
    ('atacar_mercados_establecidos_con_problema', 'y también mercados en fase embrionaria'),
    ('ciclo_de_culpa_2', 'identificando los patrones repetitivos'),
    ('construccion_tribu_de_marca', 'ya sean físicos o digitales'),
    ('plan_de_control', 'especificando unidad de medida, sensor'),
    ('plan_de_control', 'y también su cobertura de variables críticas'),
]
for nid, frag in res:
    ok = any(frag in p for p in Gpost[nid]['pasos_accionables'])
    print(nid[:44], '|', frag[:40], '->', 'SI' if ok else 'NO')
