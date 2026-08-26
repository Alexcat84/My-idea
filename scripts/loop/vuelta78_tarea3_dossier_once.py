"""VUELTA 78, TAREA 3.2: dossier de las 11 aristas de la fase 04 que la vara
de los veredictos A toca (docs/loop/_auditor_v77_guardaA.txt, seccion FASE
04 ENTERA). Para cada arista, y para cada companero en un veredicto A vivo:
- el veredicto completo (razon, puesto_intra)
- si el companero esta cubierto por alguna operacion NO EJECUTADA (eliminar,
  superviviente, o nodos de RENOMBRE_CON_ALIAS) y cual
- si el companero esta en la nomina de OP-S-09
- estado vivo/deprecado de los tres nodos (madre, hijo, companero)
Solo junta datos, no decide: la decision par a par va en el reporte.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
OPERACIONES = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"
VEREDICTOS = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"

ONCE = [
    ("concepto_proyecto_breakthrough", "pocos_vitales_muchos_utiles"),
    ("customer_validation", "mvp_alta_fidelidad"),
    ("customer_validation", "prueba_mvp_alta_fidelidad"),
    ("earlyvangelists_ventas_tempranas", "value_proposition_startup"),
    ("ecuacion_de_valor_cliente", "preguntas_need_payoff"),
    ("estrategia_de_innovacion_arenas", "product_roadmap_estrategico"),
    ("franquicia_unidad_individual", "programa_de_referidos_de_franquiciados"),
    ("funnel_get_customers_optimizacion", "disenar_tests_pass_fail"),
    ("screening_mercados_potenciales", "uso_del_us_commercial_service"),
    ("testing_process_completo", "value_proposition_canvas"),
    ("waterfall_vs_agile_development", "desarrollo_de_clientes_customer_development"),
]


def main():
    ops = [json.loads(l) for l in OPERACIONES.read_text(encoding="utf-8").splitlines() if l.strip()]
    veredictos = [json.loads(l) for l in VEREDICTOS.read_text(encoding="utf-8").splitlines() if l.strip()]
    grafo = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
    op_s09 = [o for o in ops if o["id_op"] == "OP-S-09"][0]
    nomina_s09 = set(op_s09.get("nodos") or [])

    condenado_por_op = {}
    for op in ops:
        if op.get("estado") == "HECHA":
            continue
        for nid in op.get("eliminar") or []:
            condenado_por_op.setdefault(nid, []).append((op["id_op"], "eliminar"))
        if op.get("superviviente"):
            condenado_por_op.setdefault(op["superviviente"], []).append((op["id_op"], "superviviente"))
        if op.get("tipo") == "RENOMBRE_CON_ALIAS":
            for nid in op.get("nodos") or []:
                condenado_por_op.setdefault(nid, []).append((op["id_op"], "nodos"))

    def vivo(nid):
        n = grafo.get(nid)
        if n is None:
            return "NO EXISTE"
        return "DEPRECADO" if n.get("deprecado") else "VIVO"

    def edge_exists(m, h):
        n = grafo.get(m)
        return h in (n.get("nodos_siguientes") or []) if n else False

    for madre, hijo in ONCE:
        print("=" * 100)
        print(f"{madre} -> {hijo}")
        print(f"  madre: {vivo(madre)}, condenada por: {condenado_por_op.get(madre, [])}, en nomina OP-S-09: {madre in nomina_s09}")
        print(f"  hijo:  {vivo(hijo)}, condenado por: {condenado_por_op.get(hijo, [])}, en nomina OP-S-09: {hijo in nomina_s09}")
        print(f"  arista existe hoy en el grafo: {edge_exists(madre, hijo)}")
        for v in veredictos:
            if v.get("clase") != "A":
                continue
            a, b = v.get("nodo_a"), v.get("nodo_b")
            if madre in (a, b) or hijo in (a, b):
                extremo = "madre" if madre in (a, b) else "hijo"
                companero = b if a in (madre, hijo) else a
                print(f"  --- A vivo, puesto {v['puesto_intra']}, extremo={extremo}, companero={companero} ({vivo(companero)}) ---")
                print(f"      condenado_por_op(companero)={condenado_por_op.get(companero, [])}  en_nomina_s09={companero in nomina_s09}")
                print(f"      razon: {v['razon']}")
        print()


if __name__ == "__main__":
    main()
