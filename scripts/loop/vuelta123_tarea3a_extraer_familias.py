# -*- coding: utf-8 -*-
"""vuelta123_tarea3a_extraer_familias.py . Extrae, para las 28 familias de
OP-S-09 (las 29 de scripts/loop/vuelta77_op_s09_nomina.py MENOS
estructura_de_gates/estructura_gates, ya remitida a OP-M-01-FUSION por el
toque unico de la vuelta 78), el contenido de cada nodo miembro (titulo,
dominio, fase, resumen teorico, entregable esperado) a un fichero de texto
legible, para la lectura dirigida par a par de la TAREA 3.a del encargo de
la vuelta 123.

USO:
  python scripts/loop/vuelta123_tarea3a_extraer_familias.py
"""
import ast
import json
import re

RAIZ = "C:/Users/AlexDesk/Documents/I have an idea"


def familias_28():
    lineas = open(RAIZ + "/docs/loop/SALIDA_V123_TAREA2B_NOMINA_29.txt", encoding="utf-8").read().splitlines()
    familias = []
    for l in lineas:
        m = re.match(r"\s*\[(SUFIJO NUMERICO|PARTICULAS|ORDEN DE PALABRAS|SINONIMO PURO)\]\s*(\[.*\])", l)
        if m:
            miembros = ast.literal_eval(m.group(2))
            familias.append((m.group(1), miembros))
    excluida = ["estructura_de_gates", "estructura_gates"]
    return [f for f in familias if f[1] != excluida]


def main():
    with open(RAIZ + "/dataset/metadata/master_graph.json", encoding="utf-8") as f:
        master = json.load(f)
    nodos = master["nodos"]

    familias = familias_28()
    assert len(familias) == 28, "se esperaban 28 familias, hay %d" % len(familias)
    total_nodos = sum(len(m) for _, m in familias)
    assert total_nodos == 67, "se esperaban 67 nodos, hay %d" % total_nodos

    out = []
    out.append("FAMILIAS: %d, NODOS: %d\n" % (len(familias), total_nodos))
    for i, (causa, miembros) in enumerate(familias, 1):
        out.append("=" * 90)
        out.append("FAMILIA %d/%d [%s] (%d miembros): %s" % (i, len(familias), causa, len(miembros), ", ".join(miembros)))
        out.append("=" * 90)
        for nid in miembros:
            n = nodos.get(nid)
            if n is None:
                out.append("  [%s] NO EXISTE EN EL GRAFO" % nid)
                continue
            out.append("--- %s ---" % nid)
            out.append("  dominio: %s | fase_proyecto: %s | deprecado: %s" %
                       (n.get("dominio"), n.get("fase_proyecto"), n.get("deprecado", False)))
            out.append("  titulo_concepto: %s" % n.get("titulo_concepto"))
            out.append("  etiqueta_arbol: %s" % n.get("etiqueta_arbol"))
            out.append("  resumen_teorico: %s" % n.get("resumen_teorico"))
            out.append("  pasos_accionables: %s" % json.dumps(n.get("pasos_accionables"), ensure_ascii=False))
            out.append("  entregable_esperado: %s" % n.get("entregable_esperado"))
            out.append("  ids_alias: %s" % n.get("ids_alias"))
            out.append("  merged_originals: %s" %
                       ([mo.get("node_id") for mo in n.get("merged_originals", [])] if n.get("merged_originals") else None))
            out.append("")

    with open(RAIZ + "/docs/loop/SALIDA_V123_OPS09_CONTENIDO_28FAMILIAS.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("escrito docs/loop/SALIDA_V123_OPS09_CONTENIDO_28FAMILIAS.txt, %d familias, %d nodos" %
          (len(familias), total_nodos))


if __name__ == "__main__":
    main()
