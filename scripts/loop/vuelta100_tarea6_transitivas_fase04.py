# -*- coding: utf-8 -*-
r"""vuelta100_tarea6_transitivas_fase04.py . VUELTA 100, TAREA 6: LA PARTE
MECANICA (BFS de dependencias transitivas) de la medicion de la fase 04
CONTRA LA EVIDENCIA (acta 99, 4.8: la pregunta "ejecutable hoy" se hace
contra la evidencia de las paginas, no contra el campo `estado`).

QUE HACE: para cada una de las 10 operaciones de `fase == "04_ENLACES"`,
calcula el conjunto COMPLETO de dependencias transitivas (BFS sobre
`depende_de` de `docs/plan/OPERACIONES.jsonl`) y lo imprime. LA PARTE QUE
ESTE INSTRUMENTO NO HACE, A PROPOSITO: decidir si cada dependencia tiene
"registro de cierre escrito" es lectura de prosa (tablas de cierre de fase,
frases `CERRADA`/`SELLADA`/`CIERRE MEDIDO`, remisiones), no un patron
mecanico fiable; esa parte esta en
`docs/loop/SALIDA_V100_TAREA6_FASE04_CONTRA_EVIDENCIA.md`, con cita de
fichero y linea para cada una de las 26, leida hoy a mano contra las
paginas de fase.

MECANICA DE ROJO: si `fase == "04_ENLACES"` no da exactamente 10 filas, o si
`depende_de` de alguna fila no es una lista.

USO:
  python scripts/loop/vuelta100_tarea6_transitivas_fase04.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")


def cargar():
    with io.open(OPERACIONES, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def transitivas(byid, raiz):
    vistos = set()
    pila = [raiz]
    while pila:
        cur = pila.pop()
        for d in byid.get(cur, {}).get("depende_de", []):
            if d not in vistos:
                vistos.add(d)
                pila.append(d)
    return vistos


def main():
    ops = cargar()
    byid = {o["id_op"]: o for o in ops}
    fase04 = [o for o in ops if o.get("fase") == "04_ENLACES"]

    fallos = []
    if len(fase04) != 10:
        fallos.append("fase 04_ENLACES trae %d operaciones, se esperaban 10" % len(fase04))
    for o in ops:
        if not isinstance(o.get("depende_de"), list):
            fallos.append("%s no trae depende_de como lista" % o.get("id_op"))

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE IMPRIME NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("=" * 100)
    print("DEPENDENCIAS TRANSITIVAS DE LAS 10 OPERACIONES DE LA FASE 04 (BFS sobre depende_de)")
    print("=" * 100)
    todas = set()
    for o in sorted(fase04, key=lambda x: x["id_op"]):
        t = sorted(transitivas(byid, o["id_op"]))
        todas |= set(t)
        print("%s (estado=%s): %d deps -> %s" % (o["id_op"], o.get("estado"), len(t), t))

    print()
    print("TOTAL DE DEPENDENCIAS TRANSITIVAS UNICAS ENTRE LAS 10: %d" % len(todas))
    print(sorted(todas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
