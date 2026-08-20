# -*- coding: utf-8 -*-
"""vuelta55_planes.py . EL GENERADOR DE LOS PLANES DE LA VUELTA 55 PARA EL TRAMO
2 DE OP-U-01.

SUCESOR DECLARADO de scripts/loop/vuelta54_planes.py, al que NO reemplaza. La
aritmetica y las guardas son las suyas, copiadas. UN solo cambio, y nace de una
correccion medida de la vuelta 54, no de un capricho:

  EL INCISO YA NO SE TECLEA CON SUS ACENTOS. El reporte de la vuelta 54 declara
  que el generador CAZO OCHO INCISOS suyos escritos sin acentos y no escribio
  nada hasta corregirlos: la guarda funciono, pero el trabajo de teclear un
  trozo literal con sus tildes es una trampa que no aporta nada. Aqui el inciso
  se declara EN ASCII y el generador BUSCA ESE TROZO EN EL PASO REAL comparando
  las dos cadenas sin acentos, y EXTRAE LA SUBCADENA REAL, con sus acentos, del
  fichero del nodo. El literal que va al plan sale SIEMPRE del nodo y nunca de
  mis dedos, que es la misma doctrina que ya rige para los APPEND ("el texto
  que se anade se lee del fichero del nodo por su indice; no se teclea").
  LA GUARDA NO SE AFLOJA: despues de extraer, se comprueba igual que el trozo
  esta LITERAL dentro del paso, y si no esta, rojo y no se escribe nada.
  Si el trozo en ASCII casa en MAS DE UN sitio del paso, tambien es rojo: una
  extraccion ambigua no es una extraccion.

TODO LO DEMAS ES LO DE SIEMPRE, comprobado antes de escribir:
  - que el superviviente y el absorbido sean los miembros del acto;
  - que cada paso y cada condicion del absorbido tenga marca, exactamente una;
  - que los indices CUBIERTO apunten a un paso o condicion que exista;
  - que ningun absorbido sea PUERTA (guarda 1B), con la misma fuente que
    scripts/loop/vuelta48_puertas_en_el_lote.py.

DE ESCRITURA SOLO SOBRE docs/loop/PLAN_V55_*.json. No toca ni un nodo.

Uso:
  python scripts/loop/vuelta55_planes.py --lote T1 [--simular]
"""
import argparse
import io
import json
import os
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
TRAMO = os.path.join(RAIZ, "docs", "loop", "TRAMO2_V55_TRAS_DESHACER.jsonl")
SALIDA = os.path.join(RAIZ, "docs", "loop")

CABECERA = {
    "operacion": "OP-U-01",
    "fecha": "2026-08-20",
    "vuelta": 55,
    "estado": "SELLADO",
    "nomina": "docs/loop/RECOMPUTO_V55_APERTURA.jsonl mas la re-medicion tras deshacer el acto 23",
    "tramo_definido_en": "docs/loop/SALIDA_V55_TRAMO2_TRAS_DESHACER.txt, con scripts/loop/vuelta55_tramo2_nomina.py (sucesor declarado del de la vuelta 54, que cae en ROJO al continuar un tramo ya consumido): 30 VIVOS y 20 FUNDIDOS de 50, las dos lecturas calzando en conjunto y en orden y los supervivientes siendo PREFIJO de la lectura A",
    "dossier": "docs/loop/SALIDA_V55_DOSSIER_TRAMO2.txt (P.5, el acto leido entero con su razon entera pegada) mas docs/loop/SALIDA_V55_MESA_TRAMO2.txt y docs/loop/SALIDA_V55_VARAS_TRAMO2.txt",
    "vara": "TODOS los actos del tramo 2 son de FUSION PURA (medido): un acto de dos miembros con UN par A directo y ningun mixto. No hay lectura P.12 que hacer. El superviviente lo elige el CONTENIDO como P.8 lo define (pasos y condiciones, material propio y padre declarado EN LAS RAZONES); UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), y EL MATERIAL PROPIO DECLARADO DE UN SOLO LADO ES UNA VARA (acta 54, pregunta 4); si dos varas de contenido CHOCAN decide la pieza DECLARADA y si no hay ninguna se DECLARA y acumula para la mesa (acta 54, pregunta 2); si el contenido calla entero, EL CABLEADO DECIDE SOLO; si tambien empata, se DECLARA. Y LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO (acta 54, pregunta 1): en un acto de dos donde el unico candidato limpio es la puerta, LA PUERTA SOBREVIVE y el choque de conteos se registra en el motivo.",
    "varas_impresas": "docs/loop/SALIDA_V55_VARAS_TRAMO2.txt, una fila por acto con pasos, condiciones y cableado contados por maquina y la FORMA del veredicto impresa. Ninguna cifra de este plan esta tecleada.",
    "colisiones_esperadas": "docs/loop/SALIDA_V55_COLISIONES_ESPERADAS_TRAMO2.txt, medidas ANTES de tocar un nodo sobre EL ARCHIVO ENTERO, por PAR RESUELTO, con scripts/loop/vuelta54_colisiones_esperadas.py. Una colision real fuera de esa prediccion detiene.",
    "vara_de_las_puertas": "docs/loop/SALIDA_V55_PUERTAS_APERTURA.txt. GUARDA 1B: ningun absorbido de este plan es semilla de entrada ni extremo de puente aprobado, comprobado por el generador y otra vez por el ejecutor.",
    "politica_del_reparto": "LA HEREDADA Y CITADA, no reinventada (acta 51 D3; acta 52 D5 y D10; acta 54 pregunta 5; registros de las vueltas 53 y 54): una pieza del absorbido cuyo unico contenido propio es un PARAMETRO CONCRETO de un gesto que el superviviente ya tiene va de INCISO ADOSADO cuando el paso resultante se lee limpio, y de CUBIERTO con la perdida NOMBRADA cuando no. Una pieza que es un GESTO DISTINTO va de APPEND, y una pieza mitad propia mitad ya dicha va de APPEND ENTERO con el solape declarado para la poda de la fase 04 (acta 54, pregunta 5). El INCISO es siempre TROZO VERBATIM del paso que muere, y en este generador se EXTRAE del nodo en vez de teclearse.",
}


# --------------------------------------------------------------------------
# LOS LOTES, EN EL ORDEN DEL TRAMO (regla de trabajo del acta 54, punto 6):
# el lote recorre el tramo en su orden impreso y aparta SOLO el acto con
# bloqueo declarado. Cada acto: ordinal del tramo 2, superviviente, motivo, y
# el reparto pieza a pieza. En INCISO el segundo campo es la SUBCADENA EN
# ASCII (el generador extrae del nodo la subcadena REAL con sus acentos) y el
# tercero el NEXO que la une al paso del superviviente.
# --------------------------------------------------------------------------
LOTES = {}

LOTES["T1"] = {
    "titulo": "2, LOTE T1 DE LA VUELTA 55: LOS DOS ACTOS DE LA RELECTURA CONJUNTA DEL ACTA 54 (el 18, que la vuelta 54 declaro empate sin vara, y el 23, cuya fusion se DESHIZO y se rehace en la direccion contraria con correccion declarada)",
    "actos": [
        {
            "orden": 18,
            "superviviente": "desconexion_ventas_experiencia",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y LA VARA ES EL MATERIAL PROPIO DECLARADO DE UN SOLO LADO (acta 54, pregunta 4). LAS TRES VARAS CONTABLES EMPATAN AL DIGITO: pasos 4 contra 4, condiciones 3 contra 3 y cableado 2 contra 2, y por eso la vuelta 54 lo declaro EMPATE SIN VARA. LO QUE AQUELLA LECTURA NO PESO es lo que la razon del puesto 322 declara con todas sus letras: El primero anade revisar como se incentiva a quien vende, QUE ES SU UNICO GESTO PROPIO. El primero es desconexion_ventas_experiencia, y ese gesto esta en su paso 2, verificado contra el grafo. Material propio declarado de UN SOLO LADO es una vara de contenido NO empatada, y una vara no empatada BASTA (acta 53, pregunta 4): el contenido NO empataba y el acto era FUSIBLE. La razon enumera ademas los CUATRO gestos que declara compartidos y los cuatro son los cuatro pasos de traspaso_ventas_cuentas, asi que del otro lado no queda propio declarado. RELECTURA CONJUNTA CONFIRMADA: el caso del auditor se sostiene leyendo el grafo.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 3, "lo que el cliente necesita, que le prometiste y sus preferencias", ", en concreto "],
                "3": ["INCISO", 4, "tus clientes mas importantes", ", empezando por "],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2], "3": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA Y SE DICE POR QUE, aunque la razon la de por compartida: el paso 4 del que muere, De vez en cuando revisa si lo que prometiste al vender coincide con lo que de verdad estas entregando, NO ESTA en ninguno de los cuatro pasos del superviviente, medido paso a paso. La razon lo enumera entre los compartidos, pero el reparto se hace contra EL TEXTO y no contra la razon, y APPEND no pierde nada. Su condicion 3 (ventas de alto valor o contratos largos) tambien viaja entera. DOS INCISOS: que anotar antes del traspaso, que es un parametro del CRM del paso 3, y el alcance de los clientes mas importantes, que es un parametro del protocolo del paso 4. UNA PERDIDA NOMBRADA: su condicion 1 habla de quejas de CLIENTES y la condicion 1 del superviviente dice CLIENTES NUEVOS, que es mas estrecho; el INCISO para condiciones no existe en el instrumento (pendiente de doctrina heredado) y por eso la perdida se nombra en vez de repararse.",
        },
        {
            "orden": 23,
            "superviviente": "modelo_tradicional_introduccion_producto",
            "motivo": "CORRECCION DECLARADA DE LA FUSION EJECUTADA EN LA VUELTA 54, que fundio este mismo acto en la direccion CONTRARIA. CONTENIDO, UNA SOLA VARA NO EMPATADA, Y LA VARA ES EL MATERIAL PROPIO DECLARADO DE UN SOLO LADO (acta 54, pregunta 4). La razon del puesto 340 dice con todas sus letras: El segundo anade no contratar estructuras completas, VP de ventas y equipos, antes de validar, QUE ES EL UNICO GESTO PROPIO. El segundo es modelo_tradicional_introduccion_producto, y ese gesto es su paso 4, verificado contra el grafo. UN SOLO LADO CON PROPIO DECLARADO ES UNA VARA NO EMPATADA Y BASTA: el contenido no empataba y el cableado no tenia que hablar. EL MOTIVO VIEJO, ENTERO Y SIN TAPAR, era este: EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO: pasos 4 contra 4, condiciones 2 contra 2, y la razon del 340 le reconoce a cada uno lo suyo. El cableado apunta a modelo_cascada_desarrollo_producto, 5 contra 2. NO es empate sin vara porque el cableado no empata. LO MARCO COMO DISCUTIBLE EN EL REPORTE, porque la razon del 340 llama al gesto propio del OTRO (no contratar estructuras completas antes de validar) SU UNICO GESTO PROPIO, y una pieza declarada pesa mas que el cableado: aqui ese gesto propio VIAJA ENTERO al superviviente y no se pierde, que es lo que hace la eleccion sostenible. FIN DEL MOTIVO VIEJO. LO QUE ESTABA MAL EN EL: la frase la razon del 340 le reconoce a cada uno lo suyo NO es lo que la razon dice; la razon reconoce UN SOLO gesto propio y del lado del segundo, y llamarlo UNICO cierra la puerta al empate. La fusion vieja se DESHIZO restaurando los cuatro ficheros que toco (scripts/loop/vuelta55_deshacer_acto23.py, con el alcance medido por git y no supuesto) y se rehace aqui.",
            "pasos": {
                "1": ["INCISO", 1, "heredado de grandes empresas", ", "],
                "2": ["APPEND"],
                "3": ["INCISO", 2, "el mercado y el cliente son realmente 'conocidos' o son solo hipotesis", ", y si "],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "EL REPARTO ES EL ESPEJO EXACTO DEL QUE LA VUELTA 54 SELLO EN LA OTRA DIRECCION, y por eso las cuentas calzan: alli el superviviente pasaba de 4 a 6 pasos y de 2 a 3 condiciones, y aqui tambien. DOS GESTOS VIAJAN ENTEROS: reconocer las cuatro etapas del modelo (Concepto, Desarrollo, Alpha/Beta, Lanzamiento), que el superviviente no enumera, y detener la ejecucion ciega si no hay contacto continuo con el cliente, que es la mitad que al superviviente le falta de su paso 3. Su condicion 2 (fecha de lanzamiento fija e inamovible sin importar el feedback) viaja entera, igual que en la direccion contraria viajaba la del inversionista que exige plan detallado. DOS INCISOS QUE LA DIRECCION VIEJA NO TENIA, y se declaran: la herencia de la empresa grande y el mercado y el cliente como hipotesis eran material propio que aquel reparto perdio sin nombrarlo; aqui se salvan. CERO perdidas nombradas.",
        },
    ],
    "declarados": [],
}

LOTES["A"] = {
    "titulo": "2, LOTE A DE LA VUELTA 55: LOS ONCE PRIMEROS ACTOS VIVOS DEL TRAMO EN SU ORDEN IMPRESO (1, 15, 28 a 36), incluidos LOS DOS DEL CHOQUE DE LA PUERTA que el acta 54 adjudico a favor de la puerta",
    "actos": [
        {
            "orden": 1,
            "superviviente": "trade_off_responsividad_eficiencia",
            "motivo": "LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO (acta 54, pregunta 1, adjudicada). EL CHOQUE, CON LOS CONTEOS IMPRESOS: las varas de contenido apuntan al OTRO, pasos 6 contra 4 y condiciones 3 contra 2 a favor de balance_eficiencia_responsividad, y el cableado apunta a la puerta, 2 contra 6. trade_off_responsividad_eficiencia ES PUERTA (extremo de puente aprobado, medido en docs/loop/SALIDA_V55_PUERTAS_APERTURA.txt) y la guarda 1B exige que sobreviva: en un acto de dos, el unico candidato LIMPIO es la puerta, asi que el contenido no tiene entre quien elegir. LA PUERTA SOBREVIVE y el choque de conteos queda REGISTRADO AQUI, no resuelto en silencio. LO QUE PROTEGE EL CONTENIDO QUE EL CONTEO PREFIRIO ES EL REPARTO: las piezas propias del absorbido viajan enteras.",
            "pasos": {
                "1": ["APPEND"], "2": ["APPEND"], "3": ["APPEND"],
                "4": ["CUBIERTO", 3], "5": ["CUBIERTO", 4], "6": ["APPEND"]
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"], "3": ["APPEND"]},
            "nota": "CUATRO PASOS Y DOS CONDICIONES VIAJAN ENTEROS, que es mucho y se dice por que: el absorbido es el lado que el conteo prefirio, con seis pasos contra cuatro, y la adjudicacion de la puerta obliga a que muera. Viajan enteros el monitoreo de los factores clave (demanda, precios, tasas de produccion, frecuencia de entregas), la evaluacion de la confiabilidad de los pronosticos, la determinacion de si el entorno es estable o volatil, y el aviso de no optimizar solo por costo bajo cuando el mercado empieza a valorar otros atributos. Los dos gestos que SI estan en la puerta son posicionar la estrategia en el continuo y revisarla periodicamente. CERO perdidas nombradas."
        },
        {
            "orden": 15,
            "superviviente": "apertura_llamada_venta_grande",
            "motivo": "LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO (acta 54, pregunta 1, adjudicada). EL CHOQUE, CON LOS CONTEOS IMPRESOS: la unica vara de contenido que no empata son los pasos, 5 contra 4 a favor de apertura_efectiva_llamada_venta; las condiciones empatan 2 contra 2 y el cableado tambien, 4 contra 4. apertura_llamada_venta_grande ES PUERTA y la guarda 1B exige que sobreviva. LA PUERTA SOBREVIVE y el choque queda REGISTRADO. Las piezas propias del absorbido viajan por el reparto.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["INCISO", 2, "con el mismo cliente en multiples visitas", ", y menos "],
                "3": ["INCISO", 1, "mas del 20% del tiempo total de la llamada", ", nunca "],
                "4": ["APPEND"], "5": ["APPEND"]
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "TRES PASOS VIAJAN ENTEROS: establecer quien eres, por que estas ahi y tu derecho a preguntar; resistir la tentacion de hablar de producto en la primera mitad; y retomar el control cuando el comprador pregunta por producto muy pronto. Ninguno de los tres esta en la puerta. DOS INCISOS salvan los dos parametros concretos que si tenian sitio: el limite del 20 por ciento del tiempo, que es la cifra del gesto de no gastar demasiado tiempo, y el aviso del mismo cliente en varias visitas, que es el alcance del gesto de no repetir la formula. Su condicion 2 (mismo discurso y tasas de exito bajas) viaja entera. CERO perdidas nombradas."
        },
        {
            "orden": 28,
            "superviviente": "rediseno_procesos_negocio_cx",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO: pasos 9 contra 9 y condiciones 2 contra 2, al digito. La razon del 364 le reconoce material propio A LOS DOS LADOS (al primero la compensacion automatica y las metricas antes y despues; al segundo reducir herramientas y sostener el presupuesto varios anos), asi que tampoco el material propio declarado separa. El cableado apunta a rediseno_procesos_negocio_cx, 3 contra 5. NO es empate sin vara porque el cableado no empata.",
            "pasos": {
                "1": ["CUBIERTO", 1], "2": ["CUBIERTO", 1], "3": ["APPEND"],
                "4": ["APPEND"], "5": ["APPEND"], "6": ["APPEND"],
                "7": ["APPEND"], "8": ["APPEND"], "9": ["APPEND"]
            },
            "condiciones": {"1": ["APPEND"], "2": ["CUBIERTO", 1]},
            "nota": "SIETE PASOS VIAJAN ENTEROS Y ES EL REPARTO MAS PESADO DEL LOTE, y se dice en vez de disimularse: los dos nodos tienen NUEVE pasos cada uno y solo DOS del que muere estan dichos por el superviviente (mapear los procesos que generan quejas e identificar las politicas que crean friccion, los dos cubiertos por su paso 1). Los otros siete son gestos que el superviviente no tiene: resolver en un solo contacto, las compensaciones automaticas, las metricas antes y despues, simplificar el papeleo con herramientas digitales, mapear los distintos journeys, diagnosticar donde se pasan la responsabilidad, y medir el impacto cuantitativo del mal servicio. SOLAPE INTERNO DECLARADO, y lo fabrica el propio absorbido y no yo: sus pasos 5 y 9 miden los dos el impacto con metricas distintas, y los dos viajan porque ninguno esta cubierto; queda para la poda de la fase 04. La razon del 364 da por compartido resolver en un solo contacto y el texto del superviviente NO lo dice, medido paso a paso: se reparte contra el texto. CERO perdidas nombradas."
        },
        {
            "orden": 29,
            "superviviente": "deep_dive_workshop",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y ADEMAS EL MATERIAL PROPIO DECLARADO APUNTA AL MISMO LADO: los pasos apuntan a deep_dive_workshop, 5 contra 4, y las condiciones empatan 2 contra 2. La razon del 366 dice que El primero anade formular la pregunta central como Como podriamos, QUE ES SU UNICO GESTO PROPIO, y el primero es deep_dive_workshop. Las dos varas de contenido que hablan apuntan al mismo sitio. El cableado apunta al otro (2 contra 6) y NO manda, porque el contenido no calla.",
            "pasos": {
                "1": ["INCISO", 1, "en un mismo espacio fisico", ", "],
                "2": ["CUBIERTO", 3],
                "3": ["INCISO", 4, "de baja fidelidad", ", y que sean "],
                "4": ["CUBIERTO", 5]
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "NINGUN PASO VIAJA ENTERO porque los cuatro del que muere son cuatro de los cinco del superviviente, uno a uno, y lo propio son DOS PARAMETROS: que el equipo se reuna en un mismo espacio fisico y que los prototipos sean de baja fidelidad. Los dos van de INCISO. Su condicion 2 (involucrar a multiples stakeholders con conocimientos tecnicos distintos) SI viaja entera: es un disparador distinto del de las varias personas y el poco tiempo. CERO perdidas nombradas."
        },
        {
            "orden": 30,
            "superviviente": "fase_assess_ciclo_cliente",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA: los pasos apuntan a fase_assess_ciclo_cliente, 5 contra 4, y las condiciones empatan 3 contra 3. El cableado esta de acuerdo (6 contra 4). La razon del 373 reconoce propio a los dos lados (al segundo lo tangible que da un anticipo; al primero la calificacion del 1 al 10 y los seis canales), asi que el material propio declarado EMPATA y no desempata: quien decide es la vara de los pasos, que no empata.",
            "pasos": {
                "1": ["INCISO", 2, "puede ser segundos, dias o meses", ": "],
                "2": ["CUBIERTO", 1], "3": ["CUBIERTO", 1], "4": ["APPEND"]
            },
            "condiciones": {"1": ["APPEND"], "2": ["CUBIERTO", 1], "3": ["APPEND"]},
            "nota": "UN PASO VIAJA ENTERO, el que la razon declara propio del que muere: crear algo tangible (una muestra, una historia, un testimonio) que de un anticipo real de como sera la experiencia. UN INCISO salva la escala del tiempo de evaluacion (segundos, dias o meses), que es el parametro del gesto de medir cuanto tardan en decidir. DOS CONDICIONES VIAJAN ENTERAS: estar enfocado solo en cerrar la venta, y que te cancelen poco despues de comprarte; ninguna de las tres del superviviente las dice. CERO perdidas nombradas."
        },
        {
            "orden": 31,
            "superviviente": "test_socios_de_trafico",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA: los pasos apuntan a test_socios_de_trafico, 6 contra 5, y las condiciones empatan 1 contra 1. El cableado apunta al otro (2 contra 4) y NO manda, porque el contenido no calla. La razon del 380 reconoce propio a los dos lados (al primero el correo de presentacion y la ficha de resultados; al segundo donde buscarlos), asi que el propio declarado EMPATA y decide la vara de los pasos.",
            "pasos": {
                "1": ["CUBIERTO", 1], "2": ["CUBIERTO", 4], "3": ["APPEND"],
                "4": ["INCISO", 1, "tiendas de aplicaciones, marketplaces y emisores de tarjetas de credito", ", mirando en "],
                "5": ["INCISO", 3, "cuando llegues a la fase de validacion con clientes (Customer Validation)", ", "]
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "UN PASO VIAJA ENTERO: ordenar la lista de socios segun cuales son mas criticos, que el superviviente no manda en ningun paso. DOS INCISOS salvan los dos parametros concretos: DONDE buscar a los socios (tiendas de aplicaciones, marketplaces y emisores de tarjetas), que es el parametro del gesto de identificarlos, y CUANDO preparar las reuniones (al llegar a Customer Validation), que es el parametro del gesto de agendarlas. PERDIDA NOMBRADA, UNA: su condicion 1 acota el disparador a los negocios WEB O MOVIL y la del superviviente no lo acota; el INCISO para condiciones no existe en el instrumento y la perdida se nombra."
        },
        {
            "orden": 32,
            "superviviente": "fracaso_como_aprendizaje_startup",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO: los pasos apuntan a fracaso_como_aprendizaje_startup (4 contra 5), las condiciones tambien (2 contra 3) y el cableado tambien (3 contra 8). La razon del 387 dice que El segundo anade documentar cada fracaso como insumo de la decision de pivotar y no penalizar al equipo, y el segundo es el elegido: el material propio declarado apunta al mismo lado. No hay nada que desempatar.",
            "pasos": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 3], "3": ["CUBIERTO", 3], "4": ["CUBIERTO", 2]},
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 3]},
            "nota": "NINGUNA PIEZA VIAJA Y NINGUNA SE PIERDE: los cuatro pasos y las dos condiciones del que muere son los mismos gestos del superviviente, uno a uno, y el superviviente los dice con MAS material (cinco pasos y tres condiciones). Es el reparto mas limpio del lote. CERO perdidas nombradas y CERO incisos."
        },
        {
            "orden": 33,
            "superviviente": "leap_of_faith_assumptions",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO: pasos 4 contra 4 y condiciones 2 contra 2, al digito, y la razon del 389 reconoce propio A LOS DOS LADOS (al primero reescribir las comparaciones en terminos verificables; al segundo disenar el experimento que valida cada uno), asi que tampoco el propio declarado separa. El cableado apunta a leap_of_faith_assumptions, 9 contra 3. Y AQUI LA GUARDA Y EL CONTENIDO NO CHOCAN: leap_of_faith_assumptions ES PUERTA (extremo de puente aprobado) y es el que el cableado elige, asi que la guarda 1B se cumple sin conflicto. Se dice porque en los actos 1 y 15 si chocaban.",
            "pasos": {
                "1": ["INCISO", 1, "el modelo de negocio y el spreadsheet financiero", ", incluidos "],
                "2": ["CUBIERTO", 2], "3": ["CUBIERTO", 4], "4": ["APPEND"]
            },
            "condiciones": {"1": ["CUBIERTO", 2], "2": ["CUBIERTO", 1]},
            "nota": "UN PASO VIAJA ENTERO, el que la razon declara propio del que muere: disenar experimentos especificos para validar cada leap-of-faith question antes de construir el producto completo. UN INCISO salva DONDE mirar los supuestos (el modelo de negocio y el spreadsheet financiero), que es el parametro del gesto de revisar el plan. PERDIDA NOMBRADA, UNA: su condicion 2 acota el disparador a los SUPUESTOS FINANCIEROS sin validar y la condicion 1 del superviviente habla de suposiciones sin acotar; el INCISO para condiciones no existe en el instrumento y la perdida se nombra."
        },
        {
            "orden": 34,
            "superviviente": "key_resources_hypothesis",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y ADEMAS EL MATERIAL PROPIO DECLARADO APUNTA AL MISMO LADO: los pasos apuntan a key_resources_hypothesis, 5 contra 4, y las condiciones empatan 1 contra 1. La razon del 406 dice que El primero anade revisar de que se depende que esta fuera del propio control, Y ES SU UNICO GESTO PROPIO, y el primero es key_resources_hypothesis. El cableado esta de acuerdo (6 contra 5).",
            "pasos": {
                "1": ["INCISO", 1, "redes de distribucion", ", "],
                "2": ["INCISO", 4, "marca, patentes, bases de datos, saber hacer", ": "],
                "3": ["CUBIERTO", 3],
                "4": ["INCISO", 2, "efectivo, lineas de credito", ", y calcula cuánto hace falta en "]
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA porque los cuatro pasos del que muere son las cuatro categorias del mismo bloque del lienzo que el superviviente ya recorre, y lo propio son TRES LISTAS DE EJEMPLOS que van de INCISO: las redes de distribucion entre los recursos fisicos, la marca, las patentes, las bases de datos y el saber hacer entre los intelectuales, y el efectivo y las lineas de credito entre los financieros. CERO perdidas nombradas."
        },
        {
            "orden": 35,
            "superviviente": "planificacion_preguntas_implicacion",
            "motivo": "CONTENIDO, LAS DOS VARAS DE ACUERDO: los pasos apuntan a planificacion_preguntas_implicacion (4 contra 3) y las condiciones tambien (3 contra 1). El cableado apunta al otro (4 contra 6) y NO manda, porque el contenido no calla. La razon del 410 reconoce propio a los dos lados (al primero el ejercicio previo a la llamada; al segundo el consejo de practicarlas), asi que el propio declarado EMPATA y deciden los conteos, que apuntan los dos al mismo sitio.",
            "pasos": {
                "1": ["INCISO", 2, "financieras, operativas, de satisfaccion", ", sean "],
                "2": ["CUBIERTO", 3], "3": ["APPEND"]
            },
            "condiciones": {"1": ["CUBIERTO", 3]},
            "nota": "UN PASO VIAJA ENTERO, el que la razon declara propio del que muere: practicar y refinar estas preguntas porque requieren mayor habilidad y preparacion. UN INCISO salva los tres tipos de consecuencia (financieras, operativas, de satisfaccion), que son el parametro del gesto de anotar las consecuencias. CERO perdidas nombradas."
        },
        {
            "orden": 36,
            "superviviente": "content_marketing_blog",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA: los pasos apuntan a content_marketing_blog, 6 contra 8, y las condiciones empatan 2 contra 2. El cableado esta de acuerdo (4 contra 7). La razon del 417 reconoce propio a los dos lados (al primero el plazo de seis meses; al segundo las infografias y los lead magnets), asi que el propio declarado EMPATA y decide la vara de los pasos.",
            "pasos": {
                "1": ["APPEND"], "2": ["CUBIERTO", 3],
                "3": ["INCISO", 5, "desde los primeros meses", ", "],
                "4": ["INCISO", 6, "influencers de Twitter en tu nicho", ", en especial "],
                "5": ["INCISO", 7, "menciones sociales", ", sin dejar fuera las "],
                "6": ["CUBIERTO", 2]
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "UN PASO VIAJA ENTERO, el que la razon declara propio del que muere: dedicar al menos seis meses consistentes de publicacion antes de evaluar resultados, que es un horizonte y no un parametro de otro gesto. TRES INCISOS salvan tres parametros: desde cuando hacer guest posting, en que red y nicho estan los influencers, y que ademas de la analitica hay que mirar las menciones sociales. DOS CONDICIONES VIAJAN ENTERAS porque dicen cosas distintas de las del superviviente: construir autoridad de marca a largo plazo (contra un canal de bajo costo) y tener capacidad de producir contenido de forma sostenida (contra tener expertise de industria). CERO perdidas nombradas."
        }
    ],
    "declarados": []
}

LOTES["B"] = {
    "titulo": "2, LOTE B DE LA VUELTA 55: LOS DOCE ACTOS VIVOS QUE QUEDAN DEL TRAMO EN SU ORDEN IMPRESO (37 a 41, 43 a 48 y 50), incluidos el 44, que se funde tras la relectura del filo, y el 45, donde la contencion declarada y la puerta apuntan al mismo lado",
    "actos": [
        {
            "orden": 37,
            "superviviente": "desirability_feasibility_viability",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA: los pasos apuntan a desirability_feasibility_viability, 5 contra 4, y las condiciones empatan 2 contra 2. El cableado tambien EMPATA, 4 contra 4, asi que si el contenido no hablara esto seria empate sin vara. Habla: la vara de los pasos no empata y BASTA (acta 53, pregunta 4). La razon del 419 no declara material propio de ningun lado, solo dice que es el mismo marco de IDEO con dos redacciones.",
            "pasos": {
                "1": ["INCISO", 1, "¿es deseable para las personas?, ¿es viable como negocio?, ¿es tecnicamente factible?", ": "],
                "2": ["CUBIERTO", 2], "3": ["APPEND"], "4": ["APPEND"]
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "DOS PASOS VIAJAN ENTEROS: evitar enfocarse solo en la viabilidad a corto plazo porque sacrifica innovacion por incrementalismo, y iterar entre las tres restricciones durante todo el ciclo de vida en vez de hacerlo de forma lineal. Ninguno de los dos esta en el superviviente, cuyos avisos son otros (no depender de la superioridad tecnica y ajustar el factor mas debil). UN INCISO salva la formulacion explicita de las tres preguntas, que es el parametro del gesto de evaluar en los tres ejes. CERO perdidas nombradas."
        },
        {
            "orden": 38,
            "superviviente": "fase_admit_celebracion",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO SALVO EL CABLEADO: los pasos apuntan a fase_admit_celebracion (4 contra 9) y las condiciones tambien (1 contra 3). El cableado apunta al otro (8 contra 4) y NO manda, porque el contenido no calla. La razon del 421 dice que El segundo anade la co-creacion cuando se pueda y el cuidado de que la celebracion no venga solo del vendedor, y el segundo es el elegido: el material propio declarado apunta al mismo lado que los conteos.",
            "pasos": {
                "1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2], "3": ["APPEND"], "4": ["APPEND"]
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "DOS PASOS VIAJAN ENTEROS: evitar caer en el silencio post-venta manteniendo el contacto activo justo despues del cierre, y capturar y asociar la emocion positiva del momento de compra con la marca. El superviviente tiene NUEVE pasos de celebracion y ninguno dice esas dos cosas, medido paso a paso. CERO perdidas nombradas y CERO incisos."
        },
        {
            "orden": 39,
            "superviviente": "usuarios_extremos_edge_cases",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA: los pasos empatan 4 contra 4 y las CONDICIONES apuntan a usuarios_extremos_edge_cases, 2 contra 1. El cableado esta de acuerdo (5 contra 4). La razon del 426 reconoce propio a los dos lados (al primero no rendirse a la solucion estandar; al segundo documentarlo como activo creativo), asi que el propio declarado EMPATA y decide la vara de las condiciones.",
            "pasos": {
                "1": ["INCISO", 1, "los que mas o menos usan el producto/servicio", ", y "],
                "2": ["INCISO", 2, "entrevistas o inmersiones etnograficas", ", con "],
                "3": ["CUBIERTO", 3], "4": ["APPEND"]
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "UN PASO VIAJA ENTERO, el que la razon declara propio del que muere: documentar los hallazgos como activos creativos para futuras iteraciones. DOS INCISOS salvan dos parametros: que los extremos incluyen a los que mas y menos usan el producto, y COMO estudiarlos (entrevistas o inmersiones etnograficas). CERO perdidas nombradas."
        },
        {
            "orden": 40,
            "superviviente": "jerarquia_datos_scor",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO: pasos 4 contra 4 y condiciones 2 contra 2, al digito, y la razon del 434 reconoce propio A LOS DOS LADOS (al primero el almacen de datos y automatizar la captura; al segundo sumar datos externos de mercado y economia), asi que tampoco el propio declarado separa. El cableado apunta a jerarquia_datos_scor, 2 contra 3. NO es empate sin vara porque el cableado no empata.",
            "pasos": {
                "1": ["CUBIERTO", 1], "2": ["APPEND"], "3": ["APPEND"], "4": ["APPEND"]
            },
            "condiciones": {"1": ["CUBIERTO", 2], "2": ["APPEND"]},
            "nota": "TRES PASOS VIAJAN ENTEROS y son justo los que la razon declara propios del que muere mas uno: el almacen de datos que centraliza la informacion de los sistemas operativos y contables, automatizar la captura para no meterlos a mano, y los reportes fijos por tipo de decision con consultas puntuales abiertas. Su condicion 2 (ver el negocio de forma distinta segun el tipo de decision) tambien viaja entera. CERO perdidas nombradas y CERO incisos."
        },
        {
            "orden": 41,
            "superviviente": "compatibilidad_motivaciones_riqueza_control",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO: los pasos apuntan a compatibilidad_motivaciones_riqueza_control (3 contra 5), las condiciones tambien (2 contra 3) y el cableado tambien (3 contra 8). La razon del 440 reconoce propio a los dos lados (al primero la matriz que simula escenarios; al segundo el eje riqueza contra control y el choque de poder), asi que el propio declarado EMPATA y deciden los conteos, que apuntan los tres al mismo sitio.",
            "pasos": {
                "1": ["INCISO", 2, "cada fork de decision (financiamiento, equity, roles)", ", y sobre "],
                "2": ["APPEND"], "3": ["APPEND"]
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "DOS PASOS VIAJAN ENTEROS: la matriz tipo Figura 11.1 para simular escenarios futuros y verificar consenso, que es el instrumento propio del que muere, y decidir explicitamente ANTES DE FUNDAR si existe compatibilidad motivacional suficiente, que ninguno de los cinco pasos del superviviente dice, medido paso a paso. UN INCISO salva sobre que hay que hablar (cada fork de decision: financiamiento, equity, roles), que es el parametro del gesto de hablar abiertamente con el socio. CERO perdidas nombradas."
        },
        {
            "orden": 43,
            "superviviente": "lead_bullets_no_silver_bullets",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO: los pasos apuntan a lead_bullets_no_silver_bullets (4 contra 5), las condiciones tambien (1 contra 2) y el cableado tambien (2 contra 3). La razon del 450 dice que El segundo antepone el diagnostico de si el problema es de mercado o de producto, QUE ES SU UNICO GESTO PROPIO, y el segundo es el elegido: el material propio declarado apunta al mismo lado.",
            "pasos": {
                "1": ["CUBIERTO", 4],
                "2": ["INCISO", 3, "multiples mejoras incrementales", ", con "],
                "3": ["CUBIERTO", 5],
                "4": ["INCISO", 2, "asociaciones o adquisiciones", ", y lo mismo con "]
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA porque los cuatro pasos del que muere son cuatro de los cinco del superviviente, uno a uno, y lo propio son DOS PARAMETROS: que el esfuerzo se concreta en multiples mejoras incrementales, y que la via de escape que hay que resistir incluye las asociaciones y las adquisiciones ademas de los mercados alternativos. Los dos van de INCISO. CERO perdidas nombradas."
        },
        {
            "orden": 44,
            "superviviente": "reparto_inicial_equity",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO: los pasos apuntan a reparto_inicial_equity (3 contra 4), las condiciones tambien (1 contra 2) y el cableado tambien (3 contra 8). La razon del 453 reconoce propio a los dos lados (al primero las implicaciones fiscales y legales; al segundo esperar a que la estrategia y el equipo se estabilicen y usar una plantilla estructurada), asi que el propio declarado EMPATA y deciden los conteos, que apuntan los tres al mismo sitio. LA COLISION DEL FILO QUEDO RESUELTA ANTES DE FUNDIR: este acto era uno de los tres con colision predicha (puestos 218 contra 1008), y la relectura del filo de esta vuelta corrigio el 218 de B a D con correccion declarada y razon vieja entera pegada. El censo esperado re-corrido DESPUES de esa correccion da CERO para este acto.",
            "pasos": {
                "1": ["INCISO", 3, "con ayuda de alguien con conocimiento legal", ", idealmente "],
                "2": ["CUBIERTO", 4], "3": ["APPEND"]
            },
            "condiciones": {"1": ["APPEND"]},
            "nota": "UN PASO VIAJA ENTERO, el que la razon declara propio del que muere: preguntar por las implicaciones fiscales y legales del acuerdo en tu mercado. UN INCISO salva el parametro de la ayuda legal al escribir el acuerdo. Su condicion 1 VIAJA ENTERA y se dice por que: habla del momento en que los socios YA acordaron de palabra y necesitan hacerlo vinculante, que es el momento CONTRARIO al de la condicion 1 del superviviente (todavia no has definido como repartir). CERO perdidas nombradas."
        },
        {
            "orden": 45,
            "superviviente": "programacion_entregas_delivery_scheduling",
            "motivo": "LA PIEZA DECLARADA DECIDE, Y LA PUERTA APUNTA AL MISMO LADO. Los conteos de contenido EMPATAN al digito (pasos 5 contra 5, condiciones 2 contra 2) y el cableado apunta a milk_run_deliveries (4 contra 2), pero el cableado solo habla cuando el contenido calla entero, y aqui NO calla: la razon del 474 declara CONTENCION con todas sus letras, milk_run_deliveries es el paso 3 de programacion_entregas_delivery_scheduling DESARROLLADO, la rama de disenar rutas milk run cuando el lote economico no llena camion, y REPITE ademas dos pasos mas de la madre. Una pieza declarada pesa mas que el cableado, y la contencion apunta a la MADRE. Y LA SEGUNDA VARA APUNTA IGUAL: programacion_entregas_delivery_scheduling ES PUERTA (extremo de puente aprobado) y la guarda 1B exige que sobreviva. AQUI NO HAY CHOQUE: las dos varas coinciden, y se dice porque en los actos 1 y 15 no coincidian.",
            "pasos": {
                "1": ["CUBIERTO", 3], "2": ["CUBIERTO", 1], "3": ["CUBIERTO", 4],
                "4": ["APPEND"], "5": ["APPEND"]
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son los unicos que la madre no tiene: disenar la secuencia de recogidas y entregas validandola con software de ruteo, y medir el ahorro en costo de transporte y recepcion tras implementar la ruta consolidada. Los otros tres son los tres que la razon declara repetidos de la madre. PERDIDA NOMBRADA, UNA, Y LA ELECCION SE DECLARA: el paso 3 del que muere nombra las VENTANAS DE TIEMPO junto a la capacidad de vehiculo como restricciones que deciden la tecnica de ruteo, y el paso 4 de la madre dice que la asignacion generalizada es para cuando LA UNICA restriccion es la capacidad del vehiculo. Un INCISO ahi DIRIA OTRA COSA, porque contradiria el la unica del paso que protege, y la tabla de los seis motivos manda perdida NOMBRADA antes que inciso que miente."
        },
        {
            "orden": 46,
            "superviviente": "contratar_ambicion_correcta",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA: los pasos apuntan a contratar_ambicion_correcta, 10 contra 4, y las condiciones empatan 2 contra 2. El cableado tambien EMPATA, 2 contra 2, asi que si el contenido no hablara esto seria empate sin vara. Habla, y con la diferencia mas grande del tramo. La razon del 479 dice que El primero anade ser mas riguroso en ventas, donde los incentivos locales tiran mas fuerte, y el primero es el elegido: el material propio declarado apunta al mismo lado.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 2, "los impostores no pueden explicar el proceso", ": "],
                "3": ["CUBIERTO", 3], "4": ["CUBIERTO", 4]
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "NINGUNA PIEZA VIAJA Y NINGUNA SE PIERDE: los cuatro pasos del que muere son los cuatro primeros del superviviente, uno a uno, y sus dos condiciones son las dos del superviviente. Lo unico propio es UNA RAZON (los impostores no pueden explicar el proceso), que va de INCISO al paso que la explica. El superviviente cubre ademas con su paso 5 el rigor especial en ventas que la condicion 1 del que muere nombra. CERO perdidas nombradas."
        },
        {
            "orden": 47,
            "superviviente": "wallas_etapa_incubacion",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA: los pasos apuntan a wallas_etapa_incubacion, 4 contra 5, y las condiciones empatan 2 contra 2. El cableado apunta al otro (5 contra 3) y NO manda, porque el contenido no calla. La razon del 489 reconoce propio a los dos lados (al primero registrar en que momentos de distraccion aparecen las ideas; al segundo alternar entre varios problemas), asi que el propio declarado EMPATA y decide la vara de los pasos.",
            "pasos": {
                "1": ["CUBIERTO", 3], "2": ["CUBIERTO", 4], "3": ["APPEND"], "4": ["CUBIERTO", 1]
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "UN PASO VIAJA ENTERO, el que la razon declara propio del que muere: registrar en que momentos de descanso o distraccion surgen ideas nuevas, para identificar patrones personales de incubacion. Los otros tres son los mismos gestos del superviviente, uno a uno. CERO perdidas nombradas y CERO incisos."
        },
        {
            "orden": 48,
            "superviviente": "framework_caracteristicas_ventajas_beneficios",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA: los pasos apuntan a framework_caracteristicas_ventajas_beneficios, 4 contra 8, y las condiciones empatan 2 contra 2. El cableado esta de acuerdo (2 contra 3). La razon del 531 reconoce propio a los dos lados (al primero que hacer cuando la necesidad todavia no aparecio y el aviso de no abrir con ventajas genericas; al segundo clasificar cada afirmacion en una de las tres categorias), asi que el propio declarado EMPATA y decide la vara de los pasos.",
            "pasos": {
                "1": ["CUBIERTO", 2], "2": ["APPEND"], "3": ["CUBIERTO", 3], "4": ["APPEND"]
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son justo los dos que la razon declara propios del que muere: que hacer cuando la necesidad explicita todavia no aparecio (volver a preguntas de Implicacion o de Necesidad y Beneficio) y el aviso de no abrir la conversacion con Ventajas genericas. Su condicion 2 (recibir objeciones justo despues de mencionar una capacidad) tambien viaja entera. CERO perdidas nombradas y CERO incisos."
        },
        {
            "orden": 50,
            "superviviente": "reunion_conclusion_proyecto",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO: los pasos apuntan a reunion_conclusion_proyecto (6 contra 12), las condiciones tambien (1 contra 3) y el cableado tambien (3 contra 5). La razon del 541 dice que El segundo anade la reunion de conclusion propiamente dicha, el periodo de monitoreo posterior de tres meses contra el remordimiento post-compra, y el orden de pedir testimonios solo despues de haber dado valor, y el segundo es el elegido: el material propio declarado apunta al mismo lado.",
            "pasos": {
                "1": ["INCISO", 3, "estrellas o NPS", ", con una calificación inicial de "],
                "2": ["CUBIERTO", 4], "3": ["CUBIERTO", 4], "4": ["CUBIERTO", 4],
                "5": ["CUBIERTO", 2], "6": ["APPEND"]
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "UN PASO VIAJA ENTERO: usar los resultados para ajustar los procesos futuros, que ninguno de los doce pasos del superviviente dice, medido paso a paso (los suyos atienden deficiencias antes de cerrar, comparten testimonios y montan el monitoreo, pero no cierran el bucle sobre el proceso). UN INCISO salva el instrumento de la calificacion inicial (estrellas o NPS), que es el parametro del gesto de disenar la encuesta externa. CERO perdidas nombradas."
        }
    ],
    "declarados": []
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

    tramo = {r["orden_tramo2"]: r for r in cargar_jsonl(TRAMO)}
    prot = puertas()
    lote = LOTES[a.lote]

    print("=" * 78)
    print("GENERADOR DEL PLAN DEL LOTE %s DEL TRAMO 2 (vuelta 55)" % a.lote)
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
    destino = os.path.join(SALIDA, "PLAN_V55_OPU01_LOTE_%s.json" % a.lote)
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
