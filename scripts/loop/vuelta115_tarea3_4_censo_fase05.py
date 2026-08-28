# -*- coding: utf-8 -*-
r"""vuelta115_tarea3_4_censo_fase05.py . TAREA 3.4 de la vuelta 115: censo de
la fase 05_SANEO, SOLO MEDIR. Publica, para cada una de sus operaciones,
`id_op`, `tipo`, `estado`, `orden`, `depende_de` (con la FASE y el ESTADO tal
como estan escritos hoy en la tabla, sin resolver nada) y `bloquea_a`.

NO ADJUDICA NADA: publica el campo `estado` TAL COMO ESTA y declara, en la
propia salida, que ese campo NO es la vara de "que depende de algo cerrado"
(doctrina vigente, acta de la vuelta 100 seccion 4.2: `estado` no se toca
aunque una fase quede CERRADA CON REMISION, como la 03).

USO:
  python scripts/loop/vuelta115_tarea3_4_censo_fase05.py
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
    fase05 = [f for f in filas if f.get("fase") == "05_SANEO"]
    fase05.sort(key=lambda f: f.get("orden", 0))

    print("CENSO DE LA FASE 05_SANEO, TALLADO de docs/plan/OPERACIONES.jsonl (%d filas totales)." % len(filas))
    print("SOLO MEDIR: no se adjudica orden, no se abre la fase, no se toca ningun campo.")
    print("=" * 100)
    print("filas de fase 05_SANEO: %d" % len(fase05))
    print()

    for f in fase05:
        deps = f.get("depende_de") or []
        bloq = f.get("bloquea_a") or []
        print("%s | %s | estado %s | orden %s" % (f["id_op"], f.get("tipo"), f.get("estado"), f.get("orden")))
        if not deps:
            print("   depende_de: (ninguna)")
        else:
            for d in deps:
                otra = por_id.get(d)
                if otra is None:
                    print("   depende_de: %s -- NO ENCONTRADA en OPERACIONES.jsonl" % d)
                else:
                    print("   depende_de: %s (fase %s, campo estado %s)" % (d, otra.get("fase"), otra.get("estado")))
        if not bloq:
            print("   bloquea_a: (ninguna)")
        else:
            print("   bloquea_a: %s" % ", ".join(bloq))
    print()
    print("LIMITE DECLARADO EN LA PROPIA SALIDA: el campo `estado` de arriba se publica TAL COMO")
    print("ESTA ESCRITO, sin resolver 'que depende de algo cerrado'. Doctrina vigente (acta de la")
    print("vuelta 100, seccion 4.2): `estado` NO SE TOCA y sigue en LISTA para las operaciones de")
    print("fases ya cerradas (p.ej. la fase 03, CERRADA CON REMISION desde la vuelta 74), asi que")
    print("leer solo este campo NO responde correctamente esa pregunta. Esta salida NO la resuelve:")
    print("la resolucion es adjudicacion del auditor, no de este censo.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
