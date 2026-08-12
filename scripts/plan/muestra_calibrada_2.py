# -*- coding: utf-8 -*-
"""Segunda muestra pineada, sobre la bolsa V2 y DISJUNTA de la primera.
   Semilla declarada en docs/plan/PIN_SORTEO_CALIBRADO.txt ANTES de mirar."""
import json, io, sys, random
sys.stdout.reconfigure(encoding="utf-8")
SEMILLA = 20260811002
YA = {("cuatro_etapas_llamada_de_ventas",2),("customer_discovery_phase2_problem_test",2),
("ecuacion_de_valor_cliente",3),("eliminar_desperdicio_organizacional",4),
("evitar_pseudociencia_producto",1),("genchi_gembutsu",1),("key_partners_hypothesis",5),
("liderazgo_ejecutivo_innovacion",1),("principio_correspondencia_contable",1),
("establecer_metas_reduccion_emisiones",3),("screening_mercados_potenciales",5),
("preparar_fdd",1),("reduccion_riesgo_percibido",2),("autorregulacion_seguridad",3),
("brecha_de_calidad_cuatro_gaps",1),("causas_especiales_y_comunes_variacion",3),
("certificacion_de_proveedores",3),("consejo_calidad_2",2),("criticas_muestreo_aceptacion",2),
("gestion_para_la_calidad",1),("inventario_conocimiento_estadistico_personal",4),
("key_process_product_characteristics",4),("mantenimiento_productivo_total",2),
("planes_de_muestreo_de_aceptacion",1)}
b = [json.loads(l) for l in io.open("docs/plan/PASO_NODO_CALIBRADO.jsonl", encoding="utf-8") if l.strip()]
b = [f for f in b if not f["arista"]]
b = [f for f in b if (f["madre"], f["paso"]) not in YA]
b.sort(key=lambda f: (f["dominio"], f["madre"], f["paso"], f["hijo"]))
print("bolsa V2 sin arista y sin los ya leidos:", len(b), "| semilla:", SEMILLA)
m = random.Random(SEMILLA).sample(b, 24)
G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
for i, f in enumerate(sorted(m, key=lambda x: (x["dominio"], x["madre"])), 1):
    print("="*76)
    print("N-%02d  [%s]  t%.0f c%.2f  fam %s -> %s" % (i, f["dominio"], f["titulo_ratio"], f["contencion"], f["familia_paso"], f["familia_hijo"]))
    print("  MADRE %s, paso %d:" % (f["madre"], f["paso"]))
    print("     %s" % f["texto_paso"][:185])
    print("  HIJO  %s: %s" % (f["hijo"], f["titulo_hijo"]))
    for j, s in enumerate(G[f["hijo"]].get("pasos_accionables") or [], 1):
        print("     %d. %s" % (j, s[:125]))
