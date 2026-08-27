# -*- coding: utf-8 -*-
"""Auditor vuelta 83: vuelca los textos crudos de dataset/nodos/*.json para la
relectura ciega. Los pares se LEEN del fichero del filtro, no se teclean."""
import json, sys, glob, os

FILTRO = 'docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V83.jsonl'

def cargar_nodos():
    idx = {}
    for p in glob.glob('dataset/nodos/**/*.json', recursive=True):
        try:
            d = json.load(open(p, encoding='utf-8'))
        except Exception:
            continue
        if isinstance(d, dict) and d.get('node_id'):
            idx[d['node_id']] = d
    return idx

def ficha(n, g, corto=False):
    out = []
    out.append('  ID: %s' % n)
    out.append('  TITULO: %s' % (g.get('titulo_concepto') or ''))
    out.append('  DOMINIO: %s' % (g.get('dominio') or ''))
    if not corto:
        out.append('  RESUMEN: %s' % ((g.get('resumen_teorico') or '')[:700]))
    out.append('  PASOS:')
    for i, p in enumerate(g.get('pasos_accionables') or [], 1):
        out.append('    %d. %s' % (i, p))
    out.append('  ENTREGABLE: %s' % (g.get('entregable_esperado') or ''))
    out.append('  PREVIOS: %s' % ', '.join(g.get('nodos_previos') or []))
    out.append('  SIGUIENTES: %s' % ', '.join(g.get('nodos_siguientes') or []))
    return '\n'.join(out)

def main():
    idxs = [int(a) for a in sys.argv[1:]]
    filas = [json.loads(l) for l in open(FILTRO, encoding='utf-8') if l.strip()]
    N = cargar_nodos()
    for i in idxs:
        r = filas[i]
        print('=' * 78)
        print('UNIDAD %d | dominio %s | paso %s' % (i, r['dominio'], r['paso']))
        print('PAR: %s -> %s' % (r['madre'], r['hijo']))
        print('TEXTO DEL PASO (del fichero del filtro): %s' % r['texto_paso'])
        print('-' * 78)
        print('MADRE')
        print(ficha(r['madre'], N[r['madre']]))
        print('-' * 78)
        print('HIJO')
        print(ficha(r['hijo'], N[r['hijo']]))
        print()

main()
