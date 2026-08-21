# -*- coding: utf-8 -*-
"""_v65_lote_a.py . EL CONTENIDO EDITORIAL DEL LOTE A DEL TRAMO UNICO DE OP-U-02.

NO ES UN INSTRUMENTO: es el texto del lote. La maquina que lo sella es
scripts/loop/generar_plan_del_lote.py, que entra aqui por --contenido _v65_lote_a.

EL LOTE SE DECLARA AL ABRIRLO Y ES PREFIJO SIN SALTOS del orden_universo del
tramo fijado en docs/loop/TRAMO_UNICO_OPU02_V64.jsonl: ACTOS 1 Y 3, que son los
dos primeros de ese orden. El acto 1 CIERRA ENTERO COMO DECLARADO Y NO FUNDIDO
por P.10, medido; el acto 3 CIERRA ENTERO FUNDIDO.

LA FORMA NUEVA DEL REPARTO: los actos de este tramo tienen mas de dos miembros,
asi que el reparto va POR ABSORBIDO en la clave reparto (cambio 7 del docstring
del generador, corregido en esta vuelta con caso positivo de no regresion).
"""

# ======================================================================
# ACTO 3: LA FAMILIA DE LAS CAUSAS COMUNES Y ESPECIALES DE DEMING.
# Superviviente medido por las TRES varas por forma, y las tres a un lado
# (TODAS DE ACUERDO, que funde a su lado): causas_comunes_vs_especiales
# tiene 6 pasos contra un maximo de 5, 3 condiciones contra 2 y cableado
# 14 contra un maximo de 9. Y las razones de archivo lo nombran
# superviviente en 4 de las 5 que nombran a alguno.
# ======================================================================

SUP3 = "causas_comunes_vs_especiales"

MOTIVO3 = (
    "ACTO 3 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LAS CAUSAS COMUNES Y ESPECIALES. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON MEDICION Y NO CON IMPRESION: "
    "los DIEZ miembros salen del MISMO libro (Out of the Crisis, Deming), los 14 pares "
    "internos con veredicto escrito son TODOS de clase A, hay CERO pares D internos y CERO "
    "nodos puente, medido con scripts/loop/vuelta65_puentes_del_tramo.py. P.10 solo detiene "
    "una componente cuando aparece un triangulo A mas A mas D, y aqui no hay ninguno. "
    "SOBREVIVE causas_comunes_vs_especiales POR CONTENIDO, con las TRES varas por forma a "
    "su lado y ninguna en contra (TODAS DE ACUERDO, que funde a su lado): 6 pasos contra un "
    "maximo de 5, 3 condiciones contra 2 y cableado 14 contra un maximo de 9. NO DECIDE EL "
    "ROTULO NI LA CANTIDAD SOLA: decide que es el unico del acto que trae el procedimiento "
    "entero de punta a punta, del dato en orden cronologico a la accion distinta por tipo de "
    "causa, y los otros nueve traen tramos de ese mismo camino o su aplicacion a un sujeto "
    "concreto. NINGUN MIEMBRO DE ESTE ACTO ES PUERTA, medido al sellar. "
    "LO QUE ESTE ACTO SI ESTRENA Y VA MARCADO COMO DISCUTIBLE EN LA SECCION 6 DEL REPORTE DE "
    "ESTA VUELTA: es la PRIMERA fusion de la campana con mas de dos miembros, o sea el primer "
    "uso del reparto POR ABSORBIDO."
)

NOTA3 = (
    "EL REPARTO, Y LAS TRES COSAS QUE SE DICEN EN VEZ DE CALLARSE. "
    "PRIMERA, LOS SOLAPES DECLARADOS PARA LA PODA DE LA FASE 04: dos piezas viajan de APPEND "
    "diciendo casi lo mismo, la de comunicar los hallazgos centrados en el problema y no en "
    "quien lo causo (identificacion_causa_raiz_no_culpa_individual, paso 3) y la de comunicar "
    "a los equipos que el objetivo es identificar problemas y no culpables "
    "(moral_y_sistema_no_individuo, paso 2). Van las dos ENTERAS con el solape DECLARADO, que "
    "es el carril escrito para la pieza mitad propia y mitad ya dicha; la fase 04 poda. Lo "
    "mismo con el eje de la persona: politica_no_culpar_trabajador paso 1 trae de APPEND el "
    "analisis de la distribucion de errores ENTRE PERSONAS con limites de control, y por eso "
    "las piezas de variacion_del_sistema_vs_individuo que dicen ese mismo eje van CUBIERTO con "
    "su perdida nombrada Y CON EL ATENUANTE DICHO. "
    "SEGUNDA, POR QUE HAY TRES INCISOS Y NO SEIS: el paso 4 del superviviente recibe UN inciso "
    "(ayudar al trabajador a identificarla y eliminarla) y NO recibe el segundo que pedia "
    "trampa_del_promedio_como_estandar paso 4 con sus ejemplos de vision y capacitacion, "
    "porque NO SE APILA MAS DE UN INCISO SOBRE EL MISMO PASO (acta 64, pregunta 5, registrada "
    "en esta vuelta): esa pieza va CUBIERTO con la perdida nombrada y enrutada. "
    "TERCERA, LAS ADVERTENCIAS NO SON PASOS (P.11): evitar sanciones, evitar conclusiones "
    "apresuradas, evitar tratar cada defecto como causa especial y dejar de usar el promedio "
    "como linea de corte CALIFICAN el acto y no lo constituyen, asi que van CUBIERTO con la "
    "perdida nombrada en vez de APPEND. "
    "EL SUPERVIVIENTE PASA DE 6 A 15 PASOS Y DE 3 A 10 CONDICIONES, y esa cifra se dice aqui "
    "porque es la mas alta de la campana y es consecuencia de fundir DIEZ nodos, no de repartir "
    "mal: 16 piezas viajan enteras, 39 estaban ya dichas y 3 van de inciso."
)

PERDIDAS3 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("la instruccion explicita de NO INFORMAR SOBRE DEFECTOS INDIVIDUALES cuando el "
             "proceso esta en control estadistico. El paso 5 del superviviente manda listar las "
             "causas comunes y asumir la responsabilidad sobre ellas, que es enfocar el esfuerzo "
             "en el sistema, pero NO dice que haya que dejar de reportar el defecto de cada uno"),
     "donde": "paso 2 de distincion_causas_comunes_especiales",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("la prohibicion explicita de SANCIONAR AL TRABAJADOR por fallas atribuibles al "
             "sistema. SE DICE LO QUE NO SE PIERDE: la condicion 1 del superviviente ya dispara "
             "cuando estas por culparte a ti o a alguien sin verificar si es del sistema, y el "
             "paso de rediseñar el proceso en lugar de sancionar al individuo VIAJA ENTERO de "
             "APPEND desde distincion_causas_comunes_especiales_incidentes"),
     "donde": "paso 4 de distincion_causas_comunes_especiales",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que la accion para las causas comunes sea UN CAMBIO ESTRUCTURAL DEL SISTEMA y no "
             "el rastreo caso por caso. El paso 6 del superviviente manda definir una accion "
             "distinta para cada tipo de causa pero NO dice cual es la de las comunes"),
     "donde": "paso 4 de distincion_causas_comunes_especiales_2",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("que el disparador incluya ACCIDENTES, FALLAS O RESULTADOS DESFAVORABLES "
             "RECURRENTES. La condicion 2 del superviviente nombra indicadores de desempeño, "
             "ventas, calidad o quejas, y ninguna de las cuatro es un accidente"),
     "donde": "condicion 1 de distincion_causas_comunes_especiales_incidentes",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("la remision al CAPITULO 11 de la fuente como el metodo estadistico con el que se "
             "decide si una intervencion es necesaria. El paso 3 del superviviente manda aplicar "
             "reglas simples y las nombra, pero no remite a ese capitulo"),
     "donde": "paso 4 de distincion_causas_especiales_comunes",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador del CONFLICTO INTERNO YA INSTALADO por errores o tasas de rechazo, "
             "que no es el momento de culpar sino el estado que deja el haber culpado. "
             "ATENUANTE DECLARADO, y se dice para que la perdida se pueda pesar: la condicion 1 "
             "de identificacion_causa_raiz_no_culpa_individual viaja ENTERA de APPEND y nombra "
             "el conflicto interno y la baja moral"),
     "donde": "condicion 1 de moral_y_sistema_no_individuo",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("que el disparador sea LA MORAL DEL EQUIPO YA AFECTADA por señalamientos de culpa. "
             "ATENUANTE DECLARADO: la condicion 1 de identificacion_causa_raiz_no_culpa_individual "
             "viaja entera de APPEND y nombra la baja moral por atribucion de culpas"),
     "donde": "condicion 2 de moral_y_sistema_no_individuo",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que el punto que excede el limite superior sea UNA PERSONA y que antes de actuar "
             "se investigue SU CONTEXTO. El paso 3 del superviviente detecta posibles causas "
             "especiales con reglas sobre los puntos, y el paso 4 manda investigar la señal, "
             "pero ninguno de los dos dice que el punto pueda ser alguien ni manda mirar su "
             "contexto antes de actuar"),
     "donde": "paso 2 de politica_no_culpar_trabajador",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("la prohibicion de las SANCIONES UNIFORMES Y LOS MENSAJES ESTANDAR para todos los "
             "niveles de error. El paso 6 del superviviente manda definir una accion distinta "
             "para cada tipo de causa, que es la forma positiva de lo mismo, pero no prohibe la "
             "respuesta uniforme"),
     "donde": "paso 3 de politica_no_culpar_trabajador",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL PROMEDIO SIMPLE COMO LINEA DE CORTE, nombrado como el error que se abandona. "
             "El paso 2 del superviviente manda construir el grafico con limites calculados "
             "estadisticamente, que es lo que sustituye al promedio, pero NO nombra al promedio "
             "ni dice que dejarlo es el punto. Es el titulo entero del nodo que muere"),
     "donde": "paso 1 de trampa_del_promedio_como_estandar",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("los ejemplos concretos de causa especial, PROBLEMAS DE VISION O DE CAPACITACION, "
             "que es lo que convierte la busqueda en algo que se puede hacer. NO SE ADOSA DE "
             "INCISO Y SE DICE POR QUE: el paso 4 del superviviente YA recibe el inciso del paso "
             "3 de distincion_causas_comunes_especiales, y no se apila mas de un INCISO sobre el "
             "mismo paso (acta 64, pregunta 5)"),
     "donde": "paso 4 de trampa_del_promedio_como_estandar",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que los datos sean DE UN GRUPO DE PERSONAS QUE HACEN UN TRABAJO SIMILAR. El paso 1 "
             "del superviviente recopila los datos DEL PROCESO. ATENUANTE DECLARADO: el paso 1 "
             "de politica_no_culpar_trabajador viaja ENTERO de APPEND y analiza la distribucion "
             "de errores ENTRE TODAS LAS PERSONAS con limites de control"),
     "donde": "paso 1 de variacion_del_sistema_vs_individuo",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que el caer fuera de los limites cuente TAMBIEN PARA BIEN y no solo para mal, que "
             "es lo que impide leer el grafico como una lista de culpables. El paso 3 del "
             "superviviente detecta posibles causas especiales sin decir que el punto alto "
             "tambien es una señal que se investiga"),
     "donde": "paso 3 de variacion_del_sistema_vs_individuo",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
]

REPARTO3 = {
    # ---------------------------------------------------------------
    "distincion_causas_comunes_especiales": {
        "pasos": {
            # determinar si esta en control con graficos de control = S2 mas S3
            "1": ("CUBIERTO", 2),
            # no informar defectos individuales; enfocar en el sistema = S5, con perdida
            "2": ("CUBIERTO", 5),
            # ayudar al trabajador a identificarla y eliminarla: parametro concreto de S4
            "3": ("INCISO", 4, "ayudar al trabajador a identificarla y eliminarla", ", y "),
            # evitar sanciones: ADVERTENCIA (P.11), va CUBIERTO con perdida
            "4": ("CUBIERTO", 5),
        },
        "condiciones": {
            "1": ("APPEND",),          # evaluar el desempeño individual de un trabajador
            "2": ("CUBIERTO", 3),      # decidir si corregir al individuo o al sistema = C3
        },
    },
    # ---------------------------------------------------------------
    "distincion_causas_comunes_especiales_2": {
        "pasos": {
            "1": ("CUBIERTO", 2),
            "2": ("CUBIERTO", 5),
            "3": ("CUBIERTO", 3),      # advertencia (P.11)
            "4": ("CUBIERTO", 6),      # con perdida: el cambio ESTRUCTURAL
        },
        "condiciones": {
            "1": ("CUBIERTO", 3),
            "2": ("APPEND",),          # el nivel de defectos que no baja pese a corregir caso a caso
        },
    },
    # ---------------------------------------------------------------
    "distincion_causas_comunes_especiales_incidentes": {
        "pasos": {
            # el sujeto de los datos: incidentes o accidentes, parametro de S1
            "1": ("INCISO", 1, "de incidentes o accidentes", ", incluidos los "),
            "2": ("CUBIERTO", 3),
            # evitar conclusiones apresuradas por negligencia individual = la CONDICION 1
            "3": ("CUBIERTO_COND", 1),
            # rediseñar el proceso en lugar de sancionar: GESTO DISTINTO, viaja entero
            "4": ("APPEND",),
            # la proporcion sistemicas contra especiales: parametro de S6
            "5": ("INCISO", 6, "la proporcion estimada de causas sistemicas vs especiales",
                  ", incluida "),
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),      # con perdida: accidentes y fallas recurrentes
            "2": ("CUBIERTO", 1),
        },
    },
    # ---------------------------------------------------------------
    "distincion_causas_especiales_comunes": {
        "pasos": {
            "1": ("CUBIERTO", 2),
            # rastrear causas periodicas o recurrentes por estudio de registros: GESTO DISTINTO
            "2": ("APPEND",),
            "3": ("CUBIERTO", 3),      # advertencia (P.11)
            "4": ("CUBIERTO", 3),      # con perdida: la remision al capitulo 11
        },
        "condiciones": {
            "1": ("CUBIERTO", 3),
            "2": ("CUBIERTO", 1),
        },
    },
    # ---------------------------------------------------------------
    "identificacion_causa_raiz_no_culpa_individual": {
        "pasos": {
            # registros estratificados por turno, maquina, operador y departamento: GESTO DISTINTO
            "1": ("APPEND",),
            "2": ("CUBIERTO", 3),
            # comunicar los hallazgos centrados en el problema: GESTO DISTINTO
            "3": ("APPEND",),
            "4": ("CUBIERTO", 6),
            # seguimiento a la moral y a la tasa de errores tras el cambio: GESTO DISTINTO
            "5": ("APPEND",),
        },
        "condiciones": {
            "1": ("APPEND",),          # conflicto interno o baja moral por atribucion de culpas
            "2": ("CUBIERTO", 3),
        },
    },
    # ---------------------------------------------------------------
    "moral_y_sistema_no_individuo": {
        "pasos": {
            "1": ("CUBIERTO", 2),
            "2": ("APPEND",),          # comunicar el objetivo a los equipos (solape declarado)
            "3": ("APPEND",),          # seguimiento Y APOYO a quienes caen fuera
            "4": ("APPEND",),          # colaboracion entre turnos y departamentos
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),      # con perdida y atenuante
            "2": ("CUBIERTO", 1),      # con perdida y atenuante
        },
    },
    # ---------------------------------------------------------------
    "politica_no_culpar_trabajador": {
        "pasos": {
            # la distribucion de errores ENTRE PERSONAS con limites de control: GESTO DISTINTO
            "1": ("APPEND",),
            "2": ("CUBIERTO", 3),      # con perdida: la persona y su contexto
            "3": ("CUBIERTO", 6),      # con perdida: la prohibicion de la respuesta uniforme
            "4": ("CUBIERTO", 5),
            "5": ("CUBIERTO", 6),
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),
            "2": ("APPEND",),          # alta rotacion o desmotivacion por politicas injustas
        },
    },
    # ---------------------------------------------------------------
    "trampa_del_promedio_como_estandar": {
        "pasos": {
            "1": ("CUBIERTO", 2),      # advertencia (P.11), con perdida: EL PROMEDIO nombrado
            "2": ("CUBIERTO", 2),
            "3": ("CUBIERTO", 3),
            "4": ("CUBIERTO", 4),      # con perdida: los ejemplos, y por que NO va de inciso
        },
        "condiciones": {
            "1": ("APPEND",),          # el promedio del grupo como criterio para intervenir
            "2": ("APPEND",),          # la persona señalada que cambia cada semana sin mejora
        },
    },
    # ---------------------------------------------------------------
    "variacion_del_sistema_vs_individuo": {
        "pasos": {
            "1": ("CUBIERTO", 1),      # con perdida y atenuante: el grupo de personas
            "2": ("CUBIERTO", 2),
            "3": ("CUBIERTO", 3),      # con perdida: fuera de limite TAMBIEN PARA BIEN
            "4": ("CUBIERTO", 5),
            "5": ("CUBIERTO", 4),
        },
        "condiciones": {
            "1": ("APPEND",),          # si las diferencias entre personas son reales o azar
            "2": ("CUBIERTO", 1),
        },
    },
}

# ======================================================================
# ACTO 1: DECLARADO Y NO FUNDIDO POR P.10. No lleva reparto porque no se
# funde: lleva motivo sellado y medicion.
# ======================================================================

DECLARADO_ACTO1 = {
    "acto": 1,
    "miembros": [
        "cultura_de_seguridad_interpretivista_funcionalista",
        "enfoque_situacional_vs_personal",
        "error_humano_vs_falla_mecanica",
        "errores_como_consecuencia",
        "falla_sistemica_vs_error_individual",
        "fallas_activas_condiciones_latentes",
        "human_error_como_sintoma",
        "new_view_human_error",
        "new_view_vs_old_view",
        "nueva_vision_organizacion_linea_seguridad",
        "old_view_vs_new_view_human_error",
        "preguntar_que_no_quien",
        "riesgos_del_enfoque_en_error_humano",
        "seduccion_modelo_persona",
        "vieja_vision_vs_nueva_vision_seguridad",
    ],
    "superviviente_que_el_contenido_elige": (
        "NINGUNO SE ELIGE, Y ESA ES LA DECISION. No se elige superviviente porque el acto no "
        "se funde: elegirlo seria decidir la fusion y dejarla a medias."
    ),
    "motivo": (
        "DECLARADO Y NO FUNDIDO POR P.10, LA MITAD DIAGNOSTICA DE P.5, Y LA MEDICION VA DELANTE "
        "DE LA DECISION. P.10 dice con todas sus letras que UN NODO PUENTE es el que tiene A con "
        "dos nodos que entre si son D, que la componente que forma puede ser UNA familia o DOS "
        "pegadas por el, que el cierre transitivo no lo distingue porque no lee sino que cuenta, "
        "y que SI APARECE, LA COMPONENTE NO SE FUNDE HASTA QUE ESE TRIANGULO SE CIERRE. "
        "MEDIDO EN ESTA VUELTA con scripts/loop/vuelta65_puentes_del_tramo.py sobre el acto "
        "entero, con los ids pasados por el resolutor (P.1): 15 miembros, 105 combinaciones, 20 "
        "pares A, DIEZ pares D internos ya leidos y declarados DISTINTOS, TRES NODOS PUENTE y "
        "SEIS TRIANGULOS PUENTE. errores_como_consecuencia hace de puente en cuatro (contra "
        "error_humano_vs_falla_mecanica y falla_sistemica_vs_error_individual, que son D en el "
        "puesto 2403; contra new_view_human_error y riesgos_del_enfoque_en_error_humano, D en el "
        "2299; contra new_view_human_error y seduccion_modelo_persona, D en el 2331; y contra "
        "riesgos_del_enfoque_en_error_humano y seduccion_modelo_persona, D en el 2228). "
        "human_error_como_sintoma hace de puente en uno (el 2403) y "
        "vieja_vision_vs_nueva_vision_seguridad en uno (new_view_human_error contra "
        "new_view_vs_old_view, D en el puesto 2220). "
        "FUNDIR LA COMPONENTE ENTERA DESMENTIRIA DIEZ LECTURAS QUE YA ESTAN ESCRITAS, y P.10 "
        "llama a eso exactamente lo que nunca es salida. "
        "Y HAY UNA SEGUNDA RAZON INDEPENDIENTE, TAMBIEN MEDIDA, que sola bastaria: DOS de los 15 "
        "miembros son PUERTA con la marca TIENE QUE SOBREVIVIR, enfoque_situacional_vs_personal y "
        "fallas_activas_condiciones_latentes, leidas de la salida del dossier. La GUARDA 1B dice "
        "que un nodo que es semilla de entrada o extremo de puente aprobado NO SE ABSORBE, y una "
        "fusion a un solo superviviente tendria que absorber una de las dos. "
        "LAS TRES SALIDAS DE P.10, RECORRIDAS UNA A UNA EN VEZ DE ELEGIR LA COMODA: leer el par "
        "que falta es la unica que resuelve de verdad, y quedan 75 combinaciones sin veredicto "
        "escrito, que es trabajo de cribado y no de esta operacion; releer contra el superviviente "
        "no aplica, porque aqui no hay superviviente elegido ni nodo que vaya a cambiar; y fundir "
        "solo el subconjunto CERRADO y enlazar el resto pide que TODAS las lecturas esten hechas, "
        "y no lo estan. ASI QUE NO SE FUNDE NADA Y SE DECLARA, que es lo que la letra deja. "
        "EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se deprecia ninguno y no se "
        "elige superviviente. VA MARCADO COMO DISCUTIBLE EN LA SECCION 6 DEL REPORTE DE ESTA "
        "VUELTA, porque es la primera vez que la campana declara un acto por P.10 y porque el "
        "primer acto del prefijo del tramo unico se cierra sin fundir."
    ),
    "medicion": {
        "instrumento": "scripts/loop/vuelta65_puentes_del_tramo.py",
        "salida": "docs/loop/SALIDA_V65_PUENTES_TRAMO.txt",
        "dossier": "docs/loop/SALIDA_V65_DOSSIER_ACTO1.txt",
        "miembros": 15,
        "combinaciones": 105,
        "pares_A": 20,
        "pares_D": 10,
        "pares_sin_veredicto": 75,
        "nodos_puente": 3,
        "triangulos_puente": 6,
        "puertas_dentro": ["enfoque_situacional_vs_personal", "fallas_activas_condiciones_latentes"],
    },
}

LOTE_A = {
    "titulo": ("LOTE A DEL TRAMO UNICO DE OP-U-02, PREFIJO SIN SALTOS DEL orden_universo: "
               "LOS ACTOS 1 Y 3. El 1 cierra DECLARADO Y NO FUNDIDO por P.10 y el 3 cierra "
               "FUNDIDO, y es la PRIMERA fusion de mas de dos miembros de la campana"),
    "actos": [
        {
            "orden": 3,
            "superviviente": SUP3,
            "motivo": MOTIVO3,
            "nota": NOTA3,
            "reparto": REPARTO3,
            "perdidas": PERDIDAS3,
        },
    ],
    "declarados": [DECLARADO_ACTO1],
}
