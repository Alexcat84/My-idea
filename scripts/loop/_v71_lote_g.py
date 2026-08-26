# -*- coding: utf-8 -*-
"""_v71_lote_g.py . EL CONTENIDO EDITORIAL DEL LOTE G DEL TRAMO UNICO DE OP-U-02.

NO ES UN INSTRUMENTO: es el texto del lote. La maquina que lo sella es
scripts/loop/generar_plan_del_lote.py, que entra aqui por --contenido _v71_lote_g.

EL LOTE SE DECLARA AL ABRIRLO. Abre en el ACTO 38, que es el primero del tramo
SIN DUENO medido. Los DOS saltos van DECLARADOS con su cita y NO rompen el
prefijo sin saltos, porque ninguno de los dos actos saltados esta en la cola de
fusiones de esta operacion: el acto 31 tiene dueno medido (OP-F-04-WEI y OP-S-04
en duenos_cualquier_operacion, leido hoy del fichero fijado) y el acto 37 tiene
dueno medido (OP-S-07, leido hoy del mismo fichero), y la adjudicacion 2 del acta
69 dice con todas sus letras que lo que vale para el 31 vale para el 37 cuando el
prefijo lo alcance. Sigue el PREFIJO SIN SALTOS del orden_universo de lo que
queda: el lote A de la vuelta 65 cerro los actos 1 y 3; el B de la 66 el 5, 7, 8,
9, 10 y 11; el C de la 67 el 12 al 17; el D de la 68 el 19 al 24 y dejo el 18 en
transito; el E de la 69 cerro el 18, 25, 26, 27, 29 y 30; el F de la 70 cerro el
32, 33, 34, 35 y 36.

LA DECLARACION: CINCO ACTOS CIERRAN ENTEROS Y SON 15 NODOS. Los CINCO cierran
FUNDIDOS (38, 39, 40, 41 y 42) y NINGUNO cierra DECLARADO Y NO FUNDIDO. Los
motivos de DECLARADO posibles son DOS y solo DOS (adjudicacion 4 del acta 70), y
ninguno tiene sujeto aqui: la guarda 1B pasa POR VACIO en los cinco (CERO puertas
dentro de cada acto, medido con varas_n_arias_del_tramo.py contra el universo
protegido de 256 ids) y P.5 contesta UNA FAMILIA en los cinco. P.10 y el cuarto
motivo siguen sin sujeto (cero puentes, cero triangulos y cero pares D internos
en los cinco, medido con vuelta65_puentes_del_tramo.py).

EL TOPE DEL PREFIJO NO ES ESTRUCTURAL SINO DE LOTE, Y SE DICE: el siguiente es el
ACTO 43, que NO tiene dueno y NO trae puerta. El tope cae ANTES del 43 porque el
encargo fija CINCO actos, no porque el 43 tenga nada que lo impida.

EL REPARTO VA POR ABSORBIDO en la clave reparto, que es la forma que la vuelta 65
estreno para los actos de mas de dos miembros.

DOS COSAS MEDIDAS QUE ESTE FICHERO DECLARA Y NO ESCONDE, Y LAS DOS TOCAN LA
FRONTERA DEL DUENO QUE EL ACTA 70 ADJUDICO EN SU SECCION 6.2:

  1. EL ACTO 39 tiene en docs/plan/INVENTARIO.jsonl una entrada de tipo
     familia_de_ids llamada defensas_en_profundidad, con OP-S-09 en su campo
     operaciones, y sus miembros son LOS TRES DEL ACTO: cubre la NOMINA ENTERA y
     no una parte. La letra del acta 70 dice que una entrada de OTRO tipo que
     nombra una operacion sobre PARTE de la nomina no es dueno del acto; sobre la
     nomina ENTERA la letra no lo dice, y ESO SE DECLARA en vez de estirarse. Se
     funde por el principio que esa misma letra enuncia (la familia_de_ids es
     jurisdiccion sobre SU sujeto, la familia, no sobre el acto) y porque la
     propia entrada declara su resolucion: DECISION 4 de la mesa de racimos,
     APROBADA el 9 ago 2026, familia unica, FUSION CON ALIAS, que es exactamente
     lo que esta operacion hace. VA MARCADO DISCUTIBLE Y VA COMO PREGUNTA.
  2. EL ACTO 41 tiene una entrada de la misma especie llamada
     design_for_six_sigma_dmadv, con OP-S-09 en operaciones y con DOS de los tres
     miembros: es EXACTAMENTE el caso que el acta 70 adjudico (2 de 3), y se
     funde por esa adjudicacion, citandola.

Y UNA TERCERA MEDICION QUE NINGUNA VUELTA HABIA NOMBRADO Y QUE SE NOMBRA AQUI:
las entradas de tipo acto de los cinco actos traen en operaciones NO SOLO OP-U-02
sino tambien OP-L-03, que es la mesa de la fase 09_LECTURAS_DIRIGIDAS y cuyo
campo bloquea_a nombra a OP-U-02. Leida a la letra, la frontera del dueno haria
de OP-L-03 dueno de todos los actos del tramo y ninguna fusion seria posible, que
es la misma reduccion al absurdo con la que el acta 70 resolvio el caso de
OP-U-02. Ademas la verificacion de OP-L-03 dice ningun acto se funde con un par
interno sin veredicto, que es LA MISMA letra en divergencia que el acta 65
adjudico para OP-U-02 con cuatro varas y con las palabras NO ES PARADA, y cuya
correccion declarada ya esta aplicada sobre la ficha de OP-U-02 (leida hoy). Se
declara, se cita y NO se inventa regla: va MARCADO DISCUTIBLE y va como pregunta.
"""

# ======================================================================
# ACTO 38: LA FAMILIA DE LA ESCALA DEL PROBLEMA DEL CLIENTE.
# TRES miembros del mismo libro, DOS pares internos con veredicto y los
# DOS en A, CERO D, CERO puentes, CERO triangulos y CERO puertas.
# FORMA medida: UNA SOLA VARA (la de pasos). El cableado apunta al OTRO
# lado y con el margen mas ancho del lote, y por la letra no habla.
# ======================================================================

SUP38 = "segmentos_de_clientes_problema_necesidad"

MOTIVO38 = (
    "ACTO 38 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA ESCALA DEL PROBLEMA DEL CLIENTE. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE Y NO CON "
    "IMPRESION: los TRES miembros son del MISMO LIBRO (The Startup Owner's Manual, de Steve "
    "Blank), tienen DOS pares internos con veredicto escrito de TRES combinaciones posibles y "
    "los DOS son de clase A (puestos 547 y 1216), hay CERO pares D internos, CERO nodos puente "
    "y CERO triangulos, medido con scripts/loop/vuelta65_puentes_del_tramo.py sobre el estado "
    "del dia. "
    "Y LA FAMILIA NO ES LECTURA MIA SINO DECLARACION DEL ARCHIVO: el puesto 1216 se titula LA "
    "ESCALA DEL PROBLEMA CONTADA DOS VECES y cierra con que LA MISMA ESCALA DE CUATRO NIVELES "
    "APARECE YA EN TRES ETIQUETADOS DISTINTOS EN ESTA ZONA. El par que falta es el unico sin "
    "veredicto del acto. "
    "LO QUE LAS DOS RAZONES DICEN QUE ES LO MISMO, y es el nucleo entero: ubicar el problema "
    "del cliente en una escala de conciencia o urgencia, evaluar si el producto es "
    "imprescindible o solo agradable de tener, y mapear a los distintos que intervienen en la "
    "compra. El 1216 lo dice con estas palabras: TRES DE LOS CUATRO PASOS DE "
    "problem_recognition_scale ESTAN DENTRO DE segmentos_de_clientes_problema_necesidad. "
    "P.8 EN ORDEN, Y LA FORMA MANDA: la FORMA medida es UNA SOLA VARA. La de PASOS apunta a "
    "segmentos_de_clientes_problema_necesidad (5 contra 4 y 4); la de CONDICIONES EMPATA en 2 "
    "a tres bandas y no apunta. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, "
    "pregunta 4), y las DOS razones escritas apuntan al mismo nodo. "
    "Y AQUI VA EL CHOQUE ENTERO EN VEZ DE MEDIO, PORQUE ES EL MAS ANCHO DEL LOTE POR ESTA VIA: "
    "EL CABLEADO APUNTA AL OTRO LADO, a customer_segments_hypothesis con 12 contra 5 y 4, "
    "leido de la columna cab de scripts/loop/varas_n_arias_del_tramo.py, que es la unica fuente "
    "de cifra de cableado desde la adjudicacion 3 del acta 70. LA LETRA DE P.8 ES EXPLICITA EN "
    "QUE EL CABLEADO SOLO HABLA A CONTENIDO EMPATADO, y aqui el contenido no empata. Se funde "
    "a favor del contenido, el choque va MARCADO DISCUTIBLE en el reporte con su cifra al lado, "
    "y el costo se paga en redirecciones. EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta (ni semilla de entrada ni extremo de "
    "puente aprobado), medido con scripts/loop/varas_n_arias_del_tramo.py contra el universo "
    "protegido de 256 ids. La guarda pasa POR VACIO y se dice. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; NINGUNA entrada de docs/plan/INVENTARIO.jsonl que no sea de tipo acto nombra a "
    "ninguno de los tres miembros, medido hoy con un barrido propio; NINGUNO de los tres esta "
    "en ninguna nomina de docs/RACIMOS_MIEMBROS.jsonl; y el barrido sobre "
    "docs/plan/OPERACIONES.jsonl no devuelve ninguna mencion de los tres. La entrada de tipo "
    "acto nombra OP-L-03 y OP-U-02, y eso se declara aparte en el docstring del lote."
)

NOTA38 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado en vez de maquillado. UN APPEND DE PASO Y "
    "UN APPEND DE CONDICION, mas DOS INCISO a pasos DISTINTOS, y el nodo crece de 5 pasos a 6 "
    "y de 2 condiciones a 3. "
    "LOS DOS INCISO VAN A PASOS DISTINTOS Y NINGUNO SE APILA (acta 64), y los dos son "
    "PARAMETROS CONCRETOS de gestos que el superviviente ya tiene. AL PASO 2, el cuarto nivel "
    "de la escala que el superviviente NO tiene: su escala cierra en SOLUCION CASERA y la del "
    "absorbido cierra en VISION, y el 1216 lo sella como perdida propuesta con estas palabras, "
    "EL CUARTO NIVEL ES DISTINTO. AL PASO 3, la INTENSIDAD DEL DOLOR como magnitud a "
    "determinar, que es el parametro del gesto de decidir si el producto es indispensable. "
    "Los dos pasos receptores del superviviente NO terminan en punto (uno cierra en la palabra "
    "casera y el otro en un parentesis), asi que la guarda de la JUNTURA ROTA no salta en "
    "ninguno de los dos. "
    "EL UNICO APPEND DE PASO ES EL MERCADO DE UN SOLO LADO O DE VARIOS LADOS, que es un gesto "
    "distinto y no un parametro: el superviviente mapea QUIEN interviene en la compra pero no "
    "pregunta nunca si QUIEN USA es QUIEN PAGA, que es lo que decide el modelo de negocio "
    "entero. Ninguno de los cinco pasos del superviviente lo dice. "
    "EL UNICO APPEND DE CONDICION ES UN DISPARADOR DISTINTO Y NO UN MATIZ, que es la unica "
    "puerta por la que el acta 55 (pregunta 5) deja pasar una condicion de APPEND mientras el "
    "INCISO de condiciones no exista: las DOS condiciones del superviviente disparan por un "
    "HUECO DE CONOCIMIENTO (no saber quien decide) y por un ARTEFACTO que se escribe (la "
    "historia de usuario), y la que entra dispara por la FASE DEL PROCESO (estar empezando el "
    "descubrimiento de clientes). Ninguna de las tres dispara por lo mismo. "
    "CINCO PERDIDAS SELLADAS, UNA DE ELLAS CON ATENUANTE DECLARADO Y MEDIDO, contadas por "
    "maquina sobre esta misma lista y no de memoria, que es la regla que sale de la caida del "
    "D9 de la vuelta 68."
)

PERDIDAS38 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL ROL DE QUIEN PAGA dentro del mapa de los que intervienen en la compra. El "
             "paso 4 del superviviente mapea QUIEN USA, QUIEN INFLUYE y QUIEN RECOMIENDA, y "
             "el absorbido mapea QUIEN USA, QUIEN LO PAGA y QUIEN TOMA LA DECISION FINAL: el "
             "pagador no aparece en ninguno de los cinco pasos del superviviente, y es el rol "
             "sin el cual el mercado de varios lados no se puede razonar"),
     "donde": "paso 2 de customer_segments_hypothesis",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("QUE SE CLASIFICA EN LA ESCALA: el absorbido clasifica CADA TIPO DE CLIENTE "
             "IMPORTANTE y el superviviente clasifica EL PROBLEMA. El 1216 sella esta perdida "
             "con esas mismas palabras y la llama fina y real. ATENUANTE DECLARADO Y MEDIDO: "
             "el cuarto nivel que faltaba, el de VISION, SI llega, y llega por el INCISO al "
             "paso 2 de este mismo acto; lo que no llega es que el sujeto clasificado sea el "
             "cliente y no el problema"),
     "donde": "paso 2 de problem_recognition_scale",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL VERBO BUSCAR ESPECIFICAMENTE a los clientes que ya intentaron construir su "
             "propia solucion. El paso 2 del superviviente nombra la SOLUCION CASERA como el "
             "cuarto nivel de la escala, o sea como una casilla en la que un cliente CAE, no "
             "como una poblacion que se sale a BUSCAR a proposito, que es el gesto del "
             "absorbido"),
     "donde": "paso 3 de problem_recognition_scale",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de NO TENER CLARO QUIEN ES TU CLIENTE. La condicion 1 del "
             "superviviente dispara por no tener claro QUIEN TOMA LA DECISION DE COMPRA dentro "
             "del negocio del cliente, que presupone al cliente ya identificado: es el hueco "
             "de despues, no el de antes"),
     "donde": "condicion 1 de customer_segments_hypothesis",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador del PITCH DE VENTAS, o sea el momento en que la escala se usa para "
             "escribir el argumento con el que se vende. La condicion 2 del superviviente "
             "nombra la HISTORIA DE USUARIO y la URGENCIA, que son el artefacto de producto y "
             "no el de venta"),
     "donde": "condicion 2 de problem_recognition_scale",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO38 = {
    "customer_segments_hypothesis": {
        "pasos": {
            # EL PRIMER INCISO DEL ACTO: el cuarto nivel de la escala que el
            # superviviente no tiene, adosado DENTRO del paso donde vive la escala.
            "1": ("INCISO", 2, "aun no existe y tu le muestras una vision", ", y también cuando "),
            "2": ("CUBIERTO", 4),   # con perdida: el rol de quien paga
            "3": ("CUBIERTO", 3),   # indispensable frente a agradable de tener
            "4": ("APPEND",),       # EL MERCADO DE UN SOLO LADO O DE VARIOS: el unico APPEND de paso
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: no saber QUIEN ES el cliente
            "2": ("APPEND",),       # LA FASE DEL DESCUBRIMIENTO: disparador distinto
        },
    },
    "problem_recognition_scale": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # salir a entender como el cliente vive el problema
            "2": ("CUBIERTO", 2),   # con perdida y atenuante medido: que se clasifica
            "3": ("CUBIERTO", 2),   # con perdida: el verbo buscar a los de solucion casera
            # EL SEGUNDO INCISO: la intensidad del dolor como parametro del paso 3.
            "4": ("INCISO", 3, "la intensidad del dolor que causa el problema", ", determinando "),
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),   # la urgencia del problema, que el superviviente nombra
            "2": ("CUBIERTO", 2),   # con perdida: el pitch de ventas
        },
    },
}


# ======================================================================
# ACTO 39: EL RACIMO DE LAS DEFENSAS EN PROFUNDIDAD.
# TRES miembros del mismo libro, DOS pares internos con veredicto y los
# DOS en A, CERO D, CERO puentes, CERO triangulos y CERO puertas.
# FORMA medida: UNA SOLA VARA (la de pasos). Es el acto donde LAS DOS
# RAZONES CORONAN SUPERVIVIENTES DISTINTOS, y donde el archivo declara
# UNA FIGURA PROPIA: EL HERMANO QUE CORRIGE AL HERMANO.
# ======================================================================

SUP39 = "defensas_en_profundidad_3"

MOTIVO39 = (
    "ACTO 39 DEL TRAMO UNICO DE OP-U-02, EL RACIMO DE LAS DEFENSAS EN PROFUNDIDAD. "
    "UNA SOLA FAMILIA, Y AQUI LA PREGUNTA DE P.5 NO LA CONTESTA UNA LECTURA MIA SINO UNA "
    "DECISION APROBADA: los TRES miembros son del MISMO LIBRO (Managing the Risks of "
    "Organizational Accidents, de James Reason), tienen DOS pares internos con veredicto "
    "escrito de TRES combinaciones posibles y los DOS son de clase A (puestos 2236 y 2283), "
    "hay CERO pares D internos, CERO nodos puente y CERO triangulos, medido. El puesto 2283 "
    "cierra declarando RACIMO DE LAS DEFENSAS EN PROFUNDIDAD, TRES MIEMBROS Y SIN UNA SOLA "
    "ARISTA. Y docs/plan/INVENTARIO.jsonl trae una entrada de tipo familia_de_ids llamada "
    "defensas_en_profundidad con LOS TRES miembros del acto y con esta nota, leida hoy: "
    "DECISION 4 DE LA MESA DE RACIMOS, APROBADA EL 9 AGO 2026, FAMILIA UNICA, FUSION CON "
    "ALIAS. UNA FAMILIA, y lo dice el archivo con visto del fundador. "
    "LAS DOS RAZONES CORONAN SUPERVIVIENTES DISTINTOS, Y ESO VA DICHO ENTERO EN VEZ DE "
    "ESCONDIDO: el 2236 cierra con SOBREVIVE defensas_en_profundidad y el 2283 cierra con "
    "SOBREVIVE defensas_en_profundidad_3. Las dos coronaciones son sobre SU PROPIO PAR y las "
    "dos matan al mismo nodo, defensas_en_profundidad_2; EL PAR QUE FALTA, el unico sin "
    "veredicto del acto, es exactamente el que enfrentaria a los dos coronados. Es la misma "
    "forma que el acto 34 del lote F, que el acta 70 adjudico A FAVOR en su D6 con estas "
    "palabras: cada corona es sobre SU par y las dos razones matan al mismo nodo. NINGUNA "
    "RAZON ESCRITA SE DESMIENTE al fundir a favor de defensas_en_profundidad_3, porque el 2236 "
    "dice que defensas_en_profundidad gana A defensas_en_profundidad_2 y NO dice nada sobre "
    "defensas_en_profundidad_3. "
    "LO QUE DECIDE ES P.8, Y EN ORDEN: la FORMA medida es UNA SOLA VARA. La de PASOS apunta a "
    "defensas_en_profundidad_3 (4 contra 3 y 3); la de CONDICIONES EMPATA en 2 y no apunta. "
    "UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4). "
    "Y HAY CONTENIDO ADEMAS DE LA CUENTA, QUE ES LO QUE P.8 LLAMA CONTENIDO: el 2283 declara "
    "una FIGURA NUEVA y le pone nombre, EL HERMANO QUE CORRIGE AL HERMANO, y la mide: el paso "
    "2 del superviviente, EVALUAR SI EXISTEN DEPENDENCIAS OCULTAS ENTRE CAPAS QUE SE ASUMEN "
    "INDEPENDIENTES, es EXACTAMENTE LO CONTRARIO de evaluar cada capa DE FORMA INDEPENDIENTE "
    "como pide el paso 2 del absorbido; y su paso 4, la COMPLACENCIA OPERATIVA por confiar en "
    "las multiples defensas, es EL REVERSO del principio de redundancia que el otro predica. "
    "Un nodo que desmiente el supuesto de sus dos hermanos no es el hermano chico del racimo. "
    "Y AQUI VA EL CHOQUE, ENTERO: EL CABLEADO APUNTA AL OTRO LADO Y CON EL MARGEN MAS ANCHO "
    "DEL TRAMO, a defensas_en_profundidad con 11 contra 3 y 2, leido de la columna cab del "
    "instrumento de varas y no de contar listas (adjudicacion 3 del acta 70). Ese nodo tiene "
    "NUEVE previos y CUATRO siguientes, o sea que fundirlo obliga a redirigir. LA LETRA DE P.8 "
    "ES EXPLICITA: el cableado solo habla a contenido empatado, y aqui el contenido no empata. "
    "El propio banco lo tiene ejemplificado con DIEZ CONTRA CINCO, Y PIERDE. Va MARCADO "
    "DISCUTIBLE en el reporte con su cifra al lado, y es el discutible mas fuerte del lote. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta, medido contra el universo protegido de "
    "256 ids. La guarda pasa POR VACIO y se dice. "
    "DUENOS, Y AQUI HAY UNA MEDICION QUE SE DECLARA EN VEZ DE CALLARSE: los dos campos del "
    "fichero fijado del tramo estan VACIOS para este acto, medido hoy; ninguno de los tres esta "
    "en ninguna nomina de docs/RACIMOS_MIEMBROS.jsonl; y el barrido sobre "
    "docs/plan/OPERACIONES.jsonl no devuelve ninguna mencion. PERO la entrada familia_de_ids "
    "citada arriba trae OP-S-09 en su campo operaciones Y CUBRE LA NOMINA ENTERA, 3 de 3. La "
    "adjudicacion 2 del acta 70 resolvio el caso de una entrada asi sobre PARTE de la nomina; "
    "sobre la nomina ENTERA su letra NO LO DICE, y eso se declara en vez de estirarse. SE FUNDE "
    "POR EL PRINCIPIO QUE ESA MISMA LETRA ENUNCIA, que es de TIPO y no de cobertura: una "
    "entrada de tipo familia_de_ids es jurisdiccion sobre SU sujeto, la familia, y lo que la "
    "fusion le debe es dejarselo servible y publicarlo. Y SE FUNDE ADEMAS PORQUE LA PROPIA "
    "ENTRADA DECLARA SU RESOLUCION: familia unica, FUSION CON ALIAS, aprobada por la mesa de "
    "racimos, que es exactamente lo que esta operacion ejecuta. LA CONSECUENCIA PARA OP-S-09 SE "
    "PUBLICA PARA QUE NO SE LA ENCUENTRE: tras esta fusion la familia queda con UN solo id "
    "vivo y ese id es defensas_en_profundidad_3, o sea EL QUE LLEVA EL SUFIJO NUMERICO. La "
    "verificacion de OP-S-09 exige que NINGUN ID VIVO LLEVE SUFIJO NUMERICO DE DUPLICADO, asi "
    "que le queda un RENOMBRE CON ALIAS, que es exactamente su tipo. Esta operacion no lo hace "
    "y no lo estorba. VA MARCADO DISCUTIBLE Y VA COMO PREGUNTA AL AUDITOR."
)

NOTA39 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado. TRES APPEND DE PASO Y UN INCISO, CERO "
    "APPEND DE CONDICION, y el nodo crece de 4 pasos a 7 y de 2 condiciones a 2. ES EL ACTO "
    "QUE MAS CRECE DEL LOTE Y VA MARCADO DISCUTIBLE POR ESO TAMBIEN. "
    "EL INCISO AL PASO 1 ES LA PIEZA QUE LA RAZON NOMBRA COMO EL INSTRUMENTO DEL ABSORBIDO, y "
    "es la unica forma de conservarla donde sirve. El 2236 lo dice con todas sus letras: "
    "defensas_en_profundidad SI TRAE UN INSTRUMENTO NOMBRADO QUE EL OTRO NO TIENE, LAS SIETE "
    "FUNCIONES DEFENSIVAS COMO TAXONOMIA DE INVENTARIO, QUE ES LO QUE CONVIERTE LA "
    "CLASIFICACION EN UN PROCEDIMIENTO CON CASILLAS Y NO EN UNA INTENCION. Un APPEND la habria "
    "puesto al final, lejos del mapeo; el INCISO la deja DENTRO del paso 1, que es donde se "
    "mapean las capas. El paso 1 del superviviente NO termina en punto (cierra con un "
    "parentesis), asi que la guarda de la JUNTURA ROTA no salta. "
    "LOS TRES APPEND DE PASO SON TRES GESTOS DISTINTOS Y NINGUNO ES UN PARAMETRO, y se "
    "nombran uno a uno en vez de contarse: EL BALANCE ENTRE DEFENSAS DURAS Y BLANDAS, que es "
    "la segunda mitad de lo que el 2236 llama clasificar por funcion Y MODO y que el "
    "superviviente no tiene en ninguno de sus cuatro pasos; LA IDENTIFICACION DE FUNCIONES "
    "DEFENSIVAS AUSENTES O DEBILES, que es el rendimiento de la taxonomia que entra por el "
    "INCISO y sin la cual el inventario no dice nada; y EL DISENO DE REDUNDANCIA ENTRE CAPAS, "
    "que entra porque LA RAZON LO MANDA con esas palabras, el 2236 cierra con Y EL PRINCIPIO "
    "DE REDUNDANCIA SE ABSORBE COMO LINEA SUYA. "
    "Y AQUI VA UNA COSA QUE NO SE DEJA IMPLICITA, PORQUE ES LA FIGURA DEL ACTO: EL PASO 3 QUE "
    "ENTRA DE APPEND (disenar redundancia) Y EL PASO 4 QUE EL SUPERVIVIENTE YA TIENE (revisar "
    "si la confianza en las multiples defensas ha generado complacencia) SE MIRAN DE FRENTE. "
    "El 2283 lo dice: el paso 4 del superviviente ES EL REVERSO del principio de redundancia. "
    "LOS DOS QUEDAN VIVOS Y JUNTOS A PROPOSITO, porque el aviso sin el principio no se entiende "
    "y el principio sin el aviso es lo que el libro entero viene a corregir. LO QUE ESTA "
    "OPERACION NO HACE ES REDACTAR LA BISAGRA ENTRE LOS DOS, porque redactar no es repartir: "
    "eso queda enrutado a la fase 04 y va dicho aqui para que nadie lo de por hecho. "
    "CINCO PERDIDAS SELLADAS, UNA DE ELLAS CON DOS SEDES EN UN SOLO CAMPO por el criterio que "
    "el acta 67 adjudico en su D10 (LA FILA ES POR PIEZA QUE SE PIERDE, NO POR SITIO DONDE "
    "VIVIA): el disparador de DISENAR O AUDITAR un sistema de seguridad vive en la condicion 1 "
    "de los DOS absorbidos y va en UNA fila con las dos sedes nombradas. "
    "Y UNA PERDIDA QUE NO ES UNA PERDIDA CORRIENTE Y SE SELLA IGUAL: el paso 2 del absorbido "
    "defensas_en_profundidad_2 pide evaluar cada capa DE FORMA INDEPENDIENTE, y el paso 2 del "
    "superviviente pide EXACTAMENTE LO CONTRARIO. No se pierde por descuido: se pierde porque "
    "el propio archivo declara desmentido el supuesto. Se sella con su motivo escrito para que "
    "la fase 04 sepa que ahi hubo una correccion y no un olvido."
)

PERDIDAS39 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL SUJETO DEL INVENTARIO: LAS DEFENSAS ACTUALES DE LA ORGANIZACION. El paso 1 "
             "del superviviente mapea LAS CAPAS DE DEFENSA DEL SISTEMA, que es el mismo "
             "objeto nombrado por su arquitectura y no por su dueno, y con ello se pierde que "
             "el inventario sea de lo que la organizacion TIENE HOY. ATENUANTE DECLARADO: la "
             "taxonomia de las siete funciones, que es lo que el 2236 nombra como el "
             "instrumento propio de este nodo, SI llega, y llega por el INCISO al paso 1 de "
             "este mismo acto"),
     "donde": "paso 1 de defensas_en_profundidad",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EVALUAR LA INTEGRIDAD DE CADA CAPA DE FORMA INDEPENDIENTE. NO SE PIERDE POR "
             "DESCUIDO Y ESO SE ESCRIBE: el paso 2 del superviviente pide EXACTAMENTE LO "
             "CONTRARIO, evaluar si existen DEPENDENCIAS OCULTAS entre capas que se asumen "
             "independientes, y el puesto 2283 declara esa oposicion como FIGURA con nombre, "
             "EL HERMANO QUE CORRIGE AL HERMANO. Lo que se pierde es el gesto de medir la "
             "integridad DE CADA CAPA, que sigue siendo util aunque el supuesto de "
             "independencia este desmentido"),
     "donde": "paso 2 de defensas_en_profundidad_2",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA CLASIFICACION POR MODO PEGADA A LA CLASIFICACION POR FUNCION, o sea que las "
             "dos se hagan EN EL MISMO GESTO y no en dos pasos separados. ATENUANTE DECLARADO "
             "Y ES LA ESPECIE DEL PENDIENTE 4: el modo DURA O BLANDA llega ENTERO por el "
             "APPEND del paso 2 de defensas_en_profundidad, y la funcion llega por el INCISO "
             "al paso 1; lo que no llega es que sean UN SOLO PASO"),
     "donde": "paso 1 de defensas_en_profundidad_2",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de DISENAR O AUDITAR UN SISTEMA DE SEGURIDAD, que es el momento "
             "profesional en que este procedimiento se abre. Las DOS condiciones del "
             "superviviente disparan por el ESTADO DEL SISTEMA (depender de multiples capas "
             "redundantes) y por un SUCESO (un accidente donde fallaron varias defensas): "
             "ninguna dispara por el ENCARGO. UNA SOLA PIEZA CON DOS SEDES, sellada una vez "
             "con las dos nombradas (acta 67, D10)"),
     "donde": ("condicion 1 de defensas_en_profundidad y condicion 1 de "
               "defensas_en_profundidad_2"),
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de TENER QUE JUSTIFICAR POR QUE MULTIPLES BARRERAS NO GARANTIZAN "
             "SEGURIDAD ABSOLUTA, que es el uso ARGUMENTATIVO del procedimiento y no el "
             "diagnostico. La condicion 1 del superviviente mira el mismo hecho, la "
             "dependencia de multiples capas, pero como SITUACION y no como discusion que hay "
             "que ganar"),
     "donde": "condicion 2 de defensas_en_profundidad_2",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO39 = {
    "defensas_en_profundidad": {
        "pasos": {
            # EL UNICO INCISO DEL ACTO: la taxonomia de las siete funciones,
            # dentro del paso donde se mapean las capas.
            "1": ("INCISO", 1, "clasificandolas en las siete funciones defensivas", ", "),
            "2": ("APPEND",),       # EL BALANCE ENTRE DEFENSAS DURAS Y BLANDAS
            "3": ("APPEND",),       # LAS FUNCIONES AUSENTES O DEBILES
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida de dos sedes: disenar o auditar
        },
    },
    "defensas_en_profundidad_2": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # con perdida y atenuante del pendiente 4: funcion mas modo
            "2": ("CUBIERTO", 2),   # con perdida declarada: el superviviente dice lo contrario
            "3": ("APPEND",),       # EL DISENO DE REDUNDANCIA, que la razon manda absorber
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # segunda sede de la perdida de disenar o auditar
            "2": ("CUBIERTO", 1),   # con perdida: el uso argumentativo
        },
    },
}


# ======================================================================
# ACTO 40: LA FAMILIA DE LA META DE TRACCION.
# TRES miembros del mismo libro, DOS pares internos con veredicto y los
# DOS en A, CERO D, CERO puentes, CERO triangulos y CERO puertas.
# FORMA medida: UNA SOLA VARA (la de pasos). El cableado EMPATA a tres
# bandas, o sea que ni podria desempatar si le tocara.
# ======================================================================

SUP40 = "traction_goal"

MOTIVO40 = (
    "ACTO 40 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA META DE TRACCION. "
    "UNA SOLA FAMILIA, Y LA DECLARA EL ARCHIVO: los TRES miembros son del MISMO LIBRO "
    "(Traction, de Gabriel Weinberg), tienen DOS pares internos con veredicto escrito de TRES "
    "combinaciones posibles y los DOS son de clase A (puestos 627 y 824), hay CERO pares D "
    "internos, CERO nodos puente y CERO triangulos, medido. El puesto 824 cierra con estas "
    "palabras: LA FAMILIA DE LA META DE TRACCION LLEGA A TRES NODOS Y DOS PARES LEIDOS, LOS "
    "DOS EN A, y los nombra a los tres; y anade TRES NODOS PARA UNA SOLA IDEA, Y NINGUNO "
    "ENLAZA A OTRO. El par que falta es el unico sin veredicto del acto. "
    "LO QUE LAS DOS RAZONES DICEN QUE ES LO MISMO: fijar una meta de traccion cuantificable en "
    "NUMEROS CONCRETOS y no en adjetivos, alinearla con lo que se persigue en esta etapa, y "
    "descartar o bajar de prioridad lo que no mueve la aguja hacia ella. "
    "P.8 EN ORDEN: la FORMA medida es UNA SOLA VARA. La de PASOS apunta a traction_goal (5 "
    "contra 4 y 3); la de CONDICIONES EMPATA en 2 a tres bandas; y EL CABLEADO TAMBIEN EMPATA, "
    "3 a tres bandas, leido de la columna cab del instrumento de varas. Es el unico acto del "
    "lote en el que el cableado NI SIQUIERA PODRIA DESEMPATAR si le tocara, y se dice porque "
    "un empate de cableado que nadie nombra parece un dato que no se miro. UNA SOLA VARA DE "
    "CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4). "
    "Y LA RAZON ESCRITA APUNTA AL MISMO NODO SIN NOMBRARLO COMO SUPERVIVIENTE: el 627 dice que "
    "LO PROPIO DE traction_goal ES LA MECANICA DE CALENDARIO, desglosar la meta en "
    "subobjetivos cuantitativos CON FECHAS LIMITE, ponerlos en el calendario junto a los hitos "
    "de producto y reevaluar al cambiar de fase, y cierra con EL CALENDARIO CON FECHAS Y LAS "
    "FASES NUMERADAS SON LO MAS CONCRETO DEL PAR Y ES LO QUE SE PERDERIA. Un nodo cuya perdida "
    "la razon describe como lo mas concreto del par no es el nodo que muere. NINGUNA RAZON "
    "CORONA A NADIE EN ESTE ACTO, y eso se dice en vez de fabricarle una coronacion. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta, medido contra el universo protegido de "
    "256 ids. La guarda pasa POR VACIO y se dice. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; NINGUNA entrada de docs/plan/INVENTARIO.jsonl que no sea de tipo acto nombra a "
    "ninguno de los tres; ninguno esta en ninguna nomina de docs/RACIMOS_MIEMBROS.jsonl; y el "
    "barrido sobre docs/plan/OPERACIONES.jsonl no devuelve ninguna mencion. El dueno es EL "
    "MEDIDO y aqui no hay ninguno."
)

NOTA40 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado. DOS APPEND DE PASO Y UN INCISO, CERO "
    "APPEND DE CONDICION, y el nodo crece de 5 pasos a 7 y de 2 condiciones a 2. "
    "EL INCISO AL PASO 1 ES EL PARAMETRO QUE LAS DOS RAZONES PONEN EN EL CENTRO: los NUMEROS "
    "CONCRETOS. El superviviente manda definir un objetivo CUANTIFICABLE Y SIGNIFICATIVO, que "
    "es el genero; el absorbido dice de que numeros se trata, CANTIDAD DE CLIENTES Y TASA DE "
    "CRECIMIENTO MENSUAL, que es la especie. El paso 1 del superviviente NO termina en punto, "
    "asi que la guarda de la JUNTURA ROTA no salta. "
    "LOS DOS APPEND DE PASO SON LOS DOS GESTOS QUE LAS RAZONES NOMBRAN COMO PROPIOS DE CADA "
    "ABSORBIDO, y se nombran uno a uno: LA REGLA DE DESCARTE, evaluar cada actividad de "
    "marketing preguntando si mueve la aguja hacia la meta, que el 627 llama LA REGLA DE "
    "DESCARTE EXPLICITA de definir_meta_de_traccion; y EL CALCULO PREVIO POR CANAL, estimar el "
    "VOLUMEN POTENCIAL de un canal ANTES de invertir en el, que el 824 llama lo que CONVIERTE "
    "LA DOCTRINA EN UN FILTRO APLICABLE CANAL POR CANAL. El superviviente no tiene ninguno de "
    "los dos: sus cinco pasos definen, alinean, desglosan, calendarizan y reevaluan, y ninguno "
    "descarta nada. "
    "DOS PERDIDAS CON ATENUANTE DECLARADO Y MEDIDO, Y LAS DOS DE LA ESPECIE DEL PENDIENTE 4, "
    "contadas por maquina sobre esta misma lista: el verbo DESCARTAR y el descarte POR CANAL "
    "llegan los dos por los APPEND de este mismo acto, y lo que se sella es lo que NO llega con "
    "ellos. "
    "SEIS PERDIDAS SELLADAS EN TOTAL, TRES DE PARAMETRO DE PASO Y TRES DE CONDICIONES. Es el "
    "acto del lote con mas perdidas de condiciones, y la razon esta medida: el superviviente "
    "entra con DOS condiciones muy generales (al iniciar cualquier esfuerzo de traccion, y al "
    "cambiar de fase) y los dos absorbidos traen CUATRO disparadores especificos entre los dos."
)

PERDIDAS40 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL ORDEN: la pregunta de si lo que persigues AHORA es levantar fondos o llegar a "
             "rentabilidad es en el absorbido EL PASO 1, o sea el ARRANQUE que fija el numero, "
             "y en el superviviente es el paso 2, o sea una VERIFICACION de alineacion "
             "posterior. El 824 lo llama LA PREGUNTA DE ARRANQUE y anade PORQUE CAMBIA EL "
             "NUMERO: lo que se pierde es que la eleccion venga ANTES de la meta y no despues"),
     "donde": "paso 1 de definir_meta_de_traccion",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL VERBO DESCARTAR con todas sus letras, y el sujeto ESTRATEGIAS QUE GENERAN "
             "RESULTADOS MARGINALES. ATENUANTE DECLARADO Y ES LA ESPECIE DEL PENDIENTE 4: la "
             "regla de descarte llega ENTERA por el APPEND del paso 3 de este mismo absorbido, "
             "que manda evaluar cada actividad preguntando si mueve la aguja; lo que no llega "
             "es el acto de descartar dicho como paso propio"),
     "donde": "paso 4 de definir_meta_de_traccion",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL SUJETO DEL DESCARTE CUANDO ES UN CANAL QUE FUNCIONA: descartar o bajar de "
             "prioridad canales QUE AUNQUE FUNCIONEN no generan el volumen necesario, que es "
             "el caso dificil y el unico que hace falta escribir. ATENUANTE DECLARADO Y ES LA "
             "ESPECIE DEL PENDIENTE 4: el descarte llega por el APPEND del paso 3 de "
             "definir_meta_de_traccion y el calculo por canal llega por el APPEND del paso 2 "
             "de este mismo nodo; lo que no llega es la clausula AUNQUE FUNCIONEN"),
     "donde": "paso 3 de moving_the_needle",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de QUE EL EQUIPO NO TENGA CLARIDAD SOBRE QUE RESULTADOS DE "
             "MARKETING IMPORTAN REALMENTE. La condicion 1 del superviviente dispara por el "
             "MOMENTO (al iniciar cualquier esfuerzo de crecimiento o traccion) y no por el "
             "SINTOMA, que es lo que hace que alguien busque este procedimiento cuando ya "
             "esta dentro"),
     "donde": "condicion 1 de definir_meta_de_traccion",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador del RESULTADO AMBIGUO: obtener resultados en un canal y NO SABER "
             "SI SON SUFICIENTES. Ninguna de las dos condiciones del superviviente mira un "
             "resultado ya obtenido: las dos miran el arranque de un esfuerzo o el cambio de "
             "fase"),
     "donde": "condicion 1 de moving_the_needle",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador del RIESGO DE DISPERSAR ESFUERZOS EN CANALES DE BAJO IMPACTO, que "
             "es el unico de los cuatro que mira hacia adelante y no hacia el estado actual. "
             "El superviviente no tiene ninguna condicion de riesgo anticipado"),
     "donde": "condicion 2 de moving_the_needle",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO40 = {
    "definir_meta_de_traccion": {
        "pasos": {
            "1": ("CUBIERTO", 2),   # con perdida: el orden, arranque frente a verificacion
            # EL UNICO INCISO DEL ACTO: los numeros concretos, dentro del paso
            # donde se define el objetivo cuantificable.
            "2": ("INCISO", 1, "cantidad de clientes y tasa de crecimiento mensual",
                  ", en números concretos como "),
            "3": ("APPEND",),       # LA REGLA DE DESCARTE: evaluar si mueve la aguja
            "4": ("CUBIERTO", 1),   # con perdida y atenuante del pendiente 4: el verbo descartar
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: el sintoma frente al momento
            "2": ("CUBIERTO", 1),   # antes de una campana de adquisicion: lo dice el momento
        },
    },
    "moving_the_needle": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # define la meta en numeros concretos
            "2": ("APPEND",),       # EL CALCULO PREVIO POR CANAL
            "3": ("CUBIERTO", 1),   # con perdida y atenuante del pendiente 4: el canal que funciona
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: el resultado ambiguo
            "2": ("CUBIERTO", 1),   # con perdida: el riesgo de dispersion
        },
    },
}


# ======================================================================
# ACTO 41: LA FAMILIA DEL DESIGN FOR SIX SIGMA DE JURAN.
# TRES miembros del mismo libro, DOS pares internos con veredicto y los
# DOS en A, CERO D, CERO puentes, CERO triangulos y CERO puertas.
# FORMA medida: TODAS DE ACUERDO. Es el acto mas limpio del lote y el
# unico que NO hace crecer a su superviviente ni un paso.
# ======================================================================

SUP41 = "design_for_six_sigma_dfss"

MOTIVO41 = (
    "ACTO 41 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DEL DESIGN FOR SIX SIGMA DE JURAN. "
    "UNA SOLA FAMILIA, Y LAS DOS RAZONES LA DECLARAN CON LA MISMA FORMULA: los TRES miembros "
    "son del MISMO LIBRO (Juran's Quality Handbook, de Joseph A. Defeo), tienen DOS pares "
    "internos con veredicto escrito de TRES combinaciones posibles y los DOS son de clase A "
    "(puestos 2465 y 2547), hay CERO pares D internos, CERO nodos puente y CERO triangulos, "
    "medido. Los dos absorbidos son LAS CINCO LETRAS DE DMADV contadas dos veces, y las dos "
    "razones lo dicen con esas palabras: SUS CINCO PASOS SON LAS CINCO LETRAS DE DMADV Y ESTAN "
    "TODAS EN EL OTRO. "
    "EL SUPERVIVIENTE ESTA DECLARADO VERBATIM EN LAS DOS RAZONES, Y ESO ES LO QUE DECIDE: el "
    "2465 cierra con SOBREVIVE design_for_six_sigma_dfss y el 2547 cierra con SOBREVIVE "
    "design_for_six_sigma_dfss. Es el unico acto del lote con las dos coronaciones en el mismo "
    "nodo y sin residuo. El 2547 anade que design_for_six_sigma_dfss GANA SU SEGUNDO PAR Y "
    "NINGUN PAR LEIDO LO HA HECHO PERDER, y lo llama TERCERA CANDIDATA A GANADOR POR DERECHO "
    "DEL DOMINIO. "
    "P.8 EN ORDEN, Y NO HACE FALTA LLEGAR AL CABLEADO: la FORMA medida es TODAS DE ACUERDO. La "
    "vara de PASOS apunta a design_for_six_sigma_dfss (6 contra 5 y 5), la de CONDICIONES "
    "apunta al mismo (4 contra 2 y 3) y el CABLEADO apunta tambien al mismo (12 contra 3 y 3, "
    "leido de la columna cab del instrumento de varas). CUANDO TODAS LAS VARAS DE CONTENIDO "
    "CONCUERDAN SE FUNDE A SU LADO, y las TRES cuentas apuntan al mismo sitio. EL ROTULO SOLO Y "
    "LA CANTIDAD NUNCA DECIDEN, y ninguna de las tres cuentas se teclea. "
    "Y NO HAY PERDIDA DE NOMBRE, Y LO COMPRUEBA LA RAZON Y NO YO: el 2465 cierra con Y NO HAY "
    "PERDIDA DE NOMBRE, COMPROBADO: EL TITULO DEL SUPERVIVIENTE DICE DFSS Y METODOLOGIA DMADV, "
    "ASI QUE LA DENOMINACION POR LA QUE SE BUSCA SIGUE EN EL TEXTO. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta, medido contra el universo protegido de "
    "256 ids. La guarda pasa POR VACIO y se dice. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; ninguno de los tres esta en ninguna nomina de docs/RACIMOS_MIEMBROS.jsonl; y el "
    "barrido sobre docs/plan/OPERACIONES.jsonl no devuelve ninguna mencion. PERO "
    "docs/plan/INVENTARIO.jsonl SI trae una entrada de tipo familia_de_ids llamada "
    "design_for_six_sigma_dmadv, con miembros design_for_six_sigma_dmadv y "
    "design_for_six_sigma_dmadv_2 y con OP-S-09 en su campo operaciones. ES EXACTAMENTE EL CASO "
    "QUE EL ACTA 70 ADJUDICO EN SU SECCION 6.2, DOS DE TRES DE LA NOMINA, y se funde por esa "
    "adjudicacion citandola: una entrada de OTRO tipo que nombra una operacion sobre PARTE de "
    "la nomina NO es dueno del acto, es jurisdiccion sobre SU sujeto. LA CONSECUENCIA PARA "
    "OP-S-09 SE PUBLICA: tras esta fusion esa familia queda con CERO ids vivos, porque sus DOS "
    "miembros son los dos absorbidos y el superviviente no pertenece a ella. El estado que la "
    "entrada declara es PENDIENTE, SE RESUELVE POR CONTINUA O REPITE, y esta fusion la resuelve "
    "por REPITE, que es una de las dos salidas escritas: los dos ids mueren dejando alias sobre "
    "design_for_six_sigma_dfss, y ningun id vivo de esa familia queda con sufijo numerico. Esta "
    "operacion no le estorba: le cierra el caso."
)

NOTA41 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado. CERO APPEND, CERO INCISO, y el nodo NO "
    "CRECE NI UN PASO NI UNA CONDICION: se queda en 6 pasos y 4 condiciones. ES EL UNICO ACTO "
    "DEL LOTE ASI, y se dice en vez de dejarlo como un hueco en la tabla. "
    "LA RAZON DE LOS CERO APPEND ESTA MEDIDA Y NO ES PEREZA: las DIEZ piezas de paso de los dos "
    "absorbidos son las cinco letras de DMADV contadas dos veces, y las dos razones dicen que "
    "estan TODAS dentro de los seis pasos del superviviente. Un APPEND aqui repetiria lo que ya "
    "esta escrito y engordaria el nodo sin anadirle un gesto. "
    "LA RAZON DE LOS CERO INCISO TAMBIEN ESTA MEDIDA, Y ES LA PUNTUACION, que es el carril que "
    "el acta 66 adjudico en su D5: LOS SEIS PASOS DEL SUPERVIVIENTE TERMINAN EN PUNTO, los "
    "seis, comprobado leyendolos, asi que cualquier INCISO con nexo de coma caeria en la guarda "
    "de la JUNTURA ROTA del generador. No se fuerza ninguno, y se dice en vez de dejarlo como "
    "un cero mudo. Es la misma situacion del acto 33 del lote F. "
    "SEIS PERDIDAS SELLADAS, Y AQUI LA CIFRA ALTA NO ES DESCUIDO SINO LO CONTRARIO: donde no "
    "hay APPEND ni INCISO, TODO lo que el absorbido tenia de propio se pierde o se cubre, y lo "
    "que se pierde se NOMBRA. UNA DE ELLAS CON DOS SEDES EN CAMPOS DISTINTOS por el criterio "
    "que el acta 67 adjudico en su D10 (LA FILA ES POR PIEZA QUE SE PIERDE, NO POR SITIO DONDE "
    "VIVIA): las NECESIDADES OCULTAS DEL CLIENTE viven en el paso 2 Y en la condicion 3 de "
    "design_for_six_sigma_dmadv_2 y van en UNA fila con las dos sedes nombradas. "
    "Y LA MAS PESADA VA CON EL MOTIVO QUE SU PROPIO AUTOR LE PUSO: el 2547 sella PERDIDA "
    "NOMBRADA, MOTIVO ALCANCE sobre DESCUBRIR LAS NECESIDADES OCULTAS DEL CLIENTE, y anade que "
    "NO ES LO MISMO QUE TRADUCIR LAS NECESIDADES DECLARADAS Y ES DE DONDE SALE LA "
    "CARACTERISTICA INNOVADORA. Esta operacion no la repone y no finge reponerla: la sella con "
    "el motivo del archivo y la enruta."
)

PERDIDAS41 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("DESCUBRIR LAS NECESIDADES OCULTAS DEL CLIENTE. Es la perdida que el propio "
             "puesto 2547 sella con estas palabras, PERDIDA NOMBRADA, MOTIVO ALCANCE, y "
             "explica: NO ES LO MISMO QUE TRADUCIR LAS NECESIDADES DECLARADAS Y ES DE DONDE "
             "SALE LA CARACTERISTICA INNOVADORA. El paso 2 del superviviente traduce las "
             "necesidades en CTQ medibles, que es el gesto sobre lo que el cliente YA DIJO. "
             "UNA SOLA PIEZA CON DOS SEDES EN CAMPOS DISTINTOS, sellada una vez con las dos "
             "nombradas (acta 67, D10)"),
     "donde": ("paso 2 de design_for_six_sigma_dmadv_2 y condicion 3 de "
               "design_for_six_sigma_dmadv_2"),
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL DISENO DE ALTO NIVEL como artefacto intermedio nombrado, o sea que del "
             "analisis salga PRIMERO un diseno grueso con los CTQ dentro y solo despues el "
             "detalle. El paso 3 del superviviente analiza la voz del cliente y evalua varios "
             "conceptos con metodos estadisticos, y el 4 disena en detalle: entre los dos no "
             "queda nombrado el escalon del medio"),
     "donde": "paso 3 de design_for_six_sigma_dmadv",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("OPTIMIZAR ANTES DE TRANSFERIR A OPERACIONES, con la TRANSFERENCIA A OPERACIONES "
             "como frontera nombrada. El paso 4 del superviviente disena producto y proceso de "
             "forma integrada y el 5 verifica antes de PRODUCIR A ESCALA COMPLETA: la escala "
             "es una frontera y la transferencia a operaciones es otra, y el verbo OPTIMIZAR "
             "no aparece en ninguno de los seis pasos"),
     "donde": "paso 4 de design_for_six_sigma_dmadv",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LAS CARACTERISTICAS INNOVADORAS como salida nombrada del analisis, y su "
             "combinacion como el gesto que crea la solucion. El paso 3 del superviviente "
             "evalua VARIOS CONCEPTOS DE DISENO, que es comparar alternativas, y el 4 los "
             "incorpora como criterios: en ninguno se nombra la caracteristica innovadora como "
             "el objeto que se busca"),
     "donde": "paso 3 de design_for_six_sigma_dmadv_2",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA ORGANIZACION COMO SEGUNDO SUJETO DE LA VERIFICACION: el absorbido verifica que "
             "la innovacion cumple con las necesidades DEL CLIENTE Y DE LA ORGANIZACION, y el "
             "paso 5 del superviviente verifica contra los CTQ y los niveles Six Sigma, o sea "
             "solo contra el lado del cliente traducido a metrica"),
     "donde": "paso 5 de design_for_six_sigma_dmadv_2",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de LA COMPLEJIDAD DEL PRODUCTO que exige un enfoque estadistico "
             "riguroso. Las cuatro condiciones del superviviente disparan por NOVEDAD (producto "
             "nuevo, rediseno total, proceso que no existe) y por MULTIPLICIDAD de requisitos "
             "criticos: ninguna dispara por la complejidad del objeto en si"),
     "donde": "condicion 1 de design_for_six_sigma_dmadv",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de QUERER INNOVAR DE MANERA SISTEMATICA EN LUGAR DE AZAROSA, que "
             "es el unico de todo el acto que nombra el METODO frente al azar y no el objeto "
             "que se disena. Ninguna de las cuatro condiciones del superviviente lo dice"),
     "donde": "condicion 1 de design_for_six_sigma_dmadv_2",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO41 = {
    "design_for_six_sigma_dmadv": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # definir el proyecto y su alcance
            "2": ("CUBIERTO", 2),   # medir los CTQ
            "3": ("CUBIERTO", 3),   # con perdida: el diseno de alto nivel
            "4": ("CUBIERTO", 4),   # con perdida: optimizar antes de transferir a operaciones
            "5": ("CUBIERTO", 5),   # verificar el diseno final
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: la complejidad del producto
            "2": ("CUBIERTO", 1),   # niveles extraordinarios de calidad: lo dice la calidad Six Sigma
        },
    },
    "design_for_six_sigma_dmadv_2": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # define: metas y objetivos
            "2": ("CUBIERTO", 2),   # con perdida de dos sedes: las necesidades ocultas
            "3": ("CUBIERTO", 3),   # con perdida: las caracteristicas innovadoras
            "4": ("CUBIERTO", 4),   # design: combinar las caracteristicas
            "5": ("CUBIERTO", 5),   # con perdida: la organizacion como segundo sujeto
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: innovar sistematicamente frente al azar
            "2": ("CUBIERTO", 3),   # disenar desde cero: es la condicion 3 del superviviente
            "3": ("CUBIERTO", 4),   # segunda sede de la perdida de las necesidades ocultas
        },
    },
}


# ======================================================================
# ACTO 42: LA FAMILIA DEL EQUIPO MULTIFUNCIONAL DE COOPER.
# TRES miembros del mismo libro, DOS pares internos con veredicto y los
# DOS en A, CERO D, CERO puentes, CERO triangulos y CERO puertas.
# FORMA medida: UNA SOLA VARA, y es la de CONDICIONES: la de pasos
# EMPATA en 5 entre los otros dos y no apunta.
# ======================================================================

SUP42 = "equipo_multifuncional_real"

MOTIVO42 = (
    "ACTO 42 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DEL EQUIPO MULTIFUNCIONAL DE COOPER. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE: los TRES "
    "miembros son del MISMO LIBRO (Winning at New Products, de Robert G. Cooper) y las dos "
    "razones lo dicen (el 672 cierra con LOS DOS DE WINNING AT NEW PRODUCTS, COOPER), tienen "
    "DOS pares internos con veredicto escrito de TRES combinaciones posibles y los DOS son de "
    "clase A (puestos 476 y 672), hay CERO pares D internos, CERO nodos puente y CERO "
    "triangulos, medido. El 672 los llama GEMELOS DEL MISMO LIBRO SOBRE EL MISMO PROBLEMA, SIN "
    "ARISTA ENTRE ELLOS. El par que falta es el unico sin veredicto del acto. "
    "LO QUE LAS DOS RAZONES DICEN QUE ES LO MISMO, y el 672 lo resume en una linea: EL EJE ES "
    "EL MISMO, EL LIDER DE VERDAD Y EL EQUIPO DE VERDAD. Los tres mandan nombrar un lider con "
    "autoridad real y no solo con la responsabilidad, y mantener un nucleo estable de "
    "principio a fin. "
    "P.8 EN ORDEN, Y AQUI LA VARA QUE HABLA NO ES LA DE PASOS: la FORMA medida es UNA SOLA "
    "VARA. La de PASOS EMPATA en 5 entre diseno_organizacional_equipos_innovacion y "
    "equipo_multifuncional y NO APUNTA A NADIE; la de CONDICIONES apunta a "
    "equipo_multifuncional_real (3 contra 2 y 2). UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA "
    "(acta 53, pregunta 4), Y LA VARA DE CONDICIONES ES VARA DE CONTENIDO igual que la de "
    "pasos: la campana ya decidio por ella sola en el acto 29 del lote E, con pasos y cableado "
    "empatados. "
    "Y VA DICHO LO INCOMODO EN VEZ DE MEDIO: EL SUPERVIVIENTE ES EL MIEMBRO MAS PEQUENO DEL "
    "ACTO POR PASOS (4 contra 5 y 5) Y POR CABLEADO (2 contra 5 y 4, leido de la columna cab "
    "del instrumento de varas). Gana por la unica vara de contenido que no empata, y el "
    "cableado no habla porque el contenido no empata. VA MARCADO DISCUTIBLE en el reporte. "
    "LO QUE LO SOSTIENE ADEMAS DE LA CUENTA, Y ES CONTENIDO DECLARADO POR EL ARCHIVO: el 672 "
    "dice con todas sus letras que LO QUE SE PERDERIA SI SE FUSIONA MAL SON LAS DOS CONDICIONES "
    "MATERIALES DEL SEGUNDO, LIBERAR TIEMPO Y RECOMPENSAR POR EQUIPO, QUE SON LAS UNICAS QUE "
    "CONVIERTEN EL AVISO EN ALGO EJECUTABLE. Ese SEGUNDO es equipo_multifuncional_real, y esas "
    "dos piezas son sus pasos 2 y 3. Elegir superviviente a cualquiera de los otros dos "
    "obligaria a repescar por APPEND exactamente las dos piezas que la razon llama las unicas "
    "ejecutables. EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN, y eso vale tambien para la "
    "palabra REAL del rotulo del superviviente, que es rotulo y no contenido. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta, medido contra el universo protegido de "
    "256 ids. La guarda pasa POR VACIO y se dice. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; NINGUNA entrada de docs/plan/INVENTARIO.jsonl que no sea de tipo acto nombra a "
    "ninguno de los tres; ninguno esta en ninguna nomina de docs/RACIMOS_MIEMBROS.jsonl; y el "
    "barrido sobre docs/plan/OPERACIONES.jsonl no devuelve ninguna mencion. El dueno es EL "
    "MEDIDO y aqui no hay ninguno."
)

NOTA42 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado. TRES APPEND DE PASO Y UN INCISO, CERO "
    "APPEND DE CONDICION, y el nodo crece de 4 pasos a 7 y de 3 condiciones a 3. "
    "EL INCISO AL PASO 1 ES EL PARAMETRO QUE LA RAZON PONE SOBRE EL LIDER: el ESPIRITU "
    "EMPRENDEDOR. El superviviente da al lider AUTORIDAD REAL, que es la potestad; el absorbido "
    "dice de que clase de persona se trata, y el 476 lo nombra al abrir su razon. El paso 1 del "
    "superviviente NO termina en punto, asi que la guarda de la JUNTURA ROTA no salta. "
    "LOS TRES APPEND DE PASO SON TRES GESTOS DISTINTOS, y los tres los nombran las razones "
    "como propios de su absorbido: LA FORMA DE ORGANIZACION SEGUN LA COMPLEJIDAD (compartir "
    "tiempo, dar prioridad o dedicar por completo), que el 476 nombra como lo que ANADE el "
    "primero; LA COLOCACION FISICA DEL EQUIPO o su sustituto a distancia, que el 476 nombra en "
    "la misma frase; y EVITAR EL MODELO DE PASAR EL PROYECTO DE AREA EN AREA, que el 672 "
    "nombra explicitamente entre lo que SE PERDERIA SI SE FUSIONA MAL. Ninguno de los cuatro "
    "pasos del superviviente dice ninguna de las tres cosas. "
    "DOS PIEZAS VAN A UNA CONDICION DEL SUPERVIVIENTE Y NO A UN PASO, Y ESO SE DICE PORQUE ES "
    "UNA LECTURA Y NO UN ATAJO: el paso 1 de diseno_organizacional_equipos_innovacion (armar un "
    "equipo con personas de distintas areas cuando el proyecto pasa el gate) y el paso 1 de "
    "equipo_multifuncional (incluir desde el inicio a alguien de cada area clave) describen LA "
    "COMPOSICION MULTIAREA DEL EQUIPO, y el superviviente la nombra en su condicion 1 (si tu "
    "negocio ya tiene varias personas o areas trabajando juntas en un proyecto) y NUNCA como "
    "paso. El superviviente da la composicion por supuesta y empieza por el lider. Las dos van "
    "marcadas contra esa condicion y las dos sellan su perdida. "
    "SIETE PERDIDAS SELLADAS, DOS DE ELLAS CON DOS SEDES por el criterio que el acta 67 "
    "adjudico en su D10 (LA FILA ES POR PIEZA QUE SE PIERDE, NO POR SITIO DONDE VIVIA): LA "
    "RENDICION DE CUENTAS COMPARTIDA vive en el paso 4 de equipo_multifuncional y en el paso 5 "
    "de diseno_organizacional_equipos_innovacion, y EL SILO INFORMATIVO vive en la condicion 1 "
    "de los DOS absorbidos. Cada una va en UNA fila con sus dos sedes nombradas."
)

PERDIDAS42 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL DISPARADOR DEL GATE: armar el equipo JUSTO CUANDO un proyecto importante pasa "
             "el filtro de aprobacion. La condicion 1 del superviviente presupone el equipo ya "
             "formado (si tu negocio YA TIENE varias personas o areas trabajando juntas) y "
             "ninguno de sus cuatro pasos manda formarlo: se pierde el momento exacto en que "
             "el equipo nace, que en Cooper es el unico momento en que se puede pedir "
             "dedicacion"),
     "donde": "paso 1 de diseno_organizacional_equipos_innovacion",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA COMPOSICION MULTIAREA DESDE EL INICIO Y NO AL FINAL, con el matiz que el "
             "absorbido subraya, ALGUIEN DE CADA AREA CLAVE. La condicion 1 del superviviente "
             "nombra la composicion multiarea como SITUACION DE PARTIDA y no como gesto, y por "
             "eso no dice ni cuando entra cada area ni que ninguna se quede fuera"),
     "donde": "paso 1 de equipo_multifuncional",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA RENDICION DE CUENTAS COMPARTIDA: que quede claro QUIEN RESPONDE POR QUE, y "
             "que la responsabilidad sea compartida entre todo el equipo. El paso 3 del "
             "superviviente define indicadores y recompensas POR DESEMPENO DEL EQUIPO, que es "
             "el premio colectivo, no el reparto nominal de responsabilidades. UNA SOLA PIEZA "
             "CON DOS SEDES, sellada una vez con las dos nombradas (acta 67, D10)"),
     "donde": ("paso 4 de equipo_multifuncional y paso 5 de "
               "diseno_organizacional_equipos_innovacion"),
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL HORIZONTE DEL NUCLEO ESTABLE: el absorbido lo extiende HASTA DESPUES DE "
             "LANZARLO y el paso 4 del superviviente lo cierra HASTA EL FINAL DEL PROYECTO. La "
             "diferencia es exactamente el tramo en que un producto nuevo se cae o se sostiene, "
             "y es la unica linea del acto que lo nombra"),
     "donde": "paso 5 de diseno_organizacional_equipos_innovacion",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA VISION COMPARTIDA COMO CONSTRUCCION EXPLICITA, o sea construirla entre todos "
             "los que participan y no darla por supuesta. Ninguno de los cuatro pasos del "
             "superviviente la nombra: el 4 mantiene un nucleo COMPROMETIDO, que es el "
             "resultado, y no el trabajo de fabricar el acuerdo"),
     "donde": "paso 3 de equipo_multifuncional",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador del SILO INFORMATIVO: que cada area trabaje por su cuenta sin "
             "cruzar informacion, y que el proyecto avance de forma SECUENCIAL entre areas que "
             "no se hablan. La condicion 3 del superviviente dispara porque LOS PROYECTOS "
             "AVANZAN LENTO POR FALTA DE COMPROMISO, que es el sintoma visible; el silo es la "
             "causa y no aparece nombrada. UNA SOLA PIEZA CON DOS SEDES, sellada una vez con "
             "las dos nombradas (acta 67, D10)"),
     "donde": ("condicion 1 de diseno_organizacional_equipos_innovacion y condicion 1 de "
               "equipo_multifuncional"),
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de que FALTE VISION COMPARTIDA en el equipo que desarrolla el "
             "producto. La condicion 3 del superviviente dispara por falta de COMPROMISO REAL "
             "ENTRE AREAS, que es la voluntad; la vision compartida es el acuerdo sobre el "
             "objeto, y una cosa puede faltar con la otra presente"),
     "donde": "condicion 2 de equipo_multifuncional",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO42 = {
    "diseno_organizacional_equipos_innovacion": {
        "pasos": {
            "1": ("CUBIERTO_COND", 1),   # con perdida: el disparador del gate
            # EL UNICO INCISO DEL ACTO: el espiritu emprendedor del lider.
            "2": ("INCISO", 1, "con espiritu emprendedor", ", y elígelo "),
            "3": ("APPEND",),            # LA FORMA DE ORGANIZACION SEGUN LA COMPLEJIDAD
            "4": ("APPEND",),            # LA COLOCACION FISICA Y SU SUSTITUTO A DISTANCIA
            "5": ("CUBIERTO", 4),        # con dos perdidas: el horizonte y la rendicion de cuentas
        },
        "condiciones": {
            "1": ("CUBIERTO", 3),        # con perdida de dos sedes: el silo informativo
            "2": ("CUBIERTO", 2),        # representantes sin autoridad ni dedicacion real
        },
    },
    "equipo_multifuncional": {
        "pasos": {
            "1": ("CUBIERTO_COND", 1),   # con perdida: desde el inicio y no al final
            "2": ("CUBIERTO", 1),        # el lider de verdad, no el coordinador de tareas
            "3": ("CUBIERTO", 4),        # con perdida: la vision compartida
            "4": ("CUBIERTO", 3),        # segunda sede de la perdida de la rendicion de cuentas
            "5": ("APPEND",),            # EVITAR PASAR EL PROYECTO DE AREA EN AREA
        },
        "condiciones": {
            "1": ("CUBIERTO", 3),        # segunda sede de la perdida del silo informativo
            "2": ("CUBIERTO", 3),        # con perdida: la vision compartida como disparador
        },
    },
}


# ======================================================================
# EL LOTE, ARMADO.
# ======================================================================

LOTE_G = {
    "titulo": ("LOTE G DEL TRAMO UNICO DE OP-U-02. ABRE EN EL "
              "ACTO 38, que es el PRIMERO DEL TRAMO SIN DUENO MEDIDO. LOS DOS SALTOS VAN "
              "DECLARADOS Y NO ROMPEN EL PREFIJO SIN SALTOS, porque ninguno de los dos actos "
              "saltados esta en la cola de fusiones de esta operacion: el ACTO 31 tiene dueno "
              "medido (OP-F-04-WEI y OP-S-04 en duenos_cualquier_operacion, leido hoy del "
              "fichero fijado del tramo) y el ACTO 37 tiene dueno medido (OP-S-07, leido hoy "
              "del mismo fichero), y la adjudicacion 2 del acta 69 dice con todas sus letras "
              "que lo que vale para el 31 vale para el 37 cuando el prefijo lo alcance. CINCO "
              "ACTOS CIERRAN ENTEROS Y SON 15 NODOS: los actos 38, 39, 40, 41 y 42 cierran los "
              "CINCO FUNDIDOS y NINGUNO cierra DECLARADO Y NO FUNDIDO. LOS MOTIVOS DE DECLARADO "
              "POSIBLES SON DOS Y SOLO DOS (adjudicacion 4 del acta 70) Y NINGUNO TIENE SUJETO "
              "AQUI: la guarda 1B pasa POR VACIO en los cinco actos (CERO puertas dentro de "
              "cada uno, medido contra el universo protegido de 256 ids) y P.5 contesta UNA "
              "FAMILIA en los cinco. P.10 y el cuarto motivo siguen sin sujeto: cero puentes, "
              "cero triangulos y cero pares D internos en los cinco, medido. EL TOPE DEL "
              "PREFIJO NO ES ESTRUCTURAL SINO DE LOTE, Y SE DICE EN VEZ DE DEJARLO COMO UN "
              "NUMERO ELEGIDO: el siguiente es el ACTO 43, que NO tiene dueno y NO trae puerta, "
              "y el tope cae antes de el porque el encargo fija CINCO actos. EL ACTO 44, que "
              "trae DOS puertas y cerrara DECLARADO por la guarda 1B cuando el prefijo lo "
              "alcance (adjudicacion 4 del acta 70), queda FUERA de este lote y no se toca"),
    "actos": [
        {
            "orden": 38,
            "superviviente": SUP38,
            "motivo": MOTIVO38,
            "nota": NOTA38,
            "reparto": REPARTO38,
            "perdidas": PERDIDAS38,
        },
        {
            "orden": 39,
            "superviviente": SUP39,
            "motivo": MOTIVO39,
            "nota": NOTA39,
            "reparto": REPARTO39,
            "perdidas": PERDIDAS39,
        },
        {
            "orden": 40,
            "superviviente": SUP40,
            "motivo": MOTIVO40,
            "nota": NOTA40,
            "reparto": REPARTO40,
            "perdidas": PERDIDAS40,
        },
        {
            "orden": 41,
            "superviviente": SUP41,
            "motivo": MOTIVO41,
            "nota": NOTA41,
            "reparto": REPARTO41,
            "perdidas": PERDIDAS41,
        },
        {
            "orden": 42,
            "superviviente": SUP42,
            "motivo": MOTIVO42,
            "nota": NOTA42,
            "reparto": REPARTO42,
            "perdidas": PERDIDAS42,
        },
    ],
    "declarados": [],
}
