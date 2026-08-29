# -*- coding: utf-8 -*-
r"""verificar_huerfanas_por_fusion.py . LA GUARDA NUEVA DEL PASIVO (TAREA
1.h de la vuelta 128, encargo docs/loop/PROMPT_SIGUIENTE.md).

GENERALIZA Y REEMPLAZA a vuelta126_contar_aristas_huerfanas_totales.py (que
se queda en el repo como registro, no se borra), parametrizando la unidad de
conteo, el punto de comparacion y el punto medido, para partir el pasivo
entre HEREDADO (ya estaba antes de que naciera el bucle) y FABRICADO POR LA
CAMPANA (P.16 punto 1 del banco del plan obliga a reponer lo fabricado).

UNIDAD par-resuelto (por defecto, la adjudicada por el acta 126 seccion 4.1
como unidad canonica del pasivo): por cada nodo DEPRECADO de --ref, se leen
sus dos listas TAL COMO QUEDARON (registro historico), se resuelve cada
entrada con el resolutor de --ref, y si resuelve a un nodo VIVO distinto del
superviviente del propio muerto se comprueba si esa arista existe hoy entre
los dos supervivientes, mirando las dos vistas. Dedup por PAR RESUELTO
(superviviente, destino). Es el metodo de la vuelta 126, sin cambios.

UNIDAD par-crudo: el mismo nucleo, pero deduplicando por el PAR HISTORICO
(los dos ids muertos) y contando SOLO los casos en que el otro extremo
tambien estaba deprecado en --ref. Es la unidad del 39 del acta de la
vuelta 125.

LA PARTICION, QUE ES LA RAZON DE SER DE ESTA GUARDA: se mide el conjunto en
--baseline (mismo metodo, sobre el grafo de --baseline), se PROYECTA cada
extremo por el resolutor de --ref, y se compara contra el conjunto medido
en --ref:
  TOTAL                = conjunto medido en --ref
  HEREDADAS            = TOTAL que ya estaba en la proyeccion de --baseline
  REPARADAS DE REBOTE  = proyeccion de --baseline que ya NO esta en TOTAL
  FABRICADAS POR LA CAMPANA = TOTAL que NO estaba en la proyeccion de --baseline
TOTAL = HEREDADAS + FABRICADAS siempre. REPARADAS DE REBOTE es un tercer
conjunto aparte, no se resta de TOTAL.

Las FABRICADAS se listan una por linea con el id muerto de origen y el
commit corto en que ese id quedo deprecado (git log -S sobre su fichero de
dataset/nodos, best effort).

ROJO EXIT 1 si FABRICADAS no es cero. VERDE EXIT 0 si lo es.

USO:
  python scripts/loop/verificar_huerfanas_por_fusion.py
  python scripts/loop/verificar_huerfanas_por_fusion.py --unidad par-crudo --ref 7150339f --baseline 7150339f
  python scripts/loop/verificar_huerfanas_por_fusion.py --autoprueba

CASO POSITIVO (--autoprueba, en memoria, no toca disco): sobre una copia de
--ref se busca una arista vivo-vivo que un superviviente HEREDO de su
absorbido (sigue presente hoy) y se borra de las dos vistas. El par
resultante tiene que aparecer en el TOTAL medido sobre la copia mutada, y
clasificarse en FABRICADAS o en HEREDADAS (segun si su version proyectada
del --baseline real ya lo traia), nombrado.
"""
import argparse
import json
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
BASELINE_DEFECTO = "50f03099"


def cargar(ref):
    if ref == "WORK":
        with open(RUTA_GRAFO, encoding="utf-8") as f:
            return json.load(f)["nodos"]
    r = subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % ref],
                        cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO (arnes): no se pudo leer dataset/metadata/master_graph.json en %s" % ref)
    return json.loads(r.stdout.decode("utf-8"))["nodos"]


def vivo(nodos, i):
    n = nodos.get(i)
    return n is not None and not n.get("deprecado")


def resolver_de(nodos):
    alias = {}
    for nid, n in nodos.items():
        if n.get("deprecado"):
            continue
        for x in (n.get("ids_alias") or []):
            alias[x] = nid

    def resolver(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x
    return resolver


def presente(nodos, o, d):
    no = nodos.get(o) or {}
    nd = nodos.get(d) or {}
    return d in (no.get("nodos_siguientes") or []) or o in (nd.get("nodos_previos") or [])


def medir(nodos, unidad):
    """Conjunto de huecos segun UNIDAD, mas origen_por_par: par -> lista de
    ids muertos de donde salio (para citar en FABRICADAS)."""
    resolver = resolver_de(nodos)
    conjunto = set()
    origen_por_par = {}
    for muere, n in nodos.items():
        if not n.get("deprecado"):
            continue
        sup = resolver(muere)
        if sup == muere or not vivo(nodos, sup):
            continue
        for campo, dr in (("nodos_siguientes", "sig"), ("nodos_previos", "prev")):
            for x in (n.get(campo) or []):
                otro = resolver(x)
                if otro == sup or not vivo(nodos, otro):
                    continue
                o, d = (sup, otro) if dr == "sig" else (otro, sup)
                if presente(nodos, o, d):
                    continue
                if unidad == "par-resuelto":
                    par = (o, d)
                else:
                    nx = nodos.get(x)
                    if nx is None or not nx.get("deprecado"):
                        continue
                    par = (muere, x) if dr == "sig" else (x, muere)
                conjunto.add(par)
                origen_por_par.setdefault(par, []).append(muere)
    return conjunto, origen_por_par


def proyectar(conjunto_baseline, nodos_ref, unidad):
    resolver = resolver_de(nodos_ref)
    proyectadas = set()
    for a, b in conjunto_baseline:
        a2, b2 = resolver(a), resolver(b)
        if unidad == "par-resuelto":
            if a2 == b2 or not vivo(nodos_ref, a2) or not vivo(nodos_ref, b2):
                continue
        proyectadas.add((a2, b2))
    return proyectadas


def commit_de_deprecacion(node_id):
    ruta = "dataset/nodos/%s.json" % node_id
    r = subprocess.run(["git", "log", "--follow", "-S", "\"deprecado\": true",
                         "--format=%h", "--", ruta], cwd=RAIZ, capture_output=True)
    lineas = r.stdout.decode("utf-8", errors="replace").strip().splitlines()
    return lineas[-1] if lineas else "?"


def imprimir_particion(total, origen_por_par, proyectadas, unidad, baseline_nombre, ref_nombre):
    heredadas = total & proyectadas
    reparadas = proyectadas - total
    fabricadas = total - proyectadas
    print("UNIDAD: %s | BASELINE: %s | REF: %s" % (unidad, baseline_nombre, ref_nombre))
    print("TOTAL: %d" % len(total))
    print("HEREDADAS: %d" % len(heredadas))
    for p in sorted(heredadas):
        print("  %s -> %s" % p)
    print("REPARADAS DE REBOTE: %d" % len(reparadas))
    for p in sorted(reparadas):
        print("  %s -> %s" % p)
    print("FABRICADAS POR LA CAMPANA: %d" % len(fabricadas))
    for p in sorted(fabricadas):
        muertos = sorted(set(origen_por_par.get(p, [])))
        if not muertos:
            print("  %s -> %s | id muerto: ? | commit: ?" % p)
        for m in muertos:
            print("  %s -> %s | id muerto: %s | commit: %s" % (p[0], p[1], m, commit_de_deprecacion(m)))
    return heredadas, reparadas, fabricadas


def autoprueba(unidad, ref_nombre, baseline_nombre):
    nodos_ref = cargar(ref_nombre)
    resolver = resolver_de(nodos_ref)
    candidato = None
    for muere, n in nodos_ref.items():
        if not n.get("deprecado"):
            continue
        sup = resolver(muere)
        if sup == muere or not vivo(nodos_ref, sup):
            continue
        for campo, dr in (("nodos_siguientes", "sig"), ("nodos_previos", "prev")):
            for x in (n.get(campo) or []):
                otro = resolver(x)
                if otro == sup or not vivo(nodos_ref, otro):
                    continue
                o, d = (sup, otro) if dr == "sig" else (otro, sup)
                if not presente(nodos_ref, o, d):
                    continue
                nx = nodos_ref.get(x)
                if unidad == "par-crudo" and not (nx is not None and nx.get("deprecado")):
                    continue
                candidato = (muere, x, dr, o, d)
                break
            if candidato:
                break
        if candidato:
            break

    if candidato is None:
        print("CAIDA DE LA ARNES: no se hallo una arista heredada de fusion para mutar bajo unidad=%s." % unidad)
        return 1

    muere, x, dr, o, d = candidato
    esperado = (o, d) if unidad == "par-resuelto" else ((muere, x) if dr == "sig" else (x, muere))

    clon = {nid: dict(nn) for nid, nn in nodos_ref.items()}
    clon[o]["nodos_siguientes"] = [i for i in (clon[o].get("nodos_siguientes") or []) if i != d]
    clon[d]["nodos_previos"] = [i for i in (clon[d].get("nodos_previos") or []) if i != o]

    total_mut, origen_mut = medir(clon, unidad)
    if esperado not in total_mut:
        print("CAIDA DE LA AUTOPRUEBA: borrar %s -> %s de las dos vistas no produjo el par esperado %r en TOTAL."
              % (o, d, esperado))
        return 1

    nodos_baseline = cargar(baseline_nombre)
    base_conjunto, _ = medir(nodos_baseline, unidad)
    proyectadas = proyectar(base_conjunto, clon, unidad)
    heredadas = total_mut & proyectadas
    fabricadas = total_mut - proyectadas

    if esperado in fabricadas:
        clase = "FABRICADAS"
    elif esperado in heredadas:
        clase = "HEREDADAS"
    else:
        print("CAIDA DE LA AUTOPRUEBA: %r aparecio en TOTAL pero no se clasifico en ninguna de las dos." % (esperado,))
        return 1

    print("AUTOPRUEBA VERIFICADA (unidad=%s): borrar %s -> %s de las dos vistas (heredada de %s, ref %s mutado en "
          "memoria) produce el par %r y se clasifica en %s." % (unidad, o, d, muere, ref_nombre, esperado, clase))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--unidad", choices=["par-resuelto", "par-crudo"], default="par-resuelto")
    ap.add_argument("--baseline", default=BASELINE_DEFECTO)
    ap.add_argument("--ref", default="WORK")
    ap.add_argument("--autoprueba", action="store_true",
                     help="corre el caso positivo por mutacion (en memoria) y termina")
    a = ap.parse_args()

    if a.autoprueba:
        return autoprueba(a.unidad, a.ref, a.baseline)

    nodos_ref = cargar(a.ref)
    nodos_baseline = cargar(a.baseline)
    total, origen_por_par = medir(nodos_ref, a.unidad)
    base_conjunto, _ = medir(nodos_baseline, a.unidad)
    proyectadas = proyectar(base_conjunto, nodos_ref, a.unidad)

    _, _, fabricadas = imprimir_particion(total, origen_por_par, proyectadas, a.unidad, a.baseline, a.ref)

    if fabricadas:
        print("ROJO EXIT 1: %d arista(s) huerfana(s) por fusion fabricada(s) por la campana." % len(fabricadas))
        return 1
    print("VERDE EXIT 0: cero aristas huerfanas por fusion fabricadas por la campana.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
