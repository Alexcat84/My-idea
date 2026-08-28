# -*- coding: utf-8 -*-
r"""vuelta107_actualizar_censo_relecturas.py . VUELTA 107: anade un evento de
relectura a los puestos que pasaron por la pregunta de tres vias o por
lectura entera esta vuelta (TAREA 3, TAREA 4 y TAREA 5), para que el censo no
los vuelva a contar como "nunca releido". Mantenimiento del censo, no uno de
los tres sitios aditivos.

USO:
  python scripts/loop/vuelta107_actualizar_censo_relecturas.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "loop", "CENSO_RELECTURAS_OP_E_03.jsonl")

EVENTOS_POR_PUESTO = {
    145: {
        "vuelta": 107,
        "instrumento": "TAREA 3, relectura conjunta con el auditor (docs/plan/04_ENLACES.md, "
                       "correccion_v107)",
        "resultado": "SE REVIERTE correccion_v106: vuelve a DIRECCION AFIRMADA (CEDO ante el caso del auditor)",
    },
    109: {
        "vuelta": 107,
        "instrumento": "TAREA 4.1/4.2, pregunta de tres vias mas lectura entera a ciegas "
                       "(docs/loop/SALIDA_V107_TAREA4_1_2_LECTURA_ENTERA_109.md)",
        "resultado": "reclasificado SATELITE por grafica, lectura entera: SOSTIENE",
    },
}

# TAREA 4.3 (tramo3, contadas ya por TAREA4_3_CONTADO.txt): 18 OBJETO + 109 ya arriba.
TRAMO3_TRES_VIAS = [101, 102, 106, 107, 108, 110, 111, 114, 116, 123, 127, 128, 129, 130, 132, 134, 148]
for p in TRAMO3_TRES_VIAS:
    EVENTOS_POR_PUESTO[p] = {
        "vuelta": 107,
        "instrumento": "TAREA 4.3, pregunta de tres vias con formato de tres campos "
                       "(docs/loop/SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md)",
        "resultado": "confirmada, veredicto OBJETO",
    }

# TAREA 5.3 (tramo1, el lote de diez)
TRAMO1_LOTE = [3, 5, 7, 10, 13, 16, 19, 27, 30, 33]
for p in TRAMO1_LOTE:
    EVENTOS_POR_PUESTO[p] = {
        "vuelta": 107,
        "instrumento": "TAREA 5.3, pregunta de tres vias con formato de tres campos "
                       "(docs/loop/SALIDA_V107_TAREA5_3_TRAMO1_TRES_VIAS.md)",
        "resultado": "confirmada, veredicto OBJETO",
    }


def main():
    with io.open(RUTA, encoding="utf-8") as f:
        lineas = [json.loads(l) for l in f if l.strip()]

    tocados = 0
    for fila in lineas:
        p = fila["puesto_tramo"]
        if p not in EVENTOS_POR_PUESTO:
            continue
        fila["veces_releido"] = fila.get("veces_releido", 0) + 1
        fila["nunca_releido_desde_la_lectura_original"] = False
        fila.setdefault("eventos", []).append(EVENTOS_POR_PUESTO[p])
        tocados += 1

    if tocados != len(EVENTOS_POR_PUESTO):
        raise SystemExit("ROJO: se tocaron %d filas, se esperaban %d" % (tocados, len(EVENTOS_POR_PUESTO)))

    with io.open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        for fila in lineas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    print("tocados=%d" % tocados)


if __name__ == "__main__":
    main()
