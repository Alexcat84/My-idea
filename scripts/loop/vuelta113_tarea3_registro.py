# -*- coding: utf-8 -*-
"""vuelta113_tarea3_registro.py . Escribe docs/plan/OP_E_03_LECTURA_V113_REGISTRO.jsonl,
el registro de las 29 lecturas de la TAREA 3 de la vuelta 113 (8 territorio
viejo + 21 territorio nuevo, techo sellado en
docs/loop/SALIDA_V113_TAREA3_1_CENSO_29.txt). Cosecha CERO: los 29 pares
leidos contra el grafo (los dos nodos, mas banco 9.6.1/9.6.2/9.6.3) confirman
NO RESUELTA. Ninguno se mueve, asi que ninguna fila de
docs/plan/OP_E_03_LECTURA_TRAMO*.jsonl se toca: la decision vive solo en este
registro, no en una correccion_v113 sobre el dato (que solo hace falta
cuando un par SI se mueve).
"""
import io
import json

DECISIONES = [
    (168, "formalizar_junta_asesora", "tamano_junta_directiva_vc",
     "leido dataset/nodos/formalizar_junta_asesora.json y tamano_junta_directiva_vc.json enteros: "
     "junta ASESORA (advisors sin voto) contra junta DIRECTIVA con VCs (board con voto y control), "
     "organos de gobierno distintos. Falso amigo por 'junta'. Banco 9.6.2 primer brazo: NO SE CUMPLE."),
    (170, "rol_director_calidad", "circulos_calidad_qc",
     "leido dataset/nodos/rol_director_calidad.json entero: el paso 4 ('actuar como asesor "
     "estrategico en las decisiones de calidad') es un rol generico; circulos_calidad_qc es una "
     "tecnica participativa especifica y distinta. Banco 9.6.2 primer brazo: NO SE CUMPLE."),
    (171, "canales_distribucion", "ocho_fases_experiencia_cliente",
     "paso 3 de la madre (integracion de canales, Osterwalder) contra framework de OCHO FASES de "
     "Coleman: autores y objetos distintos. Falso amigo por 'experiencia de cliente'. "
     "Banco 9.6.2 primer brazo: NO SE CUMPLE."),
    (173, "establecer_diseno_final_producto", "establecer_metas_caracteristicas",
     "paso 1 de gobernanza/cierre contra hijo de planificacion TEMPRANA (fijar metas): orden "
     "logico invertido, el hijo precede a la madre, no la ejecuta. NO SE CUMPLE."),
    (176, "constraint_management", "caso_estudio_benchmarking_terminal",
     "paso 4 (principio generico de TOC) contra caso de estudio con metodologia de benchmarking "
     "distinta (costos, rediseno organizacional, mantenimiento por riesgo). NO SE CUMPLE."),
    (178, "ingenieria_calidad_proveedores", "desarrollar_estrategias_largo_plazo",
     "paso 4 (relaciones de largo plazo con PROVEEDORES) contra ejercicio de estrategia general "
     "del negocio (FODA, 5 areas) sin relacion con proveedores. Falso amigo 'largo plazo'/"
     "'estrategias'. NO SE CUMPLE."),
    (181, "valor_intangible_sostenibilidad", "alineacion_engagement_estrategia_general",
     "paso 1 (metricas de sostenibilidad, medicion) contra practica de cultura/liderazgo (alinear "
     "equipo, elegir lideres). Falso amigo 'engagement'. NO SE CUMPLE."),
    (183, "no_shop_agreement", "dividends_terms",
     "leido dataset/nodos/no_shop_agreement.json y dividends_terms.json enteros: clausula de "
     "exclusividad contra clausula de dividendos, mismo term sheet (Venture Deals) sin ninguna "
     "accion compartida. Emparejamiento mas debil del tramo. NO SE CUMPLE."),
    (6, "issue_spotting_ambiental", "triple_bottom_line_2",
     "correccion_v104 confirmada: paso 2 es una DECISION de alcance (ambiental o tambien social), "
     "no un procedimiento de deteccion social; los tres pasos del hijo (social) no aparecen en "
     "ningun paso de la madre (ambiental). 9.6.3 procedimiento en los dos lados: SANO."),
    (8, "analisis_de_sistemas_de_medicion_msa", "capacidad_de_proceso_2",
     "correccion_v104 confirmada: 'capacidad de proceso' no aparece en el paso 3 (control "
     "estadistico del SISTEMA DE MEDICION); el hijo es capacidad del PROCESO DE PRODUCCION, "
     "topico distinto. Entregables distintos. 9.6.3: SANO."),
    (20, "waterfall_vs_agile_development", "modelo_customer_development",
     "correccion_v105 confirmada: el paso 3 pide COORDINACION (alinear procesos), no ejecutar los "
     "cinco pasos internos del modelo; ya existe el par 13 que si despliega la alineacion. "
     "Entregables distintos (decision metodologica vs estado del proceso CD)."),
    (21, "build_measure_learn", "value_proposition_canvas",
     "correccion_v105 confirmada: el paso 0 usa el VPC como INSUMO ya construido para generar una "
     "hipotesis; el hijo describe COMO construir ese insumo, no el acto de generar la hipotesis. "
     "Entregables distintos (ciclo completo vs canvas mapeado)."),
    (24, "preparacion_preguntas_problema_precall", "preguntas_situacion",
     "correccion_v104 confirmada: el objeto del paso 4 son las preguntas de PROBLEMA (tema entero "
     "de la madre); 'preguntas de situacion' vive en una subordinada de finalidad. Entregables "
     "distintos. 9.6.3: SANO."),
    (25, "histograma_calidad", "capacidad_del_proceso",
     "correccion_v104 confirmada: 'capacidad del proceso' vive en subordinada de finalidad; ademas "
     "metodo distinto (lectura visual de histograma vs formulas de control estadistico). "
     "9.6.3: SANO."),
    (28, "timing_solicitud_referidos", "fase_adopt_ciclo_cliente",
     "correccion_v103 confirmada: 'fase Adopt' es ejemplo parentetico de CUANDO comunicar el "
     "programa, no el objeto del imperativo; los 4 pasos del hijo no comunican ningun programa de "
     "referidos. 9.6.3: SANO."),
    (29, "abolir_inspeccion_masiva", "control_estadistico_del_proceso",
     "correccion_v104 confirmada: 'control estadistico' vive en subordinada de CUANDO ('a medida "
     "que'); el objeto del paso 5 es 'la inspeccion masiva'. Contra-caso de entregables (patron "
     "2.215) examinado y rechazado: un solo plan, no dos productos. 9.6.3: SANO."),
    (31, "control_estadistico_del_proceso", "causas_comunes_vs_especiales",
     "leido dataset/nodos/control_estadistico_del_proceso.json y causas_comunes_vs_especiales.json "
     "enteros: 9 de 15 pasos del hijo son territorio de CULTURA/MORAL/COMUNICACION SIN CULPA, "
     "ausente de los 7 pasos de la madre. Exceso de genero confirmado por lectura directa."),
    (38, "obtencion_compromiso", "enfoque_etapa_investigacion",
     "correccion_v105 confirmada: el paso 4 nombra DOS etapas (investigacion Y demostracion); el "
     "hijo cubre solo investigacion y argumenta explicitamente que la demostracion no necesita "
     "esfuerzo propio, lo contrario del paso."),
    (40, "analisis_valor", "customer_needs_spreadsheet",
     "correccion_v103 confirmada: el paso 1 cruza COSTOS con necesidades; el hijo cruza CLIENTES "
     "con necesidades, sin costo en ningun paso. La salvedad ya declarada en la razon original ES "
     "la falla del primer brazo del 9.6.2."),
    (52, "posicionamiento_por_tipo_de_mercado", "resegmentacion_mercado_nicho_bajo_costo",
     "correccion_v104 confirmada: el paso 5 es una rama condicional ('Si es re-segmentacion') "
     "cuyo imperativo es 'comunicar'; los 6 pasos del hijo son la metodologia entera, exceden "
     "ampliamente ese verbo. 9.6.3: SANO."),
    (62, "preservar_efectivo_buscar_modelo", "validar_modelo_negocio_hechos",
     "correccion_v104 confirmada: 'validar el modelo con hechos' vive en subordinada temporal "
     "('hasta'); el objeto del paso 1 es 'no contrates equipo de ventas ni marketing'. Entregables "
     "distintos (plan de gasto vs canvas actualizado)."),
    (66, "cultura_justa_3", "cultura_de_aprendizaje",
     "correccion_v105 confirmada: el paso 3 pide BALANCEAR accountability CON aprendizaje; el "
     "hijo desarrolla solo el lado de aprendizaje, cero lineas sobre accountability. Los dos nodos "
     "son componentes PARES del modelo de Reason, no madre e hijo."),
    (80, "estudio_desempeno_run_charts_servicios", "causas_comunes_vs_especiales",
     "correccion_v104 confirmada: mismo hijo que el par 31 (ya movido por exceso de genero); aqui "
     "el paso 3 solo nombra 'especiales' en subordinada de finalidad, el hijo cubre ambas clases "
     "mas cultura, que la madre no toca en ningun paso."),
    (93, "estandares_voluntarios", "definiciones_operacionales_de_calidad",
     "correccion_v105 confirmada: el paso 3 documenta un estandar de INDUSTRIA por consenso de "
     "comites; el hijo es un acuerdo BILATERAL cliente-proveedor con cartas compartidas de forma "
     "continua, escala y proceso de formacion distintos. 9.6.3: raiz comun, SANO."),
    (147, "clasificacion_benchmarking", "consortium_benchmarking",
     "correccion_v99 confirmada, leido dataset/nodos/clasificacion_benchmarking.json entero: el "
     "paso 2 (decidir tipo de participantes) es una DECISION; los pasos 2 a 5 del hijo son diseno "
     "y ejecucion aguas abajo de esa decision, exceden lo que el paso 2 decide."),
    (161, "seis_herramientas_comunicacion_celebracion", "celebracion_automatizada_de_hitos",
     "correccion_v100 confirmada: automatizacion de deteccion del hito y oferta de upsell no estan "
     "en ningun paso de la madre (evaluar canal, disenar mensaje, personalizar, elegir momento, "
     "medir reaccion). Exceso de genero."),
    (172, "desarrollo_en_espiral", "protocepto",
     "correccion_v100 confirmada: el hijo tiene 4 pasos que exceden el paso 1 de la madre (pasos "
     "2 y 4 del hijo son en realidad los pasos 2 y 5 de la madre); la afirmacion original de que "
     "los otros pasos de la madre 'quedan sin tocar' no se sostiene."),
    (174, "desarrollo_value_proposition_usp", "posicionamiento_vs_competidores",
     "correccion_v100 confirmada: 3 de 4 pasos del hijo son movimientos de una CONVERSACION DE "
     "VENTA con un candidato a franquiciado, no la IDENTIFICACION que pide el paso 1 de la madre. "
     "Aplicar un analisis no es ejecutarlo."),
    (175, "validar_modelo_financiero", "valor_de_vida_del_cliente",
     "correccion_v100 confirmada: solo el primer paso del hijo calcula (lo que pide el paso 2 de "
     "la madre); los otros tres son intervencion operativa (subir el LTV) que la madre no "
     "contempla en ningun paso. Prueba lexica descartada por el propio 9.6.2."),
]


def main():
    ruta = "docs/plan/OP_E_03_LECTURA_V113_REGISTRO.jsonl"
    with io.open(ruta, "w", encoding="utf-8") as f:
        for puesto, madre, hijo, nota in DECISIONES:
            fila = {
                "puesto_tramo": puesto,
                "madre_de_la_bolsa": madre,
                "hijo_de_la_bolsa": hijo,
                "operacion": "OP-E-03",
                "vuelta": 113,
                "decision": "NO_SE_MUEVE",
                "direccion_leida_final": None,
                "vara": "banco 9.6.1 (mayoria/contenido), 9.6.2 (direccion, test de reconocimiento, senal de entregables), 9.6.3 (el solape no decide)",
                "nota": nota,
            }
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")
    print("escrito %s con %d filas" % (ruta, len(DECISIONES)))
    assert len(DECISIONES) == 29, "el techo declarado es 29, no %d" % len(DECISIONES)
    print("techo 29 verificado: CUADRA")


if __name__ == "__main__":
    main()
