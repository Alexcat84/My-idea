# -*- coding: utf-8 -*-
"""Impresor CIEGO del auditor de la vuelta 158, escrito hoy y sin importar
codigo de la casa. Imprime SOLO titulo, fuente, entregable y pasos accionables
de los dos nodos de cada par. NO imprime clase, ni via, ni cita, ni razon."""
import json, sys, re, io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
g=json.load(open('dataset/metadata/master_graph.json',encoding='utf-8'))['nodos']
reg=[json.loads(l) for l in open('docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl',encoding='utf-8') if l.strip()]
por_id={}
for r in reg:
    m=re.match(r'(LD-OPC05-\d+)', r['cita'])
    if m: por_id[m.group(1)]=r
pedidos=sys.argv[1:]
def nodo(nid):
    n=g.get(nid)
    if n is None:
        for k,v in g.items():
            if k.lower()==nid.lower(): n=v; break
    return n
for p in pedidos:
    k='LD-OPC05-%03d'%int(p)
    r=por_id.get(k)
    if not r: print('== %s NO ESTA EN EL REGISTRO'%k); continue
    print('='*78); print('CASO %s'%k)
    for nid in r['par']:
        n=nodo(nid)
        print('-'*70)
        print('NODO: %s'%nid)
        if n is None: print('  (no esta en el grafo)'); continue
        print('  titulo    : %s'%n.get('titulo_concepto'))
        print('  fuente    : %s'%n.get('fuente'))
        print('  entregable: %s'%n.get('entregable_esperado'))
        print('  deprecado : %s'%bool(n.get('deprecado')))
        for i,s in enumerate(n.get('pasos_accionables') or [],1):
            print('   paso %d: %s'%(i,s))
    print()
