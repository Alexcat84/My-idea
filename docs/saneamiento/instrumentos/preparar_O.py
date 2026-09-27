# -*- coding: utf-8 -*-
"""Nivel 1, criterio 16 (decision del fundador del 27 sep 2026): pasada de ORTOGRAFIA (tildes y erratas) sobre los
textos del dataset que ve el cliente: la etiqueta del riel, los pasos y el entregable (el plan sin IA los imprime) y
las preguntas en cache. La voz de la casa no se toca (nivel 2). Solo lectura del repo.

Cada texto lleva su referencia (<bloque>.etiqueta, .paso<N>, .entregable, o <bloque>.pregunta). Trampas por lote, dos,
plantadas en textos reales: TILDE (una palabra en -cion o -sion pierde su tilde) y ERRATA (dos letras de una palabra
larga se trasponen). El lector tiene que devolver la correccion del texto que la lleva.
Uso: python preparar_O.py <repo> <W>"""
import glob
import hashlib
import io
import json
import os
import random
import re
import sys

REPO, W = sys.argv[1], sys.argv[2]
os.chdir(REPO)
nod = {}
for p in glob.glob('dataset/nodos/*.json'):
    n = json.load(io.open(p, encoding='utf-8'))
    if not n.get('deprecado'):
        nod[n['node_id']] = n
cache = json.load(io.open('engine/preguntas_cache.json', encoding='utf-8'))
ids = sorted(nod)
random.Random(20261001).shuffle(ids)
preg = sorted(k for k, v in cache.items() if isinstance(v, dict) and v.get('pregunta'))
random.Random(20261002).shuffle(preg)


def plantar(texto, tipo, az):
    if tipo == 'TILDE':
        m = [x for x in re.finditer(r'\b\w{3,}(ci|si)ón\b', texto)]
        if not m:
            return None
        x = az.choice(m)
        return texto[:x.start()] + x.group(0)[:-2] + 'on' + texto[x.end():]
    m = [x for x in re.finditer(r'\b[a-záéíóúñ]{8,}\b', texto)]
    if not m:
        return None
    x = az.choice(m)
    w = x.group(0)
    i = az.randrange(2, len(w) - 3)
    if w[i] == w[i + 1]:
        return None
    return texto[:x.start()] + w[:i] + w[i + 1] + w[i] + w[i + 2:] + texto[x.end():]


def armar(P, grupos, tam):
    D = os.path.join(W, P)
    os.makedirs(os.path.join(D, 'lotes'), exist_ok=True)
    os.makedirs(os.path.join(D, 'claves'), exist_ok=True)
    N = (len(grupos) + tam - 1) // tam
    args = {}
    for li in range(N):
        l = '%s%03d' % (P, li + 1)
        az = random.Random(int(hashlib.sha256(l.encode()).hexdigest()[:8], 16))
        textos = []  # (ref, texto real)
        for bi, (clave, campos) in enumerate(grupos[li * tam:(li + 1) * tam], 1):
            for campo, t in campos:
                textos.append(('%s-%03d.%s' % (l, bi, campo), clave, campo, t))
        trampas, cambiados = {}, {}
        for tipo in ('TILDE', 'ERRATA'):
            for _ in range(200):
                ref, clave, campo, t = az.choice(textos)
                if ref in cambiados:
                    continue
                nuevo = plantar(t, tipo, az)
                if nuevo and nuevo != t:
                    cambiados[ref] = nuevo
                    trampas[ref] = tipo
                    break
        txt, mapa, bloque_actual = ['# Lote %s: textos del catalogo de My-idea\n' % l], {}, None
        for ref, clave, campo, t in textos:
            b = ref.split('.')[0]
            if b != bloque_actual:
                txt.append('\n### %s' % b)
                bloque_actual = b
            txt.append('- [%s] %s' % (ref, ' '.join(cambiados.get(ref, t).split())))
            mapa[ref] = {'clave': clave, 'campo': campo, 'real': t, 'trampa': trampas.get(ref)}
        io.open(os.path.join(D, 'lotes', 'lote_%s.md' % l), 'w', encoding='utf-8', newline='\n').write('\n'.join(txt) + '\n')
        json.dump(mapa, io.open(os.path.join(D, 'claves', 'mapa_%s.json' % l), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        args[l] = {'n': len(textos), 'trampas': trampas}
    json.dump(args, io.open(os.path.join(D, 'args.json'), 'w', encoding='utf-8'), separators=(',', ':'))
    print(P, 'lotes', N, 'textos', sum(a['n'] for a in args.values()), 'trampas', sum(len(a['trampas']) for a in args.values()))


grupos = []
for k in ids:
    n = nod[k]
    campos = [('etiqueta', n.get('etiqueta_arbol') or '')]
    campos += [('paso%d' % i, p) for i, p in enumerate(n.get('pasos_accionables') or [])]
    campos.append(('entregable', n.get('entregable_esperado') or ''))
    grupos.append((k, [(c, t) for c, t in campos if t]))
armar('O', grupos, 40)
armar('OP', [(k, [('pregunta', cache[k]['pregunta'])]) for k in preg], 110)
