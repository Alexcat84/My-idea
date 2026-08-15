# -*- coding: utf-8 -*-
"""vuelta33_tabla_mapa.py

IMPRIME la tabla de mapa de movimiento de un plan sellado, en el formato exacto
que docs/plan/02_DESTEJIDOS.md usa y que scripts/loop/verificar_mapas_destejido.py
sabe leer. NO decide nada, NO escribe en ningun documento: imprime.

POR QUE EXISTE, y el motivo es una regla y no una comodidad. EJECUTOR.md regla 1,
cuarto renglon (15 ago 2026): LA TABLA SE IMPRIME, NO SE TECLEA. Las paradas de
credito de las vueltas 31 y 32 fueron las dos por una celda tecleada a mano en una
tabla de prosa que ningun instrumento generaba ni validaba. El verificador de mapas
cierra la mitad de atras (valida lo que ya esta escrito); este cierra la de
adelante (lo escribe desde la fuente, para que no haya nada que teclear).

LA FUENTE ES `nodos[].grupos_pasos`, la misma seccion que el verificador compara
celda a celda contra la tabla. Si el plan y la tabla salen del mismo campo, la
vara 2 del verificador no puede fallar por transcripcion.

USO:
  python scripts/loop/vuelta33_tabla_mapa.py docs/loop/PLAN_V32_OPD01_EMBLEMA.json
  python scripts/loop/vuelta33_tabla_mapa.py PLAN.json --campo grupos_condiciones

SALIDA: la tabla en markdown por stdout, y nada mas. Exit 0 siempre que el plan se
pueda leer; exit 2 si el fichero no existe o el campo esta vacio.
"""
import argparse
import json
import sys
from pathlib import Path

CABECERA = "| paso del resultado | de que origenes sale | el motivo de perdida de linea que lo modifica |"
SEPARADOR = "|---:|---|---|"


def filas_del_plan(ruta, campo):
    d = json.loads(Path(ruta).read_text(encoding="utf-8"))
    filas = []
    for nodo in d.get("nodos", []):
        destino = 0
        for g in nodo.get(campo, []) or []:
            destino += 1
            filas.append(
                {
                    "nodo": nodo.get("nodo"),
                    "paso": destino,
                    "origenes": list(g["origenes"]),
                    "motivo": (g.get("motivo") or "").strip(),
                }
            )
    return filas


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("plan", help="ruta al plan sellado JSON")
    ap.add_argument("--campo", default="grupos_pasos", help="grupos_pasos (por defecto) o grupos_condiciones")
    args = ap.parse_args()

    if not Path(args.plan).exists():
        print("NO EXISTE: %s" % args.plan)
        return 2

    filas = filas_del_plan(args.plan, args.campo)
    if not filas:
        print("CAMPO VACIO O AUSENTE: %s en %s" % (args.campo, args.plan))
        return 2

    print(CABECERA)
    print(SEPARADOR)
    for f in filas:
        origenes = ", ".join(str(x) for x in f["origenes"])
        motivo = f["motivo"] if f["motivo"] else "(sin motivo escrito en el plan)"
        print("| **%d** | %s | %s |" % (f["paso"], origenes, motivo))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
