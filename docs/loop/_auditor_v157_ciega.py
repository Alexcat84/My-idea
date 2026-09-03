# -*- coding: utf-8 -*-
"""Ciega de la vuelta 157. Imprime SOLO titulo y pasos accionables de los dos
nodos. Sin clase, sin via, sin cita y sin razon."""
import json, sys, ast, re
sys.stdout.reconfigure(encoding='utf-8')
G=json.load(open('dataset/metadata/master_graph.json',encoding='utf-8')); N=G['nodos']
def lista(v):
    if v is None: return []
    if isinstance(v,list): return v
    if isinstance(v,str):
        v=v.strip()
        if not v: return []
        try:
            r=ast.literal_eval(v); return list(r) if isinstance(r,(list,tuple)) else [r]
        except Exception: return [v]
    return []
REG=[json.loads(l) for l in open('docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl',encoding='utf-8') if l.strip()]
por_id={}
for e in REG:
    m=re.match(r'(LD-OPC05-\d+)', e.get('cita','') or '')
    if m: por_id[m.group(1)]=e
pedidos=sys.argv[1:]
if pedidos and pedidos[0]=='--nomina':
    print(' '.join(sorted(por_id))); sys.exit()
for i in pedidos:
    e=por_id.get(i)
    if not e: print('NO ESTA', i); continue
    a,b=e['par']
    print('='*78); print('CASO %s'%i)
    for nid in (a,b):
        n=N.get(nid) or {}
        print('-'*70)
        print('NODO: %s'%nid)
        print('TITULO: %s'%n.get('titulo_concepto'))
        print('FUENTE: %s'%n.get('fuente'))
        print('ENTREGABLE: %s'%n.get('entregable_esperado'))
        for j,p in enumerate(lista(n.get('pasos_accionables')),1):
            print('  paso %d: %s'%(j,p))
    print()
