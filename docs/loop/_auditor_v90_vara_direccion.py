# -*- coding: utf-8 -*-
"""VARA PROPIA DEL AUDITOR, vuelta 90. No copia el instrumento del ejecutor.
Criterio unico e independiente: en la razon, el id que aparece INMEDIATAMENTE
ANTES de la formula "trae el procedimiento" es el HIJO; el otro id del par es
la madre. Si la formula no aparece, o si el id mas cercano antes de ella no es
uno de los dos del par, la fila queda SIN VEREDICTO y se declara."""
import json, io, re
VER = {}
for l in io.open('docs/INTRA_DOMINIO_VEREDICTOS.jsonl', encoding='utf-8'):
    if l.strip():
        v = json.loads(l); VER[v['puesto_intra']] = v
DIR = {}
for l in io.open('docs/plan/OP_E_06_DIRECCION_V90.jsonl', encoding='utf-8'):
    if l.strip():
        d = json.loads(l); DIR[d['puesto']] = d
BOL = {}
for l in io.open('docs/plan/OP_E_06_REBASE_V90.jsonl', encoding='utf-8'):
    if l.strip():
        f = json.loads(l); BOL[f['puesto']] = f

coincide = discrepa = sin_veredicto = 0
lineas = []
for p in sorted(BOL):
    if p not in DIR:
        lineas.append('%-6d EXCLUIDO de la direccion (no esta en OP_E_06_DIRECCION_V90)' % p); continue
    v = VER[p]; d = DIR[p]
    a, b = v['nodo_a'], v['nodo_b']
    razon = v['razon']
    m = re.search(r'trae el procedimiento', razon)
    if not m:
        sin_veredicto += 1
        lineas.append('%-6d SIN VEREDICTO DE MI VARA (no dice "trae el procedimiento")  ejecutor: %s -> %s' % (p, d['madre'], d['hijo']))
        continue
    antes = razon[:m.start()]
    pos_a, pos_b = antes.rfind(a), antes.rfind(b)
    if pos_a < 0 and pos_b < 0:
        sin_veredicto += 1
        lineas.append('%-6d SIN VEREDICTO DE MI VARA (ningun id del par antes de la formula)  ejecutor: %s -> %s' % (p, d['madre'], d['hijo']))
        continue
    hijo_mio = a if pos_a > pos_b else b
    madre_mia = b if hijo_mio == a else a
    if (madre_mia, hijo_mio) == (d['madre'], d['hijo']):
        coincide += 1
    else:
        discrepa += 1
        lineas.append('%-6d DISCREPA  mi vara: %s -> %s   ejecutor: %s -> %s' % (p, madre_mia, hijo_mio, d['madre'], d['hijo']))
print('\n'.join(lineas))
print()
print('=' * 78)
print('filas de la bolsa V90:', len(BOL), '| filas con direccion del ejecutor:', len(DIR))
print('MI VARA: coinciden %d | discrepan %d | sin veredicto de mi vara %d' % (coincide, discrepa, sin_veredicto))
print('=' * 78)
