# CIEGA DEL AUDITOR, VUELTA 153. Imprime PRIMERO los pasos; la razon va aparte.
import json,glob,sys
nodos={}
for f in glob.glob('dataset/nodos/*.json'):
    d=json.load(open(f,encoding='utf-8'))
    nodos[d['node_id']]=d
reg=[]
for l in open('docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl',encoding='utf-8'):
    if l.strip(): reg.append(json.loads(l))
por_cita={e['cita'].split(',')[0].strip():e for e in reg}
ids=sys.argv[2:]
modo=sys.argv[1]
for i in ids:
    e=por_cita[i]
    a,b=e['par']
    if modo=='blind':
        print('='*78); print('CASO',i)
        for n in (a,b):
            d=nodos[n]
            print('  NODO',n,'|',d['titulo_concepto'])
            for p in (d.get('pasos_accionables') or []): print('     -',p)
        print('  CLASE PROPUESTA POR EL AUDITOR: ____')
    else:
        print(i,'| clase escrita:',e['clase'],'| via:',e['via'])
        print('   razon:',e['razon'][:400])
