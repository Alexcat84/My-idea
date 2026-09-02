# -*- coding: utf-8 -*-
"""_v139_opm05indice.py . EL CONTENIDO EDITORIAL DE LA FUSION DE MESA
OP-M-05-INDICE, EL INDICE DE DISCOVERY.

NO ES UN INSTRUMENTO. Es EL TEXTO del reparto pieza a pieza. Lo importa
scripts/loop/generar_plan_de_fusion_de_mesa.py, que pone LA ARITMETICA Y LAS
GUARDAS y sella el plan.

LA LECTURA CON EL OJO QUE EL ENCARGO EXIGE, Y AQUI ES LA TAREA ENTERA. Esta
ficha es la unica de las cinco cuyas TRES lineas de preservar no nombran NINGUN
id: "las cuatro fases enumeradas", "las nueve partes del lienzo" y "la puerta
del final". La maquina no puede decidir de quien es cada una, asi que se leen
con el ojo contra los dos absorbidos y contra el superviviente, y se dice de
quien es cada una. Una busqueda negativa no se puede citar (EJECUTOR regla 9).

  LINEA 1, LAS CUATRO FASES ENUMERADAS. ES DE customer_discovery_cuatro_fases,
  Y NO ES UN EMPATE. Sus cuatro pasos empiezan literalmente por "Fase 1:",
  "Fase 2:", "Fase 3:" y "Fase 4:". customer_discovery_overview trae LAS MISMAS
  CUATRO FASES COMO CONTENIDO pero NO LAS ENUMERA: solo su TITULO dice "Las
  cuatro fases", y ninguno de sus cuatro pasos lleva el rotulo. El
  superviviente no las lleva de ninguna forma: sus cinco pasos no estan
  numerados por fase. LA ENUMERACION ES DE UNO SOLO, y la verificacion 3 de la
  ficha manda comprobarla ENTERA ("si el superviviente queda sin las fases
  enumeradas, se perdio el indice").

  LINEA 2, LAS NUEVE PARTES DEL LIENZO. ES DE LOS DOS, y por eso es la pieza de
  dos duenos de este acto: el paso 1 de customer_discovery_cuatro_fases dice
  "desarma tu idea en las nueve partes del lienzo de modelo de negocio" y el
  paso 1 de customer_discovery_overview dice "descompon tu vision inicial en
  las nueve partes de tu lienzo de modelo de negocio". El superviviente NO las
  tiene: su paso 5 ajusta el modelo de negocio segun el feedback, que es otra
  cosa, y ninguno de sus cinco pasos nombra el lienzo ni sus nueve partes.

  LINEA 3, LA PUERTA DEL FINAL. ES DE LOS DOS: el paso 4 de
  customer_discovery_cuatro_fases y el paso 4 de customer_discovery_overview
  evaluan y deciden si se pasa a la fase siguiente. El superviviente NO tiene
  la puerta: su paso 4 confirma que el problema le importa al cliente lo
  suficiente para comprar, que es UNA de las preguntas de la puerta, no la
  puerta; y ningun paso suyo decide si se avanza a Customer Validation.

DE DONDE SALE CADA AFIRMACION: de leer los tres nodos enteros, sus 5 mas 4 mas
4 pasos y sus 2 mas 2 mas 2 condiciones, impresos en
docs/loop/SALIDA_V139_3_VERIF_OPM05INDICE.txt.
"""

FUSION = {
    "titulo": (
        "EL INDICE DE DISCOVERY, DE BLANK: customer_discovery absorbe a "
        "customer_discovery_cuatro_fases y a customer_discovery_overview. Es la misma "
        "figura de la cabeza duplicada de Coleman, dos indices de las mismas cuatro fases "
        "y un nodo base al que los dos describen, PERO AQUI GANA EL BASE, porque su "
        "cableado es de otro orden"
    ),
    "superviviente": "customer_discovery",
    "absorbidos": ["customer_discovery_cuatro_fases", "customer_discovery_overview"],
    "motivo": (
        "EL SUPERVIVIENTE LO FIJA LA FICHA SELLADA Y AQUI NO SE RE-ADJUDICA: "
        "docs/plan/OPERACIONES.jsonl escribe superviviente customer_discovery el 12 ago "
        "2026. Su adjudicacion dice que EL CONTENIDO NO DECIDE, porque los dos indices "
        "dicen LO MISMO entre si (puesto 156) y el nodo base dice el concepto, y que "
        "DECIDE EL CABLEADO Y NO ESTA CERCA. "
        "LA REGLA DE LA FICHA ENVEJECIDA (P.9, P.13) SE APLICA Y SE DECLARA: la ficha "
        "escribe MEDIDO: cableado 28 contra 6 contra 5 (12 ago 2026); la simulacion del 2 "
        "sep 2026, sellada en docs/loop/SALIDA_V139_3_SIM_OPM05INDICE.txt, mide 30 contra "
        "11 y 30 contra 10. NO VOLTEA NADA, y de las cinco mesas esta es la que menos "
        "riesgo corria: customer_discovery gana por casi el triple con las dos "
        "mediciones. LAS DUPLICADAS SI CUADRAN AL DIGITO Y CON SUS NOMBRES: CUATRO, "
        "customer_validation.nodos_previos, identificar_earlyvangelists.nodos_previos, "
        "lienzo_modelo_negocio.nodos_siguientes y producto_minimo_viable.nodos_previos, "
        "las mismas cuatro que la verificacion 2 de la ficha nombra. CERO auto aristas y "
        "CERO aristas internas del acto que sobrevivan. "
        "LECTURA DE ACTO POR P.5, RE-CORRIDA HOY ANTES DE FUNDIR: 3 pares leidos = 3 "
        "pares del acto, EXIT 0. SE DICE QUE MIDE, PARA QUE NADIE LO LEA DE MAS: la "
        "verificacion 4 de la ficha habla de VEINTE pares internos fuera de cola del "
        "ACTO DE DISCOVERY ENTERO, que es una zona mas ancha que esta operacion; el "
        "alcance de P.5 quedo acotado por la correccion declarada del 15 ago 2026 AL ACTO "
        "EN OPERACION Y NADA MAS, y el acto en operacion son estos TRES nodos y sus TRES "
        "pares, los tres leidos y los tres en A (puestos 206, 276 y 156). "
        "EL DUDOSO DEL 707 NO SE RESUELVE AQUI Y LA FICHA YA LO DEJA ESCRITO: "
        "customer_development_modelo contra customer_discovery_overview queda en B, y "
        "overview muere en esta fusion. TRAS EJECUTARLA, EL 707 SE RELEE CONTRA EL "
        "SUPERVIVIENTE, por el banco 9.10. Esta fusion NO lo cierra y NO lo toca."
    ),
    "pasos": {
        "customer_discovery_cuatro_fases": {
            # 1. Fase 1: desarma tu idea en las nueve partes del lienzo de
            #    modelo de negocio y escribe un resumen de una pagina por cada
            #    hipotesis   <-- preservar [2], y la redaccion que VIAJA
            "1": ["APPEND"],
            # 2. Fase 2: sal a probar tus hipotesis de 'problema' hablando
            #    directamente con clientes reales
            "2": ["APPEND"],
            # 3. Fase 3: muestra tu producto minimo viable y compara las
            #    respuestas contra tus metas de exito y fracaso definidas de
            #    antemano
            "3": ["APPEND"],
            # 4. Fase 4: evalua si entendiste el problema, si tu propuesta de
            #    valor se valida, cuantos clientes hay, si pagarian y si el
            #    negocio es rentable, y decide si avanzas a validar con clientes
            #    o vuelves a aprender mas   <-- preservar [3], LA PUERTA DEL FINAL
            "4": ["APPEND"],
        },
        "customer_discovery_overview": {
            # 1. Descompon tu vision inicial en las nueve partes de tu lienzo de
            #    modelo de negocio (Business Model Canvas)
            "1": ["VIAJA_EN_EL_ACTO", "customer_discovery_cuatro_fases", 1],
            # 2. Sal a comprobar si el problema es real y le duele a tus clientes
            "2": ["VIAJA_EN_EL_ACTO", "customer_discovery_cuatro_fases", 2],
            # 3. Muestrales tu producto minimo viable (MVP) y tu propuesta de
            #    valor para validar la solucion
            "3": ["VIAJA_EN_EL_ACTO", "customer_discovery_cuatro_fases", 3],
            # 4. Evalua los resultados y decide si tienes suficiente validacion
            #    para pasar a probar con clientes reales (Customer Validation) o
            #    si necesitas pivotar
            "4": ["VIAJA_EN_EL_ACTO", "customer_discovery_cuatro_fases", 4],
        },
    },
    "condiciones": {
        "customer_discovery_cuatro_fases": {
            # 1. Cuando necesitas ordenar de forma metodica todo el proceso de
            #    descubrir a tu cliente
            "1": ["APPEND"],
            # 2. Cuando arrancas el proceso formal de descubrir a tu cliente en
            #    un proyecto nuevo
            "2": ["APPEND"],
        },
        "customer_discovery_overview": {
            # 1. Tienes una hipotesis de negocio pero todavia no has salido a
            #    hablar con clientes reales
            "1": ["CUBIERTO", 2],
            # 2. Quieres evitar construir un producto completo sin validar antes
            #    el problema
            "2": ["APPEND"],
        },
    },
    "lineas_de_viaje": {
        "customer_discovery_overview|1": (
            "MISMO GESTO: descomponer la idea en LAS NUEVE PARTES DEL LIENZO, que es la "
            "linea 2 de preservar. El paso 1 de customer_discovery_overview y el paso 1 de "
            "customer_discovery_cuatro_fases mandan lo mismo y el superviviente no lo tiene "
            "en ninguno de sus cinco pasos. VIAJA LA REDACCION DE "
            "customer_discovery_cuatro_fases, que es la que lleva el APPEND, por dos "
            "motivos de texto: es la UNICA que trae el rotulo Fase 1, que la linea 1 de "
            "preservar exige enumerado, y ademas es la mas rica, porque anade escribir un "
            "resumen de una pagina por cada hipotesis, que la otra no dice. LO UNICO QUE "
            "ESTA REDACCION TRAE Y LA OTRA NO ES EL NOMBRE EN INGLES ENTRE PARENTESIS "
            "(Business Model Canvas), Y SE DECLARA: es una glosa de terminologia y no un "
            "gesto, asi que no se trata como pieza propia. Va marcado como DISCUTIBLE en el "
            "reporte de esta vuelta."
        ),
        "customer_discovery_overview|2": (
            "MISMO GESTO: salir a comprobar la hipotesis del problema con clientes reales. "
            "El paso 2 de customer_discovery_overview y el paso 2 de "
            "customer_discovery_cuatro_fases mandan lo mismo. VIAJA LA REDACCION DE "
            "customer_discovery_cuatro_fases, que es la que lleva el APPEND, porque es la "
            "unica que trae el rotulo Fase 2 y la linea 1 de preservar exige LAS CUATRO "
            "FASES ENUMERADAS, no tres. El matiz de esta redaccion, que el problema LE "
            "DUELE al cliente, no se pierde: el paso 4 del superviviente confirma que el "
            "problema le importa lo suficiente como para que decida comprar."
        ),
        "customer_discovery_overview|3": (
            "MISMO GESTO: mostrar el producto minimo viable para validar la solucion. El "
            "paso 3 de customer_discovery_overview y el paso 3 de "
            "customer_discovery_cuatro_fases mandan lo mismo. VIAJA LA REDACCION DE "
            "customer_discovery_cuatro_fases, que es la que lleva el APPEND, porque trae el "
            "rotulo Fase 3 que preservar exige Y porque es la mas rica: compara las "
            "respuestas contra las metas de exito y fracaso DEFINIDAS DE ANTEMANO, que esta "
            "no dice. El matiz de esta, mostrar tambien LA PROPUESTA DE VALOR, no se pierde: "
            "el paso 4 de customer_discovery_cuatro_fases evalua si la propuesta de valor se "
            "valida, y viaja entero de APPEND."
        ),
        "customer_discovery_overview|4": (
            "MISMO GESTO: LA PUERTA DEL FINAL, que es la linea 3 de preservar: evaluar si "
            "hay validacion suficiente para pasar a la fase siguiente. El paso 4 de "
            "customer_discovery_overview y el paso 4 de customer_discovery_cuatro_fases "
            "mandan lo mismo, y el superviviente NO tiene la puerta: su paso 4 confirma que "
            "el problema le importa al cliente lo suficiente para comprar, que es UNA de las "
            "preguntas de la puerta y no la puerta. VIAJA LA REDACCION DE "
            "customer_discovery_cuatro_fases, que es la que lleva el APPEND, porque trae el "
            "rotulo Fase 4 que preservar exige Y porque enumera las CINCO preguntas de la "
            "puerta (si entendiste el problema, si la propuesta de valor se valida, cuantos "
            "clientes hay, si pagarian y si el negocio es rentable) donde esta solo dice "
            "evalua los resultados. Su unico matiz propio, nombrar el PIVOTE como salida, "
            "no se pierde: la otra dice vuelves a aprender mas, que es la misma rama, y el "
            "pivote tiene su propio acto en OP-M-03-III."
        ),
    },
    "nota": (
        "DOCE PIEZAS REPARTIDAS ENTRE DOS ABSORBIDOS, 8 de paso y 4 de condicion, y el "
        "reparto lo CUENTA EL GENERADOR de las marcas: esta nota no lo teclea. "
        "EL INDICE VIAJA ENTERO Y ESA ES LA DECISION DE ESTE ACTO. Los CUATRO pasos de "
        "customer_discovery_cuatro_fases van de APPEND, los cuatro, y los CUATRO de "
        "customer_discovery_overview llevan VIAJA_EN_EL_ACTO apuntando al suyo, uno a uno. "
        "Es el uso mas limpio de la quinta marca que da la fase 06: dos indices que dicen "
        "LO MISMO paso por paso (que es exactamente lo que el puesto 156 dictamino) y un "
        "superviviente que no lleva ninguno de los dos. "
        "POR QUE LOS CUATRO DE APPEND Y NINGUNO CUBIERTO, que es la parte discutible y va "
        "dicha: LA VERIFICACION 3 DE LA FICHA MANDA COMPROBAR LAS CUATRO FASES ENTERAS, "
        "con la frase si el superviviente queda sin las fases enumeradas, SE PERDIO EL "
        "INDICE. El indice es UNA pieza de cuatro rotulos, no cuatro piezas sueltas: "
        "marcar CUBIERTO el rotulo Fase 2 o el Fase 3 dejaria un indice de tres fases, que "
        "no es un indice. Y SE DICE EL PRECIO EN VEZ DE CALLARLO: la sustancia de la fase "
        "2 (salir a probar la hipotesis del problema con clientes reales) ya esta en los "
        "pasos 1 y 2 del superviviente, y la de la fase 3 (mostrar el MVP) esta en su paso "
        "3. Las fases 2 y 3 repiten sustancia que el superviviente ya tiene, y lo que "
        "anaden es EL ROTULO y, en la 3, la comparacion contra metas definidas de antemano. "
        "EL SUPERVIVIENTE QUEDA EN 9 PASOS Y 5 CONDICIONES, contra 5 y 2 de partida, y ES "
        "CANDIDATO LEGITIMO A LA PODA DE LA FASE 04 por esa repeticion de sustancia, que "
        "es donde esa poda tiene que mirar. Va marcado como DISCUTIBLE en el reporte. "
        "LAS TRES CONDICIONES DE APPEND SON DISPARADORES DISTINTOS (acta 55, pregunta 5): "
        "NECESITAR ORDENAR METODICAMENTE el proceso es una falta de metodo, no de hechos; "
        "ARRANCAR EL PROCESO FORMAL EN UN PROYECTO NUEVO es un hito de calendario; y "
        "QUERER EVITAR CONSTRUIR UN PRODUCTO COMPLETO SIN VALIDAR es una intencion de "
        "ahorro. Ninguna de las tres es la condicion 1 del superviviente (el negocio se "
        "basa solo en tu vision) ni su condicion 2 (todavia no has probado con clientes). "
        "CERO PERDIDAS SELLADAS, Y LA LISTA VACIA ES UNA DECLARACION: la verificacion 5 de "
        "la ficha dice que LAS 3 VIAJAN todas, y las tres viajan."
    ),
    "perdidas": [],
    "simulacion_de_hoy": (
        "scripts/plan/simular_fusion.py, corrida el 2 sep 2026 ANTES de fundir, salida "
        "sellada en docs/loop/SALIDA_V139_3_SIM_OPM05INDICE.txt: CUATRO duplicadas nuevas, "
        "LAS MISMAS CUATRO que la ficha nombra, CERO auto aristas, CERO aristas internas "
        "del acto que sobrevivan, y cableado 30 contra 11 y 30 contra 10, donde la ficha "
        "del 12 ago decia 28 contra 6 contra 5. La divergencia va declarada."
    ),
}
