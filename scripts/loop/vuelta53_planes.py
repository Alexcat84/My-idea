# -*- coding: utf-8 -*-
"""vuelta53_planes.py . ESCRIBE LOS TRES PLANES SELLADOS DE LA VUELTA 53.

POR QUE EXISTE COMO INSTRUMENTO Y NO COMO TRES FICHEROS TECLEADOS: los planes
llevan marcas INCISO cuyo primer campo tiene que ser un trozo VERBATIM del paso
del nodo absorbido, con sus acentos exactos. Teclearlo a mano es la especie de
las paradas de credito de las vueltas 31 y 32. Aqui cada inciso se COMPRUEBA
contra el fichero del nodo antes de escribir el plan, y si no calza el
instrumento cae en ROJO y no escribe nada.

Tambien comprueba, antes de escribir:
  - que todos los miembros existan y esten VIVOS,
  - que la cobertura de indices sea exacta (cada paso y cada condicion del
    absorbido con marca, ninguna de mas),
  - que el superviviente y los absorbidos calcen con los miembros.

DE SOLO LECTURA sobre el dataset. Escribe unicamente los tres JSON del plan.

Uso: python scripts/loop/vuelta53_planes.py [--simular]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
LOOP = os.path.join(RAIZ, "docs", "loop")

VARA = (
    "P.12 con la receta RATIFICADA (acta de la vuelta 50, preguntas 1 a 3; acta de la vuelta 51; "
    "acta de la vuelta 52, pregunta 1): dado un superviviente S, PARTE A = S mas los miembros con "
    "arista A contra S; MIXTOS = los miembros sin arista A contra S; S es VIABLE si su parte A es "
    "clique A y deja al menos un mixto fuera. Entre los viables elige el CONTENIDO como P.8 lo "
    "define: el texto de los pasos y las condiciones, el material propio, el padre declarado y el "
    "ALCANCE DEL ROL, todo EN LAS RAZONES del archivo; el conteo de caracteres del resumen NO "
    "desempata. Si el contenido calla, el CABLEADO decide solo. Si tambien empata, se DECLARA el "
    "acto como empate sin vara."
)

CARRIL_COLISIONES = (
    "CARRIL GENERAL DE COLISIONES, adjudicado en el acta de la vuelta 52, pregunta 4, y registrado "
    "en docs/plan/03_FUSIONES.md por la TAREA 1.4.b de esta vuelta: volteo por maquina SOLO para el "
    "A ARRASTRADO contra un DIRECTO D, citando el directo y pegando la razon vieja entera; "
    "cualquier veredicto DEL FILO (B o C) en CUALQUIERA de los dos lados se RELEE EN EL MISMO ACTO "
    "con el otro como contraste, LA RELECTURA DECIDE CUAL SE MUEVE, y si destapa politica el acto "
    "se declara."
)

POLITICA_REPARTO = (
    "LA MISMA DEL LOTE B DE LA VUELTA 52, heredada y citada, no reinventada (acta 51, D3, y acta "
    "52, D5 y D10): una pieza del absorbido cuyo unico contenido propio es un PARAMETRO CONCRETO "
    "de un gesto que el superviviente ya tiene va de INCISO ADOSADO cuando el paso resultante se "
    "lee limpio, y de CUBIERTO con la perdida NOMBRADA cuando no. Una pieza que es un GESTO "
    "DISTINTO va de APPEND. Y una pieza cuya linea vive ENTERA en un vecino VIVO del racimo (el "
    "mixto que sobrevive, o un nodo de fuera que un veredicto declara su dueno) va de CUBIERTO con "
    "la perdida NOMBRADA, que es la vara del D6 del acta 51."
)


def acto(orden, miembros, superviviente, absorbidos, mixto, motivo, pasos, condiciones, nota):
    return {
        "orden": orden,
        "miembros": [superviviente] + list(absorbidos),
        "miembros_del_acto_entero": list(miembros),
        "mixto_que_queda_fuera": mixto,
        "superviviente": superviviente,
        "motivo": motivo,
        "absorbidos": list(absorbidos),
        "pasos": pasos,
        "condiciones": condiciones,
        "nota_del_reparto": nota,
    }


# =============================================================================
# LOTE A: los actos 7, 8, 9 y 11 de la nomina del cierre de la vuelta 52
# =============================================================================
A7 = acto(
    1,
    ["customer_profile", "customer_profile_value_map", "value_proposition_canvas"],
    "value_proposition_canvas",
    ["customer_profile_value_map"],
    "customer_profile",
    "CONTENIDO, Y LO DECIDE EL ALCANCE DEL ROL MAS EL PADRE DECLARADO, que P.8 nombra como "
    "contenido con el mismo peso que los pasos. Los dos viables medidos hoy son "
    "value_proposition_canvas y customer_profile; customer_profile_value_map es el CENTRO de la "
    "estrella y no es viable porque no deja ningun mixto fuera. Entre los dos viables el conteo "
    "apunta a customer_profile (5 pasos contra 4, 2 condiciones contra 1) Y EL CONTENIDO APUNTA AL "
    "OTRO, asi que el conteo no manda: el puesto 705, que es el veredicto DIRECTO del par mixto, "
    "escribe el alcance de cada uno sin rodeos, value_proposition_canvas es EL INSTRUMENTO ENTERO "
    "en cuatro instrucciones de montaje y customer_profile es EL CIRCULO DE LA DERECHA trabajado a "
    "fondo, o sea el continente y UNA DE SUS DOS MITADES. Y el puesto 477 declara al que muere "
    "SEGUNDA VERSION DEL CENTRO SIN CASA y a value_proposition_canvas EL CENTRO DE LA FAMILIA, "
    "verificado por el grafo en la propia razon: el centro enlaza con las TRES piezas que nombra y "
    "el gemelo no enlaza con ninguna. Una cabeza que vale para las dos mitades no puede llamarse "
    "como una sola (P.8, alcance del rol): sobrevive el continente. NINGUN VEREDICTO A DEL ACTO "
    "ESCRIBE LA FORMULA Sobrevive X, asi que aqui no hay choque de letra contra aritmetica.",
    {"customer_profile_value_map": {
        "1": "INCISO:2|los jobs, pains y gains del cliente|, especificando en él ",
        "2": "INCISO:3|cómo tu producto/servicio alivia pains y crea gains|, documentando en él ",
        "3": "APPEND",
        "4": "APPEND",
    }},
    {"customer_profile_value_map": {"1": "CUBIERTO:1", "2": "APPEND"}},
    "EL PUESTO 475 ESCRIBE LA LISTA DE LO QUE HAY QUE SALVAR Y AQUI SE SALVA PIEZA A PIEZA: dice "
    "que el paso 1 del que muere es customer_profile ENTERO y su paso 2 es value_map ENTERO, y que "
    "LO UNICO PROPIO QUE ANADE es comunicar los documentos a la organizacion y usarlos como "
    "marcador. Las DOS piezas propias viajan ENTERAS de APPEND, que es lo que la razon pide. Las "
    "otras dos van de INCISO y no de CUBIERTO, y el motivo se dice: los pasos 2 y 3 del "
    "superviviente mandan DIBUJAR el circulo del perfil y el cuadrado del mapa de valor, y no "
    "dicen QUE SE ESCRIBE DENTRO; el que muere si lo dice, y eso es un PARAMETRO CONCRETO de un "
    "gesto que el superviviente ya tiene. Los dos pasos resultantes se leen limpios. NOTA SOBRE "
    "LOS DOS NODOS VIVOS QUE LA RAZON NOMBRA, dicha en vez de callada: customer_profile es el "
    "MIXTO de este acto y SOBREVIVE, y value_map es un nodo vivo de fuera del acto; los incisos no "
    "los duplican, porque lo que adosan es el CONTENIDO del circulo y del cuadrado dentro de la "
    "instruccion de montaje, no el procedimiento entero de cada mitad. CERO PERDIDAS NOMBRADAS en "
    "este acto. Su condicion 1 esta CUBIERTA por la condicion 1 del superviviente (las dos dicen "
    "cuando se inicia el diseno de una propuesta de valor) y la 2 viaja entera porque habla de "
    "otra cosa, el entendimiento compartido del equipo.",
)

A8 = acto(
    2,
    ["asignacion_persona_ia", "ingenieria_de_prompts_efectiva", "prompting_por_persona_ia"],
    "ingenieria_de_prompts_efectiva",
    ["asignacion_persona_ia"],
    "prompting_por_persona_ia",
    "CONTENIDO, Y LO DECIDE EL PADRE DECLARADO, que P.8 nombra como contenido con el mismo peso "
    "que los pasos. Los dos viables medidos hoy son ingenieria_de_prompts_efectiva y "
    "prompting_por_persona_ia; asignacion_persona_ia es el CENTRO y no es viable porque no deja "
    "ningun mixto fuera. Entre los dos viables LAS DOS VARAS DE CONTEO EMPATAN (4 pasos cada uno, "
    "2 condiciones cada uno) y el cableado apunta a prompting_por_persona_ia (3 contra 2), pero el "
    "cableado NO LLEGA A HABLAR porque el contenido no calla: el puesto 1144, que es el veredicto "
    "DIRECTO del par mixto, declara la jerarquia con todas las letras, ingenieria_de_prompts_"
    "efectiva es LA ANATOMIA DEL PROMPT y dice en su paso 1, EN UNA LINEA, definir que tipo de "
    "persona debe adoptar la maquina; prompting_por_persona_ia TRAE EL PROCEDIMIENTO DE ESA LINEA. "
    "Madre e hija, y el puesto 1175 lo repite: el centro que muere es LA UNION DE UNA MADRE Y DE "
    "SU HIJA y NO TIENE NADA QUE SEA SUYO. La madre absorbe al centro y la hija se queda fuera "
    "como mixto, que es la unica direccion que no invierte la jerarquia que el archivo declaro. "
    "NINGUN VEREDICTO A DEL ACTO ESCRIBE LA FORMULA Sobrevive X, asi que aqui no hay choque de "
    "letra contra aritmetica.",
    {"asignacion_persona_ia": {
        "1": "INCISO:1|(ej. 'actúa como director de marketing de una startup B2B')| ",
        "2": "CUBIERTO:2",
        "3": "INCISO:4|refinando el output paso a paso en vez de pedir la respuesta final de una sola vez|, y en modo conversación, ",
        "4": "CUBIERTO:1",
    }},
    {"asignacion_persona_ia": {"1": "CUBIERTO:1", "2": "CUBIERTO:2"}},
    "EL PUESTO 1175 ESCRIBE LA LISTA DE LO QUE HAY QUE SALVAR Y AQUI SE SALVA PIEZA A PIEZA, con "
    "la verificacion que la propia razon ya trae hecha. Su paso 2, dar contexto y restricciones "
    "claras, la razon dice que SOBREVIVE VERBATIM en los pasos 2 y 3 del superviviente "
    "(CUBIERTO:2, y la mitad de las restricciones vive en el paso 3). Su paso 1 es el paso 1 del "
    "superviviente con un EJEMPLO encima, y el ejemplo es un parametro concreto del gesto que ya "
    "existe: va de INCISO ADOSADO y el paso resultante se lee limpio. Su paso 3 NO sobrevive "
    "verbatim y la razon lo dice con precision, aquella itera EL PROMPT y esta itera LA "
    "CONVERSACION: va de INCISO ADOSADO al paso 4 para que la conversacion no se pierda, que es la "
    "figura de la SALVAGUARDA de la tabla de los seis motivos. PERDIDA NOMBRADA, UNA: su paso 4, "
    "probar multiples personas para la misma tarea y comparar la calidad de las respuestas, se "
    "marca CUBIERTO:1 Y SE DECLARA LO QUE SE PIERDE, la COMPARACION entre varias personas. NO "
    "viaja de APPEND, y el motivo es la vara del D6 del acta 51: la linea vive ENTERA en un vecino "
    "VIVO, el paso 2 de prompting_por_persona_ia, que es el MIXTO de este acto y SOBREVIVE; y "
    "ademas el puesto 1144 declara ese paso PROCEDIMIENTO PROPIO DE LA HIJA, asi que meterlo en la "
    "madre seria re-fundir por la ventana lo que el archivo separo por la puerta. Sus DOS "
    "condiciones estan CUBIERTAS por las dos del superviviente, comprobado texto contra texto: "
    "respuestas genericas contra respuestas genericas o poco utiles, y brainstorming o generacion "
    "de contenido contra analisis, redaccion o ideacion de negocio.",
)

A9 = acto(
    3,
    ["warrant_pricing_venture_debt", "warrants_deuda_convertible", "warrants_financiamiento"],
    "warrant_pricing_venture_debt",
    ["warrants_deuda_convertible"],
    "warrants_financiamiento",
    "CONTENIDO, Y LO DECIDE EL ALCANCE DEL ROL, con la vara de conteo que no empata apuntando al "
    "otro lado y por eso VA MARCADO. Los dos viables medidos hoy son warrant_pricing_venture_debt "
    "y warrants_financiamiento; warrants_deuda_convertible es el CENTRO y no es viable porque no "
    "deja ningun mixto fuera. Entre los dos viables los PASOS EMPATAN (4 y 4) y las CONDICIONES "
    "APUNTAN A warrants_financiamiento (2 contra 1); el cableado apunta a "
    "warrant_pricing_venture_debt (5 contra 4). EL CONTENIDO NO CALLA Y POR ESO DECIDE: el puesto "
    "1448, veredicto DIRECTO del par mixto, escribe el alcance de cada uno, "
    "warrant_pricing_venture_debt TRABAJA LA MECANICA DEL PRECIO y warrants_financiamiento TRABAJA "
    "LA DECISION DE ACEPTAR. Y lo que decide es DE QUIEN ES EL MATERIAL DEL QUE MUERE: el puesto "
    "1028 dice que lo comun entre el centro y warrant_pricing_venture_debt es EL INSTRUMENTO "
    "ENTERO, definir que porcentaje cubren los warrants, decidir el precio de ejercicio y sobre "
    "que clase de accion se ejercen; y el entregable del centro es LOS TERMINOS DE LOS WARRANTS YA "
    "DEFINIDOS, porcentaje de cobertura, precio de ejercicio, plazo y que pasa en caso de fusion. "
    "Ese material es la MECANICA DEL PRECIO, no la DECISION DE ACEPTAR. NINGUN VEREDICTO A DEL "
    "ACTO ESCRIBE LA FORMULA Sobrevive X, asi que aqui no hay choque de letra contra aritmetica.",
    {"warrants_deuda_convertible": {
        "1": "APPEND",
        "2": "CUBIERTO:1",
        "3": "CUBIERTO:4",
        "4": "APPEND",
        "5": "APPEND",
    }},
    {"warrants_deuda_convertible": {"1": "APPEND", "2": "APPEND"}},
    "EL PUESTO 1028 ESCRIBE LA LISTA DE LO QUE HAY QUE SALVAR Y AQUI SE SALVA PIEZA A PIEZA: dice "
    "que lo propio de warrants_deuda_convertible son TRES, evaluar si conviene el warrant en vez "
    "de un descuento simple, fijar el plazo de ejercicio entre cinco y diez anos y que pasa si el "
    "negocio se fusiona, y pedir que el pago quede separado para evitar el problema contable del "
    "descuento de emision original. LAS TRES VIAJAN ENTERAS DE APPEND y ninguna se pierde. Las "
    "otras dos estan CUBIERTAS y la razon ya las declaraba comunes: su paso 2, definir que "
    "porcentaje del monto cubren los warrants, es el paso 1 del superviviente, revisar como "
    "aparece la cobertura en el documento de terminos, si como porcentaje del prestamo o de otra "
    "forma (CUBIERTO:1); y su paso 3, decidir el precio de ejercicio y si va sobre comunes o "
    "preferentes, vive PARTIDO EN DOS pasos del superviviente, el 4 negocia el precio de ejercicio "
    "y el 3 negocia sobre que tipo de accion se ejerce, y se marca CUBIERTO:4 por el grueso de la "
    "linea con la otra mitad dicha aqui. CERO PERDIDAS NOMBRADAS en este acto. Sus DOS condiciones "
    "viajan enteras porque hablan de otra cosa que la unica del superviviente: aquella es evaluar "
    "deuda de riesgo como complemento del capital ya levantado, y estas son que el prestamista "
    "insista en warrants en lugar de descuento y que se este levantando deuda convertible en una "
    "etapa mas avanzada.",
)

A11 = acto(
    4,
    ["definir_limites_huella_carbono", "huella_carbono_empresarial", "medir_huella_carbono_corporativa"],
    "medir_huella_carbono_corporativa",
    ["huella_carbono_empresarial"],
    "definir_limites_huella_carbono",
    "CONTENIDO, Y LAS TRES VARAS APUNTAN AL MISMO LADO SIN UNA SOLA EN CONTRA. Los dos viables "
    "medidos hoy son medir_huella_carbono_corporativa y definir_limites_huella_carbono; "
    "huella_carbono_empresarial es el CENTRO y no es viable porque no deja ningun mixto fuera. "
    "Entre los dos viables: PASOS 5 contra 4, CONDICIONES 3 contra 2 y CABLEADO 4 contra 3, los "
    "tres a favor de medir_huella_carbono_corporativa, que ademas es el unico de los tres que "
    "lleva alias (evaluar_huella_carbono). Y EL ALCANCE DEL ROL dice lo mismo: el entregable del "
    "centro que muere es un REPORTE DE HUELLA DE CARBONO con las emisiones de alcance 1, 2 y 3 "
    "cuantificadas en CO2 equivalente, que es un INVENTARIO COMPLETO, y ese es el entregable de "
    "medir_huella_carbono_corporativa, no el de definir_limites_huella_carbono, que entrega un "
    "DOCUMENTO DE LIMITES. NINGUN VEREDICTO A DEL ACTO ESCRIBE LA FORMULA Sobrevive X, asi que "
    "aqui no hay choque de letra contra aritmetica.",
    {"huella_carbono_empresarial": {
        "1": "INCISO:1|(qué divisiones, filiales o franquicias incluir)| Define el límite organizacional ",
        "2": "CUBIERTO:2",
        "3": "CUBIERTO:3",
        "4": "APPEND",
        "5": "APPEND",
        "6": "CUBIERTO:4",
    }},
    {"huella_carbono_empresarial": {"1": "CUBIERTO:2", "2": "APPEND", "3": "APPEND"}},
    "EL PUESTO 1805 ESCRIBE LA LISTA DE LO QUE HAY QUE SALVAR Y AQUI SE SALVA PIEZA A PIEZA: dice "
    "que de huella_carbono_empresarial se perderian TRES, el LIMITE ORGANIZACIONAL (que "
    "divisiones, filiales o franquicias se incluyen), CONVERTIR TODOS LOS GASES A DIOXIDO DE "
    "CARBONO EQUIVALENTE con los factores de potencial de calentamiento, y ESTABLECER UN ANO BASE "
    "y un periodo de medicion. LAS TRES SE SALVAN: las dos ultimas viajan ENTERAS de APPEND, y la "
    "primera va de INCISO ADOSADO al paso 1 del superviviente, identificar todas las fuentes de "
    "emision, porque el limite organizacional es un PARAMETRO CONCRETO de ese gesto (dice HASTA "
    "DONDE llega la operacion que se identifica) y el paso resultante se lee limpio. Las otras "
    "tres estaban ya declaradas comunes por la misma razon: su paso 2, el limite operacional por "
    "alcances, es el paso 2 del superviviente, clasificar cada emision segun los tres alcances "
    "(CUBIERTO:2); su paso 3, recolectar datos de consumo, es el paso 3 (CUBIERTO:3); y su paso 6, "
    "aplicar el estandar del protocolo de gases de efecto invernadero, es el paso 4, usar "
    "metodologias estandarizadas como las del mismo protocolo (CUBIERTO:4). CERO PERDIDAS "
    "NOMBRADAS en este acto. De sus tres condiciones, la primera esta CUBIERTA por la condicion 2 "
    "del superviviente (las dos hablan de cumplir requisitos de divulgacion o reportar), y las "
    "otras dos viajan enteras porque hablan de cosas que el superviviente no dice, el ahorro "
    "energetico y las metas de neutralidad de carbono.",
)

# =============================================================================
# LOTE B: los actos 13, 14, 15 y 17
# =============================================================================
B13 = acto(
    1,
    ["cinco_categorias_costos_franquicia", "costos_preparacion_franquicia", "estimacion_inversion_inicial_franquiciador"],
    "estimacion_inversion_inicial_franquiciador",
    ["cinco_categorias_costos_franquicia"],
    "costos_preparacion_franquicia",
    "CONTENIDO, Y LO DECIDE EL ALCANCE DEL ROL con los pasos de acuerdo. Los dos viables medidos "
    "hoy son estimacion_inversion_inicial_franquiciador y costos_preparacion_franquicia; "
    "cinco_categorias_costos_franquicia es el CENTRO y no es viable porque no deja ningun mixto "
    "fuera. Entre los dos viables: PASOS 5 contra 4 a favor de estimacion, CONDICIONES EMPATADAS "
    "(2 y 2) y CABLEADO 3 contra 2 a favor de costos_preparacion. EL CONTENIDO NO CALLA Y POR ESO "
    "EL CABLEADO NO LLEGA A HABLAR: el centro que muere es EL PRESUPUESTO ENTERO DE LAS CINCO "
    "CATEGORIAS y su entregable lo dice, un presupuesto detallado Y SUMADO del programa de "
    "franquicia dividido en las cinco categorias. El entregable de estimacion_inversion_inicial_"
    "franquiciador es UN PRESUPUESTO DETALLADO DE LA INVERSION INICIAL para lanzar el sistema, y "
    "su paso 5 es DEFINIR EL CAPITAL TOTAL antes de lanzar; el de costos_preparacion_franquicia es "
    "UNA LISTA DE COSTOS DE PREPARACION, que es UNA de las cinco categorias, la que el propio "
    "centro presupuesta en su paso 6. Una cabeza que vale para las cinco categorias no puede "
    "llamarse como una sola (P.8, alcance del rol). NINGUN VEREDICTO A DEL ACTO ESCRIBE LA FORMULA "
    "Sobrevive X, asi que aqui no hay choque de letra contra aritmetica.",
    {"cinco_categorias_costos_franquicia": {
        "1": "APPEND",
        "2": "CUBIERTO:3",
        "3": "CUBIERTO:2",
        "4": "CUBIERTO:4",
        "5": "APPEND",
        "6": "APPEND",
        "7": "CUBIERTO:5",
    }},
    {"cinco_categorias_costos_franquicia": {"1": "CUBIERTO:2"}},
    "EL PUESTO 2074 ESCRIBE EL MAPA AL REVES Y AQUI SE USA EN SU SENTIDO: dice que CUATRO Y MEDIO "
    "de los cinco pasos del superviviente viven dentro del centro, y nombra la correspondencia una "
    "por una, asi que las mismas lineas leidas del lado del centro estan CUBIERTAS. Su paso 2, "
    "presupuestar los costos de desarrollo con el documento de divulgacion, el contrato y EL "
    "MANUAL DE OPERACIONES, es el paso 3 del superviviente, presupuestar el desarrollo del manual "
    "de operaciones y los materiales de entrenamiento (CUBIERTO:3); su paso 3, los costos legales, "
    "es el paso 2, cotizar el costo de armar los documentos legales (CUBIERTO:2); su paso 4, el "
    "marketing para atraer compradores de franquicia, es el paso 4 (CUBIERTO:4); y su paso 7, "
    "sumar todo en un solo presupuesto antes de arrancar, es el paso 5, definir el capital total "
    "antes de lanzar (CUBIERTO:5). Y EL PUESTO 2074 ESCRIBE ADEMAS LAS TRES COSAS PROPIAS DEL "
    "CENTRO, que son las que hay que salvar: CUANTAS FRANQUICIAS SE QUIEREN VENDER EL PRIMER ANO, "
    "que es lo que dimensiona todo el presupuesto; LA CATEGORIA DE PERSONAL; y PREGUNTAR EL PRECIO "
    "PROMEDIO POR FRANQUICIA VENDIDA EN EL MERCADO. Las dos primeras viajan ENTERAS de APPEND (sus "
    "pasos 1 y 5) y la tercera viaja dentro del paso 6 que tambien va de APPEND, los costos de "
    "preparacion, junto con la nueva entidad legal, duplicar materiales y viajes y equipo nuevo. "
    "SE DICE LO QUE ESO ULTIMO SIGNIFICA EN VEZ DE CALLARLO: el paso 6 del centro es la categoria "
    "que el MIXTO desarrolla entera, y el puesto 2092 declara que las dos categorias NO SE PISAN, "
    "asi que el APPEND mete en el superviviente el RENGLON de la categoria y no su procedimiento, "
    "que sigue vivo y entero en costos_preparacion_franquicia. El puesto 2074 ya lo habia escrito "
    "de la otra forma: en el centro la entidad es UN RENGLON DE UNA LISTA y en el mixto es UNA "
    "DECISION. CERO PERDIDAS NOMBRADAS. Su unica condicion esta CUBIERTA por la condicion 2 del "
    "superviviente, las dos dicen cuando hay que planificar el capital que se va a necesitar para "
    "franquiciar.",
)

B14 = acto(
    2,
    ["contratar_abogado_especializado_franquicias", "contratar_abogado_franquicias", "eleccion_abogado_franquicias"],
    "eleccion_abogado_franquicias",
    ["contratar_abogado_especializado_franquicias"],
    "contratar_abogado_franquicias",
    "CONTENIDO, Y LO DECIDE EL CONTEO DE PASOS CON EL ALCANCE DEL ROL DE ACUERDO, con el material "
    "propio apuntando al otro lado y por eso VA MARCADO. Los dos viables medidos hoy son "
    "eleccion_abogado_franquicias y contratar_abogado_franquicias; "
    "contratar_abogado_especializado_franquicias es el CENTRO (aqui el nodo CORTO contenido en los "
    "dos largos, la estrella INVERTIDA que el puesto 2090 nombra) y no es viable porque no deja "
    "ningun mixto fuera. Entre los dos viables: PASOS 6 contra 5 a favor de eleccion, CONDICIONES "
    "EMPATADAS (2 y 2), CABLEADO 5 contra 4 a favor de eleccion, y eleccion es ademas el unico de "
    "los tres con alias (contratacion_abogado_franquicia). EN CONTRA: el puesto 2086 declara "
    "CUATRO cosas propias de contratar_abogado_franquicias y TRES de eleccion_abogado_franquicias, "
    "y esa vara apunta al otro lado. LO QUE DESEMPATA ES EL ALCANCE DEL ROL: el entregable del "
    "centro que muere es un contrato firmado CON EL PLAN DE NEGOCIO COMPLETO ENTREGADO "
    "PREVIAMENTE, y esa condicion previa es el paso 1 de eleccion_abogado_franquicias (confirmar "
    "primero con el consultor que franquiciar es la estrategia correcta), que "
    "contratar_abogado_franquicias no tiene. NINGUN VEREDICTO A DEL ACTO ESCRIBE LA FORMULA "
    "Sobrevive X, asi que aqui no hay choque de letra contra aritmetica.",
    {"contratar_abogado_especializado_franquicias": {
        "1": "CUBIERTO:1",
        "2": "CUBIERTO:2",
        "3": "CUBIERTO:2",
        "4": "CUBIERTO:2",
    }},
    {"contratar_abogado_especializado_franquicias": {"1": "CUBIERTO:1", "2": "APPEND"}},
    "EL PUESTO 2076 ESCRIBE LA CORRESPONDENCIA UNA POR UNA Y AQUI SE EJECUTA TAL CUAL: su paso 1, "
    "completar la planificacion de negocio antes de buscar asesoria legal, ES EL PASO 1 DEL "
    "SUPERVIVIENTE, confirmar primero con el consultor que franquiciar es la estrategia correcta "
    "(CUBIERTO:1); su paso 2, verificar la experiencia real en franquicias y no la general, esta "
    "en los pasos 2 y 6 del superviviente y se marca por el grueso (CUBIERTO:2); y su paso 4, "
    "confirmar que se dedica activamente a la practica privada de franquicias, es TAMBIEN el paso "
    "2 (CUBIERTO:2). PERDIDA NOMBRADA, UNA, Y ES LA QUE EL PROPIO PUESTO 2076 ANUNCIA: su paso 3, "
    "SOLICITAR REFERENCIAS DE OTROS FRANQUICIANTES que hayan trabajado con el abogado, es LO UNICO "
    "QUE QUEDA FUERA del superviviente. Se marca CUBIERTO:2 Y SE DECLARA LO QUE SE PIERDE, LAS "
    "REFERENCIAS. NO viaja de APPEND, y el motivo es la vara del D6 del acta 51 mas la del D5 del "
    "acta 52: la linea vive ENTERA en un vecino VIVO, el paso 1 de contratar_abogado_franquicias "
    "(buscar referencias en consultoras de franquicia y en otros franquiciadores), que es el MIXTO "
    "de este acto y SOBREVIVE; y el puesto 2086, que es el veredicto DIRECTO del par mixto, la "
    "declara EXPRESAMENTE una de las CUATRO cosas propias de ese nodo. Meterla en el superviviente "
    "seria vaciar por la ventana lo que el D declara propio del otro. De sus dos condiciones, la "
    "primera esta CUBIERTA (su primera mitad, el plan de negocio terminado, es la condicion 1 del "
    "superviviente, y su segunda mitad, que se necesita documentacion legal, es la condicion 2, "
    "antes de elaborar el documento de divulgacion o los contratos) y la segunda viaja entera "
    "porque es la unica del acto que nombra el error a evitar, contratar al primer abogado "
    "disponible sin verificar su experiencia.",
)

B15 = acto(
    3,
    ["deteccion_franquicia_inadvertida", "estructuras_combinadas_franquicia", "prevenir_franquicias_inadvertidas"],
    "prevenir_franquicias_inadvertidas",
    ["estructuras_combinadas_franquicia"],
    "deteccion_franquicia_inadvertida",
    "CONTENIDO, Y TRES VARAS APUNTAN AL MISMO LADO CON LA CUARTA EMPATADA. Los dos viables medidos "
    "hoy son prevenir_franquicias_inadvertidas y deteccion_franquicia_inadvertida; "
    "estructuras_combinadas_franquicia es el CENTRO y no es viable porque no deja ningun mixto "
    "fuera; ademas los puestos 2181 y 2207 lo declaran DOS VECES sin nada propio, sus tres pasos "
    "NO TRAEN NADA SUYO y lo unico propio es EL MOMENTO, y eso CABE EN UNA LINEA. Entre los dos "
    "viables: PASOS EMPATADOS (4 y 4), CONDICIONES 2 contra 1, CABLEADO 3 contra 1 y MATERIAL "
    "PROPIO 3 contra 2, los tres desempates a favor de prevenir_franquicias_inadvertidas. El "
    "material propio lo cuenta el puesto 2073, que es el veredicto DIRECTO del par mixto: "
    "prevenir_franquicias_inadvertidas TRAE LA LETRA (nombra los tres elementos legales, verifica "
    "los umbrales de tarifa y las definiciones estado por estado, y documenta la naturaleza de "
    "cada relacion) y deteccion_franquicia_inadvertida TRAE EL TIEMPO (llamarle licencia no libra, "
    "y auditar cada cierto tiempo). LOS DOS VEREDICTOS A DEL ACTO NOMBRAN SUPERVIVIENTE Y LOS DOS "
    "NOMBRAN A UN VIABLE, cada uno al suyo (2181 nombra deteccion_franquicia_inadvertida y 2207 "
    "nombra prevenir_franquicias_inadvertidas), asi que NO HAY CHOQUE de letra contra estructura: "
    "los dos coinciden en que el que muere es el centro, y el desempate entre los dos viables lo "
    "hace el contenido.",
    {"estructuras_combinadas_franquicia": {
        "1": "INCISO:1|cada estructura de negocio diseñada|, y aplica la misma prueba a ",
        "2": "CUBIERTO:1",
        "3": "CUBIERTO:2",
    }},
    {"estructuras_combinadas_franquicia": {"1": "APPEND", "2": "APPEND"}},
    "EL PUESTO 2181 ESCRIBE LA RECETA DEL REPARTO Y AQUI SE EJECUTA AL PIE: dice que lo unico "
    "propio del centro es EL MOMENTO, aplicarlo a una estructura que aun estas disenando en vez de "
    "a una que ya opera, y que ESO CABE EN UNA LINEA y SE ABSORBE COMO UNA LINEA SUYA. Eso es "
    "exactamente un INCISO ADOSADO: su paso 1, aplicar la prueba de tres elementos a cada "
    "estructura de negocio disenada, se adosa al paso 1 del superviviente, que aplica los mismos "
    "elementos legales a los acuerdos EXISTENTES, y el paso resultante se lee limpio y guarda los "
    "dos momentos. Los otros dos estaban ya declarados sin nada propio por el puesto 2207: su paso "
    "2, revisar si se combinan accidentalmente marca, control y tarifa, ES ESA MISMA PRUEBA dicha "
    "de otro modo (CUBIERTO:1); y su paso 3, validar legalmente cada estructura antes de lanzarla, "
    "es el paso 2 del superviviente DICHO IGUAL, consultar a un abogado especializado antes de "
    "estructurar cualquier relacion (CUBIERTO:2). CERO PERDIDAS NOMBRADAS en este acto. Sus DOS "
    "condiciones viajan enteras porque las dos del superviviente hablan de otra cosa: aquellas "
    "hablan de acuerdos ya existentes con terceros que usan la marca y de evitar INTENCIONALMENTE "
    "el nombre de franquicia, y estas hablan del momento de DISENAR una estructura alternativa y "
    "del riesgo de haberla creado INADVERTIDAMENTE, que es justo la diferencia entre lo "
    "intencional y lo inadvertido.",
)

B17 = acto(
    4,
    ["critica_gestion_por_objetivos", "eliminacion_gestion_por_objetivos_y_numeros", "eliminar_metas_numericas_gerencia"],
    "eliminar_metas_numericas_gerencia",
    ["critica_gestion_por_objetivos"],
    "eliminacion_gestion_por_objetivos_y_numeros",
    "CONTENIDO, Y LO DECIDE LA UNICA VARA QUE NO EMPATA, y por eso VA MARCADO. Los dos viables "
    "medidos hoy son eliminar_metas_numericas_gerencia y eliminacion_gestion_por_objetivos_y_"
    "numeros; critica_gestion_por_objetivos es el CENTRO y no es viable porque no deja ningun "
    "mixto fuera. Entre los dos viables casi todo EMPATA: PASOS 4 y 4, CABLEADO 2 y 2, y MATERIAL "
    "PROPIO 2 y 2 contado por el puesto 2534, que es el veredicto DIRECTO del par mixto y escribe "
    "los dos bloques al digito. LA UNICA VARA QUE NO EMPATA SON LAS CONDICIONES, 2 contra 1, a "
    "favor de eliminar_metas_numericas_gerencia, y las condiciones son contenido por la letra del "
    "encargo. SE DICE LO QUE ESTA VARA NO DECIDE, porque seria facil colarlo: LA PERDIDA DE NOMBRE "
    "NO DISCRIMINA AQUI, y el motivo es que los DOS viables sobreviven a este acto (uno como "
    "superviviente y el otro como mixto), asi que la denominacion GESTION POR OBJETIVOS se queda "
    "en el catalogo dentro del titulo de eliminacion_gestion_por_objetivos_y_numeros elija quien "
    "elija. LOS DOS VEREDICTOS A DEL ACTO NOMBRAN SUPERVIVIENTE Y LOS DOS NOMBRAN A UN VIABLE, "
    "cada uno al suyo (2488 nombra eliminacion y 2477 nombra eliminar_metas), asi que NO HAY "
    "CHOQUE de letra contra estructura.",
    {"critica_gestion_por_objetivos": {
        "1": "CUBIERTO:3",
        "2": "CUBIERTO:2",
        "3": "CUBIERTO:4",
        "4": "APPEND",
    }},
    {"critica_gestion_por_objetivos": {"1": "CUBIERTO:2"}},
    "EL PUESTO 2477 ESCRIBE LA CORRESPONDENCIA UNA POR UNA Y AQUI SE EJECUTA TAL CUAL: su paso 1, "
    "evaluar si las metas se basan en la capacidad real, es el paso 3 del superviviente, "
    "DETERMINAR LA CAPACIDAD REAL DEL SISTEMA MEDIANTE ANALISIS ESTADISTICO ANTES DE FIJAR "
    "CUALQUIER META (CUBIERTO:3); su paso 2, eliminar las arbitrarias, es el paso 2 (CUBIERTO:2); "
    "y su paso 3, cambiar el manejo por objetivos por mejora continua, es el paso 4 (CUBIERTO:4). "
    "Y AQUI SE SALVA LO QUE DOS VEREDICTOS DIERON POR PERDIDO, que es el dato de este acto: su "
    "paso 4, RECONOCER EL COSTO OCULTO DE MANEJAR EL NEGOCIO POR MIEDO A LOS NUMEROS, esta "
    "declarado SALVAGUARDA y PERDIDA NOMBRADA por el puesto 2477 y el puesto 2488 dice que NINGUNO "
    "DE LOS DOS SUPERVIVIENTES LO RECOGE. Es un GESTO DISTINTO y no un parametro de nada: VIAJA "
    "ENTERO DE APPEND, y con eso la salvaguarda deja de ser una perdida. CERO PERDIDAS NOMBRADAS "
    "DE PASO en este acto. Su unica condicion esta CUBIERTA por la condicion 2 del superviviente, "
    "las dos dicen lo mismo, que se exigen metas numericas fijas sin base real ni comprension del "
    "proceso. LA PERDIDA DE NOMBRE QUE DOS VEREDICTOS DAN POR SEGURA NO EXISTE, Y SE DICE PORQUE "
    "LA REGLA 9 OBLIGA A RE-VERIFICAR TODA PERDIDA DECLARADA CONTRA EL GRAFO: el puesto 2488 "
    "escribe que el ACRONIMO MBO SOLO APARECE EN EL NODO QUE CAE, y el puesto 2477 escribe que "
    "el superviviente NO NOMBRA EL MBO EN NINGUN SITIO. Medido HOY sobre los 3.489 nodos vivos, "
    "campo por campo (docs/loop/SALIDA_V53_MBO.txt), EL ACRONIMO VIVE EN DOS NODOS y no en uno: "
    "critica_gestion_por_objetivos, que muere aqui, Y eliminacion_gestion_por_objetivos_y_numeros, "
    "que es el MIXTO de este acto y SOBREVIVE, en su resumen teorico (LA GESTION POR OBJETIVOS "
    "(MBO) Y POR NUMEROS IGNORA LA VARIACION NATURAL DEL SISTEMA). Es la clase VIVE DENTRO de "
    "P.13: la perdida era real contra aquel par y es FALSA contra esta nomina. Se declara la "
    "discrepancia en vez de resolverla copiando, que es lo que manda la regla 2 del EJECUTOR; las "
    "dos razones viejas NO se tocan. La denominacion en castellano GESTION POR OBJETIVOS vive "
    "ademas en un tercer nodo vivo, cuestionario_autoevaluacion_gerencial_calidad.",
)

# =============================================================================
# LOTE C: los actos 19, 20, 21 y 6
# =============================================================================
C19 = acto(
    1,
    ["analisis_pareto", "analisis_pareto_de_proveedores", "principio_pareto"],
    "analisis_pareto_de_proveedores",
    ["analisis_pareto"],
    "principio_pareto",
    "CONTENIDO, Y LAS TRES VARAS DE CONTENIDO APUNTAN AL MISMO LADO, con el cableado en contra y "
    "un CHOQUE DE LETRA CONTRA ARITMETICA que se registra. Los dos viables medidos hoy son "
    "analisis_pareto_de_proveedores y principio_pareto; analisis_pareto es el CENTRO y NO ES "
    "VIABLE porque no deja ningun mixto fuera. Entre los dos viables: PASOS 5 contra 3, "
    "CONDICIONES 2 contra 1 y MATERIAL PROPIO 2 contra 1 contado por el puesto 3087, que es el "
    "veredicto DIRECTO del par mixto (analisis_pareto_de_proveedores trae LA SEGMENTACION POR "
    "PROVEEDOR, PARTE O PROCESO y REPETIR POR DIFERENTES DIMENSIONES, dos pasos enteros propios; "
    "principio_pareto trae PRIORIZAR PROYECTOS, uno). El cableado apunta al otro (4 contra 2) y NO "
    "LLEGA A HABLAR porque el contenido no calla. CHOQUE DE LETRA CONTRA ARITMETICA, REGISTRADO "
    "CON SUS PUESTOS: los veredictos 2546 y 2551 escriben SOBREVIVE ANALISIS_PARETO, y "
    "analisis_pareto no es viable por la estructura del acto. MANDA LA ARITMETICA, que es la "
    "adjudicacion 3 del acta de la vuelta 50: P.12 es regla y la formula Sobrevive X es el cierre "
    "de una razon de PAR. Y SE DICE LO QUE ESTE CHOQUE TIENE DE NUEVO, en vez de colarlo con los "
    "cinco anteriores: en aquellos cinco el nodo nombrado SEGUIA VIVO como mixto, y aqui MUERE, "
    "porque es el centro de la estrella. Va marcado en el reporte.",
    {"analisis_pareto": {
        "1": "INCISO:1|calcular el gran total| y ",
        "2": "APPEND",
        "3": "APPEND",
        "4": "INCISO:3|el punto de quiebre en la curva|, analizando ",
        "5": "APPEND",
        "6": "CUBIERTO:4",
    }},
    {"analisis_pareto": {"1": "CUBIERTO:2", "2": "APPEND", "3": "APPEND"}},
    "EL PUESTO 2546 ESCRIBE LA LISTA DE LO QUE HAY QUE SALVAR Y AQUI SE SALVA PIEZA A PIEZA, Y ES "
    "LA LISTA DEL LADO QUE MUERE: dice que analisis_pareto trae LA CONSTRUCCION Y EL CRITERIO DE "
    "CORTE, dibujar los ejes CON BARRAS DE MAGNITUD Y LINEA DE PORCENTAJE ACUMULADO y ANALIZAR EL "
    "PUNTO DE QUIEBRE DE LA CURVA, que es lo unico del par que dice DONDE CORTAR en vez de repetir "
    "el 80/20 como si fuera una ley. LAS DOS SE SALVAN: la construccion viaja ENTERA de APPEND "
    "(sus pasos 2 y 3, reordenar de mayor a menor con el porcentaje acumulado, y dibujar los ejes) "
    "y el punto de quiebre va de INCISO ADOSADO al paso 3 del superviviente, identificar los pocos "
    "proveedores o partes que concentran la mayoria de los problemas, porque el punto de quiebre "
    "es el CRITERIO CONCRETO de ese mismo gesto y el paso resultante se lee limpio. Su paso 5, "
    "REPETIR EL ANALISIS SOBRE LAS SUBCATEGORIAS, viaja ENTERO de APPEND aunque el superviviente "
    "ya tenga un paso de repetir, y el motivo lo escribe el propio 2546: los dos repiten DE FORMAS "
    "OPUESTAS, el que muere BAJA sobre las subcategorias del problema principal y el superviviente "
    "RECORTA por otras dimensiones (costo, modo de falla), BAJAR Y RECORTAR ENCUENTRAN COSAS "
    "DISTINTAS Y LA FUSION SE QUEDA CON LAS DOS. Su paso 1 va de INCISO porque el superviviente ya "
    "manda recopilar los datos y lo unico que anade es CALCULAR EL GRAN TOTAL. Su paso 6, enfocar "
    "los recursos en los pocos vitales, es el paso 4 del superviviente dicho igual (CUBIERTO:4). "
    "CERO PERDIDAS NOMBRADAS DE PASO. De sus tres condiciones, la primera esta CUBIERTA por la "
    "condicion 2 del superviviente (priorizar recursos limitados de mejora) y las otras dos viajan "
    "enteras. LO QUE SI SE PIERDE Y VA DECLARADO CON NOMBRE ES UNA PERDIDA DE NOMBRE: el nodo que "
    "muere se titula ANALISIS DE PARETO a secas, que es el nombre general del instrumento, y el "
    "superviviente se titula ANALISIS DE PARETO APLICADO A PROVEEDORES. Medido hoy contra el grafo "
    "entero (docs/loop/SALIDA_V53_PARETO.txt), la palabra PARETO sigue viva en CINCO titulos de nodos vivos, y al morir analisis_pareto quedan CUATRO, "
    "entre ellos el del MIXTO que sobrevive, APLICACION DEL PRINCIPIO DE PARETO EN SELECCION DE "
    "PROYECTOS, asi que lo que se pierde no es la palabra sino EL TITULO GENERAL SIN ADJETIVO. "
    "Esta operacion NO redacta titulos: queda DECLARADO para el auditor.",
)

C20 = acto(
    2,
    ["error_proofing_servicio", "mistake_proofing_poka_yoke_2", "poka_yoke_a_prueba_de_errores"],
    "error_proofing_servicio",
    ["mistake_proofing_poka_yoke_2"],
    "poka_yoke_a_prueba_de_errores",
    "CONTENIDO, Y LAS TRES VARAS QUE NO EMPATAN APUNTAN AL MISMO LADO, con un CHOQUE DE LETRA "
    "CONTRA ARITMETICA que se registra. Los dos viables medidos hoy son error_proofing_servicio y "
    "poka_yoke_a_prueba_de_errores; mistake_proofing_poka_yoke_2 es el CENTRO y NO ES VIABLE "
    "porque no deja ningun mixto fuera. Entre los dos viables: PASOS 6 contra 4, CABLEADO 4 contra "
    "1 y MATERIAL PROPIO 3 contra 2 contado por el puesto 2931, que es el veredicto DIRECTO del "
    "par mixto (error_proofing_servicio trae evaluar si la actividad se elimina, buscar sustitutos "
    "mas confiables y DISENAR MECANISMOS PARA MINIMIZAR EL IMPACTO CUANDO EL ERROR YA OCURRIO; "
    "poka_yoke_a_prueba_de_errores trae probarlo en condiciones reales y estandarizarlo). Las "
    "CONDICIONES EMPATAN (2 y 2). CHOQUE DE LETRA CONTRA ARITMETICA, REGISTRADO CON SU PUESTO: el "
    "veredicto 2613 escribe SOBREVIVE MISTAKE_PROOFING_POKA_YOKE_2, y ese nodo no es viable por la "
    "estructura del acto. MANDA LA ARITMETICA (adjudicacion 3 del acta de la vuelta 50), y otra "
    "vez con la novedad de que el nombrado MUERE en vez de quedar vivo como mixto. Va marcado en "
    "el reporte.",
    {"mistake_proofing_poka_yoke_2": {
        "1": "INCISO:1|o producto| ",
        "2": "APPEND",
        "3": "APPEND",
        "4": "APPEND",
        "5": "APPEND",
    }},
    {"mistake_proofing_poka_yoke_2": {"1": "CUBIERTO:1", "2": "APPEND", "3": "APPEND"}},
    "EL PUESTO 2613 ESCRIBE LO QUE EL CENTRO TRAE DE MAS Y AQUI SE SALVA ENTERO: LA CLASIFICACION "
    "POR LOS CINCO PRINCIPIOS (eliminacion, reemplazo, facilitacion, deteccion, mitigacion) y la "
    "GUARDA de priorizar la prevencion proactiva en el diseno por encima de la mitigacion "
    "reactiva. LAS DOS VIAJAN ENTERAS DE APPEND (sus pasos 2 y 4), y con eso el superviviente pasa "
    "a NOMBRAR los cinco principios que hasta hoy solo EJECUTABA sin nombrar, que es exactamente "
    "lo que el puesto 2737 describe cuando dice que los pasos de error_proofing_servicio SON los "
    "cinco principios que el otro enumera. Su paso 3, disenar dispositivos fisicos o logicos que "
    "hagan imposible o detectable el error, viaja ENTERO de APPEND porque el superviviente no "
    "tiene ningun paso de DISENO DEL DISPOSITIVO y el puesto 2931 no lo cuenta entre lo propio del "
    "mixto. Su paso 1 va de INCISO porque el superviviente ya identifica actividades propensas a "
    "error EN EL PROCESO y lo unico que el otro anade es O PRODUCTO. SE DICE LO QUE ESTE REPARTO "
    "TIENE DE DISCUTIBLE EN VEZ DE CALLARLO: su paso 5, VALIDAR QUE EL DISPOSITIVO FUNCIONE "
    "CONSISTENTEMENTE ANTES DE ESCALAR SU USO, viaja de APPEND, y el puesto 2931 declara PROBARLO "
    "EN CONDICIONES REALES una de las dos cosas propias del MIXTO que sobrevive. Se elige APPEND y "
    "no CUBIERTO con perdida nombrada por dos motivos escritos: la pieza es un GESTO DISTINTO y no "
    "un parametro, y el solape que fabrica NO es una contradiccion sino un solape, que es "
    "exactamente lo que la poda de la fase 04 recoge cuando P.12 dice CONTINUA (enlace MAS PODA "
    "DEL SOLAPE). Va marcado en el reporte. De sus tres condiciones, la primera esta CUBIERTA por "
    "la condicion 1 del superviviente (defectos por error humano evitable contra puntos del "
    "proceso propensos a fallos humanos) y las otras dos viajan enteras, reducir inspecciones y "
    "lograr trabajo libre de defectos, y prevenir errores desde el origen AL DISENAR un proceso "
    "nuevo, que es un momento que el superviviente no nombra.",
)

C21 = acto(
    3,
    ["criterios_seleccion_proyectos_calidad", "dmaic_fase_select", "proceso_nominacion_seleccion"],
    "criterios_seleccion_proyectos_calidad",
    ["proceso_nominacion_seleccion"],
    "dmaic_fase_select",
    "CONTENIDO, Y LO DECIDE EL ALCANCE DEL ROL con las condiciones y el cableado de acuerdo, con "
    "el conteo de pasos en contra y por eso VA MARCADO. Los dos viables medidos hoy son "
    "criterios_seleccion_proyectos_calidad y dmaic_fase_select; proceso_nominacion_seleccion es el "
    "CENTRO y NO ES VIABLE porque no deja ningun mixto fuera. Entre los dos viables: PASOS 5 "
    "contra 4 a favor de dmaic_fase_select, CONDICIONES 2 contra 1 y CABLEADO 6 contra 5 a favor "
    "de criterios_seleccion_proyectos_calidad, y MATERIAL PROPIO EMPATADO en 2 y 2 contado por el "
    "puesto 2933, que es el veredicto DIRECTO del par mixto (criterios trae LA MATRIZ DE "
    "EVALUACION COMPUESTA y la presentacion al consejo; dmaic_fase_select trae EL TEAM CHARTER y "
    "la asignacion de personal capacitado). LO QUE DESEMPATA ES EL ALCANCE DEL ROL: el que muere "
    "es EL PROCESO GENERAL DE NOMINACION Y SELECCION DE PROYECTOS, y dmaic_fase_select es UNA FASE "
    "DEL MAPA DMAIC, cosa que el propio puesto 2742 subraya al escribir que quien lo lea como "
    "ficha de fase dira D y que las fases DMAIC salen D entre si. Meter el proceso general dentro "
    "de la ficha de una fase de una metodologia es llamar a una cabeza como una sola de sus partes "
    "(P.8, alcance del rol); meterlo en los CRITERIOS DE SELECCION DE PROYECTOS DE CALIDAD es "
    "quedarse en la misma casa, y el puesto 2627 ya escribio que EL PRIMERO VA DENTRO DEL SEGUNDO. "
    "GUARDA 1B, y aqui NO pasa por vacio: criterios_seleccion_proyectos_calidad ES PUERTA (aparece "
    "en el listado de SALVABLES de docs/loop/SALIDA_V53_PUERTAS_APERTURA.txt) y por eso NO PUEDE "
    "SER ABSORBIDO; aqui es el superviviente, asi que la puerta no solo sobrevive sino que se "
    "queda con el material. CHOQUE DE LETRA CONTRA ARITMETICA, REGISTRADO CON SU PUESTO: el "
    "veredicto 2627 escribe SOBREVIVE PROCESO_NOMINACION_SELECCION, y ese nodo no es viable. MANDA "
    "LA ARITMETICA (adjudicacion 3 del acta de la vuelta 50), y otra vez el nombrado MUERE. Va "
    "marcado en el reporte.",
    {"proceso_nominacion_seleccion": {
        "1": "INCISO:1|(datos, encuestas, empleados, clientes)| desde todas las fuentes posibles ",
        "2": "INCISO:2|factibilidad, significancia, medibilidad|, y también según ",
        "3": "APPEND",
        "4": "CUBIERTO:4",
        "5": "APPEND",
    }},
    {"proceso_nominacion_seleccion": {"1": "CUBIERTO:1", "2": "APPEND"}},
    "EL PUESTO 2627 ESCRIBE LO QUE EL CENTRO TRAE DE MAS Y AQUI SE SALVA PIEZA A PIEZA: dice que "
    "proceso_nominacion_seleccion trae de mas LAS FUENTES DE NOMINACION (datos, encuestas, "
    "empleados, clientes), DELEGAR EL FILTRADO INICIAL y ASEGURAR EL BALANCE VITALES POCOS CONTRA "
    "UTILES MUCHOS. LAS TRES SE SALVAN: delegar el filtrado y el balance viajan ENTEROS de APPEND "
    "(sus pasos 3 y 5) porque son gestos distintos, y las fuentes van de INCISO ADOSADO al paso 1 "
    "del superviviente, listar todas las nominaciones de proyectos disponibles, porque las fuentes "
    "son el PARAMETRO CONCRETO de ese gesto (dicen DE DONDE salen las nominaciones) y el paso "
    "resultante se lee limpio. Su paso 2, aplicar criterios de screening, es el paso 2 del "
    "superviviente con TRES criterios de mas, y el propio 2627 dice que los criterios SE SOLAPAN "
    "CASI POR COMPLETO: va de INCISO ADOSADO con los tres que faltan (factibilidad, significancia, "
    "medibilidad) para no perderlos ni duplicar los seis que ya estan. Su paso 4, presentar la "
    "lista priorizada al consejo para la decision final, es el paso 4 del superviviente dicho "
    "igual (CUBIERTO:4). CERO PERDIDAS NOMBRADAS en este acto. De sus dos condiciones, la primera "
    "esta CUBIERTA por la condicion 1 del superviviente (multiples nominaciones o candidatos y hay "
    "que priorizar) y la segunda viaja entera porque es la unica del acto que nombra el sintoma "
    "que dispara todo, que los proyectos ejecutados no generan impacto real en resultados "
    "financieros.",
)

C6 = acto(
    4,
    ["investigar_datos_cliente", "personalizacion_investigacion_prospecto", "seguimiento_informacion_cliente"],
    "investigar_datos_cliente",
    ["seguimiento_informacion_cliente"],
    "personalizacion_investigacion_prospecto",
    "CONTENIDO, Y ES EL MARGEN MAS ANCHO DE LA TANDA. Los dos viables medidos hoy son "
    "investigar_datos_cliente y personalizacion_investigacion_prospecto; "
    "seguimiento_informacion_cliente es el CENTRO y no es viable porque no deja ningun mixto "
    "fuera. Entre los dos viables: PASOS 11 contra 4, CABLEADO 4 contra 2, CONDICIONES EMPATADAS "
    "(3 y 3). ESTE ES UNO DE LOS DOS ACTOS CON PAR MIXTO EN B Y SU RAZON SE LEYO ANTES DE FUNDIR, "
    "que es lo que el acta 51, pregunta 5, manda: el puesto 811 no escribe una pregunta de "
    "POLITICA DE CATALOGO sino una CONDICION DE CONTEO, con estas palabras, la familia de los "
    "datos del cliente de Coleman ya lleva CUATRO nodos vistos y LOS PARES SE CONTRADICEN ENTRE SI "
    "SEGUN CON QUIEN SE COMPARE: HAY QUE CONTARLA ANTES DE DECIDIR. Esa condicion se descarga "
    "midiendo, no decidiendo en la mesa, y se midio hoy (docs/loop/SALIDA_V53_FAMILIA_COLEMAN.txt) "
    "ANTES de sellar este plan, y lo que mide es que LA COBERTURA DE LA FAMILIA YA ES 6 DE 6: los "
    "cuatro nodos que el 811 nombra estan VIVOS y sus SEIS pares estan LEIDOS (317 A, 509 D, 657 D, "
    "687 D, 811 B y 1222 A), CERO pares sin leer. La condicion queda DESCARGADA POR MEDICION. Por "
    "eso el acto SE FUNDE y el B va a la relectura POST FUSION, que "
    "es la que decide y a la que la correccion cita. NINGUN VEREDICTO A DEL ACTO ESCRIBE LA "
    "FORMULA Sobrevive X, asi que aqui no hay choque de letra contra aritmetica.",
    {"seguimiento_informacion_cliente": {
        "1": "INCISO:1|(básica, profesional, personal, preferencias, actividad de compra)|, clasificados por categorías ",
        "2": "CUBIERTO:8",
        "3": "APPEND",
        "4": "APPEND",
        "5": "APPEND",
        "6": "APPEND",
    }},
    {"seguimiento_informacion_cliente": {"1": "CUBIERTO:2", "2": "APPEND", "3": "CUBIERTO:2"}},
    "EL PUESTO 1222 ESCRIBE LA LISTA DE LO QUE HAY QUE SALVAR Y AQUI SE SALVA PIEZA A PIEZA: dice "
    "que de seguimiento_informacion_cliente se perderian CUATRO, LA TAXONOMIA DE CATEGORIAS "
    "(basica, profesional y personal), LA FECHA de adquisicion y actualizacion de cada dato para "
    "saber si sigue fresco, capturar LA RAZON DECLARADA Y LA RAZON REAL de compra, y DOCUMENTAR "
    "RESULTADOS Y DISPOSICION del cliente tras cada interaccion. LAS CUATRO SE SALVAN: las tres "
    "ultimas viajan ENTERAS de APPEND (sus pasos 3, 4 y 5) y la taxonomia va de INCISO ADOSADO al "
    "paso 1 del superviviente, elegir de 5 a 10 datos para registrar de inmediato, porque las "
    "categorias son el PARAMETRO CONCRETO de ese gesto (dicen DE QUE TIPO son los datos que se "
    "eligen) y el paso resultante se lee limpio. Su paso 6, usar la informacion activamente en "
    "comunicaciones personalizadas, viaja ENTERO de APPEND porque el superviviente RECOGE datos y "
    "no dice que hacer con ellos, y el puesto 317 declara ese uso comun a los dos pero el texto "
    "del superviviente no lo tiene en ningun paso. Su paso 2, establecer un sistema o CRM para "
    "registrar y actualizar los datos, es el paso 8 del superviviente, elegir una herramienta para "
    "organizar tus contactos que realmente vayas a usar (CUBIERTO:8). CERO PERDIDAS NOMBRADAS en "
    "este acto. De sus tres condiciones, la primera y la tercera estan CUBIERTAS por la condicion "
    "2 del superviviente (mejorar la retencion construyendo relaciones mas personales, contra "
    "mejorar la retencion y pasar de transacciones anonimas a relaciones personalizadas) y la "
    "segunda viaja entera porque habla del EQUIPO, que el superviviente no nombra.",
)

DECLARADO_MAPA = {
    "acto_por_sus_miembros": ["influence_map_organizacional", "mapa_de_influencia",
                              "mapa_organizacional_influencia"],
    "especie": "PREGUNTA DE POLITICA DE CATALOGO CONGELADA EN UNA B",
    "por_que_no_se_funde":
        "ES UNO DE LOS DOS ACTOS CON PAR MIXTO EN B Y SU RAZON SE LEYO ANTES DE FUNDIR, que es lo "
        "que el acta 51, pregunta 5, manda. EL PROPIO VEREDICTO 604 ESCRIBE LA PREGUNTA Y LA MANDA "
        "A LA MESA, con estas palabras: LO QUE HAY QUE DECIDIR EN LA MESA ES SI EL LEVANTAMIENTO Y "
        "EL USO SON UN NODO O DOS; SI SON DOS, LA ARISTA ENTRE ELLOS ES OBLIGATORIA Y HOY NO "
        "EXISTE. No es una condicion de TEXTO que se descargue leyendo ni de CONTEO que se "
        "descargue midiendo: es politica de catalogo, la misma especie exacta del acto del S&OP "
        "(puesto 703). El acto se DECLARA y se acumula para la mesa del PARA_ALEXIS del cierre.",
    "lo_que_la_lectura_si_deja_medido":
        "mapa_organizacional_influencia LEVANTA el mapa (listar a las personas, dibujar el diagrama "
        "de relaciones, representar el impacto del producto en la vida de cada una, actualizarlo y "
        "volcarlo al lienzo) y mapa_de_influencia lo USA para planear el asalto (identificar los "
        "grupos de poder, decidir cual se contacta primero, apalancar un grupo para convencer al "
        "siguiente, marcar a los saboteadores y no saltarse etapas). Los dos son VIABLES por la "
        "estructura y el centro influence_map_organizacional no lo es. Si la mesa dice UN NODO, el "
        "acto se funde y el contenido tendria que elegir; si dice DOS, lo que falta es la ARISTA, "
        "que es fase 04.",
}

PLANES = [
    ("PLAN_V53_OPU01_LOTE_A.json",
     "1, P.12, LOTE A DE LA VUELTA 53: los actos 7, 8, 9 y 11 de la nomina del cierre de la "
     "vuelta 52 (el LIENZO DE PROPUESTA DE VALOR, los PROMPTS, los WARRANTS y la HUELLA DE CARBONO)",
     [A7, A8, A9, A11], []),
    ("PLAN_V53_OPU01_LOTE_B.json",
     "1, P.12, LOTE B DE LA VUELTA 53: los actos 13, 14, 15 y 17 de la nomina del cierre de la "
     "vuelta 52 (los COSTOS DE FRANQUICIA, el ABOGADO DE FRANQUICIAS, la FRANQUICIA INADVERTIDA y "
     "la GESTION POR OBJETIVOS)",
     [B13, B14, B15, B17], []),
    ("PLAN_V53_OPU01_LOTE_C.json",
     "1, P.12, LOTE C DE LA VUELTA 53: los actos 19, 20, 21 y 6 de la nomina del cierre de la "
     "vuelta 52 (el PARETO, el POKA YOKE, el DMAIC SELECT y la INVESTIGACION DEL CLIENTE, este "
     "ultimo con par mixto en B)",
     [C19, C20, C21, C6], [DECLARADO_MAPA]),
]


def cargar(nid):
    p = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(p):
        return None
    return json.load(io.open(p, encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("LOS TRES PLANES SELLADOS DE LA VUELTA 53, con sus incisos VERIFICADOS")
    print("modo: %s" % ("SIMULACION, no escribe" if a.simular else "ESCRITURA"))
    print("=" * 78)

    fallos = []
    for nombre, tramo, actos, declarados in PLANES:
        print()
        print("--- %s" % nombre)
        for act in actos:
            sup, abs_ = act["superviviente"], act["absorbidos"]
            print("  acto %d  sobrevive %-44s absorbe %s"
                  % (act["orden"], sup, ", ".join(abs_)))
            for nid in act["miembros_del_acto_entero"]:
                d = cargar(nid)
                if d is None:
                    fallos.append("%s: %s no existe" % (nombre, nid))
                elif d.get("deprecado") or d.get("deprecated"):
                    fallos.append("%s: %s ya esta deprecado" % (nombre, nid))
            if sorted(act["miembros"]) != sorted([sup] + list(abs_)):
                fallos.append("%s acto %d: miembros no calzan" % (nombre, act["orden"]))
            for muere in abs_:
                d = cargar(muere)
                if d is None:
                    continue
                for etq, campo, marcas in (("pasos", "pasos_accionables", act["pasos"]),
                                           ("condiciones", "condiciones_activacion", act["condiciones"])):
                    real = set(str(i) for i in range(1, len(d.get(campo) or []) + 1))
                    dicho = set((marcas.get(muere) or {}).keys())
                    if real != dicho:
                        fallos.append("%s acto %d, %s de %s: faltan %s, sobran %s"
                                      % (nombre, act["orden"], etq, muere,
                                         sorted(real - dicho), sorted(dicho - real)))
                # LA COMPROBACION QUE JUSTIFICA ESTE INSTRUMENTO: el inciso es VERBATIM
                for i, texto in enumerate(d.get("pasos_accionables") or [], 1):
                    m = (act["pasos"].get(muere) or {}).get(str(i), "")
                    if not m.startswith("INCISO:"):
                        continue
                    try:
                        cual, inciso, nexo = m[len("INCISO:"):].split("|")
                        k = int(cual)
                    except ValueError:
                        fallos.append("%s acto %d: marca INCISO mal formada %r"
                                      % (nombre, act["orden"], m))
                        continue
                    if inciso not in texto:
                        fallos.append("%s acto %d: el inciso %r NO es trozo verbatim del paso %d de %s"
                                      % (nombre, act["orden"], inciso, i, muere))
                    else:
                        s = cargar(sup)
                        pasos_sup = s.get("pasos_accionables") or []
                        if not (1 <= k <= len(pasos_sup)):
                            fallos.append("%s acto %d: INCISO al paso %d, que el superviviente no tiene"
                                          % (nombre, act["orden"], k))
                        else:
                            print("      INCISO al paso %d: %s"
                                  % (k, pasos_sup[k - 1] + nexo + inciso))

    if fallos:
        print()
        print("ROJO. NO SE ESCRIBE NADA:")
        for f in fallos:
            print("  - %s" % f)
        return 1

    if not a.simular:
        for nombre, tramo, actos, declarados in PLANES:
            plan = {
                "operacion": "OP-U-01",
                "tramo": tramo,
                "fecha": "2026-08-20",
                "vuelta": 53,
                "estado": "SELLADO",
                "nomina": "docs/loop/RECOMPUTO_V52_CIERRE.jsonl",
                "dossier": "docs/loop/SALIDA_V53_DOSSIER_01_23.txt",
                "vara": VARA,
                "viabilidad": "docs/loop/SALIDA_V53_VIABLES.txt, corrida sobre la nomina del cierre "
                              "de la vuelta 52. Los cuatro actos salen VARIOS VIABLES con dos cada "
                              "uno, y en los cuatro el CENTRO de la estrella no es viable porque no "
                              "deja ningun mixto fuera.",
                "colisiones_esperadas": "docs/loop/SALIDA_V53_COLISIONES_ESPERADAS.txt, medidas "
                                        "ANTES de tocar un nodo sobre EL ARCHIVO ENTERO, por PAR "
                                        "RESUELTO. Una colision real fuera de esa prediccion detiene.",
                "carril_de_colisiones": CARRIL_COLISIONES,
                "vara_de_las_puertas": "Medida hoy con el instrumento reparado en la TAREA 1.3 "
                                       "(docs/loop/SALIDA_V53_PUERTAS_APERTURA.txt, 31 actos con "
                                       "puerta dentro: 26 salvables, 2 imposibles por nomina, 3 por "
                                       "estructura, 0 sin receta). Ninguno de los absorbidos de este "
                                       "lote es semilla ni extremo de puente aprobado.",
                "politica_del_reparto": POLITICA_REPARTO,
                "actos": actos,
                "declarados_y_no_fundidos": declarados,
            }
            io.open(os.path.join(LOOP, nombre), "w", encoding="utf-8", newline="\n").write(
                json.dumps(plan, ensure_ascii=False, indent=1) + "\n")
            print()
            print("ESCRITO: docs/loop/%s" % nombre)

    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
