"""Vuelta 31: mide las costuras que los cortes de OP-F-04-COL crearon en sus
destinos.

Mismo oficio que scripts/loop/vuelta29_costuras.py y con dos cambios declarados:
la nomina de receptores NO se escribe a mano, se lee del plan sellado (asi no se
puede olvidar ninguno, que es la omision que el acta de la vuelta 28 adjudico), y
LOS NODOS PROPIOS ENTRAN TAMBIEN, porque la primera puerta alcanza a la costura
que nace dentro de un nodo recien creado (registro del 14 ago 2026 en
08_VERIFICACION.md, adjudicado por el acta de la vuelta 29 punto 3: el disparador
es la repeticion, no el domicilio).

Este script NO desteje y NO decide: MIDE. Por cada destino imprime los pasos que
tenia ANTES del corte y los que entraron, para que la costura se declare con su
medicion al lado, o para que se declare que no la hay.

Uso: python scripts/loop/vuelta31_costuras_col.py <plan.json> <commit_antes>
"""
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def hoy(nid):
    with open(os.path.join(NODOS, nid + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


def antes(nid, commit):
    p = subprocess.run(["git", "show", "%s:dataset/nodos/%s.json" % (commit, nid)],
                       cwd=RAIZ, capture_output=True)
    if p.returncode != 0:
        return None
    return json.loads(p.stdout.decode("utf-8"))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    plan = json.load(open(sys.argv[1], encoding="utf-8"))
    commit = sys.argv[2]

    receptores = {}
    for c in plan["cortes"]:
        did = c["destino"].get("nodo") or c["destino"]["nuevo"]["node_id"]
        receptores.setdefault(did, []).append(
            (c["origen"], c["frontera"], c["pasos_que_salen_texto"]))

    print("COMMIT ANTES DEL CORTE: %s" % commit)
    print("MEDIDO HOY CONTRA: dataset/nodos/ del arbol de trabajo")
    print("DESTINOS: %d (los que el plan sellado declara, ninguno a mano)" % len(receptores))
    print("=" * 78)
    for nid in sorted(receptores):
        d_hoy = hoy(nid)
        d_ant = antes(nid, commit)
        p_hoy = d_hoy["pasos_accionables"]
        p_ant = d_ant["pasos_accionables"] if d_ant else []
        entraron = [t for _o, _f, ts in receptores[nid] for t in ts]
        print()
        print("DESTINO   : %s%s" % (nid, "   [NODO NUEVO]" if d_ant is None else ""))
        for o, f, ts in receptores[nid]:
            print("DONANTE   : %s (%s), %d paso(s)" % (o, f, len(ts)))
        print("PASOS     : %d hoy, contra %d antes del corte" % (len(p_hoy), len(p_ant)))
        print("FUENTE HOY: %s" % d_hoy.get("fuente"))
        print("-" * 78)
        print("  LOS QUE YA TENIA (%d):" % len(p_ant))
        for i, p in enumerate(p_ant, 1):
            print("    %2d. %s" % (i, p))
        print("  LOS QUE ENTRARON (%d):" % len(entraron))
        for i, p in enumerate(entraron, len(p_ant) + 1):
            print("    %2d. %s" % (i, p))
        print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
