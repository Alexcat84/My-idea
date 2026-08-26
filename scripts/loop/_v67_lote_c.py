# -*- coding: utf-8 -*-
"""_v67_lote_c.py . EL CONTENIDO EDITORIAL DEL LOTE C DEL TRAMO UNICO DE OP-U-02.

NO ES UN INSTRUMENTO: es el texto del lote. La maquina que lo sella es
scripts/loop/generar_plan_del_lote.py, que entra aqui por --contenido _v67_lote_c.

EL LOTE SE DECLARA AL ABRIRLO Y ES PREFIJO SIN SALTOS del orden_universo de lo
que queda del tramo fijado en docs/loop/TRAMO_UNICO_OPU02_V64.jsonl (el lote A de
la vuelta 65 cerro los actos 1 y 3, y el lote B de la vuelta 66 cerro los actos
5, 7, 8, 9, 10 y 11): ACTOS 12, 13, 14, 15, 16 Y 17, que son los SEIS primeros de
ese orden, 30 nodos. UNO CIERRA FUNDIDO (el 16) y CINCO CIERRAN DECLARADOS Y NO
FUNDIDOS con motivo sellado (12, 13, 14, 15 y 17). Los seis cierran ENTEROS en
esta vuelta.

EL REPARTO VA POR ABSORBIDO en la clave reparto, que es la forma que la vuelta 65
estreno para los actos de mas de dos miembros.
"""

# ======================================================================
# ACTO 16: LA FAMILIA DEL ENCUADRE DEL PROBLEMA (HOW MIGHT WE).
# CINCO miembros, CUATRO pares internos con veredicto y los CUATRO en A,
# CERO D, CERO nodos puente y CERO triangulos. NINGUN MIEMBRO ES PUERTA.
# FORMA medida: UNA SOLA VARA. La vara de PASOS apunta a
# encuadre_desafio_diseno (5 contra un maximo de 4) y la de CONDICIONES
# empata en 2. El cableado apunta a how_might_we_briefs (8), y POR P.8 NO
# HABLA: el contenido dice algo, y donde el contenido dice algo el
# contenido manda.
# ======================================================================

SUP16 = "encuadre_desafio_diseno"

MOTIVO16 = (
    "ACTO 16 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DEL ENCUADRE DEL PROBLEMA (HOW MIGHT "
    "WE). UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON MEDICION Y CON LAS "
    "RAZONES DELANTE, NO CON IMPRESION: los CINCO miembros tienen CUATRO pares internos "
    "con veredicto escrito y los CUATRO son de clase A, hay CERO pares D internos, CERO "
    "nodos puente y CERO triangulos, medido con scripts/loop/vuelta65_puentes_del_tramo.py "
    "sobre el estado del dia (5 miembros, 10 combinaciones, 4 A, 0 D, 6 sin veredicto, 0 "
    "puentes, 0 triangulos). P.10 solo detiene una componente cuando aparece un triangulo A "
    "mas A mas D, y aqui no hay ninguno. "
    "Y LAS CUATRO A ENCADENAN A LOS CINCO SIN UNA SOLA CONTRADICCION, leidas del dossier: "
    "el puesto 525 encadena encuadre_desafio_diseno con how_might_we_framing, el 264 "
    "encadena how_might_we_framing con how_might_we_hmw, el 1319 encadena how_might_we_hmw "
    "con how_might_we_briefs y el 236 encadena how_might_we_briefs con "
    "how_might_we_brief_social. Es una cadena de cuatro lecturas DIRECTAS que toca a los "
    "cinco miembros, no un cierre transitivo sin lectura. "
    "EL PUESTO 1319 DECLARA LA UNION CON TODAS SUS LETRAS Y SE CITA EN VEZ DE RESUMIRSE: "
    "hasta hoy la familia HMW eran DOS componentes separadas, how_might_we_briefs con "
    "how_might_we_brief_social por la A del 236, y how_might_we_hmw con how_might_we_framing "
    "y encuadre_desafio_diseno por las A del 264 y el 525, y esa A las UNE en UNA SOLA de "
    "CINCO NODOS. Y el mismo 1319 nombra el gesto comun de los cinco: tomar el problema "
    "central, reformularlo con la formula de como podriamos, y CALIBRAR SU ALTURA para que "
    "no quede ni tan amplio que sea imposible de abordar ni tan estrecho que no deje "
    "espacio a soluciones. "
    "SOBREVIVE encuadre_desafio_diseno, Y LA VARA QUE LO ELIGE ES LA DE PASOS, CON SU "
    "LETRA: la FORMA medida del acto es UNA SOLA VARA "
    "(scripts/loop/varas_n_arias_del_tramo.py, docs/loop/SALIDA_V67_VARAS_N_ARIAS.txt), la "
    "vara de PASOS apunta a encuadre_desafio_diseno con 5 contra un maximo de 4 en los "
    "otros cuatro, y la de CONDICIONES empata en 2 entre cuatro miembros. UNA SOLA VARA "
    "BASTA (acta 53, pregunta 4). EL CABLEADO APUNTA AL OTRO LADO Y NO HABLA, Y SE DICE EN "
    "VEZ DE CALLARLO: how_might_we_briefs tiene cableado 8 contra 3 del superviviente, pero "
    "P.8 es regla de PRELACION, el desempate por cableado SOLO habla a contenido empatado, "
    "y aqui el contenido dice algo. NO DECIDE EL ROTULO NI LA CANTIDAD SOLA: decide que "
    "encuadre_desafio_diseno es el unico del acto que ademas de formular la pregunta define "
    "el impacto que se busca, documenta contexto y restricciones, y manda revisar y ajustar "
    "la pregunta con lo aprendido, o sea que trae el encuadre entero y no solo la formula. "
    "NINGUN MIEMBRO DE ESTE ACTO ES PUERTA, medido al sellar: la guarda 1B pasa por vacio y "
    "se dice en vez de darla por buena."
)

NOTA16 = (
    "EL REPARTO, Y LAS CUATRO COSAS QUE SE DICEN EN VEZ DE CALLARSE. "
    "PRIMERA, LOS DOS INCISOS DEL ACTO Y POR QUE SON DOS Y NO MAS. El superviviente viene "
    "del field guide de IDEO y NO NOMBRA LA FORMULA que da nombre a la familia: su paso 1 "
    "dice formular el problema como una pregunta de diseno abierta y ahi se queda. La "
    "formula viaja de INCISO adosado al paso 1, EXTRAIDA VERBATIM del paso 2 de "
    "how_might_we_hmw, y el paso resultante se lee limpio porque el paso 1 del superviviente "
    "NO termina en punto. El segundo INCISO va al paso 5, extraido VERBATIM del paso 3 de "
    "how_might_we_framing, y mete en el paso de revisar lo unico que le faltaba: con quien "
    "se itera y cual es el criterio de parada. NO SE APILA MAS DE UN INCISO SOBRE EL MISMO "
    "PASO (acta 64, registrada en esta pagina): los otros dos pasos que traen la formula, el "
    "1 de how_might_we_framing y el 2 de how_might_we_briefs, van CUBIERTO por el paso 1 y "
    "SIN perdida, porque el INCISO ya la trae. "
    "SEGUNDA, LOS CINCO PASOS DE APPEND Y POR QUE NINGUNO ES RELLENO: el paso 1 de "
    "how_might_we_briefs es el unico del acto que dice DE DONDE SALE la pregunta, "
    "identificar el objetivo macro; el paso 2 de how_might_we_framing es LA CALIBRACION DE "
    "LA ALTURA por sus dos lados, que el puesto 1319 declara gesto comun de la familia "
    "entera y que el superviviente NO TIENE en ningun paso; el paso 4 de how_might_we_framing "
    "y el 4 de how_might_we_hmw dicen PARA QUE SIRVE la pregunta despues de escribirla, y el "
    "SOLAPE ENTRE LOS DOS VA DECLARADO en vez de escondido: el de framing la usa como "
    "BRUJULA durante todo el proceso y el de hmw como TITULAR de las sesiones de lluvia de "
    "ideas, que no es lo mismo aunque se toquen, y el puesto 1319 llama al segundo su unico "
    "gesto propio; y el paso 4 de how_might_we_brief_social es validar el brief con "
    "CONOCIMIENTO LOCAL antes de prototipar, que no lo dice ningun otro miembro. Los cinco "
    "viajan ENTEROS por la politica escrita, y la fase 04 poda. "
    "TERCERA, LAS TRES PERDIDAS CON ATENUANTE DECLARADO Y POR QUE SE DICEN IGUAL: la "
    "verificacion de la ESPECIFICIDAD y la de la FLEXIBILIDAD sobre la pregunta (pasos 2 y 3 "
    "de how_might_we_brief_social, paso 3 de how_might_we_briefs y paso 3 de "
    "how_might_we_hmw) van CUBIERTO con la perdida NOMBRADA, Y SE DICE QUE EL CONTENIDO "
    "LLEGA IGUAL por el APPEND del paso 2 de how_might_we_framing, que dice literalmente que "
    "la pregunta no sea demasiado general ni demasiado especifica. Sellar la perdida con el "
    "atenuante dicho es mas auditable que callarla (acta 63, D8, y acta 65, D10), y es la "
    "cuenta que el pendiente 4 del acta 66 lleva. "
    "CUARTA, UNA PERDIDA QUE SE SELLA UNA SOLA VEZ CON SUS DOS SITIOS NOMBRADOS: el "
    "disparador de PROYECTO DE INNOVACION lo traen la condicion 1 de how_might_we_framing y "
    "la condicion 1 de how_might_we_hmw, y es LA MISMA perdida vista desde dos nodos. Se "
    "sella UNA vez con los DOS sitios escritos en su campo donde, en vez de dos veces, "
    "porque inflar la cuenta de perdidas duplicando una sola tambien falsea el campo. VA "
    "MARCADO DISCUTIBLE. "
    "EL SUPERVIVIENTE PASA DE 5 A 10 PASOS Y DE 2 A 3 CONDICIONES."
)

PERDIDAS16 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que de UN objetivo amplio salgan VARIAS preguntas y no una sola. El paso 1 del "
             "superviviente manda formular EL problema como UNA pregunta de diseno abierta, y "
             "el entregable de how_might_we_briefs pedia de tres a cinco preguntas"),
     "donde": "paso 1 de how_might_we_brief_social",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que la ESPECIFICIDAD se VERIFIQUE sobre la pregunta, con contexto, poblacion y "
             "restriccion, para que sea accionable. El paso 4 del superviviente documenta el "
             "contexto y las restricciones pero no los usa de vara sobre la pregunta. "
             "ATENUANTE DECLARADO: el APPEND del paso 2 de how_might_we_framing trae la "
             "calibracion de la altura de la pregunta por sus dos lados"),
     "donde": "paso 2 de how_might_we_brief_social",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que la FLEXIBILIDAD se verifique sobre LA PREGUNTA antes de idear, y no solo al "
             "listar soluciones. El paso 3 del superviviente manda listar posibles soluciones "
             "pensando ampliamente, que es un gesto posterior y sobre otra cosa. ATENUANTE "
             "DECLARADO: el APPEND del paso 2 de how_might_we_framing dice literalmente ni "
             "demasiado especifica, que limita soluciones"),
     "donde": "paso 3 de how_might_we_brief_social y paso 3 de how_might_we_briefs",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador SOCIAL, un problema social muy amplio, y el gesto de ACOTARLO para "
             "poder empezar a disenar. La condicion 2 del superviviente habla de falta de "
             "claridad sobre el alcance del problema, que es mas general y no nombra ni lo "
             "social ni el acotar"),
     "donde": "condicion 1 de how_might_we_brief_social",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("que la especificidad se exija para CONECTAR CON LA VIDA REAL de los beneficiarios "
             "y no solo con el problema abstracto. Es una de las DOS perdidas que el puesto "
             "1319 nombro de este nodo antes de que nadie fundiera nada, y el superviviente no "
             "la dice en ninguno de sus cinco pasos"),
     "donde": "paso 4 de how_might_we_briefs",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("la MISION FILANTROPICA sin punto de partida concreto como disparador. La "
             "condicion 2 del superviviente habla de falta de claridad sobre el alcance y no "
             "nombra ni la mision ni el objetivo abstracto sin punto de partida"),
     "donde": "condicion 1 de how_might_we_briefs",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("que el encuadre valga tambien para cualquier proyecto de INNOVACION y no solo "
             "para uno de diseno centrado en humanos, que es lo que dice la condicion 1 del "
             "superviviente. ES LA MISMA PERDIDA VISTA DESDE DOS NODOS y se sella UNA sola vez "
             "con sus dos sitios nombrados, en vez de dos, para no inflar el campo duplicando"),
     "donde": "condicion 1 de how_might_we_framing y condicion 1 de how_might_we_hmw",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("la calibracion de la ALTURA de la pregunta por sus dos lados, ni demasiado amplio "
             "que sea imposible de resolver ni demasiado estrecho que limite la innovacion. El "
             "paso 5 del superviviente manda revisar y ajustar la pregunta segun lo aprendido "
             "pero no dice contra que vara. ATENUANTE DECLARADO: el APPEND del paso 2 de "
             "how_might_we_framing trae esa misma calibracion entera y con sus dos puntas"),
     "donde": "paso 3 de how_might_we_hmw",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el ESTANCAMIENTO del equipo por los DOS extremos, un problema demasiado abstracto "
             "o demasiado restrictivo, como disparador. La condicion 2 del superviviente habla "
             "de falta de claridad sobre el alcance y no nombra ni el estancamiento ni los dos "
             "extremos"),
     "donde": "condicion 2 de how_might_we_hmw",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO16 = {
    # ---------------------------------------------------------------
    "how_might_we_brief_social": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # con perdida: de un objetivo salen VARIAS preguntas
            "2": ("CUBIERTO", 4),   # con perdida y atenuante: la especificidad como vara
            "3": ("CUBIERTO", 3),   # con perdida y atenuante: la flexibilidad como vara
            "4": ("APPEND",),       # validar con conocimiento local (GESTO DISTINTO)
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),   # con perdida: el disparador social y el acotar
            "2": ("APPEND",),       # objetivos institucionales o de politica publica
        },
    },
    # ---------------------------------------------------------------
    "how_might_we_briefs": {
        "pasos": {
            "1": ("APPEND",),       # identificar el objetivo macro (DE DONDE SALE LA PREGUNTA)
            "2": ("CUBIERTO", 1),   # sin perdida: el INCISO del paso 1 ya trae la formula
            "3": ("CUBIERTO", 3),   # con perdida y atenuante (sellada con sus dos sitios)
            "4": ("CUBIERTO", 4),   # con perdida: conectar con la VIDA REAL
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),   # con perdida: la mision filantropica
        },
    },
    # ---------------------------------------------------------------
    "how_might_we_framing": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # sin perdida: el INCISO del paso 1 ya trae la formula
            "2": ("APPEND",),       # LA CALIBRACION DE LA ALTURA (gesto comun que el sup no tiene)
            # EL SEGUNDO INCISO DEL ACTO: con quien se itera y el criterio de parada,
            # que el paso 5 del superviviente no dice, y ese paso no termina en punto.
            "3": ("INCISO", 5,
                  "con el equipo hasta encontrar el nivel de abstraccion correcto",
                  ", iterando la formulación "),
            "4": ("APPEND",),       # usar la pregunta como BRUJULA de todo el proceso
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida sellada una vez con sus dos sitios
            "2": ("CUBIERTO", 2),   # sin perdida
        },
    },
    # ---------------------------------------------------------------
    "how_might_we_hmw": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # sin perdida: es el insumo del paso 1, y briefs lo APPENDea
            # EL PRIMER INCISO DEL ACTO: LA FORMULA que da nombre a la familia y que
            # el superviviente NO nombra, extraida verbatim de este paso.
            "2": ("INCISO", 1,
                  "utilizando la formula '¿Como podriamos...?'",
                  ", "),
            "3": ("CUBIERTO", 5),   # con perdida y atenuante: la calibracion de la altura
            "4": ("APPEND",),       # la pregunta como TITULAR de la sesion de ideacion
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # misma perdida del disparador de innovacion, sellada arriba
            "2": ("CUBIERTO", 2),   # con perdida: el estancamiento por los dos extremos
        },
    },
}


# ======================================================================
# LOS CINCO DECLARADOS Y NO FUNDIDOS, CADA UNO CON SU MOTIVO SELLADO.
# ======================================================================

DECLARADO_ACTO12 = {
    "acto": 12,
    "miembros": [
        "cash_burn_calculation",
        "metrics_that_matter_framework",
        "validacion_hipotesis_ingresos",
        "validar_modelo_financiero",
        "verificar_modelo_ingresos",
    ],
    "superviviente_que_el_contenido_elige": (
        "NINGUNO SE ELIGE, Y ESA ES LA DECISION. No se elige superviviente porque el acto no "
        "se funde: elegirlo seria decidir la fusion y dejarla a medias. Se dice ademas a quien "
        "habria apuntado la forma, para que nadie tenga que adivinarlo: la FORMA medida es UNA "
        "SOLA VARA y apunta a metrics_that_matter_framework (4 condiciones contra un maximo de "
        "3), con la vara de PASOS empatada en 6 a tres bandas y el cableado apuntando al mismo "
        "nodo con 14 contra un maximo de 8."
    ),
    "motivo": (
        "ACTO 12 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA FINANCIERA DEL FIN DE LA VALIDACION. "
        "DECLARADO Y NO FUNDIDO PORQUE UNA FUSION ENTERA DESMENTIRIA UN VEREDICTO D DIRECTO Y "
        "ESCRITO, Y ESTE MOTIVO NO ES NINGUNO DE LOS TRES SELLADOS: VA COMO PENDIENTE DE "
        "DOCTRINA POR LA REGLA 5 Y MARCADO DISCUTIBLE EN EL REPORTE. "
        "LO PRIMERO QUE SE DICE ES QUE P.10 NO SE DISPARA, medido y no supuesto: CERO nodos "
        "puente y CERO triangulos A mas A mas D, con scripts/loop/vuelta65_puentes_del_tramo.py "
        "sobre el estado del dia (5 miembros, 10 combinaciones, 5 A, 1 D, 4 sin veredicto). Y "
        "NINGUN MIEMBRO ES PUERTA: la guarda 1B pasa por vacio y se dice en vez de darla por "
        "buena. Con P.10 sola y con la guarda 1B sola, este acto se fundiria. "
        "LO QUE LO DETIENE ES EL PUESTO 1374, UN VEREDICTO D DIRECTO ENTRE DOS MIEMBROS: "
        "cash_burn_calculation contra validacion_hipotesis_ingresos, y su razon dice, leida del "
        "dossier, que los dos parten del mismo dato, el ingreso neto de canal, y SALEN POR "
        "PUERTAS DISTINTAS, uno responde cuanto tiempo queda y el otro cuanto se puede gastar "
        "en traer al siguiente cliente. Una fusion de los CINCO a un superviviente unico "
        "deprecaria a los dos contra el mismo vivo y SELLARIA QUE REPITEN ENTRE SI, que es "
        "exactamente lo que ese veredicto niega. "
        "LA FAMILIA ES UNA Y AUN ASI NO SE FUNDE, Y LAS DOS COSAS SE DICEN JUNTAS PORQUE NO SE "
        "CONTRADICEN: la pregunta de P.5, una familia o dos, se contesta UNA y esta escrita con "
        "nombres propios en el puesto 451, que enumera los CINCO sobre el mismo modelo "
        "financiero del fin de la validacion, y la sostienen el 404 (la familia llega a TRES) y "
        "el 807 (llega a CUATRO). Pero una familia con un D dentro es una familia MEZCLADA, que "
        "es el mismo nombre que el archivo usa en el puesto 863 para la familia de la estrategia "
        "de innovacion cuando le entra su primer D. FAMILIA NO ES FUSION: la fusion exige que "
        "todos los absorbidos REPITAN al superviviente, y aqui hay dos miembros que una lectura "
        "escrita declara distintos entre si. "
        "LAS CUATRO LETRAS QUE SOSTIENEN EL DECLARADO, cada una citable: PRIMERA, P.10 cierra "
        "con que LO QUE NUNCA ES SALIDA ES FUNDIR LA COMPONENTE ENTERA PORQUE EL CIERRE "
        "TRANSITIVO LA JUNTA, y aqui cash_burn_calculation y validacion_hipotesis_ingresos solo "
        "coinciden en la componente por el camino cash_burn, metrics, verificar, validacion: la "
        "unica lectura DIRECTA entre ellos es el D. SEGUNDA, P.12 manda que el cierre "
        "transitivo convoque y LA LECTURA DECIDA, y la lectura decide D. TERCERA, el acta 66 "
        "declaro el acto 5 por la pregunta de P.5 porque fundir sellaria identidades QUE NADIE "
        "LEYO, y aqui el caso es mas fuerte y no mas debil: alguien las leyo y dijo que no. "
        "CUARTA, las alternativas estan prohibidas por letra vigente: leer los 4 pares que "
        "faltan es cribado que esta fase no tiene (banco 9.21 y regla 4), y fundir solo el "
        "subconjunto cerrado es una FUSION PARCIAL que el encargo prohibe con todas sus letras. "
        "POR QUE NO ES PARADA Y SI ES PENDIENTE DE DOCTRINA: nada se toca, ningun nodo se "
        "depreca, es reversible entero y no desmiente ninguna lectura escrita. La regla 5 manda "
        "registrar lo mejor sostenido y seguir. LO DISCUTIBLE, DICHO ANTES DE SABER SI ACIERTO: "
        "el encargo de esta vuelta enumera TRES motivos sellables (el triangulo de P.10, la "
        "guarda 1B y la respuesta DOS FAMILIAS de P.5) y esa lista se puede leer como CERRADA, "
        "y leida asi este acto tenia que fundirse. "
        "EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se depreca ninguno y no se elige "
        "superviviente. Su destino comparte carril con el pendiente 3 del acta 66: el cierre de "
        "la fase 03."
    ),
    "medicion": {
        "instrumento": "scripts/loop/vuelta65_puentes_del_tramo.py",
        "salida": "docs/loop/SALIDA_V67_PUENTES_LOTE_C.txt",
        "dossier": "docs/loop/SALIDA_V67_DOSSIER_LOTE_C.txt",
        "varas": "docs/loop/SALIDA_V67_VARAS_N_ARIAS.txt",
        "miembros": 5,
        "combinaciones": 10,
        "pares_A": 5,
        "pares_D": 1,
        "pares_sin_veredicto": 4,
        "nodos_puente": 0,
        "triangulos_puente": 0,
        "puertas_dentro": [],
        "puestos_D_internos": [1374],
    },
}

DECLARADO_ACTO13 = {
    "acto": 13,
    "miembros": [
        "channels_hypothesis_physical",
        "channels_hypothesis_web_mobile",
        "hipotesis_de_canales",
        "seleccion_canal_distribucion",
        "seleccion_canal_fisico",
    ],
    "superviviente_que_el_contenido_elige": (
        "NINGUNO SE ELIGE, Y ESA ES LA DECISION. No se elige superviviente porque el acto no se "
        "funde. Se dice ademas a quien habria apuntado la forma: la FORMA medida es CONTENIDO "
        "EMPATA (la vara de PASOS empata en 5 a cuatro bandas y la de CONDICIONES en 2 a tres), "
        "asi que por P.8 decidiria EL CABLEADO SOLO, y el cableado apunta a hipotesis_de_canales "
        "con 8 contra un maximo de 7. Ese nodo ES PUERTA, o sea que sobrevivir podria; lo que no "
        "puede es absorber a la SEGUNDA puerta."
    ),
    "motivo": (
        "ACTO 13 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA SELECCION DE CANAL DE "
        "DISTRIBUCION. DECLARADO Y NO FUNDIDO CON LA GUARDA 1B COMO MOTIVO SELLADO, POR EL "
        "CARRIL QUE EL ACTA 65 ADJUDICO Y QUE ESTA PAGINA YA REGISTRA: un acto que no se pueda "
        "fundir sin absorber una puerta cierra DECLARADO con la guarda 1B como motivo, SIN "
        "improvisar fusiones parciales que ninguna letra escribe. ES LA PRIMERA VEZ DE LA "
        "CAMPANA QUE LA GUARDA 1B ES EL MOTIVO UNICO Y NO EL SEGUNDO. "
        "LO MEDIDO, Y ES LO QUE MANDA: DOS de los cinco miembros son PUERTA (semilla de entrada "
        "o extremo de puente aprobado), hipotesis_de_canales y seleccion_canal_distribucion, "
        "medido con scripts/loop/varas_n_arias_del_tramo.py contra el universo protegido de 256 "
        "ids. Con DOS puertas dentro, cualquier eleccion de superviviente absorbe a la otra, y "
        "la guarda 1B lo prohibe. NO HAY SALIDA DE FUSION QUE NO ROMPA LA GUARDA. "
        "Y P.10 NO SE DISPARA, se dice en vez de sumar razones que no estan: CERO pares D "
        "internos, CERO nodos puente y CERO triangulos (5 miembros, 10 combinaciones, 8 A, 0 D, "
        "2 sin veredicto). La razon del DECLARADO es UNA y no dos. "
        "LA PREGUNTA DE P.5 SE CONTESTA IGUAL Y SE DEJA ESCRITA, porque el acto se lee entero "
        "aunque no se funda: ES UNA FAMILIA, y no es lectura mia sino declaracion del archivo. "
        "El puesto 609 dice FAMILIA DECLARADA y nombra el racimo LA SELECCION DE CANAL de seis "
        "miembros, y el 762 lo repite; el 214 dice que la familia del canal del nucleo llega a "
        "CUATRO nodos y el 1488 cierra que el racimo NO crece, sigue en SEIS miembros, su "
        "cobertura pasa a 8 de 15 con los ocho en A, y SIGUE SIENDO SUB-PURO. "
        "UNA COSA MAS QUE SE DICE EN VEZ DE CALLARSE: el puesto 537 declara un CHOQUE CON LA "
        "DIRECCION DE FUSION DE LA RELECTURA R1 y avisa con todas sus letras de que LA "
        "DIRECCION DE FUSION NO SE PUEDE CERRAR PAR POR PAR, porque fisico y digital son "
        "especializaciones que el nodo general NO lleva. No es el motivo sellado, pero apunta al "
        "mismo sitio que la guarda. "
        "EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se depreca ninguno y no se elige "
        "superviviente. Su destino comparte carril con el pendiente 3 del acta 66: el cierre de "
        "la fase 03."
    ),
    "medicion": {
        "instrumento": "scripts/loop/vuelta65_puentes_del_tramo.py",
        "salida": "docs/loop/SALIDA_V67_PUENTES_LOTE_C.txt",
        "dossier": "docs/loop/SALIDA_V67_DOSSIER_LOTE_C.txt",
        "varas": "docs/loop/SALIDA_V67_VARAS_N_ARIAS.txt",
        "miembros": 5,
        "combinaciones": 10,
        "pares_A": 8,
        "pares_D": 0,
        "pares_sin_veredicto": 2,
        "nodos_puente": 0,
        "triangulos_puente": 0,
        "puertas_dentro": ["hipotesis_de_canales", "seleccion_canal_distribucion"],
        "puestos_D_internos": [],
    },
}

DECLARADO_ACTO14 = {
    "acto": 14,
    "miembros": [
        "construccion_de_leverage",
        "estrategia_competencia_vcs",
        "gestion_multiples_term_sheets",
        "leverage_en_negociacion_con_vcs",
        "tecnica_anclaje_negociacion",
    ],
    "superviviente_que_el_contenido_elige": (
        "NINGUNO SE ELIGE, Y ESA ES LA DECISION. Se dice ademas a quien habria apuntado la "
        "forma, y aqui la respuesta es parte del motivo: la FORMA medida es CONTENIDO EMPATA "
        "(la vara de PASOS empata en 5 entre construccion_de_leverage y "
        "gestion_multiples_term_sheets, y la de CONDICIONES en 2 entre construccion_de_leverage "
        "y leverage_en_negociacion_con_vcs), asi que por P.8 decidiria EL CABLEADO SOLO, y el "
        "cableado apunta a tecnica_anclaje_negociacion con 7 contra un maximo de 6. ES "
        "EXACTAMENTE EL NODO QUE LA LECTURA DEJA FUERA DE LA FAMILIA."
    ),
    "motivo": (
        "ACTO 14 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA PALANCA FRENTE A LOS "
        "INVERSIONISTAS. DECLARADO Y NO FUNDIDO CON P.5 COMO MOTIVO SELLADO, POR EL TERCER "
        "MOTIVO QUE EL ACTA 66 ADJUDICO POR EXTENSION Y QUE ESTA PAGINA REGISTRA: un acto cuyo "
        "P.5 contesta que NO ES UNA FAMILIA cierra DECLARADO Y NO FUNDIDO aunque P.10 no se "
        "dispare. EL PRECEDENTE ES EL ACTO 5 DE LA VUELTA 66 Y ESTE ES EL SEGUNDO USO DEL "
        "CARRIL. "
        "LO PRIMERO QUE SE DICE ES QUE P.10 NO SE DISPARA, medido: CERO pares D internos, CERO "
        "nodos puente y CERO triangulos (5 miembros, 10 combinaciones, 7 A, 0 D, 3 sin "
        "veredicto). Y NINGUN MIEMBRO ES PUERTA: la guarda 1B pasa por vacio y se dice. Con "
        "P.10 sola y con la guarda 1B sola, este acto se fundiria. "
        "LA PREGUNTA DE P.5 SE CONTESTA SOBRE EL TEXTO ESTABLE Y LA RESPUESTA ES NO ES UNA: HAY "
        "UN PURO DE CUATRO Y UN QUINTO QUE LA LECTURA DEJA FUERA CON TODAS SUS LETRAS. El puesto "
        "1030 declara, verbatim del dossier, que CON ESTE PAR NACE EL PRIMER PURO DE CUATRO, y "
        "enumera la familia: construccion_de_leverage, leverage_en_negociacion_con_vcs, "
        "gestion_multiples_term_sheets y estrategia_competencia_vcs, CUATRO miembros, SEIS pares "
        "posibles, LOS SEIS LEIDOS Y LOS SEIS EN A, y anade que es el PRIMER PURO DE CUATRO "
        "MIEMBROS del archivo. Cuatro, no cinco. "
        "Y EL QUINTO NO ESTA FUERA POR OLVIDO: el puesto 878 lo levanta por el BARRIDO DE LAS A "
        "del banco 9.15, lo mira y decide, y su razon dice que LA LECTURA LO DEJA FUERA PORQUE "
        "SU OBJETO ES COMO NEGOCIAR TERMINOS Y NO COMO GENERAR COMPETENCIA ENTRE INVERSORES. El "
        "mismo puesto llama a tecnica_anclaje_negociacion EL PASO CUATRO CONTADO COMO NODO, sin "
        "procedimiento propio, y cierra que el candidato SE LEVANTA POR EL ARCHIVO Y SE RESUELVE "
        "LEYENDO, QUE ES EXACTAMENTE PARA LO QUE SE ESCRIBIO LA REGLA. Son DOS objetos y no uno: "
        "generar competencia entre inversores, y anclar terminos dentro de una negociacion. "
        "LA VARA APUNTA AL NODO EXCLUIDO, Y ESO NO ES UN DETALLE: fundir el acto entero pondria "
        "de superviviente al mismo nodo que la lectura saco de la familia, y sellaria que el "
        "PURO DE CUATRO repite a un nodo que el archivo declara de otro objeto. P.12 manda que "
        "los veredictos DIRECTOS gobiernen, y el directo aqui dice que el objeto es otro. "
        "LAS ALTERNATIVAS, RECORRIDAS EN VEZ DE ELEGIR LA COMODA: leer los 3 pares que faltan es "
        "cribado que esta fase no tiene (banco 9.21 y regla 4); fundir solo el PURO DE CUATRO y "
        "dejar fuera al quinto es una FUSION PARCIAL, que el encargo prohibe con todas sus "
        "letras; y fundir entero desmiente la lectura del 878. ASI QUE NO SE FUNDE NADA Y SE "
        "DECLARA. "
        "EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se depreca ninguno y no se elige "
        "superviviente. Su destino comparte carril con el pendiente 3 del acta 66: el cierre de "
        "la fase 03."
    ),
    "medicion": {
        "instrumento": "scripts/loop/vuelta65_puentes_del_tramo.py",
        "salida": "docs/loop/SALIDA_V67_PUENTES_LOTE_C.txt",
        "dossier": "docs/loop/SALIDA_V67_DOSSIER_LOTE_C.txt",
        "varas": "docs/loop/SALIDA_V67_VARAS_N_ARIAS.txt",
        "miembros": 5,
        "combinaciones": 10,
        "pares_A": 7,
        "pares_D": 0,
        "pares_sin_veredicto": 3,
        "nodos_puente": 0,
        "triangulos_puente": 0,
        "puertas_dentro": [],
        "puestos_D_internos": [],
    },
}

DECLARADO_ACTO15 = {
    "acto": 15,
    "miembros": [
        "construccion_de_valor_percibido",
        "ecuacion_de_valor",
        "ecuacion_de_valor_cliente",
        "ecuacion_de_valor_venta",
        "prevencion_objeciones_vs_manejo",
    ],
    "superviviente_que_el_contenido_elige": (
        "NINGUNO SE ELIGE, Y ESA ES LA DECISION. Se dice ademas a quien habria apuntado la "
        "forma: la FORMA medida es TODAS DE ACUERDO y las tres varas apuntan al MISMO miembro, "
        "prevencion_objeciones_vs_manejo (6 pasos contra un maximo de 4, 3 condiciones contra 2 "
        "y cableado 9 contra un maximo de 4). Ese nodo ES PUERTA, o sea que sobrevivir podria y "
        "no habria choque de puerta; lo que no puede es absorber a la SEGUNDA puerta, "
        "ecuacion_de_valor."
    ),
    "motivo": (
        "ACTO 15 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA ECUACION DE VALOR DE RACKHAM. "
        "DECLARADO Y NO FUNDIDO CON LA GUARDA 1B COMO MOTIVO SELLADO, POR EL MISMO CARRIL DEL "
        "ACTO 13 DE ESTE LOTE: un acto que no se pueda fundir sin absorber una puerta cierra "
        "DECLARADO con la guarda 1B como motivo. "
        "Y SE DICE PRIMERO LO QUE ESTE ACTO NO ES, PORQUE SE PARECE Y NO LO ES: NO ES UN CHOQUE "
        "DE PUERTA. En el choque, la vara de contenido apunta a un miembro y la puerta es OTRO, "
        "y el carril escrito manda fundir A LA PUERTA y registrar el choque (acta 54, pregunta "
        "1, con el acto 9 de la vuelta 66 de precedente nuevo). Aqui LAS TRES VARAS APUNTAN A LA "
        "PUERTA, o sea que no hay nada que chocar. Lo que hay es una SEGUNDA puerta dentro, "
        "ecuacion_de_valor, que cualquier fusion tendria que absorber. "
        "LO MEDIDO: DOS de los cinco miembros son PUERTA, ecuacion_de_valor y "
        "prevencion_objeciones_vs_manejo, medido con scripts/loop/varas_n_arias_del_tramo.py "
        "contra el universo protegido de 256 ids. NO HAY SALIDA DE FUSION QUE NO ROMPA LA "
        "GUARDA. "
        "Y P.10 NO SE DISPARA, se dice en vez de sumar razones que no estan: CERO pares D "
        "internos, CERO nodos puente y CERO triangulos (5 miembros, 10 combinaciones, 5 A, 0 D, "
        "5 sin veredicto). La razon del DECLARADO es UNA y no dos. "
        "LA PREGUNTA DE P.5 SE CONTESTA IGUAL Y SE DEJA ESCRITA, porque el acto se lee entero "
        "aunque no se funda, Y LA RESPUESTA TIENE UN MATIZ QUE SE DICE EN VEZ DE ALISARSE: hay "
        "un nucleo de la ECUACION DE VALOR de cuatro miembros que el archivo declara y mide, "
        "el puesto 217 lo levanta como RACIMO NUEVO de tres y el 950 lo lleva a CUATRO con "
        "construccion_de_valor_percibido, DEGRADANDOLO A SUB-PURO con dos lecturas por hacer. El "
        "quinto, prevencion_objeciones_vs_manejo, entra por el puesto 1146, cuya razon dice EL "
        "MODELO CONTRA LA REGLA QUE YA LO CONTIENE y avisa de que NO ES UN PAR DE MADRE E HIJO "
        "SINO DOS NODOS LATERALES, y nombra las perdidas de los dos lados. Con la guarda 1B "
        "deteniendo la fusion, la pregunta de si el quinto es de la misma familia NO HACE FALTA "
        "CONTESTARLA HOY y no se contesta: se deja medida y escrita para quien la necesite. "
        "EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se depreca ninguno y no se elige "
        "superviviente. Su destino comparte carril con el pendiente 3 del acta 66: el cierre de "
        "la fase 03."
    ),
    "medicion": {
        "instrumento": "scripts/loop/vuelta65_puentes_del_tramo.py",
        "salida": "docs/loop/SALIDA_V67_PUENTES_LOTE_C.txt",
        "dossier": "docs/loop/SALIDA_V67_DOSSIER_LOTE_C.txt",
        "varas": "docs/loop/SALIDA_V67_VARAS_N_ARIAS.txt",
        "miembros": 5,
        "combinaciones": 10,
        "pares_A": 5,
        "pares_D": 0,
        "pares_sin_veredicto": 5,
        "nodos_puente": 0,
        "triangulos_puente": 0,
        "puertas_dentro": ["ecuacion_de_valor", "prevencion_objeciones_vs_manejo"],
        "puestos_D_internos": [],
    },
}

DECLARADO_ACTO17 = {
    "acto": 17,
    "miembros": [
        "estrategia_de_innovacion_arenas",
        "estrategia_de_innovacion_de_producto",
        "estrategia_de_innovacion_y_tecnologia",
        "estrategia_innovacion_producto",
        "seleccion_arenas_estrategicas",
    ],
    "superviviente_que_el_contenido_elige": (
        "NINGUNO SE ELIGE, Y ESA ES LA DECISION. Se dice ademas a quien habria apuntado la "
        "forma: la FORMA medida es UNA SOLA VARA y apunta a seleccion_arenas_estrategicas (4 "
        "condiciones contra un maximo de 3), con la vara de PASOS empatada en 6 entre "
        "estrategia_de_innovacion_de_producto y seleccion_arenas_estrategicas y el cableado "
        "empatado en 14 entre estrategia_innovacion_producto y seleccion_arenas_estrategicas."
    ),
    "motivo": (
        "ACTO 17 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA ESTRATEGIA DE INNOVACION DE "
        "PRODUCTO DE COOPER. DECLARADO Y NO FUNDIDO POR P.10, CON SU TRIANGULO MEDIDO, Y ES EL "
        "PRIMERO DE LOS SEIS ACTOS CON PUENTE QUE EL ACTA 66 DEJO CONTADOS AL CIERRE. "
        "LO MEDIDO, con scripts/loop/vuelta65_puentes_del_tramo.py sobre el estado del dia: 5 "
        "miembros, 10 combinaciones, 6 A, 2 D, 2 sin veredicto, UN nodo puente y DOS triangulos "
        "A mas A mas D. El puente es estrategia_de_innovacion_arenas, que tiene A con "
        "estrategia_de_innovacion_de_producto y A con estrategia_de_innovacion_y_tecnologia "
        "siendo esos dos D entre si (puesto 530), y A con estrategia_de_innovacion_y_tecnologia "
        "y A con estrategia_innovacion_producto siendo esos dos D entre si (puesto 863). "
        "LOS DOS D SON DE UNA PIEZA Y NO UN ACCIDENTE, y los dos hablan del MISMO nodo: el 863 "
        "dice LA MADRE Y SU PIEZA DE ARENAS y declara que estrategia_de_innovacion_y_tecnologia "
        "desarrolla con un procedimiento propio la UNA LINEA que la madre despacha, con el "
        "metodo de seleccion, la frontera del alcance y el uso como filtro de gate que no estan "
        "en ningun paso de la madre. El 530 es una CORRECCION DECLARADA del 13 ago 2026 por "
        "relectura conjunta encargada por el auditor: era A, se midio paso por paso contra el "
        "grafo, la afirmacion resulto FALSA y paso a D por la vara del banco 9.6.1, con el mismo "
        "esqueleto del 863. Una fusion entera desmentiria las dos. "
        "Y HAY UNA SEGUNDA RAZON INDEPENDIENTE, QUE SE DICE EN VEZ DE CALLARSE: "
        "estrategia_de_innovacion_y_tecnologia ES PUERTA, y no es el miembro al que apunta la "
        "vara, asi que cualquier fusion tendria que absorberla y la guarda 1B lo prohibe. Este "
        "acto tiene DOS motivos independientes, como el acto 1 de la vuelta 65, y no uno. "
        "LAS TRES SALIDAS DE P.10, RECORRIDAS UNA A UNA: leer los 2 pares que faltan es la unica "
        "que resuelve de verdad y es cribado que esta fase no tiene; releer contra el "
        "superviviente no aplica porque no hay superviviente elegido; y fundir solo el "
        "subconjunto CERRADO pide que TODAS las lecturas esten hechas, y no lo estan. ASI QUE NO "
        "SE FUNDE NADA Y SE DECLARA. "
        "UNA CITA QUE SE TRAE COMO CONTRASTE Y NO COMO FUENTE: el puesto 460 dice que ESTA "
        "FAMILIA YA ESTA DECLARADA COMO RACIMO NUEVO DE SEIS NODOS Y SE DECIDE EN MESA, NO AQUI. "
        "MEDIDO HOY CONTRA EL FICHERO DEL TRAMO, este acto NO tiene dueno en mesa ni en "
        "destejido (el campo duenos_mesa_o_destejido esta vacio), que es el criterio con el que "
        "OP-U-02 abrio su universo en la vuelta 63. La discrepancia se declara y no se resuelve "
        "copiando: la razon habla de una mesa que ninguna operacion escrita nombra, y el acto "
        "cierra DECLARADO igual, asi que ninguna de las dos lecturas mueve un nodo. "
        "EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se depreca ninguno y no se elige "
        "superviviente. Su destino comparte carril con el pendiente 3 del acta 66: el cierre de "
        "la fase 03."
    ),
    "medicion": {
        "instrumento": "scripts/loop/vuelta65_puentes_del_tramo.py",
        "salida": "docs/loop/SALIDA_V67_PUENTES_LOTE_C.txt",
        "dossier": "docs/loop/SALIDA_V67_DOSSIER_LOTE_C.txt",
        "varas": "docs/loop/SALIDA_V67_VARAS_N_ARIAS.txt",
        "miembros": 5,
        "combinaciones": 10,
        "pares_A": 6,
        "pares_D": 2,
        "pares_sin_veredicto": 2,
        "nodos_puente": 1,
        "triangulos_puente": 2,
        "puertas_dentro": ["estrategia_de_innovacion_y_tecnologia"],
        "puestos_D_internos": [530, 863],
    },
}

LOTE_C = {
    "titulo": ("LOTE C DEL TRAMO UNICO DE OP-U-02, PREFIJO SIN SALTOS DEL orden_universo DE LO "
               "QUE QUEDA: LOS ACTOS 12, 13, 14, 15, 16 Y 17, SEIS ACTOS Y 30 NODOS. El acto 16 "
               "cierra FUNDIDO; los actos 12, 13, 14, 15 y 17 cierran DECLARADOS Y NO FUNDIDOS "
               "con motivo sellado. El acto 13 y el acto 15 son las DOS PRIMERAS veces de la "
               "campana en que la guarda 1B es el motivo UNICO de un DECLARADO; el acto 14 es el "
               "SEGUNDO uso del carril que el acta 66 adjudico (P.5 contesta que no es una "
               "familia); y el acto 12 estrena una situacion sin letra, un veredicto D DIRECTO "
               "sin triangulo que cerrar, que va como PENDIENTE DE DOCTRINA y marcado "
               "DISCUTIBLE"),
    "actos": [
        {
            "orden": 16,
            "superviviente": SUP16,
            "motivo": MOTIVO16,
            "nota": NOTA16,
            "reparto": REPARTO16,
            "perdidas": PERDIDAS16,
        },
    ],
    "declarados": [DECLARADO_ACTO12, DECLARADO_ACTO13, DECLARADO_ACTO14,
                   DECLARADO_ACTO15, DECLARADO_ACTO17],
}
