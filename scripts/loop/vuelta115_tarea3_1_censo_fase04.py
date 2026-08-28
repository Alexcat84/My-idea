# -*- coding: utf-8 -*-
r"""vuelta115_tarea3_1_censo_fase04.py . TAREA 3.1 de la vuelta 115: censo de
la fase 04_ENLACES con un tallador, no tecleado. Lee
docs/plan/OPERACIONES.jsonl entero, filtra las filas de `fase` ==
"04_ENLACES", y para cada una publica `id_op`, `tipo`, `estado`, `orden` y,
para cada entrada de su `depende_de`, la FASE y el ESTADO de esa dependencia
(leidos de la misma tabla, por `id_op`, no supuestos).

SOLO MIDE: no adjudica, no cambia `estado`, no escribe ni retira aristas.

USO:
  python scripts/loop/vuelta115_tarea3_1_censo_fase04.py
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")


def cargar():
    filas = []
    with open(RUTA, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))
    return filas


def main():
    filas = cargar()
    por_id = {f["id_op"]: f for f in filas}
    fase04 = [f for f in filas if f.get("fase") == "04_ENLACES"]
    fase04.sort(key=lambda f: f.get("orden", 0))

    print("CENSO DE LA FASE 04_ENLACES, TALLADO de docs/plan/OPERACIONES.jsonl (%d filas totales)." % len(filas))
    print("=" * 100)
    print("filas de fase 04_ENLACES: %d" % len(fase04))
    print()

    for f in fase04:
        deps = f.get("depende_de") or []
        print("%s | %s | %s | orden %s" % (f["id_op"], f.get("tipo"), f.get("estado"), f.get("orden")))
        if not deps:
            print("   depende_de: (ninguna)")
        else:
            for d in deps:
                otra = por_id.get(d)
                if otra is None:
                    print("   depende_de: %s -- NO ENCONTRADA en OPERACIONES.jsonl" % d)
                else:
                    print("   depende_de: %s (fase %s, estado %s)" % (d, otra.get("fase"), otra.get("estado")))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
