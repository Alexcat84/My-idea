# -*- coding: utf-8 -*-
"""Auditor v151: relectura propia del expediente. Tres piernas, escritas hoy."""
import json, re, subprocess, os, collections
BS = chr(92)
F=[json.loads(l) for l in open('docs/plan/OPERACIONES.jsonl',encoding='utf-8') if l.strip()]
ids=[f['id_op'] for f in F]
cuerpo={}
for base in ('scripts','engine','web/lib'):
    for dp,dn,fn in os.walk(base):
        dpn=dp.replace(BS,'/')
        if dpn.startswith('scripts/loop'): continue
        for x in fn:
            p=dpn+'/'+x
            try: cuerpo[p]=open(p,encoding='utf-8',errors='ignore').read()
            except Exception: pass
print('ficheros de codigo vivo barridos:', len(cuerpo))
def pal(i): return re.compile(r'(?<![A-Za-z0-9-])'+re.escape(i)+r'(?![A-Za-z0-9-])')
p2={}
for i in ids:
    rx=pal(i); p2[i]=[p for p,c in cuerpo.items() if rx.search(c)]
log=subprocess.run(['git','log','--format=%H|%s|%b','--name-only'],capture_output=True,text=True,errors='ignore').stdout
p3=collections.defaultdict(list); cur=None; msg=''; rutas=[]
bloques=[]
for linea in log.splitlines():
    if re.match(r'^[0-9a-f]{40}[|]', linea):
        if cur: bloques.append((cur,msg,rutas))
        partes=linea.split('|',2); cur=partes[0]; msg=' '.join(partes[1:]); rutas=[]
    elif cur is not None:
        if '/' in linea and not linea.startswith(' '): rutas.append(linea.strip())
        else: msg+=' '+linea
if cur: bloques.append((cur,msg,rutas))
print('commits leidos:', len(bloques))
for h,m,rr in bloques:
    if not any(r.startswith(('dataset/','scripts/','engine/','web/')) for r in rr): continue
    for i in ids:
        if pal(i).search(m): p3[i].append(h[:8])
sal=subprocess.run(['python','scripts/loop/tallar_estado_de_fase.py'],capture_output=True,text=True,errors='ignore')
txt=sal.stdout+sal.stderr
open('docs/loop/_auditor_v151_estado_de_fase.txt','w',encoding='utf-8').write(txt)
p1=set()
for i in ids:
    for linea in txt.splitlines():
        if pal(i).search(linea) and 'CUMPLIDO' in linea.upper(): p1.add(i)
MARCAS=('ESTADO','DIFERIDA','CONGELAD','SIGUE EN LISTA','NO SE MUEVE')
n1=n2=n3=0; nocalzan=[]; dec=0; sil=0; hsin=0
for f in F:
    i=f['id_op']; a=i in p1; b=bool(p2[i]); c=bool(p3[i])
    n1+=a; n2+=b; n3+=c; ejec=a or b or c
    if f['estado']=='HECHA' and not ejec: hsin+=1
    if f['estado']=='LISTA' and ejec:
        nocalzan.append(i)
        blob=(str(f.get('nota') or '')+' '+str(f.get('adjudicacion') or '')).upper()
        if any(m in blob for m in MARCAS): dec+=1
        else: sil+=1
print('fichas %d | NO CALZAN %d | calzan %d' % (len(F),len(nocalzan),len(F)-len(nocalzan)))
print('  DECLARADAS %d | EN SILENCIO %d' % (dec,sil))
print('  HECHA sin ninguna prueba: %d' % hsin)
print('cobertura: P1 %d / P2 %d / P3 %d' % (n1,n2,n3))
hechas={f['id_op'] for f in F if f['estado']=='HECHA'}
print('DESBLOQUEADAS:', [f['id_op'] for f in F if f['estado']=='LISTA' and all(d in hechas for d in (f.get('depende_de') or []))])
print('LISTA sin ninguna prueba:', [(f['id_op'],f['fase'],f.get('tipo'),f.get('depende_de')) for f in F if f['estado']=='LISTA' and not (f['id_op'] in p1 or p2[f['id_op']] or p3[f['id_op']])])
