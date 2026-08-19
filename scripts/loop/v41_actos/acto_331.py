# -*- coding: utf-8 -*-
"""ACTO 331 de OP-D-06: analisis_de_gastos_de_capital con propuesta_gasto_capital.

LO UNICO TECLEADO: los grupos, sus motivos y la lectura. La medicion la hace
scripts/loop/vuelta41_plan_acto.py contra el grafo.
"""

SUP = "analisis_de_gastos_de_capital"
ABS = ["propuesta_gasto_capital"]
PREF = {"A": SUP, "P": ABS[0]}

OPERACION = ("OP-D-06, ACTO 2 DE NUEVE (puesto 331): analisis_de_gastos_de_capital "
             "absorbe a propuesta_gasto_capital")

ESTADO = ("SELLADO en la vuelta 42, 19 ago 2026, ANTES de ejecutar. El destejido "
          "del acto quedo declarado SIN COSTURA QUE DESTEJER en los dos nodos, y "
          "aqui la declaracion es MAS FUERTE que en el acto 285: los DOS estan "
          "FUERA de la cola de 1.495 que el instrumento entrego, o sea que el "
          "instrumento NO CITA a ninguno de los dos. Y la razon del archivo, que "
          "SI describia una costura en propuesta_gasto_capital (doce pasos "
          "partidos por la mitad, del seis al doce un caso de negocio de sistemas "
          "de hardware y software), esta RANCIA EN ESE DETALLE porque esa costura "
          "YA SE DESTEJIO: OP-F-03 mando su bloque 6 a 12 a "
          "tecnologia_como_medio_no_fin (docs/plan/01_FUENTES.md, tabla del tercer "
          "desenlace) y el nodo mide HOY CINCO pasos, que son exactamente los "
          "cinco primeros que aquella razon llamaba el analisis generico de capex. "
          "La regla de fuente primero queda satisfecha POR PRECEDENCIA, con "
          "OP-F-03 HECHA en su nota 3376 SI segun la apertura de esta vuelta.")

REGLA = ("OP-D-06 de docs/plan/02_DESTEJIDOS.md, LOS NUEVE ACTOS DE DOS, acto del "
         "puesto 331 de su tabla sellada. Este acto NO tiene reparto escrito (solo "
         "lo tienen el 392 y el 341), asi que se resuelve con la regla adjudicada "
         "el 11 ago 2026: cada perdida al bloque del que proviene, y la que no "
         "tenga bloque al superviviente.")

MOTIVO = ("El acto se leyo ENTERO por P.5 y es UNA familia de DOS: el par 331 es A "
          "en el archivo y los cuatro pares que meten un tercero (869, 1225, 1406, "
          "1533) son los cuatro D. CERO terceros de clase A, asi que el acto es de "
          "dos, como la tabla sellada dice. CERO pares vuelven a la cola de "
          "relectura post fusion, porque entre los cuatro terceros no hay ni un B "
          "ni un C. LA FUENTE, DICHA COMO SE MIDE Y NO COMO CONVIENE: el "
          "instrumento medira DOS cadenas de fuente distintas y por eso imprimira "
          "FUENTE MIXTA, pero las dos cadenas nombran EL MISMO LIBRO, Financial "
          "Intelligence for Entrepreneurs; lo unico que las separa es que la del "
          "superviviente trae ademas a sus autores (Berman, Karen; Knight, Joe) y "
          "la del absorbido no. No es un cruce de libros: es la misma pagina "
          "citada con dos precisiones distintas.")

# ---------------------------------------------------------------------------
# LOS GRUPOS. Doce origenes en CINCO pasos y DOS condiciones, dentro del
# estandar de 3 a 6.
# ---------------------------------------------------------------------------
GRUPOS_PASOS = [
    (["A1", "P1"],
     "Determina el desembolso inicial de efectivo incluyendo todos los costos "
     "asociados de la inversión: compra, envío, instalación, capacitación e "
     "interrupciones operativas (downtime)",
     "LA MISMA ACCION CON LAS DOS LISTAS DE COSTOS, y ninguna de las dos era "
     "completa sola: el superviviente traia la capacitacion y las interrupciones "
     "operativas, el donante traia el envio y el downtime. La accion es literal en "
     "los dos (reunir TODOS los costos, no solo el precio de compra) y lo que "
     "viaja del donante son las dos partidas que al superviviente le faltaban. "
     "Juntas, la lista deja de tener huecos, que es justo lo que este paso existe "
     "para evitar."),
    (["A2", "P2", "A4"],
     "Proyecta de forma conservadora los flujos de efectivo futuros que generará "
     "la inversión, en términos de ahorro de costos o de ingresos adicionales, e "
     "involucra en esas proyecciones a los empleados y gerentes con conocimiento "
     "técnico",
     "LA MISMA PROYECCION CON SU CAUTELA, SU CONTENIDO Y SU AUTOR. El "
     "superviviente decia COMO proyectar (de forma conservadora) y no decia EN QUE "
     "se miden los flujos; el donante dice que se miden en ahorro o ingresos "
     "adicionales. Y la tercera pieza es del superviviente y modifica esta misma "
     "accion y ninguna otra: QUIEN proyecta. Por P.11 involucrar a quien tiene el "
     "conocimiento tecnico califica el procedimiento de proyectar en vez de anadir "
     "un paso suelto, y por eso entra aqui y no tiene grupo propio."),
    (["A3", "P3", "P4"],
     "Evalúa los flujos proyectados con métodos financieros: calcula el NPV usando "
     "el hurdle rate de tu empresa, y respáldalo con el payback y el IRR",
     "EL MISMO PASO CON SU UMBRAL Y SU JERARQUIA. El superviviente nombraba los "
     "tres metodos (payback, NPV y/o IRR) y los dejaba al mismo nivel y sin vara; "
     "el donante trae las dos cosas que faltaban: CONTRA QUE se calcula el NPV (el "
     "hurdle rate de la empresa, que es el numero sin el cual el NPV no decide "
     "nada) y QUE PAPEL juegan los otros dos (respaldo adicional, no criterio "
     "principal). Un metodo sin su umbral es una cuenta, no una decision."),
    (["P5"],
     "Redacta la propuesta de inversión incluyendo los riesgos, los supuestos y un "
     "análisis de sensibilidad",
     "PIEZA PROPIA DEL DONANTE, sin equivalente en el superviviente: es el UNICO "
     "paso del acto que convierte el analisis en un DOCUMENTO que alguien de fuera "
     "puede leer y juzgar, y el unico que nombra la sensibilidad. Viaja entero y "
     "solo, y por eso tiene grupo propio en vez de disolverse dentro de otro."),
    (["A5"],
     "Toma la decisión de inversión basada en el análisis, no al revés: el análisis "
     "no se hace para justificar una decisión que ya estaba tomada",
     "PIEZA PROPIA DEL SUPERVIVIENTE, y es una ADVERTENCIA y no un procedimiento: "
     "por P.11 viaja ENTERA, porque una advertencia es lo mas facil de perder en "
     "una fusion y lo mas caro de recuperar. Va la ultima a proposito: es la regla "
     "que ordena a las otras cuatro, y sin ella los cuatro pasos anteriores se "
     "pueden hacer enteros al servicio de una decision ya tomada."),
]

GRUPOS_CONDICIONES = [
    (["AC1"],
     "Cuando tu empresa debe decidir sobre la compra de equipo, una expansión, una "
     "adquisición o el desarrollo de un nuevo producto que involucre una inversión "
     "significativa de efectivo",
     "EL DISPARADOR DE DECISION, y es propio del superviviente. Se queda solo "
     "porque NO es la misma condicion que la del donante: esta se enciende cuando "
     "hay que DECIDIR si se invierte."),
    (["PC1"],
     "Cuando necesitas solicitar financiamiento para un activo o un proyecto de "
     "capital",
     "EL DISPARADOR DE FINANCIAMIENTO, y es propio del donante. Se resiste la "
     "tentacion de juntarlo con el anterior: decidir si conviene invertir y "
     "necesitar que alguien te preste para hacerlo son DOS momentos distintos, y "
     "el segundo puede llegar con la decision ya tomada. Fundirlos borraria una "
     "senal en vez de resumirla."),
]

ENTREGABLE = ("Un análisis completo de gasto de capital con el desembolso inicial, "
              "los flujos proyectados y la evaluación de retorno por NPV, payback e "
              "IRR, redactado como propuesta de inversión con sus riesgos, "
              "supuestos y análisis de sensibilidad, listo para presentar a un "
              "banco o inversionista")

RESUMEN = (
    "Proceso estructurado para decidir si vale la pena una inversión grande de "
    "capital y para pedir el financiamiento que necesita: (1) determinar el "
    "desembolso inicial de efectivo con todos sus costos, (2) proyectar de forma "
    "conservadora los flujos de efectivo futuros que generará, y (3) evaluar esos "
    "flujos con payback, NPV o IRR para decidir si la inversión es rentable. El "
    "mismo análisis, redactado con sus riesgos, supuestos y análisis de "
    "sensibilidad, es la propuesta que se lleva a un banco o inversionista. Y la "
    "regla que ordena todo lo demás: la decisión se toma con el análisis, no al "
    "revés.")

PRESERVAR = [
    "hurdle rate",
    "downtime",
    "capacitación",
    "interrupciones operativas",
    "análisis de sensibilidad",
    "no al revés",
    "banco o inversionista",
    "payback",
    "NPV",
    "IRR",
]

RASTROS = [
    "desembolso inicial",
    "flujos de efectivo",
    "conservadora",
    "propuesta",
    "sensibilidad",
]

ELECCION_P8 = {
    "regla": ("P.8, EL CABLEADO DESEMPATA, NO DECIDE. Donde el contenido dice algo "
              "manda el contenido, aunque el margen de aristas apunte al otro lado."),
    "decide": "EL CONTENIDO",
    "elegido": SUP,
    "especie_de_9_3_1": ("POR ELEGIR. La razon del unico par A del acto (el 331) NO "
                         "nombra ganador: la vara del verbo da NO. No hay GANADOR "
                         "POR DERECHO, asi que la eleccion es de P.8."),
    "lectura_de_contenido": [
        "1. EL TITULO DE UNO ES EL CONCEPTO Y EL DEL OTRO ES UN PROCEDIMIENTO SOBRE "
        "ESE CONCEPTO, exactamente la misma forma que decidio el acto 285. "
        "analisis_de_gastos_de_capital se titula 'Analisis de Gastos de Capital "
        "(Capital Expenditure Analysis)', que ES el nombre del eje; "
        "propuesta_gasto_capital se titula 'Guia paso a paso para analizar gastos "
        "de capital (ROI)', y su propio titulo APUNTA AL DEL OTRO con la "
        "preposicion delante: es una guia PARA ANALIZAR gastos de capital. La "
        "cabeza de una serie es el nodo cuyo titulo ES el eje, no el que dice como "
        "recorrerlo.",
        "2. EL GRAFO LO TIENE DE EJE DE SU FAMILIA, y P.8 cuenta el cableado "
        "declarado como contenido cuando dibuja una jerarquia y no solo un numero. "
        "analisis_de_gastos_de_capital cuelga de valor_del_dinero_en_el_tiempo y "
        "tasa_de_retorno_requerida (los DOS prerrequisitos conceptuales del capex) "
        "y de el cuelgan metodo_payback, metodo_valor_presente_neto y "
        "tasa_interna_retorno_irr (los TRES metodos que este mismo acto nombra en "
        "su paso 3). O sea que el grafo ya lo tiene puesto como el nodo del que los "
        "tres metodos son hijos. propuesta_gasto_capital cuelga de "
        "comparacion_metodos_inversion y lleva a gestion_capital_trabajo: esta al "
        "lado de la familia, no en su centro.",
        "3. LA PIEZA QUE ORDENA A TODAS LAS DEMAS ES SUYA: 'Tomar la decision de "
        "inversion basada en el analisis, no al reves'. Es la advertencia contra la "
        "racionalizacion, la unica linea del acto que dice para que NO sirve todo "
        "el procedimiento, y vive solo en el superviviente. Elegir al otro la "
        "convertiria en una linea prestada dentro de un documento de propuesta, que "
        "es justo el sitio donde menos se lee.",
        "4. EL OBJETO DE CADA UNO, leido en su entregable: el superviviente entrega "
        "UN ANALISIS (desembolso, flujos, evaluacion de retorno) y el donante "
        "entrega UN DOCUMENTO PARA UN TERCERO (la propuesta lista para el banco). "
        "El analisis existe sin la propuesta; la propuesta no existe sin el "
        "analisis. Lo que se puede tener solo es la cabeza.",
        "5. PIEZAS PROPIAS DEL DONANTE QUE NADIE MAS TIENE, y por eso viajan "
        "enteras: el hurdle rate como vara del NPV, el papel de respaldo del "
        "payback y del IRR, el envio y el downtime en la lista de costos, y el paso "
        "entero de redactar la propuesta con riesgos, supuestos y sensibilidad. "
        "Ninguna de las cuatro depende de que el donante sobreviva: dependen de que "
        "el plan las mande viajar, y este las manda.",
    ],
    "cableado_solo_como_desempate": {
        "usado_para_decidir": False,
        "va_a_favor_del_elegido": True,
        "por_que_se_cita": ("PORQUE ESTA VEZ VA A FAVOR DEL ELEGIDO Y ESO TAMBIEN "
                            "HAY QUE DECIRLO. Medido hoy: "
                            "analisis_de_gastos_de_capital tiene grado 5 y "
                            "propuesta_gasto_capital tiene grado 2. Las dos varas "
                            "coinciden, y cuando coinciden la regla NO SE LUCE: la "
                            "que mandaba era la primera, y se deja escrito para que "
                            "nadie le atribuya al cableado una decision que ya "
                            "estaba tomada por el contenido. Contraste util: en el "
                            "acto 285 las dos varas se separaron y el cableado "
                            "perdio."),
        "instrumento": ("scripts/loop/vuelta41_lectura_acto.py --puesto 331, salida "
                        "docs/loop/SALIDA_V42_ACTO331_LECTURA.txt, bloque (e)"),
        "grados_medidos_hoy": {SUP: 5, ABS[0]: 2},
        "coste_medido_de_la_eleccion": ("CERO aristas. Los dos nodos tienen CERO "
                                        "aristas propias sin reciproco, asi que "
                                        "elegir a cualquiera de los dos no pierde "
                                        "ni una arista: las reciprocas las "
                                        "reescribe la simetrizacion de run_phase1 "
                                        "paso 5."),
    },
}
