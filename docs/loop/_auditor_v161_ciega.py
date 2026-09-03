# CIEGA DEL AUDITOR, VUELTA 161. Imprime SOLO titulo, fuente, entregable y pasos
# de los dos nodos. Sin clase, sin via, sin cita y sin razon.
import json, sys, os
RAIZ = r"C:\Users\AlexDesk\Documents\I have an idea"
G = json.load(open(os.path.join(RAIZ,'dataset','metadata','master_graph.json'),encoding='utf-8'))['nodos']
REG = [json.loads(l) for l in open(os.path.join(RAIZ,'docs','plan','REGISTRO_DE_CITAS_OPC05.jsonl'),encoding='utf-8') if l.strip()]
IDX = {}
for r in REG:
    cid = r['cita'].split(',')[0].strip()
    IDX[cid] = r
def pinta(nid):
    v = G[nid]
    print('  NODO %s' % nid)
    print('    titulo: %s' % v.get('titulo_concepto'))
    print('    fuente: %s' % (v.get('fuente') or '')[:90])
    print('    entregable: %s' % (v.get('entregable_esperado') or ''))
    for i,p in enumerate(v.get('pasos_accionables') or [],1):
        print('      %2d. %s' % (i,p))
for cid in sys.argv[1:]:
    key = 'LD-OPC05-%s' % cid
    r = IDX[key]
    print('='*78)
    print('CASO %s   par: %s  <->  %s' % (key, r['par'][0], r['par'][1]))
    print('='*78)
    pinta(r['par'][0]); print('  ---'); pinta(r['par'][1]); print()
