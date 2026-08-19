# -*- coding: utf-8 -*-
"""ACTO 392 de OP-D-06: metricas_de_adquisicion_activacion con build_metrics_toolset.

LO UNICO TECLEADO: los grupos, sus motivos y la lectura. La medicion la hace
scripts/loop/vuelta41_plan_acto.py contra el grafo.
"""

SUP = "metricas_de_adquisicion_activacion"
ABS = ["build_metrics_toolset"]
PREF = {"M": SUP, "B": ABS[0]}

OPERACION = ("OP-D-06, ACTO 6 DE NUEVE (puesto 392): "
             "metricas_de_adquisicion_activacion absorbe a build_metrics_toolset")

ESTADO = (
    "SELLADO en la vuelta 44, 19 ago 2026, ANTES de ejecutar. EL DESTEJIDO QUE LA "
    "RAZON PEDIA YA SE HIZO, y no aqui: lo hizo OP-F-04-WEI. La razon del archivo "
    "dice que el segundo de los dos tiene NUEVE pasos y que del 6 al 9 entra otro "
    "bloque (definir que es una conversion, calcular clics y costo por campana, "
    "comparar costo de adquisicion contra valor de vida, y usar SEM para aprender "
    "que mensaje funciona), y esta RANCIA EN ESE DETALLE. docs/plan/01_FUENTES.md "
    "linea 952 publica la frontera leida (1 a 5 contra 6 a 9) y la linea 985 "
    "publica el miembro receptor (sem_estrategia_ejecucion) con su motivo. LA "
    "MEDICION DE HOY LO CONFIRMA POR PARTIDA DOBLE: "
    "metricas_de_adquisicion_activacion tiene CINCO pasos, que son exactamente los "
    "cinco primeros, y el commit que lo corto es 1eef1c6b (OP-F-04-WEI segunda "
    "tanda), medido con git show sobre el fichero, 9 pasos antes y 5 despues. Y EL "
    "BLOQUE NO SE PERDIO: los pasos 9 a 12 de sem_estrategia_ejecucion, leidos hoy "
    "del grafo, son las cuatro piezas una a una (definir que es una conversion, "
    "CTR y CPC y CPA por campana, comparar el costo de adquisicion contra el LTV, "
    "y usar SEM para aprender que mensaje funciona). Fuente primero satisfecha POR "
    "PRECEDENCIA, con OP-F-04-WEI HECHA en su nota 3541 SI segun la apertura de "
    "esta vuelta. LO QUE EL INSTRUMENTO DE COSTURAS CITA HOY SE DICE EN VEZ DE "
    "CALLARSE, y esta vez es lo mas simple que ha dado la operacion: LOS DOS "
    "NODOS ESTAN FUERA de la cola de 1.493. El instrumento NO cita a ninguno de "
    "los dos, asi que no hay cita que registrar ni que despachar.")

REGLA = (
    "OP-D-06 de docs/plan/02_DESTEJIDOS.md, LOS NUEVE ACTOS DE DOS, acto del "
    "puesto 392 de su tabla sellada. ESTE ACTO SI TIENE REPARTO ESCRITO, y es uno "
    "de los DOS unicos que lo tienen (el otro es el 341). La tabla sellada dice, "
    "en la linea 1143 de ese fichero leida hoy: 'en la fusion: que el sistema "
    "escale luego a retencion y cohortes, de build_metrics_toolset. Con el "
    "destejido: definir que es una conversion, comparar el CAC contra el LTV, y "
    "usar SEM para aprender que mensaje funciona'. SE CUMPLE TAL COMO ESTA, Y LAS "
    "DOS MITADES SE VERIFICAN POR SEPARADO: la mitad DEL DESTEJIDO ya esta "
    "descargada por OP-F-04-WEI y comprobada contra el grafo (las tres piezas "
    "viven hoy en sem_estrategia_ejecucion, pasos 9, 11 y 12); la mitad DE LA "
    "FUSION es trabajo de este acto y viaja al grupo 6, con 'retención' y "
    "'cohortes' en preservar_literal para que una guarda lo compruebe en vez de "
    "confiarlo. Y EL 'DE build_metrics_toolset' DE ESA LINEA ES LO QUE NOMBRA AL "
    "DONANTE: solo se manda preservar una pieza DE alguien cuando ese alguien "
    "deja de existir. El reparto escrito y la lectura de contenido apuntan al "
    "mismo superviviente, asi que no hay contradiccion que traer y no hay parada.")

MOTIVO = (
    "El acto se leyo ENTERO por P.5 y es UNA familia de DOS: el par 392 es A en el "
    "archivo y los OCHO pares que meten un tercero (681, 699, 900, 990, 1011, "
    "1226, 1282, 1545) son los ocho D. CERO terceros de clase A, asi que el acto "
    "es de dos, como la tabla sellada dice. Y ES EL ACTO CON MAS TERCEROS DE TODA "
    "LA OPERACION, ocho contra los cuatro del 344 y los dos del 361, lo que dice "
    "que este par vive en el barrio mas poblado del catalogo (metricas): la guarda "
    "de transitividad sobre las A es justo la que impide que ese barrio se cuele "
    "en el acto. CERO pares vuelven a la cola de relectura post fusion, porque "
    "entre los ocho terceros no hay ni un B ni un C. LA FUENTE, DICHA COMO SE MIDE "
    "Y NO COMO CONVIENE: el instrumento medira DOS cadenas distintas e imprimira "
    "FUENTE MIXTA, pero las dos nombran EL MISMO LIBRO ('The Startup Owner's "
    "Manual' contra 'The Startup Owner's Manual - Steve Blank'), que es la misma "
    "diferencia de forma y no de libro que salio en el 331, el 341 y el 344. La "
    "fuente del superviviente NO se toca.")

# ---------------------------------------------------------------------------
# LOS GRUPOS. Diez origenes de paso en SEIS pasos, dentro del estandar de 3 a 6,
# y cuatro origenes de condicion en CUATRO condiciones.
# ---------------------------------------------------------------------------
GRUPOS_PASOS = [
    (["M1", "B1"],
     "Define qué relación quieres tener con tus clientes, que es una de las "
     "hipótesis de tu modelo de negocio, y a partir de ahí decide qué métricas te "
     "dirán si vas bien",
     "EL MISMO ARRANQUE CON SU PROCEDENCIA. Los dos empiezan por la relacion con "
     "el cliente: el superviviente manda definirla y sacar de ahi las metricas, y "
     "el donante manda identificarla como HIPOTESIS DEL MODELO DE NEGOCIO. La "
     "pieza del donante no es otra accion, es de donde sale la del superviviente, "
     "y separarlas dejaria un primer paso que manda definir una relacion sin decir "
     "de que documento se saca. Se funden porque son el mismo momento, que es la "
     "vara del 344 y del 341."),
    (["M2", "B2"],
     "Quédate con menos de 12 métricas accionables, todas deben ayudarte a decidir "
     "algo, y organízalas en adquisición, activación y referidos",
     "EL MISMO TOPE CON SUS TRES GRUPOS NOMBRADOS. Los dos mandan quedarse en "
     "menos de doce y los dos piden que sirvan para decidir; el donante ademas "
     "NOMBRA en el paso los tres grupos en que se organizan, y el superviviente "
     "solo nombraba dos y en su resumen, no en el paso, que es justo donde hacen "
     "falta. LOS REFERIDOS SON LA UNICA PIEZA DE ESTE ACTO QUE ENSANCHA EL ALCANCE "
     "Y SE DICE ASI EN VEZ DE COLARLA: entran como CATEGORIA de la seleccion, no "
     "como medicion propia, porque ningun paso del acto manda medir referidos. "
     "Perderla seria borrar en la fusion lo unico que el donante nombraba de mas."),
    (["B3"],
     "Instrumenta tu producto para capturar cada clic y de qué fuente de tráfico "
     "viene",
     "PIEZA PROPIA DEL DONANTE, sin equivalente en ningun paso del superviviente, "
     "y es la mas cara de perder del acto: es el UNICO paso que dice como se "
     "consiguen los datos. El superviviente lo daba por hecho (su resumen dice "
     "'mide cada clic', pero su procedimiento arranca ya con los datos puestos), y "
     "un tablero de metricas sin el producto instrumentado detras es un tablero "
     "vacio. Va en tercer lugar a proposito, entre elegir que medir y medirlo, "
     "porque es lo que hay que hacer en medio."),
    (["M3"],
     "Mide tus métricas de adquisición: visitas totales, de dónde vienen, cuántas "
     "convierten y cuánto te cuesta conseguir cada cliente",
     "PIEZA PROPIA DEL SUPERVIVIENTE, y es la mitad del corazon del acto. El "
     "donante nombra el grupo 'adquisicion' y no dice ni una sola metrica suya; "
     "aqui estan las cuatro con nombre. Va en grupo propio porque medir la "
     "adquisicion y medir la activacion son dos mediciones distintas sobre dos "
     "poblaciones distintas, y juntarlas en un paso convertiria el paso mas util "
     "del acto en una lista de ocho cosas."),
    (["M4"],
     "Mide tus métricas de activación: cuántos o qué porcentaje se activa según la "
     "fuente, cuánto cuesta cada activación y qué tan buena es la calidad de esos "
     "usuarios",
     "PIEZA PROPIA DEL SUPERVIVIENTE, y es la otra mitad del corazon. Misma razon "
     "que el anterior y una mas: esta es la que cruza la activacion CON LA FUENTE, "
     "que es lo que permite comparar canales, y es la unica linea de los dos nodos "
     "que habla de la CALIDAD de los usuarios y no solo de su numero."),
    (["M5", "B4", "B5"],
     "Arma o compra un tablero en tiempo real que resuma el comportamiento clave "
     "de tus usuarios y las tendencias que te ayuden a decidir, y móntalo de forma "
     "que pueda crecer luego a métricas de retención y de cohortes",
     "EL MISMO CIERRE CON SU FORMA, SU PLAZO Y SU FUTURO. Las tres piezas hablan "
     "del MISMO artefacto y por eso van juntas: el superviviente dice QUE tiene "
     "que resumir el tablero (comportamiento clave y tendencias), el donante dice "
     "que se puede COMPRAR en vez de construir y que va EN TIEMPO REAL, y su "
     "ultima pieza dice que el sistema tiene que poder crecer a retencion y "
     "cohortes. ESTA ULTIMA ES LA QUE EL REPARTO ESCRITO DE LA TABLA SELLADA MANDA "
     "PRESERVAR EN LA FUSION, con esas palabras, y por eso 'retención' y "
     "'cohortes' van ademas en preservar_literal. Y NO ENSANCHA EL ALCANCE DEL "
     "NODO: manda que el sistema PUEDA escalar, no que se midan hoy la retencion "
     "ni las cohortes, que es la misma frontera entre preparar y ejecutar que el "
     "acto 344 dejo adjudicada."),
]

GRUPOS_CONDICIONES = [
    (["MC1"],
     "Cuando necesitas decidir en qué invertir basándote en datos reales de "
     "comportamiento",
     "EL DISPARADOR DE LA DECISION DE DINERO, propio del superviviente. Se queda "
     "solo porque es el unico de los cuatro que dice PARA QUE se monta todo esto: "
     "no para tener un tablero, sino para decidir donde va el dinero."),
    (["BC1"],
     "Cuando tu producto ya está en la fase de validar clientes y necesitas medir "
     "el comportamiento real de tus usuarios",
     "EL DISPARADOR QUE NOMBRA LA FASE DEL METODO, propio del donante, y NO se "
     "funde con el anterior. Es la misma vara del 344: el unico de los cuatro que "
     "dice DONDE del metodo de Blank esta parado el que lee, y esa ubicacion es lo "
     "que distingue este tablero de un panel de analitica cualquiera. Disolverlo "
     "en el de arriba borraria la unica puerta que abre por fase."),
    (["MC2"],
     "Si todavía no tienes forma de medir el camino completo que recorre alguien "
     "hasta convertirse en cliente",
     "LA CARENCIA DE INSTRUMENTO, propia del superviviente: no es que no sepas que "
     "mirar, es que NO PUEDES medir. Es la puerta que atiende el paso de "
     "instrumentar el producto, y por eso no se funde con la de abajo, "
     "que atiende a otro paso."),
    (["BC2"],
     "Si tu equipo no tiene claro qué datos son los relevantes para decidir en el "
     "negocio",
     "LA CARENCIA DE CRITERIO, propia del donante: aqui SI puedes medir y lo que "
     "falta es saber QUE. Es la puerta que atiende el paso de quedarse en menos de "
     "doce metricas accionables, y es una carencia distinta de la de arriba, no un caso "
     "suyo. LAS CUATRO CONDICIONES SE QUEDAN SEPARADAS Y SE DICE POR QUE: son DOS "
     "momentos (decidir inversion, entrar en validacion) y DOS carencias (no poder "
     "medir, no saber que medir), y ninguna es un caso particular de otra. Es la "
     "misma lectura que el acta de la vuelta 43 adjudico a favor en su D6, donde "
     "tres condiciones eran tres entradas distintas al mismo procedimiento."),
]

ENTREGABLE = (
    "Un tablero en tiempo real con menos de 12 indicadores que te ayuden a "
    "decidir, cubriendo adquisición, activación y referidos, alimentado por tu "
    "producto ya instrumentado y montado de forma que pueda crecer luego a "
    "retención y cohortes")

RESUMEN = (
    "Si tienes un negocio web o de aplicación, instrumenta el producto para medir "
    "cada clic y ver el camino completo que recorre alguien hasta convertirse en "
    "cliente (el embudo de conversión). Parte de qué relación quieres tener con "
    "tus clientes, que es una de las hipótesis de tu modelo de negocio, y elige "
    "menos de una docena de métricas accionables que te ayuden a decidir, "
    "organizadas en cuántos llegan, qué tan rápido, cuánto te cuesta y qué tan "
    "buenos son esos clientes, y agrupadas en adquisición, activación y referidos. "
    "Mide la adquisición con visitas totales, de dónde vienen, cuántas convierten "
    "y cuánto te cuesta conseguir cada cliente; mide la activación con cuántos o "
    "qué porcentaje se activa según la fuente, cuánto cuesta cada activación y qué "
    "tan buena es la calidad de esos usuarios. El resultado se arma o se compra "
    "como un tablero en tiempo real que resume el comportamiento clave y las "
    "tendencias, y que se monta de forma que pueda crecer luego a métricas de "
    "retención y de cohortes sin rehacerlo.")

PRESERVAR = [
    "referidos",
    "retención",
    "cohortes",
    "cada clic",
    "fuente de tráfico",
    "visitas totales",
    "calidad de esos usuarios",
    "menos de 12",
    "tiempo real",
    "modelo de negocio",
]

RASTROS = [
    "accionables",
    "embudo",
    "tablero",
    "adquisición",
    "activación",
    "tendencias",
]

ELECCION_P8 = {
    "regla": ("P.8, EL CABLEADO DESEMPATA, NO DECIDE. Donde el contenido dice algo "
              "manda el contenido, aunque el margen de aristas apunte al otro lado."),
    "decide": "EL CONTENIDO",
    "elegido": SUP,
    "especie_de_9_3_1": ("POR ELEGIR. La razon del unico par A del acto (el 392) NO "
                         "nombra ganador: la vara del verbo da NO. No hay GANADOR "
                         "POR DERECHO, asi que la eleccion es de P.8. LO QUE SI HAY, "
                         "y es lo que distingue a este acto de los cinco anteriores, "
                         "es REPARTO ESCRITO en la tabla sellada, y su redaccion "
                         "nombra al donante sin nombrarlo: manda preservar en la "
                         "fusion una pieza 'DE build_metrics_toolset'."),
    "lectura_de_contenido": [
        "1. UNO DICE QUE MEDIR Y EL OTRO SOLO DICE QUE HAY QUE MEDIR, y esa es la "
        "diferencia entera. build_metrics_toolset nombra los grupos "
        "('adquisicion, activacion, referidos') y NO da una sola metrica; "
        "metricas_de_adquisicion_activacion da SIETE con nombre en dos pasos: "
        "visitas totales, de donde vienen, cuantas convierten, cuanto cuesta "
        "conseguir cada cliente, que porcentaje se activa segun la fuente, cuanto "
        "cuesta cada activacion, y que tan buena es la calidad de esos usuarios. "
        "Es EXACTAMENTE la segunda aplicacion escrita de P.8, la del acto II del "
        "racimo del pivote: alli sobrevivio el que llevaba el material propio "
        "aunque el cableado fuera diez contra cinco. Aqui el material propio y el "
        "cableado van del mismo lado, asi que la regla no tiene ni que forzarse.",
        "2. EL REPARTO ESCRITO DE LA TABLA SELLADA NOMBRA AL DONANTE. La linea "
        "1143 de docs/plan/02_DESTEJIDOS.md manda preservar 'en la fusion: que el "
        "sistema escale luego a retencion y cohortes, DE build_metrics_toolset'. "
        "Una pieza solo se manda rescatar DE alguien cuando ese alguien deja de "
        "existir: si build_metrics_toolset sobreviviera, su paso 5 no necesitaria "
        "que nadie lo preservara. Y la otra mitad de la misma linea ('con el "
        "destejido: definir que es una conversion, comparar el CAC contra el LTV, "
        "y usar SEM') son los pasos 6 a 9 DEL SUPERVIVIENTE, que es de quien "
        "habla la fila entera. Esto es contenido del plan sellado, no cableado.",
        "3. LA VARA DEL ALCANCE DEL ROL, Y AQUI ES DONDE APRIETA, ASI QUE SE DICE "
        "ENTERA EN VEZ DE ELEGIR EL LADO COMODO. P.8 cuenta como contenido el "
        "alcance del rol, y el acta de la vuelta 43 (D3) extendio la vara a la "
        "direccion inversa: un nodo tampoco se llama por dos grupos cuando su "
        "procedimiento cubre tres. El titulo del superviviente dice "
        "'(adquisicion y activacion)' y el resultado nombrara ademas 'referidos'. "
        "LA LECTURA FINA, medida sobre los seis pasos del resultado: los unicos "
        "dos pasos que MIDEN son el 4 (adquisicion) y el 5 (activacion). Ningun "
        "paso manda medir referidos, ni retencion, ni cohortes: los referidos "
        "entran como CATEGORIA de la seleccion del paso 2 y las cohortes como "
        "CAPACIDAD FUTURA del tablero del paso 6. La frontera entre preparar y "
        "ejecutar es la que el acto 344 dejo adjudicada por el acta ('los dos la "
        "DEJAN LISTA, que no es lo mismo'). El titulo nombra lo que el "
        "procedimiento MIDE, y eso sigue siendo adquisicion y activacion. LA "
        "TENSION SE DECLARA IGUAL, y va marcada como discutible del reporte.",
        "4. EL TITULO DEL DONANTE NO SE PUEDE ARREGLAR EN UNA FUSION, Y ESO "
        "IMPORTA PARA ELEGIR. La guarda 12 del ejecutor (a6 del acta) obliga a "
        "dejar titulo y etiqueta del superviviente INTACTOS, asi que lo que se "
        "elige aqui es el nombre definitivo del resultante. El del donante es "
        "'Construir un Toolset de Metricas Clave' con etiqueta 'Arma tu Set de "
        "Metricas': dos anglicismos crudos ('Toolset', 'Set') en un catalogo cuyo "
        "canon de voz prohibe la jerga (docs/BANCO_DE_TEXTOS.md). Y sus cinco "
        "pasos estan en infinitivo ('Identificar', 'Seleccionar', 'Instrumentar'), "
        "que es la voz vieja anterior al redactor, mientras el superviviente ya "
        "esta en la voz de hoy ('Define', 'Quedate', 'Mide', 'Arma'). Elegir al "
        "donante congelaria esa jerga en el grafo para siempre. Es argumento de "
        "forma y va el cuarto a proposito: no decide, acompana.",
        "5. PIEZAS PROPIAS DEL DONANTE QUE NADIE MAS TIENE, y por eso viajan "
        "enteras: INSTRUMENTAR EL PRODUCTO para capturar cada clic y su fuente de "
        "trafico (el unico paso de los dos nodos que dice de donde salen los "
        "datos, y el mas caro de perder), la hipotesis de relacion como pieza DEL "
        "MODELO DE NEGOCIO, los REFERIDOS como tercer grupo de la seleccion, el "
        "'o comprar' del tablero y su 'en tiempo real', y la escalabilidad a "
        "RETENCION Y COHORTES, que es la que el reparto escrito manda preservar. "
        "Diez origenes de paso entran y diez viajan: CERO se pierden.",
    ],
    "cableado_solo_como_desempate": {
        "usado_para_decidir": False,
        "va_a_favor_del_elegido": True,
        "por_que_se_cita": (
            "PORQUE NO HIZO FALTA Y SE IMPRIME PARA PODER DECIRLO. Medido hoy: "
            "metricas_de_adquisicion_activacion tiene grado 7 y "
            "build_metrics_toolset tiene grado 6. UNA ARISTA DE MARGEN, que es "
            "exactamente el ejemplar escrito de P.8 (3 contra 2) y exactamente el "
            "caso en el que la propia regla dice que UNA ARISTA DE MARGEN NO VENCE "
            "A NINGUNA de las dos cosas que cuentan como contenido. Va a favor del "
            "elegido, y por eso NO SUMA NADA: si hubiera ido en contra tampoco "
            "habria movido la eleccion. El acto que llevo el peso de verdad fue el "
            "361, donde el cableado empato 6 a 6 y el contenido decidio solo."),
        "instrumento": ("scripts/loop/vuelta41_lectura_acto.py --puesto 392, salida "
                        "docs/loop/SALIDA_V44_ACTO392_LECTURA.txt, bloque (e)"),
        "grados_medidos_hoy": {SUP: 7, ABS[0]: 6},
        "coste_medido_de_la_eleccion": ("CERO aristas. Los dos nodos tienen CERO "
                                        "aristas propias sin reciproco, asi que "
                                        "elegir a cualquiera de los dos no pierde "
                                        "ni una arista: las reciprocas las "
                                        "reescribe la simetrizacion de run_phase1 "
                                        "paso 5."),
    },
}
