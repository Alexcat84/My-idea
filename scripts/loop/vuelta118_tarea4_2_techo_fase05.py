# -*- coding: utf-8 -*-
r"""vuelta118_tarea4_2_techo_fase05.py . TAREA 4.2 de la vuelta 118: EL TECHO
DE LA FASE 05, SELLADO EN SU PROPIO COMMIT ANTES DE MEDIR NADA de OP-S-01.

QUE MIDE, SOLO LECTURA. De docs/plan/OPERACIONES.jsonl: cuantas operaciones
tienen `fase == "05_SANEO"`, su `orden` uno por uno (ordenadas), cuantas
traen `pregunta_pendiente` distinto de None, y cuantas traen `depende_de` no
vacio.

USO:
  python scripts/loop/vuelta118_tarea4_2_techo_fase05.py
"""
import json

RUTA_OPS = "docs/plan/OPERACIONES.jsonl"
FASE = "05_SANEO"


def main():
    ops = [json.loads(l) for l in open(RUTA_OPS, encoding="utf-8") if l.strip()]
    de_la_fase = [o for o in ops if o.get("fase") == FASE]
    de_la_fase.sort(key=lambda o: o.get("orden", 0))

    print("TECHO DE LA FASE %s, TAREA 4.2 VUELTA 118." % FASE)
    print("=" * 100)
    print("numero de operaciones: %d" % len(de_la_fase))
    print()
    print("| id_op | orden | pregunta_pendiente | depende_de |")
    print("|---|---:|---|---|")
    for o in de_la_fase:
        pp = o.get("pregunta_pendiente")
        dd = o.get("depende_de") or []
        print("| %s | %s | %s | %s |" % (o["id_op"], o.get("orden"),
              "None" if pp is None else repr(pp), ", ".join(dd) if dd else "NINGUNA"))

    con_pregunta = [o["id_op"] for o in de_la_fase if o.get("pregunta_pendiente") is not None]
    con_dependencia = [o["id_op"] for o in de_la_fase if o.get("depende_de")]
    print()
    print("con pregunta_pendiente distinta de None: %d de %d: %s"
          % (len(con_pregunta), len(de_la_fase), con_pregunta or "NINGUNA"))
    print("con depende_de no vacio: %d de %d: %s"
          % (len(con_dependencia), len(de_la_fase), con_dependencia or "NINGUNA"))
    print()
    ordenes = [o.get("orden") for o in de_la_fase]
    print("ordenes, en el orden en que aparecen tras ordenar: %s" % ordenes)


if __name__ == "__main__":
    main()
