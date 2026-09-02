# -*- coding: utf-8 -*-
"""_v139_opm05apertura.py . EL CONTENIDO EDITORIAL DE LA FUSION DE MESA
OP-M-05-APERTURA, LA APERTURA DE CUSTOMER VALIDATION.

NO ES UN INSTRUMENTO. Es EL TEXTO del reparto pieza a pieza. Lo importa
scripts/loop/generar_plan_de_fusion_de_mesa.py, que pone LA ARITMETICA Y LAS
GUARDAS y sella el plan.

AQUI VA LA DISCREPANCIA MAS GRANDE DE ESTA VUELTA, Y VA MARCADA COMO DISCUTIBLE
1 EN EL REPORTE, ESCRITA ANTES DE SABER SI ACIERTO.

El acta de la vuelta 138, caida 4.2, midio a mano que la linea 3 de `preservar`
de esta ficha nombra DOS absorbidos y concluyo, con estas palabras, que "EL
HUECO MUERDE EN TRES GRUPOS MEDIDOS, NO EN DOS", contando esta mesa como el
tercero. El encargo de la 139 lo repite: "la pieza es probar que el proceso de
venta SE REPITE, buscar pedidos a PRECIO COMPLETO como prueba dura, y probar los
canales, esta en el paso 1 de introduccion_validacion_clientes y en el paso 5 de
filosofia_customer_validation".

LO MEDI PIEZA POR PIEZA ANTES DE MARCAR NADA, Y NO CUADRA ASI:

  - LA PIEZA DE LA LINEA 3 TIENE TRES PARTES y las TRES estan en
    introduccion_validacion_clientes, una por paso: la repetibilidad en su paso
    1, los pedidos A PRECIO COMPLETO en su paso 2, y los canales en su paso 3.
  - EL PASO 5 DE filosofia_customer_validation NO CONTIENE ESA PIEZA. Contiene
    TRES PREGUNTAS ("puede crecer tu negocio", "tu forma de vender se repite",
    "puedes predecir cuanta gente avanza hacia la compra"), que son
    exactamente LA LINEA 1 de preservar, LAS TRES PREGUNTAS DE ESCALA. De las
    tres partes de la linea 3 solo toca UNA, la repetibilidad, y la toca como
    PREGUNTA DE PUERTA, no como prueba que se corre.
  - O SEA: los dos absorbidos NO comparten la pieza. Comparten UN TERCIO de UNA
    de sus tres partes, y con figuras distintas: uno manda CORRER LA PRUEBA de
    repetibilidad, el otro manda RESPONDER SI SE REPITE.

Y POR ESO AQUI NO SE USA VIAJA_EN_EL_ACTO, POR LA REGLA DEL PROPIO AUDITOR: "SI
EL SEGUNDO DUENO TRAE UN MATIZ QUE EL PRIMERO NO TRAE, ESE MATIZ NO ES
VIAJA_EN_EL_ACTO: es una pieza propia y viaja con su propia marca, por P.13".
Los dos traen matices que el otro no trae, y de sobra: el paso 5 de la filosofia
trae DOS preguntas mas (crecer y predecir) que el otro no tiene y que la
verificacion 2 de la ficha manda comprobar UNA POR UNA; y el paso 1 de la
introduccion trae la adquisicion de usuarios y la forma imperativa de prueba.
Marcar uno VIAJA_EN_EL_ACTO perderia contenido que preservar exige.

LOS DOS VIAJAN DE APPEND, y se declara el solape: en el texto final la
repetibilidad de la venta aparece DOS VECES, una como prueba (paso de la
introduccion) y otra como pregunta de puerta (dentro de las tres preguntas de la
filosofia). Es candidato legitimo a la poda de la fase 04 y va dicho, no callado.

DONDE SI MUERDE EL HUECO EN ESTA VUELTA, para que la cuenta quede clara: en
OP-M-01-FUSION (los entregables, TRES duenos), en OP-M-03-III (dos piezas, dos
duenos cada una), en OP-M-05-INDICE (el indice entero, cuatro pasos) y en
OP-M-05-EDIFICIO (no delegar, dos duenos). CUATRO grupos medidos, y esta mesa
NO es uno de ellos.
"""

FUSION = {
    "titulo": (
        "LA APERTURA DE CUSTOMER VALIDATION, DE BLANK: customer_validation absorbe a "
        "filosofia_customer_validation y a introduccion_validacion_clientes. Se funde EL "
        "TRIANGULO CERRADO DE TRES y customer_validation_sell_phase queda fuera y se "
        "enlaza, como LD-59 corrigio el 12 ago 2026"
    ),
    "superviviente": "customer_validation",
    "absorbidos": ["filosofia_customer_validation", "introduccion_validacion_clientes"],
    "motivo": (
        "EL SUPERVIVIENTE LO FIJA LA FICHA SELLADA Y AQUI NO SE RE-ADJUDICA: "
        "docs/plan/OPERACIONES.jsonl escribe superviviente customer_validation el 12 ago "
        "2026, por P.8 en orden: el contenido esta empatado (los dos LISTAN LAS ACTIVIDADES "
        "DE LA ETAPA y coinciden en las tres centrales, puesto 549) y decide el cableado. "
        "LA REGLA DE LA FICHA ENVEJECIDA (P.9, P.13) SE APLICA Y SE DECLARA, y aqui las DOS "
        "cifras se mueven: "
        "  (a) CABLEADO. La ficha escribe MEDIDO: cableado 14 contra 8 contra 6 contra 5 (12 "
        "ago 2026), que es una cuenta de CUATRO nodos, la nomina de antes de LD-59. La "
        "simulacion del 2 sep 2026 mide 18 contra 10 y 18 contra 8 sobre los TRES que hoy "
        "se funden. NO VOLTEA NADA: customer_validation gana por casi el doble contra los "
        "dos. "
        "  (b) DUPLICADAS. La ficha escribe TRES y las nombra: "
        "business_model_canvas_scorecard.nodos_siguientes, customer_creation.nodos_previos y "
        "customer_discovery.nodos_siguientes. La simulacion de hoy mide SEIS, y SOLO DOS DE "
        "LOS NOMBRES COINCIDEN: siguen business_model_canvas_scorecard y customer_discovery, "
        "YA NO ESTA customer_creation, y aparecen checkpoints_validacion.nodos_previos, "
        "decision_pivotar_o_proceder.nodos_previos, "
        "preservar_efectivo_buscar_modelo.nodos_siguientes y "
        "realizar_pruebas_pasa_no_pasa.nodos_previos. ES LA DIVERGENCIA MAS GRANDE DE LAS "
        "CINCO MESAS DE ESTA VUELTA, y se declara entera en vez de copiarse: las SEIS siguen "
        "enrutadas a OP-S-12 por la propia ficha, que se equivoco en la cantidad y en cuatro "
        "nombres, no en el destino. CERO auto aristas y CERO aristas internas del acto que "
        "sobrevivan, las dos como la ficha dice. "
        "LECTURA DE ACTO POR P.5, RE-CORRIDA HOY ANTES DE FUNDIR: 3 pares leidos = 3 pares "
        "del acto, EXIT 0. Los tres del triangulo estan en A (247, 709 y 549). "
        "customer_validation_sell_phase NO ENTRA, y no por olvido: su D con "
        "introduccion_validacion_clientes lo deja fuera, y meterlo seria fundir sobre un D "
        "(verificacion 4 de la ficha). "
        "TRES RELECTURAS QUEDAN PENDIENTES Y NO SE TOCAN AQUI, todas por el banco 9.10 y "
        "todas escritas por la ficha: earlyvangelists_ventas_tempranas contra el "
        "superviviente (verificacion 3), y los puestos 781 y 245 contra el superviviente "
        "(verificacion 5). NO SE DECIDEN POR ADELANTADO."
    ),
    "pasos": {
        "filosofia_customer_validation": {
            # 1. Revisa las hipotesis de negocio que ya confirmaste hablando con
            #    clientes
            "1": ["CUBIERTO_COND", 1],
            # 2. Prepara tu primera version del producto (MVP) y los materiales
            #    que necesitas para vender y difundirlo
            "2": ["CUBIERTO", 1],
            # 3. Sal a pedir pedidos reales, no solo opiniones
            "3": ["CUBIERTO", 4],
            # 4. Confirma que haya pedidos, usuarios o clics reales, no solo
            #    respuestas de encuestas   <-- preservar [2] dice, con estas
            #    palabras: VIVE DENTRO EN SU NUCLEO (el paso 4 del superviviente)
            #    y VIAJA SOLO EL MATIZ. Por eso INCISO y no APPEND.
            "4": ["INCISO", 4, "usuarios o clics reales, no solo respuestas de encuestas",
                  ", y cuentan como evidencia los "],
            # 5. Responde estas tres preguntas: puede crecer tu negocio, tu forma
            #    de vender se repite, puedes predecir cuanta gente avanza hacia
            #    la compra   <-- preservar [1], LAS TRES PREGUNTAS DE ESCALA
            "5": ["APPEND"],
        },
        "introduccion_validacion_clientes": {
            # 1. Probar la repetibilidad del proceso de ventas o adquisicion de
            #    usuarios   <-- preservar [3], primera parte
            "1": ["APPEND"],
            # 2. Buscar pedidos u ordenes reales a precio completo como prueba de
            #    validacion   <-- preservar [3], segunda parte, PRECIO COMPLETO
            "2": ["APPEND"],
            # 3. Probar canales de ventas y distribucion
            #    <-- preservar [3], tercera parte
            "3": ["APPEND"],
            # 4. Escuchar activamente a los clientes para identificar pivotes
            #    necesarios   <-- preservar [5]
            "4": ["APPEND"],
            # 5. Posicionar correctamente el producto y la empresa
            #    <-- preservar [5]
            "5": ["APPEND"],
        },
    },
    "condiciones": {
        "filosofia_customer_validation": {
            # 1. Cuando ya hablaste con clientes y confirmaste tus hipotesis, y
            #    necesitas comprobar si tu negocio realmente genera ventas
            "1": ["CUBIERTO", 1],
        },
        "introduccion_validacion_clientes": {
            # 1. Cuando el equipo decidio 'proceder' tras el descubrimiento de
            #    clientes y necesita iniciar la fase de validacion
            "1": ["CUBIERTO", 1],
        },
    },
    "nota": (
        "DOCE PIEZAS REPARTIDAS ENTRE DOS ABSORBIDOS, 10 de paso y 2 de condicion, y el "
        "reparto lo CUENTA EL GENERADOR de las marcas: esta nota no lo teclea. "
        "CERO VIAJA_EN_EL_ACTO EN ESTA MESA, Y ES LA DISCREPANCIA QUE ESTA VUELTA TRAE "
        "MARCADA. El acta 138 conto esta mesa como el TERCER grupo donde el hueco muerde. "
        "Medido pieza por pieza antes de marcar nada, no cuadra asi: la pieza de la linea 3 "
        "de preservar tiene TRES partes y las tres estan en introduccion_validacion_clientes "
        "(repetibilidad en su paso 1, precio completo en su paso 2, canales en su paso 3); "
        "el paso 5 de filosofia_customer_validation NO contiene esa pieza, contiene LAS TRES "
        "PREGUNTAS DE ESCALA, que son la linea 1 de preservar, y de las tres partes de la "
        "linea 3 solo toca UNA, la repetibilidad, y la toca como PREGUNTA DE PUERTA y no "
        "como prueba que se corre. LOS DOS TRAEN MATICES QUE EL OTRO NO TRAE, y la regla del "
        "propio auditor dice que entonces cada uno es PIEZA PROPIA y viaja con su propia "
        "marca. Los dos van de APPEND. "
        "Y SE DECLARA EL SOLAPE EN VEZ DE CALLARLO: en el texto final la repetibilidad de la "
        "venta aparece DOS VECES, una como prueba y otra como pregunta de puerta dentro de "
        "las tres preguntas de escala. Es candidato legitimo a la poda de la fase 04. "
        "EL UNICO INCISO ES EL QUE LA FICHA MANDA, con sus palabras: su linea 2 de preservar "
        "dice VIVE DENTRO EN SU NUCLEO, confirmar con ventas reales y con dinero de por "
        "medio es el paso 4 del superviviente, y VIAJA SOLO EL MATIZ, que los clics y los "
        "usuarios cuentan como evidencia y las respuestas de encuesta no. El trozo se EXTRAE "
        "VERBATIM del paso 4 de la filosofia y se adosa al paso 4 del superviviente, que no "
        "cierra en punto. Es la unica linea de preservar de las cinco mesas que pide "
        "expresamente un matiz y no una pieza. "
        "UN CUBIERTO_COND, Y ES EL PRIMERO DE LA FASE 06: el paso 1 de la filosofia (revisa "
        "las hipotesis que ya confirmaste hablando con clientes) no es un paso del "
        "superviviente, es SU CONDICION 1 (si ya terminaste el descubrimiento de clientes y "
        "confirmaste el problema y la solucion). La marca CUBIERTO_COND existe justo para "
        "esto y se usa en vez de forzar un CUBIERTO de paso que no seria verdad. "
        "LA LINEA 4 DE preservar NO SE REPARTE PORQUE LA PROPIA FICHA LA RETIRA: dice YA NO "
        "APLICA, customer_validation_sell_phase DEJO DE ENTRAR en esta fusion por LD-59, el "
        "nodo sigue vivo y se queda con su pieza. No hay nada que marcar. "
        "LA VERIFICACION 6 SE COMPRUEBA SIN TOCAR NADA: lo propio del hijo (confirmar el "
        "proceso real de compra y de aprobacion DENTRO DEL NEGOCIO DEL CLIENTE) sigue en "
        "customer_validation_sell_phase, que no entra en esta fusion, asi que no se copia "
        "arriba por construccion. "
        "EL SUPERVIVIENTE QUEDA EN 11 PASOS Y 2 CONDICIONES, contra 5 y 2 de partida. "
        "CERO PERDIDAS SELLADAS, Y LA LISTA VACIA ES UNA DECLARACION: las cuatro lineas "
        "vivas de preservar viajan (la 1 de APPEND, la 2 de INCISO, la 3 en tres APPEND y la "
        "5 en dos APPEND) y la 4 la retira la ficha."
    ),
    "perdidas": [],
    "simulacion_de_hoy": (
        "scripts/plan/simular_fusion.py, corrida el 2 sep 2026 ANTES de fundir, salida "
        "sellada en docs/loop/SALIDA_V139_3_SIM_OPM05APERTURA.txt: SEIS duplicadas nuevas "
        "donde la ficha decia TRES, y solo DOS de los nombres coinciden; CERO auto aristas; "
        "CERO aristas internas del acto que sobrevivan; y cableado 18 contra 10 y 18 contra "
        "8, donde la ficha decia 14 contra 8 contra 6 contra 5 sobre una nomina de cuatro. "
        "Las divergencias van declaradas, no resueltas copiando."
    ),
}
