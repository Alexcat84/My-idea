# -*- coding: utf-8 -*-
"""Instrumento propio del auditor de la vuelta 157. No importa codigo de la casa.
Censo, aristas, auto-aristas, pares bidireccionales entre vivos y su cita en el
registro de OP-C-05, leyendo el registro de una REF DE GIT y no del arbol."""
import json, sys, subprocess, ast
sys.stdout.reconfigure(encoding='utf-8')

REF = sys.argv[1] if len(sys.argv) > 1 else 'HEAD'

G = json.load(open('dataset/metadata/master_graph.json', encoding='utf-8'))
N = G['nodos']

def lista(v):
    if v is None: return []
    if isinstance(v, list): return v
    if isinstance(v, str):
        v = v.strip()
        if not v: return []
        try:
            r = ast.literal_eval(v)
            return list(r) if isinstance(r, (list, tuple)) else [r]
        except Exception:
            return [v]
    return []

# resolutor de alias propio
alias = {}
for k, n in N.items():
    alias[k] = k
    for a in lista(n.get('ids_alias')):
        alias.setdefault(a, k)
def R(x):
    return alias.get(x, x)

vivos = {k for k, n in N.items() if not n.get('deprecado')}
depre = {k for k, n in N.items() if n.get('deprecado')}
print('CENSO nodos=%d vivos=%d deprecados=%d' % (len(N), len(vivos), len(depre)))

sig = prev = 0
union = set(); auto = 0; dup_lista = 0
solo_sig = set(); solo_prev = set()
for k, n in N.items():
    s = lista(n.get('nodos_siguientes')); p = lista(n.get('nodos_previos'))
    sig += len(s); prev += len(p)
    for d in s:
        union.add((k, d)); solo_sig.add((k, d))
        if k in vivos and R(d) == R(k): auto += 1
    for d in p:
        union.add((d, k)); solo_prev.add((d, k))
        if k in vivos and R(d) == R(k): auto += 1
    for lst in (s, p):
        rr = [R(x) for x in lst]
        if k in vivos and len(rr) != len(set(rr)): dup_lista += 1
print('ARISTAS sig=%d prev=%d suma=%d union=%d' % (sig, prev, sig + prev, len(union)))
print('AUTO-ARISTAS tras resolver (nodos vivos)=%d | listas con duplicada tras resolver=%d' % (auto, dup_lista))
print('solo_sig=%d solo_prev=%d' % (len(solo_sig - solo_prev), len(solo_prev - solo_sig)))

# pares bidireccionales entre VIVOS, resolviendo alias
dirig = set()
for k, n in N.items():
    if k not in vivos: continue
    for d in lista(n.get('nodos_siguientes')):
        r = R(d)
        if r in vivos and r != k: dirig.add((k, r))
    for d in lista(n.get('nodos_previos')):
        r = R(d)
        if r in vivos and r != k: dirig.add((r, k))
bidi = {tuple(sorted((a, b))) for (a, b) in dirig if (b, a) in dirig}
print('PARES BIDIRECCIONALES entre vivos (vara viva)=%d' % len(bidi))

# universo ensanchado: admitiendo declarante deprecado, con los dos extremos vivos
dirig2 = set()
for k, n in N.items():
    kk = R(k)
    for d in lista(n.get('nodos_siguientes')):
        r = R(d)
        if r in vivos and kk in vivos and r != kk: dirig2.add((kk, r))
    for d in lista(n.get('nodos_previos')):
        r = R(d)
        if r in vivos and kk in vivos and r != kk: dirig2.add((r, kk))
bidi2 = {tuple(sorted((a, b))) for (a, b) in dirig2 if (b, a) in dirig2}
print('PARES BIDIRECCIONALES universo ENSANCHADO=%d | ensanchado menos vivo=%d' % (len(bidi2), len(bidi2 - bidi)))
for p in sorted(bidi2 - bidi):
    print('   FUERA DE LA VARA VIVA: %s <-> %s' % p)

# registro leido de una ref de git
txt = subprocess.run(['git', 'show', '%s:docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl' % REF],
                     capture_output=True).stdout.decode('utf-8')
REG = [json.loads(l) for l in txt.splitlines() if l.strip()]
citados = set()
for e in REG:
    p = e['par']
    p = tuple(sorted((R(p[0]), R(p[1])))) if isinstance(p, list) else tuple(sorted(R(x) for x in p.split(' <-> ')))
    citados.add(p)
sin = sorted(bidi - citados)
print('REGISTRO en %s: %d linea(s), %d par(es) distinto(s)' % (REF, len(REG), len(citados)))
from collections import Counter
print('CLASES en %s: %s' % (REF, dict(Counter(e.get('clase') for e in REG))))
print('CON CITA: %d de %d | SIN CITA: %d %s' % (len(bidi) - len(sin), len(bidi), len(sin), sin[:5]))

# aritmetica de los nodos que participan
part = sorted({x for p in bidi for x in p})
dest = sum(1 for _ in dirig if _[0] in {x for p in bidi for x in p})
print('NODOS que participan en algun par bidireccional=%d' % len(part))
