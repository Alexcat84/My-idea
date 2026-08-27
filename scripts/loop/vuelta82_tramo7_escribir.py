# -*- coding: utf-8 -*-
"""VUELTA 82, TAREA 5: OP-E-01, TRAMO 7. Lee las primeras 30 UNIDADES de la
cabeza de la bolsa filtrada de esta vuelta
(docs/loop/SALIDA_V82_TRAMO7_FILTRO_P91_GUARDA_CADENA.txt), en orden de
fichero y sin sorteo. De las 30, VEINTISIETE (indices 0 a 26) YA ESTABAN
DECIDIDAS por vueltas anteriores de esta misma campana (las 20 del tramo
6 mas las 7 NO SE ENLAZA de la lectura fresca del tramo 6, que siguen sin
arista y por eso reaparecen en la cabeza): se citan sin re-derivar. Las
TRES restantes (indices 27, 28 y 29) son lectura fresca de esta vuelta.

CRITERIO ADJUDICADO (sin cambio sobre tramos anteriores): veredicto del
cribado PRIMERO; el paso senalado manda cuando hay veredicto de contenido
que lo respalde; LA VARA NUEVA DE LA CADENA (acta 79, seccion 5 punto 6):
si el hijo ya cuelga de la cadena PROPIA de la madre, o de un radio sobre
una cadena ya establecida por otros hijos directos, la arista no se
escribe aunque el contenido por si solo pasara 9.6.2.

Las TRES, leidas y NO enlazadas, con su razon:

1. `participacion_preferente -> seed_deals_riesgos_precedente` (paso 4,
   dominio core). El paso 4 ("los terminos de la ronda semilla suelen
   convertirse en precedente... vale la pena negociarlos bien desde el
   inicio") es un RECORDATORIO de una linea, no la instruccion que produce
   el entregable del hijo: el hijo despliega un procedimiento propio de
   CINCO pasos que desborda muy por encima del recordatorio (evaluar
   sostenibilidad de la valoracion, anticipar el impacto en rondas
   futuras, preferir un inversionista lider frente a una ronda de fiesta,
   comunicar expectativas a inversionistas no sofisticados, evitar
   valoraciones infladas). Los entregables no coinciden: la madre entrega
   claridad sobre el TIPO DE PARTICIPACION acordado y su impacto en
   escenarios de salida; el hijo entrega una ESTRUCTURA DE RONDA con
   inversionista lider identificado y analisis de sostenibilidad de
   valoracion, un producto distinto. Y el hijo YA TIENE madres
   establecidas y coherentes con su propio tema
   (`dataset/nodos/seed_deals_riesgos_precedente.json`, nodos_previos:
   `valuacion_pre_post_money`, `errores_comunes_fundraising`, las dos
   sobre valoracion y errores de fundraising, no sobre tipos de
   participacion). La vara de la cadena encuentra un camino alcanzable de
   4 saltos (`participacion_preferente -> preferencias_apiladas_vs_blended
   -> cap_table_basico -> valuacion_pre_post_money -> seed_deals_riesgos_
   precedente`) que termina exactamente en la madre real y establecida del
   hijo: anadir un atajo directo saltaria esa progresion ya tejida de
   temas de venture deals. NO SE ENLAZA.

2. `preservar_efectivo_buscar_modelo -> validar_modelo_negocio_hechos`
   (paso 1, dominio core). LA VARA DE LA CADENA MUERDE, exactamente el
   patron de D2 (vuelta 80): `decision_pivotar_o_proceder` es YA un hijo
   DIRECTO establecido de la madre
   (`dataset/nodos/preservar_efectivo_buscar_modelo.json`,
   nodos_siguientes incluye `decision_pivotar_o_proceder`), y
   `decision_pivotar_o_proceder.nodos_siguientes` incluye EXACTAMENTE
   `validar_modelo_negocio_hechos` (verificado campo a campo, camino de 2
   saltos, YA ALCANZABLE). Escribir la arista candidata seria un radio
   sobre una cadena YA ESTABLECIDA de dos aristas reales, el mismo error
   que produjo D2, revertido en la TAREA 3 de la vuelta 80. NO SE ENLAZA.

3. `estructura_reporte_dual_estadistico -> organizacion_liderazgo_
   estadistico` (paso 1, dominio quality). VEREDICTO DEL CRIBADO: puesto
   3121, clase D, DISCUTIBLE MARCADO fuerte y resuelto por el propio
   veredicto: "organizacion trae un paso entero que estructura no tiene,
   EXIGIR DOMINIO REAL del lider [...] estructura trae un paso entero que
   organizacion no tiene, DEFINIR MECANISMOS DE RESOLUCION DE DIFERENCIAS
   DE OPINION [...] Son concerns distintos [...] montados sobre el mismo
   nucleo de reporte dual, no dos lineas sobre el mismo acto. D."
   Mandato expreso del archivo (docs/INTRA_DOMINIO_VEREDICTOS.jsonl). El
   paso 1 de la madre ("nombrar un lider de metodologia estadistica...")
   solo NOMBRA el nombramiento como prerequisito de su propio tema mas
   estrecho (el reporte dual), sin mandar la ejecucion completa del
   procedimiento de liderazgo estadistico de SEIS pasos propios que el
   hijo despliega (formacion y experiencia demostrable, autoridad
   transversal, presencia en decisiones, capacitacion organizacional).
   Entregables distintos: organigrama de reporte dual contra esquema de
   responsabilidad del metodo. NO SE ENLAZA.

Sin escrituras esta lectura: cero aristas nuevas en el tramo 7.
"""

# Los VEINTISIETE ya decididos en vueltas anteriores (las 20 del tramo 6 mas
# las 7 NO SE ENLAZA de su lectura fresca), citados sin re-derivar.
PARES_YA_DECIDIDOS_TRAMO6_Y_ANTERIORES = [
    ("clasificacion_tipos_activos", "tipos_de_pasivos"),
    ("proceso_llamada_inicial_venta", "proceso_venta_franquicias"),
    ("equipo_customer_development", "customer_development_team"),
    ("extraer_priorizar_hipotesis", "value_proposition_startup"),
    ("preparacion_preguntas_problema_precall", "preguntas_situacion"),
    ("timing_solicitud_referidos", "fase_adopt_ciclo_cliente"),
    ("requisitos_numericos_calidad_lotes", "critica_acceptable_quality_level"),
    ("hipotesis_relacion_clientes_web", "mvp_alta_fidelidad"),
    ("producto_mercado_fit_motores", "afinar_motor_crecimiento"),
    ("valor_intangible_sostenibilidad", "compromiso_cliente_sostenibilidad"),
    ("analisis_valor", "customer_needs_spreadsheet"),
    ("posicionamiento_vs_competidores", "analisis_competencia_franquicias"),
    ("organizacion_interna_exportacion", "estructura_plan_exportacion"),
    ("errores_comunes_fundraising", "confidencialidad_nda_adquisicion"),
    ("mvp_catalogo_tecnicas", "mvp_tipo_video"),
    ("reporte_estado_miembro_equipo", "variance_analysis"),
    ("terminologia_clave_breakthrough", "analisis_sintomas"),
    ("evaluacion_actitudes_empleados", "identificar_oportunidades_sostenibilidad"),
    ("pre_control_estadistico", "limites_de_especificacion_vs_limites_de_control"),
    ("posicionamiento_por_tipo_de_mercado", "resegmentacion_mercado_nicho_bajo_costo"),
    ("control_calidad_operaciones_servicio", "descubrir_necesidades_del_cliente"),
    ("el_riesgo_nunca_se_acaba_se_administra", "cuando_el_riesgo_se_vuelve_realidad"),
    ("abolir_inspeccion_masiva", "eliminacion_inspeccion_masiva_por_control_estadistico"),
    ("recursos_apoyo_gubernamental_exportacion", "trabajo_con_bancos_comerciales"),
    ("definiciones_operacionales_de_calidad", "optimizacion_caracteristicas_diseno"),
    ("qfd_matriz", "identificar_clientes_externos_e_internos"),
    ("analisis_variacion_desempeno_servicio", "pre_control_estadistico"),
]

# Las TRES, leidas y NO enlazadas esta vuelta, con su razon (arriba en el docstring).
PARES_DESCARTADOS_NUEVOS = [
    ("participacion_preferente", "seed_deals_riesgos_precedente"),
    ("preservar_efectivo_buscar_modelo", "validar_modelo_negocio_hechos"),
    ("estructura_reporte_dual_estadistico", "organizacion_liderazgo_estadistico"),
]


def main():
    print("ARISTAS ESCRITAS (nodos_siguientes Y nodos_previos): 0")
    print(f"YA DECIDIDOS EN VUELTAS ANTERIORES (citados, no re-derivados): {len(PARES_YA_DECIDIDOS_TRAMO6_Y_ANTERIORES)}")
    for m, h in PARES_YA_DECIDIDOS_TRAMO6_Y_ANTERIORES:
        print(f"  {m} -> {h}")
    print(f"NO ESCRITOS ESTA LECTURA FRESCA, con razon: {len(PARES_DESCARTADOS_NUEVOS)}")
    for m, h in PARES_DESCARTADOS_NUEVOS:
        print(f"  {m} -> {h}")
    print()
    print("DISCUTIBLES marcados para la relectura ciega del auditor: 0")


if __name__ == "__main__":
    main()
