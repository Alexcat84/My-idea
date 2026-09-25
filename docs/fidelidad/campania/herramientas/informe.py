# -*- coding: utf-8 -*-
"""Construye el informe del tramo 1 y el registro por paso, y comprueba cobertura y citas."""
import csv
import io
import json
import math
import re
import sys
import unicodedata

W, REPO = sys.argv[1], sys.argv[2]
R = json.load(io.open(W + '/resultado_tramo1.json', encoding='utf-8'))
LOTES = [r['lote'] for r in R]


def norm(s):
    s = unicodedata.normalize('NFKC', s or '')
    s = re.sub(r'(?<=[a-z\.])\d{1,2}(?= [A-Z])', '', s)
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('—', '--'), ('–', '-'), ('‑', '-'), ('‐', '-')):
        s = s.replace(a, b)
    return ' '.join(s.split()).lower()


def sin_rayas(s):
    return (s or '').replace('—', '--').replace('–', '-')


libros = {}


def libro(f):
    if f not in libros:
        libros[f] = io.open(f, encoding='utf-8', errors='replace').read().splitlines()
    return libros[f]


def rango(lineas):
    nums = [int(n) for n in re.findall(r'L(\d+)', lineas or '')]
    if not nums:
        return None
    return min(nums), max(nums)


def wilson(k, n):
    if n == 0:
        return (0, 0)
    z = 1.96
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (100 * (c - h), 100 * (c + h))


def leer_tsv(ruta):
    filas = {}
    try:
        for c in csv.reader(io.open(ruta, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
            if c and re.match(r'^[A-Z0-9]+-\d{3}$', c[0].strip()):
                filas[c[0].strip()] = c
    except FileNotFoundError:
        pass
    return filas


registro, fichas, errores = [], [], []
cuenta = {}
for r in R:
    lote = r['lote']
    mapa = json.load(io.open('%s/claves/mapa_%s.json' % (W, lote), encoding='utf-8'))
    tsv = leer_tsv('%s/salidas/lector_%s.tsv' % (W, lote))
    nofiel = {x['id']: x for x in r['noFiel']}
    reales = [i for i, m in mapa.items() if m['real']]
    for ident in sorted(reales):
        m = mapa[ident]
        nodo = json.load(io.open('%s/dataset/nodos/%s.json' % (REPO, m['node_id']), encoding='utf-8'))
        actual = nodo['pasos_accionables'][m['paso'] - 1]
        fichero = json.load(io.open(W + '/libros.json', encoding='utf-8'))[m['libro']]['fichero']
        if ident in nofiel:
            x = dict(nofiel[ident])
        else:
            c = tsv.get(ident, [])
            x = {'veredicto': 'FIEL', 'lineas': c[2] if len(c) > 2 else '', 'frase_clave': c[3] if len(c) > 3 else '',
                 'decidido_por': 'lector'}
            if not c:
                errores.append('%s: FIEL sin fila en el TSV del lector' % ident)
        v = x['veredicto']
        cuenta.setdefault(m['libro'], {}).setdefault(v, 0)
        cuenta[m['libro']][v] += 1
        registro.append({'id': ident, 'node_id': m['node_id'], 'paso': m['paso'], 'libro': m['libro'], 'veredicto': v,
                         'lineas': x.get('lineas', ''), 'frase_clave': sin_rayas(x.get('frase_clave', '')),
                         'decidido_por': x.get('decidido_por', '')})
        if v == 'FIEL':
            continue
        rg = rango(x.get('lineas'))
        texto = libro(fichero)
        pasaje = ''
        if rg and rg[1] <= len(texto):
            a, b = rg
            pasaje = '\n'.join('L%d: %s' % (k, sin_rayas(texto[k - 1])) for k in range(a, b + 1) if texto[k - 1].strip())
        else:
            errores.append('%s: rango de lineas ilegible o fuera del libro (%s)' % (ident, x.get('lineas')))
        # la frase clave, literal: se busca en el rango y, si no, en todo el libro
        fc = x.get('frase_clave', '')
        limpio = re.sub(r'\(L\d+[^)]*\)', ' ', fc)
        trozos = [t for t in re.split(r'\.\.\.|…| / ', limpio) if len(t.strip()) > 8]
        en_rango = all(norm(t.strip(' "')) in norm(pasaje) for t in trozos) if trozos else False
        en_libro = all(norm(t.strip(' "')) in norm('\n'.join(texto)) for t in trozos) if trozos else False
        if not en_libro:
            errores.append('%s: frase clave no literal en el libro' % ident)
        fichas.append({'id': ident, 'node_id': m['node_id'], 'fichero_nodo': 'dataset/nodos/%s.json' % m['node_id'],
                       'paso_desde_0': m['paso'] - 1, 'paso_desde_1': m['paso'], 'libro': m['libro'], 'fichero_libro': fichero,
                       'veredicto': v, 'decidido_por': x.get('decidido_por', ''), 'texto_actual': sin_rayas(actual),
                       'lineas': x.get('lineas', ''), 'frase_clave': sin_rayas(fc), 'frase_en_rango': en_rango,
                       'frase_en_libro': en_libro, 'dato': sin_rayas(x.get('dato', '')),
                       'texto_fiel': sin_rayas(x.get('texto_fiel', '')), 'razon': sin_rayas(x.get('razon', '')),
                       'pasaje': pasaje})

# cobertura: cada paso vivo de los libros del tramo 1, exactamente una vez
esperados = set()
for m in [json.load(io.open('%s/claves/reales_%s.json' % (W, l), encoding='utf-8')) for l in LOTES]:
    for it in m:
        esperados.add((it['node_id'], it['paso']))
vistos = [(x['node_id'], x['paso']) for x in registro]
if len(vistos) != len(set(vistos)) or set(vistos) != esperados:
    errores.append('COBERTURA: %d vistos, %d unicos, %d esperados' % (len(vistos), len(set(vistos)), len(esperados)))

base = REPO + '/docs/fidelidad/campania'
import os
os.makedirs(base, exist_ok=True)
with io.open(base + '/VEREDICTOS_TRAMO1.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for x in registro:
        f.write(json.dumps(x, ensure_ascii=False) + '\n')

ORD = {'CONTRARIO': 0, 'ANADIDO': 1, 'OPERATIVO': 2}
fichas.sort(key=lambda f: (ORD[f['veredicto']], f['libro'], f['node_id'], f['paso_desde_1']))
json.dump(fichas, io.open(W + '/fichas_tramo1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'errores': errores, 'cuenta': cuenta, 'n': len(registro), 'fichas': len(fichas)},
          io.open(W + '/comprobacion_tramo1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('pasos', len(registro), 'fichas', len(fichas), 'errores', len(errores))
for e in errores[:30]:
    print('  ', e)
for l, c in cuenta.items():
    n = sum(c.values())
    print(l[:40], c, n)
