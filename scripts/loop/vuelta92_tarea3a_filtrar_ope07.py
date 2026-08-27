# -*- coding: utf-8 -*-
"""vuelta92_tarea3a_filtrar_ope07.py . VUELTA 92, TAREA 3(a): EL GUARDA DE LA
TAREA 2 (`scripts/loop/vuelta92_tarea2_guarda_direccion.py`) SACA EL PUESTO
1098 DE `docs/plan/OP_E_07_DIRECCION_V91.jsonl` (88 filas) Y ESCRIBE
`docs/plan/OP_E_07_DIRECCION_V92.jsonl` (87 filas).

POR QUE ES EL GUARDA Y NO LA MANO. El encargo de la vuelta 92 lo dice
literal: "el guarda nuevo es el que tiene que senalar el 1098 antes de que tu
lo saques a mano: si lo sacas a mano y el guarda no lo veia, el remedio no
sirve y lo dices". Este script NO tiene una lista de puestos a excluir: llama
a `guarda_direccion(razon)` fila por fila, sobre la razon COMPLETA de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, y lo que el guarda diga es lo que sale.

ROJO si el guarda saca algo distinto de exactamente {1098}, o si alguna razon
no se puede leer: NO SE ESCRIBE NADA.

USO:
  python scripts/loop/vuelta92_tarea3a_filtrar_ope07.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
ENTRADA = os.path.join(PLAN, "OP_E_07_DIRECCION_V91.jsonl")
SALIDA = os.path.join(PLAN, "OP_E_07_DIRECCION_V92.jsonl")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta92_tarea2_guarda_direccion import guarda_direccion  # noqa: E402


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    filas = cargar_jsonl(ENTRADA)
    veredictos = {int(v["puesto_intra"]): v for v in cargar_jsonl(VEREDICTOS)}

    print("=" * 90)
    print("TAREA 3(a): EL GUARDA FILTRA LAS %d FILAS DE %s" % (len(filas), os.path.basename(ENTRADA)))
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
    if [p for p, _ in salen] != [1098]:
        print("ROJO: el guarda tenia que sacar EXACTAMENTE {1098} y saco otra cosa. NO SE ESCRIBE NADA.")
        return 1

    puesto, razon = salen[0]
    print()
    print("EL 1098 SALE, con la frase literal de su razon:")
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
