# -*- coding: utf-8 -*-
r"""vuelta112_tarea3_3_volcado_ciego.py . TAREA 3.3 de la vuelta 112.

Vuelca, para cada uno de los 80 puestos del lote (los 88 sin reabrir del
3.1, menos los 8 que quedan para la vuelta 113), el paso_casado exacto de
la madre (texto del pasos_accionables[paso_casado-1]) y el nodo hijo
ENTERO, SIN direccion_leida, SIN razon vieja y SIN vara: para leer a ciegas
contra el grafo, igual que hace la relectura ciega del auditor.

USO: python scripts/loop/vuelta112_tarea3_3_volcado_ciego.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LOTE_80 = [11, 12, 15, 22, 23, 26, 32, 34, 35, 36, 37, 41, 43, 44, 50, 51, 54, 55, 56, 60,
           63, 65, 67, 68, 69, 70, 71, 72, 76, 79, 81, 82, 85, 86, 89, 90, 95, 96, 103, 104,
           105, 112, 113, 115, 117, 118, 119, 120, 121, 122, 124, 125, 126, 131, 133, 135,
           136, 137, 138, 139, 140, 141, 142, 143, 144, 146, 149, 150, 151, 152, 155, 157,
           159, 160, 162, 163, 164, 165, 166, 167]

TRAMOS = [
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl"),
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl"),
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO3_V98.jsonl"),
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO4_V99.jsonl"),
]


def cargar_filas():
    filas = {}
    for ruta in TRAMOS:
        with io.open(ruta, encoding="utf-8") as f:
            for linea in f:
                if linea.strip():
                    d = json.loads(linea)
                    filas[d["puesto_tramo"]] = d
    return filas


def main():
    g = json.load(io.open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8"))
    nodos = g["nodos"]
    filas = cargar_filas()

    assert len(LOTE_80) == 80, len(LOTE_80)
    out = io.open(sys.argv[1], "w", encoding="utf-8") if len(sys.argv) > 1 else sys.stdout

    for p in LOTE_80:
        f = filas[p]
        madre = nodos.get(f["madre_de_la_bolsa"], {})
        hijo = nodos.get(f["hijo_de_la_bolsa"], {})
        pasos_madre = madre.get("pasos_accionables", [])
        idx = f["paso_casado"] - 1
        paso_texto = pasos_madre[idx] if 0 <= idx < len(pasos_madre) else "(INDICE FUERA DE RANGO)"

        out.write("=" * 100 + "\n")
        out.write("PUESTO %d | dominio %s | clase %s\n" % (p, f["dominio"], f["clase"]))
        out.write("-" * 100 + "\n")
        out.write("MADRE %s -- paso %d casado: %s\n" % (f["madre_de_la_bolsa"], f["paso_casado"], paso_texto))
        out.write("   (todos los pasos de la madre, para contexto: %s)\n" % pasos_madre)
        out.write("   entregable_esperado de la madre: %s\n" % madre.get("entregable_esperado"))
        out.write("-" * 100 + "\n")
        out.write("HIJO %s\n" % f["hijo_de_la_bolsa"])
        out.write("   titulo: %s\n" % hijo.get("titulo_concepto"))
        out.write("   resumen_teorico: %s\n" % hijo.get("resumen_teorico"))
        out.write("   pasos_accionables: %s\n" % hijo.get("pasos_accionables"))
        out.write("   entregable_esperado: %s\n" % hijo.get("entregable_esperado"))
        out.write("\n")

    if out is not sys.stdout:
        out.close()
        print("escrito: %s (%d puestos)" % (sys.argv[1], len(LOTE_80)))


if __name__ == "__main__":
    main()
