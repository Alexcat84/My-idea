# -*- coding: utf-8 -*-
"""AUDITOR, vuelta 84. Todas las mediciones propias de la seccion 1 del acta,
en un solo instrumento, para que ninguna cifra del acta viva solo en la prosa.
Los pares se LEEN de los ficheros; ninguno se teclea.

  python docs/loop/_auditor_v84_mediciones.py > docs/loop/_auditor_v84_mediciones.txt
"""
import collections
import json
import re
import subprocess

GRAFO = "dataset/metadata/master_graph.json"
CAL = "docs/plan/PASO_NODO_CALIBRADO.jsonl"
F84 = "docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V84.jsonl"
F83 = "docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V83.jsonl"
REG = "docs/plan/OP_E_01_DECIDIDAS.jsonl"
VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
FILTRO_V84_TXT = "docs/loop/SALIDA_V84_TRAMO9_FILTRO_P91_GUARDA_CADENA.txt"

REFS = [("b59bb827", "apertura, acta 83"),
        ("9918fc1d", "apertura medida + TAREA 1"),
        ("5abd8616", "tras la TAREA 3"),
        ("6e387b1d", "cierre, HEAD")]

PARES_T1 = [("gestion_efectiva_benchmarking", "reconocimiento_publico_recompensas"),
            ("estructura_competencias_six_sigma_lean", "evaluacion_desempeno_proyectos"),
            ("poder_a_traves_de_la_accion", "compromiso_organismico_en_la_accion")]


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

    titulo("1.2. LAS OCHO CIFRAS DEL GRAFO EN CUATRO REFS DE GIT")
    for ref, que in REFS:
        crudo = subprocess.run(["git", "show", "%s:%s" % (ref, GRAFO)],
                               capture_output=True)
        n = json.loads(crudo.stdout.decode("utf-8"))["nodos"]
        t, viv, dep, sig, prev, suma, uni, auto, dup = cifras(n)
        print("  %s (%s): nodos %d vivos %d depre %d | sig %d prev %d suma %d "
              "union %d | auto %d dup %d" % (ref, que, t, viv, dep, sig, prev,
                                             suma, uni, auto, dup))
    t, viv, dep, sig, prev, suma, uni, auto, dup = cifras(nodos)
    print("  arbol de trabajo: nodos %d vivos %d depre %d | sig %d prev %d "
          "suma %d union %d | auto %d dup %d" % (t, viv, dep, sig, prev, suma,
                                                 uni, auto, dup))

    titulo("1.3. LAS TRES ARISTAS DE LA TAREA 1, EN LAS DOS VISTAS")
    for a, b in PARES_T1:
        s, p = vistas(nodos, a, b)
        invs, invp = vistas(nodos, b, a)
        print("  %s -> %s | en_sig_madre %s en_prev_hijo %s | INVERSAS %s/%s"
              % (a, b, s, p, invs, invp))

    titulo("1.4. EL MARCADOR DEL CRIBADO")
    ver = filas(VER)
    c = collections.Counter(v["clase"] for v in ver)
    puestos = [v["puesto_intra"] for v in ver]
    print("  n %d | A %d B %d C %d D %d" % (len(ver), c["A"], c["B"], c["C"],
                                            c["D"]))
    print("  puestos: min %d max %d unicos %d huecos %d"
          % (min(puestos), max(puestos), len(set(puestos)),
             len(set(range(min(puestos), max(puestos) + 1)) - set(puestos))))

    titulo("1.5. EL REGISTRO DE DECIDIDAS, CRUZADO CONTRA EL GRAFO DE HOY")
    reg = filas(REG)
    dec = collections.Counter(r["decision"] for r in reg)
    pares = [(r["madre"], r["hijo"]) for r in reg]
    print("  filas %d | ESCRITA %d | NO SE ENLAZA %d | pares unicos %d"
          % (len(reg), dec["ESCRITA"], dec["NO SE ENLAZA"], len(set(pares))))
    print("  por tramo: %s" % dict(sorted(collections.Counter(
        r["tramo"] for r in reg).items())))
    print("  paso NO RECONSTRUIBLE: %d | filas con nota: %d"
          % (sum(1 for r in reg if str(r.get("paso")) == "NO RECONSTRUIBLE"),
             sum(1 for r in reg if r.get("nota"))))
    malas = []
    for r in reg:
        s, p = vistas(nodos, r["madre"], r["hijo"])
        esperado = (s and p) if r["decision"] == "ESCRITA" else not (s or p)
        if not esperado:
            malas.append(r)
    print("  FILAS CUYA DECISION NO CALZA CON EL GRAFO DE HOY: %d" % len(malas))
    for r in malas:
        print("     %s -> %s (%s)" % (r["madre"], r["hijo"], r["decision"]))

    titulo("1.6. LA BOLSA, EL FILTRO Y EL DESFASE DEL CALIBRADO RASTREADO")
    cal = filas(CAL)
    f84 = filas(F84)
    f83 = filas(F83)
    print("  PASO_NODO_CALIBRADO.jsonl: %d filas, %d sin arista, %d con arista"
          % (len(cal), sum(1 for r in cal if not r.get("arista")),
             sum(1 for r in cal if r.get("arista"))))
    print("  FILTRADO_V84: %d | FILTRADO_V83: %d" % (len(f84), len(f83)))
    corto = min(len(f84), len(f83))
    print("  V84 y V83 coinciden par a par hasta donde alcanza el mas corto: %s"
          % ([(r["madre"], r["hijo"]) for r in f84][:corto]
             == [(r["madre"], r["hijo"]) for r in f83][:corto]))
    en84 = {(x["madre"], x["hijo"]) for x in f84}
    fuera = [(r["madre"], r["hijo"]) for r in f83 if (r["madre"], r["hijo"]) not in en84]
    print("  unidades que estaban en V83 y YA NO estan en V84: %d" % len(fuera))
    for a, b in fuera:
        print("     %s -> %s" % (a, b))

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
    print("  DESFASE del calibrado rastreado contra el grafo de hoy: %d filas"
          % len(desfase))
    for r in desfase:
        print("     %s -> %s (campo arista %s)"
              % (r["madre"], r["hijo"], r.get("arista")))

    titulo("1.7. LA GUARDA DEL REGISTRO SOBRE LA BOLSA V84, RECOMPUTADA")
    en_reg = {(r["madre"], r["hijo"]) for r in reg}
    primera = None
    fuera_de_orden = []
    visto_sin = False
    for i, r in enumerate(f84):
        decidida = (r["madre"], r["hijo"]) in en_reg
        if not decidida and primera is None:
            primera = (i, r)
        if not decidida:
            visto_sin = True
        elif visto_sin:
            fuera_de_orden.append(i)
    print("  prefijo de decididas: indices 0 a %d (%d unidades)"
          % (primera[0] - 1, primera[0]))
    print("  primera SIN DECIDIR: indice %d, %s -> %s (paso %s, %s)"
          % (primera[0], primera[1]["madre"], primera[1]["hijo"],
             primera[1]["paso"], primera[1]["dominio"]))
    print("  decididas por detras de una sin decidir: %d %s"
          % (len(fuera_de_orden), fuera_de_orden[:10]))
    print("  sin decidir restantes tras las 30 frescas: %d"
          % sum(1 for r in f84[primera[0] + 30:]
                if (r["madre"], r["hijo"]) not in en_reg))

    base = primera[0]
    titulo("1.8. EL TRAMO 9 (indices %d..%d), MEDIDO EN LAS DOS VISTAS"
           % (base, base + 29))
    escritas, noenl, incons, inversas = [], [], [], []
    for i in range(base, base + 30):
        r = f84[i]
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

    titulo("1.9. LA VARA DE LA CADENA, RECOMPUTADA DE CERO (BFS PROPIO)")
    nuevas = {(f84[i]["madre"], f84[i]["hijo"]) for i in escritas}
    ady = collections.defaultdict(set)
    for k, v in nodos.items():
        for d in (v.get("nodos_siguientes") or []):
            if (k, d) not in nuevas:
                ady[k].add(d)
        for o in (v.get("nodos_previos") or []):
            if (o, k) not in nuevas:
                ady[o].add(k)
    print("  (el grafo se mide SIN las tres aristas nuevas del tramo 9, o sea")
    print("   como estaba antes de escribir; horizonte 6 y contraste a 30)")
    sin6 = []
    sin30 = []
    for i in range(base, base + 30):
        r = f84[i]
        d6, c6 = bfs(ady, r["madre"], r["hijo"], tope=6)
        celda = "ALCANZABLE (%d saltos)" % d6 if d6 is not None else "SIN CAMINO PREVIO"
        extra = ""
        if d6 is not None:
            extra = "   via %s" % (" -> ".join(c6[1:-1]) if len(c6) > 2 else "(directo)")
        else:
            sin6.append(i)
            d30, c30 = bfs(ady, r["madre"], r["hijo"], tope=30)
            if d30 is not None:
                extra = "   [HORIZONTE 30: %d saltos]" % d30
            else:
                sin30.append(i)
                extra = "   [ni a 30 saltos]"
        print("  %3d %-24s%s" % (i, celda, extra))
    print("  SIN CAMINO PREVIO (horizonte 6): %d %s" % (len(sin6), sin6))
    print("  SIN CAMINO ni a 30 saltos: %d %s" % (len(sin30), sin30))

    titulo("1.10. LA VARA DE LA TAREA 4 (LAS 30 FRESCAS DEL TRAMO 9)")
    idx = {}
    for v in ver:
        idx[frozenset((v["nodo_a"], v["nodo_b"]))] = v
    print("  veredictos %d | pares no dirigidos unicos %d | bolsa filtrada V83 %d"
          % (len(ver), len(idx), len(f83)))
    txt = open(FILTRO_V84_TXT, encoding="utf-8", errors="replace").read()
    leidos = re.findall(r"^\s*(\d+):\s+([a-z0-9_]+) -> ([a-z0-9_]+)", txt, re.M)
    print("  unidades leidas del fichero del filtro V84: %d" % len(leidos))
    con = rec = 0
    for i in range(base, base + 30):
        r = f84[i]
        a, b = r["madre"], r["hijo"]
        v = idx.get(frozenset((a, b)))
        if v:
            con += 1
            print("  %3d %s -> %s | VEREDICTO clase %s puesto_intra %s (%s) "
                  "sentido %s" % (i, a, b, v["clase"], v["puesto_intra"],
                                  v["dominio"],
                                  "mismo" if v["nodo_a"] == a else "contrario"))
        if any(x["madre"] == b and x["hijo"] == a for x in f83):
            rec += 1
            print("  %3d %s -> %s | RECIPROCA en la bolsa V83" % (i, a, b))
    print("  frescas con veredicto: %d de 30 | reciprocas: %d de 30" % (con, rec))
    print()
    print("FIN")


main()
