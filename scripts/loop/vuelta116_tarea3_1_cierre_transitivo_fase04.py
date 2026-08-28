# -*- coding: utf-8 -*-
r"""vuelta116_tarea3_1_cierre_transitivo_fase04.py . TAREA 3.1 de la vuelta
116, encargo del auditor (acta de la vuelta 115, seccion "ESTA VUELTA MIDE EL
CIERRE DE LA FASE 04").

QUE MIDE, SOLO LECTURA, CERO ADJUDICACION. Para cada una de las DIEZ
operaciones de la fase 04_ENLACES (docs/plan/OPERACIONES.jsonl, campo
`fase`): sus dependencias DIRECTAS (campo `depende_de`), el CIERRE
TRANSITIVO completo (BFS sobre `depende_de`, sin contarse a si misma), el
TAMANO de ese cierre, y que operaciones de fase `06_MESAS` alcanza. Para las
que alcanzan la fase 06, publica tambien EL CAMINO CONCRETO (un camino real
de ids, hallado por BFS desde la propia operacion hasta la mesa, no solo el
destino).

No decide si esas mesas bloquean o no bloquean: eso es la TAREA 3.2 (registro
de cierre de las nueve dependencias de aguas arriba) y la adjudicacion del
auditor en la 117.

USO:
  python scripts/loop/vuelta116_tarea3_1_cierre_transitivo_fase04.py
"""
import json

RUTA_OPS = "docs/plan/OPERACIONES.jsonl"


def cargar():
    ops = [json.loads(l) for l in open(RUTA_OPS, encoding="utf-8") if l.strip()]
    return {o["id_op"]: o for o in ops}


def cierre_transitivo(by_id, raiz):
    """BFS sobre depende_de. Devuelve (cierre_sin_raiz, padres) donde padres
    mapea cada id alcanzado a quien lo trajo, para reconstruir caminos."""
    visitado = set()
    padres = {}
    cola = [raiz]
    while cola:
        actual = cola.pop(0)
        o = by_id.get(actual)
        if o is None:
            continue
        for dep in o.get("depende_de") or []:
            if dep not in visitado and dep != raiz:
                visitado.add(dep)
                padres[dep] = actual
                cola.append(dep)
    return visitado, padres


def camino_hasta(padres, raiz, destino):
    camino = [destino]
    actual = destino
    while actual in padres:
        actual = padres[actual]
        camino.append(actual)
    camino.append(raiz)
    camino.reverse()
    # quita duplicado si raiz == primer padre registrado
    if len(camino) >= 2 and camino[0] == camino[1]:
        camino = camino[1:]
    return camino


def main():
    by_id = cargar()
    fase04 = sorted([oid for oid, o in by_id.items() if o.get("fase") == "04_ENLACES"])

    print("CIERRE TRANSITIVO DE LAS DIEZ OPERACIONES DE LA FASE 04, TAREA 3.1 VUELTA 116.")
    print("=" * 100)
    print("%d operacion(es) en fase 04_ENLACES (fuente: %s, campo fase)." % (len(fase04), RUTA_OPS))
    print()

    for oid in fase04:
        o = by_id[oid]
        directas = o.get("depende_de") or []
        cierre, padres = cierre_transitivo(by_id, oid)
        mesas = sorted([n for n in cierre if by_id.get(n, {}).get("fase") == "06_MESAS"])
        print("%s" % oid)
        print("  dependencias DIRECTAS (%d): %s" % (len(directas), directas if directas else "NINGUNA"))
        print("  cierre transitivo (%d, sin contarse a si misma): %s" % (len(cierre), sorted(cierre)))
        if mesas:
            for mesa in mesas:
                camino = camino_hasta(padres, oid, mesa)
                print("  ALCANZA fase 06_MESAS: %s -- camino: %s" % (mesa, " -> ".join(camino)))
        else:
            print("  ALCANZA fase 06_MESAS: NINGUNA")
        print()

    total_alcanzan = [oid for oid in fase04
                       if any(by_id.get(n, {}).get("fase") == "06_MESAS" for n in cierre_transitivo(by_id, oid)[0])]
    print("RESUMEN: %d de %d operaciones de la fase 04 alcanzan alguna mesa de la fase 06: %s"
          % (len(total_alcanzan), len(fase04), total_alcanzan))


if __name__ == "__main__":
    main()
