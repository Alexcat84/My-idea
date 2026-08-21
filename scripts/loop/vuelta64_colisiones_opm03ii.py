# -*- coding: utf-8 -*-
"""vuelta64_colisiones_opm03ii.py . MIDE LAS COLISIONES DE CLASE QUE LA FUSION
OP-M-03-II FABRICA, SU CUENTA ESPERADA SOBRE EL ARBOL DE ANTES, Y DE QUIEN SON
LOS PUESTOS QUE CHOCAN.

POR QUE NACE, y se dice con la caida que lo levanto: en esta misma vuelta corri
scripts/loop/vuelta51_censo_colisiones.py con --esperadas 0 SIN HABER MEDIDO
ESA CIFRA. La cuenta esperada salio de mi cabeza y no de un instrumento, que es
justo lo que la regla 1 prohibe, y el censo midio 2. La cifra esperada se mide
AQUI, sobre el arbol de ANTES de fundir, y se compara con la de despues.

LA ARITMETICA ES LA DE LA CASA y no se reinventa: se resuelven los 3.388
veredictos por la cadena de alias (P.1), un auto-par NO es colision, y hay
colision cuando DOS O MAS CLASES distintas caen sobre el MISMO par resuelto.

LO QUE ANADE, y es lo que la decision necesita: para cada puesto que choca dice
SI ESE PUESTO ES DE ALGUIEN, o sea si sus dos nodos estan en la nomina de alguna
operacion PENDIENTE de docs/plan/OPERACIONES.jsonl, y si el puesto esta nombrado
literalmente en el texto de alguna ficha. Un veredicto que una mesa tiene
reservado no lo re-lee el ejecutor.

DE SOLO LECTURA ENTERO. No toca ni un veredicto ni un nodo.

Uso: python scripts/loop/vuelta64_colisiones_opm03ii.py --antes <hash>
"""
import argparse
import io
import json
import os
import subprocess
import sys
from collections import defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
SUP = "pivote_o_proceder"
MUERE = "pivotar_o_proceder"


def alias_de_arbol(commit=None):
    """El mapa de alias del arbol de hoy, o del arbol de un commit."""
    alias = {}
    if commit is None:
        for f in os.listdir(NODOS):
            if f.endswith(".json"):
                j = json.load(io.open(os.path.join(NODOS, f), encoding="utf-8"))
                for a in (j.get("ids_alias") or []):
                    alias.setdefault(a, j.get("node_id") or f[:-5])
        return alias
    rutas = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", commit, "dataset/nodos/"],
        cwd=RAIZ).decode("utf-8").split(chr(10))
    bruto = subprocess.check_output(
        ["git", "cat-file", "--batch"], cwd=RAIZ,
        input=chr(10).join("%s:%s" % (commit, r) for r in rutas if r.strip()).encode())
    # el batch devuelve cabecera y contenido; se parsea por tamano
    pos, datos = 0, bruto
    while pos < len(datos):
        fin = datos.index(b"\n", pos)
        cab = datos[pos:fin].decode("utf-8").split()
        if len(cab) < 3:
            pos = fin + 1
            continue
        tam = int(cab[2])
        cuerpo = datos[fin + 1:fin + 1 + tam]
        pos = fin + 1 + tam + 1
        try:
            j = json.loads(cuerpo.decode("utf-8"))
        except Exception:
            continue
        nid = j.get("node_id")
        if nid:
            for a in (j.get("ids_alias") or []):
                alias.setdefault(a, nid)
    return alias


def resolver(alias):
    def r(x):
        v = set()
        while x in alias and x not in v:
            v.add(x)
            x = alias[x]
        return x
    return r


def colisiones(alias, veredictos):
    r = resolver(alias)
    por_par = defaultdict(list)
    for v in veredictos:
        a, b = r(v["nodo_a"]), r(v["nodo_b"])
        if a == b:
            continue          # auto-par: NO es colision
        por_par[tuple(sorted((a, b)))].append(v)
    out = []
    for par, vs in sorted(por_par.items()):
        if len({v["clase"] for v in vs}) > 1:
            out.append((par, vs))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--antes", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    veredictos = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    al_hoy = alias_de_arbol()
    al_ant = alias_de_arbol(a.antes)

    print("=" * 78)
    print("LAS COLISIONES DE CLASE DE OP-M-03-II: ESPERADAS Y MEDIDAS")
    print("  veredictos leidos: %d" % len(veredictos))
    print("  alias del arbol de HOY : %d" % len(al_hoy))
    print("  alias del arbol de %s: %d" % (a.antes, len(al_ant)))
    print("=" * 78)

    print()
    print("--- 1. ANTES DE FUNDIR, sobre el arbol de %s ---" % a.antes)
    c_ant = colisiones(al_ant, veredictos)
    print("   colisiones vigentes: %d" % len(c_ant))

    print()
    print("--- 2. LA CUENTA ESPERADA, SIMULADA SOBRE EL ARBOL DE ANTES ---")
    print("   Se anade al mapa de alias de ANTES la sola entrada que la fusion")
    print("   crea (%s -> %s) y se vuelve a contar." % (MUERE, SUP))
    sim = dict(al_ant)
    sim[MUERE] = SUP
    c_sim = colisiones(sim, veredictos)
    print("   colisiones ESPERADAS tras la fusion: %d" % len(c_sim))
    for par, vs in c_sim:
        print("      par resuelto: %s contra %s" % par)
        for v in sorted(vs, key=lambda x: x["puesto_intra"]):
            print("         puesto %-6d %s | crudo: %s + %s"
                  % (v["puesto_intra"], v["clase"], v["nodo_a"], v["nodo_b"]))

    print()
    print("--- 3. DESPUES DE FUNDIR, sobre el arbol de HOY ---")
    c_hoy = colisiones(al_hoy, veredictos)
    print("   colisiones MEDIDAS: %d" % len(c_hoy))
    for par, vs in c_hoy:
        print("      par resuelto: %s contra %s" % par)
        for v in sorted(vs, key=lambda x: x["puesto_intra"]):
            print("         puesto %-6d %s | crudo: %s + %s"
                  % (v["puesto_intra"], v["clase"], v["nodo_a"], v["nodo_b"]))

    calza = len(c_sim) == len(c_hoy) and {p for p, _ in c_sim} == {p for p, _ in c_hoy}
    print()
    print("   ESPERADAS %d | MEDIDAS %d | LAS MISMAS: %s | CALZA: %s"
          % (len(c_sim), len(c_hoy), {p for p, _ in c_sim} == {p for p, _ in c_hoy},
             "SI" if calza else "NO"))
    nuevas = len(c_hoy) - len(c_ant)
    print("   colisiones que ESTA fusion fabrica: %d (antes %d, despues %d)"
          % (nuevas, len(c_ant), len(c_hoy)))

    print()
    print("--- 4. DE QUIEN SON LOS PUESTOS QUE CHOCAN ---")
    ops = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    for par, vs in c_hoy:
        print()
        print("   par resuelto: %s contra %s" % par)
        for v in sorted(vs, key=lambda x: x["puesto_intra"]):
            p = v["puesto_intra"]
            duenos = []
            for o in ops:
                nom = set(o.get("nodos") or [])
                if v["nodo_a"] in nom or v["nodo_b"] in nom:
                    duenos.append("%s (%s, %s)" % (o["id_op"], o.get("fase"), o.get("estado")))
            citado = []
            for o in ops:
                if str(p) in json.dumps(o, ensure_ascii=False):
                    citado.append(o["id_op"])
            print("      puesto %-6d %s | %s + %s" % (p, v["clase"], v["nodo_a"], v["nodo_b"]))
            print("         nodos en nomina de: %s" % (", ".join(duenos) or "NINGUNA"))
            print("         el numero del puesto aparece en el texto de: %s"
                  % (", ".join(citado) or "NINGUNA ficha"))

    print()
    print("--- 5. SE RESUELVEN SOLAS CUANDO CORRA LO QUE YA ESTA ESCRITO? ---")
    print("   Se simula, sobre el arbol de HOY, cada fusion de mesa PENDIENTE que")
    print("   toque a un nodo de los pares que chocan, y se vuelve a contar.")
    pendientes = [o for o in ops
                  if o.get("fase") == "03_FUSIONES" and o.get("superviviente")
                  and (o.get("nodos") or [])
                  and o["id_op"] != "OP-M-03-II"]
    nodos_en_choque = {x for par, vs in c_hoy for v in vs
                       for x in (v["nodo_a"], v["nodo_b"])}
    sim2 = dict(al_hoy)
    aplicadas = []
    for o in pendientes:
        if not (set(o["nodos"]) & nodos_en_choque):
            continue
        # solo si su par sigue SIN consumir hoy
        r = resolver(al_hoy)
        if len({r(x) for x in o["nodos"]}) == 1:
            continue
        for x in (o.get("eliminar") or []):
            sim2[x] = o["superviviente"]
        aplicadas.append("%s (%s absorbe %s)"
                         % (o["id_op"], o["superviviente"], ", ".join(o.get("eliminar") or [])))
    print("   fusiones pendientes que tocan un nodo en choque: %d" % len(aplicadas))
    for x in aplicadas:
        print("      %s" % x)
    c_fut = colisiones(sim2, veredictos)
    print("   colisiones que quedarian tras esas fusiones: %d" % len(c_fut))
    for par, vs in c_fut:
        print("      par resuelto: %s contra %s" % par)
        for v in sorted(vs, key=lambda x: x["puesto_intra"]):
            print("         puesto %-6d %s | crudo: %s + %s"
                  % (v["puesto_intra"], v["clase"], v["nodo_a"], v["nodo_b"]))
    print("   LAS QUE SE RESUELVEN SOLAS: %d de %d"
          % (len(c_hoy) - len(c_fut), len(c_hoy)))

    print()
    print("--- 6. LA NOMINA DE LA MESA OP-M-03, LEIDA DE SU FICHA ---")
    mesa = [o for o in ops if o["id_op"] == "OP-M-03"]
    if mesa:
        print("   nodos: %s" % (mesa[0].get("nodos") or "SIN NOMINA"))
        for par, vs in c_hoy:
            dentro = [x for x in par if x in set(mesa[0].get("nodos") or [])]
            print("   el par %s contra %s toca la nomina de la mesa en: %s"
                  % (par[0], par[1], dentro or "NINGUNO"))
    else:
        print("   ROJO: OP-M-03 no esta en la ficha.")

    print()
    print("=" * 78)
    if not calza:
        print("ROJO: la cuenta esperada y la medida NO calzan.")
        return 1
    print("LA CUENTA ESPERADA Y LA MEDIDA CALZAN: %d y %d, y son LAS MISMAS."
          % (len(c_sim), len(c_hoy)))
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
