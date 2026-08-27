# -*- coding: utf-8 -*-
"""AUDITOR, vuelta 87. Mediciones propias de la seccion 1 del acta, en un solo
instrumento. Los pares se LEEN de los ficheros; ninguno se teclea.

  python docs/loop/_auditor_v87_mediciones.py > docs/loop/_auditor_v87_mediciones.txt
"""
import collections
import json
import subprocess

GRAFO = "dataset/metadata/master_graph.json"
CAL = "docs/plan/PASO_NODO_CALIBRADO.jsonl"
F87 = "docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V87.jsonl"
F86 = "docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V86.jsonl"
REG = "docs/plan/OP_E_01_DECIDIDAS.jsonl"
VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"

REFS = [("fe24bd71", "apertura, mi acta 86"),
        ("c3642f7f", "TAREA 2, el instrumento"),
        ("b32a83bf", "cierre, HEAD")]

TRAMO_INI, TRAMO_FIN = 117, 121   # indices del tramo 12 en la bolsa V87


def filas(ruta):
    return [json.loads(l) for l in open(ruta, encoding="utf-8") if l.strip()]


def texto_de(ref, ruta):
    return subprocess.run(["git", "show", "%s:%s" % (ref, ruta)],
                          capture_output=True, check=True).stdout.decode("utf-8")


def grafo_de(ref):
    return json.loads(texto_de(ref, GRAFO))["nodos"]


def cifras(nodos):
    total = len(nodos)
    vivos = sum(1 for v in nodos.values() if not v.get("deprecado"))
    sig = sum(len(v.get("nodos_siguientes") or []) for v in nodos.values())
    prev = sum(len(v.get("nodos_previos") or []) for v in nodos.values())
    union, auto, dup = set(), 0, 0
    for k, v in nodos.items():
        s = v.get("nodos_siguientes") or []
        p = v.get("nodos_previos") or []
        if len(s) != len(set(s)) or len(p) != len(set(p)):
            dup += 1
        if k in s or k in p:
            auto += 1
        for d in s:
            union.add((k, d))
        for o in p:
            union.add((o, k))
    return total, vivos, total - vivos, sig, prev, sig + prev, len(union), auto, dup


def vistas(nodos, madre, hijo):
    a, b = nodos.get(madre), nodos.get(hijo)
    return (a is not None and hijo in (a.get("nodos_siguientes") or []),
            b is not None and madre in (b.get("nodos_previos") or []))


def bfs(ady, a, b, tope=None):
    if a == b:
        return 0, [a]
    cola = collections.deque([(a, [a])])
    visto = {a}
    while cola:
        n, cam = cola.popleft()
        if tope is not None and len(cam) - 1 >= tope:
            continue
        for m in sorted(ady.get(n, ())):
            if m == b:
                return len(cam), cam + [b]
            if m not in visto:
                visto.add(m)
                cola.append((m, cam + [m]))
    return None, None


def t(s):
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


t("1. LAS OCHO CIFRAS DEL GRAFO, EN TRES PUNTOS DE GIT Y EN EL ARBOL")
print("ref | nodos | vivos | depre | sig | prev | suma | union | auto | dupint")
por_ref = {}
for ref, nom in REFS:
    n = grafo_de(ref)
    por_ref[ref] = n
    c = cifras(n)
    print("%-10s %-28s %5d %5d %4d | %5d %5d %6d %5d | %d %d"
          % (ref, nom, c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8]))
NODOS = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
c = cifras(NODOS)
print("%-10s %-28s %5d %5d %4d | %5d %5d %6d %5d | %d %d"
      % ("arbol", "de trabajo", c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8]))
ca = cifras(por_ref["fe24bd71"])
cc = cifras(por_ref["b32a83bf"])
print()
print("MOVIDAS cierre menos apertura: sig %+d, prev %+d, suma %+d, union %+d"
      % (cc[3] - ca[3], cc[4] - ca[4], cc[5] - ca[5], cc[6] - ca[6]))

t("2. EL MARCADOR DEL CRIBADO")
V = filas(VER)
cl = collections.Counter(f["clase"] for f in V)
pu = [f["puesto_intra"] for f in V]
print("n=%d  A %d  B %d  C %d  D %d" % (len(V), cl["A"], cl["B"], cl["C"], cl["D"]))
print("puestos: min %d  max %d  unicos %d  huecos %d"
      % (min(pu), max(pu), len(set(pu)), len(set(range(min(pu), max(pu) + 1)) - set(pu))))
nd = set()
for f in V:
    nd.add(frozenset((f["nodo_a"], f["nodo_b"])))
print("pares no dirigidos unicos: %d" % len(nd))

t("3. EL REGISTRO DE DECIDIDAS, CRUZADO FILA POR FILA CONTRA EL GRAFO DE HOY")
R = filas(REG)
dec = collections.Counter(f["decision"] for f in R)
tr = collections.Counter(f["tramo"] for f in R)
print("filas %d  unicos %d  %s" % (len(R), len(set((f["madre"], f["hijo"]) for f in R)), dict(dec)))
print("reparto por tramo: %s" % dict(sorted(tr.items())))
malas = []
for f in R:
    s, p = vistas(NODOS, f["madre"], f["hijo"])
    hay = s or p
    if (f["decision"] == "ESCRITA") != hay:
        malas.append((f["madre"], f["hijo"], f["decision"], s, p))
print("FILAS QUE NO CALZAN CON EL GRAFO: %d" % len(malas))
for m in malas:
    print("   ", m)

t("4. LA BOLSA, EL FILTRO Y EL DESFASE DEL CALIBRADO")
C = filas(CAL)
print("%s: %d filas, %d sin arista, %d con arista"
      % (CAL, len(C), sum(1 for f in C if not f["arista"]), sum(1 for f in C if f["arista"])))
B87, B86 = filas(F87), filas(F86)
print("FILTRADO_V87: %d filas   FILTRADO_V86: %d filas" % (len(B87), len(B86)))
k87 = [(f["madre"], f["hijo"]) for f in B87]
k86 = [(f["madre"], f["hijo"]) for f in B86]
fuera = [k for k in k86 if k not in set(k87)]
nuevas = [k for k in k87 if k not in set(k86)]
print("en V86 y ya no en V87: %d" % len(fuera))
for k in fuera:
    print("   ", k[0], "->", k[1])
print("NUEVAS en V87 que no estaban en V86: %d" % len(nuevas))
for k in nuevas:
    print("   ", k[0], "->", k[1])
desf = []
for f in C:
    s, p = vistas(NODOS, f["madre"], f["hijo"])
    if (s or p) != bool(f["arista"]):
        desf.append((f["madre"], f["hijo"], f["arista"], s, p))
print("DESFASE estricto (definicion mia, sin alias): %d fila(s)" % len(desf))

t("5. LA GUARDA, RECOMPUTADA DE CERO CON LAS DOS DEFINICIONES")
regset_todo = set((f["madre"], f["hijo"]) for f in R)
regset_nose = set((f["madre"], f["hijo"]) for f in R if f["decision"] == "NO SE ENLAZA")
regdec = dict(((f["madre"], f["hijo"]), f["decision"]) for f in R)
for nom, S in (("solo NO SE ENLAZA", regset_nose), ("cualquier decision", regset_todo)):
    pri = None
    for i, k in enumerate(k87):
        if k not in S:
            pri = i
            break
    if pri is None:
        print("%-22s -> TODA LA BOLSA DECIDIDA (%d de %d), VERDE" % (nom, len(k87), len(k87)))
        continue
    detras = sum(1 for k in k87[pri + 1:] if k in S)
    f = B87[pri]
    print("%-22s -> prefijo 0..%d, primera SIN DECIDIR indice %d (%s -> %s, paso %s, %s), decididas por detras %d, %s"
          % (nom, pri - 1, pri, f["madre"], f["hijo"], f["paso"], f["dominio"], detras,
             "VERDE" if detras == 0 else "ROJO"))

t("5b. LA GUARDA EN EL ESTADO PRE FILTRO (registro de la apertura, bolsa V87)")
R216 = [json.loads(l) for l in texto_de("fe24bd71", REG).splitlines() if l.strip()]
d216 = collections.Counter(f["decision"] for f in R216)
print("registro en fe24bd71 (apertura): %d filas, %s" % (len(R216), dict(d216)))
s216 = set((f["madre"], f["hijo"]) for f in R216)
pref = 0
for k in k87:
    if k in s216:
        pref += 1
    else:
        break
print("prefijo decidido de la bolsa V87 con el registro de apertura: %d" % pref)
print("primera sin decidir: indice %d, %s -> %s (paso %s, %s)"
      % (pref, B87[pref]["madre"], B87[pref]["hijo"], B87[pref]["paso"], B87[pref]["dominio"]))
sind = [i for i, k in enumerate(k87) if k not in s216]
print("sin decidir con el registro de apertura: %d -> %s" % (len(sind), sind))
print("el registro de apertura es PREFIJO EXACTO del de hoy (nada borrado): %s"
      % ([(f["madre"], f["hijo"]) for f in R216] == [(f["madre"], f["hijo"]) for f in R][:len(R216)]))

t("6. EL TRAMO 12 (INDICES 117 A 120), MEDIDO EN LAS DOS VISTAS")
esc, nol, incons, rota = [], [], [], []
for i in range(TRAMO_INI, TRAMO_FIN):
    f = B87[i]
    s, p = vistas(NODOS, f["madre"], f["hijo"])
    inv_s, inv_p = vistas(NODOS, f["hijo"], f["madre"])
    d = regdec.get((f["madre"], f["hijo"]), "SIN REGISTRO")
    if s != p:
        incons.append(i)
    if s and p:
        esc.append(i)
    else:
        nol.append(i)
    if inv_s or inv_p:
        rota.append(i)
    print("%3d %-58s -> %-46s sig=%-5s prev=%-5s inv=%-5s registro=%s"
          % (i, f["madre"], f["hijo"], s, p, inv_s or inv_p, d))
print()
print("ESCRITAS %d %s" % (len(esc), esc))
print("NO ESCRITAS %d" % len(nol))
print("INCONSISTENTES %d %s" % (len(incons), incons))
print("INVERSAS presentes %d %s" % (len(rota), rota))

t("7. LA VARA DE LA CADENA, BFS PROPIO SOBRE EL GRAFO DE ANTES DE ESCRIBIR")
ady = collections.defaultdict(set)
for k, v in NODOS.items():
    for d in (v.get("nodos_siguientes") or []):
        ady[k].add(d)
    for o in (v.get("nodos_previos") or []):
        ady[o].add(k)
for i in esc:
    f = B87[i]
    ady[f["madre"]].discard(f["hijo"])
alc6, sin6 = [], []
for i in range(TRAMO_INI, TRAMO_FIN):
    f = B87[i]
    n, cam = bfs(ady, f["madre"], f["hijo"], tope=6)
    if n is None:
        sin6.append(i)
        print("%3d SIN CAMINO PREVIO (tope 6)   %s -> %s" % (i, f["madre"], f["hijo"]))
    else:
        alc6.append((i, n))
        print("%3d ALCANZABLE (%d saltos)  %s" % (i, n, " -> ".join(cam)))
print()
print("ALCANZABLE %d: %s" % (len(alc6), alc6))
print("SIN CAMINO PREVIO %d: %s" % (len(sin6), sin6))
print()
print("HORIZONTE 30 sobre las SIN CAMINO PREVIO:")
for i in sin6:
    f = B87[i]
    n, cam = bfs(ady, f["madre"], f["hijo"], tope=30)
    print("%3d %s" % (i, "NI A 30 SALTOS" if n is None else "%d saltos: %s" % (n, " -> ".join(cam))))

t("8. LA VARA DE LA TAREA 4: VEREDICTO SIN DIRECCION Y RECIPROCA CONTRA V86")
vpar = {}
for f in V:
    vpar[frozenset((f["nodo_a"], f["nodo_b"]))] = f
rec86 = set((f["hijo"], f["madre"]) for f in B86)
con_ver, con_rec = [], []
for i in range(TRAMO_INI, TRAMO_FIN):
    f = B87[i]
    v = vpar.get(frozenset((f["madre"], f["hijo"])))
    if v:
        con_ver.append((i, f["madre"], f["hijo"], v["clase"], v["puesto_intra"], v["dominio"],
                        regdec.get((f["madre"], f["hijo"]), "SIN REGISTRO")))
    if (f["madre"], f["hijo"]) in rec86:
        con_rec.append(i)
for x in con_ver:
    print("%3d %-52s / %-44s clase %s puesto %4d %-12s registro %s" % x)
print("CON VEREDICTO: %d de 4    CON RECIPROCA EN V86: %d de 4" % (len(con_ver), len(con_rec)))

t("9. EL PATRON HISTORICO, RECOMPUTADO DE CERO")
print("tramo | par | clase | puesto | dominio | decision de hoy")
porTramo = collections.defaultdict(lambda: [0, 0, 0, 0])
for f in R:
    v = vpar.get(frozenset((f["madre"], f["hijo"])))
    if not v:
        continue
    a = porTramo[f["tramo"]]
    a[0] += 1
    if v["clase"] == "D":
        a[1] += 1
    if f["decision"] == "ESCRITA":
        a[2] += 1
    else:
        a[3] += 1
    print("%2d | %s -> %s | %s | %d | %s | %s"
          % (f["tramo"], f["madre"], f["hijo"], v["clase"], v["puesto_intra"],
             v["dominio"], f["decision"]))
print()
print("RESUMEN POR TRAMO (con veredicto | clase D | ESCRITA | NO SE ENLAZA):")
for k in sorted(porTramo):
    a = porTramo[k]
    print("  tramo %2d: %d|%d|%d|%d" % (k, a[0], a[1], a[2], a[3]))

t("10. LAS DOS QUE SIGUEN SIN ESCRIBIRSE (adjudicacion 5.9 del acta 85)")
claves = set((f["madre"], f["hijo"]) for f in C)
for par in (("descubrir_necesidades_del_cliente", "customer_needs_spreadsheet"),
            ("curva_caracteristica_operativa", "distribucion_poisson")):
    print("%s -> %s : en PASO_NODO_CALIBRADO = %s" % (par[0], par[1], par in claves))

t("11. EL CIERRE DE OP-E-01: TODA LA BOLSA DECIDIDA")
faltan = [k for k in k87 if k not in regset_todo]
print("bolsa V87 (%d) toda en el registro: %s" % (len(k87), not faltan))
print("unidades de la bolsa V87 SIN decision: %d %s" % (len(faltan), faltan))
print("filas del registro que NO estan en la bolsa V87: %d (bolsas viejas de tramos anteriores)"
      % len([k for k in regset_todo if k not in set(k87)]))
