# Sonda del auditor v72 sobre el lote H: guarda D (absorbidos deprecados con
# texto entero y alias al superviviente), supervivientes y sus pasos, el acto
# 44 intacto, la familia de OP-S-09, los INCISO verbatim (fuente pre fusion por
# git show y resultante de hoy), referencias colgando, duenos del tramo,
# inventario, menciones en OPERACIONES.jsonl y racimos. Solo lee.
import json, subprocess

plan = json.load(open('docs/loop/PLAN_V72_OPU02_LOTE_H.json', encoding='utf-8'))
fusiones = plan['actos']
declarado = plan['declarados_y_no_fundidos'][0]
miembros_44 = declarado['miembros']
supervivientes = [a['superviviente'] for a in fusiones]
absorbidos = [m for a in fusiones for m in a['absorbidos']]
quince = sorted(set(m for a in fusiones for m in a['miembros']) | set(miembros_44))
print('supervivientes:', supervivientes)
print('absorbidos (%d):' % len(absorbidos), absorbidos)
print('miembros del 44:', miembros_44)
print('miembros del lote:', len(quince))

hoy = json.load(open('dataset/metadata/master_graph.json', encoding='utf-8'))['nodos']
raw_pre = subprocess.run(['git', 'show', 'c4c38956:dataset/metadata/master_graph.json'],
                         capture_output=True, text=True, encoding='utf-8').stdout
pre = json.loads(raw_pre)['nodos']


def resolver(nid):
    visto = set()
    while nid in hoy and hoy[nid].get('deprecado') and nid not in visto:
        visto.add(nid)
        nid = hoy[nid].get('alias_de') or hoy[nid].get('resuelve_a') or hoy[nid].get('alias') or nid
        if nid in visto:
            break
    return nid


print('\n--- GUARDA D: los 8 absorbidos ---')
for a in fusiones:
    for m in a['absorbidos']:
        n = hoy[m]
        texto_entero = bool(n.get('pasos_accionables')) and bool(n.get('titulo'))
        destino = resolver(m)
        print('  %-42s deprecado=%s texto_entero=%s resuelve_a=%s (%s)' % (
            m, bool(n.get('deprecado')), texto_entero, destino,
            'OK' if destino == a['superviviente'] else 'MAL'))

print('\n--- SUPERVIVIENTES hoy (pasos/condiciones) ---')
for a in fusiones:
    s = hoy[a['superviviente']]
    print('  %-42s vivo=%s pasos=%d cond=%d' % (a['superviviente'], not s.get('deprecado'),
          len(s.get('pasos_accionables') or []), len(s.get('condiciones_activacion') or [])))

print('\n--- ACTO 44: intacto ---')
for m in miembros_44:
    n = hoy[m]
    igual = json.dumps(n, sort_keys=True, ensure_ascii=False) == json.dumps(pre[m], sort_keys=True, ensure_ascii=False)
    print('  %-42s vivo=%s identico_a_c4c38956=%s' % (m, not n.get('deprecado'), igual))

print('\n--- OP-S-09: la familia ---')
for nid in ('responsabilidad_extendida_productor_2', 'responsabilidad_extendida_productor'):
    n = hoy.get(nid)
    print('  %-42s deprecado=%s resuelve_a=%s' % (nid, bool(n.get('deprecado')), resolver(nid)))

print('\n--- INCISO: trozo verbatim en la fuente PRE y en el resultante de HOY ---')
n_inciso = 0
for a in fusiones:
    for absorbido, piezas in a['pasos'].items():
        for num, pieza in piezas.items():
            if pieza.startswith('INCISO:'):
                n_inciso += 1
                resto = pieza.split(':', 1)[1]
                destino_paso, trozo = resto.split('|')[0], resto.split('|')[1]
                fuente = (pre[absorbido].get('pasos_accionables') or [])[int(num) - 1]
                en_fuente = trozo in fuente
                paso_res = (hoy[a['superviviente']].get('pasos_accionables') or [])[int(destino_paso) - 1]
                en_res = trozo in paso_res
                print('  %s paso %s -> %s paso %s | en_fuente=%s en_resultante=%s' % (
                    absorbido, num, a['superviviente'], destino_paso, en_fuente, en_res))
print('  INCISO totales:', n_inciso)

print('\n--- referencias de vivos a absorbidos (deben ser 0) ---')
colgando = 0
for nid, n in hoy.items():
    if n.get('deprecado'):
        continue
    for campo in ('nodos_previos', 'nodos_siguientes'):
        for ref in n.get(campo) or []:
            if ref in absorbidos:
                colgando += 1
                print('  COLGANDO:', nid, campo, ref)
print('  colgando:', colgando)

print('\n--- duenos del tramo fijado (43-47) y saltos (31, 37) ---')
tramo = [json.loads(l) for l in open('docs/loop/TRAMO_UNICO_OPU02_V64.jsonl', encoding='utf-8')]
for t in tramo:
    o = t.get('orden_universo')
    if o in (31, 37, 43, 44, 45, 46, 47, 49):
        print('  acto %-3s duenos_mesa=%s duenos_cualq=%s' % (o, t.get('duenos_mesa_o_destejido'), t.get('duenos_cualquier_operacion')))

print('\n--- INVENTARIO: entradas que tocan a los 15 ---')
inv = [json.loads(l) for l in open('docs/plan/INVENTARIO.jsonl', encoding='utf-8')]
tocan = []
for e in inv:
    blob = json.dumps(e, ensure_ascii=False)
    if any(m in blob for m in quince):
        tocan.append(e)
import collections
print('  total tocan:', len(tocan), 'por tipo:', dict(collections.Counter(e.get('tipo') for e in tocan)))
for e in tocan:
    if e.get('tipo') == 'familia_de_ids':
        print('  FAMILIA:', json.dumps(e, ensure_ascii=False)[:400])
    if e.get('tipo') == 'figura':
        print('  FIGURA:', (e.get('nombre') or e.get('id') or '?'), '| ops:', e.get('operaciones'), '| nombra a los 3 del 44:',
              all(m in json.dumps(e, ensure_ascii=False) for m in miembros_44))

print('\n--- OPERACIONES.jsonl: menciones de los 15 ---')
ops = [json.loads(l) for l in open('docs/plan/OPERACIONES.jsonl', encoding='utf-8')]
menciones = 0
fichas = set()
for o in ops:
    for k, v in o.items():
        blob = json.dumps(v, ensure_ascii=False)
        hits = [m for m in quince if m in blob]
        if hits:
            menciones += len(hits)
            fichas.add(o['id_op'])
            print('  %-10s campo %-14s -> %s' % (o['id_op'], k, hits))
print('  menciones:', menciones, 'en fichas:', sorted(fichas))

print('\n--- RACIMOS: los 15 en nominas ---')
rac = [json.loads(l) for l in open('docs/RACIMOS_MIEMBROS.jsonl', encoding='utf-8')]
en_racimo = [m for m in quince for r in rac if m in json.dumps(r, ensure_ascii=False)]
print('  lineas racimos:', len(rac), '| miembros hallados:', en_racimo or 'NINGUNO')
EOF_MARKER = None
