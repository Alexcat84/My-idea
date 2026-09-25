# -*- coding: utf-8 -*-
"""Punto 7 (27 sep): listas exactas para la sesion con credencial, sacadas del repo y no de memoria.

- RE-EMBEBER: scripts/build_semantic_index_voyage.texto_nodo embebe titulo_concepto + resumen_teorico +
  condiciones_activacion. Un nodo vivo va a la lista si alguna correccion declarada toco uno de esos campos.
- PREGUNTAS: build_question_cache.generar_pregunta usa resumen_teorico[:400] del nodo (y titulos y condiciones
  de los candidatos, que ninguna correccion toca). Obligatorias: las retiradas de la cache
  (docs/fidelidad/PREGUNTAS_RETIRADAS.json). Recomendadas: nodos con pregunta viva cuyo resumen cambio dentro de
  los 400 primeros caracteres por una correccion de sugerencia de My Idea (no retiradas: no afirman un dato).

Uso: python listas_credencial.py <repo_correcciones>
Escribe docs/fidelidad/credencial/nodos_a_reembeber.txt, preguntas_a_regenerar.txt y LISTAS.md.
"""
import glob
import io
import json
import os
import sys

R = sys.argv[1]
EMB = {'titulo_concepto', 'resumen_teorico', 'condiciones_activacion'}
cache = json.load(io.open(R + '/engine/preguntas_cache.json', encoding='utf-8'))
retiradas = {x['node_id'] for x in json.load(io.open(R + '/docs/fidelidad/PREGUNTAS_RETIRADAS.json', encoding='utf-8'))}
reemb, recom = {}, {}
for f in glob.glob(R + '/dataset/nodos/*.json'):
    d = json.load(io.open(f, encoding='utf-8'))
    if d.get('deprecado') is True:
        continue
    for c in d.get('correcciones', []):
        if c.get('campo') in EMB:
            reemb.setdefault(d['node_id'], []).append(c['id'])
        if c.get('campo') == 'resumen_teorico' and d['node_id'] in cache and d['node_id'] not in retiradas:
            a, b = c['texto_anterior'], c['texto_nuevo']
            p = 0
            while p < min(len(a), len(b)) and a[p] == b[p]:
                p += 1
            if p < 400:
                recom.setdefault(d['node_id'], []).append((c['id'], p))
os.makedirs(R + '/docs/fidelidad/credencial', exist_ok=True)
io.open(R + '/docs/fidelidad/credencial/nodos_a_reembeber.txt', 'w', encoding='utf-8', newline='\n').write('\n'.join(sorted(reemb)) + '\n')
io.open(R + '/docs/fidelidad/credencial/preguntas_a_regenerar.txt', 'w', encoding='utf-8', newline='\n').write('\n'.join(sorted(retiradas | set(recom))) + '\n')
L = ['# Sesion con credencial: listas exactas de la campania de fidelidad', '',
     'Sacadas del repositorio por script (campo `correcciones` de cada nodo vivo, cache de preguntas y registro de retiradas), no de memoria.', '',
     '## 1. Nodos a re-embeber (Voyage): %d' % len(reemb), '',
     'El indice semantico embebe titulo, resumen_teorico y condiciones_activacion (`scripts/build_semantic_index_voyage.py`, `texto_nodo`). Los pasos y el entregable NO entran: una correccion de paso no cambia el vector. Van aqui los nodos con alguna correccion en esos campos. Fichero, uno por linea: `docs/fidelidad/credencial/nodos_a_reembeber.txt`.', '',
     'El constructor no tiene modo parcial: vuelve a embeber todos los nodos vivos (unos 3.500, dentro de la cuota gratuita de Voyage). La lista sirve para comprobar despues que estos vectores si cambiaron.', '']
L += ['- `%s` (%s)' % (k, ', '.join(v)) for k, v in sorted(reemb.items())]
L += ['', '## 2. Preguntas a regenerar: %d' % len(retiradas | set(recom)), '',
      'Con `python engine/build_question_cache.py --patch-file docs/fidelidad/credencial/preguntas_a_regenerar.txt`.', '',
      '### Obligatorias: las %d retiradas de la cache' % len(retiradas), '',
      'Retiradas el 24 sep por la decision del fundador 1 (commit de fidelidad-cache-1): su pregunta nacio de un resumen corregido por CONTRARIO o por cifra, plazo o norma. Detalle y motivo de cada una en `docs/fidelidad/PREGUNTAS_RETIRADAS.json`.', '']
L += ['- `%s`' % k for k in sorted(retiradas)]
L += ['', '### Recomendadas: %d' % len(recom), '',
      'Su resumen cambio dentro de los 400 caracteres que lee el generador, pero por una correccion de "Sugerencia de My Idea" (un anadido practico, no un dato): la pregunta no afirma nada falso y sigue en la cache. Regenerarla la alinea con el texto nuevo.', '']
L += ['- `%s` (%s)' % (k, ', '.join('%s desde el caracter %d' % x for x in v)) for k, v in sorted(recom.items())]
io.open(R + '/docs/fidelidad/credencial/LISTAS.md', 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
print('re-embeber', len(reemb), '| preguntas obligatorias', len(retiradas), 'recomendadas', len(recom))
