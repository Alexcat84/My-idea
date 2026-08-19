# -*- coding: utf-8 -*-
"""ACTO 285 de OP-D-06: producto_unico_superior con superioridad_producto_beneficios.

LO UNICO TECLEADO: los grupos, sus motivos y la lectura. La medicion la hace
scripts/loop/vuelta41_plan_acto.py contra el grafo.
"""

SUP = "producto_unico_superior"
ABS = ["superioridad_producto_beneficios"]
PREF = {"P": SUP, "B": ABS[0]}

OPERACION = ("OP-D-06, ACTO 1 DE NUEVE (puesto 285): producto_unico_superior "
             "absorbe a superioridad_producto_beneficios")

ESTADO = ("SELLADO en la vuelta 41, 19 ago 2026, ANTES de ejecutar. El destejido "
          "del acto quedo declarado SIN COSTURA QUE DESTEJER en los dos nodos: el "
          "instrumento de costuras CITA a los dos por bloque (45,4 con corte tras "
          "3 y 44,7 con corte tras 4) y NINGUNO por pareja, y la lectura textual "
          "con el texto delante dice que en los dos el segundo bloque CONTINUA al "
          "primero en vez de volver a contarlo. La cita queda registrada en la "
          "cola, como manda la practica adjudicada en el acta 40.")

REGLA = ("OP-D-06 de docs/plan/02_DESTEJIDOS.md, LOS NUEVE ACTOS DE DOS, acto del "
         "puesto 285 de su tabla sellada. Este acto NO tiene reparto escrito (solo "
         "lo tienen el 392 y el 341), asi que se resuelve con la regla adjudicada "
         "el 11 ago 2026: cada perdida al bloque del que proviene, y la que no "
         "tenga bloque al superviviente.")

MOTIVO = ("El acto se leyo ENTERO por P.5 y es UNA familia de DOS: el par 285 es A "
          "en el archivo y los cuatro pares que meten un tercero (163, 461, 835, "
          "1390) son D, D, B y D. CERO terceros de clase A, asi que el acto es de "
          "dos, como la tabla sellada dice. Los dos nodos son de la MISMA fuente, "
          "Winning at New Products de Robert G. Cooper: NO es acto de fuente mixta. "
          "El par 835 (brief_competitivo con producto_unico_superior, clase B) "
          "vuelve a la cola de relectura post fusion porque el superviviente cambia "
          "de texto.")

# ---------------------------------------------------------------------------
# LOS GRUPOS. Doce origenes en SEIS pasos, dentro del estandar de 3 a 6.
# ---------------------------------------------------------------------------
GRUPOS_PASOS = [
    (["P1", "B2"],
     "Haz un estudio de necesidades y deseos con tus clientes desde el inicio del "
     "proyecto, saliendo a escucharlos con una investigación de voz del cliente, "
     "VoC, para descubrir sus necesidades y no solo sus deseos",
     "LA MISMA ACCION EN EL MISMO MOMENTO, y del donante viaja lo que le faltaba "
     "al superviviente: EL NOMBRE DEL INSTRUMENTO (voz del cliente, VoC) y la "
     "distincion entre necesidades y deseos, que es la que hace util el estudio. "
     "El superviviente decia QUE hacer y CUANDO; el donante dice COMO se llama y "
     "QUE se busca."),
    (["P2", "P3"],
     "Busca necesidades que tu cliente ni siquiera sabe nombrar, no solo lo obvio "
     "que ya te pide, y descubre qué es lo que realmente le importa a la hora de "
     "decidir",
     "LAS DOS CARAS DE LA MISMA INDAGACION: lo que el cliente no sabe pedir y lo "
     "que de verdad pesa cuando compra. Y ES EXACTAMENTE LA PAREJA QUE EL "
     "INSTRUMENTO DE COSTURAS CITA en este nodo (pasos 2 y 3, similitud 52,7). "
     "Esa cita NO disparo por pareja, porque el umbral es 80: no es una costura "
     "probada, es una cita. La fusion es el momento en que se resuelve, y "
     "resolverla juntando dos pasos del superviviente NO es destejer nada: "
     "destejer es partir un nodo en dos, y esto es lo contrario."),
    (["P4", "B1"],
     "Define tu producto como un conjunto de beneficios para el cliente y no como "
     "una lista de características técnicas, teniendo clara la diferencia: las "
     "características (features) te cuestan dinero a ti, y los beneficios "
     "(benefits) son lo que tu cliente realmente compra",
     "EL SUPERVIVIENTE DABA LA ORDEN Y EL DONANTE DA EL PORQUE. Definir por "
     "beneficios sin la distincion features contra benefits es una consigna; con "
     "ella es un criterio que se puede aplicar. Las dos palabras inglesas viajan "
     "literales porque son el vocabulario con el que el lector va a reconocer la "
     "idea en cualquier otra pagina."),
    (["P5", "B3", "B4"],
     "Compara directamente lo que ofreces contra la competencia en beneficios "
     "percibidos, valor por el dinero y calidad: desarma sus productos y encuentra "
     "sus puntos débiles, y no te quedes con la foto de hoy, imagina cómo "
     "evolucionará el producto de tu competidor en el futuro",
     "EL MISMO PASO CON SU METODO Y SU HORIZONTE. El superviviente decia CONTRA "
     "QUE comparar (los tres ejes) y no decia COMO; el donante trae el como "
     "(desarmar el producto) y ademas el aviso que ninguno de los dos tenia dos "
     "veces: que la comparacion contra la foto de hoy caduca."),
    (["P6", "B5"],
     "Traduce todo lo que encuentres en una definición de tu producto centrada en "
     "beneficios y en tu propuesta de valor, y revisa si esa propuesta depende "
     "solo del precio bajo o si también conecta con lo que tu cliente siente y "
     "necesita, aunque eso cambie con el tiempo",
     "EL CIERRE DEL PROCEDIMIENTO, dicho por los dos: el donante manda TRADUCIR lo "
     "aprendido a una definicion, y el superviviente manda REVISAR esa definicion "
     "contra la trampa del precio bajo. Escribir y revisar lo escrito son el mismo "
     "paso partido en dos, y juntos dicen que la propuesta de valor no es un "
     "documento que se firma sino uno que se somete a prueba."),
    (["B6"],
     "Antes de desarrollar todo, prueba la idea con usuarios reales usando "
     "prototipos simples o conceptuales (protocepts)",
     "PIEZA PROPIA DEL DONANTE, sin equivalente en el superviviente: es el UNICO "
     "paso del acto que dice que hacer ANTES de construir. Viaja entera y sola, y "
     "por eso tiene grupo propio en vez de disolverse dentro de otro."),
]

GRUPOS_CONDICIONES = [
    (["PC1", "BC2"],
     "Si tu producto se parece demasiado a los de la competencia o no logra "
     "diferenciarse claramente de ella",
     "LA MISMA CONDICION DICHA DOS VECES, una por cada nodo. Se junta en una sola "
     "porque son la misma senal vista con las mismas palabras."),
    (["PC2", "BC1"],
     "Si no tienes una propuesta de valor clara y diferenciada, o defines tu "
     "producto solo por sus características técnicas sin pensar en la mirada del "
     "cliente",
     "LA MISMA CONDICION POR SUS DOS SINTOMAS: no tener propuesta de valor es el "
     "resultado, y definir por caracteristicas tecnicas es la causa. El donante "
     "aporta la causa, que es la que se ve antes."),
]

ENTREGABLE = ("Un documento con tu propuesta de valor diferenciada, que convierte "
              "las características técnicas de tu producto en beneficios claros "
              "para el cliente, validado hablando directamente con tus clientes y "
              "mirando a la competencia")

RESUMEN = (
    "Lo que más determina si tu producto nuevo tiene éxito es que sea diferente y "
    "le ofrezca al cliente beneficios únicos con una propuesta de valor "
    "convincente. Si logras un producto superior, tienes 5 veces más probabilidad "
    "de éxito, 4 veces más participación de mercado y 4 veces más rentabilidad. "
    "Define esa superioridad desde la mirada de tu cliente, no desde lo técnico: "
    "las características (features) te cuestan dinero a ti, y los beneficios "
    "(benefits) son lo que tu cliente realmente compra y por lo que está dispuesto "
    "a pagar. Piensa en tu producto como un conjunto de beneficios para quien lo "
    "usa, no como una lista de funciones técnicas. Evita caer en copiar lo que ya "
    "existe sin diferenciarte, y evita también desarrollar una solución técnica "
    "que después sale a buscar un mercado que la quiera.")

PRESERVAR = [
    "5 veces más probabilidad de éxito",
    "4 veces más participación de mercado",
    "voz del cliente, VoC",
    "(features)",
    "(benefits)",
    "protocepts",
    "desarma sus productos",
    "valor por el dinero",
    "evolucionará el producto de tu competidor",
]

RASTROS = [
    "propuesta de valor",
    "características técnicas",
    "precio bajo",
    "competencia",
    "prototipos",
]

ELECCION_P8 = {
    "regla": ("P.8, EL CABLEADO DESEMPATA, NO DECIDE. Donde el contenido dice algo "
              "manda el contenido, aunque el margen de aristas apunte al otro lado."),
    "decide": "EL CONTENIDO",
    "elegido": SUP,
    "especie_de_9_3_1": ("POR ELEGIR. La razon del unico par A del acto (el 285) NO "
                         "nombra ganador: la vara del verbo da NO. No hay GANADOR "
                         "POR DERECHO, asi que la eleccion es de P.8."),
    "lectura_de_contenido": [
        "1. EL TITULO DE UNO ES EL SUJETO Y EL DEL OTRO ES UN PREDICADO SOBRE ESE "
        "SUJETO. producto_unico_superior se titula 'Tener un Producto Único y "
        "Superior: El Factor Número Uno de Rentabilidad'; "
        "superioridad_producto_beneficios se titula 'La superioridad de tu producto "
        "está en los beneficios, no en las características'. El segundo habla DE la "
        "superioridad que el primero nombra. La cabeza de una serie es el nodo cuyo "
        "titulo ES el eje, no el que lo califica.",
        "2. PADRE DECLARADO POR EL GRAFO, que P.8 cuenta como contenido. "
        "producto_unico_superior tiene UN previo y es "
        "'ocho_factores_exito_criticos': el nodo esta colgado, por el propio grafo, "
        "de la lista de factores criticos de Cooper, y su titulo dice cual de ellos "
        "es (el numero uno). superioridad_producto_beneficios cuelga de "
        "customer_gains, tecnologia_como_medio_no_fin y "
        "alfabetizacion_en_materiales_maliciosos, que no son esa lista.",
        "3. LA CIFRA QUE SOLO TIENE UNO. El 5 veces mas probabilidad de exito, 4 "
        "veces mas participacion de mercado y 4 veces mas rentabilidad vive SOLO en "
        "el resumen de producto_unico_superior. Es el argumento entero por el que "
        "el nodo existe, y elegir al otro obligaria a mudarlo. Se preserva igual "
        "por P.13, pero el nodo que ya lo tiene es el que lo sostiene.",
        "4. LO QUE DICE LA PROPIA RAZON DEL ARCHIVO, leida entera: 'El segundo "
        "desarrolla mas el discurso de venta segun ese posicionamiento, pero la "
        "instruccion es la misma'. El archivo describe a "
        "superioridad_producto_beneficios como un DESARROLLO del posicionamiento "
        "que el otro fija. Un desarrollo no es la cabeza.",
        "5. PIEZAS PROPIAS DEL DONANTE QUE NADIE MAS TIENE, y por eso viajan "
        "enteras: los protocepts, el desarmado del producto del competidor, la "
        "evolucion futura de ese producto y el par features contra benefits. "
        "Ninguna de las cuatro depende de que el donante sobreviva: dependen de que "
        "el plan las mande viajar, y este las manda.",
    ],
    "cableado_solo_como_desempate": {
        "usado_para_decidir": False,
        "va_a_favor_del_elegido": False,
        "por_que_se_cita": ("PORQUE VA EN CONTRA DEL ELEGIDO Y HAY QUE DECIRLO. "
                            "Medido hoy: producto_unico_superior tiene grado 6 y "
                            "superioridad_producto_beneficios tiene grado 7. El "
                            "cableado apunta al donante. P.8 dice que el cableado "
                            "DESEMPATA y NO DECIDE, asi que aqui PIERDE contra el "
                            "contenido, y se escribe que perdio en vez de "
                            "esconderlo. Es el primer acto de esta campaña en que "
                            "las dos varas se separan."),
        "instrumento": ("scripts/loop/vuelta41_lectura_acto.py --puesto 285, salida "
                        "docs/loop/SALIDA_V41_ACTO285_LECTURA.txt, bloque (e)"),
        "grados_medidos_hoy": {SUP: 6, ABS[0]: 7},
        "coste_medido_de_la_eleccion": ("CERO aristas. Los dos nodos tienen CERO "
                                        "aristas propias sin reciproco, asi que "
                                        "elegir a cualquiera de los dos no pierde "
                                        "ni una arista: las reciprocas las "
                                        "reescribe la simetrizacion de run_phase1 "
                                        "paso 5. La diferencia de UNO en el grado "
                                        "no cuesta nada."),
    },
}
