# -*- coding: utf-8 -*-
"""Punto 1 (27 sep): busca los textos_anteriores de las correcciones CONTRARIO y ANADIDO de cifra/plazo/norma
en la cache de preguntas y en todo fichero derivado del grafo. Uso: python derivados.py <repo> <salida.json>"""
import difflib, glob, io, json, os, re, sys, unicodedata
R, OUT = sys.argv[1:3]
def norm(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return ' '.join(re.sub(r'[^\w%$.,]+', ' ', s.lower()).split())
corr = []
for f in glob.glob(R + '/docs/fidelidad/tandas/fidelidad-t*.json'):
    for c in json.load(io.open(f, encoding='utf-8')):
        if c['veredicto'] == 'CONTRARIO':
            clase = 'CONTRARIO'
        elif not c['texto_nuevo'].startswith('Sugerencia de My Idea'):
            clase = 'CIFRA_PLAZO_NORMA'
        else:
            continue
        a, b = c['texto_anterior'].split(), c['texto_nuevo'].split()
        frags = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, [norm(x) for x in a], [norm(x) for x in b], autojunk=False).get_opcodes():
            if op in ('delete', 'replace'):
                # el fragmento quitado con una palabra de contexto a cada lado, para que sea buscable
                s = norm(' '.join(a[max(0, i1 - 1):min(len(a), i2 + 1)]))
                if len(s) >= 12:
                    frags.append(s)
        corr.append({'id': c['id'], 'node_id': c['node_id'], 'campo': c['campo'], 'indice': c.get('indice'), 'clase': clase,
                     'anterior': norm(c['texto_anterior']), 'frags': frags, 'texto_anterior': c['texto_anterior']})
print('correcciones buscadas', len(corr), {k: sum(1 for c in corr if c['clase'] == k) for k in ('CONTRARIO', 'CIFRA_PLAZO_NORMA')})
# 1. cache de preguntas
cache = json.load(io.open(R + '/engine/preguntas_cache.json', encoding='utf-8'))
directas, causales = {}, {}
for nid, e in cache.items():
    q = norm(e.get('pregunta', ''))
    for c in corr:
        hit = [f for f in [c['anterior']] + c['frags'] if f in q]
        if hit:
            directas.setdefault(nid, []).append((c['id'], hit[0]))
# causal: el generador leyo resumen_teorico[:400] del nodo actual (build_question_cache.generar_pregunta)
for c in corr:
    if c['campo'] != 'resumen_teorico' or c['node_id'] not in cache:
        continue
    viejo = c['texto_anterior']
    # la correccion toca el resumen: miramos si el tramo cambiado caia en los 400 primeros caracteres del resumen viejo
    nodo = json.load(io.open('%s/dataset/nodos/%s.json' % (R, c['node_id']), encoding='utf-8'))
    actual = nodo['resumen_teorico']
    # reconstruimos el resumen viejo deshaciendo esta y las posteriores correcciones del mismo campo
    regs = [r for r in nodo.get('correcciones', []) if r.get('campo') == 'resumen_teorico']
    orig = actual
    for r in reversed(regs):
        orig = orig.replace(r['texto_nuevo'], r['texto_anterior'], 1)
    pos = orig.find(viejo)
    if pos == -1:
        causales.setdefault(c['node_id'], []).append((c['id'], 'posicion desconocida, se retira por prudencia'))
    elif pos < 400:
        causales.setdefault(c['node_id'], []).append((c['id'], 'tramo viejo desde el caracter %d del resumen' % pos))
# 2. todo fichero del repo que no sea la fuente ni la documentacion de fidelidad
excl = re.compile(r'(/\.git/|/node_modules/|/\.next/|/dataset/nodos/|/docs/fidelidad/|/packs/[^/]+/nodos/)')
hallazgos = {}
fr = [(c, f) for c in corr for f in [c['anterior']] + c['frags'] if len(f) >= 20]
for p in glob.glob(R + '/**/*', recursive=True):
    q = p.replace(chr(92), '/')
    if excl.search(q) or os.path.isdir(p) or os.path.getsize(p) > 60_000_000 or not re.search(r'\.(json|jsonl|ts|tsx|js|md|txt|csv|html|py)$', q):
        continue
    try:
        t = norm(io.open(p, encoding='utf-8').read())
    except Exception:
        continue
    for c, f in fr:
        if f in t:
            hallazgos.setdefault(q[len(R) + 1:], set()).add(c['id'])
out = {'directas_en_cache': directas, 'causales_en_cache': causales,
       'retirar': sorted(set(directas) | set(causales)),
       'otros_ficheros': {k: sorted(v) for k, v in sorted(hallazgos.items())}}
json.dump(out, io.open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('cache: directas %d, causales %d, a retirar %d' % (len(directas), len(causales), len(out['retirar'])))
for k, v in out['otros_ficheros'].items():
    print(' fichero', k, len(v))
