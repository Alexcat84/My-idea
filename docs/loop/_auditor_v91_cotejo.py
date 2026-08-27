import re, sys
# 86 aristas nuevas del diff de la union
nuevas = set()
for l in open('docs/loop/_auditor_v91_union_diff.txt', encoding='utf-8'):
    if l.startswith('> '):
        a, b = l[2:].strip().split(' -> ')
        nuevas.add((a, b))
# filas ESCRITA del log del ejecutor
escritas = set(); n_esc = 0; ya = []
pat = re.compile(r'^puesto (\d+)\s+\| (\w+)\s+\| (\S+) -> (\S+) \(resuelto: (.*)\)$')
for l in open('docs/loop/SALIDA_V91_TAREA4_ESCRITURA.txt', encoding='utf-8'):
    m = pat.match(l.strip())
    if not m: continue
    puesto, clase, o, d, res = m.groups()
    if clase == 'ESCRITA':
        n_esc += 1
        # el par REAL escrito es el resuelto si hay alias
        if res == 'sin alias': escritas.add((o, d))
        else:
            ro, rd = res.split(' -> '); escritas.add((ro, rd))
    elif clase == 'YA_ESTABA':
        ya.append((puesto, o, d, res))
print('aristas nuevas en el grafo (diff union):', len(nuevas))
print('filas ESCRITA en el log:', n_esc, '| pares distintos tras resolver:', len(escritas))
print('YA_ESTABA:', len(ya), ya)
print('EN EL GRAFO Y NO EN EL LOG:', sorted(nuevas - escritas))
print('EN EL LOG Y NO EN EL GRAFO:', sorted(escritas - nuevas))
print('CALZAN EXACTO:', nuevas == escritas)
