# -*- coding: utf-8 -*-
"""GUARDA DE JURISDICCION: ningun nodo vivo con contenido de un pais queda sin clase.

Decision del fundador del 26 sep 2026 (saneamiento del dataset, tanda 1, punto 3; docs/POLITICA_MARCO_PAIS.md).
La clase no se deduce: se DECLARA en dataset/metadata/jurisdiccion.json (pais y clase A, B o C, con su motivo).
Esta guarda exige:
  1. que cada entrada sea de un nodo vivo, con clase A, B o C, un pais conocido y motivo;
  2. que todo nodo vivo cuyo texto tenga una marca fuerte de pais (Estados Unidos, EE.UU., un organismo como OSHA,
     IRS, FDA, FTC, la Union Europea...) este en la lista con su clase, o adjudicado como sin pais en
     `_adjudicados_sin_pais` con su motivo (una mencion que no es contenido de pais, por ejemplo una empresa de ejemplo);
  3. caso negativo: un nodo con una marca de pais fuera de la lista hace fallar la guarda.

    python engine/test_jurisdiccion.py
"""
import glob
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTA = os.path.join(RAIZ, 'dataset', 'metadata', 'jurisdiccion.json')
PAISES = {'US', 'EU', 'CA', 'GB', 'FR', 'MX', 'ES', 'CO', 'AR'}  # con sus formas en web/lib/i18n/mensajes/avisoNodo.ts
MARCA = re.compile(
    r'EE\.?\s?UU\.?|Estados Unidos|estadounidense|\bOSHA\b|\bIRS\b|\bFDA\b|\bEPA\b|\bFTC\b|\bSBA\b|\bUSPTO\b|\bNIOSH\b'
    r'|\bUSDA\b|\bEEOC\b|\bCPSC\b|Uni[oó]n Europea|\bRGPD\b|\bGDPR\b|Reino Unido|Canad[aá]\b')


def texto(n):
    partes = [n.get('titulo_concepto', ''), n.get('resumen_teorico', ''), n.get('entregable_esperado', '')]
    return '\n'.join(partes + list(n.get('pasos_accionables') or []) + list(n.get('condiciones_activacion') or []))


def fallos_de(lista, nodos):
    fallos = []
    entradas = lista.get('nodos') or {}
    sin_pais = lista.get('_adjudicados_sin_pais') or {}
    for k, e in entradas.items():
        n = nodos.get(k)
        if n is None or n.get('deprecado'):
            fallos.append('%s: no es un nodo vivo' % k)
        if e.get('clase') not in ('A', 'B', 'C'):
            fallos.append('%s: clase %r' % (k, e.get('clase')))
        if e.get('pais') not in PAISES and not (e.get('clase') == 'A' and e.get('pais') == 'INT'):
            fallos.append('%s: pais %r sin sus formas en los once idiomas' % (k, e.get('pais')))
        if not str(e.get('motivo', '')).strip():
            fallos.append('%s: sin motivo' % k)
    for k, m in sin_pais.items():
        if not str(m).strip():
            fallos.append('%s: adjudicado sin pais sin motivo' % k)
    for k, n in nodos.items():
        if n.get('deprecado'):
            continue
        if MARCA.search(texto(n)) and k not in entradas and k not in sin_pais:
            fallos.append('%s: tiene contenido de pais y no tiene clase' % k)
    return fallos


def main():
    lista = json.load(io.open(LISTA, encoding='utf-8'))
    nodos = {}
    for p in glob.glob(os.path.join(RAIZ, 'dataset', 'nodos', '*.json')):
        n = json.load(io.open(p, encoding='utf-8'))
        nodos[n['node_id']] = n
    fallos = fallos_de(lista, nodos)
    # caso negativo: un nodo inventado con OSHA y sin clase tiene que fallar
    falso = dict(nodos)
    falso['__prueba_sin_clase__'] = {'node_id': '__prueba_sin_clase__', 'titulo_concepto': 'x',
                                     'resumen_teorico': 'Reporta a OSHA en 8 horas.', 'pasos_accionables': [],
                                     'condiciones_activacion': [], 'entregable_esperado': ''}
    if not any('__prueba_sin_clase__' in f for f in fallos_de(lista, falso)):
        fallos.append('caso negativo: la guarda no detecto un nodo con OSHA sin clase')
    if fallos:
        print('ROJO: %d fallos' % len(fallos))
        for f in fallos[:40]:
            print('  ' + f)
        return 1
    print('VERDE: %d nodos con clase de pais (%s), %d adjudicados sin pais, ninguno con pais sin clase' % (
        len(lista['nodos']), ', '.join('%s %d' % (c, sum(1 for e in lista['nodos'].values() if e['clase'] == c)) for c in 'ABC'),
        len(lista.get('_adjudicados_sin_pais') or {})))
    return 0


if __name__ == '__main__':
    sys.exit(main())
