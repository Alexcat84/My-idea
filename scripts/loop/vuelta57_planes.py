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


LOTES["B"] = {
    "titulo": "4, LOTE B DE LA VUELTA 57: LOS ACTOS 18 A 34 EN EL ORDEN IMPRESO DEL TRAMO, apartando el 24 por EMPATE SIN VARA, el 31 por CONTEOS QUE CHOCAN SIN PIEZA QUE DESEMPATE, y el 25 por una especie que la campana no habia visto: LOS DOS MIEMBROS SON PUERTA",
    "actos": [
        {
            "orden": 18,
            "superviviente": "certificado_de_origen_tratados_libre_comercio",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 5 contra 5, empatados, y condiciones 2 contra 1 a favor de certificado_de_origen_tratados_libre_comercio, que es la unica vara de contenido no empatada del acto. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que ADEMAS EMPATA (2 contra 2), con lo que no habria decidido nada. La razon del puesto 1955 reconoce material propio a los DOS lados (del que sobrevive, la tercera via de calificacion y conservar la documentacion por el periodo que exija la aduana; del que muere, las cifras y los nombres de los formularios), asi que esa vara EMPATA y no desempata: la que decide es la de las condiciones. NO ES EMPATE SIN VARA porque la vara de las condiciones SI separa.",
            "pasos": {
                "1": ["INCISO", 2, "las cuatro reglas de origen del Articulo 401", ", que son "],
                "2": ["INCISO", 3, "60% metodo de transaccion o 50% metodo de costo neto", ", con los umbrales de "],
                "3": ["INCISO", 4, "CF 434, Form B-232, o Certificado de Origen", ", en el formulario que corresponda: "],
                "4": ["CUBIERTO", 1],
                "5": ["INCISO", 5, "disponible para el importador", ", y "],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA Y LAS TRES COSAS QUE LA RAZON LLAMA LAS CIFRAS Y LOS NOMBRES SE SALVAN LAS TRES DE INCISO, que es justo lo que la razon teme perder: las CUATRO REGLAS DEL ARTICULO 401 se adosan al paso 2 del superviviente, que manda determinar la regla de origen sin decir cuantas hay; LOS DOS PORCENTAJES se adosan a su paso 3, que manda calcular el valor de contenido regional sin dar el umbral; y LOS NOMBRES DE LOS FORMULARIOS se adosan a su paso 4, que sin ellos no dice que papel llenar. Un cuarto inciso salva el DISPONIBLE PARA EL IMPORTADOR, que es el destinatario que el paso 5 del superviviente no nombra. Su paso 4 queda cubierto por el paso 1 del superviviente. Su unica condicion queda cubierta por la condicion 1 del superviviente, que dice que el mercado destino forma parte de un tratado de libre comercio. CERO perdidas nombradas.",
        },
        {
            "orden": 19,
            "superviviente": "uso_intermediarios_exportacion",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 4 contra 5 y condiciones 1 contra 2, las dos a favor de uso_intermediarios_exportacion. EL CABLEADO APUNTA AL OTRO (3 contra 2) y por P.8 no le toca hablar, porque el contenido no calla. LA PIEZA DECLARADA APUNTA AL MISMO LADO QUE EL CONTENIDO Y POR CANTIDAD: la razon del puesto 1957 nombra UNA sola pieza propia del que muere (evaluar si la empresa tiene recursos internos para exportar directamente) contra TRES del superviviente (las referencias comerciales y bancarias, si tomara titulo de la mercancia o actuara solo como comisionista, y la exclusividad y duracion del acuerdo).",
            "pasos": {
                "1": ["APPEND"],
                "2": ["INCISO", 1, "especializado en la industria o region objetivo", ", y "],
                "3": ["INCISO", 5, "comision, salario o retencion", ", y el modelo de compensacion entre "],
                "4": ["INCISO", 3, "el alcance de responsabilidades delegadas", ", y "],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: evaluar si la empresa tiene recursos internos para exportar directamente, que es la unica linea del par que se pregunta SI HACE FALTA un intermediario antes de buscarlo. TRES INCISOS, y los tres son parametros concretos de gestos que el superviviente ya tiene: el ESPECIALIZADO EN LA INDUSTRIA O REGION, adosado a su paso 1 (identificar el tipo mas adecuado segun producto y mercado); el MODELO DE COMPENSACION entre comision, salario o retencion, adosado a su paso 5 (formalizar el acuerdo especificando comision, exclusividad y duracion); y el ALCANCE DE RESPONSABILIDADES DELEGADAS, adosado a su paso 3 (negociar el nivel de control que la empresa retendra). Su unica condicion queda cubierta por la condicion 1 del superviviente, que habla de una empresa nueva en exportacion sin personal ni fondos que comprometer. CERO perdidas nombradas.",
        },
        {
            "orden": 20,
            "superviviente": "seleccion_canales_distribucion",
            "motivo": "LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO (acta 54, pregunta 1, registrada en 03_FUSIONES.md), Y AQUI EL CONTENIDO NO TIENE ENTRE QUIEN ELEGIR. seleccion_canales_distribucion ES PUERTA (extremo de puente aprobado) y la guarda 1B exige que sobreviva: es el UNICO candidato limpio del acto. EL CHOQUE SE REGISTRA CON SUS CIFRAS Y ES DE CONTENIDO: pasos 4 contra 4, empatados, y condiciones 1 contra 2 A FAVOR DEL OTRO, que es la unica vara de contenido no empatada del acto. MISMA FIGURA QUE EL ACTO 35 DEL TRAMO 3 Y QUE LOS ACTOS 1 Y 15 DEL TRAMO 2, y se dice cual es porque hay dos especies: esta es DE CONTENIDO. SE DICE ADEMAS QUE EL CABLEADO APUNTABA A LA PUERTA (4 contra 1), o sea al mismo lado que la guarda, aunque por P.8 no le tocara hablar. LO QUE PROTEGE EL CONTENIDO QUE EL CONTEO PREFIRIO ES EL REPARTO, y se mide abajo: las DOS piezas que la razon del puesto 1961 declara propias del que muere viajan ENTERAS.",
            "pasos": {
                "1": ["INCISO", 2, "e-commerce propio o de terceros, franquicia", ", y tambien "],
                "2": ["INCISO", 4, "velocidad de entrada", ", y la "],
                "3": ["APPEND"],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "DOS PIEZAS VIAJAN ENTERAS y son exactamente las dos que la razon declara propias del que muere: SELECCIONAR UNO O MAS CANALES COMPLEMENTARIOS en lugar de depender de uno solo, que es la unica regla de diversificacion del par; y DEFINIR UN PLAN DE EXPANSION GRADUAL a multiples mercados, que saca la decision de un canal y la convierte en una secuencia de entrada. DOS INCISOS: los canales que el superviviente no enumera (e-commerce propio o de terceros, franquicia), adosados a su paso 2; y la VELOCIDAD DE ENTRADA como criterio de evaluacion, adosada a su paso 4, que solo pesa control y recursos. SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto: exportar hoy a un solo mercado y buscar diversificar no lo dice la unica condicion del superviviente. CERO perdidas nombradas, que es lo que hace defendible que sobreviva el que el conteo de condiciones no prefirio.",
        },
        {
            "orden": 21,
            "superviviente": "ecosistema_global_emprendimiento_gee",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 6 contra 4 a favor de ecosistema_global_emprendimiento_gee; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice porque apuntaba al OTRO (3 contra 4). LA PIEZA DECLARADA APUNTA AL MISMO LADO QUE LOS PASOS Y POR CANTIDAD: la razon del puesto 1963 nombra UNA sola pieza propia del que muere (el asesor voluntario con experiencia) contra CUATRO del superviviente, entre ellas ARMAR UN DIRECTORIO DE CONTACTOS CON NOMBRES, ROLES Y DATOS, que la razon llama lo unico que convierte una lista de instituciones en una agenda utilizable.",
            "pasos": {
                "1": ["CUBIERTO", 3],
                "2": ["CUBIERTO", 3],
                "3": ["CUBIERTO", 3],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: consultar a un ASESOR VOLUNTARIO CON EXPERIENCIA para evaluar el potencial exportador, que es el unico recurso gratuito del par que da una opinion sobre el negocio en vez de tramites. LOS OTROS TRES PASOS CAEN LOS TRES EN EL PASO 3 DEL SUPERVIVIENTE, y se dice en vez de repartirlos por comodidad: ese paso manda localizar el centro de desarrollo de pequenos negocios de la zona Y verificar si tiene un asesor especializado en exportacion, que es la oficina, el especialista y el centro en una sola linea. Su condicion 1 queda cubierta por la condicion 1 del superviviente (no saber donde buscar ayuda para empezar a exportar). SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto: necesitar financiamiento comercial de bajo costo no lo dice ninguna de las dos del superviviente. CERO perdidas nombradas.",
        },
        {
            "orden": 22,
            "superviviente": "letra_de_cambio_bill_of_exchange",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 4 contra 6 y condiciones 2 contra 3, las dos a favor de letra_de_cambio_bill_of_exchange, y el cableado apunta al mismo lado (2 contra 3) aunque por P.8 no le toque hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO Y POR CANTIDAD: la razon del puesto 1969 nombra UNA sola pieza propia del que muere (el aviso del riesgo de no pago en envios aereos con pago contra documentos) contra TRES del superviviente, entre ellas DECIDIR QUIEN PAGA LOS COSTOS DEL BANCO Y SI SE PIDE PROTESTO FORMAL, que la razon llama la unica linea del par que prepara la via legal antes de que haga falta.",
            "pasos": {
                "1": ["CUBIERTO", 4],
                "2": ["CUBIERTO", 6],
                "3": ["CUBIERTO", 3],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere y llama un aviso operativo importante: EVALUAR EL RIESGO DE NO PAGO, ESPECIALMENTE EN ENVIOS AEREOS CON PAGO CONTRA DOCUMENTOS, porque la mercancia llega antes que los papeles. Y SE DICE UNA COSA MEDIDA EN VEZ DE CALLARLA: su paso 2 nombra el DOCUMENTO DE TITULO (bill of lading) y el paso 6 del superviviente solo dice enviar la letra y los documentos, pero ese documento NO se pierde del nodo, porque el paso 3 del superviviente enumera literalmente factura, CONOCIMIENTO DE EMBARQUE, lista de empaque y certificados, que es el mismo papel con su nombre en castellano. Se marca CUBIERTO y NO se cuenta perdida, con la comprobacion escrita. SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos: tener CIERTA CONFIANZA en el comprador pero querer mantener el control sobre el titulo, y buscar un metodo MAS ECONOMICO que la carta de credito; ninguna de las tres del superviviente dice ninguna de las dos. CERO perdidas nombradas.",
        },
        {
            "orden": 23,
            "superviviente": "seleccion_de_metodo_de_pago",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y APUNTA A LA PUERTA, ASI QUE NO HAY CHOQUE QUE REGISTRAR. Pasos 4 contra 5 a favor de seleccion_de_metodo_de_pago; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que apuntaba al mismo lado y por mucho (3 contra 9). Y ESE MISMO NODO ES PUERTA (extremo de puente aprobado): la guarda 1B y el contenido piden lo mismo, y por eso este acto NO es de la especie del 20, donde si hay choque. La razon del puesto 1981 nombra UNA pieza propia del que muere contra TRES del superviviente, asi que la vara del propio declarado apunta tambien al mismo lado.",
            "pasos": {
                "1": ["INCISO", 1, "verificaciones de credito exhaustivas antes de cada transaccion", ", con "],
                "2": ["APPEND"],
                "3": ["INCISO", 5, "ante circunstancias inusuales", ", tambien "],
                "4": ["INCISO", 1, "International Company Profile (ICP) del U.S. Commercial Service", ", como el "],
            },
            "condiciones": {"1": ["CUBIERTO", 2], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: MONITOREAR CONTINUAMENTE LOS PATRONES DE PAGO DE LOS CLIENTES EXISTENTES, que es la unica linea del par que vigila DESPUES de la primera venta, cuando el riesgo ya no es el desconocido sino el conocido que empieza a atrasarse. TRES INCISOS: las VERIFICACIONES DE CREDITO ANTES DE CADA TRANSACCION y el nombre propio de la herramienta, el INTERNATIONAL COMPANY PROFILE, los dos adosados al paso 1 del superviviente, que manda evaluar la solvencia con un perfil de credito comercial sin nombrar ni el momento ni el instrumento; y el ANTE CIRCUNSTANCIAS INUSUALES, adosado a su paso 5, que es la consulta al banco. SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto (reducir el riesgo de cuentas incobrables). UNA PERDIDA NOMBRADA: su condicion 1 dispara con compradores nuevos O RECURRENTES, y la condicion 2 del superviviente solo habla del comprador DESCONOCIDO O CON POCO HISTORIAL; el recurrente que ya tiene historial se queda fuera. El INCISO para condiciones no existe en el instrumento (pendiente de doctrina heredado) y por eso la perdida se nombra en vez de repararse.",
        },
        {
            "orden": 26,
            "superviviente": "uso_del_us_commercial_service",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 3 contra 6 y condiciones 1 contra 4, las dos a favor de uso_del_us_commercial_service, y el cableado apunta al mismo lado (1 contra 6) aunque por P.8 no le toque hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO Y ES LA VARA MAS FUERTE: la razon del puesto 2043 escribe que el corto cabe ENTERO dentro del largo por SUBCONJUNTO ESTRICTO, y que lo unico que anade son DOS NOMBRES PROPIOS, el del consejo y el de uno de sus seminarios.",
            "pasos": {
                "1": ["INCISO", 1, "afiliada a un DEC", ", incluida la "],
                "2": ["INCISO", 4, "talleres o seminarios organizados por el DEC, como Export University", ", y en "],
                "3": ["CUBIERTO", 3],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA Y LOS DOS NOMBRES PROPIOS QUE LA RAZON NOMBRA COMO LO UNICO PROPIO SE SALVAN LOS DOS DE INCISO: la oficina AFILIADA A UN DEC, adosada al paso 1 del superviviente, que contacta la oficina local sin decir cual; y los TALLERES DEL DEC, COMO EXPORT UNIVERSITY, adosados a su paso 4, que enumera seminarios, ferias y misiones sin nombrar este. Su paso 3 queda cubierto por el paso 3 del superviviente, que solicita apoyo para identificar mercados y encontrar compradores. Y SE DICE UNA COSA MEDIDA EN VEZ DE CALLARLA: su unica condicion dice MENTORIA PRACTICA y la condicion 1 del superviviente dice ORIENTACION EXPERTA gratuita o de bajo costo; el matiz de acompanamiento NO se pierde del nodo, porque el entregable del superviviente es literalmente un plan de acompanamiento junto a un especialista comercial. Se marca CUBIERTO y NO se cuenta perdida, con la comprobacion escrita. CERO perdidas nombradas.",
        },
        {
            "orden": 27,
            "superviviente": "preparar_fdd",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO, Y LA RAZON MIDE EL SUPERVIVIENTE CON ESAS PALABRAS. Pasos 4 contra 5 y condiciones 1 contra 2, las dos a favor de preparar_fdd, y el cableado apunta al mismo lado (6 contra 7) aunque por P.8 no le toque hablar. LA RAZON DEL PUESTO 2078 ESCRIBE SUPERVIVIENTE MEDIDO: preparar_fdd, y lo sostiene con la vara del banco 9.6.1 pesada pieza a pieza: lo propio de elaboracion_fdd son DOS LINEAS (un criterio de completitud y una accion unica) y lo propio de preparar_fdd es UNA LINEA MAS UN PROCEDIMIENTO que el otro no tiene en ninguna forma, preparar o crear una entidad corporativa nueva con estados financieros auditados. ES ADEMAS UN VEREDICTO REESCRITO DE D A A el 12 ago 2026, con la razon vieja conservada entera dentro de la nueva.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["APPEND"],
                "3": ["INCISO", 5, "cualquier firma o cobro", ", y antes de "],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["APPEND"]},
            "nota": "DOS PIEZAS VIAJAN ENTERAS y son EXACTAMENTE las dos que la razon nombra como PERDIDAS QUE VIAJAN, con el aviso de que la segunda importa mas de lo que parece: ASEGURAR QUE TODAS LAS CUOTAS Y FUENTES DE INGRESO ESTEN COMPLETAMENTE DIVULGADAS, que es la falta clasica de este documento; y DOCUMENTAR LA ENTREGA MEDIANTE LA PAGINA DE RECIBO (ITEM 23), que la razon llama lo unico del par que sirve para probar el cumplimiento despues, cuando ya nadie recuerda la fecha, y advierte que si la fusion se la lleva por delante el catalogo pierde la prueba y se queda con la obligacion. VAN DE APPEND, que no pierde nada, y por eso ese riesgo NO se materializa. UN INCISO: el ANTES DE CUALQUIER FIRMA O COBRO, adosado al paso 5 del superviviente, que solo dice antes de la venta. SU UNICA CONDICION VIAJA ENTERA por ser un disparador distinto: tener YA un abogado de franquicias y necesitar el documento legal no lo dice ninguna de las dos del superviviente. CERO perdidas nombradas.",
        },
        {
            "orden": 28,
            "superviviente": "franquicia_mas_crecimiento_corporativo_hibrido",
            "motivo": "LOS CONTEOS EMPATAN Y LA PIEZA DECLARADA DECIDE, CON EL CABLEADO DE ACUERDO. Pasos 4 contra 4 y condiciones 2 contra 2: las dos varas contables de contenido empatan al digito. PERO EL CONTENIDO NO CALLA, porque EL MATERIAL PROPIO DECLARADO ES UNA VARA DE CONTENIDO (acta 54, pregunta 4) y aqui esta A UN SOLO LADO: la razon del puesto 2079 escribe que estrategia_multicanal_expansion cabe ENTERO dentro del otro por SUBCONJUNTO ESTRICTO, que su paso 4 NO ES UN PASO NUEVO sino el resumen de los pasos 1 y 2, y que el largo trae ademas un paso propio, el plan de personal que sostiene la doble estrategia sin sacrificar velocidad. El cableado apunta al mismo lado (2 contra 3) y por eso NO decide nada aqui: se dice para que quede medido.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
                "3": ["INCISO", 3, "cuando el programa de franquicias genera suficiente caja", ", y "],
                "4": ["CUBIERTO", 2],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "NINGUNA PIEZA DE PASO VIAJA ENTERA Y NINGUNA SE PIERDE, que es lo que un subconjunto estricto tiene que dar. UN INCISO, y es la unica cosa que el corto dice y el largo no: el CUANDO de la reapertura del canal corporativo, adosado al paso 3 del superviviente, que pregunta EN QUE MERCADOS O SITUACIONES. La razon mide que las dos son la misma decision vista por dos caras, y el inciso conserva la cara que faltaba. Su paso 4 se marca CUBIERTO por el paso 2 del superviviente Y SE DICE POR QUE, porque es la unica marca del acto que no es obvia: la razon escribe que separar temporalmente los dos crecimientos NO ES UN PASO NUEVO sino el resumen de los pasos 1 y 2, o sea la secuencia misma. SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos: operar ya algunas unidades propias y planear escalar con los dos canales, y no tener claro en que ORDEN priorizar; las dos del superviviente hablan de maximizar la valoracion y de reinvertir cuando ya hay caja excedente. CERO perdidas nombradas.",
        },
        {
            "orden": 29,
            "superviviente": "proceso_llamada_inicial_venta",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y APUNTA A LA PUERTA, ASI QUE NO HAY CHOQUE QUE REGISTRAR. Pasos 8 contra 7 a favor de proceso_llamada_inicial_venta; condiciones 1 contra 1, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que apuntaba al mismo lado y por mucho (8 contra 2). Y ESE MISMO NODO ES PUERTA: la guarda 1B y el contenido piden lo mismo. LA RAZON DEL PUESTO 2080 DEJA ANOTADA UNA NOTA DE DOCTRINA PARA EL AUDITOR y se traslada aqui sin tocarla: es el PRIMER par donde la vara del banco 9.22 vuelve LINEA POR LOS DOS LADOS, que es el caso espejo del uso habitual y da A. La razon no la presenta como regla nueva sino como el 9.6.1 y el 9.22 aplicados juntos.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 2, "en los primeros 5 minutos", ", y hazlo "],
                "3": ["CUBIERTO", 4],
                "4": ["CUBIERTO", 6],
                "5": ["CUBIERTO", 7],
                "6": ["INCISO", 8, "agenda la siguiente llamada", ", y "],
                "7": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: SI NO CALIFICA, RECHAZALO CON AMABILIDAD Y SUGIERELE COMO RESOLVER SU SITUACION, que es la unica salida del guion para el candidato que no entra. DOS INCISOS, y son los DOS DETALLES DE RELOJ que la razon nombra: calificar EN LOS PRIMEROS CINCO MINUTOS, adosado al paso 2 del superviviente; y AGENDAR LA SIGUIENTE LLAMADA, adosado a su paso 8, que pide el avance sin fijar la proxima cita. Los otros cuatro pasos son el mismo guion en el mismo orden, y se marcan uno a uno contra el paso del superviviente que los dice. Su unica condicion queda cubierta por la condicion 1 del superviviente. CERO perdidas nombradas.",
        },
        {
            "orden": 30,
            "superviviente": "sitio_web_franquicia",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 3 contra 5 a favor de sitio_web_franquicia; condiciones 1 contra 1, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que ADEMAS EMPATA (3 contra 3), con lo que no habria decidido nada. LA PIEZA DECLARADA APUNTA AL MISMO LADO QUE LOS PASOS Y POR CANTIDAD: la razon del puesto 2087 nombra UNA sola pieza propia del que muere (la oferta de valor que se entrega a cambio del contacto) contra TRES del superviviente (separar la seccion de franquicia de la del consumidor, optimizar el sitio para los dos publicos, y los llamados a la accion). Y LA RAZON DEJA UNA COMPROBACION QUE SE COPIA AQUI PORQUE ES LA QUE SOSTIENE LA CLASE: se leyeron los pasos y no el titulo, porque el titulo del corto promete una tesis (el sitio captura y no vende) que solo esta escrita en su paso 3, y ese paso ya esta en el largo.",
            "pasos": {
                "1": ["INCISO", 2, "formularios, descargas, videos", ", del tipo "],
                "2": ["APPEND"],
                "3": ["INCISO", 3, "informacion financiera o de soporte", ", en especial la "],
            },
            "condiciones": {"1": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon llama LO UNICO QUE QUEDA FUERA: definir la OFERTA DE VALOR que se entrega a cambio del contacto, un reporte o un video. DOS INCISOS: los TIPOS de mecanismo de captura (formularios, descargas, videos), adosados al paso 2 del superviviente, que fija el emplazamiento pero no los tipos; y la INFORMACION FINANCIERA O DE SOPORTE como la que no hay que publicar, adosada a su paso 3, que habla de informacion excesiva sin decir cual. SU UNICA CONDICION VIAJA ENTERA por ser un disparador distinto: REDISENAR un sitio ya existente no es lo mismo que INICIAR la comercializacion activa, que es lo que dice la condicion del superviviente. CERO perdidas nombradas.",
        },
        {
            "orden": 32,
            "superviviente": "referidos_franquiciados_existentes",
            "motivo": "LOS TRES CONTEOS EMPATAN Y DECIDE LA PIEZA DECLARADA POR CANTIDAD. Pasos 5 contra 5, condiciones 2 contra 2 y cableado 3 contra 3: los tres al digito. NO ES EMPATE SIN VARA, Y ESA ES LA UNICA COSA DELICADA DE ESTE ACTO, ASI QUE VA MARCADA COMO DISCUTIBLE EN EL REPORTE. El motivo es que EL MATERIAL PROPIO DECLARADO ES UNA VARA DE CONTENIDO (acta 54, pregunta 4) y aqui NO empata: la razon del puesto 2127 mide que lo propio de programa_de_referidos_de_franquiciados es UNA LINEA (informar tambien a empleados, proveedores y socios) y que lo propio de referidos_franquiciados_existentes son DOS LINEAS (educar al franquiciado sobre los beneficios del crecimiento del sistema, y EVALUAR CON EL ABOGADO EL RIESGO DE CONFLICTO DE INTERES al pagar comisiones por referidos, que la razon llama lo unico del par que protege de una practica que parece obviamente buena). Una contra dos: la vara del propio declarado separa, y por eso el cableado no llega a hablar.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["INCISO", 3, "destacando su rol como embajadores de marca", ", "],
                "3": ["CUBIERTO", 1],
                "4": ["INCISO", 4, "desde el inicio de la relacion", ", y "],
                "5": ["CUBIERTO", 5],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: INFORMAR TAMBIEN A EMPLEADOS, PROVEEDORES Y SOCIOS del perfil buscado, que amplia el universo mas alla de los franquiciados. DOS INCISOS: el ROL DE EMBAJADORES DE MARCA con el que se pide el referido, adosado al paso 3 del superviviente; y el DESDE EL INICIO DE LA RELACION como momento en que el equipo de campo empieza a hablar de expansion, adosado a su paso 4, que dice REGULARMENTE sin fijar el arranque. Su paso 5 queda cubierto por el paso 5 del superviviente, que es el mismo asunto de los incentivos por referir y ademas lo mira con el abogado. SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto: reducir el COSTO POR LEAD aprovechando canales de alta credibilidad no lo dice ninguna de las dos del superviviente. CERO perdidas nombradas.",
        },
        {
            "orden": 33,
            "superviviente": "motivated_management_franquiciado",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 3 contra 4 a favor de motivated_management_franquiciado; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que ADEMAS EMPATA (2 contra 2). LA PIEZA DECLARADA APUNTA AL MISMO LADO Y LA RAZON DEL PUESTO 2145 LO DICE CON TODAS SUS LETRAS: uno de los dos NO TRAE PROCEDIMIENTO PROPIO. Lo unico propio de mito_control_calidad_corporativo es una ADVERTENCIA, que por la vara del banco 9.6.1 es LINEA; y motivated_management_franquiciado SI trae procedimiento que el otro no tiene, entre otros DISENAR UN ESQUEMA DE INCENTIVOS QUE REPLIQUE LA MOTIVACION DE PROPIEDAD.",
            "pasos": {
                "1": ["INCISO", 2, "ingresos, gestion de gastos", ", incluidos "],
                "2": ["APPEND"],
                "3": ["CUBIERTO", 3],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA Y ES EXACTAMENTE LA QUE LA RAZON NOMBRA COMO PERDIDA, ASI QUE LA PERDIDA NO OCURRE: la advertencia de que la falta de control operativo directo NO IMPLICA MENOR CALIDAD, SINO QUE EXIGE MECANISMOS ALTERNATIVOS DE CONTROL. La razon la llama una linea para la clase y una perdida para la fusion, y avisa de que es lo unico del par que impide leer el argumento como que el control sobra. VA DE APPEND, que no pierde nada, y por eso este acto NO cuenta perdida pese a que la razon la anticipaba. UN INCISO: las metricas que el superviviente no enumera (ingresos, gestion de gastos), adosadas a su paso 2, que compara ventas, limpieza y rotacion. SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos: la DUDA DEL FUNDADOR sobre si franquiciar reducira la calidad, y PRESENTAR EL CASO DE NEGOCIO a inversionistas o socios; las dos del superviviente hablan de gerentes dificiles de retener y de mejorar el desempeno de unidades existentes. CERO perdidas nombradas.",
        },
        {
            "orden": 34,
            "superviviente": "desarrollar_manual_operaciones",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 3 contra 6 y condiciones 1 contra 3, las dos a favor de desarrollar_manual_operaciones, y el cableado apunta al mismo lado y por mucho (2 contra 10) aunque por P.8 no le toque hablar. LA RAZON DEL PUESTO 2196 MIDE EL SUPERVIVIENTE CON ESAS PALABRAS: sobrevive desarrollar_manual_operaciones, que tiene seis pasos y toda la doctrina legal del documento, y la regla de need to know se absorbe como linea suya. Lo que el que muere anade son TRES FORMAS DE LA MISMA POLITICA (una accion unica, una obligacion y un criterio suelto), que por la precision del banco 9.6.1 son LINEA y no procedimiento.",
            "pasos": {
                "1": ["CUBIERTO", 5],
                "2": ["INCISO", 5, "mantener el manual bajo resguardo controlado", ", exigiendo a los franquiciados "],
                "3": ["INCISO", 5, "solo segun necesidad de entrenamiento", ", y limitando su divulgacion a los empleados "],
            },
            "condiciones": {"1": ["APPEND"]},
            "nota": "NINGUNA PIEZA DE PASO VIAJA ENTERA Y NINGUNA SE PIERDE: las TRES formas de la politica de confidencialidad se recogen en el paso 5 del superviviente, que es el que ya vincula el manual al contrato MANTENIENDOLO FUERA DEL CONTRATO MISMO Y CONFIDENCIAL. La primera queda CUBIERTA por ese mismo paso, que es donde vive la declaracion de confidencialidad; las otras dos van de INCISO adosadas al mismo paso, porque son los dos gestos concretos que ese paso no dice: EL RESGUARDO CONTROLADO exigido al franquiciado, y el LIMITE DE DIVULGACION A LOS EMPLEADOS SEGUN NECESIDAD DE ENTRENAMIENTO, que es la regla de need to know que la razon manda absorber como linea. SU UNICA CONDICION VIAJA ENTERA por ser un disparador distinto: el momento de DISTRIBUIR el manual a los franquiciados y tener que proteger la propiedad intelectual no lo dice ninguna de las tres del superviviente, que hablan de tener sistemas listos para documentar, de antes de vender franquicias y del riesgo de responsabilidad. CERO perdidas nombradas.",
        },
    ],
    "declarados": [
        {
            "orden": 24,
            "miembros": ["barreras_comerciales_no_arancelarias", "cumplimiento_acuerdos_comerciales_tanc"],
            "especie": "EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN",
            "motivo": "LAS DOS VARAS DE CONTENIDO EMPATAN AL DIGITO (pasos 4 contra 4 y condiciones 2 contra 2) Y EL CABLEADO TAMBIEN EMPATA (2 contra 2). El empate sin vara exige exactamente eso (acta 53, pregunta 4), y aqui se cumple. Y LA PIEZA DECLARADA NO DESEMPATA porque hay material propio declarado a LOS DOS lados Y EN LA MISMA CANTIDAD, UNA LINEA CADA UNO: la razon del puesto 1984 escribe que de barreras_comerciales_no_arancelarias se perderia AJUSTAR EL PRODUCTO O EL PROCESO segun lo que descubra la revision regulatoria, y que de cumplimiento_acuerdos_comerciales_tanc se perderia DAR SEGUIMIENTO HASTA QUE EL CASO SE RESUELVA. Sin vara que separe, el acto SE DECLARA y acumula.",
            "acumula_para": "LA MESA. Y con el dato que la propia razon subraya y que hace este empate distinto de los demas: LAS DOS PIEZAS PROPIAS SON LAS DOS RESPUESTAS OPUESTAS AL MISMO PROBLEMA. Un nodo termina CEDIENDO ante la barrera (ajustar el producto) y el otro INSISTIENDO (dar seguimiento hasta que se resuelva), y la razon escribe que la fusion tiene que conservar las dos porque son las dos salidas legitimas. Un empate cuyas dos mitades son opuestas no se rompe eligiendo la mas larga, y por eso este ejemplar merece llegar a la mesa con esa frase delante."
        },
        {
            "orden": 25,
            "miembros": ["licenciamiento_tecnologico", "proteccion_propiedad_intelectual_internacional"],
            "especie": "LOS DOS MIEMBROS SON PUERTA: NO HAY ABSORBIDO POSIBLE",
            "motivo": "ESPECIE NUEVA EN LA CAMPANA Y POR ESO VA CON SU NOMBRE PROPIO. La guarda 1B, escrita desde la vuelta 48 y nacida de un Gate 0 en rojo, dice que UN NODO QUE ES SEMILLA O EXTREMO DE PUENTE NO SE ABSORBE y que su acto SE DECLARA. Hasta hoy esa guarda habia mordido con UNA puerta en el acto, y la vara del acta 54 pregunta 1 resolvia el caso: la guarda restringe y el contenido elige entre lo permitido, o sea sobrevive la puerta. AQUI LOS DOS MIEMBROS SON PUERTA, medido por el propio abridor y otra vez por el generador de planes, asi que NO QUEDA NINGUN CANDIDATO A ABSORBIDO: cualquiera de las dos elecciones deprecaria una puerta. No es que el contenido no separe (separa, y por mucho: pasos 6 contra 4 y condiciones 3 contra 2 a favor de licenciamiento_tecnologico, con la razon del puesto 2022 declarando SUBCONJUNTO ESTRICTO por el banco 9.6.1). Es que la guarda no deja fundir en ninguna direccion.",
            "acumula_para": "LA MESA, Y CON UNA PREGUNTA QUE NO ES DE PAR SINO DE CATALOGO: que se hace con un acto CERRADO cuyos DOS miembros son puertas. La vara del acta 54 pregunta 1 esta escrita para el acto con UNA puerta y no dice nada de este caso. Hay al menos dos salidas imaginables y ninguna esta escrita, asi que NO se elige aqui: fundir moviendo antes el puente o la semilla al superviviente, o dejar el par como enlace permanente. Va marcado como PENDIENTE DE DOCTRINA en el reporte, con el aviso de que el tramo 4 lo destapa pero no lo inventa: la figura estaba esperando desde que existen las puertas."
        },
        {
            "orden": 31,
            "miembros": ["comprender_definicion_legal_franquicia", "marco_name_system_fee"],
            "especie": "CONTEOS QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA",
            "motivo": "LAS DOS VARAS DE CONTENIDO APUNTAN A LADOS DISTINTOS: pasos 4 contra 5 a favor de marco_name_system_fee y condiciones 3 contra 2 a favor de comprender_definicion_legal_franquicia. El cableado NO PUEDE HABLAR y se dice por que: por P.8 solo decide cuando el contenido CALLA ENTERO, y aqui el contenido no calla, CHOCA (acta 54, pregunta 4). Y LA PIEZA DECLARADA NO DESEMPATA porque la razon del puesto 2105 mide UNA LINEA DE CADA LADO y lo escribe asi: comprender_definicion_legal_franquicia anade EL UMBRAL CONCRETO de quinientos dolares en los primeros seis meses, que es un criterio suelto; marco_name_system_fee anade separar el soporte del control como pregunta aparte, que es un matiz de la misma casilla. Una y una: la vara del propio declarado EMPATA. Sin vara que separe, el acto SE DECLARA y acumula.",
            "acumula_para": "LA MESA. Con un dato que la razon aporta y que a la mesa le sirve para no leer este empate como los otros: la unica diferencia real entre los dos nodos ES EL MODO, uno pregunta si YA se es franquicia y el otro si se QUIERE serlo, y la razon deja escrito que la clase se decide leyendo los pasos y no el modo. Es el TERCER ejemplar de conteos que chocan de este tramo, y el primero en el que lo que chocan son cuatro contra cinco pasos y tres contra dos condiciones sobre un test de tres elementos identico."
        },
    ],
}


LOTES["C"] = {
    "titulo": "4, LOTE C DE LA VUELTA 57: LOS ACTOS 35 A 50 EN EL ORDEN IMPRESO DEL TRAMO, LOS DIECISEIS SIN APARTAR NINGUNO. Es el primer lote de la campana en el que la vara de LO DECLARADO gana a un conteo CUATRO veces (actos 41, 45, 47 y 50), y las cuatro van marcadas como discutibles en el reporte",
    "actos": [
        {
            "orden": 35,
            "superviviente": "ferias_comerciales_franquicia",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y LA RAZON DECLARA EL MISMO SUPERVIVIENTE. Pasos 6 contra 5 a favor de ferias_comerciales_franquicia; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que ADEMAS EMPATA (3 contra 3). La razon del puesto 2202 escribe SOBREVIVE ferias_comerciales_franquicia y lo sostiene con la vara del banco 9.6.1: lo propio del que muere son DOS TACTICAS SUELTAS que caben en una linea, y el que sobrevive si trae procedimiento propio, entre otras cosas pedir las estadisticas de asistentes de ediciones pasadas y contactar a quienes expusieron antes.",
            "pasos": {
                "1": ["INCISO", 1, "la region donde quieres crecer", ", y con "],
                "2": ["INCISO", 4, "tarifas de hotel y reserva vuelos con anticipacion", ", y para reducirlos negocia "],
                "3": ["INCISO", 5, "un mini folleto economico para repartir a todos y un folleto completo para los prospectos que realmente te interesan", ", con "],
                "4": ["CUBIERTO", 5],
                "5": ["INCISO", 6, "inmediato", ", y que sea "],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "NINGUNA PIEZA DE PASO VIAJA ENTERA Y LAS DOS TACTICAS QUE LA RAZON DECLARA PROPIAS DEL QUE MUERE SE SALVAN LAS DOS DE INCISO, que es lo que la razon manda al decir que se absorben como lineas suyas: negociar hotel y vuelos con anticipacion se adosa al paso 4 del superviviente, que es el del costeo; y los DOS FOLLETOS, el barato para todos y el completo para los que interesan, se adosan a su paso 5, que es el del estand. Otros dos incisos afinan alcance y ritmo: la REGION donde se quiere crecer como criterio de eleccion de feria, y el INMEDIATO del seguimiento. SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos: TENER PRESUPUESTO suficiente para presencia fisica, y QUERER COMPETIR mostrando la marca frente a otros franquiciadores; las dos del superviviente hablan de buscar contacto cara a cara y de tener un perfil de inversor muy especifico. CERO perdidas nombradas.",
        },
        {
            "orden": 36,
            "superviviente": "mix_ubicaciones_corporativas_franquicia",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO, Y LA RAZON DECLARA EL MISMO SUPERVIVIENTE. Pasos 4 contra 6 y condiciones 2 contra 3, las dos a favor de mix_ubicaciones_corporativas_franquicia. EL CABLEADO APUNTA AL OTRO (6 contra 4) y por P.8 no le toca hablar, porque el contenido no calla. La razon del puesto 2204 escribe SOBREVIVE mix_ubicaciones_corporativas_franquicia: lo que le queda propio al otro son DOS AVISOS, y una advertencia es LINEA por la precision del banco 9.6.1, mientras que el superviviente trae EL MENU NOMBRADO DE CUATRO ESTRATEGIAS DE UBICACION con sus criterios de validacion y riesgo.",
            "pasos": {
                "1": ["INCISO", 1, "una iniciativa separada que no compita con el desarrollo corporativo", ", lanzando el canal de franquicia como "],
                "2": ["INCISO", 4, "para evitar encroachment", ", y "],
                "3": ["INCISO", 6, "en mercados distantes", ", y en especial las de "],
                "4": ["INCISO", 2, "recursos dedicados suficientes para crecer sin canibalizarse", ", asegurando a los dos canales "],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "NINGUNA PIEZA DE PASO VIAJA ENTERA Y LAS CUATRO SE SALVAN DE INCISO, que es lo que la razon manda al decir que las dos advertencias se absorben como lineas suyas: la de LANZAR EL CANAL COMO INICIATIVA SEPARADA se adosa al paso 1 del superviviente, que es donde se decide si se siguen abriendo locales propios en paralelo; y la de los RECURSOS DEDICADOS PARA NO CANIBALIZARSE se adosa a su paso 2, que es donde se mira el capital disponible. Las otras dos son las que la razon mide como ya presentes: el ENCROACHMENT como nombre del conflicto de territorio, adosado a su paso 4; y los MERCADOS DISTANTES como el caso en que la tienda corporativa sirve de centro de entrenamiento, adosado a su paso 6, que ya nombra ese uso sin decir donde. SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto: MAXIMIZAR EL VALOR de la empresa combinando los dos canales no lo dice ninguna de las tres del superviviente. CERO perdidas nombradas.",
        },
        {
            "orden": 37,
            "superviviente": "rutas_salida_planificacion_emergencias",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y LA RAZON DECLARA EL MISMO SUPERVIVIENTE. Pasos 5 contra 6 a favor de rutas_salida_planificacion_emergencias; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice porque apuntaba al OTRO (3 contra 1). La razon del puesto 2223 escribe SOBREVIVE rutas_salida_planificacion_emergencias: lo unico propio del que muere son DOS LINEAS (la bisagra lateral y el estandar del pais para el herraje), y ademas la bisagra lateral es el reverso de una linea que el superviviente SI tiene, la prohibicion de puertas giratorias, corredizas o elevadizas.",
            "pasos": {
                "1": ["INCISO", 2, "bisagra lateral", ", y con "],
                "2": ["CUBIERTO", 1],
                "3": ["INCISO", 4, "que abran con poca fuerza, segun el estandar de tu pais", ", "],
                "4": ["CUBIERTO", 5],
                "5": ["CUBIERTO", 6],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "NINGUNA PIEZA DE PASO VIAJA ENTERA Y LAS DOS LINEAS PROPIAS SE SALVAN LAS DOS DE INCISO: la BISAGRA LATERAL se adosa al paso 2 del superviviente, que es el que exige que la puerta abra sin llave; y el QUE ABRAN CON POCA FUERZA SEGUN EL ESTANDAR DEL PAIS se adosa a su paso 4, que instala el herraje de panico sin decir con que fuerza ni contra que norma. Los otros tres pasos quedan cubiertos uno a uno: las rutas libres y senalizadas por su paso 1, la liberacion interna de las camaras frias por su paso 5, y las barreras hacia el trafico vehicular por su paso 6. SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos: TENER UN LOCAL FISICO CON VARIAS PERSONAS TRABAJANDO, y NECESITAR CUMPLIR LA NORMATIVA del pais; las dos del superviviente hablan de disenar o revisar el plan de evacuacion y de detectar puertas bloqueadas. CERO perdidas nombradas.",
        },
        {
            "orden": 38,
            "superviviente": "responsabilidad_prospectiva",
            "motivo": "LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO (acta 54, pregunta 1), Y AQUI EL CONTENIDO NO TIENE ENTRE QUIEN ELEGIR. responsabilidad_prospectiva ES PUERTA (extremo de puente aprobado) y la guarda 1B exige que sobreviva: es el UNICO candidato limpio del acto. EL CHOQUE SE REGISTRA CON SUS CIFRAS Y ES DE PIEZA DECLARADA, que es una TERCERA especie de choque de puerta y por eso se dice aparte de las dos anteriores: los conteos de contenido EMPATAN AL DIGITO (pasos 4 contra 4 y condiciones 2 contra 2) y el cableado apunta a la puerta (3 contra 4), asi que ni los conteos ni el cableado contradicen a la guarda. QUIEN CONTRADICE ES LA RAZON: el puesto 2230 escribe SOBREVIVE rendicion_cuentas_prospectiva, porque ese nodo trae dos cosas que el otro no tiene, COMPARTIR EL RELATO DE LA PERSONA INVOLUCRADA como mecanismo y DAR APOYO A LA SEGUNDA VICTIMA. LAS DOS VIAJAN ENTERAS EN EL REPARTO, asi que la eleccion de la guarda no cuesta ninguna de las dos piezas por las que la razon la prefiere. VA MARCADO COMO DISCUTIBLE EN EL REPORTE.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
                "3": ["APPEND"],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "DOS PIEZAS VIAJAN ENTERAS Y SON EXACTAMENTE LAS DOS POR LAS QUE LA RAZON PREFERIA AL OTRO NODO, que es lo que hace defendible respetar la guarda sin perder nada: COMPARTIR EL RELATO DE LA PERSONA INVOLUCRADA para que todos aprendan en lugar de sancionarla, que convierte el anuncio del paso 4 del superviviente en un mecanismo; y DAR APOYO A QUIEN VIVIO EL INCIDENTE DE CERCA PORQUE TAMBIEN CARGA CON EL GOLPE, la segunda victima, que la razon mide que no aparece en ninguna linea del superviviente. Sus dos primeros pasos quedan cubiertos: cambiar quien fallo por que hay que cambiar es el paso 1 del superviviente, y decidir quien ejecuta las mejoras y quien revisa que funcionaron son sus pasos 2 y 3, y se marca contra el 2 porque es el que asigna. SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos: DESPUES DE UN INCIDENTE que se quiere aprovechar para aprender, y QUERER DEJAR EL CASTIGO y pasar a la mejora continua; las dos del superviviente hablan de decidir como se manejaran los errores y de que la gente cuente los problemas sin miedo. CERO perdidas nombradas.",
        },
        {
            "orden": 39,
            "superviviente": "capacitacion_educacion_seguridad",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO, Y LA RAZON DECLARA EL MISMO SUPERVIVIENTE. Pasos 4 contra 6 y condiciones 2 contra 3, las dos a favor de capacitacion_educacion_seguridad, y el cableado apunta al mismo lado (7 contra 9) aunque por P.8 no le toque hablar. La razon del puesto 2232 escribe SOBREVIVE capacitacion_educacion_seguridad y nombra las TRES cosas que solo el tiene: formar a quienes supervisan en liderazgo e investigacion de incidentes, capacitar en reconocimiento de peligros y jerarquia de controles, y considerar cursos de certificacion segun el rol. Y DEJA REGISTRADA UNA FIGURA NUEVA que se traslada aqui sin tocarla: LA MISMA NORMA EN DOS FOLLETOS, porque la repeticion no viene de dos autores que piensan parecido sino de dos publicaciones del MISMO organismo (OSHA3885 y OSHA3886) que cubren el mismo requisito con distinto detalle.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 3],
                "3": ["CUBIERTO", 5],
                "4": ["INCISO", 2, "a reportar sin temor a represalias", ", incluido el derecho "],
            },
            "condiciones": {"1": ["APPEND"], "2": ["CUBIERTO", 1]},
            "nota": "NINGUNA PIEZA DE PASO VIAJA ENTERA Y NINGUNA SE PIERDE: capacitar en politicas, metas y procedimientos es el paso 1 del superviviente; ensenar a reportar peligros, lesiones y casi accidentes es su paso 3; e impartirlo en el idioma y nivel adecuado es su paso 5. UN INCISO, y es el que la razon mide como el unico que estaba DENTRO de otro paso y no pareado: el DERECHO A REPORTAR SIN TEMOR A REPRESALIAS, adosado al paso 2 del superviviente, que habla de la proteccion de los derechos de los trabajadores sin nombrar este. SU CONDICION 1 VIAJA ENTERA por ser un disparador distinto: AL LANZAR UN NUEVO PROGRAMA de seguridad y salud no lo dice ninguna de las tres del superviviente, que hablan de incorporaciones, de brechas de conocimiento y de nuevos controles. Su condicion 2 queda cubierta por la condicion 1 del superviviente, que nombra a los nuevos trabajadores. CERO perdidas nombradas.",
        },
        {
            "orden": 40,
            "superviviente": "confusion_de_modos_automatizacion",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y LA RAZON DECLARA EL MISMO SUPERVIVIENTE. Pasos 4 contra 3 a favor de confusion_de_modos_automatizacion; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que apuntaba AL MISMO LADO (3 contra 2). La razon del puesto 2235 escribe SOBREVIVE confusion_de_modos_automatizacion: lo unico propio del otro son DOS MATICES que son LINEA, y el superviviente trae un paso mas y una cuenta que el otro no pide, INVENTARIAR CUANTOS MODOS OPERATIVOS TIENE CADA SISTEMA CRITICO, ademas de separar el diagnostico de la interfaz del remedio.",
            "pasos": {
                "1": ["CUBIERTO", 2],
                "2": ["INCISO", 3, "la logica interna de transicion de modos", ", y en "],
                "3": ["INCISO", 4, "reduciendo la carga cognitiva en momentos de alta demanda", ", "],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA Y LOS DOS MATICES QUE LA RAZON DECLARA PROPIOS DEL QUE MUERE SE SALVAN LOS DOS DE INCISO: la LOGICA INTERNA DE TRANSICION DE MODOS, que es el grano de profundidad que el paso 3 del superviviente no fija al entrenar en los modos y sus transiciones; y el REDUCIR LA CARGA COGNITIVA EN MOMENTOS DE ALTA DEMANDA, que es el motivo del rediseno y que su paso 4 no dice. Su paso 1 queda cubierto por el paso 2 del superviviente, que evalua si la interfaz permite detectar las transiciones. Sus dos condiciones quedan cubiertas una a una: operar sistemas con multiples modos por la condicion 1, e investigar sorpresas de automatizacion por la condicion 2, que habla de incidentes de confusion operador maquina. CERO perdidas nombradas.",
        },
        {
            "orden": 41,
            "superviviente": "clasificacion_sistemas_por_nivel_seguridad",
            "motivo": "LA PIEZA DECLARADA GANA A UN CONTEO, Y VA MARCADO COMO DISCUTIBLE. Los pasos apuntan al OTRO (3 contra 4 a favor de niveles_de_madurez_de_seguridad); las condiciones EMPATAN (2 contra 2) y el cableado apunta tambien al otro (2 contra 3). LA PIEZA DECLARADA APUNTA AQUI, Y ES LA UNICA VARA QUE LO HACE: la razon del puesto 2250 escribe SOBREVIVE clasificacion_sistemas_por_nivel_seguridad y mide por que, porque este trae EL INSTRUMENTO y el otro solo el aviso: LA ESCALERA NOMBRADA (unsafe, safer, safe y ultra safe), LA BASE DE MEDICION (datos historicos de fatalidad o lesion) y LAS ESTRATEGIAS NOMBRADAS POR PELDANO. Del otro dice que le queda UNA LINEA propia y que su paso 2 identifica las intervenciones SIN NOMBRARLAS. LA VARA QUE SE APLICA es la del acta 53 pregunta 3 y el acta 54 pregunta 2, GANA LO DECLARADO Y NO EL CONTEO, que es la misma que el acta 56 confirmo para el acto 23 del tramo 3. SE DICE EL RIESGO EN VEZ DE CALLARLO: el acta 50, adjudicacion 3, dice que en el choque entre la letra y la aritmetica manda la aritmetica, y por eso este acto va al reporte marcado.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 2, "han funcionado historicamente en ese nivel", ", entre las que "],
                "3": ["CUBIERTO", 3],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la unica linea que la razon declara propia del que muere: AJUSTAR LAS INVERSIONES EN SEGURIDAD SEGUN EL NIVEL DE MADUREZ DETECTADO. UN INCISO: el criterio de que las intervenciones sean las que HAN FUNCIONADO HISTORICAMENTE EN ESE NIVEL, adosado al paso 2 del superviviente, que nombra las tres estrategias sin decir de donde sale que corresponden. Sus otros dos pasos quedan cubiertos uno a uno. SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto: que LAS INTERVENCIONES ANTERIORES NO HAYAN FUNCIONADO como se esperaba no lo dice ninguna de las dos del superviviente. CERO perdidas nombradas, Y ESO IMPORTA AQUI MAS QUE EN OTROS ACTOS: el nodo que muere tiene MAS pasos que el que sobrevive, asi que la unica forma de que la eleccion no cueste nada es que sus cuatro piezas viajen, y las cuatro viajan.",
        },
        {
            "orden": 42,
            "superviviente": "accident_proneness_fallacy",
            "motivo": "LOS CONTEOS EMPATAN Y LA PIEZA DECLARADA DECIDE. Pasos 3 contra 3 y condiciones 2 contra 2: las dos varas contables de contenido empatan al digito. PERO EL CONTENIDO NO CALLA, porque EL MATERIAL PROPIO DECLARADO ES UNA VARA DE CONTENIDO (acta 54, pregunta 4) y aqui esta A UN SOLO LADO Y CON TODAS SUS LETRAS: la razon del puesto 2252 escribe que a declive_teoria_manzana_podrida NO LE QUEDA NI UNA LINEA PROPIA, y que accident_proneness_fallacy trae dos cosas suyas, LAS VARIABLES DE EXPOSICION NOMBRADAS (tipo de tarea, ruta y turno), que convierten el aviso en una comparacion que se puede hacer, y LA PROHIBICION CONCRETA de usar perfiles de propension para contratar o despedir, que es la unica frontera institucional del par. El cableado apuntaba al otro (2 contra 3) y NO llega a hablar, porque el contenido no calla.",
            "pasos": {
                "1": ["INCISO", 1, "que asumen exposicion al riesgo homogenea entre trabajadores", ", incluidas las "],
                "2": ["INCISO", 2, "antes de atribuir culpa personal", ", y hacerlo "],
                "3": ["CUBIERTO", 3],
            },
            "condiciones": {"1": ["APPEND"], "2": ["CUBIERTO", 1]},
            "nota": "NINGUNA PIEZA DE PASO VIAJA ENTERA Y NINGUNA SE PIERDE, que es lo que cabe esperar cuando la razon mide que al que muere NO LE QUEDA NI UNA LINEA PROPIA. DOS INCISOS que afinan la misma critica: la forma EXPOSICION HOMOGENEA de la estadistica sospechosa, adosada al paso 1 del superviviente; y el ANTES DE ATRIBUIR CULPA PERSONAL como momento del analisis de exposicion, adosado a su paso 2. SU CONDICION 1 VIAJA ENTERA por ser un disparador distinto: atribuir un accidente RECURRENTE unicamente a caracteristicas personales de un trabajador no lo dice ninguna de las dos del superviviente, que hablan de evidencia estadistica comparativa y de usar historiales como criterio de seleccion. CERO perdidas nombradas.",
        },
        {
            "orden": 43,
            "superviviente": "cultura_justa",
            "motivo": "LA GUARDA RESTRINGE Y ADEMAS LOS TRES CONTEOS APUNTAN AL MISMO LADO. cultura_justa ES PUERTA (extremo de puente aprobado) y la guarda 1B exige que sobreviva: es el UNICO candidato limpio del acto. Y AQUI, A DIFERENCIA DE LOS ACTOS 20 Y 38, NO HAY CHOQUE DE CONTEOS: los pasos (5 contra 4), las condiciones (3 contra 2) y el cableado (16 contra 4) apuntan LOS TRES a cultura_justa. QUIEN APUNTA AL OTRO LADO ES LA RAZON, y se dice con sus palabras: el puesto 2255 escribe SOBREVIVE cultura_justa_organizacional porque ese nodo trae UNA INSTITUCION PERMANENTE que el otro no tiene, EL GRUPO DE CONFIANZA QUE REVISA LOS CASOS DIFICILES O AMBIGUOS, y la propia razon se califica como DE LOS MAS DISCUTIBLES y avisa de que muere el nodo de cinco pasos contra el de cuatro. LA GUARDA NO DEJA HACER LO QUE LA RAZON PIDE, y el grupo de confianza VIAJA ENTERO en el reparto, asi que la institucion no se pierde. VA MARCADO COMO DISCUTIBLE EN EL REPORTE.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 4],
                "3": ["APPEND"],
                "4": ["INCISO", 2, "por escrito", ", y dejarla "],
            },
            "condiciones": {"1": ["APPEND"], "2": ["CUBIERTO", 2]},
            "nota": "UNA PIEZA VIAJA ENTERA Y ES EXACTAMENTE LA INSTITUCION POR LA QUE LA RAZON PREFERIA AL OTRO NODO: ARMAR UN GRUPO DE CONFIANZA QUE REVISE LOS CASOS DIFICILES O AMBIGUOS, que la razon llama lo unico del par que resuelve el caso donde los criterios no alcanzan. VA DE APPEND, que no pierde nada, y por eso la guarda puede mandar sin que el catalogo pague el precio que la razon temia. UN INCISO: el POR ESCRITO de la separacion entre error normal y mala conducta deliberada, adosado al paso 2 del superviviente, que traza esa linea sin exigir que quede escrita. Sus otros dos pasos quedan cubiertos. SU CONDICION 1 VIAJA ENTERA por ser un disparador distinto: BUSCAR QUE EL EQUIPO REPORTE ERRORES DE FORMA VOLUNTARIA no lo dice ninguna de las tres del superviviente, que hablan de ambiguedad sobre que sancionar, de desconfianza en el sistema disciplinario y de disenar politicas de manejo de errores. CERO perdidas nombradas.",
        },
        {
            "orden": 44,
            "superviviente": "vulnerabilidad_instalacion",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y LA RAZON DECLARA EL MISMO SUPERVIVIENTE. Pasos 3 contra 4 a favor de vulnerabilidad_instalacion; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice porque apuntaba al OTRO (5 contra 2). La razon del puesto 2264 escribe SOBREVIVE vulnerabilidad_instalacion: lo que el otro anade son TRES CALIFICATIVOS que son LINEA, y el superviviente trae un requisito de diseno que el otro no tiene, PROCEDIMIENTOS DE REINSTALACION CON SECUENCIAS NUMERADAS Y VERIFICABLES, mas la tesis que le da nombre y que ordena donde poner el esfuerzo, QUE LA INSTALACION ES MAS VULNERABLE QUE EL DESENSAMBLAJE.",
            "pasos": {
                "1": ["INCISO", 4, "cubiertas, sujetadores", ", incluidas las omisiones en "],
                "2": ["INCISO", 2, "con firma paso a paso", ", obligatorias y "],
                "3": ["INCISO", 3, "independientes posteriores al reensamblaje antes de la puesta en servicio", ", con inspecciones "],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA Y LOS TRES CALIFICATIVOS QUE LA RAZON DECLARA PROPIOS DEL QUE MUERE SE SALVAN LOS TRES DE INCISO, que es lo que la razon manda al decir que la firma y la inspeccion independiente se absorben como lineas suyas: las OMISIONES HISTORICAS NOMBRADAS (cubiertas, sujetadores) se adosan al paso 4 del superviviente, que analiza los historicos sin decir en que; la FIRMA PASO A PASO y el caracter OBLIGATORIO se adosan a su paso 2, que implementa las listas sin exigir firma; y la INDEPENDENCIA DEL INSPECTOR con la PUERTA DE LA PUESTA EN SERVICIO se adosan a su paso 3, que aumenta la supervision sin decir de quien ni hasta cuando. Sus dos condiciones quedan cubiertas una a una. CERO perdidas nombradas.",
        },
        {
            "orden": 45,
            "superviviente": "clasificacion_riesgos_por_dominio",
            "motivo": "LA PIEZA DECLARADA GANA A UN CONTEO, Y VA MARCADO COMO DISCUTIBLE. Los pasos EMPATAN (4 contra 4); las condiciones apuntan al OTRO (3 contra 2 a favor de areas_riesgo_primario) y el cableado apunta aqui (1 contra 4). LA PIEZA DECLARADA APUNTA AQUI Y CON MEDICION: la razon del puesto 2265 escribe SOBREVIVE clasificacion_riesgos_por_dominio, mide que el paso 1 del otro HABLA DE LOS CUATRO TIPOS DE RIESGO SIN NOMBRAR NI UNO mientras este los nombra (personal, operador clave, latente y terceros), aplica la regla de que EL QUE REMITE SIN NOMBRAR ES EL DERIVADO, y anade que este trae DOS INSTRUMENTOS que el otro no tiene, el BENCHMARK contra dominios similares con referencias historicas y la FECHA DE CADUCIDAD sobre el propio marco (si el enfoque quedo desactualizado frente a cambios tecnologicos o sociales). Del otro dice que le queda UNA linea propia. LA VARA QUE SE APLICA es la del acta 53 pregunta 3 y el acta 54 pregunta 2, GANA LO DECLARADO Y NO EL CONTEO. SE DICE EL RIESGO EN VEZ DE CALLARLO, igual que en el acto 41.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 4],
                "3": ["CUBIERTO", 4],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2], "3": ["APPEND"]},
            "nota": "UNA PIEZA DE PASO VIAJA ENTERA y es exactamente la unica linea que la razon declara propia del que muere: DEFINIR COMO SE VIGILARA CADA TIPO DE RIESGO que se identifique. Sus otros tres pasos quedan cubiertos: identificar los cuatro tipos es el paso 1 del superviviente, que ademas los NOMBRA; y determinar cual es mas urgente y revisar si solo se ha mirado el de lesiones personales son los dos su paso 4, que prioriza segun el tipo predominante y no solo lesiones, y se marcan los dos contra el porque la razon los mide asi. SU CONDICION 3 VIAJA ENTERA por ser un disparador distinto y ademas es la que sostiene el conteo que este acto no siguio: DESPUES DE UN INCIDENTE que muestre un tipo de riesgo que no se habia tomado en cuenta, por ejemplo el de terceros. VIAJANDO ENTERA, la vara de las condiciones no cuesta nada: el superviviente termina con las tres. CERO perdidas nombradas.",
        },
        {
            "orden": 46,
            "superviviente": "evitar_perdida_situacion_awareness",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y LA RAZON DECLARA EL MISMO SUPERVIVIENTE. Pasos 4 contra 4, empatados, y condiciones 2 contra 3 a favor de evitar_perdida_situacion_awareness, que es la unica vara de contenido no empatada del acto. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que apuntaba AL MISMO LADO (1 contra 2). La razon del puesto 2268 escribe SOBREVIVE evitar_perdida_situacion_awareness: lo unico propio del otro es RECHAZAR EL TERMINO EN CONTEXTOS LEGALES O DISCIPLINARIOS, y una prohibicion es LINEA, mientras que el superviviente trae DOS PASOS DE TRABAJO, definir explicitamente que normativa o estandar se usa para juzgar el comportamiento, y RECONSTRUIR EL TUNEL DEL OPERADOR con sus tres elementos.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 4],
                "3": ["CUBIERTO", 2],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la unica que la razon declara propia del que muere: RECHAZAR EL USO DEL TERMINO EN CONTEXTOS LEGALES O DISCIPLINARIOS como sustituto de una explicacion causal real. LA RAZON DICE QUE SE ABSORBE COMO LINEA SUYA Y AQUI VA DE APPEND, que es la forma que NO pierde nada, y se dice la diferencia en vez de darla por equivalente. Sus otros tres pasos quedan cubiertos uno a uno: evitar el termino como explicacion es el paso 1 del superviviente; reconstruir que informacion y contexto tenia el operador es su paso 4, el del TUNEL; y preguntar por que tenia sentido para ellos es su paso 2. Sus dos condiciones quedan cubiertas una a una. CERO perdidas nombradas.",
        },
        {
            "orden": 47,
            "superviviente": "sesgo_retrospectivo_hindsight_2",
            "motivo": "LA PIEZA DECLARADA GANA A UN CONTEO, Y VA MARCADO COMO DISCUTIBLE. LOS CONTEOS CHOCAN: pasos 3 contra 4 a favor de sesgo_retrospectivo_hindsight_2 y condiciones 2 contra 1 a favor de sesgo_retrospectivo_hindsight. El cableado NO PUEDE HABLAR porque el contenido no calla, CHOCA (acta 54, pregunta 4), y se dice que apuntaba al que muere (6 contra 3). LA PIEZA DECLARADA DESEMPATA Y APUNTA AL MISMO LADO QUE LOS PASOS: la razon del puesto 2281 escribe SOBREVIVE sesgo_retrospectivo_hindsight_2, mide que al otro le queda UNA linea propia (entrenar a los investigadores en el sesgo) y que este conserva DOS lineas de doctrina que el otro no tiene, el test de la forma de la pregunta y la advertencia contra la causa y efecto lineal. Y DEJA UNA COHERENCIA DECLARADA que se traslada sin tocarla: el nodo de Reason sobrevivio en los puestos 2234 y 2239 porque alli era el unico que preguntaba si la senal era siquiera visible; contra el unico nodo de Dekker que tambien lo pregunta, esa ventaja desaparece.",
            "pasos": {
                "1": ["CUBIERTO", 2],
                "2": ["APPEND"],
                "3": ["INCISO", 3, "el volumen de informacion disperso entre los participantes", ", sin olvidar "],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la unica linea que la razon declara propia del que muere: ENTRENAR A LOS INVESTIGADORES DE INCIDENTES EN EL RECONOCIMIENTO Y MITIGACION DEL SESGO RETROSPECTIVO. UN INCISO: el VOLUMEN DE INFORMACION DISPERSO ENTRE LOS PARTICIPANTES, que es la formulacion operativa del test compartido y que el paso 3 del superviviente deja en distinguir lo disponible de lo observable. Su paso 1 queda cubierto por el paso 2 del superviviente, que reconstruye la situacion sin usar lo que ya se sabe del resultado. SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos: evaluar LA CULPABILIDAD O PREVISIBILIDAD de los actores tras un accidente, y DISENAR PROCESOS DE APRENDIZAJE ORGANIZACIONAL a partir de fallos; la unica condicion del superviviente habla de revisar un error para entender que paso. CERO perdidas nombradas, y aqui importa decirlo: el superviviente pasa de UNA condicion a TRES, asi que la vara de las condiciones que apuntaba al otro queda saldada por el reparto.",
        },
        {
            "orden": 48,
            "superviviente": "limite_busqueda_causas_pendulo",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y LA RAZON DECLARA EL MISMO SUPERVIVIENTE. Pasos 4 contra 3 a favor de limite_busqueda_causas_pendulo; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que apuntaba AL MISMO LADO (4 contra 2). La razon del puesto 2328 escribe SOBREVIVE limite_busqueda_causas_pendulo: al otro le queda UN criterio propio que es UNA LINEA, y este trae dos cosas que el otro no tiene, EL TEST OPERATIVO (en que punto el analisis causal deja de aportar valor remedial practico), que es un criterio de utilidad y no de jurisdiccion, y EL CONTRAPESO QUE IMPIDE ABUSAR DE LA PROPIA REGLA (no diluir la responsabilidad organizacional atribuyendolo todo a fuerzas sociales incontrolables), sin el cual, dice la razon, una regla de parada es una excusa.",
            "pasos": {
                "1": ["CUBIERTO", 3],
                "2": ["CUBIERTO", 3],
                "3": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente el unico criterio que la razon declara propio del que muere: PRIORIZAR LA CALIDAD Y DISPONIBILIDAD DE EVIDENCIA CONFIABLE al fijar los limites del analisis, que es un criterio de EVIDENCIA y no de jurisdiccion ni de utilidad, asi que no lo dice ninguno de los cuatro pasos del superviviente. Sus otros dos pasos caen los dos en el paso 3 del superviviente, y se dice en vez de repartirlos por comodidad: ese paso reconoce explicitamente que factores societales y economicos son DADOS y no controlables por el gestor de riesgo, que es a la vez definir el alcance por lo controlable y evitar extenderlo a lo inmutable, o sea la misma frase por sus dos caras. SU CONDICION 2 VIAJA ENTERA por ser un disparador distinto: DECIDIR DONDE TRAZAR LA LINEA DE RESPONSABILIDAD ORGANIZACIONAL no lo dice ninguna de las dos del superviviente. CERO perdidas nombradas.",
        },
        {
            "orden": 49,
            "superviviente": "condiciones_latentes_largo_plazo",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y LA RAZON DECLARA EL MISMO SUPERVIVIENTE CON UNA CORRECCION FECHADA DETRAS. Pasos 3 contra 3, empatados, y condiciones 1 contra 2 a favor de condiciones_latentes_largo_plazo, que es la unica vara de contenido no empatada del acto. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice porque apuntaba al OTRO (3 contra 1). LA RAZON DEL PUESTO 2335 TRAE UN SUPERVIVIENTE CORREGIDO EL 18 ago 2026 y explica el volteo con P.8: EL ALCANCE DEL ROL ES CONTENIDO, y una cabeza que vale para toda infraestructura critica no puede llamarse como un descarrilamiento concreto. Lo prueba con los entregables: el del superviviente es un INFORME DE AUDITORIA HISTORICA generico, y el del que muere es un INFORME DE CASO DE ESTUDIO que manda buscar POSIBLES FALLAS DE 1916 EQUIVALENTES, o sea que lleva la fecha de un terraplen dentro de su propio producto. La razon deja registrada la FIGURA NUEVA con nombre: EL CASO NO ES LA CASA.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 2, "eliminacion de fauna, patrones climaticos", " Cuentan entre ellos la "],
                "3": ["APPEND"],
            },
            "condiciones": {"1": ["APPEND"]},
            "nota": "DOS PIEZAS VIAJAN ENTERAS Y SON EXACTAMENTE LAS DOS QUE LA RAZON MANDA REPONER, que es lo que hace que EL CASO NO SEA LA CASA sin perder lo que el caso traia: el REQUISITO DE METODO propio, ANALISIS GEOTECNICOS O DE INGENIERIA PROFUNDOS Y NO SOLO INSPECCION VISUAL EXTERNA, que la razon llama real y dice que viaja; y su unica condicion, ILUSTRAR CON UN EJEMPLO CONCRETO el concepto de condicion latente sin fallo humano activo, que es exactamente la forma en que la razon quiere que Nakina quede dentro de la doctrina, como EJEMPLO NOMBRADO con su falla latente de setenta y seis anos. UN INCISO: los factores ambientales nombrados (eliminacion de fauna, patrones climaticos), adosados al paso 2 del superviviente, que habla de factores ambientales naturales sin dar ninguno. CERO perdidas nombradas.",
        },
        {
            "orden": 50,
            "superviviente": "cultura_de_aprendizaje",
            "motivo": "LA PIEZA DECLARADA GANA A UN CONTEO, Y VA MARCADO COMO DISCUTIBLE. Los pasos EMPATAN (4 contra 4); las condiciones apuntan al OTRO (2 contra 3 a favor de ingenieria_cultura_aprendizaje) y el cableado apunta aqui (5 contra 3). LA PIEZA DECLARADA APUNTA AQUI: la razon del puesto 2389 escribe SOBREVIVE cultura_de_aprendizaje, mide que lo unico propio del otro es EL ENFASIS de comprometerse a implementar y no solo hablar de ello, y que un enfasis es LINEA; y nombra los DOS PASOS que solo el superviviente tiene y que son los que CIERRAN EL CICLO, MEDIR LA EFECTIVIDAD DE LAS REFORMAS con seguimiento continuo, sin lo cual nadie sabe si la mejora sirvio, e INSTITUCIONALIZAR LA REVISION PERIODICA DE LECCIONES APRENDIDAS. La razon lo resume en una frase que es la vara: el otro termina donde se implementa; este comprueba y vuelve a empezar. LA VARA QUE SE APLICA es la del acta 53 pregunta 3 y el acta 54 pregunta 2, GANA LO DECLARADO Y NO EL CONTEO. SE DICE EL RIESGO EN VEZ DE CALLARLO, igual que en los actos 41 y 45.",
            "pasos": {
                "1": ["INCISO", 1, "observar incidentes y condiciones de riesgo", ", incluida una forma sistematica de "],
                "2": ["INCISO", 1, "momentos regulares para analizar y diagnosticar", ", y "],
                "3": ["CUBIERTO", 2],
                "4": ["INCISO", 2, "tu tiempo y tus recursos explicitamente para IMPLEMENTAR las mejoras encontradas, no solo hablar de ellas", ", comprometiendo "],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"], "3": ["APPEND"]},
            "nota": "NINGUNA PIEZA DE PASO VIAJA ENTERA Y EL ENFASIS QUE LA RAZON DECLARA COMO LO UNICO PROPIO DEL QUE MUERE SE SALVA DE INCISO: el COMPROMETER TIEMPO Y RECURSOS PARA IMPLEMENTAR Y NO SOLO HABLAR DE ELLO se adosa al paso 2 del superviviente, que define los procesos de decision para implementar reformas sin exigir ese compromiso. Otros dos incisos recogen las dos primeras casillas del ciclo con las palabras del que muere, las dos adosadas al paso 1 del superviviente, que es donde vive el analisis de los datos del reporte. DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos, y una de ellas es justo la que sostenia el conteo que este acto no siguio: POSPONER REFORMAS DE SEGURIDAD POR TAREAS MAS URGENTES, y QUERER EVITAR REPETIR ERRORES YA IDENTIFICADOS. VIAJANDO ENTERAS, el superviviente termina con TRES condiciones y la vara que apuntaba al otro queda saldada por el reparto. CERO perdidas nombradas.",
        },
    ],
    "declarados": [],
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
