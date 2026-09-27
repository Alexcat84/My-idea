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
# Solo lo PENDIENTE: correcciones de tandas desde DESDE (la sesion con credencial del 24 sep ya hizo t1 a t14) y
# preguntas retiradas que hoy no estan en la cache.
DESDE = int(sys.argv[2]) if len(sys.argv) > 2 else 1
EMB = {'titulo_concepto', 'resumen_teorico', 'condiciones_activacion'}
cache = json.load(io.open(R + '/engine/preguntas_cache.json', encoding='utf-8'))
retiradas = {x['node_id'] for x in json.load(io.open(R + '/docs/fidelidad/PREGUNTAS_RETIRADAS.json', encoding='utf-8'))} - set(cache)
reemb, recom = {}, {}
for x in json.load(io.open(R + '/docs/fidelidad/PREGUNTAS_RETIRADAS.json', encoding='utf-8')):
    if 'RESTAURADA' in x.get('estado', ''):
        recom.setdefault(x['node_id'], []).append(('restaurada, puerta de mundo (guarda H13)', 0))
for f in glob.glob(R + '/dataset/nodos/*.json'):
    d = json.load(io.open(f, encoding='utf-8'))
    if d.get('deprecado') is True:
        continue
    for c in d.get('correcciones', []):
        if int(c['id'].split('-t')[1].split('-')[0]) < DESDE:
            continue
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
     '**Primera sesion con credencial: HECHA el 24 sep 2026** (commit 58362389): 44 nodos re-embebidos con sus vectores comprobados y 23 preguntas regeneradas y de vuelta en la cache, tras las tandas fidelidad-t1 a fidelidad-t14. **Lo que sigue es lo PENDIENTE** para una segunda sesion, desde fidelidad-t%d (la pasada sobre los campos que llegan a la IA).' % DESDE, '',
     '## 1. Nodos a re-embeber (Voyage): %d' % len(reemb), '',
     'El indice semantico embebe titulo, resumen_teorico y condiciones_activacion (`scripts/build_semantic_index_voyage.py`, `texto_nodo`). Los pasos y el entregable NO entran: una correccion de paso no cambia el vector. Van aqui los nodos con alguna correccion en esos campos. Fichero, uno por linea: `docs/fidelidad/credencial/nodos_a_reembeber.txt`.', '',
     'El constructor no tiene modo parcial: vuelve a embeber todos los nodos vivos (unos 3.500, dentro de la cuota gratuita de Voyage). La lista sirve para comprobar despues que estos vectores si cambiaron.', '']
L += ['- `%s` (%s)' % (k, ', '.join(v)) for k, v in sorted(reemb.items())]
L += ['', '## 2. Preguntas a regenerar: %d' % len(retiradas | set(recom)), '',
      'Con `python engine/build_question_cache.py --patch-file docs/fidelidad/credencial/preguntas_a_regenerar.txt`.', '',
      '### Obligatorias: las %d retiradas de la cache' % len(retiradas), '',
      'Retiradas de la cache porque nacieron de texto corregido por CONTRARIO o por cifra, plazo o norma: el resumen del propio nodo (el generador lee sus 400 primeros caracteres) o las condiciones de un candidato (lee las 3 primeras de cada uno). Mientras tanto la app usa la pregunta generica adaptada en vivo. Detalle y motivo de cada una en `docs/fidelidad/PREGUNTAS_RETIRADAS.json`, que guarda tambien, como historia, las 23 ya regeneradas.', '']
L += ['- `%s`' % k for k in sorted(retiradas)]
L += ['', '### Recomendadas: %d' % len(recom), '',
      'Siguen en la cache y no afirman nada falso, pero nacieron de texto que luego cambio: o su resumen cambio por una Sugerencia de My Idea, o son puertas de un mundo que se retiraron y se restauraron porque la guarda AUD-09 H13 exige que toda puerta tenga su pregunta escrita. Regenerarlas las alinea con el texto nuevo.', '']
L += ['- `%s` (%s)' % (k, ', '.join(x[0] if isinstance(x[0], str) and ' ' in x[0] else '%s desde el caracter %d' % x for x in v)) for k, v in sorted(recom.items())]
io.open(R + '/docs/fidelidad/credencial/LISTAS.md', 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
print('re-embeber', len(reemb), '| preguntas obligatorias', len(retiradas), 'recomendadas', len(recom))
