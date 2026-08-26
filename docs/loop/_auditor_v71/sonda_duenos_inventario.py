# Sonda del auditor v71: duenos del tramo, entradas de inventario, fichas de
# OP-L-03 / OP-U-02 / OP-S-09, racimos y barrido de los 15 miembros del lote.
import json

miembros = ['segmentos_de_clientes_problema_necesidad', 'customer_segments_hypothesis', 'problem_recognition_scale',
            'defensas_en_profundidad_3', 'defensas_en_profundidad', 'defensas_en_profundidad_2',
            'traction_goal', 'definir_meta_de_traccion', 'moving_the_needle',
            'design_for_six_sigma_dfss', 'design_for_six_sigma_dmadv', 'design_for_six_sigma_dmadv_2',
            'equipo_multifuncional_real', 'diseno_organizacional_equipos_innovacion', 'equipo_multifuncional']

tramo = [json.loads(l) for l in open('docs/loop/TRAMO_UNICO_OPU02_V64.jsonl', encoding='utf-8')]
print('tramo filas', len(tramo), 'claves', sorted(tramo[0].keys()))
for t in tramo:
    a = t.get('acto') or t.get('numero') or t.get('orden')
    if a in (31, 37, 38, 39, 40, 41, 42, 43, 44):
        duen = {k: v for k, v in t.items() if 'duen' in k}
        print('acto', a, duen)

inv = [json.loads(l) for l in open('docs/plan/INVENTARIO.jsonl', encoding='utf-8')]
print('\ninventario', len(inv))
for e in inv:
    nombre = e.get('nombre') or e.get('id') or ''
    if e.get('tipo') == 'familia_de_ids' and nombre in ('defensas_en_profundidad', 'design_for_six_sigma_dmadv'):
        print('FAMILIA', json.dumps(e, ensure_ascii=False)[:600])
# entradas de tipo acto de los cinco del lote
for e in inv:
    if e.get('tipo') == 'acto':
        ms = e.get('miembros') or []
        if any(m in miembros for m in ms):
            print('ACTO-ENTRADA', e.get('nombre'), 'operaciones', e.get('operaciones'))

ops = [json.loads(l) for l in open('docs/plan/OPERACIONES.jsonl', encoding='utf-8')]
for o in ops:
    if o['id_op'] in ('OP-L-03', 'OP-U-02', 'OP-S-09'):
        print('\n===', o['id_op'], 'fase', o.get('fase'), 'estado', o.get('estado'), 'bloquea_a', o.get('bloquea_a'))
        v = o.get('verificacion')
        print('VERIFICACION:', (v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))[:900])

rac = [json.loads(l) for l in open('docs/RACIMOS_MIEMBROS.jsonl', encoding='utf-8')]
print('\nracimos lineas', len(rac))
tocados = []
for r in rac:
    noms = json.dumps(r, ensure_ascii=False)
    for m in miembros:
        if '"%s"' % m in noms:
            tocados.append((r.get('nombre') or r.get('racimo'), m))
print('miembros del lote en racimos:', tocados if tocados else 'NINGUNO')

texto_ops = open('docs/plan/OPERACIONES.jsonl', encoding='utf-8').read()
menciones = [m for m in miembros if m in texto_ops]
print('menciones de los 15 en OPERACIONES.jsonl:', menciones if menciones else 'CERO')
