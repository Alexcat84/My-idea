# -*- coding: utf-8 -*-
"""vuelta57_planes.py . EL GENERADOR DE LOS PLANES DE LA VUELTA 57 PARA EL TRAMO
4 DE OP-U-01.

SUCESOR DECLARADO de scripts/loop/vuelta56_planes.py, al que NO reemplaza. LA
ARITMETICA Y LAS GUARDAS SON LAS SUYAS, COPIADAS LITERALMENTE Y NO RETECLEADAS
(la extraccion del INCISO desde el nodo comparando sin tildes, la cobertura
exacta, la guarda 1B, los indices CUBIERTO comprobados contra el superviviente
real, y el campo declarados_y_no_fundidos que el ejecutor exige). LO UNICO QUE
CAMBIA, y va declarado porque es lo unico que no es copia:

  1. EL FICHERO DEL TRAMO es docs/loop/TRAMO4_V57.jsonl.
  2. EL PLAN SE ESCRIBE EN docs/loop/PLAN_V57_OPU01_LOTE_*.json.
  3. LA CABECERA CITA LAS MEDICIONES DE ESTA VUELTA.

La clave del ordinal se sigue descubriendo del fichero, como en la 56: aqui es
"orden_tramo4", y el instrumento no la lleva escrita a mano.

EL INCISO SE DECLARA EN ASCII y el generador BUSCA ESE TROZO EN EL PASO REAL
comparando las dos cadenas sin acentos, y EXTRAE LA SUBCADENA REAL, con sus
acentos, del fichero del nodo. El literal que va al plan sale SIEMPRE del nodo y
nunca de mis dedos. LA GUARDA NO SE AFLOJA: despues de extraer se comprueba
igual que el trozo esta LITERAL dentro del paso, y una casacion ambigua es rojo.

DE ESCRITURA SOLO SOBRE docs/loop/PLAN_V57_*.json. No toca ni un nodo.

Uso:
  python scripts/loop/vuelta57_planes.py --lote A [--simular]
"""
import argparse
import io
import json
import os
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
TRAMO = os.path.join(RAIZ, "docs", "loop", "TRAMO4_V57.jsonl")
SALIDA = os.path.join(RAIZ, "docs", "loop")

CABECERA = {
    "operacion": "OP-U-01",
    "fecha": "2026-08-20",
    "vuelta": 57,
    "estado": "SELLADO",
    "nomina": "docs/loop/RECOMPUTO_V57_APERTURA.jsonl, corrida ANTES de la primera operacion de la vuelta",
    "tramo_definido_en": "docs/loop/SALIDA_V57_TRAMO4_NOMINA.txt, con scripts/loop/vuelta57_tramo4_nomina.py (abridor del tramo 4, sucesor declarado del de la 56). LAS DOS LECTURAS CALZAN, mismo conjunto y mismo orden, sin ninguna divergencia que diagnosticar. La LECTURA B de este tramo ya NO es un bloque fijo de la nomina de la 48 y se dice por que: el tramo 3 realmente abierto no es el bloque 101 a 150, asi que tomar el 151 a 200 dejaria FUERA DE LAS DOS LECTURAS al acto que la vuelta 56 desplazo. La lectura B es la nomina de la 48 EN SU ORDEN saltando los tramos FIJADOS. Guarda del prefijo VERDE con los 19 vivos MEDIDOS en los puestos 1 a 19 sin huecos. El tramo son los puestos 20 a 69 de hoy.",
    "dossier": "docs/loop/SALIDA_V57_DOSSIER_TRAMO4.txt (P.5, el acto leido entero con su razon entera pegada) mas docs/loop/SALIDA_V57_VARAS_TRAMO4.txt",
    "vara": "LOS 50 ACTOS DEL TRAMO 4 SON DE FUSION PURA (medido: tamano 2 y PURO A, 50 de 50): un acto de dos miembros con UN par A directo y ningun mixto. No hay lectura P.12 que hacer. El superviviente lo elige el CONTENIDO como P.8 lo define (pasos y condiciones, material propio y padre declarado EN LAS RAZONES); UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), y EL MATERIAL PROPIO DECLARADO DE UN SOLO LADO ES UNA VARA (acta 54, pregunta 4); si dos varas de contenido CHOCAN decide la pieza DECLARADA y si no hay ninguna se DECLARA y acumula para la mesa (acta 54, pregunta 2; acta 53, pregunta 3); si el contenido calla entero, EL CABLEADO DECIDE SOLO; si tambien empata, se DECLARA. Y LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO (acta 54, pregunta 1, registrada en 03_FUSIONES.md): en un acto de dos donde el unico candidato limpio es la puerta, LA PUERTA SOBREVIVE y el choque se registra en el motivo.",
    "varas_impresas": "docs/loop/SALIDA_V57_VARAS_TRAMO4.txt, una fila por acto con pasos, condiciones y cableado contados por maquina y la FORMA del veredicto impresa. Ninguna cifra de este plan esta tecleada.",
    "colisiones_esperadas": "docs/loop/SALIDA_V57_COLISIONES_ESPERADAS_TRAMO4.txt, medidas ANTES de tocar un nodo sobre EL ARCHIVO ENTERO, por PAR RESUELTO, con scripts/loop/vuelta56_colisiones_esperadas.py: 100 combinaciones simuladas y CERO que fabriquen colision, con cualquiera de los dos supervivientes en cualquiera de los 50 actos. El censo esperado de cada lote es CERO y una colision real DETIENE.",
    "vara_de_las_puertas": "GUARDA 1B: ningun absorbido de este plan es semilla de entrada ni extremo de puente aprobado, comprobado por el generador y otra vez por el ejecutor. La guarda de los CUATRO AJENOS se lee ademas POR EL RESOLUTOR en docs/loop/SALIDA_V57_TRAMO4_NOMINA.txt y sale VERDE por los dos caminos: ninguno de los cuatro entra en el tramo 4, ni literal ni bajo alias.",
    "politica_del_reparto": "LA HEREDADA Y CITADA, no reinventada (acta 51 D3; acta 52 D5 y D10; acta 54 pregunta 5; acta 55 preguntas 3, 4 y 5; registros de las vueltas 53, 54, 55 y 56): una pieza del absorbido cuyo unico contenido propio es un PARAMETRO CONCRETO de un gesto que el superviviente ya tiene va de INCISO ADOSADO cuando el paso resultante se lee limpio, y de CUBIERTO con la perdida NOMBRADA cuando no. Una pieza que es un GESTO DISTINTO va de APPEND, y una pieza mitad propia mitad ya dicha va de APPEND ENTERO con el solape declarado para la poda de la fase 04. CUANDO LA RAZON DECLARA COMPARTIDO UN GESTO QUE EL TEXTO NO DICE, PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3). LAS PERDIDAS DE CONDICIONES NO VAN DE APPEND POR DEFECTO: se NOMBRAN mientras el INCISO de condiciones no exista (acta 55, pregunta 5). El INCISO es siempre TROZO VERBATIM del paso que muere, y en este generador se EXTRAE del nodo en vez de teclearse.",
}


# --------------------------------------------------------------------------
# LOS LOTES, EN EL ORDEN IMPRESO DEL TRAMO (regla de trabajo del acta 54,
# punto 6): el lote recorre el tramo en su orden y aparta SOLO el acto con
# bloqueo declarado. Cada acto: ordinal del tramo 4, superviviente, motivo, y
# el reparto pieza a pieza. En INCISO el segundo campo es la SUBCADENA EN
# ASCII (el generador extrae del nodo la subcadena REAL con sus acentos) y el
# tercero el NEXO que la une al paso del superviviente.
# --------------------------------------------------------------------------
LOTES = {}

LOTES["A"] = {
    "titulo": "4, LOTE A DE LA VUELTA 57: LOS DIECISIETE PRIMEROS ACTOS DEL TRAMO EN SU ORDEN IMPRESO (1 a 17), apartando el 11 por EMPATE SIN VARA y el 13 y el 14 por CONTEOS QUE CHOCAN SIN PIEZA QUE DESEMPATE. Lo encabeza EL ACTO 1, que es el acto que la vuelta 56 dejo DESPLAZADO al tramo siguiente y nombrado en su reporte",
    "actos": [
        {
            "orden": 1,
            "superviviente": "crecimiento_ingresos_verdes",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO, Y ADEMAS APUNTA A LA PUERTA, ASI QUE NO HAY CHOQUE QUE REGISTRAR. Pasos 4 contra 4 y condiciones 2 contra 2: las dos varas de contenido empatan al digito, y la razon del puesto 1793 reconoce material propio a LOS DOS lados (del primero, la exigencia de que el menor impacto sea MEDIBLE y las metricas de crecimiento propias de la linea verde; del segundo, validar precio y calidad antes de comunicar el atributo y los ejemplos con nombre propio), asi que tampoco la pieza declarada desempata. Con el contenido callado entero, EL CABLEADO DECIDE SOLO y apunta a crecimiento_ingresos_verdes, 4 contra 3. Y ESE MISMO NODO ES PUERTA (extremo de puente aprobado), asi que la guarda 1B y el cableado piden lo mismo: SE DICE APARTE de los choques de puerta de las vueltas 55 y 56 justamente porque aqui NO HAY CHOQUE, y confundir las dos figuras seria la mezcla que el acta 55 castigo. NO ES EMPATE SIN VARA: el empate sin vara exige que TAMBIEN el cableado empate (acta 53, pregunta 4), y aqui no empata.",
            "pasos": {
                "1": ["INCISO", 1, "nichos de mercado desatendidos", ", incluidos los "],
                "2": ["INCISO", 2, "sin sacrificar precio ni desempeno", ", y "],
                "3": ["APPEND"],
                "4": ["INCISO", 2, "modelo EcoLogical de CardPak, Green Works de Clorox", ", con ejemplos como el "],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere y llama PUERTA: validar que el producto verde cumple primero con expectativas de precio y calidad ANTES de comunicar atributos ambientales. TRES INCISOS: los nichos de mercado desatendidos, que es el alcance del paso 1 del superviviente (que habla de clientes); el sin sacrificar precio ni desempeno, que es la restriccion del rediseno del paso 2; y los ejemplos con nombre propio, que la razon nombra como lo segundo que se perderia, adosados al mismo paso 2 porque es el que desarrolla las lineas de producto. Sus dos condiciones quedan cubiertas una a una: la diferenciacion de mercado por la de diferenciarte con innovacion ambiental, y la demanda creciente de consumidores por la de clientes que piden alternativas mas sostenibles. CERO perdidas nombradas.",
        },
        {
            "orden": 2,
            "superviviente": "critica_del_pib_como_metrica_de_progreso",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 3 contra 6 y condiciones 1 contra 3, las dos a favor de critica_del_pib_como_metrica_de_progreso, y el cableado apunta al mismo lado (1 contra 5) aunque por P.8 no le toque hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO Y ES LA VARA MAS FUERTE: la razon del puesto 1794 escribe que es un SUBCONJUNTO ESTRICTO y que del que muere NO SE PIERDE NADA PROPIO, mientras que del superviviente se perderia TODO lo que lo vuelve accionable.",
            "pasos": {
                "1": ["CUBIERTO", 2],
                "2": ["CUBIERTO", 5],
                "3": ["CUBIERTO", 4],
            },
            "condiciones": {"1": ["CUBIERTO", 2]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA Y NINGUNA SE PIERDE, que es lo que un subconjunto estricto tiene que dar: cuestionar el uso exclusivo de indicadores economicos es el paso 2 del superviviente (cuestionar si esos indicadores solo miden actividad economica sin distinguir su calidad); explorar metricas que incorporen capital natural y social es su paso 5 (proponer metricas complementarias que capturen salud ecologica, cultural y social); y diferenciar el crecimiento que genera valor real del que solo compensa danos previos es su paso 4 (evaluar el verdadero costo beneficio de la actividad economica). Su unica condicion queda cubierta por la condicion 2 del superviviente, que dice justificar el proyecto unicamente con cifras de crecimiento economico o ingresos. CERO perdidas nombradas.",
        },
        {
            "orden": 3,
            "superviviente": "manejo_de_hibridos_monstruosos",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 3 contra 4 a favor de manejo_de_hibridos_monstruosos; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que apuntaba AL MISMO LADO (2 contra 5) para que quede medido y no parezca que se calla porque estorba. La razon del puesto 1806 reconoce material propio a los DOS lados (del que muere, evaluar la toxicidad de los aditivos; del que sobrevive, el rediseno POR PARTES y comunicar la recuperacion como ventaja competitiva), asi que la vara del propio declarado EMPATA y no desempata: la que decide es la de los pasos.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 2, "mono-materiales", ", o pasar a "],
                "3": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: evaluar la toxicidad de los aditivos usados (curtientes, tintes, adhesivos) en cada componente, sin la cual un producto desmontable puede seguir siendo irreciclable. UN INCISO: los mono-materiales, que son la otra salida del paso 2 del que muere y que el superviviente no nombra, adosados a su rediseno por partes. Su paso 1 queda cubierto por el paso 1 del superviviente, que identifica los productos que mezclan biologico y tecnico sin separacion posible. SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto: detectar materiales toxicos ocultos en combinaciones de manufactura no es ninguna de las dos del superviviente, que hablan de no poder clasificar el producto limpiamente y de necesitar una solucion de transicion. CERO perdidas nombradas.",
        },
        {
            "orden": 4,
            "superviviente": "vision_alineacion_sostenibilidad",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 3 contra 6 y condiciones 2 contra 3, las dos a favor de vision_alineacion_sostenibilidad, y el cableado apunta al mismo lado (3 contra 7) aunque por P.8 no le toque hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO: la razon del puesto 1811 escribe que es un SUBCONJUNTO ESTRICTO, que lo unico propio del que muere es DE SUJETO (que sea el director general quien la articule y publicamente) y que del superviviente se perderia todo lo que la vuelve operable.",
            "pasos": {
                "1": ["INCISO", 2, "publicamente", ", y articulala "],
                "2": ["CUBIERTO", 2],
                "3": ["CUBIERTO", 6],
            },
            "condiciones": {"1": ["CUBIERTO", 3], "2": ["APPEND"]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA Y LA UNICA COSA PROPIA QUE LA RAZON NOMBRA SE SALVA: el PUBLICAMENTE va de INCISO adosado al paso 2 del superviviente, que es donde se redacta la declaracion. Y SE DICE UNA COSA MEDIDA EN VEZ DE CALLARLA: la otra mitad de ese propio, que sea EL DIRECTOR GENERAL quien la articule, NO se pierde del nodo, porque el entregable del superviviente dice literalmente que el documento va definido y comunicado POR TI COMO FUNDADOR, que es el mismo sujeto dicho en la voz de este catalogo. Se marca CUBIERTO y NO se cuenta perdida, y la comprobacion queda escrita. Su paso 3 (diseminar a todos los niveles) es el paso 6 del superviviente. SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto: que el impulso venga solo de mandos medios sin respaldo ejecutivo no lo dice ninguna de las tres del superviviente. CERO perdidas nombradas.",
        },
        {
            "orden": 5,
            "superviviente": "incentivos_reconocimiento_sostenibilidad",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 4 contra 6 y condiciones 2 contra 3, las dos a favor de incentivos_reconocimiento_sostenibilidad, y el cableado apunta al mismo lado (6 contra 7) aunque por P.8 no le toque hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO Y POR CANTIDAD: la razon del puesto 1816 nombra UNA sola pieza propia del que muere (los indicadores de sostenibilidad en la evaluacion de desempeno de los gerentes) contra TRES del superviviente (los concursos con premios tangibles, los beneficios ecologicos concretos y los rankings entre equipos, sedes o periodos).",
            "pasos": {
                "1": ["APPEND"],
                "2": ["INCISO", 5, "bonos y promociones", ", incluidos "],
                "3": ["INCISO", 1, "premios de reconocimiento anual", ", por ejemplo "],
                "4": ["INCISO", 3, "reuniones de staff y sitios web corporativos", ", en "],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: incorporar indicadores de sostenibilidad en las evaluaciones de desempeno de los gerentes, que es la unica linea del par que mete el tema en el instrumento formal de recursos humanos y no solo en el premio. TRES INCISOS, y los tres son parametros concretos de gestos que el superviviente ya tiene: los bonos y promociones, adosados a su paso 5 (vincular el desempeno a la compensacion o al presupuesto); los premios de reconocimiento anual, adosados a su paso 1 (el sistema de reconocimiento publico regular); y los dos canales de publicacion, adosados a su paso 3 (publicar los datos de forma transparente). SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto: que las metas ambientales no se traduzcan en resultados concretos no lo dice ninguna de las tres del superviviente. CERO perdidas nombradas.",
        },
        {
            "orden": 6,
            "superviviente": "menos_malo_vs_bueno",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 4 contra 3 a favor de menos_malo_vs_bueno; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice porque apuntaba al OTRO (2 contra 3): el cableado solo decide cuando el contenido calla ENTERO, y aqui no calla. La razon del puesto 1818 reconoce material propio a los DOS lados (del que muere, presentar a los interesados la vision de ser cien por ciento bueno; del que sobrevive, el diagnostico de si las mejoras son reduccion o transformacion y las metricas de eficiencia que optimizan el aspecto equivocado), asi que esa vara EMPATA y no desempata.",
            "pasos": {
                "1": ["CUBIERTO", 4],
                "2": ["INCISO", 3, "al menos una meta ambiental", ", empezando por "],
                "3": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: presentar a los interesados la vision de ser cien por ciento bueno como alternativa a las metas actuales, que es el unico paso del par que saca la reformulacion del escritorio y la lleva a una reunion. UN INCISO: el AL MENOS UNA META AMBIENTAL, que es el grano concreto de la reformulacion y que el paso 3 del superviviente no fija. Su paso 1 (revisar el lenguaje de las metas) queda cubierto por el paso 4 del superviviente, que manda evitar el lenguaje de culpa y nombra los mismos ejemplos. SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto: que el equipo necesite una vision inspiradora en lugar de una lista de restricciones no lo dice ninguna de las dos del superviviente. CERO perdidas nombradas.",
        },
        {
            "orden": 7,
            "superviviente": "diseno_mensaje_verde",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 5 contra 3 y condiciones 2 contra 1, las dos a favor de diseno_mensaje_verde, y el cableado apunta al mismo lado (4 contra 3) aunque por P.8 no le toque hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO Y POR CANTIDAD: la razon del puesto 1824 nombra DOS piezas propias del que muere (el humor y las historias atractivas, y el vocabulario de innovacion o progreso) contra TRES del superviviente (alinear el mensaje con lo que le importa al cliente objetivo, la coherencia con la identidad historica de la marca, y seleccionar mensajeros creibles).",
            "pasos": {
                "1": ["INCISO", 4, "humor o historias atractivas", ", con "],
                "2": ["INCISO", 5, "ahorro, calidad de vida", ", del tipo "],
                "3": ["INCISO", 4, "conceptos pragmaticos como innovacion o progreso", ", apoyandote en "],
            },
            "condiciones": {"1": ["APPEND"]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA Y NINGUNA SE PIERDE: los tres pasos del que muere son los mismos movimientos del superviviente, y LAS DOS COSAS QUE LA RAZON NOMBRA COMO PROPIAS SE SALVAN LAS DOS DE INCISO. El humor y las historias atractivas y los conceptos pragmaticos de innovacion o progreso se adosan los dos al paso 4 del superviviente, que es el que fija el tono; los beneficios de ahorro y calidad de vida se adosan a su paso 5, que es el que fija el foco en beneficios tangibles. SU UNICA CONDICION VIAJA ENTERA por ser un disparador distinto: ampliar el alcance a audiencias NO COMPROMETIDAS con el ambientalismo no lo dice ninguna de las dos del superviviente, que hablan de haber validado el atributo verde y de campanas anteriores sin conexion emocional. CERO perdidas nombradas.",
        },
        {
            "orden": 8,
            "superviviente": "unirse_organizacion_rsc_ambiental",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 4 contra 4, empatados, y condiciones 1 contra 2 a favor de unirse_organizacion_rsc_ambiental, que es la unica vara de contenido no empatada del acto. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que ADEMAS EMPATA (2 contra 2), con lo que no habria decidido nada. La razon del puesto 1826 reconoce material propio a los DOS lados (del que muere, que la participacion sea en el intercambio de mejores practicas; del que sobrevive, aprovechar el acceso a redes de inversionistas o certificaciones), asi que esa vara EMPATA y no desempata. NO ES EMPATE SIN VARA porque la vara de las condiciones SI separa.",
            "pasos": {
                "1": ["INCISO", 1, "ONGs o iniciativas", ", incluidas "],
                "2": ["INCISO", 2, "compromisos", ", y sus "],
                "3": ["CUBIERTO", 3],
                "4": ["INCISO", 3, "el intercambio de mejores practicas", ", incluido "],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA Y NINGUNA SE PIERDE: la razon mide que LOS CUATRO PASOS SE CORRESPONDEN UNO A UNO, y lo unico que la razon declara propio del que muere, que la participacion sea en el INTERCAMBIO DE MEJORES PRACTICAS, se salva de INCISO adosado al paso 3 del superviviente, que es donde vive el participar activamente. Otros dos incisos afinan alcance: las ONGs o iniciativas como tipo de organizacion a investigar, y los COMPROMISOS de membresia junto a los requisitos. Su unica condicion queda cubierta por la condicion 1 del superviviente, que dice credibilidad externa y acceso a mejores practicas de la industria. CERO perdidas nombradas.",
        },
        {
            "orden": 9,
            "superviviente": "compra_offsets_carbono",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 5 contra 4 y condiciones 2 contra 1, las dos a favor de compra_offsets_carbono, y el cableado apunta al mismo lado (2 contra 1) aunque por P.8 no le toque hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO Y POR CANTIDAD: la razon del puesto 1828 nombra UNA sola pieza propia del que muere (definir que alcances de emisiones entran en la meta) contra DOS del superviviente (que porcentaje de las emisiones no puede reducirse internamente, y verificar la validez y trazabilidad de los proyectos).",
            "pasos": {
                "1": ["APPEND"],
                "2": ["INCISO", 4, "antes de recurrir a compensaciones", " El plan de reduccion se establece "],
                "3": ["CUBIERTO", 2],
                "4": ["INCISO", 5, "el alcance real de la declaracion de neutralidad", " Se comunica igualmente "],
            },
            "condiciones": {"1": ["CUBIERTO", 2]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: definir QUE ALCANCES DE EMISIONES entran en la meta de neutralidad, que es lo que decide si una declaracion de neutralidad significa algo o solo cubre la electricidad de las oficinas. DOS INCISOS: el ANTES DE RECURRIR A COMPENSACIONES, que es el orden que el paso 4 del superviviente da por supuesto al mandar combinar offsets con metas de reduccion real; y el ALCANCE REAL DE LA DECLARACION, adosado a su paso 5, que ya manda comunicar de forma transparente. Su paso 3 queda cubierto por el paso 2 del superviviente, que investiga proveedores certificados. Su unica condicion queda cubierta por la condicion 2 del superviviente, que habla de posicionarse como carbono neutral en el mercado. CERO perdidas nombradas.",
        },
        {
            "orden": 10,
            "superviviente": "eco_efectividad_2",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 5 contra 4 a favor de eco_efectividad_2; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que apuntaba AL MISMO LADO (6 contra 2). La razon del puesto 1829 reconoce material propio a los DOS lados (del que muere, disenar sistemas que se autorregulen; del que sobrevive, el analisis del ciclo de vida con todos los flujos de materiales y el proposito completo del sistema), asi que esa vara EMPATA y no desempata: la que decide es la de los pasos.",
            "pasos": {
                "1": ["INCISO", 2, "si realmente regenera el entorno", ", y "],
                "2": ["CUBIERTO", 4],
                "3": ["APPEND"],
                "4": ["INCISO", 5, "regeneracion positiva", ", y en concreto la de "],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: disenar sistemas que se AUTORREGULEN, inspirados en los ciclos naturales de agua, nutrientes y energia, que es la unica linea del par que pide una propiedad del sistema y no una intencion del disenador. DOS INCISOS: el SI REALMENTE REGENERA EL ENTORNO, que es la segunda mitad de la pregunta del paso 2 del superviviente (que solo pregunta si el diseno es el correcto y no solo mas eficiente); y la REGENERACION POSITIVA como nombre de la meta, adosada a su paso 5, que manda poner metas positivas sin nombrar esta. Su paso 2 queda cubierto por el paso 4 del superviviente, que redisena para que los materiales se conviertan en nutrientes. SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto: buscar diferenciarse de las estrategias convencionales de sostenibilidad no lo dice ninguna de las dos del superviviente. CERO perdidas nombradas.",
        },
        {
            "orden": 12,
            "superviviente": "eco_eficiencia",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 5 contra 4 y condiciones 3 contra 2, las dos a favor de eco_eficiencia, y el cableado apunta al mismo lado (6 contra 3) aunque por P.8 no le toque hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO Y POR CANTIDAD: la razon del puesto 1905 nombra DOS piezas propias del que muere (medir por cada etapa del proceso y el sistema de seguimiento con metricas ampliables) contra TRES del superviviente (los nombres de los marcos de identificacion de desperdicio, la revision de la utilizacion de activos fijos, y reportar los ahorros para justificar la expansion).",
            "pasos": {
                "1": ["INCISO", 1, "en cada etapa de tu proceso", ", y "],
                "2": ["INCISO", 2, "redisena el proceso para reducirlo", ", y "],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 3],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "UNA PIEZA VIAJA ENTERA y es la que la razon llama lo unico del par que deja instalada una medicion permanente en vez de una auditoria de una vez: el sistema de seguimiento ambiental con metricas que se puedan ir ampliando, el panel de control digital. DOS INCISOS: el EN CADA ETAPA DE TU PROCESO, que es el grano mas fino que la razon nombra como la otra pieza propia y que el paso 1 del superviviente no tiene (mide por operaciones completas); y el REDISENA EL PROCESO PARA REDUCIRLO, que es la accion que sigue a identificar el desperdicio y que el paso 2 del superviviente deja en identificar. Su paso 4 queda cubierto por el paso 3 del superviviente, que prioriza inversiones por retorno. UNA PERDIDA NOMBRADA: su condicion 1 acota el disparador a UN CONTEXTO DE RECESION ECONOMICA y la condicion 1 del superviviente solo dice buscar reducir costos operativos; el INCISO para condiciones no existe en el instrumento (pendiente de doctrina heredado) y por eso la perdida se nombra en vez de repararse.",
        },
        {
            "orden": 15,
            "superviviente": "export_administration_regulations",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 6 contra 4 y condiciones 3 contra 2, las dos a favor de export_administration_regulations, y el cableado EMPATA (4 contra 4), con lo que no habria decidido nada aunque le tocara hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO Y ES LA VARA MAS FUERTE: la razon del puesto 1943 escribe que es un SUBCONJUNTO ESTRICTO, que del que muere NO SE PIERDE NADA PROPIO, y que del superviviente se perderian dos piezas duras (separar en un paso propio verificar el uso final y el usuario final, y APLICAR POR LA LICENCIA, que es el unico paso del par que ejecuta el tramite en vez de solo determinarlo).",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
                "3": ["CUBIERTO", 4],
                "4": ["CUBIERTO", 6],
            },
            "condiciones": {"1": ["APPEND"], "2": ["CUBIERTO", 2]},
            "nota": "NINGUNA PIEZA DE PASO VIAJA ENTERA Y NINGUNA SE PIERDE, que es lo que un subconjunto estricto tiene que dar: la clasificacion tecnica es el paso 1 del superviviente, la consulta a la tabla de las regulaciones es su paso 2, la clasificacion de mercancia u opinion consultiva es su paso 4, y la oficina local del servicio comercial es su paso 6. SU CONDICION 1 VIAJA ENTERA por ser un disparador distinto y MAS ANCHO: dice ANTES DE CUALQUIER EMBARQUE DE EXPORTACION, y la condicion 1 del superviviente solo dice si vas a exportar un producto POR PRIMERA VEZ; no es un matiz sino otro momento, y APPEND no pierde nada. Su condicion 2 queda cubierta por la condicion 2 del superviviente, que nombra el doble uso civil y militar. CERO perdidas nombradas.",
        },
        {
            "orden": 16,
            "superviviente": "seguro_exportacion",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 4 contra 5 a favor de seguro_exportacion; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, Y SE DICE FUERTE PORQUE AQUI APUNTABA AL OTRO CON MUCHA DIFERENCIA (8 contra 2): el cableado solo decide cuando el contenido calla ENTERO, y aqui no calla. LA PIEZA DECLARADA APUNTA AL MISMO LADO QUE LOS PASOS y es lo que sostiene la eleccion: la razon del puesto 1947 escribe que del superviviente se perderia UNA MITAD ENTERA DEL NODO, la del credito (evaluar el seguro de credito a la exportacion y verificar los requisitos de las instituciones financieras del comprador), y que del que muere se perderia UNA sola linea. Son dos riesgos distintos, que la mercancia se dane y que el cliente no pague, y solo uno de los dos nodos cubre los dos.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
                "3": ["INCISO", 3, "verificar documentacion", ", y "],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: consultar con aseguradoras internacionales o agentes de carga para DEFINIR EL NIVEL DE COBERTURA (tipicamente el 110 por ciento del valor CIF o CIP), que es lo unico del par que dice CUANTO asegurar y no solo QUIEN. UN INCISO: el VERIFICAR DOCUMENTACION, que es la accion concreta que sigue a no asumir que el comprador contrato cobertura y que el paso 3 del superviviente deja implicita. Y SE DICE UNA COSA MEDIDA EN VEZ DE CALLARLA: su paso 1 dice terminos de venta ENTRE PARENTESIS INCOTERMS y el paso 1 del superviviente dice terminos de venta a secas; el nombre no se pierde del catalogo porque terminos_de_venta_incoterms y incoterms_reglas_comerciales_internacionales son nodos propios y ademas el acto 17 de este mismo tramo los funde. Se marca CUBIERTO y NO se cuenta perdida, con la comprobacion escrita. SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto: que el termino de venta acordado responsabilice al exportador por el seguro no lo dice ninguna de las dos del superviviente. UNA PERDIDA NOMBRADA: su condicion 1 dispara ante CUALQUIER envio internacional que necesite definir cobertura de riesgos de transporte, y la condicion 1 del superviviente acota a MERCANCIA DE ALTO VALOR; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra.",
        },
        {
            "orden": 17,
            "superviviente": "incoterms_reglas_comerciales_internacionales",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 6 contra 3 y condiciones 3 contra 2, las dos a favor de incoterms_reglas_comerciales_internacionales, y el cableado apunta al mismo lado y por mucho (13 contra 4) aunque por P.8 no le toque hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO Y ES LA VARA MAS FUERTE: la razon del puesto 1952 escribe que es un SUBCONJUNTO ESTRICTO, que del que muere NO SE PIERDE NADA PROPIO, y que del superviviente se perderian TRES piezas duras (negociar el punto exacto de transferencia de riesgo y costo, consultar con un agente de carga o aduanal las obligaciones especificas, y verificar que el termino sea compatible con los requisitos de documentacion del pais importador).",
            "pasos": {
                "1": ["CUBIERTO", 2],
                "2": ["CUBIERTO", 4],
                "3": ["CUBIERTO", 3],
            },
            "condiciones": {"1": ["CUBIERTO", 2], "2": ["CUBIERTO", 3]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA Y NINGUNA SE PIERDE, que es lo que un subconjunto estricto tiene que dar: seleccionar el termino segun el modo de transporte es el paso 2 del superviviente; especificarlo en la factura proforma y en la comercial es su paso 4, que ademas anade la cotizacion y el contrato de venta; y comunicarlo al comprador y al agente de carga para evitar disputas es su paso 3, que negocia con el comprador el punto exacto de transferencia de riesgo y costo. Sus dos condiciones quedan cubiertas una a una por las condiciones 2 y 3 del superviviente, que hablan de negociar un contrato definiendo quien asume costos y riesgos y de la confusion sobre responsabilidades de transporte, seguro o despacho. CERO perdidas nombradas.",
        },
    ],
    "declarados": [
        {
            "orden": 11,
            "miembros": ["disruptores_endocrinos_y_salud_industrial", "quimicos_toxicos_en_diseno"],
            "especie": "EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN",
            "motivo": "LAS DOS VARAS DE CONTENIDO EMPATAN AL DIGITO (pasos 4 contra 4 y condiciones 2 contra 2) Y EL CABLEADO TAMBIEN EMPATA (2 contra 2 en el cuadro de varas). El empate sin vara exige exactamente eso, que TAMBIEN el cableado empate (acta 53, pregunta 4), y aqui se cumple. Y LA PIEZA DECLARADA NO DESEMPATA porque hay material propio declarado a LOS DOS lados: la razon del puesto 1884 escribe que de quimicos_toxicos_en_diseno se perderian las PRUEBAS DE EMISION DE GASES Y LIBERACION DE SUSTANCIAS DURANTE EL USO NORMAL, que es la unica linea del par que comprueba lo que el producto suelta cuando ya esta en casa del cliente; y que de disruptores_endocrinos_y_salud_industrial se perderian la CONSULTA A LAS BASES DE DATOS antes de cerrar la lista de materiales, el PROTOCOLO INTERNO DE REVISION TOXICOLOGICA, y sobre todo PRIORIZAR LA SUSTITUCION DE LAS SUSTANCIAS NO ESTUDIADAS. Sin vara que separe, el acto SE DECLARA y acumula.",
            "acumula_para": "LA MESA. Y con un dato que la propia razon aporta y que conviene que la mesa tenga delante: la pieza de disruptores_endocrinos_y_salud_industrial que la razon llama LA UNICA REGLA PRECAUTORIA DEL CATALOGO (no basta con quitar lo que se sabe malo, hay que desconfiar de lo que nadie ha mirado) no tiene equivalente en ningun otro nodo del par. Un empate de conteos que pone en riesgo una regla unica del catalogo es el caso que hace visible el pendiente de doctrina 1 desde otro angulo que el del acto 45 de la vuelta 56."
        },
        {
            "orden": 13,
            "miembros": ["desperdicio_es_alimento", "metabolismo_biologico_y_tecnico"],
            "especie": "CONTEOS QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA",
            "motivo": "LAS DOS VARAS DE CONTENIDO APUNTAN A LADOS DISTINTOS: pasos 6 contra 5 a favor de desperdicio_es_alimento y condiciones 3 contra 4 a favor de metabolismo_biologico_y_tecnico. El cableado NO PUEDE HABLAR y se dice por que: por P.8 solo decide cuando el contenido CALLA ENTERO, y aqui el contenido no calla, CHOCA (acta 54, pregunta 4; misma figura que el acto 27 del tramo 3 en la vuelta 56). Y LA PIEZA DECLARADA NO DESEMPATA porque la razon del puesto 1917 nombra DOS perdidas de cada lado: de metabolismo_biologico_y_tecnico, la regla de NO MEZCLAR dicha como prohibicion explicita y que las RUTAS DE RETORNO SEAN ESPECIFICAS Y DISTINTAS; de desperdicio_es_alimento, analizar el ciclo de vida completo identificando QUE SUCEDE CON CADA SALIDA y EXPLORAR MODELOS DE SERVICIO reteniendo la propiedad del material tecnico. Dos y dos: la vara del propio declarado EMPATA. Sin vara que separe, el acto SE DECLARA y acumula.",
            "acumula_para": "LA MESA. Con un dato de familia: los dos nodos son el eje del que cuelga media seccion del libro (el paso 5 de metabolismo_biologico_y_tecnico nombra el upcycling sobre el downcycling y el paso 6 de desperdicio_es_alimento cambia el MODELO DE NEGOCIO en vez del producto), y ninguno de los dos es la madre del otro. Es el segundo ejemplar de conteos que chocan sin pieza que desempate, y el primero fuera del dominio core."
        },
        {
            "orden": 14,
            "miembros": ["carta_de_credito_letter_of_credit", "letters_of_credit"],
            "especie": "CONTEOS QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA",
            "motivo": "LAS DOS VARAS DE CONTENIDO APUNTAN A LADOS DISTINTOS: pasos 5 contra 6 a favor de letters_of_credit y condiciones 3 contra 2 a favor de carta_de_credito_letter_of_credit. El cableado NO PUEDE HABLAR por la misma razon que en el acto 13: el contenido no calla, CHOCA. Y LA PIEZA DECLARADA NO DESEMPATA porque la razon del puesto 1942 nombra DOS perdidas de cada lado: de carta_de_credito_letter_of_credit, EL PLAZO CONCRETO DE PRESENTACION (veintiun dias desde el embarque, que es la unica cifra del par y la que hace perder cobros) y coordinar con el BANCO CONFIRMADOR del pais del exportador; de letters_of_credit, las dos de la etapa ANTERIOR, negociar que la carta sea IRREVOCABLE (que es la condicion que la vuelve util) y solicitar la CONFIRMACION DE UN BANCO PROPIO si hay riesgo pais. Dos y dos: la vara del propio declarado EMPATA. Sin vara que separe, el acto SE DECLARA y acumula.",
            "acumula_para": "LA MESA. Y con una observacion medida que la mesa deberia tener delante porque no es de conteo: los dos nodos cubren ETAPAS DISTINTAS del mismo tramite, uno la negociacion previa a que la carta exista y el otro la revision de la carta ya recibida, y la razon lo dice con esas palabras. Es el PRIMER PAR DEL DOMINIO DE EXPORTACION que entra a la mesa, y entra por la misma puerta por la que entro el ambiental."
        },
    ],
}


def cargar_jsonl(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def puertas():
    """MISMA fuente que scripts/loop/vuelta48_puertas_en_el_lote.py."""
    out = set()
    p = os.path.join(RAIZ, "dataset", "metadata", "entry_seeds.json")
    if os.path.exists(p):
        out.update(json.load(io.open(p, encoding="utf-8")).get("seeds", []))
    packs = os.path.join(RAIZ, "packs")
    if os.path.isdir(packs):
        for d in sorted(os.listdir(packs)):
            q = os.path.join(packs, d, "metadata", "entry_seeds.json")
            if os.path.exists(q):
                out.update(json.load(io.open(q, encoding="utf-8")))
            q = os.path.join(packs, d, "metadata", "bridges_aprobados.json")
            if os.path.exists(q):
                for x in json.load(io.open(q, encoding="utf-8")).get("aprobados", []):
                    for extremo in ("core", "dominio"):
                        if x.get(extremo):
                            out.add(x[extremo])
    return out


def sin_acentos(s):
    """Quita las tildes dejando el resto intacto: la enye, los signos de
    interrogacion de apertura y la puntuacion se conservan."""
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def extraer_verbatim(texto, trozo_ascii):
    """LA NOVEDAD DE ESTE GENERADOR, declarada en el docstring: recibe el trozo
    escrito EN ASCII, lo casa contra el paso REAL comparando las dos cadenas sin
    tildes, y devuelve LA SUBCADENA REAL del paso, con sus acentos. Devuelve
    (verbatim, motivo_del_rojo). Si no casa o casa en mas de un sitio, devuelve
    None y el motivo: una extraccion ambigua no es una extraccion."""
    plano_texto = sin_acentos(texto)
    plano_trozo = sin_acentos(trozo_ascii)
    if len(plano_texto) != len(texto):
        return None, "la normalizacion cambio la longitud del paso y las posiciones no son fiables"
    veces = plano_texto.count(plano_trozo)
    if veces == 0:
        return None, "el trozo no casa dentro del paso ni comparando sin tildes"
    if veces > 1:
        return None, "el trozo casa %d veces dentro del paso: extraccion ambigua" % veces
    i = plano_texto.index(plano_trozo)
    return texto[i:i + len(plano_trozo)], None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lote", required=True)
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    filas = cargar_jsonl(TRAMO)
    # LO UNICO QUE NO ES COPIA: la clave del ordinal se descubre del fichero.
    claves = sorted({k for k in filas[0] if k.startswith("orden_tramo")}) if filas else []
    if len(claves) != 1:
        print("ROJO: el fichero del tramo tiene %d claves de ordinal (%s). PARADA."
              % (len(claves), claves))
        return 1
    ORD = claves[0]
    tramo = {r[ORD]: r for r in filas}
    prot = puertas()
    lote = LOTES[a.lote]

    print("=" * 78)
    print("GENERADOR DEL PLAN DEL LOTE %s DEL TRAMO 4 (vuelta 57)" % a.lote)
    print("=" * 78)
    print()

    fallos = []
    actos = []
    for spec in lote["actos"]:
        n = spec["orden"]
        if n not in tramo:
            fallos.append("acto %d: no esta en el tramo vivo %s" % (n, TRAMO))
            continue
        act = tramo[n]
        mi = sorted(act["miembros"])
        sup = spec["superviviente"]
        if sup not in mi:
            fallos.append("acto %d: el superviviente %s no es miembro" % (n, sup))
            continue
        ab = [x for x in mi if x != sup][0]
        if ab in prot:
            fallos.append("acto %d: GUARDA 1B EN ROJO, el absorbido %s es puerta" % (n, ab))
        oa = json.load(io.open(os.path.join(NODOS, ab + ".json"), encoding="utf-8"))
        os_ = json.load(io.open(os.path.join(NODOS, sup + ".json"), encoding="utf-8"))
        if oa.get("deprecado") or os_.get("deprecado"):
            fallos.append("acto %d: alguno de los dos miembros YA esta deprecado" % n)
        pa = oa.get("pasos_accionables") or []
        ca = oa.get("condiciones_activacion") or []
        ps = os_.get("pasos_accionables") or []
        cs = os_.get("condiciones_activacion") or []

        marcas_p, marcas_c = {}, {}
        for i, texto in enumerate(pa, 1):
            m = spec["pasos"].get(str(i))
            if not m:
                fallos.append("acto %d: el paso %d de %s no tiene marca" % (n, i, ab))
                continue
            if m[0] == "APPEND":
                marcas_p[str(i)] = "APPEND"
            elif m[0] == "CUBIERTO":
                if not (1 <= m[1] <= len(ps)):
                    fallos.append("acto %d: CUBIERTO:%d y el superviviente tiene %d pasos"
                                  % (n, m[1], len(ps)))
                marcas_p[str(i)] = "CUBIERTO:%d" % m[1]
            elif m[0] == "CUBIERTO_COND":
                if not (1 <= m[1] <= len(cs)):
                    fallos.append("acto %d: CUBIERTO_COND:%d y el superviviente tiene %d condiciones"
                                  % (n, m[1], len(cs)))
                marcas_p[str(i)] = "CUBIERTO_COND:%d" % m[1]
            elif m[0] == "INCISO":
                _, k, ascii_trozo, nexo = m
                trozo, motivo = extraer_verbatim(texto, ascii_trozo)
                if trozo is None:
                    fallos.append("acto %d, paso %d de %s: INCISO %r, %s"
                                  % (n, i, ab, ascii_trozo, motivo))
                    continue
                # LA GUARDA NO SE AFLOJA: tras extraer, se comprueba LITERAL.
                if trozo not in texto:
                    fallos.append("acto %d: el INCISO extraido %r NO es trozo verbatim del paso %d de %s"
                                  % (n, trozo, i, ab))
                if "|" in trozo or "|" in nexo:
                    fallos.append("acto %d: el INCISO o su nexo llevan la barra vertical, que es el separador de la marca" % n)
                if not (1 <= k <= len(ps)):
                    fallos.append("acto %d: INCISO al paso %d y el superviviente tiene %d"
                                  % (n, k, len(ps)))
                else:
                    # LA GUARDA DE LA JUNTURA, NUEVA EN ESTE GENERADOR Y CON SU
                    # MOTIVO MEDIDO: la vuelta 56 escribio SEIS junturas de PUNTO
                    # MAS COMA en sus lotes A y B y tuvo que repararlas despues
                    # con un instrumento aparte, porque el paso del superviviente
                    # terminaba en punto y el nexo empezaba por coma. Aqui la
                    # juntura se comprueba ANTES de sellar el plan: si el paso
                    # acaba en punto y el nexo abre con coma o punto y coma, es
                    # ROJO y no se escribe nada. Una guarda que se corre despues
                    # del dano repara; esta impide.
                    resultante = ps[k - 1] + nexo + trozo
                    if (ps[k - 1].rstrip().endswith((".", "!", "?"))
                            and nexo.lstrip().startswith((",", ";"))):
                        fallos.append(
                            "acto %d, paso %d de %s: JUNTURA ROTA, el paso del "
                            "superviviente acaba en punto y el nexo abre con coma: %r"
                            % (n, i, ab, resultante[max(0, len(ps[k - 1]) - 30):][:80]))
                    print("  acto %-3d INCISO al paso %d" % (n, k))
                    print("      trozo pedido en ASCII : %r" % ascii_trozo)
                    print("      trozo EXTRAIDO del nodo: %r" % trozo)
                    print("      paso resultante        : %s" % (ps[k - 1] + nexo + trozo))
                marcas_p[str(i)] = "INCISO:%d|%s|%s" % (k, trozo, nexo)
            else:
                fallos.append("acto %d: marca desconocida %r" % (n, m))
        for i, texto in enumerate(ca, 1):
            m = spec["condiciones"].get(str(i))
            if not m:
                fallos.append("acto %d: la condicion %d de %s no tiene marca" % (n, i, ab))
                continue
            if m[0] == "APPEND":
                marcas_c[str(i)] = "APPEND"
            elif m[0] == "CUBIERTO":
                if not (1 <= m[1] <= len(cs)):
                    fallos.append("acto %d: CUBIERTO:%d y el superviviente tiene %d condiciones"
                                  % (n, m[1], len(cs)))
                marcas_c[str(i)] = "CUBIERTO:%d" % m[1]
            else:
                fallos.append("acto %d: marca de condicion desconocida %r" % (n, m))
        sobra_p = set(spec["pasos"]) - {str(i) for i in range(1, len(pa) + 1)}
        sobra_c = set(spec["condiciones"]) - {str(i) for i in range(1, len(ca) + 1)}
        if sobra_p or sobra_c:
            fallos.append("acto %d: marcas que sobran, pasos %s condiciones %s"
                          % (n, sorted(sobra_p), sorted(sobra_c)))

        actos.append({
            "orden": n,
            "miembros": [sup, ab],
            "miembros_del_acto_entero": mi,
            "figura": "FUSION PURA, un solo par A directo y ningun mixto",
            "superviviente": sup,
            "motivo": spec["motivo"],
            "absorbidos": [ab],
            "pasos": {ab: marcas_p},
            "condiciones": {ab: marcas_c},
            "nota_del_reparto": spec["nota"],
        })

    print()
    if fallos:
        print("  ROJO, %d fallos y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("     %s" % f)
        return 1
    print("  las %d fichas del lote %s: TODAS en verde" % (len(actos), a.lote))
    print("  guarda 1B: ningun absorbido es puerta")
    print("  cobertura: cada paso y cada condicion de cada absorbido con marca UNICA")
    print("  incisos: todos EXTRAIDOS del nodo y comprobados VERBATIM dentro del paso")
    print()
    print("  RESUMEN DEL REPARTO POR ACTO:")
    tot = {"APPEND": 0, "CUBIERTO": 0, "INCISO": 0}
    for x in actos:
        c = {"APPEND": 0, "CUBIERTO": 0, "INCISO": 0}
        for d in (x["pasos"], x["condiciones"]):
            for marcas in d.values():
                for m in marcas.values():
                    k = "APPEND" if m == "APPEND" else ("INCISO" if m.startswith("INCISO") else "CUBIERTO")
                    c[k] += 1
                    tot[k] += 1
        print("     acto %-3d sobrevive %-46s piezas %2d (enteras %d, ya dichas %d, de INCISO %d)"
              % (x["orden"], x["superviviente"], sum(c.values()),
                 c["APPEND"], c["CUBIERTO"], c["INCISO"]))
    print("     TOTAL del lote %s: piezas %d (enteras %d, ya dichas %d, de INCISO %d)"
          % (a.lote, sum(tot.values()), tot["APPEND"], tot["CUBIERTO"], tot["INCISO"]))

    plan = dict(CABECERA)
    plan["tramo"] = lote["titulo"]
    plan["actos"] = actos
    # EL CAMPO QUE EL EJECUTOR IMPRIME AL CERRAR Y QUE NO ES OPCIONAL: sin el,
    # vuelta49_fundir_tramo.py cae con KeyError DESPUES de haber hecho todas las
    # guardas en verde (le paso a la vuelta 53 y otra vez a la 54). Va SIEMPRE.
    plan["declarados_y_no_fundidos"] = lote.get("declarados", [])
    destino = os.path.join(SALIDA, "PLAN_V57_OPU01_LOTE_%s.json" % a.lote)
    if not a.simular:
        io.open(destino, "w", encoding="utf-8", newline=chr(10)).write(
            json.dumps(plan, ensure_ascii=False, indent=1) + chr(10))
        print()
        print("  plan escrito: %s" % os.path.relpath(destino, RAIZ))
    else:
        print()
        print("  MODO SIMULAR: no se escribe el plan.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
