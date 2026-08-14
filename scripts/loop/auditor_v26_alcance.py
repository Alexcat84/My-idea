# Auditor vuelta 26: contexto de cada casacion de crear/nodo propio en las siete
# operaciones que el reporte nombra (14 ago 2026)
import json, io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ops = [json.loads(l) for l in open('docs/plan/OPERACIONES.jsonl', encoding='utf-8') if l.strip()]
pat = re.compile(r'crea|nodo propio|nodo nuevo', re.I)
SIETE = ('OP-D-08', 'OP-D-09', 'OP-F-02', 'OP-F-04-HOR', 'OP-F-04-COL', 'OP-F-04-WEI', 'OP-F-04-RAC')
for o in ops:
    if o['id_op'] not in SIETE:
        continue
    for campo, val in o.items():
        txt = json.dumps(val, ensure_ascii=False)
        for m in pat.finditer(txt):
            ctx = txt[max(0, m.start() - 80):m.end() + 80].replace('\n', ' ')
            print(f"{o['id_op']:14} {campo:16} ...{ctx}...")
    print()
