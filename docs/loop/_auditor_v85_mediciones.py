# -*- coding: utf-8 -*-
"""AUDITOR, vuelta 85. Todas las mediciones propias de la seccion 1 del acta,
en un solo instrumento. Los pares se LEEN de los ficheros; ninguno se teclea.

  python docs/loop/_auditor_v85_mediciones.py > docs/loop/_auditor_v85_mediciones.txt
"""
import collections
import json
import subprocess

GRAFO = "dataset/metadata/master_graph.json"
CAL = "docs/plan/PASO_NODO_CALIBRADO.jsonl"
F85 = "docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V85.jsonl"
F84 = "docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V84.jsonl"
REG = "docs/plan/OP_E_01_DECIDIDAS.jsonl"
VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"

REFS = [("2d75140e", "apertura, acta 84"),
        ("b0fd12ff", "apertura medida + TAREA 2"),
        ("a905fe47", "TAREA 3, instrumento"),
        ("425736f2", "tras la TAREA 4"),
        ("0933a988", "cierre, HEAD")]


def filas(ruta):
    return [json.loads(l) for l in open(ruta, encoding="utf-8") if l.strip()]


def cifras(nodos):
    total = len(nodos)
    vivos = sum(1 for v in nodos.values() if not v.get("deprecado"))
    sig = sum(len(v.get("nodos_siguientes") or []) for v in nodos.values())
    prev = sum(len(v.get("nodos_previos") or []) for v in nodos.values())
    union = set()
    auto = 0
    dup = 0
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
    a = nodos.get(madre)
    b = nodos.get(hijo)
    s = a is not None and hijo in (a.get("nodos_siguientes") or [])
    p = b is not None and madre in (b.get("nodos_previos") or [])
    return s, p


def bfs(ady, a, b, tope=None):
    if a == b:
        return 0, []
    cola = collections.deque([(a, [a])])
    visto = {a}
    while cola:
        n, camino = cola.popleft()
        if tope is not None and len(camino) - 1 >= tope:
            continue
        for m in sorted(ady.get(n, ())):
            if m == b:
                return len(camino), camino + [b]
            if m not in visto:
                visto.add(m)
                cola.append((m, camino + [m]))
    return None, None


def titulo(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def main():
    nodos = json.load(open(GRAFO, encoding="utf-8"))["nodos"]

    titulo("1.A. LAS OCHO CIFRAS DEL GRAFO EN CINCO REFS DE GIT")
    for ref, que in REFS:
        crudo = subprocess.run(["git", "show", "%s:%s" % (ref, GRAFO)],
                               capture_output=True)
        n = json.loads(crudo.stdout.decode("utf-8"))["nodos"]
        t, viv, dep, sig, prev, suma, uni, auto, dup = cifras(n)
        print("  %s (%-28s): nodos %d vivos %d depre %d | sig %d prev %d "
              "suma %d union %d | auto %d dup %d"
              % (ref, que, t, viv, dep, sig, prev, suma, uni, auto, dup))
    t, viv, dep, sig, prev, suma, uni, auto, dup = cifras(nodos)
    print("  arbol de trabajo                                : nodos %d vivos %d "
          "depre %d | sig %d prev %d suma %d union %d | auto %d dup %d"
          % (t, viv, dep, sig, prev, suma, uni, auto, dup))

    titulo("1.B. EL MARCADOR DEL CRIBADO")
    ver = filas(VER)
    c = collections.Counter(v["clase"] for v in ver)
    puestos = [v["puesto_intra"] for v in ver]
    print("  n %d | A %d B %d C %d D %d" % (len(ver), c["A"], c["B"], c["C"],
                                            c["D"]))
    print("  puestos: min %d max %d unicos %d huecos %d"
          % (min(puestos), max(puestos), len(set(puestos)),
             len(set(range(min(puestos), max(puestos) + 1)) - set(puestos))))

    titulo("1.C. EL REGISTRO DE DECIDIDAS, CRUZADO CONTRA EL GRAFO DE HOY")
    reg = filas(REG)
    dec = collections.Counter(r["decision"] for r in reg)
    pares = [(r["madre"], r["hijo"]) for r in reg]
    print("  filas %d | ESCRITA %d | NO SE ENLAZA %d | pares unicos %d"
          % (len(reg), dec["ESCRITA"], dec["NO SE ENLAZA"], len(set(pares))))
    print("  por tramo: %s" % dict(sorted(collections.Counter(
        r["tramo"] for r in reg).items())))
    print("  por fichero_origen:")
    for k, n in sorted(collections.Counter(
            str(r.get("fichero_origen")) for r in reg).items()):
        print("     %-52s %d" % (k, n))
    malas = []
    for r in reg:
        s, p = vistas(nodos, r["madre"], r["hijo"])
        esperado = (s and p) if r["decision"] == "ESCRITA" else not (s or p)
        if not esperado:
            malas.append(r)
    print("  FILAS CUYA DECISION NO CALZA CON EL GRAFO DE HOY: %d" % len(malas))
    for r in malas:
        print("     %s -> %s (%s)" % (r["madre"], r["hijo"], r["decision"]))

    titulo("1.D. LA BOLSA, EL FILTRO Y EL DESFASE DEL CALIBRADO")
    cal = filas(CAL)
    f85 = filas(F85)
    f84 = filas(F84)
    print("  PASO_NODO_CALIBRADO.jsonl: %d filas, %d sin arista, %d con arista"
          % (len(cal), sum(1 for r in cal if not r.get("arista")),
             sum(1 for r in cal if r.get("arista"))))
    print("  FILTRADO_V85: %d | FILTRADO_V84: %d" % (len(f85), len(f84)))
    en85 = {(x["madre"], x["hijo"]) for x in f85}
    fuera = [(r["madre"], r["hijo"]) for r in f84
             if (r["madre"], r["hijo"]) not in en85]
    print("  unidades que estaban en V84 y YA NO estan en V85: %d" % len(fuera))
    for a, b in fuera:
        print("     %s -> %s" % (a, b))
    en84 = {(x["madre"], x["hijo"]) for x in f84}
    nuevas85 = [(r["madre"], r["hijo"]) for r in f85
                if (r["madre"], r["hijo"]) not in en84]
    print("  unidades NUEVAS en V85 que no estaban en V84: %d" % len(nuevas85))
    for a, b in nuevas85[:20]:
        print("     %s -> %s" % (a, b))
    corto = min(len(f84), len(f85))
    print("  V85 y V84 coinciden par a par hasta el mas corto: %s"
          % ([(r["madre"], r["hijo"]) for r in f85][:corto]
             == [(r["madre"], r["hijo"]) for r in f84][:corto]))

    def vecinos(n):
        g = nodos.get(n)
        if not g:
            return set()
        out = set()
        for campo in ("nodos_siguientes", "nodos_previos"):
            for y in (g.get(campo) or []):
                if y in nodos and y != n:
                    out.add(y)
        return out

    desfase = [r for r in cal
               if bool(r.get("arista")) != (r["hijo"] in vecinos(r["madre"])
                                            or r["madre"] in vecinos(r["hijo"]))]
    print("  DESFASE del calibrado contra el grafo de hoy: %d filas" % len(desfase))
    for r in desfase:
        print("     %s -> %s (campo arista %s)"
              % (r["madre"], r["hijo"], r.get("arista")))

    titulo("1.E. LA GUARDA SOBRE LA BOLSA V85, CON LAS DOS DEFINICIONES")
    en_reg_no = {(r["madre"], r["hijo"]) for r in reg
                 if r["decision"] == "NO SE ENLAZA"}
    en_reg_todo = {(r["madre"], r["hijo"]) for r in reg}
    for etiq, conj in (("SOLO NO SE ENLAZA (la del instrumento)", en_reg_no),
                       ("CUALQUIER decision registrada", en_reg_todo)):
        primera = None
        fuera_de_orden = []
        visto_sin = False
        for i, r in enumerate(f85):
            decidida = (r["madre"], r["hijo"]) in conj
            if not decidida and primera is None:
                primera = (i, r)
            if not decidida:
                visto_sin = True
            elif visto_sin:
                fuera_de_orden.append(i)
        print("  --- definicion de DECIDIDA: %s" % etiq)
        if primera is None:
            print("      no queda ninguna sin decidir")
            continue
        print("      prefijo: indices 0 a %d (%d unidades)"
              % (primera[0] - 1, primera[0]))
        print("      primera SIN DECIDIR: indice %d, %s -> %s (paso %s, %s)"
              % (primera[0], primera[1]["madre"], primera[1]["hijo"],
                 primera[1]["paso"], primera[1]["dominio"]))
        print("      decididas por detras de una sin decidir: %d %s"
              % (len(fuera_de_orden), fuera_de_orden[:25]))
        print("      sin decidir restantes tras las 30 frescas: %d"
              % sum(1 for r in f85[primera[0] + 30:]
                    if (r["madre"], r["hijo"]) not in conj))

    base = 72
    titulo("1.F. EL TRAMO 10 (indices %d..%d de V85), EN LAS DOS VISTAS"
           % (base, base + 29))
    escritas, noenl, incons, inversas = [], [], [], []
    for i in range(base, base + 30):
        r = f85[i]
        s, p = vistas(nodos, r["madre"], r["hijo"])
        invs, invp = vistas(nodos, r["hijo"], r["madre"])
        if s and p:
            escritas.append(i)
        elif not (s or p):
            noenl.append(i)
        else:
            incons.append(i)
        if invs or invp:
            inversas.append(i)
        estado = "ESCRITA" if (s and p) else ("NO SE ENLAZA" if not (s or p)
                                              else "INCONSISTENTE")
        print("  %3d %-14s paso %-3s %s -> %s"
              % (i, estado, r["paso"], r["madre"], r["hijo"]))
    print("  ESCRITAS %d %s" % (len(escritas), escritas))
    print("  NO SE ENLAZA %d | INCONSISTENTES %d | ESCALERA ROTA %d"
          % (len(noenl), len(incons), len(inversas)))

    titulo("1.G. LAS TRES ARISTAS DE LA TAREA 2, EN LAS DOS VISTAS")
    t2 = [r for r in reg if "TAREA2" in str(r.get("fichero_origen")).upper()]
    print("  (filas del registro cuyo fichero_origen nombra la TAREA 2: %d)"
          % len(t2))
    pares_t2 = [(r["madre"], r["hijo"]) for r in t2]
    for a, b in pares_t2:
        s, p = vistas(nodos, a, b)
        invs, invp = vistas(nodos, b, a)
        print("  %s -> %s | en_sig_madre %s en_prev_hijo %s | INVERSAS %s/%s"
              % (a, b, s, p, invs, invp))

    titulo("1.H. LA VARA DE LA CADENA DEL TRAMO 10, BFS PROPIO, SIN LAS NUEVAS")
    nuevas = {(f85[i]["madre"], f85[i]["hijo"]) for i in escritas}
    nuevas |= set(pares_t2)
    ady = collections.defaultdict(set)
    for k, v in nodos.items():
        for d in (v.get("nodos_siguientes") or []):
            if (k, d) not in nuevas:
                ady[k].add(d)
        for o in (v.get("nodos_previos") or []):
            if (o, k) not in nuevas:
                ady[o].add(k)
    print("  (grafo SIN las %d aristas del tramo 10 y SIN las %d de la TAREA 2)"
          % (len(escritas), len(pares_t2)))
    sin6, sin30 = [], []
    for i in range(base, base + 30):
        r = f85[i]
        d6, c6 = bfs(ady, r["madre"], r["hijo"], tope=6)
        celda = "ALCANZABLE (%d saltos)" % d6 if d6 is not None else "SIN CAMINO PREVIO"
        extra = ""
        if d6 is not None:
            extra = "   via %s" % (" -> ".join(c6[1:-1]) if len(c6) > 2 else "(directo)")
        else:
            sin6.append(i)
            d30, _ = bfs(ady, r["madre"], r["hijo"], tope=30)
            if d30 is not None:
                extra = "   [HORIZONTE 30: %d saltos]" % d30
            else:
                sin30.append(i)
                extra = "   [ni a 30 saltos]"
        print("  %3d %-24s%s" % (i, celda, extra))
    print("  SIN CAMINO PREVIO a 6: %d %s" % (len(sin6), sin6))
    print("  NI A 30 SALTOS: %d %s" % (len(sin30), sin30))

    titulo("1.I. LA VARA DE LA TAREA 5, RECOMPUTADA")
    pares_ver = {}
    for v in ver:
        pares_ver[frozenset((v["nodo_a"], v["nodo_b"]))] = v
    print("  veredictos leidos: %d | pares no dirigidos unicos: %d"
          % (len(ver), len(pares_ver)))
    print("  bolsa filtrada V84: %d unidades" % len(f84))
    reciproca = {(r["hijo"], r["madre"]) for r in f84}
    con_ver, con_rec = [], []
    for i in range(base, base + 30):
        r = f85[i]
        v = pares_ver.get(frozenset((r["madre"], r["hijo"])))
        if v:
            con_ver.append((i, r, v))
        if (r["madre"], r["hijo"]) in reciproca:
            con_rec.append(i)
    print("  RESUMEN: %d de 30 con veredicto, %d de 30 con reciproca"
          % (len(con_ver), len(con_rec)))
    for i, r, v in con_ver:
        print("     %3d %s / %s | clase %s | puesto %d | %s"
              % (i, r["madre"], r["hijo"], v["clase"], v["puesto_intra"],
                 v["dominio"]))


main()
