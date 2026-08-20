# -*- coding: utf-8 -*-
"""vuelta56_planes.py . EL GENERADOR DE LOS PLANES DE LA VUELTA 56 PARA EL TRAMO
3 DE OP-U-01.

SUCESOR DECLARADO de scripts/loop/vuelta55_planes.py, al que NO reemplaza. LA
ARITMETICA Y LAS GUARDAS SON LAS SUYAS, COPIADAS LITERALMENTE (la extraccion
del INCISO desde el nodo comparando sin tildes, la cobertura exacta, la guarda
1B, los indices CUBIERTO comprobados contra el superviviente real). LO UNICO
QUE CAMBIA, y va declarado porque es lo unico que no es copia:

  1. EL FICHERO DEL TRAMO es docs/loop/TRAMO3_V56.jsonl.
  2. LA CLAVE DEL ORDINAL SE DESCUBRE DEL FICHERO en vez de estar escrita a
     mano ("orden_tramo2" alli, "orden_tramo3" aqui). Si hay ninguna o mas de
     una clave que empiece por "orden_tramo", es ROJO y PARA: un ordinal
     ambiguo no es un ordinal.
  3. EL PLAN SE ESCRIBE EN docs/loop/PLAN_V56_OPU01_LOTE_*.json.

EL INCISO SE DECLARA EN ASCII y el generador BUSCA ESE TROZO EN EL PASO REAL
comparando las dos cadenas sin acentos, y EXTRAE LA SUBCADENA REAL, con sus
acentos, del fichero del nodo. El literal que va al plan sale SIEMPRE del nodo
y nunca de mis dedos. LA GUARDA NO SE AFLOJA: despues de extraer se comprueba
igual que el trozo esta LITERAL dentro del paso, y una casacion ambigua es
rojo.

DE ESCRITURA SOLO SOBRE docs/loop/PLAN_V56_*.json. No toca ni un nodo.

Uso:
  python scripts/loop/vuelta56_planes.py --lote A [--simular]
"""
import argparse
import io
import json
import os
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
TRAMO = os.path.join(RAIZ, "docs", "loop", "TRAMO3_V56.jsonl")
SALIDA = os.path.join(RAIZ, "docs", "loop")

CABECERA = {
    "operacion": "OP-U-01",
    "fecha": "2026-08-20",
    "vuelta": 56,
    "estado": "SELLADO",
    "nomina": "docs/loop/RECOMPUTO_V56_APERTURA.jsonl, corrida ANTES de la primera operacion de la vuelta",
    "tramo_definido_en": "docs/loop/SALIDA_V56_TRAMO3_NOMINA.txt, con scripts/loop/vuelta56_tramo3_nomina.py (abridor del tramo 3, identidad POR MIEMBROS del sucesor de la 55 y ordinal del ABRIDOR de la 54). LAS DOS LECTURAS NO CALZAN Y LA DIVERGENCIA QUEDA EXPLICADA ENTERA: un CERRADO NACIDO DESPUES de la nomina de la 48 (construir_sobre_ideas_ajenas mas reglas_brainstorming, hoy puesto 23) entra en el corte y empuja al que ocupaba el puesto 150 de la 48 hasta el puesto 67 de hoy, DESPLAZADO al tramo siguiente y no perdido. El tramo se toma por la VARA VIGENTE, que es la LECTURA A: la nomina RE-MEDIDA AL ABRIRLO (03_FUSIONES.md, cabecera del registro del tramo 1, vuelta 48).",
    "dossier": "docs/loop/SALIDA_V56_DOSSIER_TRAMO3.txt (P.5, el acto leido entero con su razon entera pegada) mas docs/loop/SALIDA_V56_VARAS_TRAMO3.txt",
    "vara": "LOS 50 ACTOS DEL TRAMO 3 SON DE FUSION PURA (medido: tamano 2 y PURO A, 50 de 50): un acto de dos miembros con UN par A directo y ningun mixto. No hay lectura P.12 que hacer. El superviviente lo elige el CONTENIDO como P.8 lo define (pasos y condiciones, material propio y padre declarado EN LAS RAZONES); UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), y EL MATERIAL PROPIO DECLARADO DE UN SOLO LADO ES UNA VARA (acta 54, pregunta 4); si dos varas de contenido CHOCAN decide la pieza DECLARADA y si no hay ninguna se DECLARA y acumula para la mesa (acta 54, pregunta 2); si el contenido calla entero, EL CABLEADO DECIDE SOLO; si tambien empata, se DECLARA. Y LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO (acta 54, pregunta 1, registrada en 03_FUSIONES.md): en un acto de dos donde el unico candidato limpio es la puerta, LA PUERTA SOBREVIVE y el choque se registra en el motivo.",
    "varas_impresas": "docs/loop/SALIDA_V56_VARAS_TRAMO3.txt, una fila por acto con pasos, condiciones y cableado contados por maquina y la FORMA del veredicto impresa. Ninguna cifra de este plan esta tecleada.",
    "colisiones_esperadas": "docs/loop/SALIDA_V56_COLISIONES_ESPERADAS_TRAMO3.txt, medidas ANTES de tocar un nodo sobre EL ARCHIVO ENTERO, por PAR RESUELTO, con scripts/loop/vuelta56_colisiones_esperadas.py: 100 combinaciones simuladas y UNA SOLA que fabrica colision, el acto 15. Resuelta por relectura del filo ANTES de fundir (puesto 203 de C a D) y RE-MEDIDA en docs/loop/SALIDA_V56_COLISIONES_ESPERADAS_TRAS_FILO.txt, que baja de UNA a CERO. Una colision real fuera de esa prediccion detiene.",
    "vara_de_las_puertas": "GUARDA 1B: ningun absorbido de este plan es semilla de entrada ni extremo de puente aprobado, comprobado por el generador y otra vez por el ejecutor. La guarda de los CUATRO AJENOS se lee ademas POR EL RESOLUTOR en docs/loop/SALIDA_V56_TRAMO3_NOMINA.txt, y se declara lo que ese segundo camino destapa en el acto 7.",
    "politica_del_reparto": "LA HEREDADA Y CITADA, no reinventada (acta 51 D3; acta 52 D5 y D10; acta 54 pregunta 5; acta 55 preguntas 3, 4 y 5; registros de las vueltas 53, 54 y 55): una pieza del absorbido cuyo unico contenido propio es un PARAMETRO CONCRETO de un gesto que el superviviente ya tiene va de INCISO ADOSADO cuando el paso resultante se lee limpio, y de CUBIERTO con la perdida NOMBRADA cuando no. Una pieza que es un GESTO DISTINTO va de APPEND, y una pieza mitad propia mitad ya dicha va de APPEND ENTERO con el solape declarado para la poda de la fase 04. CUANDO LA RAZON DECLARA COMPARTIDO UN GESTO QUE EL TEXTO NO DICE, PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3). LAS PERDIDAS DE CONDICIONES NO VAN DE APPEND POR DEFECTO: se NOMBRAN mientras el INCISO de condiciones no exista (acta 55, pregunta 5). El INCISO es siempre TROZO VERBATIM del paso que muere, y en este generador se EXTRAE del nodo en vez de teclearse.",
}


# --------------------------------------------------------------------------
# LOS LOTES, EN EL ORDEN IMPRESO DEL TRAMO (regla de trabajo del acta 54,
# punto 6): el lote recorre el tramo en su orden y aparta SOLO el acto con
# bloqueo declarado. Cada acto: ordinal del tramo 3, superviviente, motivo, y
# el reparto pieza a pieza. En INCISO el segundo campo es la SUBCADENA EN
# ASCII (el generador extrae del nodo la subcadena REAL con sus acentos) y el
# tercero el NEXO que la une al paso del superviviente.
# --------------------------------------------------------------------------
LOTES = {}

LOTES["A"] = {
    "titulo": "3, LOTE A DE LA VUELTA 56: LOS DIECISIETE PRIMEROS ACTOS DEL TRAMO EN SU ORDEN IMPRESO (1 a 17), incluidos EL ACTO 7, que es el CERRADO nacido despues de la nomina de la 48 y el que la guarda de ajenos destapa por el resolutor, y LOS DOS DEL CHOQUE DE LA PUERTA (el 8 por cableado)",
    "actos": [
        {
            "orden": 1,
            "superviviente": "economia_de_la_experiencia",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 5 contra 3 a favor de economia_de_la_experiencia; condiciones 2 contra 2, empatadas. UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice porque apuntaba al OTRO (5 contra 3): el cableado solo decide cuando el contenido calla ENTERO, y aqui no calla. La razon del puesto 558 reconoce material propio a los DOS lados (el primero anade mirar marcas de experiencia como ejemplo; el segundo anade cuidar la ejecucion del detalle y iterar el diseno de la experiencia con el mismo rigor que la ingenieria del producto), asi que la vara del propio declarado EMPATA y no desempata: la que decide es la de los pasos.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
                "3": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: mirar ejemplos de marcas de experiencia (Whole Foods, Virgin America) para inspirar el diseno propio. Los otros dos pasos son los dos primeros movimientos del superviviente dichos con otras palabras. Las dos condiciones quedan cubiertas: la generica o puramente funcional por la de cumple su funcion pero no logra diferenciarse, y la de diferenciacion de marca mediante la experiencia por la de elevar la oferta al nivel de experiencia. CERO perdidas nombradas.",
        },
        {
            "orden": 2,
            "superviviente": "evaluacion_vp_ventas",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 6 contra 6 y condiciones 2 contra 2: las dos varas de contenido empatan al digito, y la razon del puesto 561 reconoce material propio a los DOS lados (el primero anade los procesos tecnicos de venta, benchmarking, POC y demos; el segundo anade pedir referencias de su equipo actual), asi que tampoco la pieza declarada desempata. Con el contenido callado entero, EL CABLEADO DECIDE SOLO y apunta a evaluacion_vp_ventas, 4 contra 2. NO ES EMPATE SIN VARA, y se dice por que: el empate sin vara exige que TAMBIEN el cableado empate (acta 53, pregunta 4), y aqui no empata.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["INCISO", 3, "ejemplos de contrataciones que salieron mal", ", pidiendole "],
                "3": ["CUBIERTO", 1],
                "4": ["APPEND"],
                "5": ["APPEND"],
                "6": ["CUBIERTO", 5],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "TRES PASOS VIAJAN ENTEROS: presentar su empresa actual como prueba de que sabe articular una vision, pedir referencias de su equipo actual (que es el propio declarado del que muere) y el bloque de compensacion, incentivos y conflictos de canal. ESE TERCERO SE DICE APARTE porque la razon lo da por compartido y EL TEXTO NO LO DICE: el paso 6 del superviviente habla de marketing y de conflictos de canal, y NO de planes de compensacion ni de incentivos por resultados, medido paso a paso. PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3), y APPEND no pierde nada. UN INCISO: los ejemplos de contrataciones que salieron mal, que es un parametro concreto del paso 3 del superviviente. Su condicion 2 (hacer crecer el equipo comercial que vende a otras empresas) viaja entera porque es un disparador distinto del suyo. CERO perdidas nombradas.",
        },
        {
            "orden": 3,
            "superviviente": "plan_a_b_c_soft_landing",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO. Pasos 5 contra 4 y condiciones 3 contra 1, las dos a favor de plan_a_b_c_soft_landing; el cableado apunta al mismo lado (4 contra 3) y se dice que coincide, aunque por P.8 no le tocaba hablar. La razon del puesto 562 reconoce propio a los dos lados (el primero detalla el Plan C como cierre ordenado; el segundo anade avisar al prestamista en cuanto el desempeno se desvia y averiguar como te esta clasificando), asi que esa vara empata y las que deciden son las contables.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["APPEND"],
                "3": ["CUBIERTO", 1],
                "4": ["CUBIERTO", 2],
            },
            "condiciones": {"1": ["CUBIERTO", 3]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son los dos que la razon declara propios del que muere: avisar al prestamista apenas el desempeno se desvia del plan, y revisar como te esta calificando el prestamista en este momento. Los otros dos son los planes A, B y C armados con los inversionistas, que el superviviente despliega en sus pasos 1, 2 y 4, y el trabajo profesional con prestamista e inversionistas para capital, venta o venta de activos, que es su paso 2. Su unica condicion queda cubierta por la condicion 3 del superviviente, que nombra la deuda de venture debt y el riesgo de incumplimiento con las mismas palabras. CERO perdidas nombradas.",
        },
        {
            "orden": 4,
            "superviviente": "publicidad_offline_pruebas_locales",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO, Y ADEMAS ES LA MADRE DECLARADA. Pasos 9 contra 4 y condiciones 2 contra 1, las dos a favor de publicidad_offline_pruebas_locales; el cableado empata (3 contra 3) y por eso no habria decidido nada aunque le tocara. Y LA PIEZA DECLARADA APUNTA AL MISMO LADO: la razon del puesto 568 escribe que tracking_publicidad_offline ES EL PASO 3 DE publicidad_offline_pruebas_locales DESARROLLADO, y que lo unico suyo es la pregunta de como se entero de nosotros en el formulario. Madre e hijo con el hijo declarado: la madre sobrevive.",
            "pasos": {
                "1": ["CUBIERTO", 3],
                "2": ["INCISO", 3, "un codigo de descuento distinto para cada canal", ", y "],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 4],
            },
            "condiciones": {"1": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara como lo unico propio del hijo: la pregunta de como se entero de nosotros en el formulario de registro o compra. UN INCISO: el codigo de descuento distinto POR CANAL, que es un parametro concreto del paso 3 del superviviente, que habla de codigo unico o direccion web POR CAMPANA. Su condicion viaja entera porque es un disparador distinto (correr varias campanas offline a la vez y necesitar saber cual funciona) y ninguna de las dos del superviviente lo dice. CERO perdidas nombradas.",
        },
        {
            "orden": 5,
            "superviviente": "desarrollo_presentacion_problema",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y LA PUERTA APUNTA AL MISMO LADO. Pasos 6 contra 5 a favor de desarrollo_presentacion_problema y condiciones 1 contra 1, empatadas: una sola vara de contenido no empatada BASTA. Y LA SEGUNDA VARA APUNTA IGUAL: desarrollo_presentacion_problema ES PUERTA (extremo de puente aprobado) y la guarda 1B exige que sobreviva. AQUI NO HAY CHOQUE: las dos varas coinciden, y se dice porque en el acto 8 de este mismo lote no coinciden. La razon del puesto 570 declara que la madre RE-DESARROLLA al mismo grano que el hijo y que lo propio de cada uno es poco.",
            "pasos": {
                "1": ["CUBIERTO", 2],
                "2": ["INCISO", 3, "preguntar como las rankean", ", y "],
                "3": ["INCISO", 4, "sin entrar en features", ", "],
                "4": ["CUBIERTO", 4],
                "5": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "UNA PIEZA VIAJA ENTERA: preguntar como se compara la solucion propuesta con las soluciones actuales, que es un gesto que ninguno de los seis pasos del superviviente dice, medido paso a paso. DOS INCISOS, y los dos son lo que la razon declara propio del hijo o parametro de un gesto ya dicho: el ranking explicito de las soluciones actuales, que se adosa al paso 3 del superviviente (preguntar como resuelve hoy el problema), y el sin entrar en features, que se adosa al paso 4 (presentar la solucion al final). UNA PERDIDA NOMBRADA: su condicion 1 pide validar el problema Y la reaccion inicial a la solucion EN UNA MISMA SESION DE ENTREVISTA, y la condicion 1 del superviviente solo habla de validar si el problema es real y urgente antes de mostrar el producto; el INCISO para condiciones no existe en el instrumento (pendiente de doctrina heredado) y por eso la perdida se nombra en vez de repararse.",
        },
        {
            "orden": 6,
            "superviviente": "gamificacion_onboarding_visual",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 5 contra 5 y condiciones 1 contra 1: las dos varas de contenido empatan al digito, y la razon del puesto 571 reconoce propio a los DOS lados (la version gamificada nombra el rompecabezas y el evento final como recuerdo tangible; la de progreso manda dosificar la informacion), asi que tampoco la pieza declarada desempata. Con el contenido callado entero, EL CABLEADO DECIDE SOLO y apunta a gamificacion_onboarding_visual, 4 contra 2. NO es empate sin vara porque el cableado no empata.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["CUBIERTO", 2],
                "3": ["APPEND"],
                "4": ["APPEND"],
                "5": ["CUBIERTO", 5],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son exactamente la dosificacion de la informacion que la razon declara como lo unico que se perderia: enviar solo la informacion necesaria para el paso actual sin saturar, y anticipar el siguiente paso en cada comunicacion para generar expectativa. Los otros tres son los mismos movimientos del superviviente. UNA PERDIDA NOMBRADA: su condicion 1 anade que el proceso PUEDE GENERAR ANSIEDAD EN EL CLIENTE y la condicion 1 del superviviente habla de proceso tecnico, largo o con usuarios sin experiencia previa, que no es lo mismo; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra.",
        },
        {
            "orden": 7,
            "superviviente": "reglas_brainstorming",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO, Y ADEMAS ES LA MADRE DECLARADA Y LA PUERTA. Pasos 7 contra 3 y condiciones 4 contra 1, las dos a favor de reglas_brainstorming, y el cableado apunta al mismo lado (26 contra 4). LA PIEZA DECLARADA APUNTA IGUAL: la razon del puesto 586 (brainstorming_efectivo contra construir_sobre_ideas_ajenas, que hoy resuelve a reglas_brainstorming contra construir_sobre_ideas_ajenas) escribe que construir_sobre_ideas_ajenas ES EL PASO 2 DE LA MADRE DESARROLLADO y que lo unico que se perderia es la no atribucion. Y LA TERCERA VARA APUNTA IGUAL: reglas_brainstorming ES PUERTA y la guarda 1B exige que sobreviva. LAS TRES COINCIDEN. LO QUE ESTE ACTO TIENE DE PARTICULAR Y SE DECLARA EN VEZ DE CALLARSE, con las dos cosas medidas hoy: PRIMERA, ES UN CERRADO NACIDO DESPUES DE LA NOMINA DE LA VUELTA 48 (alli era la componente 62, ABIERTA y de tamano 3, y se partio cuando la vuelta 49 corrigio el veredicto del puesto 844 de A a D), asi que su puesto de la 48 dice nuevo. SEGUNDA, LA GUARDA DE LOS CUATRO AJENOS MUERDE POR EL RESOLUTOR Y NO POR EL CAMINO LITERAL: brainstorming_divergente, uno de los cuatro que 03_FUSIONES.md declara fuera de OP-U-01 para siempre, esta DEPRECADO y vive hoy dentro del ids_alias de reglas_brainstorming. SE FUNDE IGUAL, Y LA VARA VA ESCRITA: la propia pagina midio esa guarda sobre las COMPONENTES el 19 ago 2026 (vuelta 48) y escribio que ab_testing_optimizacion y brainstorming_divergente ya no aparecen en ninguna componente porque sus operaciones corrieron y los deprecaron; por esa vara escrita la guarda esta VERDE hoy tambien. Y ademas esta fusion NO TOCA AL AJENO por ningun lado: el nodo que lleva su alias es el que SOBREVIVE, el que muere es construir_sobre_ideas_ajenas, y ni el id ni el alias ni la clase del ajeno cambian. Por la marca operativa registrada esta misma vuelta (acta 55, pregunta 1), una reserva que una vara escrita resuelve es MATIZ y no bloquea. VA MARCADO COMO DISCUTIBLE EN EL REPORTE.",
            "pasos": {
                "1": ["CUBIERTO", 3],
                "2": ["INCISO", 3, "sesiones de construccion colectiva ('yes, and...')", ", en "],
                "3": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon del puesto 586 declara como lo unico que se perderia: evitar atribuir ideas exclusivamente a una sola persona para promover su evolucion. UN INCISO: el nombre de la tecnica, las sesiones de construccion colectiva del tipo yes, and, que es un parametro concreto del paso 3 del superviviente, donde ya esta la regla de construir sobre las ideas de otros por encima de generar ideas propias de forma aislada. Su condicion queda cubierta por la condicion 1 del superviviente. CERO perdidas nombradas.",
        },
        {
            "orden": 8,
            "superviviente": "five_whys_inversion_proporcional",
            "motivo": "LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO (acta 54, pregunta 1, registrada en 03_FUSIONES.md), Y AQUI EL CONTENIDO NO TIENE ENTRE QUIEN ELEGIR. five_whys_inversion_proporcional ES PUERTA (extremo de puente aprobado) y la guarda 1B exige que sobreviva: es el UNICO candidato limpio del acto. EL CHOQUE SE REGISTRA CON SUS CIFRAS, y esta vez NO es de contenido sino de CABLEADO: pasos 5 contra 5 y condiciones 3 contra 3, o sea el contenido EMPATA ENTERO, y el cableado, que es quien decidiria con el contenido callado, apunta al OTRO, 5 contra 10. Se dice asi en vez de llamarlo choque de conteos de contenido, que es lo que fueron los actos 1 y 15 del tramo 2. LA RAZON DEL PUESTO 590 APUNTA ADEMAS AL SUPERVIVIENTE POR CONTENIDO: escribe que five_whys_inversion_proporcional trae los cinco niveles, la inversion proporcional al dano, la separacion entre causa tecnica y humana y el no culpar a personas, QUE ES LO QUE tecnica_cinco_porques DICE ENTERO.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["CUBIERTO", 1],
                "3": ["CUBIERTO", 1],
                "4": ["APPEND"],
                "5": ["CUBIERTO", 2],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 3], "3": ["APPEND"]},
            "nota": "DOS PASOS VIAJAN ENTEROS Y SE DICE POR QUE, aunque la razon los de por compartidos: reunir a todas las personas involucradas en el descubrimiento, diagnostico y resolucion del fallo, e identificar en cada nivel si la causa es tecnica o humana u organizacional. NINGUNO DE LOS CINCO PASOS DEL SUPERVIVIENTE LOS DICE, medido paso a paso: su paso 4 dice evitar culpar a individuos y enfocar el analisis en procesos y sistemas, que no es lo mismo que clasificar la causa nivel por nivel. PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3), y APPEND no pierde nada. Su condicion 3 (balancear velocidad de ejecucion con calidad de forma incremental) tambien viaja entera por ser un disparador distinto. UNA PERDIDA NOMBRADA: su condicion 1 incluye UN RESULTADO DE NEGOCIO INESPERADO junto al fallo tecnico o de proceso, y la condicion 1 del superviviente solo habla de error o falla tecnica u operativa repetible; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra.",
        },
        {
            "orden": 9,
            "superviviente": "fase_accomplish_experiencia_cliente",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO. Pasos 10 contra 4 y condiciones 3 contra 1, las dos a favor de fase_accomplish_experiencia_cliente; el cableado apunta al mismo lado (9 contra 7) y se dice que coincide, aunque por P.8 no le tocaba hablar. La razon del puesto 595 reconoce propio a los dos lados (el primero manda recoger evidencia y testimonios; el segundo clasifica en tres escenarios y reserva el cinco por ciento de las ganancias) y ademas escribe que ese cinco por ciento ES LO MAS CONCRETO DEL PAR: esa pieza vive en el superviviente y por ahi tambien apunta.",
            "pasos": {
                "1": ["INCISO", 1, "no solo la entrega del producto", ", y "],
                "2": ["CUBIERTO", 2],
                "3": ["CUBIERTO", 4],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: recoger evidencia, testimonios y datos del resultado logrado para usos futuros. UN INCISO: el no solo la entrega del producto, que es el matiz que separa el resultado deseado de la entrega y que el paso 1 del superviviente no dice. Los otros dos pasos son el sistema de seguimiento y la celebracion, que el superviviente ya tiene en sus pasos 2 y 4. Su unica condicion queda cubierta. CERO perdidas nombradas.",
        },
        {
            "orden": 10,
            "superviviente": "acquisicion_viral_engineering",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO, Y ADEMAS LA PIEZA DECLARADA APUNTA IGUAL. Pasos 6 contra 5 y condiciones 2 contra 1, las dos a favor de acquisicion_viral_engineering; el cableado apunta al mismo lado (6 contra 1). La razon del puesto 596 escribe que herramientas_adquisicion_viral CABE ENTERO DENTRO de acquisicion_viral_engineering y que lo unico propio del largo es su paso 1, identificar QUE TIPO de efecto de red aplica: el propio declarado esta del lado del que sobrevive y del otro lado no hay ninguno.",
            "pasos": {
                "1": ["CUBIERTO", 2],
                "2": ["CUBIERTO", 4],
                "3": ["CUBIERTO", 3],
                "4": ["INCISO", 6, "videos o demostraciones", ", como "],
                "5": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 2]},
            "nota": "UNA PIEZA VIAJA ENTERA Y SE DICE POR QUE, aunque la razon la de por compartida: animar a los primeros clientes a que lo promuevan activamente NO ESTA en ninguno de los seis pasos del superviviente, medido paso a paso; su paso 5 habla de RECOMPENSAS para quienes refieran, que es otra cosa. PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3), y APPEND no pierde nada. UN INCISO: los formatos del contenido compartible (videos o demostraciones), que es un parametro concreto del paso 6 del superviviente, que habla de sitios y blogs. CERO perdidas nombradas.",
        },
        {
            "orden": 11,
            "superviviente": "ficcion_especulativa_como_metodo",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 5 contra 5, empatados, y condiciones 3 contra 2 a favor de ficcion_especulativa_como_metodo: una sola vara de contenido no empatada BASTA (acta 53, pregunta 4), asi que el cableado NO habla, y se dice que apuntaba al mismo lado (5 contra 4). Y LA PIEZA DECLARADA APUNTA IGUAL: la razon del puesto 602 nombra TRES cosas que se perderian si el superviviente se escribe mal, el plazo, los tres personajes y los PRINCIPIOS DE DISENO, y los principios de diseno son el paso 5 del que sobrevive, o sea que estan a salvo por construccion.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 2, "en 10-15 anos", ", "],
                "3": ["INCISO", 2, "usuarios, empresas, reguladores", ", del tipo "],
                "4": ["CUBIERTO", 3],
                "5": ["INCISO", 4, "antes de definir requisitos del producto", ", y "],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA Y NINGUNA SE PIERDE: los cinco pasos del que muere estan uno a uno en los del superviviente, y las TRES cosas que la razon nombra como caras de perder se salvan las tres. EL PLAZO (10-15 anos) y LOS TRES TIPOS DE PERSONAJE (usuarios, empresas, reguladores) van de INCISO adosados al paso 2 del superviviente, que es donde vive la historia con personajes. LOS PRINCIPIOS DE DISENO no hacen falta salvarlos porque son el paso 5 del propio superviviente. UN TERCER INCISO: el antes de definir requisitos del producto, que es el momento concreto de la conversacion del paso 4. CERO perdidas nombradas.",
        },
        {
            "orden": 12,
            "superviviente": "evaluacion_industria_cliente",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 6 contra 5 a favor de evaluacion_industria_cliente y condiciones 2 contra 2, empatadas: una sola vara de contenido no empatada BASTA, asi que el cableado NO habla, y se dice que apuntaba al mismo lado (4 contra 3). La razon del puesto 605 reconoce propio a los DOS lados (dos entradas de campo en evaluacion_industria_cliente, la voz del cliente cara a cara y los usuarios lider; dos de futuro en analisis_disrupciones_mercado, la desintermediacion y los escenarios), asi que esa vara EMPATA y la que decide es la de los pasos.",
            "pasos": {
                "1": ["CUBIERTO", 3],
                "2": ["APPEND"],
                "3": ["INCISO", 5, "y como estan cambiando", ", "],
                "4": ["CUBIERTO", 4],
                "5": ["APPEND"],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son exactamente los dos que la razon declara propios del que muere: evaluar el futuro de cada actor de la cadena y quien queda desintermediado, y definir escenarios futuros de los que salen las arenas. UN INCISO: el y como estan cambiando de los drivers de rentabilidad, que es el matiz de futuro del paso 5 del superviviente (el Profit Pool Map de margenes por actividad). SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos de los del superviviente: buscar innovacion A NIVEL ESTRATEGICO y no de producto individual, e industria del cliente atravesando CAMBIOS ESTRUCTURALES; ninguna de las dos del superviviente los dice. CERO perdidas nombradas.",
        },
        {
            "orden": 13,
            "superviviente": "definicion_alineacion_cadena_suministro",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO. Pasos 7 contra 4 y condiciones 2 contra 1, las dos a favor de definicion_alineacion_cadena_suministro; el cableado apunta al mismo lado y por mucho (17 contra 5). La razon del puesto 614 reconoce propio a los dos lados y nombra EL DRIVER DE INFORMACION como lo mas caro de perder; ese driver esta del lado del que MUERE, y por eso el reparto lo salva con inciso en vez de dejarlo caer, que es lo que hace la eleccion sostenible.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["INCISO", 2, "y sus core competencies", ", "],
                "3": ["INCISO", 4, "los 5 drivers (produccion, inventario, ubicacion, transporte, informacion)", ", que son "],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son los dos que la razon declara propios del que muere: las seis preguntas de Chopra y Meindl sobre el mercado, y la validacion final de que la estrategia de cadena sea coherente con la propuesta de valor al cliente. DOS INCISOS, y el segundo es la pieza que la razon llama la mas cara: EL QUINTO DRIVER, LA INFORMACION, se adosa al paso 4 del superviviente, que enumera produccion, inventario, ubicacion y transporte y NO nombra la informacion. El primero son las core competencies, parametro del rol dentro de la cadena del paso 2. Su unica condicion queda cubierta. CERO perdidas nombradas.",
        },
        {
            "orden": 14,
            "superviviente": "creacion_data_warehouse",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO. Pasos 5 contra 4 y condiciones 2 contra 1, las dos a favor de creacion_data_warehouse; el cableado apunta al mismo lado (3 contra 2). La razon del puesto 630 reconoce propio a los dos lados (automatizar la captura y dar acceso por internet a los socios de la cadena en uno; la cadencia y el argumento de prioridad en el otro), asi que esa vara empata y las que deciden son las contables.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 3, "diaria u horariamente", ", consolidando "],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 4],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "UNA PIEZA VIAJA ENTERA y es la mitad del propio declarado del que muere: priorizar el repositorio como base ANTES de construir los modulos analiticos de pronostico y programacion. UN INCISO: la CADENCIA (diaria u horariamente), que es la otra mitad de ese propio y es un parametro concreto del paso 3 del superviviente. UNA PERDIDA NOMBRADA: su condicion 1 nombra el OBJETIVO que dispara el proyecto (querer mejorar pronostico, inventario o gestion de pedidos) y la condicion 1 del superviviente solo habla de manejar varios sistemas de informacion dispersos; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra.",
        },
        {
            "orden": 15,
            "superviviente": "ciclo_de_conversion_de_efectivo",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO, Y ADEMAS ES EL CENTRO MEDIDO DEL RACIMO. Pasos 6 contra 4 y condiciones 4 contra 2, las dos a favor de ciclo_de_conversion_de_efectivo; el cableado apunta al mismo lado (8 contra 3). LA PIEZA DECLARADA APUNTA IGUAL Y ES LA MAS FUERTE DEL ACTO: la razon del puesto 653 escribe que EL CORTO CABE DENTRO DEL LARGO, que lo unico propio del corto son las causas del DSO alto, y que la remedicion de la seccion 14 del informe midio que EL CENTRO es ciclo_de_conversion_de_efectivo y que dso_dpo_gestion_capital_trabajo es EL AISLADO, el gemelo sin casa. ESTE ACTO ES EL UNICO DEL TRAMO CON COLISION PREVISTA, y se resolvio ANTES de fundir por relectura del filo (el puesto 203 pasa de C a D con correccion declarada), con el censo esperado RE-CORRIDO despues y bajando de UNA colision a CERO.",
            "pasos": {
                "1": ["INCISO", 1, "cuentas por cobrar finales dividido entre ingresos diarios", ", el DSO es "],
                "2": ["INCISO", 1, "cuentas por pagar finales dividido entre COGS diario", ", y el DPO es "],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 4],
            },
            "condiciones": {"1": ["CUBIERTO", 2], "2": ["CUBIERTO", 3]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara como lo unico propio del que muere: investigar las causas de un DSO elevado, quejas de clientes, terminos de venta laxos y facturacion lenta. DOS INCISOS: LAS DOS FORMULAS DE CALCULO, la del DSO y la del DPO, que se adosan al paso 1 del superviviente, donde el DSO y el DPO se mandan calcular pero NO se dice como. Su paso 4 queda cubierto por el paso 4 del superviviente, que es el mismo trade-off de maximizar el DPO sin quemar proveedores. UNA PERDIDA NOMBRADA: su condicion 1 dice PESE A VENTAS SALUDABLES, que es lo que hace del sintoma un problema de ciclo y no de demanda, y la condicion 2 del superviviente solo dice problemas de liquidez; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra.",
        },
        {
            "orden": 16,
            "superviviente": "fase_mobilizar_modelo_negocio",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 5 contra 4 a favor de fase_mobilizar_modelo_negocio y condiciones 1 contra 1, empatadas: una sola vara de contenido no empatada BASTA, asi que el cableado NO habla, y se dice que apuntaba al mismo lado (3 contra 2). La razon del puesto 674 reconoce propio a los DOS lados (el kill/thrill y el respaldo visible de quienes mandan en uno; la educacion de los que deciden con historias e imagenes en el otro), asi que esa vara EMPATA y la que decide es la de los pasos.",
            "pasos": {
                "1": ["CUBIERTO", 2],
                "2": ["INCISO", 2, "diferentes niveles jerarquicos y areas de expertise", ", incluyendo "],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 1],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: educar a los tomadores de decisiones sobre modelos de negocio usando historias e imagenes y no teoria. UN INCISO: los diferentes niveles jerarquicos y areas de expertise, que es un parametro concreto del equipo diverso del paso 2 del superviviente. Y SE DICE UNA COSA MEDIDA EN VEZ DE CALLARLA: su condicion 1 acota el disparador a UNA ORGANIZACION ESTABLECIDA y la condicion 1 del superviviente no lo acota, pero el alcance NO se pierde del nodo, porque el paso 5 del superviviente dice literalmente que si estas dentro de una empresa ya establecida consigas el respaldo visible de quienes mandan. Se marca CUBIERTO y NO se cuenta perdida, y la comprobacion queda escrita. CERO perdidas nombradas.",
        },
        {
            "orden": 17,
            "superviviente": "community_building_estrategia",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO. Pasos 7 contra 5 y condiciones 3 contra 2, las dos a favor de community_building_estrategia; el cableado apunta al mismo lado (8 contra 4). La razon del puesto 713 reconoce propio a los DOS lados y nombra como lo mas caro de perder DOS piezas del que muere, la pregunta previa de si tu modelo de negocio SE PRESTA a la comunidad y la conexion CRUZADA entre miembros: las dos viajan enteras en el reparto, y eso es lo que hace la eleccion sostenible.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["INCISO", 2, "comunidades complementarias existentes online y offline", ", incluidas "],
                "3": ["CUBIERTO", 1],
                "4": ["APPEND"],
                "5": ["CUBIERTO", 7],
            },
            "condiciones": {"1": ["APPEND"], "2": ["CUBIERTO", 3]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son exactamente los dos que la razon llama lo mas caro de perder: evaluar si tu modelo de negocio se presta naturalmente a la construccion de comunidad, y fomentar la conexion cruzada entre miembros y no solo entre miembro y empresa. UN INCISO: las comunidades complementarias ya existentes online y offline, que es un parametro concreto de la audiencia existente del paso 2 del superviviente. Su condicion 1 (negocio que depende de conectar personas entre si) viaja entera por ser un disparador distinto del de contenido generado por usuarios. CERO perdidas nombradas.",
        },
    ],
    "declarados": [],
}



LOTES["B"] = {
    "titulo": "3, LOTE B DE LA VUELTA 56: LOS ACTOS 18 A 34 EN EL ORDEN IMPRESO DEL TRAMO, apartando SOLO el 27, que queda DECLARADO porque sus dos varas de contenido CHOCAN y la pieza declarada no desempata",
    "actos": [
        {
            "orden": 18,
            "superviviente": "embudo_secuencial_de_inversores",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 4 contra 4 y condiciones 2 contra 2: las dos varas de contenido empatan al digito, y la razon del puesto 752 reconoce material propio a los DOS lados (lo propio de seleccion_etapa_fondo_vc es investigar el tamano de fondo y el foco de etapa; lo propio de embudo_secuencial_de_inversores son la planificacion escalonada y las metricas de traccion de paso), asi que tampoco la pieza declarada desempata. Con el contenido callado entero, EL CABLEADO DECIDE SOLO y apunta a embudo_secuencial_de_inversores, 4 contra 3. NO es empate sin vara porque el cableado no empata. Y SE DICE QUE LA ELECCION COINCIDE CON LO QUE LA RAZON LLAMA LO MAS CARO DE PERDER: las METRICAS DE TRACCION de paso, que son del que sobrevive.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["APPEND"],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 2],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son exactamente lo que la razon declara propio del que muere, que ademas llama LO UNICO ACCIONABLE DEL PAR: investigar el tamano de fondo y el foco de etapa de cada inversor de la lista, y descartar a los que no coinciden con tu etapa. Los otros dos son la etapa actual y el enfoque del esfuerzo, que el superviviente ya tiene. Sus dos condiciones quedan cubiertas una a una. CERO perdidas nombradas.",
        },
        {
            "orden": 19,
            "superviviente": "vesting_acciones_fundadores",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO. Pasos 7 contra 5 y condiciones 5 contra 4, las dos a favor de vesting_acciones_fundadores; el cableado apunta al mismo lado (14 contra 7). Y LA PIEZA DECLARADA APUNTA IGUAL: la razon del puesto 776 nombra LOS TREINTA DIAS DEL 83(b) Y EL DOBLE DISPARO como lo mas caro de perder porque son plazos y clausulas, no consejos, y las dos piezas son de vesting_acciones_fundadores: estan a salvo por construccion.",
            "pasos": {
                "1": ["INCISO", 3, "distinguelo del tuyo como fundador", ", y "],
                "2": ["CUBIERTO", 4],
                "3": ["APPEND"],
                "4": ["APPEND"],
                "5": ["CUBIERTO", 6],
            },
            "condiciones": {"1": ["CUBIERTO", 3], "2": ["APPEND"], "3": ["APPEND"],
                            "4": ["CUBIERTO", 5]},
            "nota": "DOS PASOS VIAJAN ENTEROS: decidir si cada rol consolida solo por tiempo o tambien por desempeno, que es lo que la razon declara propio del que muere, y dejar por escrito las condiciones de cada persona de forma consistente. ESTE SEGUNDO SE DICE APARTE porque la razon lo da por compartido y EL TEXTO NO LO DICE: los siete pasos del superviviente documentan la recompra, la causa y la razon justificada, pero NINGUNO manda dejar por escrito las condiciones de CADA PERSONA de forma consistente, medido paso a paso. PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3). UN INCISO: distinguir el plazo del equipo del tuyo como fundador, parametro concreto del cronograma del paso 3. DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos (definir como pagaras a las primeras contrataciones, y formalizar la oferta a un nuevo ejecutivo). Y SE DICE UNA COSA MEDIDA EN VEZ DE CALLARLA: su condicion 4 junta recibir inversion Y vender, y la condicion 5 del superviviente solo habla de negociar una venta; el otro medio disparador NO se pierde del nodo porque la condicion 3 del superviviente nombra al inversionista que exige vesting. Se marca CUBIERTO y NO se cuenta perdida, con la comprobacion escrita. CERO perdidas nombradas.",
        },
        {
            "orden": 20,
            "superviviente": "homogeneidad_vs_diversidad_equipo",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO. Pasos 5 contra 4 y condiciones 3 contra 2, las dos a favor de homogeneidad_vs_diversidad_equipo; el cableado apunta al mismo lado (6 contra 2). La razon del puesto 782 reconoce propio a los dos lados (el analisis estructurado de capital humano, social y financiero y la balanza cohesion contra perspectiva en uno; la formula corta de habilidades distintas y valores parecidos en el otro), asi que esa vara empata y las que deciden son las contables.",
            "pasos": {
                "1": ["CUBIERTO", 2],
                "2": ["CUBIERTO", 3],
                "3": ["INCISO", 4, "cuanto compromiso espera cada uno", ", y "],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA: no caer en el default de elegir a alguien solo porque se parece a ti o te da comodidad, que es el aviso que ninguno de los cinco pasos del superviviente da. UN INCISO: cuanto compromiso espera cada uno, que es un factor blando que el paso 4 del superviviente no nombra entre los suyos (tolerancia al riesgo, valores, estilo de trabajo). SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos: armar el equipo fundador DESDE CERO y estar POR SUMAR a un nuevo cofundador, dos momentos que las tres del superviviente no dicen, porque las tres describen un equipo YA formado y parecido. CERO perdidas nombradas.",
        },
        {
            "orden": 21,
            "superviviente": "ia_como_nivelador_habilidades",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO. Pasos 5 contra 4 y condiciones 4 contra 2, las dos a favor de ia_como_nivelador_habilidades; el cableado apunta al mismo lado (3 contra 2). Y LA PIEZA DECLARADA APUNTA IGUAL: la razon del puesto 783 dice que lo propio de ia_como_nivelador_habilidades es MEDIR EL CAMBIO EN LA BRECHA, que es LA UNICA FORMA DE COMPROBAR QUE LA IA NIVELA Y NO SOLO MEJORA, y esa pieza es del que sobrevive.",
            "pasos": {
                "1": ["INCISO", 1, "memos, informes, comunicados", ", como "],
                "2": ["CUBIERTO", 2],
                "3": ["CUBIERTO", 3],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["APPEND"], "2": ["CUBIERTO", 1]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: la revision humana rapida antes de enviar cualquier documento generado con asistencia de IA. UN INCISO: los ejemplos de tarea (memos, informes, comunicados), parametro concreto del paso 1 del superviviente, que habla de tareas con mayor variabilidad sin nombrar ninguna. Su condicion 1 (el equipo dedica mucho tiempo a redaccion de informes, propuestas o comunicaciones internas) viaja entera por ser un disparador distinto. CERO perdidas nombradas.",
        },
        {
            "orden": 22,
            "superviviente": "mantener_puntaje_innovacion",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 4 contra 4 y condiciones 2 contra 2: las dos varas de contenido empatan al digito, y la razon del puesto 789 reconoce material propio a los DOS lados (dos cifras de comparacion hacia afuera en auditoria_desempeno_new_products; la proporcion de RECURSOS por resultado en mantener_puntaje_innovacion, que la razon subraya como la unica que mira el dinero), asi que tampoco la pieza declarada desempata. Con el contenido callado entero, EL CABLEADO DECIDE SOLO y apunta a mantener_puntaje_innovacion, 4 contra 2.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["CUBIERTO", 1],
                "3": ["APPEND"],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 2], "2": ["APPEND"]},
            "nota": "TRES PASOS VIAJAN ENTEROS y son exactamente las TRES CIFRAS que la razon dice que hay que salvar del que muere: el porcentaje de las ventas actuales que viene de productos lanzados en los ultimos tres anos, la tasa de atraso entre lo planeado y lo real, y la comparacion contra el estandar de la industria. Ninguna de las tres esta en los cuatro pasos del superviviente, medido paso a paso. Su condicion 2 (justificar con datos una inversion mayor en investigacion y desarrollo) viaja entera por ser un disparador distinto. CERO perdidas nombradas.",
        },
        {
            "orden": 23,
            "superviviente": "duration_estimating_worksheet",
            "motivo": "CONTEOS DE CONTENIDO CONTRA PIEZA DECLARADA, Y DECIDE LA PIEZA DECLARADA (acta 53, pregunta 3, y acta 54, pregunta 2). ES EL PRIMER ACTO DEL TRAMO DONDE LAS DOS COSAS NO APUNTAN AL MISMO LADO, y por eso el motivo lo dice entero. LOS CONTEOS APUNTAN AL OTRO: pasos 4 contra 5 y condiciones 1 contra 2, las dos a favor de estimacion_tres_puntos, y el cableado tambien (3 contra 5). LA PIEZA DECLARADA APUNTA AQUI, Y ES LA MAS ESPECIFICA DEL ACTO: la razon del puesto 793 escribe que duration_estimating_worksheet OFRECE TRES METODOS DE ESTIMACION y que el tercero ES el de tres puntos; que estimacion_tres_puntos DESARROLLA ESE TERCER METODO; que sus tres primeros pasos son el mismo paso partido en tres, el cuarto es el CALCULAR que la madre ya manda y el quinto es el REGISTRAR que la madre ya manda; y que LO QUE ANADE CABE EN UNA LINEA, el nombre de la ponderacion Beta. Por la vara del banco 9.6.1 la razon concluye REPITE. El padre declarado es parte del CONTENIDO que P.8 pesa, no un extra: cuando choca con los conteos, decide el declarado. Y SE DICE LA CONSECUENCIA MEDIDA QUE HACE LA ELECCION SOSTENIBLE: la madre tiene TRES metodos y el hijo solo desarrolla UNO; si sobreviviera el hijo, los metodos parametrico y analogo tendrian que viajar de APPEND a un nodo titulado Estimacion de Tres Puntos, y esta operacion NO redacta titulos. VA MARCADO COMO DISCUTIBLE EN EL REPORTE.",
            "pasos": {
                "1": ["CUBIERTO", 3],
                "2": ["CUBIERTO", 3],
                "3": ["CUBIERTO", 3],
                "4": ["INCISO", 3, "la formula de ponderacion Beta", ", con "],
                "5": ["CUBIERTO", 4],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "NINGUNA PIEZA DE PASO VIAJA ENTERA Y NINGUNA SE PIERDE: los tres primeros pasos del que muere son el paso 3 del superviviente partido en tres (optimista, mas probable y pesimista) y su paso 5 es el paso 4 del superviviente (registrar). UN INCISO, y es exactamente LA UNICA LINEA que la razon dice que el hijo anade: el nombre de la ponderacion Beta, adosado al paso 3 del superviviente, que ya manda calcular la duracion esperada usando distribucion Beta pero no nombra la formula de ponderacion. SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos del suyo: la incertidumbre significativa en duracion o costo, y el analisis cuantitativo de riesgo en la planificacion; la unica condicion del superviviente habla de requerir una estimacion cuantitativa y detallada con metodos formales, que es otra cosa. CERO perdidas nombradas.",
        },
        {
            "orden": 24,
            "superviviente": "eventos_offline_como_canal_traccion",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 7 contra 5 a favor de eventos_offline_como_canal_traccion y condiciones 3 contra 3, empatadas: una sola vara de contenido no empatada BASTA, asi que el cableado NO habla, y se dice que apuntaba al mismo lado (6 contra 5). La razon del puesto 804 reconoce propio a los DOS lados y nombra como lo que hay que salvar EL PRECIO ALTO COMO FILTRO, que es del que sobrevive, y LOS MEETUPS SATELITE, que son del que muere y viajan enteros en el reparto.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["INCISO", 2, "evento lujoso multi-dia para decision makers de alto nivel", ", o un "],
                "3": ["INCISO", 3, "sin que el evento parezca un pitch de ventas", ", y "],
                "4": ["APPEND"],
                "5": ["APPEND"],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"], "3": ["APPEND"]},
            "nota": "TRES PASOS VIAJAN ENTEROS: validar la demanda del evento preguntando a la audiencia o vendiendo entradas por anticipado, y los DOS que la razon declara propios del que muere, la transmision en vivo o los meetups satelite y la repeticion anual ajustando precio y escala. EL PRIMERO SE DICE APARTE porque la razon lo da por compartido y EL TEXTO NO LO DICE: el paso 1 del superviviente manda PENSAR si la gente comparte intereses, no PREGUNTARLE ni vender entradas por anticipado, medido paso a paso. PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3). DOS INCISOS: el formato caro de varios dias para decision makers, alternativa concreta del evento pequeno del paso 2, y el aviso de que el evento no parezca un pitch de ventas, parametro del paso 3. SUS TRES CONDICIONES VIAJAN ENTERAS por ser disparadores distintos de los tres del superviviente, que hablan de a quien vendes y de que otros canales fallan, no de si existe evento de industria ni de posicionamiento de marca. CERO perdidas nombradas.",
        },
        {
            "orden": 25,
            "superviviente": "genchi_gembutsu_salir_del_edificio",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 5 contra 4 a favor de genchi_gembutsu_salir_del_edificio y condiciones 2 contra 2, empatadas: una sola vara de contenido no empatada BASTA, asi que el cableado NO habla, y se dice que apuntaba al mismo lado (6 contra 3). La razon del puesto 840 reconoce a cada uno UN SOLO gesto propio, asi que esa vara EMPATA y la que decide es la de los pasos.",
            "pasos": {
                "1": ["INCISO", 2, "get out of the building", ", lo que se llama "],
                "2": ["CUBIERTO", 4],
                "3": ["CUBIERTO", 5],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 2], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente el unico gesto que la razon declara propio del que muere: usar las observaciones para ajustar el diseno del producto o servicio. UN INCISO: el nombre en ingles del principio, get out of the building, que el paso 2 del superviviente no trae y que es lo que lo hace buscable. Su condicion 2 (el equipo fundador sin experiencia directa con el mercado objetivo) viaja entera por ser un disparador distinto del de tener solo intuicion o corazonadas. CERO perdidas nombradas.",
        },
        {
            "orden": 26,
            "superviviente": "technology_platform_evaluation",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 4 contra 4 y condiciones 2 contra 2: las dos varas de contenido empatan al digito, y la razon del puesto 852 reconoce material propio a los DOS lados (dos piezas en flexible_go_kill_criteria, tres en technology_platform_evaluation), asi que tampoco la pieza declarada desempata. Con el contenido callado entero, EL CABLEADO DECIDE SOLO y apunta a technology_platform_evaluation, 4 contra 5 en el cuadro de varas. Y SE DECLARA UN CONTRASTE DE CONTEO EN VEZ DE TAPARLO: el dossier imprime el cableado CRUDO del fichero (6 contra 5) y el cuadro de varas lo imprime RESUELTO (4 contra 5); la vara que decide es la del cuadro, que es la que pasa por el resolutor de P.1, y la direccion NO es la misma en los dos, asi que se dice cual se usa y por que.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 3, "ajuste estrategico, ventaja competitiva, potencial de mercado", ", que son "],
                "3": ["APPEND"],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son exactamente los dos que la razon declara propios del que muere: los metodos financieros sofisticados para riesgo (opciones reales, Monte Carlo y valor comercial esperado) y la integracion de las decisiones de puerta con revisiones trimestrales de portafolio. UN INCISO: los TRES criterios de la tabla de evaluacion (ajuste estrategico, ventaja competitiva, potencial de mercado), que el paso 3 del superviviente pide sin nombrarlos. Sus dos condiciones quedan cubiertas una a una. CERO perdidas nombradas.",
        },
        {
            "orden": 28,
            "superviviente": "simulacion_de_operaciones_supply_chain",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO. Pasos 6 contra 5 y condiciones 3 contra 2, las dos a favor de simulacion_de_operaciones_supply_chain; el cableado EMPATA (4 contra 4) y por eso no habria decidido nada aunque le tocara, y se dice. La razon del puesto 868 reconoce propio a los DOS lados (los datos de ERP y SCM y el horizonte de decision en uno; la estrategia previa, las tecnologias y la repeticion periodica en el otro), asi que esa vara empata y las que deciden son las contables.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["INCISO", 4, "no solo optimizar lo existente", ", y "],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 5],
                "5": ["APPEND"],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "TRES PASOS VIAJAN ENTEROS y son exactamente los tres que la razon declara propios del que muere: definir la estrategia de negocio ANTES de disenar la cadena, probar combinaciones de tecnologias (robots, manufactura aditiva, vehiculos autonomos) y repetir la simulacion de forma periodica para adaptarse a cambios del mercado global. UN INCISO: el no solo optimizar lo existente, que es el matiz que separa simular escenarios de optimizar la red actual y que el paso 4 del superviviente no dice. SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos: redisenar la cadena para ESCALAR y el crecimiento de ventas que exige repensar la logistica; las tres del superviviente hablan de ubicacion de planta, incertidumbre de demanda y stock de seguridad. CERO perdidas nombradas.",
        },
        {
            "orden": 29,
            "superviviente": "colaboracion_transporte_ctm",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 5 contra 4 a favor de colaboracion_transporte_ctm y condiciones 2 contra 2, empatadas: una sola vara de contenido no empatada BASTA, asi que el cableado NO habla, y SE DICE QUE APUNTABA AL OTRO (3 contra 5), porque el cableado solo decide cuando el contenido calla ENTERO y aqui no calla. La razon del puesto 883 reconoce DOS piezas propias concretas a colaboracion_transporte_ctm (el modelo matematico de la red y las reglas de expectativas y reparto de beneficios) y UNA a collaborative_transportation_management, y ademas avisa con todas sus letras que HAY QUE LEER CUAL DE LOS DOS TRAE MAS ANTES DE FUSIONAR: leido, trae mas el de nombre en espanol.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["INCISO", 3, "en tiempo real", ", "],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 5],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: definir el NIVEL de colaboracion deseado y el intercambio de informacion asociado. UN INCISO: el en tiempo real del hub de informacion comun, que es un parametro concreto del paso 3 del superviviente. SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos: operar con multiples transportistas o socios logisticos, y buscar reducir costos de transporte mediante colaboracion; las dos del superviviente hablan de competir contra rivales mas grandes y de sinergias de peso o volumen. CERO perdidas nombradas.",
        },
        {
            "orden": 30,
            "superviviente": "search_for_business_model",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO, Y ADEMAS LA PIEZA DECLARADA APUNTA IGUAL. Pasos 6 contra 4 y condiciones 4 contra 2, las dos a favor de search_for_business_model; el cableado apunta al mismo lado y por mucho (35 contra 6). La razon del puesto 905 escribe que LO PROPIO DE customer_development_vs_business_plan ES UNA LINEA, el lienzo como herramienta de planificacion flexible, y que por la vara del banco 9.6.1 eso es REPITE; y nombra como lo que hay que salvar la distincion BUSQUEDA contra EJECUCION y el aviso de no montar estructura antes de tiempo, que son las dos del que sobrevive.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["CUBIERTO", 3],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 5],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "DOS PASOS VIAJAN ENTEROS: usar el Business Model Canvas y el Value Proposition Canvas como herramientas de planificacion flexible, que es LA LINEA que la razon declara propia del que muere; y abandonar la idea de escribir un plan de negocio detallado al inicio. ESTE SEGUNDO SE DICE APARTE porque la razon lo da por compartido y EL TEXTO NO LO DICE: los seis pasos del superviviente mandan determinar el modo, listar hipotesis marcadas como no probadas, salir a probarlas, no montar estructura, iterar y adoptar mentalidad de aprendizaje, y NINGUNO manda abandonar el plan de negocio, medido paso a paso. PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3), y APPEND no pierde nada. Sus dos condiciones quedan cubiertas una a una. CERO perdidas nombradas.",
        },
        {
            "orden": 31,
            "superviviente": "planificacion_consecuencias_no_intencionadas",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 5 contra 4 a favor de planificacion_consecuencias_no_intencionadas y condiciones 2 contra 2, empatadas: una sola vara de contenido no empatada BASTA, asi que el cableado NO habla, y SE DICE QUE APUNTABA AL OTRO (5 contra 4 en el cuadro de varas). Y LA PIEZA DECLARADA APUNTA AL MISMO LADO QUE LOS PASOS: la razon del puesto 928 dice que LAS DOS PIEZAS OPERATIVAS QUE HAY QUE SALVAR, detectar temprano los comportamientos no esperados y tener un plan para frenar o revertir, son de planificacion_consecuencias_no_intencionadas: estan a salvo por construccion.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["APPEND"],
                "3": ["INCISO", 2, "los que aparecen despues del primer impacto", ", o sea "],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["APPEND"], "2": ["CUBIERTO", 2]},
            "nota": "TRES PASOS VIAJAN ENTEROS: los DOS que la razon declara propios del que muere y que son su punto de entrada (describir como se ve el exito total, y preguntarse que sale mal si funciona exactamente como se imagino), mas anotar los riesgos y pensar como reducirlos desde ahora. ESTE TERCERO SE DICE APARTE porque la razon lo da por compartido y EL TEXTO NO LO DICE: los cinco pasos del superviviente listan efectos, cruzan variables, identifican lo que no se controla, disenan la deteccion temprana y preparan la reversion, y NINGUNO manda ANOTAR los riesgos encontrados, medido paso a paso. PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3). UN INCISO: la definicion de efecto indirecto (los que aparecen despues del primer impacto), parametro del paso 2 del superviviente. Su condicion 1 (vision muy optimista y sin pensar en los riesgos) viaja entera por ser un disparador distinto. CERO perdidas nombradas.",
        },
        {
            "orden": 32,
            "superviviente": "estrategia_multicanal_bienvenida",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO. Pasos 5 contra 4 y condiciones 2 contra 1, las dos a favor de estrategia_multicanal_bienvenida; el cableado apunta al mismo lado (3 contra 2). La razon del puesto 948 reconoce propio a los dos lados (dos piezas de ejecucion en estrategia_multicanal_bienvenida, la personalizacion con el nombre y los detalles de la compra y la MEDICION antes y despues; una de criterio en seis_medios_comunicacion_cliente, elegir el medio segun la fase y el efecto emocional), asi que esa vara empata y las que deciden son las contables.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["APPEND"],
                "3": ["INCISO", 2, "correo fisico, video personalizado o regalos significativos", ", incluidos los medios subutilizados como "],
                "4": ["INCISO", 3, "Evitar gestos genericos (cupones, tazas con logo)", ", y "],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: seleccionar deliberadamente que medio usar segun la FASE en que esta el cliente y el efecto emocional que se busca. DOS INCISOS: los medios subutilizados con nombre (correo fisico, video personalizado, regalos significativos), que el paso 2 del superviviente lista de otra manera, y el aviso de evitar gestos genericos con sus dos ejemplos (cupones, tazas con logo), adosado al paso de la personalizacion. UNA PERDIDA NOMBRADA: su condicion 1 pide diversificar y personalizar la comunicacion EN CADA ETAPA DEL CICLO DE VIDA, y la condicion 1 del superviviente acota el disparador a la confirmacion de compra generica y automatizada, que es solo la bienvenida; el INCISO para condiciones no existe en el instrumento (pendiente de doctrina heredado) y por eso la perdida se nombra.",
        },
        {
            "orden": 33,
            "superviviente": "intellectual_property_strategy",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y LA PUERTA APUNTA AL MISMO LADO. Pasos 5 contra 4 a favor de intellectual_property_strategy y condiciones 1 contra 1, empatadas: una sola vara no empatada BASTA, asi que el cableado NO habla, y se dice que EMPATABA (5 contra 5). Y LA SEGUNDA VARA APUNTA IGUAL: intellectual_property_strategy ES PUERTA (extremo de puente aprobado) y la guarda 1B exige que sobreviva. AQUI NO HAY CHOQUE, las dos varas coinciden. La razon del puesto 978 lo confirma por el lado del contenido: TRES de los cuatro pasos del corto estan dentro del largo y lo que el corto anade CABE EN UNA LINEA, con lo que la vara del banco 9.6.1 devuelve REPITE.",
            "pasos": {
                "1": ["INCISO", 4, "desde que fundas tu empresa", ", "],
                "2": ["INCISO", 3, "acuerdo de 'work for hire'", ", incluido el "],
                "3": ["CUBIERTO", 5],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente LA LINEA que la razon dice que hay que salvar del corto: buscar a alguien con buen criterio legal antes de avanzar mas en construir el negocio. DOS INCISOS: el momento (desde que fundas tu empresa), parametro de la cadena de titulo del paso 4, y el nombre del acuerdo (work for hire), parametro del acuerdo de cesion del paso 3. Su condicion viaja entera por ser un disparador distinto: haber compartido ya la idea o haber contratado a alguien para desarrollarla, contra depender de tecnologia, marca o contenido propio como ventaja competitiva. CERO perdidas nombradas.",
        },
        {
            "orden": 34,
            "superviviente": "metricas_accionables",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO, Y LA PUERTA APUNTA AL MISMO LADO. Pasos 6 contra 4 y condiciones 4 contra 2, las dos a favor de metricas_accionables; el cableado apunta al mismo lado (12 contra 3). Y LA SEGUNDA VARA APUNTA IGUAL: metricas_accionables ES PUERTA (extremo de puente aprobado) y la guarda 1B exige que sobreviva. AQUI NO HAY CHOQUE. La razon del puesto 1031 reconoce propio a los dos lados y nombra como lo que hay que salvar LA INSTRUCCION SOBRE QUE ENSENARLE AL INVERSIONISTA, que es del que muere y viaja entera en el reparto.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["APPEND"],
                "3": ["APPEND"],
                "4": ["INCISO", 1, "metricas de vanidad (visitas, descargas) y metricas accionables (retencion, conversion, recompra)", ", distinguiendo entre "],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "TRES PASOS VIAJAN ENTEROS: los DOS que la razon declara propios del que muere (evitar campanas de marketing o prensa disenadas solo para inflar metricas superficiales, y presentar al inversionista el APRENDIZAJE VALIDADO con curvas de comportamiento real en vez de cifras aisladas) mas definir que hipotesis se quiere validar antes de buscar crecimiento en numeros brutos, que es un gesto que ninguno de los seis pasos del superviviente dice. UN INCISO: la lista de las dos familias con sus ejemplos (visitas y descargas contra retencion, conversion y recompra), adosada al paso 1 del superviviente, que evita los numeros brutos sin nombrar ninguna. SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos de las cuatro del superviviente: numeros pequenos con riesgo de perder la confianza, y la tentacion de aparentar traccion con marketing. CERO perdidas nombradas.",
        },
    ],
    "declarados": [
        {
            "orden": 27,
            "miembros": ["decision_pivote_perseverar", "pivotar_o_perseverar"],
            "especie": "CONTEOS DE CONTENIDO QUE CHOCAN Y LA PIEZA DECLARADA NO DESEMPATA",
            "motivo": "LAS DOS VARAS DE CONTENIDO APUNTAN A LADOS DISTINTOS: pasos 4 contra 5 a favor de pivotar_o_perseverar y condiciones 3 contra 2 a favor de decision_pivote_perseverar. Por el acta 53 pregunta 3 y el acta 54 pregunta 2, cuando dos varas de contenido CHOCAN decide LA PIEZA DECLARADA, y si no hay ninguna el acto SE DECLARA y acumula para la mesa. AQUI LA PIEZA DECLARADA NO DESEMPATA PORQUE HAY MATERIAL PROPIO DECLARADO A LOS DOS LADOS: la razon del puesto 860 escribe que lo propio de pivotar_o_perseverar son DOS (establecer una linea base NUEVA despues de pivotar, y comprobar que las acciones nuevas rinden mas que las viejas) y que lo propio del bloque de Ries del otro es evaluar si el equipo esta racionalizando el fracaso en vez de aceptarlo. EL MATERIAL PROPIO DECLARADO DE UN SOLO LADO ES UNA VARA (acta 54, pregunta 4), y de LOS DOS lados EMPATA. Y EL CABLEADO NO PUEDE HABLAR: solo decide cuando el contenido calla ENTERO, y aqui el contenido no calla, CHOCA. MISMA ESPECIE que los actos 4, 20 y 42 del tramo 2, con el pendiente de doctrina nombrado en 03_FUSIONES.md: la mesa tiene que elegir una PRELACION ENTRE CONTEOS DE CONTENIDO o una AMPLIACION de donde vive la pieza declarada.",
            "acumula_para": "LA MESA, con el pendiente de doctrina 1 de la vuelta 55, ahora con CUATRO actos y no tres",
        },
    ],
}



LOTES["C"] = {
    "titulo": "3, LOTE C DE LA VUELTA 56: LOS ACTOS 35 A 50 EN EL ORDEN IMPRESO DEL TRAMO, apartando el 37 y el 45, que quedan DECLARADOS por EMPATE SIN VARA (ni el contenido ni el cableado separan)",
    "actos": [
        {
            "orden": 35,
            "superviviente": "alineacion_de_objetivos_en_sistemas",
            "motivo": "LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO (acta 54, pregunta 1, registrada en 03_FUSIONES.md), Y AQUI EL CONTENIDO NO TIENE ENTRE QUIEN ELEGIR. alineacion_de_objetivos_en_sistemas ES PUERTA (extremo de puente aprobado) y la guarda 1B exige que sobreviva: es el UNICO candidato limpio del acto. EL CHOQUE SE REGISTRA CON SUS CIFRAS Y ES DE CONTENIDO: pasos 4 contra 4, empatados, y condiciones 1 contra 2 A FAVOR DEL OTRO, que es la unica vara de contenido no empatada del acto; el cableado tambien apunta al otro (4 contra 5). MISMA FIGURA QUE LOS ACTOS 1 Y 15 DEL TRAMO 2, y distinta de la del acto 8 de este tramo, donde el contenido empataba entero y el choque era de cableado. LO QUE PROTEGE EL CONTENIDO QUE EL CONTEO PREFIRIO ES EL REPARTO, y se mide abajo.",
            "pasos": {
                "1": ["INCISO", 1, "no solo a quien usa el servicio", ", "],
                "2": ["APPEND"],
                "3": ["CUBIERTO", 3],
                "4": ["INCISO", 4, "en lugar de imponer una regla desde arriba", ", "],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon del puesto 1034 declara propia del que muere: redisenar el recorrido y el espacio fisico para darle mas informacion a cada participante. DOS INCISOS: el no solo a quien usa el servicio, que es el alcance del paso 1 del superviviente, y el en lugar de imponer una regla desde arriba, que es el contraste del paso 4. Su condicion 2 (las soluciones de hoy son solo reglas administrativas sin diseno de experiencia) viaja entera por ser un disparador distinto. UNA PERDIDA NOMBRADA: su condicion 1 acota el disparador a que el problema involucre VARIAS ORGANIZACIONES O ENTIDADES DEL GOBIERNO, y la condicion 1 del superviviente habla de un sistema grande con distintos tipos de usuarios en conflicto, que no lo dice; el INCISO para condiciones no existe en el instrumento (pendiente de doctrina heredado) y por eso la perdida se nombra.",
        },
        {
            "orden": 36,
            "superviviente": "esfuerzo_voluntario_vs_urge_espontaneo",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 3 contra 4 a favor de esfuerzo_voluntario_vs_urge_espontaneo y condiciones 2 contra 2, empatadas: una sola vara de contenido no empatada BASTA, asi que el cableado NO habla, y se dice que apuntaba al mismo lado (3 contra 4). La razon del puesto 1059 reconoce propio a los DOS lados (un gesto mental concreto y un criterio en control_voluntario_del_pensamiento; los rituales y senales para concentrarse a voluntad en el otro), asi que esa vara EMPATA y la que decide es la de los pasos.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["APPEND"],
                "3": ["CUBIERTO", 3],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son exactamente los dos que la razon declara propios del que muere: el criterio de controlar mas cuando se esta aprendiendo una forma nueva de pensar y menos cuando la tarea ya se domina, y el gesto mental de sostener o desviar a proposito una idea que promete. Su tercer paso (no forzarte a corregir lo que ya dominas) queda cubierto por el paso 3 del superviviente, que manda dejar espacios donde la curiosidad aparezca sin que la ahogue la rigidez. Su condicion 2 (la discusion sobre cuanta estructura poner en una sesion de ideas) viaja entera por ser un disparador distinto. UNA PERDIDA NOMBRADA: su condicion 1 dispara al ESTAR APRENDIENDO una habilidad nueva de pensamiento o creacion, y la condicion 1 del superviviente dispara al DEPENDER SOLO DE LA INSPIRACION ESPONTANEA, que es otro estado; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra.",
        },
        {
            "orden": 38,
            "superviviente": "cuatro_etapas_del_pensamiento_creativo",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO, Y LA PUERTA APUNTA AL MISMO LADO. Pasos 6 contra 4 y condiciones 4 contra 1, las dos a favor de cuatro_etapas_del_pensamiento_creativo; el cableado apunta al mismo lado y por mucho (22 contra 6). Y LA SEGUNDA VARA APUNTA IGUAL: cuatro_etapas_del_pensamiento_creativo ES PUERTA y la guarda 1B exige que sobreviva. AQUI NO HAY CHOQUE. Y LA PIEZA DECLARADA APUNTA IGUAL, y es la mas fuerte del acto: la razon del puesto 1109 escribe que LA MADRE YA SE HABIA TRAGADO AL HIJO, que sus seis pasos para cuatro etapas incluyen justamente los dos del hijo, y que por la prueba del banco 9.12 EL ESCALON NO PIDE NADA QUE EL PRIMERO NO PIDA YA.",
            "pasos": {
                "1": ["CUBIERTO", 3],
                "2": ["INCISO", 3, "como indicio de Intimacion", ", "],
                "3": ["CUBIERTO", 4],
                "4": ["INCISO", 2, "silencio, actividad relajada", ", creando condiciones de "],
            },
            "condiciones": {"1": ["APPEND"]},
            "nota": "NINGUNA PIEZA DE PASO VIAJA ENTERA Y LA UNICA PERDIDA QUE LA RAZON PROPONIA SE SALVA. La razon del puesto 1109 proponia perder EL NOMBRE TECNICO DE WALLAS, LA INTIMACION, que el hijo usa en su paso 2 y la madre describe sin nombrar: aqui ese nombre va de INCISO adosado al paso 3 del superviviente, asi que NO se pierde. El segundo inciso son las condiciones concretas (silencio, actividad relajada), parametro del paso 2 del superviviente, que manda alejarse, dormir, caminar o trabajar en otra cosa. Su condicion viaja entera por ser un disparador distinto de las cuatro del superviviente: la idea repentina que llega EN un momento de relajacion, contra el bloqueo, el inicio de la ideacion, la necesidad de estructurar y la presion constante. CERO perdidas nombradas.",
        },
        {
            "orden": 39,
            "superviviente": "practica_de_observacion_atenta",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO. Pasos 4 contra 3 y condiciones 2 contra 1, las dos a favor de practica_de_observacion_atenta; el cableado apunta al mismo lado (8 contra 3). LA RAZON DEL PUESTO 1120 DEJA UNA COSA SIN ADJUDICAR Y AQUI SE ADJUDICA, con la vara escrita y no a ojo: escribe que los dos nodos SE CONTRADICEN en el momento de interpretar, uno manda preguntarse el porque MIENTRAS se observa y el otro manda SUSPENDER EL JUICIO y anotar primero, que el superviviente NO PUEDE LLEVAR LAS DOS, y cierra con queda anotado para quien haga la cura, no lo adjudico. LA CURA ES ESTA, asi que la remision es al ejecutor y no a una mesa: por la marca operativa registrada esta vuelta (acta 55, pregunta 1), una remision a una INSTANCIA NOMBRADA bloquea, y aqui la instancia nombrada es quien hace la cura. SE ADJUDICA POR LA TABLA DE LOS SEIS MOTIVOS DE PERDIDA DE LINEA, que es la vara escrita para este caso exacto: una linea que CONTRADIRIA al superviviente va de PERDIDA NOMBRADA antes que de inciso que miente, que es la misma vara con la que se resolvio el acto 45 del tramo 2. VA MARCADO COMO DISCUTIBLE EN EL REPORTE.",
            "pasos": {
                "1": ["INCISO", 4, "el habito diario", " Y hazlo con "],
                "2": ["CUBIERTO", 3],
                "3": ["CUBIERTO", 2],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "NINGUNA PIEZA VIAJA ENTERA. UN INCISO: el habito DIARIO, cadencia concreta que el paso 4 del superviviente no pone al hablar de disciplina regular. UNA PERDIDA NOMBRADA, Y NO ES DE CONDICIONES SINO DE MOMENTO DE UN PASO, que es la especie del acto 45 de la vuelta 55 y se dice para no mezclarlas: el paso 2 del que muere manda PREGUNTARSE EL PORQUE detras de objetos y comportamientos triviales MIENTRAS se observa, y el paso 2 del superviviente manda SUSPENDER EL JUICIO INMEDIATO, anotar primero e interpretar despues. La interpretacion NO se pierde del nodo, porque el paso 3 del superviviente busca patrones que revelen necesidades no declaradas; LO QUE SE PIERDE ES EL MOMENTO, y un INCISO ahi DIRIA LO CONTRARIO de lo que el paso que protege manda. La tabla de los seis motivos manda perdida NOMBRADA antes que inciso que miente.",
        },
        {
            "orden": 40,
            "superviviente": "bullseye_framework",
            "motivo": "CONTENIDO, TODAS LAS VARAS DE ACUERDO, Y ADEMAS LA PIEZA DECLARADA APUNTA IGUAL. Pasos 11 contra 5 y condiciones 3 contra 2, las dos a favor de bullseye_framework; el cableado apunta al mismo lado (12 contra 6). La razon del puesto 1142 escribe que EL ANILLO INTERMEDIO ES LA DIANA MISMA, que CUATRO de los cinco pasos del hijo estan dentro de la madre y en el mismo orden, y que EL ESCALON BAJA EN VEZ DE SUBIR: donde la madre dice menos de mil dolares y un mes, el hijo dice baratas y de corto plazo. Ademas la razon cuenta CUATRO piezas que se perderian del lado de la madre contra UNA del lado del hijo, y por eso escribe que la direccion de la fusion esta casi decidida.",
            "pasos": {
                "1": ["CUBIERTO", 2],
                "2": ["INCISO", 3, "en AdWords, pregunta el precio en tu mercado", " Prueba "],
                "3": ["CUBIERTO", 4],
                "4": ["APPEND"],
                "5": ["INCISO", 5, "para pasar a las pruebas del anillo interno", " Es el paso previo "],
            },
            "condiciones": {"1": ["CUBIERTO", 3], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente el UNICO gesto que la razon declara propio del hijo: comparar los resultados de las estrategias probadas EN UNA HOJA DE CALCULO. DOS INCISOS, y el segundo salva LA OTRA MITAD de la perdida que la razon proponia: el nombre del anillo interno como destino, adosado al paso 5 del superviviente. El primero es el ejemplo de canal barato (AdWords) del paso 3. Su condicion 2 (recursos limitados que impiden probar todos los canales a la vez) viaja entera por ser un disparador distinto. CERO perdidas nombradas.",
        },
        {
            "orden": 41,
            "superviviente": "diseno_consecuencias_no_intencionadas",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 5 contra 4 a favor de diseno_consecuencias_no_intencionadas y condiciones 3 contra 3, empatadas: una sola vara de contenido no empatada BASTA, asi que el cableado NO habla, y se dice que EMPATABA (5 contra 5). Y LA PIEZA DECLARADA APUNTA AL MISMO LADO: la razon del puesto 1230 nombra TRES piezas que se perderian de diseno_consecuencias_no_intencionadas contra DOS del otro, y subraya que una de las tres, DISENAR SALVAGUARDAS, LIMITES DE USO Y MECANISMOS DE REVERSION, es EL UNICO PASO DEL PAR QUE REMEDIA en vez de solo anticipar: esa pieza esta a salvo por construccion.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["APPEND"],
                "3": ["INCISO", 2, "no esta en la sala de diseno pero sera afectado", " Incluye a quien "],
                "4": ["INCISO", 5, "mecanismos de monitoreo post-lanzamiento", " Establece "],
            },
            "condiciones": {"1": ["CUBIERTO", 2], "2": ["CUBIERTO", 1], "3": ["APPEND"]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son exactamente los dos que la razon declara propios del que muere: el encuadre de efectos de SEGUNDO Y TERCER ORDEN, y las dos preguntas que lo operan (que comportamientos nuevos habilita esto y que sistemas existentes altera). DOS INCISOS: quien no esta en la sala de diseno, alcance concreto del paso 2 del superviviente, que habla de quien se beneficia y quien se perjudica; y los mecanismos de monitoreo POST-LANZAMIENTO, momento concreto del paso 5, que manda revisitar los riesgos periodicamente. Su condicion 3 (ignorar los efectos sistemicos por mirar solo la funcionalidad inmediata) viaja entera por ser un disparador distinto. UNA PERDIDA NOMBRADA: su condicion 2 incluye los SISTEMAS QUE APRENDEN Y SE RETROALIMENTAN junto a los datos y la IA, y la condicion 1 del superviviente enumera IA, datos personales y biotecnologia sin nombrarlos; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra.",
        },
        {
            "orden": 42,
            "superviviente": "arquitectura_tecnica_modular",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA, Y LA PUERTA APUNTA AL MISMO LADO. Pasos 4 contra 5 a favor de arquitectura_tecnica_modular y condiciones 2 contra 2, empatadas: una sola vara no empatada BASTA, asi que el cableado NO habla, y se dice que apuntaba al mismo lado (2 contra 3). Y LA SEGUNDA VARA APUNTA IGUAL: arquitectura_tecnica_modular ES PUERTA y la guarda 1B exige que sobreviva. AQUI NO HAY CHOQUE. La razon del puesto 1257 cuenta ademas DOS piezas propias del que sobrevive contra UNA del que muere.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["CUBIERTO", 2],
                "3": ["CUBIERTO", 4],
                "4": ["INCISO", 3, "APIs abiertas para facilitar integraciones futuras", ", y que sean "],
            },
            "condiciones": {"1": ["APPEND"], "2": ["CUBIERTO", 2]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: AUDITAR primero las soluciones tecnologicas que ya existen en el mercado (nube y programas por suscripcion), que la razon llama el unico paso que manda mirar afuera ANTES de decidir nada. UN INCISO: las APIs ABIERTAS para facilitar integraciones futuras, matiz del paso 3 del superviviente, que manda conectar via APIs sin pedir que sean abiertas. Su condicion 1 (el equipo evalua construir tecnologia propia contra usar soluciones existentes) viaja entera por ser un disparador distinto. CERO perdidas nombradas.",
        },
        {
            "orden": 43,
            "superviviente": "entrenamiento_funcional_empleados",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 4 contra 4 y condiciones 2 contra 2: las dos varas de contenido empatan al digito, y la razon del puesto 1387 reconoce DOS piezas propias a cada lado, asi que tampoco la pieza declarada desempata. Con el contenido callado entero, EL CABLEADO DECIDE SOLO y apunta a entrenamiento_funcional_empleados, 2 contra 3. NO es empate sin vara porque el cableado no empata.",
            "pasos": {
                "1": ["APPEND"],
                "2": ["INCISO", 2, "para roles clave (ventas, ingenieria, gestion)", " Hazlo "],
                "3": ["APPEND"],
                "4": ["INCISO", 3, "con seguimiento de cumplimiento", " Y hazlo "],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son exactamente los dos que la razon declara propios del que muere: NO ASUMIR que la inteligencia o la experiencia previa reemplazan el entrenamiento propio de la empresa, que la razon llama la unica linea que ataca el motivo por el que no se entrena; y EXIGIR QUE LOS LIDERES DE AREA DOCUMENTEN Y ENSENEN sus procesos en vez de ejecutarlos por intuicion, la unica que pone la carga sobre quien ya sabe. DOS INCISOS: los roles clave con nombre (ventas, ingenieria, gestion), parametro del paso 2 del superviviente, y el seguimiento de cumplimiento, parametro de la obligatoriedad del paso 3. UNA PERDIDA NOMBRADA: su condicion 2 dispara al detectar que los empleados nuevos NO COMPRENDEN EL CONTEXTO COMPLETO de su trabajo, y la condicion 2 del superviviente habla de alta rotacion o baja productividad, que es otro sintoma; el INCISO para condiciones no existe en el instrumento y por eso la perdida se nombra.",
        },
        {
            "orden": 44,
            "superviviente": "convertir_necesidad_en_demanda",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 4 contra 4 y condiciones 2 contra 2: las dos varas de contenido empatan al digito, y la razon del puesto 1421 reconoce DOS piezas propias a cada lado, asi que tampoco la pieza declarada desempata. Con el contenido callado entero, EL CABLEADO DECIDE SOLO y apunta a convertir_necesidad_en_demanda, 5 contra 3. NO es empate sin vara porque el cableado no empata.",
            "pasos": {
                "1": ["INCISO", 2, "no solo preguntarles que quieren", ", y "],
                "2": ["APPEND"],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 3],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
            "nota": "DOS PASOS VIAJAN ENTEROS y son exactamente los dos que la razon declara propios del que muere: los ACTOS SIN PENSAR (thoughtless acts), las soluciones improvisadas que la gente usa para adaptarse a productos mal disenados, que la razon llama el unico nombre propio que el catalogo le da a esa senal; y evitar depender solo de encuestas o datos cuantitativos que confirman lo que ya se sabe. UN INCISO: el no solo preguntarles que quieren, contraste del paso 2 del superviviente, que manda investigacion etnografica o cualitativa sin decir contra que. SUS DOS CONDICIONES VIAJAN ENTERAS por ser disparadores distintos: contar solo con datos convencionales (encuestas, focus groups), e iniciar la fase de inspiracion de un proyecto de diseno centrado en las personas; las dos del superviviente hablan del mercado estancado y de la dependencia de la innovacion tecnologica incremental. CERO perdidas nombradas.",
        },
        {
            "orden": 46,
            "superviviente": "business_model_canvas_scorecard",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 5 contra 5 y condiciones 3 contra 3: las dos varas de contenido empatan al digito, y la razon del puesto 1468 reconoce DOS piezas propias a cada lado, asi que tampoco la pieza declarada desempata. Con el contenido callado entero, EL CABLEADO DECIDE SOLO y apunta a business_model_canvas_scorecard, 14 contra 8. NO es empate sin vara porque el cableado no empata.",
            "pasos": {
                "1": ["CUBIERTO", 1],
                "2": ["APPEND"],
                "3": ["INCISO", 2, "cada vez que obtengas nueva evidencia", ", y ademas "],
                "4": ["APPEND"],
                "5": ["APPEND"],
            },
            "condiciones": {"1": ["APPEND"], "2": ["APPEND"], "3": ["APPEND"]},
            "nota": "TRES PASOS VIAJAN ENTEROS: los DOS que la razon declara propios del que muere (conservar todas las versiones como un CUADERNO DE HOJEAR que documente la evolucion, y EVITAR convertir el lienzo en un plan operativo prematuro basado en suposiciones sin validar, que la razon llama la unica linea que pone un limite al uso del lienzo) mas salir a validar cada hipotesis con clientes reales cara a cara, que ninguno de los cinco pasos del superviviente dice, medido paso a paso. UN INCISO: la cadencia POR EVIDENCIA, adosada al paso 2 del superviviente, que solo trae la cadencia SEMANAL: el nodo queda con las dos, que es lo que la razon pedia salvar de los dos lados. SUS TRES CONDICIONES VIAJAN ENTERAS por ser disparadores distintos de las tres del superviviente, que hablan de rastrear cambios de hipotesis, de falta de claridad y de customer discovery, no del plan de negocio estatico ni de escribirlo para pedir financiamiento. EL SOLAPE QUE ESTO FABRICA SE DECLARA para la poda de la fase 04: el superviviente queda con SEIS condiciones y las tres nuevas son de la misma familia (el plan de negocio como documento rigido). CERO perdidas nombradas.",
        },
        {
            "orden": 47,
            "superviviente": "bucle_retroalimentacion_autoajustable",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 4 contra 4 y condiciones 2 contra 2: las dos varas de contenido empatan al digito, y la razon del puesto 1552 reconoce UNA pieza propia a cada lado, asi que tampoco la pieza declarada desempata. Con el contenido callado entero, EL CABLEADO DECIDE SOLO y apunta a bucle_retroalimentacion_autoajustable, 6 contra 2. NO es empate sin vara porque el cableado no empata.",
            "pasos": {
                "1": ["INCISO", 1, "para los equipos operativos", ", "],
                "2": ["APPEND"],
                "3": ["CUBIERTO", 2],
                "4": ["INCISO", 3, "no solo periodicamente", ", y "],
            },
            "condiciones": {"1": ["CUBIERTO", 2], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: ESTABLECER RECOMPENSAS O INCENTIVOS ligados al cumplimiento de las metas, que la razon llama la unica que engancha el lazo a la motivacion de las personas. DOS INCISOS: el destinatario de las metas (para los equipos operativos), parametro del paso 1 del superviviente, y la cadencia del ajuste (no solo periodicamente), matiz del paso 3. Su condicion 2 (buscar resiliencia y adaptabilidad ante un entorno VUCA) viaja entera por ser un disparador distinto. CERO perdidas nombradas.",
        },
        {
            "orden": 48,
            "superviviente": "evitar_greenwashing",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 5 contra 3 a favor de evitar_greenwashing y condiciones 2 contra 2, empatadas: una sola vara de contenido no empatada BASTA, asi que el cableado NO habla, y se dice que apuntaba al mismo lado (4 contra 2). Y LA PIEZA DECLARADA APUNTA IGUAL: la razon del puesto 1776 escribe que evitar_greenwashing_2 es un SUBCONJUNTO ESTRICTO, que sus TRES pasos tienen su correspondiente en el otro, y cuenta TRES perdidas del lado de evitar_greenwashing contra UNA del lado del que muere.",
            "pasos": {
                "1": ["INCISO", 4, "tres veces", ", verificando "],
                "2": ["CUBIERTO", 4],
                "3": ["CUBIERTO", 2],
            },
            "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
            "nota": "NINGUNA PIEZA DE PASO VIAJA ENTERA Y LA UNICA PERDIDA QUE LA RAZON PROPONIA SE SALVA: la razon proponia perder EL VERIFICAR TRES VECES antes de publicar, que llama la unica linea del dominio que pone un numero a la comprobacion, y aqui va de INCISO adosado al paso 4 del superviviente, que manda sustentar cada reclamo con datos verificables o certificaciones de terceros. Su condicion 2 (presion de marketing para exagerar logros ambientales) viaja entera por ser un disparador distinto del riesgo de escrutinio de ONGs o consumidores. CERO perdidas nombradas.",
        },
        {
            "orden": 49,
            "superviviente": "contabilidad_ambiental",
            "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO. Pasos 4 contra 4 y condiciones 2 contra 2: las dos varas de contenido empatan al digito, y la razon del puesto 1789 reconoce UNA pieza propia a un lado y DOS al otro, pero material propio declarado a LOS DOS lados EMPATA (acta 54, pregunta 4), asi que tampoco la pieza declarada desempata. Con el contenido callado entero, EL CABLEADO DECIDE SOLO y apunta a contabilidad_ambiental, 4 contra 2. NO es empate sin vara porque el cableado no empata.",
            "pasos": {
                "1": ["CUBIERTO", 2],
                "2": ["INCISO", 3, "full cost accounting, EMA", ", como "],
                "3": ["INCISO", 4, "un equipo interdisciplinario (cientificos, ingenieros, contadores)", ", o a "],
                "4": ["APPEND"],
            },
            "condiciones": {"1": ["CUBIERTO", 2], "2": ["APPEND"]},
            "nota": "UNA PIEZA VIAJA ENTERA y es una de las dos que la razon declara propias del que muere: REPORTAR LOS RESULTADOS TAMBIEN HACIA AFUERA, a los interesados externos, que la razon llama la unica linea que saca el ejercicio de la contabilidad interna. LA OTRA SE SALVA CON INCISO: el NOMBRE DE LAS HERRAMIENTAS (full cost accounting, EMA), que la razon llama lo unico que convierte la instruccion en algo buscable, adosado al paso 3 del superviviente, que manda elegir las herramientas sin nombrarlas. UN SEGUNDO INCISO: el equipo interdisciplinario con sus tres perfiles, alternativa concreta a la persona de sostenibilidad del paso 4. Su condicion 2 (reportar sostenibilidad a inversionistas o reguladores) viaja entera por ser un disparador distinto. CERO perdidas nombradas.",
        },
        {
            "orden": 50,
            "superviviente": "reduccion_cargas_regulatorias",
            "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA. Pasos 4 contra 4, empatados, y condiciones 1 contra 2 a favor de reduccion_cargas_regulatorias: una sola vara de contenido no empatada BASTA, asi que el cableado NO habla, y se dice que apuntaba al mismo lado (2 contra 3). Y LA PIEZA DECLARADA APUNTA IGUAL: la razon del puesto 1791 cuenta DOS perdidas del lado de reduccion_cargas_regulatorias (el encuadre POSITIVO de priorizar los materiales mejor calificados en nuevos productos, y el nombre de la herramienta, LA LISTA VERDE) contra UNA del lado del que muere.",
            "pasos": {
                "1": ["INCISO", 1, "procesos de manufactura", ", y tambien en los "],
                "2": ["CUBIERTO", 2],
                "3": ["APPEND"],
                "4": ["CUBIERTO", 4],
            },
            "condiciones": {"1": ["CUBIERTO", 1]},
            "nota": "UNA PIEZA VIAJA ENTERA y es exactamente la que la razon declara propia del que muere: el encuadre NEGATIVO, priorizar el rediseno de productos para ELIMINAR los materiales de alto riesgo regulatorio, que la razon llama la unica formulacion que ataca lo que YA ESTA en el producto. El nodo queda con los dos encuadres, el positivo del superviviente y el negativo del que muere. UN INCISO: el alcance del mapeo (y procesos de manufactura), que el paso 1 del superviviente acota a cada producto. Su unica condicion queda cubierta. CERO perdidas nombradas.",
        },
    ],
    "declarados": [
        {
            "orden": 37,
            "miembros": ["seis_herramientas_comunicacion_celebracion",
                         "seis_herramientas_comunicacion_fase_activate"],
            "especie": "EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN",
            "motivo": "LAS DOS VARAS DE CONTENIDO EMPATAN AL DIGITO (pasos 5 contra 5 y condiciones 1 contra 1) Y EL CABLEADO TAMBIEN EMPATA (2 contra 2 en el cuadro de varas). El empate sin vara exige exactamente eso, que TAMBIEN el cableado empate (acta 53, pregunta 4), y aqui se cumple. Y LA PIEZA DECLARADA NO DESEMPATA porque hay material propio declarado a LOS DOS lados: la razon del puesto 1068 escribe que lo propio de seis_herramientas_comunicacion_celebracion es atarlo al logro (disenar el mensaje para el hito concreto y enviarlo justo tras confirmarlo) y que lo propio de seis_herramientas_comunicacion_fase_activate son DOS gestos de diagnostico (identificar cual es el primer contacto real despues de la compra, y ponerle una nota del uno al diez a la experiencia actual antes de mejorarla). Sin vara que separe, el acto SE DECLARA y acumula.",
            "acumula_para": "LA MESA. Y con un dato de familia que la propia razon aporta y conviene que la mesa tenga delante: este par cierra el tratamiento de la serie de los seis medios de Coleman, porque prueba que LAS INSTANCIAS POR FASE TAMBIEN SE REPITEN ENTRE ELLAS, no solo los dos nodos generales. La serie esta duplicada tantas veces como fases la instancien, y eso es una decision de catalogo, no de par.",
        },
        {
            "orden": 45,
            "miembros": ["framework_flujos_de_datos_ppp", "framework_ppph_flujos"],
            "especie": "EMPATE SIN VARA: NI EL CONTENIDO NI EL CABLEADO SEPARAN",
            "motivo": "LAS DOS VARAS DE CONTENIDO EMPATAN AL DIGITO (pasos 5 contra 5 y condiciones 2 contra 2) Y EL CABLEADO TAMBIEN EMPATA (3 contra 3). Se cumple la exigencia del empate sin vara (acta 53, pregunta 4). Y LA PIEZA DECLARADA NO DESEMPATA porque hay material propio declarado a LOS DOS lados, y ademas en la misma cantidad: la razon del puesto 1438 nombra DOS perdidas de cada lado (de framework_flujos_de_datos_ppp, QUIEN CONTROLA cada parte y si el ritmo beneficia a los usuarios O SOLO AL SISTEMA; de framework_ppph_flujos, si el proposito tiene PROPOSITOS SECUNDARIOS EN CONFLICTO y que pasa cuando alguien opera FUERA DEL RITMO ESPERADO). Sin vara que separe, el acto SE DECLARA y acumula.",
            "acumula_para": "LA MESA. La propia razon lo llama la trampa de identificador MAS LIMPIA de todas: son el mismo marco, uno nombrado por las tres primeras letras y el otro por las cuatro, con LOS CINCO PASOS CORRESPONDIENDOSE UNO A UNO en el mismo orden y con los mismos nombres. Que un par tan limpio no se pueda fundir por falta de vara es exactamente el caso que hace visible el pendiente de doctrina 1.",
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
    print("GENERADOR DEL PLAN DEL LOTE %s DEL TRAMO 3 (vuelta 56)" % a.lote)
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
    destino = os.path.join(SALIDA, "PLAN_V56_OPU01_LOTE_%s.json" % a.lote)
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
