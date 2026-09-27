import json, glob, os, collections
REPO = 'C:/Users/AlexDesk/Documents/my-idea-correcciones'
os.chdir(REPO)
nod = {}
for p in glob.glob('dataset/nodos/*.json'):
    n = json.load(open(p, encoding='utf-8')); nod[n['node_id']] = n
viv = {k for k, n in nod.items() if not n.get('deprecado')}
alias = {}
for k, n in nod.items():
    for a in n.get('ids_alias') or []:
        if a != k:
            alias[a] = k


def res(i):
    seen = {i}; cur = i
    while cur not in viv and cur in alias:
        cur = alias[cur]
        if cur in seen:
            return None
        seen.add(cur)
    return cur if cur in viv else None


R = json.load(open('docs/saneamiento/resultados/R/final.json', encoding='utf-8'))
juicio = collections.defaultdict(set)
motivo = {}
for x in R:
    if x['trampa']:
        continue
    par = (x['nodo'], x['vecino']) if x['sentido'] == 'siguiente' else (x['vecino'], x['nodo'])
    juicio[par].add(x['estado'])
    if x['estado'] != 'VIGENTE':
        motivo[par] = (x['estado'], x['motivo'], x['id'], x['decidido_por'])
conflicto = [p for p, s in juicio.items() if len(s) > 1]
rancias = sorted(p for p, s in juicio.items() if s and 'VIGENTE' not in s)
# Los 4 pares juzgados VIGENTE desde un extremo y RANCIA desde el otro, a un arbitro que leyo los dos nodos
# (26 sep 2026): 3 VIGENTE (se quedan) y 1 RANCIA.
ARBITRO = {('causas_comunes_vs_especiales', 'muestreo_con_seguimiento_no_respondientes'):
           'Distinguir la variacion comun de la especial con graficos de control no lleva a disenar una encuesta con seguimiento a quienes no responden; solo los une el libro.'}
for par, m in ARBITRO.items():
    rancias.append(par)
    motivo[par] = ('RANCIA_DE_ANTES', m, 'arbitro de los pares en conflicto', 'arbitro')
rancias.sort()
print('pares juzgados', len(juicio), '| rancias sin conflicto', len(rancias), '| en conflicto (un extremo VIGENTE)', len(conflicto))
for p in conflicto:
    print('  CONFLICTO', p, juicio[p], motivo.get(p, ('',))[0])
ops = []
DEC = 'Saneamiento del dataset, TANDA 2, punto 7 (decision del fundador del 26 sep 2026)'
for i, (a, b) in enumerate(rancias, 1):
    est, mot, rid, quien = motivo[(a, b)]
    ops.append({'id': 't2-arista-%03d' % i, 'operacion': 'QUITAR', 'desde': a, 'hacia': b,
                'motivo': mot.replace(chr(0x2014), ',').replace(chr(0x2013), '-'),
                'evidencia': 'Pasada R (docs/saneamiento/resultados/R/final.json, %s): %s, %s' % (rid, est, quien),
                'decision': DEC + ': quitar la arista rancia por la correccion y las rancias de antes.', 'fecha': '2026-09-26'})
n = len(ops)
refs = []
for k in sorted(viv):
    for campo in ('nodos_siguientes', 'nodos_previos'):
        for x in nod[k].get(campo) or []:
            if x in nod and nod[x].get('deprecado'):
                refs.append((k, x) if campo == 'nodos_siguientes' else (x, k))
vistos = set()
for a, b in refs:
    if (a, b) in vistos:
        continue
    vistos.add((a, b))
    muerto = b if b not in viv else a
    n += 1
    ops.append({'id': 't2-arista-%03d' % n, 'operacion': 'RECABLEAR', 'desde': a, 'hacia': b, 'hacia_nuevo': res(muerto),
                'motivo': 'Referencia de un nodo vivo a %s, deprecado; su superviviente es %s.' % (muerto, res(muerto)),
                'evidencia': 'Determinista: resolutor por ids_alias (AUD-09 B15; pasada R, 54 referencias a deprecados).',
                'decision': DEC + ': recablear al superviviente las referencias a deprecados.', 'fecha': '2026-09-26'})
print('operaciones', len(ops), collections.Counter(o['operacion'] for o in ops))
json.dump(ops, open('docs/saneamiento/tandas/saneamiento-t2-aristas.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
