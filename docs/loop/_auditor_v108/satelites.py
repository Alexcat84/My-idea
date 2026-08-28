import json, os, sys, re
sys.path.insert(0,os.path.join('scripts','loop'))
import verificar_cobertura_bolsa_tres_vias as m
import contar_cierre_efectivo as cce
# veredicto por puesto y por fichero
RE_B_CAB=re.compile(r"^--- PUESTO (\d+) ---")
RE_B_VER=re.compile(r"VEREDICTO:\s*(OBJETO|SATELITE|NO_OBJETO)\b")
RE_T=re.compile(r"^(\d+)\s*\|.*\|\s*(OBJETO|SATELITE|NO_OBJETO)\b")
por_fichero={}
for nombre,fmt in m.FICHEROS_VEREDICTO:
    txt=open(os.path.join('docs','loop',nombre),encoding='utf-8').read()
    d={}
    if fmt=='bloque':
        act=None
        for l in txt.splitlines():
            c=RE_B_CAB.match(l)
            if c: act=int(c.group(1)); continue
            if not l.strip(): act=None; continue
            v=RE_B_VER.search(l)
            if act is not None and v: d[act]=v.group(1); act=None
    else:
        for l in txt.splitlines():
            t=RE_T.match(l)
            if t: d[int(t.group(1))]=t.group(2)
    por_fichero[nombre]=d
vivas=m.vivas_de_hoy([])
sat=set()
for n,d in por_fichero.items():
    for p,v in d.items():
        if v=='SATELITE': sat.add(p)
print('puestos con ALGUN veredicto SATELITE en la historia:', sorted(sat))
print('de esos, RESUELTA vivas HOY:', sorted(sat & vivas))
print()
print('VUELCOS (mismo puesto, veredicto distinto en dos ficheros):')
todos={}
for n,d in por_fichero.items():
    for p,v in d.items(): todos.setdefault(p,[]).append((n,v))
vuelcos=0
for p in sorted(todos):
    vs={v for _,v in todos[p]}
    if len(vs)>1:
        vuelcos+=1
        print('  puesto %d  (vivo hoy: %s)' % (p, p in vivas), ' | '.join('%s=%s'%(n.replace('SALIDA_','').replace('_TRES_VIAS','').replace('.txt','').replace('.md',''),v) for n,v in todos[p]))
print('total vuelcos:', vuelcos)
