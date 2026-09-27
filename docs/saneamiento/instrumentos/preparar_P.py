# -*- coding: utf-8 -*-
"""Pasada P del saneamiento (TANDA 2, punto 9, decision del fundador del 26 sep 2026): las aristas vivas del nucleo a
un mundo que NINGUN bridges_aprobados declara. Cada una se lee: PUENTE (se declara en el fichero del mundo, dentro de la
ley del ancla) o RETIRAR. Lector con trampas, verificador ciego y arbitro. Solo lectura del repo.

Trampas, dos por lote:
  FALSO: un nodo del nucleo con un nodo del mundo que no tiene nada que ver (tiene que salir RETIRAR);
  APROBADO: un puente que el fichero ya aprueba y el grafo ya teje (tiene que salir PUENTE).

Uso: python preparar_P.py <repo> <W>"""
import glob
import hashlib
import io
import json
import os
import random
import sys

REPO, W = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(REPO, 'scripts'))
from run_phase1 import aristas_a_simetrizar  # noqa: E402

nodos = {}
for p in glob.glob(os.path.join(REPO, 'dataset/nodos/*.json')):
    n = json.load(io.open(p, encoding='utf-8'))
    nodos[n['node_id']] = n
vivos = {k for k, n in nodos.items() if not n.get('deprecado')}
dom = {k: n['dominio'] for k, n in nodos.items()}
aprob = {}
for p in glob.glob(os.path.join(REPO, 'packs/*/metadata/bridges_aprobados.json')):
    d = os.path.basename(os.path.dirname(os.path.dirname(p)))
    aprob[d] = {(x['core'], x['dominio']) for x in json.load(io.open(p, encoding='utf-8'))['aprobados']}
todos = set().union(*aprob.values())
E = aristas_a_simetrizar(nodos)
reales = sorted((a, b) for a, b in E if a in vivos and b in vivos and dom[a] == 'core' and dom[b] != 'core')
fuera = [e for e in reales if e not in todos]
tejidos = [e for e in reales if e in todos]
MUNDO = {'quality': 'gestion de la calidad', 'health_safety': 'seguridad y salud en el trabajo',
         'environmental': 'gestion ambiental', 'compras': 'compras y proveedores', 'entrega': 'logistica y entrega',
         'risk_management': 'gestion de riesgos', 'seguridad_digital': 'seguridad digital', 'exportacion': 'exportacion',
         'franquicias': 'franquicias'}


def ficha(i):
    n = nodos[i]
    pasos = ' / '.join((n.get('pasos_accionables') or [])[:4])
    return 'titulo: %s\n  resumen: %s\n  pasos: %s' % (n['titulo_concepto'], n['resumen_teorico'], pasos)


N = 3
azar = random.Random(20260929)
orden = fuera[:]
azar.shuffle(orden)
lotes = {'P%d' % (i + 1): orden[i::N] for i in range(N)}
os.makedirs(os.path.join(W, 'P', 'lotes'), exist_ok=True)
os.makedirs(os.path.join(W, 'P', 'claves'), exist_ok=True)
args = {}
nucleo = sorted(k for k in vivos if dom[k] == 'core')
for l, pares in sorted(lotes.items()):
    az = random.Random(int(hashlib.sha256(('P' + l).encode()).hexdigest()[:8], 16))
    items = [(a, b, None) for a, b in pares]
    t = az.choice(tejidos)
    items.append((t[0], t[1], 'APROBADO'))
    while True:
        a = az.choice(nucleo)
        b = az.choice(sorted(k for k in vivos if dom[k] == 'health_safety'))
        if (a, b) not in E and (b, a) not in E:
            break
    items.append((a, b, 'FALSO'))
    az.shuffle(items)
    mapa, txt, trampas = {}, ['# Lote %s: %d aristas del nucleo a un mundo\n' % (l, len(items))], {}
    for i, (a, b, tipo) in enumerate(items, 1):
        cid = '%s-%02d' % (l, i)
        mapa[cid] = {'core': a, 'mundo': b, 'dominio': dom[b], 'trampa': tipo}
        if tipo:
            trampas[cid] = tipo
        txt.append('### %s\n- NODO DEL NUCLEO\n  %s\n- NODO DEL MUNDO "%s"\n  %s\n' % (cid, ficha(a), MUNDO[dom[b]], ficha(b)))
    io.open(os.path.join(W, 'P', 'lotes', 'lote_%s.md' % l), 'w', encoding='utf-8').write('\n'.join(txt))
    json.dump(mapa, io.open(os.path.join(W, 'P', 'claves', 'mapa_%s.json' % l), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    args[l] = {'n': len(items), 'trampas': trampas}
json.dump({'fuera': len(fuera), 'lotes': args}, io.open(os.path.join(W, 'P', 'args.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('aristas nucleo a mundo fuera de todo aprobados:', len(fuera), '| lotes', json.dumps(args))
