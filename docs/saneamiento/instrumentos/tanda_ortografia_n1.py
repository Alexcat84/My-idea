# -*- coding: utf-8 -*-
"""Nivel 1, criterio 16 (decision del fundador del 27 sep 2026): la tanda de ORTOGRAFIA de la pasada O.
  - pasos y entregables: correccion declarada, veredicto ORTOGRAFIA (aplicar_correcciones.py);
  - etiquetas del riel: la lista curada dataset/metadata/etiquetas_de_cara_v1_ortografia.json (la ultima, manda);
  - preguntas en cache: engine/preguntas_cache.json, con su tanda escrita (la pregunta no es un nodo).
Solo cambia lo que el verificador acepto como falta real (tildes, erratas, enie). Uso: python tanda_ortografia_n1.py <repo>"""
import glob
import io
import json
import os
import sys

os.chdir(sys.argv[1])
R = 'docs/saneamiento/resultados/O/'
fin = json.load(io.open(R + 'final.json', encoding='utf-8'))
mapa = {}
for p in glob.glob(R + 'claves/mapa_*.json') + glob.glob(R + 'claves_OP/mapa_*.json'):
    mapa.update(json.load(io.open(p, encoding='utf-8')))
FECHA = '2026-09-27'
DEC = 'Saneamiento del dataset, nivel 1 (decision del fundador del 27 sep 2026), criterio 16: ortografia de los textos que ve el cliente.'
INST = 'Pasada O del saneamiento (docs/saneamiento/resultados/O): lector con trampas, verificador de cada cambio'
nodos, etiquetas, preguntas, sin_casar = [], {}, [], []
for lote in fin:
    for x in lote['final']:
        m = mapa[x['ref']]
        clave, campo, real = m['clave'], m['campo'], m['real']
        nuevo = ' '.join(x['texto_final'].split())
        if nuevo == ' '.join(real.split()):
            continue
        ev = '%s: %s (%s)' % (x['ref'], x['faltas'], x['motivo'])
        if campo == 'pregunta':
            preguntas.append({'id': 'n1-orto-p%03d' % (len(preguntas) + 1), 'nodo': clave, 'texto_anterior': real, 'texto_nuevo': nuevo, 'evidencia': ev})
        elif campo == 'etiqueta':
            etiquetas[clave] = (real, nuevo, ev)
        else:
            n = json.load(io.open('dataset/nodos/%s.json' % clave, encoding='utf-8'))
            if campo == 'entregable':
                c = {'campo': 'entregable_esperado', 'texto_anterior': n['entregable_esperado']}
                if n['entregable_esperado'] != real:
                    sin_casar.append(x['ref'])
                    continue
            else:
                i = int(campo[4:])
                if i >= len(n['pasos_accionables']) or n['pasos_accionables'][i] != real:
                    sin_casar.append(x['ref'])
                    continue
                c = {'campo': 'pasos_accionables', 'indice': i, 'texto_anterior': real}
            c.update({'id': 'n1-orto-%04d' % (len(nodos) + 1), 'node_id': clave, 'veredicto': 'ORTOGRAFIA', 'texto_nuevo': nuevo,
                      'cita': {'instrumento': INST, 'evidencia': ev}, 'decision': DEC, 'fecha': FECHA})
            nodos.append(c)
json.dump(nodos, io.open('docs/saneamiento/tandas/saneamiento-n1-ortografia.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
json.dump(preguntas, io.open('docs/saneamiento/tandas/saneamiento-n1-ortografia-preguntas.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
lista = {'_nota': ('Ortografia de las etiquetas del riel (saneamiento, nivel 1, criterio 16, decision del fundador del 27 sep 2026): solo '
                   'tildes, erratas y enie, aceptadas por el verificador de la pasada O. La ultima lista: manda sobre las anteriores.'),
         '_motivos': {k: v[2] for k, v in sorted(etiquetas.items())}}
lista.update({k: v[1] for k, v in sorted(etiquetas.items())})
io.open('dataset/metadata/etiquetas_de_cara_v1_ortografia.json', 'w', encoding='utf-8', newline='\n').write(json.dumps(lista, ensure_ascii=False, indent=1) + '\n')
print('nodos', len(nodos), '| etiquetas', len(etiquetas), '| preguntas', len(preguntas), '| sin casar (el texto ya cambio)', sin_casar)
