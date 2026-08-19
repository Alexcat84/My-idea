# -*- coding: utf-8 -*-
"""ACTO 969 de OP-D-06: retention_metrics con customer_retention_metrics_webmobile.

LO UNICO TECLEADO: los grupos, sus motivos y la lectura. La medicion la hace
scripts/loop/vuelta41_plan_acto.py contra el grafo.
"""

SUP = "retention_metrics"
ABS = ["customer_retention_metrics_webmobile"]
PREF = {"R": SUP, "W": ABS[0]}

OPERACION = ("OP-D-06, ACTO 8 DE NUEVE (puesto 969): retention_metrics absorbe a "
             "customer_retention_metrics_webmobile")

ESTADO = (
    "SELLADO en la vuelta 44, 19 ago 2026, ANTES de ejecutar. Y ES EL ULTIMO ACTO "
    "CON FUSION DE OP-D-06: cerrado este, de los nueve quedan ocho fundidos y el "
    "494 cerrado por declaracion. EL DESTEJIDO QUE LA RAZON PEDIA YA SE HIZO, y no "
    "aqui: lo hizo OP-F-04-COL. La razon del archivo dice que lo propio de "
    "retention_metrics es, entre otras cosas, 'despues el bloque entero del costo "
    "de adquisicion', y esta RANCIA EN ESE DETALLE. docs/plan/01_FUENTES.md linea "
    "1235 publica la frontera leida (1 a 5 contra 6 a 9) con el bloque nombrado "
    "pieza a pieza (el CAC exacto por canal, el breakeven, el porcentaje que "
    "abandona antes de alcanzarlo, y presentarlo a la direccion) y la linea 1353 "
    "publica el miembro receptor, persuasion_directivos_prioridad_cliente, con el "
    "desempate escrito: el ultimo paso del bloque NOMBRA AL DESTINATARIO. LA "
    "MEDICION DE HOY LO CONFIRMA POR PARTIDA DOBLE: retention_metrics tiene CINCO "
    "pasos, que son exactamente los cinco primeros, y el commit que lo corto es "
    "575be1e3 (OP-F-04-COL SEGUNDO TIEMPO EJECUTADO), medido con git show sobre el "
    "fichero, 9 pasos antes y 5 despues. Fuente primero satisfecha POR "
    "PRECEDENCIA, con OP-F-04-COL HECHA en su nota 7981 SI segun la apertura de "
    "esta vuelta, que es ademas la operacion que declaraba BLOQUEAR a OP-D-06 en "
    "su campo bloquea_a: el bloqueo queda levantado y medido, no supuesto. LO QUE "
    "EL INSTRUMENTO DE COSTURAS CITA HOY SE DICE EN VEZ DE CALLARSE: "
    "retention_metrics esta FUERA de la cola de 1.494 y "
    "customer_retention_metrics_webmobile esta DENTRO, con bloque 55,7 y corte "
    "tras 4 (la pareja, 63,8 sobre sus pasos 1 y 5, NO dispara: el umbral de "
    "pareja es 80). LA CITA ES DEL DONANTE Y NO DEL SUPERVIVIENTE, y la lectura "
    "textual con el texto delante dice que tampoco alli hay costura: sus pasos 1 a "
    "4 miran al cliente que esta (alta, actividad, abandono, clics) y los 5 y 6 "
    "miran lo que ese cliente produce (referidos y respuesta a campanas). "
    "CONTINUAN en vez de volver a contar. La cita queda REGISTRADA en la cola y no "
    "despachada, y el auditor la relee.")

REGLA = (
    "OP-D-06 de docs/plan/02_DESTEJIDOS.md, LOS NUEVE ACTOS DE DOS, acto del "
    "puesto 969 de su tabla sellada. Este acto NO tiene reparto escrito en esa "
    "tabla (solo lo tienen el 392 y el 341), asi que se resuelve con la regla "
    "adjudicada el 11 ago 2026: cada perdida al bloque del que proviene, y la que "
    "no tenga bloque al superviviente. PERO LA RAZON DEL ARCHIVO SI DEJO ESCRITO "
    "LO PROPIO DE CADA LADO, y se cumple pieza por pieza: del donante, la fuente "
    "de cada cliente, los clics que hace y los que no dentro del sitio, los "
    "referidos que genera cada uno y el resultado de cada promocion; del "
    "superviviente, la agrupacion por cohortes de mes de ingreso, el valor de "
    "vida, y las quejas y tickets. Las siete piezas viajan al resultado, y "
    "'fuente de cada cliente', 'clics', 'referidos', 'promoción', 'mes de "
    "ingreso', 'lifetime value' y 'tickets de soporte' van en preservar_literal "
    "para que una guarda las compruebe una a una en vez de confiarlas.")

MOTIVO = (
    "El acto se leyo ENTERO por P.5 y es UNA familia de DOS: el par 969 es A en el "
    "archivo y los CINCO pares que meten un tercero son el 233 (B), el 522 (D), el "
    "848 (D), el 884 (D) y el 1362 (D). CERO terceros de clase A, asi que el acto "
    "es de dos, como la tabla sellada dice. Y AQUI SI VUELVE UN PAR A LA COLA, el "
    "segundo de toda la operacion despues del 599: el puesto 233, "
    "analisis_de_cohortes con retention_metrics, es clase B y su nodo CAMBIA DE "
    "TEXTO al absorber, asi que se relee al cierre del acto como manda "
    "08_VERIFICACION. Los actos 392 y 711 de esta misma vuelta salieron los dos en "
    "CERO; este no. LA FUENTE, DICHA COMO SE MIDE: el instrumento imprimira FUENTE "
    "UNICA, porque las dos cadenas son IDENTICAS ('The Startup Owner's Manual - "
    "Steve Blank'). Es el SEGUNDO acto de OP-D-06 en el que la etiqueta sale unica, "
    "despues del 361, y se deja escrito porque en esta misma vuelta el 711 salio "
    "MIXTA DE VERDAD con dos libros: la etiqueta del instrumento distingue las tres "
    "situaciones y las tres estan ahora registradas con nombre.")

# ---------------------------------------------------------------------------
# LOS GRUPOS. Once origenes de paso en SEIS pasos, dentro del estandar de 3 a 6,
# y tres origenes de condicion en TRES condiciones.
# ---------------------------------------------------------------------------
GRUPOS_PASOS = [
    (["W1", "R5"],
     "Registra la fecha de inicio y la fuente de cada cliente, y agrúpalos en "
     "cohortes por mes de ingreso para poder comparar su comportamiento",
     "EL DATO Y LO QUE SE HACE CON EL, y es la fusion mas justificada del acto: el "
     "donante manda rastrear LA FECHA DE INICIO de cada cliente y el superviviente "
     "manda agrupar por COHORTES DE MES DE INGRESO. La cohorte se construye con esa "
     "fecha y con ninguna otra cosa, asi que son dos mitades de una sola "
     "instruccion. Separarlas dejaria un paso que registra una fecha sin decir para "
     "que y otro que agrupa por un mes que nadie registro. Y la fuente de cada "
     "cliente viaja pegada porque se anota en el mismo momento del alta."),
    (["R1", "R2", "W2"],
     "Mide la actividad de cada cliente y de cada cohorte: visitas, páginas vistas, "
     "tiempo en el sitio o la aplicación, frecuencia y duración de cada visita, y "
     "el tiempo promedio que pasa entre una y la siguiente",
     "LA MISMA MEDICION DE ACTIVIDAD CON LAS DOS UNIDADES Y SU DERIVADA. El "
     "superviviente mide POR COHORTE (visitas, page views, tiempo en sitio) y el "
     "donante mide POR CLIENTE (frecuencia y duracion de visitas): es la misma "
     "medicion con dos granularidades, y quedarse con una sola era la unica perdida "
     "real que este acto podia producir. La segunda pieza del superviviente, el "
     "tiempo promedio entre visitas, es una CUENTA que se saca de esas mismas "
     "visitas, asi que entra en el mismo paso en vez de quedarse como un paso de "
     "una sola division."),
    (["W4"],
     "Monitorea el comportamiento dentro del sitio: qué clics hace cada cliente y "
     "cuáles no",
     "PIEZA PROPIA DEL DONANTE, sin equivalente en el superviviente, y con grupo "
     "propio porque mide una cosa distinta de la de arriba: aquella cuenta CUANTO "
     "viene el cliente y esta mira QUE HACE cuando viene. La razon del archivo la "
     "nombra expresamente como lo propio de este lado, y el matiz de los clics QUE "
     "NO HACE es la unica linea de los dos nodos que mide una ausencia en vez de "
     "una presencia."),
    (["W3", "R4"],
     "Detecta el momento y la causa del abandono, y monitorea las quejas, los "
     "tickets de soporte y las tasas de respuesta a tus correos",
     "LAS DOS CARAS DE LA MISMA SENAL DE SALIDA. El donante detecta el abandono "
     "cuando ya ocurrio (momento y causa) y el superviviente monitorea lo que lo "
     "anuncia antes (quejas, tickets, correos sin respuesta). Van juntas porque son "
     "el mismo objeto medido antes y despues, y porque separarlas dejaria el aviso "
     "en un paso y la confirmacion en otro, que es justo lo que hace que nadie mire "
     "el primero. Ninguna de las dos se pierde: las dos listas de senales viajan "
     "enteras."),
    (["R3"],
     "Estima la vida promedio del cliente y su valor de vida (lifetime value)",
     "PIEZA PROPIA DEL SUPERVIVIENTE, sin equivalente en el donante, y va en grupo "
     "propio y DESPUES del abandono porque no se puede calcular antes: la vida "
     "promedio se estima con el momento del abandono que el paso anterior acaba de "
     "detectar. Es ademas la unica linea de los dos nodos que convierte "
     "comportamiento en dinero, que es lo que permite decidir cuanto vale la pena "
     "gastar en retener."),
    (["W5", "W6"],
     "Mide lo que tu retención produce: los referidos que genera cada cliente y el "
     "resultado de cada promoción o campaña de retención",
     "LAS DOS PIEZAS DEL DONANTE QUE MIDEN EFECTO Y NO ESTADO, y van juntas y al "
     "final por la misma razon: las cinco anteriores describen como esta el "
     "cliente, y estas dos miden que devuelve. La razon del archivo nombra las dos "
     "como propias del donante. Cierran el acto contra la condicion que el "
     "superviviente ya traia (cuantificar el exito de las tacticas de retencion), "
     "que sin ellas se quedaba sin ningun paso que la atendiera."),
]

GRUPOS_CONDICIONES = [
    (["RC1"],
     "Cuando necesitas cuantificar el éxito de tus tácticas de retención",
     "EL DISPARADOR GENERAL, propio del superviviente y el que corresponde a la "
     "cabeza: se enciende por lo que quieres SABER, sin importar por que canal "
     "llegue el cliente."),
    (["WC1"],
     "Si tu startup ya cuenta con una base de usuarios activos en web o en móvil",
     "EL DISPARADOR DEL CANAL DIGITAL, propio del donante, y NO se funde con el "
     "anterior aunque sea un caso suyo. El motivo es el mismo que el acta de la "
     "vuelta 43 adjudico a favor en el acto 361: el canal digital ES la identidad "
     "entera del nodo absorbido, hasta en su titulo, y disolver su condicion dentro "
     "de la general seria borrar en la fusion justamente lo unico que el donante "
     "tenia de propio. Se queda como segundo disparador, con su nombre, para que "
     "quien llegue con un producto web o movil encuentre el acto por su puerta."),
    (["WC2"],
     "Si buscas reducir el abandono con datos de comportamiento en lugar de "
     "suposiciones",
     "EL DISPARADOR DEL METODO, propio del donante, y tampoco se funde: los otros "
     "dos dicen QUE quieres y DONDE estas, y este dice CON QUE lo vas a hacer. Es "
     "la frase que separa este tablero de una encuesta de satisfaccion, y es la "
     "misma lectura de tres puertas distintas al mismo procedimiento que el acta de "
     "la vuelta 43 adjudico a favor en su D6."),
]

ENTREGABLE = (
    "Un tablero de métricas de retención segmentado por cohortes de mes de ingreso "
    "y con el comportamiento individual de cada cliente, que incluya su valor de "
    "vida, las señales y la causa del abandono, los referidos que genera y el "
    "resultado de cada campaña de retención")

RESUMEN = (
    "Los programas de retención dependen de mirar de cerca el comportamiento del "
    "cliente para saber quién se queda, quién se va y por qué. En canales digitales "
    "se puede rastrear el comportamiento individual de cada usuario (su fecha de "
    "inicio, su fuente, su actividad, su abandono, sus clics) sin violar su "
    "privacidad, y eso permite personalizar los esfuerzos de retención con datos "
    "reales en vez de suposiciones. Los indicadores se organizan por cohortes, "
    "grupos de clientes que entraron el mismo mes, para poder comparar su "
    "comportamiento entre sí y detectar señales tempranas de abandono (churn). Al "
    "lado del comportamiento se miden las quejas, los tickets de soporte y las "
    "respuestas a los correos, se estima la vida promedio del cliente y su valor de "
    "vida (lifetime value), y se cierra midiendo lo que la retención devuelve: los "
    "referidos que genera cada cliente y el resultado de cada promoción o campaña.")

PRESERVAR = [
    "mes de ingreso",
    "fuente de cada cliente",
    "clics",
    "referidos",
    "promoción",
    "lifetime value",
    "tickets de soporte",
    "privacidad",
    "abandono",
    "páginas vistas",
]

RASTROS = [
    "cohortes",
    "retención",
    "comportamiento",
    "visitas",
    "churn",
    "tablero",
]

ELECCION_P8 = {
    "regla": ("P.8, EL CABLEADO DESEMPATA, NO DECIDE. Donde el contenido dice algo "
              "manda el contenido, aunque el margen de aristas apunte al otro lado."),
    "decide": "EL CONTENIDO",
    "elegido": SUP,
    "especie_de_9_3_1": ("POR ELEGIR. La razon del unico par A del acto (el 969) NO "
                         "nombra ganador: la vara del verbo da NO. Lo que si hace es "
                         "repartir lo propio de cada lado con nombre, y esas siete "
                         "piezas son las que este plan manda comprobar por guarda."),
    "lectura_de_contenido": [
        "1. UNO SE LLAMA POR LA MEDIDA Y EL OTRO POR EL CANAL, y es el mismo caso "
        "que el acto 361 resolvio hace dos actos. 'Metricas de Retencion' contra "
        "'Monitoreo de Metricas de Retencion WEB/MOBILE': no es que un titulo sea el "
        "concepto y el otro se le parezca, es EL MISMO TITULO con un canal pegado "
        "detras. Y la etiqueta lo repite por su lado: 'Mide la Retencion de "
        "Clientes' contra 'Vigila la Retencion Digital'. Es el ejemplar escrito de "
        "P.8: LA CABEZA DE UNA SERIE NO SE LLAMA COMO UNO DE SUS PASOS, y web o "
        "movil son DOS canales de los que un negocio puede tener, mientras que la "
        "retencion se mide en todos.",
        "2. LAS CONDICIONES DE ENTRADA LO CONFIRMAN POR EL OTRO EXTREMO DEL NODO, "
        "que es la misma comprobacion que el 361 uso. La del superviviente se "
        "enciende por lo que quieres SABER (cuantificar el exito de las tacticas de "
        "retencion) y la del donante por lo que TU PRODUCTO ES (que ya tengas una "
        "base de usuarios activos en web o movil). Un nodo cuya puerta de entrada "
        "es una propiedad del canal no puede ser la cabeza de una medida que vale "
        "para todos los canales.",
        "3. EL ENTREGABLE DEL DONANTE PROMETE ALGO QUE SU PROPIO PROCEDIMIENTO NO "
        "CONSTRUYE, y esto es medicion y no opinion. Su entregable dice 'metricas "
        "de retencion POR COHORTE y comportamiento individual', y NINGUNO de sus "
        "seis pasos agrupa por cohortes: la unica linea de los dos nodos que "
        "construye una cohorte es la del superviviente (agrupar por mes de "
        "ingreso). O sea que el donante DEPENDE de un paso que solo el "
        "superviviente tiene para poder entregar lo que promete. La dependencia va "
        "en una sola direccion, y el que esta abajo no es la cabeza.",
        "4. EL EJE SOBRE EL QUE SE ORDENA TODO ES DEL SUPERVIVIENTE. Los dos "
        "entregables nombran la cohorte, los dos resumenes la nombran, y la cohorte "
        "es lo que convierte una lista de clics en una comparacion (este mes contra "
        "el anterior). Es contenido y no cableado: es el armazon del tablero.",
        "5. PIEZAS PROPIAS DEL DONANTE QUE NADIE MAS TIENE, y por eso viajan "
        "enteras: LA FUENTE de cada cliente anotada en el alta, la medicion de "
        "actividad POR CLIENTE y no solo por cohorte, EL MOMENTO Y LA CAUSA DEL "
        "ABANDONO, los CLICS QUE HACE Y LOS QUE NO (la unica linea de los dos que "
        "mide una ausencia), LOS REFERIDOS que genera cada uno, EL RESULTADO DE "
        "CADA PROMOCION (la unica que cierra contra la condicion del superviviente, "
        "que sin ella se quedaba sin paso que la atendiera), su condicion del canal "
        "digital, su condicion del metodo (datos en vez de suposiciones) y la nota "
        "de PRIVACIDAD de su resumen. Once origenes de paso entran y once viajan: "
        "CERO se pierden.",
    ],
    "cableado_solo_como_desempate": {
        "usado_para_decidir": False,
        "va_a_favor_del_elegido": False,
        "por_que_se_cita": (
            "PORQUE ES EL SEGUNDO EMPATE EXACTO DE LA OPERACION Y NO PUEDE DECIDIR "
            "NADA. Medido hoy: retention_metrics tiene grado 4 y "
            "customer_retention_metrics_webmobile tiene grado 4. En el 361 paso lo "
            "mismo (6 contra 6) y se registro como el caso limpio de la operacion; "
            "este es el segundo, y llega justo despues del 711, donde el margen fue "
            "el mas ancho de todos (10 contra 3). LOS DOS EXTREMOS EN LA MISMA "
            "VUELTA, y la eleccion se sostuvo por contenido en los dos. AQUI EL "
            "CABLEADO NO APORTA NI UN GRAMO: si el contenido estuviera mal no "
            "habria nada detras que lo tapara. NOTA: 'va_a_favor_del_elegido' se "
            "pone en False porque un empate no va a favor de nadie, y decir que si "
            "iria seria contar un cero como un voto."),
        "instrumento": ("scripts/loop/vuelta41_lectura_acto.py --puesto 969, salida "
                        "docs/loop/SALIDA_V44_ACTO969_LECTURA.txt, bloque (e)"),
        "grados_medidos_hoy": {SUP: 4, ABS[0]: 4},
        "coste_medido_de_la_eleccion": ("CERO aristas. Los dos nodos tienen CERO "
                                        "aristas propias sin reciproco, asi que "
                                        "elegir a cualquiera de los dos no pierde "
                                        "ni una arista: las reciprocas las "
                                        "reescribe la simetrizacion de run_phase1 "
                                        "paso 5."),
    },
}
