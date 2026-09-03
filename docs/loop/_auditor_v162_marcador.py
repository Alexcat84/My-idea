# Auditor de la vuelta 162: recomputo propio del censo, aristas, marcador y registro.
# Claves de esta casa: 'nodos' en el grafo, 'puesto_intra' en el archivo del cribado.
import json, collections, hashlib, os, re
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
G = json.load(open(os.path.join(RAIZ,'dataset','metadata','master_graph.json'),encoding='utf-8'))
if 'nodos' not in G: raise SystemExit('el grafo no trae la clave nodos')
N = G['nodos']
vivos = [k for k,v in N.items() if not v.get('deprecado')]
depr  = [k for k,v in N.items() if v.get('deprecado')]
print('CENSO nodos / vivos / deprecados: %d / %d / %d' % (len(N), len(vivos), len(depr)))
sig = sum(len(v.get('nodos_siguientes') or []) for v in N.values())
prev= sum(len(v.get('nodos_previos') or []) for v in N.values())
pares_sig=set(); pares_prev=set(); auto=0
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
tit = collections.Counter((N[k].get('titulo_concepto') or '').strip() for k in vivos)
print('DUPLICADAS DE TITULO EXACTO entre vivos: %d' % sum(1 for t,c in tit.items() if c>1 and t))
filas = [json.loads(l) for l in open(os.path.join(RAIZ,'docs','INTRA_DOMINIO_VEREDICTOS.jsonl'),encoding='utf-8') if l.strip()]
puestos = [f['puesto_intra'] for f in filas]
clases = collections.Counter(f['clase'] for f in filas)
n = max(puestos)
huecos = [p for p in range(1,n+1) if p not in set(puestos)]
dups = [p for p,c in collections.Counter(puestos).items() if c>1]
print('MARCADOR n=%d  A=%d  B=%d  C=%d  D=%d  filas=%d' % (n, clases['A'], clases['B'], clases['C'], clases['D'], len(filas)))
print('HUECOS %d  DUPLICADOS %d' % (len(huecos), len(dups)))
reg = [json.loads(l) for l in open(os.path.join(RAIZ,'docs','plan','REGISTRO_DE_CITAS_OPC05.jsonl'),encoding='utf-8') if l.strip()]
porvia = collections.Counter((r['via'], r['clase']) for r in reg)
print('REGISTRO filas=%d' % len(reg))
for kk in sorted(porvia): print('   %-18s %s : %d' % (kk[0], kk[1], porvia[kk]))
ld = [r for r in reg if r['via']=='LECTURA_DIRIGIDA']
print('CITAS de lectura dirigida: %d' % len(ld))
rastro = sum(1 for r in ld if '[' in r['cita'] and 'CORRECCION' in r['cita'].upper())
print('CITAS con rastro de correccion (corchete en cita, sobre las de lectura dirigida): %d' % rastro)
mal = [r['cita'][:60] for r in reg if ('clase %s' % r['clase']) not in r['cita']]
print('CITAS que declaran clase distinta de la vigente: %d' % len(mal))
for m in mal[:10]: print('   ', m)
cs = sorted(r['cita'].split(',')[0] for r in reg if r['via']=='LECTURA_DIRIGIDA' and r['clase']=='C')
print('C DE LECTURA DIRIGIDA (%d): %s' % (len(cs), ', '.join(x.replace('LD-OPC05-','') for x in cs)))
# --- especifico de la vuelta 162: las marcas de la ciega del auditor ---
MARCA = 'RELECTURA CIEGA DEL AUDITOR, VUELTA 161'
con_marca = [r['cita'].split(',')[0].replace('LD-OPC05-','') for r in reg if MARCA in r.get('razon','')]
print('FILAS CON LA MARCA DE LA CIEGA 161: %d -> %s' % (len(con_marca), ', '.join(sorted(con_marca))))
sello = sum(1 for r in reg if 'ffe1fa6f' in r.get('razon',''))
print('FILAS QUE CITAN EL SELLO ffe1fa6f: %d' % sello)
h = hashlib.sha256(open(os.path.join(RAIZ,'dataset','metadata','master_graph.json'),'rb').read()).hexdigest()
print('sha256 master_graph: %s' % h[:16])
