"""Vuelta 30, fase 01: LA FUSION INTERNA (`P.19`) Y EL CORTE UNICO (`P.20`).

`scripts/loop/vuelta27_cortar.py` sabe SACAR un bloque de un nodo y llevarlo a su
destino. Lo que no sabe hacer, y `P.19` manda, es FUNDIR dentro del nodo: el
material que repite el mismo objeto no tiene destino que buscar, se refunde en un
solo procedimiento y el nodo queda MULTIFUENTE LEGITIMO. Y `P.20` manda que un
nodo de dos operaciones se corte UNA sola vez, asi que la fusion y la salida del
material ajeno tienen que ocurrir en el MISMO acto.

Este script no decide nada: aplica un plan declarativo que el ejecutor escribe por
lectura. Las guardas son las mismas de la vuelta 27, mas las que la fusion pide:

  * SIMULACION SOBRE COPIA EN MEMORIA por defecto: no escribe nada.
  * GUARDA DE CONTEO: el nodo tiene hoy los pasos que el plan espera.
  * GUARDA DE TEXTO SOBRE TODOS LOS PASOS, no solo sobre los que salen: una
    fusion reescribe el procedimiento entero, asi que el plan declara el prefijo
    de LOS PASOS ORIGINALES uno por uno y este script los coteja.
  * GUARDA DE FUENTE en el nodo y en cada destino.
  * CERO PERDIDA, y es la guarda central: la union de los origenes del mapa de
    destejido y de los pasos que salen tiene que cubrir EXACTAMENTE 1..N, sin
    huecos y sin repetidos. Un paso o se funde o se va, nunca las dos cosas y
    nunca ninguna.
  * GUARDA DE PROCEDENCIA: `P.19` punto 2 exige la procedencia declarada por
    bloque, asi que el plan la trae y este script exige que cubra todos los pasos
    del resultado.
  * EL FINAL DE FICHERO SE PRESERVA TAL CUAL.

Uso:
    python scripts/loop/vuelta30_fundir.py <plan.json> --simular
    python scripts/loop/vuelta30_fundir.py <plan.json> --ejecutar
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def leer_crudo(nid):
    with open(ruta(nid), encoding="utf-8", newline="") as fh:
        crudo = fh.read()
    return json.loads(crudo), ("\n" if crudo.endswith("\n") else "")


def escribir(nid, datos, cola):
    with open(ruta(nid), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    plan_path = sys.argv[1]
    modo = sys.argv[2] if len(sys.argv) > 2 else "--simular"
    if modo not in ("--simular", "--ejecutar"):
        print(__doc__)
        return 2

    plan = json.load(open(plan_path, encoding="utf-8"))
    print("PLAN     : %s" % plan_path)
    print("OPERACION: %s" % plan["operacion"])
    print("REGLA    : %s" % plan.get("regla", "?"))
    print("MODO     : %s" % modo)
    print("NODOS    : %d" % len(plan["nodos"]))
    print("=" * 78)

    fallos = []
    memoria = {}

    def cargar(nid):
        if nid not in memoria:
            memoria[nid] = leer_crudo(nid)
        return memoria[nid]

    for f in plan["nodos"]:
        nid = f["nodo"]
        print("\n" + "-" * 78)
        print("NODO: %s" % nid)
        if not os.path.exists(ruta(nid)):
            fallos.append("%s: no existe en el dataset" % nid)
            print("  [ROJO] no existe")
            continue
        d, cola = cargar(nid)
        pasos = list(d.get("pasos_accionables") or [])

        # GUARDA DE CONTEO
        if len(pasos) != f["pasos_totales"]:
            fallos.append("%s: tiene %d pasos y el plan esperaba %d"
                          % (nid, len(pasos), f["pasos_totales"]))
            print("  [ROJO] pasos %d, esperados %d" % (len(pasos), f["pasos_totales"]))
            continue

        # GUARDA DE FUENTE
        if d.get("fuente") != f["fuente_esperada"]:
            fallos.append("%s: fuente inesperada" % nid)
            print("  [ROJO] fuente de hoy : %r" % d.get("fuente"))
            print("         fuente esperada: %r" % f["fuente_esperada"])
            continue

        # GUARDA DE TEXTO SOBRE TODOS LOS PASOS
        prefijos = f["prefijos"]
        if len(prefijos) != len(pasos):
            fallos.append("%s: el plan trae %d prefijos para %d pasos"
                          % (nid, len(prefijos), len(pasos)))
            print("  [ROJO] prefijos %d, pasos %d" % (len(prefijos), len(pasos)))
            continue
        malos = [(i + 1, pasos[i][:60]) for i, p in enumerate(prefijos)
                 if not pasos[i].startswith(p)]
        if malos:
            fallos.append("%s: %d paso(s) no calzan con el prefijo del plan" % (nid, len(malos)))
            print("  [ROJO] pasos que no calzan: %s" % malos)
            continue
        print("  guarda de texto: %d de %d pasos calzan con su prefijo" % (len(pasos), len(pasos)))

        # CERO PERDIDA
        mapa = {int(k): list(v) for k, v in f["mapa_destejido"].items()}
        salidas = f.get("salidas") or []
        origenes_fundidos = []
        for v in mapa.values():
            origenes_fundidos.extend(v)
        origenes_salida = []
        for s in salidas:
            origenes_salida.extend(s["pasos_que_salen"])
        todos = origenes_fundidos + origenes_salida
        esperados = set(range(1, len(pasos) + 1))
        repetidos = sorted({i for i in todos if todos.count(i) > 1})
        faltan = sorted(esperados - set(todos))
        sobran = sorted(set(todos) - esperados)
        print("  cero perdida: %d origenes fundidos, %d que salen, %d en total"
              % (len(origenes_fundidos), len(origenes_salida), len(todos)))
        if repetidos or faltan or sobran:
            fallos.append("%s: cobertura rota (repetidos %s, faltan %s, sobran %s)"
                          % (nid, repetidos, faltan, sobran))
            print("  [ROJO] repetidos %s, faltan %s, sobran %s" % (repetidos, faltan, sobran))
            continue

        # EL RESULTADO
        finales = f["pasos_finales"]
        if sorted(mapa) != list(range(1, len(finales) + 1)):
            fallos.append("%s: el mapa cubre %s y el resultado tiene %d pasos"
                          % (nid, sorted(mapa), len(finales)))
            print("  [ROJO] el mapa no indexa 1..%d" % len(finales))
            continue

        # GUARDA DE PROCEDENCIA (P.19 punto 2)
        proc = f.get("procedencia") or []
        cubiertos = set()
        for p in proc:
            cubiertos |= set(p["pasos_del_resultado"])
        if cubiertos != set(range(1, len(finales) + 1)):
            fallos.append("%s: la procedencia no cubre los %d pasos del resultado (cubre %d)"
                          % (nid, len(finales), len(cubiertos)))
            print("  [ROJO] procedencia incompleta: %s" % sorted(cubiertos))
            continue

        print("  pasos %d -> %d, y la procedencia declara %d bloque(s)"
              % (len(pasos), len(finales), len(proc)))
        print("  fuente: %r" % d.get("fuente"))
        print("          -> %r%s" % (f["fuente_queda"],
                                     "  (SIN CAMBIO: multifuente legitimo)"
                                     if f["fuente_queda"] == d.get("fuente") else ""))
        print("\n  EL MAPA DEL DESTEJIDO, destino <- origenes:")
        for k in sorted(mapa):
            print("    %2d <- %-18s %s" % (k, mapa[k], finales[k - 1][:88]))
        for p in proc:
            print("    procedencia: pasos %s del resultado <- %s"
                  % (p["pasos_del_resultado"], p["libro"]))

        # LAS SALIDAS (P.18, el material ajeno al objeto)
        for s in salidas:
            dest = s["destino"]
            mid = dest["nodo"]
            print("\n  SALE por P.18: pasos %s -> %s" % (s["pasos_que_salen"], mid))
            if dest["tipo"] != "miembro":
                fallos.append("%s: tipo de destino no soportado %r" % (nid, dest["tipo"]))
                print("  [ROJO] tipo de destino %r" % dest["tipo"])
                continue
            if not os.path.exists(ruta(mid)):
                fallos.append("%s: el miembro destino %s no existe" % (nid, mid))
                print("  [ROJO] no existe %s" % mid)
                continue
            m, mcola = cargar(mid)
            if dest.get("fuente_esperada_destino") is not None \
                    and m.get("fuente") != dest["fuente_esperada_destino"]:
                fallos.append("%s: fuente inesperada en el destino %s" % (nid, mid))
                print("  [ROJO] fuente destino: %r" % m.get("fuente"))
                continue
            viajan = [pasos[i - 1] for i in s["pasos_que_salen"]]
            if s.get("pasos_que_viajan") is not None and s["pasos_que_viajan"] != viajan:
                fallos.append("%s: el texto que viaja no es el del grafo" % nid)
                print("  [ROJO] el texto que viaja no calza con el grafo")
                continue
            antes = len(m.get("pasos_accionables") or [])
            m["pasos_accionables"] = list(m.get("pasos_accionables") or []) + viajan
            print("    %s: pasos %d -> %d" % (mid, antes, len(m["pasos_accionables"])))
            for i, p in zip(s["pasos_que_salen"], viajan):
                print("      viaja %2d. %s" % (i, p[:92]))
            memoria[mid] = (m, mcola)

        d["pasos_accionables"] = finales
        d["fuente"] = f["fuente_queda"]
        memoria[nid] = (d, cola)

    print("\n" + "=" * 78)
    print("RESUMEN")
    print("  ficheros que se tocarian: %d" % len(memoria))
    if fallos:
        print("\nPARADA: %d guarda(s) en rojo. NO se escribe nada." % len(fallos))
        for x in fallos:
            print("  - %s" % x)
        return 1

    if modo == "--simular":
        print("\nSIMULACION: cero escrituras.")
        return 0

    for nid, (datos, cola) in memoria.items():
        escribir(nid, datos, cola)
    print("\nESCRITO: %d fichero(s) en dataset/nodos/." % len(memoria))
    for nid in sorted(memoria):
        print("  - %s" % nid)
    return 0


if __name__ == "__main__":
    sys.exit(main())
