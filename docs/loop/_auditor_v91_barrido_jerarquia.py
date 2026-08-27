# -*- coding: utf-8 -*-
"""VARA PROPIA DEL AUDITOR, VUELTA 91. Barre las 88 razones de la bolsa de
OP-E-07 buscando FORMULAS QUE NIEGAN LA JERARQUIA (las que mandan al par
FUERA de la operacion segun su propia `verificacion`), no las que la afirman."""
import io, json, re, os
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V = {}
for l in io.open(os.path.join(RAIZ,'docs','INTRA_DOMINIO_VEREDICTOS.jsonl'), encoding='utf-8'):
    l=l.strip()
    if l:
        d=json.loads(l); V[int(d['puesto_intra'])]=d
EJ=[json.loads(l) for l in io.open(os.path.join(RAIZ,'docs','plan','OP_E_07_DIRECCION_V91.jsonl'), encoding='utf-8')]
NEGACIONES = [
    r"NO CREA JERARQUIA", r"no crea jerarquia",
    r"ninguno la expande", r"NINGUNO LA EXPANDE",
    r"ninguno de los dos la expande",
    r"cada uno trae lo suyo",
    r"no tiene en ninguna forma", r"que el otro no tiene",
    r"no hay jerarquia", r"NO HAY JERARQUIA",
    r"9\.22", r"ENLACE MUTUO", r"enlace mutuo",
    r"sin jerarquia", r"no la desarrolla", r"ninguno desarrolla",
]
RE=[(p,re.compile(p)) for p in NEGACIONES]
hits={}
for e in EJ:
    p=int(e['puesto']); r=V[p]['razon']
    m=[pat for pat,rx in RE if rx.search(r)]
    if m: hits[p]=m
for p in sorted(hits):
    print('puesto %-6s %s' % (p, ' | '.join(sorted(set(hits[p])))))
print()
print('TOTAL de las 88 con alguna formula que niega jerarquia:', len(hits))
