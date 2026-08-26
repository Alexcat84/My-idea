# -*- coding: utf-8 -*-
"""VUELTA 79, TAREA 3.2: relectura AL DOBLE del tramo 4 de OP-E-01 (24 aristas
escritas en la vuelta 78), por el credito rebajado (el hallazgo del par en dos
direcciones, acta 78 seccion 4, aparecio FUERA de los discutibles marcados;
AUDITOR.md seccion 1.2 manda releer el tramo al doble).

DOS BARRIDOS, LOS DOS CON FICHERO DE SALIDA Y LA TABLA CONTADA DE SU FICHERO:

1. Cruza las 24 aristas escritas contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl,
   emparejando SIN DIRECCION (el cribado lee PARES, no aristas dirigidas).
   Publica par a par si el cribado lo habia leido y con que clase.

2. Cruza las 24 contra la bolsa filtrada de la vuelta 78
   (docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V78.jsonl, snapshot de 191 filas
   ANTES de que el tramo 4 escribiera, que es donde vive la vara nueva de la
   TAREA 4: el mismo par propuesto en las dos direcciones), buscando el MISMO
   PAR en la DIRECCION CONTRARIA. Publica cuantas de las 24 tenian su
   reciproca propuesta y no leida.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]

PARES_SANOS = [
    ("necesidades_reales_vs_declaradas", "descubrir_necesidades_del_cliente"),
    ("sujetos_de_control", "key_process_product_characteristics"),
    ("metas_desmaterializacion_energia", "establecer_metas_reduccion_emisiones"),
    ("diferencia_iso9001_iso9004", "trilogia_de_juran"),
    ("aprobacion_alta_direccion", "metas_negocio_calidad"),
    ("seguimiento_cumplimiento_cadena_suministro", "auditorias_proveedores"),
    ("gestion_diferencias_culturales", "participacion_ferias_comerciales"),
    ("decision_momento_fundacion", "evaluacion_conocimiento_industria"),
    ("actualizar_business_model_canvas_tuneup", "value_proposition_startup"),
    ("etapa_build_business_case", "value_proposition_startup"),
    ("extraer_priorizar_hipotesis", "value_proposition_startup"),
    ("optimizacion_embudo_get_customers", "mvp_alta_fidelidad"),
    ("producto_mercado_fit_motores", "contabilidad_innovacion"),
    ("technology_platform_evaluation", "stage_gate_td_tecnologia"),
    ("ventaja_competitiva_producto", "value_proposition_startup"),
    ("conformidad_comercio_internacional", "sistema_gestion_calidad"),
    ("viaje_diagnostico_remedial", "resistencia_al_cambio"),
    ("breakthrough_cultural", "reconocimiento_publico_recompensas"),
    ("auditoria_de_proceso", "seguimiento_accion_correctiva"),
    ("planificacion_inicial_calidad", "medicion_capacidad_servicio"),
    ("etapa_discovery_ideacion", "internal_idea_capture"),
    ("uso_inadecuado_computadoras", "causas_especiales_y_comunes_variacion"),
    ("diamante_de_innovacion", "asignacion_recursos_en_gates"),
    ("plan_cambio_climatico", "formar_consejo_asesor_sostenibilidad"),
]

assert len(PARES_SANOS) == 24, "el tramo 4 escribio 24, contadas: %d" % len(PARES_SANOS)


def cargar_veredictos():
    ruta = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
    por_par = {}
    with open(ruta, encoding="utf-8") as f:
        for i, linea in enumerate(f, start=1):
            d = json.loads(linea)
            a, b = d.get("nodo_a"), d.get("nodo_b")
            clave = frozenset((a, b))
            por_par.setdefault(clave, []).append((i, d))
    return por_par


def cargar_bolsa_v78():
    ruta = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO_FILTRADO_V78.jsonl"
    filas = []
    with open(ruta, encoding="utf-8") as f:
        for i, linea in enumerate(f, start=1):
            d = json.loads(linea)
            d["_fila"] = i
            filas.append(d)
    return filas


def main():
    veredictos = cargar_veredictos()
    bolsa = cargar_bolsa_v78()

    print("=" * 78)
    print("BARRIDO 1: LAS 24 ARISTAS DEL TRAMO 4 CONTRA INTRA_DOMINIO_VEREDICTOS.jsonl (SIN DIRECCION)")
    print("=" * 78)
    leidos = 0
    clase_a = 0
    a_revertir = []
    for madre, hijo in PARES_SANOS:
        clave = frozenset((madre, hijo))
        entradas = veredictos.get(clave, [])
        if not entradas:
            print("  %s -> %s | SIN VEREDICTO" % (madre, hijo))
            continue
        leidos += 1
        for puesto, d in entradas:
            clase = d.get("clase")
            print("  %s -> %s | puesto %d | clase %s" % (madre, hijo, puesto, clase))
            if clase == "A":
                clase_a += 1
                # a revertir si la arista escrita contradice un veredicto A
                a_revertir.append((madre, hijo, puesto))
    print()
    print("RESUMEN BARRIDO 1: pares %d | LEIDOS por el cribado %d | clase A %d | A REVERTIR %d"
          % (len(PARES_SANOS), leidos, clase_a, len(a_revertir)))
    print()

    print("=" * 78)
    print("BARRIDO 2: LAS 24 CONTRA LA BOLSA FILTRADA DE LA VUELTA 78 (191 FILAS), BUSCANDO LA RECIPROCA")
    print("=" * 78)
    con_reciproca = []
    for madre, hijo in PARES_SANOS:
        reciprocas = [f for f in bolsa if f["madre"] == hijo and f["hijo"] == madre]
        if reciprocas:
            for r in reciprocas:
                print("  %s -> %s | RECIPROCA en fila %d (paso %s), arista=%s"
                      % (madre, hijo, r["_fila"], r["paso"], r["arista"]))
            con_reciproca.append((madre, hijo))
        else:
            pass
    print()
    print("RESUMEN BARRIDO 2: de las 24, con reciproca propuesta en la bolsa filtrada: %d"
          % len(con_reciproca))
    for madre, hijo in con_reciproca:
        print("  -> %s -> %s" % (madre, hijo))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
