# -*- coding: utf-8 -*-
"""vuelta59_planes.py . EL GENERADOR DE LOS PLANES DE LOS LOTES DE UN TRAMO DE
OP-U-01: EL NUMERO DE TRAMO NO SE TALLA AQUI, LO DICE EL INSUMO QUE ENTRA POR
--tramo, QUE ES LO QUE EL PRINT DE TITULO YA HACIA.

SUCESOR DECLARADO de scripts/loop/vuelta57_planes.py, al que NO reemplaza. LA
ARITMETICA Y LAS GUARDAS SON LAS SUYAS, COPIADAS LITERALMENTE Y NO RETECLEADAS
(la extraccion del INCISO desde el nodo comparando sin tildes, la cobertura
exacta, la guarda 1B, los indices CUBIERTO comprobados contra el superviviente
real, la guarda de la juntura, y el campo declarados_y_no_fundidos que el
ejecutor exige).

LO QUE CAMBIA, declarado porque es lo unico que no es copia:

  1. EL CONTENIDO EDITORIAL, que es el fichero entero: los cincuenta actos del
     tramo 5 con su superviviente, su motivo y su reparto pieza a pieza. Eso no
     se hereda de ningun ancestro y por eso este generador SI lleva numero de
     vuelta en el nombre: lo que cambia no es una cifra, es el texto.
  2. EL TITULO NO TALLA EL TRAMO NI LA VUELTA, y esta es la correccion que la
     TAREA 1.1 de esta vuelta manda aplicar a los instrumentos que se corran:
     el numero de tramo se LEE de la clave del ordinal del propio fichero
     medido (orden_tramo5 dice tramo 5) y la vuelta entra por --vuelta. El
     ancestro tallaba "TRAMO 4 (vuelta 57)" en su print de titulo, que es
     ejemplar ROJO en scripts/loop/barrido_titulos_tallados.py.
  3. EL FICHERO DEL TRAMO y el prefijo del plan entran por argumento
     (--tramo, --prefijo), asi que el instrumento no puede quedarse apuntando
     a la nomina de otra vuelta.
  4. LA CABECERA YA NO TALLA EL TRAMO (correccion de la vuelta 60, TAREA 1.2 del
     encargo, y el texto viejo se queda escrito aqui porque una correccion que
     tapa lo que corrige no se puede auditar). LA CABECERA DECIA:

         EL GENERADOR DE LOS PLANES DE ESTA VUELTA PARA EL TRAMO 5 DE OP-U-01.

     El print de titulo SI estaba curado desde que este fichero nacio (punto 2
     de arriba), pero la CABECERA no, y el barrido de titulos tallados la caza
     como ROJO con todas sus letras: 'recibe el sujeto por --tramo y el titulo
     no se entera'. Lo cazo LA CORRIDA DEL AUDITOR de la vuelta 59, no una
     lectura. Se elige LA VIA DE REFORMULAR (no la del rotulo de procedencia)
     porque aqui el numero NO nombraba a un ancestro: nombraba al sujeto de
     hoy, que es justo lo que el argumento puede cambiar. LA ARITMETICA Y LAS
     GUARDAS NO SE TOCAN en esta correccion: solo el texto de la cabecera.

EL INCISO SE DECLARA EN ASCII y el generador BUSCA ESE TROZO EN EL PASO REAL
comparando las dos cadenas sin acentos, y EXTRAE LA SUBCADENA REAL, con sus
acentos, del fichero del nodo. El literal que va al plan sale SIEMPRE del nodo y
nunca de mis dedos. LA GUARDA NO SE AFLOJA: despues de extraer se comprueba
igual que el trozo esta LITERAL dentro del paso, y una casacion ambigua es rojo.

DE ESCRITURA SOLO SOBRE docs/loop/PLAN_V<N>_*.json. No toca ni un nodo.

Uso:
  python scripts/loop/vuelta59_planes.py --lote A --vuelta 59 [--simular]
"""
import argparse
import datetime
import io
import json
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop")

CABECERA = {
    "operacion": "OP-U-01",
    # LA FECHA SE MIDE, NO SE TECLEA (correccion de la vuelta 60, TAREA 1.1 del
    # encargo; motivo: LA CAIDA DE LA VUELTA 59 FUE LA FECHA). Este campo decia
    # "2026-08-21" tallado a mano y era FALSO: los seis commits de aquella vuelta
    # son del 2026-08-20 medido por git. EL PLAN YA SELLADO DEL LOTE A NO SE
    # REEDITA (lo prohibe el encargo) y su error se declara en el registro del
    # tramo cuando el tramo cierre; los planes que se sellen DE AQUI EN ADELANTE
    # llevan la fecha del reloj, que es la unica que no se puede suponer.
    "fecha": datetime.date.today().isoformat(),
    "estado": "SELLADO",
    "nomina": "docs/loop/RECOMPUTO_V59_APERTURA.jsonl, corrida ANTES de la primera operacion de la vuelta",
    "tramo_definido_en": "docs/loop/SALIDA_V58_TRAMO5_NOMINA.txt, con scripts/loop/vuelta58_tramo5_nomina.py. EL INSUMO ESTA MEDIDO Y FIJADO POR LA VUELTA 58 Y NO SE RE-MIDE (encargo de esta vuelta): 50 actos, puestos 27 a 76 de hoy y 200 a 249 en la nomina de la 48, todos PURO A y fusion pura, solape con el tramo 4 CERO, prefijo de 26 confirmado por las dos puntas y verificado por el auditor sobre nomina propia (acta 58, seccion 1).",
    "dossier": "docs/loop/SALIDA_V58_DOSSIER_TRAMO5.txt (P.5, el acto leido entero con su razon entera pegada, 1.979 lineas) mas docs/loop/SALIDA_V58_VARAS_TRAMO5.txt",
    "vara": "LOS 50 ACTOS DEL TRAMO 5 SON DE FUSION PURA (medido por la vuelta 58: tamano 2 y PURO A, 50 de 50): un acto de dos miembros con UN par A directo y ningun mixto. No hay lectura P.12 que hacer. El superviviente lo elige el CONTENIDO como P.8 lo define (pasos y condiciones, material propio y padre declarado EN LAS RAZONES); UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), y EL MATERIAL PROPIO DECLARADO DE UN SOLO LADO ES UNA VARA (acta 54, pregunta 4); si dos varas de contenido CHOCAN decide la pieza DECLARADA y si no hay ninguna se DECLARA y acumula para la mesa (acta 54, pregunta 2; acta 53, pregunta 3); si el contenido calla entero, EL CABLEADO DECIDE SOLO; si tambien empata, se DECLARA. Y LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO (acta 54, pregunta 1, registrada en 03_FUSIONES.md): en un acto de dos donde el unico candidato limpio es la puerta, LA PUERTA SOBREVIVE y el choque se registra en el motivo. LA RAMA DE LA CANTIDAD COMO VARA SIGUE NO ADOPTADA y no se usa en ningun acto de este plan (acta 58; encargo de esta vuelta).",
    "varas_impresas": "docs/loop/SALIDA_V58_VARAS_TRAMO5.txt, una fila por acto con pasos, condiciones y cableado contados por maquina y la FORMA del veredicto impresa: 22 de UNA SOLA VARA, 11 de TODAS DE ACUERDO, 7 de CONTENIDO EMPATA, 6 que CHOCAN y 4 de EMPATE SIN VARA. EL AUDITOR LO RE-DERIVO CON CODIGO PROPIO Y LAS 50 FILAS CALZAN AL DIGITO, DISTINTAS 0 (acta 58, seccion 2). Ninguna cifra de este plan esta tecleada. LA FORMA IMPRESA ES MEDICION DE LOS TRES CONTEOS Y NO ADJUDICACION: no conoce la pieza declarada, que por acta 54 pregunta 4 es tambien vara de contenido, y por eso un acto puede salir de la tabla como EMPATE SIN VARA y decidirse por la pieza declarada, o al reves.",
    "colisiones_esperadas": "docs/loop/SALIDA_V58_COLISIONES_ESPERADAS_TRAMO5.txt, medidas por la vuelta 58 ANTES de tocar un nodo sobre EL ARCHIVO ENTERO, por PAR RESUELTO: 100 combinaciones simuladas y CERO que fabriquen colision, con cualquiera de los dos supervivientes en cualquiera de los 50 actos. El censo esperado de cada lote es CERO y una colision real DETIENE.",
    "vara_de_las_puertas": "GUARDA 1B: ningun absorbido de este plan es semilla de entrada ni extremo de puente aprobado, comprobado por el generador y otra vez por el ejecutor. En el tramo 5 hay CUATRO actos con un miembro PUERTA (1, 9, 36 y 43, leidos del dossier): en tres de ellos la puerta es ademas el que el contenido elige y no hay choque; en el acto 1 la puerta NO es el que la razon declara y el choque se registra en el motivo por acta 54 pregunta 1.",
    "politica_del_reparto": "LA HEREDADA Y CITADA, no reinventada (acta 51 D3; acta 52 D5 y D10; acta 54 pregunta 5; acta 55 preguntas 3, 4 y 5; registros de las vueltas 53, 54, 55, 56 y 57): una pieza del absorbido cuyo unico contenido propio es un PARAMETRO CONCRETO de un gesto que el superviviente ya tiene va de INCISO ADOSADO cuando el paso resultante se lee limpio, y de CUBIERTO con la perdida NOMBRADA cuando no. Una pieza que es un GESTO DISTINTO va de APPEND, y una pieza mitad propia mitad ya dicha va de APPEND ENTERO con el solape declarado para la poda de la fase 04. CUANDO LA RAZON DECLARA COMPARTIDO UN GESTO QUE EL TEXTO NO DICE, PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3). LAS PERDIDAS DE CONDICIONES NO VAN DE APPEND POR DEFECTO: se NOMBRAN mientras el INCISO de condiciones no exista (acta 55, pregunta 5), y solo van de APPEND cuando la condicion es un DISPARADOR DISTINTO y no un matiz del que el superviviente ya tiene. El INCISO es siempre TROZO VERBATIM del paso que muere, y en este generador se EXTRAE del nodo en vez de teclearse.",
}


# --------------------------------------------------------------------------
# LOS LOTES, EN EL ORDEN IMPRESO DEL TRAMO (regla de trabajo del acta 54,
# punto 6): el lote recorre el tramo en su orden y aparta SOLO el acto con
# bloqueo declarado. Cada acto: ordinal del tramo, superviviente, motivo, y el
# reparto pieza a pieza. En INCISO el segundo campo es la SUBCADENA EN ASCII
# (el generador extrae del nodo la subcadena REAL con sus acentos) y el
# tercero el NEXO que la une al paso del superviviente.
# --------------------------------------------------------------------------
LOTES = {}

# LOS LOTES B Y C VIENEN DE FICHEROS DE CONTENIDO APARTE (vuelta 60): el lote A
# nacio dentro de este fichero y ahi se queda, porque moverlo seria reescribir un
# plan ya SELLADO y ejecutado. Los que faltan entran por import para que un
# cambio de TEXTO y un cambio de ARITMETICA no se pisen en el mismo diff.
try:
    from _v60_lote_b import LOTE_B
except ImportError:  # corrido desde otra carpeta
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from _v60_lote_b import LOTE_B
LOTES["B"] = LOTE_B
try:
    from _v60_lote_c import LOTE_C
except ImportError:
    from _v60_lote_c import LOTE_C
LOTES["C"] = LOTE_C

LOTES["A"] = {
    "titulo": "LOTE A DE LA VUELTA 59: LOS DIECISIETE PRIMEROS ACTOS DEL TRAMO EN SU ORDEN IMPRESO (1 a 17), apartando el 13 por EMPATE SIN VARA. Lo encabeza EL ACTO 1, que es el unico choque de puerta del lote: la razon declara superviviente a un nodo que la guarda 1B no permite absorber por el otro lado",
    "declarados": [
        {
            "orden": 13,
            "miembros": ["premio_shingo", "shingo_prize"],
            "especie": "EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN",
            "acumula_para": "LA MESA, dentro del pendiente de doctrina 1. LOS TRES CONTEOS EMPATAN AL DIGITO: pasos 4 contra 4, condiciones 2 contra 2 y cableado 2 contra 2 (cuadro de varas de la vuelta 58, fila 13, re-derivado por el auditor). Por acta 53 pregunta 4, el empate sin vara es cuando TODO empata, y aqui todo empata. LA RAZON DEL PUESTO 2475 DECLARA PROPIO A LOS DOS LADOS, que es la figura exacta del acto 32 del tramo 4 resuelta en esta misma campana: de premio_shingo declara DOS PASOS que el otro no tiene (documentar evidencia de implementacion de principios Lean, y usar el feedback de la evaluacion externa para planificar los proximos pasos); de shingo_prize declara la madurez CULTURAL Y OPERATIVA y la puerta de los criterios minimos. Que la razon llame LINEA a lo del segundo y PASOS a lo del primero es una comparacion de PESO entre dos propios declarados, y pesar dos propios declarados para romper un empate triple es EXACTAMENTE la rama que el acta 58 dejo NO ADOPTADA al deshacer el acto 32. SE DECLARA Y NO SE FUNDE. Y va marcado como DISCUTIBLE en el reporte, porque hay una lectura sostenible en contra: cuando la razon clasifica el propio de un lado como LINEA esta diciendo que no lo cuenta, y entonces el propio declarado seria de UN SOLO LADO y por acta 54 pregunta 4 seria vara. No la aplico porque decidirlo asi es estrenar doctrina sobre un empate, y deshacer una fusion cuesta una vuelta entera, como acaba de costarla el 32.",
        },
    ],
    "actos": [
        {
            "orden": 1,
            "superviviente": "programa_mejora_calidad_14_pasos",
            "motivo": "LA GUARDA RESTRINGE Y LA PUERTA SOBREVIVE, CON EL CHOQUE REGISTRADO, y el choque es de los que hay que decir con todas sus letras porque la razon declara lo contrario. La razon del puesto 2414 escribe SOBREVIVE programa_de_mejora_de_calidad y le reconoce TRES precisiones propias (medir la calidad en todas las areas incluidas las que no son de produccion, calcular el costo de la calidad con apoyo de quien lleve las cuentas, y entrenar a quienes coordinan equipos). PERO programa_mejora_calidad_14_pasos ES PUERTA (extremo de puente aprobado, leido del dossier), asi que absorberlo esta PROHIBIDO por la guarda 1B y el unico candidato limpio del acto es el. Por el acta 54, pregunta 1, registrada en 03_FUSIONES.md, LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO: aqui lo permitido es uno solo, LA PUERTA SOBREVIVE, y el choque se registra en vez de taparse. SE DICE ADEMAS QUE LOS CONTEOS TAMPOCO ACOMPANAN A LA RAZON: pasos 6 contra 7 apunta a la puerta, condiciones 3 contra 2 y cableado 13 contra 11 apuntan al otro, o sea que CHOCAN entre si (cuadro de varas, fila 1), y ni siquiera sin la guarda habria una vara de contenido limpia. Las tres precisiones declaradas NO SE PIERDEN: dos viajan en el APPEND del paso 3 y la tercera de INCISO al paso 7, y eso esta abajo pieza a pieza.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 4],
                "5": ["INCISO", 7, "a quienes coordinan equipos", ", entrenando "],
                "6": ["CUBIERTO", 7],
            },
            "condiciones": {
                "1": ["CUBIERTO", 1],
                "2": ["APPEND"],
                "3": ["CUBIERTO", 2],
            },
            "nota": "LAS DOS PRECISIONES DE MEDICION VIAJAN JUNTAS Y ENTERAS. El paso 3 del que muere (establecer medidas de calidad en todas las areas, incluidas las que no son de produccion, y calcular el costo de la calidad con apoyo de quien lleve tus numeros) es MITAD YA DICHA Y MITAD PROPIA: el paso 3 del superviviente dice definir como vas a medir la calidad y el costo de la no calidad, y ahi acaba. Va de APPEND ENTERO CON EL SOLAPE DECLARADO para la poda de la fase 04, que es la figura escrita para la pieza mitad y mitad, en vez de partirla en un inciso que dejaria fuera al que lleva las cuentas. LA TERCERA PRECISION, entrenar a quienes coordinan equipos, va de INCISO al paso 7 del superviviente, que es donde el ciclo se cierra con metas, causas y reconocimiento. Los pasos 1, 2, 4 y 6 del que muere estan dichos: el compromiso personal es el paso 1, el equipo por areas es el paso 2 (que ademas afina la escala, aunque sea de dos o tres personas), la conciencia mas la accion correctiva son los pasos 4 y 5, y el reconocimiento mas repetir el ciclo son el paso 7. PERDIDA NOMBRADA, UNA: crear un espacio de seguimiento de calidad, que el superviviente no tiene y que la razon no declara entre los propios; se nombra aqui para la fase 04 en vez de colarse de APPEND sin declararse.",
        },
        {
            "orden": 2,
            "superviviente": "sostener_las_ganancias",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 5 contra 5 y condiciones 2 contra 2: las dos varas de contenido empatan al digito. Y LA PIEZA DECLARADA TAMPOCO SEPARA, porque la razon del puesto 2417 dice REPITE POR FUSION MUTUA, NINGUNO DE LOS DOS DOMINA, y reconoce material propio a LOS DOS lados (de mantener_las_ganancias, los responsables de supervision y el disparador de la rotacion de personal; de sostener_las_ganancias, el mistake proofing, que la razon llama una CLASE DE CONTROL DISTINTA). Con el contenido callado entero, por P.8 EL CABLEADO DECIDE SOLO, y apunta a sostener_las_ganancias, 2 contra 3. NO ES EMPATE SIN VARA: el empate sin vara exige que TAMBIEN el cableado empate (acta 53, pregunta 4), y aqui no empata.",
            "pasos": {
                "1": ["CUBIERTO", 5],
                "2": ["CUBIERTO", 3],
                "3": ["INCISO", 4, "responsables de supervision que verifiquen el cumplimiento del control", ", con "],
                "4": ["CUBIERTO", 4],
                "5": ["APPEND"],
            },
            "condiciones": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
            },
            "nota": "LAS DOS PIEZAS PROPIAS DEL QUE MUERE SE REPONEN, CADA UNA POR SU FIGURA, y por eso este acto cierra con CERO perdidas nombradas pese a ser fusion mutua. Los responsables de supervision son un PARAMETRO del gesto de auditar que el superviviente ya tiene (auditar periodicamente que los controles se esten cumpliendo), asi que van de INCISO a su paso 4. El disparador de la rotacion de personal (revisar el sistema tras rotacion para asegurar continuidad) es un GESTO DISTINTO, no un matiz de auditar: el superviviente audita por calendario y esta pieza audita por evento, asi que va de APPEND. Los otros tres pasos estan dichos y se cotejan uno a uno: documentar el plan de control es su paso 5, el programa de entrenamiento para nuevos es su paso 3, y auditar que sigan vigentes es su paso 4. LAS DOS CONDICIONES ESTAN DICHAS a la letra: la sostenibilidad tras la mejora es su condicion 1 y el riesgo de rotacion es su condicion 2. EL MISTAKE PROOFING NO SE PIERDE PORQUE VIVE EN EL QUE SOBREVIVE: la razon lo nombra como perdida pensando en la direccion contraria de la fusion, y en esta direccion se queda en casa.",
        },
        {
            "orden": 3,
            "superviviente": "innovacion_tipo_ii",
            "motivo": "LA PIEZA DECLARADA GANA A LOS DOS CONTEOS DE CONTENIDO, que es la vara escrita para cuando las varas de contenido CHOCAN (acta 53, pregunta 3, y acta 54, pregunta 2, las dos en la cabecera de este plan). Los conteos apuntan a tipos_innovacion_i_ii: pasos 5 contra 6 y condiciones 2 contra 3. LA PIEZA DECLARADA APUNTA AL OTRO LADO Y LO HACE DE UN SOLO LADO, que por acta 54 pregunta 4 es vara no empatada: la razon del puesto 2420 escribe SOBREVIVE innovacion_tipo_ii y le reconoce DOS FILTROS que el otro no tiene (filtrar y transformar las ideas mas disruptivas en propuestas viables, que es un criterio de seleccion y no un refinamiento, y separar despues las de mayor potencial), mientras que del propio de tipos_innovacion_i_ii dice literalmente que ESO NO ANADE NADA, porque su paso de mas es el mismo ejercicio escrito mas suelto, un paso por columna en vez de un paso con las tres. EL CONTEO DE PASOS DE ESTE ACTO MIDE FORMATO Y NO SUSTANCIA, y la razon lo dice antes de que nadie lo mida. SE DEJA DICHO QUE ESTA ES LA FIGURA DEL TITULO QUE PROMETE LO QUE LOS PASOS NO DAN: el que muere se llama DOS TIPOS DE INNOVACION, TIPO I Y TIPO II, y sus seis pasos son solo el ejercicio del Tipo II.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
                "3": ["CUBIERTO", 2],
                "4": ["CUBIERTO", 2],
                "5": ["CUBIERTO", 3],
                "6": ["CUBIERTO", 4],
            },
            "condiciones": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
                "3": ["APPEND"],
            },
            "nota": "NINGUN PASO DEL QUE MUERE VIAJA ENTERO Y NINGUNO SE PIERDE, que es lo que un mismo ejercicio escrito mas suelto tiene que dar. Sus tres pasos de generacion (hacerlo mas grande, hacerlo mas pequeno, combinarlo con) son LAS TRES COLUMNAS del paso 2 del superviviente, que las nombra a las tres en una sola linea, asi que los tres van a CUBIERTO:2 y no hay nada que reponer. Identificar el producto a innovar es su paso 1; diferir la critica hasta terminar es su paso 3, que dice generar sin criticar durante la generacion; y refinar lo prometedor en propuestas viables es su paso 4. LA UNICA PIEZA QUE SI VIAJA ES UNA CONDICION, Y VIAJA PORQUE ES UN DISPARADOR DISTINTO Y NO UN MATIZ: cuando no se dispone de recursos para innovacion tipo I (revolucionaria) y se busca innovacion incremental efectiva. Es ademas EL UNICO SITIO DEL PAR DONDE EL TIPO I EXISTE, y perderla dejaria al superviviente sin decir nunca frente a que se elige el Tipo II. Las otras dos condiciones estan dichas: generar ideas para un nuevo producto o servicio es su condicion 1, y romper el bloqueo o los esquemas mentales limitantes es su condicion 2.",
        },
        {
            "orden": 4,
            "superviviente": "funcion_perdida_limites_especificacion",
            "motivo": "UNA SOLA VARA DE CONTENIDO NO EMPATADA, Y BASTA (acta 53, pregunta 4). Los pasos empatan 5 contra 5, pero las condiciones son 2 contra 1 a favor de funcion_perdida_limites_especificacion, y esa vara no empatada decide sola. EL CABLEADO APUNTA AL MISMO LADO (3 contra 2) aunque por P.8 no le toque hablar con el contenido ya decidido, y LA PIEZA DECLARADA TAMBIEN: la razon del puesto 2432 escribe SOBREVIVE funcion_perdida_limites_especificacion y le reconoce un paso operativo que el otro no cierra, ESTABLECER LOS LIMITES RESULTANTES ALREDEDOR DEL VALOR NOMINAL, que es donde se colocan; mientras que de funcion_perdida_taguchi dice que sus dos matices (el cliente PROMEDIO y el costo de fabrica USUALMENTE MENOR) son LINEA. Las tres varas de contenido apuntan al mismo sitio o callan: no hay choque que adjudicar.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 3],
                "3": ["INCISO", 3, "coeficiente k", ", el llamado "],
                "4": ["INCISO", 2, "usualmente menor", ", que es "],
                "5": ["CUBIERTO", 4],
            },
            "condiciones": {
                "1": ["CUBIERTO", 1],
            },
            "nota": "LOS DOS MATICES QUE LA RAZON LLAMA LINEA SE REPONEN LOS DOS, cada uno de INCISO al paso que lo alberga: que el costo de ajuste en fabrica sea usualmente menor va al paso 2 del superviviente, y el nombre COEFICIENTE K va al paso 3, que habla de la misma constante sin nombrarla asi. El de la k no es cosmetico: es el termino con el que este instrumento se busca en cualquier manual, y el superviviente decia solo LA CONSTANTE. El paso 2 del que muere (el punto de desviacion en que el cliente promedio reclamaria) esta dicho en el paso 3 del superviviente, que mide con LA DESVIACION PROMEDIO QUE GENERA QUEJAS DEL CLIENTE, o sea el mismo dato con el promedio dentro; y su paso 5 (despejar los limites igualando el costo de fabrica a la funcion de perdida) es el paso 4 del superviviente palabra por palabra en otro orden. PERDIDA NOMBRADA, UNA, Y ES DE NOMBRE, NO DE PASOS: el que muere es EL UNICO DEL PAR QUE DICE TAGUCHI, y la razon pide reponer ese nombre en el titulo o en la primera linea del superviviente. ESTA OPERACION NO PUEDE HACERLO Y SE DICE EN VEZ DE CALLARLO: el contrato del instrumento de fundir NO TOCA titulo_concepto ni ningun campo de redaccion, y TAGUCHI no aparece en ningun PASO del que muere, solo en su titulo y su entregable, asi que no hay trozo verbatim que mover por INCISO. Queda NOMBRADA para la fase 04, que es la que redacta.",
        },
        {
            "orden": 5,
            "superviviente": "enfermedades_mortales_gestion",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 4 contra 4 y condiciones 2 contra 2: las dos varas de contenido empatan al digito. Y LA PIEZA DECLARADA TAMPOCO SEPARA, porque la razon del puesto 2436 dice REPITE POR FUSION MUTUA y reparte propio a LOS DOS lados con el mismo peso, DOS LINEAS cada uno: de enfermedades_mortales_gestion, el impacto EN TUS NUMEROS y que el compromiso es de QUIEN DECIDE; de las_siete_enfermedades_mortales, el impacto EN LA CULTURA y el criterio de empezar por la que genera MAYOR DANO DE FONDO. Con el contenido callado entero, por P.8 EL CABLEADO DECIDE SOLO, y apunta a enfermedades_mortales_gestion, 5 contra 4. NO ES EMPATE SIN VARA porque el cableado no empata (acta 53, pregunta 4).",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 2, "en la cultura de tu negocio", ", y "],
                "3": ["INCISO", 3, "empezando por la que genera mayor dano de fondo", ", "],
                "4": ["CUBIERTO", 4],
            },
            "condiciones": {
                "1": ["APPEND"],
                "2": ["APPEND"],
            },
            "nota": "LAS DOS LINEAS PROPIAS DEL QUE MUERE SE REPONEN LAS DOS DE INCISO, y las dos caen en el paso que ya hace ese gesto: el impacto EN LA CULTURA se adosa al paso 2 del superviviente, que ya mide el impacto en tus numeros y en como trabajas dia a dia, de modo que el paso resultante mide las tres cosas; y el criterio de EMPEZAR POR LA QUE GENERA MAYOR DANO DE FONDO se adosa al paso 3, que elegia el orden segun tu situacion y no decia con que vara. Esa segunda es la mas util de las dos: el superviviente priorizaba sin criterio escrito. Sus otros dos pasos estan dichos: identificar cuales estan presentes es su paso 1, y saber que hace falta transformacion profunda y no parches es su paso 4, que ademas le pone dueno (comprometerte tu, quien decide). LAS DOS CONDICIONES VIAJAN ENTERAS Y SE DICE POR QUE, porque es la excepcion a que las condiciones no van de APPEND por defecto (acta 55, pregunta 5): las dos son DISPARADORES DISTINTOS y no matices de los que el superviviente ya tiene. El superviviente entra por diagnostico previo o por calidad baja constante pese a invertir; estas dos entran por RESISTENCIA CONSTANTE A MEJORAR y por QUE LOS 14 PUNTOS NO LOGRAN APLICARSE PESE A INTENTOS REPETIDOS, que es el fracaso de otro instrumento y no un sintoma de calidad. CERO perdidas nombradas.",
        },
        {
            "orden": 6,
            "superviviente": "eliminar_trabajo_a_destajo",
            "motivo": "UNA SOLA VARA DE CONTENIDO NO EMPATADA, Y BASTA (acta 53, pregunta 4). Los pasos empatan 4 contra 4 y las condiciones son 1 contra 2 a favor de eliminar_trabajo_a_destajo. EL CABLEADO APUNTA AL MISMO LADO (2 contra 3) y LA PIEZA DECLARADA TAMBIEN, de un solo lado: la razon del puesto 2437 escribe SOBREVIVE eliminar_trabajo_a_destajo y le reconoce DOS cosas que el otro no tiene y que son las dos mitades que faltan de la operacion, QUE PONER EN LUGAR DEL INCENTIVO (un modelo de capacitacion y supervision enfocado en calidad y no en velocidad) y CON QUE SE MIDE DESPUES (control estadistico de proceso para dar seguimiento objetivo sin presion de produccion); ademas de que sus dos primeros pasos son los del otro con mas precision. Ninguna vara apunta al otro lado: no hay choque.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 4],
            },
            "condiciones": {
                "1": ["CUBIERTO", 1],
            },
            "nota": "LA UNICA PIEZA PROPIA DEL QUE MUERE VIAJA ENTERA, y es la que la razon nombra como perdida si se cae: COMUNICAR EL CAMBIO DE ENFOQUE A LOS TRABAJADORES Y SINDICATOS. Va de APPEND y no de INCISO porque es un GESTO DISTINTO y no el parametro de ningun gesto que el superviviente tenga: el superviviente audita, redisena, capacita y mide, y en ningun paso ANUNCIA. La razon lo dice con estas palabras, que es EL UNICO PASO DEL PAR QUE SE OCUPA DE COMO SE ANUNCIA QUITARLE A ALGUIEN UNA FORMA DE COBRAR. Los otros tres estan dichos y con mas precision del lado que vive: auditar los esquemas de incentivo es su paso 1, que afina a identificar pago por pieza o metas de volumen QUE PENALICEN LA CALIDAD; redisenar para priorizar calidad sobre volumen es su paso 2, que afina a DESVINCULAR EL PAGO DE LA CANTIDAD DE PIEZAS; y monitorear el impacto en calidad es su paso 4, que ademas dice con que instrumento. La condicion unica del que muere (pago por pieza o bonos por volumen) es su condicion 1. CERO perdidas nombradas.",
        },
        {
            "orden": 7,
            "superviviente": "adaptaciones_sectoriales_iso",
            "motivo": "LA PIEZA DECLARADA GANA A UN CONTEO DE CONTENIDO (acta 53, pregunta 3). El unico conteo de contenido que no empata son las condiciones, 1 contra 2, y apunta a estandares_especificos_industria; los pasos empatan 4 contra 4 y EL CABLEADO TAMBIEN EMPATA, 1 contra 1, asi que ni siquiera puede desempatar por P.8. LA PIEZA DECLARADA ESTA DE UN SOLO LADO Y APUNTA AL OTRO, que es vara por acta 54 pregunta 4: la razon del puesto 2445 escribe SOBREVIVE adaptaciones_sectoriales_iso y le reconoce UN REQUISITO SUSTANTIVO que el otro no menciona, actualizar procesos y tecnologia para cumplir con EL CARACTER ACTUALIZADO que exigen regulaciones como cGMP, que es lo que significa la c de current en esa norma y lo que la distingue de una certificacion que se saca una vez; mientras que del propio de estandares_especificos_industria dice que es UNA LISTA DE EJEMPLOS mas ancha y QUE ESO ES LINEA. Un requisito sustantivo contra una lista de ejemplos declarada linea: la pieza declarada decide y el conteo de condiciones cede.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
                "3": ["CUBIERTO", 3],
                "4": ["INCISO", 4, "AS9100, cGMP, ISO 14000", ", por ejemplo "],
            },
            "condiciones": {
                "1": ["CUBIERTO", 1],
                "2": ["APPEND"],
            },
            "nota": "LA LISTA DE EJEMPLOS SE REPONE ENTERA DE INCISO, y es justo la pieza que la razon nombra como perdida: AS9100 e ISO 14000 son LAS DOS NORMAS SECTORIALES POR LAS QUE UN LECTOR DE OTRO RUBRO LLEGARIA, y el superviviente solo nombraba cGMP e ISO/TS 16949. El inciso va al paso 4, que es el que certifica, asi que el lector aeroespacial o ambiental encuentra su norma en el paso donde tiene que buscarla. Los otros tres pasos van uno a uno en el mismo orden: identificar la norma sectorial aplicable es su paso 1, comparar los requisitos suplementarios sobre la base ISO es su paso 2, y adaptar los procesos internos es su paso 3. LA CONDICION 2 VIAJA ENTERA POR SER DISPARADOR DISTINTO (cumplimiento regulatorio adicional mas alla del estandar generico), que no es el sector de la condicion 1 sino la exigencia. PERDIDA NOMBRADA, UNA, Y ES DE CONDICION: la condicion 1 del que muere nombra AEROESPACIAL Y DEFENSA entre los sectores y la del superviviente nombra farmaceutico, dispositivos medicos y automotriz. Va de CUBIERTO:1 con la perdida NOMBRADA y no de APPEND, porque es un MATIZ de la misma condicion y no un disparador distinto, y el INCISO de condiciones no existe (acta 55, pregunta 5). Los dos sectores quedan anotados aqui para la fase 04.",
        },
        {
            "orden": 8,
            "superviviente": "estilo_gerencial_ballet_vs_hockey",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 6 contra 4 y condiciones 4 contra 2, las dos a favor de estilo_gerencial_ballet_vs_hockey, y el cableado apunta al mismo lado (5 contra 3) aunque por P.8 no le toque hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO Y ES LA VARA MAS FUERTE: la razon del puesto 2447 escribe SOBREVIVE estilo_gerencial_ballet_vs_hockey y le reconoce UN PROTOCOLO COMPLETO que el otro no tiene (reunirse con los afectados en vez de imponer, presentar evidencia objetiva sin dramatismo ni urgencia artificial, dejar que el analisis conjunto llegue a la causa raiz antes de decidir, y acordar seguimiento regular) mas UNA METRICA PROPIA, medir la gestion por la cantidad de problemas QUE SE EVITAN y no solo por los que se resuelven, que la razon llama la unica forma del par de saber si el estilo cambio de verdad. Del otro dice que le quedan DOS LINEAS. Tercera aparicion de la firma del TITULO ESPEJO en el archivo tras el 2221 y el 2412, y aqui el espejo no confunde a ninguna vara.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["APPEND"],
                "3": ["CUBIERTO", 6],
                "4": ["APPEND"],
            },
            "condiciones": {
                "1": ["CUBIERTO", 2],
                "2": ["APPEND"],
            },
            "nota": "LAS DOS LINEAS QUE LA RAZON RECONOCE AL QUE MUERE VIAJAN ENTERAS, y las dos van de APPEND y no de INCISO por la misma razon: son GESTOS DISTINTOS y no parametros de ningun gesto del superviviente. Fomentar la comunicacion clara y coordinada ENTRE LOS NIVELES DE LA ORGANIZACION es estructura organizacional, y el protocolo del superviviente es de reunion por problema; y capacitar A LOS SUPERVISORES en tecnicas de comunicacion y coordinacion de equipo es formacion de un rol concreto, que el superviviente no menciona en ninguno de sus seis pasos. Sus otros dos pasos estan dichos: evaluar si el estilo actual detecta o previene es su paso 1 palabra por palabra, y sustituir practicas reactivas por preventivas es SU CONCLUSION, el paso 6, que la mide por los problemas evitados. LA CONDICION 2 VIAJA ENTERA POR SER DISPARADOR DISTINTO: los CONFLICTOS DE COMUNICACION ENTRE DEPARTAMENTOS que afectan la calidad no son ninguna de las cuatro del superviviente, que entran todas por crisis, por costo de correccion o por exigencia de prevenir. La condicion 1 esta dicha en su condicion 2 (dedicas mas tiempo y recursos a corregir errores que a prevenirlos). CERO perdidas nombradas.",
        },
        {
            "orden": 9,
            "superviviente": "roi_proyectos_calidad",
            "motivo": "UNA SOLA VARA DE CONTENIDO NO EMPATADA, Y BASTA (acta 53, pregunta 4), Y LA GUARDA PIDE LO MISMO, ASI QUE NO HAY CHOQUE QUE REGISTRAR. Los pasos son 4 contra 5 a favor de roi_proyectos_calidad y las condiciones empatan 2 contra 2, asi que hay una sola vara de contenido y no esta empatada. EL CABLEADO APUNTA AL MISMO LADO (2 contra 3) y LA PIEZA DECLARADA TAMBIEN, de un solo lado: la razon del puesto 2451 escribe SOBREVIVE roi_proyectos_calidad y le reconoce LO QUE EL OTRO NO CIERRA, LA FORMULA (calcular el ROI como la razon entre la ganancia estimada y los recursos necesarios, que el otro nombra sin definir) y REVISAR EL CALCULO CON LA PERSONA QUE AYUDA CON LAS FINANZAS ANTES DE DECIDIR. Y ESE MISMO NODO ES PUERTA (extremo de puente aprobado, leido del dossier), de modo que la guarda 1B y el contenido piden el mismo superviviente. SE DICE APARTE DEL ACTO 1 DE ESTE MISMO LOTE justamente porque aqui NO HAY CHOQUE, y confundir las dos figuras seria la mezcla que el acta 55 castigo.",
            "pasos": {
                "1": ["CUBIERTO", 3],
                "2": ["CUBIERTO", 4],
                "3": ["APPEND"],
                "4": ["APPEND"],
            },
            "condiciones": {
                "1": ["APPEND"],
                "2": ["APPEND"],
            },
            "nota": "ESTE ES EL ACTO DEL LOTE CON MAS PIEZAS QUE VIAJAN ENTERAS, Y CADA UNA TIENE SU MOTIVO ESCRITO EN LA RAZON. Los dos primeros pasos del que muere estan dichos: el costo de diagnostico y remedio es el paso 3 del superviviente, y comparar ese costo con el ahorro esperado es su paso 4, que es la formula misma. Los otros dos son las DOS PERDIDAS QUE LA RAZON NOMBRA y van de APPEND: DOCUMENTAR EL ROI PARA REPORTARLO A LA DIRECCION, que la razon distingue expresamente de calcularlo bien (el superviviente calcula y valida con quien lleva las finanzas, pero no reporta hacia arriba); y USAR CASOS DE EXITO PARA JUSTIFICAR LA INVERSION CONTINUA, que es la PERDIDA DE LINEA CON MOTIVO DE ALCANCE que la razon registra como segundo ejemplar de su clase tras el 2445, porque con ella se va EL BENCHMARK NOMBRADO, el Six Sigma de Samsung, y el superviviente no menciona ningun benchmark. LAS DOS CONDICIONES VIAJAN ENTERAS POR SER DISPARADORES DISTINTOS Y NO MATICES, y la diferencia es de momento: las del superviviente entran ANTES de lanzar (decidir si vale la pena lanzar un proyecto, comparar invertir en calidad contra otras opciones) y las dos del que muere entran DESPUES, con el programa ya andando (justificar financieramente LA CONTINUIDAD de un programa de mejora, y que LA DIRECCION SOLICITE evidencia cuantitativa). Un ROI que solo sabe entrar antes de empezar no sirve para defender lo que ya empezo. CERO perdidas nombradas.",
        },
        {
            "orden": 10,
            "superviviente": "teoria_triple_rol_sistemas_abiertos",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 4 contra 4 y condiciones 2 contra 2: las dos varas de contenido empatan al digito. LA PIEZA DECLARADA NO EMPATA Y APUNTA AL MISMO LADO QUE EL CABLEADO, asi que las dos concuerdan: la razon del puesto 2458 escribe SOBREVIVE teoria_triple_rol_sistemas_abiertos y le reconoce los mismos cuatro pasos PERO MAS AFINADOS EN LOS CUATRO (transacciones repetitivas en vez de relaciones; expectativas mutuas explicitas ENTRE CADA PAR DE ROLES, que es una regla de completitud sobre los tres pares y no un canal suelto; bucles PARA MEDIR CUMPLIMIENTO y no solo para existir; y evaluar el impacto EN TODAS LAS FUNCIONES INTERRELACIONADAS, que es la version accionable de evitar el cambio aislado), mientras que del propio de pensamiento_sistemico_rol_triple dice que es LA PARTICION POR DIRECCION Y QUE ESO ES LINEA. El cableado apunta a teoria_triple_rol_sistemas_abiertos, 2 contra 3. NO ES EMPATE SIN VARA porque el cableado no empata.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 2, "canales claros de comunicacion de requisitos entre proveedor y procesador", ", estableciendo "],
                "3": ["INCISO", 3, "entre cliente y procesador", ", "],
                "4": ["CUBIERTO", 4],
            },
            "condiciones": {
                "1": ["CUBIERTO", 1],
                "2": ["APPEND"],
            },
            "nota": "LA PARTICION POR DIRECCION SE REPONE ENTERA Y EN SUS DOS MITADES, que es lo que la razon nombra como la unica perdida del acto: los REQUISITOS BAJAN, del proveedor al procesador, y la RETROALIMENTACION SUBE, del cliente al procesador. Cada mitad va de INCISO al paso del superviviente que hace ese gesto sin decir la direccion: los canales de requisitos entre proveedor y procesador se adosan a su paso 2, que identificaba expectativas mutuas entre cada par de roles sin decir que baja por donde; y el entre cliente y procesador se adosa a su paso 3, que establecia bucles de retroalimentacion sin decir entre quienes. Los dos incisos juntos devuelven lo que la razon dice que se pierde, y ninguno anade nada que el nodo que muere no tuviera escrito. Sus otros dos pasos estan dichos y con mas precision del lado que vive: mapear las relaciones proveedor procesador cliente es su paso 1 (transacciones repetitivas en cada proceso clave), y evitar el cambio organizacional aislado es su paso 4. LA CONDICION 2 VIAJA ENTERA POR SER DISPARADOR DISTINTO, y es de los mas concretos del tramo: CUANDO UN CAMBIO ORGANIZACIONAL AISLADO YA GENERO MAS PROBLEMAS DE LOS QUE RESOLVIO. Las del superviviente entran por diagnostico de causa raiz o por querer un breakthrough; esta entra por el dano ya hecho, que es cuando de verdad se busca este nodo. La condicion 1 esta dicha en su condicion 1 (defectos o errores que cruzan multiples funciones). CERO perdidas nombradas.",
        },
        {
            "orden": 11,
            "superviviente": "descubrir_necesidades_del_cliente",
            "motivo": "LAS VARAS DE CONTENIDO CHOCAN Y DECIDE LA PIEZA DECLARADA (acta 53, pregunta 3). Los pasos son 3 contra 6 a favor de descubrir_necesidades_del_cliente y las condiciones 2 contra 1 a favor del otro: las dos varas de contenido chocan de frente, y el cableado (7 contra 6) tampoco puede hablar, porque por P.8 solo habla a contenido EMPATADO y este no empata, choca. LA PIEZA DECLARADA DECIDE Y ESTA ESCRITA: la razon del puesto 2461 dice SOBREVIVE descubrir_necesidades_del_cliente y le reconoce TRES COSAS que el otro no tiene, y las tres son de sustancia y no de forma: RECOPILAR EN EL LENGUAJE PROPIO DEL CLIENTE y despues TRADUCIR AL LENGUAJE TECNICO DE LA ORGANIZACION, que la razon subraya que son DOS PASOS Y NO UNO; e INVESTIGAR LOS USOS NO PREVISTOS DEL PRODUCTO Y SUS RIESGOS DE SEGURIDAD, que la razon llama LA UNICA LINEA DEL PAR QUE MIRA LO QUE EL CLIENTE HACE Y NADIE DISENO. Del otro lado la razon declara UNA pieza y la declara como PERDIDA NOMBRADA, no como titulo de supervivencia. NO SE DECIDE POR CANTIDAD DE PIEZAS DECLARADAS, que es la rama NO ADOPTADA: se decide porque de un lado la razon nombra los propios PARA SOSTENER AL NODO y del otro los nombra PARA QUE LA FUSION LOS REPONGA, que es la diferencia entre una vara y una lista de encargos.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 3, "por cada segmento de cliente", ", "],
                "3": ["INCISO", 5, "de forma consensuada, sin asumir jerarquias automaticas por tipo de cliente", ", "],
            },
            "condiciones": {
                "1": ["CUBIERTO", 1],
                "2": ["APPEND"],
            },
            "nota": "LA PERDIDA QUE LA RAZON NOMBRA SE REPONE DE INCISO Y ES LA PIEZA MAS IMPORTANTE DEL ACTO. El superviviente priorizaba (su paso 5, analizar y priorizar las necesidades identificadas) SIN DECIR CON QUE CRITERIO, y la razon lo dice con todas sus letras: sin esa advertencia LA PRIORIZACION SE RESUELVE SOLA POR TAMANO DE FACTURA. El inciso le adosa el criterio entero y verbatim, de forma consensuada y sin asumir jerarquias automaticas por tipo de cliente, que es exactamente lo que impide que el cliente grande mande. LA SEGMENTACION TAMBIEN SE REPONE: el paso 2 del que muere identificaba necesidades POR CADA SEGMENTO DE CLIENTE, y el paso 3 del superviviente distingue cuatro clases de necesidad (declaradas, reales, percibidas y culturales) sin decir sobre que poblacion; el inciso le pone la poblacion. Su paso 1 esta dicho: recolectar voz del cliente es el paso 1 del superviviente, que ademas planifica los metodos (encuestas, focus groups, quejas, visitas). LA CONDICION 2 VIAJA ENTERA POR SER DISPARADOR DISTINTO Y GRAVE: cuando existan REQUISITOS REGULATORIOS O TECNICOS QUE PUEDAN BLOQUEAR EL PROYECTO SI SE IGNORAN. El superviviente tiene una sola condicion y entra por querer entender a fondo al cliente; esta entra por riesgo de bloqueo, que es otra cosa, y perderla dejaria al nodo sin su unica alarma. CERO perdidas nombradas.",
        },
        {
            "orden": 12,
            "superviviente": "qfd_matriz",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 6 contra 4 y condiciones 4 contra 1, las dos a favor de qfd_matriz, y el cableado apunta al mismo lado (6 contra 1) aunque por P.8 no le toque hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO: la razon del puesto 2469 escribe SOBREVIVE qfd_matriz y le reconoce EL MECANISMO QUE HACE FUNCIONAR AL QFD Y QUE EL OTRO SOLO INSINUA, ENCADENAR MATRICES SUCESIVAS USANDO EL COMO DE UNA COMO EL QUE DE LA SIGUIENTE hasta llegar a los controles de proceso, mas la actualizacion continua para el analisis de brechas y la transferencia a operaciones; del otro dice que le queda UNA LINEA propia. SE REGISTRA LA FIGURA DE FAMILIA QUE LA RAZON DECLARA, sin que cambie el veredicto: spreadsheet_diseno_para_la_calidad era LA MADRE en el puesto 2425, donde su paso 3 era la linea que product_design_spreadsheet desplegaba, y aqui muere. Por 9.3 su direccion de entonces queda PROVISIONAL, como en accion_correctiva, los ROI y las adopciones ISO. Cuarta familia decidiendose de a dos.",
            "pasos": {
                "1": ["CUBIERTO", 2],
                "2": ["INCISO", 3, "en niveles de especificidad, de lo general a lo particular", ", desglosadas "],
                "3": ["CUBIERTO", 4],
                "4": ["CUBIERTO", 5],
            },
            "condiciones": {
                "1": ["CUBIERTO", 4],
            },
            "nota": "LA UNICA LINEA PROPIA DEL QUE MUERE SE REPONE DE INCISO Y CAE DONDE HACE FALTA. El paso 3 del superviviente lista las necesidades en vertical y los medios tecnicos en horizontal, pero no dice a que nivel de detalle se listan; el desglose de lo general a lo particular es justamente el parametro que falta, y adosado ahi el paso queda diciendo que las necesidades entran desglosadas en niveles de especificidad. Los otros tres pasos del que muere estan dichos uno a uno, como corresponde a un subconjunto: la hoja de necesidades del cliente listando clientes y prioridades es su paso 2 (identifica a tus clientes internos y externos y descubre sus necesidades); la hoja de diseno de producto que vincula cada necesidad con una caracteristica tecnica es su paso 4 (califica la relacion entre cada necesidad y cada medio dentro de la matriz); y extender el analisis a las hojas de diseno y control de proceso es su paso 5, que es el encadenamiento de matrices hasta los controles de proceso. Su condicion unica queda cubierta por la condicion 4 del superviviente, que dice traducir sistematicamente la voz del cliente en especificaciones tecnicas. CERO perdidas nombradas.",
        },
        {
            "orden": 14,
            "superviviente": "reinicio_programa_calidad",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 5 contra 3 y condiciones 3 contra 1, las dos a favor de reinicio_programa_calidad, y el cableado empata 3 contra 3, asi que no habla ni falta que hace. LA PIEZA DECLARADA APUNTA AL MISMO LADO Y ES DE UN SOLO LADO: la razon del puesto 2482 escribe SOBREVIVE reinicio_programa_calidad y le reconoce TRES cosas que el otro no tiene, ROTAR A LOS VETERANOS DEJANDO ALGUNO COMO PADRINO (que es como se conserva la memoria del ciclo anterior), RECONOCIMIENTO FORMAL a los lideres salientes, y la razon de fondo, USAR EL PROCESO COMO HERRAMIENTA DE DESARROLLO GERENCIAL, que explica por que se rota en vez de dejar al mismo equipo; y del otro dice, con estas palabras, que NO LE QUEDA NI UNA LINEA PROPIA. Es el caso mas limpio del lote: subconjunto estricto con las tres varas de acuerdo o calladas.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
                "3": ["CUBIERTO", 5],
            },
            "condiciones": {
                "1": ["CUBIERTO", 2],
            },
            "nota": "NINGUNA PIEZA VIAJA Y NINGUNA SE PIERDE, que es lo que un subconjunto estricto tiene que dar, y la razon lo predijo al escribir que al que muere no le queda ni una linea propia. Los tres pasos se cotejan uno a uno contra el superviviente: formar un nuevo equipo de representantes tras 12 a 18 meses es su paso 1 (al alcanzar las metas, formar un nuevo equipo de calidad con nuevo lider y coordinador) reforzado por su paso 5, que fija el ciclo aproximadamente cada dieciocho meses; conmemorar el aniversario del Dia de Cero Defectos es su paso 2, que programa la repeticion a lo largo de un ano completo con nuevas iniciativas y nombra el ZD Dia II; y reiniciar el ciclo de los catorce pasos con nuevos objetivos es su paso 5, que repite el ciclo completo. Su condicion unica (senales de estancamiento o perdida de impulso tras el primer ciclo) queda cubierta por la condicion 2 del superviviente, que dice si existe riesgo de que el programa se abandone tras el exito inicial. CERO perdidas nombradas.",
        },
        {
            "orden": 15,
            "superviviente": "eliminar_slogans_y_exhortaciones",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 4 contra 4 y condiciones 2 contra 2: las dos varas de contenido empatan al digito. Y LA PIEZA DECLARADA TAMPOCO SEPARA, porque la razon del puesto 2484 dice REPITE POR FUSION MUTUA, escribe que CADA UNO ANADE UNA LINEA, NINGUNO UN PROCEDIMIENTO, y las nombra a las dos: de eliminar_slogans_metas, UNA EXTENSION DE ALCANCE (trabajar con los proveedores de forma colaborativa, que lleva el punto 10 fuera de la empresa); de eliminar_slogans_y_exhortaciones, UN TEST DE QUE QUITAR (eliminar toda frase que pida mejorar sin venir acompanada de un metodo o plan concreto). Con el contenido callado entero, por P.8 EL CABLEADO DECIDE SOLO, y apunta a eliminar_slogans_y_exhortaciones, 2 contra 3. NO ES EMPATE SIN VARA porque el cableado no empata. LA ARISTA NO EXCULPA, y con este ya son 56 ejemplares.",
            "pasos": {
                "1": ["INCISO", 1, "y metas numericas que le exiges solo a quienes ejecutan el trabajo", ", "],
                "2": ["CUBIERTO", 3],
                "3": ["CUBIERTO", 4],
                "4": ["APPEND"],
            },
            "condiciones": {
                "1": ["CUBIERTO", 1],
                "2": ["APPEND"],
            },
            "nota": "LAS DOS PERDIDAS QUE LA RAZON NOMBRA SE REPONEN, CADA UNA POR SU FIGURA, y la eleccion de figura es distinta a proposito. EL TEST DE QUE QUITAR NO HAY QUE REPONERLO PORQUE VIVE EN EL QUE SOBREVIVE (es su paso 2, eliminar toda frase que pida mejorar sin venir acompanada de un metodo o plan concreto). EL OTRO CRITERIO, el del que muere, es un PARAMETRO del mismo gesto de revisar y va de INCISO a su paso 1: el superviviente revisaba carteles, lemas o mensajes motivacionales, y el inciso le anade LAS METAS NUMERICAS Y A QUIEN SE LE EXIGEN, solo a quienes ejecutan el trabajo, que es el criterio complementario del suyo, distinto y no repetido. LA EXTENSION DE ALCANCE VA DE APPEND porque es un GESTO DISTINTO y encima FUERA DE LA EMPRESA: trabajar con los proveedores de forma colaborativa en lugar de exigirles cambios abruptos sin apoyo no es un matiz de ningun paso del superviviente, que se queda entero puertas adentro. Sus otros dos pasos estan dichos: calcular que proporcion de los defectos viene del sistema y cual de las personas es su paso 3, y cambiar las exhortaciones por acciones concretas es su paso 4. LA CONDICION 2 VIAJA ENTERA POR SER DISPARADOR DISTINTO: responsabilizar a quien te ayuda por fallas que vienen de materiales o procesos deficientes es una situacion, y las del superviviente son el uso de carteles y el desanimo posterior. CERO perdidas nombradas.",
        },
        {
            "orden": 16,
            "superviviente": "rol_black_belt_six_sigma",
            "motivo": "UNA SOLA VARA DE CONTENIDO NO EMPATADA, Y BASTA (acta 53, pregunta 4). Los pasos empatan 4 contra 4 y las condiciones son 1 contra 2 a favor de rol_black_belt_six_sigma. EL CABLEADO APUNTA AL MISMO LADO (3 contra 5) aunque con el contenido ya decidido no le toque hablar. LA PIEZA DECLARADA NO SEPARA Y SE DICE: la razon del puesto 2498 escribe REPITE POR FUSION MUTUA, que los cuatro pasos van uno a uno y que CADA UNO ANADE SOLO LINEAS, NINGUNO UN PROCEDIMIENTO, dos por lado (de rol_black_belt, la certificacion ante un organismo reconocido del tipo ASQ y la coordinacion entre equipos; de rol_black_belt_six_sigma, la forma de la capacitacion en cuatro sesiones semanales con intervalos, y el umbral de retorno minimo por proyecto). Como la pieza declarada esta a los dos lados y con el mismo peso declarado, no es vara (acta 54, pregunta 4), y decide la unica vara de contenido que no empata, que es la de condiciones. CIFRAS PUBLICADAS CON SU CORTE, banco 9.21: los 250.000 dolares y las hasta seis semanas de entrenamiento son de Juran, no mediciones de este catalogo.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 4],
                "3": ["APPEND"],
                "4": ["APPEND"],
            },
            "condiciones": {
                "1": ["APPEND"],
            },
            "nota": "AQUI HAY UN AVISO DE LA RAZON QUE MANDA SOBRE EL REPARTO Y SE OBEDECE AL PIE: LOS DOS NODOS DAN DURACIONES DE CAPACITACION QUE NO CUADRAN, hasta seis semanas contra cuatro sesiones semanales, Y LA FUSION TIENE QUE RESOLVERLO, NO APILARLAS. Por eso el paso 1 del que muere (seleccionar candidatos para certificacion Black Belt, hasta 6 semanas de entrenamiento) va de CUBIERTO:1 A SECAS, sin inciso: su gesto, elegir a la persona, ya esta en el paso 1 del superviviente, y su parametro de duracion NO SE ADOSA porque adosarlo dejaria al nodo diciendo dos duraciones distintas en dos pasos, que es exactamente lo que el aviso prohibe. LA DURACION DE HASTA SEIS SEMANAS QUEDA NOMBRADA COMO PERDIDA, con su corte de Juran, y la que vive es la del superviviente, cuatro sesiones semanales con intervalos para aplicar lo aprendido, que la razon describe como practica espaciada y no como una duracion. VA MARCADO COMO DISCUTIBLE en el reporte: la razon lo dejo escrito como DISCUTIBLE PARA LA R55 y la eleccion entre las dos duraciones no la decide ninguna vara de la casa, solo la regla de no apilar. LAS OTRAS DOS PIEZAS PROPIAS VIAJAN ENTERAS DE APPEND por ser gestos distintos: la coordinacion entre equipos y analisis complejos es una definicion de responsabilidades que el superviviente no da, y CERTIFICAR COMPETENCIAS ANTE UN ORGANISMO RECONOCIDO COMO ASQ es una validacion externa que el superviviente no menciona, aunque su propio entregable habla de una persona CERTIFICADA sin decir por quien. El paso 2 del que muere (encargarle la seleccion y nominacion de proyectos) esta dicho en su paso 4. LA CONDICION VIAJA ENTERA POR SER DISPARADOR DISTINTO: institucionalizar breakthrough A GRAN ESCALA es una escala, y las dos del superviviente son la decision de implementar Six Sigma y la necesidad de liderazgo tecnico.",
        },
        {
            "orden": 17,
            "superviviente": "mapeo_flujo_valor",
            "motivo": "TODAS LAS VARAS DE CONTENIDO DE ACUERDO. Pasos 5 contra 4 y condiciones 4 contra 2, las dos a favor de mapeo_flujo_valor, y el cableado apunta al mismo lado (9 contra 7) aunque por P.8 no le toque hablar. LA PIEZA DECLARADA APUNTA TAMBIEN AL MISMO LADO Y ES LA VARA MAS FUERTE: la razon del puesto 2500 escribe SOBREVIVE mapeo_flujo_valor y le reconoce LO QUE DEFINE LA HERRAMIENTA Y EL OTRO NO TIENE EN NINGUN PASO, LA CLASIFICACION DE TRES CASILLAS (valor agregado, NO VALOR AGREGADO PERO NECESARIA, y desperdicio puro, donde la casilla del medio es la que evita cortar lo que sostiene el proceso), EL MAPA DEL ESTADO FUTURO (que la razon llama LA MITAD DEL METODO, y sin el solo hay una foto), y los MECANISMOS DE CONTROL para validar el avance contra ese mapa futuro.",
            "pasos": {
                "1": ["INCISO", 2, "el flujo actual de materiales e informacion en el proceso", ", y "],
                "2": ["APPEND"],
                "3": ["CUBIERTO", 3],
                "4": ["APPEND"],
            },
            "condiciones": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
            },
            "nota": "LA RAZON NOMBRA TRES PERDIDAS Y LAS TRES SE REPONEN, cada una por la figura que le toca, de modo que este acto cierra con CERO perdidas nombradas pese a ser el que mas traia. LA PRIMERA, EL FLUJO DE INFORMACION, que la razon llama LA OTRA MITAD DE UN VSM CANONICO porque el superviviente solo mapea materiales y tiempos, va de INCISO a su paso 2, que es el que documenta el estado actual; el paso resultante mapea tiempos de ciclo, esperas, inventarios, downtime y capacidad Y ADEMAS el flujo de materiales e informacion. LA SEGUNDA, EL COSTO POR ETAPA, viaja en el APPEND del paso 2 del que muere, que es MITAD YA DICHA Y MITAD PROPIA (el tiempo de ciclo ya esta en el paso 2 del superviviente, el costo por etapa no esta en ninguna parte): va de APPEND ENTERO CON EL SOLAPE DECLARADO para la poda de la fase 04, que es la figura escrita para la pieza mitad y mitad. LA TERCERA, LA PRIORIZACION DE LOS PROBLEMAS COMO PROYECTOS DE MEJORA, va de APPEND por ser gesto distinto: la razon dice que el superviviente PASA DIRECTO AL MAPA FUTURO SIN CARTERA, y sin ese paso el metodo salta del diagnostico al rediseno sin decidir en que orden se ataca. Su paso 3 esta dicho: identificar los puntos de desperdicio es el paso 3 del superviviente, que ademas los clasifica en las tres casillas. LAS DOS CONDICIONES ESTAN DICHAS: la visibilidad completa para identificar cuellos de botella es su condicion 1 y el inicio de un proyecto Lean es su condicion 2. COMPROBADO CONTRA EL TEXTO Y NO SUPUESTO, NO HAY PERDIDA DE NOMBRE: aunque muere el nodo con el id en ingles, el superviviente dice VALUE STREAM MAPPING en su paso 1, asi que la denominacion sigue siendo buscable.",
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
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def extraer_verbatim(texto, trozo_ascii):
    """Recibe el trozo escrito EN ASCII, lo casa contra el paso REAL comparando
    las dos cadenas sin tildes, y devuelve LA SUBCADENA REAL del paso, con sus
    acentos. Una extraccion ambigua no es una extraccion."""
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
    ap.add_argument("--vuelta", type=int, required=True)
    ap.add_argument("--tramo", default="docs/loop/TRAMO5_V58.jsonl")
    ap.add_argument("--prefijo", default=None,
                    help="prefijo del plan; por defecto PLAN_V<vuelta>_OPU01_LOTE_")
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    filas = cargar_jsonl(os.path.join(RAIZ, a.tramo.replace("/", os.sep)))
    claves = sorted({k for k in filas[0] if k.startswith("orden_tramo")}) if filas else []
    if len(claves) != 1:
        print("ROJO: el fichero del tramo tiene %d claves de ordinal (%s). PARADA."
              % (len(claves), claves))
        return 1
    ORD = claves[0]
    # EL NUMERO DE TRAMO SALE DEL FICHERO MEDIDO Y NO DE UNA CONSTANTE, que es la
    # correccion que la TAREA 1.1 de esta vuelta manda: orden_tramo5 dice tramo 5.
    m = re.search(r"(\d+)$", ORD)
    num_tramo = m.group(1) if m else "SIN NUMERO EN LA CLAVE %s" % ORD

    tramo = {r[ORD]: r for r in filas}
    prot = puertas()
    lote = LOTES[a.lote]
    prefijo = a.prefijo or ("PLAN_V%d_OPU01_LOTE_" % a.vuelta)

    print("=" * 78)
    print("GENERADOR DEL PLAN DEL LOTE %s DEL TRAMO %s (vuelta %d)"
          % (a.lote, num_tramo, a.vuelta))
    print("  fichero del tramo: %s" % a.tramo)
    print("=" * 78)
    print()

    fallos = []
    actos = []
    for spec in lote["actos"]:
        n = spec["orden"]
        if n not in tramo:
            fallos.append("acto %d: no esta en el tramo vivo %s" % (n, a.tramo))
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
            m2 = spec["pasos"].get(str(i))
            if not m2:
                fallos.append("acto %d: el paso %d de %s no tiene marca" % (n, i, ab))
                continue
            if m2[0] == "APPEND":
                marcas_p[str(i)] = "APPEND"
            elif m2[0] == "CUBIERTO":
                if not (1 <= m2[1] <= len(ps)):
                    fallos.append("acto %d: CUBIERTO:%d y el superviviente tiene %d pasos"
                                  % (n, m2[1], len(ps)))
                marcas_p[str(i)] = "CUBIERTO:%d" % m2[1]
            elif m2[0] == "CUBIERTO_COND":
                if not (1 <= m2[1] <= len(cs)):
                    fallos.append("acto %d: CUBIERTO_COND:%d y el superviviente tiene %d condiciones"
                                  % (n, m2[1], len(cs)))
                marcas_p[str(i)] = "CUBIERTO_COND:%d" % m2[1]
            elif m2[0] == "INCISO":
                _, k, ascii_trozo, nexo = m2
                trozo, motivo = extraer_verbatim(texto, ascii_trozo)
                if trozo is None:
                    fallos.append("acto %d, paso %d de %s: INCISO %r, %s"
                                  % (n, i, ab, ascii_trozo, motivo))
                    continue
                if trozo not in texto:
                    fallos.append("acto %d: el INCISO extraido %r NO es trozo verbatim del paso %d de %s"
                                  % (n, trozo, i, ab))
                if "|" in trozo or "|" in nexo:
                    fallos.append("acto %d: el INCISO o su nexo llevan la barra vertical, que es el separador de la marca" % n)
                if not (1 <= k <= len(ps)):
                    fallos.append("acto %d: INCISO al paso %d y el superviviente tiene %d"
                                  % (n, k, len(ps)))
                else:
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
                fallos.append("acto %d: marca desconocida %r" % (n, m2))
        for i, texto in enumerate(ca, 1):
            m2 = spec["condiciones"].get(str(i))
            if not m2:
                fallos.append("acto %d: la condicion %d de %s no tiene marca" % (n, i, ab))
                continue
            if m2[0] == "APPEND":
                marcas_c[str(i)] = "APPEND"
            elif m2[0] == "CUBIERTO":
                if not (1 <= m2[1] <= len(cs)):
                    fallos.append("acto %d: CUBIERTO:%d y el superviviente tiene %d condiciones"
                                  % (n, m2[1], len(cs)))
                marcas_c[str(i)] = "CUBIERTO:%d" % m2[1]
            else:
                fallos.append("acto %d: marca de condicion desconocida %r" % (n, m2))
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
                for m2 in marcas.values():
                    k = "APPEND" if m2 == "APPEND" else ("INCISO" if m2.startswith("INCISO") else "CUBIERTO")
                    c[k] += 1
                    tot[k] += 1
        print("     acto %-3d sobrevive %-46s piezas %2d (enteras %d, ya dichas %d, de INCISO %d)"
              % (x["orden"], x["superviviente"], sum(c.values()),
                 c["APPEND"], c["CUBIERTO"], c["INCISO"]))
    print("     TOTAL del lote %s: piezas %d (enteras %d, ya dichas %d, de INCISO %d)"
          % (a.lote, sum(tot.values()), tot["APPEND"], tot["CUBIERTO"], tot["INCISO"]))

    plan = dict(CABECERA)
    plan["vuelta"] = a.vuelta
    plan["tramo"] = "%s, %s" % (num_tramo, lote["titulo"])
    plan["actos"] = actos
    plan["declarados_y_no_fundidos"] = lote.get("declarados", [])
    destino = os.path.join(SALIDA, "%s%s.json" % (prefijo, a.lote))
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
