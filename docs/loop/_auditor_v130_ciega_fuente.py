# AUDITOR VUELTA 130, relectura ciega del censo de `fuente`.
# Escrito SIN mirar scripts/loop/vuelta130_censo_fuente.py.
import json, glob, collections
todos, viv = [], []
for p in sorted(glob.glob('dataset/nodos/*.json')):
    d = json.load(open(p, encoding='utf-8'))
    todos.append(d)
    if not (d.get('deprecated') or d.get('deprecado')): viv.append(d)
print('FICHEROS dataset/nodos/:', len(todos), ' VIVOS:', len(viv))
def censo(nodos, seps):
    c = collections.Counter()
    for n in nodos:
        f = (n.get('fuente') or '').strip()
        if not f: continue
        partes = [f]
        for s in seps:
            partes = [x for p in partes for x in p.split(s)]
        for p in partes:
            p = p.strip()
            if p: c[p] += 1
    return c
for nombre, seps in [('solo ;', [';']), ('solo |', ['|']), ('; y |', [';','|']), ('ninguno', [])]:
    c = censo(viv, seps)
    print(f'  separador {nombre:10s} -> GRAFIAS DISTINTAS {len(c):4d}  declaraciones {sum(c.values()):5d}')
print('NODOS VIVOS con `;` en fuente:', sum(1 for n in viv if ';' in (n.get('fuente') or '')),
      ' con `|`:', sum(1 for n in viv if '|' in (n.get('fuente') or '')),
      ' sin fuente:', sum(1 for n in viv if not (n.get('fuente') or '').strip()))
for autor in ['Hugos', 'Horowitz']:
    for nombre, seps in [('fuente entero, sin partir', []), ('partido por |', ['|'])]:
        c = censo(viv, seps)
        g = {k: v for k, v in c.items() if autor in k}
        print(f'  {autor:9s} [{nombre:26s}] grafias {len(g):2d}  declaraciones {sum(g.values()):3d}')
    print(f'  {autor:9s} NODOS VIVOS cuyo fuente lo menciona: {sum(1 for n in viv if autor in (n.get("fuente") or ""))}')

print('--- AHORA EN PRIMERA POSICION, que es lo que el reporte dice medir ---')
def censo1(nodos, seps):
    c = collections.Counter()
    for n in nodos:
        f = (n.get('fuente') or '').strip()
        if not f: continue
        partes = [f]
        for s in seps:
            partes = [x for p in partes for x in p.split(s)]
        # PRIMERA POSICION = la primera declaracion de cada nodo
        p = partes[0].strip()
        if p: c[p] += 1
    return c
for nombre, seps in [('solo ;', [';']), ('solo |', ['|']), ('; y |', [';','|']), ('ninguno', [])]:
    c = censo1(viv, seps)
    print(f'  1a pos, separador {nombre:10s} -> GRAFIAS DISTINTAS {len(c):4d}  nodos {sum(c.values()):5d}')
