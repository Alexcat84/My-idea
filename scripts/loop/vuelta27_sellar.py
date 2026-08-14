"""Vuelta 27: SELLA un plan de corte. Rellena en el plan los datos que se leen
del dataset (prefijos de los pasos que salen, conteo total de pasos y fuente de
hoy) para que la guarda de vuelta27_cortar.py no dependa de que yo transcriba
bien un acento.

El plan sigue diciendo LO QUE YO DECIDO (que pasos salen y a donde van); el sello
solo copia lo que el fichero del nodo dice HOY, y lo imprime para leerlo.

Uso:
    python scripts/loop/vuelta27_sellar.py docs/loop/PLAN_V27_OPF02.json
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
LARGO = 34


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    ruta_plan = sys.argv[1]
    plan = json.load(open(ruta_plan, encoding="utf-8"))
    for c in plan["cortes"]:
        p = os.path.join(NODOS, c["origen"] + ".json")
        d = json.load(open(p, encoding="utf-8"))
        pasos = d.get("pasos_accionables") or []
        c["pasos_totales"] = len(pasos)
        c["fuente_esperada"] = d.get("fuente")
        c["prefijos"] = [pasos[i - 1][:LARGO] for i in c["pasos_que_salen"]]
        c["pasos_que_salen_texto"] = [pasos[i - 1] for i in c["pasos_que_salen"]]
    with open(ruta_plan, "w", encoding="utf-8") as fh:
        json.dump(plan, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("SELLADO: %s" % ruta_plan)
    for c in plan["cortes"]:
        print("\n%s  (%d pasos hoy, salen %s)" % (
            c["origen"], c["pasos_totales"], c["pasos_que_salen"]))
        print("  fuente hoy: %s" % c["fuente_esperada"])
        for i, t in zip(c["pasos_que_salen"], c["pasos_que_salen_texto"]):
            print("  %2d. %s" % (i, t))
    return 0


if __name__ == "__main__":
    sys.exit(main())
