# -*- coding: utf-8 -*-
"""AUDITOR, vuelta 83. Todas las mediciones propias de la seccion 1 del acta,
en un solo instrumento, para que ninguna cifra del acta viva solo en la prosa.
Los pares se LEEN de los ficheros; ninguno se teclea.

  python docs/loop/_auditor_v83_mediciones.py > docs/loop/_auditor_v83_mediciones.txt
"""
import collections
import json
import re
import subprocess

RAIZ = "."
GRAFO = "dataset/metadata/master_graph.json"
CAL = "docs/plan/PASO_NODO_CALIBRADO.jsonl"
F83 = "docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V83.jsonl"
F82 = "docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V82.jsonl"
REG = "docs/plan/OP_E_01_DECIDIDAS.jsonl"
VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
FILTRO_V82_TXT = "docs/loop/SALIDA_V82_TRAMO7_FILTRO_P91_GUARDA_CADENA.txt"

REFS = [("0af51e43", "apertura, acta 82"),
        ("9b0b76a1", "TAREA 0, medicion de apertura"),
        ("dd8f539f", "tras la TAREA 3"),
        ("2e974a63", "cierre, HEAD")]


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
        for m in ady.get(n, ()):
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

    titulo("1.5. EL MARCADOR DEL CRIBADO")
    ver = filas(VER)
    c = collections.Counter(v["clase"] for v in ver)
    puestos = [v["puesto_intra"] for v in ver]
    print("  n %d | A %d B %d C %d D %d" % (len(ver), c["A"], c["B"], c["C"],
                                            c["D"]))
    print("  puestos: min %d max %d unicos %d huecos %d"
          % (min(puestos), max(puestos), len(set(puestos)),
             len(set(range(min(puestos), max(puestos) + 1)) - set(puestos))))

    titulo("1.7. EL REGISTRO DE DECIDIDAS, CRUZADO CONTRA EL GRAFO DE HOY")
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

    titulo("1.8. LA BOLSA, EL FILTRO Y EL DESFASE DEL CALIBRADO RASTREADO")
    cal = filas(CAL)
    f83 = filas(F83)
    f82 = filas(F82)
    print("  PASO_NODO_CALIBRADO.jsonl: %d filas, %d sin arista"
          % (len(cal), sum(1 for r in cal if not r.get("arista"))))
    print("  FILTRADO_V83: %d | FILTRADO_V82: %d | iguales fila a fila y en "
          "orden: %s" % (len(f83), len(f82),
                         [(r["madre"], r["hijo"]) for r in f83]
                         == [(r["madre"], r["hijo"]) for r in f82]))

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

    desfase = []
    for r in cal:
        real = r["hijo"] in vecinos(r["madre"]) or r["madre"] in vecinos(r["hijo"])
        if bool(r.get("arista")) != real:
            desfase.append(r)
    print("  DESFASE del calibrado rastreado contra el grafo de hoy, con la")
    print("  definicion del propio calibrador (vecino no dirigido): %d filas"
          % len(desfase))
    for r in desfase:
        print("     %s -> %s (campo arista %s)"
              % (r["madre"], r["hijo"], r.get("arista")))

    titulo("1.9. EL TRAMO 8, MEDIDO CONTRA EL GRAFO EN LAS DOS VISTAS")
    escritas, noenl, incons, inversas = [], [], [], []
    for i in range(30, 60):
        r = f83[i]
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

    titulo("1.10. LA VARA DE LA CADENA, RECOMPUTADA DE CERO (BFS PROPIO)")
    nuevas = {(f83[i]["madre"], f83[i]["hijo"]) for i in escritas}
    ady = collections.defaultdict(set)
    for k, v in nodos.items():
        for d in (v.get("nodos_siguientes") or []):
            if (k, d) not in nuevas:
                ady[k].add(d)
        for o in (v.get("nodos_previos") or []):
            if (o, k) not in nuevas:
                ady[o].add(k)
    print("  (el grafo se mide SIN las nueve aristas nuevas, o sea como estaba")
    print("   antes de escribir; el instrumento tiene horizonte de 6 saltos)")
    for i in range(30, 60):
        r = f83[i]
        d6, _ = bfs(ady, r["madre"], r["hijo"], tope=6)
        dinf, camino = bfs(ady, r["madre"], r["hijo"])
        celda = "ALCANZABLE (%d saltos)" % d6 if d6 is not None else "SIN CAMINO PREVIO"
        extra = ""
        if d6 is None and dinf is not None:
            extra = "   [SIN HORIZONTE: %d saltos via %s]" % (
                dinf, " -> ".join(camino[1:-1]) if len(camino) > 2 else "(directo)")
        elif d6 is not None:
            extra = "   via %s" % (" -> ".join(camino[1:-1])
                                   if len(camino) > 2 else "(directo)")
        print("  %3d %-24s%s" % (i, celda, extra))

    titulo("1.11. LA VARA DE LA TAREA 4 (LAS 3 FRESCAS DEL TRAMO 7)")
    idx = {}
    for v in ver:
        idx[frozenset((v["nodo_a"], v["nodo_b"]))] = v
    print("  veredictos %d | pares no dirigidos unicos %d | bolsa filtrada V82 %d"
          % (len(ver), len(idx), len(f82)))
    txt = open(FILTRO_V82_TXT, encoding="utf-8", errors="replace").read()
    leidos = re.findall(r"^\s*(\d+):\s+([a-z0-9_]+) -> ([a-z0-9_]+)", txt, re.M)
    print("  unidades leidas del fichero del filtro V82: %d" % len(leidos))
    con = rec = 0
    for i, a, b in [(int(x), y, z) for x, y, z in leidos][-3:]:
        v = idx.get(frozenset((a, b)))
        if v:
            con += 1
            print("  %3d %s -> %s | VEREDICTO clase %s puesto_intra %s (%s)"
                  % (i, a, b, v["clase"], v["puesto_intra"], v["dominio"]))
        else:
            print("  %3d %s -> %s | sin veredicto" % (i, a, b))
        if any(r["madre"] == b and r["hijo"] == a for r in f82):
            rec += 1
    print("  frescas con veredicto: %d | reciprocas en la bolsa: %d" % (con, rec))

    titulo("3. LA COLA DE LA VUELTA SIGUIENTE, CON Y SIN EL TRAMO 8 EN EL REGISTRO")
    en_reg = {(r["madre"], r["hijo"]) for r in reg}
    tramo8 = {(f83[i]["madre"], f83[i]["hijo"]) for i in range(30, 60)}
    print("  decisiones del tramo 8 dentro del registro de hoy: %d de 30"
          % len(tramo8 & en_reg))
    restante = [r for r in f83 if (r["madre"], r["hijo"]) not in nuevas]
    print("  bolsa tras salir las nueve escritas: %d unidades" % len(restante))
    for etiqueta, conjunto in (("registro DE HOY (96 filas)", en_reg),
                               ("registro RE-HORNEADO (con el tramo 8)",
                                en_reg | tramo8)):
        primera = None
        for i, r in enumerate(restante):
            if (r["madre"], r["hijo"]) not in conjunto:
                primera = (i, r)
                break
        dec = len([r for r in restante if (r["madre"], r["hijo"]) in conjunto])
        sind = len(restante) - dec
        print("  con el %s: primera sin decidir indice %d, %s -> %s (paso %s, %s)"
              % (etiqueta, primera[0], primera[1]["madre"], primera[1]["hijo"],
                 primera[1]["paso"], primera[1]["dominio"]))
        print("     decididas que siguen en la bolsa: %d | sin decidir: %d"
              % (dec, sind))
    print()
    print("FIN")


main()
