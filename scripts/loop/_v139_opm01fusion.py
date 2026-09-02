# -*- coding: utf-8 -*-
"""_v139_opm01fusion.py . EL CONTENIDO EDITORIAL DE LA FUSION DE MESA
OP-M-01-FUSION, LA CAMARILLA DE CINCO.

NO ES UN INSTRUMENTO: no mide, no escribe y no decide nada por si mismo. Es EL
TEXTO del reparto pieza a pieza, con su motivo citado y LAS PERDIDAS SELLADAS EN
CAMPO PROPIO. Lo importa scripts/loop/generar_plan_de_fusion_de_mesa.py, que es
quien pone LA ARITMETICA Y LAS GUARDAS y quien sella el plan.

EL SUPERVIVIENTE NO SE ELIGE AQUI: LO ELIGIO LA FICHA. La adjudicacion de
OP-M-01-FUSION esta sellada en docs/plan/OPERACIONES.jsonl desde el 12 ago 2026 y
el generador cae en ROJO si este fichero nombra otro.

ES EL ESTRENO DE LA QUINTA MARCA, VIAJA_EN_EL_ACTO (vuelta 139, operacion 2.a;
acta de la vuelta 138, adjudicacion 3.1). La linea 4 de `preservar` de esta ficha
es exactamente el caso que la marca existe para decir: LOS ENTREGABLES CLAROS Y
ESTANDARIZADOS los tienen TRES de los cuatro absorbidos y el superviviente NO.

Y ES LA PRIMERA FUSION DE CUATRO ABSORBIDOS DE LA CAMPANA: estrena tambien el
camino del reparto POR PAR (vuelta 138, operacion 2.a), que hasta hoy solo habia
corrido con un absorbido.
"""

FUSION = {
    "titulo": (
        "LA CAMARILLA DE CINCO, DE COOPER: sistema_gates_go_kill absorbe a los CUATRO, "
        "gates_go_kill_decision_points, requisitos_gates_con_dientes, estructura_gates y "
        "estructura_de_gates. Es la SEGUNDA fusion de la fase 06 y la PRIMERA de la "
        "campana con CUATRO absorbidos. ES LA UNICA FUSION DEL PLAN CON SU ACTO LEIDO "
        "ENTERO: diez pares posibles, DIEZ leidos, LOS DIEZ EN A, y por eso su ficha dice "
        "P.5 SATISFECHA POR CONSTRUCCION y no como condicion"
    ),
    "superviviente": "sistema_gates_go_kill",
    "absorbidos": [
        "gates_go_kill_decision_points",
        "requisitos_gates_con_dientes",
        "estructura_gates",
        "estructura_de_gates",
    ],
    "motivo": (
        "EL SUPERVIVIENTE LO FIJA LA FICHA SELLADA Y AQUI NO SE RE-ADJUDICA: "
        "docs/plan/OPERACIONES.jsonl escribe superviviente sistema_gates_go_kill el 12 ago "
        "2026, POR CONTENIDO Y POR P.8 EN ORDEN, y el generador cae en ROJO si este "
        "fichero nombrara otro. "
        "LO QUE LA FICHA MIDIO Y POR QUE: el veredicto 801 dice que EL EJE SE REPITE "
        "ENTERO (definir cada puerta como momento real de seguir o cancelar, pedir "
        "entregables, establecer criterios visibles y documentados, y comprometer recursos "
        "solo despues de pasar), y que sobre ese eje LO PROPIO DE sistema_gates_go_kill "
        "SON TRES (el scorecard simple, comprometer recursos solo despues del gate, y "
        "anotar la decision y el motivo) contra DOS de requisitos_gates_con_dientes. Los "
        "otros tres son de cuatro pasos y ninguno contiene a nadie. "
        "LA REGLA DE LA FICHA ENVEJECIDA (P.9 y P.13, y la correccion declarada que el "
        "acta 138 adjudico en su 3.4) SE APLICA Y SE DECLARA, con las dos cifras y sus "
        "dos cortes, SIN promediar y SIN elegir una: "
        "  (a) CABLEADO. La ficha escribe, el 12 ago 2026, MEDIDO: cableado 9 contra 7, "
        "5, 5 y 4. La simulacion del 2 sep 2026, corrida antes de fundir y sellada en "
        "docs/loop/SALIDA_V139_3_SIM_OPM01FUSION.txt, mide 10 contra 7, 5, 4 y 5. "
        "NO VOLTEA NADA: el superviviente gana por los dos conteos y por el margen mas "
        "ancho de las seis mesas. "
        "  (b) DUPLICADAS. La ficha escribe, en su verificacion, SIMULADA (P.7): CUATRO "
        "duplicadas nuevas, y las nombra: gates_sin_dientes_problema.nodos_previos, "
        "gestion_portafolio_formal.nodos_previos, mitos_stage_gate.nodos_siguientes y "
        "scorecards_criterios_gate.nodos_previos. La simulacion del 2 sep 2026 mide "
        "CINCO, esas cuatro Y ADEMAS tipos_criterios_gate.nodos_previos. "
        "LAS CINCO SIGUEN ENRUTADAS A OP-S-12 por la propia ficha, que es lo que gobierna: "
        "la ficha se equivoco en la CANTIDAD, no en el DESTINO. Las dos divergencias van "
        "registradas POR ADICION en docs/plan/CORRECCIONES_A_APLICAR.md, sin tocar la "
        "ficha. "
        "CERO AUTO ARISTAS y CERO ARISTAS INTERNAS del acto que sobrevivan, las dos "
        "medidas hoy en la misma simulacion, igual que la ficha dice. "
        "LECTURA DE ACTO POR P.5, RE-CORRIDA HOY ANTES DE FUNDIR con "
        "scripts/loop/vuelta138_p5_lectura_de_acto.py --id-op OP-M-01-FUSION: 10 pares "
        "leidos, 10 pares del acto, EXIT 0. Salida en "
        "docs/loop/SALIDA_V139_3_P5_LECTURA_DE_ACTO.txt."
    ),
    # EL REPARTO VA POR PAR (absorbido, numero de paso), que es el unico formato
    # que el generador acepta con dos o mas absorbidos desde la vuelta 138.
    "pasos": {
        "gates_go_kill_decision_points": {
            # 1. Define con claridad cada punto de decision en tu camino de la
            #    idea al lanzamiento
            "1": ["CUBIERTO", 1],
            # 2. En cada uno de esos puntos, preguntate de verdad si sigues o si
            #    paras, no solo revises como va el proyecto
            "2": ["APPEND"],
            # 3. No dejes que un proyecto avance a la siguiente etapa sin que
            #    hayas decidido conscientemente seguir
            "3": ["APPEND"],
            # 4. Anota que decidiste: seguir, parar, dejarlo en espera,
            #    replantearlo, o seguir pero con condiciones
            "4": ["CUBIERTO", 6],
        },
        "requisitos_gates_con_dientes": {
            # 1. Define cada punto de decision (gate) como un momento real donde
            #    decides seguir o cancelar (Go/Kill).
            "1": ["CUBIERTO", 1],
            # 2. Pide entregables claros y estandarizados que debes presentar en
            #    cada punto de decision.   <-- LA PIEZA DE TRES DUENOS
            "2": ["VIAJA_EN_EL_ACTO", "estructura_de_gates", 1],
            # 3. Establece criterios de avance visibles y documentados, una tabla
            #    de criterios, para todos los que participan en la decision.
            "3": ["CUBIERTO", 2],
            # 4. Acuerda con tu equipo los criterios de exito de cada etapa antes
            #    de llegar al punto de decision.   <-- preservar [1]
            "4": ["APPEND"],
            # 5. Conecta cada punto de decision con la forma en que asignas
            #    recursos y con la vision general de tus proyectos.
            #    <-- preservar [3], EL PUENTE AL PORTAFOLIO
            "5": ["APPEND"],
            # 6. Haz una revision despues del lanzamiento para confirmar que se
            #    cumplio lo prometido.   <-- preservar [2]
            "6": ["APPEND"],
        },
        "estructura_gates": {
            # 1. Define una lista clara de lo que debes entregar en cada punto de
            #    decision de tu proceso   <-- LA PIEZA DE TRES DUENOS
            "1": ["VIAJA_EN_EL_ACTO", "estructura_de_gates", 1],
            # 2. Crea una lista de criterios eliminatorios para descartar de
            #    entrada los proyectos que no son viables   <-- preservar [9]
            "2": ["APPEND"],
            # 3. Decide como vas a priorizar los proyectos que si cumplen,
            #    dandole mas peso a lo que mas te importa   <-- preservar [9]
            "3": ["APPEND"],
            # 4. Decide quien sera la persona con experiencia y con poder sobre
            #    los recursos necesarios, responsable de aprobar cada etapa
            #    <-- preservar [8], EL GATEKEEPER
            "4": ["APPEND"],
        },
        "estructura_de_gates": {
            # 1. Definir de antemano una lista estandar de entregables requeridos
            #    para cada gate (ej. plantillas de business case).
            #    <-- preservar [4]. ESTA ES LA REDACCION QUE VIAJA.
            "1": ["APPEND"],
            # 2. Establecer criterios de decision claros: must-meet, go/kill
            #    financieros, y should-meet cualitativos.   <-- preservar [6]
            "2": ["APPEND"],
            # 3. Definir explicitamente las posibles salidas de la reunion
            #    (Go/Kill/Hold/Recycle/Conditional Go).   <-- preservar [5], y la
            #    ficha dice que YA NO SON LAS CINCO, SOLO LA QUINTA, porque el
            #    superviviente ya trae cuatro. Por eso INCISO y no APPEND.
            "3": ["INCISO", 4, "Conditional Go", ", y una quinta salida, "],
            # 4. Comunicar estas expectativas al equipo de proyecto antes de que
            #    lleguen al gate.   <-- preservar [7]
            "4": ["APPEND"],
        },
    },
    "condiciones": {
        "gates_go_kill_decision_points": {
            # 1. Cuando tienes mas de un proyecto avanzando al mismo tiempo
            "1": ["CUBIERTO", 1],
            # 2. Cuando necesitas una forma clara de decidir si sigues
            #    invirtiendo en un proyecto o lo cierras
            "2": ["CUBIERTO", 3],
        },
        "requisitos_gates_con_dientes": {
            # 1. Cuando estas disenando o rediseñando tu propio sistema de etapas
            #    y decisiones (Stage-Gate).
            "1": ["APPEND"],
            # 2. Si tus puntos de decision actuales no producen decisiones reales
            #    de seguir o cancelar.
            "2": ["CUBIERTO", 3],
        },
        "estructura_gates": {
            # 1. Si tus proyectos avanzan sin puntos de control claros
            "1": ["APPEND"],
            # 2. Si necesitas una forma objetiva de priorizar entre varios
            #    proyectos
            "2": ["CUBIERTO", 1],
        },
        "estructura_de_gates": {
            # 1. Si las reuniones de revision de proyecto terminan con decisiones
            #    vagas o ambiguas.
            "1": ["CUBIERTO", 3],
            # 2. Si los lideres de proyecto no saben que se espera de ellos en
            #    cada etapa.
            "2": ["APPEND"],
        },
    },
    # GUARDA (v) DE LA QUINTA MARCA: cada VIAJA_EN_EL_ACTO lleva SU linea
    # editorial, copiada VERBATIM al plan, diciendo POR QUE los dos son el mismo
    # gesto y CUAL de las dos redacciones viaja. El generador cae en ROJO si
    # falta, y tambien si la linea no NOMBRA al absorbido destino.
    "lineas_de_viaje": {
        "requisitos_gates_con_dientes|2": (
            "MISMO GESTO: pedir entregables claros y estandarizados en cada punto de "
            "decision. El paso 2 de requisitos_gates_con_dientes (pide entregables claros y "
            "estandarizados que debes presentar en cada punto de decision) y el paso 1 de "
            "estructura_de_gates (definir de antemano una lista estandar de entregables "
            "requeridos para cada gate, ej. plantillas de business case) mandan lo mismo, y "
            "es la linea 4 de preservar de la ficha: LOS ENTREGABLES CLAROS Y "
            "ESTANDARIZADOS con sus plantillas, que el superviviente NO tiene y los tres "
            "que mueren si. VIAJA LA REDACCION DE estructura_de_gates, que es la que lleva "
            "el APPEND, Y EL MOTIVO NO ES EL ORDEN SINO EL TEXTO: es la UNICA de las tres "
            "que trae LAS PLANTILLAS, y la linea de preservar las exige con esas palabras "
            "(con sus plantillas). Si viajara esta, las plantillas se perderian y la ficha "
            "quedaria incumplida. Esta redaccion no anade ningun matiz que la de "
            "estructura_de_gates no traiga: estandarizados y lista estandar dicen lo mismo, "
            "y en cada punto de decision y para cada gate tambien."
        ),
        "estructura_gates|1": (
            "MISMO GESTO: definir la lista de lo que hay que entregar en cada punto de "
            "decision. El paso 1 de estructura_gates (define una lista clara de lo que "
            "debes entregar en cada punto de decision de tu proceso) y el paso 1 de "
            "estructura_de_gates son el mismo gesto, y los dos caen bajo la linea 4 de "
            "preservar. VIAJA LA REDACCION DE estructura_de_gates, que es la que lleva el "
            "APPEND, porque es la unica de las tres que nombra LAS PLANTILLAS que esa linea "
            "de preservar exige. Esta redaccion es la mas pobre de las tres (dice lista "
            "clara donde la otra dice lista estandar definida de antemano) y no trae ningun "
            "matiz propio: no es una pieza propia, es la misma pieza."
        ),
    },
    "nota": (
        "VEINTISEIS PIEZAS REPARTIDAS ENTRE CUATRO ABSORBIDOS, 18 de paso y 8 de "
        "condicion, y el reparto lo CUENTA EL GENERADOR de las marcas: esta nota no lo "
        "teclea. "
        "LA PIEZA DE TRES DUENOS ES EL ESTRENO DE LA QUINTA MARCA, y es literalmente el "
        "caso que la vuelta 138 no supo decir y que el acta 138 cerro citando P.13: los "
        "ENTREGABLES estan en el paso 2 de requisitos_gates_con_dientes, en el paso 1 de "
        "estructura_gates y en el paso 1 de estructura_de_gates, y el superviviente NO los "
        "tiene en ninguno de sus seis pasos. Marcar los tres APPEND habria injertado el "
        "mismo gesto TRES VECES, que es la repeticion que P.13 prohibe por su nombre; "
        "marcarlos CUBIERTO habria afirmado del superviviente algo que su texto no dice; y "
        "declararlos PERDIDA es la PERDIDA FALSA que la misma frase de P.13 prohibe. UNO "
        "viaja de APPEND y los otros DOS llevan VIAJA_EN_EL_ACTO apuntandolo, con su linea "
        "editorial cada uno. "
        "CUAL VIAJA, Y NO ES EL ORDEN: viaja estructura_de_gates, porque es la UNICA de las "
        "tres que trae LAS PLANTILLAS, y la linea 4 de preservar las exige literalmente "
        "(LOS ENTREGABLES CLAROS Y ESTANDARIZADOS con sus plantillas). Con cualquiera de "
        "las otras dos, la ficha quedaria incumplida. "
        "LA QUINTA SALIDA VA DE INCISO Y NO DE APPEND, y lo manda la propia ficha: su nota "
        "dice que la taxonomia de salidas DEJO DE SER LAS CINCO Y PASO A SER SOLO LA "
        "QUINTA, porque el superviviente ya trae cuatro (Go, Kill, Hold y Recycle en su "
        "paso 4). Appendear el paso 3 de estructura_de_gates entero volveria a listar las "
        "cuatro que ya estan. El INCISO extrae VERBATIM del nodo que muere el trozo "
        "Conditional Go y lo adosa al paso 4 del superviviente, que no cierra en punto. Con "
        "eso queda cumplida la verificacion 4 de la ficha: TRAS LA FUSION EL SUPERVIVIENTE "
        "TIENE CINCO SALIDAS Y UNA DE ELLAS ES CONDITIONAL GO. "
        "EL PUENTE AL PORTAFOLIO VIAJA ENTERO Y ES LA PIEZA MAS CARA, y la ficha lo dice "
        "con esas palabras: es la bisagra sobre la que las 26 lecturas dirigidas "
        "encontraron que se sostiene la jerarquia entre las dos mitades de la mesa. Va de "
        "APPEND, el paso 5 de requisitos_gates_con_dientes, y con eso queda cumplida la "
        "verificacion 5, que pide comprobarlo LITERAL en el texto final. "
        "LAS DOS ADVERTENCIAS DE gates_go_kill_decision_points VIAJAN LAS DOS, y la ficha "
        "ya declara su figura: POR P.11 SON LINEA PARA LA VARA Y PERDIDA PARA LA FUSION, o "
        "sea que no deciden la clase pero siempre viajan. Son sus pasos 2 y 3. "
        "LOS CINCO CUBIERTO DE PASO, uno por uno y sin silencios: el paso 1 de "
        "gates_go_kill_decision_points y el paso 1 de requisitos_gates_con_dientes dicen "
        "definir los puntos de decision, que es el paso 1 del superviviente; el paso 3 de "
        "requisitos_gates_con_dientes pide criterios visibles y documentados, que es el "
        "paso 2 del superviviente con sus tres preguntas; y el paso 4 de "
        "gates_go_kill_decision_points pide anotar que decidiste, que es el paso 6 del "
        "superviviente. Su enumeracion de salidas no se pierde: viaja por el INCISO de "
        "estructura_de_gates, que es donde vive la taxonomia. "
        "LAS CUATRO CONDICIONES QUE VAN DE APPEND SON DISPARADORES DISTINTOS y no matices "
        "(acta 55, pregunta 5): DISENAR O REDISENAR TU PROPIO SISTEMA DE ETAPAS es un "
        "proyecto, no un sintoma; PROYECTOS QUE AVANZAN SIN PUNTOS DE CONTROL CLAROS es la "
        "ausencia del sistema, distinta de tener demasiados proyectos o de decidir sin "
        "criterio; y QUE LOS LIDERES NO SEPAN QUE SE ESPERA DE ELLOS es un fallo de "
        "expectativas, no de decision. Las otras cuatro van CUBIERTO contra las tres "
        "condiciones del superviviente. "
        "EL SUPERVIVIENTE CRECE Y SE DICE EN VEZ DE CALLARLO: de 6 pasos a 17 y de 3 "
        "condiciones a 6. Ninguna regla lo prohibe (preservar es SUELO y no techo, acta "
        "138 adjudicacion 3.3) y las diez lineas de preservar quedan cubiertas, pero es "
        "CANDIDATO LEGITIMO A LA PODA DE LA FASE 04 y va marcado como DISCUTIBLE en el "
        "reporte de esta vuelta. "
        "CERO PERDIDAS SELLADAS, Y LA LISTA VACIA ES UNA DECLARACION Y NO UN OLVIDO "
        "(contrato CAMPO PROPIO v1): la verificacion 3 de la ficha dice que LAS DIEZ QUE "
        "QUEDAN VIAJAN TODAS, y las diez viajan, ocho de APPEND, una de INCISO y una por "
        "VIAJA_EN_EL_ACTO con su redaccion elegida por texto."
    ),
    "perdidas": [],
    "simulacion_de_hoy": (
        "scripts/plan/simular_fusion.py, corrida el 2 sep 2026 ANTES de fundir, salida "
        "sellada en docs/loop/SALIDA_V139_3_SIM_OPM01FUSION.txt: CINCO duplicadas nuevas "
        "(gates_sin_dientes_problema.nodos_previos, gestion_portafolio_formal.nodos_previos, "
        "mitos_stage_gate.nodos_siguientes, scorecards_criterios_gate.nodos_previos y "
        "tipos_criterios_gate.nodos_previos), CERO auto aristas, CERO aristas internas del "
        "acto que sobrevivan, y cableado 10 contra 7, 5, 4 y 5. La ficha del 12 ago 2026 "
        "decia CUATRO duplicadas y 9 de cableado: las dos divergencias van declaradas en "
        "docs/plan/CORRECCIONES_A_APLICAR.md, no resueltas copiando."
    ),
}
