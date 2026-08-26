# -*- coding: utf-8 -*-
"""_v69_lote_e.py . EL CONTENIDO EDITORIAL DEL LOTE E DEL TRAMO UNICO DE OP-U-02.

NO ES UN INSTRUMENTO: es el texto del lote. La maquina que lo sella es
scripts/loop/generar_plan_del_lote.py, que entra aqui por --contenido _v69_lote_e.

EL LOTE SE DECLARA AL ABRIRLO. Abre con LA FUSION ADJUDICADA DEL ACTO 18 (acta 68,
adjudicaciones 1 y 3: el superviviente es alianzas_cross_industry, la fusion se
ejecuta como PRIMERA operacion de este lote, dentro de ESTE plan propio, y el acto
CUENTA en la declaracion como uno de los que cierran ENTEROS). Despues sigue el
PREFIJO SIN SALTOS del orden_universo de lo que queda del tramo fijado en
docs/loop/TRAMO_UNICO_OPU02_V64.jsonl desde el acto 25 (el lote A de la vuelta 65
cerro los actos 1 y 3; el lote B de la vuelta 66 cerro el 5, 7, 8, 9, 10 y 11; el
lote C de la vuelta 67 cerro el 12 al 17; el lote D de la vuelta 68 cerro el 19,
20, 21, 22, 23 y 24 y dejo el 18 ABIERTO EN TRANSITO).

LA DECLARACION: SEIS ACTOS CIERRAN ENTEROS Y SON 22 NODOS. El 18 (fusion
adjudicada), el 25, el 26, el 29 y el 30 cierran FUNDIDOS, y el 27 cierra
DECLARADO Y NO FUNDIDO con el TRIANGULO DE P.10 como motivo sellado.

EL TOPE DEL PREFIJO ES ESTRUCTURAL Y SE DICE, en vez de dejarlo como un numero
elegido: el siguiente del prefijo es el ACTO 31, y ESE ACTO TIENE DUENO. Medido
hoy sobre el fichero fijado del tramo, su campo duenos_cualquier_operacion trae
OP-F-04-WEI y OP-S-04. El encargo prohibe FUNDIR un acto con dueno con todas sus
letras, y el acto 31 no trae NINGUNO de los cuatro motivos sellados con los que
podria cerrar DECLARADO (cero pares D internos, cero nodos puente, cero
triangulos, una sola familia y una sola puerta, medido). O sea que NO PODRIA
CERRAR ENTERO, y el contrato del lote es entregar lo declarado: por eso el tope
cae ANTES de el y no despues. El acto 31 se lee, se mide y se deja donde esta.

EL REPARTO VA POR ABSORBIDO en la clave reparto, que es la forma que la vuelta 65
estreno para los actos de mas de dos miembros.
"""

# ======================================================================
# ACTO 18: LA FAMILIA DE LA ALIANZA SECTORIAL DE SOSTENIBILIDAD.
# CUATRO miembros, TRES pares internos con veredicto y los TRES en A,
# CERO D, CERO nodos puente y CERO triangulos. NINGUN MIEMBRO ES PUERTA.
# FORMA medida: EMPATE SIN VARA (pasos 4 a cuatro bandas, condiciones 2 a
# cuatro bandas, cableado empatado en 3). NINGUNA VARA APUNTA, y por eso
# EL SUPERVIVIENTE NO LO ELIGE EL EJECUTOR: lo adjudico el auditor en el
# acta 68, seccion 5.1, por el carril del transito que el acta 67 abrio.
# ======================================================================

SUP18 = "alianzas_cross_industry"

MOTIVO18 = (
    "ACTO 18 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA ALIANZA SECTORIAL DE "
    "SOSTENIBILIDAD, Y ES LA PRIMERA FUSION DE LA CAMPANA CUYO SUPERVIVIENTE NO LO ELIGE EL "
    "EJECUTOR. "
    "EL SUPERVIVIENTE ESTA ADJUDICADO POR EL AUDITOR, Y ESA ES LA MITAD DEL MOTIVO. La forma "
    "medida de este acto es EMPATE SIN VARA: pasos 4 a CUATRO bandas, condiciones 2 a CUATRO "
    "bandas y el cableado empatado en 3, medido con "
    "scripts/loop/varas_n_arias_del_tramo.py sobre el estado del dia. NINGUNA VARA APUNTA y "
    "el desempate de P.8 tampoco desempata, que es la fila de P.8 que dice EMPATADO Y EL "
    "CABLEADO TAMBIEN: SE TRAE AL AUDITOR. Por el carril del EMPATE SIN VARA (acta 67, "
    "pregunta 2, registrado en 03_FUSIONES.md) el ejecutor de la vuelta 68 escribio el caso "
    "entero, NO eligio, y dejo el acto ABIERTO EN TRANSITO; el acta 68 lo adjudico en su "
    "seccion 5.1: EL SUPERVIVIENTE ES alianzas_cross_industry. Este plan EJECUTA esa "
    "adjudicacion, no la re-decide. "
    "LAS CUATRO LETRAS DE LA ADJUDICACION, copiadas del acta: PRIMERA, EL ALCANCE, es el "
    "unico de los cuatro que apunta al MERCADO ENTERO (el poder de compra colectivo para "
    "mover el mercado hacia otro tipo de producto) y los otros tres caben dentro de ese marco "
    "mientras el marco no cabe en ninguno de los tres. SEGUNDA, EL REPARTO CON MENOS PERDIDA, "
    "sus piezas ya alojan lo propio de los otros con la costura mas corta. TERCERA, LO "
    "BUSCABLE, trae los nombres propios EICC y AIM-PROGRESS que la razon del puesto 1903 "
    "senala como lo que vuelve buscable el paso. CUARTA, EL CABLEADO NO LO DESMIENTE, empata "
    "en cabeza con co_opetition_industria en 3. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE: los CUATRO "
    "miembros son del MISMO LIBRO (The Green to Gold Business Play, de Esty), tienen TRES "
    "pares internos con veredicto escrito y los TRES son de clase A (puestos 1797, 1871 y "
    "1903), hay CERO pares D internos, CERO nodos puente y CERO triangulos, medido con "
    "scripts/loop/vuelta65_puentes_del_tramo.py sobre el estado del dia. Y LA FAMILIA NO ES "
    "LECTURA MIA SINO DECLARACION DEL ARCHIVO: el 1871 la ve pasar de DOS a TRES nodos por "
    "cierre transitivo y el 1903 de TRES a CUATRO, con cobertura 3 de 6 y forma PROVISIONAL. "
    "GUARDA 1B: NINGUNO de los cuatro miembros es puerta (ni semilla de entrada ni extremo de "
    "puente aprobado), medido contra el universo protegido de 256 ids. La guarda pasa por "
    "vacio y se dice. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto "
    "(duenos_mesa_o_destejido y duenos_cualquier_operacion), medido hoy; y NINGUNA entrada de "
    "docs/plan/INVENTARIO.jsonl que no sea de tipo acto nombra a ninguno de los cuatro "
    "miembros, medido hoy tambien. Por el criterio que el acta 68 adjudico en su seccion 5.2, "
    "el dueno es EL MEDIDO y aqui no hay ninguno."
)

NOTA18 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado en vez de maquillado. LAS CINCO PIEZAS "
    "QUE EL ACTA 68 MANDO CONSERVAR O SELLAR QUEDAN LAS CINCO CONSERVADAS, ninguna sellada "
    "como perdida, y se dicen una a una con su destino medido: publicar y monitorear el "
    "cumplimiento colectivo (co_opetition_industria, paso 4) va de APPEND; aplicar el "
    "estandar conjunto a los proveedores compartidos (trabajo_colectivo_estandares_industria, "
    "paso 4) va de APPEND; el marco nombrado Responsible Care "
    "(trabajo_colectivo_estandares_industria, paso 3) va de APPEND; el encuadre por riesgo "
    "reputacional compartido (trabajo_colectivo_estandares_industria, condicion 1) va de "
    "APPEND; y el test del poder de mercado como ARRANQUE EXPLICITO (colaboracion_sectorial, "
    "paso 1) va de INCISO ADOSADO AL PASO 1 del superviviente, que es la unica forma de que "
    "siga siendo un arranque: un APPEND lo habria puesto al final. "
    "UN SOLO INCISO Y AL PASO 1, extraido VERBATIM del nodo que muere y con el paso "
    "resultante impreso por el generador. El paso 1 del superviviente NO termina en punto, "
    "asi que la guarda de la JUNTURA ROTA no salta. "
    "CUATRO APPEND DE PASO Y DOS DE CONDICION, y el nodo crece de 4 pasos a 7 y de 2 "
    "condiciones a 4. La eleccion es la del carril del D8 del acta 67 y del D4 del acta 68: "
    "catalogo mas rico con solapes declarados por encima de CUBIERTO que calla texto vivo. "
    "LOS DOS APPEND DE CONDICION SON DISPARADORES DISTINTOS, que es la unica puerta por la "
    "que el acta 55 (pregunta 5) deja pasar una condicion de APPEND mientras el INCISO de "
    "condiciones no exista: el RIESGO REPUTACIONAL COMPARTIDO (que el superviviente no tiene: "
    "el suyo es el poder de compra insuficiente y el desafio sistemico) y la DEPENDENCIA DE "
    "LOS MISMOS PROVEEDORES CRITICOS, que es ademas el disparador propio del paso 4 que este "
    "mismo acto adosa. "
    "UNA PERDIDA CON DOS SEDES EN UN SOLO CAMPO donde, por el criterio que el acta 67 "
    "adjudico en su D10: LA FILA ES POR PIEZA QUE SE PIERDE, NO POR SITIO DONDE VIVIA. El "
    "canal de convocatoria por LAS ASOCIACIONES INDUSTRIALES EXISTENTES vive en el paso 2 de "
    "co_opetition_industria y en el paso 2 de colaboracion_sectorial, y va en UNA fila con "
    "los dos sitios nombrados. "
    "TRES PERDIDAS CON ATENUANTE DECLARADO, contadas por maquina sobre esta misma lista y no "
    "de memoria, que es la regla que sale de la caida del D9 de la vuelta 68; DOS de ellas "
    "son de la especie del pendiente 4 (ya lo dice el APPEND de un hermano) y la cuenta de "
    "ese pendiente crece y se publica."
)

PERDIDAS18 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL CANAL DE LA CONVOCATORIA: convocar MEDIANTE LAS ASOCIACIONES INDUSTRIALES "
             "EXISTENTES, que la razon del puesto 1797 llama la unica linea que dice por donde "
             "se convoca sin que parezca acuerdo entre competidores. El paso 2 del "
             "superviviente manda BUSCAR COALICIONES EXISTENTES o formar una nueva, que es el "
             "mismo terreno visto desde quien se suma y no desde quien convoca. ATENUANTE "
             "DECLARADO: ese paso 2 trae ademas los nombres propios de las coaliciones, asi "
             "que el sitio donde buscarlas no se pierde. UNA SOLA PIEZA CON DOS SEDES, sellada "
             "una vez con las dos nombradas (acta 67, D10)"),
     "donde": "paso 2 de co_opetition_industria y paso 2 de colaboracion_sectorial",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("las METAS COMPARTIDAS DE DESEMPENO AMBIENTAL, o sea la parte MEDIBLE del pacto. "
             "El paso 3 del superviviente define ESTANDARES COMUNES DE CONDUCTA social y "
             "ambiental para toda la industria, que es la regla, pero en ningun paso pide "
             "metas de desempeno contra las que medirse"),
     "donde": "paso 3 de co_opetition_industria",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("las METRICAS Y COMPROMISOS CONJUNTOS para los proveedores comunes, dichos como "
             "definicion propia. ATENUANTE DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: el "
             "APPEND del paso 4 de trabajo_colectivo_estandares_industria manda APLICAR EL "
             "ESTANDAR CONJUNTO A PROVEEDORES COMPARTIDOS, o sea que la palanca hacia arriba "
             "en la cadena llega entera por el hermano; lo que no llega es la palabra "
             "METRICAS"),
     "donde": "paso 4 de colaboracion_sectorial",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("el RIESGO REPUTACIONAL COMPARTIDO dicho como PRIMER PASO, o sea como test de "
             "arranque y no como disparador. ATENUANTE DECLARADO, Y ES LA ESPECIE DEL "
             "PENDIENTE 4: el encuadre llega entero por el APPEND de la condicion 1 de este "
             "mismo nodo, pero cambia de sitio, de paso a condicion"),
     "donde": "paso 1 de trabajo_colectivo_estandares_industria",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("la CRISIS REGULATORIA compartida como disparador. La mitad reputacional de esa "
             "condicion llega entera por el APPEND de la condicion 1 de "
             "trabajo_colectivo_estandares_industria; lo que se pierde es la palabra "
             "REGULATORIA, que es el unico sitio del acto donde el disparador es el regulador "
             "y no el mercado ni la prensa"),
     "donde": "condicion 1 de co_opetition_industria",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("las ECONOMIAS DE ESCALA en la colaboracion sectorial como disparador. Las dos "
             "condiciones del superviviente miran la DEBILIDAD (el poder de compra individual "
             "insuficiente) y el PROBLEMA (el desafio sistemico); ninguna mira el AHORRO de "
             "hacerlo juntos"),
     "donde": "condicion 2 de colaboracion_sectorial",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("el alcance del test sobre los PROVEEDORES: no tener poder individual SOBRE "
             "PROVEEDORES. La condicion 1 del superviviente mide el poder de compra sobre EL "
             "MERCADO, que es mas ancho y por eso no dice lo mismo. ATENUANTE DECLARADO Y "
             "MEDIDO: el INCISO al paso 1 de este mismo acto adosa el test del poder de "
             "mercado VERBATIM como arranque, asi que el test no se pierde; lo que se pierde "
             "es el objeto proveedores"),
     "donde": "condicion 1 de colaboracion_sectorial",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO18 = {
    # ---------------------------------------------------------------
    "co_opetition_industria": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # sin perdida: identificar el problema comun del sector
            "2": ("CUBIERTO", 2),   # con perdida de dos sedes: el canal de la convocatoria
            "3": ("CUBIERTO", 3),   # con perdida: las metas de desempeno medibles
            "4": ("APPEND",),       # PUBLICAR Y MONITOREAR (pieza 1 de las cinco del acta 68)
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: la crisis REGULATORIA
            "2": ("CUBIERTO", 1),   # sin perdida: los esfuerzos individuales no bastan
        },
    },
    # ---------------------------------------------------------------
    "colaboracion_sectorial": {
        "pasos": {
            # EL UNICO INCISO DEL ACTO: el test del poder de mercado, que el acta 68
            # manda conservar COMO ARRANQUE EXPLICITO. Un APPEND lo habria puesto al
            # final; el INCISO lo deja dentro del PASO 1, que es donde arranca.
            "1": ("INCISO", 1,
                  "si la empresa tiene suficiente poder de mercado para exigir cambios individualmente",
                  ", evaluando antes "),
            "2": ("CUBIERTO", 2),   # segunda sede de la perdida del canal de convocatoria
            "3": ("CUBIERTO", 3),   # sin perdida: la agenda compartida son los estandares comunes
            "4": ("CUBIERTO", 4),   # con perdida y atenuante: las metricas para proveedores
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida y atenuante medido: el objeto proveedores
            "2": ("CUBIERTO", 2),   # con perdida: las economias de escala
        },
    },
    # ---------------------------------------------------------------
    "trabajo_colectivo_estandares_industria": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # con perdida y atenuante: el riesgo reputacional como paso
            "2": ("CUBIERTO", 3),   # sin perdida: convocar para definir estandares comunes
            "3": ("APPEND",),       # EL MARCO Responsible Care (pieza 5 de las cinco)
            "4": ("APPEND",),       # A LOS PROVEEDORES COMPARTIDOS (pieza 2 de las cinco)
        },
        "condiciones": {
            "1": ("APPEND",),       # EL RIESGO REPUTACIONAL COMPARTIDO (pieza 4 de las cinco)
            "2": ("APPEND",),       # LOS MISMOS PROVEEDORES CRITICOS (DISPARADOR DISTINTO)
        },
    },
}


# ======================================================================
# ACTO 25: LA FAMILIA DE LA ETAPA DE INVESTIGACION EN LA VENTA.
# CUATRO miembros, CINCO pares internos con veredicto y los CINCO en A,
# CERO D, CERO nodos puente y CERO triangulos. UNA PUERTA DENTRO, y por
# la letra de la guarda 1B (una sola puerta: el acto SI se funde y la
# puerta SOBREVIVE, acta 54 pregunta 1) esa puerta es el superviviente.
# FORMA medida: CONTENIDO EMPATA, y el cableado apunta a LA MISMA PUERTA.
# ======================================================================

SUP25 = "enfoque_etapa_investigacion"

MOTIVO25 = (
    "ACTO 25 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA ETAPA DE INVESTIGACION EN LA VENTA. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE Y NO CON "
    "IMPRESION: los CUATRO miembros son del MISMO LIBRO (SPIN Selling, de Rackham), tienen "
    "CINCO pares internos con veredicto escrito de SEIS combinaciones posibles y los CINCO "
    "son de clase A (puestos 209, 278, 303, 800 y 862), hay CERO pares D internos, CERO nodos "
    "puente y CERO triangulos, medido con scripts/loop/vuelta65_puentes_del_tramo.py sobre el "
    "estado del dia. ES EL ACTO MEJOR LEIDO DEL PREFIJO. "
    "Y LA CUARTA MEMBRESIA NO ES LECTURA MIA SINO DECLARACION DEL ARCHIVO: el puesto 800 dice "
    "con todas sus letras que LA FAMILIA NO ES DE TRES SINO DE CUATRO y que el CUARTO PURO "
    "queda DEGRADADO A SUB-PURO con correccion declarada en el banco; y el 862 cierra la "
    "cuenta diciendo que el sub-puro llega a CINCO DE SEIS pares leidos y los CINCO en A. "
    "EL RACIMO CENSADO NO SE PARTE, Y ESO SE MIDE EN VEZ DE SUPONERSE. El racimo LA ETAPA DE "
    "INVESTIGACION EN LA VENTA vive en docs/RACIMOS_MIEMBROS.jsonl con nomina de TRES "
    "(etapa_investigacion_ventas, etapa_de_investigacion y enfoque_etapa_investigacion), y los "
    "TRES estan DENTRO de este acto: el racimo cabe entero en el acto y esta fusion no lo "
    "corta por ningun sitio. El cuarto miembro del acto, investigacion_como_habilidad_clave, "
    "es el que el puesto 800 anadio por lectura y no esta en esa nomina. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; NINGUNA entrada de docs/plan/INVENTARIO.jsonl que no sea de tipo acto nombra a "
    "ninguno de los cuatro miembros; y NINGUNA ficha de docs/plan/OPERACIONES.jsonl los "
    "nombra en su campo nodos. Por el criterio del acta 68 (seccion 5.2) el dueno es EL "
    "MEDIDO y aqui no hay ninguno. "
    "GUARDA 1B, Y AQUI SI MUERDE: enfoque_etapa_investigacion ES PUERTA, medido con "
    "scripts/loop/varas_n_arias_del_tramo.py contra el universo protegido de 256 ids. La "
    "letra registrada en 03_FUSIONES.md dice que un acto con DOS O MAS puertas cierra "
    "DECLARADO, y que EL CASO DE UNA SOLA PUERTA NO ES ESE: con UNA el acto SI SE FUNDE y LA "
    "PUERTA SOBREVIVE (acta 54, pregunta 1). Aqui hay UNA y por eso el acto se funde a su "
    "lado. "
    "P.8 EN ORDEN, Y NO HACE FALTA QUE HABLE PARA QUE EL RESULTADO SEA EL MISMO: la FORMA "
    "medida es CONTENIDO EMPATA (pasos 4 a cuatro bandas, condiciones 2 a tres bandas), asi "
    "que EL CABLEADO DECIDE SOLO, que es el unico supuesto en que P.8 le da la palabra, y "
    "apunta a enfoque_etapa_investigacion con 6 contra un maximo de 3. LA PUERTA Y EL "
    "CABLEADO APUNTAN AL MISMO NODO: no hay choque que resolver, y se dice para que nadie "
    "tenga que reconstruirlo. EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN."
)

NOTA25 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado. DOS APPEND DE PASO Y CERO DE CONDICION, "
    "y el nodo crece de 4 pasos a 6 y se queda en 2 condiciones. Es el reparto mas barato del "
    "lote y la razon esta medida: el acto tiene CINCO pares leidos y los cinco dicen REPITE, "
    "asi que casi todo el catalogo esta CUBIERTO de verdad y no por conveniencia. "
    "LOS DOS APPEND DE PASO son gestos que el superviviente no tiene y que las razones nombran "
    "como propios: USAR LAS RESPUESTAS DEL CLIENTE PARA DESARROLLAR Y AMPLIAR LA PERCEPCION DE "
    "SUS PROPIAS NECESIDADES, que es el unico paso del acto donde la pregunta no solo averigua "
    "sino que MUEVE al cliente; y PRACTICAR ESCUCHAR DE VERDAD PARA DETECTAR PROBLEMAS QUE EL "
    "CLIENTE NO DICE DE MANERA DIRECTA, que el puesto 862 nombra con todas sus letras como lo "
    "propio de investigacion_como_habilidad_clave. "
    "CERO INCISO EN ESTE ACTO, y la razon es la puntuacion, que es el carril que el acta 66 "
    "adjudico en su D5: LOS CUATRO PASOS DEL SUPERVIVIENTE TERMINAN EN PUNTO, asi que "
    "cualquier INCISO con nexo de coma caeria en la guarda de la JUNTURA ROTA del generador. "
    "No se fuerza ninguno. "
    "CERO PERDIDAS DE CONDICIONES, Y SE DICE EN VEZ DE CALLARLO: las CINCO condiciones de los "
    "tres absorbidos dicen lo mismo que las dos del superviviente (presentar antes de "
    "entender, y no cerrar a pesar de buenas presentaciones), leidas una a una. La lista de "
    "perdidas trae TRES filas y las TRES son DE PARAMETRO DE PASO. "
    "UNA PERDIDA CON ATENUANTE DECLARADO, contada por maquina sobre esta misma lista, y es de "
    "la especie del pendiente 4. "
    "Y UNA FILA QUE VA DONDE VA POR LETRA Y NO POR GUSTO: la razon del puesto 862 declara "
    "COMUN el no apoyarse en el conocimiento tecnico del producto como sustituto de indagar, "
    "pero NINGUN paso del superviviente lo dice con esas palabras. CUANDO LA RAZON DECLARA "
    "COMPARTIDO UN GESTO QUE EL TEXTO NO DICE, PARA EL REPARTO MANDA EL TEXTO (acta 55, "
    "pregunta 3): va CUBIERTO con la perdida NOMBRADA."
)

PERDIDAS25 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL NIVEL DE EQUIPO: que la prioridad de las preguntas sobre la presentacion sea "
             "una decision de DESARROLLO DE HABILIDADES del equipo comercial y no solo de la "
             "planificacion de la llamada propia. El paso 1 del superviviente manda dedicar "
             "mas tiempo a disenar preguntas que a preparar el discurso de producto, que es la "
             "misma prioridad dicha para una sola cabeza. ATENUANTE DECLARADO: el paso 4 del "
             "superviviente si ordena el ENTRENAMIENTO, primero Situacion y Problema y "
             "despues Implicacion y Necesidad-beneficio, asi que el nivel de equipo asoma por "
             "ahi aunque no acompane a la prioridad"),
     "donde": "paso 1 de etapa_investigacion_ventas",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("entrenar al equipo en preguntas que revelen NECESIDADES OCULTAS. El paso 4 del "
             "superviviente entrena por TIPO de pregunta (Situacion, Problema, Implicacion, "
             "Necesidad-beneficio) y no por lo que la pregunta tiene que sacar a la luz. "
             "ATENUANTE DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: lo de los problemas que el "
             "cliente no dice llega entero por el APPEND del paso 3 de "
             "investigacion_como_habilidad_clave, que es su hermano en este mismo acto"),
     "donde": "paso 3 de etapa_investigacion_ventas",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL CONOCIMIENTO TECNICO DEL PRODUCTO COMO SUSTITUTO DE INDAGAR, nombrado. El "
             "paso 2 del superviviente prohibe MOSTRAR BENEFICIOS O CAPACIDADES antes de "
             "desarrollar el problema, que es la conducta, pero no nombra la causa que el "
             "absorbido si nombra: apoyarse en lo que uno sabe del producto. La razon del "
             "puesto 862 declara este gesto COMUN a los dos nodos; el texto del superviviente "
             "no lo dice, y PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3)"),
     "donde": "paso 2 de investigacion_como_habilidad_clave",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
]

REPARTO25 = {
    # ---------------------------------------------------------------
    "etapa_de_investigacion": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # sin perdida: preguntar antes de presentar
            "2": ("CUBIERTO", 2),   # sin perdida: resistir la demostracion temprana
            "3": ("APPEND",),       # DESARROLLAR Y AMPLIAR LA PERCEPCION (GESTO DISTINTO)
            "4": ("CUBIERTO", 3),   # sin perdida: evaluar la proporcion tras la llamada
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # sin perdida: presentar antes de entender
        },
    },
    # ---------------------------------------------------------------
    "etapa_investigacion_ventas": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # con perdida y atenuante: el nivel de equipo
            "2": ("CUBIERTO", 3),   # sin perdida: medir la proporcion
            "3": ("CUBIERTO", 4),   # con perdida y atenuante: las necesidades ocultas
            "4": ("CUBIERTO", 2),   # sin perdida: no demostrar sin haber investigado
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),   # sin perdida: las ventas complejas no cierran
            "2": ("CUBIERTO", 1),   # sin perdida: el equipo presenta en vez de preguntar
        },
    },
    # ---------------------------------------------------------------
    "investigacion_como_habilidad_clave": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # sin perdida: preparar preguntas de descubrimiento
            "2": ("CUBIERTO", 2),   # con perdida: el conocimiento tecnico como sustituto
            "3": ("APPEND",),       # ESCUCHAR LO QUE EL CLIENTE NO DICE (GESTO DISTINTO)
            "4": ("CUBIERTO", 3),   # sin perdida: el porcentaje de tiempo de la llamada
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # sin perdida: hablar del producto mas que preguntar
            "2": ("CUBIERTO", 2),   # sin perdida: no cerrar aunque se conozca el producto
        },
    },
}


# ======================================================================
# ACTO 26: LA FAMILIA DE LA ETNOGRAFIA DE CAMPO.
# CUATRO miembros, TRES pares internos con veredicto y los TRES en A,
# CERO D, CERO nodos puente y CERO triangulos. UNA PUERTA DENTRO, que por
# la letra de la guarda 1B sobrevive. FORMA medida: CHOCAN (pasos e
# cableado a la puerta, condiciones al otro lado), y por P.8 decide LA
# PIEZA DECLARADA, que apunta al mismo sitio que la puerta.
# ======================================================================

SUP26 = "investigacion_etnografica_ideacion"

MOTIVO26 = (
    "ACTO 26 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA ETNOGRAFIA DE CAMPO. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LA RAZON QUE LA CERRO DELANTE: "
    "los CUATRO miembros tienen TRES pares internos con veredicto escrito y los TRES son de "
    "clase A (puestos 230, 381 y 839), hay CERO pares D internos, CERO nodos puente y CERO "
    "triangulos, medido con scripts/loop/vuelta65_puentes_del_tramo.py sobre el estado del "
    "dia. Y LA FAMILIA NO ES LECTURA MIA: el puesto 839 dice con todas sus letras que la "
    "familia de la etnografia de campo TENIA DOS PAREJAS DECLARADAS Y SEPARADAS, la de Brown "
    "en el 381 y la de Cooper en el 230, y que ESTE ES EL CRUCE Y SALE A, o sea que SON "
    "CUATRO NODOS DEL MISMO INSTRUMENTO Y NO DOS PAREJAS VECINAS. Son DOS LIBROS distintos "
    "(Change by Design de Brown y Winning at New Products de Cooper) y eso NO parte la "
    "familia: el par que cruza los dos libros es justamente el que la cerro. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; ninguna entrada de docs/plan/INVENTARIO.jsonl que no sea de tipo acto nombra a "
    "ninguno de los cuatro miembros, y ninguna ficha de docs/plan/OPERACIONES.jsonl los nombra "
    "en su campo nodos. "
    "GUARDA 1B: investigacion_etnografica_ideacion ES PUERTA, medido contra el universo "
    "protegido de 256 ids, y es UNA SOLA. Por la letra registrada en 03_FUSIONES.md, con UNA "
    "puerta el acto SI SE FUNDE y LA PUERTA SOBREVIVE (acta 54, pregunta 1). "
    "P.8 EN ORDEN, Y ESTE ES EL PRIMER CHOCAN DEL TRAMO QUE LLEGA A FUNDIRSE: la FORMA medida "
    "es CHOCAN. La vara de PASOS apunta a investigacion_etnografica_ideacion (6 contra un "
    "maximo de 5) y la de CONDICIONES apunta al otro lado, a etnografia_investigacion_usuario "
    "(3 contra 2). Cuando las varas de contenido CHOCAN decide LA PIEZA DECLARADA, y la pieza "
    "declarada esta escrita: el puesto 839 enumera lo propio de cada lado y el catalogo de "
    "gestos propios que el superviviente ya trae es el mas ancho de los cuatro (el periodo "
    "extendido, la capacitacion del equipo observador, la reduccion del tiempo por visita y la "
    "traduccion a conceptos de producto concretos). EL CABLEADO NO DECIDE AQUI porque el "
    "contenido dice algo, pero SE PUBLICA COMO DATO Y APUNTA AL MISMO SITIO: 14 contra un "
    "maximo de 8. Y LA PUERTA TAMBIEN. Las tres cuentas y la guarda apuntan al mismo nodo, y "
    "por eso este CHOCAN no deja residuo."
)

NOTA26 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado, y ES EL MAS CARO DEL LOTE. TRES APPEND "
    "DE PASO, UNO DE CONDICION Y UN INCISO, y el nodo crece de 6 pasos a 9 y de 2 condiciones "
    "a 3. VA MARCADO DISCUTIBLE: NUEVE PASOS iguala al nodo mas grande que este tramo ha "
    "producido, que fue el del acto 22 de la vuelta 68. La eleccion es la del carril del D8 "
    "del acta 67 y del D4 del acta 68, catalogo mas rico con solapes declarados por encima de "
    "CUBIERTO que calla texto vivo, Y LOS TRES APPEND DE PASO SON LOS QUE LAS RAZONES NOMBRAN "
    "COMO PROPIOS antes de que nadie fundiera nada: EL EQUIPO MIXTO de antropologos y "
    "etnografos con disenadores, arquitectos e ingenieros (el unico paso del acto que dice de "
    "QUE ESTA HECHO el equipo y no solo que se le capacita); LAS SITUACIONES ANALOGAS, el pit "
    "stop de carreras para entender una sala de urgencias, que el 381 y el 839 llaman los dos "
    "el unico gesto propio de etnografia_de_proyecto; y CONSTRUIR CONFIANZA GENUINA con los "
    "sujetos observados antes de sacar insights, que es lo unico del acto que pone una "
    "condicion etica delante del hallazgo. "
    "UN SOLO INCISO Y AL PASO 2, extraido VERBATIM del paso 3 de "
    "etnografia_aplicada_en_equipos_multidisciplinarios: DEPUTIZAR, meter a lideres o clientes "
    "en la observacion de campo. Va de INCISO y no de APPEND porque es un PARAMETRO de la "
    "observacion que el superviviente ya manda hacer, no un gesto aparte; el paso 2 del "
    "superviviente NO termina en punto y la juntura se lee limpia. "
    "EL APPEND DE CONDICION ES UN DISPARADOR DISTINTO (acta 55, pregunta 5): los contextos "
    "CULTURALMENTE distintos al del equipo de diseno. Las dos condiciones del superviviente "
    "disparan por la AMBICION (ideas breakthrough) y por el FRACASO DEL METODO (encuestas y "
    "focus groups que no revelan); ninguna dispara por la DISTANCIA CULTURAL. "
    "OCHO PERDIDAS SELLADAS, que es la cifra mas alta de un acto en este tramo, y va dicho: es "
    "el precio de fundir cuatro nodos de dos libros distintos con catalogos que se solapan a "
    "medias. CUATRO DE ELLAS LLEVAN ATENUANTE DECLARADO, contadas por maquina sobre esta misma "
    "lista y no de memoria, que es la regla que sale de la caida del D9 de la vuelta 68: DOS "
    "son de la especie del pendiente 4 (ya lo dice el APPEND de un hermano), UNA es de la "
    "especie del D10 del acta 68 (el INCISO del mismo acto la repara y se sella igual, porque "
    "el sello es del reparto y no del resultado) y UNA se apoya en un paso vecino del "
    "superviviente."
)

PERDIDAS26 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA INMERSION PROFUNDA como forma de la observacion: convivencia y estadias EN "
             "LUGAR DE entrevistas puntuales. El paso 2 del superviviente manda observar "
             "durante un PERIODO EXTENDIDO, que es duracion y no convivencia, y su paso 5 "
             "empuja en el sentido contrario, REDUCIR EL TIEMPO POR VISITA si hace falta. "
             "ATENUANTE DECLARADO: el periodo extendido del paso 2 conserva la mitad larga de "
             "la pieza"),
     "donde": "paso 2 de etnografia_aplicada_en_equipos_multidisciplinarios",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("CONSTRUIR CONFIANZA CON LAS COMUNIDADES ESTUDIADAS antes de extraer conclusiones "
             "de diseno, dicho sobre COMUNIDADES y no sobre sujetos. ATENUANTE DECLARADO, Y ES "
             "LA ESPECIE DEL PENDIENTE 4: el gesto llega entero por el APPEND del paso 5 de "
             "etnografia_de_proyecto, que lo dice sobre LOS SUJETOS OBSERVADOS; lo que no "
             "llega es la palabra COMUNIDADES"),
     "donde": "paso 4 de etnografia_aplicada_en_equipos_multidisciplinarios",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("ENSAMBLAR UN EQUIPO CROSS-DISCIPLINARIO con perfiles tecnicos y sociales. El "
             "paso 4 del superviviente CAPACITA al equipo observador en escucha e inferencia, "
             "que es entrenar a quien ya esta, no elegir de que esta hecho. ATENUANTE "
             "DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: la composicion mixta llega entera y "
             "con mas detalle por el APPEND del paso 1 de "
             "etnografia_aplicada_en_equipos_multidisciplinarios"),
     "donde": "paso 1 de etnografia_de_proyecto",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("DEPUTIZAR dicho por segunda vez, con la palabra CONSIDERAR delante y sobre "
             "CLIENTES O EJECUTIVOS PROPIOS. ATENUANTE DECLARADO Y MEDIDO: el INCISO al paso 2 "
             "de este mismo acto adosa VERBATIM el deputizar del hermano, asi que la pieza NO "
             "se pierde de hecho; se sella igual porque el sello es del reparto y no del "
             "resultado (acta 68, D10)"),
     "donde": "paso 4 de etnografia_de_proyecto",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("OBSERVAR SIN INTERFERIR. El paso 2 del superviviente manda observar DIRECTAMENTE "
             "a los usuarios usando o mal usando el producto, y recoge por tanto el mal uso, "
             "pero en ningun sitio dice que el observador no intervenga. Es la unica linea del "
             "acto que pone una regla sobre la conducta DEL OBSERVADOR, y el puesto 839 la "
             "nombra como lo propio de etnografia_investigacion_usuario"),
     "donde": "paso 2 de etnografia_investigacion_usuario",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA TIPOLOGIA DE LO QUE SE DOCUMENTA: problemas FISICOS, EMOCIONALES Y "
             "CONTEXTUALES. El paso 3 del superviviente documenta problemas, quejas y "
             "comportamientos no verbalizados, que es una lista distinta y sin el eje "
             "emocional. El puesto 839 la nombra tambien como propia"),
     "donde": "paso 3 de etnografia_investigacion_usuario",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("LA NECESIDAD DE CONFIANZA PROFUNDA con los usuarios ANTES de disenar, como "
             "disparador. Es el disparador propio del paso de confianza que este mismo acto "
             "adosa por APPEND, y ninguna de las dos condiciones del superviviente lo recoge"),
     "donde": "condicion 2 de etnografia_aplicada_en_equipos_multidisciplinarios",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("EL CONTEXTO FISICO COMPLEJO (campo, hospital, fabrica) como disparador. El paso 1 "
             "del superviviente nombra esos mismos sitios como EJEMPLO de donde observar, pero "
             "como PASO y no como condicion: el acto pierde el CUANDO y conserva el DONDE. "
             "ATENUANTE DECLARADO Y MEDIDO: los tres sitios estan escritos verbatim en el paso "
             "1 del superviviente"),
     "donde": "condicion 3 de etnografia_investigacion_usuario",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO26 = {
    # ---------------------------------------------------------------
    "etnografia_aplicada_en_equipos_multidisciplinarios": {
        "pasos": {
            "1": ("APPEND",),       # EL EQUIPO MIXTO (GESTO DISTINTO)
            "2": ("CUBIERTO", 2),   # con perdida y atenuante: la inmersion profunda
            # EL UNICO INCISO DEL ACTO: DEPUTIZAR, que es un PARAMETRO de la
            # observacion que el superviviente ya manda hacer.
            "3": ("INCISO", 2,
                  "a lideres o clientes (deputizar) en la observacion de campo para generar empatia directa",
                  ", involucrando "),
            "4": ("CUBIERTO", 2),   # con perdida y atenuante: la confianza con comunidades
        },
        "condiciones": {
            "1": ("APPEND",),       # LOS CONTEXTOS CULTURALMENTE DISTINTOS (DISPARADOR DISTINTO)
            "2": ("CUBIERTO", 2),   # con perdida: la confianza profunda como disparador
        },
    },
    # ---------------------------------------------------------------
    "etnografia_de_proyecto": {
        "pasos": {
            "1": ("CUBIERTO", 4),   # con perdida y atenuante: el equipo cross-disciplinario
            "2": ("CUBIERTO", 2),   # sin perdida: la observacion de campo directa
            "3": ("APPEND",),       # LAS SITUACIONES ANALOGAS (GESTO DISTINTO)
            "4": ("CUBIERTO", 2),   # con perdida y atenuante medido: deputizar otra vez
            "5": ("APPEND",),       # LA CONFIANZA GENUINA ANTES DEL INSIGHT (GESTO DISTINTO)
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # sin perdida: entender comportamientos reales antes de idear
            "2": ("CUBIERTO", 2),   # sin perdida: encuestas y focus groups que no revelan
        },
    },
    # ---------------------------------------------------------------
    "etnografia_investigacion_usuario": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # sin perdida: seleccionar el entorno real
            "2": ("CUBIERTO", 2),   # con perdida: observar SIN INTERFERIR
            "3": ("CUBIERTO", 3),   # con perdida: la tipologia fisico, emocional, contextual
            "4": ("CUBIERTO", 6),   # sin perdida: traducir a conceptos de producto
            "5": ("CUBIERTO", 4),   # sin perdida: equipos con observacion e inferencia
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # sin perdida: innovacion radical y no incremental
            "2": ("CUBIERTO", 2),   # sin perdida: encuestas y focus groups que no revelan
            "3": ("CUBIERTO", 1),   # con perdida y atenuante: el contexto fisico complejo
        },
    },
}


# ======================================================================
# ACTO 29: LA FAMILIA DEL AVANCE CONTRA LA CONTINUACION.
# TRES miembros, DOS pares internos con veredicto y los DOS en A, CERO D,
# CERO nodos puente y CERO triangulos. NINGUN MIEMBRO ES PUERTA.
# FORMA medida: UNA SOLA VARA, la de CONDICIONES, que apunta a
# marco_avances_continuaciones. UNA SOLA VARA BASTA.
# ======================================================================

SUP29 = "marco_avances_continuaciones"

MOTIVO29 = (
    "ACTO 29 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DEL AVANCE CONTRA LA CONTINUACION. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE: los TRES "
    "miembros son del MISMO LIBRO (SPIN Selling, de Rackham), tienen DOS pares internos con "
    "veredicto escrito de TRES combinaciones posibles y los DOS son de clase A (puestos 220 y "
    "482), hay CERO pares D internos, CERO nodos puente y CERO triangulos, medido con "
    "scripts/loop/vuelta65_puentes_del_tramo.py sobre el estado del dia. Los dos veredictos "
    "dicen REPITE con todas sus letras y nombran el mismo trio de gestos: definir el objetivo "
    "como una accion concreta del cliente, descartar los objetivos vagos, y clasificar despues "
    "el resultado. "
    "EL RACIMO CENSADO SI SE TOCA, Y ESO SE MIDE Y SE DECLARA EN VEZ DE CALLARSE, que es la "
    "pieza mas delicada de este acto. El racimo EL AVANCE Y EL COMPROMISO EN LA VENTA vive en "
    "docs/RACIMOS_MIEMBROS.jsonl con nomina censada de CINCO: advances_vs_continuations, "
    "objetivos_de_llamada_orientados_a_avance, obtencion_de_compromiso, "
    "obtencion_compromiso_venta y obtencion_compromiso. Este acto contiene DOS de esos cinco "
    "(los dos primeros) y anade marco_avances_continuaciones, que NO esta en esa nomina. LOS "
    "OTROS TRES NO SE TOCAN Y TIENEN CASA PROPIA MEDIDA: docs/plan/INVENTARIO.jsonl trae la "
    "entrada racimo EL COMPROMISO CONTADO TRES VECES, forma PURO, estado sano y forma cerrada, "
    "con nomina de exactamente esos TRES. O sea que el censo de cinco del cribado ya esta "
    "PARTIDO en el inventario en un PURO de tres mas dos sueltos, y esta fusion opera sobre "
    "los DOS SUELTOS sin tocar el PURO ni una sola vez. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; el campo operaciones de la entrada de inventario del PURO de tres tambien esta "
    "VACIO; y NINGUNA entrada de inventario que no sea de tipo acto nombra a ninguno de los "
    "tres miembros de ESTE acto. Por el criterio del acta 68 (seccion 5.2) el dueno es EL "
    "MEDIDO y aqui no hay ninguno. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta, medido con "
    "scripts/loop/varas_n_arias_del_tramo.py contra el universo protegido de 256 ids. La "
    "guarda pasa por vacio y se dice. "
    "P.8 EN ORDEN: la FORMA medida es UNA SOLA VARA. La vara de PASOS empata en 4 a tres "
    "bandas y el CABLEADO empata en 3 a dos bandas, pero la vara de CONDICIONES apunta a "
    "marco_avances_continuaciones (2 contra un maximo de 1). UNA SOLA VARA BASTA: donde el "
    "contenido dice algo, el contenido manda, y aqui lo dice la unica que no empata. EL "
    "ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN, y el cableado no llega a hablar porque el "
    "contenido no esta empatado."
)

NOTA29 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado. DOS APPEND DE PASO Y CERO DE CONDICION, "
    "y el nodo crece de 4 pasos a 6 y se queda en 2 condiciones. "
    "LOS DOS APPEND DE PASO son gestos que el superviviente no tiene: DESCARTAR LOS OBJETIVOS "
    "AMBIGUOS con sus dos ejemplares nombrados (construir relacion y recolectar informacion), "
    "que es la unica linea del acto que dice que NO cuenta como objetivo, y LA ALTERNATIVA EN "
    "CALIENTE, buscar durante la llamada otra accion medible cuando el objetivo principal "
    "falla, que es el unico paso del acto que opera DENTRO de la reunion y no antes ni "
    "despues. "
    "CERO INCISO Y ES POR LA PUNTUACION, el carril del D5 del acta 66: LOS CUATRO PASOS DEL "
    "SUPERVIVIENTE TERMINAN EN PUNTO, asi que cualquier INCISO con nexo de coma caeria en la "
    "guarda de la JUNTURA ROTA. No se fuerza ninguno. "
    "UNA SOLA PERDIDA SELLADA Y ES LA MAS BARATA DEL LOTE, DE PARAMETRO DE PASO, con ATENUANTE "
    "DECLARADO de la especie del pendiente 4. CERO PERDIDAS DE CONDICIONES, y se dice en vez "
    "de callarlo: las DOS condiciones de los absorbidos dicen lo mismo que las dos del "
    "superviviente (el ciclo largo con muchas interacciones, y confundir senales positivas con "
    "progreso real), leidas una a una."
)

PERDIDAS29 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL DESCARTE DE LOS OBJETIVOS VAGOS dicho por segunda vez, con RECOPILAR "
             "INFORMACION y CONSTRUIR RELACION nombrados. El paso 3 del superviviente disena la "
             "siguiente interaccion con el objetivo explicito de lograr una accion medible, o "
             "sea que manda lo que SI hay que hacer, pero no nombra lo que NO cuenta. ATENUANTE "
             "DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: el descarte llega entero, con los dos "
             "ejemplares nombrados, por el APPEND del paso 2 de "
             "objetivos_de_llamada_orientados_a_avance, que es su hermano en este mismo acto"),
     "donde": "paso 2 de advances_vs_continuations",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
]

REPARTO29 = {
    # ---------------------------------------------------------------
    "advances_vs_continuations": {
        "pasos": {
            "1": ("CUBIERTO", 3),   # sin perdida: el objetivo como accion concreta del cliente
            "2": ("CUBIERTO", 3),   # con perdida y atenuante: los objetivos vagos
            "3": ("CUBIERTO", 1),   # sin perdida: clasificar avance contra continuacion
            "4": ("CUBIERTO", 2),   # sin perdida: que falto para que fuera avance
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # sin perdida: la venta consultiva compleja y larga
        },
    },
    # ---------------------------------------------------------------
    "objetivos_de_llamada_orientados_a_avance": {
        "pasos": {
            "1": ("CUBIERTO", 3),   # sin perdida: el objetivo especifico con accion del cliente
            "2": ("APPEND",),       # DESCARTAR LOS OBJETIVOS AMBIGUOS (GESTO DISTINTO)
            "3": ("APPEND",),       # LA ALTERNATIVA EN CALIENTE (GESTO DISTINTO)
            "4": ("CUBIERTO", 1),   # sin perdida: revisar despues si hubo accion concreta
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),   # sin perdida: llamadas exitosas sin progreso medible
        },
    },
}


# ======================================================================
# ACTO 30: LA FAMILIA DEL VIAJE DIAGNOSTICO DE JURAN.
# TRES miembros, DOS pares internos con veredicto y los DOS en A, CERO D,
# CERO nodos puente y CERO triangulos. NINGUN MIEMBRO ES PUERTA.
# FORMA medida: CHOCAN (pasos a viaje_diagnostico_remedial, condiciones a
# analisis_causa_raiz_diagnostico, cableado empatado), y por P.8 decide LA
# PIEZA DECLARADA, que aqui esta escrita con todas sus letras en el
# puesto 2838: A POR CONTENCION, superviviente viaje_diagnostico_remedial.
# ======================================================================

SUP30 = "viaje_diagnostico_remedial"

MOTIVO30 = (
    "ACTO 30 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DEL VIAJE DIAGNOSTICO DE JURAN. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE: los TRES "
    "miembros son de la MISMA FUENTE (Juran's Quality Handbook, de Defeo), tienen DOS pares "
    "internos con veredicto escrito de TRES combinaciones posibles y los DOS son de clase A "
    "(puestos 2600 y 2838), hay CERO pares D internos, CERO nodos puente y CERO triangulos, "
    "medido con scripts/loop/vuelta65_puentes_del_tramo.py sobre el estado del dia. "
    "EL RACIMO CENSADO SE TOCA EN PARTE, Y SE DICE MEDIDO: el racimo ANALISIS DE CAUSA RAIZ de "
    "docs/RACIMOS_MIEMBROS.jsonl tiene nomina censada de CUATRO "
    "(analisis_causa_raiz_diagnostico, analisis_diagnostico_causa, analisis_causa_raiz_defectos "
    "y juran_rcca_metodo). Este acto contiene DOS de esos cuatro y anade "
    "viaje_diagnostico_remedial, que no esta en la nomina. LOS OTROS DOS NO SE TOCAN: ni "
    "analisis_causa_raiz_defectos ni juran_rcca_metodo entran en este acto, y ninguno de los "
    "dos queda deprecado por esta fusion. Ese censo del cribado NO trae forma escrita ni "
    "particion en docs/plan/INVENTARIO.jsonl, o sea que no hay frontera escrita que cruzar; se "
    "declara igual porque una nomina que se toca a medias se declara aunque no sea frontera. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy. Y SE DECLARA UN CONTRASTE EN VEZ DE RESOLVERLO COPIANDO (regla 2 del ejecutor): "
    "analisis_diagnostico_causa aparece nombrado UNA vez en docs/plan/OPERACIONES.jsonl, "
    "dentro del campo evidencia de OP-D-09 y hablando de una arista que entra desde su paso 3. "
    "El campo nodos de OP-D-09 es planificacion_recoleccion_datos y NADA MAS, medido hoy: una "
    "mencion en la evidencia de una ficha NO es dueno por el criterio del acta 68 (seccion "
    "5.2), que mide el dueno en los dos campos duenos_* del tramo y en el campo operaciones de "
    "la entrada de inventario. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta, medido contra el universo protegido de "
    "256 ids. La guarda pasa por vacio y se dice. "
    "P.8 EN ORDEN, Y ESTE CHOCAN LO DECIDE UNA PIEZA DECLARADA POR ESCRITO: la FORMA medida es "
    "CHOCAN. La vara de PASOS apunta a viaje_diagnostico_remedial (8 contra un maximo de 5), la "
    "de CONDICIONES apunta al otro lado, a analisis_causa_raiz_diagnostico (2 contra 1), y el "
    "CABLEADO EMPATA en 4 a dos bandas, o sea que ni siquiera podria desempatar si le tocara. "
    "Cuando las varas de contenido CHOCAN decide LA PIEZA DECLARADA, y aqui la declaracion es "
    "explicita y verbatim: el puesto 2838 dice A POR CONTENCION, que "
    "analisis_causa_raiz_diagnostico ES EL VIAJE DIAGNOSTICO ENTERO Y SE DETIENE EXPLICITAMENTE "
    "ANTES DEL REMEDIO, que viaje_diagnostico_remedial es ESE MISMO VIAJE MAS EL VIAJE REMEDIAL "
    "COMPLETO, y cierra con la frase A, SUPERVIVIENTE viaje_diagnostico_remedial. "
    "Y SE DICE LO QUE ESA MISMA RAZON MARCA COMO DISCUTIBLE, en vez de callarlo: el 2838 lleva "
    "un DISCUTIBLE MARCADO FUERTE de su propio autor (quien lea el viaje diagnostico como una "
    "PARTE contra el mapa de los dos viajes, o como cara distinta por su Pareto y su validacion "
    "estadistica, dira D). ESA ES LA RAZON POR LA QUE ESTE ACTO SE FUNDE CON CUATRO INCISO Y NO "
    "CON CUATRO CUBIERTO MUDOS: lo que el 2838 llama discutible es exactamente el rigor "
    "estadistico del absorbido, y ese rigor entra VERBATIM en los pasos del superviviente."
)

NOTA30 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado, Y ES EL REPARTO MAS RARO DEL TRAMO: "
    "CUATRO INCISO, UN APPEND DE CONDICION Y CERO APPEND DE PASO. El nodo se queda en 8 pasos "
    "y crece de 1 condicion a 2. VA MARCADO DISCUTIBLE: cuatro INCISO en un solo acto es la "
    "cifra mas alta de la campana, y aunque NINGUNO se apila sobre el mismo paso (la regla que "
    "el acta 64 dejo escrita), cuatro pasos del superviviente salen de aqui con una oracion "
    "cosida detras. "
    "LA RAZON DE ESA FORMA ESTA MEDIDA Y NO ES DE GUSTO: el superviviente ya trae OCHO pasos, "
    "que es el nodo mas largo de todo el prefijo que queda, y las cuatro piezas propias del "
    "absorbido NO son gestos nuevos sino PARAMETROS DE RIGOR de gestos que el superviviente ya "
    "manda hacer. Por la politica del reparto heredada, una pieza cuyo unico contenido propio "
    "es un PARAMETRO CONCRETO de un gesto que el superviviente ya tiene va de INCISO ADOSADO "
    "cuando el paso resultante se lee limpio, y de CUBIERTO con la perdida NOMBRADA cuando no. "
    "Los cuatro pasos del superviviente que reciben INCISO NO TERMINAN EN PUNTO, asi que la "
    "guarda de la JUNTURA ROTA no salta en ninguno, y los cuatro resultantes van impresos por "
    "el generador. "
    "LAS CUATRO PIEZAS QUE ENTRAN POR INCISO, una a una: EL ANALISIS DE PARETO para descartar "
    "variables no relevantes, al paso 1, que es donde el absorbido lo pone, ANTES de teorizar; "
    "LOS DIAGRAMAS CAUSA-EFECTO y el brainstorming, al paso 2, que es la perdida que el puesto "
    "2600 nombro con todas sus letras al declarar aquel par; EL MECANISMO DE RECOLECCION "
    "DISENADO PARA CORRELACIONAR cada teoria con el defecto, al paso 3; y LA VALIDACION "
    "ESTADISTICA de cual teoria explica la mayoria de los casos, al paso 4. "
    "EL APPEND DE CONDICION ES UN DISPARADOR DISTINTO (acta 55, pregunta 5): tener MULTIPLES "
    "HIPOTESIS SIN VALIDAR. La unica condicion del superviviente dispara por el problema "
    "cronico que pide metodologia estructurada, que es el problema; esta dispara por el estado "
    "del equipo, que es otra cosa. "
    "DOS PERDIDAS SELLADAS, contadas por maquina sobre esta misma lista, y UNA de las dos lleva "
    "ATENUANTE DECLARADO Y MEDIDO de la especie del D10 del acta 68: la repara un INCISO de "
    "este mismo acto y se sella igual, porque el sello es del reparto y no del resultado."
)

PERDIDAS30 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA PARADA EXPLICITA ANTES DEL REMEDIO: confirmar la causa raiz ANTES de disenar "
             "el remedio, dicho como orden y no solo como orden de los pasos. Es la frase que "
             "el puesto 2838 usa para separar los dos viajes, y el superviviente conserva el "
             "ORDEN (su paso 4 establece la causa y su paso 5 disena remedios) pero pierde la "
             "PROHIBICION de adelantarse. ATENUANTE DECLARADO: el orden de los ocho pasos del "
             "superviviente hace lo mismo de hecho, aunque sin decirlo"),
     "donde": "paso 5 de analisis_causa_raiz_diagnostico",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL DIAGRAMA CAUSA-EFECTO, el de Ishikawa, que es la perdida que el puesto 2600 "
             "nombro por su nombre al declarar aquel par: la herramienta que un dueno sin "
             "estadistica puede usar para el mismo paso de generar teorias. ATENUANTE "
             "DECLARADO Y MEDIDO: el INCISO al paso 2 de este mismo acto adosa VERBATIM "
             "USANDO BRAINSTORMING Y DIAGRAMAS CAUSA-EFECTO, asi que la pieza NO se pierde de "
             "hecho; se sella igual porque el sello es del reparto y no del resultado (acta "
             "68, D10), y porque la perdida la nombro una razon publicada y una perdida "
             "publicada que desaparece sin decirlo es peor que una sellada de mas"),
     "donde": "paso 2 de analisis_diagnostico_causa",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
]

REPARTO30 = {
    # ---------------------------------------------------------------
    "analisis_causa_raiz_diagnostico": {
        "pasos": {
            # INCISO 1 DE 4: el Pareto va al PASO 1 porque es donde el absorbido lo
            # pone, ANTES de teorizar. Un APPEND lo habria dejado en el paso 9.
            "1": ("INCISO", 1,
                  "analisis de Pareto para descartar variables no relevantes (ej. turno de trabajo)",
                  ", con un "),
            "2": ("CUBIERTO", 2),   # sin perdida: generar la lista de teorias con el equipo
            # INCISO 3 DE 4: la recoleccion disenada para correlacionar.
            "3": ("INCISO", 3,
                  "que permita correlacionar cada teoria con el defecto observado",
                  ", con un mecanismo de recolección "),
            # INCISO 4 DE 4: la validacion estadistica.
            "4": ("INCISO", 4,
                  "estadisticamente cual teoria explica la mayoria de los casos",
                  ", validando "),
            "5": ("CUBIERTO", 4),   # con perdida y atenuante: la parada antes del remedio
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # sin perdida: el problema cronico de calidad
            "2": ("APPEND",),       # MULTIPLES HIPOTESIS SIN VALIDAR (DISPARADOR DISTINTO)
        },
    },
    # ---------------------------------------------------------------
    "analisis_diagnostico_causa": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # sin perdida: analizar los sintomas
            # INCISO 2 DE 4: el brainstorming y los diagramas causa-efecto, que es la
            # perdida que el puesto 2600 nombro por su nombre.
            "2": ("INCISO", 2,
                  "usando brainstorming y diagramas causa-efecto",
                  ", "),
            "3": ("CUBIERTO", 3),   # sin perdida: probar las teorias con datos
            "4": ("CUBIERTO", 4),   # sin perdida: la causa raiz confirmada con evidencia
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # sin perdida: problema definido y causa por identificar
        },
    },
}


# ======================================================================
# EL UNICO DECLARADO Y NO FUNDIDO DEL LOTE, POR EL TRIANGULO DE P.10,
# QUE ES EL PRIMERO DE LOS CUATRO MOTIVOS SELLADOS DEL CATALOGO.
# ======================================================================

DECLARADO_ACTO27 = {
    "acto": 27,
    "miembros": [
        "fase_diseno_prototipado_modelos",
        "proceso_ideacion_modelo_negocio",
        "prototipado_modelos_negocio",
        "prototyping_possibilities",
    ],
    "superviviente_que_el_contenido_elige": (
        "NINGUNO SE ELIGE, Y ESA ES LA DECISION. Se dice a quien habria apuntado la forma, "
        "porque callarlo seria esconder el costo: la FORMA medida es TODAS DE ACUERDO, la "
        "unica del lote, y las tres cuentas apuntan al MISMO nodo, prototipado_modelos_negocio "
        "(6 pasos contra un maximo de 5, 3 condiciones contra 2 y cableado 14 contra un maximo "
        "de 9). Es el acto con la forma mas limpia del prefijo y aun asi NO SE FUNDE: P.10 "
        "detiene ANTES, y ademas el nodo al que las varas apuntan es un PERIFERICO de una "
        "figura declarada del inventario."
    ),
    "motivo": (
        "ACTO 27 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DEL PROTOTIPADO DE MODELOS DE NEGOCIO. "
        "DECLARADO Y NO FUNDIDO CON EL TRIANGULO DE P.10 COMO MOTIVO SELLADO, que es el primero "
        "de los CUATRO motivos del catalogo, Y CON UNA SEGUNDA RAZON INDEPENDIENTE QUE SE "
        "PUBLICA EN VEZ DE CALLARSE. "
        "LO MEDIDO, Y ES LO QUE MANDA: UN nodo puente, fase_diseno_prototipado_modelos, que hace "
        "de puente en UN triangulo A mas A mas D (A con proceso_ideacion_modelo_negocio por el "
        "puesto 507 y A con prototipado_modelos_negocio por el 641, y esos dos son D entre si "
        "por el puesto 572); y UN par D interno, ese 572. La ultima linea de P.10 dice que LO "
        "QUE NUNCA ES SALIDA es fundir la componente entera porque el cierre transitivo la "
        "junta, y aqui el cierre la junta por ese puente. "
        "LA LECTURA QUE UNA FUSION ENTERA DESMENTIRIA, con su razon delante: el 572 se titula EL "
        "HIJO CON CASA PROPIA y dice que prototipado_modelos_negocio DESARROLLA EL PASO 5 de "
        "proceso_ideacion_modelo_negocio y le anade lo suyo entero (la escalera del boceto al "
        "lienzo y de ahi al caso de negocio en hoja de calculo, la manipulacion por escenarios "
        "quitando un segmento o un recurso clave, la prueba de campo con clientes reales y la "
        "regla de construir al menos tres antes de elegir), mientras LA MADRE SE QUEDA CON LO "
        "SUYO (el equipo diverso en antiguedad y area, la inmersion previa y los criterios de "
        "seleccion por tiempo, ingresos y resistencia interna). Fundir los cuatro a un vivo "
        "unico deprecaria los dos extremos de ese D contra el mismo superviviente y sellaria "
        "que repiten entre si, que es exactamente lo que esa lectura niega, y ademas es una "
        "cadena de TRES PISOS que el propio 572 cuenta al cerrar. "
        "SEGUNDA RAZON, INDEPENDIENTE Y MEDIDA: ESTE ACTO ES UN EJEMPLAR DECLARADO DE UNA FIGURA "
        "DEL CATALOGO. La entrada figura ESTRELLA (9.23) de docs/plan/INVENTARIO.jsonl lo nombra "
        "como su ejemplar numero CUATRO, la fase de diseno, con el centro "
        "fase_diseno_prototipado_modelos, los radios 507 y 641 y el periferico 572 en D, y "
        "declara que LAS OCHO ESTRELLAS NOMBRADAS VERIFICAN con las dos cuentas que el banco "
        "9.23 exige. El centro de esa estrella es EXACTAMENTE el nodo puente que P.10 detecto, y "
        "el periferico es EXACTAMENTE el par D. Fundir el acto entero deprecaria a la vez el "
        "centro y sus perifericos y borraria un ejemplar de una figura del inventario. Es la "
        "misma forma que el acto 24 de la vuelta 68, con la estrella de pass/fail. "
        "LA PREGUNTA DE P.5 SE CONTESTA IGUAL Y SE DEJA ESCRITA, porque el acto se lee entero "
        "aunque no se funda: ES UNA FAMILIA, con cuatro pares leidos de seis, tres A y un D, "
        "PERO ES UNA FAMILIA MEZCLADA, que es el nombre que el archivo usa para una familia con "
        "un D dentro, y ademas es una FIGURA con centro y periferia, que es una forma mas fina "
        "que una familia plana. FAMILIA NO ES FUSION. Los cuatro no son del mismo libro: tres "
        "son de Business Model Generation de Osterwalder y prototyping_possibilities es de Value "
        "Proposition Design, y el puesto 1056 es el que los cruza. "
        "GUARDA 1B: NINGUN miembro es puerta, medido; la guarda pasa por vacio y se dice, para "
        "que la razon del declarado quede en UNA mas su segunda razon y no en tres. "
        "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
        "hoy. Este acto NO se declara por dueno. "
        "EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se depreca ninguno y no se elige "
        "superviviente. Su destino comparte carril con el pendiente heredado del subconjunto "
        "cerrado: el cierre de la fase 03."
    ),
    "medicion": {
        "instrumento": "scripts/loop/vuelta65_puentes_del_tramo.py",
        "salida": "docs/loop/SALIDA_V69_PUENTES_TRAMO.txt",
        "dossier": "docs/loop/SALIDA_V69_DOSSIER_LOTE_E.txt",
        "varas": "docs/loop/SALIDA_V69_VARAS_N_ARIAS.txt",
        "miembros": 4,
        "combinaciones": 6,
        "pares_A": 3,
        "pares_D": 1,
        "pares_sin_veredicto": 2,
        "nodos_puente": 1,
        "triangulos_puente": 1,
        "puertas_dentro": [],
        "puestos_D_internos": [572],
        "duenos_cualquier_operacion": [],
        "figura_del_inventario": "ESTRELLA (9.23), ejemplar 4, la fase de diseno",
    },
}


LOTE_E = {
    "titulo": ("LOTE E DEL TRAMO UNICO DE OP-U-02. ABRE CON LA FUSION ADJUDICADA DEL ACTO 18 "
               "(acta 68, adjudicaciones 1 y 3: superviviente alianzas_cross_industry, ejecutada "
               "como PRIMERA operacion del lote y dentro de ESTE plan propio, sin reabrir el del "
               "lote D) Y SIGUE CON EL PREFIJO SIN SALTOS DESDE EL ACTO 25. SEIS ACTOS CIERRAN "
               "ENTEROS Y SON 22 NODOS: los actos 18, 25, 26, 29 y 30 cierran FUNDIDOS y el acto "
               "27 cierra DECLARADO Y NO FUNDIDO con el TRIANGULO DE P.10 como motivo sellado, "
               "mas una segunda razon independiente (es el ejemplar 4 de la figura ESTRELLA del "
               "inventario, y el centro de esa estrella es el mismo nodo puente que P.10 "
               "detecto). EL TOPE DEL PREFIJO ES ESTRUCTURAL Y SE DICE: el siguiente es el ACTO "
               "31, que TIENE DUENO (OP-F-04-WEI y OP-S-04 en duenos_cualquier_operacion, medido "
               "hoy sobre el fichero fijado) y que ademas NO trae ninguno de los cuatro motivos "
               "sellados con los que podria cerrar DECLARADO, o sea que no podria cerrar ENTERO; "
               "el contrato del lote es entregar lo declarado y por eso el tope cae ANTES de el"),
    "actos": [
        {
            "orden": 18,
            "superviviente": SUP18,
            "motivo": MOTIVO18,
            "nota": NOTA18,
            "reparto": REPARTO18,
            "perdidas": PERDIDAS18,
        },
        {
            "orden": 25,
            "superviviente": SUP25,
            "motivo": MOTIVO25,
            "nota": NOTA25,
            "reparto": REPARTO25,
            "perdidas": PERDIDAS25,
        },
        {
            "orden": 26,
            "superviviente": SUP26,
            "motivo": MOTIVO26,
            "nota": NOTA26,
            "reparto": REPARTO26,
            "perdidas": PERDIDAS26,
        },
        {
            "orden": 29,
            "superviviente": SUP29,
            "motivo": MOTIVO29,
            "nota": NOTA29,
            "reparto": REPARTO29,
            "perdidas": PERDIDAS29,
        },
        {
            "orden": 30,
            "superviviente": SUP30,
            "motivo": MOTIVO30,
            "nota": NOTA30,
            "reparto": REPARTO30,
            "perdidas": PERDIDAS30,
        },
    ],
    "declarados": [DECLARADO_ACTO27],
}
