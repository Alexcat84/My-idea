# -*- coding: utf-8 -*-
"""vuelta124_tarea3a_extraer_contenido_resto.py . TAREA 3.a de la vuelta 124.

Extrae, FRESCO del master_graph.json de HOY (regla 2 de EJECUTOR.md: el
instrumento manda, la salida se lee de la corrida de esta vuelta), el
contenido completo de los nodos que intervienen en los 12 pares que
docs/loop/SALIDA_V124_TAREA2A_CONTEO_PARES.txt nombra como faltantes del
racimo de OP-S-09, para la lectura dirigida par a par de la TAREA 3.a.

USO:
  python scripts/loop/vuelta124_tarea3a_extraer_contenido_resto.py
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PARES_FALTANTES = [
    ("accion_correctiva", "accion_correctiva", "accion_correctiva_4"),
    ("auditoria_de_producto", "auditoria_de_producto", "auditoria_producto"),
    ("consejo_de_calidad", "consejo_de_calidad", "consejo_de_calidad_3"),
    ("capacidad_de_proceso", "capacidad_de_proceso", "capacidad_del_proceso"),
    ("dia_cero_defectos", "dia_cero_defectos", "dia_cero_defectos_3"),
    ("make_certain_programa", "make_certain_programa", "programa_make_certain_2"),
    ("make_certain_programa", "make_certain_programa", "programa_make_certain_3"),
    ("make_certain_programa", "programa_make_certain", "programa_make_certain_3"),
    ("clasificacion_de_seriedad_de_defectos", "clasificacion_de_seriedad_de_defectos", "clasificacion_seriedad_defectos"),
    ("cultura_justa", "cultura_justa", "cultura_justa_3"),
    ("definiciones_operacionales", "definiciones_operacionales", "definiciones_operacionales_3"),
    ("estrategia_de_innovacion_de_producto", "estrategia_de_innovacion_de_producto", "estrategia_innovacion_producto"),
]


def main():
    with open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8") as f:
        master = json.load(f)
    nodos = master["nodos"]

    ids_por_familia = {}
    for fam, a, b in PARES_FALTANTES:
        ids_por_familia.setdefault(fam, [])
        for i in (a, b):
            if i not in ids_por_familia[fam]:
                ids_por_familia[fam].append(i)

    out = ["12 PARES FALTANTES DEL RACIMO DE OP-S-09, %d familias, %d nodos distintos\n" %
           (len(ids_por_familia), len(set(i for ids in ids_por_familia.values() for i in ids)))]
    for fam, ids in ids_por_familia.items():
        out.append("=" * 90)
        out.append("FAMILIA [%s] (%d nodos en esta lectura): %s" % (fam, len(ids), ", ".join(sorted(ids))))
        out.append("=" * 90)
        for nid in sorted(ids):
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

    ruta_out = os.path.join(RAIZ, "docs", "loop", "SALIDA_V124_OPS09_CONTENIDO_RESTO.txt")
    with open(ruta_out, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("escrito docs/loop/SALIDA_V124_OPS09_CONTENIDO_RESTO.txt, %d familias, %d nodos distintos" %
          (len(ids_por_familia), sum(len(v) for v in ids_por_familia.values())))


if __name__ == "__main__":
    main()
