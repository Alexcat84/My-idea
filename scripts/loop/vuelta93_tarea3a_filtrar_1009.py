# -*- coding: utf-8 -*-
"""vuelta93_tarea3a_filtrar_1009.py . VUELTA 93, TAREA 3(a) (analoga a la
TAREA 3(a) de la vuelta 92): EL GUARDA REPARADO
(`scripts/loop/vuelta93_tarea3_guarda_direccion.py`) SACA EL PUESTO 1009 DE
`docs/plan/OP_E_07_DIRECCION_V92.jsonl` (87 filas) Y ESCRIBE
`docs/plan/OP_E_07_DIRECCION_V93.jsonl` (86 filas).

POR QUE ES EL GUARDA Y NO LA MANO, otra vez (EJECUTOR.md, mismo principio que
la vuelta 92): este script NO tiene una lista de puestos a excluir; llama a
`guarda_direccion(razon)` fila por fila, sobre la razon COMPLETA de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, y lo que el guarda diga es lo que sale.
La decision de que el 1009 tenia que salir es de la TAREA 2 (la relectura
conjunta, `scripts/loop/vuelta93_tarea2_relectura_1009.py`); este script solo
confirma que EL GUARDA YA REPARADO coincide con esa decision sobre la bolsa
VIGENTE (las 87 que sobrevivieron a la vuelta 92, no las 88 originales).

ROJO si el guarda saca algo distinto de exactamente {1009}, o si alguna razon
no se puede leer: NO SE ESCRIBE NADA.

USO:
  python scripts/loop/vuelta93_tarea3a_filtrar_1009.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
ENTRADA = os.path.join(PLAN, "OP_E_07_DIRECCION_V92.jsonl")
SALIDA = os.path.join(PLAN, "OP_E_07_DIRECCION_V93.jsonl")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta93_tarea3_guarda_direccion import guarda_direccion  # noqa: E402


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    filas = cargar_jsonl(ENTRADA)
    veredictos = {int(v["puesto_intra"]): v for v in cargar_jsonl(VEREDICTOS)}

    print("=" * 90)
    print("TAREA 3(a) de la vuelta 93: EL GUARDA REPARADO FILTRA LAS %d FILAS DE %s"
          % (len(filas), os.path.basename(ENTRADA)))
    print("=" * 90)

    quedan, salen = [], []
    for f in filas:
        puesto = f["puesto"]
        v = veredictos.get(puesto)
        if v is None:
            print("ROJO: el puesto %s no tiene entrada en %s. NO SE ESCRIBE NADA." % (puesto, VEREDICTOS))
            return 1
        veredicto = guarda_direccion(v["razon"])
        if veredicto == "SALE":
            salen.append((puesto, v["razon"]))
        else:
            quedan.append(f)

    print("total: %d, SALEN por el guarda: %d %s" % (len(filas), len(salen), [p for p, _ in salen]))
    if [p for p, _ in salen] != [1009]:
        print("ROJO: el guarda tenia que sacar EXACTAMENTE {1009} y saco otra cosa. NO SE ESCRIBE NADA.")
        return 1

    puesto, razon = salen[0]
    print()
    print("EL 1009 SALE, con la frase literal de su razon:")
    print("  %r" % razon)
    print()
    print("QUEDAN: %d filas con direccion" % len(quedan))

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        for f in quedan:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")
    print("ESCRITO: %s (%d filas)" % (SALIDA, len(quedan)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
