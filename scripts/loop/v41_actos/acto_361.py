# -*- coding: utf-8 -*-
"""ACTO 361 de OP-D-06: key_partners_hypothesis con partners_hypothesis_physical.

LO UNICO TECLEADO: los grupos, sus motivos y la lectura. La medicion la hace
scripts/loop/vuelta41_plan_acto.py contra el grafo.
"""

SUP = "key_partners_hypothesis"
ABS = ["partners_hypothesis_physical"]
PREF = {"K": SUP, "P": ABS[0]}

OPERACION = ("OP-D-06, ACTO 5 DE NUEVE (puesto 361): key_partners_hypothesis "
             "absorbe a partners_hypothesis_physical")

ESTADO = (
    "SELLADO en la vuelta 43, 19 ago 2026, ANTES de ejecutar. EL DESTEJIDO QUE LA "
    "RAZON PEDIA YA SE HIZO, y no aqui: lo hizo OP-F-04-WEI. La razon del archivo "
    "dice que el primero tiene CATORCE pasos y se parte con claridad, y que del "
    "seis al catorce entra otro bloque con vocabulario propio (objetivo de "
    "traccion, Critical Path, licensing, socios de distribucion y de suministro), "
    "y esta RANCIA EN ESE DETALLE. docs/plan/01_FUENTES.md linea 951 publica la "
    "frontera leida (1 a 5 contra 6 a 14) y declara ALLI MISMO que el tramo de "
    "cola traia DOS subbloques distinguibles y que decidir si eran uno o dos era "
    "lectura pendiente que no se resolvia adivinando; las lineas 983 y 984 traen "
    "esa lectura ya hecha y los DOS destinos: el bloque 6 a 10 al miembro "
    "alineacion_bd_metricas_core (evaluar socios por su capacidad de mover la "
    "metrica clave) y el 11 a 14 al miembro pipeline_alianzas_bd (clasificar por "
    "tipo segun el cuello de botella), separados A PROPOSITO. LA MEDICION DE HOY "
    "LO CONFIRMA: key_partners_hypothesis tiene CINCO pasos, que son exactamente "
    "los cinco primeros. Fuente primero satisfecha POR PRECEDENCIA, con "
    "OP-F-04-WEI HECHA en su nota 3541 SI segun la apertura de esta vuelta. LO "
    "QUE EL INSTRUMENTO SIGUE CITANDO HOY SE DICE EN VEZ DE CALLARSE: "
    "partners_hypothesis_physical esta FUERA de la cola de 1.494 y "
    "key_partners_hypothesis sigue DENTRO con bloque 50,8 y corte tras 2. Esa "
    "cita NO es la costura vieja de Weinberg, que ya no existe en el fichero, y "
    "la lectura textual con el texto delante dice que NO hay costura: los pasos "
    "1 y 2 construyen la lista y el intercambio, y los 3 a 5 juzgan al proveedor, "
    "trazan la frontera contra los recursos clave y llevan el resultado al "
    "Canvas. CONTINUAN en vez de volver a contar. La cita queda REGISTRADA en la "
    "cola y no despachada, y el auditor la relee.")

REGLA = (
    "OP-D-06 de docs/plan/02_DESTEJIDOS.md, LOS NUEVE ACTOS DE DOS, acto del "
    "puesto 361 de su tabla sellada. Este acto NO tiene reparto escrito en esa "
    "tabla (solo lo tienen el 392 y el 341), asi que se resuelve con la regla "
    "adjudicada el 11 ago 2026: cada perdida al bloque del que proviene, y la que "
    "no tenga bloque al superviviente.")

MOTIVO = (
    "El acto se leyo ENTERO por P.5 y es UNA familia de DOS: el par 361 es A en "
    "el archivo y los DOS pares que meten un tercero son el 427 (D) y el 599 (B). "
    "CERO terceros de clase A, asi que el acto es de dos, como la tabla sellada "
    "dice. Y AQUI SI HAY RELECTURA POST FUSION, la primera de esta vuelta: el par "
    "599 (asociaciones_clave con key_partners_hypothesis) es clase B y su nodo "
    "cambia de texto al absorber, asi que VUELVE A LA COLA y se relee al cierre "
    "del acto como manda 08_VERIFICACION. LA FUENTE, DICHA COMO SE MIDE: esta vez "
    "el instrumento imprimira FUENTE UNICA, porque las dos cadenas son "
    "IDENTICAS ('The Startup Owner's Manual - Steve Blank'). Es el primer acto de "
    "OP-D-06 en el que la etiqueta sale unica, y se deja escrito porque los tres "
    "anteriores (331, 341 y 344) salieron MIXTA por diferencias de forma y no de "
    "libro: aqui se ve que la etiqueta funciona cuando las cadenas calzan.")

# ---------------------------------------------------------------------------
# LOS GRUPOS. Doce origenes en SEIS pasos y DOS condiciones, dentro del
# estandar de 3 a 6.
# ---------------------------------------------------------------------------
GRUPOS_PASOS = [
    (["K1", "P2", "P4"],
     "Lista los socios potenciales, los primarios y sus candidatos suplentes, "
     "clasificados en los cuatro tipos: alianzas estratégicas, coopetición, "
     "desarrollo conjunto de negocio y relaciones con proveedores clave",
     "LA MISMA LISTA CON SUS CUATRO TIPOS NOMBRADOS Y SU BANQUILLO. El "
     "superviviente manda listar socios primarios y alternativos POR TIPO y NO "
     "dice cuales son los tipos: los nombra en su resumen y no en el paso, que es "
     "justo donde hacen falta. El donante los nombra en un paso propio (alianzas "
     "estrategicas, coopetencia, desarrollo conjunto, proveedores clave) y ademas "
     "trae el suyo de identificar primarios y suplentes, que es la misma accion "
     "que la del superviviente dicha con otras palabras. Las tres piezas son UNA "
     "sola instruccion, y separarlas dejaria un paso que dice POR TIPO sin decir "
     "que tipos."),
    (["K2", "P1"],
     "Define en una tabla de tres columnas qué proveerá cada socio y qué recibirá "
     "de la empresa a cambio: nombre del socio, qué provee, qué ofreces tú",
     "LA MISMA DEFINICION CON SU FORMA. El superviviente dice QUE se define (que "
     "provee cada socio y que recibe a cambio) y el donante dice EN QUE se anota "
     "(una tabla de tres columnas, con las tres nombradas). Y hay una razon "
     "medida para tomar la forma del donante en vez de dejarla fuera: las tres "
     "columnas que el donante manda crear son LAS MISMAS TRES que el entregable "
     "del superviviente ya pedia, asi que el paso y el entregable dejan de "
     "contradecirse en el nivel de detalle."),
    (["K3", "P3"],
     "Evalúa la flexibilidad de cada proveedor en tiempos de entrega, tamaños de "
     "pedido, crédito, precio y condiciones",
     "LA MISMA EVALUACION CON LA LISTA COMPLETA. El superviviente evalua en "
     "tiempos, precios y condiciones; el donante evalua en tiempos de entrega, "
     "tamanos de pedido, credito o precio. Se toman las cinco varas porque "
     "ninguna sobra y dos de ellas (tamanos de pedido y credito) son las que "
     "distinguen a un proveedor flexible de uno rigido cuando el precio es el "
     "mismo. El texto queda mas largo y mas util, que es el intercambio que P.13 "
     "autoriza."),
    (["K4"],
     "Distingue claramente entre socios y recursos clave",
     "PIEZA PROPIA DEL SUPERVIVIENTE, y es una DISTINCION y no un procedimiento: "
     "por P.11 viaja ENTERA y con grupo propio. Es la unica linea del acto que "
     "traza una frontera conceptual en vez de mandar hacer algo, y es la que "
     "impide el error tipico de este ejercicio, meter en la tabla de socios lo "
     "que en realidad es un recurso de la casa. El donante no la tiene."),
    (["K5"],
     "Actualiza el Business Model Canvas con los socios identificados",
     "PIEZA PROPIA DEL SUPERVIVIENTE, y es la que cierra el acto contra el "
     "artefacto del metodo: sin ella la tabla de socios se queda en un documento "
     "suelto en vez de entrar en el modelo de negocio, que es de donde salio la "
     "hipotesis. El donante cierra de otra manera (planeando la validacion), y "
     "por eso los dos cierres viajan y ninguno se come al otro."),
    (["P5"],
     "Planea la validación posterior con reuniones reales con cada socio "
     "candidato",
     "PIEZA PROPIA DEL DONANTE, sin equivalente en el superviviente, y es la mas "
     "cara de perder de todo el acto: es la UNICA linea que saca el ejercicio del "
     "escritorio. El metodo de Blank entero se sostiene sobre salir a hablar con "
     "gente real, y una tabla de socios clave sin una reunion detras sigue siendo "
     "una hipotesis con formato de tabla. Va la ultima a proposito, porque es lo "
     "que se hace DESPUES de tener el documento."),
]

GRUPOS_CONDICIONES = [
    (["KC1"],
     "Cuando el modelo de negocio requiere capacidades externas críticas "
     "(manufactura, contenido, distribución)",
     "EL DISPARADOR GENERAL, propio del superviviente, y el que corresponde a la "
     "cabeza: se enciende por lo que el MODELO DE NEGOCIO necesita, sin importar "
     "de que sea el producto."),
    (["PC1"],
     "Cuando el producto es físico y requiere proveedores, alianzas o "
     "distribución mediante terceros",
     "EL DISPARADOR DEL CANAL FISICO, propio del donante, y NO se funde con el "
     "anterior aunque sea un caso suyo. El motivo es el de siempre y aqui pesa "
     "mas que nunca: el canal fisico ES la identidad entera del nodo absorbido, y "
     "disolver su condicion dentro de la general seria borrar en la fusion "
     "justamente lo unico que el donante tenia de propio. Se queda como segundo "
     "disparador, con su nombre, para que quien llegue con un producto fisico "
     "encuentre el acto por su puerta."),
]

ENTREGABLE = (
    "Tabla de socios clave con columnas: nombre del socio, tipo de relación, qué "
    "provee, y qué ofrece la empresa a cambio como contraprestación, con los "
    "candidatos suplentes identificados y la validación con reuniones reales ya "
    "planeada")

RESUMEN = (
    "Identifica los socios esenciales que proveen capacidades, productos o "
    "servicios que la startup no puede o no quiere desarrollar internamente. Se "
    "organizan en cuatro tipos: alianzas estratégicas, coopetición, desarrollo "
    "conjunto de negocio y relaciones con proveedores clave. Con cada uno se "
    "define el 'intercambio de valor', qué provee y qué recibe a cambio, anotado "
    "en una tabla de tres columnas junto a sus candidatos suplentes. La "
    "flexibilidad de cada proveedor se evalúa en tiempos de entrega, tamaños de "
    "pedido, crédito y precio, y se distingue con cuidado entre socios y recursos "
    "clave, que no son lo mismo. El resultado se lleva al Business Model Canvas y "
    "se planea su validación posterior con reuniones reales, porque una tabla de "
    "socios sin una reunión detrás sigue siendo una hipótesis. El ejemplo de "
    "Apple y el iPod con las discográficas muestra cómo un socio puede potenciar "
    "el modelo de negocio entero. Aplica igual cuando el producto es físico y "
    "necesita proveedores, alianzas o distribución mediante terceros.")

PRESERVAR = [
    "coopetición",
    "alianzas estratégicas",
    "desarrollo conjunto",
    "Business Model Canvas",
    "suplentes",
    "tamaños de pedido",
    "crédito",
    "reuniones reales",
    "producto es físico",
    "Apple",
]

RASTROS = [
    "intercambio de valor",
    "recursos clave",
    "capacidades externas",
    "flexibilidad",
    "contraprestación",
]

ELECCION_P8 = {
    "regla": ("P.8, EL CABLEADO DESEMPATA, NO DECIDE. Donde el contenido dice algo "
              "manda el contenido, aunque el margen de aristas apunte al otro lado."),
    "decide": "EL CONTENIDO",
    "elegido": SUP,
    "especie_de_9_3_1": ("POR ELEGIR. La razon del unico par A del acto (el 361) NO "
                         "nombra ganador: la vara del verbo da NO. No hay GANADOR "
                         "POR DERECHO, asi que la eleccion es de P.8."),
    "lectura_de_contenido": [
        "1. LOS DOS SE LLAMAN IGUAL Y UNO TRAE UN PARENTESIS QUE LO ESTRECHA, y "
        "esta es la forma mas limpia que ha dado la operacion. 'Hipotesis de "
        "Socios Clave' contra 'Hipotesis de Socios Clave (Canal Fisico)': no es "
        "que un titulo sea el concepto y el otro se le parezca, es EL MISMO "
        "TITULO con un canal metido entre parentesis. Y esto es EXACTAMENTE el "
        "ejemplar escrito de P.8: alli el id que ganaba por cableado decia "
        "BIENVENIDA, que es UNA fase, mientras la doctrina valia para las OCHO, y "
        "la regla concluye que LA CABEZA DE UNA SERIE NO SE LLAMA COMO UNO DE SUS "
        "PASOS. Aqui el canal fisico es UN canal y la hipotesis de socios vale "
        "para todos.",
        "2. EL GRAFO DECLARA LA JERARQUIA, Y ESO ES CONTENIDO Y NO CABLEADO. P.8 "
        "cuenta como contenido 'un PADRE DECLARADO', y aqui no hay que deducirlo "
        "de un conteo de grados: hay una ARISTA DIRECTA que lo dice. "
        "partners_hypothesis_physical lleva a key_partners_hypothesis en sus "
        "nodos_previos, y key_partners_hypothesis lleva a "
        "partners_hypothesis_physical en sus nodos_siguientes. El grafo ya tiene "
        "escrito que uno viene DEL otro, y en esa arista el que va primero es el "
        "superviviente. Una arista que dice quien va antes no es un margen de "
        "aristas: es una declaracion.",
        "3. LAS CONDICIONES DE ENTRADA, y son la misma vara del punto 1 dicha por "
        "el otro extremo del nodo. La del superviviente se enciende por lo que EL "
        "MODELO DE NEGOCIO necesita (capacidades externas criticas: manufactura, "
        "contenido, distribucion) y la del donante por lo que EL PRODUCTO es "
        "(fisico). Un nodo cuya puerta de entrada es una propiedad del producto "
        "no puede ser la cabeza de una hipotesis del modelo de negocio.",
        "4. EL PASO QUE CIERRA CONTRA EL ARTEFACTO DEL METODO ES DEL "
        "SUPERVIVIENTE: 'Actualizar el Business Model Canvas con los socios "
        "identificados'. La hipotesis de socios NACE de una casilla del Canvas y "
        "vuelve a ella; el nodo que completa ese circuito es el que el metodo "
        "puede colgar de esa casilla. El donante no lo tiene.",
        "5. PIEZAS PROPIAS DEL DONANTE QUE NADIE MAS TIENE, y por eso viajan "
        "enteras: los CUATRO TIPOS nombrados dentro de un paso (el superviviente "
        "solo los tenia en su resumen), la tabla de TRES COLUMNAS con sus nombres, "
        "los tamanos de pedido y el credito como varas de flexibilidad, LA "
        "VALIDACION POSTERIOR CON REUNIONES REALES (la unica linea del acto que "
        "saca el ejercicio del escritorio, y la mas cara de perder), el ejemplar "
        "de Apple y el iPod con las discograficas, y su condicion del canal "
        "fisico, que se queda como SEGUNDO DISPARADOR CON SU NOMBRE en vez de "
        "disolverse, porque el canal fisico es la identidad entera del donante.",
    ],
    "cableado_solo_como_desempate": {
        "usado_para_decidir": False,
        "va_a_favor_del_elegido": False,
        "por_que_se_cita": (
            "PORQUE ESTA VEZ NO PUEDE DECIDIR NADA, Y ESO ROMPE EL PATRON COMODO "
            "DE LOS TRES ACTOS ANTERIORES. Medido hoy: key_partners_hypothesis "
            "tiene grado 6 y partners_hypothesis_physical tiene grado 6. ES UN "
            "EMPATE EXACTO. En el 331, el 341 y el 344 el cableado fue a favor "
            "del elegido por contenido (5 contra 2, 9 contra 5, 8 contra 3) y "
            "esta vuelta declaro que ese patron era comodo y restaba evidencia. "
            "AQUI EL CABLEADO NO APORTA NI UN GRAMO: la eleccion la sostiene "
            "SOLO el contenido, y si el contenido estuviera mal no habria nada "
            "detras que lo tapara. Se registra como el caso limpio de la "
            "operacion. NOTA: 'va_a_favor_del_elegido' se pone en False porque "
            "un empate no va a favor de nadie, y decir que si iria seria contar "
            "un cero como un voto."),
        "instrumento": ("scripts/loop/vuelta41_lectura_acto.py --puesto 361, salida "
                        "docs/loop/SALIDA_V43_ACTO361_LECTURA.txt, bloque (e)"),
        "grados_medidos_hoy": {SUP: 6, ABS[0]: 6},
        "coste_medido_de_la_eleccion": ("CERO aristas. Los dos nodos tienen CERO "
                                        "aristas propias sin reciproco, asi que "
                                        "elegir a cualquiera de los dos no pierde "
                                        "ni una arista: las reciprocas las "
                                        "reescribe la simetrizacion de run_phase1 "
                                        "paso 5."),
    },
}
