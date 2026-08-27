import re
nuevas = set()
for l in open('docs/loop/_auditor_v91_union_diff.txt', encoding='utf-8'):
    if l.startswith('> '):
        a, b = l[2:].strip().split(' -> ')
        nuevas.add((a, b))
declaradas = set(); n_esc = 0
pat = re.compile(r'^puesto (\d+)\s+\| (\w+)\s+\| (\S+) -> (\S+) \(resuelto: (.*)\)$')
for l in open('docs/loop/SALIDA_V91_TAREA4_ESCRITURA.txt', encoding='utf-8'):
    m = pat.match(l.strip())
    if not m: continue
    puesto, clase, o, d, res = m.groups()
    if clase == 'ESCRITA':
        n_esc += 1; declaradas.add((o, d))
print('nuevas en grafo:', len(nuevas), '| filas ESCRITA:', n_esc, '| pares declarados distintos:', len(declaradas))
print('EN EL GRAFO Y NO EN EL LOG:', sorted(nuevas - declaradas))
print('EN EL LOG Y NO EN EL GRAFO:', sorted(declaradas - nuevas))
print('CALZAN EXACTO, CONJUNTO CONTRA CONJUNTO:', nuevas == declaradas)
