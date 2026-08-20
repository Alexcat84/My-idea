# -*- coding: utf-8 -*-
"""vuelta50_tramo_por_miembros.py . RE-IDENTIFICA EL TRAMO 1 DE `OP-U-01` SOBRE LA
NOMINA DE HOY, POR SUS MIEMBROS Y NO POR SU NUMERO.

POR QUE EXISTE, y lo manda el encargo de la vuelta 50 (TAREA 2.2) con estas
palabras: "IDENTIFICALOS EN TU NOMINA RE-MEDIDA POR SUS MIEMBROS, no por el
numero, que baila con cada fusion". El tramo 1 se definio en la vuelta 48 como
los CINCUENTA primeros actos `CERRADOS` de la nomina re-medida AL ABRIRLO, en el
orden impreso por `scripts/plan/recomputo_3388.py`. Cada fusion ejecutada desde
entonces borra un acto de la nomina y corre todos los numeros de detras. Un
instrumento que hable de "el acto 29" sin decir de que corrida es un instrumento
que miente en cuanto alguien funde algo.

LA VARA DE IDENTIDAD, escrita para poder discutirla: dos actos son EL MISMO acto
si sus miembros RESUELTOS por el resolutor de la casa (`P.1`) coinciden como
conjunto. Resolver es lo que hace que un acto sobreviva a su propia fusion: los
absorbidos quedan deprecados con alias y resuelven al superviviente, asi que el
conjunto resuelto de un acto ya fundido colapsa a UN solo id vivo.

DE AHI SALEN LOS TRES DESTINOS de cada uno de los 50, y son los tres que el
registro del tramo necesita:
  - CONSUMIDO: su conjunto resuelto tiene UN solo miembro vivo. El acto se
    fundio (en la vuelta 48 o en la 49) y ya no esta en la nomina.
  - VIVO: su conjunto resuelto sigue teniendo dos o mas miembros vivos y
    aparece en la nomina de hoy. Se imprime CON SU NUMERO DE HOY.
  - PARTIDO: su conjunto resuelto sigue teniendo dos o mas vivos pero NO aparece
    entero en ninguna componente de hoy. Es lo que pasa cuando un volteo de
    clase quita una arista `A` (le paso al 844 en la vuelta 49). No se adivina:
    se imprime como PARTIDO y se dicen las componentes de hoy que lo recogen.

Y PARA CADA ACTO VIVO, LA FIGURA QUE DECIDE EL TRABAJO (`P.12`): si todos sus
pares internos son `A` es FUSION PURA; si hay pares `A` y pares NO-`A` es MIXTO y
pide la lectura `P.12`; y se imprime ademas si tiene LA FORMA que fabrica
colision (algun miembro cargando a la vez un par `A` y un par NO-`A`), porque de
eso depende cuantas colisiones esperar.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo ni un veredicto: imprime.

Uso:
  python scripts/loop/vuelta50_tramo_por_miembros.py \
      --tramo docs/loop/RECOMPUTO_V48_COMPONENTES.jsonl \
      --hoy   docs/loop/RECOMPUTO_V50_APERTURA.jsonl \
      --desde 1 --hasta 50
"""
import argparse
import io
import itertools
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

# 03_FUSIONES.md declara desde el 11 ago 2026 que estos cuatro no se resuelven
# nunca en OP-U-01. La guarda se re-comprueba en cada corrida, como en el
# instrumento de dossier de la vuelta 48.
AJENOS = ["gates_go_kill_decision_points", "customer_discovery",
          "ab_testing_optimizacion", "brainstorming_divergente"]


def cargar_jsonl(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def cargar_nodos():
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
        todos[d["node_id"]] = d
    alias = {}
    for nid, d in todos.items():
        if d.get("deprecado") or d.get("deprecated"):
            continue
        for x in (d.get("ids_alias") or []):
            alias[x] = nid
    return todos, alias


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", required=True,
                    help="la nomina con la que se DEFINIO el tramo (vuelta 48)")
    ap.add_argument("--hoy", required=True, help="la nomina re-medida HOY")
    ap.add_argument("--desde", type=int, default=1)
    ap.add_argument("--hasta", type=int, default=50)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    todos, alias = cargar_nodos()

    def res(x):
        s = set()
        while x in alias and x not in s:
            s.add(x)
            x = alias[x]
        return x

    def vivo(x):
        d = todos.get(x)
        return bool(d) and not (d.get("deprecado") or d.get("deprecated"))

    tramo = [c for c in cargar_jsonl(a.tramo) if c["estado"] == "CERRADO"]
    tramo = tramo[a.desde - 1:a.hasta]
    hoy = cargar_jsonl(a.hoy)
    # El numero de HOY es la posicion en la nomina impresa de hoy, contando
    # SOLO los CERRADOS, que es la misma vara con la que el tramo se numero.
    hoy_cerrados = [c for c in hoy if c["estado"] == "CERRADO"]
    porclave = {}
    for i, c in enumerate(hoy_cerrados, 1):
        porclave[frozenset(res(m) for m in c["miembros"])] = (i, c)
    # Indice de que componente de hoy recoge a cada id vivo.
    dondevive = {}
    for i, c in enumerate(hoy_cerrados, 1):
        for m in c["miembros"]:
            dondevive[res(m)] = i

    veredictos = cargar_jsonl(VER)
    porpar = {}
    for v in veredictos:
        k = frozenset((res(v["nodo_a"]), res(v["nodo_b"])))
        porpar.setdefault(k, []).append(v)

    print("=" * 78)
    print("EL TRAMO 1 DE OP-U-01, RE-IDENTIFICADO POR MIEMBROS SOBRE LA NOMINA DE HOY")
    print("definicion del tramo: %s (actos CERRADOS %d a %d)"
          % (a.tramo, a.desde, a.hasta))
    print("nomina de hoy       : %s (%d CERRADOS)" % (a.hoy, len(hoy_cerrados)))
    print("=" * 78)
    print()

    consumidos, vivos_l, partidos = [], [], []
    for n, c in enumerate(tramo, a.desde):
        resueltos = set(res(m) for m in c["miembros"])
        vivos_del_acto = sorted(x for x in resueltos if vivo(x))
        clave = frozenset(resueltos)
        if len(vivos_del_acto) <= 1:
            consumidos.append((n, c, vivos_del_acto))
            continue
        if clave in porclave:
            vivos_l.append((n, c, porclave[clave]))
        else:
            partidos.append((n, c, vivos_del_acto))

    print("--- RESUMEN DE LOS %d ACTOS DEL TRAMO ---" % len(tramo))
    print("  CONSUMIDOS (ya fundidos, un solo vivo): %d" % len(consumidos))
    print("  VIVOS en la nomina de hoy             : %d" % len(vivos_l))
    print("  PARTIDOS (no calzan enteros hoy)      : %d" % len(partidos))
    print()

    print("--- LOS CONSUMIDOS, con el vivo al que colapsaron ---")
    for n, c, v in consumidos:
        print("  tramo %2d  ->  %s" % (n, v[0] if v else "(ninguno vivo, ROJO)"))
    print()

    if partidos:
        print("--- LOS PARTIDOS, con las componentes de hoy que los recogen ---")
        for n, c, v in partidos:
            print("  tramo %2d  vivos %s" % (n, ", ".join(v)))
            for x in v:
                print("       %-52s hoy en la componente %s"
                      % (x, dondevive.get(x, "NINGUNA (fuera del retrato)")))
        print()

    print("--- LOS VIVOS, con su figura y su trabajo pendiente ---")
    mixtos, puros = [], []
    for n, c, (hoyn, hc) in vivos_l:
        miembros = sorted(set(res(m) for m in hc["miembros"]))
        # Las clases de los pares internos, por par RESUELTO.
        clases, pares = {}, []
        for x, y in itertools.combinations(miembros, 2):
            vs = porpar.get(frozenset((x, y))) or []
            cl = sorted(set(v["clase"] for v in vs))
            pares.append((x, y, cl, [v["puesto_intra"] for v in vs]))
            for k in cl:
                clases[k] = clases.get(k, 0) + 1
        hay_a = any("A" in p[2] for p in pares)
        hay_no_a = any([k for k in p[2] if k != "A"] for p in pares)
        figura = "MIXTO" if (hay_a and hay_no_a) else ("FUSION PURA" if hay_a else "SIN A")
        # LA FORMA: un miembro que carga a la vez un par A y un par NO-A.
        conforma = []
        for m in miembros:
            suyas = set()
            for x, y, cl, _ in pares:
                if m in (x, y):
                    suyas.update(cl)
            if "A" in suyas and (suyas - {"A"}):
                conforma.append(m)
        ajeno = [m for m in miembros if m in AJENOS]
        print()
        print("  tramo %2d  ==  HOY el acto %d   tam %d   %s%s"
              % (n, hoyn, len(miembros), figura,
                 "   [AJENO DECLARADO: %s]" % ", ".join(ajeno) if ajeno else ""))
        print("       miembros: %s" % ", ".join(miembros))
        for x, y, cl, ps in pares:
            print("         %-46s %-46s %-8s puestos %s"
                  % (x, y, ",".join(cl) or "SIN VEREDICTO", ps))
        if figura == "MIXTO":
            print("       LA FORMA que fabrica colision: %s"
                  % (", ".join(conforma) if conforma else "NO la tiene"))
            mixtos.append((n, hoyn, miembros, bool(conforma)))
        elif figura == "FUSION PURA":
            puros.append((n, hoyn, miembros))

    print()
    print("=" * 78)
    print("EL TRABAJO QUE QUEDA EN EL TRAMO 1, medido hoy")
    print("=" * 78)
    print("  actos MIXTOS vivos (piden lectura P.12): %d" % len(mixtos))
    for n, hoyn, ms, f in mixtos:
        print("     tramo %2d = hoy %3d  %s  %s"
              % (n, hoyn, "CON forma" if f else "SIN forma", ", ".join(ms)))
    print("  actos de FUSION PURA vivos (sin P.12)  : %d" % len(puros))
    for n, hoyn, ms in puros:
        print("     tramo %2d = hoy %3d  %s" % (n, hoyn, ", ".join(ms)))
    print()
    print("  COLISIONES ESPERADAS: una por cada CONTINUA sobre un mixto CON forma,")
    print("  y CERO por cada ENTRA. Los mixtos SIN forma no fabrican ninguna.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
