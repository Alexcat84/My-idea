# -*- coding: utf-8 -*-
"""vuelta126_tarea3c_remedicion_ops10.py . REMEDICION DE LAS CIFRAS
DERIVADAS DE OP-S-10 (TAREA 3.c de la vuelta 126), contra el grafo de HOY.

Mide, sobre los 31 ids de la nomina de OP-S-10 (docs/plan/OPERACIONES.jsonl):
  - cuantos siguen VIVOS hoy
  - de los vivos, cuantos ya nombran el pais (Estados Unidos / EE.UU. / USA)
    en condiciones_activacion
  - cuantos no lo nombran en NINGUN sitio (condiciones_activacion,
    resumen_teorico, pasos_accionables)
  - cuantos SOLO lo nombran en resumen_teorico (no en condiciones_activacion
    ni en pasos_accionables)
  - de los OCHO nodos que la nota de OP-S-10 da como "dentro de un acto",
    cuantos siguen vivos hoy

Uso:
  python scripts/loop/vuelta126_tarea3c_remedicion_ops10.py
"""
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

NOMINA = [
    "comprender_definicion_legal_franquicia", "cumplimiento_ftc_rule_436",
    "calculo_roi_franquiciado_2", "cumplir_leyes_estatales_franquicia",
    "eleccion_abogado_franquicias", "registro_estatal_franquicia",
    "alternativa_business_opportunity_licensing", "alternativa_trademark_licensing",
    "calificacion_prospectos_award", "cinco_categorias_costos_franquicia",
    "concepto_de_advances", "decision_fpr", "decision_marca_comun_branding",
    "desarrollar_manual_operaciones", "diseno_programa_capacitacion_franquicia",
    "elaboracion_fdd", "estimacion_inversion_inicial_franquiciador",
    "estructura_proveedores_aprobados_designados", "estructuras_combinadas_franquicia",
    "exenciones_legales_franquicia", "financial_performance_representations",
    "ingresos_por_rebates", "los_tres_grandes_criterios",
    "multiples_compradores_influyentes", "obtencion_marca_registrada",
    "preparar_fdd", "proceso_venta_franquicias", "programas_compra_franquicia",
    "propuesta_valor_franquicia", "proteccion_propiedad_intelectual_franq",
    "revision_legal_marketing",
]

OCHO_DENTRO_DE_UN_ACTO = [
    "cinco_categorias_costos_franquicia", "estimacion_inversion_inicial_franquiciador",
    "eleccion_abogado_franquicias", "elaboracion_fdd", "preparar_fdd",
    "comprender_definicion_legal_franquicia", "estructuras_combinadas_franquicia",
    "desarrollar_manual_operaciones",
]

PATRON_PAIS = re.compile(r"Estados Unidos|EE\.?UU\.?|USA\b", re.IGNORECASE)


def cargar():
    with open(RUTA_GRAFO, encoding="utf-8") as f:
        return json.load(f)["nodos"]


def nombra_pais(textos):
    return any(PATRON_PAIS.search(t or "") for t in textos)


def main():
    nodos = cargar()
    vivos, deprecados, ausentes = [], [], []
    for nid in NOMINA:
        n = nodos.get(nid)
        if n is None:
            ausentes.append(nid)
        elif n.get("deprecado"):
            deprecados.append(nid)
        else:
            vivos.append(nid)

    en_condiciones, en_ningun_sitio, solo_en_resumen, solo_en_pasos = [], [], [], []
    for nid in vivos:
        n = nodos[nid]
        cond = n.get("condiciones_activacion") or []
        resumen = [n.get("resumen_teorico") or ""]
        pasos = n.get("pasos_accionables") or []

        pais_cond = nombra_pais(cond)
        pais_resumen = nombra_pais(resumen)
        pais_pasos = nombra_pais(pasos)

        if pais_cond:
            en_condiciones.append(nid)
        if not (pais_cond or pais_resumen or pais_pasos):
            en_ningun_sitio.append(nid)
        if pais_resumen and not pais_cond and not pais_pasos:
            solo_en_resumen.append(nid)
        if pais_pasos and not pais_cond and not pais_resumen:
            solo_en_pasos.append(nid)

    ocho_vivos = [nid for nid in OCHO_DENTRO_DE_UN_ACTO if nodos.get(nid) and not nodos[nid].get("deprecado")]
    ocho_deprecados = [nid for nid in OCHO_DENTRO_DE_UN_ACTO if nodos.get(nid) and nodos[nid].get("deprecado")]

    print("NOMINA DE OP-S-10: %d ids" % len(NOMINA))
    print("AUSENTES DEL GRAFO: %d %s" % (len(ausentes), ausentes))
    print("DEPRECADOS: %d %s" % (len(deprecados), sorted(deprecados)))
    print("VIVOS: %d" % len(vivos))
    print()
    print("DE LOS %d VIVOS:" % len(vivos))
    print("  ya nombran el pais en condiciones_activacion: %d" % len(en_condiciones))
    for nid in sorted(en_condiciones):
        print("    %s" % nid)
    print("  NO nombran el pais en NINGUN sitio (condiciones/resumen/pasos): %d" % len(en_ningun_sitio))
    for nid in sorted(en_ningun_sitio):
        print("    %s" % nid)
    print("  lo nombran SOLO en el resumen_teorico: %d" % len(solo_en_resumen))
    for nid in sorted(solo_en_resumen):
        print("    %s" % nid)
    print("  lo nombran SOLO en pasos_accionables (no en condiciones ni resumen): %d" % len(solo_en_pasos))
    for nid in sorted(solo_en_pasos):
        print("    %s" % nid)
    print("  SUMA DE LAS CUATRO CATEGORIAS (debe dar %d): %d" %
          (len(vivos), len(en_condiciones) + len(en_ningun_sitio) + len(solo_en_resumen) + len(solo_en_pasos)))
    print()
    print("DE LOS 8 NODOS 'DENTRO DE UN ACTO' (nota de OP-S-10):")
    print("  siguen VIVOS: %d %s" % (len(ocho_vivos), sorted(ocho_vivos)))
    print("  DEPRECADOS: %d %s" % (len(ocho_deprecados), sorted(ocho_deprecados)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
