# -*- coding: utf-8 -*-
r"""vuelta197_tarea3b_mis_clases.py . LAS CLASES DEL EJECUTOR SOBRE LOS 240,
ESCRITAS Y SELLADAS ANTES DE ABRIR EL DESTAPE.

EL ORDEN ES LO UNICO QUE HACE QUE EL COTEJO VALGA, y por eso este fichero y su
salida se commitean ANTES de que nadie abra `SALIDA_V197_T3_DESTAPE.txt`.

LOS PUESTOS NO SE TECLEAN: se leen de `docs/loop/SALIDA_V197_T3_CIEGA.txt`. Lo
unico tecleado aqui es MI CLASE y MI RAZON de cada par, que es lo que se esta
midiendo.

USO:
  python scripts/loop/vuelta197_tarea3b_mis_clases.py
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

CLASES_A = [160, 161, 166, 206, 209, 211, 400, 401, 403, 404, 614, 655, 723, 724,
            883, 885, 886, 908, 916, 976, 1218, 1807, 1808, 1809, 1810, 1818,
            1822, 1824, 1826, 1828, 1829, 2430, 2431, 2432, 2434, 2662, 2663,
            2664, 2666, 2668, 2838, 2916, 2922, 3076, 3094, 3095, 3173]
CLASES_C = [1077]
CLASES_B = []

RAZON_D = ("D. CONTINUA o ARISTA QUE FALTA: procedimiento en UN SOLO sentido, o "
           "dos nodos distintos que no se repiten. Lo que uno anade al otro NO "
           "cabe en una linea.")

RAZONES = {
160: "A. gestion_sindicato_inversores y manejo_syndicate_inversion dicen los MISMOS actos: lider, acuerdo de que negocia por todos, comunicacion con cada uno, no renegociar por separado. Duplicacion en dos idiomas.",
161: "A. CONTENCION: los 4 pasos de presupuesto_agil_innovacion caben ENTEROS en asignacion_agil_de_recursos, dos de ellos palabra por palabra, y no traen ni un paso propio.",
166: "A. human_in_the_loop_ia y principio_humano_en_el_loop: los mismos cuatro, donde decide sola, revisar cada respuesta, reconocer la alucinacion, doble revision en alto impacto.",
206: "A. CONTENCION: los 4 pasos de customer_discovery_overview son los pasos 6 a 9 de customer_discovery condensados. Nada propio.",
209: "A. etapa_de_investigacion y etapa_investigacion_ventas: preguntar antes de presentar, resistir la demo, medir la proporcion. Lo que B anade es una LINEA, entrenar al equipo.",
211: "A. CONTENCION: el paso 4 de preguntas_excelencia_operacional es LITERALMENTE el paso 11 de framework_excelencia_operacional, y sus otros tres son sus pasos 1 a 3.",
400: "A. hipotesis_de_canales y seleccion_canal_distribucion comparten cuatro de cinco: precio contra canal, costos del canal, UN canal, recalcular el ingreso neto. Los dos residuos son lineas.",
401: "A. CONTENCION AL REVES: los pasos 7, 8 y 9 de modelo_spin_preguntas son LITERALMENTE los pasos 1, 3 y 4 de modelo_spin, y el orden SPIN que modelo_spin nombra ya esta expandido dentro.",
403: "A. intimation_illumination cabe entero en wallas_intimacion_fringe_consciousness: notar la sensacion, atenderla, sostenerla, registrarla.",
404: "A. CONTENCION: cash_burn_calculation entero son los pasos 3, 4 y 5 de metrics_that_matter_framework.",
614: "A. CONTENCION: los pasos 2, 8 y 9 de definicion_alineacion_cadena_suministro son LITERALMENTE los pasos 2, 1 y 4 de alineacion_cadena_estrategia_negocio.",
655: "A. filosofia_customer_validation y filosofia_validacion_clientes son el mismo nodo con dos nombres: pedidos reales como evidencia dura y la venta como prueba de hipotesis. QUEMADO.",
723: "A. ciclo_construir_medir_aprender y design_test_repeat: construir o prototipar, medir o testear, aprender, repetir. El mismo ciclo con otras palabras.",
724: "A. voice_of_customer_estrategico y voz_del_cliente_voc: observar en contexto y no quedarse en la encuesta, preguntar el porque. El mismo VoC.",
883: "A. CONTENCION: los 4 pasos de collaborative_transportation_management estan los cuatro en colaboracion_transporte_ctm: socios, hub, nivel de colaboracion, medir.",
885: "A. CONTENCION AL REVES: los pasos 5, 6 y 7 de pensamiento_convergente_divergente contienen LITERALMENTE los pasos 3, 4 y 1 de design_attitude_vs_decision_attitude.",
886: "A. customer_discovery_overview y fit_problema_solucion: comprobar el problema, testear la propuesta, evaluar si el modelo escala. B no trae paso propio.",
908: "A. encontrar_grandes_problemas_mercados_emergentes y resolver_problemas_grandes: los MISMOS cuatro pasos EN EL MISMO ORDEN, mercado, puntos de dolor, capacidades propias, solucion de sistema.",
916: "A. cumplimiento_inversionistas_acreditados y equity_crowdfunding: verificar la acreditacion, las excepciones del JOBS Act, el abogado de valores. Los residuos son lineas.",
976: "A. formalize_advisory_board e identificar_junta_asesores: el mapa de asesores por area y sumar clientes como asesores estan en los dos. QUEMADO por la 4.1 del acta 197.",
1218: "A. sales_operations_planning y sop_colaborativo: ciclo mensual de demanda y oferta, pronosticos, ajuste continuo. El mismo S&OP.",
1807: "A. compra_energia_limpia y energia_fuentes_limpias: convertir residuos en energia y comprar renovable estan en los dos, y los residuos de cada lado son lineas.",
1808: "A. employee_mobilization_sostenibilidad e involucramiento_empleados_sostenibilidad: el mismo nodo, involucrar y reconocer al personal en sostenibilidad.",
1809: "A. critica_eco_eficiencia y menos_malo_vs_bueno: la misma critica, menos malo no es bueno, la metrica de eficiencia optimiza lo equivocado, pasar al rediseno regenerativo. QUEMADO.",
1810: "A. construccion_capacidad_empleados e inversion_capacitacion_sostenibilidad: disenar la capacitacion de sostenibilidad por rol. Residuos de linea. QUEMADO.",
1818: "A. CONTENCION: los 3 pasos de ser_menos_malo_vs_ser_bueno son los pasos 4, 3 y 5 de menos_malo_vs_bueno, y el ultimo palabra por palabra.",
1822: "A. CONTENCION: los 4 pasos de responsabilidad_extendida_productor estan los cuatro en mitigacion_riesgos_ambientales: mapear la cadena, guias a proveedores, verificacion, comunicacion de crisis.",
1824: "A. CONTENCION: los 3 pasos de mensajeria_creativa_positiva estan DENTRO de los pasos 4 y 5 de diseno_mensaje_verde: tono positivo, beneficios practicos, innovacion y progreso.",
1826: "A. unirse_grupo_lideres_climaticos y unirse_organizacion_rsc_ambiental: los mismos cuatro pasos, casi literales.",
1828: "A. CONTENCION: los 4 pasos de neutralidad_carbono son los pasos 6, 4, 2 y 5 de compra_offsets_carbono, uno de ellos palabra por palabra.",
1829: "A. CONTENCION: los 4 pasos de eco_efectividad_re_evolucion_industrial son los pasos 2, 4, 6 y 5 de eco_efectividad_2, uno de ellos palabra por palabra.",
2430: "A. introduccion_lean y lean_manufacturing: mapear, eliminar lo que no agrega valor, sistema pull. La misma introduccion.",
2431: "A. CONTENCION: los pasos 7 y 8 de accion_correctiva_sistematica son LITERALMENTE los pasos 4 y 5 de accion_correctiva_5, y el resto se corresponde uno a uno.",
2432: "A. funcion_perdida_limites_especificacion y funcion_perdida_taguchi: los mismos cinco pasos, reordenados.",
2434: "A. filosofia_zero_defectos y zero_defects_concepto: eliminar el lenguaje del nivel aceptable y comunicar el estandar. El mismo concepto.",
2662: "A. consejo_calidad_2 y consejo_de_calidad_3: conformar el consejo y su funcionamiento periodico. QUEMADO por la 4.2 y la 5.3 del acta 197.",
2663: "A. CONTENCION: los pasos 7 a 11 de consejo_de_calidad son LITERALMENTE los pasos 2, 3 y 4 de consejo_calidad y los pasos 2 y 3 de consejo_calidad_2.",
2664: "A. CONTENCION: los 6 pasos de rol_alta_direccion_benchmarking son LITERALMENTE los pasos 2 a 7 de gestion_efectiva_benchmarking.",
2666: "A. CONTENCION: los pasos 1 y 3 de consumidor_parte_linea_produccion son PALABRA POR PALABRA los pasos 5 y 6 de consumidor_como_eje_de_produccion.",
2668: "A. definiciones_operacionales y definiciones_operacionales_defectos: reunir a los mismos, redactar definiciones sin ambiguedad, difundir y medir. El mismo nodo.",
2838: "A. CONTENCION: analisis_causa_raiz_diagnostico cabe ENTERO en los pasos 1 a 4 de viaje_diagnostico_remedial y NO trae ni un paso propio. Que al largo le sobre el remedio NO lo cambia. QUEMADO.",
2916: "A. CONTENCION: los 4 pasos de consejo_de_calidad_3 caben en consejo_de_calidad, que trae once. QUEMADO.",
2922: "A. control_estadistico_del_proceso y control_estadistico_proceso: cartas de control, eliminar causas especiales, usar el control para innovar. El mismo nodo con dos nombres.",
3076: "A. CONTENCION: los 4 pasos de accion_correctiva_4, reuniones regulares, escalar, formalizar y seguimiento, estan los cuatro dentro de accion_correctiva_sistematica.",
3094: "A. distincion_causas_comunes_especiales_incidentes y responsabilidad_gerencial_causas_comunes: la carta de control para repartir comunes y especiales, y no culpar al individuo. Residuos de linea.",
3095: "A. limites_control_por_juicio_error y limites_de_especificacion_vs_limites_de_control: calcular los limites del proceso y no de la especificacion, y capacitar a supervisores. Residuos de linea.",
3173: "A. autocontrol_planificacion_servicio y autocontrol_y_controlabilidad: las mismas condiciones de autocontrol, saber la meta, saber el desempeno, poder ajustar. QUEMADO.",
1077: "C. LOS DOS POLOS del 9.22, primer polo: PROCEDIMIENTO en los DOS sentidos sobre DOS LINEAS DISTINTAS. El paso 5 de herramientas, paginas segun la fuente del trafico, lo expande diseno_landing_page entera; el paso 4 de landing, demos de menos de un minuto, lo expande herramientas entera. Enlace mutuo, NO fusion. QUEMADO: el banco lo nombra como su ejemplar y el encargo me manda citar el 9.22.",
}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ciega = io.open(os.path.join(LOOP, "SALIDA_V197_T3_CIEGA.txt"),
                    encoding="utf-8").read()
    puestos = [int(x) for x in re.findall(r"^puesto_intra:\s*(\d+)", ciega, re.M)]
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 197, TAREA 3: MIS CLASES SOBRE LOS 240, ESCRITAS ANTES DEL DESTAPE")
    w("=" * 78)
    w("")
    w("LOS PUESTOS SE LEEN DE docs/loop/SALIDA_V197_T3_CIEGA.txt Y NO SE TECLEAN.")
    w("EL DESTAPE, docs/loop/SALIDA_V197_T3_DESTAPE.txt, NO SE HA ABIERTO.")
    w("")
    w("LA VARA, CITADA POR NUMERO Y NO PARAFRASEADA: docs/BANCO_DE_TEXTOS.md 9.6.1,")
    w("LA VARA DE LA RAMA CONTENIDO-MANDA, con sus precisiones 9.6.2 (LA VARA TIENE")
    w("DIRECCION: pregunta que anade el HIJO a la MADRE, nunca al reves) y 9.6.3 (EL")
    w("TAMANO DEL SOLAPE NO DECIDE: se pesa el resto y en que lado), y la tabla de")
    w("LOS DOS POLOS del 9.22: procedimiento en los dos sentidos sobre DOS LINEAS")
    w("DISTINTAS es C con enlace mutuo; linea en los dos sentidos es A con fusion;")
    w("y procedimiento en UN solo sentido es el caso corriente, que continua.")
    w("")
    w("Y CON LOS DOS ERRORES DEL AUDITOR PUESTOS DELANTE, que son los que su cotejo")
    w("midio y no una sospecha:")
    w("  . LA VARA ES EL SUELO Y NO EL TECHO. Antes de aplicarla se pregunta si el")
    w("    par pertenece a una familia con REGLA PROPIA ya fijada. Es la especie del")
    w("    719 (la regla del puesto 595) y la del 976 (el sub-puro 7).")
    w("  . LA CONTENCION SE MIDE SOBRE EL CONTENIDO, NO SOBRE EL CONTENEDOR. Si el")
    w("    corto cabe ENTERO en el largo y no trae ni un paso propio, es A, POR")
    w("    MUCHO QUE al largo le sobre un procedimiento entero. Es la especie del")
    w("    2838, y la aplique en catorce pares que marco como CONTENCION.")
    w("")
    w("LA B NI SE SALTA NI SE SOBRE EMITE, Y AQUI EMITO CERO, CON SU RIESGO DELANTE.")
    w("El sesgo esta medido en las dos direcciones y las dos son perdida. No")
    w("encontre ningun par que se pise sin arista y sin que ninguno nombre al otro.")
    w("SI EL ARCHIVO TRAE ALGUNA B EN ESTOS 240, LA FALLE POR OMISION, y lo escribo")
    w("aqui antes de saberlo.")
    w("")
    w("DOS QUEMADOS QUE NO ESTABAN EN LA LISTA SELLADA DEL SUJETO, Y LOS DECLARO")
    w("IGUAL AUNQUE LLEGAN TARDE, PORQUE CALLARLOS SERIA PEOR:")
    w("  . EL 654. Su clase de archivo me llego por la lista QUEMADOS del fichero")
    w("    scripts/loop/vuelta196_tarea2_relectura_al_doble.py, que lei ENTERO al")
    w("    clonarlo para escribir el sujeto de esta vuelta, o sea ANTES de leer la")
    w("    ciega. Es contaminacion MIA por no comprobar si la lista de quemados de")
    w("    la 196 nombraba puestos de MI universo. Sale del credito.")
    w("  . EL 1077. Es el EJEMPLAR del 9.22 y el banco lo nombra con su clase y con")
    w("    sus dos nodos. El encargo me manda citar el 9.22, asi que LA DOCTRINA QUE")
    w("    ME ORDENAN LEER QUEMA UN PUESTO DE MI PROPIO SUJETO. Sale del credito y")
    w("    va levantado como hallazgo.")
    w("")
    w("| puesto | mi clase | mi razon |")
    w("|---:|:---:|---|")
    n = {"A": 0, "B": 0, "C": 0, "D": 0}
    for p in puestos:
        if p in CLASES_C:
            c = "C"
        elif p in CLASES_B:
            c = "B"
        elif p in CLASES_A:
            c = "A"
        else:
            c = "D"
        n[c] += 1
        w("| %d | %s | %s |" % (p, c, RAZONES.get(p) or RAZON_D))
    w("")
    w("CIFRA pares clasificados: %d" % len(puestos))
    w("MI REPARTO: A %d | B %d | C %d | D %d" % (n["A"], n["B"], n["C"], n["D"]))
    w("")
    w("FIN. Estas clases se commitean ANTES de abrir el destape.")
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V197_T3_MIS_CLASES.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    print("CIFRA pares: %d" % len(puestos))
    print("MI REPARTO: A %d | B %d | C %d | D %d" % (n["A"], n["B"], n["C"], n["D"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
