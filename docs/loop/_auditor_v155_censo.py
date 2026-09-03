"""Instrumento propio del auditor, vuelta 155. Escrito hoy, sin importar codigo
de la casa. Lee dataset/nodos/*.json y mide: censo, aristas, y las CUATRO VARAS
de pares bidireccionales de OP-C-05, con resolutor de alias propio.
Imprime lineas CIFRA en el formato del contrato (CIFRA <etiqueta>: <n> <unidad>)."""
import json, glob, sys, subprocess

nodos = {}
for f in glob.glob('dataset/nodos/**/*.json', recursive=True):
    d = json.load(open(f, encoding='utf-8'))
    nodos[d['node_id']] = d

vivos = {k for k, v in nodos.items() if not v.get('deprecado')}
depre = set(nodos) - vivos
print(f"CIFRA censo nodos totales: {len(nodos)} nodos")
print(f"CIFRA censo nodos vivos: {len(vivos)} nodos")
print(f"CIFRA censo nodos deprecados: {len(depre)} nodos")

sig = prev = 0
union = set()
for k, v in nodos.items():
    s = v.get('nodos_siguientes') or []
    p = v.get('nodos_previos') or []
    sig += len(s); prev += len(p)
    for x in s: union.add((k, x))
    for x in p: union.add((x, k))
print(f"CIFRA aristas nodos_siguientes: {sig} aristas")
print(f"CIFRA aristas nodos_previos: {prev} aristas")
print(f"CIFRA aristas suma de los dos campos: {sig+prev} aristas")
print(f"CIFRA aristas union dirigida de los dos campos: {len(union)} aristas")

# resolutor de alias propio: cadena de alias hasta nodo vivo, con tope
dueno = {}
for k, v in nodos.items():
    for a in (v.get('ids_alias') or []):
        dueno[a] = k

def resolver(x, tope=10):
    visto = set()
    for _ in range(tope):
        if x in nodos and x not in depre:
            return x
        if x in visto:
            return None
        visto.add(x)
        if x in dueno:
            x = dueno[x]; continue
        if x in nodos:  # existe pero deprecado y sin alias que lo suba
            return None
        return None
    return None

def pares(fuentes_vivas_solo, dos_campos):
    """Devuelve el conjunto de pares no ordenados {a,b} entre VIVOS declarados
    en las dos direcciones tras resolver."""
    dirigidas = set()
    for k, v in nodos.items():
        if fuentes_vivas_solo and k in depre:
            continue
        fk = resolver(k)
        if fk is None:
            continue
        campos = ['nodos_siguientes', 'nodos_previos'] if dos_campos else ['nodos_siguientes']
        for c in campos:
            for x in (v.get(c) or []):
                dx = resolver(x)
                if dx is None or dx == fk:
                    continue
                if c == 'nodos_siguientes':
                    dirigidas.add((fk, dx))
                else:
                    dirigidas.add((dx, fk))
    bidi = set()
    for a, b in dirigidas:
        if (b, a) in dirigidas:
            bidi.add(frozenset((a, b)))
    return bidi

# registro de citas: se lee de una REF DE GIT, no del arbol de trabajo
ref = sys.argv[1] if len(sys.argv) > 1 else 'HEAD'
raw = subprocess.run(['git', 'show', f'{ref}:docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl'],
                     capture_output=True, text=True, encoding='utf-8')
citado = set()
lineas = 0
clases = {}
vias = {}
for ln in raw.stdout.splitlines():
    ln = ln.strip()
    if not ln:
        continue
    lineas += 1
    e = json.loads(ln)
    a, b = e['par'][0], e['par'][1]
    citado.add(frozenset((a, b)))
    clases[e.get('clase')] = clases.get(e.get('clase'), 0) + 1
    vias[e.get('via')] = vias.get(e.get('via'), 0) + 1
print(f"CIFRA registro lineas del registro de citas en {ref}: {lineas} lineas")
print(f"CIFRA registro pares distintos del registro de citas en {ref}: {len(citado)} pares")
print(f"  clases: {clases} | vias: {vias}")

print()
print("LAS CUATRO VARAS (registro leido de %s)" % ref)
for etiqueta, fv, dc in [
        ("vara estrecha (fuentes vivas, solo nodos_siguientes)", True, False),
        ("vara completa (fuentes vivas, los dos campos)", True, True),
        ("todas las fuentes, solo nodos_siguientes", False, False),
        ("todas las fuentes, los dos campos", False, True)]:
    P = pares(fv, dc)
    sin = [sorted(p) for p in P if p not in citado]
    print(f"  {etiqueta}: {len(P)} pares, {len(sin)} sin cita")
    for s in sorted(sin):
        print(f"      SIN CITA: {s[0]} <-> {s[1]}")

# la aritmetica del 4.3: destinos de ida y vuelta declarados DENTRO de un nodo vivo
nodos_con = 0; destinos = 0; mutuos = 0; solo_un_lado = []
dirigidas_estrecha = set()
for k, v in nodos.items():
    if k in depre:
        continue
    S = {resolver(x) for x in (v.get('nodos_siguientes') or [])} - {None, k}
    P = {resolver(x) for x in (v.get('nodos_previos') or [])} - {None, k}
    amb = S & P
    if amb:
        nodos_con += 1; destinos += len(amb)
    for d in amb:
        w = nodos[d]
        S2 = {resolver(x) for x in (w.get('nodos_siguientes') or [])} - {None, d}
        P2 = {resolver(x) for x in (w.get('nodos_previos') or [])} - {None, d}
        if k in (S2 & P2):
            mutuos += 1
        else:
            solo_un_lado.append(f"{k} -> {d}")
print()
print(f"CIFRA aritmetica nodos vivos con destino de ida y vuelta: {nodos_con} nodos")
print(f"CIFRA aritmetica destinos de ida y vuelta declarados dentro de un nodo vivo: {destinos} direcciones")
print(f"CIFRA aritmetica destinos mutuos: {mutuos} direcciones")
print(f"  declarados por un solo lado: {solo_un_lado}")
