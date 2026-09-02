# -*- coding: utf-8 -*-
"""_v139_opm05edificio.py . EL CONTENIDO EDITORIAL DE LA FUSION DE MESA
OP-M-05-EDIFICIO, LA FAMILIA DE SALIR DEL EDIFICIO.

NO ES UN INSTRUMENTO. Es EL TEXTO del reparto pieza a pieza. Lo importa
scripts/loop/generar_plan_de_fusion_de_mesa.py, que pone LA ARITMETICA Y LAS
GUARDAS y sella el plan.

TRES COSAS QUE ESTA MESA OBLIGA A DECIR, y las tres estan medidas:

  1. EL MARGEN CORTO NO VOLTEA. La ficha avisa: EL MARGEN DE CABLEADO ES CORTO,
     6 contra 5, asi que la lectura de acto de P.5 no es formalidad. Medido hoy
     (docs/loop/SALIDA_V139_3_SIM_OPM05EDIFICIO.txt): 8 contra 6 y 8 contra 3.
     El margen se ENSANCHA de 1 a 2 y el superviviente es el mismo por las dos
     mediciones.

  2. LA LINEA 1 DE preservar TIENE DOS DUENOS, y la ficha solo nombra a uno.
     Dice "de get_out_of_the_building: LIDERAR TU MISMO estas conversaciones y
     no delegarlas en personal junior", y el paso 2 de
     manifiesto_regla1_hechos_fuera_del_edificio dice "No deleguees la
     investigacion de clientes en empleados o consultores": es el mismo gesto.
     El superviviente no lo tiene en ninguno de sus cuatro pasos. Lo dice la
     quinta marca.

  3. LA LINEA 4 DE preservar PIDE ALGO QUE NINGUNA MARCA DEL CONTRATO PUEDE
     HACER, y esto es un hallazgo de esta vuelta, no una opinion. Pide preservar
     "la formulacion que le da nombre, NO HAY HECHOS DENTRO DEL EDIFICIO", y la
     verificacion 2 manda comprobarla "como FRASE" en el texto final. MEDIDO
     CAMPO POR CAMPO sobre el nodo: esa formulacion vive SOLO en `node_id` y en
     `titulo_concepto`. NO ESTA EN NINGUNO DE SUS CUATRO PASOS ni en
     `resumen_teorico`. Las cuatro marcas del contrato mueven pasos y
     condiciones, VERBATIM, y ninguna mueve un titulo; un INCISO caeria en ROJO
     porque el trozo no es literal de ningun paso, y escribirla a mano seria
     inventar texto, que es justo lo que el INCISO existe para impedir.
     LO QUE SE HACE, y con regla escrita, no inventada: se sella como PERDIDA
     DE ESPECIE `DE NOMBRE`, que es una de las tres de ESPECIES_DE_PERDIDA, con
     sus cuatro claves, y se declara DONDE VIVE de verdad tras la fusion: en
     `merged_originals` del superviviente, que es donde el fundidor guarda el
     node_id, el titulo y la fuente de cada absorbido. La verificacion 2 de la
     ficha, TAL COMO ESTA ESCRITA, NO SE PUEDE CUMPLIR, y se dice en vez de
     fingir que si.
"""

FUSION = {
    "titulo": (
        "LA FAMILIA DE SALIR DEL EDIFICIO, DE BLANK: "
        "customer_discovery_get_out_of_building absorbe a get_out_of_the_building y a "
        "manifiesto_regla1_hechos_fuera_del_edificio. Triangulo CERRADO POR LECTURA, los "
        "tres pares leidos y los tres en A"
    ),
    "superviviente": "customer_discovery_get_out_of_building",
    "absorbidos": [
        "get_out_of_the_building",
        "manifiesto_regla1_hechos_fuera_del_edificio",
    ],
    "motivo": (
        "EL SUPERVIVIENTE LO FIJA LA FICHA SELLADA Y AQUI NO SE RE-ADJUDICA: "
        "docs/plan/OPERACIONES.jsonl escribe superviviente "
        "customer_discovery_get_out_of_building el 12 ago 2026, por P.8 en orden: el "
        "contenido esta empatado (los tres mandan salir a hablar con clientes reales, con "
        "cuatro pasos cada uno) y decide el cableado. "
        "EL MARGEN CORTO, QUE ES LO QUE LA FICHA MANDA VIGILAR, MEDIDO HOY Y NO SUPUESTO: "
        "la ficha escribe MEDIDO: cableado 6 contra 5 contra 3 (12 ago 2026) y avisa en su "
        "nota de que con 6 contra 5 la lectura de acto no es formalidad. La simulacion del "
        "2 sep 2026 mide 8 contra 6 y 8 contra 3. EL MARGEN SE ENSANCHA DE 1 A 2 Y EL "
        "SUPERVIVIENTE NO CAMBIA: la vigilancia que la ficha pedia se hizo y salio a favor "
        "de lo sellado. La divergencia se declara igual, sin promediar ni elegir. "
        "LA DUPLICADA SI CUADRA AL DIGITO Y CON SU NOMBRE: UNA, "
        "producto_minimo_viable.nodos_previos, la misma que la verificacion 1 de la ficha "
        "nombra. CERO auto aristas y CERO aristas internas del acto que sobrevivan. "
        "LECTURA DE ACTO POR P.5, RE-CORRIDA HOY ANTES DE FUNDIR: 3 pares leidos = 3 pares "
        "del acto, EXIT 0. Los tres estan en A (puestos 175, 510 y 439). "
        "LA PIEZA PROPIA QUE LA NOTA DE LA FICHA MANDABA BUSCAR: la nota dice que si al "
        "leer los textos enteros aparece una pieza propia que no este en la lista de "
        "perdidas, SE REGISTRA ANTES DE FUNDIR. Aparecen DOS, y las dos en el manifiesto y "
        "no en get_out_of_the_building: su paso 3 (conseguir experiencia de primera mano "
        "sobre CADA PARTE del modelo de negocio) y su paso 4 (prepararse para recibir "
        "feedback impredecible y a veces doloroso). Ninguna de las dos esta en los cuatro "
        "pasos del superviviente y ninguna esta en las cuatro lineas de preservar. VIAJAN "
        "LAS DOS, de APPEND, porque preservar es SUELO y no techo (acta 138, adjudicacion "
        "3.3) y marcarlas CUBIERTO seria afirmar del superviviente algo que su texto no "
        "dice. QUEDAN REGISTRADAS AQUI, que es lo que la nota pedia."
    ),
    "pasos": {
        "get_out_of_the_building": {
            # 1. Programa reuniones directas y repetidas con clientes
            #    potenciales
            "1": ["CUBIERTO", 2],
            # 2. Lidera tu mismo estas conversaciones, no las delegues en
            #    personal junior   <-- preservar [1]. LA REDACCION QUE VIAJA.
            "2": ["APPEND"],
            # 3. Evita hacer listas con todas las caracteristicas que te piden
            #    los clientes   <-- preservar [2] dice, con estas palabras, VIVE
            #    DENTRO, no es perdida: es el paso 3 del superviviente.
            "3": ["CUBIERTO", 3],
            # 4. Documenta lo que aprendes de cada conversacion en el momento
            #    (blog, CRM)   <-- preservar [3]
            "4": ["APPEND"],
        },
        "manifiesto_regla1_hechos_fuera_del_edificio": {
            # 1. Sal fisicamente a hablar con tus clientes potenciales
            "1": ["CUBIERTO", 2],
            # 2. No deleguees la investigacion de clientes en empleados o
            #    consultores   <-- LA PIEZA DE DOS DUENOS
            "2": ["VIAJA_EN_EL_ACTO", "get_out_of_the_building", 2],
            # 3. Consigue experiencia de primera mano sobre cada parte de tu
            #    modelo de negocio   <-- PIEZA PROPIA que preservar NO lista
            "3": ["APPEND"],
            # 4. Preparate para recibir feedback impredecible y a veces doloroso
            #    <-- PIEZA PROPIA que preservar NO lista
            "4": ["APPEND"],
        },
    },
    "condiciones": {
        "get_out_of_the_building": {
            # 1. Si estas construyendo tu producto sin validarlo con clientes
            #    reales
            "1": ["CUBIERTO", 2],
            # 2. Si tus decisiones se basan en suposiciones internas y no en lo
            #    que dicen los clientes
            "2": ["CUBIERTO", 1],
        },
        "manifiesto_regla1_hechos_fuera_del_edificio": {
            # 1. Al iniciar la busqueda de tus primeros clientes
            "1": ["CUBIERTO", 2],
            # 2. Cuando dependes demasiado de reportes internos en lugar de
            #    hablar tu mismo con tus clientes
            "2": ["CUBIERTO", 1],
        },
    },
    "lineas_de_viaje": {
        "manifiesto_regla1_hechos_fuera_del_edificio|2": (
            "MISMO GESTO: no delegar las conversaciones con clientes, llevarlas tu mismo. "
            "El paso 2 de manifiesto_regla1_hechos_fuera_del_edificio (no deleguees la "
            "investigacion de clientes en empleados o consultores) y el paso 2 de "
            "get_out_of_the_building (lidera tu mismo estas conversaciones, no las delegues "
            "en personal junior) mandan lo mismo, y el superviviente no lo tiene en ninguno "
            "de sus cuatro pasos: su paso 2 manda salir a entrevistar, pero no dice QUIEN "
            "entrevista. "
            "VIAJA LA REDACCION DE get_out_of_the_building, y el motivo es la ficha: su "
            "linea 1 de preservar cita esa redaccion casi palabra por palabra, LIDERAR TU "
            "MISMO estas conversaciones y no delegarlas en personal junior, y es la unica "
            "de las dos que dice LO QUE SI HAY QUE HACER (liderarlas) y no solo lo que no. "
            "UN MATIZ QUE NO VIAJA Y SE DECLARA: esta redaccion prohibe delegar en "
            "EMPLEADOS O CONSULTORES, que es un conjunto mas ancho que PERSONAL JUNIOR. No "
            "se trata como pieza propia porque el gesto es el mismo y la ficha fija la "
            "redaccion, pero el ensanchamiento se pierde y va marcado como DISCUTIBLE en el "
            "reporte de esta vuelta."
        ),
    },
    "nota": (
        "DOCE PIEZAS REPARTIDAS ENTRE DOS ABSORBIDOS, 8 de paso y 4 de condicion, y el "
        "reparto lo CUENTA EL GENERADOR de las marcas: esta nota no lo teclea. "
        "LA LINEA 4 DE preservar NO SE PUEDE CUMPLIR COMO ESTA ESCRITA, Y SE DICE: pide "
        "preservar la formulacion NO HAY HECHOS DENTRO DEL EDIFICIO y la verificacion 2 "
        "manda comprobarla COMO FRASE en el texto final. Medido campo por campo sobre el "
        "nodo, esa formulacion vive SOLO en node_id y en titulo_concepto: no esta en "
        "ninguno de sus cuatro pasos ni en resumen_teorico. Ninguna de las cinco marcas del "
        "contrato mueve un titulo, y el INCISO caeria en ROJO porque el trozo no es literal "
        "de ningun paso. Escribirla a mano en el superviviente seria INVENTAR TEXTO. "
        "POR ESO VA SELLADA COMO PERDIDA DE ESPECIE `DE NOMBRE`, que es una de las tres "
        "escritas, con sus cuatro claves y diciendo DONDE VIVE de verdad tras la fusion: en "
        "merged_originals del superviviente, que es donde el fundidor guarda el node_id, el "
        "titulo y la fuente de cada absorbido. NO SE PIERDE DEL CATALOGO; lo que no se "
        "puede es ponerla en el texto de los pasos sin inventarla. "
        "LAS OTRAS TRES LINEAS DE preservar SI SE CUMPLEN Y SE DICE DONDE: liderar tu mismo "
        "las conversaciones en el paso 2 de get_out_of_the_building (APPEND); documentar EN "
        "EL MOMENTO en su paso 4 (APPEND); y la linea 2, que la propia ficha marca como "
        "VIVE DENTRO Y NO ES PERDIDA, en el paso 3 del superviviente, que ademas anade las "
        "encuestas de foco tradicionales (CUBIERTO:3, exactamente como la ficha manda). "
        "DOS PIEZAS PROPIAS QUE preservar NO LISTABA, halladas al leer los textos enteros, "
        "que es lo que la nota de la ficha mandaba hacer: el paso 3 del manifiesto "
        "(experiencia de primera mano sobre CADA PARTE del modelo de negocio, mas ancho que "
        "el paso 1 del superviviente, que solo identifica hipotesis sobre problema, cliente "
        "y solucion) y su paso 4 (prepararse para feedback impredecible y doloroso, que es "
        "una disposicion y no la tiene nadie mas). Las dos de APPEND: preservar es SUELO y "
        "no techo (acta 138, adjudicacion 3.3). "
        "LAS CUATRO CONDICIONES VAN TODAS CUBIERTO y ninguna de APPEND: las dos que hablan "
        "de construir o decidir sin haber hablado con clientes son la condicion 2 del "
        "superviviente, y las dos que hablan de apoyarse en suposiciones o reportes "
        "internos son su condicion 1. Ni una trae un disparador nuevo. "
        "EL SUPERVIVIENTE QUEDA EN 8 PASOS Y 2 CONDICIONES, contra 4 y 2 de partida. "
        "Y UNA QUE NO ES DE ESTA MESA Y LA FICHA MANDA NO OLVIDAR: get_out_of_the_building "
        "es el hijo de una jerarquia sana medida en la muestra calibrada de la fase 04, "
        "contra genchi_gembutsu. Al fundir, esa arista candidata pasa al superviviente. NO "
        "SE TOCA AQUI y queda dicho."
    ),
    "perdidas": [
        {
            "especie": "DE NOMBRE",
            "que": (
                "LA FORMULACION QUE DA NOMBRE AL NODO: NO HAY HECHOS DENTRO DEL EDIFICIO. Es "
                "la linea 4 de preservar de la ficha, y su verificacion 2 manda comprobarla "
                "COMO FRASE en el texto final."
            ),
            "donde": (
                "SOLO en node_id (manifiesto_regla1_hechos_fuera_del_edificio) y en "
                "titulo_concepto (No Hay Hechos Dentro del Edificio: Sal a Buscarlos), "
                "medido campo por campo sobre el nodo el 2 sep 2026. NO esta en ninguno de "
                "sus cuatro pasos_accionables ni en resumen_teorico, asi que ninguna marca "
                "del contrato puede moverla al texto del superviviente sin inventarla. TRAS "
                "LA FUSION VIVE EN merged_originals del superviviente, donde el fundidor "
                "guarda el node_id, el titulo y la fuente de cada absorbido."
            ),
            "enrutada_a": (
                "LA FASE 04, la pasada editorial: es ahi, y no en una fusion, donde se "
                "decide si una formulacion que vive en un titulo tiene que entrar en el "
                "cuerpo del superviviente. Y QUEDA DICHO PARA EL AUDITOR que la verificacion "
                "2 de esta ficha, tal como esta escrita, NO SE PUEDE CUMPLIR con las cinco "
                "marcas de hoy."
            ),
        }
    ],
    "simulacion_de_hoy": (
        "scripts/plan/simular_fusion.py, corrida el 2 sep 2026 ANTES de fundir, salida "
        "sellada en docs/loop/SALIDA_V139_3_SIM_OPM05EDIFICIO.txt: UNA duplicada nueva "
        "(producto_minimo_viable.nodos_previos, la misma que la ficha nombra), CERO auto "
        "aristas, CERO aristas internas del acto que sobrevivan, y cableado 8 contra 6 y 8 "
        "contra 3, donde la ficha del 12 ago decia 6 contra 5 contra 3. EL MARGEN SE "
        "ENSANCHA Y EL SUPERVIVIENTE NO CAMBIA."
    ),
}
