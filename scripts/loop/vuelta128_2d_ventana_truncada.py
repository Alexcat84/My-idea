# -*- coding: utf-8 -*-
"""vuelta128_2d_ventana_truncada.py . MEDICION PARA LA FICHA NUEVA
ventana-truncada-de-condiciones-activacion (TAREA 2.d de la vuelta 128).

Sobre los 31 ids de la nomina de OP-S-10, cuenta cuantos tienen HOY mas
condiciones_activacion que la ventana ([:2] o [:3]), lo que significa que,
tras anteponer la condicion de pais (vueltas 126 y 128), la ULTIMA condicion
vieja del nodo queda fuera de lo que consume el motor en esos tres sitios.
No toca ningun nodo: solo mide y publica.
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TOCADOS_126 = [
    "alternativa_business_opportunity_licensing", "alternativa_trademark_licensing",
    "calculo_roi_franquiciado_2", "calificacion_prospectos_award", "concepto_de_advances",
    "cumplir_leyes_estatales_franquicia", "decision_fpr", "decision_marca_comun_branding",
    "desarrollar_manual_operaciones", "diseno_programa_capacitacion_franquicia",
]
TOCADOS_128 = [
    "eleccion_abogado_franquicias", "estimacion_inversion_inicial_franquiciador",
    "estructura_proveedores_aprobados_designados", "exenciones_legales_franquicia",
    "financial_performance_representations", "ingresos_por_rebates", "los_tres_grandes_criterios",
    "multiples_compradores_influyentes", "obtencion_marca_registrada", "preparar_fdd",
    "proceso_venta_franquicias", "programas_compra_franquicia", "propuesta_valor_franquicia",
    "proteccion_propiedad_intelectual_franq", "registro_estatal_franquicia", "revision_legal_marketing",
]
TOCADOS = set(TOCADOS_126) | set(TOCADOS_128)


def main():
    ops = [json.loads(l) for l in open(os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl"), encoding="utf-8") if l.strip()]
    op = [o for o in ops if o.get("id_op") == "OP-S-10"][0]
    nomina = op["nodos"]
    hoy = json.load(open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8"))["nodos"]

    print("nomina OP-S-10: %d ids" % len(nomina))
    for ventana in (2, 3):
        afectados = []
        for nid in sorted(nomina):
            n = hoy.get(nid)
            if n is None:
                continue
            conds = n.get("condiciones_activacion") or []
            if len(conds) > ventana:
                afectados.append(nid)
        tocados_afectados = [nid for nid in afectados if nid in TOCADOS]
        no_tocados_afectados = [nid for nid in afectados if nid not in TOCADOS]
        print()
        print("VENTANA [:%d]: %d de los 31 tienen mas de %d condiciones_activacion hoy (la ultima vieja queda "
              "fuera de lo que consume el motor en esos sitios):" % (ventana, len(afectados), ventana))
        print("  DE ELLOS, AFECTADOS POR ANTEPONER (tocados en 126 o en 128): %d -> %s"
              % (len(tocados_afectados), tocados_afectados))
        print("  YA EXCEDIAN LA VENTANA ANTES, SIN TOCAR EN ESTA CAMPANA (contramodelos u otros): %d -> %s"
              % (len(no_tocados_afectados), no_tocados_afectados))


if __name__ == "__main__":
    main()
