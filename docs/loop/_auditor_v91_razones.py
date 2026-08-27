import json, io, sys
puestos = set(int(x) for x in sys.argv[1:])
for l in io.open('docs/INTRA_DOMINIO_VEREDICTOS.jsonl', encoding='utf-8'):
    l = l.strip()
    if not l: continue
    v = json.loads(l)
    if int(v.get('puesto_intra', -1)) in puestos:
        print('='*90)
        print('PUESTO', v['puesto_intra'], '| clase', v.get('clase'), '| dominio', v.get('dominio'))
        print('nodo_a:', v.get('nodo_a'))
        print('nodo_b:', v.get('nodo_b'))
        print('RAZON COMPLETA:')
        print(v.get('razon'))
        print()
