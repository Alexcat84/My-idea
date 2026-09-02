# -*- coding: utf-8 -*-
"""_v144_opm04_328.py . EL CONTENIDO EDITORIAL DE LA FUSION 328 DE LA MESA
OP-M-04, LA JUNTA ASESORA.

NO ES UN INSTRUMENTO: no mide, no escribe y no decide nada por si mismo. Es EL
TEXTO del reparto pieza a pieza, con su motivo citado y LAS PERDIDAS SELLADAS EN
CAMPO PROPIO. Lo importa scripts/loop/vuelta144_3b_sellar_mesa_opm04.py.

EL SUPERVIVIENTE NO SE ELIGE AQUI: LO ELIGIO LA FICHA, adjudicada el 11 ago 2026
(docs/plan/EXPEDIENTE_MESA_JUNTA_ASESORA.md, punto c, DESEMPATE POR CABLEADO) y
sellada en docs/plan/OPERACIONES.jsonl.

ES LA SEGUNDA MITAD DE UNA MESA DE DOS FUSIONES: la otra es
scripts/loop/_v144_opm04_367.py. Las dos van en el MISMO plan, con dos actos.
"""

FUSION = {
    "titulo": (
        "FUSION 328 DE LA MESA DE LA JUNTA ASESORA: formalizar_junta_asesora absorbe "
        "formalize_advisory_board. EL MISMO NOMBRE EN DOS IDIOMAS, con el contenido "
        "EMPATADO y el desempate dado por EL CABLEADO: formalizar_junta_asesora es el "
        "unico nodo del acto conectado con el otro lado. LA OPCION DE INVERTIR EN "
        "ACCIONES PREFERENTES VIAJA COMO INCISO, la primera pieza del reparto"
    ),
    "superviviente": "formalizar_junta_asesora",
    "absorbidos": ["formalize_advisory_board"],
    "motivo": (
        "EL SUPERVIVIENTE LO FIJA LA FICHA SELLADA Y AQUI NO SE RE-ADJUDICA: "
        "docs/plan/OPERACIONES.jsonl escribe superviviente formalizar_junta_asesora "
        "(fusion 328) el 11 ago 2026, POR DESEMPATE POR CABLEADO, y el expediente lo "
        "razona: el contenido esta empatado, y lo dice el propio veredicto 328 (los ids "
        "son el mismo nombre en dos idiomas y los pasos coinciden), asi que el desempate "
        "lo da el grafo. LA SIMULACION DEL 2 SEP 2026 lo confirma y por mas margen que el "
        "expediente: 7 contra 3 (docs/loop/SALIDA_V144_3B_SIMULACION.txt). "
        "LA ENTRADA POR customer_discovery, QUE EL AUDITOR PIDIO NOMBRAR: "
        "customer_discovery.nodos_siguientes trae HOY las dos, formalizar_junta_asesora y "
        "formalize_advisory_board; tras la fusion las dos resuelven al superviviente, asi "
        "que LA ENTRADA NO SE PIERDE y queda DUPLICADA, que es lo que limpia OP-S-12, que "
        "corre despues por la atadura 2 del indice."
    ),
    "pasos": {
        "formalize_advisory_board": {
            # 1. Haz un mapa de que asesores necesitas por area: tecnico,
            #    negocio, cliente, industria, marketing
            "1": ["APPEND"],
            # 2. Recluta solo a quienes puedan tener impacto estrategico real,
            #    priorizando calidad sobre cantidad
            "2": ["APPEND"],
            # 3. Suma como asesores a clientes potenciales clave para tener su
            #    mirada de compra
            "3": ["CUBIERTO", 1],
            # 4. Define como vas a compensarlos: acciones comunes con periodo de
            #    consolidacion (vesting), o la posibilidad de invertir en
            #    acciones preferentes
            "4": ["INCISO", 4, "o la posibilidad de invertir en acciones preferentes", ", "],
            # 5. Acuerda con cada asesor con que frecuencia y de que forma se van
            #    a reunir
            "5": ["CUBIERTO", 5],
        },
    },
    "condiciones": {
        "formalize_advisory_board": {
            # 1. Cuando ya validaste tus primeras hipotesis y necesitas ampliar
            #    tu red de contactos y tu vision estrategica
            "1": ["CUBIERTO", 2],
        },
    },
    "nota": (
        "SEIS PIEZAS REPARTIDAS: DOS VIAJAN ENTERAS, UNA VIAJA COMO INCISO, y TRES ya "
        "estaban dichas. El reparto se comprueba contra el texto de hoy, no contra la "
        "tabla del expediente, y donde discrepa SE DECLARA. "
        "LAS DOS QUE VIAJAN ENTERAS son las que la ficha manda preservar y son propias del "
        "que muere: EL MAPA DE ASESORES POR AREA (tecnico, negocio, cliente, industria, "
        "marketing), que el superviviente no hace en ningun grado (recluta expertos de "
        "industria y busca un asesor tipo CEO, que son dos areas sueltas, no el mapa); y "
        "PRIORIZAR CALIDAD SOBRE CANTIDAD, reclutar solo a quien tenga impacto estrategico "
        "real, que es una vara de seleccion que el superviviente no escribe. "
        "LA QUE VIAJA COMO INCISO es la tercera de las que la ficha manda preservar: LA "
        "OPCION DE INVERTIR EN ACCIONES PREFERENTES. El paso 4 del superviviente define el "
        "esquema de compensacion con stock comun y vesting mensual, o sea que ya trae el "
        "gesto y le falta LA OTRA VIA. Por eso no es APPEND (fabricaria un paso que repite "
        "la compensacion) ni CUBIERTO (afirmaria del superviviente algo que su texto no "
        "dice): es el INCISO, que adosa el trozo al paso que ya existe. "
        "LA QUE VIVE DENTRO, y la ficha ya la reclasifico en su propio recomputo P.13: "
        "SUMAR CLIENTES POTENCIALES CLAVE POR SU MIRADA DE COMPRA es literalmente el paso "
        "1 del superviviente, identificar clientes potenciales clave descubiertos en "
        "customer discovery para invitarlos a la junta asesora. Va de CUBIERTO y no se "
        "injerta, que es lo que P.13 manda con las piezas que viven dentro. "
        "DIVERGENCIA DECLARADA CON LA PASADA P.13 DE LA FICHA, Y NO SE RESUELVE COPIANDO: "
        "la ficha recomputo cuatro piezas y dijo tres viajan y una vive dentro. Leido el "
        "nodo entero HOY, paso por paso, EL PASO 5 DEL QUE MUERE TIENE UN PARAMETRO QUE EL "
        "SUPERVIVIENTE NO DICE: acordar CON QUE FRECUENCIA se van a reunir. El paso 5 del "
        "superviviente decide SI habra reuniones formales o consultas individuales, que es "
        "la forma, no el ritmo. Va de CUBIERTO por el gesto y la frecuencia va SELLADA EN "
        "CAMPO PROPIO como perdida de parametro: la lista `preservar` de la ficha es el "
        "SUELO de lo que no se puede perder, no el TECHO. Lo mismo con la CONDICION 1, "
        "cuyo disparador temporal (YA VALIDASTE TUS PRIMERAS HIPOTESIS) no esta en ninguna "
        "de las tres condiciones del superviviente. LAS DOS DIVERGENCIAS VAN MARCADAS COMO "
        "DISCUTIBLE EN EL REPORTE DE ESTA VUELTA."
    ),
    "perdidas": [
        {
            "especie": "DE PARAMETRO DE PASO",
            "que": ("la FRECUENCIA acordada con cada asesor, con que frecuencia se van a "
                    "reunir; el paso 5 del superviviente decide si habra reuniones formales "
                    "o consultas individuales, que es la FORMA del encuentro y no su RITMO, "
                    "y el paso 6 documenta la operacion de la junta sin fijar cada cuanto "
                    "se reune"),
            "donde": "paso 5 de formalize_advisory_board",
            "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente",
        },
        {
            "especie": "DE CONDICIONES",
            "que": ("el disparador TEMPORAL, cuando YA VALIDASTE TUS PRIMERAS HIPOTESIS; las "
                    "tres condiciones del superviviente disparan por NECESIDAD (credibilidad "
                    "ante inversores, introducciones de alto nivel, falta de experiencia "
                    "operativa) y ninguna dice EN QUE MOMENTO DEL PROYECTO toca"),
            "donde": "condicion 1 de formalize_advisory_board",
            "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)",
        },
    ],
    "simulacion_de_hoy": (
        "scripts/plan/simular_fusion.py corrido en la vuelta 144 ANTES de tocar un nodo "
        "(docs/loop/SALIDA_V144_3B_SIMULACION.txt), con las DOS fusiones de la mesa a la "
        "vez: TRES entradas se redirigen a este superviviente (customer_discovery, "
        "customer_validation_sell_phase y hire_data_analytics_chief), UNA duplicada NUEVA "
        "de su lado (customer_discovery.nodos_siguientes), CERO auto aristas, y el alias "
        "del superviviente queda con formalize_advisory_board. CALZA AL DIGITO CON LA "
        "FICHA: la verificacion 3 predice exactamente la duplicada de customer_discovery y "
        "la verificacion 4 el alias unico. LA UNICA DIVERGENCIA CON EL EXPEDIENTE ES A "
        "FAVOR DEL MISMO SUPERVIVIENTE: el cableado de hoy es 7 contra 3 y el expediente "
        "no publico cifra para este par, solo la razon."
    ),
}
