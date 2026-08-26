# -*- coding: utf-8 -*-
"""_v72_lote_h.py . EL CONTENIDO EDITORIAL DEL LOTE H DEL TRAMO UNICO DE OP-U-02.

NO ES UN INSTRUMENTO: es el texto del lote. La maquina que lo sella es
scripts/loop/generar_plan_del_lote.py, que entra aqui por --contenido _v72_lote_h.

EL LOTE SE DECLARA AL ABRIRLO. Abre en el ACTO 43, que es el primero del tramo
SIN DUENO medido. Los DOS saltos van DECLARADOS con su cita y NO rompen el
prefijo sin saltos, porque ninguno de los dos actos saltados esta en la cola de
fusiones de esta operacion: el acto 31 tiene dueno medido (OP-F-04-WEI y OP-S-04
en duenos_cualquier_operacion, leido hoy del fichero fijado) y el acto 37 tiene
dueno medido (OP-S-07, leido hoy del mismo fichero), y la adjudicacion 2 del acta
69 dice con todas sus letras que lo que vale para el 31 vale para el 37 cuando el
prefijo lo alcance. Sigue el PREFIJO SIN SALTOS del orden_universo de lo que
queda: el lote A de la vuelta 65 cerro los actos 1 y 3; el B de la 66 el 5, 7, 8,
9, 10 y 11; el C de la 67 el 12 al 17; el D de la 68 el 19 al 24 y dejo el 18 en
transito; el E de la 69 cerro el 18, 25, 26, 27, 29 y 30; el F de la 70 el 32,
33, 34, 35 y 36; el G de la 71 el 38, 39, 40, 41 y 42.

LA DECLARACION: CINCO ACTOS CIERRAN ENTEROS Y SON 15 NODOS. CUATRO cierran
FUNDIDOS (43, 45, 46 y 47) y UNO cierra DECLARADO Y NO FUNDIDO (el 44), que es el
PRIMER DECLARADO DESDE EL LOTE E de la vuelta 69. Los motivos de DECLARADO
posibles son DOS y solo DOS (adjudicacion 4 del acta 70), y aqui muerde el
SEGUNDO: LA GUARDA 1B CON DOS O MAS PUERTAS. P.10 y el cuarto motivo siguen sin
sujeto en los cinco (cero puentes, cero triangulos y cero pares D internos,
medido con vuelta65_puentes_del_tramo.py), y P.5 contesta UNA FAMILIA en los
cinco, incluido el 44: lo que detiene al 44 no es la familia, son sus puertas.

LAS DOS PUERTAS DEL ACTO 44, Y POR QUE CIERRAN EL ACTO EN VEZ DE ELEGIR
SUPERVIVIENTE. El acto 44 tiene DOS de sus tres miembros dentro del universo
protegido de 256 ids (explotacion_tecnologias_disruptivas y
tecnologias_disruptivas_oportunidad, medido con varas_n_arias_del_tramo.py). La
guarda 1B prohibe ABSORBER una puerta; con DOS puertas, cualquier superviviente
que se eligiera absorberia a la otra. La pagina lo tiene registrado con estas
palabras: SI APARECE UN ACTO QUE NO SE PUEDA FUNDIR SIN ABSORBER UNA PUERTA,
CIERRA DECLARADO CON LA GUARDA 1B COMO MOTIVO, SIN IMPROVISAR FUSIONES PARCIALES
QUE NINGUNA LETRA ESCRIBE. NO SE IMPROVISA NINGUNA FUSION PARCIAL, y se dice: no
se funde el tercer miembro contra una de las dos puertas, no se parte el acto en
dos, y no se elige puerta ganadora. El acto queda VIVO Y ENTERO.

LA UNICA PUERTA DEL ACTO 46, Y POR QUE ESE SI SE FUNDE. Con UNA puerta el acto SI
se funde y LA PUERTA SOBREVIVE, gane o pierda en contenido (acta 54, pregunta 1;
registrado en esta pagina en la seccion de las adjudicaciones del acta 65,
apartado c, con el acto 20 de un tramo de OP-U-01 como precedente). AQUI LA
PUERTA PIERDE EN CONTENIDO Y EL CHOQUE VA ESCRITO ENTERO EN EL MOTIVO SELLADO,
que es exactamente lo que esa misma letra manda: la vara de condiciones apunta a
gestion_eco_riesgos y el superviviente es mitigacion_riesgos_ambientales.

EL TOPE DEL PREFIJO NO ES ESTRUCTURAL SINO DE LOTE, Y SE DICE: el siguiente es el
ACTO 49, que NO tiene dueno y NO trae puerta. El tope cae ANTES del 49 porque el
encargo fija CINCO actos, no porque el 49 tenga nada que lo impida.

EL REPARTO VA POR ABSORBIDO en la clave reparto, que es la forma que la vuelta 65
estreno para los actos de mas de dos miembros.

TRES MEDICIONES QUE ESTE FICHERO DECLARA Y NO ESCONDE:

  1. LA FRONTERA DEL DUENO PASA SU BORDE, Y SE MIDIO EN VEZ DE SUPONERSE. El acta
     71 dejo escrito en su adjudicacion 2 un BORDE: una familia_de_ids de nomina
     ENTERA sin resolucion aprobada que la fusion ejecute NO queda cubierta y va
     como PREGUNTA. Barrido hoy sobre docs/plan/INVENTARIO.jsonl: DOCE entradas
     tocan a alguno de los 15 miembros, y de ellas UNA SOLA es de tipo
     familia_de_ids. Cubre 1 de los 3 miembros del acto 46
     (responsabilidad_extendida_productor mas responsabilidad_extendida_productor_2,
     con OP-S-09 en operaciones), o sea PARTE de la nomina, que es EXACTAMENTE el
     caso que el acta 70 adjudico en su adjudicacion 2. CERO familia_de_ids
     cubren la nomina entera de un acto de este lote: EL BORDE NO SE PISA.
  2. Y LA CONSECUENCIA PARA OP-S-09 SE PUBLICA EN VEZ DE CALLARSE, que es lo que
     esa misma adjudicacion exige (la fusion le debe dejar su sujeto servible y
     publicado): el acto 46 ABSORBE a responsabilidad_extendida_productor, asi
     que a OP-S-09 le queda responsabilidad_extendida_productor_2 VIVO (medido
     hoy sobre master_graph: sin marca de deprecado) y el otro id resolviendo por
     alias a mitigacion_riesgos_ambientales. La familia sigue teniendo un id
     vivo y el otro resuelve, o sea SERVIBLE; lo que cambia es que su resolucion
     aprobada (familia unica, fusion con alias) tendra que ejecutarse sobre un
     alias que apunta FUERA de la familia. VA MARCADO DISCUTIBLE.
  3. LAS ENTRADAS DE TIPO ACTO DE LOS CINCO traen en operaciones NO SOLO OP-U-02
     sino tambien OP-L-03, igual que en el lote G. La diferencia con la vuelta
     71 es que ahora la ficha de OP-L-03 YA LLEVA SU CORRECCION DECLARADA
     aplicada (TAREA 1 de esta vuelta, adjudicacion 3 del acta 71), asi que la
     letra vieja ya no esta en divergencia: la clausula sigue entera arriba y la
     vara nueva esta escrita debajo. Se sigue declarando, y ya no como pregunta
     abierta sino como pregunta CONTESTADA con su cita.

Y UNA CUARTA, QUE ES DE ESTE LOTE Y DE NINGUN OTRO: la nota de OP-L-03 declara
que evaluacion_tecnologias_disruptivas es LD-04, una de las DOS lecturas
dirigidas de la primera tanda YA LEIDAS. Ese nodo es miembro del acto 44, que
cierra DECLARADO por la guarda 1B: no se toca, no se depreca y no se funde. La
medicion se deja escrita para quien lo retome en el cierre de la fase 03.
"""

# ======================================================================
# ACTO 43: LA FAMILIA DEL FRENO AL GASTO ANTES DE VALIDAR EL MODELO.
# TRES miembros del mismo libro, DOS pares internos con veredicto y los
# DOS en A, CERO D, CERO puentes, CERO triangulos y CERO puertas.
# FORMA medida: UNA SOLA VARA (la de condiciones). El cableado apunta al
# OTRO lado y con el margen mas ancho del lote, y por la letra no habla.
# ======================================================================

SUP43 = "preservar_efectivo_buscar_modelo"

MOTIVO43 = (
    "ACTO 43 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DEL FRENO AL GASTO ANTES DE VALIDAR EL "
    "MODELO. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE Y NO CON "
    "IMPRESION: los TRES miembros son del MISMO LIBRO (The Startup Owner's Manual, de Steve "
    "Blank), tienen DOS pares internos con veredicto escrito de TRES combinaciones posibles y "
    "los DOS son de clase A (puestos 550 y 935), hay CERO pares D internos, CERO nodos puente "
    "y CERO triangulos, medido con scripts/loop/vuelta65_puentes_del_tramo.py sobre el estado "
    "del dia. "
    "Y LA FAMILIA NO ES LECTURA MIA SINO DECLARACION DEL ARCHIVO: el puesto 935 se titula EL "
    "MISMO FRENO CONTRA EL ESCALAMIENTO TEMPRANO, DEL MISMO LIBRO Y SIN ARISTA ENTRE ELLOS, y "
    "el 550 abre con REPITE. El par que falta es el unico sin veredicto del acto. "
    "LO QUE LAS DOS RAZONES DICEN QUE ES LO MISMO, y es el nucleo entero: no contratar equipo "
    "de ventas ni marketing hasta que el modelo este validado con hechos, no confundir la venta "
    "puntual por relacion personal con un patron repetible, y vigilar el consumo de caja "
    "durante toda la etapa. "
    "P.8 EN ORDEN, Y LA FORMA MANDA: la FORMA medida es UNA SOLA VARA. La de PASOS EMPATA en 5 "
    "entre preservar_efectivo_buscar_modelo y restriccion_gasto_validacion y no apunta; la de "
    "CONDICIONES apunta a preservar_efectivo_buscar_modelo (4 contra 2 y 2). UNA SOLA VARA DE "
    "CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), y es la misma forma que el acta 71 "
    "adjudico A FAVOR en su D4 para el acto 42, con estas palabras: UNA SOLA VARA BASTA es la "
    "letra. "
    "Y AQUI VA EL CHOQUE ENTERO EN VEZ DE MEDIO, PORQUE ES EL MAS CARO DEL LOTE: EL CABLEADO "
    "APUNTA AL OTRO LADO, a restriccion_gasto_validacion con 11 contra 7 y 7, leido de la "
    "columna cab de scripts/loop/varas_n_arias_del_tramo.py, que es la unica fuente de cifra de "
    "cableado desde la adjudicacion 3 del acta 70. LA LETRA DE P.8 ES EXPLICITA EN QUE EL "
    "CABLEADO SOLO HABLA A CONTENIDO EMPATADO, y aqui el contenido no empata: la vara de "
    "condiciones apunta y las dos varas de contenido no estan las dos empatadas. Se funde a "
    "favor del contenido, el choque va MARCADO DISCUTIBLE en el reporte con su cifra al lado, y "
    "el costo se paga en redirecciones: restriccion_gasto_validacion tiene DIEZ nodos "
    "siguientes, la cifra mas alta de todo el lote, y los diez se redirigen. "
    "NINGUNA RAZON ESCRITA SE DESMIENTE, y va comprobado en vez de supuesto: NI EL 550 NI EL "
    "935 CORONAN A NADIE. El 550 reparte lo propio de cada lado sin elegir, y el 935 nombra dos "
    "piezas de restriccion_gasto_validacion como LO QUE HAY QUE SALVAR, que no es coronarlo: es "
    "encargar su rescate, y ESTE REPARTO LO EJECUTA, las dos, de APPEND entero. "
    "EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta (ni semilla de entrada ni extremo de "
    "puente aprobado), medido con scripts/loop/varas_n_arias_del_tramo.py contra el universo "
    "protegido de 256 ids. La guarda pasa POR VACIO y se dice. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; NINGUNA entrada de docs/plan/INVENTARIO.jsonl que no sea de tipo acto nombra a "
    "ninguno de los tres miembros, medido hoy con un barrido propio; NINGUNO de los tres esta "
    "en ninguna nomina de docs/RACIMOS_MIEMBROS.jsonl; y el barrido sobre "
    "docs/plan/OPERACIONES.jsonl no devuelve ninguna mencion de los tres. La entrada de tipo "
    "acto nombra OP-L-03 y OP-U-02, y eso se declara aparte en el docstring del lote."
)

NOTA43 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado en vez de maquillado. TRES APPEND DE PASO "
    "Y UN INCISO, cero APPEND de condicion, y el nodo crece de 5 pasos a 8 y se queda en 4 "
    "condiciones. "
    "ES EL ACTO QUE MAS CRECE DEL LOTE Y VA MARCADO DISCUTIBLE, porque es la especie que el "
    "acta 71 anoto en su D7 (nodos grandes dos vueltas seguidas) llevada un escalon mas arriba. "
    "LOS TRES APPEND SON GESTOS QUE LAS RAZONES ESCRITAS NOMBRAN COMO PROPIOS, uno a uno y sin "
    "que haga falta interpretarlas. El 935 dice, de restriccion_gasto_validacion: DOS PIEZAS "
    "CONCRETAS QUE EL OTRO NO DA, definir un presupuesto maximo por prueba, de dos mil a diez "
    "mil dolares por test, y reservar caja suficiente para financiar VARIOS pivotes; y remata "
    "con ESAS DOS SON LO QUE HAY QUE SALVAR. Las dos entran de APPEND ENTERO. El mismo 935 dice, "
    "de escalamiento_prematuro, que lo propio suyo es RETRASAR LAS INVERSIONES GRANDES EN "
    "INFRAESTRUCTURA hasta tener traccion real: el superviviente habla de a quien se contrata y "
    "nunca de en que se invierte, y ninguno de sus cinco pasos lo dice. Ese es el tercero. "
    "EL UNICO INCISO VA AL PASO 3 Y NO SE APILA CON NADIE (acta 64), y es un PARAMETRO CONCRETO "
    "de un gesto que el superviviente ya tiene: su paso 3 aplica el test de escalabilidad sobre "
    "el dolar adicional, o sea ya mide dinero, y lo que entra es CON QUE VARA medirlo, el ritmo "
    "de consumo de caja como metrica principal. El paso 3 del superviviente NO termina en punto "
    "(cierra en la palabra invertido), asi que la guarda de la JUNTURA ROTA no salta. "
    "LA SEGUNDA COPIA DEL BURN RATE NO SE APILA NI SE CALLA: el paso 5 de "
    "restriccion_gasto_validacion manda medir constantemente la tasa de consumo de caja, que es "
    "LO MISMO que el INCISO acaba de traer del hermano. Va de CUBIERTO con ATENUANTE DECLARADO "
    "Y MEDIDO, que es la especie del pendiente heredado (ya lo dice el APPEND de un hermano), "
    "aqui por INCISO en vez de por APPEND, y se dice cual es la diferencia: lo que llega es la "
    "vara, lo que se pierde es el adverbio CONSTANTEMENTE. "
    "CUATRO PERDIDAS SELLADAS, UNA DE ELLAS CON ATENUANTE DECLARADO Y MEDIDO, contadas por "
    "maquina sobre esta misma lista y no de memoria, que es la regla que sale de la caida del "
    "D9 de la vuelta 68."
)

PERDIDAS43 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL ADVERBIO CONSTANTEMENTE sobre la medicion del consumo de caja. ATENUANTE "
             "DECLARADO Y MEDIDO: la vara SI llega, y llega por el INCISO al paso 3 de este "
             "mismo acto, que trae el ritmo de consumo de caja como metrica principal desde el "
             "paso 3 del hermano escalamiento_prematuro; lo que no llega es la CADENCIA, o sea "
             "que la medicion sea continua y no de una vez"),
     "donde": "paso 5 de restriccion_gasto_validacion",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("CONFIRMAR EL SEGMENTO DE CLIENTES como el hito que libera el gasto en marketing "
             "de demanda. El paso 1 del superviviente condiciona el gasto a VALIDAR EL MODELO "
             "CON HECHOS, que es el hito grande; el absorbido nombra un hito distinto y mas "
             "temprano, el del segmento, y esa distincion se pierde"),
     "donde": "paso 2 de restriccion_gasto_validacion",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de LOS INVERSIONISTAS QUE PRESIONAN SIN DATOS DE RETENCION. La "
             "condicion 3 del superviviente nombra la PRESION EXTERNA en general; lo que se "
             "pierde es de quien viene y contra que se contrasta, que es el dato de que los "
             "clientes se quedan"),
     "donde": "condicion 2 de escalamiento_prematuro",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador del MOMENTO JUSTO DESPUES DE LANZAR EL PRODUCTO. La condicion 1 del "
             "superviviente dispara por ESTAR GASTANDO ya, que es un estado; el absorbido "
             "dispara por una FASE del calendario del proyecto, que es otra cosa y llega antes"),
     "donde": "condicion 1 de escalamiento_prematuro",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO43 = {
    "escalamiento_prematuro": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # no aumentar ventas y marketing hasta validar lo repetible
            "2": ("APPEND",),       # LAS INVERSIONES GRANDES EN INFRAESTRUCTURA: gesto propio
            # EL UNICO INCISO DEL ACTO: la vara con la que se mide el dinero, adosada
            # DENTRO del paso donde el superviviente ya mide dinero.
            "3": ("INCISO", 3, "tu ritmo de consumo de caja (burn rate) como tu metrica principal",
                  ", usando "),
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: la fase de justo despues de lanzar
            "2": ("CUBIERTO", 3),   # con perdida: los inversionistas y el dato de retencion
        },
    },
    "restriccion_gasto_validacion": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # posponer la contratacion masiva hasta validar
            "2": ("CUBIERTO", 1),   # con perdida: confirmar el SEGMENTO como hito propio
            "3": ("APPEND",),       # EL PRESUPUESTO MAXIMO POR PRUEBA, con su cifra
            "4": ("APPEND",),       # RESERVAR CAJA PARA FINANCIAR VARIOS PIVOTES
            "5": ("CUBIERTO", 3),   # con perdida y atenuante: llega por el INCISO del hermano
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # el equipo quiere escalar antes de validar
            "2": ("CUBIERTO", 4),   # dudas sobre el momento de pisar el acelerador
        },
    },
}


# ======================================================================
# ACTO 45: LA FAMILIA DE LA RECONSTRUCCION SIN SESGO RETROSPECTIVO.
# TRES miembros del mismo libro, DOS pares internos con veredicto y los
# DOS en A, CERO D, CERO puentes, CERO triangulos y CERO puertas.
# FORMA medida: CONTENIDO EMPATA. Es el UNICO acto del lote donde el
# cableado decide SOLO, y es tambien el segundo acto seguido del tramo
# donde LAS DOS RAZONES CORONAN SUPERVIVIENTES DISTINTOS.
# ======================================================================

SUP45 = "reconstruccion_contexto_situacional"

MOTIVO45 = (
    "ACTO 45 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA RECONSTRUCCION DEL CONTEXTO SIN "
    "SESGO RETROSPECTIVO. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE: los TRES "
    "miembros son del MISMO LIBRO (The Field Guide to Understanding Human Error, de Sidney "
    "Dekker), tienen DOS pares internos con veredicto escrito de TRES combinaciones posibles y "
    "los DOS son de clase A (puestos 2244 y 2294), hay CERO pares D internos, CERO nodos puente "
    "y CERO triangulos, medido. Las dos razones abren las dos con REPITE y las dos hacen la "
    "misma cuenta: los CINCO PASOS de evitar_sesgo_retrospectivo_hindsight estan cubiertos uno "
    "a uno, y las dos cierran con la misma frase, NO LE QUEDA NI UNA LINEA PROPIA. "
    "LAS DOS RAZONES CORONAN SUPERVIVIENTES DISTINTOS, Y ESO VA DICHO ENTERO EN VEZ DE "
    "ESCONDIDO: el 2244 cierra con SOBREVIVE reconstruccion_contexto_situacional y el 2294 con "
    "SOBREVIVE evitar_shopping_bag. Las dos coronaciones son sobre SU PROPIO PAR y las dos matan "
    "al mismo nodo, evitar_sesgo_retrospectivo_hindsight; EL PAR QUE FALTA, el unico sin "
    "veredicto del acto, es exactamente el que enfrentaria a los dos coronados. Es la misma "
    "forma que el acto 34 del lote F y el acto 39 del lote G, que las actas 70 y 71 adjudicaron "
    "A FAVOR en su D6 y su D5 con estas palabras: cada corona es sobre SU par y las dos razones "
    "matan al mismo nodo. NINGUNA RAZON ESCRITA SE DESMIENTE al fundir a favor de "
    "reconstruccion_contexto_situacional, porque el 2294 dice que evitar_shopping_bag gana A "
    "evitar_sesgo_retrospectivo_hindsight y NO dice nada sobre reconstruccion_contexto_situacional. "
    "Y HAY UNA DIFERENCIA CON AQUELLOS DOS QUE NO SE CALLA: alli el par que faltaba no tenia "
    "arista; aqui los dos coronados SI la tienen, y en los dos sentidos "
    "(reconstruccion_contexto_situacional nombra a evitar_shopping_bag entre sus siguientes y "
    "evitar_shopping_bag lo nombra entre sus previos). El archivo ya dice que uno viene del otro. "
    "P.8 EN ORDEN, Y AQUI LA FORMA ES OTRA: la FORMA medida es CONTENIDO EMPATA, la unica del "
    "lote. La de PASOS EMPATA en 5 A TRES BANDAS y no apunta; la de CONDICIONES EMPATA en 2 "
    "entre reconstruccion_contexto_situacional y evitar_sesgo_retrospectivo_hindsight y tampoco "
    "apunta. CON EL CONTENIDO EMPATADO, Y SOLO ENTONCES, HABLA EL CABLEADO, que es la letra "
    "exacta de P.8: apunta a reconstruccion_contexto_situacional con 8 contra 3 y 2, leido de "
    "la columna cab de scripts/loop/varas_n_arias_del_tramo.py, que es la unica fuente de cifra "
    "de cableado desde la adjudicacion 3 del acta 70. "
    "ESTE ES EL UNICO ACTO DEL LOTE QUE DECIDE EL CABLEADO SOLO, y por eso el margen se publica "
    "y no se resume: 8 contra 3 y 2 no es un margen de uno. EL ROTULO SOLO Y LA CANTIDAD NUNCA "
    "DECIDEN, y aqui no deciden: decide la unica vara que P.8 deja hablar cuando el contenido "
    "empata. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta, medido con "
    "scripts/loop/varas_n_arias_del_tramo.py contra el universo protegido de 256 ids. La guarda "
    "pasa POR VACIO y se dice. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; NINGUNA entrada de docs/plan/INVENTARIO.jsonl que no sea de tipo acto nombra a "
    "ninguno de los tres miembros, medido hoy con un barrido propio; NINGUNO de los tres esta "
    "en ninguna nomina de docs/RACIMOS_MIEMBROS.jsonl; y el barrido sobre "
    "docs/plan/OPERACIONES.jsonl no devuelve ninguna mencion de los tres. La entrada de tipo "
    "acto nombra OP-L-03 y OP-U-02, y eso se declara aparte en el docstring del lote."
)

NOTA45 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado en vez de maquillado. UN APPEND DE PASO Y "
    "UN INCISO, cero APPEND de condicion, y el nodo crece de 5 pasos a 6 y se queda en 2 "
    "condiciones. Es el reparto mas barato del lote, y no por generosidad del reparto sino "
    "porque el absorbido grande no tenia lineas propias: las dos razones lo dicen. "
    "EL UNICO APPEND ES EL QUE LA RAZON NOMBRA POR SU NOMBRE: el paso 2 de evitar_shopping_bag, "
    "IDENTIFICAR QUE SENALES SE CONTRADECIAN ENTRE SI EN EL MOMENTO. El 2294 lo llama EL PASO "
    "QUE LE DA NOMBRE AL EFECTO Y QUE NINGUN OTRO NODO DEL RACIMO TIENE, y remata con que sin "
    "el LA BOLSA DE EVIDENCIA SIGUE PARECIENDO COHERENTE. Es un gesto distinto y no un "
    "parametro: el superviviente reconstruye QUE senales llegaron y EN QUE ORDEN, pero nunca "
    "pregunta si se contradecian entre si. "
    "EL UNICO INCISO VA AL PASO 5 Y NO SE APILA CON NADIE (acta 64), y es un PARAMETRO CONCRETO "
    "de un gesto que el superviviente ya tiene: su paso 5 prohibe imponer marcos de referencia "
    "posteriores, y lo que entra es la forma concreta que ese vicio toma cuando se escribe el "
    "informe, presentar el conjunto completo de evidencia como si hubiera sido evidente desde el "
    "inicio. El paso 5 del superviviente NO termina en punto (cierra en la palabra real), asi "
    "que la guarda de la JUNTURA ROTA no salta. "
    "TRES PERDIDAS SELLADAS Y LAS TRES DE CONDICIONES, contadas por maquina sobre esta misma "
    "lista y no de memoria. NINGUNA ES DE PASO, y eso se dice porque es la primera vez en el "
    "tramo que un acto de tres cierra sin una sola perdida de paso: los diez pasos de los dos "
    "absorbidos entran enteros, cinco de CUBIERTO uno a uno, tres de CUBIERTO al mismo paso 4, "
    "uno de APPEND y uno de INCISO."
)

PERDIDAS45 = [
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de LA TENTACION DE JUZGAR DECISIONES PASADAS CON LA INFORMACION "
             "ACTUAL. Las dos condiciones del superviviente disparan por un ARTEFACTO que se "
             "escribe (el informe final) y por una TAREA que se pide (explicar por que las "
             "acciones tuvieron sentido); la que se pierde dispara por un ESTADO MENTAL del "
             "investigador, que llega antes que los dos"),
     "donde": "condicion 1 de evitar_sesgo_retrospectivo_hindsight",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de LA PREGUNTA ACUSATORIA LITERAL, como no vieron la evidencia. Es "
             "la frase que la gente dice en voz alta, y es el unico disparador del acto que se "
             "reconoce por una CITA y no por una descripcion"),
     "donde": "condicion 2 de evitar_sesgo_retrospectivo_hindsight",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de LA SITUACION DE PELIGRO QUE EN RETROSPECTIVA PARECE OBVIA, con "
             "su ejemplar nombrado, el clima adverso. La condicion 2 del superviviente pide "
             "explicar por que las acciones tuvieron sentido, que es el encargo; esta nombra el "
             "caso en que el encargo se vuelve dificil, y ademas trae el unico ejemplo concreto "
             "de las cinco condiciones del acto"),
     "donde": "condicion 1 de evitar_shopping_bag",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO45 = {
    "evitar_sesgo_retrospectivo_hindsight": {
        "pasos": {
            "1": ("CUBIERTO", 2),   # la linea de tiempo de cuando llego cada senal
            "2": ("CUBIERTO", 5),   # no dar el resultado por predecible
            "3": ("CUBIERTO", 1),   # imaginar la situacion sin conocer el desenlace
            "4": ("CUBIERTO", 4),   # que pudo significar cada senal en su contexto
            "5": ("CUBIERTO", 4),   # el entendimiento incompleto y cambiante
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: la tentacion de juzgar con la info de hoy
            "2": ("CUBIERTO", 2),   # con perdida: la pregunta acusatoria literal
        },
    },
    "evitar_shopping_bag": {
        "pasos": {
            "1": ("CUBIERTO", 2),   # el orden temporal exacto de las senales
            "2": ("APPEND",),       # LAS SENALES QUE SE CONTRADECIAN: el gesto que da nombre
            "3": ("CUBIERTO", 4),   # que significaban en su contexto, no ahora
            "4": ("CUBIERTO", 4),   # la comprension incompleta e incierta
            # EL UNICO INCISO: la forma concreta del vicio que el paso 5 prohibe.
            "5": ("INCISO", 5, "presentar el conjunto completo de evidencia como si hubiera "
                  "sido evidente desde el inicio", ", y sin "),
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),   # con perdida: el peligro que en retrospectiva parece obvio
        },
    },
}


# ======================================================================
# ACTO 46: LA FAMILIA DEL RIESGO AMBIENTAL DE LA CADENA EXTENDIDA.
# TRES miembros del mismo libro, DOS pares internos con veredicto y los
# DOS en A, CERO D, CERO puentes, CERO triangulos y UNA PUERTA.
# FORMA medida: UNA SOLA VARA (la de condiciones), Y LA VARA APUNTA A UN
# NODO QUE NO ES LA PUERTA. Con UNA puerta el acto SI se funde y LA
# PUERTA SOBREVIVE (acta 54, pregunta 1), gane o pierda en contenido.
# ======================================================================

SUP46 = "mitigacion_riesgos_ambientales"

MOTIVO46 = (
    "ACTO 46 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DEL RIESGO AMBIENTAL DE LA CADENA "
    "EXTENDIDA. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE: los TRES "
    "miembros son del MISMO LIBRO (The Green to Gold Business Playbook, de Daniel C. Esty), "
    "tienen DOS pares internos con veredicto escrito de TRES combinaciones posibles y los DOS "
    "son de clase A (puestos 1788 y 1822), hay CERO pares D internos, CERO nodos puente y CERO "
    "triangulos, medido. El 1822 lo declara con estas palabras: LA FAMILIA DEL RIESGO AMBIENTAL "
    "EXTENDIDO PASA DE DOS A TRES NODOS POR CIERRE TRANSITIVO, CON "
    "mitigacion_riesgos_ambientales DE CENTRO. El par que falta es el unico sin veredicto del "
    "acto. "
    "LO QUE LAS DOS RAZONES DICEN QUE ES LO MISMO, y las dos hacen la misma cuenta de TRES DE "
    "CUATRO PASOS: auditar y verificar a los proveedores de la cadena extendida, los PLANES DE "
    "CONTINGENCIA, y la exposicion regulatoria y legal en un caso y la comunicacion de crisis "
    "en el otro. "
    "AQUI DECIDE LA GUARDA 1B ANTES QUE P.8, Y EL CHOQUE SE ESCRIBE ENTERO EN VEZ DE "
    "MAQUILLARSE. UNA de las tres es PUERTA: mitigacion_riesgos_ambientales esta en el universo "
    "protegido de 256 ids, medido con scripts/loop/varas_n_arias_del_tramo.py. La letra de la "
    "puerta unica esta registrada en esta pagina, en la seccion de las adjudicaciones del acta "
    "65, apartado c, con estas palabras: CON UNA PUERTA EL ACTO SI SE FUNDE, LA PUERTA "
    "SOBREVIVE (acta 54, pregunta 1) Y EL CHOQUE CON LA VARA DE CONTENIDO QUEDA ESCRITO EN EL "
    "MOTIVO SELLADO, con el acto 20 de un tramo de OP-U-01 como precedente. ESTE ES EXACTAMENTE "
    "ESE CASO, Y EL CHOQUE EXISTE: la FORMA medida es UNA SOLA VARA y esa vara NO APUNTA A LA "
    "PUERTA. "
    "P.8 EN ORDEN, MEDIDO Y PUBLICADO AUNQUE NO DECIDA: la de PASOS EMPATA en 4 A TRES BANDAS y "
    "no apunta; la de CONDICIONES apunta a gestion_eco_riesgos (3 contra 2 y 2); el CABLEADO "
    "EMPATA en 4 entre gestion_eco_riesgos y responsabilidad_extendida_productor y tampoco "
    "apunta, leido de la columna cab de scripts/loop/varas_n_arias_del_tramo.py. O SEA QUE LA "
    "UNICA VARA QUE HABLA APUNTA AL OTRO LADO, y aun asi el superviviente es la puerta: LA "
    "PUERTA NO SE ABSORBE, GANE O PIERDA EN CONTENIDO. VA MARCADO DISCUTIBLE en el reporte con "
    "las tres cifras al lado. "
    "Y NO SE IMPROVISA NINGUNA SALIDA INTERMEDIA, que es lo que la misma letra prohibe: no se "
    "funde gestion_eco_riesgos como superviviente dejando la puerta fuera del acto, no se parte "
    "el acto en dos y no se declara. Con UNA puerta la letra dice FUNDE, y funde. "
    "EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy. Y AQUI SI HAY UNA ENTRADA QUE NO ES DE TIPO ACTO, Y SE DECLARA ENTERA: "
    "docs/plan/INVENTARIO.jsonl trae una entrada de tipo familia_de_ids con "
    "responsabilidad_extendida_productor y responsabilidad_extendida_productor_2, con OP-S-09 "
    "en su campo operaciones, estado pendiente se resuelve por continua o repite, y con esta "
    "nota leida hoy: DECISION 4 DE LA MESA DE RACIMOS, APROBADA EL 9 AGO 2026, FAMILIA UNICA, "
    "FUSION CON ALIAS. Cubre UNO de los tres miembros del acto, o sea PARTE de la nomina, que "
    "es EXACTAMENTE el caso que el acta 70 adjudico en su adjudicacion 2: una entrada que "
    "nombra una operacion sobre PARTE de la nomina NO es dueno del acto. EL BORDE QUE EL ACTA "
    "71 ESCRIBIO (nomina ENTERA sin resolucion aprobada) NO SE PISA, y va medido y no supuesto: "
    "CERO familia_de_ids cubren la nomina entera de ningun acto de este lote. "
    "LA CONSECUENCIA PARA OP-S-09 SE PUBLICA, que es lo que esa misma adjudicacion exige: este "
    "acto ABSORBE a responsabilidad_extendida_productor, y a OP-S-09 le queda "
    "responsabilidad_extendida_productor_2 VIVO (medido hoy sobre master_graph, sin marca de "
    "deprecado) mas el otro id resolviendo por alias a mitigacion_riesgos_ambientales. SU "
    "SUJETO QUEDA SERVIBLE, y lo que cambia se dice: su resolucion aprobada tendra que "
    "ejecutarse sobre un alias que apunta FUERA de la familia. VA MARCADO DISCUTIBLE. "
    "NINGUNO de los tres esta en ninguna nomina de docs/RACIMOS_MIEMBROS.jsonl y el barrido "
    "sobre docs/plan/OPERACIONES.jsonl no devuelve ninguna mencion de los tres. La entrada de "
    "tipo acto nombra OP-L-03 y OP-U-02, y eso se declara aparte en el docstring del lote."
)

NOTA46 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado en vez de maquillado. UN APPEND DE PASO, "
    "UN APPEND DE CONDICION Y UN INCISO, y el nodo crece de 4 pasos a 5 y de 2 condiciones a 3. "
    "EL UNICO APPEND DE PASO ES EL QUE LA RAZON NOMBRA POR SU NOMBRE: el paso 1 de "
    "gestion_eco_riesgos, MAPEAR TODOS LOS PUNTOS DE LA CADENA DE VALOR donde pueden surgir "
    "riesgos ambientales, con sus cinco estaciones dentro (materias primas, produccion, "
    "distribucion, uso y disposicion final). El 1788 lo llama EL UNICO PASO QUE DA UN METODO "
    "PARA ENCONTRARLOS EN VEZ DE SUPONERLOS, y es exacto: el superviviente AUDITA riesgos que "
    "ya sabe donde estan, y este dice donde buscarlos. Es un gesto distinto y no un parametro. "
    "EL UNICO INCISO VA AL PASO 3 Y NO SE APILA CON NADIE (acta 64), y es un PARAMETRO CONCRETO "
    "de un gesto que el superviviente ya tiene: su paso 3 disena planes de contingencia, y lo "
    "que entra es SOBRE QUE se disenan, los escenarios y probabilidades de riesgo, que es lo "
    "que el 1788 llama EL UNICO QUE LE PONE UNA MEDIDA DE VEROSIMILITUD A CADA RIESGO. El paso "
    "3 del superviviente NO termina en punto (cierra en la palabra ambientales), asi que la "
    "guarda de la JUNTURA ROTA no salta. "
    "EL UNICO APPEND DE CONDICION ES UN DISPARADOR DISTINTO Y NO UN MATIZ, que es la unica "
    "puerta por la que el acta 55 (pregunta 5) deja pasar una condicion de APPEND mientras el "
    "INCISO de condiciones no exista: las DOS condiciones del superviviente disparan por lo que "
    "la empresa MANEJA (materiales peligrosos, cadenas complejas) y por lo que ya le PASO "
    "(antecedentes de incidentes), y la que entra dispara por un HUECO DE CONOCIMIENTO, no "
    "haber evaluado formalmente la exposicion. Ninguna de las tres dispara por lo mismo, y la "
    "que entra es la unica que llega ANTES de que haya materia ni antecedente. "
    "CUATRO PERDIDAS SELLADAS, contadas por maquina sobre esta misma lista y no de memoria. "
    "DOS DE ELLAS SON LAS QUE EL 1822 YA HABIA PROPUESTO POR ESCRITO y esta nota no las "
    "descubre: los proveedores de segundo y tercer nivel, y la verificacion mas alla de las "
    "politicas escritas."
)

PERDIDAS46 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LOS PROVEEDORES DE SEGUNDO Y TERCER NIVEL. El paso 2 del superviviente establece "
             "protocolos en LA CADENA DE SUMINISTRO EXTENDIDA, que nombra el alcance pero no lo "
             "cuantifica; el absorbido baja de nivel y dice hasta donde, que es la unica linea "
             "del acto que pasa del proveedor directo. El 1822 la propone por escrito como "
             "perdida antes que esta nota"),
     "donde": "paso 1 de responsabilidad_extendida_productor",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA EXIGENCIA DE QUE LA VERIFICACION VAYA MAS ALLA DE LAS POLITICAS ESCRITAS. El "
             "paso 2 del superviviente pide protocolos de cumplimiento y verificacion; el "
             "absorbido pide que la verificacion no se satisfaga con el papel, que es la "
             "diferencia entre auditar y leer un archivo. El 1822 tambien la propone por "
             "escrito"),
     "donde": "paso 3 de responsabilidad_extendida_productor",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA EXPOSICION DE REPUTACION Y DE MERCADO. El paso 4 del superviviente monitorea "
             "los cambios REGULATORIOS que generen exposiciones LEGALES, o sea dos de las "
             "cuatro clases que el absorbido evalua; las otras dos, la de reputacion y la de "
             "mercado, no aparecen en ninguno de los cuatro pasos del superviviente"),
     "donde": "paso 2 de gestion_eco_riesgos",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de TENER UNA MARCA DE CARA AL CONSUMIDOR. La condicion 2 del "
             "superviviente dispara por ANTECEDENTES de incidentes de reputacion, o sea cuando "
             "el dano ya ocurrio; el absorbido dispara por la EXPOSICION estructural a ese "
             "dano, que existe desde el primer dia y sin antecedente ninguno"),
     "donde": "condicion 1 de responsabilidad_extendida_productor",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO46 = {
    "gestion_eco_riesgos": {
        "pasos": {
            "1": ("APPEND",),       # MAPEAR LA CADENA DE VALOR: el metodo para encontrarlos
            "2": ("CUBIERTO", 4),   # con perdida: la exposicion de reputacion y de mercado
            "3": ("CUBIERTO", 2),   # protocolos de auditoria a proveedores y terceros
            # EL UNICO INCISO: sobre que se disenan los planes de contingencia.
            "4": ("INCISO", 3, "escenarios y probabilidades de riesgo", ", a partir de "),
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # materiales toxicos, metales pesados o quimicos peligrosos
            "2": ("CUBIERTO", 1),   # proveedores externos o cadenas extendidas
            "3": ("APPEND",),       # NO HABER EVALUADO FORMALMENTE: disparador distinto
        },
    },
    "responsabilidad_extendida_productor": {
        "pasos": {
            "1": ("CUBIERTO", 2),   # con perdida: los proveedores de segundo y tercer nivel
            "2": ("CUBIERTO", 2),   # guias de cumplimiento explicitas para los proveedores
            "3": ("CUBIERTO", 2),   # con perdida: mas alla de las politicas escritas
            "4": ("CUBIERTO", 3),   # los planes de comunicacion de crisis
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),   # con perdida: la marca de cara al consumidor
            "2": ("CUBIERTO", 1),   # terceriza produccion o depende de proveedores externos
        },
    },
}


# ======================================================================
# ACTO 47: LA FAMILIA DE LA TERMINACION DEL FRANQUICIADO.
# TRES miembros del mismo libro, DOS pares internos con veredicto y los
# DOS en A, CERO D, CERO puentes, CERO triangulos y CERO puertas.
# FORMA medida: UNA SOLA VARA (la de pasos). LAS DOS RAZONES CORONAN AL
# MISMO NODO, que es el unico acto del lote donde eso pasa, y el
# superviviente NO CRECE NI UN PASO: los dos absorbidos entran de
# CUBIERTO salvo una linea cada uno, y esa linea entra de INCISO.
# ======================================================================

SUP47 = "gestion_terminacion_franquiciado"

MOTIVO47 = (
    "ACTO 47 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA TERMINACION DEL FRANQUICIADO. "
    "UNA SOLA FAMILIA, Y ES EL ACTO MEJOR DECLARADO DEL LOTE: los TRES miembros son del MISMO "
    "LIBRO (Franchise Your Business, de Mark Siebert), tienen DOS pares internos con veredicto "
    "escrito de TRES combinaciones posibles y los DOS son de clase A (puestos 2072 y 2190), hay "
    "CERO pares D internos, CERO nodos puente y CERO triangulos, medido. El par que falta es el "
    "unico sin veredicto del acto. "
    "LAS DOS RAZONES CORONAN AL MISMO NODO, Y ES EL UNICO ACTO DEL LOTE DONDE ESO PASA: las dos "
    "cierran con POR LA VARA, REPITE, y el 2190 remata con SOBREVIVE "
    "gestion_terminacion_franquiciado POR CONTENIDO. No hay coronas cruzadas que reconciliar. "
    "Y EL ARCHIVO DECLARA UNA FIGURA SOBRE ESTE ACTO, leida hoy de "
    "docs/plan/INVENTARIO.jsonl: la entrada de tipo figura del SUBCONJUNTO ESTRICTO (banco "
    "9.6.1) nombra al par de gestion_terminacion_franquiciado con "
    "terminacion_franquiciado_causas, con esta glosa: LOS PASOS DEL CORTO VIVEN DENTRO DEL "
    "LARGO Y LO UNICO PROPIO CABE EN UNA LINEA. El 2072 hace esa cuenta paso por paso: los "
    "CUATRO pasos del corto viven dentro de los cinco del largo, casi con las mismas palabras. "
    "P.8 EN ORDEN, Y LA FORMA MANDA: la FORMA medida es UNA SOLA VARA. La de PASOS apunta a "
    "gestion_terminacion_franquiciado (5 contra 4 y 4); la de CONDICIONES EMPATA en 2 entre "
    "gestion_terminacion_franquiciado y terminacion_franquiciado_causas y no apunta. UNA SOLA "
    "VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4), y aqui las DOS razones escritas "
    "apuntan ademas al mismo nodo que la vara. "
    "EL CABLEADO APUNTA AL OTRO LADO Y NO HABLA, Y SE PUBLICA IGUAL: apunta a "
    "perdida_control_operativo con 2 contra 1 y 1, leido de la columna cab de "
    "scripts/loop/varas_n_arias_del_tramo.py. ES EL MARGEN MAS ESTRECHO DE TODO EL LOTE, UN "
    "SOLO ENLACE DE DIFERENCIA, y por eso se dice entero en vez de resumirse: el superviviente "
    "es el nodo peor cableado del acto (1 enlace, y CERO siguientes), y aun asi gana por "
    "contenido, porque LA LETRA DE P.8 ES EXPLICITA EN QUE EL CABLEADO SOLO HABLA A CONTENIDO "
    "EMPATADO y aqui el contenido no empata. EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta, medido con "
    "scripts/loop/varas_n_arias_del_tramo.py contra el universo protegido de 256 ids. La guarda "
    "pasa POR VACIO y se dice. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; NINGUNA entrada de docs/plan/INVENTARIO.jsonl de tipo familia_de_ids nombra a ninguno "
    "de los tres (la unica entrada que no es de tipo acto y los toca es la figura del "
    "subconjunto estricto, que es una FIGURA y no una jurisdiccion, y ademas no nombra "
    "operacion ninguna); NINGUNO de los tres esta en ninguna nomina de "
    "docs/RACIMOS_MIEMBROS.jsonl. Y AQUI SI HAY MENCIONES EN docs/plan/OPERACIONES.jsonl, Y VAN "
    "LEIDAS ENTERAS EN VEZ DE CONTADAS: TRES fichas nombran a alguno de los tres miembros "
    "(OP-U-01, OP-U-02 y OP-I-01), y en LAS TRES la mencion vive en el campo nota y es PROSA "
    "HISTORICA sobre el recomputo, no nomina: las tres cuentan que este mismo acto CRECIO DE 2 "
    "A 3 entre el corte 2117 y el corte 3388 al ganar perdida_control_operativo. Ninguna de las "
    "tres lo reclama, ninguna lo pone en un campo nodos y ninguna es de las TRES fuentes que la "
    "adjudicacion 2 del acta 68 fija como frontera del dueno. La entrada de tipo acto nombra "
    "OP-L-03 y OP-U-02, y eso se declara aparte en el docstring del lote."
)

NOTA47 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado en vez de maquillado. CERO APPEND Y DOS "
    "INCISO, y el nodo NO CRECE NI UN PASO NI UNA CONDICION: se queda en 5 pasos y 2 "
    "condiciones. Es el unico acto del lote que cierra sin un solo APPEND, y no por avaricia "
    "del reparto sino porque las dos razones dicen lo mismo con las mismas palabras: LO UNICO "
    "QUE EL CORTO ANADE ES UNA FRASE y LO UNICO PROPIO DE perdida_control_operativo ES SU PASO "
    "1, Y ESO CABE EN UNA LINEA. Cuando lo propio cabe en una linea, la linea va de INCISO. "
    "LOS DOS INCISO VAN A PASOS DISTINTOS Y NINGUNO SE APILA (acta 64), y los dos son la unica "
    "linea propia de su absorbido, nombrada por su razon. AL PASO 2, la GRADUACION DE LOS "
    "PLAZOS SEGUN LA GRAVEDAD, que es el parametro que el 2072 aisla con estas palabras: LO "
    "UNICO QUE EL CORTO ANADE ES UNA FRASE, QUE LOS PLAZOS SE GRADUEN SEGUN LA GRAVEDAD, Y ESO "
    "CABE EN UNA LINEA. AL PASO 1, LAS DECISIONES OPERATIVAS QUE QUEDAN BAJO CONTROL DEL "
    "FRANQUICIADO, que el 2190 no solo aisla sino que ENRUTA: LA LINEA DE LA ACEPTACION DEL "
    "CONTROL CEDIDO SE ABSORBE EN EL. El INCISO ejecuta esa frase al pie. "
    "LOS DOS PASOS RECEPTORES DEL SUPERVIVIENTE NO TERMINAN EN PUNTO (uno cierra en la palabra "
    "no y el otro en la palabra incumplimiento), asi que la guarda de la JUNTURA ROTA no salta "
    "en ninguno de los dos. "
    "UNA SOLA PERDIDA SELLADA, contada por maquina sobre esta misma lista y no de memoria, y es "
    "LA CIFRA MAS BAJA DEL TRAMO PARA UN ACTO DE TRES MIEMBROS. Se dice por que: los ocho pasos "
    "de los dos absorbidos entran ENTEROS, seis de CUBIERTO y dos de INCISO, y de las tres "
    "condiciones absorbidas dos entran de CUBIERTO limpias."
)

PERDIDAS47 = [
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de LA NECESIDAD DE CONTROL DEL PROPIO EMPRENDEDOR, que es lo que "
             "genera dudas sobre franquiciar. Las DOS condiciones del superviviente disparan "
             "por hechos del NEGOCIO (un franquiciado que incumple, un contrato que se "
             "redacta); esta dispara por una disposicion del FUNDADOR, y es la unica del acto "
             "que llega ANTES de que exista franquiciado alguno. NO va de APPEND y se dice por "
             "que: el acta 55 (pregunta 5) solo deja pasar de APPEND la condicion que es un "
             "disparador distinto Y que el reparto necesita, y este acto ya paga su unico "
             "cupo de crecimiento en los dos INCISO; la perdida queda NOMBRADA, que es lo que "
             "el contrato manda mientras el INCISO de condiciones no exista"),
     "donde": "condicion 1 de perdida_control_operativo",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO47 = {
    "terminacion_franquiciado_causas": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # las violaciones no curables listadas en el contrato
            # EL PRIMER INCISO: la unica frase que el corto anade, segun su propia razon.
            "2": ("INCISO", 2, "segun su gravedad", ", graduados "),
            "3": ("CUBIERTO", 3),   # las plantillas de carta de default
            "4": ("CUBIERTO", 4),   # el checklist de cumplimiento como evidencia objetiva
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),   # al redactar el contrato legal de franquicia
            "2": ("CUBIERTO", 1),   # un franquiciado existente que incumple
        },
    },
    "perdida_control_operativo": {
        "pasos": {
            # EL SEGUNDO INCISO: la unica linea propia, y su razon manda absorberla ahi.
            "1": ("INCISO", 1, "que decisiones operativas quedaran bajo control del franquiciado",
                  ", tras aceptar y documentar "),
            "2": ("CUBIERTO", 1),   # el contrato con curables y no curables
            "3": ("CUBIERTO", 2),   # plazos y procedimientos para notificar y curar
            "4": ("CUBIERTO", 5),   # con el abogado, las causales de terminacion inmediata
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: la necesidad de control del emprendedor
        },
    },
}


# ======================================================================
# ACTO 44: DECLARADO Y NO FUNDIDO POR LA GUARDA 1B, CON DOS PUERTAS.
# NO SE TOCA NI UN NODO. Es el PRIMER DECLARADO DESDE EL LOTE E de la
# vuelta 69, y el PRIMERO DE TODO EL TRAMO cuyo motivo sellado es la
# guarda 1B y no el triangulo de P.10.
# ======================================================================

DECLARADO_ACTO44 = {
    "acto": 44,
    "miembros": [
        "evaluacion_tecnologias_disruptivas",
        "explotacion_tecnologias_disruptivas",
        "tecnologias_disruptivas_oportunidad",
    ],
    "superviviente_que_el_contenido_elige": (
        "NINGUNO SE ELIGE, Y ESA ES LA DECISION. Se dice a quien habria apuntado la forma, "
        "porque callarlo seria esconder el costo: la FORMA medida es UNA SOLA VARA, la de "
        "PASOS, y apunta a explotacion_tecnologias_disruptivas (6 contra 4 y 4); la de "
        "CONDICIONES EMPATA en 2 a tres bandas y no apunta; y el CABLEADO apunta AL OTRO LADO, "
        "a tecnologias_disruptivas_oportunidad con 6 contra 5 y 2, leido de la columna cab de "
        "scripts/loop/varas_n_arias_del_tramo.py. LOS DOS NODOS A LOS QUE APUNTAN LAS VARAS SON "
        "LAS DOS PUERTAS, y ese es justamente el problema: cualquiera de los dos que se "
        "eligiera absorberia a la otra."
    ),
    "motivo": (
        "ACTO 44 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LAS TECNOLOGIAS DISRUPTIVAS. "
        "DECLARADO Y NO FUNDIDO CON LA GUARDA 1B COMO MOTIVO SELLADO, que es el SEGUNDO de los "
        "DOS motivos que la adjudicacion 4 del acta 70 deja abiertos, y es la PRIMERA VEZ EN "
        "TODO EL TRAMO UNICO que muerde este y no el triangulo de P.10. "
        "LO MEDIDO, Y ES LO QUE MANDA: DOS de los tres miembros son PUERTA, o sea estan dentro "
        "del universo protegido de 256 ids (semillas de entrada mas extremos de puente "
        "aprobado), medido con scripts/loop/varas_n_arias_del_tramo.py sobre el estado del dia: "
        "explotacion_tecnologias_disruptivas y tecnologias_disruptivas_oportunidad. LA GUARDA "
        "1B PROHIBE ABSORBER UNA PUERTA, y con DOS puertas en el mismo acto no existe ningun "
        "superviviente posible que no absorba a la otra. "
        "LA LETRA ESTA REGISTRADA EN ESTA MISMA PAGINA, en la seccion de las adjudicaciones del "
        "acta 65, apartado c, y dice: SI APARECE UN ACTO QUE NO SE PUEDA FUNDIR SIN ABSORBER "
        "UNA PUERTA, CIERRA DECLARADO CON LA GUARDA 1B COMO MOTIVO, SIN IMPROVISAR FUSIONES "
        "PARCIALES QUE NINGUNA LETRA ESCRIBE. "
        "LO QUE NO SE HACE, ENUMERADO PARA QUE NADIE LO LEA COMO UN OLVIDO: no se funde "
        "evaluacion_tecnologias_disruptivas contra una de las dos puertas dejando la otra "
        "fuera, porque eso seria una FUSION PARCIAL y ninguna letra la escribe; no se elige "
        "puerta ganadora, porque la guarda no ordena las puertas entre si; no se parte el acto "
        "en dos componentes, porque el acto es la componente y partirla es re-cribar; y no se "
        "toca ni un nodo, ni un alias, ni un veredicto. "
        "Y LA FAMILIA NO ES LO QUE LO DETIENE, QUE ES LO QUE HAY QUE DECIR PARA QUE EL CIERRE "
        "DE LA FASE 03 LO ENCUENTRE LISTO: P.5 contesta UNA SOLA FAMILIA con las razones "
        "delante. Los TRES miembros son del MISMO LIBRO (Winning at New Products, de Robert G. "
        "Cooper), los DOS pares internos con veredicto son de clase A (puestos 505 y 513), hay "
        "CERO pares D internos, CERO nodos puente y CERO triangulos. El 505 abre con REPITE con "
        "tecnologias_disruptivas_oportunidad, LOS DOS MANDAN LO MISMO DE CHRISTENSEN, y el 513 "
        "cierra declarando ESTA FAMILIA LLEGA A TRES NODOS DEL NUCLEO Y NINGUNO ESTA EN "
        "RACIMOS_MIEMBROS.jsonl. Es UNA familia que NO SE PUEDE FUNDIR, que no es lo mismo que "
        "DOS familias. "
        "EL ARCHIVO YA TENIA ESTE ACTO NOMBRADO COMO FIGURA, y se declara: "
        "docs/plan/INVENTARIO.jsonl trae una entrada de tipo figura, la ESTRELLA (banco 9.23), "
        "que nombra a los TRES miembros de este acto como uno de sus ejemplares, con la glosa "
        "UN CENTRO QUE REPITE CON DOS PERIFERIOS QUE ENTRE SI SON SANOS. Es una FIGURA y no una "
        "jurisdiccion (no nombra operacion ninguna), asi que NO es dueno por la adjudicacion 2 "
        "del acta 68; se declara porque una fusion entera habria deprecado a dos de los tres "
        "ejemplares de una figura declarada, y esa es una SEGUNDA razon independiente para no "
        "fundir, medida y no supuesta. "
        "Y UNA TERCERA MEDICION QUE SE DEJA ESCRITA PARA QUIEN RETOME ESTE ACTO: la nota de la "
        "ficha de OP-L-03, leida hoy, declara que evaluacion_tecnologias_disruptivas es LD-04, "
        "una de las DOS lecturas dirigidas de la primera tanda YA LEIDAS. El acto no se toca, "
        "asi que esa lectura no se gasta ni se contradice. "
        "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, "
        "medido hoy, y ninguno de los tres miembros esta en ninguna nomina de "
        "docs/RACIMOS_MIEMBROS.jsonl. "
        "EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se depreca ninguno y no se "
        "elige superviviente. Su destino comparte carril con los CATORCE declarados que ya "
        "esperan: el cierre de la fase 03. CON ESTE SON QUINCE."
    ),
    "medicion": {
        "instrumento": "scripts/loop/vuelta65_puentes_del_tramo.py",
        "salida": "docs/loop/SALIDA_V72_PUENTES_TRAMO.txt",
        "dossier": "docs/loop/SALIDA_V72_DOSSIER_LOTE_H.txt",
        "varas": "docs/loop/SALIDA_V72_VARAS_N_ARIAS.txt",
        "miembros": 3,
        "combinaciones": 3,
        "pares_A": 2,
        "pares_D": 0,
        "pares_sin_veredicto": 1,
        "nodos_puente": 0,
        "triangulos_puente": 0,
        "puertas_dentro": [
            "explotacion_tecnologias_disruptivas",
            "tecnologias_disruptivas_oportunidad",
        ],
        "puestos_D_internos": [],
        "duenos_cualquier_operacion": [],
        "figura_del_inventario": "ESTRELLA (9.23), un centro que repite con dos periferios sanos",
    },
}


LOTE_H = {
    "titulo": ("LOTE H DEL TRAMO UNICO DE OP-U-02. ABRE EN EL ACTO 43, que es el PRIMERO DEL "
               "TRAMO SIN DUENO MEDIDO. LOS DOS SALTOS VAN DECLARADOS Y NO ROMPEN EL PREFIJO "
               "SIN SALTOS, porque ninguno de los dos actos saltados esta en la cola de "
               "fusiones de esta operacion: el ACTO 31 tiene dueno medido (OP-F-04-WEI y "
               "OP-S-04 en duenos_cualquier_operacion, leido hoy del fichero fijado del tramo) "
               "y el ACTO 37 tiene dueno medido (OP-S-07, leido hoy del mismo fichero), y la "
               "adjudicacion 2 del acta 69 dice con todas sus letras que lo que vale para el 31 "
               "vale para el 37 cuando el prefijo lo alcance. CINCO ACTOS CIERRAN ENTEROS Y SON "
               "15 NODOS: los actos 43, 45, 46 y 47 cierran FUNDIDOS y el ACTO 44 cierra "
               "DECLARADO Y NO FUNDIDO con LA GUARDA 1B como motivo sellado, por sus DOS "
               "PUERTAS (explotacion_tecnologias_disruptivas y tecnologias_disruptivas_oportunidad, "
               "medidas hoy), que es el PRIMER DECLARADO DESDE EL LOTE E de la vuelta 69 y el "
               "PRIMERO DE TODO EL TRAMO con ese motivo y no el triangulo de P.10. EL ACTO 46 "
               "FUNDE CON SU UNICA PUERTA SOBREVIVIENDO (acta 54, pregunta 1) AUNQUE LA VARA DE "
               "CONTENIDO APUNTE AL OTRO LADO, y el choque queda escrito entero en su motivo "
               "sellado. EL TOPE DEL PREFIJO NO ES ESTRUCTURAL SINO DE LOTE, Y SE DICE: el "
               "siguiente es el ACTO 49, que NO tiene dueno y NO trae puerta; el tope cae ANTES "
               "del 49 porque el encargo fija CINCO actos, no porque el 49 tenga nada que lo "
               "impida"),
    "actos": [
        {
            "orden": 43,
            "superviviente": SUP43,
            "motivo": MOTIVO43,
            "nota": NOTA43,
            "reparto": REPARTO43,
            "perdidas": PERDIDAS43,
        },
        {
            "orden": 45,
            "superviviente": SUP45,
            "motivo": MOTIVO45,
            "nota": NOTA45,
            "reparto": REPARTO45,
            "perdidas": PERDIDAS45,
        },
        {
            "orden": 46,
            "superviviente": SUP46,
            "motivo": MOTIVO46,
            "nota": NOTA46,
            "reparto": REPARTO46,
            "perdidas": PERDIDAS46,
        },
        {
            "orden": 47,
            "superviviente": SUP47,
            "motivo": MOTIVO47,
            "nota": NOTA47,
            "reparto": REPARTO47,
            "perdidas": PERDIDAS47,
        },
    ],
    "declarados": [DECLARADO_ACTO44],
}
