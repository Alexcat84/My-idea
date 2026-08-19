# -*- coding: utf-8 -*-
"""vuelta38_bloques.py - LA PROSA SELLADA DE LOS DOS PLANES DE OP-D-04.

DATOS, NO CODIGO. Vive aparte de scripts/loop/vuelta38_sellar_planes.py por una
razon de auditoria y no de estilo: el sellador COMPRUEBA (particion, verbatim,
grafo) y esto es lo que un humano ESCRIBIO (la lectura de contenido de P.8, la
tabla de perdidas de P.13, los dos resumenes). Separarlos deja ver de un vistazo
que parte del plan esta medida y que parte esta argumentada.

Nada de aqui se ejecuta contra dataset: el sellador lo copia dentro de los dos
ficheros de plan bajo docs/loop/.
"""

# ---------------------------------------------------------------------------
# LA ELECCION DE SUPERVIVIENTE (P.8), POR FUSION.
#
# P.8: EL CABLEADO DESEMPATA, NO DECIDE. Las dos elecciones se hacen POR LECTURA
# DE CONTENIDO escrita entera, como manda la DECISION 2 del fundador del 19 ago
# 2026, y el cableado se cita SOLO como lo que es: en el taller va EN CONTRA del
# elegido y no lo mueve; en la alternancia coincide y tampoco decide.
# ---------------------------------------------------------------------------

ELECCION_TALLER = {
    "regla": "P.8, EL CABLEADO DESEMPATA, NO DECIDE. Donde el contenido dice algo, manda el "
             "contenido, aunque el margen de aristas apunte al otro lado.",
    "decide": "EL CONTENIDO",
    "elegido": "reglas_brainstorming",
    "criterio_del_encargo": "que procedimiento es el mas completo y cierra mas motivos de la "
                            "tabla de perdidas",
    "lectura_de_contenido": [
        "COBERTURA DEL ARCO DE LA SESION, contada sobre los pasos de los tres. "
        "reglas_brainstorming cubre CINCO momentos: el enunciado del problema (su paso 1), la "
        "preparacion del equipo por inmersion (su paso 3), el juego de reglas (su paso 2), la "
        "captura visual (su paso 4) y el calentamiento (su paso 5). brainstorming_divergente "
        "cubre TRES: la sala, las reglas y la captura, mas el empujon de generar. "
        "brainstorming_efectivo cubre UNO Y MEDIO: las reglas y la composicion del grupo, y NO "
        "TIENE NI UN PASO DE CAPTURA, aunque su entregable promete una sesion documentada.",

        "PIEZAS UNICAS, o sea material que ningun otro miembro del triangulo tiene. "
        "reglas_brainstorming tiene DOS: la inmersion previa de campo y el calentamiento con "
        "ejercicio nombrado. brainstorming_efectivo tiene DOS: la composicion social del grupo "
        "y la separacion de sesiones. brainstorming_divergente tiene CERO: la sala sin "
        "distracciones es su unico gesto propio y es un calificativo del espacio, no un "
        "procedimiento.",

        "LO QUE CIERRA LA TABLA DE PERDIDAS, que es el criterio literal del encargo. La tabla "
        "de este plan clasifica NUEVE piezas como VIAJA, y ninguna de las nueve es un momento "
        "entero de la sesion: son una sala, tres reglas, un acto de generar, una composicion "
        "de grupo, una separacion de sesiones y dos glosas. Con brainstorming_efectivo vivo "
        "habria que injertarle ademas el enunciado del problema, la inmersion, la captura "
        "visual y el calentamiento, que son CUATRO momentos completos de los que no tiene "
        "ninguno. El mas completo deja menos trabajo de injerto, y esa es la misma cuenta dicha "
        "dos veces.",

        "EL DESEMPATE POR ENTREGABLE, que es la senal de verificacion del 9.6.2. "
        "reglas_brainstorming entrega ideas capturadas en Post-its Y AGRUPADAS POR TEMA; "
        "brainstorming_divergente entrega una coleccion documentada visualmente; "
        "brainstorming_efectivo entrega una sesion documentada sin decir con que. El que "
        "entrega mas lejos es el que lleva mas procedimiento.",
    ],
    "cableado_solo_como_desempate": {
        "usado_para_decidir": False,
        "por_que_se_cita": "porque va EN CONTRA del elegido, y un desempate que se ignora se "
                           "escribe, no se esconde",
        "instrumento": "scripts/loop/vuelta38_triangulos.py, salida "
                       "docs/loop/SALIDA_V38_TRIANGULOS.txt, bloques 1 y 4",
        "grados_medidos_hoy": {
            "brainstorming_efectivo": 13,
            "reglas_brainstorming": 11,
            "brainstorming_divergente": 4,
        },
        "lectura": "TRECE CONTRA ONCE, y pierde el trece. Es la forma dura de P.8, la misma del "
                   "acto II del racimo del pivote, donde pivote_o_proceder sobrevivio con 5 "
                   "contra 10 por llevar material propio.",
        "coste_medido_de_ir_contra_el_cableado": "CERO aristas. Las trece de "
                                                 "brainstorming_efectivo son reciprocas, las "
                                                 "trece, asi que las trece se redirigen solas "
                                                 "al superviviente. Medido en el bloque 2 de "
                                                 "SALIDA_V38_TRIANGULOS.txt. El cableado no "
                                                 "solo no decide: aqui no cuesta nada.",
    },
}

PERDIDAS_TALLER = [
    {"pieza": "el espacio dedicado sin distracciones", "de": "brainstorming_divergente",
     "clase": "VIAJA", "destino": "paso 1 del resultado",
     "motivo": "el superviviente no nombra el espacio en ninguno de sus cinco pasos"},

    {"pieza": "diferir el juicio", "de": "brainstorming_divergente y brainstorming_efectivo",
     "clase": "VIVE DENTRO", "destino": "paso 3 del resultado, ya estaba",
     "motivo": "es la primera regla del paso 2 del superviviente"},

    {"pieza": "ir por cantidad", "de": "brainstorming_divergente",
     "clase": "VIVE DENTRO", "destino": "paso 3 del resultado, ya estaba",
     "motivo": "el superviviente ya manda ir por cantidad; viaja solo el matiz sobre calidad"},

    {"pieza": "las ideas descabelladas", "de": "brainstorming_efectivo",
     "clase": "VIVE DENTRO", "destino": "paso 3 del resultado, ya estaba",
     "motivo": "el superviviente ya manda fomentar ideas locas"},

    {"pieza": "la regla de construir sobre las ideas de otros, y su prioridad sobre generar "
              "ideas propias aisladas",
     "de": "brainstorming_divergente y brainstorming_efectivo",
     "clase": "VIAJA", "destino": "paso 3 del resultado",
     "motivo": "ES LA UNICA REGLA DEL TRIANGULO QUE EL SUPERVIVIENTE NO DICE, medido sobre sus "
               "cinco pasos. Viaja LA LINEA. El PROCEDIMIENTO de esa linea NO se injerta porque "
               "vive en construir_sobre_ideas_ajenas, que queda VIVO fuera de la fusion y "
               "enlazado por P.10: injertarlo seria fabricar la repeticion nueva contra la que "
               "P.13 avisa"},

    {"pieza": "hacer las reglas VISIBLES", "de": "brainstorming_efectivo",
     "clase": "VIAJA", "destino": "paso 3 del resultado",
     "motivo": "el superviviente manda establecerlas y hacerlas cumplir, no visibilizarlas"},

    {"pieza": "mantenerse enfocado en el tema", "de": "brainstorming_efectivo",
     "clase": "VIAJA", "destino": "paso 3 del resultado",
     "motivo": "el superviviente centra el ENUNCIADO al principio pero no manda sostener el "
               "foco durante la sesion"},

    {"pieza": "generar el mayor numero de ideas sin filtrar prematuramente",
     "de": "brainstorming_divergente",
     "clase": "VIAJA", "destino": "paso 7 del resultado",
     "motivo": "el superviviente lo tiene como REGLA y no como PASO: no hay en el ningun "
               "momento en que efectivamente se genere"},

    {"pieza": "el registro visual y la pizarra como soporte", "de": "brainstorming_divergente",
     "clase": "VIVE DENTRO", "destino": "paso 5 del resultado, ya estaba",
     "motivo": "el superviviente ya captura y mueve en Post-its; viaja solo el soporte alterno"},

    {"pieza": "formar grupos donde los participantes se conozcan y tengan confianza mutua",
     "de": "brainstorming_efectivo",
     "clase": "VIAJA", "destino": "paso 1 y condicion 4 del resultado",
     "motivo": "ningun otro miembro del triangulo habla de quien compone el grupo"},

    {"pieza": "separar las sesiones de generar de las de seleccionar",
     "de": "brainstorming_efectivo",
     "clase": "VIAJA", "destino": "paso 7 del resultado",
     "motivo": "el superviviente no menciona la convergencia en ninguna parte"},

    {"pieza": "que la cosecha se filtra despues, en la fase de convergencia",
     "de": "brainstorming_divergente",
     "clase": "VIAJA", "destino": "entregable y resumen del resultado",
     "motivo": "el entregable del superviviente se queda en las ideas agrupadas y no dice a "
               "donde van"},

    {"pieza": "que sin reglas la sesion degenera en reunion ordenada o en caos improductivo",
     "de": "brainstorming_efectivo",
     "clase": "VIAJA", "destino": "resumen del resultado",
     "motivo": "es el por que de las reglas, y el superviviente solo las enumera"},

    {"pieza": "que el brainstorming no es la unica tecnica de ideacion",
     "de": "brainstorming_divergente",
     "clase": "YA NO APLICA", "destino": "se retira",
     "motivo": "es un encuadre del libro sobre el lugar de la tecnica, no material del "
               "procedimiento, y no hay linea del superviviente donde colgarlo sin inventarsela"},
]

ELECCION_ALTERNANCIA = {
    "regla": "P.8, EL CABLEADO DESEMPATA, NO DECIDE.",
    "decide": "EL CONTENIDO",
    "elegido": "pensamiento_convergente_divergente",
    "criterio_del_encargo": "que procedimiento es el mas completo y cierra mas motivos de la "
                            "tabla de perdidas",
    "lectura_de_contenido": [
        "ES EL UNICO DE LOS TRES QUE TIENE LOS DOS MOVIMIENTOS, y esto solo decide. "
        "generar_multiples_opciones solo abre: sus tres pasos son generar, ponerle plazo a "
        "generar y cruzar lo generado. design_attitude_vs_decision_attitude solo abre: aceptar "
        "la ambiguedad, explorar, alternar y no quedarse con la primera. "
        "pensamiento_convergente_divergente ABRE Y CIERRA: el embudo que estrecha (su paso 2) y "
        "el descarte de ideas prometedoras (su paso 4) no estan en ninguno de los otros dos. Un "
        "triangulo que se llama LA ALTERNANCIA no puede quedar en manos de un nodo que solo "
        "sabe divergir.",

        "LA UNICA DISCIPLINA QUE SE REPITE EN EL TIEMPO, que por el informe 67.6 es lo que "
        "convierte un paso en PROCEDIMIENTO. Su paso 3 manda alternar CONSCIENTEMENTE entre "
        "fases a lo largo del proyecto, y su resumen anade que cada iteracion es menos amplia y "
        "mas detallada que la anterior. Los otros dos describen UN momento: una fase de "
        "ideacion con su plazo, y una mentalidad.",

        "EL ENTREGABLE ES EL QUE MAS LEJOS LLEGA, senal de verificacion del 9.6.2. "
        "pensamiento_convergente_divergente entrega UN MAPA O REGISTRO DE ITERACIONES A LO "
        "LARGO DEL PROYECTO, o sea un documento que dura; generar_multiples_opciones entrega un "
        "set de 3 a 5 alternativas, o sea el producto de un momento; "
        "design_attitude_vs_decision_attitude entrega MENTALIDAD Y PROCESO DE TRABAJO, que no "
        "es documento, y por eso no puede ser el entregable de la cabeza.",

        "LO QUE CIERRA LA TABLA DE PERDIDAS. La tabla de este plan clasifica OCHO piezas como "
        "VIAJA, y ninguna de las ocho es un movimiento entero: son un plazo, un cruce de ideas, "
        "tres matices de la exploracion, una actitud y dos glosas. Con cualquiera de los otros "
        "dos vivo habria que injertarle el embudo Y el descarte de ideas prometedoras, que son "
        "las dos mitades del cierre, y un nodo al que hay que injertarle la mitad de su propio "
        "nombre no era la cabeza.",
    ],
    "cableado_solo_como_desempate": {
        "usado_para_decidir": False,
        "por_que_se_cita": "porque COINCIDE con el contenido, y una coincidencia que no se "
                           "declara se lee despues como si hubiera sido la razon",
        "instrumento": "scripts/loop/vuelta38_triangulos.py, salida "
                       "docs/loop/SALIDA_V38_TRIANGULOS.txt, bloques 1 y 4",
        "grados_medidos_hoy": {
            "pensamiento_convergente_divergente": 5,
            "generar_multiples_opciones": 3,
            "design_attitude_vs_decision_attitude": 2,
        },
        "lectura": "CINCO CONTRA TRES Y CONTRA DOS. Dos aristas de margen sobre el segundo, o "
                   "sea margen de los que P.8 llama margen, y con el contenido hablando tan "
                   "claro no hace falta. Se cita y no se usa.",
        "coste_medido_de_la_eleccion": "CERO aristas: las de los dos absorbidos son reciprocas "
                                       "y se redirigen solas.",
    },
}

PERDIDAS_ALTERNANCIA = [
    {"pieza": "generar deliberadamente multiples alternativas antes de elegir una",
     "de": "generar_multiples_opciones",
     "clase": "VIVE DENTRO", "destino": "paso 1 del resultado, ya estaba",
     "motivo": "es el paso 1 del superviviente dicho con otras palabras; viaja el adverbio"},

    {"pieza": "dedicar tiempo Y ENERGIA a explorar antes de converger",
     "de": "design_attitude_vs_decision_attitude",
     "clase": "VIVE DENTRO", "destino": "paso 1 del resultado, ya estaba",
     "motivo": "el superviviente ya manda dedicar tiempo explicito; viaja la energia"},

    {"pieza": "el deadline claro para la fase de divergencia, y la paralisis por analisis",
     "de": "generar_multiples_opciones",
     "clase": "VIAJA", "destino": "paso 2 del resultado",
     "motivo": "el superviviente manda divergir y no le pone freno en ninguno de sus pasos"},

    {"pieza": "la polinizacion cruzada entre ideas distintas",
     "de": "generar_multiples_opciones",
     "clase": "VIAJA", "destino": "paso 4 del resultado",
     "motivo": "no esta ni en el superviviente ni en el otro donante"},

    {"pieza": "alternar entre investigacion de mercado, prototipado y generacion de forma no "
              "lineal",
     "de": "design_attitude_vs_decision_attitude",
     "clase": "VIAJA", "destino": "paso 5 del resultado",
     "motivo": "el superviviente alterna entre GENERAR y SELECCIONAR y no nombra ninguna de "
               "esas tres actividades"},

    {"pieza": "evitar adoptar la primera solucion razonable",
     "de": "design_attitude_vs_decision_attitude",
     "clase": "VIAJA", "destino": "paso 6 del resultado",
     "motivo": "el superviviente lo dice en su resumen, que la cultura occidental favorece la "
               "convergencia rapida, y no lo tiene como paso"},

    {"pieza": "aceptar la ambiguedad y la incertidumbre como parte del proceso",
     "de": "design_attitude_vs_decision_attitude",
     "clase": "VIAJA", "destino": "paso 7 del resultado",
     "motivo": "no esta en el superviviente"},

    {"pieza": "el set documentado de al menos 3 a 5 alternativas evaluadas",
     "de": "generar_multiples_opciones",
     "clase": "VIAJA", "destino": "entregable del resultado",
     "motivo": "el entregable del superviviente cuenta ciclos y no cuenta alternativas"},

    {"pieza": "el contraste ACTITUD DE DISENO contra ACTITUD DE DECISION de Collopy y Boland, "
              "con el Design Squiggle de Damien Newman",
     "de": "design_attitude_vs_decision_attitude",
     "clase": "VIAJA", "destino": "resumen del resultado",
     "motivo": "ES LA PIEZA MAS CARA DE ESTA FUSION: un concepto con autores nombrados y con su "
               "figura. Perderla seria borrar material atribuido"},

    {"pieza": "que los plazos ponen un limite productivo a la exploracion, y que no conformarse "
              "con la primera buena idea separa lo incremental de lo verdaderamente creativo",
     "de": "generar_multiples_opciones",
     "clase": "VIAJA", "destino": "resumen del resultado",
     "motivo": "es el por que del paso 2 que viaja; sin el, la orden del deadline queda sin "
               "motivo escrito"},

    {"pieza": "mentalidad y proceso de trabajo del equipo, como ENTREGABLE",
     "de": "design_attitude_vs_decision_attitude",
     "clase": "YA NO APLICA", "destino": "se retira del entregable; su contenido vive en el "
                                         "resumen",
     "motivo": "una mentalidad no es un documento y el superviviente entrega uno. Retirarla del "
               "entregable no pierde material: viaja entero al resumen"},
]

RESUMEN_TALLER = (
    "Conjunto de reglas para maximizar la generación de ideas útiles en sesiones de lluvia de "
    "ideas: mantener el foco en un problema bien definido (idealmente centrado en la necesidad "
    "del cliente), diferir el juicio crítico, mantener una sola conversación a la vez, "
    "priorizar cantidad, pensar visualmente (Post-it) y fomentar ideas alocadas. Incluye un "
    "ejercicio de calentamiento ('Silly Cow') para desbloquear la creatividad. Las reglas no "
    "son decorado: sin ellas la sesión degenera en reunión ordenada o en caos improductivo, y "
    "la más importante de todas es construir sobre las ideas de los demás, que genera un efecto "
    "acumulativo de creatividad superior al trabajo individual. La sesión pertenece a la fase "
    "divergente: abre el espectro de opciones y su cosecha se filtra después, en la fase de "
    "convergencia."
)

RESUMEN_ALTERNANCIA = (
    "El design thinking se experimenta como una danza entre cuatro estados mentales, siendo el "
    "más fundamental el intercambio rítmico entre pensamiento divergente (multiplicar opciones, "
    "crear posibilidades) y pensamiento convergente (elegir entre alternativas existentes, "
    "eliminar opciones). La cultura occidental tiende a favorecer la convergencia rápida, pero "
    "la innovación requiere primero divergir ampliamente antes de converger. Cada iteración del "
    "proceso es menos amplia y más detallada que la anterior. No conformarse con la primera "
    "buena idea es lo que separa las soluciones incrementales y fácilmente copiables de las "
    "verdaderamente creativas, y los plazos ayudan a poner un límite productivo a esa "
    "exploración. Detrás hay un contraste que Collopy y Boland nombraron: la actitud de "
    "decisión asume que generar alternativas es fácil y elegir entre ellas es difícil, mientras "
    "que la actitud de diseño asume que diseñar una alternativa sobresaliente es difícil pero "
    "que, una vez lograda, elegirla es trivial. Innovar pide actitud de diseño: exploración "
    "iterativa, prototipado y tolerancia a la ambigüedad, representada visualmente en el Design "
    "Squiggle de Damien Newman."
)
