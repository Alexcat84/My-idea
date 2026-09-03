# CIEGA DEL AUDITOR, VUELTA 162. Imprime SOLO titulo, fuente, entregable y pasos
# de los dos nodos. Sin clase, sin via, sin cita y sin razon.
import json, sys, os
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
G = json.load(open(os.path.join(RAIZ,'dataset','metadata','master_graph.json'),encoding='utf-8'))['nodos']
REG = [json.loads(l) for l in open(os.path.join(RAIZ,'docs','plan','REGISTRO_DE_CITAS_OPC05.jsonl'),encoding='utf-8') if l.strip()]
IDX = {}
for r in REG:
    IDX[r['cita'].split(',')[0].strip()] = r
def pinta(nid):
    v = G[nid]
    print('  NODO %s' % nid)
    print('    titulo: %s' % v.get('titulo_concepto'))
    print('    fuente: %s' % (v.get('fuente') or '')[:90])
    print('    entregable: %s' % (v.get('entregable_esperado') or ''))
    for i,p in enumerate(v.get('pasos_accionables') or [],1):
        print('      %2d. %s' % (i,p))
for cid in sys.argv[1:]:
    r = IDX['LD-OPC05-%s' % cid]
    print('='*78)
    print('CASO LD-OPC05-%s   par: %s  <->  %s' % (cid, r['par'][0], r['par'][1]))
    print('='*78)
    pinta(r['par'][0]); print('  ---'); pinta(r['par'][1]); print()
