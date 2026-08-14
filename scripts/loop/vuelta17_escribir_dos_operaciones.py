"""VUELTA 17, TAREA 2. Escribe en docs/plan/OPERACIONES.jsonl las DOS operaciones
de destejido de las dos costuras que la DECISION DEL FUNDADOR del 14 ago 2026
saca de "sin dueno": lienzo_modelo_negocio y planificacion_recoleccion_datos.

El plan pasa de 69 a 71 operaciones. No toca ninguna de las 69 existentes.

Controles antes de escribir (si alguno falla, no escribe):
  1. hay 69 operaciones y los ids son unicos
  2. OP-D-08 y OP-D-09 no existen todavia
  3. los ordenes 8 y 9 estan libres en la fase 02_DESTEJIDOS
  4. los dos nodos existen en el grafo y no estan en la nomina de ninguna operacion
  5. cero guiones largos y cero guiones medios en lo que se escribe

Uso:
  python scripts/loop/vuelta17_escribir_dos_operaciones.py              (simulacro)
  python scripts/loop/vuelta17_escribir_dos_operaciones.py --escribir
"""

import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")


OP_D_08 = {
    "id_op": "OP-D-08",
    "fase": "02_DESTEJIDOS",
    "tipo": "DESTEJIDO",
    "nodos": ["lienzo_modelo_negocio"],
    "superviviente": None,
    "preservar": [
        "LA COLUMNA VERTEBRAL LA SENALA LA SIMULACION, NO EL GUSTO: de las CUATRO narraciones del Canvas, la unica que sobrevive a la prueba de veredictos si se conserva SOLA es la CUARTA, los pasos 13 a 17, la enumeracion bloque a bloque (segmentos, propuesta de valor por segmento, canales y relaciones e ingresos, recursos y actividades y asociaciones, costos y resultado). Las otras tres, conservadas solas, rompen al menos un veredicto vivo. Medido, no supuesto: scripts/plan/simular_destejido.py",
        "PERO CONSERVAR SOLO ESA COLUMNA ES PODA, Y LA PODA AQUI ESTA PROHIBIDA POR P.3: las cuatro narraciones son del MISMO tema (las cuatro mandan completar los nueve bloques del mismo lienzo), y cuando el bloque pegado es del mismo tema NO SE PODA, SE REPARTE. El lector que sigue este nodo no puede distinguir donde acaba una narracion y empieza la otra, asi que podar tres le quitaria practica que estaba usando entera",
        "DEL BLOQUE 1 (pasos 1 a 4), material propio que no esta en ninguna otra narracion y que por la REGLA DE REPARTO de esta fase viaja AL BLOQUE DEL QUE PROVIENE o, si no tiene bloque, al superviviente: imprimir el lienzo en tamano grande para trabajo colaborativo (paso 1); LA CLAUSULA DE LAS NOTAS POST-IT del paso 2, que es el ancla del veredicto 1136; iterar y discutir en grupo hasta lograr coherencia entre los bloques (paso 3); usar el lienzo como base para pivotar o validar hipotesis del negocio (paso 4)",
        "DEL BLOQUE 3 (pasos 9 a 12), y es la narracion con mas practica propia de las cuatro: imprimir un canvas para CADA MIEMBRO del equipo (paso 9), que es la SEGUNDA orden de imprimir del nodo y se funde con la del paso 1 en una sola linea con sus dos formatos; reunirse ACEPTANDO QUE HABRA VACIOS EN LA PRIMERA VERSION (paso 10); PAUSAR PARA INVESTIGAR donde haya vacios importantes (paso 11); publicar el canvas en el espacio de trabajo y ACTUALIZARLO conforme avanza el proyecto (paso 12). Ninguna de estas cuatro lineas aparece en las otras tres narraciones",
        "EL PASO 14 ES INTOCABLE Y ESTA MEDIDO: definir la propuesta de valor para cada segmento es el ancla del veredicto 1434 (D contra value_proposition_canvas), y ese es el UNICO de los tres veredictos que citan pasos de este nodo cuya razon NO se declara invariante. Si el destejido se lleva el paso 14, el 1434 deja de sostenerse y hay que releerlo. Los otros dos (998 y 1136) declaran su invarianza dentro de su propia razon",
        "DEL BLOQUE 2 (pasos 5 a 8) NO SOBREVIVE NINGUNA LINEA NUEVA, y se dice por que: sus tres pasos de contenido (6 socios y actividades, 7 canales y relaciones y segmentos, 8 costos e ingresos) estan los tres cubiertos por la enumeracion mas fina de 13 a 17, que ademas anade la propuesta de valor por segmento que el bloque 2 no tiene. LO QUE HAY QUE COMPROBAR AL EJECUTAR Y NO SE DA POR HECHO: si la frase PARA LA SOLUCION DISENADA del paso 5 es un MARCO propio (aplicar el lienzo a una solucion ya disenada) y no solo un encabezado repetido, entonces es material propio y se reparte como los demas, no se va con el bloque",
    ],
    "eliminar": [
        "las TRES copias sobrantes de la orden de completar los nueve bloques: el nodo termina con UNA sola. Se van como linea los pasos 5, 6, 7 y 8 (el bloque 2 entero, cubierto por la enumeracion de 13 a 17) y el paso 9 en su forma actual (la segunda orden de imprimir, que se funde con la del paso 1)",
        "NINGUNA LINEA DE CONTENIDO PROPIO SE ELIMINA. Lo que se va es repeticion; todo lo propio de los tres bloques que no son la columna esta listado en preservar, uno por uno. Si al ejecutar aparece contenido propio en un paso marcado para irse, ese paso NO se va: se reparte",
    ],
    "aristas_nuevas": [],
    "orden": 8,
    "depende_de": [],
    "bloquea_a": [],
    "verificacion": [
        "CASO POSITIVO DE LA OPERACION, y es el que la manda: EL PAR 784 SE DESCONGELA Y SE JUZGA. Su razon dice, con esas palabras, NO SE JUZGA HOY: el nodo largo es costura confirmada Y EL SOLAPE ES SU PROPIO NUCLEO REPETIDO, y remata con primero la cirugia y despues el par. Si tras el destejido el par 784 sigue sin poderse juzgar, la cirugia no hizo lo que dice que hace. MEDIDO EN LA VUELTA 17: 784 es el UNICO par de los 3.388 cuya razon lleva la frase NO SE JUZGA HOY",
        "Y AL JUZGARLO SE COMPRUEBA LO QUE EL PROPIO 784 DEJO ANOTADO: que el analisis cruzado (como una debilidad de un bloque golpea a los otros) NO esta en el nodo largo y es lo unico que aporta swot_business_model_canvas. Si tras el destejido resultara que si esta, el par cambia de clase y hay que decirlo",
        "el veredicto 1434 (D contra value_proposition_canvas) se RELEE contra el nodo destejido y tiene que seguir dando D: su ancla, la linea definir la propuesta de valor para cada segmento, tiene que seguir viva",
        "el veredicto 1136 (D contra pensamiento_visual_modelos_negocio) se relee: la clausula de las NOTAS ADHESIVAS tiene que seguir viva, porque es la linea cuyo procedimiento trae el otro nodo",
        "CERO MOVIMIENTO DE GRAFO, medido y no supuesto (banco 9.14 y P.1): lienzo_modelo_negocio declara 91 vecinos en sus dos campos antes de la operacion y tiene que declarar 91 despues; el grafo entero tiene 16.866 entradas de arista antes y tiene que tener 16.866 despues. Ningun id se mueve, ningun alias se crea. UN DESTEJIDO QUE MUEVA UNA ARISTA NO ES ESTE DESTEJIDO",
        "las TRES aristas paso a nodo en las que este nodo es HIJO siguen resolviendo (de tipo_de_mercado_estrategia_competitiva paso 5, de customer_discovery_overview paso 1 y de unbundling_business_models paso 4, las tres YA ESCRITAS): no dependen de los pasos de este nodo sino de los de su madre, verificado en la simulacion de la vuelta 17",
        "EL RECUENTO QUE CIERRA LA CIRUGIA: el nodo queda con UNA sola orden de completar los nueve bloques. Si al recontar quedan dos, el destejido no se hizo",
        "el entregable_esperado se relee contra el texto que quede: hoy dice Lienzo de Modelo de Negocio completo con los 9 bloques definidos y coherentes entre si, y esa frase tiene que seguir siendo cierta del nodo destejido",
        "GATE 0 verde, y recomputo del cierre transitivo tras el acto (banco 9.21): el destejido puede cambiar el veredicto del 784, y si el 784 saliera A este nodo dejaria de ser componente de uno",
    ],
    "evidencia": [
        "docs/FICHA_SUBFUSION_GRADIENTE.md, lote C2 punto 2: costura CONFIRMADA, 17 pasos, CUATRO NARRACIONES DEL CANVAS, con el reparto escrito por bloques (1 a 4 con post-its, 5 a 8 para la solucion disenada, 9 a 12 con el equipo y publicacion, 13 a 17 bloque por bloque) y el literal completar cada uno de los 9 bloques localizado en los pasos 2 y 5. Nodo insignia, como el MVP",
        "docs/COSTURAS_INTERNAS.jsonl: senal de bloque 59,2, senal de pareja 66,0, corte mecanico en el 13, disparo por bloque. En la tabla de la franja de FICHA_SUBFUSION_GRADIENTE.md cae en la fila POR ENCIMA DE 52,0, donde nueve de nueve son confirmadas y cero falsas",
        "veredicto del puesto 784 (B): NO SE JUZGA HOY, el solape cruza las CUATRO junturas a la vez, por el TOQUE UNICO del banco 9.4 con el refinamiento del 673, primero la cirugia y despues el par. Y se nombra a si mismo TERCER NODO DEL ARCHIVO QUE BLOQUEA UN PAR POR COSTURA, con voz_del_cliente_voc y los dos de A/B del 738",
        "veredicto del puesto 998 (D): la orden de completar los nueve bloques repetida en sus pasos 2, 5, 13, 14, 15, 16 y 17, o sea que POR POSICION cualquier solape toca alguna juntura; y su veredicto se declara INVARIANTE por dependencia",
        "veredictos de los puestos 1123 y 1136 (D): de las costuras mas averiadas del archivo, con el lienzo mandado imprimir DOS veces; los dos se declaran invariantes y el 1136 apoya el suyo en el paso 2",
        "veredicto del puesto 1434 (D): dice literalmente que lienzo_modelo_negocio ES COSTURA CONFIRMADA Y NO TIENE GEMELO, ASI QUE SU ARREGLO ES UN DESTEJIDO SOLO. Es la frase del propio archivo que esta operacion ejecuta, y estaba escrita desde antes de que la operacion existiera",
        "docs/plan/CONTROL_MUESTRA_D.md, cierre: el control de las D levanto de paso, sin buscarlo, que el veredicto del puesto 998 deja anotado que lienzo_modelo_negocio es una costura de DIECISIETE pasos con la orden de completar los nueve bloques repetida en SIETE de ellos",
        "docs/plan/RECOMPUTO_3388.md, TAREA 2.B puntos 3 y 4: de las 31 costuras confirmadas SIN gemelo vigente, es UNA DE LAS DOS que no aparecia en la nomina de ninguna operacion del plan, ni de fuente ni de fusion",
        "MEDIDO EN LA VUELTA 17 con scripts/loop/vuelta17_dos_costuras.py, de solo lectura: SIETE pares en el cribado (543 D, 784 B, 998 D, 999 D, 1123 D, 1136 D, 1434 D), CERO A vigentes sobre un dominio core con 1.445 pares juzgados, CERO nominas de operacion, y UNA SOLA FUENTE DECLARADA (Business Model Generation, Osterwalder), que es lo que descarta la dependencia de una DECISION_DE_FUENTE",
        "SIMULADO EN LA VUELTA 17 con scripts/plan/simular_destejido.py, de solo lectura sobre una copia en memoria: las CUATRO opciones de conservar una sola narracion se probaron una a una, y TRES DE LAS CUATRO rompen el veredicto 1434; la cuarta (pasos 13 a 17) no rompe ningun apoyo medido pero se lleva TODA la practica propia de los bloques 1 y 3, que es justo lo que P.3 prohibe podar. El reparto escrito en preservar es el unico escenario probado que no rompe ningun apoyo y no pierde practica propia",
    ],
    "estado": "LISTA",
    "fecha_corte": "2026-08-14",
    "adjudicacion": "DECISION DEL FUNDADOR, 14 ago 2026: lienzo_modelo_negocio RECIBE DUENO. Queda revertida la adjudicacion anterior del auditor (docs/loop/ACTA_AUDITOR.md VUELTA 13 seccion 5 punto 5, NO SE CREAN OPERACIONES NUEVAS PARA ELLAS), que no se borra y sigue escrita con su fecha. FORMA DE LA OPERACION: DESTEJIDO SOLO, sin fusion acoplada, y no es eleccion de esta vuelta sino la que el propio archivo ya tenia escrita en el veredicto del puesto 1434 (es costura confirmada y no tiene gemelo, asi que su arreglo es un destejido solo). REMEDIO: REPARTO Y NO PODA, por P.3, porque las cuatro narraciones son del mismo tema. La eleccion de columna vertebral (los pasos 13 a 17) NO se adjudica por gusto: la senala la simulacion, que tumbo las otras tres.",
    "pregunta_pendiente": "UNA, concreta y de lectura corta, no de alcance: el paso 5 dice completar los nueve bloques PARA LA SOLUCION DISENADA. Si esa frase es un MARCO propio (aplicar el lienzo a una solucion ya disenada, que es un momento distinto del proyecto) entonces es material propio del bloque 2 y se reparte como el resto; si es solo un encabezado repetido, se va con su bloque. No se decide aqui porque decidirlo exige leer el nodo con el ojo puesto en esa frase, y esta operacion se escribio SIN releer el nodo de cero, con la evidencia que el frente de costuras ya tenia medida. Es la unica pieza del reparto que queda abierta.",
    "nota": "TRES CONTEOS DEL MISMO HECHO QUE PARECIAN CONTRADECIRSE Y NO SE CONTRADICEN, reconciliados en la vuelta 17 leyendo los tres sitios en vez de elegir uno: docs/FICHA_SUBFUSION_GRADIENTE.md dice que el literal completar cada uno de los 9 bloques esta en los pasos 2 y 5 (DOS); docs/INTRA_DOMINIO_INFORME.md dice los nueve bloques mandados completar CUATRO veces; y el veredicto del 998, via docs/plan/CONTROL_MUESTRA_D.md, dice repetida en SIETE de sus pasos. Los tres son correctos y cuentan tres objetos distintos: DOS es el literal exacto, CUATRO son las narraciones, y SIETE son los pasos que dan la orden contando la enumeracion de 13 a 17 que recorre los bloques uno por uno. Ninguno se corrige. UNA DISCREPANCIA QUE SE DECLARA EN VEZ DE CUADRARSE: el veredicto del 1123 estima que UN DESTEJIDO LO DEJARIA EN UNOS CINCO PASOS. El reparto medido en esta operacion deja DOCE portadores de linea, no cinco, porque el 1123 estimaba una PODA (quedarse con una narracion) y P.3 obliga a un REPARTO (conservar toda la practica propia de las cuatro). La estimacion de cinco no era una medicion y no se toca; la de doce sale de la simulacion y lleva su instrumento al lado. AVISO DE ORDEN, declarado y no arreglado por cuenta propia: el criterio de orden de esta fase es CONGELADOS LIBERADOS (docs/plan/02_DESTEJIDOS.md), y por ese criterio esta operacion libera UNO (el par 784) y le tocaria ir entre OP-D-03 (libera dos) y OP-D-04 (libera cero). Se escribe con orden 8, al final, PORQUE RENUMERAR SIETE OPERACIONES YA ADJUDICADAS NO ES ALGO QUE ESTA VUELTA TENGA AUTORIZADO. Queda como discutible marcado del reporte de la vuelta 17. HUECO QUE ESTA OPERACION TAPA, y es el motivo de fondo de la decision del fundador: el par 784 estaba congelado por una costura cuya cirugia no tenia dueno, asi que el congelado no entraba en la contabilidad de nadie. MEDIDO EN LA VUELTA 17: el numero 784 no aparece NI UNA VEZ en todo docs/plan/. Su propia razon se nombra TERCER NODO DEL ARCHIVO QUE BLOQUEA UN PAR POR COSTURA, y de los tres, dos ya tenian operacion (voz_del_cliente_voc en OP-D-02 y ab_testing_optimizacion en OP-D-03) y este era el que no la tenia.",
}


OP_D_09 = {
    "id_op": "OP-D-09",
    "fase": "02_DESTEJIDOS",
    "tipo": "DESTEJIDO",
    "nodos": ["planificacion_recoleccion_datos"],
    "superviviente": None,
    "preservar": [
        "EL METODO COMPLETO, pasos 5 a 16, que es el cuerpo del nodo y no se toca: definir puntos de recoleccion, seleccionar y capacitar recolectores imparciales, disenar y probar metodos y formularios con MSA, auditar y validar, filtrar y analizar, evaluar supuestos de muestra, aplicar tecnicas graficas y estadisticas, decidir si hacen falta mas datos, analisis de sensibilidad, revisar que las conclusiones respondan al problema original, presentar el informe con resumen ejecutivo, y determinar si las conclusiones aplican a otros problemas",
        "EL PASO 7 ES INTOCABLE Y ESTA MEDIDO: disenar, preparar y probar metodos, formularios e instrucciones de recoleccion (incluir MSA) es el ancla del UNICO veredicto de este nodo en todo el cribado, el 2695 (D contra diseno_de_metodos_de_recoleccion_de_datos), cuya razon dice que el diseno del metodo PROFUNDIZA UN PASO DEL PLAN y nombra ese paso 7. Vive en el bloque 5 a 16, asi que el destejido no lo toca; se escribe igual para que nadie lo mueva al reordenar",
        "EL PASO 10 SOSTIENE DOS ARISTAS PASO A NODO YA CALIBRADAS: evaluar supuestos del tamano de muestra y del analisis es el ancla de las candidatas hacia analisis_pareto y hacia analisis_pareto_proyectos_elefante (docs/plan/PASO_NODO_CALIBRADO.jsonl, las dos con arista TODAVIA NO ESCRITA). Tambien vive en el bloque 5 a 16 y tampoco se toca",
        "DEL INDICE (pasos 1 a 4), LO UNICO QUE NO TIENE CASA EN EL METODO Y POR TANTO NO SE PUEDE PODAR: establecer los objetivos de recoleccion y FORMULAR LA PREGUNTA ESPECIFICA (paso 1). Por la REGLA DE REPARTO de esta fase (la perdida que no tenga bloque va AL SUPERVIVIENTE) sobrevive como cabecera del metodo. Y hay un motivo interno ademas del formal: el paso 14 que sobrevive dice revisar que las conclusiones respondan AL PROBLEMA TECNICO ORIGINAL, y quien establece ese problema original es el paso 1. Podarlo dejaria al 14 apuntando a algo que el nodo ya no dice. El resumen teorico del propio nodo lo dice igual: empezar con el fin en mente, trabajando hacia atras DESDE LA PREGUNTA",
        "LOS PASOS 2, 3 Y 4 SE VAN COMO LINEA PERO SU CONTENIDO SE COMPRUEBA UNO A UNO ANTES, no despues: decidir que medir (2) contra los pasos 9 y 15 que analizan y presentan; decidir como medir la poblacion o muestra con herramienta, estrategia de muestreo y tamano (3) contra los pasos 7 y 10; recolectar con minimo sesgo (4) contra los pasos 5, 6 y 8. Si alguna de las tres deja un resto que el metodo no dice, ese resto se reparte y no se pierde",
    ],
    "eliminar": [
        "el INDICE que se colo como pasos: los pasos 2, 3 y 4, que anuncian lo que el metodo de 5 a 16 hace en detalle. El paso 1 NO se elimina, se reparte al superviviente (ver preservar)",
        "NINGUN CONTENIDO SIN CASA SE ELIMINA. Los tres pasos que se van tienen que tener, cada uno, el paso del metodo que ya los dice, comprobado antes de quitarlos y no despues",
    ],
    "aristas_nuevas": [],
    "orden": 9,
    "depende_de": [],
    "bloquea_a": [],
    "verificacion": [
        "CASO POSITIVO DE LA OPERACION: el par 2695 se RELEE contra el nodo destejido y tiene que seguir dando D. Y su propio DISCUTIBLE MARCADO es la prueba fina: la razon del 2695 avisa de que QUIEN LEA EL DISENO DEL METODO COMO EL PASO 7 DEL PLAN SUBSUMIDO DIRA A POR CONTENCION. Tras quitar el indice, el plan queda MAS parecido a un metodo y menos a un resumen, o sea que el riesgo de contencion SUBE, no baja. SI TRAS EL DESTEJIDO EL 2695 SE VUELVE A, ESO ES UN RESULTADO DE LA OPERACION Y SE ESCRIBE, no un fallo de la cirugia",
        "el paso 7 sigue vivo palabra por palabra, con su MSA dentro",
        "el paso 10 sigue vivo: es el ancla de las dos aristas paso a nodo candidatas hacia analisis_pareto y analisis_pareto_proyectos_elefante, que siguen sin escribirse y no se escriben aqui",
        "EL PASO 14 NO QUEDA COLGANDO: revisar que las conclusiones respondan al problema tecnico original solo se sostiene si el nodo sigue diciendo en algun sitio cual era el problema. Si tras la cirugia el nodo no lo dice, la cirugia se paso",
        "CERO MOVIMIENTO DE GRAFO, medido y no supuesto: planificacion_recoleccion_datos declara 5 vecinos en sus dos campos (2 previos, 3 siguientes) antes de la operacion y tiene que declarar 5 despues; el grafo entero tiene 16.866 entradas de arista antes y despues. Ningun id se mueve, ningun alias se crea",
        "el entregable_esperado se relee contra el texto que quede: hoy dice plan documentado de recoleccion y analisis de datos con preguntas formuladas, metodo de muestreo definido y plan de presentacion de resultados, y las TRES piezas que nombra (preguntas, muestreo, presentacion) tienen que seguir estando en los pasos que sobrevivan. La primera de las tres es justo el paso 1, que por eso no se poda",
        "GATE 0 verde, y recomputo del cierre transitivo tras el acto (banco 9.21)",
    ],
    "evidencia": [
        "docs/FICHA_SUBFUSION_GRADIENTE.md, lote C2 punto 5: costura CONFIRMADA, 16 pasos, COSTURA LEVE, con la anatomia escrita y con su remedio ya nombrado: los cuatro primeros pasos son UN RESUMEN pegado delante del metodo completo que empieza en el 5, y DESTEJIDO FACIL, no hay que elegir entre narraciones, HAY QUE QUITAR UN INDICE QUE SE COLO COMO PASOS",
        "docs/COSTURAS_INTERNAS.jsonl: senal de bloque 52,3, senal de pareja 63,4, corte mecanico en el 11, disparo por bloque. Cae en la fila POR ENCIMA DE 52,0 de la tabla de la franja, donde nueve de nueve son confirmadas y cero falsas, y es la ultima de esa fila",
        "docs/FICHA_SUBFUSION_GRADIENTE.md, cierre de la asimetria: es LA UNICA de las 46 costuras confirmadas que NO es del nucleo (45 nucleo y 1 quality), y la ficha deja escrito el dato que vale mas que la excepcion: tiene 16 pasos, o sea que el unico nodo de mundo con costura confirmada es UN NODO LARGO, que es lo que predice la hipotesis de que la asimetria sea efecto del tamano y no de la salud. La ficha remata: cuando el barrido normalice la tasa de costura por longitud, ESTE ES EL CASO QUE HAY QUE MIRAR PRIMERO",
        "veredicto del puesto 2695 (D, sano), unico par de este nodo en todo el cribado: el diseno del metodo profundiza un paso del plan, y ese paso es el 7. Con DISCUTIBLE MARCADO en su propia razon: quien lea el diseno del metodo como el paso 7 del plan subsumido dira A por contencion",
        "docs/plan/PASO_NODO_CALIBRADO.jsonl: dos candidatas paso a nodo salen del paso 10 de este nodo, hacia analisis_pareto y hacia analisis_pareto_proyectos_elefante, las dos con arista todavia sin escribir; y una tercera entra desde analisis_diagnostico_causa paso 3, que no depende de los pasos de este nodo",
        "docs/plan/RECOMPUTO_3388.md, TAREA 2.B puntos 3 y 4: de las 31 costuras confirmadas SIN gemelo vigente, es UNA DE LAS DOS que no aparecia en la nomina de ninguna operacion del plan",
        "MEDIDO EN LA VUELTA 17 con scripts/loop/vuelta17_dos_costuras.py, de solo lectura, y ES UNA MEDICION QUE EN EL CORTE 2.117 NO SE PODIA HACER: UN solo par en el cribado (2695, D), CERO A vigentes, CERO nominas de operacion, y UNA SOLA FUENTE DECLARADA (Juran's Quality Handbook, Defeo). El dominio quality tenia CERO pares juzgados al corte 2.117 (estaba SIN CRIBAR) y al corte 3.388 tiene 844 con 126 A, asi que el CERO A VIGENTES de este nodo pasa de ser un hueco de cribado a ser una medicion de verdad",
        "SIMULADO EN LA VUELTA 17 con scripts/plan/simular_destejido.py, de solo lectura sobre una copia en memoria: se probaron los dos escenarios, quitar los pasos 1 a 4 enteros y quitar solo el 2, 3 y 4. NINGUNO DE LOS DOS rompe el veredicto 2695 ni las dos anclas del paso 10. LA SIMULACION NO LOS DISTINGUE, y por eso la eleccion no la hace ella: la hace la REGLA DE REPARTO de esta fase, que manda que la perdida sin bloque vaya al superviviente, y esa perdida es la pregunta especifica del paso 1",
    ],
    "estado": "LISTA",
    "fecha_corte": "2026-08-14",
    "adjudicacion": "DECISION DEL FUNDADOR, 14 ago 2026: planificacion_recoleccion_datos RECIBE DUENO. Queda revertida la adjudicacion anterior del auditor (docs/loop/ACTA_AUDITOR.md VUELTA 13 seccion 5 punto 5), que no se borra y sigue escrita con su fecha. FORMA DE LA OPERACION: DESTEJIDO SOLO, sin fusion acoplada, porque no tiene gemelo con A vigente y su unico par del cribado (2695) es D sano. REMEDIO: QUITAR EL INDICE, tal como la ficha del gradiente ya lo tenia escrito, PERO CON UNA CORRECCION QUE ESTA VUELTA MIDE Y LA FICHA NO DECIA: el indice son los pasos 2, 3 y 4, no los cuatro. El paso 1 (formular la pregunta especifica) no tiene casa en el metodo de 5 a 16 y sostiene al paso 14, asi que se reparte al superviviente en vez de podarse. La ficha decia destejido facil y sigue siendo facil; lo que no es es de cuatro.",
    "pregunta_pendiente": "NINGUNA para escribir la operacion. Queda ANOTADO, no preguntado, un desajuste interno del nodo que esta operacion NO resuelve porque no es suyo: el resumen_teorico del nodo declara que el proceso INVOLUCRA 17 PASOS y el nodo tiene 16 pasos_accionables (medido en la vuelta 17 sobre dataset/metadata/master_graph.json). Puede ser que el original de Juran tenga 17 y el catalogo perdiera uno al tejer, o que el resumen cuente mal. NO SE RELLENA: es hueco nombrado, y decidirlo exige la fuente, que esta fuera del repo.",
    "nota": "POR QUE ESTA ES LA MAS BARATA DE LAS DOS Y AUN ASI NO ES AUTOMATICA. La ficha del gradiente la clasifico como COSTURA LEVE y como DESTEJIDO FACIL, y lo es: no hay que elegir entre narraciones rivales, solo hay que quitar un indice. Pero el facil se rompe en un sitio, y esta medido: PODAR LOS CUATRO PASOS DEL INDICE PIERDE LA PREGUNTA. El paso 1 no es indice de nada, es el marco del que cuelga todo el metodo (el propio resumen teorico dice empezar con el fin en mente, trabajando hacia atras desde la pregunta), y el paso 14, que sobrevive, apunta al PROBLEMA TECNICO ORIGINAL que solo el paso 1 establece. Por eso el indice son tres pasos y no cuatro. LA DISCREPANCIA DE CORTE, declarada y no cuadrada: el instrumento mecanico (docs/COSTURAS_INTERNAS.jsonl) pone el corte en el paso 11 y la lectura de la ficha lo pone en el 4. NO SE ELIGE UNO Y SE BORRA EL OTRO: el corte mecanico es donde la senal de bloque es maxima (y la pareja que la disparo son los pasos 14 y 16, los dos del final), y el corte leido es donde esta la juntura real. Esta operacion opera sobre el corte LEIDO, y el mecanico queda escrito al lado como lo que es, la senal que llevo a mirar. EL DATO QUE ESTA OPERACION HEREDA Y NO GASTA: la ficha deja dicho que este es el caso que hay que mirar primero cuando el barrido normalice la tasa de costura por longitud, porque es el unico nodo de mundo con costura confirmada y es un nodo largo. Esa medicion NO es de esta operacion ni de esta fase, y se deja nombrada para que no se pierda al cerrar el destejido.",
}


def main():
    escribir = "--escribir" in sys.argv

    filas = []
    with open(OPERACIONES, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))

    print("CONTROL 1, operaciones antes:", len(filas))
    assert len(filas) == 69, "no son 69 operaciones"
    ids = [o["id_op"] for o in filas]
    assert len(ids) == len(set(ids)), "ids repetidos antes de escribir"

    print("CONTROL 2, OP-D-08 / OP-D-09 ya existen?:",
          "OP-D-08" in ids, "/", "OP-D-09" in ids)
    assert "OP-D-08" not in ids and "OP-D-09" not in ids, "ya existian"

    ordenes = sorted(o["orden"] for o in filas if o["fase"] == "02_DESTEJIDOS")
    print("CONTROL 3, ordenes usados en 02_DESTEJIDOS:", ordenes)
    assert 8 not in ordenes and 9 not in ordenes, "los ordenes 8 o 9 estan ocupados"

    grafo = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
    for nueva in (OP_D_08, OP_D_09):
        nid = nueva["nodos"][0]
        assert nid in grafo, "el nodo no esta en el grafo: " + nid
        duenos = [o["id_op"] for o in filas if nid in (o.get("nodos") or [])]
        print("CONTROL 4,", nid, "| en el grafo: si | duenos previos:",
              duenos if duenos else "NINGUNO")
        assert not duenos, "ese nodo ya tiene dueno"

    # el esquema tiene que ser el mismo que el de las 69
    claves = list(filas[0].keys())
    for nueva in (OP_D_08, OP_D_09):
        assert list(nueva.keys()) == claves, (
            "el esquema no calza. esperado " + str(claves) + " y llego " + str(list(nueva.keys())))
    print("CONTROL 5, esquema identico al de las 69:", claves)

    texto = json.dumps([OP_D_08, OP_D_09], ensure_ascii=False)
    # los dos caracteres van por codigo a proposito: la regla de cero guiones largos
    # y medios vale tambien para el script que los busca
    largos = texto.count(chr(0x2014)) + texto.count(chr(0x2013))
    print("CONTROL 6, guiones largos o medios en lo nuevo:", largos)
    assert largos == 0, "hay guiones largos o medios"

    filas.append(OP_D_08)
    filas.append(OP_D_09)
    print("operaciones despues:", len(filas))

    if not escribir:
        print("SIMULACRO: no se escribio nada.")
        return

    with open(OPERACIONES, "a", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(OP_D_08, ensure_ascii=False) + "\n")
        fh.write(json.dumps(OP_D_09, ensure_ascii=False) + "\n")
    print("ANADIDAS AL FINAL de", OPERACIONES, "(las 69 viejas no se reescriben)")


if __name__ == "__main__":
    main()
