# -*- coding: utf-8 -*-
"""_v63_opm03i.py . EL CONTENIDO EDITORIAL DE LA FUSION DE MESA OP-M-03-I.

NO ES UN INSTRUMENTO: no mide, no escribe y no decide nada por si mismo. Es EL
TEXTO del reparto pieza a pieza, con su motivo citado y LAS PERDIDAS SELLADAS EN
CAMPO PROPIO. Lo importa scripts/loop/generar_plan_de_fusion_de_mesa.py, que es
quien pone LA ARITMETICA Y LAS GUARDAS y quien sella el plan.

EL PREFIJO _ DEL NOMBRE es el que la casa ya usa para los ficheros de contenido
que otro corre (_v62_lote_a.py y los suyos).

EL SUPERVIVIENTE NO SE ELIGE AQUI: LO ELIGIO LA FICHA. La adjudicacion de
OP-M-03-I esta sellada en docs/plan/OPERACIONES.jsonl desde el 12 ago 2026 y el
generador cae en ROJO si este fichero nombra otro. Lo que se decide aqui es SOLO
el reparto de las siete piezas del que muere.

CADA PERDIDA LLEVA SUS CUATRO CLAVES (especie, que, donde, enrutada_a) y su
especie es UNA DE LAS TRES ESCRITAS. El generador cae en ROJO al sellar si alguna
se sale, y el tallador vuelve a comprobarlo despues.
"""

FUSION = {
    "titulo": (
        "ACTO I DE LA MESA DEL PIVOTE, LA PUERTA DE METRICAS DE RIES: "
        "pivotar_o_perseverar absorbe decision_pivote_perseverar. Es la primera fusion "
        "de mesa de la campana y la primera operacion de la fase 03 despues de que "
        "OP-U-01 quedara agotada. EL BLOQUE DEL PUNTO BRILLANTE NO SE TOCA: vive entero "
        "en su nodo propio puntos_brillantes_antes_del_pivote y lo unico que esta fusion "
        "tiene que hacer con el es NO PERDER SU ARISTA"
    ),
    "superviviente": "pivotar_o_perseverar",
    "absorbidos": ["decision_pivote_perseverar"],
    "motivo": (
        "EL SUPERVIVIENTE LO FIJA LA FICHA SELLADA Y AQUI NO SE RE-ADJUDICA: "
        "docs/plan/OPERACIONES.jsonl escribe superviviente pivotar_o_perseverar el 12 ago "
        "2026, POR CABLEADO A CONTENIDO EMPATADO, 6 contra 4, que es el supuesto en el que "
        "P.8 deja decidir al grafo. DOS DIVERGENCIAS ENTRE LA MEDICION DE AQUEL DIA Y LA DE "
        "HOY, Y LAS DOS SE DECLARAN EN VEZ DE TAPARSE, PORQUE NINGUNA CAMBIA EL "
        "SUPERVIVIENTE. PRIMERA: el cableado de hoy es 6 contra 5 y no 6 contra 4, medido "
        "con scripts/plan/simular_fusion.py en esta vuelta; la entrada que el que muere "
        "gano es la de puntos_brillantes_antes_del_pivote, que NACIO EL 14 AGO 2026 por "
        "OP-F-04-WEI, o sea DESPUES de la simulacion sellada. El superviviente sigue "
        "ganando. SEGUNDA: leido con las varas por forma de los tramos, el contenido de hoy "
        "NO empata entero: pasos 5 contra 4 apunta a pivotar_o_perseverar y condiciones 2 "
        "contra 3 apunta al que muere, o sea CHOCAN. Y en un CHOCAN decide LA PIEZA "
        "DECLARADA (acta 53, pregunta 3), que aqui es la adjudicacion sellada de la propia "
        "ficha y nombra a pivotar_o_perseverar con todas sus letras. LAS DOS VIAS "
        "CONVERGEN EN EL MISMO NODO, y por eso esto es una divergencia declarada y no una "
        "parada. VA MARCADO COMO DISCUTIBLE EN LA SECCION 6 DEL REPORTE DE ESTA VUELTA."
    ),
    "pasos": {
        # 1. Revisar si las metricas accionables muestran mejora suficiente hacia
        #    un modelo de negocio sostenible
        "1": ["CUBIERTO", 1],
        # 2. Evaluar si el equipo puede racionalizar el fracaso en lugar de aceptarlo
        "2": ["APPEND"],
        # 3. Comparar el progreso actual con las expectativas cuantitativas
        #    definidas al inicio
        "3": ["INCISO", 1, "las expectativas cuantitativas definidas al inicio", " y con "],
        # 4. Decidir con datos concretos en la sala, no solo con intuicion
        "4": ["INCISO", 3, "con datos concretos en la sala, no solo con intuicion", ", "],
    },
    "condiciones": {
        # 1. Cuando los experimentos de producto muestran efectividad decreciente
        "1": ["CUBIERTO", 1],
        # 2. Cuando el equipo siente que el desarrollo de producto deberia ser mas productivo
        "2": ["APPEND"],
        # 3. Cuando la startup lleva atrapada en la tierra de los muertos vivientes
        "3": ["CUBIERTO", 2],
    },
    "nota": (
        "SIETE PIEZAS REPARTIDAS: dos viajan enteras, dos de INCISO y tres ya estaban "
        "dichas. LA PIEZA QUE LA FICHA MANDA PRESERVAR VIAJA ENTERA Y ES LA PRIMERA DEL "
        "REPARTO: evaluar si el equipo RACIONALIZA EL FRACASO en vez de aceptarlo (paso 2 "
        "del que muere) es un gesto que el superviviente no hace en ningun grado, porque "
        "el superviviente mira las metricas y no mira al equipo. Va de APPEND. "
        "LAS DOS PIEZAS QUE LA FICHA RECLASIFICA COMO QUE VIVEN DENTRO SE COMPRUEBAN Y NO "
        "SE TOCAN: la LINEA BASE NUEVA es el paso 4 del superviviente y la COMPROBACION "
        "POSTERIOR es su paso 5, los dos leidos hoy y los dos intactos tras la fusion. "
        "LOS DOS INCISOS SE ADOSAN PORQUE CABEN LIMPIOS, que es la letra de la politica y "
        "el limite que el acta 62 le puso al D9: no se marca CUBIERTO con perdida para "
        "ahorrarse un INCISO que si cabe. El paso 3 del que muere anade a que se compara "
        "el progreso (las expectativas cuantitativas definidas al inicio) sobre un paso 1 "
        "del superviviente que no cierra en punto; el paso 4 anade COMO se decide (con "
        "datos concretos en la sala y no solo con intuicion) sobre un paso 3 que cierra en "
        "parentesis y admite la coma. "
        "EL BLOQUE DEL PUNTO BRILLANTE NO ENTRA EN ESTE REPARTO PORQUE NO ESTA EN EL QUE "
        "MUERE, y eso se midio antes de repartir: decision_pivote_perseverar tiene HOY "
        "cuatro pasos y NINGUNO es del bloque; los cinco viven en "
        "puntos_brillantes_antes_del_pivote, que esta VIVO y no se toca. Lo unico que esta "
        "fusion le hace es REDIRIGIR su arista al superviviente, con su espejo. "
        "TRES PERDIDAS SELLADAS EN EL CAMPO, y las tres son de matiz y ninguna de gesto. "
        "LAS DOS DE CONDICIONES SE NOMBRAN EN VEZ DE IR DE APPEND porque son matices de "
        "disparadores que el superviviente ya tiene y no disparadores distintos, que es la "
        "vara del acta 55, pregunta 5; LA TERCERA CONDICION DEL QUE MUERE SI ES UN "
        "DISPARADOR DISTINTO y por eso esa si va de APPEND: que el EQUIPO SIENTA que el "
        "desarrollo deberia ser mas productivo es una senal subjetiva del equipo, no una "
        "cuenta de metricas, y el superviviente no dispara por nada parecido."
    ),
    "perdidas": [
        {
            "especie": "DE PARAMETRO DE PASO",
            "que": ("el calificativo ACCIONABLES de las metricas que se revisan, y el rotulo "
                    "de MODELO DE NEGOCIO SOSTENIBLE como destino; el paso 1 del "
                    "superviviente dice tus metricas actuales y el modelo ideal de tu plan "
                    "de negocio, que es el mismo gesto sin esos dos rotulos. SE DICE LO QUE "
                    "NO SE PIERDE: metricas_accionables es HOY uno de los cinco "
                    "nodos_previos del superviviente, medido en esta vuelta, asi que el "
                    "concepto sigue a un salto del nodo vivo"),
            "donde": "paso 1 de decision_pivote_perseverar",
            "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente",
        },
        {
            "especie": "DE CONDICIONES",
            "que": ("el disparador de que los experimentos de producto muestren efectividad "
                    "DECRECIENTE; la condicion 1 del superviviente dispara porque las "
                    "metricas clave NO MEJORAN tras varios ciclos, que es el mismo "
                    "fenomeno sin la pendiente"),
            "donde": "condicion 1 de decision_pivote_perseverar",
            "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)",
        },
        {
            "especie": "DE CONDICIONES",
            "que": ("la imagen de la startup ATRAPADA EN LA TIERRA DE LOS MUERTOS VIVIENTES, "
                    "que es el estado de ni crecer ni morir; la condicion 2 del "
                    "superviviente dispara por haber agotado las mejoras posibles sin ver "
                    "resultados, que es el mismo callejon dicho sin la imagen"),
            "donde": "condicion 3 de decision_pivote_perseverar",
            "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)",
        },
    ],
    "simulacion_de_hoy": (
        "scripts/plan/simular_fusion.py corrido en la vuelta 63 ANTES de tocar un nodo "
        "(docs/loop/SALIDA_V63_SIM_OPM03I.txt): CINCO entradas se redirigen "
        "(catalogo_pivotes, ciclo_crear_medir_aprender, contabilidad_innovacion_pivote, "
        "puntos_brillantes_antes_del_pivote y reunion_pivotar_o_perseverar), CERO "
        "duplicadas nuevas y CERO auto aristas. LA SIMULACION SELLADA DEL PLAN DECIA "
        "CUATRO y nombraba a las cuatro primeras; LA QUINTA ES EXACTAMENTE LA QUE LA "
        "CORRECCION DECLARADA DE LA FICHA MANDA REDIRIGIR, y nacio despues de aquella "
        "simulacion. El cotejo de las dos listas es identidad mas ese unico anadido."
    ),
}
