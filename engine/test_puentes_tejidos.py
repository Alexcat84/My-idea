# -*- coding: utf-8 -*-
"""GUARDA DE PUENTES: lo que aprueba el fichero es lo que teje el grafo (saneamiento, TANDA 2, punto 9, decision del
fundador del 26 sep 2026; AUD-09 M51 y M53, ficha puentes-reanclados-sin-tejer).

Hasta esta guarda, `validar_anclas_de_todos_los_puentes` (scripts/integrar_packs.py) y el chequeo de puentes de
scripts/run_phase1.py leian el FICHERO y ningun guardian miraba las aristas: 22 puentes aprobados no estaban tejidos y
61 aristas del nucleo a un mundo no las declaraba ningun fichero. Esta guarda exige, en cada mundo:
  1. que cada puente de packs/<mundo>/metadata/bridges_aprobados.json este tejido en el grafo (nucleo -> mundo);
  2. que cada arista viva del nucleo a ese mundo este aprobada en su fichero;
  3. la ley del ancla: ningun nodo del nucleo ancla mas de 2 puentes aprobados en el mismo mundo, y todo puente
     ancla en el nucleo y llega a un nodo vivo de su mundo;
  4. caso negativo: un puente aprobado sin tejer, una arista sin declarar y un ancla con 3 hacen fallar la guarda.

    python engine/test_puentes_tejidos.py
"""
import collections
import glob
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'scripts'))
from run_phase1 import aristas_a_simetrizar  # noqa: E402

TOPE_POR_ANCLA = 2


def fallos_de(nodos, aprobados):
    fallos = []
    vivos = {k for k, n in nodos.items() if not n.get('deprecado')}
    dom = {k: n.get('dominio') for k, n in nodos.items()}
    aristas = aristas_a_simetrizar(nodos)
    reales = collections.defaultdict(set)
    for a, b in aristas:
        if a in vivos and b in vivos and dom[a] == 'core' and dom[b] != 'core':
            reales[dom[b]].add((a, b))
    for mundo in sorted(set(aprobados) | set(reales)):
        ap = aprobados.get(mundo, [])
        pares = {(x['core'], x['dominio']) for x in ap}
        for a, b in sorted(pares - reales[mundo]):
            fallos.append('%s: el puente aprobado %s -> %s no esta tejido en el grafo' % (mundo, a, b))
        for a, b in sorted(reales[mundo] - pares):
            fallos.append('%s: la arista %s -> %s va del nucleo al mundo y ningun fichero la aprueba' % (mundo, a, b))
        for a, b in sorted(pares):
            if dom.get(a) != 'core' or a not in vivos:
                fallos.append('%s: el ancla %s no es un nodo vivo del nucleo' % (mundo, a))
            if dom.get(b) != mundo or b not in vivos:
                fallos.append('%s: el puente llega a %s, que no es un nodo vivo de %s' % (mundo, b, mundo))
        for ancla, n in sorted(collections.Counter(x['core'] for x in ap).items()):
            if n > TOPE_POR_ANCLA:
                fallos.append('%s: el ancla %s lleva %d puentes (ley del ancla: %d)' % (mundo, ancla, n, TOPE_POR_ANCLA))
    return fallos


def main():
    nodos = {}
    for p in glob.glob(os.path.join(RAIZ, 'dataset', 'nodos', '*.json')):
        n = json.load(io.open(p, encoding='utf-8'))
        nodos[n['node_id']] = n
    aprobados = {}
    for p in glob.glob(os.path.join(RAIZ, 'packs', '*', 'metadata', 'bridges_aprobados.json')):
        mundo = os.path.basename(os.path.dirname(os.path.dirname(p)))
        aprobados[mundo] = json.load(io.open(p, encoding='utf-8'))['aprobados']
    fallos = fallos_de(nodos, aprobados)

    # caso negativo: un grafo inventado con los tres defectos
    falso = {
        'c1': {'dominio': 'core', 'nodos_siguientes': ['q1', 'q2', 'q3']},
        'c2': {'dominio': 'core', 'nodos_siguientes': ['q4']},
        'q1': {'dominio': 'quality'}, 'q2': {'dominio': 'quality'}, 'q3': {'dominio': 'quality'},
        'q4': {'dominio': 'quality'}, 'q5': {'dominio': 'quality'},
    }
    ap_falso = {'quality': [{'core': 'c1', 'dominio': 'q1'}, {'core': 'c1', 'dominio': 'q2'},
                            {'core': 'c1', 'dominio': 'q3'}, {'core': 'c2', 'dominio': 'q5'}]}
    neg = ' | '.join(fallos_de(falso, ap_falso))
    for esperado in ('c2 -> q5 no esta tejido', 'c2 -> q4 va del nucleo', 'el ancla c1 lleva 3'):
        if esperado not in neg:
            fallos.append('caso negativo: la guarda no detecto "%s"' % esperado)

    if fallos:
        print('ROJO: %d fallos' % len(fallos))
        for f in fallos[:40]:
            print('  ' + f)
        return 1
    print('VERDE: %d puentes aprobados en %d mundos, todos tejidos; ninguna arista del nucleo a un mundo sin aprobar; '
          'ninguna ancla con mas de %d' % (sum(len(v) for v in aprobados.values()), len(aprobados), TOPE_POR_ANCLA))
    return 0


if __name__ == '__main__':
    sys.exit(main())
