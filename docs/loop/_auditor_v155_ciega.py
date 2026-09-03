"""Relectura ciega del auditor, vuelta 155. Imprime SOLO titulo y pasos
accionables de los dos nodos. Sin clase, sin via, sin cita y sin la razon."""
import json, glob, sys

nodos = {}
for f in glob.glob('dataset/nodos/**/*.json', recursive=True):
    d = json.load(open(f, encoding='utf-8'))
    nodos[d['node_id']] = d

reg = [json.loads(l) for l in open('docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl', encoding='utf-8') if l.strip()]
por_cita = {e['cita'].split(',')[0].strip(): e for e in reg}

modo = sys.argv[1]
if modo == 'marcados':
    casos = ['LD-OPC05-097', 'LD-OPC05-046', 'LD-OPC05-040', 'LD-OPC05-122']
    print("MUESTRA: los CUATRO discutibles marcados del reporte de la vuelta 154.")
else:
    ld = sorted([e for e in reg if e['via'] == 'LECTURA_DIRIGIDA'], key=lambda e: e['cita'])
    # zancada DISTINTA de la del ejecutor (el uso zancada 3 arranque 1)
    sel = ld[1::12]
    casos = [e['cita'].split(',')[0].strip() for e in sel]
    print(f"MUESTRA POR COMPUTO, FUERA DEL MARCADO: universo {len(ld)} lecturas dirigidas "
          f"ordenadas por cita, zancada 12, arranque en el puesto 2. "
          f"SELECCIONADAS: {len(casos)} puesto(s).")
print("AQUI NO HAY CLASE, NI VIA, NI CITA, NI LA RAZON ESCRITA.")
print()
for i, c in enumerate(casos, 1):
    e = por_cita[c]
    a, b = e['par']
    print("=" * 90)
    print(f"CASO {i} de {len(casos)}  [ref interna {c}]")
    for nid in (a, b):
        n = nodos[nid]
        print(f"  --- {nid} (deprecado={n.get('deprecado')}, dominio={n.get('dominio')})")
        print(f"      titulo: {n.get('titulo_concepto')}")
        for j, p in enumerate(n.get('pasos_accionables') or [], 1):
            print(f"       {j}. {p}")
    print()
