# -*- coding: utf-8 -*-
"""Censo propio del auditor v112: de las NO RESUELTA de hoy, cuantas traen
ya una correccion_vNN declarada y cuantas nunca fueron reabiertas."""
import io, json, glob, os, re, collections
RUTAS = sorted(glob.glob('docs/plan/OP_E_03_LECTURA_TRAMO*.jsonl'))
filas = []
for r in RUTAS:
    for ln in io.open(r, encoding='utf-8'):
        if ln.strip():
            filas.append(json.loads(ln))
print('n total', len(filas))
no_res = [d for d in filas if not d.get('direccion_leida')]
res = [d for d in filas if d.get('direccion_leida')]
print('RESUELTA', len(res), 'NO RESUELTA', len(no_res))
RE = re.compile(r'correccion_v\d+', re.I)
con = [d for d in no_res if RE.search(json.dumps(d, ensure_ascii=False))]
sin = [d for d in no_res if not RE.search(json.dumps(d, ensure_ascii=False))]
print('NO RESUELTA con correccion_vNN', len(con))
print('NO RESUELTA nunca reabiertas', len(sin))
print('reparto por dominio de las nunca reabiertas:',
      dict(collections.Counter(d['dominio'] for d in sin).most_common()))
puestos = sorted(d['puesto_tramo'] for d in sin)
print('puestos:', puestos)
print('primeros 80:', puestos[:80])
print('los 8 que quedan:', puestos[80:])
