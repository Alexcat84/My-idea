# -*- coding: utf-8 -*-
"""GUARDA DE FUENTES INTERNAS (decisiones del fundador del 27 sep 2026, puntos 1 y 4).

Cada nodo vivo lleva en `fuentes_internas` TODOS los libros de los que viene: el suyo y los de todo lo que absorbio,
por cualquier fusion y en cadena, sin limite. Esta guarda exige:
  1. que el campo y el inventario interno (docs/internos/INVENTARIO_FUENTES.md) esten al dia con lo que calcula
     scripts/fuentes_internas.py (una fusion nueva sin recalcular hace fallar la guarda);
  2. que la primera fuente sea la del propio nodo (el campo `fuente` no se toca) y que cada libro este en la lista
     canonica (dataset/metadata/fuentes_canonicas.json), para que la guarda de titulos lo conozca;
  3. caso negativo: una cadena inventada de cuatro fusiones por cuatro vias distintas (ids_alias de un deprecado,
     merge_decisions, un mapa de capas y el historial) entrega los cuatro libros, y un nodo que pierde uno falla.

    python engine/test_fuentes_internas.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'scripts'))
import fuentes_internas as fi  # noqa: E402


def main():
    fallos = []
    nodos, *resto = fi.cargar()
    resultado, absorbidos, sin_fuente = fi.calcular(nodos, *resto)
    for k, v in resultado.items():
        if nodos[k].get('fuentes_internas') != v:
            fallos.append('%s: fuentes_internas desfasadas (corre python scripts/fuentes_internas.py)' % k)
        propias = fi.partes(nodos[k].get('fuente'))
        if v[:len(propias)] != propias:
            fallos.append('%s: la lista no empieza por la fuente propia del nodo' % k)
        for f in v:
            if f not in fi.CANON:
                fallos.append('%s: el libro %r no esta en la lista canonica' % (k, f))
    for k, n in nodos.items():
        if n.get('deprecado') and 'fuentes_internas' in n:
            fallos.append('%s: un deprecado no lleva fuentes_internas (las lleva quien lo absorbio)' % k)
    if fi.main(['--comprobar']) != 0:
        fallos.append('el inventario interno no esta al dia')

    # caso negativo: vivo <- deprecado (ids_alias) <- perdedor de un cluster <- id de capa <- id historico
    falsos = {
        'vivo': {'node_id': 'vivo', 'fuente': 'Libro A', 'ids_alias': ['dep']},
        'dep': {'node_id': 'dep', 'fuente': 'Libro B', 'deprecado': True},
    }
    decisiones = [{'losers': ['perdedor'], 'canonical_id': 'dep'}]
    originales = {'perdedor': ['Libro C']}
    capas = {'capa': 'perdedor', 'fantasma_sin_libro': 'vivo'}
    historicas = {'capa': {'fuente': 'Libro D'}}
    r, a, s = fi.calcular(falsos, originales, decisiones, capas, {}, historicas)
    v = r.get('vivo') or []
    if v[:1] != ['Libro A'] or sorted(v) != ['Libro A', 'Libro B', 'Libro C', 'Libro D']:
        fallos.append('caso negativo: la cadena de cuatro fusiones entrego %r' % r.get('vivo'))
    if s != ['fantasma_sin_libro']:
        fallos.append('caso negativo: el id sin libro no se conto aparte: %r' % s)

    if fallos:
        print('ROJO: %d fallos' % len(fallos))
        for f in fallos[:40]:
            print('  ' + f)
        return 1
    print('VERDE: %d nodos vivos con todos sus libros (%d con mas de uno); %d ids absorbidos sin libro, contados aparte' % (
        len(resultado), sum(1 for v in resultado.values() if len(v) > 1), len(sin_fuente)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
