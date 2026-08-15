"""Vuelta 31: sella OP-F-04-COL, SEGUNDO TIEMPO. La tanda de Coleman.

EL PRIMER TIEMPO YA ESTA HECHO Y NO SE REHACE: las fronteras de los quince estan
leidas y publicadas en docs/plan/01_FUENTES.md (la tabla de doce de la vuelta 30,
mas viral_loop_marketing por P.20 y voz_del_cliente_voc y metas_vs_proposito de
antes). Lo que este sellador anade es el DESTINO por P.18 sobre la nomina de la
familia Coleman MEDIDA AL DIA (83 nodos vivos, 68 con fuente unica, corrida de
hoy en docs/loop/SALIDA_V31_FAMILIA_COLEMAN.txt), que es lo que P.18 punto 1
obliga.

SON TRECE DESTINOS, no quince, y la cuenta la confirmo el acta de la vuelta 30 en
su adjudicacion 5 (linea 6639, leida hoy): quince de la nomina, menos
viral_loop_marketing (su mitad ya la hizo el corte unico de P.20 en la vuelta 30 y
la nota de la operacion lo cita) menos keep_customers_strategy (adjudicado
MULTIFUENTE LEGITIMO sin corte por extension citable de P.19, acta 30 punto 2).

blueprint_de_experiencia SE PARTE EN SUBBLOQUES POR OBJETO, y el encargo lo
autoriza con su motivo escrito: la frontera es de LIBROS y el destino es de
OBJETOS, y su bloque 5 a 17 trae al menos tres actos distintos (la postventa
proactiva, el ritual del si y los cien dias), como la propia fila de la tabla de
01_FUENTES.md declara. Cada subbloque lleva su lectura y su destino propios.

Uso: python scripts/loop/vuelta31_sellar_col.py
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop", "PLAN_V31_OPF04_COL.json")

COLEMAN = "Never Lose a Customer Again - Joey Coleman"


def todos():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.load(open(os.path.join(NODOS, nombre), encoding="utf-8"))
            fuera[d["node_id"]] = d
    return fuera


# ---------------------------------------------------------------------------
# LOS CINCO NODOS PROPIOS, cada uno por P.18 PUNTO 3: ningun miembro de la nomina
# de hoy tiene ese objeto, y forzar un encaje es lo que la regla prohibe. El
# motivo de cada uno va en su corte, con los candidatos descartados por nombre.
# ---------------------------------------------------------------------------

PERSONALIZACION = {
    "node_id": "personalizacion_guiada_por_el_cliente",
    "fase_proyecto": "ejecucion",
    "dominio": "core",
    "titulo_concepto": "Personalizacion Guiada y el Simbolo de la Decision del Cliente",
    "fuente": COLEMAN,
    "resumen_teorico": (
        "Dejar que tu cliente decida sobre tu producto no es lo mismo que dejarlo solo delante "
        "de un catalogo de opciones. Primero eliges en que partes de tu producto o servicio la "
        "decision es suya de verdad, y despues disenas el camino para que tomarla sea facil en "
        "vez de abrumador: demasiadas opciones sin guia paralizan y el cliente abandona a mitad. "
        "La segunda mitad es la que casi nadie hace: cuando tu cliente ya decidio, devuelvele esa "
        "decision convertida en algo que pueda tocar o ensenar. Un objeto tangible o simbolico "
        "que represente lo que eligio, y cuando tenga sentido, mostrarlo de forma visible, "
        "convierte una eleccion privada en un compromiso que el cliente reconoce como propio."
    ),
    "entregable_esperado": (
        "El mapa de las decisiones de personalizacion que tu cliente puede tomar, el proceso "
        "guiado que se las hace faciles, y el objeto tangible o simbolico con el que le "
        "devuelves esa decision"
    ),
    "nodos_previos": ["cliente_disena_producto"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando tu producto admite decisiones de personalizacion y no sabes cuales dejar en "
        "manos de tu cliente sin abrumarlo",
        "Cuando tu cliente elige algo importante y no recibe nada tangible que se lo recuerde",
    ],
    "etiqueta_arbol": "Deja Decidir a tu Cliente",
}

SILLA = {
    "node_id": "silla_vacia_del_cliente_en_decisiones",
    "fase_proyecto": "ejecucion",
    "dominio": "core",
    "titulo_concepto": "La Silla Vacia del Cliente en las Reuniones de Decision",
    "fuente": COLEMAN,
    "resumen_teorico": (
        "En las reuniones internas donde se deciden las cosas que afectan al cliente, el cliente "
        "no esta. Todos hablan de el y nadie habla por el, y la conversacion se inclina sola "
        "hacia lo que le conviene a la operacion. El remedio es fisico y barato: instalar un "
        "simbolo permanente que represente al cliente en esa mesa, como la silla vacia que Amazon "
        "usa, para que quede a la vista que hay una parte interesada que no puede replicar. No es "
        "decoracion: el simbolo funciona cuando alguien tiene el encargo de ocuparlo y la reunion "
        "tiene la costumbre de preguntarle antes de cerrar la decision."
    ),
    "entregable_esperado": (
        "Un simbolo del cliente instalado en tus reuniones internas de decision, con la regla "
        "escrita de quien lo ocupa y en que momento de la reunion se le pregunta"
    ),
    "nodos_previos": ["cultura_de_experiencia", "customer_journey_mapping"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando las decisiones internas se toman por comodidad operativa y el cliente aparece "
        "solo al final, si aparece",
        "Cuando quieres instalar un recordatorio permanente en vez de una campana de una vez",
    ],
    "etiqueta_arbol": "Sienta al Cliente en tu Mesa",
}

INCENTIVOS = {
    "node_id": "incentivos_internos_alineados_a_retencion",
    "fase_proyecto": "ejecucion",
    "dominio": "core",
    "titulo_concepto": "Alineacion de los Incentivos Internos con la Retencion del Cliente",
    "fuente": COLEMAN,
    "resumen_teorico": (
        "La gente hace aquello por lo que se le paga, y en la mayoria de los negocios se paga por "
        "cerrar cuentas nuevas y por atender rapido. Las dos cosas suenan bien y las dos empujan "
        "en contra de la relacion: la primera deja al cliente recien firmado sin dueno, y la "
        "segunda premia despachar la llamada antes que resolver el problema. Corregirlo pide "
        "auditar los esquemas que ya tienes y preguntarles a que premian de verdad, poner "
        "metricas y bonos ligados a retencion, satisfaccion y valor vitalicio del cliente, "
        "quitar los incentivos que premian la rapidez por encima de la calidad de la relacion, y "
        "sentar a quien responde por la experiencia del cliente donde se toman las decisiones "
        "ejecutivas, que es la unica forma de que esa voz no dependa de la buena voluntad ajena."
    ),
    "entregable_esperado": (
        "La auditoria de tus incentivos actuales con lo que premian hoy, y el esquema corregido: "
        "metricas y bonos ligados a retencion, satisfaccion y valor vitalicio, los incentivos "
        "daninos retirados, y el asiento ejecutivo de quien responde por la experiencia"
    ),
    "nodos_previos": ["diseno_estructura_recompensas_roles"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando tu equipo cobra por vender y nadie cobra por que el cliente se quede",
        "Cuando la atencion al cliente se mide por tiempo de llamada y no por problema resuelto",
    ],
    "etiqueta_arbol": "Premia Retener, no solo Vender",
}

AUTOSANACION = {
    "node_id": "autoservicio_y_autosanacion_del_producto",
    "fase_proyecto": "ejecucion",
    "dominio": "core",
    "titulo_concepto": "Autoservicio y Autosanacion del Producto",
    "fuente": COLEMAN,
    "resumen_teorico": (
        "Cada llamada de soporte es un sintoma: en algun punto tu producto le pidio a tu cliente "
        "algo que no supo resolver solo. La cura no empieza por reforzar el soporte sino por "
        "mirar que puntos de friccion generan esas llamadas, y despues por darle la vuelta a "
        "quien avisa: en vez de esperar a que tu cliente descubra el fallo y te escriba, el "
        "producto detecta la anomalia y le avisa el primero, con lo que ya esta haciendo para "
        "arreglarla. Encima de eso se construyen las herramientas de autoservicio y "
        "autosanacion, para que el problema se resuelva sin que nadie tenga que intervenir. Y "
        "todo esto se mide con una sola cifra honesta: que porcentaje de los problemas se "
        "resuelve sin intervencion humana."
    ),
    "entregable_esperado": (
        "El inventario de las fricciones de tu producto que generan llamadas de soporte, los "
        "mecanismos de deteccion proactiva con aviso automatico a tu cliente, las herramientas "
        "de autoservicio construidas, y el porcentaje de problemas resueltos sin intervencion "
        "humana"
    ),
    "nodos_previos": ["sistema_inmune_producto"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando el volumen de soporte crece al mismo ritmo que los clientes y no hay forma de "
        "contratar a esa velocidad",
        "Cuando tu cliente se entera de los fallos de tu producto antes que tu",
    ],
    "etiqueta_arbol": "Resuelve sin que te Llamen",
}

OBSERVAR = {
    "node_id": "observar_al_cliente_en_su_contexto",
    "fase_proyecto": "ejecucion",
    "dominio": "core",
    "titulo_concepto": "Observar a tu cliente en su contexto (segundo paso del metodo IOPS)",
    "fuente": COLEMAN,
    "resumen_teorico": (
        "Es el segundo paso del metodo IOPS (investigar, observar, personalizar, sorprender), y "
        "el que casi siempre se salta. Investigar te da datos que tu cliente te conto; observar "
        "te da lo que hace cuando nadie le pregunta. Se practica yendo a verlo usar tu producto "
        "en su contexto real con una cadencia fija, y poniendote tu mismo en su lugar para "
        "recorrer tu producto desde cero como si fueras el, que es cuando aparecen las asperezas "
        "que dejaste de ver por costumbre. Lo que vale casi nunca es la respuesta a una pregunta: "
        "son los detalles pequenos y los comentarios casuales, las pepitas de oro que ninguna "
        "encuesta captura. Por eso se anota en caliente y se relee uno o dos dias despues, "
        "cuando ya se puede buscar el patron en vez del episodio."
    ),
    "entregable_esperado": (
        "Tu cuaderno de observacion con lo que viste en el contexto real de tu cliente, anotado "
        "en caliente y releido a los dos dias, y los patrones o momentos clave que salieron de "
        "ahi para mejorar su experiencia"
    ),
    "nodos_previos": ["voz_del_cliente_voc", "investigar_datos_cliente"],
    "nodos_siguientes": ["personalizar_interacciones_cliente"],
    "condiciones_activacion": [
        "Cuando ya reuniste los datos de tu cliente y no sabes que hacer con ellos",
        "Cuando tus decisiones de producto salen de encuestas y de lo que el cliente dice, y "
        "nunca de verlo usarlo",
    ],
    "etiqueta_arbol": "Observa a tu Cliente de Verdad",
}


# ---------------------------------------------------------------------------
# LOS CORTES. (origen, indices, fuente que queda, destino, huella, motivo P.18)
# La lectura de cada destino se hizo HOY sobre la nomina de la familia Coleman
# medida hoy. El motivo dice POR QUE el objeto coincide, que es lo que P.18
# punto 2 obliga, y nombra a los candidatos descartados donde hubo mas de uno.
# ---------------------------------------------------------------------------
CORTES = [
    # ---- blueprint_de_experiencia: SEIS subbloques por objeto (bloque 5 a 17) ----
    ("blueprint_de_experiencia", [5, 6, 7],
     "Change by Design",
     ("miembro", "comunicacion_proactiva_puntos_estres"),
     "a las 2 horas, a las 24 horas",
     "P.18. SUBBLOQUE 1 del bloque 5 a 17, por objeto: la postventa que se adelanta. Los tres "
     "pasos documentan el proceso postventa, localizan los momentos de mayor ansiedad o "
     "incertidumbre del cliente y programan seguimientos a horas fijas SIN esperar a que se "
     "queje. El entregable del miembro es literal a eso: lista de puntos de estres identificados "
     "y sistema de notificaciones proactivas implementado para cada uno. Descartado "
     "experiencia_del_cliente_proactiva, cuyo objeto es la DISTINCION entre servicio reactivo y "
     "experiencia proactiva y cuyo entregable es un mapa emocional con metrica base, no el "
     "calendario de seguimientos."),

    ("blueprint_de_experiencia", [8],
     "Change by Design",
     ("miembro", "rediseno_procesos_negocio_cliente"),
     "formularios, papeleo",
     "P.18. SUBBLOQUE 2, un solo paso y objeto propio: simplificar formularios y papeleo con "
     "herramientas digitales es una FRICCION AUTOINFLIGIDA, la que el negocio se causa a si "
     "mismo con sus propios tramites, que es exactamente el objeto del miembro (su ejemplar es "
     "Comcast). No va con los tres anteriores porque aquellos anticipan una emocion del cliente "
     "y este quita un obstaculo que puso la casa."),

    ("blueprint_de_experiencia", [9, 10, 11, 13],
     "Change by Design",
     ("miembro", "fase_admit_celebracion"),
     "se convierte oficialmente en cliente",
     "P.18. SUBBLOQUE 3, el ritual del si: identificar el instante exacto en que el prospecto se "
     "vuelve cliente (el pago, la firma), disenar el ritual de ese momento, dejarle un recuerdo "
     "que pueda conservar e involucrar al equipo en la celebracion. El miembro es la fase Admit "
     "de Coleman y su entregable es el diseno de un momento de celebracion o bienvenida tangible "
     "en el instante de la compra: mismo objeto, palabra por palabra. Descartado "
     "celebracion_hitos_cliente, que celebra los LOGROS del cliente durante la relacion, no el "
     "momento de la compra."),

    ("blueprint_de_experiencia", [12],
     "Change by Design",
     ("miembro", "calibracion_intensidad_celebracion"),
     "evita sobreactuar",
     "P.18. SUBBLOQUE 4, un solo paso, y sale del anterior a proposito: alinear la INTENSIDAD de "
     "la celebracion con la naturaleza del producto y evitar sobreactuar es el objeto entero del "
     "miembro (su titulo es no alcanzar el pico demasiado pronto y su entregable una guia de "
     "niveles de celebracion segun tipo de producto y ticket promedio). Dejarlo dentro del "
     "subbloque 3 habria escondido una advertencia que tiene nodo propio en la familia."),

    ("blueprint_de_experiencia", [15],
     "Change by Design",
     ("miembro", "handoff_transicion_ventas_cuentas"),
     "no se pierda información ni calidez",
     "P.18. SUBBLOQUE 5, un solo paso: redisenar el traspaso entre quien vende y quien da "
     "soporte para que no se pierda ni la informacion ni la calidez. El miembro es ese traspaso "
     "con nombre propio y su entregable es un protocolo estandarizado vendedor a cuenta con "
     "guion o checklist replicable. Descartados dos hermanos con el mismo tema y otro objeto: "
     "desconexion_ventas_experiencia diagnostica POR QUE ocurre (los incentivos de quien vende) "
     "y traspaso_ventas_cuentas vigila que lo prometido llegue intacto; el paso pide el REDISENO "
     "del traspaso, que es el objeto del miembro elegido."),

    ("blueprint_de_experiencia", [14, 16, 17],
     "Change by Design",
     ("miembro", "fase_acclimate_mapa_de_proceso"),
     "entre la compra y el día 100",
     "P.18. SUBBLOQUE 6, los cien dias: listar todos los puntos de contacto entre la compra y el "
     "dia 100, poner hitos de comunicacion proactiva distribuidos en ese periodo y asignar un "
     "responsable por punto de contacto midiendo la consistencia. El entregable del miembro es "
     "un mapa visual del proceso de onboarding y un calendario de comunicaciones por hito: el "
     "mapa y el calendario son los pasos 14 y 16, y el responsable por punto es como ese mapa se "
     "ejecuta. Descartado fase_acclimate_experiencia_cliente, cuyo entregable mira los RIESGOS "
     "DE ABANDONO por etapa y no el calendario, y descartado estrategia_multicanal_bienvenida, "
     "que reparte los touchpoints POR CANAL (los seis medios de Coleman) y no por el tiempo."),

    # ---- cliente_disena_producto ----
    ("cliente_disena_producto", [5, 6, 7, 8],
     "Winning at New Products - Robert G. Cooper",
     ("nodo_propio", PERSONALIZACION),
     "co-crear no lo abrume",
     "P.18 PUNTO 3. Barrida la nomina de hoy, NINGUN miembro tiene por objeto que sea EL CLIENTE "
     "quien tome la decision de personalizacion: micro_experiencias_personalizadas captura "
     "preferencias que recoge EL EQUIPO para hacer gestos, y personalizar_interacciones_cliente "
     "es el tercer paso de IOPS, mensajes que escribe la empresa. En los cuatro pasos quien "
     "decide es el cliente y la empresa solo pone el camino y le devuelve el simbolo de lo que "
     "eligio. El bloque forma nodo propio dentro de la familia."),

    # ---- cultura_de_experiencia ----
    ("cultura_de_experiencia", [9, 10, 11],
     "Change by Design",
     ("miembro", "rediseno_procesos_negocio_cx"),
     "peer-to-peer a gran escala",
     "P.18: el entregable del miembro es un plan de transformacion de tus procesos CON FORMACION "
     "PARA TU GENTE Y MENOS HERRAMIENTAS DUPLICADAS, y los tres pasos son esas dos cosas: "
     "diagnosticar si los empleados saben que la experiencia del cliente es parte de su trabajo, "
     "el programa de capacitacion peer-to-peer a gran escala con plazos, y unificar las "
     "herramientas internas de informacion del cliente. Descartado el propio nodo donante como "
     "destino: los pasos 1 a 8 que se quedan son Change by Design (inmersion y talleres), y este "
     "bloque es la transformacion operativa de Coleman."),

    ("cultura_de_experiencia", [12],
     "Change by Design",
     ("nodo_propio", SILLA),
     "símbolo o recordatorio del cliente",
     "P.18 PUNTO 3. Ningun miembro tiene por objeto instalar un simbolo permanente del cliente en "
     "las reuniones internas de decision: persuasion_directivos_prioridad_cliente arma un caso "
     "con datos para convencer a quien decide UNA vez, y pensamiento_h2h es la mirada de persona "
     "a persona en la venta. El paso pide un artefacto de gobierno permanente. Y el mismo objeto "
     "aparece en el bloque de customer_journey_mapping (paso 9, la silla vacia): los DOS van al "
     "MISMO nodo propio por la adjudicacion 3 del acta de la vuelta 27, que prohibe fabricar el "
     "gemelo. La costura que eso crea dentro del nodo nuevo se declara en el reporte y entra por "
     "LA PRIMERA PUERTA de la cola (08_VERIFICACION.md, registro de la vuelta 30)."),

    # ---- customer_journey_mapping ----
    ("customer_journey_mapping", [6, 7, 8],
     "Change by Design, Revised and U - Tim Brown",
     ("miembro", "rediseno_procesos_negocio_cliente"),
     "se pasan la responsabilidad del cliente",
     "P.18: el objeto del miembro son las fricciones que causa la propia estructura interna, y "
     "los tres pasos son su diagnostico exacto: mapear los journeys por area (facturacion, "
     "soporte, onboarding), localizar en que punto los departamentos se pasan la responsabilidad "
     "del cliente sin resolver, y medir el impacto cuantitativo del mal servicio (llamadas "
     "repetidas, visitas tecnicas, abandono), que es el mecanismo de compensacion y la metrica "
     "de impacto de su entregable. Descartado persuasion_directivos_prioridad_cliente para el "
     "paso 8: ahi la cifra se usa para CONVENCER a quien decide, y aqui para localizar la "
     "friccion que se va a redisenar."),

    ("customer_journey_mapping", [9],
     "Change by Design, Revised and U - Tim Brown",
     ("miembro", "silla_vacia_del_cliente_en_decisiones"),
     "silla vacía representando al cliente",
     "P.18, MISMO destino que el paso 12 de cultura_de_experiencia, y por la misma adjudicacion 3 "
     "del acta de la vuelta 27: los dos pasos son el MISMO objeto de Coleman escrito en dos "
     "nodos anfitriones (el simbolo del cliente en la reunion interna), y partirlos en dos nodos "
     "propios habria fabricado el gemelo que la campana existe para deshacer. El nodo propio lo "
     "crea el corte anterior de este mismo plan."),

    ("customer_journey_mapping", [10],
     "Change by Design, Revised and U - Tim Brown",
     ("miembro", "rediseno_procesos_negocio_cx"),
     "sistema unificado de gestión de cuentas",
     "P.18, MISMO destino que el paso 11 de cultura_de_experiencia: consolidar las herramientas "
     "internas dispersas en un sistema unificado de gestion de cuentas es la linea MENOS "
     "HERRAMIENTAS DUPLICADAS del entregable del miembro. Los dos pasos dicen lo mismo con "
     "distintas palabras y por eso van al mismo sitio; la costura se declara en el reporte y "
     "entra por LA PRIMERA PUERTA de la cola."),

    # ---- diseno_estructura_recompensas_roles ----
    ("diseno_estructura_recompensas_roles", [4, 5, 6, 7],
     "The Founder's Dilemmas",
     ("nodo_propio", INCENTIVOS),
     "premian solo adquisición",
     "P.18 PUNTO 3. Ningun miembro tiene por objeto los INCENTIVOS INTERNOS alineados a la "
     "retencion: desconexion_ventas_experiencia usa esa desalineacion como CAUSA de un traspaso "
     "roto y su entregable es el proceso de traspaso con su CRM, y "
     "persuasion_directivos_prioridad_cliente arma el caso economico para convencer a quien "
     "decide. Los cuatro pasos son una auditoria y un rediseno del esquema de compensacion "
     "(bonos ligados a retencion y valor vitalicio, quitar el premio a la rapidez, sentar al "
     "lider de experiencia en el comite ejecutivo), que es un objeto propio. Forma nodo propio "
     "dentro de la familia."),

    # ---- estrategia_crecimiento_clientes ----
    ("estrategia_crecimiento_clientes", [7, 8, 10],
     "The Startup Owner's Manual - Steve Blank",
     ("miembro", "incentivos_no_monetarios_advocacy"),
     "mecánica simple de referido",
     "HUELLA CAMBIADA Y DECLARADA: la primera eleccion fue 'bajo costo marginal' (paso 7) y la "
     "guarda del sellador la paro porque ESA huella YA VIVE en el nodo destino "
     "(incentivos_no_monetarios_advocacy). Una prueba que el destino ya pasa antes del corte no "
     "prueba nada, que es la leccion de la huella insatisfacible de la vuelta 30. Se cambio a la "
     "mecanica del paso 8, que vive solo en el origen. "
     "P.18: el miembro son los incentivos que impulsan la advocacy sin dinero, y su ejemplar es "
     "dar mas del propio producto (el almacenamiento extra de Dropbox), que es LITERALMENTE el "
     "paso 7 (mayor valor percibido para el cliente y bajo costo marginal para ti). Su entregable "
     "pide la estructura VALIDADA CON METRICAS DE ADOPCION Y REFERIDOS, que es el paso 10, y la "
     "mecanica del paso 8 (codigo, link, verificacion) es como ese incentivo se entrega. "
     "Descartado programa_referidos_exclusividad, cuyo objeto es limitar la cantidad de referidos "
     "por exclusividad y escasez, lo contrario de un incentivo abierto."),

    ("estrategia_crecimiento_clientes", [9],
     "The Startup Owner's Manual - Steve Blank",
     ("miembro", "timing_solicitud_referidos"),
     "fase Adopt/Advocate",
     "P.18, un paso con destino propio: comunicar el programa en los momentos clave del ciclo de "
     "vida, nombrando la fase Adopt y Advocate, es el objeto entero del miembro (el punto de "
     "activacion optimo para pedir una referencia, que si se pide antes del logro la destruye). "
     "Su entregable es la definicion documentada de ese punto con la automatizacion configurada. "
     "Meterlo con los otros tres habria escondido el unico paso que habla de CUANDO."),

    # ---- ganar_comprension_del_cliente ----
    ("ganar_comprension_del_cliente", [7, 8, 9, 10],
     "The Startup Owner's Manual - Steve Blank",
     ("miembro", "investigar_datos_cliente"),
     "entre 5 y 10 datos prioritarios",
     "P.18: el miembro es el PRIMER paso del metodo IOPS de Coleman, investigar, y su entregable "
     "es tu CRM con los datos personales y emocionales de cada cliente. Los cuatro pasos son ese "
     "procedimiento: elegir la herramienta que de verdad vas a usar, definir entre cinco y diez "
     "datos prioritarios, completar lo que ya sabes y no registraste, e investigar los perfiles "
     "publicos. Descartado seguimiento_informacion_cliente, cuyo objeto es la FICHA estructurada "
     "y su actualizacion regular, es decir el mantenimiento del sistema, no el arranque."),

    ("ganar_comprension_del_cliente", [11],
     "The Startup Owner's Manual - Steve Blank",
     ("miembro", "conexion_personal_emocional"),
     "carga afectiva positiva",
     "P.18, un paso con destino propio: priorizar los datos PERSONALES (unicos de cada persona) y "
     "EMOCIONALES (con carga afectiva) es la definicion misma del miembro, que existe para "
     "distinguir esas dos clases de dato y explicar que el que es las dos cosas a la vez vale el "
     "doble. Es el criterio de seleccion, no el acto de registrar: por eso no va con los cuatro "
     "anteriores."),

    # ---- metas_vs_proposito ----
    ("metas_vs_proposito", [5, 6, 7, 8, 9],
     "Assembling Tomorrow: A Guide to Designing a Thriving Future",
     ("miembro", "fase_accomplish_experiencia_cliente"),
     "objetivo superficial que el cliente dice buscar",
     "P.18: el miembro es la fase Accomplish de Coleman, verificar que el cliente logro DE VERDAD "
     "el objetivo por el que te compro, y su resumen ya distingue los escenarios en que el logro "
     "es solo nominal. Los cinco pasos son ese procedimiento: separar el objetivo declarado del "
     "deseo real, poner un punto de seguimiento POSTERIOR al logro aparente (pedir la foto, "
     "confirmar el resultado), sostener el contacto mas alla del cumplimiento del contrato y "
     "evitar que el equipo desacelere cuando el cliente cree haber terminado. Descartado "
     "fase_accomplish, el nodo generico de la fase, cuyo entregable es solo un indicador o "
     "checkpoint; el bloque pide el sistema de tracking y el protocolo, que es el entregable del "
     "elegido. Su frontera VIGENTE es 1 a 4 / 5 a 9, corrida porque OP-F-04-HOR le corto el "
     "bloque de Horowitz en la vuelta 29, y la lectura se rehizo sobre el nodo de hoy (P.18 "
     "punto 1)."),

    # ---- project_close_out ----
    ("project_close_out", [6, 7, 8, 9, 10, 11],
     "A Project Manager's Book of Forms - Cynthia Stackpole Snyder",
     ("miembro", "reunion_conclusion_proyecto"),
     "métricas de éxito definidas en el kickoff",
     "P.18: el miembro es la reunion de conclusion que ESPEJA el kickoff, y su resumen dice "
     "revisando los objetivos organizacionales y metricas de exito definidas al inicio, que es el "
     "paso 6 palabra por palabra; su entregable pide las encuestas interna y externa y el plan de "
     "monitoreo post entrega, que son los pasos 7, 8 y 11. Descartado gestion_testimonios para el "
     "paso 10: ahi el objeto es REDACTAR el testimonio y conseguir su aprobacion, y aqui "
     "compartir testimonios y reconocimientos mutuos es un momento de la propia reunion de "
     "cierre. Descartado encuesta_satisfaccion_postproyecto, que es la encuesta con sus ramas, "
     "una pieza de la reunion y no la reunion."),

    # ---- relaciones_con_clientes ----
    ("relaciones_con_clientes", [5],
     "Business Model Generation - Osterwalder",
     ("miembro", "construccion_tribu_de_marca"),
     "rituales o símbolos que representen",
     "P.18, un paso con destino propio: identificar los rituales o simbolos que representan los "
     "VALORES CENTRALES de la marca es el ethos y el artefacto simbolico, que es exactamente como "
     "la vuelta 30 delimito el objeto de este miembro cuando lo descarto para otro paso (su "
     "entregable es un statement de ethos de marca y al menos un artefacto simbolico de "
     "pertenencia). Los otros tres pasos del bloque son el onboarding en la comunidad, que es "
     "otro acto."),

    ("relaciones_con_clientes", [6, 7, 8],
     "Business Model Generation - Osterwalder",
     ("miembro", "onboarding_comunitario_y_lenguaje_propio"),
     "momento de iniciación público",
     "P.18: el entregable del miembro es un programa de onboarding con etapas de introduccion, "
     "MENTORIA personalizada, LENGUAJE de marca y calendario de eventos comunitarios, y los tres "
     "pasos son esas tres cosas: el momento de iniciacion publico donde se presenta al nuevo "
     "cliente, el vocabulario o identidad compartida (creed, apodos, insignias) y la conexion "
     "entre clientes nuevos y veteranos. Descartado welcome_call_cliente_veterano para el paso 8: "
     "ese es UNA tactica concreta (la llamada de bienvenida de un cliente veterano) y el paso "
     "pide facilitar la conexion por varias vias, mentoria, foros y eventos."),

    # ---- retention_metrics ----
    ("retention_metrics", [6, 7, 8, 9],
     "The Startup Owner's Manual - Steve Blank",
     ("miembro", "persuasion_directivos_prioridad_cliente"),
     "breakeven point",
     "P.18: el entregable del miembro es un caso CON DATOS NUMERICOS listo para presentar a quien "
     "decide, y su resumen ya usa la estadistica del porcentaje de clientes nuevos que se pierden "
     "temprano. Los cuatro pasos construyen ese caso y lo entregan: el CAC exacto por canal, el "
     "tiempo de recuperacion de esa inversion, el porcentaje real que abandona ANTES de "
     "alcanzarlo, y presentar el impacto financiero de esa perdida temprana al equipo directivo. "
     "El paso 9 nombra al destinatario, que es lo que desempata. Descartado dejarlos en el nodo "
     "donante: los pasos 1 a 5 que se quedan son el dashboard de cohortes de Blank, y estos "
     "cuatro son un argumento economico dirigido a la direccion."),

    # ---- sistema_inmune_producto ----
    ("sistema_inmune_producto", [6, 7, 8, 9],
     "The Lean Startup - Eric Ries",
     ("nodo_propio", AUTOSANACION),
     "autoservicio y autosanación",
     "P.18 PUNTO 3. Ningun miembro tiene por objeto que el PRODUCTO resuelva el problema del "
     "cliente sin intervencion humana: comunicacion_proactiva_puntos_estres avisa en los momentos "
     "de estres emocional del cliente y su entregable es un sistema de notificaciones, "
     "rediseno_procesos_negocio_cliente arregla las fricciones de los PROCESOS internos, y "
     "gratificacion_inmediata_producto quita la friccion del primer uso. Los cuatro pasos piden "
     "herramientas de autoservicio y autosanacion DENTRO del producto y su cifra de problemas "
     "resueltos sin humanos, que es un objeto propio. Forma nodo propio dentro de la familia."),

    # ---- voz_del_cliente_voc ----
    ("voz_del_cliente_voc", [6, 7, 8, 9, 10],
     "Winning at New Products - Robert G. Cooper",
     ("nodo_propio", OBSERVAR),
     "pepitas de oro",
     "P.18 PUNTO 3, y es el caso mas medible de los cinco: la familia tiene TRES de los cuatro "
     "pasos del metodo IOPS de Coleman escritos como nodo propio y le FALTA el segundo. "
     "investigar_datos_cliente declara en su resumen ser el PRIMER paso del metodo IOPS "
     "(investigar, observar, personalizar, sorprender), personalizar_interacciones_cliente "
     "declara ser el TERCERO y sorprender_cliente_estrategico el CUARTO Y ULTIMO. El segundo, "
     "OBSERVAR, no tiene nodo en la nomina de hoy, y este bloque es exactamente ese paso: ver al "
     "cliente usando el producto en su contexto con cadencia fija, recorrerlo tu mismo como si "
     "fueras el, cazar las pepitas de oro de los comentarios casuales, anotar en caliente y "
     "releer a los dos dias para buscar el patron. El bloque forma nodo propio y tapa el hueco "
     "medido."),
]


def main():
    grafo = todos()
    cortes = []
    fallos = []
    creados = set()
    for origen, idx, fuente_queda, (tipo, destino), huella, motivo in CORTES:
        if origen not in grafo:
            fallos.append("%s: no existe en el grafo" % origen)
            continue
        d = grafo[origen]
        pasos = d["pasos_accionables"]
        fuera = [i for i in idx if i < 1 or i > len(pasos)]
        if fuera:
            fallos.append("%s: pasos fuera de rango %s (%d pasos)" % (origen, fuera, len(pasos)))
            continue
        salen = [pasos[i - 1] for i in idx]

        # GUARDA DE HUELLA: tiene que vivir en el bloque que sale, y NO fuera del
        # origen. Si vive fuera, el caso positivo no probaria nada.
        if not any(huella in p for p in salen):
            fallos.append("%s: la huella %r NO esta en el bloque que sale" % (origen, huella))
            continue
        portadores = [nid for nid, dd in grafo.items()
                      if nid != origen
                      and any(huella in p for p in dd.get("pasos_accionables") or [])]
        if portadores:
            fallos.append("%s: la huella %r ya vive fuera del origen, en %s"
                          % (origen, huella, portadores))
            continue

        # GUARDA NUEVA DE ESTA VUELTA, y esta escrita porque el plan parte un
        # bloque en seis subbloques: la huella tiene que ser UNICA dentro del
        # propio origen tambien. Si dos subbloques del mismo nodo comparten
        # huella, la prueba 1 del caso positivo (el origen ya no la lleva) se
        # cumpliria por el corte del vecino y no probaria nada del suyo.
        if sum(1 for p in pasos if huella in p) != len(
                [p for p in salen if huella in p]):
            fallos.append("%s: la huella %r tambien vive en pasos que NO salen en este corte"
                          % (origen, huella))
            continue

        destino_id = destino["node_id"] if tipo == "nodo_propio" else destino
        if tipo == "nodo_propio":
            if destino_id in grafo:
                fallos.append("%s: el nodo propio %s YA EXISTE" % (origen, destino_id))
                continue
            creados.add(destino_id)
            dest = {"tipo": "nodo_propio", "motivo_p18": motivo, "nuevo": destino}
        else:
            if destino_id not in grafo and destino_id not in creados:
                fallos.append("%s: el destino %s no existe ni lo crea este plan"
                              % (origen, destino_id))
                continue
            dest = {"tipo": "miembro", "nodo": destino_id, "motivo_p18": motivo}
            if destino_id in creados:
                dest["creado_por_este_plan"] = True
            else:
                dest["fuente_esperada_destino"] = grafo[destino_id]["fuente"]

        cortes.append({
            "origen": origen,
            "frontera": "los pasos %s de %d" % (idx, len(pasos)),
            "pasos_que_salen": idx,
            "fuente_queda": fuente_queda,
            "destino": dest,
            "pasos_totales": len(pasos),
            "fuente_esperada": d["fuente"],
            "huella": huella,
            "prefijos": [p[:34] for p in salen],
            "pasos_que_salen_texto": salen,
        })
        print("SELLADO: %-38s %-22s -> %s" % (origen, str(idx)[:22], destino_id))

    if fallos:
        print("\nPARADA: %d guarda(s) en rojo. No se sella nada." % len(fallos))
        for f in fallos:
            print("  - %s" % f)
        return 1

    # GUARDA DE COBERTURA POR ORIGEN: la union de los subbloques de un mismo nodo
    # tiene que ser exactamente el bloque que su frontera publicada declara, sin
    # huecos ni repetidos. Es la guarda que el reparto en subbloques obliga.
    porori = {}
    for c in cortes:
        porori.setdefault(c["origen"], []).extend(c["pasos_que_salen"])
    print("\nCOBERTURA POR ORIGEN (la union de los subbloques):")
    for o in sorted(porori):
        v = sorted(porori[o])
        rep = len(v) != len(set(v))
        print("  %-38s salen %2d pasos: %s%s"
              % (o, len(v), v, "   [ROJO: REPETIDOS]" if rep else ""))
        if rep:
            fallos.append("%s: subbloques con pasos repetidos" % o)
    if fallos:
        print("\nPARADA: %d guarda(s) en rojo. No se sella nada." % len(fallos))
        return 1

    plan = {
        "operacion": "OP-F-04-COL, SEGUNDO TIEMPO: los trece destinos por P.18",
        "fecha_corte": "2026-08-14",
        "cuenta": (
            "TRECE destinos, confirmados por la adjudicacion 5 del acta de la vuelta 30 "
            "(linea 6639, leida hoy): quince de la nomina, menos viral_loop_marketing (su "
            "mitad ya la hizo el corte unico de P.20 en la vuelta 30 y la nota de la "
            "operacion lo cita) menos keep_customers_strategy (MULTIFUENTE LEGITIMO sin "
            "corte, adjudicacion 2 del acta 30, con la fuente intacta)."
        ),
        "nomina_de_la_familia": (
            "La familia Coleman medida HOY, antes de decidir un solo destino: 83 nodos "
            "vivos declaran a Coleman y 68 lo declaran como fuente UNICA. Salida completa "
            "en docs/loop/SALIDA_V31_FAMILIA_COLEMAN.txt. Es lo que P.18 punto 1 obliga: "
            "la lectura se hace sobre la nomina vigente al dia de la ejecucion."
        ),
        "subbloques": (
            "blueprint_de_experiencia se parte en SEIS subbloques por objeto, autorizado "
            "por el encargo con su motivo: la frontera es de LIBROS y el destino es de "
            "OBJETOS, y su bloque 5 a 17 trae la postventa proactiva, la friccion "
            "autoinfligida, el ritual del si con su calibracion, el traspaso y los cien "
            "dias. Cada subbloque lleva su lectura y su destino propios."
        ),
        "cortes": cortes,
    }
    with open(SALIDA, "w", encoding="utf-8", newline="") as fh:
        json.dump(plan, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("\nPLAN SELLADO: %s" % SALIDA)
    print("  cortes         : %d" % len(cortes))
    print("  nodos origen   : %d" % len(porori))
    print("  nodos propios  : %d %s" % (len(creados), sorted(creados)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
