# -*- coding: utf-8 -*-
"""_v66_lote_b.py . EL CONTENIDO EDITORIAL DEL LOTE B DEL TRAMO UNICO DE OP-U-02.

NO ES UN INSTRUMENTO: es el texto del lote. La maquina que lo sella es
scripts/loop/generar_plan_del_lote.py, que entra aqui por --contenido _v66_lote_b.

EL LOTE SE DECLARA AL ABRIRLO Y ES PREFIJO SIN SALTOS del orden_universo de lo
que queda del tramo fijado en docs/loop/TRAMO_UNICO_OPU02_V64.jsonl (el lote A de
la vuelta 65 cerro los actos 1 y 3): ACTOS 5, 7, 8, 9, 10 Y 11, que son los SEIS
primeros de ese orden, 37 nodos. TRES CIERRAN FUNDIDOS (7, 8 y 9) y TRES CIERRAN
DECLARADOS Y NO FUNDIDOS con motivo sellado (5, 10 y 11). Los seis cierran
ENTEROS en esta vuelta.

EL REPARTO VA POR ABSORBIDO en la clave reparto, que es la forma que la vuelta 65
estreno para los actos de mas de dos miembros.
"""

# ======================================================================
# ACTO 7: LA FAMILIA DEL DMAIC Y LA SECUENCIA UNIVERSAL DE JURAN.
# SEIS miembros, TODOS del mismo libro (Juran's Quality Handbook), SIETE
# pares internos con veredicto y los SIETE en A, CERO D y CERO puentes.
# FORMA medida: CONTENIDO EMPATA (pasos empatan en 6 a tres bandas y
# condiciones empatan en 3 a dos bandas), asi que DECIDE EL CABLEADO SOLO
# por P.8, y el cableado apunta a six_sigma_dmaic con 11 contra un maximo
# de 5 en los demas.
# ======================================================================

SUP7 = "six_sigma_dmaic"

MOTIVO7 = (
    "ACTO 7 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DEL DMAIC Y LA SECUENCIA UNIVERSAL DE "
    "JURAN. UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON MEDICION Y NO CON "
    "IMPRESION: los SEIS miembros salen del MISMO libro (Juran's Quality Handbook, Defeo), "
    "los SIETE pares internos con veredicto escrito son TODOS de clase A, hay CERO pares D "
    "internos y CERO nodos puente, medido con scripts/loop/vuelta65_puentes_del_tramo.py "
    "sobre el estado del dia (6 miembros, 15 combinaciones, 7 A, 0 D, 8 sin veredicto, 0 "
    "puentes, 0 triangulos). P.10 solo detiene una componente cuando aparece un triangulo A "
    "mas A mas D, y aqui no hay ninguno. Y LAS RAZONES YA NOMBRAN AL SUPERVIVIENTE DOS "
    "VECES: el puesto 2548 cierra en 'Sobrevive six_sigma_dmaic' y el 2618 tambien, y el "
    "2887 declara la identidad BREAKTHROUGH IGUAL DMAIC con la correspondencia paso a paso "
    "escrita (nominar y proyecto igual Definir, viaje diagnostico igual Medir y Analizar, "
    "viaje remedial igual Mejorar, controles igual Controlar). "
    "SOBREVIVE six_sigma_dmaic, Y LA VARA QUE LO ELIGE ES EL CABLEADO SOLO, POR P.8, CON SU "
    "LETRA: la FORMA medida del acto es CONTENIDO EMPATA "
    "(scripts/loop/varas_n_arias_del_tramo.py, docs/loop/SALIDA_V66_VARAS_N_ARIAS.txt), "
    "porque la vara de PASOS empata en 6 entre secuencia_universal_breakthrough, "
    "secuencia_universal_para_el_breakthrough y six_sigma_dmaic, y la de CONDICIONES empata "
    "en 3 entre six_sigma_dmaic y six_sigma_dmaic_2. NINGUNA VARA DE CONTENIDO SEPARA, y la "
    "receta escrita dice que entonces DECIDE EL CABLEADO SOLO: 11 contra un maximo de 5. "
    "NO DECIDE EL ROTULO NI LA CANTIDAD SOLA. "
    "NINGUN MIEMBRO DE ESTE ACTO ES PUERTA, medido al sellar: la guarda 1B pasa por vacio y "
    "se dice en vez de darla por buena."
)

NOTA7 = (
    "EL REPARTO, Y LAS TRES COSAS QUE SE DICEN EN VEZ DE CALLARSE. "
    "PRIMERA, POR QUE LA SECUENCIA UNIVERSAL APORTA SEIS PASOS DE APPEND Y EL DMAIC NO LOS "
    "TENIA: la identidad que las razones declaran es de VIAJE (definir, medir, analizar, "
    "mejorar, controlar), no de ANDAMIAJE. secuencia_universal_breakthrough trae cuatro "
    "gestos que el DMAIC no dice en ninguno de sus seis pasos y que un dueno puede ejecutar: "
    "establecer la creencia de que el cambio es deseable y factible, el estudio de "
    "factibilidad CON ANALISIS DE PARETO para separar los pocos vitales, la creacion de un "
    "brazo directivo y uno diagnostico, y la evaluacion del impacto cultural con la gestion "
    "de la resistencia. secuencia_universal_para_el_breakthrough trae otros dos: establecer "
    "un proyecto formal con equipo asignado, y REPLICAR los resultados exitosos nominando "
    "nuevos proyectos, que es lo unico del acto que cierra el bucle hacia el siguiente "
    "proyecto. Los seis viajan ENTEROS de APPEND por la politica escrita, y la fase 04 poda. "
    "SEGUNDA, POR QUE NO HAY NI UN SOLO INCISO EN ESTE ACTO, Y NO ES PEREZA: el criterio "
    "escrito de la politica del INCISO es LA LEGIBILIDAD DEL PASO RESULTANTE, y LOS SEIS "
    "PASOS DE six_sigma_dmaic TERMINAN EN PUNTO (leidos del nodo al sellar). Un inciso "
    "adosado detras de un punto no se lee limpio en ninguno de los seis, asi que todas las "
    "piezas que son PARAMETRO CONCRETO de un gesto que el superviviente ya tiene van "
    "CUBIERTO con la perdida NOMBRADA Y ENRUTADA, que es la otra mitad del mismo carril. "
    "TERCERA, LAS DOS PERDIDAS QUE LLEVAN ATENUANTE DECLARADO Y POR QUE SE DICEN IGUAL: la "
    "condicion 1 de secuencia_universal_para_el_breakthrough (mejora significativa y no "
    "incremental) y la 3 de six_sigma_dmaic_2 (mejora de tipo breakthrough) van CUBIERTO con "
    "perdida, Y SE DICE QUE EL CONTENIDO LLEGA IGUAL: la condicion 1 de "
    "secuencia_universal_breakthrough viaja ENTERA de APPEND y dice literalmente cambio "
    "radical de desempeno, no solo mejora incremental. Sellar la perdida con el atenuante "
    "dicho es mas auditable que callarla (acta 63, D8, y acta 65, D10). "
    "EL SUPERVIVIENTE PASA DE 6 A 12 PASOS Y DE 3 A 8 CONDICIONES."
)

PERDIDAS7 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL APOYO DE QUIEN TE ASESORE al definir el problema, que es lo unico del acto "
             "que mete a un tercero en el paso de definir. El paso 2 del superviviente manda "
             "definir el problema con claridad y en una frase de diez segundos, pero lo deja "
             "como tarea de uno solo"),
     "donde": "paso 1 de breakthrough_desempeno_actual",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("que el disparador incluya RETRASOS Y COSTOS CRONICOS y no solo defectos, y que "
             "lo que se ve afectado sea LA SATISFACCION DEL CLIENTE. La condicion 1 del "
             "superviviente habla de un problema cronico de calidad que ya se intento "
             "resolver sin exito duradero, y ninguna de esas tres cosas esta nombrada"),
     "donde": "condicion 1 de breakthrough_desempeno_actual",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que la nominacion del problema se haga A NIVEL DE GERENCIA, que es quien "
             "selecciona y no solo que se seleccione. El paso 1 del superviviente manda "
             "seleccionar el problema concreto y darse un plazo, pero no dice a que altura de "
             "la organizacion se decide"),
     "donde": "paso 1 de secuencia_universal_para_el_breakthrough",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL VIAJE DIAGNOSTICO con sus cuatro tiempos nombrados, sintomas, teorias, "
             "pruebas y causa raiz, que es el metodo con el que se llega a la causa. El paso 4 "
             "del superviviente manda analizar hasta encontrar la causa raiz pero no dice por "
             "que camino"),
     "donde": "paso 3 de secuencia_universal_para_el_breakthrough",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que el remedio se PRUEBE BAJO CONDICIONES OPERATIVAS REALES antes de darlo por "
             "bueno, que es el viaje remedial. El paso 5 del superviviente manda implementar un "
             "remedio dirigido a la causa raiz, pero no manda probarlo en condiciones reales "
             "antes"),
     "donde": "paso 4 de secuencia_universal_para_el_breakthrough",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("que el disparador sea buscar UNA MEJORA SIGNIFICATIVA Y NO INCREMENTAL. "
             "ATENUANTE DECLARADO, y se dice para que la perdida se pueda pesar: la condicion 1 "
             "de secuencia_universal_breakthrough viaja ENTERA de APPEND y dice literalmente "
             "cambio radical de desempeno, no solo mejora incremental"),
     "donde": "condicion 1 de secuencia_universal_para_el_breakthrough",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL EJEMPLO CONCRETO DE SERVICIOS, reducir el ciclo de emision de credito, que es "
             "lo unico del acto que aterriza el metodo fuera de la manufactura. El paso 2 del "
             "superviviente manda definir el problema en una frase, sin ejemplo"),
     "donde": "paso 1 de seis_sigma_servicios",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("que el proceso con el problema cronico sea UN PROCESO DE SERVICIO y que el "
             "problema sea CUANTIFICABLE. La condicion 1 del superviviente nombra el problema "
             "cronico de calidad sin decir de que tipo de proceso ni que tenga que poder "
             "contarse"),
     "donde": "condicion 1 de seis_sigma_servicios",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL CHARTER como instrumento con el que se define el problema, y LOS OBJETIVOS DEL "
             "PROYECTO junto al problema. El paso 2 del superviviente manda definir el problema "
             "con claridad y en diez segundos, pero no nombra ni el documento ni los objetivos"),
     "donde": "paso 1 de six_sigma_dmaic_2",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("RECOPILAR LA VOZ DEL CLIENTE (VOC) dentro del paso de medir, que es lo que evita "
             "medir solo hacia dentro. El paso 3 del superviviente manda medir la magnitud real "
             "de los sintomas con datos, y el cliente no aparece"),
     "donde": "paso 2 de six_sigma_dmaic_2",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("que el disparador sea buscar una mejora DE TIPO BREAKTHROUGH EN PROCESOS CRITICOS "
             "PARA EL CLIENTE. ATENUANTE DECLARADO: la condicion 1 de "
             "secuencia_universal_breakthrough viaja ENTERA de APPEND y nombra el cambio radical "
             "de desempeno; lo que si se pierde sin atenuante es que el proceso sea CRITICO PARA "
             "EL CLIENTE"),
     "donde": "condicion 3 de six_sigma_dmaic_2",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO7 = {
    # ---------------------------------------------------------------
    "breakthrough_desempeno_actual": {
        "pasos": {
            "1": ("CUBIERTO", 2),   # definir el problema, con perdida: el asesor
            "2": ("CUBIERTO", 3),   # medir el desempeno actual
            "3": ("CUBIERTO", 4),   # analizar causas raiz de lo cronico
            "4": ("CUBIERTO", 5),   # implementar mejoras
            "5": ("CUBIERTO", 6),   # controles para sostener
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: retrasos, costos y satisfaccion
            "2": ("CUBIERTO", 2),
        },
    },
    # ---------------------------------------------------------------
    "secuencia_universal_breakthrough": {
        "pasos": {
            "1": ("APPEND",),       # establecer la creencia de que el cambio es deseable
            "2": ("APPEND",),       # estudio de factibilidad con Pareto, pocos vitales
            "3": ("APPEND",),       # brazo directivo y brazo diagnostico
            "4": ("CUBIERTO", 4),   # recolectar y analizar hechos = analizar hasta la causa
            "5": ("APPEND",),       # impacto cultural y gestion de la resistencia
            "6": ("CUBIERTO", 6),   # controles para sostener el nuevo nivel
        },
        "condiciones": {
            "1": ("APPEND",),       # cambio radical, no incremental (DISPARADOR DISTINTO)
            "2": ("APPEND",),       # resistencia cultural anticipada (DISPARADOR DISTINTO)
        },
    },
    # ---------------------------------------------------------------
    "secuencia_universal_para_el_breakthrough": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # nominar problemas prioritarios, con perdida: la gerencia
            "2": ("APPEND",),       # proyecto formal con equipo asignado (GESTO DISTINTO)
            "3": ("CUBIERTO", 4),   # con perdida: el viaje diagnostico y sus cuatro tiempos
            "4": ("CUBIERTO", 5),   # con perdida: probar bajo condiciones operativas reales
            "5": ("CUBIERTO", 6),
            "6": ("APPEND",),       # replicar y nominar nuevos proyectos (GESTO DISTINTO)
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),   # con perdida y atenuante
            "2": ("APPEND",),       # altos costos de mala calidad recurrentes
        },
    },
    # ---------------------------------------------------------------
    "seis_sigma_servicios": {
        "pasos": {
            "1": ("CUBIERTO", 2),   # con perdida: el ejemplo de servicios
            "2": ("CUBIERTO", 3),
            "3": ("CUBIERTO", 4),
            "4": ("CUBIERTO", 5),
            "5": ("CUBIERTO", 6),
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: proceso de servicio y cuantificable
            "2": ("APPEND",),       # institucionalizar cultura de mejora continua con datos
        },
    },
    # ---------------------------------------------------------------
    "six_sigma_dmaic_2": {
        "pasos": {
            "1": ("CUBIERTO", 2),   # con perdida: el charter y los objetivos
            "2": ("CUBIERTO", 3),   # con perdida: la voz del cliente
            "3": ("CUBIERTO", 4),
            "4": ("CUBIERTO", 5),
            "5": ("CUBIERTO", 6),
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),
            "2": ("APPEND",),       # niveles de calidad cercanos a la perfeccion (ppm)
            "3": ("CUBIERTO", 2),   # con perdida y atenuante parcial
        },
    },
}


# ======================================================================
# ACTO 8: LA FAMILIA DEL CIERRE EN LA VENTA GRANDE.
# SEIS miembros, TODOS de SPIN Selling (Rackham), NUEVE pares internos
# con veredicto y los NUEVE en A, CERO D y CERO puentes.
# FORMA medida: TODAS DE ACUERDO, y las dos varas de contenido apuntan a
# cierre_segun_complejidad_venta (5 pasos contra un maximo de 4 y 3
# condiciones contra un maximo de 2).
# ======================================================================

SUP8 = "cierre_segun_complejidad_venta"

MOTIVO8 = (
    "ACTO 8 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DEL CIERRE EN LA VENTA GRANDE. UNA SOLA "
    "FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON MEDICION: los SEIS miembros salen del "
    "MISMO libro (SPIN Selling, Rackham), los NUEVE pares internos con veredicto escrito son "
    "TODOS de clase A, hay CERO pares D internos y CERO nodos puente, medido con "
    "scripts/loop/vuelta65_puentes_del_tramo.py sobre el estado del dia (6 miembros, 15 "
    "combinaciones, 9 A, 0 D, 6 sin veredicto, 0 puentes, 0 triangulos). P.10 solo detiene "
    "una componente cuando aparece un triangulo A mas A mas D, y aqui no hay ninguno. Y LA "
    "FAMILIA NO LA DECLARA ESTA VUELTA: el puesto 601 dice con todas sus letras FAMILIA "
    "DECLARADA, los dos son miembros del racimo EL CIERRE EN VENTA GRANDE, asi que no se "
    "pelea la clase. "
    "SOBREVIVE cierre_segun_complejidad_venta POR CONTENIDO, con las DOS varas de contenido a "
    "su lado y ninguna en contra (FORMA medida TODAS DE ACUERDO, "
    "scripts/loop/varas_n_arias_del_tramo.py, docs/loop/SALIDA_V66_VARAS_N_ARIAS.txt): 5 "
    "pasos contra un maximo de 4 en los otros cinco, y 3 condiciones contra un maximo de 2. "
    "EL CABLEADO NO HACE FALTA Y NO SE USA: por P.8 solo habla a contenido empatado, y aqui "
    "el contenido no empata (ademas empata el, 6 contra 6). NO DECIDE EL ROTULO NI LA "
    "CANTIDAD SOLA: decide que es el UNICO del acto que trae las DOS MITADES de la tesis de "
    "Rackham, la permisiva y la prohibitiva (en la venta pequena las tecnicas de cierre SI se "
    "aplican sin restriccion, y en la grande se sustituyen por indagacion), y que ademas "
    "manda mirar el proceso de venta ENTERO y no solo el cierre. Los otros cinco traen la "
    "mitad prohibitiva o su aplicacion a un sujeto concreto. "
    "NINGUN MIEMBRO DE ESTE ACTO ES PUERTA, medido al sellar: la guarda 1B pasa por vacio y "
    "se dice en vez de darla por buena."
)

NOTA8 = (
    "EL REPARTO, Y LAS TRES COSAS QUE SE DICEN EN VEZ DE CALLARSE. "
    "PRIMERA, LAS TRES MEDICIONES QUE VIAJAN ENTERAS Y POR QUE SON TRES Y NO UNA: el acto "
    "propone TRES formas distintas de comprobar que el cambio de enfoque funciona, y las tres "
    "van de APPEND porque ninguna esta en el superviviente: medir TIEMPO DE TRANSACCION Y TASA "
    "DE EXITO antes y despues (cierre_segun_tamano_decision, paso 4), AUDITAR EL USO DE "
    "TECNICAS OBSERVANDO LLAMADAS REALES y comparar tasas entre quienes usan muchas y quienes "
    "usan pocas (ineficacia_cierre_ventas_grandes, pasos 2 y 3), y MEDIR LA SATISFACCION "
    "POSVENTA para detectar el dano a la relacion (riesgo_tecnicas_cierre_venta_compleja, paso "
    "4). Las razones de los puestos 1004 y 1564 las nombran una a una como lo propio de cada "
    "lado, y la del 1564 llama a la de las llamadas reales la mas dura de perder. Van las "
    "tres, con el solape DECLARADO entre las dos que miden tasa de exito, y la fase 04 poda. "
    "SEGUNDA, EL UNICO INCISO DEL ACTO Y POR QUE SOLO UNO: el paso 1 del superviviente "
    "clasifica por valor, sofisticacion del cliente y relacion posventa, y "
    "diferencias_venta_pequena_venta_grande anade DOS criterios que no estan, el ciclo (una "
    "llamada contra multiples) y la visibilidad de la decision. Van de INCISO adosado al paso "
    "1, que no termina en punto y se lee limpio. Los demas criterios que otros hermanos "
    "aportan al MISMO paso 1 (precio, riesgo e impacto organizacional, de "
    "cierre_segun_tamano_decision) NO se apilan encima: NO SE APILA MAS DE UN INCISO SOBRE EL "
    "MISMO PASO (acta 64, pregunta 5, registrada en la vuelta 65), asi que esa pieza va "
    "CUBIERTO con la perdida nombrada y enrutada. "
    "TERCERA, LA PERDIDA CON ATENUANTE DECLARADO: la condicion 2 de "
    "riesgo_tecnicas_cierre_venta_compleja (la baja satisfaccion de clientes como sintoma que "
    "dispara) va CUBIERTO con perdida, Y SE DICE QUE EL CONTENIDO LLEGA A MEDIAS: el paso 4 de "
    "ese mismo nodo viaja ENTERO de APPEND y manda MEDIR la satisfaccion posventa, o sea que "
    "el gesto se salva aunque el disparador no. "
    "EL SUPERVIVIENTE PASA DE 5 A 12 PASOS Y DE 3 A 7 CONDICIONES."
)

PERDIDAS8 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LOS TRES CRITERIOS DE CLASIFICACION DEL PORTAFOLIO, precio, riesgo e IMPACTO "
             "ORGANIZACIONAL, y el tercero es el que no es una cifra. El paso 1 del "
             "superviviente clasifica por valor, sofisticacion del cliente y relacion posventa, "
             "y ninguno de los tres es el impacto organizacional. NO SE ADOSA DE INCISO Y SE "
             "DICE POR QUE: el paso 1 YA recibe el inciso del paso 1 de "
             "diferencias_venta_pequena_venta_grande, y no se apila mas de un INCISO sobre el "
             "mismo paso (acta 64, pregunta 5)"),
     "donde": "paso 1 de cierre_segun_tamano_decision",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("que el disparador sea querer optimizar la estrategia comercial SEGUN EL TICKET "
             "PROMEDIO, que es el unico sitio del acto donde el criterio de entrada es una "
             "cifra del negocio y no una caracteristica de la venta. La condicion 1 del "
             "superviviente habla de alto valor y ciclos largos, que es otra cosa"),
     "donde": "condicion 2 de cierre_segun_tamano_decision",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LOS SUJETOS CONCRETOS con los que no se presiona, compradores corporativos, "
             "PROCUREMENT y ejecutivos experimentados. El paso 3 del superviviente manda "
             "minimizar el cierre en la venta grande y relacional, pero describe la VENTA y no "
             "a QUIEN se le vende"),
     "donde": "paso 2 de cierre_sofisticacion_comprador",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que la razon de no presionar entre llamadas sea que ESO REDUCE LA PROBABILIDAD DE "
             "EXITO FINAL, que es el dato empirico detras de la regla. El paso 3 del "
             "superviviente manda minimizar el cierre sin decir que pasa si no se hace"),
     "donde": "paso 2 de diferencias_venta_pequena_venta_grande",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que lo que se sustituya al cierre sean PREGUNTAS QUE EXPLOREN LA NECESIDAD REAL, "
             "nombradas como enfoque consultivo. El paso 3 del superviviente manda enfocar el "
             "esfuerzo en las etapas de indagacion (SPIN), que es el nombre del metodo pero no "
             "el gesto de preguntar"),
     "donde": "paso 3 de cierre_sofisticacion_comprador",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que el esfuerzo se ponga en las etapas previas DE INVESTIGACION Y DESARROLLO DE "
             "NECESIDADES y no en frases de cierre. El paso 3 del superviviente nombra la "
             "indagacion (SPIN) pero no la investigacion previa ni el desarrollo de la "
             "necesidad como dos tiempos"),
     "donde": "paso 3 de riesgo_tecnicas_cierre_venta_compleja",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("que el sintoma que dispara sea LA BAJA SATISFACCION DE CLIENTES junto a los "
             "scripts de cierre agresivo. ATENUANTE DECLARADO, y se dice para que la perdida se "
             "pueda pesar: el paso 4 de ESTE MISMO nodo viaja ENTERO de APPEND y manda medir la "
             "satisfaccion posventa para detectar el dano, o sea que el gesto se salva aunque el "
             "disparador no"),
     "donde": "condicion 2 de riesgo_tecnicas_cierre_venta_compleja",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("que el disparador sea que el equipo usa tecnicas de cierre tradicionales SIN "
             "RESULTADOS. La condicion 3 del superviviente dice que los resultados del cierre "
             "agresivo no mejoran las ventas COMPLEJAS, que acota a un tipo de venta lo que aqui "
             "se dice del equipo entero"),
     "donde": "condicion 2 de ineficacia_cierre_ventas_grandes",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO8 = {
    # ---------------------------------------------------------------
    "cierre_segun_tamano_decision": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # con perdida: precio, riesgo e impacto organizacional
            "2": ("CUBIERTO", 2),
            "3": ("CUBIERTO", 3),
            "4": ("APPEND",),       # medir tiempo de transaccion y tasa de exito
        },
        "condiciones": {
            "1": ("APPEND",),       # portafolio mixto (DISPARADOR DISTINTO)
            "2": ("CUBIERTO", 1),   # con perdida: el ticket promedio
        },
    },
    # ---------------------------------------------------------------
    "cierre_sofisticacion_comprador": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # la sofisticacion del cliente ya esta en el paso 1
            "2": ("CUBIERTO", 3),   # con perdida: procurement y ejecutivos
            "3": ("CUBIERTO", 3),   # con perdida: las preguntas que exploran la necesidad
            "4": ("APPEND",),       # construir la relacion sobre confianza y transparencia
        },
        "condiciones": {
            "1": ("APPEND",),       # comprador profesional o departamento de compras
            "2": ("APPEND",),       # B2B con procesos de decision formales
        },
    },
    # ---------------------------------------------------------------
    "diferencias_venta_pequena_venta_grande": {
        "pasos": {
            # EL UNICO INCISO DEL ACTO: dos criterios de clasificacion que el paso 1
            # del superviviente no tiene, y ese paso no termina en punto.
            "1": ("INCISO", 1,
                  "su ciclo (una llamada vs multiples), monto y visibilidad de la decision",
                  ", y tambien por "),
            "2": ("CUBIERTO", 3),   # con perdida: la probabilidad de exito final
            "3": ("APPEND",),       # la estrategia de seguimiento entre llamadas
            "4": ("APPEND",),       # el cliente evalua tambien la relacion
        },
        "condiciones": {
            "1": ("APPEND",),       # se aplica la misma tecnica a todas las ventas
        },
    },
    # ---------------------------------------------------------------
    "ineficacia_cierre_ventas_grandes": {
        "pasos": {
            "1": ("CUBIERTO", 1),
            "2": ("APPEND",),       # auditar observando llamadas reales
            "3": ("APPEND",),       # comparar tasas entre quienes usan muchas y pocas
            "4": ("CUBIERTO", 3),
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),
            "2": ("CUBIERTO", 3),   # con perdida: sin resultados, dicho del equipo entero
        },
    },
    # ---------------------------------------------------------------
    "riesgo_tecnicas_cierre_venta_compleja": {
        "pasos": {
            "1": ("CUBIERTO", 1),
            "2": ("CUBIERTO", 3),
            "3": ("CUBIERTO", 3),   # con perdida: investigacion y desarrollo de necesidades
            "4": ("APPEND",),       # medir la satisfaccion posventa
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),
            "2": ("CUBIERTO", 3),   # con perdida y atenuante
        },
    },
}


# ======================================================================
# ACTO 9: LA FAMILIA DE LOS CUADRANTES DE MERCADO Y LAS CUATRO
# CAPACIDADES. SEIS miembros, TODOS de Essentials of Supply Chain
# Management (Hugos), SIETE pares internos con veredicto y los SIETE en
# A, CERO D y CERO puentes.
# Y AQUI HAY CHOQUE DE PUERTA, REGISTRADO EN VEZ DE TAPADO: la FORMA
# medida es TODAS DE ACUERDO y las dos varas de contenido apuntan a
# cuatro_categorias_desempeno_cadena_suministro, pero LA PUERTA es
# marco_analisis_mercado_cadena_suministro. LA GUARDA 1B PROHIBE
# ABSORBER UNA PUERTA, asi que LA PUERTA SOBREVIVE (acta 54, pregunta 1).
# ======================================================================

SUP9 = "marco_analisis_mercado_cadena_suministro"

MOTIVO9 = (
    "ACTO 9 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LOS CUADRANTES DE MERCADO Y LAS CUATRO "
    "CAPACIDADES. UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON MEDICION: los SEIS "
    "miembros salen del MISMO libro (Essentials of Supply Chain Management, Hugos), los SIETE "
    "pares internos con veredicto escrito son TODOS de clase A, hay CERO pares D internos y "
    "CERO nodos puente, medido con scripts/loop/vuelta65_puentes_del_tramo.py sobre el estado "
    "del dia (6 miembros, 15 combinaciones, 7 A, 0 D, 8 sin veredicto, 0 puentes, 0 "
    "triangulos). P.10 solo detiene una componente cuando aparece un triangulo A mas A mas D, "
    "y aqui no hay ninguno. La razon del puesto 483 declara la familia con nombre: FAMILIA "
    "anotada, de CUATRO, sobre el mismo modelo de cuadrantes. "
    "SOBREVIVE marco_analisis_mercado_cadena_suministro POR LA GUARDA 1B, Y EL CHOQUE SE "
    "REGISTRA EN VEZ DE TAPARSE, QUE ES LA MITAD MAS IMPORTANTE DE ESTE MOTIVO. LAS DOS VIAS "
    "APUNTABAN A LADOS DISTINTOS: la vara de contenido apunta a "
    "cuatro_categorias_desempeno_cadena_suministro con las DOS varas y ninguna en contra "
    "(FORMA medida TODAS DE ACUERDO: 10 pasos contra un maximo de 5 y 4 condiciones contra un "
    "maximo de 3, scripts/loop/varas_n_arias_del_tramo.py, "
    "docs/loop/SALIDA_V66_VARAS_N_ARIAS.txt), y ademas la razon del puesto 704 dice que EL "
    "MARCO LARGO SE TRAGA AL CORTO nombrando a marco_analisis_mercado_cadena_suministro como "
    "el largo frente a cuatro_capacidades_mercado. PERO "
    "marco_analisis_mercado_cadena_suministro ES PUERTA, con la marca TIENE QUE SOBREVIVIR "
    "leida de la salida del dossier (docs/loop/SALIDA_V66_DOSSIER_LOTE_B.txt) y del cuadro de "
    "varas, y LA GUARDA 1B dice que un nodo que es semilla de entrada o extremo de puente "
    "aprobado NO SE ABSORBE. LA PUERTA SOBREVIVE POR EL ACTA 54, PREGUNTA 1, y el choque "
    "queda escrito aqui, que es el mismo carril con el que esta campana cerro el ACTO 20 de "
    "un tramo de OP-U-01 (registrado en docs/plan/03_FUSIONES.md). "
    "Y LA CONSECUENCIA VA DICHA Y NO ESCONDIDA: cuatro_categorias_desempeno_cadena_suministro, "
    "el nodo que la vara de contenido elegia, es el que mas piezas manda de APPEND, OCHO de "
    "sus diez pasos, y ese bulto es CONSECUENCIA DE LA GUARDA y no de repartir mal. VA "
    "MARCADO COMO DISCUTIBLE EN EL REPORTE DE ESTA VUELTA."
)

NOTA9 = (
    "EL REPARTO, Y LAS CUATRO COSAS QUE SE DICEN EN VEZ DE CALLARSE. "
    "PRIMERA, EL SUPERVIVIENTE ES EL MAS CORTO DEL ACTO Y POR ESO EL NODO CRECE TANTO: 5 "
    "pasos contra los 10 del que la vara elegia. La guarda 1B no admite la otra salida y el "
    "resultado es que el superviviente pasa de 5 a 21 pasos, que es el nodo mas largo que la "
    "campana ha fabricado, por encima de los 15 del acto 3 de la vuelta 65. LA CIFRA SE DICE "
    "AQUI porque es consecuencia medible de una guarda y no de una decision editorial "
    "escondida, y porque la fase 04 existe para podar. "
    "SEGUNDA, LOS CUATRO CALCULOS FINANCIEROS DE cuatro_categorias_desempeno_cadena_suministro, "
    "SUS PASOS 7 A 10 (rotacion de inventario, retorno sobre ventas, ciclo de conversion de "
    "efectivo, y mirar cuentas por cobrar y pagar antes que el inventario): SE OBSERVA Y NO SE "
    "ACTUA. Tienen la firma de un bloque pegado, porque los pasos 1 a 6 de ese nodo son el "
    "tablero de las cuatro categorias y estos cuatro son razones financieras que no vuelven a "
    "nombrarlas. LA OBSERVACION SE REGISTRA Y NO SE EJECUTA: decidir si eso es un injerto es "
    "materia de DESTEJIDO (P.3 y P.19) y ninguna operacion escrita lo nombra, asi que los "
    "cuatro viajan ENTEROS de APPEND con la observacion declarada y la fase 04 poda. Fundir no "
    "es sitio para destejer. "
    "TERCERA, EL UNICO INCISO DEL ACTO: el paso 2 del superviviente manda definir en que TIPO "
    "de mercado esta cada linea hoy y en dos anos, y no nombra los cuatro tipos; los cuatro "
    "cuadrantes (desarrollo, crecimiento, estable o maduro) son el modelo entero de la familia "
    "y viajan de INCISO adosado al paso 2, extraidos VERBATIM del paso 1 de "
    "clasificacion_mercados_cadena_suministro. El paso 2 no termina en punto y se lee limpio. "
    "Ningun otro paso recibe un segundo inciso (acta 64, pregunta 5). "
    "CUARTA, LAS DOS PERDIDAS CON ATENUANTE DECLARADO: los pasos 2 y 4 de "
    "modelo_cuadrantes_mercado (identificar y ajustar la mezcla de capacidades segun el "
    "cuadrante) van CUBIERTO al paso 4 del superviviente, y SE DICE QUE EL CONTENIDO LLEGA "
    "IGUAL: el paso 2 de cuatro_categorias_desempeno_cadena_suministro viaja ENTERO de APPEND y "
    "manda determinar cual categoria es critica SEGUN EL CUADRANTE en el que operas, que es "
    "exactamente ese amarre."
)

PERDIDAS9 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("ANALIZAR LA RELACION ENTRE OFERTA Y DEMANDA DE LA INDUSTRIA como la medicion con "
             "la que se decide el cuadrante. SE DICE LO QUE NO SE PIERDE: el paso 2 de "
             "clasificacion_mercados_cadena_suministro viaja ENTERO de APPEND y trae ese "
             "analisis; lo que se pierde es que sea EL CRITERIO del diagnostico del paso 1 de "
             "modelo_cuadrantes_mercado, que va CUBIERTO al paso 2 del superviviente"),
     "donde": "paso 1 de modelo_cuadrantes_mercado",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que la comparacion sea contra LOS ESTANDARES ESPERADOS PARA TU TIPO DE MERCADO y "
             "no solo contra la competencia. El paso 3 del superviviente compara con la "
             "competencia en las cuatro areas, que es otra vara: un mercado entero puede estar "
             "por debajo del estandar y la comparacion con el vecino no lo dice"),
     "donde": "paso 5 de cuatro_categorias_desempeno_cadena_suministro",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LAS METRICAS ESPECIFICAS POR CAPACIDAD con sus ejemplos, fill rate y tiempo de "
             "entrega. ATENUANTE DECLARADO: el paso 1 de "
             "cuatro_categorias_desempeno_cadena_suministro viaja ENTERO de APPEND y manda "
             "definir metricas concretas para cada una de las cuatro categorias; lo que se "
             "pierde son los DOS EJEMPLOS, que son lo que hace ejecutable el paso"),
     "donde": "paso 4 de cuatro_capacidades_mercado",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que lo que se identifique sea LA VENTAJA COMPETITIVA YA EXISTENTE, o sea donde ya "
             "se es mejor, como insumo de la decision. El paso 4 del superviviente decide si "
             "liderar, igualar o superar en cada area, pero no manda antes localizar la "
             "fortaleza que ya se tiene"),
     "donde": "paso 2 de cuatro_capacidades_mercado",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que la fortaleza relativa se mida FRENTE A COMPETIDORES y de forma RELATIVA. SE "
             "DICE LO QUE NO SE PIERDE: el paso 3 del superviviente ya compara con la "
             "competencia en las cuatro areas; lo que se pierde es que esa comparacion sirva "
             "para elegir DONDE CONCENTRARSE, que llega igual por el APPEND del paso 3 de "
             "estrategia_cuatro_capacidades_mercado"),
     "donde": "paso 2 de estrategia_cuatro_capacidades_mercado",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que las capacidades a reforzar se elijan SEGUN EL CUADRANTE detectado, y que sean "
             "esas cuatro nombradas (servicio, eficiencia, flexibilidad o desarrollo de "
             "producto). ATENUANTE DECLARADO: el paso 2 de "
             "cuatro_categorias_desempeno_cadena_suministro viaja ENTERO de APPEND y manda "
             "determinar cual categoria es critica SEGUN EL CUADRANTE de mercado en el que "
             "operas, que es ese mismo amarre"),
     "donde": "paso 2 de modelo_cuadrantes_mercado",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("AJUSTAR LA MEZCLA de capacidades, o sea que la decision no es por area suelta sino "
             "sobre el reparto entre las cuatro. ATENUANTE DECLARADO, el mismo del paso 2: el "
             "APPEND del paso 2 de cuatro_categorias_desempeno_cadena_suministro trae la "
             "priorizacion por cuadrante"),
     "donde": "paso 4 de modelo_cuadrantes_mercado",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("que el disparador sea NO SABER COMO PRIORIZAR RECURSOS SEGUN EL TIPO DE MERCADO. "
             "La condicion 2 del superviviente dice no tener claro en que areas enfocar los "
             "recursos para competir, y le falta el amarre al tipo de mercado, que es lo que "
             "esta familia aporta"),
     "donde": "condicion 2 de clasificacion_mercados_cadena_suministro",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("que el disparador sea necesitar ESTABLECER KPIs de cadena de suministro, que es "
             "una entrada por el instrumento y no por la oportunidad. La condicion 1 del "
             "superviviente entra por definir oportunidades para la cadena de suministro"),
     "donde": "condicion 1 de cuatro_categorias_desempeno_cadena_suministro",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("que el disparador sea necesitar EVALUAR OBJETIVAMENTE el desempeno de la cadena, "
             "con el acento en lo objetivo. La condicion 2 del superviviente habla de no tener "
             "claro en que areas enfocar los recursos, que es una duda de foco y no de metodo"),
     "donde": "condicion 3 de cuatro_categorias_desempeno_cadena_suministro",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("que el disparador sea DEFINIR LA ESTRATEGIA DE INVERSION EN OPERACIONES. La "
             "condicion 1 del superviviente entra por definir oportunidades de cadena de "
             "suministro, que es el paso anterior y no la decision de inversion"),
     "donde": "condicion 1 de cuatro_capacidades_mercado",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("que el disparador sea NO TENER CLARO QUE PRIORIZAR entre servicio, eficiencia, "
             "flexibilidad o innovacion, con las cuatro nombradas. La condicion 2 del "
             "superviviente dice no tener claro en que areas enfocar los recursos sin nombrar "
             "ninguna"),
     "donde": "condicion 2 de modelo_cuadrantes_mercado",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO9 = {
    # ---------------------------------------------------------------
    "clasificacion_mercados_cadena_suministro": {
        "pasos": {
            # EL UNICO INCISO DEL ACTO: los cuatro cuadrantes, que el paso 2 del
            # superviviente no nombra y que son el modelo entero de la familia.
            "1": ("INCISO", 2, "desarrollo, crecimiento, estable o maduro",
                  ", de entre los cuadrantes "),
            "2": ("APPEND",),       # analizar oferta y demanda de la industria
            "3": ("APPEND",),       # que oportunidades ofrece ese cuadrante
            "4": ("APPEND",),       # ajustar inventario, precios y cadena segun el cuadrante
            "5": ("APPEND",),       # revisar periodicamente porque el cuadrante cambia
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),
            "2": ("CUBIERTO", 2),   # con perdida: el amarre al tipo de mercado
            "3": ("APPEND",),       # varios mercados con dinamicas distintas
        },
    },
    # ---------------------------------------------------------------
    "cuatro_capacidades_mercado": {
        "pasos": {
            "1": ("CUBIERTO", 3),
            "2": ("CUBIERTO", 4),   # con perdida: la ventaja ya existente
            "3": ("APPEND",),       # invertir en la fortaleza, la doctrina propia
            "4": ("CUBIERTO", 5),   # con perdida y atenuante: los ejemplos de metrica
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: la estrategia de inversion
            "2": ("APPEND",),       # la tentacion de igualar en eficiencia interna
        },
    },
    # ---------------------------------------------------------------
    "cuatro_categorias_desempeno_cadena_suministro": {
        "pasos": {
            "1": ("APPEND",),       # metricas concretas por categoria
            "2": ("APPEND",),       # que categorias son criticas segun el cuadrante
            "3": ("APPEND",),       # recolectar datos de forma diaria o continua
            "4": ("CUBIERTO", 5),   # objetivos alineados = fijar metas concretas
            "5": ("CUBIERTO", 3),   # con perdida: los estandares del tipo de mercado
            "6": ("APPEND",),       # usar los datos para detectar problemas
            "7": ("APPEND",),       # rotacion de inventario (bloque financiero, observado)
            "8": ("APPEND",),       # retorno sobre ventas
            "9": ("APPEND",),       # ciclo de conversion de efectivo
            "10": ("APPEND",),      # cuentas por cobrar y pagar antes que el inventario
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: establecer KPIs
            "2": ("CUBIERTO", 2),
            "3": ("CUBIERTO", 2),   # con perdida: evaluar objetivamente
            "4": ("APPEND",),       # justificar una inversion en operacion logistica
        },
    },
    # ---------------------------------------------------------------
    "estrategia_cuatro_capacidades_mercado": {
        "pasos": {
            "1": ("CUBIERTO", 2),
            "2": ("CUBIERTO", 3),   # con perdida: la fortaleza RELATIVA
            "3": ("APPEND",),       # concentrar en 1 o 2 capacidades y no en todas
            "4": ("APPEND",),       # no invertir en eficiencia interna en mercado de crecimiento
        },
        "condiciones": {
            "1": ("APPEND",),       # mercado de rapido crecimiento con recursos limitados
            "2": ("APPEND",),       # confusion entre competir por precio o por servicio
        },
    },
    # ---------------------------------------------------------------
    "modelo_cuadrantes_mercado": {
        "pasos": {
            "1": ("CUBIERTO", 2),   # con perdida: oferta contra demanda como criterio
            "2": ("CUBIERTO", 4),   # con perdida y atenuante
            "3": ("APPEND",),       # senales de cambio de cuadrante, para anticiparse
            "4": ("CUBIERTO", 4),   # con perdida y atenuante: la MEZCLA
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),
            "2": ("CUBIERTO", 2),   # con perdida: las cuatro nombradas
        },
    },
}


# ======================================================================
# LOS TRES DECLARADOS Y NO FUNDIDOS. No llevan reparto porque no se
# funden: llevan motivo sellado y medicion.
# ======================================================================

DECLARADO_ACTO5 = {
    "acto": 5,
    "miembros": [
        "build_measure_learn",
        "ciclo_construir_medir_aprender",
        "ciclo_crear_medir_aprender",
        "desarrollo_en_espiral",
        "design_test_repeat",
        "design_thinking_proceso",
        "startup_como_experimento_cientifico",
        "testing_process_completo",
    ],
    "superviviente_que_el_contenido_elige": (
        "NINGUNO SE ELIGE, Y ESA ES LA DECISION. No se elige superviviente porque el acto no "
        "se funde: elegirlo seria decidir la fusion y dejarla a medias. Se dice ademas a quien "
        "habria apuntado la forma, para que nadie tenga que adivinarlo: la FORMA medida es UNA "
        "SOLA VARA y apunta a desarrollo_en_espiral (4 condiciones contra un maximo de 2 y "
        "cableado 18 contra 16), con la vara de PASOS empatada en 6 entre desarrollo_en_espiral "
        "y design_thinking_proceso."
    ),
    "motivo": (
        "DECLARADO Y NO FUNDIDO POR P.5, Y ES LA PRIMERA VEZ QUE LA CAMPANA CIERRA UN ACTO POR "
        "LA PREGUNTA DE P.5 EN VEZ DE POR EL TRIANGULO DE P.10. VA MARCADO COMO DISCUTIBLE, EL "
        "MAS FUERTE DE ESTA VUELTA. "
        "LA MEDICION VA DELANTE DE LA DECISION. P.10 NO SE DISPARA AQUI Y SE DICE PRIMERO para "
        "que no se confunda con el acto 1: medido con "
        "scripts/loop/vuelta65_puentes_del_tramo.py sobre el estado del dia, el acto 5 tiene 8 "
        "miembros, 28 combinaciones, 9 pares A, CERO pares D internos, 19 sin veredicto, CERO "
        "nodos puente y CERO triangulos. NO HAY TRIANGULO A MAS A MAS D, asi que el disparador "
        "mecanico de P.10 NO se cumple, y por la adjudicacion del acta 65 (pregunta 1) un "
        "veredicto ausente NO es un par sin leer. Si esto se cerrara solo con P.10, el acto se "
        "fundiria. "
        "LO QUE LO DETIENE ES LA OTRA MITAD, LA PREGUNTA QUE P.5 OBLIGA A CONTESTAR ANTES DE "
        "FUNDIR: EL ACTO ES UNA FAMILIA O SON DOS. Y contestada sobre el texto estable de los "
        "ocho nodos, leidos enteros en el dossier de esta vuelta "
        "(docs/loop/SALIDA_V66_DOSSIER_LOTE_B.txt), LA RESPUESTA ES QUE NO ES UNA FAMILIA. "
        "HAY UN BUCLE DE CUATRO TIEMPOS Y HAY TRES PROCESOS LARGOS QUE LO CONTIENEN COMO UNO DE "
        "SUS PASOS, Y NO SON LO MISMO. La sub-familia del bucle es build_measure_learn, "
        "ciclo_construir_medir_aprender, ciclo_crear_medir_aprender y "
        "startup_como_experimento_cientifico, cerrada entre si por los puestos 213, 376, 486 y "
        "1208, todos de Ries o de Value Proposition Design. Los otros tres son procesos con "
        "procedimiento propio: design_thinking_proceso (Cooper) recorre ENTENDER, OBSERVAR con "
        "tecnicas etnograficas, DEFINIR UN PUNTO DE VISTA e IDEAR antes de prototipar; "
        "testing_process_completo (Value Proposition Design) da forma a las ideas con los dos "
        "lienzos, extrae las hipotesis criticas, disena experimentos con la tarjeta de test y "
        "mide con el Progress Board; desarrollo_en_espiral (Cooper) fija QUE se mide en cada "
        "prueba, CUANTAS vueltas y la documentacion de cada iteracion. "
        "Y LO QUE LOS PEGA AL BUCLE ES UN SOLO NODO QUE NO TIENE NADA PROPIO: design_test_repeat. "
        "SUS CUATRO A SON LA UNICA VIA por la que los tres procesos entran en la componente, "
        "medido sobre los nueve pares A del acto: el 723 lo une a "
        "ciclo_construir_medir_aprender, el 796 a testing_process_completo, el 1182 a "
        "desarrollo_en_espiral, el 1449 a build_measure_learn y el 1573 a "
        "design_thinking_proceso. QUITADO design_test_repeat, los tres procesos quedan sueltos, "
        "cada uno con CERO A hacia el resto. Y las cuatro razones lo dicen con la misma frase en "
        "cuatro sitios: el 796 dice EL CICLO DESNUDO CONTRA EL PROCESO QUE LO CONTIENE y que lo "
        "que anade no llega ni a una linea; el 1182 y el 1573 lo llaman SUBCONJUNTO ESTRICTO; y "
        "el 1573 dice que de design_thinking_proceso se perderian CUATRO ETAPAS ENTERAS y que "
        "hay que decirlo fuerte porque son la mayor parte del nodo. "
        "P.12 ES LA LETRA QUE CIERRA ESTO, Y SE CITA ENTERA: EL CIERRE TRANSITIVO CONVOCA, LA "
        "LECTURA DECIDE, y con el acto leido entero MANDAN LOS VEREDICTOS DIRECTOS, porque UNA "
        "A QUE NADIE LEYO NO EXISTE. Fundir el acto entero a un superviviente sellaria que "
        "design_thinking_proceso, testing_process_completo y desarrollo_en_espiral repiten "
        "ENTRE SI y con la sub-familia del bucle, y NINGUNO de esos pares esta leido: los tres "
        "procesos no tienen entre ellos ni un solo veredicto escrito. Eso no es lo que el "
        "cierre transitivo probo: el cierre transitivo cuenta, no lee. "
        "LAS TRES SALIDAS DE P.10 NO APLICAN PORQUE P.10 NO SE DISPARA, Y LAS ALTERNATIVAS A "
        "DECLARAR SE RECORREN IGUAL, UNA A UNA, EN VEZ DE ELEGIR LA COMODA. Leer los 19 pares "
        "que faltan es la unica que resuelve de verdad, y es cribado que esta fase no tiene "
        "(banco 9.21, el barrido corre UNA vez; regla 4 de EJECUTOR.md, en ejecucion no se "
        "cribra). Fundir solo la sub-familia cerrada del bucle y dejar los tres procesos fuera "
        "es una FUSION PARCIAL, y el encargo de esta vuelta dice con todas sus letras que no se "
        "improvisan fusiones parciales que ninguna letra escribe. Y fundir el acto entero "
        "desmentiria las cuatro razones que declaran a design_test_repeat subconjunto estricto "
        "de tres procesos distintos entre si. ASI QUE NO SE FUNDE NADA Y SE DECLARA. "
        "EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se depreca ninguno y no se elige "
        "superviviente. ES REVERSIBLE ENTERO y no desmiente ninguna lectura escrita, que es "
        "exactamente lo que el acta 65 dijo del acto 1 al adjudicarlo A FAVOR. "
        "Y VA COMO PENDIENTE DE DOCTRINA EN EL REPORTE, POR LA REGLA 5, SIN PARAR: la letra "
        "escrita no dice que hacer cuando P.5 contesta DOS y P.10 no se dispara. Lo mejor "
        "sostenido es el carril que ya existe, DECLARADO Y NO FUNDIDO CON MOTIVO SELLADO, que es "
        "el mismo con el que cerraron el acto 1 (por P.10) y el que el acta 65 extendio al acto "
        "de dos puertas (por la guarda 1B). El auditor adjudica."
    ),
    "medicion": {
        "instrumento": "scripts/loop/vuelta65_puentes_del_tramo.py",
        "salida": "docs/loop/SALIDA_V66_PUENTES_LOTE_B.txt",
        "dossier": "docs/loop/SALIDA_V66_DOSSIER_LOTE_B.txt",
        "varas": "docs/loop/SALIDA_V66_VARAS_N_ARIAS.txt",
        "miembros": 8,
        "combinaciones": 28,
        "pares_A": 9,
        "pares_D": 0,
        "pares_sin_veredicto": 19,
        "nodos_puente": 0,
        "triangulos_puente": 0,
        "puertas_dentro": [],
        "nodo_que_pega": "design_test_repeat",
        "A_del_nodo_que_pega": [723, 796, 1182, 1449, 1573],
        "procesos_que_solo_entran_por_el": [
            "design_thinking_proceso",
            "testing_process_completo",
            "desarrollo_en_espiral",
        ],
    },
}

DECLARADO_ACTO10 = {
    "acto": 10,
    "miembros": [
        "customer_validation_sales_roadmap",
        "estrategia_de_ventas",
        "hoja_de_ruta_de_ventas",
        "refinar_sales_roadmap",
        "sales_roadmap",
        "sales_roadmap_vs_sales_force",
    ],
    "superviviente_que_el_contenido_elige": (
        "NINGUNO SE ELIGE, Y ESA ES LA DECISION. No se elige superviviente porque el acto no se "
        "funde. Se dice a quien habria apuntado la forma para que nadie tenga que adivinarlo: "
        "FORMA medida UNA SOLA VARA, que apunta a refinar_sales_roadmap (6 pasos contra un "
        "maximo de 5), con la vara de condiciones empatada en 2 a cuatro bandas y el cableado "
        "apuntando a otro lado, hoja_de_ruta_de_ventas con 10."
    ),
    "motivo": (
        "DECLARADO Y NO FUNDIDO POR P.10, LA MITAD DIAGNOSTICA DE P.5, Y LA MEDICION VA DELANTE "
        "DE LA DECISION. P.10 dice con todas sus letras que UN NODO PUENTE es el que tiene A con "
        "dos nodos que entre si son D, que la componente que forma puede ser UNA familia o DOS "
        "pegadas por el, que el cierre transitivo no lo distingue porque no lee sino que cuenta, "
        "y que SI APARECE, LA COMPONENTE NO SE FUNDE HASTA QUE ESE TRIANGULO SE CIERRE. "
        "MEDIDO EN ESTA VUELTA con scripts/loop/vuelta65_puentes_del_tramo.py sobre el acto "
        "entero, con los ids pasados por el resolutor (P.1): 6 miembros, 15 combinaciones, 6 "
        "pares A, CUATRO pares D internos ya leidos y declarados DISTINTOS, 5 sin veredicto, DOS "
        "NODOS PUENTE y TRES TRIANGULOS PUENTE. refinar_sales_roadmap hace de puente en DOS "
        "(tiene A con hoja_de_ruta_de_ventas y con sales_roadmap_vs_sales_force, que son D entre "
        "si en el puesto 1330; y A con sales_roadmap y con sales_roadmap_vs_sales_force, que son "
        "D entre si en el 1306). sales_roadmap_vs_sales_force hace de puente en UNO (A con "
        "customer_validation_sales_roadmap y con refinar_sales_roadmap, que son D entre si en el "
        "1023). Los cuatro pares D internos son los puestos 872, 1023, 1306 y 1330. "
        "FUNDIR LA COMPONENTE ENTERA DESMENTIRIA CUATRO LECTURAS QUE YA ESTAN ESCRITAS, y P.10 "
        "llama a eso exactamente lo que nunca es salida. Y LA LECTURA DE ESAS CUATRO ES DE UNA "
        "PIEZA Y NO UN ACCIDENTE: las razones del 1306 y del 1330 dicen las dos EL CONTENIDO DEL "
        "MAPA CONTRA EL USO DEL MAPA, y la del 872 dice LA ECONOMIA DE LA VENTA CONTRA EL MAPA DE "
        "ACCESO y declara que el sub-puro del sales roadmap SE ROMPE. "
        "LAS TRES SALIDAS DE P.10, RECORRIDAS UNA A UNA EN VEZ DE ELEGIR LA COMODA: leer los 5 "
        "pares que faltan es la unica que resuelve de verdad, y es trabajo de cribado que esta "
        "fase no tiene (banco 9.21; regla 4 de EJECUTOR.md); releer contra el superviviente no "
        "aplica, porque aqui no hay superviviente elegido ni nodo que vaya a cambiar; y fundir "
        "solo el subconjunto CERRADO y enlazar el resto pide que TODAS las lecturas esten hechas, "
        "y no lo estan. ASI QUE NO SE FUNDE NADA Y SE DECLARA, que es lo que la letra deja, y es "
        "el carril que el acta 65 confirmo A FAVOR para el acto 1 y que el encargo de esta vuelta "
        "nombra para los actos con puente. "
        "NINGUN MIEMBRO DE ESTE ACTO ES PUERTA, medido al sellar: la guarda 1B pasa por vacio y se "
        "dice en vez de darla por buena, o sea que la razon del DECLARADO es UNA y no dos. "
        "EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se depreca ninguno y no se elige "
        "superviviente. Su destino comparte carril con el pendiente 2 del acta 65: el cierre de la "
        "fase 03."
    ),
    "medicion": {
        "instrumento": "scripts/loop/vuelta65_puentes_del_tramo.py",
        "salida": "docs/loop/SALIDA_V66_PUENTES_LOTE_B.txt",
        "dossier": "docs/loop/SALIDA_V66_DOSSIER_LOTE_B.txt",
        "varas": "docs/loop/SALIDA_V66_VARAS_N_ARIAS.txt",
        "miembros": 6,
        "combinaciones": 15,
        "pares_A": 6,
        "pares_D": 4,
        "pares_sin_veredicto": 5,
        "nodos_puente": 2,
        "triangulos_puente": 3,
        "puertas_dentro": [],
        "puestos_D_internos": [872, 1023, 1306, 1330],
    },
}

DECLARADO_ACTO11 = {
    "acto": 11,
    "miembros": [
        "alineacion_etica_ia_negocio",
        "human_in_the_loop_ia",
        "mitigar_falling_asleep_wheel",
        "principio_humano_en_el_loop",
        "riesgo_sobredependencia_ia",
    ],
    "superviviente_que_el_contenido_elige": (
        "NINGUNO SE ELIGE, Y ESA ES LA DECISION. No se elige superviviente porque el acto no se "
        "funde. Se dice a quien habria apuntado la forma: FORMA medida UNA SOLA VARA, que apunta "
        "a alineacion_etica_ia_negocio (5 pasos contra un maximo de 4), con la vara de "
        "condiciones empatada en 2 a cuatro bandas y el cableado apuntando a otro lado, "
        "human_in_the_loop_ia con 5."
    ),
    "motivo": (
        "DECLARADO Y NO FUNDIDO POR P.10, LA MITAD DIAGNOSTICA DE P.5, Y LA MEDICION VA DELANTE "
        "DE LA DECISION. P.10 dice que UN NODO PUENTE es el que tiene A con dos nodos que entre "
        "si son D, y que SI APARECE, LA COMPONENTE NO SE FUNDE HASTA QUE ESE TRIANGULO SE CIERRE. "
        "MEDIDO EN ESTA VUELTA con scripts/loop/vuelta65_puentes_del_tramo.py sobre el acto "
        "entero, con los ids pasados por el resolutor (P.1): 5 miembros, 10 combinaciones, 5 "
        "pares A, DOS pares D internos ya leidos y declarados DISTINTOS, 3 sin veredicto, DOS "
        "NODOS PUENTE y DOS TRIANGULOS PUENTE. human_in_the_loop_ia hace de puente en UNO (A con "
        "mitigar_falling_asleep_wheel y con principio_humano_en_el_loop, que son D entre si en el "
        "puesto 1541). mitigar_falling_asleep_wheel hace de puente en UNO (A con "
        "human_in_the_loop_ia y con riesgo_sobredependencia_ia, que son D entre si en el 1496). "
        "Los dos pares D internos son los puestos 1496 y 1541. "
        "FUNDIR LA COMPONENTE ENTERA DESMENTIRIA DOS LECTURAS QUE YA ESTAN ESCRITAS, y las dos "
        "dicen LA MISMA FRONTERA con las mismas palabras, que es lo que las hace de una pieza: el "
        "1496 dice UNO PROTEGE LA DECISION DE HOY, EL OTRO PROTEGE LA CAPACIDAD DE DECIDIR DE "
        "MANANA, y el 1541 repite PROTEGE LA DECISION DE HOY contra PROTEGE LA CAPACIDAD DE "
        "MANANA. Ademas el 1541 declara que con ese par EL RACIMO DE LA IA TERMINA SU COLA y que "
        "la particion escrita en la seccion 11.bis del informe NO se mueve: hay una frontera "
        "escrita dentro de este acto y una fusion entera la borraria. "
        "LAS TRES SALIDAS DE P.10, RECORRIDAS UNA A UNA: leer los 3 pares que faltan es la unica "
        "que resuelve de verdad y es cribado que esta fase no tiene; releer contra el "
        "superviviente no aplica porque no hay superviviente elegido; y fundir solo el "
        "subconjunto CERRADO pide que TODAS las lecturas esten hechas, y no lo estan. ASI QUE NO "
        "SE FUNDE NADA Y SE DECLARA. "
        "NINGUN MIEMBRO DE ESTE ACTO ES PUERTA, medido al sellar: la guarda 1B pasa por vacio y se "
        "dice en vez de darla por buena. "
        "EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se depreca ninguno y no se elige "
        "superviviente. Su destino comparte carril con el pendiente 2 del acta 65: el cierre de la "
        "fase 03."
    ),
    "medicion": {
        "instrumento": "scripts/loop/vuelta65_puentes_del_tramo.py",
        "salida": "docs/loop/SALIDA_V66_PUENTES_LOTE_B.txt",
        "dossier": "docs/loop/SALIDA_V66_DOSSIER_LOTE_B.txt",
        "varas": "docs/loop/SALIDA_V66_VARAS_N_ARIAS.txt",
        "miembros": 5,
        "combinaciones": 10,
        "pares_A": 5,
        "pares_D": 2,
        "pares_sin_veredicto": 3,
        "nodos_puente": 2,
        "triangulos_puente": 2,
        "puertas_dentro": [],
        "puestos_D_internos": [1496, 1541],
    },
}

LOTE_B = {
    "titulo": ("LOTE B DEL TRAMO UNICO DE OP-U-02, PREFIJO SIN SALTOS DEL orden_universo DE LO "
               "QUE QUEDA: LOS ACTOS 5, 7, 8, 9, 10 Y 11, SEIS ACTOS Y 37 NODOS. Los actos 7, 8 "
               "y 9 cierran FUNDIDOS; los actos 5, 10 y 11 cierran DECLARADOS Y NO FUNDIDOS con "
               "motivo sellado. El acto 9 lleva el PRIMER CHOQUE DE PUERTA del tramo (la puerta "
               "sobrevive por la guarda 1B contra la vara de contenido) y el acto 5 es el PRIMER "
               "acto de la campana declarado por la pregunta de P.5 y no por el triangulo de "
               "P.10"),
    "actos": [
        {
            "orden": 7,
            "superviviente": SUP7,
            "motivo": MOTIVO7,
            "nota": NOTA7,
            "reparto": REPARTO7,
            "perdidas": PERDIDAS7,
        },
        {
            "orden": 8,
            "superviviente": SUP8,
            "motivo": MOTIVO8,
            "nota": NOTA8,
            "reparto": REPARTO8,
            "perdidas": PERDIDAS8,
        },
        {
            "orden": 9,
            "superviviente": SUP9,
            "motivo": MOTIVO9,
            "nota": NOTA9,
            "reparto": REPARTO9,
            "perdidas": PERDIDAS9,
        },
    ],
    "declarados": [DECLARADO_ACTO5, DECLARADO_ACTO10, DECLARADO_ACTO11],
}
