# -*- coding: utf-8 -*-
"""_v144_opm04_367.py . EL CONTENIDO EDITORIAL DE LA FUSION 367 DE LA MESA
OP-M-04, LA JUNTA ASESORA.

NO ES UN INSTRUMENTO: no mide, no escribe y no decide nada por si mismo. Es EL
TEXTO del reparto pieza a pieza, con su motivo citado y LAS PERDIDAS SELLADAS EN
CAMPO PROPIO. Lo importa scripts/loop/vuelta144_3b_sellar_mesa_opm04.py, que es
quien pone LA ARITMETICA Y LAS GUARDAS y quien sella el plan.

EL SUPERVIVIENTE NO SE ELIGE AQUI: LO ELIGIO LA FICHA, adjudicada el 11 ago 2026
(docs/plan/EXPEDIENTE_MESA_JUNTA_ASESORA.md, punto b) y sellada en
docs/plan/OPERACIONES.jsonl. El sellador cae en ROJO si este fichero nombra otro.

ES LA PRIMERA MITAD DE UNA MESA DE DOS FUSIONES: la otra es
scripts/loop/_v144_opm04_328.py. Las dos van en el MISMO plan, con dos actos.
"""

FUSION = {
    "titulo": (
        "FUSION 367 DE LA MESA DE LA JUNTA ASESORA: identificar_consejo_asesores absorbe "
        "identificar_junta_asesores. LOS DOS GEMELOS DE IDENTIFICAR, y sobrevive el de "
        "SEIS pasos porque su paso 6 es LA UNICA LINEA DE LOS CUATRO NODOS QUE ENTREGA "
        "EL TESTIGO: formalizar el consejo asesor mas adelante, durante la validacion de "
        "clientes"
    ),
    "superviviente": "identificar_consejo_asesores",
    "absorbidos": ["identificar_junta_asesores"],
    "motivo": (
        "EL SUPERVIVIENTE LO FIJA LA FICHA SELLADA Y AQUI NO SE RE-ADJUDICA: "
        "docs/plan/OPERACIONES.jsonl escribe superviviente identificar_consejo_asesores "
        "(fusion 367) el 11 ago 2026, POR CONTENIDO, y la adjudicacion del expediente lo "
        "razona en una linea: el paso 6 es la unica de los cuatro nodos que entrega el "
        "testigo. LA COBERTURA DEL ACTO ES COMPLETA Y ES LA UNICA DE LAS CINCO MESAS QUE "
        "LA TIENE: seis pares posibles, SEIS LEIDOS, cinco en el archivo de veredictos "
        "(367 A, 328 A, 712 A, 976 A, 1190 D CONGELADO) y el sexto por lectura dirigida "
        "(LD-01, D). EL DESEMPATE POR CABLEADO NO HACE FALTA AQUI Y AUN ASI CONCUERDA: la "
        "simulacion del 2 sep 2026 (docs/loop/SALIDA_V144_3B_SIMULACION.txt) mide 5 "
        "contra 4 a favor del superviviente. "
        "Y LA DISTINCION QUE EL EXPEDIENTE MANDA ESCRIBIR: el paso 3 del absorbido, "
        "evaluar su interes en convertirse en asesores formales, MUERE COMO SOLAPE Y NO "
        "COMO PERDIDA. No se pierde contenido: se deja de decir dos veces. Una perdida se "
        "registra y viaja; un solape se poda y no viaja a ninguna parte."
    ),
    "pasos": {
        "identificar_junta_asesores": {
            # 1. Identificar clientes o expertos que destaquen por su
            #    conocimiento o entusiasmo
            "1": ["CUBIERTO", 1],
            # 2. Invitarlos a compartir su opinion mediante almuerzos o
            #    reuniones informales
            "2": ["CUBIERTO", 2],
            # 3. Evaluar su interes en convertirse en asesores formales
            "3": ["CUBIERTO", 2],
            # 4. Buscar asesores para problemas tecnicos, introducciones a
            #    clientes clave, conocimiento de dominio y desarrollo de producto
            "4": ["CUBIERTO", 3],
        },
    },
    "condiciones": {
        "identificar_junta_asesores": {
            # 1. Cuando el equipo necesita orientacion tecnica o de negocio
            #    externa
            "1": ["CUBIERTO", 3],
            # 2. Si se han identificado clientes con voces destacadas durante el
            #    descubrimiento
            "2": ["CUBIERTO", 1],
        },
    },
    "nota": (
        "SEIS PIEZAS REPARTIDAS, LAS SEIS DE CUBIERTO Y NINGUNA DE APPEND, y eso es "
        "exactamente lo que la adjudicacion del expediente dice con sus palabras: EL "
        "GEMELO DE CUATRO PASOS NO APORTA NADA PROPIO. Se comprueba paso por paso contra "
        "el texto de hoy y no contra la tabla del expediente. "
        "PASO 1 contra PASO 1: el absorbido identifica clientes o expertos que destaquen "
        "por su conocimiento o entusiasmo; el superviviente identifica, durante las "
        "entrevistas de descubrimiento, personas con conocimiento de dominio o entusiasmo "
        "notable. Es el mismo gesto en el mismo momento, y el superviviente ademas fija el "
        "momento. "
        "PASO 2 contra PASO 2: el absorbido invita a almuerzos o reuniones informales; el "
        "superviviente invita a un cafe o charla informal. Mismo gesto, otros ejemplos, y "
        "el matiz va SELLADO EN CAMPO PROPIO como perdida de parametro. "
        "PASO 3 contra PASO 2: evaluar el interes en convertirse en asesores formales es "
        "explorar su interes en asesorarte, que es lo que el paso 2 del superviviente "
        "manda hacer en el mismo encuentro. ES EL SOLAPE QUE EL EXPEDIENTE NOMBRA, y por "
        "su propia letra NO SE REGISTRA COMO PERDIDA. "
        "PASO 4 contra PASOS 3 y 5: buscar asesores para problemas tecnicos y desarrollo "
        "de producto es el paso 3 del superviviente; introducciones a clientes clave y "
        "conocimiento de dominio es su paso 5. La marca apunta al 3 porque una marca "
        "nombra UN paso; el 5 queda dicho aqui. "
        "CONDICION 1 contra CONDICION 3: necesitar orientacion tecnica o de negocio "
        "EXTERNA es necesitar conocimiento externo especializado que no se puede contratar "
        "a tiempo completo. CONDICION 2 contra CONDICION 1: haber identificado clientes "
        "con voces destacadas DURANTE EL DESCUBRIMIENTO es el disparador oportunista del "
        "superviviente, durante todo el proceso de customer discovery. "
        "UNA PERDIDA SELLADA, DE MATIZ Y NO DE GESTO."
    ),
    "perdidas": [
        {
            "especie": "DE PARAMETRO DE PASO",
            "que": ("el ALMUERZO o la REUNION INFORMAL como formato del primer encuentro, y "
                    "el encuadre de invitarlos a COMPARTIR SU OPINION antes de pedirles "
                    "nada; el paso 2 del superviviente invita a un cafe o charla informal "
                    "para explorar su interes en asesorarte, que es el mismo encuentro con "
                    "otros ejemplos y con la pregunta hecha de frente"),
            "donde": "paso 2 de identificar_junta_asesores",
            "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente",
        },
    ],
    "simulacion_de_hoy": (
        "scripts/plan/simular_fusion.py corrido en la vuelta 144 ANTES de tocar un nodo "
        "(docs/loop/SALIDA_V144_3B_SIMULACION.txt), con las DOS fusiones de la mesa a la "
        "vez porque es un solo acto: CUATRO entradas se redirigen a este superviviente "
        "(ai_como_coach_personalizado, formalizar_junta_asesora, producto_minimo_viable y "
        "verificar_product_market_fit), UNA duplicada NUEVA de su lado "
        "(verificar_product_market_fit.nodos_previos), CERO auto aristas, y el alias del "
        "superviviente queda con identificar_advisory_board, el que ya tenia, mas "
        "identificar_junta_asesores. CALZA AL DIGITO CON LO QUE LA FICHA ESCRIBIO EL 11 "
        "AGO 2026 en su verificacion 4 y en su nota: las cuatro entradas que se redirigen "
        "limpias y las dos duplicadas de la clase OP-S-12. LA ARISTA INTERNA DEL ACTO QUE "
        "SOBREVIVE ES UNA Y ES LA VUELTA, formalizar_junta_asesora hacia "
        "identificar_consejo_asesores, que es exactamente lo que la nota de la ficha "
        "predice y lo que el GIRO de esta misma operacion viene a corregir."
    ),
}
