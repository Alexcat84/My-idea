# -*- coding: utf-8 -*-
r"""vuelta106_tarea4_actualizar_censo_relecturas.py . VUELTA 106, TAREA 4:
anade un evento de relectura a los 27 puestos de docs/loop/CENSO_RELECTURAS_
OP_E_03.jsonl que pasaron por la pregunta de tres vias esta vuelta (TAREA 4.3
y 4.4), para que el censo del proximo vuelta no los vuelva a contar como
"nunca releido". No es uno de los tres sitios aditivos que TAREA 4.4 manda
recomputar (04_ENLACES.md, OPERACIONES.jsonl, tramos jsonl): es
mantenimiento del propio censo de cobertura.

USO:
  python scripts/loop/vuelta106_tarea4_actualizar_censo_relecturas.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "loop", "CENSO_RELECTURAS_OP_E_03.jsonl")

VEREDICTOS = {
    101: "OBJETO", 102: "OBJETO", 106: "OBJETO", 107: "OBJETO", 108: "OBJETO",
    109: "OBJETO", 110: "OBJETO", 111: "OBJETO", 114: "OBJETO", 116: "OBJETO",
    123: "SATELITE, lectura entera: SOSTIENE", 127: "OBJETO", 128: "OBJETO",
    129: "OBJETO", 130: "OBJETO", 132: "OBJETO", 134: "OBJETO",
    145: "SATELITE, lectura entera: MUEVE (correccion_v106)",
    153: "OBJETO", 154: "SATELITE, lectura entera: SOSTIENE",
    156: "OBJETO", 158: "OBJETO", 169: "OBJETO", 177: "OBJETO", 179: "OBJETO",
    180: "OBJETO", 182: "OBJETO",
}

EVENTO_BASE = {
    "vuelta": 106,
    "instrumento": "docs/loop/SALIDA_V106_TAREA4_3_TRES_VIAS.txt (pregunta de tres vias: "
                   "OBJETO del imperativo / SATELITE en complemento preposicional / NO_OBJETO); "
                   "docs/loop/SALIDA_V106_TAREA4_4_LECTURA_ENTERA.md para los SATELITE",
}


def main():
    with io.open(RUTA, encoding="utf-8") as f:
        lineas = [json.loads(l) for l in f if l.strip()]

    tocados = 0
    for fila in lineas:
        p = fila["puesto_tramo"]
        if p not in VEREDICTOS:
            continue
        fila["veces_releido"] = fila.get("veces_releido", 0) + 1
        fila["nunca_releido_desde_la_lectura_original"] = False
        evento = dict(EVENTO_BASE)
        evento["resultado"] = "confirmada, veredicto %s" % VEREDICTOS[p]
        fila.setdefault("eventos", []).append(evento)
        tocados += 1

    if tocados != len(VEREDICTOS):
        raise SystemExit("ROJO: se tocaron %d filas, se esperaban %d" % (tocados, len(VEREDICTOS)))

    with io.open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        for fila in lineas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")
    print("OK: %d puestos actualizados en %s" % (tocados, os.path.relpath(RUTA, RAIZ)))


if __name__ == "__main__":
    main()
