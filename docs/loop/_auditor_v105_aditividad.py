import subprocess,json,difflib,glob
BASE='9cf7a06a'
def show(rev,path):
    return subprocess.run(['git','show',rev+':'+path],capture_output=True).stdout.decode('utf-8')
for path in ['docs/plan/04_ENLACES.md','docs/PENDIENTES.md']:
    a=show(BASE,path).splitlines(); b=open(path,encoding='utf-8').read().splitlines()
    sm=difflib.SequenceMatcher(None,a,b); dele=rep=ins=0
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=='delete': dele+=i2-i1
        elif tag=='replace': rep+=i2-i1
        elif tag=='insert': ins+=j2-j1
    print(path+': borradas %d / replace %d / +%d  (%d -> %d lineas)'%(dele,rep,ins,len(a),len(b)))
a=[json.loads(l) for l in show(BASE,'docs/plan/OPERACIONES.jsonl').splitlines() if l.strip()]
b=[json.loads(l) for l in open('docs/plan/OPERACIONES.jsonl',encoding='utf-8') if l.strip()]
print('OPERACIONES.jsonl: filas',len(a),'->',len(b),'| mismo orden de id_op:',[x['id_op'] for x in a]==[x['id_op'] for x in b])
tocadas=[];est=0
for x,y in zip(a,b):
    difs=[k for k in set(x)|set(y) if x.get(k)!=y.get(k)]
    if difs: tocadas.append((x['id_op'],difs))
    if x.get('estado')!=y.get('estado'): est+=1
print('filas tocadas:',tocadas); print('filas con estado cambiado:',est)
for idop,difs in tocadas:
    xa=[x for x in a if x['id_op']==idop][0]; yb=[y for y in b if y['id_op']==idop][0]
    for k in difs:
        va,vb=str(xa.get(k)),str(yb.get(k))
        print('  %s.%s: %d -> %d chars | prefijo estricto: %s'%(idop,k,len(va),len(vb),vb.startswith(va) and len(vb)>len(va)))
for f in sorted(glob.glob('docs/plan/OP_E_03_LECTURA_TRAMO*_V*.jsonl')):
    fp=f.replace(chr(92),'/')
    fa=[json.loads(l) for l in show(BASE,fp).splitlines() if l.strip()]
    fb=[json.loads(l) for l in open(f,encoding='utf-8') if l.strip()]
    ch=[]
    for x,y in zip(fa,fb):
        perd=[k for k in x if k not in y]; cam=[k for k in x if k in y and x[k]!=y[k]]; gan=[k for k in y if k not in x]
        if perd or cam or gan: ch.append((x['puesto_tramo'],'PERDIDAS'+str(perd) if perd else '','CAMBIADAS'+str(cam) if cam else '','gana'+str(gan)))
    print(fp.split('/')[-1],'filas',len(fa),'->',len(fb),'| cambios:',ch)
