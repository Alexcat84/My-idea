#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""backlog_l03_vuelta14.py . Recomputo del backlog de OP-L-03 al corte 3.388,
por la via del archivo de componentes (docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl),
la misma que se uso para OP-U-02 en la vuelta 13.

SOLO LECTURA. No escribe nodos, veredictos ni operaciones. Imprime.

METODO, calcado del que ya definio el propio OP-L-03 en LECTURAS_DIRIGIDAS.md:
  1. Universo: actos (componentes de A, tamano >= 2) ABIERTOS de tamano 3 a 6,
     leidos de docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl (ya generado por
     scripts/plan/recomputo_3388.py sobre el corte 3.388).
  2. Se excluyen los actos que tocan alguna de las SEIS nominas que OP-L-02 ya
     cerro por LECTURA DIRIGIDA (cuadrantes de mercado, ecuacion de valor,
     bloque humano de la supervision de la IA, sales roadmap, seleccion de
     canal, junta asesora). Esas lecturas no viven en
     docs/INTRA_DOMINIO_VEREDICTOS.jsonl (son fuera de cola), asi que el
     archivo de componentes las sigue marcando ABIERTAS: si no se excluyen a
     mano, se cuentan dos veces entre OP-L-02 y OP-L-03.
  3. Del resto, se excluyen los actos que "esperan destejido o cirugia": los
     que tienen algun nodo en la nomina de una operacion tipo DESTEJIDO
     (docs/plan/OPERACIONES.jsonl). "Cirugia" es sinonimo de DESTEJIDO en el
     banco del plan (00_INDICE.md linea 326: "las siete cirugias hechas" son
     los siete OP-D-*).
  4. Lo que queda es el backlog de OP-L-03 al corte 3.388.

DISCUTIBLE, declarado en el reporte: quedan actos del resto que tocan la
nomina de otras operaciones NO destejido (MESA, HERRAMIENTA, CAMPO_SUCIO,
DECISION_DE_FUENTE). No se excluyen porque la regla escrita de OP-L-02 solo
nombra "destejido o cirugia", no "cualquier operacion" (ese es el criterio
ANCHO que uso OP-U-02 para otra pregunta, no esta). Se listan aparte para que
el auditor los vea.
"""
import io
import json
from pathlib import Path
from collections import Counter

RAIZ = Path(__file__).resolve().parents[2]


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


NOMINAS_OP_L_02 = {
    "sales_roadmap": {"customer_validation_sales_roadmap", "estrategia_de_ventas",
                       "hoja_de_ruta_de_ventas", "refinar_sales_roadmap", "sales_roadmap",
                       "sales_roadmap_vs_sales_force"},
    "cuadrantes_de_mercado": {"clasificacion_mercados_cadena_suministro", "cuatro_capacidades_mercado",
                               "cuatro_categorias_desempeno_cadena_suministro",
                               "estrategia_cuatro_capacidades_mercado",
                               "marco_analisis_mercado_cadena_suministro", "modelo_cuadrantes_mercado"},
    "bloque_humano_supervision_ia": {"alineacion_etica_ia_negocio", "human_in_the_loop_ia",
                                      "mitigar_falling_asleep_wheel", "principio_humano_en_el_loop",
                                      "riesgo_sobredependencia_ia"},
    "ecuacion_de_valor": {"construccion_de_valor_percibido", "ecuacion_de_valor",
                           "ecuacion_de_valor_cliente", "ecuacion_de_valor_venta",
                           "prevencion_objeciones_vs_manejo"},
    "seleccion_de_canal": {"channels_hypothesis_physical", "channels_hypothesis_web_mobile",
                            "hipotesis_de_canales", "seleccion_canal_distribucion",
                            "seleccion_canal_fisico"},
    "junta_asesora": {"formalizar_junta_asesora", "formalize_advisory_board",
                       "identificar_consejo_asesores", "identificar_junta_asesores"},
}


def main():
    comps = cargar(RAIZ / "docs" / "plan" / "RECOMPUTO_3388_COMPONENTES.jsonl")
    ops = cargar(RAIZ / "docs" / "plan" / "OPERACIONES.jsonl")

    excluir_l02 = set()
    for s in NOMINAS_OP_L_02.values():
        excluir_l02 |= s

    destejidos = [o for o in ops if o["tipo"] == "DESTEJIDO"]
    nomop_no_destejido = [o for o in ops if o.get("nodos") and o["tipo"] != "DESTEJIDO"]

    abiertos = [c for c in comps if c["estado"] == "ABIERTO" and 3 <= c["tamano"] <= 6]
    print("ABIERTOS tamano 3-6, corte 3.388: %d actos, %d pares fuera de cola"
          % (len(abiertos), sum(c["fuera_de_cola"] for c in abiertos)))

    resto = [c for c in abiertos if not (set(c["miembros"]) & excluir_l02)]
    print("tras excluir las SEIS nominas ya cerradas por OP-L-02: %d actos, %d pares"
          % (len(resto), sum(c["fuera_de_cola"] for c in resto)))

    esperan = []
    backlog = []
    for c in resto:
        ms = set(c["miembros"])
        hits_destejido = [o["id_op"] for o in destejidos if ms & set(o["nodos"])]
        if hits_destejido:
            esperan.append((c, hits_destejido))
        else:
            backlog.append(c)

    print("de esos, ESPERAN destejido o cirugia (tocan una nomina DESTEJIDO): %d actos, %d pares"
          % (len(esperan), sum(c["fuera_de_cola"] for c, _ in esperan)))
    for c, hits in esperan:
        print("   tamano %d, %d pares: %s -- %s" % (c["tamano"], c["fuera_de_cola"],
                                                      sorted(c["miembros"]), hits))

    print()
    print("BACKLOG DE OP-L-03 AL CORTE 3.388: %d actos, %d pares" % (
        len(backlog), sum(c["fuera_de_cola"] for c in backlog)))
    print("reparto por tamano de acto:")
    tam = Counter(c["tamano"] for c in backlog)
    pares_por_tam = Counter()
    for c in backlog:
        pares_por_tam[c["tamano"]] += c["fuera_de_cola"]
    for t in sorted(tam):
        print("   tamano %d: %d actos, %d pares" % (t, tam[t], pares_por_tam[t]))

    print()
    print("LISTA DECLARADA, un acto por linea:")
    for c in sorted(backlog, key=lambda x: (-x["tamano"], sorted(x["miembros"]))):
        print("   [%d, %d pares] %s" % (c["tamano"], c["fuera_de_cola"], ", ".join(sorted(c["miembros"]))))

    print()
    print("DISCUTIBLE: de los %d del backlog, cuantos tocan ADEMAS una operacion NO destejido"
          " (MESA, HERRAMIENTA, CAMPO_SUCIO, DECISION_DE_FUENTE), sin que la regla escrita mande excluirlos:"
          % len(backlog))
    tocan_otra = 0
    for c in backlog:
        ms = set(c["miembros"])
        hits = [o["id_op"] + ":" + o["tipo"] for o in nomop_no_destejido if ms & set(o["nodos"])]
        if hits:
            tocan_otra += 1
            print("   tamano %d, %d pares: %s -- %s" % (c["tamano"], c["fuera_de_cola"],
                                                          sorted(c["miembros"]), hits))
    print("total: %d de %d" % (tocan_otra, len(backlog)))


if __name__ == "__main__":
    main()
