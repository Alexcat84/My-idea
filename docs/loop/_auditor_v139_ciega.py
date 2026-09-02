# -*- coding: utf-8 -*-
"""CIEGA DEL AUDITOR, VUELTA 139. Imprime el texto de la pieza del absorbido y
TODOS los pasos/condiciones del superviviente TAL COMO ESTABAN ANTES de la
fusion, SIN la marca que el ejecutor le puso. El auditor adjudica su marca y
solo despues se destapa."""
import json, subprocess, sys, io
CASOS = [('OP-M-01-FUSION','OPM01FUSION','3f249a03','sistema_gates_go_kill'),
         ('OP-M-03-III','OPM03III','495c140e','pivote_estrategico'),
         ('OP-M-05-INDICE','OPM05INDICE','c351cc30','customer_discovery'),
         ('OP-M-05-EDIFICIO','OPM05EDIFICIO','4f2e151b','customer_discovery_get_out_of_building'),
         ('OP-M-05-APERTURA','OPM05APERTURA','6c976514','customer_validation')]
def blob(ref, nid):
    for p in ('dataset/nodos/%s.json'%nid,'dataset/nodos/core/%s.json'%nid):
        r=subprocess.run(['git','show','%s:%s'%(ref,p)],capture_output=True)
        if r.returncode==0: return json.loads(r.stdout.decode('utf-8'))
    return None
def lista(d,bloque):
    return list(d.get('pasos_accionables' if bloque=='pasos' else 'condiciones_activacion') or [])
revelar = '--revelar' in sys.argv
out=[]
for op,slug,commit,sup in CASOS:
    plan=json.load(open('docs/loop/PLAN_V139_%s.json'%slug,encoding='utf-8'))
    acto=plan['actos'][0]
    nsup=blob(commit+'^',sup)
    out.append('='*78)
    out.append('%s | superviviente %s (ANTES de fundir)'%(op,sup))
    for b in ('pasos','condiciones'):
        for i,t in enumerate(lista(nsup,b),1):
            out.append('   SUP %s %d: %s'%(b[:4].upper(),i,t))
    for absid, marcas in (acto.get('pasos') or {}).items():
        nab=blob(commit+'^',absid)
        for k in sorted(marcas,key=int):
            t=lista(nab,'pasos')[int(k)-1]
            out.append('  --- PIEZA: paso %s de %s'%(k,absid))
            out.append('      %s'%t)
            if revelar: out.append('      >>> MARCA DEL EJECUTOR: %s'%marcas[k])
    for absid, marcas in (acto.get('condiciones') or {}).items():
        nab=blob(commit+'^',absid)
        for k in sorted(marcas,key=int):
            t=lista(nab,'condiciones')[int(k)-1]
            out.append('  --- PIEZA: condicion %s de %s'%(k,absid))
            out.append('      %s'%t)
            if revelar: out.append('      >>> MARCA DEL EJECUTOR: %s'%marcas[k])
io.open('docs/loop/_auditor_v139_ciega_%s.txt'%('reveal' if revelar else 'blind'),'w',encoding='utf-8').write('\n'.join(out))
print('escrito, %d lineas'%len(out))
