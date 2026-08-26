# -*- coding: utf-8 -*-
"""_v70_lote_f.py . EL CONTENIDO EDITORIAL DEL LOTE F DEL TRAMO UNICO DE OP-U-02.

NO ES UN INSTRUMENTO: es el texto del lote. La maquina que lo sella es
scripts/loop/generar_plan_del_lote.py, que entra aqui por --contenido _v70_lote_f.

EL LOTE SE DECLARA AL ABRIRLO. Abre en el ACTO 32, que es donde la adjudicacion 2
del acta 69 manda abrir el prefijo (el acto 31 tiene dueno medido, OP-F-04-WEI y
OP-S-04, y NO es una fusion de OP-U-02: su salto va DECLARADO con esa cita y no
rompe el prefijo sin saltos, porque el 31 no esta en la cola de fusiones de esta
operacion). Sigue el PREFIJO SIN SALTOS del orden_universo de lo que queda del
tramo fijado en docs/loop/TRAMO_UNICO_OPU02_V64.jsonl: el lote A de la vuelta 65
cerro los actos 1 y 3; el B de la 66 el 5, 7, 8, 9, 10 y 11; el C de la 67 el 12
al 17; el D de la 68 el 19, 20, 21, 22, 23 y 24 y dejo el 18 en transito; el E de
la 69 cerro el 18, 25, 26, 27, 29 y 30.

LA DECLARACION: CINCO ACTOS CIERRAN ENTEROS Y SON 15 NODOS. Los CINCO cierran
FUNDIDOS (32, 33, 34, 35 y 36) y NINGUNO cierra DECLARADO Y NO FUNDIDO, que es
exactamente lo que la adjudicacion 4 del acta 69 anticipo: en lo que resta del
tramo no hay actos con nodo puente ni con par D interno, asi que P.10 y el cuarto
motivo quedan SIN SUJETO; y de los tres motivos que si podrian disparar, la
guarda 1B pasa POR VACIO en los cinco (CERO puertas dentro de cada acto, medido),
P.5 contesta UNA FAMILIA en los cinco, y ninguna forma sale EMPATE SIN VARA.

EL TOPE DEL PREFIJO ES ESTRUCTURAL Y SE DICE, en vez de dejarlo como un numero
elegido: el siguiente del prefijo es el ACTO 37 y ESE ACTO TIENE DUENO. Medido
hoy sobre el fichero fijado del tramo, su campo duenos_cualquier_operacion trae
OP-S-07, y la adjudicacion 2 del acta 69 dice con todas sus letras que lo mismo
que vale para el 31 vale para el 37 cuando el prefijo lo alcance. El acto 37 se
leyo entero igual (esta en el dossier y en las varas de esta vuelta, por el
carril del D16 del acta 68: la letra prohibe FUNDIR un acto con dueno, no
leerlo), se mide y se deja donde esta.

EL REPARTO VA POR ABSORBIDO en la clave reparto, que es la forma que la vuelta 65
estreno para los actos de mas de dos miembros.

UNA COSA MEDIDA QUE ESTE FICHERO DECLARA Y NO ESCONDE, porque toca al ACTO 34 y
a la frontera del dueno que el acta 68 escribio: docs/plan/INVENTARIO.jsonl trae
una entrada de tipo familia_de_ids llamada ciclo_de_culpa, con miembros
ciclo_de_culpa y ciclo_de_culpa_2 y con OP-S-09 en su campo operaciones. Leida al
pie de la letra, la frontera del acta 68 diria que eso es dueno y que el acto no
se funde. LA PRACTICA MEDIDA DE LA CAMPANA DICE LO CONTRARIO Y ES LA QUE MANDA
POR PRECEDENTE: el acto 3 (lote A, vuelta 65) y el acto 7 (lote B, vuelta 66) se
fundieron los dos teniendo cada uno una entrada familia_de_ids con OP-S-09
cubriendo PARTE de su nomina (3 de 10 y 2 de 6), y hoy tienen 1 miembro vivo de
10 y 1 de 6. La frontera del acta 68 se escribio sobre un RACIMO que cubria la
NOMINA ENTERA de su acto y con operaciones VACIO. Aqui la entrada cubre 2 de 3 y
es de otra especie. El acto 34 se funde por ese precedente, la lectura contraria
va MARCADA DISCUTIBLE en el reporte, y la pregunta va al auditor.
"""

# ======================================================================
# ACTO 32: LA FAMILIA DE LA BUSQUEDA DE PROBLEMAS GRANDES.
# TRES miembros, DOS pares internos con veredicto y los DOS en A, CERO D,
# CERO nodos puente, CERO triangulos y CERO puertas.
# FORMA medida: CONTENIDO EMPATA (pasos 4 a tres bandas, condiciones 2 a
# tres bandas), asi que EL CABLEADO DECIDE SOLO, que es el unico supuesto
# en que P.8 le da la palabra.
# ======================================================================

SUP32 = "atacar_mercados_establecidos_con_problema"

MOTIVO32 = (
    "ACTO 32 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA BUSQUEDA DE PROBLEMAS GRANDES. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE Y NO CON "
    "IMPRESION: los TRES miembros son del MISMO LIBRO (Winning at New Products, de Robert G. "
    "Cooper), tienen DOS pares internos con veredicto escrito de TRES combinaciones posibles y "
    "los DOS son de clase A (puestos 908 y 1507), hay CERO pares D internos, CERO nodos puente "
    "y CERO triangulos, medido con scripts/loop/vuelta65_puentes_del_tramo.py sobre el estado "
    "del dia. "
    "Y LA FAMILIA NO ES LECTURA MIA SINO DECLARACION DEL ARCHIVO: el puesto 1507 cierra "
    "diciendo que encontrar_grandes_problemas_mercados_emergentes YA TENIA GEMELO, el puesto "
    "908, y que con ese par LA FAMILIA DE LA BUSQUEDA DE PROBLEMAS GRANDES PASA A TRES NODOS "
    "POR CIERRE TRANSITIVO, con cobertura de 2 de 3. El par que falta es el unico sin "
    "veredicto del acto. "
    "LO QUE LAS DOS RAZONES DICEN QUE ES LO MISMO, y es el nucleo entero: identificar el "
    "mercado, listar los problemas o puntos de dolor que los competidores actuales no "
    "resuelven, evaluar si la empresa tiene fortalezas o capacidades propias para resolverlos, "
    "y disenar o validar antes de invertir. El 1507 lo dice con estas palabras: LOS CUATRO "
    "PASOS SE CORRESPONDEN UNO A UNO Y EN EL MISMO ORDEN, y lo unico que cambia es EL "
    "PARAMETRO, o sea el tipo de mercado donde se caza. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta (ni semilla de entrada ni extremo de "
    "puente aprobado), medido con scripts/loop/varas_n_arias_del_tramo.py contra el universo "
    "protegido de 256 ids. La guarda pasa POR VACIO y se dice. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto "
    "(duenos_mesa_o_destejido y duenos_cualquier_operacion), medido hoy; NINGUNA entrada de "
    "docs/plan/INVENTARIO.jsonl que no sea de tipo acto nombra a ninguno de los tres miembros, "
    "medido hoy con un barrido propio; y el barrido sobre docs/plan/OPERACIONES.jsonl no "
    "devuelve ninguna mencion de los tres. Por el criterio que el acta 68 adjudico en su "
    "seccion 5.2, el dueno es EL MEDIDO y aqui no hay ninguno. "
    "P.8 EN ORDEN, Y LA FORMA MANDA: la FORMA medida es CONTENIDO EMPATA (los tres empatan en "
    "4 pasos y los tres empatan en 2 condiciones), asi que EL CABLEADO DECIDE SOLO, que es el "
    "unico supuesto en que P.8 le da la palabra, y apunta a "
    "atacar_mercados_establecidos_con_problema con 3 contra 2 y 2. EL MARGEN ES DE UNO Y SE "
    "DICE EN VEZ DE MAQUILLARSE: es el margen mas estrecho con el que este tramo ha elegido "
    "superviviente por cableado, y por eso va MARCADO DISCUTIBLE en el reporte. EL ROTULO SOLO "
    "Y LA CANTIDAD NUNCA DECIDEN, y ninguna de las tres cuentas se teclea: las tres salen del "
    "instrumento."
)

NOTA32 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado en vez de maquillado. UN APPEND DE PASO Y "
    "UN APPEND DE CONDICION, mas UN INCISO al paso 1, y el nodo crece de 4 pasos a 5 y de 2 "
    "condiciones a 3. "
    "EL INCISO AL PASO 1 ES LA PIEZA QUE LAS DOS RAZONES MANDAN CONSERVAR, y es la unica forma "
    "de conservarla donde sirve. El puesto 908 lo dice con todas sus letras: la unica "
    "diferencia entre los dos nodos es DONDE MIRAR, esa diferencia NO ES CONTRADICCION SINO "
    "COBERTURA, y ES JUSTO LO QUE HAY QUE SALVAR EN LA FUSION, o sea que EL NODO SUPERVIVIENTE "
    "TIENE QUE DECIR QUE LA BUSQUEDA VALE EN LOS DOS SITIOS. Un APPEND habria puesto el "
    "segundo coto de paso 5, o sea al final y despues de la validacion economica; el INCISO lo "
    "deja DENTRO del paso 1, que es donde se elige el coto. El paso 1 del superviviente NO "
    "termina en punto (cierra con un parentesis), asi que la guarda de la JUNTURA ROTA no "
    "salta. "
    "EL UNICO APPEND DE PASO es DISENAR UNA SOLUCION DE SISTEMA INTEGRADO EN LUGAR DE SOLO UN "
    "PRODUCTO AISLADO, que es el paso que el 908 nombra como el cuarto gesto comun de los dos "
    "absorbidos y que EL SUPERVIVIENTE NO TIENE: sus cuatro pasos llegan hasta la validacion "
    "economica y ninguno llega hasta la solucion. Se elige el texto de resolver_problemas_grandes "
    "y no el de su hermano porque nombra ademas EL CONTRASTE (sistema integrado frente a "
    "producto aislado), que es lo que hace util el paso. "
    "EL UNICO APPEND DE CONDICION ES UN DISPARADOR DISTINTO Y NO UN MATIZ, que es la unica "
    "puerta por la que el acta 55 (pregunta 5) deja pasar una condicion de APPEND mientras el "
    "INCISO de condiciones no exista: las DOS condiciones del superviviente miran MERCADOS "
    "MADUROS y GRANDES DESAFIOS SIN RESOLVER, y la que entra mira el ALTO POTENCIAL DE "
    "CRECIMIENTO, que es el coto contrario. Sin ella el nodo diria que la busqueda vale en los "
    "dos sitios en su paso 1 y solo se activaria en uno. "
    "CINCO PERDIDAS SELLADAS, UNA DE ELLAS CON DOS SEDES EN UN SOLO CAMPO donde por el "
    "criterio que el acta 67 adjudico en su D10 (LA FILA ES POR PIEZA QUE SE PIERDE, NO POR "
    "SITIO DONDE VIVIA): el nombre propio de la fortaleza que se evalua vive en el paso 3 de "
    "los dos absorbidos y va en UNA fila con las dos sedes nombradas. "
    "UNA PERDIDA CON ATENUANTE DECLARADO Y DE LA ESPECIE DEL PENDIENTE 4, contada por maquina "
    "sobre esta misma lista y no de memoria, que es la regla que sale de la caida del D9 de la "
    "vuelta 68."
)

PERDIDAS32 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA ACLARACION DE QUE NO HACE FALTA UN OCEANO AZUL, y con ella el criterio de "
             "ALTA INSATISFACCION DEL USUARIO para elegir el mercado. El puesto 908 la nombra "
             "como la aclaracion EXPLICITA de resolver_problemas_grandes, y es la unica linea "
             "del acto que sale al paso de la objecion de que buscar en mercados existentes no "
             "sirve. El paso 1 del superviviente manda mercados grandes y maduros con "
             "necesidades no resueltas, que es el mismo coto sin la aclaracion"),
     "donde": "paso 1 de resolver_problemas_grandes",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL ENLACE EXPLICITO DE LA SOLUCION A LOS PUNTOS DE DOLOR PRINCIPALES, o sea que "
             "lo que se disena ataque exactamente lo que se listo en el paso anterior. "
             "ATENUANTE DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: el paso de diseno llega "
             "ENTERO por el APPEND del paso 4 de resolver_problemas_grandes; lo que no llega "
             "es el amarre entre la solucion y la lista de dolores"),
     "donde": "paso 4 de encontrar_grandes_problemas_mercados_emergentes",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL NOMBRE PROPIO DE LA FORTALEZA QUE SE EVALUA: CAPACIDADES UNICAS de diseno y "
             "tecnologia en un lado y COMPETENCIAS CENTRALES en el otro. El paso 3 del "
             "superviviente dice SUS FORTALEZAS a secas, que es el genero sin ninguna de las "
             "dos especies. UNA SOLA PIEZA CON DOS SEDES, sellada una vez con las dos "
             "nombradas (acta 67, D10)"),
     "donde": ("paso 3 de encontrar_grandes_problemas_mercados_emergentes y paso 3 de "
               "resolver_problemas_grandes"),
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de UN MERCADO CON MULTIPLES COMPETIDORES DONDE NINGUNO RESUELVE "
             "BIEN el problema del cliente. Las tres condiciones que el nodo tendra tras la "
             "fusion miran la MADUREZ del mercado, el DESAFIO sin resolver y el POTENCIAL DE "
             "CRECIMIENTO; ninguna mira la COMPETENCIA que ya esta dentro y lo hace mal"),
     "donde": "condicion 2 de encontrar_grandes_problemas_mercados_emergentes",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de CREER QUE HACE FALTA INVENTAR TECNOLOGIA NUEVA SIN TENER I MAS "
             "D RADICAL. La condicion 1 del superviviente mira a la empresa que OPERA EN "
             "MERCADOS MADUROS Y BUSCA INNOVACION DISRUPTIVA, que es la misma situacion "
             "descrita por el mercado y no por la creencia ni por la carencia de medios"),
     "donde": "condicion 1 de resolver_problemas_grandes",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO32 = {
    "encontrar_grandes_problemas_mercados_emergentes": {
        "pasos": {
            # EL UNICO INCISO DEL ACTO: el segundo coto, que el 908 manda salvar
            # y que el superviviente tiene que decir DENTRO del paso donde se
            # elige donde mirar.
            "1": ("INCISO", 1,
                  "mercados en fase embrionaria o de rapido crecimiento",
                  ", y también "),
            "2": ("CUBIERTO", 2),   # listar problemas y frustraciones del cliente
            "3": ("CUBIERTO", 3),   # con perdida de dos sedes: el nombre de la fortaleza
            "4": ("CUBIERTO", 4),   # con perdida y atenuante del pendiente 4: llega por el APPEND del hermano
        },
        "condiciones": {
            "1": ("APPEND",),       # ALTO POTENCIAL DE CRECIMIENTO: disparador distinto
            "2": ("CUBIERTO", 2),   # con perdida: los multiples competidores que no resuelven
        },
    },
    "resolver_problemas_grandes": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # con perdida: el oceano azul y la alta insatisfaccion
            "2": ("CUBIERTO", 2),   # los puntos de dolor que los competidores no resuelven
            "3": ("CUBIERTO", 3),   # segunda sede de la perdida del nombre de la fortaleza
            "4": ("APPEND",),       # LA SOLUCION DE SISTEMA INTEGRADO: el unico APPEND de paso
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: inventar tecnologia sin I mas D radical
            "2": ("CUBIERTO", 1),   # mercados maduros y comoditizados: es la condicion 1 del superviviente
        },
    },
}


# ======================================================================
# ACTO 33: LA FAMILIA DE LA CONCIENCIA PERIFERICA (FRINGE-CONSCIOUSNESS).
# TRES miembros, DOS pares internos con veredicto y los DOS en A, CERO D,
# CERO nodos puente, CERO triangulos y CERO puertas.
# FORMA medida: UNA SOLA VARA (la de pasos), y el cableado apunta al OTRO
# lado con el margen mas ancho del lote. La letra dice que donde el
# contenido dice algo el contenido manda.
# ======================================================================

SUP33 = "wallas_intimacion_fringe_consciousness"

MOTIVO33 = (
    "ACTO 33 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA CONCIENCIA PERIFERICA. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE: los TRES "
    "miembros son del MISMO LIBRO (The Art of Thought, de Graham Wallas), tienen DOS pares "
    "internos con veredicto escrito de TRES combinaciones posibles y los DOS son de clase A "
    "(puestos 403 y 1510), hay CERO pares D internos, CERO nodos puente y CERO triangulos, "
    "medido con scripts/loop/vuelta65_puentes_del_tramo.py sobre el estado del dia. Y el 1510 "
    "cierra declarando que LA FAMILIA DE LA CONCIENCIA PERIFERICA PASA A TRES NODOS POR CIERRE "
    "TRANSITIVO. "
    "EL SUPERVIVIENTE LO DECLARA UNA RAZON, Y ESO ES LO PRIMERO QUE SE DICE PORQUE ES LO QUE "
    "MANDA. El puesto 403 trae una linea rotulada DATO QUE DECIDE CUAL SOBREVIVE, verificada "
    "contra el grafo por su autor y anticipada en el puesto 279: LA MADRE wallas_etapa_iluminacion "
    "TIENE ARISTA CON wallas_intimacion_fringe_consciousness Y NO LA TIENE CON "
    "intimation_illumination, y el que no la tiene ES EL GEMELO SIN CASA. La razon nombra al "
    "superviviente sin ambiguedad. "
    "P.8 EN ORDEN, Y LA VARA DE CONTENIDO DICE LO MISMO QUE LA RAZON: la FORMA medida es UNA "
    "SOLA VARA. La de PASOS apunta a wallas_intimacion_fringe_consciousness (4 contra 3 y 3); "
    "la de CONDICIONES EMPATA en 2 entre los otros dos y no apunta. UNA SOLA VARA DE CONTENIDO "
    "NO EMPATADA BASTA (acta 53, pregunta 4). "
    "Y AQUI VA EL CHOQUE ENTERO EN VEZ DE MEDIO, PORQUE ES EL MAS FUERTE DEL LOTE: EL CABLEADO "
    "APUNTA AL OTRO LADO Y CON EL MARGEN MAS ANCHO DEL LOTE, a intimation_illumination con 9 "
    "contra 4 y 3, y ese nodo tiene SEIS siguientes y TRES previos, o sea que fundirlo obliga "
    "a redirigir nueve referencias. LA LETRA DE P.8 ES EXPLICITA EN QUE EL CABLEADO SOLO HABLA "
    "A CONTENIDO EMPATADO, y aqui el contenido no empata: habla la vara de pasos y ademas "
    "habla la razon escrita. Se funde a favor del contenido y del dato declarado, y el choque "
    "va MARCADO DISCUTIBLE en el reporte con su cifra al lado. EL ROTULO SOLO Y LA CANTIDAD "
    "NUNCA DECIDEN. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta, medido contra el universo protegido de "
    "256 ids. La guarda pasa POR VACIO y se dice. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; NINGUNA entrada de docs/plan/INVENTARIO.jsonl que no sea de tipo acto nombra a "
    "ninguno de los tres; y el barrido sobre docs/plan/OPERACIONES.jsonl no devuelve ninguna "
    "mencion. El dueno es EL MEDIDO y aqui no hay ninguno."
)

NOTA33 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado. UN APPEND DE PASO Y DOS APPEND DE "
    "CONDICION, y el nodo crece de 4 pasos a 5 y de 1 condicion a 3. Es el unico acto del lote "
    "que triplica sus condiciones, y la razon es que el superviviente entraba con UNA sola. "
    "CERO INCISO EN ESTE ACTO, y la razon es la puntuacion, que es el carril que el acta 66 "
    "adjudico en su D5: LOS CUATRO PASOS DEL SUPERVIVIENTE TERMINAN EN PUNTO, asi que "
    "cualquier INCISO con nexo de coma caeria en la guarda de la JUNTURA ROTA del generador. "
    "No se fuerza ninguno, y se dice en vez de dejarlo como un cero mudo. "
    "EL UNICO APPEND DE PASO ES EL QUE LA RAZON MANDA CONSERVAR Y ADEMAS EXPLICAR: PRACTICAR "
    "LA INHIBICION de la tendencia natural a enfocar de inmediato cualquier estimulo "
    "interesante. El puesto 1510 la llama LA UNICA INSTRUCCION DEL CATALOGO QUE PIDE NO "
    "PRESTAR ATENCION A PROPOSITO, y ademas avisa de que esta EN TENSION con los pasos 2 y 3 "
    "del superviviente, que piden justo lo contrario: dedicar atencion voluntaria a la "
    "sensacion y sostenerla. La razon dice que LA FUSION TIENE QUE CONSERVAR LAS DOS Y DECIR "
    "CUAL ES EL DISPARADOR DE CADA UNA, y las dos quedan conservadas: la inhibicion entra como "
    "paso 5 y los pasos 2 y 3 se quedan enteros. LO QUE ESTA OPERACION NO HACE ES REDACTAR EL "
    "DISPARADOR DE CADA UNA, porque redactar no es repartir: eso queda enrutado a la fase 04 y "
    "va dicho aqui para que nadie lo de por hecho. "
    "LOS DOS APPEND DE CONDICION SON DISPARADORES DISTINTOS, que es la unica puerta por la que "
    "el acta 55 (pregunta 5) los deja pasar: la condicion 1 del superviviente es REACTIVA (un "
    "miembro del equipo REPORTA sentir que algo se acerca), la primera que entra es DELIBERADA "
    "(se BUSCA mejorar la sensibilidad para captar insights emergentes) y la segunda es de "
    "CONTEXTO (se realiza investigacion exploratoria o brainstorming). Ninguna de las tres "
    "dispara por lo mismo. "
    "CUATRO PERDIDAS SELLADAS, UNA CON DOS SEDES (el soporte nombrado del registro) y UNA CON "
    "ATENUANTE DECLARADO de la especie del pendiente 4, contadas por maquina sobre esta misma "
    "lista."
)

PERDIDAS33 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("SIN FORZAR AUN LA CONCLUSION, o sea el freno explicito en el momento de "
             "registrar la sensacion. El paso 4 del superviviente manda registrar las "
             "sensaciones como senales tempranas, pero no dice que al registrarlas no se debe "
             "empujar todavia hacia la conclusion, que es justo el error que el registro "
             "invita a cometer"),
     "donde": "paso 2 de intimation_illumination",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("DEJAR MADURAR como tercera opcion junto a sostener y prolongar, y ANTES DE "
             "INTENTAR VERBALIZARLA como el momento en que se decide. El paso 3 del "
             "superviviente manda SOSTENER O PROLONGAR la linea de pensamiento y ahi se "
             "detiene: no ofrece la opcion pasiva ni fija el momento de la decision"),
     "donde": "paso 3 de intimation_illumination",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL SOPORTE NOMBRADO DEL REGISTRO: mentalmente o por escrito en un lado, por "
             "escrito o grabacion en el otro. El paso 4 del superviviente manda REGISTRAR a "
             "secas y no dice en que. UNA SOLA PIEZA CON DOS SEDES, sellada una vez con las "
             "dos nombradas (acta 67, D10)"),
     "donde": "paso 2 de intimation_illumination y paso 3 de atencion_focal_y_periferica",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador de BUSCAR TECNICAS para captar insights no evidentes DURANTE LA "
             "IDEACION, que es el unico que nombra la etapa del trabajo donde se activa. "
             "ATENUANTE DECLARADO, Y ES LA ESPECIE DEL PENDIENTE 4: la mitad de buscar mejorar "
             "la sensibilidad para captar insights llega entera por el APPEND de la condicion "
             "2 de intimation_illumination; lo que no llega es la palabra IDEACION"),
     "donde": "condicion 1 de atencion_focal_y_periferica",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO33 = {
    "intimation_illumination": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # prestar atencion a las sensaciones difusas
            "2": ("CUBIERTO", 4),   # con perdida: sin forzar aun la conclusion, y el soporte
            "3": ("CUBIERTO", 3),   # con perdida: dejar madurar y antes de verbalizar
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # sospechar que una idea esta por surgir sin poder formularla
            "2": ("APPEND",),       # MEJORAR LA SENSIBILIDAD: disparador distinto, deliberado
        },
    },
    "atencion_focal_y_periferica": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # notar los pensamientos perifericos sin forzarlos
            "2": ("APPEND",),       # LA INHIBICION: la unica instruccion que pide NO atender
            "3": ("CUBIERTO", 4),   # segunda sede de la perdida del soporte del registro
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida y atenuante del pendiente 4: la ideacion
            "2": ("APPEND",),       # INVESTIGACION EXPLORATORIA O BRAINSTORMING: disparador de contexto
        },
    },
}


# ======================================================================
# ACTO 34: LA FAMILIA DEL CICLO DE CULPA Y LOS PATRONES DISFUNCIONALES.
# TRES miembros, DOS pares internos con veredicto y los DOS en A, CERO D,
# CERO nodos puente, CERO triangulos y CERO puertas.
# FORMA medida: TODAS DE ACUERDO (las dos varas de contenido apuntan al
# mismo nodo). Es el acto con la entrada de inventario que la nota del
# docstring declara, y por eso su motivo la nombra entera.
# ======================================================================

SUP34 = "ciclo_de_culpa_2"

MOTIVO34 = (
    "ACTO 34 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DEL CICLO DE CULPA Y LOS PATRONES "
    "DISFUNCIONALES DE CULTURA. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS DOS RAZONES DELANTE Y CON EL "
    "COSTO DICHO: los TRES miembros son del MISMO LIBRO (Managing the Risks of Organizational "
    "Accidents, de James Reason), tienen DOS pares internos con veredicto escrito de TRES "
    "combinaciones posibles y los DOS son de clase A (puestos 2233 y 2272), hay CERO pares D "
    "internos, CERO nodos puente y CERO triangulos, medido. EL NUCLEO COMPARTIDO ESTA "
    "DECLARADO POR LAS DOS RAZONES Y NO ES LECTURA MIA: los CUATRO pasos de ciclo_de_culpa "
    "estan DENTRO de los otros dos, uno por uno y con el paso receptor nombrado en cada caso. "
    "El 2233 lo dice de dysfunctional_organizational_culture_patterns y el 2272 lo dice de "
    "ciclo_de_culpa_2. Un nodo que cabe entero dentro de los otros dos es la bisagra que hace "
    "de esto UNA familia. "
    "Y AQUI VA LO QUE HACE DE ESTE ACTO EL MAS DISCUTIBLE DEL LOTE, DICHO ENTERO EN VEZ DE "
    "ESCONDIDO: LAS DOS RAZONES CORONAN SUPERVIVIENTES DISTINTOS. El 2233 cierra con SOBREVIVE "
    "dysfunctional_organizational_culture_patterns y el 2272 cierra con SOBREVIVE "
    "ciclo_de_culpa_2. Las dos coronaciones son sobre SU PROPIO PAR y las dos matan al mismo "
    "nodo, ciclo_de_culpa; EL PAR QUE FALTA, el unico sin veredicto del acto, es exactamente "
    "el que enfrentaria a los dos coronados. NINGUNA RAZON ESCRITA SE DESMIENTE FUNDIENDO A "
    "FAVOR DE ciclo_de_culpa_2, porque el 2233 dice que dysfunctional gana A ciclo_de_culpa y "
    "NO dice nada sobre ciclo_de_culpa_2. Lo que decide es P.8. "
    "P.8 EN ORDEN: la FORMA medida es TODAS DE ACUERDO. La vara de PASOS apunta a "
    "ciclo_de_culpa_2 (5 contra 4 y 4) y la de CONDICIONES apunta al mismo (3 contra 2 y 2). "
    "Cuando TODAS las varas de contenido concuerdan se funde a su lado. El CABLEADO apunta a "
    "ciclo_de_culpa (6 contra 5 y 2), que es el nodo QUE LAS DOS RAZONES MATAN, y por la letra "
    "el cableado solo habla a contenido empatado: aqui no empata. EL ROTULO SOLO Y LA CANTIDAD "
    "NUNCA DECIDEN, y eso vale tambien para el sufijo _2 del superviviente, que es rotulo y no "
    "contenido. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta, medido contra el universo protegido de "
    "256 ids. La guarda pasa POR VACIO. "
    "DUENOS, Y AQUI HAY UNA MEDICION QUE SE DECLARA EN VEZ DE CALLARSE: los dos campos del "
    "fichero fijado del tramo estan VACIOS para este acto, medido hoy, y el barrido sobre "
    "docs/plan/OPERACIONES.jsonl no devuelve ninguna mencion de los tres miembros en ningun "
    "campo. PERO docs/plan/INVENTARIO.jsonl SI trae una entrada de tipo familia_de_ids llamada "
    "ciclo_de_culpa, con miembros ciclo_de_culpa y ciclo_de_culpa_2, forma IDS QUE DIFIEREN "
    "POR SUFIJO, estado PENDIENTE y OP-S-09 en su campo operaciones. LEIDA AL PIE DE LA LETRA, "
    "la frontera que el acta 68 escribio en su seccion 5.2 diria que eso es dueno y que el "
    "acto no se funde. LA PRACTICA MEDIDA DE LA CAMPANA DICE LO CONTRARIO, Y ES PRECEDENTE Y "
    "NO OPINION: el acto 3 (fundido por el lote A de la vuelta 65) y el acto 7 (fundido por el "
    "lote B de la vuelta 66) tenian cada uno una entrada familia_de_ids con OP-S-09 cubriendo "
    "PARTE de su nomina, 3 de 10 y 2 de 6, y los dos se fundieron; medido hoy sobre el grafo, "
    "les queda 1 miembro vivo de 10 y 1 de 6. La frontera del acta 68 se escribio sobre un "
    "RACIMO que cubria la NOMINA ENTERA de su acto y que tenia operaciones VACIO; esta entrada "
    "es de otra especie y cubre 2 de 3. SE FUNDE POR ESE PRECEDENTE, LA LECTURA CONTRARIA VA "
    "MARCADA DISCUTIBLE Y LA PREGUNTA VA AL AUDITOR. "
    "Y UNA CONSECUENCIA MEDIDA QUE SE PUBLICA PARA QUE OP-S-09 NO SE LA ENCUENTRE: tras esta "
    "fusion la familia de ids ciclo_de_culpa queda con UN solo id vivo, y ese id vivo es "
    "ciclo_de_culpa_2, o sea EL QUE LLEVA EL SUFIJO NUMERICO. La verificacion de OP-S-09 exige "
    "que NINGUN ID VIVO LLEVE SUFIJO NUMERICO DE DUPLICADO, asi que OP-S-09 sigue teniendo "
    "trabajo sobre este id: un RENOMBRE CON ALIAS, que es exactamente su tipo. Esta operacion "
    "no lo hace ni lo estorba, y lo deja escrito."
)

NOTA34 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado en vez de maquillado. TRES APPEND DE PASO "
    "Y UN APPEND DE CONDICION, mas UN INCISO al paso 2, y el nodo crece de 5 pasos a 8 y de 3 "
    "condiciones a 4. ES EL SEGUNDO NODO MAS GRANDE DEL LOTE Y VA MARCADO DISCUTIBLE. "
    "LA ELECCION ES LA DEL CARRIL DEL D8 DEL ACTA 67, DEL D4 DEL ACTA 68 Y DEL D2 DEL ACTA 69: "
    "catalogo mas rico con solapes declarados por encima de CUBIERTO que calla texto vivo. Y "
    "los tres APPEND son piezas que el 2233 nombra como propias de "
    "dysfunctional_organizational_culture_patterns y que el superviviente NO TIENE: LA "
    "INDEFENSION APRENDIDA como sintoma medible con la falta de iniciativa ante riesgos; LOS "
    "RITUALES O PROCEDIMIENTOS REPETIDOS SIN EVIDENCIA DE EFECTIVIDAD; y SUSTITUIR LAS "
    "REACCIONES DE EVITACION DE ANSIEDAD POR ANALISIS GENUINO DE CAUSAS RAIZ, que es la unica "
    "pieza del acto que nombra la causa raiz y que el superviviente no dice en ninguno de sus "
    "cinco pasos. "
    "EL UNICO INCISO VA AL PASO 2 Y ES LA FRASE QUE DA NOMBRE AL PATRON: PATRONES REPETITIVOS "
    "DE CULPAR Y ENTRENAR TRAS INCIDENTES. El 2272 declara que ese paso esta CUBIERTO por el "
    "paso 2 del superviviente, y lo esta en el gesto (evitar sanciones o advertencias como "
    "unica respuesta), pero el superviviente no dice CULPAR Y ENTRENAR con esas palabras, que "
    "son las que vuelven buscable el patron. El INCISO lo repone VERBATIM dentro del paso donde "
    "vive el gesto. El paso 2 del superviviente NO termina en punto, asi que la guarda de la "
    "JUNTURA ROTA no salta, y NO HAY MAS DE UN INCISO POR PASO (acta 64). "
    "EL UNICO APPEND DE CONDICION ES UN DISPARADOR DISTINTO: las tres condiciones del "
    "superviviente miran la ESCALADA DE SANCIONES, la REPETICION DE INCIDENTES y el DISENO DE "
    "UN SISTEMA DE REPORTE JUSTO; la que entra mira la APATIA O RESIGNACION DEL PERSONAL, que "
    "es el sintoma de la indefension aprendida y el disparador propio del paso que este mismo "
    "acto adosa. Sin ella el nodo tendria el paso y no tendria cuando aplicarlo. "
    "CINCO PERDIDAS SELLADAS, UNA CON DOS SEDES, DOS CON ATENUANTE DECLARADO Y MEDIDO y UNA "
    "TERCERA CON ATENUANTE DECLARADO, contadas por maquina sobre esta misma lista y no de "
    "memoria."
)

PERDIDAS34 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA PREGUNTA DE AUDITORIA SOBRE LAS MEDIDAS CORRECTIVAS: si atacan CAUSAS RAIZ o "
             "solo SINTOMAS SUPERFICIALES, dicha como par y como pregunta. ATENUANTE DECLARADO "
             "Y MEDIDO: el analisis genuino de causas raiz llega ENTERO por el APPEND del paso "
             "4 de dysfunctional_organizational_culture_patterns, que este mismo acto adosa; "
             "lo que se pierde es el CONTRASTE con el sintoma superficial y la forma de "
             "pregunta sobre lo ya hecho"),
     "donde": "paso 2 de ciclo_de_culpa",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA PREGUNTA DE SI LA ORGANIZACION BUSCA RESOLVER EL PROBLEMA O SOLO APARENTAR "
             "ACCION, que es la sospecha dicha sobre la INTENCION y no sobre el metodo. "
             "ATENUANTE DECLARADO: los RITUALES O PROCEDIMIENTOS REPETIDOS SIN EVIDENCIA DE "
             "EFECTIVIDAD llegan por el APPEND del paso 2 de "
             "dysfunctional_organizational_culture_patterns, que es la misma sospecha vista "
             "desde el ritual y no desde la intencion"),
     "donde": "paso 3 de ciclo_de_culpa",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA NUEVA NORMA, o sea ESCRIBIR OTRO PROCEDIMIENTO, como reflejo automatico "
             "DISTINTO del de culpar. El 2233 la nombra con todas sus letras como una de las "
             "tres cosas propias de dysfunctional. ATENUANTE DECLARADO Y MEDIDO: la otra mitad "
             "del par, CULPAR Y ENTRENAR, llega VERBATIM por el INCISO al paso 2 de este mismo "
             "acto; lo que se pierde es el reflejo normativo. UNA SOLA PIEZA CON DOS SEDES, "
             "sellada una vez con las dos nombradas (acta 67, D10)"),
     "donde": "paso 3 de dysfunctional_organizational_culture_patterns y condicion 1 de ciclo_de_culpa",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("LA TASA DE ACCIDENTES QUE NO MEJORA PESE A LAS MEDIDAS CORRECTIVAS REPETIDAS, "
             "que es el unico disparador del acto que es MEDIBLE con una cifra. La condicion 2 "
             "del superviviente dice que los incidentes SE REPITEN a pesar de advertencias o "
             "sanciones, que es el hecho sin la medida"),
     "donde": "condicion 2 de ciclo_de_culpa",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador donde lo que se repite es LA RESPUESTA ORGANIZACIONAL SIN CAMBIOS "
             "SUSTANCIALES y no el incidente. Las condiciones del superviviente miran la "
             "repeticion del INCIDENTE y la escalada de la SANCION; ninguna mira la repeticion "
             "de la respuesta como sintoma en si"),
     "donde": "condicion 2 de dysfunctional_organizational_culture_patterns",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO34 = {
    "ciclo_de_culpa": {
        "pasos": {
            # EL UNICO INCISO DEL ACTO: la frase que da nombre al patron, repuesta
            # VERBATIM dentro del paso que el 2272 declara receptor.
            "1": ("INCISO", 2,
                  "patrones repetitivos de 'culpar y entrenar' tras incidentes",
                  ", identificando los "),
            "2": ("CUBIERTO", 3),   # con perdida y atenuante medido: causa raiz contra sintoma
            "3": ("CUBIERTO", 3),   # con perdida y atenuante: resolver o aparentar accion
            "4": ("CUBIERTO", 4),   # redirigir hacia los factores sistemicos: cubierto limpio
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # segunda sede de la perdida de la NUEVA NORMA
            "2": ("CUBIERTO", 2),   # con perdida: la tasa de accidentes que no mejora
        },
    },
    "dysfunctional_organizational_culture_patterns": {
        "pasos": {
            "1": ("APPEND",),       # LA INDEFENSION APRENDIDA como sintoma medible
            "2": ("APPEND",),       # LOS RITUALES REPETIDOS SIN EVIDENCIA DE EFECTIVIDAD
            "3": ("CUBIERTO", 2),   # con perdida y atenuante medido: LA NUEVA NORMA
            "4": ("APPEND",),       # SUSTITUIR LA EVITACION DE ANSIEDAD POR CAUSAS RAIZ
        },
        "condiciones": {
            "1": ("APPEND",),       # APATIA O RESIGNACION: el disparador de la indefension
            "2": ("CUBIERTO", 2),   # con perdida: lo que se repite es la respuesta
        },
    },
}


# ======================================================================
# ACTO 35: LA FAMILIA DE LA TRIBU DE MARCA.
# TRES miembros, DOS pares internos con veredicto y los DOS en A, CERO D,
# CERO nodos puente, CERO triangulos y CERO puertas.
# FORMA medida: CHOCAN (pasos a un lado, condiciones al otro), y por la
# letra decide LA PIEZA DECLARADA.
# ======================================================================

SUP35 = "construccion_tribu_de_marca"

MOTIVO35 = (
    "ACTO 35 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DE LA TRIBU DE MARCA. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE: los TRES "
    "miembros son del MISMO LIBRO (Never Lose a Customer Again, de Joey Coleman), tienen DOS "
    "pares internos con veredicto escrito de TRES combinaciones posibles y los DOS son de "
    "clase A (puestos 178 y 880), hay CERO pares D internos, CERO nodos puente y CERO "
    "triangulos, medido. El 178 llama a su par IDS CASI IDENTICOS y CANDIDATO A FUSION, y el "
    "880 titula el suyo LA MISMA TRIBU CON DOS NOMBRES y lo llama CANDIDATO CLARO A FUSION. "
    "P.8 EN ORDEN, Y LA FORMA ES CHOCAN: la vara de PASOS apunta a comunidad_tribu_marca (6 "
    "contra 5 y 5) y la de CONDICIONES apunta a construccion_tribu_de_marca (2 contra 1 y 1). "
    "Cuando dos varas de contenido CHOCAN decide LA PIEZA DECLARADA (acta 53, pregunta 3), y "
    "LA PIEZA DECLARADA AQUI ESTA ESCRITA CON TODAS SUS LETRAS: el 880 cierra diciendo que LO "
    "QUE HAY QUE SALVAR ES EL ETHOS Y LA TRANSFORMACION DE IDENTIDAD, y esas dos piezas son "
    "EXACTAMENTE los pasos 1 y 2 de construccion_tribu_de_marca. La pieza que la razon manda "
    "salvar vive dentro del nodo al que apunta la vara de condiciones, y no dentro del otro. "
    "Y NO ESTA SOLA: construccion_tribu_de_marca es ademas EL HUB DEL ACTO, el unico miembro "
    "que aparece en LOS DOS pares con veredicto, que es el mismo criterio con el que el puesto "
    "2639 resolvio el acto 36 de este mismo lote; y el CABLEADO apunta al mismo nodo (4 contra "
    "2 y 2). O sea que de las cuatro cuentas del acto, TRES apuntan a construccion_tribu_de_marca "
    "y una a comunidad_tribu_marca. ESTE CHOCAN NO DEJA RESIDUO. "
    "LA VARA DE PASOS SE PIERDE POR UNO Y SE DICE EN VEZ DE CALLARSE: 6 contra 5. Va MARCADO "
    "DISCUTIBLE. EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta, medido contra el universo protegido de "
    "256 ids. La guarda pasa POR VACIO. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; NINGUNA entrada de docs/plan/INVENTARIO.jsonl que no sea de tipo acto nombra a "
    "ninguno de los tres; y el barrido sobre docs/plan/OPERACIONES.jsonl devuelve UNA sola "
    "mencion, comunidad_tribu_marca dentro del campo nota de una ficha, que POR LA FRONTERA "
    "DEL ACTA 68 NO ES DUENO: dueno es el campo nodos, y ninguna ficha lo nombra ahi. Se "
    "declara en vez de callarse. "
    "UNA ARISTA INTERNA MEDIDA Y DECLARADA: marcador_visual_marca tiene a comunidad_tribu_marca "
    "en sus siguientes y comunidad_tribu_marca tiene a marcador_visual_marca en sus previos, o "
    "sea que los dos absorbidos estan cableados entre si. Al fundir, esa arista colapsa en un "
    "AUTO-PAR sobre el superviviente, que es exactamente lo que el censo cuenta aparte y no "
    "como colision. Va predicho aqui y medido en el censo."
)

NOTA35 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado. TRES APPEND DE PASO Y CERO DE CONDICION, "
    "mas UN INCISO al paso 4, y el nodo crece de 5 pasos a 8 y se queda en 2 condiciones. VA "
    "MARCADO DISCUTIBLE junto con el del acto 36. "
    "LOS TRES APPEND SON GESTOS DISTINTOS Y NO PARAMETROS, y por eso van enteros: CELEBRAR Y "
    "AMPLIFICAR LAS HISTORIAS DE LOS CLIENTES MAS COMPROMETIDOS; ESCUCHAR SU FEEDBACK Y DARLES "
    "VOZ VISIBLE DENTRO DE LA COMUNIDAD; y MONITOREAR EL EFECTO DE RECONOCIMIENTO DE MARCA "
    "GENERADO, que es el unico paso de medicion del acto y que el puesto 880 nombra con todas "
    "sus letras como LO PROPIO de marcador_visual_marca. El superviviente entra con cinco "
    "pasos que definen, crean y facilitan, y con ninguno que mida ni que devuelva la voz. "
    "EL UNICO INCISO VA AL PASO 4 Y REPONE EL SOPORTE DEL ESPACIO: FISICOS O DIGITALES, "
    "extraido VERBATIM del paso 2 de comunidad_tribu_marca. El paso 4 del superviviente manda "
    "facilitar espacios donde los miembros se reconozcan entre si y no dice de que clase son, "
    "que es justo lo que hace accionable el paso. NO termina en punto, asi que la guarda de la "
    "JUNTURA ROTA no salta, y no hay mas de un INCISO por paso. "
    "CERO APPEND DE CONDICION, Y SE DICE EN VEZ DE CALLARLO: las DOS condiciones de los dos "
    "absorbidos dicen lo mismo que las dos del superviviente (una base de clientes "
    "comprometidos sin comunidad formal, y el boca a boca por identidad compartida), leidas "
    "una a una. Ninguna es un DISPARADOR DISTINTO y por eso ninguna entra de APPEND, que es la "
    "letra del acta 55, pregunta 5. "
    "CUATRO PERDIDAS SELLADAS, UNA CON ATENUANTE DECLARADO Y MEDIDO y otra con ATENUANTE "
    "DECLARADO, contadas por maquina sobre esta misma lista."
)

PERDIDAS35 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL REQUISITO DE QUE EL SIMBOLO SEA FACILMENTE RECONOCIBLE EN CONTEXTOS PUBLICOS "
             "O SOCIALES, que es la prueba que separa un simbolo que funciona de uno que solo "
             "existe. El paso 3 del superviviente manda CREAR elementos visuales o simbolicos "
             "que permitan mostrar la afiliacion, pero no pone ninguna prueba sobre el "
             "resultado"),
     "donde": "paso 2 de marcador_visual_marca",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL PACKAGING DISTINTIVO como soporte del simbolo. ATENUANTE DECLARADO: el paso 3 "
             "del superviviente nombra MERCHANDISING E INSIGNIAS, asi que el soporte no se "
             "pierde entero; lo que se pierde es el envase, que es el unico de los tres que "
             "viaja con el producto y no con la persona"),
     "donde": "paso 3 de marcador_visual_marca",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("CONECTAR ENTRE SI como fin del espacio, frente a RECONOCERSE ENTRE SI. El "
             "reconocimiento es ver quien es de los mios; la conexion es hablarse. ATENUANTE "
             "DECLARADO Y MEDIDO: el INCISO al paso 4 de este mismo acto adosa VERBATIM la "
             "clase del espacio (FISICOS O DIGITALES), asi que el soporte no se pierde; lo que "
             "se pierde es el verbo"),
     "donde": "paso 2 de comunidad_tribu_marca",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("LA FIGURA DEL EMBAJADOR como aquello en lo que el cliente muy comprometido puede "
             "convertirse. La condicion 1 del superviviente mira la base de clientes FIELES sin "
             "comunidad formal, que es el punto de partida sin el destino"),
     "donde": "condicion 1 de comunidad_tribu_marca",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO35 = {
    "comunidad_tribu_marca": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # el espiritu o estilo de vida mas alla del producto
            # EL UNICO INCISO DEL ACTO: la clase del espacio, repuesta VERBATIM.
            "2": ("INCISO", 4,
                  "fisicos o digitales",
                  ", ya sean "),
            "3": ("CUBIERTO", 2),   # la narrativa que conecta con la identidad personal
            "4": ("CUBIERTO", 4),   # que los miembros se reconozcan entre si: cubierto literal
            "5": ("APPEND",),       # CELEBRAR Y AMPLIFICAR LAS HISTORIAS
            "6": ("APPEND",),       # ESCUCHAR EL FEEDBACK Y DAR VOZ VISIBLE
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: la figura del embajador
        },
    },
    "marcador_visual_marca": {
        "pasos": {
            "1": ("CUBIERTO", 3),   # identificar o disenar el elemento visual distintivo
            "2": ("CUBIERTO", 3),   # con perdida: reconocible en contextos publicos
            "3": ("CUBIERTO", 3),   # con perdida y atenuante: el packaging distintivo
            "4": ("CUBIERTO", 4),   # fomentar comunidad alrededor del simbolo
            "5": ("APPEND",),       # MONITOREAR EL EFECTO DE RECONOCIMIENTO: la unica medicion
        },
        "condiciones": {
            "1": ("CUBIERTO", 2),   # reconocimiento social y marketing organico: el boca a boca
        },
    },
}


# ======================================================================
# ACTO 36: LA FAMILIA DEL PLAN DE CONTROL DE JURAN.
# TRES miembros, DOS pares internos con veredicto y los DOS en A, CERO D,
# CERO nodos puente, CERO triangulos y CERO puertas.
# FORMA medida: CHOCAN, y la PIEZA DECLARADA nombra al superviviente
# VERBATIM en las DOS razones. Es el acto mejor declarado del lote.
# ======================================================================

SUP36 = "plan_de_control"

MOTIVO36 = (
    "ACTO 36 DEL TRAMO UNICO DE OP-U-02, LA FAMILIA DEL PLAN DE CONTROL DE JURAN. "
    "UNA SOLA FAMILIA, Y LA PREGUNTA DE P.5 SE CONTESTA CON LAS RAZONES DELANTE: los TRES "
    "miembros son del MISMO LIBRO (Juran's Quality Handbook, de Joseph A. Defeo), tienen DOS "
    "pares internos con veredicto escrito de TRES combinaciones posibles y los DOS son de "
    "clase A (puestos 2562 y 2639), hay CERO pares D internos, CERO nodos puente y CERO "
    "triangulos, medido. El 2562 dice SON EL MISMO ARTEFACTO y el 2639 dice LOS DOS SON EL "
    "PLAN DE CONTROL DE JURAN, EL MISMO BUCLE DE REALIMENTACION. "
    "EL SUPERVIVIENTE ESTA DECLARADO VERBATIM EN LAS DOS RAZONES, Y ESO ES LO QUE DECIDE: el "
    "2562 cierra con SOBREVIVE plan_de_control y el 2639 cierra con SOBREVIVE plan_de_control, "
    "EL BUCLE COMPLETO DE OCHO PASOS. El 2639 ademas nombra a plan_de_control EL HUB del acto. "
    "P.8 EN ORDEN, Y LA FORMA ES CHOCAN: la vara de PASOS apunta a plan_de_control (8 contra 6 "
    "y 6) y la de CONDICIONES apunta a matriz_de_control_de_proceso (2 contra 1 y 1). Cuando "
    "dos varas de contenido CHOCAN decide LA PIEZA DECLARADA (acta 53, pregunta 3), y aqui la "
    "declaracion no hay que interpretarla: esta escrita dos veces y con el nombre del nodo. El "
    "CABLEADO apunta a matriz_de_control_de_proceso (5 contra 4 y 3) y por la letra solo habla "
    "a contenido empatado, que aqui no empata. EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN. "
    "ESTE ACTO TRAE UN DISCUTIBLE HEREDADO DE SU PROPIO AUTOR Y NO SE ESCONDE: el 2639 cierra "
    "con DISCUTIBLE MARCADO, quien lea CAPACITAR A LOS DUENOS y AUDITAR LA EFECTIVIDAD como "
    "pasos enteros propios dira FUSION MUTUA, POR ELEGIR. El reparto de esta operacion "
    "responde a ese aviso de la unica forma que lo desactiva: LOS DOS pasos entran de APPEND y "
    "NINGUNO se sella como perdida, o sea que lo que la lectura contraria querria conservar "
    "queda vivo dentro del superviviente. Va MARCADO DISCUTIBLE igual. "
    "GUARDA 1B: NINGUNO de los tres miembros es puerta, medido contra el universo protegido de "
    "256 ids. La guarda pasa POR VACIO. "
    "DUENOS: los dos campos del fichero fijado del tramo estan VACIOS para este acto, medido "
    "hoy; NINGUNA entrada de docs/plan/INVENTARIO.jsonl que no sea de tipo acto nombra a "
    "ninguno de los tres; y el barrido sobre docs/plan/OPERACIONES.jsonl no devuelve ninguna "
    "mencion. El dueno es EL MEDIDO y aqui no hay ninguno."
)

NOTA36 = (
    "EL REPARTO DE ESTE ACTO, con su costo publicado. DOS APPEND DE PASO Y UN APPEND DE "
    "CONDICION, mas DOS INCISO, y el nodo crece de 8 pasos a 10 y de 1 condicion a 2. ES EL "
    "NODO MAS GRANDE QUE LA CAMPANA HA PRODUCIDO Y VA MARCADO DISCUTIBLE CON ESA PALABRA: DIEZ "
    "PASOS. El anterior mayor fueron NUEVE (acta 67, D8, y acta 69, D2). "
    "LA RAZON DE QUE SEA GRANDE ESTA MEDIDA Y NO ES CAPRICHO: el superviviente ENTRA con ocho "
    "pasos porque el 2562 lo describe como el nodo MAS GRANULADO de los tres (separa la "
    "medicion del registro y separa a quien analiza de quien actua), y los dos que se le adosan "
    "son los DOS que el 2639 nombra como LINEAS A REPONER. Y NO ES UNA PUERTA: ningun miembro "
    "del acto lo es, medido, asi que este nodo no es de los que la gente ve al entrar. "
    "LOS DOS APPEND SON LAS DOS LINEAS QUE LA RAZON MANDA REPONER: CAPACITAR A LOS DUENOS DEL "
    "PROCESO EN EL USO DEL PLAN DE CONTROL, que es la unica pieza del acto sobre las personas "
    "que van a operarlo; y AUDITAR PERIODICAMENTE LA EFECTIVIDAD DEL PLAN DE CONTROL, que NO "
    "es lo mismo que el paso 8 del superviviente: aquel REVISA LA MATRIZ, o sea el documento, "
    "una vez; este AUDITA EL PLAN EN OPERACION y periodicamente. Se dice la diferencia porque "
    "es lo unico que justifica el paso 10. "
    "LOS DOS INCISO VAN A PASOS DISTINTOS Y NINGUNO SE APILA (acta 64), y los dos reponen "
    "piezas que las razones nombran: al paso 3, la especificacion de UNIDAD DE MEDIDA, SENSOR, "
    "FRECUENCIA Y TAMANO DE MUESTRA, que es lo que convierte DEFINIR COMO SE MEDIRA en algo "
    "ejecutable; y al paso 8, la revision por COBERTURA DE VARIABLES CRITICAS Y VELOCIDAD DE "
    "RESPUESTA, que es EXACTAMENTE la linea que el 2562 sella como UNA LINEA A REPONER EN LA "
    "OPERACION DE FUSION. Los dos pasos receptores NO terminan en punto, asi que la guarda de "
    "la JUNTURA ROTA no salta en ninguno. "
    "Y POR ESO ESTE ACTO SELLA POCAS PERDIDAS: TRES. Las dos piezas que las razones mandaban "
    "reponer estan REPUESTAS (una por INCISO y las dos lineas del 2639 por APPEND), asi que no "
    "se sellan como perdidas: una perdida sellada que en realidad no se pierde infla la cuenta. "
    "Se dice para que la cifra baja no se lea como descuido. "
    "DOS ABSORBIDOS CUYOS PASOS SE PARTEN EN DOS DEL SUPERVIVIENTE, dicho porque la marca solo "
    "puede apuntar a uno: el paso 3 de matriz_de_control_de_proceso (COMO, DONDE Y CUANDO se "
    "medira) vive repartido entre los pasos 3 y 4 del superviviente, y su paso 4 (QUIEN "
    "ANALIZA Y QUIEN ACTUA) entre los pasos 5 y 6. La marca apunta al PRIMERO de los dos y no "
    "hay perdida: las dos mitades estan vivas. "
    "UNA PERDIDA CON ATENUANTE DECLARADO, contada por maquina sobre esta misma lista."
)

PERDIDAS36 = [
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("EL NOMBRE JURAN DEL SUJETO DE CONTROL: LAS CARACTERISTICAS DEL PRODUCTO O DEL "
             "PROCESO A MONITOREAR, y el verbo SELECCIONAR. El paso 1 del superviviente manda "
             "IDENTIFICAR LAS VARIABLES QUE AFECTAN AL REMEDIO Y AL CLIENTE, que es el mismo "
             "sujeto nombrado por su efecto y no por lo que es, y pierde el termino del libro"),
     "donde": "paso 1 de control_mantener_ganancias",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE PARAMETRO DE PASO",
     "que": ("LA META ACEPTABLE DE DESEMPENO como alternativa explicita al limite de control "
             "estadistico. ATENUANTE DECLARADO: el paso 2 del superviviente dice IDEALMENTE UN "
             "LIMITE DE CONTROL, y esa palabra deja la puerta abierta a otro estandar; lo que "
             "se pierde es que la alternativa este NOMBRADA en vez de solo permitida"),
     "donde": "paso 2 de control_mantener_ganancias",
     "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente"},
    {"especie": "DE CONDICIONES",
     "que": ("el disparador dicho como REMEDIO YA IMPLEMENTADO con la garantia de QUE EL "
             "PROBLEMA NO VUELVA A OCURRIR. La condicion 1 del superviviente mira la MEJORA DE "
             "PROCESO COMPLETADA y el SOSTENER LOS RESULTADOS, que es el mismo momento dicho "
             "por lo que se conserva y no por lo que se teme"),
     "donde": "condicion 1 de control_mantener_ganancias",
     "enrutada_a": "la fase 04, mientras el INCISO de condiciones no exista (acta 55, pregunta 5)"},
]

REPARTO36 = {
    "matriz_de_control_de_proceso": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # identificar las variables que afectan al remedio y al cliente
            "2": ("CUBIERTO", 2),   # el estandar que dispara la accion
            "3": ("CUBIERTO", 3),   # como, donde y cuando: se parte entre los pasos 3 y 4
            "4": ("CUBIERTO", 5),   # quien analiza y quien actua: se parte entre los pasos 5 y 6
            "5": ("CUBIERTO", 7),   # los pasos para regresar el proceso a control
            # INCISO 2 DEL ACTO: la linea que el 2562 sella como A REPONER.
            "6": ("INCISO", 8,
                  "cobertura de variables criticas y velocidad de respuesta",
                  ", y también su "),
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # mejora completada y sostenerla en el tiempo
            "2": ("APPEND",),       # CLARIDAD SOBRE RESPONSABILIDADES: disparador distinto
        },
    },
    "control_mantener_ganancias": {
        "pasos": {
            "1": ("CUBIERTO", 1),   # con perdida: el nombre Juran del sujeto de control
            "2": ("CUBIERTO", 2),   # con perdida y atenuante: la meta aceptable de desempeno
            # INCISO 1 DEL ACTO: lo que vuelve ejecutable el paso 3 del superviviente.
            "3": ("INCISO", 3,
                  "unidad de medida, sensor, frecuencia y tamano de muestra",
                  ", especificando "),
            "4": ("CUBIERTO", 5),   # criterios de accion y responsables
            "5": ("APPEND",),       # CAPACITAR A LOS DUENOS DEL PROCESO (linea a reponer del 2639)
            "6": ("APPEND",),       # AUDITAR PERIODICAMENTE LA EFECTIVIDAD (linea a reponer del 2639)
        },
        "condiciones": {
            "1": ("CUBIERTO", 1),   # con perdida: el remedio implementado y la no recurrencia
        },
    },
}


LOTE_F = {
    "titulo": ("LOTE F DEL TRAMO UNICO DE OP-U-02. ABRE EN EL ACTO 32, que es donde la "
               "adjudicacion 2 del acta 69 manda abrir el prefijo: el acto 31 TIENE DUENO "
               "MEDIDO (OP-F-04-WEI y OP-S-04 en duenos_cualquier_operacion, leido hoy del "
               "fichero fijado del tramo) y NO es una fusion de OP-U-02, asi que su salto va "
               "DECLARADO con esa cita y NO rompe el prefijo sin saltos, porque el 31 no esta "
               "en la cola de fusiones de esta operacion. CINCO ACTOS CIERRAN ENTEROS Y SON 15 "
               "NODOS: los actos 32, 33, 34, 35 y 36 cierran los CINCO FUNDIDOS y NINGUNO "
               "cierra DECLARADO Y NO FUNDIDO. Es el primer lote del tramo sin ningun "
               "DECLARADO, y esta anticipado: la adjudicacion 4 del acta 69 midio que en lo "
               "que resta del tramo no hay actos con nodo puente ni con par D interno, asi que "
               "P.10 y el cuarto motivo quedan SIN SUJETO; de los otros dos motivos, la guarda "
               "1B pasa POR VACIO en los cinco actos (CERO puertas dentro de cada uno, medido) "
               "y P.5 contesta UNA FAMILIA en los cinco. EL TOPE DEL PREFIJO ES ESTRUCTURAL Y "
               "SE DICE: el siguiente es el ACTO 37, que TIENE DUENO (OP-S-07 en "
               "duenos_cualquier_operacion, medido hoy) y sobre el que la adjudicacion 2 del "
               "acta 69 dice con todas sus letras que vale lo mismo que para el 31. El acto 37 "
               "se leyo entero igual, por el carril del D16 del acta 68 (la letra prohibe "
               "FUNDIR un acto con dueno, no leerlo): esta en el dossier y en las varas de "
               "esta vuelta, su forma medida es UNA SOLA VARA y su destino queda con su dueno "
               "en su fase"),
    "actos": [
        {
            "orden": 32,
            "superviviente": SUP32,
            "motivo": MOTIVO32,
            "nota": NOTA32,
            "reparto": REPARTO32,
            "perdidas": PERDIDAS32,
        },
        {
            "orden": 33,
            "superviviente": SUP33,
            "motivo": MOTIVO33,
            "nota": NOTA33,
            "reparto": REPARTO33,
            "perdidas": PERDIDAS33,
        },
        {
            "orden": 34,
            "superviviente": SUP34,
            "motivo": MOTIVO34,
            "nota": NOTA34,
            "reparto": REPARTO34,
            "perdidas": PERDIDAS34,
        },
        {
            "orden": 35,
            "superviviente": SUP35,
            "motivo": MOTIVO35,
            "nota": NOTA35,
            "reparto": REPARTO35,
            "perdidas": PERDIDAS35,
        },
        {
            "orden": 36,
            "superviviente": SUP36,
            "motivo": MOTIVO36,
            "nota": NOTA36,
            "reparto": REPARTO36,
            "perdidas": PERDIDAS36,
        },
    ],
    "declarados": [],
}
