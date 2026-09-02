# -*- coding: utf-8 -*-
"""_v139_opm03iii.py . EL CONTENIDO EDITORIAL DE LA FUSION DE MESA OP-M-03-III,
EL ACTO III DE LA MESA DEL PIVOTE.

NO ES UN INSTRUMENTO: no mide, no escribe y no decide nada por si mismo. Es EL
TEXTO del reparto pieza a pieza. Lo importa
scripts/loop/generar_plan_de_fusion_de_mesa.py, que pone LA ARITMETICA Y LAS
GUARDAS y sella el plan.

EL SUPERVIVIENTE NO SE ELIGE AQUI: LO ELIGIO LA FICHA (pivote_estrategico, 12
ago 2026, por P.8 con el contenido empatado y el cableado desempatando).

AQUI EL HUECO DEL CONTRATO MUERDE DOS VECES, no una, y las dos las dice la
quinta marca VIAJA_EN_EL_ACTO (vuelta 139, operacion 2.a).
"""

FUSION = {
    "titulo": (
        "ACTO III DE LA MESA DEL PIVOTE: pivote_estrategico absorbe a pivote_startup y a "
        "pivotes_e_iteraciones. Es la TERCERA fusion de la fase 06, y la primera en la que "
        "la quinta marca se usa DOS VECES en el mismo acto"
    ),
    "superviviente": "pivote_estrategico",
    "absorbidos": ["pivote_startup", "pivotes_e_iteraciones"],
    "motivo": (
        "EL SUPERVIVIENTE LO FIJA LA FICHA SELLADA Y AQUI NO SE RE-ADJUDICA: "
        "docs/plan/OPERACIONES.jsonl escribe superviviente pivote_estrategico el 12 ago "
        "2026. Su adjudicacion dice que EL CONTENIDO ESTA EMPATADO (veredicto 857, los "
        "pasos se emparejan uno a uno, cinco contra cinco) y que por P.8, con el contenido "
        "empatado, DECIDE EL CABLEADO. "
        "LA REGLA DE LA FICHA ENVEJECIDA (P.9, P.13) SE APLICA Y SE DECLARA, con las dos "
        "cifras y sus dos cortes, SIN promediar y SIN elegir una: la ficha escribe MEDIDO: "
        "cableado 13 contra 11 y 13 contra 4 (12 ago 2026); la simulacion del 2 sep 2026, "
        "sellada en docs/loop/SALIDA_V139_3_SIM_OPM03III.txt, mide 13 contra 12 y 13 contra "
        "3. NO VOLTEA NADA: pivote_estrategico gana por los dos conteos y contra los dos "
        "absorbidos. Las duplicadas SI cuadran al digito con la ficha: DOS, "
        "customer_development_agile_pairing.nodos_siguientes y "
        "fracaso_como_aprendizaje_startup.nodos_siguientes, y CERO auto aristas. "
        "LA LECTURA DE ACTO POR P.5 ESTA HECHA Y ERA OBLIGATORIA POR DOS MOTIVOS que la "
        "propia ficha escribe: el par interno pivote_estrategico contra "
        "pivotes_e_iteraciones NUNCA SE HABIA LEIDO, y los pares internos fuera de cola "
        "tampoco. La escribio la vuelta 138 en docs/plan/LD_ACTO_III_DEL_PIVOTE.md "
        "(veredicto LD-138-01, CLASE A), y EL AUDITOR LA RELEYO A CIEGAS en el acta 138: "
        "imprimio los pasos de los tres nodos, adjudico su clase ANTES de abrir la LD, y "
        "coincidieron en la clase y en los tres pares. RE-CORRIDA HOY ANTES DE FUNDIR con "
        "scripts/loop/vuelta138_p5_lectura_de_acto.py --id-op OP-M-03-III: 3 pares leidos "
        "= 3 pares del acto, EXIT 0."
    ),
    "pasos": {
        "pivote_startup": {
            # 1. Revisa los resultados de tus pruebas de si o no sobre las
            #    hipotesis de tu negocio
            "1": ["CUBIERTO", 1],
            # 2. Identifica que parte de tu modelo de negocio necesita cambiar
            #    <-- preservar [1]. LA PIEZA DE DOS DUENOS, PRIMERA.
            "2": ["VIAJA_EN_EL_ACTO", "pivotes_e_iteraciones", 3],
            # 3. Decide con rapidez y sin miedo al fracaso si toca pivotar
            #    <-- preservar [2]. ESTA ES LA REDACCION QUE VIAJA de la segunda
            #    pieza de dos duenos.
            "3": ["APPEND"],
            # 4. Si trabajas con alguien mas, cuentale el cambio como parte
            #    normal del proceso
            "4": ["CUBIERTO", 5],
            # 5. Vuelve a poner a prueba tu modelo ajustado hablando con clientes
            "5": ["CUBIERTO", 4],
        },
        "pivotes_e_iteraciones": {
            # 1. Distingue con claridad entre un ajuste menor y un cambio
            #    sustancial   <-- preservar [3]
            "1": ["APPEND"],
            # 2. Corre pruebas pasa/no pasa constantes sobre las hipotesis de tu
            #    modelo de negocio
            "2": ["CUBIERTO", 1],
            # 3. Usa tu lienzo de modelo de negocio para ubicar que parte
            #    necesita el cambio   <-- preservar [1]. ESTA ES LA REDACCION QUE
            #    VIAJA de la primera pieza de dos duenos.
            "3": ["APPEND"],
            # 4. Cuando los datos contradigan una hipotesis, admite el error y
            #    decide sin demora si ajustas o cambias de rumbo
            #    <-- LA PIEZA DE DOS DUENOS, SEGUNDA.
            "4": ["VIAJA_EN_EL_ACTO", "pivote_startup", 3],
            # 5. Documenta cada cambio de rumbo como una nueva version de tu
            #    lienzo de modelo de negocio   <-- preservar [4]
            "5": ["APPEND"],
            # 6. No te aferres a tu idea original si los datos indican lo
            #    contrario
            "6": ["CUBIERTO", 1],
        },
    },
    "condiciones": {
        "pivote_startup": {
            # 1. Si lo que ves con tus clientes contradice lo que pensabas al
            #    inicio sobre tu negocio
            "1": ["CUBIERTO", 1],
            # 2. Si tu negocio esta estancado y necesita un cambio grande para
            #    avanzar
            "2": ["CUBIERTO", 2],
        },
        "pivotes_e_iteraciones": {
            # 1. Si las pruebas con clientes te dan resultados negativos o
            #    ambiguos
            "1": ["CUBIERTO", 1],
            # 2. Si tus metricas de validacion muestran que una hipotesis de tu
            #    modelo de negocio es falsa
            "2": ["CUBIERTO", 1],
            # 3. Si tu crecimiento esta estancado y necesitas un cambio para
            #    sobrevivir
            "3": ["CUBIERTO", 2],
        },
    },
    "lineas_de_viaje": {
        "pivote_startup|2": (
            "MISMO GESTO: senalar QUE PARTE del modelo cambia. El paso 2 de pivote_startup "
            "(identifica que parte de tu modelo de negocio necesita cambiar) y el paso 3 de "
            "pivotes_e_iteraciones (usa tu lienzo de modelo de negocio para ubicar que "
            "parte necesita el cambio) mandan lo mismo, y el superviviente no lo tiene en "
            "ninguno de sus cinco pasos: su paso 2 formula una hipotesis NUEVA y su paso 3 "
            "redirige el desarrollo, pero ninguno UBICA la parte que cambia. "
            "VIAJA LA REDACCION DE pivotes_e_iteraciones, Y EL MOTIVO ES EL TEXTO DE LA "
            "FICHA: su linea 1 de preservar pide senalar QUE PARTE DEL LIENZO cambia, y de "
            "las dos redacciones SOLO la de pivotes_e_iteraciones nombra EL LIENZO. La de "
            "pivote_startup dice modelo de negocio y se queda corta justo en la palabra que "
            "la ficha exige. SE DECLARA LA DESVIACION: esa linea de preservar atribuye la "
            "pieza a pivote_startup, y aqui viaja la redaccion del OTRO dueno; la pieza "
            "viaja igual y viaja MEJOR, pero la atribucion de la ficha y la redaccion que "
            "sobrevive no coinciden, y eso se dice en vez de callarse."
        ),
        "pivotes_e_iteraciones|4": (
            "MISMO GESTO: decidir sin demora cuando los datos contradicen. El paso 4 de "
            "pivotes_e_iteraciones (cuando los datos contradigan una hipotesis, admite el "
            "error y decide sin demora si ajustas o cambias de rumbo) y el paso 3 de "
            "pivote_startup (decide con rapidez y sin miedo al fracaso si toca pivotar) son "
            "el mismo gesto, y es la linea 2 de preservar, que la ficha marca con un aviso: "
            "NO SE PODA aunque parezca redundante, porque es un lado de la frontera "
            "declarada del 1298. "
            "VIAJA LA REDACCION DE pivote_startup, que es la que lleva el APPEND, y por dos "
            "motivos: es a quien la linea 2 de preservar atribuye la pieza, y es la que trae "
            "SIN MIEDO AL FRACASO, que es la disposicion de Blank que la ficha manda no "
            "podar. LOS TRES MATICES DEL PASO 4 NO SE PIERDEN Y NO SON PIEZA PROPIA, uno "
            "por uno: cuando los datos contradigan una hipotesis es el paso 1 del "
            "superviviente (aceptar la evidencia empirica aunque contradiga) y su condicion "
            "1; admite el error es ese mismo paso 1; y si ajustas o cambias de rumbo viaja "
            "entero en el paso 1 de pivotes_e_iteraciones, que va de APPEND y distingue el "
            "ajuste menor del cambio sustancial."
        ),
    },
    "nota": (
        "DIECISEIS PIEZAS REPARTIDAS ENTRE DOS ABSORBIDOS, 11 de paso y 5 de condicion, "
        "y el reparto lo CUENTA EL GENERADOR de las marcas: esta nota no lo teclea. "
        "LA QUINTA MARCA SE USA DOS VECES Y EN LAS DOS DIRECCIONES, que es lo que hace de "
        "esta fusion la prueba de fuego del vocabulario nuevo: pivote_startup cede su paso "
        "2 a pivotes_e_iteraciones, y pivotes_e_iteraciones cede su paso 4 a pivote_startup. "
        "NO ES UNA CADENA: cada VIAJA_EN_EL_ACTO apunta a un paso que lleva APPEND, o sea "
        "que las dos piezas llegan a viajar de verdad, y la guarda (ii) del generador cae "
        "en ROJO con la letra cadena que no llega a viajar si alguna apuntara a la otra. "
        "LAS CUATRO LINEAS DE preservar QUEDAN CUBIERTAS Y SE DICE DONDE: la parte del "
        "lienzo en el paso 3 de pivotes_e_iteraciones (APPEND); decidir con rapidez y sin "
        "miedo en el paso 3 de pivote_startup (APPEND); el ajuste menor contra el cambio "
        "sustancial en el paso 1 de pivotes_e_iteraciones (APPEND); y la version nueva del "
        "lienzo en su paso 5 (APPEND). "
        "LOS SIETE CUBIERTO DE PASO, sin silencios: revisar los resultados de las pruebas "
        "(paso 1 de pivote_startup), correr pruebas pasa o no pasa (paso 2 de "
        "pivotes_e_iteraciones) y no aferrarse a la idea original (su paso 6) son el paso 1 "
        "del superviviente, que acepta la evidencia empirica aunque contradiga meses de "
        "trabajo; contarle el cambio a quien te acompana (paso 4 de pivote_startup) es su "
        "paso 5, que comunica el pivote a inversores, empleados y stakeholders; y volver a "
        "poner a prueba el modelo ajustado (paso 5 de pivote_startup) es su paso 4, que "
        "valida la nueva direccion con nuevos experimentos. "
        "LAS CINCO CONDICIONES VAN TODAS CUBIERTO Y NINGUNA DE APPEND, y eso es una "
        "medicion y no una comodidad: las tres que hablan de pruebas o metricas que "
        "contradicen la hipotesis son la condicion 1 del superviviente, y las dos que "
        "hablan de estancamiento son su condicion 2. Ni una trae un disparador que el "
        "superviviente no tenga (acta 55, pregunta 5). "
        "EL SUPERVIVIENTE QUEDA EN 9 PASOS Y 2 CONDICIONES, contra 5 y 2 de partida. "
        "CERO PERDIDAS SELLADAS, Y LA LISTA VACIA ES UNA DECLARACION: la verificacion 5 de "
        "la ficha dice que LAS 4 VIAJAN todas, y las cuatro viajan."
    ),
    "perdidas": [],
    "simulacion_de_hoy": (
        "scripts/plan/simular_fusion.py, corrida el 2 sep 2026 ANTES de fundir, salida "
        "sellada en docs/loop/SALIDA_V139_3_SIM_OPM03III.txt: DOS duplicadas nuevas "
        "(customer_development_agile_pairing.nodos_siguientes y "
        "fracaso_como_aprendizaje_startup.nodos_siguientes, las mismas dos que la ficha "
        "nombra), CERO auto aristas, CERO aristas internas del acto que sobrevivan, y "
        "cableado 13 contra 12 y 13 contra 3, donde la ficha del 12 ago decia 13 contra 11 "
        "y 13 contra 4. La divergencia va declarada y no resuelta copiando."
    ),
}
