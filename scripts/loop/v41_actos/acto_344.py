# -*- coding: utf-8 -*-
"""ACTO 344 de OP-D-06: plan_de_adquisicion_acquire con plan_acquire_activate.

LO UNICO TECLEADO: los grupos, sus motivos y la lectura. La medicion la hace
scripts/loop/vuelta41_plan_acto.py contra el grafo.
"""

SUP = "plan_de_adquisicion_acquire"
ABS = ["plan_acquire_activate"]
PREF = {"D": SUP, "A": ABS[0]}

OPERACION = ("OP-D-06, ACTO 4 DE NUEVE (puesto 344): plan_de_adquisicion_acquire "
             "absorbe a plan_acquire_activate")

ESTADO = (
    "SELLADO en la vuelta 43, 19 ago 2026, ANTES de ejecutar. EL DESTEJIDO QUE LA "
    "RAZON PEDIA YA SE HIZO, y no aqui: lo hizo OP-F-04-WEI. La razon del archivo "
    "dice que uno de los dos se parte por la mitad y que del paso 8 al 12 entra el "
    "bloque de los 19 canales de traccion de Weinberg, y esta RANCIA EN ESE "
    "DETALLE: docs/plan/01_FUENTES.md linea 928 publica la frontera leida (1 a 7 "
    "contra 8 a 12) y el miembro receptor (bullseye_framework), con el saldo "
    "medido entonces de 12 pasos a 7. LA MEDICION DE HOY LO CONFIRMA: "
    "plan_de_adquisicion_acquire tiene SIETE pasos. Fuente primero satisfecha POR "
    "PRECEDENCIA, con OP-F-04-WEI HECHA en su nota 3541 SI segun la apertura de "
    "esta vuelta. Y EL PROPIO ARCHIVO YA HABIA DICHO POR QUE ESTA FUSION SE PUEDE "
    "HACER PESE A LA COSTURA: docs/INTRA_DOMINIO_INFORME.md linea 1996 dice que el "
    "solape con plan_acquire_activate cae ENTERO en el bloque 1 a 7, el de Blank, "
    "y NO TOCA LA JUNTURA. LO QUE EL INSTRUMENTO SIGUE CITANDO HOY SE DICE EN VEZ "
    "DE CALLARSE: los DOS estan DENTRO de la cola, plan_de_adquisicion_acquire con "
    "bloque 48,4 y corte tras 4, y plan_acquire_activate con bloque 47,3 y corte "
    "tras 5. Ninguna de las dos citas es la costura vieja de Weinberg, que ya no "
    "existe en el fichero, y la lectura textual con el texto delante dice que NO "
    "hay costura en ninguno de los dos: los dos son UNA sola narracion que va de "
    "preparar la prueba a correrla, y los bloques que el instrumento parte "
    "CONTINUAN en vez de volver a contar. Las dos citas quedan REGISTRADAS en la "
    "cola y no despachadas, y el auditor las relee.")

REGLA = (
    "OP-D-06 de docs/plan/02_DESTEJIDOS.md, LOS NUEVE ACTOS DE DOS, acto del "
    "puesto 344 de su tabla sellada. Este acto NO tiene reparto escrito en esa "
    "tabla (solo lo tienen el 392 y el 341), asi que se resuelve con la regla "
    "adjudicada el 11 ago 2026: cada perdida al bloque del que proviene, y la que "
    "no tenga bloque al superviviente. PERO EL ARCHIVO SI DEJO ESCRITO QUE HAY QUE "
    "SALVAR DOS PIEZAS EN ESTA FUSION, y se cumple: docs/INTRA_DOMINIO_INFORME.md "
    "lineas 1999 a 2003 corrige la lectura de las cuatro perdidas anotadas del par "
    "y dice que DOS son del bloque Bullseye (los 19 canales y anotar lo que falla) "
    "y por lo tanto NO se pierden en esta fusion porque se fueron con el "
    "destejido, y que LAS QUE DE VERDAD HAY QUE SALVAR AQUI SON LAS OTRAS DOS: EL "
    "TOPE BAJO POR PRUEBA Y LAS PRUEBAS ESCALONADAS. Las dos viven en el "
    "superviviente y las dos viajan al resultado por plan, con 'escalonada' en "
    "preservar_literal para que una guarda lo compruebe en vez de confiarlo.")

MOTIVO = (
    "El acto se leyo ENTERO por P.5 y es UNA familia de DOS: el par 344 es A en el "
    "archivo y los cuatro pares que meten un tercero (1131, 1276, 1287, 1403) son "
    "los cuatro D. CERO terceros de clase A, asi que el acto es de dos, como la "
    "tabla sellada dice. CERO pares vuelven a la cola de relectura post fusion, "
    "porque entre los cuatro terceros no hay ni un B ni un C. LA FUENTE, DICHA "
    "COMO SE MIDE Y NO COMO CONVIENE: el instrumento medira DOS cadenas de fuente "
    "distintas y por eso imprimira FUENTE MIXTA, pero las dos nombran EL MISMO "
    "LIBRO Y AL MISMO AUTOR, The Startup Owner's Manual de Steve Blank; lo unico "
    "que las separa es el ORDEN del nombre ('Blank, Steve' en el superviviente y "
    "'Steve Blank' en el absorbido). Es la tercera vez seguida en esta operacion "
    "que la etiqueta FUENTE MIXTA sale de una diferencia de forma y no de libro, y "
    "se deja escrito para que se pueda auditar como patron del instrumento.")

# ---------------------------------------------------------------------------
# LOS GRUPOS. Diecisiete origenes en SEIS pasos y DOS condiciones. Los seis
# pasos quedan DENTRO del estandar de 3 a 6, en su borde alto.
# ---------------------------------------------------------------------------
GRUPOS_PASOS = [
    (["D1", "A1"],
     "Revisa las hipótesis de segmentos de clientes, relaciones y propuesta de "
     "valor que trazaste en tu mapa del modelo de negocio, y define a qué "
     "segmento le vas a hablar con lo que aprendiste hablando con clientes "
     "(customer discovery)",
     "EL MISMO ARRANQUE CON SUS DOS ANCLAS, y ninguna de las dos era completa "
     "sola. El superviviente ancla al papel (las hipotesis que YA ESCRIBISTE en "
     "el mapa del modelo de negocio) y el donante ancla a la calle (lo que te "
     "DIJERON los clientes en customer discovery). El metodo de Blank pide las "
     "dos: la hipotesis sin la calle es una suposicion y la calle sin la "
     "hipotesis no se puede contrastar contra nada. Y la accion es la misma en "
     "los dos, decidir a que segmento le hablas antes de gastar un peso."),
    (["D2", "A2"],
     "Para cada actividad define quién la hace, qué táctica usas (posicionamiento "
     "en buscadores SEO, anuncios pagos PPC, correo, referidos), cuánto "
     "presupuesto le das, en cuánto tiempo la corres y qué meta medible persigues",
     "LA MISMA TABLA CON SUS TACTICAS NOMBRADAS. El superviviente da las CINCO "
     "columnas (quien, que tactica, cuanto, en cuanto tiempo y que meta) y NO "
     "nombra ni una tactica; el donante nombra cuatro (SEO, PPC, correo, "
     "referidos) y no da las columnas. Una columna que se llama tactica y no trae "
     "ni un ejemplo es un hueco para el que la rellena, y una lista de tacticas "
     "sin presupuesto ni plazo ni meta no es un plan. Juntas son la fila entera."),
    (["D3", "A4"],
     "Establece antes de cada prueba qué resultado la hace pasar o fracasar, con "
     "el número concreto que lo decide",
     "EL MISMO PASA O FALLA CON SU NUMERO. El superviviente manda establecer que "
     "resultado la hace pasar o fracasar y no dice en que se expresa; el donante "
     "dice que se decide CON UN NUMERO. Un pasa o falla sin numero se convierte "
     "en una opinion despues del hecho, que es exactamente lo que este paso "
     "existe para impedir. Y los dos coinciden en lo que de verdad importa: se "
     "decide ANTES de lanzar."),
    (["D4", "A5"],
     "Instrumenta tu sitio, tu app o tu producto para capturar cada acción del "
     "cliente antes de lanzar cualquier prueba",
     "LA MISMA INSTRUMENTACION CON SU OBJETO AMPLIADO. El superviviente dice "
     "SITIO O APP y el donante dice TU PRODUCTO, que cubre lo que no es ni un "
     "sitio ni una app; y donde el superviviente dice datos de COMPORTAMIENTO el "
     "donante dice CADA ACCION QUE HACE EL CLIENTE, que es lo mismo dicho con la "
     "unidad que se mide. Se toman las dos ampliaciones porque no se estorban: la "
     "instruccion queda buena para un local fisico igual que para una web."),
    (["D5", "D6", "A3", "A7"],
     "Lanza las pruebas de forma escalonada, no todas a la vez, para poder medir "
     "cada resultado por separado, con el gasto de cada prueba limitado a una "
     "cifra que puedas permitirte y preguntada en tu mercado antes de "
     "comprometerte, y escala con más fuerza y más presupuesto solo lo que de "
     "verdad funcione",
     "LA DISCIPLINA ENTERA DE CORRER LAS PRUEBAS, en un solo paso porque son una "
     "sola decision: cuantas a la vez, con cuanto dinero y que se hace con lo que "
     "gana. AQUI ESTAN LAS DOS PIEZAS QUE EL ARCHIVO MANDO SALVAR EN ESTA FUSION "
     "(docs/INTRA_DOMINIO_INFORME.md lineas 1999 a 2003): las pruebas ESCALONADAS "
     "y el TOPE BAJO por prueba, y las dos viajan literales. El donante anade dos "
     "cosas que el superviviente no tenia: PREGUNTAR cuanto cuesta cada tactica "
     "en tu mercado antes de comprometerte, y que el escalado es CON MAS FUERZA Y "
     "MAS PRESUPUESTO y no solo un permiso de seguir. Se agrupan y no se parten "
     "porque separar el tope del escalado deja el tope sin su premio y el "
     "escalado sin su freno."),
    (["D7", "A6"],
     "Asegúrate de que todo lo que activa a un cliente (el sistema detrás, los "
     "pagos, los correos de confirmación) esté listo antes de lanzar la "
     "adquisición",
     "LA MISMA PLOMERIA DE ACTIVACION, y los dos la dicen casi con las mismas "
     "palabras y en el mismo sitio: la ULTIMA, aunque sea un requisito PREVIO. Se "
     "respeta ese orden porque es deliberado en los dos originales: se escribe al "
     "final para que quien ya tiene el plan hecho no lance sin la plomeria. Es la "
     "unica pieza del acto que trae el nombre ACTIVAR, y por eso viaja entera y "
     "con sus tres ejemplares nombrados (sistema, pagos, correos de "
     "confirmacion)."),
]

GRUPOS_CONDICIONES = [
    (["DC1"],
     "Cuando entras en la fase de validar clientes (customer validation) y "
     "necesitas probar qué canales de adquisición funcionan",
     "EL DISPARADOR QUE NOMBRA LA FASE DEL METODO, propio del superviviente. Se "
     "queda solo porque es el unico de los tres origenes de condicion que dice "
     "DONDE del metodo de Blank esta parado el que lee, y esa ubicacion es lo que "
     "distingue este plan de un plan de marketing cualquiera."),
    (["DC2", "AC1"],
     "Si todavía no sabes qué canal te trae clientes al menor costo, sea por "
     "internet, por celular o en un local físico",
     "EL MISMO DESCONOCIMIENTO CON SUS TRES TERRENOS, y fundir aqui NO borra una "
     "senal: le anade la que faltaba. El superviviente dice QUE no sabes (que "
     "canal te trae clientes al menor costo) y el donante dice DONDE se prueba "
     "(internet, celular o local fisico), que el superviviente no nombraba en "
     "ninguna de sus dos condiciones. La vara es la misma que en el acto 341: se "
     "funde lo que es el mismo momento y se separa lo que no, y este es el mismo "
     "momento con mas terreno."),
]

ENTREGABLE = (
    "Tu plan de adquisición de una página, con las tácticas nombradas, el "
    "presupuesto, quién hace qué, el cronograma y la meta medible de cada prueba, "
    "con su número de pasar o fracasar decidido de antemano, más tu sistema de "
    "datos ya activo para medir cada acción del cliente")

RESUMEN = (
    "Es un documento táctico de una página donde detallas los experimentos con "
    "los que vas a atraer clientes de forma predecible y a bajo costo hacia tu "
    "embudo de ventas, y con los que vas a convertirlos en usuarios activos o "
    "compradores. Te apoyas en dos anclas y no en una: las hipótesis de "
    "segmentos, relaciones y propuesta de valor que ya trazaste en tu mapa del "
    "modelo de negocio, y lo que aprendiste hablando con clientes (customer "
    "discovery). Cada prueba lleva su táctica nombrada (SEO, PPC, correo, "
    "referidos), su responsable, su presupuesto con tope, su plazo y el número "
    "que decide si va a pasar o fracasar, fijado antes de lanzarla. Las pruebas "
    "se lanzan de forma escalonada y no todas a la vez, para poder medir cada "
    "resultado por separado, y solo se escala con más fuerza y más presupuesto lo "
    "que de verdad funcionó. Nada de esto se lanza antes de que esté lista la "
    "plomería que activa al cliente: el sistema detrás, los pagos y los correos "
    "de confirmación. En esta etapa tu meta es aprender qué canales funcionan, no "
    "generar ingresos ni lanzar el producto de forma oficial.")

PRESERVAR = [
    "escalonada",
    "SEO",
    "PPC",
    "referidos",
    "customer validation",
    "customer discovery",
    "mapa del modelo de negocio",
    "pasar o fracasar",
    "correos de confirmación",
    "local físico",
]

RASTROS = [
    "presupuesto",
    "meta medible",
    "cada acción del cliente",
    "de verdad funcione",
    "antes de lanzar la adquisición",
]

ELECCION_P8 = {
    "regla": ("P.8, EL CABLEADO DESEMPATA, NO DECIDE. Donde el contenido dice algo "
              "manda el contenido, aunque el margen de aristas apunte al otro lado."),
    "decide": "EL CONTENIDO",
    "elegido": SUP,
    "especie_de_9_3_1": ("POR ELEGIR. La razon del unico par A del acto (el 344) NO "
                         "nombra ganador: la vara del verbo da NO. No hay GANADOR "
                         "POR DERECHO, asi que la eleccion es de P.8."),
    "lectura_de_contenido": [
        "1. EL ALCANCE DEL ROL, que P.8 cuenta como contenido con el mismo peso "
        "que el texto, Y AQUI LA VARA CAE CONTRA EL TITULO MAS AMBICIOSO. "
        "plan_acquire_activate se titula 'Plan para atraer y activar clientes "
        "(Acquire/Activate)' y nombra DOS fases, pero NINGUNO de sus siete pasos "
        "describe como se activa a un cliente: su unico paso de activacion (el 6) "
        "es la PLOMERIA lista antes de atraer, que es exactamente lo que el otro "
        "nodo dice en su paso 7. O sea que la mitad ACTIVATE de su nombre no esta "
        "respaldada por su propio texto. Y el grafo ya tiene esa fase con nodo "
        "propio y vivo, plan_de_activacion, que el archivo declara DISTINTO de el "
        "en el puesto 1276 con clase D. El ejemplar de P.8 dice que una cabeza "
        "que vale para las ocho fases no puede llamarse como una sola; aqui la "
        "misma vara al reves: un nodo no puede llamarse por dos fases cuando la "
        "segunda ni la ejecuta ni le pertenece.",
        "2. LAS CONDICIONES DE ENTRADA, que son donde un nodo declara su sitio en "
        "el metodo. El superviviente nombra LA FASE ('cuando entras en la fase de "
        "validar clientes, customer validation') y nombra el problema exacto ('si "
        "todavia no sabes que canal de marketing te trae clientes al menor "
        "costo'); el donante dice 'cuando estas listo para probar como atraer "
        "clientes', que es una condicion que no ubica a nadie. El nodo que sabe "
        "en que parte del metodo vive es el que aguanta ser cabeza.",
        "3. EL ENTREGABLE DEL SUPERVIVIENTE CONTIENE AL DEL DONANTE Y ANADE UNA "
        "PIEZA. Los dos entregan un plan de una pagina con tacticas, presupuesto, "
        "quien hace que y la metrica; el superviviente entrega ademas 'tu sistema "
        "de datos ya activo para medir cada prueba'. Un plan de pruebas sin el "
        "sistema que las mide entrega la mitad del trabajo.",
        "4. LA PIEZA QUE EL ARCHIVO MANDO SALVAR VIVE SOLO EN EL SUPERVIVIENTE. "
        "docs/INTRA_DOMINIO_INFORME.md (lineas 1999 a 2003) dice que de las "
        "cuatro perdidas anotadas del par, las que de verdad hay que salvar en "
        "esta fusion son el tope bajo por prueba y LAS PRUEBAS ESCALONADAS. El "
        "tope existe en los dos; LAS ESCALONADAS EXISTEN SOLO EN EL "
        "SUPERVIVIENTE, y son la unica linea del acto que dice cuantas pruebas "
        "corren a la vez, sin la cual no se puede atribuir ningun resultado a "
        "ninguna tactica. Elegir al otro pondria la pieza mas fragil del acto a "
        "depender de que el plan la mande viajar, en vez de que ya este en casa.",
        "5. PIEZAS PROPIAS DEL DONANTE QUE NADIE MAS TIENE, y por eso viajan "
        "enteras: las cuatro tacticas nombradas (SEO, PPC, correo, referidos), el "
        "numero concreto del pasa o falla, la instrumentacion dicha sobre EL "
        "PRODUCTO y sobre CADA ACCION del cliente, preguntar el precio de la "
        "tactica en tu mercado antes de comprometerte, el escalado dicho con MAS "
        "FUERZA Y MAS PRESUPUESTO, el ancla a customer discovery, y los TRES "
        "TERRENOS de su condicion (internet, celular, local fisico). Las ocho "
        "viajan por plan y no por suerte, y cinco de ellas estan en "
        "preservar_literal o en rastros para que una guarda lo compruebe.",
    ],
    "cableado_solo_como_desempate": {
        "usado_para_decidir": False,
        "va_a_favor_del_elegido": True,
        "por_que_se_cita": (
            "PORQUE VA A FAVOR DEL ELEGIDO Y ESO TAMBIEN HAY QUE DECIRLO. Medido "
            "hoy: plan_de_adquisicion_acquire tiene grado 8 y plan_acquire_activate "
            "tiene grado 3. Las dos varas coinciden, y cuando coinciden la regla NO "
            "SE LUCE. LIMITACION DECLARADA, la misma del acto 341 y por la misma "
            "causa: el instrumento imprime los cinco bloques en una sola salida, "
            "asi que el ejecutor vio el cableado en la misma corrida en que leyo "
            "el contenido y su adjudicacion NO es ciega respecto del cableado. Los "
            "cinco puntos de la lectura de contenido no lo mencionan y se "
            "sostienen solos; la relectura ciega del auditor es la guarda. Y SE "
            "ANOTA UN PATRON QUE YA VA POR TRES ACTOS SEGUIDOS (331, 341 y 344): "
            "el cableado ha ido a favor del elegido por contenido las tres veces, "
            "con margenes de 5 contra 2, 9 contra 5 y 8 contra 3. Un patron asi "
            "es comodo y por eso se declara: cuanto mas seguido coinciden las dos "
            "varas, menos evidencia hay de que la primera este haciendo el "
            "trabajo. El contraejemplo esta en la misma operacion, el acto 285, "
            "donde se separaron y el cableado PERDIO."),
        "instrumento": ("scripts/loop/vuelta41_lectura_acto.py --puesto 344, salida "
                        "docs/loop/SALIDA_V43_ACTO344_LECTURA.txt, bloque (e)"),
        "grados_medidos_hoy": {SUP: 8, ABS[0]: 3},
        "coste_medido_de_la_eleccion": ("CERO aristas. Los dos nodos tienen CERO "
                                        "aristas propias sin reciproco, asi que "
                                        "elegir a cualquiera de los dos no pierde "
                                        "ni una arista: las reciprocas las "
                                        "reescribe la simetrizacion de run_phase1 "
                                        "paso 5."),
    },
}
