# -*- coding: utf-8 -*-
"""GUARDA DE FUENTES: ningun titulo de libro llega a un texto de cara al cliente.

REGLA ESTRICTA del fundador (26 sep 2026): el cliente NUNCA ve el titulo de un libro ni un autor citado como
fuente, ni en pantalla, ni en un documento, ni en un correo, ni en una respuesta de la IA. Las fuentes viven SOLO
en metadatos internos (el campo `fuente` de cada nodo, dataset/metadata/fuentes_canonicas.json, vigencia.json).

Esta guarda exige:
  1. que cada fuente de un nodo vivo este en la lista canonica (un libro nuevo no entra sin declarar sus titulos);
  2. que ningun titulo de la lista aparezca en un texto de cara al cliente:
       - los catalogos de la interfaz, los correos y los avisos (web/lib/i18n/mensajes/*.ts, los once idiomas);
       - las etiquetas del riel en los diez idiomas derivados (web/lib/i18n/etiquetas/*.json);
       - las preguntas pregeneradas (web/lib/assets/preguntas_cache.json);
       - las instrucciones de la IA (web/lib/assets/prompts.json): lo que la IA no lee no lo puede repetir;
       - el codigo de la web que arma texto (web/app y web/lib, sin comentarios ni pruebas);
       - el texto de cada nodo vivo que llega a la IA o a la pantalla (etiqueta, resumen, pasos, condiciones,
         entregable). El titulo_concepto NO se pinta (AGENTS.md) y no se toca por doctrina: no se barre aqui;
  3. que cada nodo vivo tenga etiqueta_arbol, para que ninguna pantalla caiga al titulo por falta de etiqueta;
  4. caso negativo: un texto con un titulo de la lista hace fallar la guarda.
Un hallazgo que sea vocabulario y no cita (un concepto que se llama igual que un libro) se adjudica en
`_adjudicados` de la lista canonica, con su texto y su motivo.

    python engine/test_fuentes_de_cara.py
"""
import glob
import io
import json
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTA = os.path.join(RAIZ, 'dataset', 'metadata', 'fuentes_canonicas.json')
WEB = os.path.join(RAIZ, 'web')
CAMPOS_NODO = ('etiqueta_arbol', 'resumen_teorico', 'entregable_esperado', 'pasos_accionables', 'condiciones_activacion')


def normal(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).lower()


def patrones(lista):
    out = {}
    for fuente, e in lista['fuentes'].items():
        for t in e.get('titulos') or []:
            out[normal(t)] = re.compile(r'(?<![a-z0-9])' + re.escape(normal(t)) + r'(?![a-z0-9])')
    return out


def sin_comentarios(src):
    src = re.sub(r'/\*.*?\*/', ' ', src, flags=re.S)
    return re.sub(r'(^|[^:"\'`])//[^\n]*', r'\1', src)


def textos_de_cara():
    """(donde, texto) de cada superficie de cara al cliente."""
    for p in sorted(glob.glob(os.path.join(WEB, 'lib', 'i18n', 'mensajes', '*.ts'))):
        if not p.endswith('.test.ts'):
            yield os.path.relpath(p, RAIZ), sin_comentarios(io.open(p, encoding='utf-8').read())
    for p in sorted(glob.glob(os.path.join(WEB, 'lib', 'i18n', 'etiquetas', '*.json'))):
        d = json.load(io.open(p, encoding='utf-8'))
        for k, v in (d.items() if isinstance(d, dict) else []):
            if isinstance(v, str):
                yield '%s:%s' % (os.path.relpath(p, RAIZ), k), v
    cache = json.load(io.open(os.path.join(WEB, 'lib', 'assets', 'preguntas_cache.json'), encoding='utf-8'))
    for k, v in cache.items():
        yield 'preguntas_cache:%s' % k, json.dumps(v, ensure_ascii=False)
    yield 'prompts.json', io.open(os.path.join(WEB, 'lib', 'assets', 'prompts.json'), encoding='utf-8').read()
    for carpeta in ('app', 'lib'):
        for p in sorted(glob.glob(os.path.join(WEB, carpeta, '**', '*.ts*'), recursive=True)):
            if '.test.' in p or os.sep + 'mensajes' + os.sep in p:
                continue
            yield os.path.relpath(p, RAIZ), sin_comentarios(io.open(p, encoding='utf-8').read())


def textos_de_nodos(nodos):
    for k, n in sorted(nodos.items()):
        for c in CAMPOS_NODO:
            v = n.get(c)
            for i, t in enumerate(v if isinstance(v, list) else [v] if v else []):
                yield '%s.%s%s' % (k, c, '[%d]' % i if isinstance(v, list) else ''), t


def fallos_de(lista, nodos, textos):
    fallos = []
    pats = patrones(lista)
    adjudicados = lista.get('_adjudicados') or {}
    for k, n in nodos.items():
        for f in str(n.get('fuente', '')).split(' | '):
            if f.strip() and f.strip() not in lista['fuentes']:
                fallos.append('%s: la fuente %r no esta en la lista canonica' % (k, f.strip()))
        if not str(n.get('etiqueta_arbol') or '').strip():
            fallos.append('%s: sin etiqueta_arbol (la pantalla caeria al titulo)' % k)
    for donde, texto in textos:
        bajo = normal(texto)
        for t, rx in pats.items():
            if rx.search(bajo) and '%s|%s' % (donde, t) not in adjudicados:
                fallos.append('%s: nombra el libro "%s"' % (donde, t))
    return fallos


def cargar_nodos():
    nodos = {}
    for p in glob.glob(os.path.join(RAIZ, 'dataset', 'nodos', '*.json')):
        n = json.load(io.open(p, encoding='utf-8'))
        if not n.get('deprecado'):
            nodos[n['node_id']] = n
    return nodos


def main():
    lista = json.load(io.open(LISTA, encoding='utf-8'))
    nodos = cargar_nodos()
    textos = list(textos_de_cara()) + list(textos_de_nodos(nodos))
    fallos = fallos_de(lista, nodos, textos)
    # caso negativo: un correo inventado que cita un libro tiene que fallar
    falso = [('prueba:correo', 'Como dice The Lean Startup, valida antes de construir.')]
    if not any(f.startswith('prueba:correo') for f in fallos_de(lista, {}, falso)):
        fallos.append('caso negativo: la guarda no detecto un texto con el titulo de un libro')
    if fallos:
        print('ROJO: %d fallos' % len(fallos))
        for f in fallos[:60]:
            print('  ' + f)
        return 1
    print('VERDE: %d fuentes con %d titulos; %d textos de cara al cliente barridos, ninguno nombra un libro; '
          '%d nodos vivos con etiqueta' % (len(lista['fuentes']), len(patrones(lista)), len(textos), len(nodos)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
