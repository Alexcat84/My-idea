# -*- coding: utf-8 -*-
"""ACTO 341 de OP-D-06: customer_journey_mapping con blueprint_de_experiencia.

LO UNICO TECLEADO: los grupos, sus motivos y la lectura. La medicion la hace
scripts/loop/vuelta41_plan_acto.py contra el grafo.
"""

SUP = "customer_journey_mapping"
ABS = ["blueprint_de_experiencia"]
PREF = {"J": SUP, "B": ABS[0]}

OPERACION = ("OP-D-06, ACTO 3 DE NUEVE (puesto 341): customer_journey_mapping "
             "absorbe a blueprint_de_experiencia")

ESTADO = (
    "SELLADO en la vuelta 43, 19 ago 2026, ANTES de ejecutar. EL DESTEJIDO DE "
    "ESTE ACTO YA SE HIZO, y no aqui: lo hizo OP-F-04-COL, la mesa de Coleman. "
    "La razon del archivo describe DOS costuras gordas, diecisiete pasos el "
    "primero y diez el segundo, con bloques enteros pegados que no son mapeo (el "
    "ritual de celebracion del momento de la compra en uno y la silla vacia del "
    "cliente en las reuniones en el otro), y esa razon esta RANCIA EN ESE "
    "DETALLE: docs/plan/01_FUENTES.md publica las dos fronteras leidas en su "
    "tabla de los doce (linea 1225 para blueprint_de_experiencia, 1 a 4 contra 5 "
    "a 17; linea 1228 para customer_journey_mapping, 1 a 5 contra 6 a 10) y el "
    "reparto de los seis subbloques del primero (lineas 1332 a 1337) y de los "
    "tres del segundo (lineas 1341 a 1343). LA MEDICION DE HOY LO CONFIRMA: "
    "blueprint_de_experiencia tiene CUATRO pasos y customer_journey_mapping "
    "tiene CINCO, que son exactamente los tramos que aquellas fronteras dejaban "
    "en pie. La regla de fuente primero queda satisfecha POR PRECEDENCIA, con "
    "OP-F-04-COL HECHA en su nota 7981 SI segun la apertura de esta vuelta. "
    "Y LO QUE EL INSTRUMENTO SIGUE CITANDO HOY SE DICE EN VEZ DE CALLARSE: "
    "blueprint_de_experiencia esta FUERA de la cola de 1.495, pero "
    "customer_journey_mapping sigue DENTRO con bloque 49,4 y corte tras 2. Esa "
    "cita NO es la costura vieja de Coleman, que ya no existe en el fichero: es "
    "el residuo del bloque original de Brown, y la lectura textual con el texto "
    "delante dice que NO hay costura, porque los pasos 3 a 5 CONTINUAN a los 1 y "
    "2 en vez de volver a contarlos (el 1 y el 2 observan y documentan las "
    "ETAPAS, el 3 abre cada etapa en sus TOUCHPOINTS, el 4 los juzga y el 5 "
    "prioriza). Comparten vocabulario, no narracion. LA CITA QUEDA REGISTRADA EN "
    "LA COLA Y NO DESPACHADA, y el auditor la relee: es la guarda contra el juez "
    "y parte.")

REGLA = (
    "OP-D-06 de docs/plan/02_DESTEJIDOS.md, LOS NUEVE ACTOS DE DOS, acto del "
    "puesto 341 de su tabla sellada. ESTE ACTO SI TIENE REPARTO ESCRITO, y es "
    "uno de los dos que lo tienen (el otro es el 392): la tabla dice que lo que "
    "se preserva es el 'precedente de la cura acoplada, mapa contra mapa'. SE "
    "CUMPLE TAL COMO ESTA ESCRITO y se lee con su fuente delante: "
    "docs/INTRA_DOMINIO_INFORME.md linea 3012 llama a este puesto el PRECEDENTE "
    "EXACTO de la cura acoplada mayor de OP-D-01, 'donde los dos estaban "
    "costurados y el solape era mapa contra mapa'. O sea que el reparto escrito "
    "NO reparte piezas: declara la FORMA del acto, COSTURADA CONTRA COSTURADA, "
    "que son tres movimientos y no dos (destejer uno, destejer el otro, y solo "
    "entonces fundir lo que queda). Los dos destejidos ya los hizo OP-F-04-COL, "
    "asi que lo que queda es el tercer movimiento: mapa contra mapa. Para las "
    "piezas, la regla adjudicada el 11 ago 2026: cada perdida al bloque del que "
    "proviene, y la que no tenga bloque al superviviente.")

MOTIVO = (
    "El acto se leyo ENTERO por P.5 y es UNA familia de DOS: el par 341 es A en "
    "el archivo y NINGUN otro par del archivo mete a un tercero con cualquiera "
    "de los dos, asi que el subconjunto es CERRADO y el acto es de dos, como la "
    "tabla sellada dice. CERO pares vuelven a la cola de relectura post fusion, "
    "porque no hay ni un tercero que releer. LA FUENTE, DICHA COMO SE MIDE Y NO "
    "COMO CONVIENE: el instrumento medira DOS cadenas de fuente distintas y por "
    "eso imprimira FUENTE MIXTA, pero las dos nombran EL MISMO LIBRO, Change by "
    "Design de Tim Brown; lo unico que las separa es que la del superviviente "
    "trae la edicion y el autor ('Change by Design, Revised and U - Tim Brown') "
    "y la del absorbido dice solo 'Change by Design'. Es la misma especie de "
    "diferencia que el acto 331 ya declaro: no es un cruce de libros, es el "
    "mismo libro citado con dos precisiones distintas. Y ADEMAS SE DICE LO QUE "
    "LA TABLA DE FUENTES YA HABIA MEDIDO: los dos declaraban tambien a Coleman "
    "como segundo libro, y ese segundo libro es justo el que OP-F-04-COL se "
    "llevo; que hoy el campo fuente ya no lo nombre es la huella de aquel "
    "destejido, no una perdida de este acto.")

# ---------------------------------------------------------------------------
# LOS GRUPOS. Trece origenes en CINCO pasos y TRES condiciones. Los cinco
# pasos quedan DENTRO del estandar de 3 a 6.
# ---------------------------------------------------------------------------
GRUPOS_PASOS = [
    (["J1", "B1"],
     "Observa directamente a clientes reales durante toda su experiencia de "
     "servicio, acompañándolos en todo su recorrido (shadowing) y sin limitarte "
     "al punto de contacto que asumiste como el más importante",
     "LA MISMA OBSERVACION CON SU ADVERTENCIA, y la advertencia es lo unico que "
     "los separaba. Los dos mandan lo mismo (acompanar al cliente real por su "
     "experiencia entera), y la propia razon del par lo llamo 'el mismo aviso de "
     "partida'; lo que viaja del donante es ese aviso, que el superviviente NO "
     "tenia: no te quedes en el punto de contacto que supusiste critico. Por "
     "P.11 una advertencia que califica un procedimiento entra DENTRO del paso "
     "que califica en vez de fabricar un paso suelto, y este califica a este y a "
     "ninguno mas. Sin ella el paso dice que observes todo y no dice contra que "
     "error observas."),
    (["J2", "B2", "B4"],
     "Documenta cada etapa del viaje, desde el primer contacto hasta el cierre, "
     "identificando en cada una los momentos emocionales clave (los 'momentos de "
     "verdad'), y levanta el mapa con la estrategia general y el detalle "
     "operativo al mismo tiempo",
     "LA MISMA DOCUMENTACION CON SU CAPA EMOCIONAL Y SU FORMA, y ninguna de las "
     "dos era completa sola. El superviviente decia DONDE empieza y acaba el "
     "mapa (del primer contacto al cierre) y no decia QUE se marca dentro de "
     "cada etapa; el donante dice que se marcan los momentos emocionales clave, "
     "que son los que su propio resumen llama los momentos de verdad. Y la "
     "tercera pieza es tambien del donante y modifica esta misma accion y "
     "ninguna otra: COMO se documenta, con la estrategia general y el detalle "
     "operativo a la vez, que es la linea que distingue este mapa de un manual "
     "operativo. Por P.11 las dos califican el procedimiento de documentar y por "
     "eso entran aqui y no tienen grupo propio. Un mapa de etapas sin momentos "
     "emocionales es un diagrama de flujo, y un mapa que solo trae la estrategia "
     "no se puede ejecutar."),
    (["J3"],
     "Identifica todos los 'touchpoints' donde el cliente interactúa con la "
     "marca o el servicio",
     "PIEZA PROPIA DEL SUPERVIVIENTE, sin equivalente en el donante: el mapa del "
     "donante llega hasta la ETAPA y se detiene ahi, y este paso abre cada etapa "
     "en los puntos concretos donde alguien toca a la marca. Viaja entero y "
     "solo, y tiene grupo propio porque es el que fabrica el objeto sobre el que "
     "trabajan los dos pasos siguientes: sin touchpoints identificados no hay "
     "nada que evaluar ni nada que priorizar."),
    (["J4", "B3"],
     "Evalúa cada touchpoint con dos varas distintas: si crea valor positivo o "
     "pierde al cliente, y si solo evita una mala experiencia o genera una "
     "experiencia memorable",
     "LA MISMA EVALUACION CON DOS VARAS QUE NO SON LA MISMA, y por eso van "
     "juntas y se nombran las dos. El superviviente juzga por VALOR (crear valor "
     "o perder al cliente), que es una vara economica; el donante juzga por "
     "MEMORIA (evitar lo malo o generar lo memorable), que es una vara de "
     "experiencia. Fundirlas en una sola frase borraria una de las dos, y no son "
     "intercambiables: un touchpoint puede crear valor y ser perfectamente "
     "olvidable, y el donante existe justo para ver eso. Por P.13 la vara del "
     "donante viaja ENTERA y dentro de la misma accion, porque modifica la MISMA "
     "evaluacion y no anade un paso."),
    (["J5"],
     "Prioriza las mejoras en los puntos de mayor impacto, no solo en el "
     "producto central",
     "PIEZA PROPIA DEL SUPERVIVIENTE, y es la unica linea del acto que convierte "
     "el mapa en una DECISION: todo lo anterior describe, y esta reparte el "
     "esfuerzo. Va la ultima a proposito. Y su coletilla, 'no solo en el "
     "producto central', es una advertencia por P.11 y viaja pegada al paso: sin "
     "ella el acto entero se puede hacer completo y terminar arreglando el "
     "producto, que es exactamente el error que las dos condiciones de entrada "
     "describen."),
]

GRUPOS_CONDICIONES = [
    (["JC1", "BC2"],
     "Cuando estás diseñando o rediseñando un servicio complejo, con múltiples "
     "etapas y múltiples puntos de interacción",
     "EL MISMO DISPARADOR DICHO CON LAS DOS GRANULARIDADES DEL MISMO MAPA, y "
     "aqui fundir NO borra una senal: la quita de repetir. El superviviente dice "
     "'multiples puntos de interaccion' y el donante 'multiples etapas', que son "
     "el touchpoint y la etapa, las dos unidades del unico mapa que este acto "
     "levanta. Es el CONTRARIO del caso del acto 331, donde las dos condiciones "
     "eran dos momentos distintos (decidir la inversion y pedir el "
     "financiamiento) y NO se fundieron. La vara es la misma en los dos: se "
     "funde lo que es el mismo momento y se separa lo que no."),
    (["JC2"],
     "Cuando el foco inicial del proyecto se ha limitado erróneamente a un solo "
     "producto o a una sola etapa",
     "EL DISPARADOR DEL FOCO ESTRECHO, propio del superviviente. Se enciende "
     "ANTES de gastar: el proyecto todavia se esta encuadrando y el encuadre ya "
     "salio estrecho."),
    (["BC1"],
     "Cuando has invertido en un punto de contacto que asumiste como crítico sin "
     "validarlo con observación real",
     "EL DISPARADOR DEL DINERO YA GASTADO, propio del donante, y se resiste la "
     "tentacion de juntarlo con el anterior. Los dos hablan de un foco mal "
     "puesto, pero en DOS momentos distintos: aquel se enciende mientras se "
     "encuadra el proyecto y este se enciende cuando la inversion YA se hizo y "
     "ademas se hizo sin observacion real. Fundirlos dejaria el acto sin su "
     "alarma cara, que es la que llega tarde. Por la misma vara que el acto 331 "
     "uso para NO fundir sus dos condiciones."),
]

ENTREGABLE = (
    "Un mapa visual del viaje del cliente con todas sus etapas y todos sus "
    "touchpoints, los momentos emocionales clave identificados, cada punto "
    "evaluado por el valor que crea y por lo memorable que resulta, levantado "
    "con la estrategia general y el detalle operativo al mismo tiempo, y con las "
    "mejoras priorizadas por impacto")

RESUMEN = (
    "El mapa del viaje del cliente traza el recorrido completo por el que pasa "
    "un cliente en una experiencia de servicio, desde el primer contacto hasta "
    "el cierre, para ver dónde se crea valor y dónde se pierde al cliente. Se "
    "levanta observando a clientes reales durante toda su experiencia, sin "
    "limitarse al punto de contacto que uno asumió como el más importante, y se "
    "documenta etapa por etapa marcando los momentos emocionales clave: los "
    "'momentos de verdad'. Dentro de esas etapas se identifican los "
    "'touchpoints', los puntos concretos donde el cliente interactúa con la "
    "marca o el servicio, y cada uno se evalúa con dos varas que no son la "
    "misma: si crea valor o pierde al cliente, y si solo evita una mala "
    "experiencia o genera una memorable. A diferencia de un manual operativo, "
    "este mapa lleva la estrategia general y el detalle operativo al mismo "
    "tiempo, conecta la experiencia del cliente con la oportunidad de negocio y "
    "revela ideas que a veces contradicen lo que se suponía al principio, como "
    "el momento de exhalar que descubrió Marriott en lugar del check-in. "
    "Termina priorizando las mejoras en los puntos de mayor impacto, no solo en "
    "el producto central.")

PRESERVAR = [
    "touchpoints",
    "shadowing",
    "momentos emocionales clave",
    "momentos de verdad",
    "memorable",
    "estrategia general",
    "detalle operativo",
    "Marriott",
    "observación real",
    "no solo en el producto central",
]

RASTROS = [
    "primer contacto",
    "etapa",
    "mayor impacto",
    "manual operativo",
    "clientes reales",
]

ELECCION_P8 = {
    "regla": ("P.8, EL CABLEADO DESEMPATA, NO DECIDE. Donde el contenido dice algo "
              "manda el contenido, aunque el margen de aristas apunte al otro lado."),
    "decide": "EL CONTENIDO",
    "elegido": SUP,
    "especie_de_9_3_1": ("POR ELEGIR. La razon del unico par A del acto (el 341) NO "
                         "nombra ganador: la vara del verbo da NO. No hay GANADOR "
                         "POR DERECHO, asi que la eleccion es de P.8."),
    "lectura_de_contenido": [
        "1. EL QUE EXISTE SIN EL OTRO ES LA CABEZA, que es la misma vara que "
        "decidio el acto 331 (alli: el analisis existe sin la propuesta y la "
        "propuesta no existe sin el analisis). Aqui el mapa del viaje existe sin "
        "el blueprint, y el blueprint NO existe sin el mapa del viaje: su propio "
        "paso 2 es 'mapea cada etapa de la experiencia', o sea que para hacerse a "
        "si mismo tiene que hacer antes lo que el otro nodo ES. Un blueprint es "
        "un mapa del viaje CON dos capas mas encima (la emocional y la "
        "operativa); un mapa del viaje no necesita ser un blueprint para "
        "servir. Lo que se puede tener solo es la cabeza.",
        "2. EL TITULO DE UNO ES EL CONCEPTO Y EL DEL OTRO NOMBRA UN ARTEFACTO DE "
        "ESE CONCEPTO. customer_journey_mapping se titula 'Mapeo del Customer "
        "Journey (Viaje del Cliente)', que ES el nombre de la practica; "
        "blueprint_de_experiencia se titula 'El Mapa de Experiencia del Cliente "
        "(Blueprint)', y el parentesis es el que manda: blueprint es el nombre de "
        "UN documento concreto de la disciplina, no el de la practica. Es la "
        "tercera vez seguida en esta operacion que la forma del titulo apunta al "
        "mismo lado que el resto del contenido (285 y 331 antes que este), y se "
        "deja escrito para que se pueda auditar como patron y no como corazonada.",
        "3. EL PROCEDIMIENTO DEL SUPERVIVIENTE CIERRA EL CICLO Y EL DEL DONANTE "
        "NO. El superviviente va observar, documentar, identificar touchpoints, "
        "evaluarlos y PRIORIZAR: termina en una decision sobre donde gastar el "
        "esfuerzo. El donante va acompanar, mapear, distinguir y DOCUMENTAR: "
        "termina en el artefacto. El nodo que llega hasta la decision es el que "
        "aguanta ser cabeza de la familia, porque los nodos que cuelgan de el son "
        "los que ejecutan esa decision.",
        "4. EL ALCANCE DEL ROL, que P.8 cuenta como contenido con el mismo peso "
        "que el texto. Las condiciones del superviviente cubren el encuadre "
        "entero (disenar o redisenar cualquier servicio de multiples puntos, y el "
        "foco estrechado a un solo producto o etapa); las del donante cubren un "
        "caso mas estrecho dentro de eso (ya invertiste en un punto de contacto "
        "sin validarlo). La cabeza es la que vale para el caso general.",
        "5. PIEZAS PROPIAS DEL DONANTE QUE NADIE MAS TIENE, y por eso viajan "
        "enteras: el aviso de partida (no te quedes en el punto que supusiste "
        "critico), los momentos emocionales clave y su nombre propio (los "
        "momentos de verdad), la vara de lo memorable contra lo que solo evita lo "
        "malo, la exigencia de llevar estrategia general y detalle operativo al "
        "mismo tiempo, la distincion contra el manual operativo, y el ejemplar de "
        "Marriott. Las seis viajan por plan y no por suerte: cinco estan en "
        "preservar_literal y la sexta, la distincion contra el manual operativo, "
        "esta en rastros. NINGUNA depende de que el donante sobreviva.",
    ],
    "cableado_solo_como_desempate": {
        "usado_para_decidir": False,
        "va_a_favor_del_elegido": True,
        "por_que_se_cita": (
            "PORQUE VA A FAVOR DEL ELEGIDO Y ESO TAMBIEN HAY QUE DECIRLO, Y "
            "PORQUE AQUI EL MARGEN ES GRANDE Y UN MARGEN GRANDE A FAVOR ES "
            "JUSTO EL SITIO DONDE UNA DECISION POR CABLEADO SE PUEDE DISFRAZAR "
            "DE DECISION POR CONTENIDO. Medido hoy: customer_journey_mapping "
            "tiene grado 9 y blueprint_de_experiencia tiene grado 5. Las dos "
            "varas coinciden, y cuando coinciden la regla NO SE LUCE. LIMITACION "
            "DECLARADA, no escondida: el instrumento imprime los cinco bloques en "
            "una sola salida, asi que el ejecutor de esta vuelta vio el cableado "
            "en la misma corrida en que leyo el contenido y su adjudicacion NO es "
            "ciega respecto del cableado. Los cinco puntos de la lectura de "
            "contenido se sostienen SIN el cableado y ninguno lo menciona; la "
            "relectura ciega del auditor es la guarda que decide si eso es "
            "cierto. Contraste util dentro de la misma operacion: en el acto 285 "
            "las dos varas se separaron y el cableado PERDIO."),
        "instrumento": ("scripts/loop/vuelta41_lectura_acto.py --puesto 341, salida "
                        "docs/loop/SALIDA_V43_ACTO341_LECTURA.txt, bloque (e)"),
        "grados_medidos_hoy": {SUP: 9, ABS[0]: 5},
        "coste_medido_de_la_eleccion": ("CERO aristas. Los dos nodos tienen CERO "
                                        "aristas propias sin reciproco, asi que "
                                        "elegir a cualquiera de los dos no pierde "
                                        "ni una arista: las reciprocas las "
                                        "reescribe la simetrizacion de run_phase1 "
                                        "paso 5."),
    },
}
