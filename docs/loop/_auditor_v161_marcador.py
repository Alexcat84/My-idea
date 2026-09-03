# Auditor de la vuelta 161: recomputo propio del censo, aristas, marcador y registro.
# Claves de esta casa: 'nodos' en el grafo, 'puesto_intra' en el archivo del cribado.
import json, collections, hashlib, os
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(RAIZ)
G = json.load(open(os.path.join(RAIZ,'dataset','metadata','master_graph.json'),encoding='utf-8'))
if 'nodos' not in G: raise SystemExit('el grafo no trae la clave nodos')
N = G['nodos']
vivos = [k for k,v in N.items() if not v.get('deprecado')]
depr  = [k for k,v in N.items() if v.get('deprecado')]
print('CENSO nodos / vivos / deprecados: %d / %d / %d' % (len(N), len(vivos), len(depr)))
sig = sum(len(v.get('nodos_siguientes') or []) for v in N.values())
prev= sum(len(v.get('nodos_previos') or []) for v in N.values())
pares_sig = set(); pares_prev = set(); auto = 0
for k,v in N.items():
    for d in (v.get('nodos_siguientes') or []):
        pares_sig.add((k,d))
        if d==k: auto+=1
    for o in (v.get('nodos_previos') or []):
        pares_prev.add((o,k))
        if o==k: auto+=1
union = pares_sig | pares_prev
print('ARISTAS sig / prev / suma / union: %d / %d / %d / %d' % (sig, prev, sig+prev, len(union)))
print('solo_sig %d  solo_prev %d  auto_enlaces %d' % (len(pares_sig-pares_prev), len(pares_prev-pares_sig), auto))
# titulos duplicados entre vivos
tit = collections.Counter((N[k].get('titulo_concepto') or '').strip().lower() for k in vivos)
print('DUPLICADAS DE TITULO entre vivos: %d' % sum(1 for t,c in tit.items() if c>1 and t))
# marcador del archivo del cribado
filas = [json.loads(l) for l in open(os.path.join(RAIZ,'docs','INTRA_DOMINIO_VEREDICTOS.jsonl'),encoding='utf-8') if l.strip()]
puestos = [f['puesto_intra'] for f in filas]
clases = collections.Counter(f['clase'] for f in filas)
n = max(puestos)
huecos = [p for p in range(1,n+1) if p not in set(puestos)]
dups = [p for p,c in collections.Counter(puestos).items() if c>1]
print('MARCADOR n=%d  A=%d  B=%d  C=%d  D=%d  filas=%d' % (n, clases['A'], clases['B'], clases['C'], clases['D'], len(filas)))
print('HUECOS %d  DUPLICADOS %d' % (len(huecos), len(dups)))
# registro de citas
reg = [json.loads(l) for l in open(os.path.join(RAIZ,'docs','plan','REGISTRO_DE_CITAS_OPC05.jsonl'),encoding='utf-8') if l.strip()]
via = collections.Counter(r['via'] for r in reg)
porvia = collections.Counter((r['via'], r['clase']) for r in reg)
print('REGISTRO filas=%d  %s' % (len(reg), dict(via)))
for kk in sorted(porvia): print('   %-18s %s : %d' % (kk[0], kk[1], porvia[kk]))
rastro = sum(1 for r in reg if 'CORRECCION DECLARADA' in r['razon'] or 'RECLASIFICADA' in r['razon'] or 'CORRECCION' in r['razon'])
print('CITAS con rastro de correccion: %d' % rastro)
# coherencia cita<->clase
mal = [r['cita'][:40] for r in reg if ('clase %s' % r['clase']) not in r['cita']]
print('CITAS que declaran clase distinta de la vigente: %d' % len(mal))
for m in mal[:10]: print('   ', m)
# las C de lectura dirigida, nominadas
cs = sorted(r['cita'].split(',')[0] for r in reg if r['via']=='LECTURA_DIRIGIDA' and r['clase']=='C')
print('C DE LECTURA DIRIGIDA (%d): %s' % (len(cs), ', '.join(x.replace('LD-OPC05-','') for x in cs)))
# sha256 del grafo
h = hashlib.sha256(open(os.path.join(RAIZ,'dataset','metadata','master_graph.json'),'rb').read()).hexdigest()
print('sha256 master_graph: %s' % h[:16])
