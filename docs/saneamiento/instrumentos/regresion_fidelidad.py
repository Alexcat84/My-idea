# -*- coding: utf-8 -*-
"""REGRESION POR FIDELIDAD (anadido del fundador al diagnostico, 26 sep 2026), solo lectura.
Cruza las 487 correcciones de la campania con los nodos de clase B y C de la politica de pais.
Clase de un nodo: por las listas del repo (packs/_core/poda/_reencuadre_clase.json = B, _frontera_eeuu.json,
_cierre_ftc.json, _revive_pais.json y falsos_positivos_adjudicados NODO-FRONTERA o POLITICA DE PAIS = C,
packs/exportacion/metadata/auditoria_copyright.json punteros_jurisdiccionales = A o vigencia) y, fuera de las
listas, por su texto ANTES de la campania (condicion de pais = C; formula de localizacion = B).
Uso: python regresion_fidelidad.py <repo> <salida.json>"""
import glob
import io
import json
import os
import re
import sys

REPO, SALIDA = sys.argv[1], sys.argv[2]
MARCA_B = re.compile(r'en tu (?:pa[ií]s|mercado|jurisdicci[oó]n)|equivalente (?:en|de) tu|autoridad equivalente|organismo equivalente|averigua[^.]{0,80}(?:tu pa[ií]s|tu mercado)|pregunta[^.]{0,40}tu mercado')
MARCA_C = re.compile(r'(?:[Ss]i|[Ss]olo si)[^.]{0,80}(?:Estados Unidos|EE\.?\s?UU)')
PAIS = re.compile(r'EE\.?\s?UU\.?|Estados Unidos|estadounidense|\bIRS\b|\bOSHA\b|\bFDA\b|\bEPA\b|\bFTC\b|\bSEC\b|\bSBA\b|federal')


def ids_de(ruta, clave=None):
    try:
        d = json.load(io.open(os.path.join(REPO, ruta), encoding='utf-8'))
    except (OSError, ValueError):
        return set()
    if clave:
        d = d.get(clave, d)
    if isinstance(d, dict):
        for k in ('sobrevivientes', 'ids', 'nodos', 'node_ids', 'lista'):
            if k in d and isinstance(d[k], list):
                d = d[k]
                break
        else:
            d = [k for k in d if not k.startswith('_')]
    salida = set()
    for x in d:
        salida.add(x if isinstance(x, str) else (x.get('node_id') or x.get('id') or ''))
    return salida - {''}


listas_C = set()
for r in ('packs/_core/poda/_frontera_eeuu.json', 'packs/_core/poda/_cierre_ftc.json', 'packs/_core/poda/_revive_pais.json'):
    listas_C |= ids_de(r)
listas_B = ids_de('packs/_core/poda/_reencuadre_clase.json')
listas_A = ids_de('packs/exportacion/metadata/auditoria_copyright.json', 'punteros_jurisdiccionales')
fp = json.load(io.open(os.path.join(REPO, 'dataset/metadata/falsos_positivos_adjudicados.json'), encoding='utf-8'))
for a in fp.get('adjudicados', []):
    m = a.get('motivo', '')
    if 'NODO-FRONTERA' in m or 'POLITICA DE PAIS' in m:
        listas_C.add(a['node_id'])
print('listas: C', len(listas_C), 'B', len(listas_B), 'A/vigencia', len(listas_A))

filas = []
nodos_tocados = set()
for p in sorted(glob.glob(os.path.join(REPO, 'dataset/nodos/*.json'))):
    n = json.load(io.open(p, encoding='utf-8'))
    corr = n.get('correcciones') or []
    if not corr:
        continue
    k = n['node_id']
    # el texto ANTES de la campania: se deshacen las correcciones sobre el texto de hoy
    antes_cond = ' '.join(n.get('condiciones_activacion') or [])
    for c in corr:
        if c['campo'] == 'condiciones_activacion':
            antes_cond = antes_cond.replace(c['texto_nuevo'], c['texto_anterior'])
    texto_hoy = json.dumps(n, ensure_ascii=False)
    clase = ('C' if k in listas_C else 'B' if k in listas_B else 'A' if k in listas_A else
             'C_texto' if MARCA_C.search(antes_cond) else None)
    for c in corr:
        ant, nue = c['texto_anterior'], c['texto_nuevo']
        f = {'node_id': k, 'deprecado': bool(n.get('deprecado')), 'clase': clase, 'id': c['id'], 'campo': c['campo'],
             'veredicto': c['veredicto'],
             'quita_B': bool(MARCA_B.search(ant)) and not MARCA_B.search(nue),
             'quita_C': bool(MARCA_C.search(ant)) and not MARCA_C.search(nue),
             'quita_pais': bool(PAIS.search(ant)) and not PAIS.search(nue),
             'pone_B': not MARCA_B.search(ant) and bool(MARCA_B.search(nue)),
             'pone_pais': not PAIS.search(ant) and bool(PAIS.search(nue)),
             'anterior': ant, 'nuevo': nue}
        filas.append(f)
        if clase:
            nodos_tocados.add(k)
json.dump(filas, io.open(SALIDA, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
en_clase = [f for f in filas if f['clase']]
print('correcciones:', len(filas), '| sobre nodos con clase de pais:', len(en_clase), 'en', len(nodos_tocados), 'nodos')
for cl in ('A', 'B', 'C', 'C_texto'):
    sub = [f for f in en_clase if f['clase'] == cl]
    print('  clase %-7s correcciones %3d en %3d nodos' % (cl, len(sub), len(set(f['node_id'] for f in sub))))
for eti in ('quita_B', 'quita_C', 'quita_pais', 'pone_B', 'pone_pais'):
    sub = [f for f in en_clase if f[eti]]
    print('%-10s en nodos con clase: %d  %s' % (eti, len(sub), [(f['node_id'], f['id'], f['clase']) for f in sub][:8]))
sub = [f for f in filas if not f['clase'] and (f['quita_C'] or f['quita_B'])]
print('fuera de clase, quita B o C:', len(sub), [(f['node_id'], f['id']) for f in sub][:8])
sub = [f for f in en_clase if f['clase'].startswith('C') and f['pone_B']]
print('REGRESION clase C que recibe formula B:', len(sub), [(f['node_id'], f['id']) for f in sub])
