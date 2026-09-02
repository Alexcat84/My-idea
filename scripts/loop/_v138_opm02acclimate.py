# -*- coding: utf-8 -*-
"""_v138_opm02acclimate.py . EL CONTENIDO EDITORIAL DE LA FUSION DE MESA
OP-M-02-ACCLIMATE.

NO ES UN INSTRUMENTO: no mide, no escribe y no decide nada por si mismo. Es EL
TEXTO del reparto pieza a pieza, con su motivo citado y LAS PERDIDAS SELLADAS EN
CAMPO PROPIO. Lo importa scripts/loop/generar_plan_de_fusion_de_mesa.py, que es
quien pone LA ARITMETICA Y LAS GUARDAS y quien sella el plan.

EL SUPERVIVIENTE NO SE ELIGE AQUI: LO ELIGIO LA FICHA. La adjudicacion de
OP-M-02-ACCLIMATE esta sellada en docs/plan/OPERACIONES.jsonl desde el 12 ago
2026 (DESEMPATE POR CABLEADO, 10 contra 3) y el generador cae en ROJO si este
fichero nombra otro.

EL REPARTO VA EN EL FORMATO POR PAR, {"<absorbido>": {"1": marca, ...}}, que la
operacion 2.a de esta misma vuelta estreno. Esta fusion tiene UN solo absorbido y
el formato viejo plano habria valido igual; se usa el nuevo a proposito, para que
la primera mesa que se sienta despues de la reparacion la use.
"""

FUSION = {
    "titulo": (
        "LA FASE ACCLIMATE DE AFFIRM, UN NODO POR FASE: "
        "fase_acclimate_experiencia_cliente absorbe fase_acclimate_mapa_de_proceso. "
        "Es la segunda fusion de la fase 06 por el orden del acta 137, 3.5, y la unica "
        "de las seis que el generador sellado podia hacer sin la reparacion 2.a, porque "
        "es la unica con un solo absorbido. EL MAPA VISUAL DEL PROCESO ES LA PIEZA QUE "
        "LA FICHA MANDA PRESERVAR y va de APPEND, la primera del reparto"
    ),
    "superviviente": "fase_acclimate_experiencia_cliente",
    "absorbidos": ["fase_acclimate_mapa_de_proceso"],
    "motivo": (
        "EL SUPERVIVIENTE LO FIJA LA FICHA SELLADA Y AQUI NO SE RE-ADJUDICA: "
        "docs/plan/OPERACIONES.jsonl escribe superviviente "
        "fase_acclimate_experiencia_cliente el 12 ago 2026, POR DESEMPATE POR CABLEADO, "
        "10 contra 3. LA LECTURA DE ACTO POR P.5 ESTA HECHA Y MEDIDA EN ESTA VUELTA: el "
        "acto tiene UN solo par interno, fase_acclimate_experiencia_cliente contra "
        "fase_acclimate_mapa_de_proceso, y esta LEIDO, en el puesto 447 del cribado, "
        "clase A (docs/loop/SALIDA_V138_3_P5_LAS_SEIS.txt, corrido con "
        "scripts/loop/vuelta138_p5_lectura_de_acto.py --id-op OP-M-02-ACCLIMATE). La "
        "verificacion de la ficha dice 'si la lectura completa cambia la clase, la "
        "fusion se detiene': NO cambia, sigue en A, y por eso la fusion sigue. "
        "LA NOTA DE LA FICHA SE RESPETA Y NO SE TOCA: la fase queda con DOS nodos y no "
        "con uno, porque fase_acclimate, el nodo base, NO entra (sus dos pares son "
        "DUDOSOS, puestos 196 y 253). Este reparto no lo mete ni lo nombra."
    ),
    "pasos": {
        "fase_acclimate_mapa_de_proceso": {
            # 1. Mapear todos los pasos del proceso de entrega/servicio desde la
            #    perspectiva del cliente
            "1": ["CUBIERTO", 1],
            # 2. Crear un documento o grafico visual (mapa) que muestre en que
            #    etapa esta el cliente en cada momento
            "2": ["APPEND"],
            # 3. Establecer comunicaciones recurrentes atadas a micro-logros o
            #    hitos del proceso
            "3": ["CUBIERTO", 4],
            # 4. Detectar senales silenciosas de desconexion del cliente antes de
            #    que se quejen o abandonen
            "4": ["APPEND"],
            # 5. Simplificar procesos complejos dividiendolos en pasos pequenos y
            #    digeribles
            "5": ["APPEND"],
            # 6. Haz una lista de todos los puntos de contacto que atraviesa un
            #    cliente nuevo entre la compra y el dia 100
            "6": ["CUBIERTO", 1],
            # 7. Establece hitos de comunicacion proactiva (bienvenida, chequeos
            #    de progreso, celebracion de logros tempranos) distribuidos en ese
            #    periodo
            "7": ["CUBIERTO", 3],
            # 8. Asigna un responsable claro para cada punto de contacto y mide
            #    que tan consistente es la ejecucion
            "8": ["APPEND"],
        },
    },
    "condiciones": {
        "fase_acclimate_mapa_de_proceso": {
            # 1. Cuando los clientes se pierden, dejan de responder o preguntan
            #    'que sigue?' durante la implementacion o entrega del servicio
            "1": ["CUBIERTO", 1],
        },
    },
    "nota": (
        "NUEVE PIEZAS REPARTIDAS: cuatro viajan enteras y cinco ya estaban dichas. "
        "LA PIEZA QUE LA FICHA MANDA PRESERVAR VIAJA ENTERA Y ES LA PRIMERA DEL "
        "REPARTO: el MAPA VISUAL del proceso, el documento o grafico que muestra en que "
        "etapa esta el cliente en cada momento (paso 2 del que muere), es el artefacto "
        "propio del que muere y el superviviente no lo tiene en ningun grado: el "
        "superviviente MAPEA los puntos de contacto, que es la accion, pero no fabrica "
        "el artefacto que los ensena. Va de APPEND. "
        "LAS CINCO QUE YA ESTABAN DICHAS, una por una y contra el texto de hoy: el paso "
        "1 del que muere mapea el proceso y el paso 1 del superviviente mapea todos los "
        "puntos de contacto entre la primera compra y el logro del objetivo, que es el "
        "mismo barrido; el paso 6 hace LA LISTA de esos mismos puntos de contacto, o sea "
        "el mismo paso 1 otra vez con otro horizonte; el paso 3 pide comunicaciones "
        "atadas a hitos y el paso 4 del superviviente establece hitos claros y los "
        "celebra; y el paso 7 distribuye hitos de comunicacion proactiva, que es el paso "
        "3 del superviviente, disenar herramientas de comunicacion para cada etapa. "
        "DIVERGENCIA DECLARADA CON LA PASADA P.13 DE LA FICHA, Y NO SE RESUELVE "
        "COPIANDO: la ficha recomputo perdidas el 12 ago 2026 y dejo UNA sola pieza en "
        "preservar, el mapa visual. Leido el nodo entero HOY, paso por paso, hay TRES "
        "gestos mas que el superviviente NO hace en ningun grado y que por tanto no "
        "pueden ir de CUBIERTO sin afirmar del superviviente algo que no dice: "
        "DETECTAR LAS SENALES SILENCIOSAS de desconexion ANTES de la queja (el "
        "superviviente MIDE con encuestas y check-ins, que es preguntar, no vigilar lo "
        "que no se dice); SIMPLIFICAR los procesos complejos partiendolos en pasos "
        "pequenos (el superviviente reconoce la complejidad en su condicion 2 pero no "
        "manda hacer nada con ella); y ASIGNAR UN RESPONSABLE claro por punto de "
        "contacto y medir la consistencia de la ejecucion (el superviviente no nombra a "
        "nadie). LOS TRES VAN DE APPEND: la lista `preservar` de la ficha es el SUELO de "
        "lo que no se puede perder, no el TECHO de lo que puede viajar, y su propia "
        "verificacion manda que 'el superviviente conserva las piezas propias del que "
        "muere: se comprueban una por una en su texto'. LA DIVERGENCIA SE DECLARA EN VEZ "
        "DE TAPARSE y VA MARCADA COMO DISCUTIBLE EN EL REPORTE DE ESTA VUELTA. "
        "TRES PERDIDAS SELLADAS EN EL CAMPO, y las tres son de matiz y ninguna de gesto."
    ),
    "perdidas": [
        {
            "especie": "DE PARAMETRO DE PASO",
            "que": ("el HORIZONTE CONCRETO del recorrido, entre la compra y EL DIA 100, y "
                    "el encuadre DESDE LA PERSPECTIVA DEL CLIENTE; el paso 1 del "
                    "superviviente dice entre la primera compra y el logro del objetivo "
                    "del cliente, que es el mismo tramo medido por el resultado en vez de "
                    "por los dias"),
            "donde": "pasos 1 y 6 de fase_acclimate_mapa_de_proceso",
            "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente",
        },
        {
            "especie": "DE PARAMETRO DE PASO",
            "que": ("la ENUMERACION de los hitos de comunicacion proactiva, bienvenida, "
                    "chequeos de progreso y celebracion de logros tempranos, y el "
                    "calificativo MICRO-LOGROS; los pasos 3 y 4 del superviviente disenan "
                    "las herramientas de comunicacion por etapa y establecen hitos claros "
                    "que se celebran, que es el mismo gesto sin la lista de ejemplos"),
            "donde": "pasos 3 y 7 de fase_acclimate_mapa_de_proceso",
            "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente",
        },
        {
            "especie": "DE CONDICIONES",
            "que": ("el disparador de que el cliente PREGUNTE QUE SIGUE durante la "
                    "implementacion, que es la senal dicha en voz alta; la condicion 1 del "
                    "superviviente dispara por ALTA TASA DE ABANDONO en los primeros meses "
                    "tras la venta, que recoge al que se pierde y al que deja de responder "
                    "pero no al que pregunta"),
            "donde": "condicion 1 de fase_acclimate_mapa_de_proceso",
            "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)",
        },
    ],
    "simulacion_de_hoy": (
        "scripts/plan/simular_fusion.py corrido en la vuelta 138 ANTES de tocar un nodo "
        "(docs/loop/SALIDA_V138_3_SIM_OPM02ACCLIMATE.txt): CUATRO entradas se redirigen "
        "(gamificacion_onboarding_visual, ocho_fases_experiencia_cliente, "
        "seis_herramientas_comunicacion_fase_activate y shock_and_awe_kit_bienvenida), "
        "DOS duplicadas NUEVAS, CERO auto aristas, y el acto queda SIN ARISTAS INTERNAS. "
        "DOS DIVERGENCIAS ENTRE LA MEDICION SELLADA DEL 12 AGO 2026 Y LA DE HOY, Y LAS "
        "DOS SE DECLARAN EN VEZ DE TAPARSE, PORQUE NINGUNA CAMBIA EL SUPERVIVIENTE. "
        "PRIMERA: el cableado de hoy es 11 contra 4 y no 10 contra 3; el superviviente "
        "sigue ganando y por mas margen. SEGUNDA, Y ES LA QUE IMPORTA: la ficha dice en "
        "su verificacion 'la simulacion fabrica 0 duplicadas' y en su nota 'es ademas la "
        "unica de las cinco que NO fabrica ninguna duplicada', y LA SIMULACION DE HOY "
        "FABRICA DOS: gamificacion_onboarding_visual en nodos_previos y "
        "ocho_fases_experiencia_cliente en nodos_siguientes. No se corrige la ficha ni se "
        "copia su cifra: se declara la discrepancia. LAS DOS QUEDAN PARA OP-S-12, que es "
        "lo que la propia verificacion de la ficha manda ('las duplicadas que la fusion "
        "fabrica quedan para OP-S-12, que corre despues') y que va AL FINAL de la pasada "
        "entera por la atadura 2 del indice. VA MARCADA COMO DISCUTIBLE EN EL REPORTE."
    ),
}
