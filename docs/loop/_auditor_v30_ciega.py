"""Auditor vuelta 30: impresion CIEGA de pasos para la relectura.

Imprime SOLO los pasos y campos de objeto (titulo, resumen, entregable),
nunca los motivos escritos del ejecutor. Los tres nodos cortados se leen
de la APERTURA (4e0a87ea); el resto, del arbol de hoy.
"""
import json
import subprocess
import sys

APERTURA = "4e0a87ea"


def nodo(nid, ref=None):
    ruta = "dataset/nodos/%s.json" % nid
    if ref:
        out = subprocess.run(["git", "show", "%s:%s" % (ref, ruta)],
                             capture_output=True, text=True, encoding="utf-8")
        return json.loads(out.stdout)
    return json.load(open(ruta, encoding="utf-8"))


def imprimir(nid, ref=None, con_objeto=False):
    d = nodo(nid, ref)
    print("=" * 74)
    print("%s (%s)  fuente: %s" % (nid, "APERTURA" if ref else "HOY", d.get("fuente")))
    if con_objeto:
        print("titulo   : %s" % d.get("titulo"))
        print("resumen  : %s" % d.get("resumen"))
        print("entregable: %s" % d.get("entregable_esperado"))
    for i, p in enumerate(d["pasos_accionables"], 1):
        print("  %2d. %s" % (i, p))
    print()


if __name__ == "__main__":
    cual = sys.argv[1]
    if cual == "cortados":
        for nid in ["viral_loop_marketing", "coeficiente_viral",
                    "decision_de_vender_startup"]:
            imprimir(nid, APERTURA)
    elif cual == "col":
        for nid in ["cultura_de_experiencia", "blueprint_de_experiencia",
                    "keep_customers_strategy", "retention_metrics",
                    "ganar_comprension_del_cliente", "estrategia_crecimiento_clientes"]:
            imprimir(nid)
    elif cual == "destinos":
        for nid in ["experiencias_exclusivas_vip", "comunidad_tribu_marca",
                    "construccion_tribu_de_marca"]:
            imprimir(nid, APERTURA, con_objeto=True)
    elif cual == "fundidos":
        for nid in ["viral_loop_marketing", "coeficiente_viral",
                    "decision_de_vender_startup"]:
            imprimir(nid)
