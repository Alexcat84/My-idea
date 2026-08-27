# -*- coding: utf-8 -*-
"""El mismo barrido de formulas que NIEGAN jerarquia, pero sobre las 114
direcciones de OP-E-06 (ya escritas en la vuelta 90): si la caida del 1098
tiene hermanos alli, son aristas ya en el grafo."""
import io, json, re
V = {}
for l in io.open('docs/INTRA_DOMINIO_VEREDICTOS.jsonl', encoding='utf-8'):
    l = l.strip()
    if l:
        d = json.loads(l); V[int(d['puesto_intra'])] = d
EJ = [json.loads(l) for l in io.open('docs/plan/OP_E_06_DIRECCION_V90.jsonl', encoding='utf-8')]
NIEGA = re.compile(r"no crea jerarquia|ninguno la expande|no hay jerarquia|sin jerarquia|"
                   r"ninguno de los dos la expande|no era madre e hijo|linea compartida y procedimiento propio",
                   re.IGNORECASE)
hits = []
for e in EJ:
    p = int(e['puesto'])
    if p not in V:
        print('AVISO: puesto', p, 'no esta en VEREDICTOS'); continue
    if NIEGA.search(V[p]['razon']):
        hits.append(p)
print('direcciones de OP-E-06 barridas:', len(EJ))
print('con formula que NIEGA la jerarquia:', len(hits), hits)
