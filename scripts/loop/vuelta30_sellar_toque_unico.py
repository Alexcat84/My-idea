"""Vuelta 30: SELLA los planes de los tres bloques de TOQUE UNICO.

Escribe docs/loop/PLAN_V30_P19_COEFICIENTE.json, PLAN_V30_P19_VENDER.json y
PLAN_V30_P20_VIRAL_LOOP.json para que scripts/loop/vuelta30_fundir.py los aplique.

LO QUE ESTE SCRIPT DECIDE Y LO QUE NO. La LECTURA es del ejecutor y esta escrita
a mano aqui: que paso de destino recoge que origenes (el mapa del destejido), el
texto de cada paso fundido, la procedencia por bloque y cual tramo es ajeno al
objeto del nodo. Lo que el script hace por su cuenta es lo mecanico y verificable:
lee los pasos del grafo HOY, saca de ahi los prefijos de la guarda de texto y el
texto verbatim de los pasos que no se funden, y comprueba antes de sellar que el
mapa cubre 1..N sin huecos ni repetidos.

UN PASO CON UN SOLO ORIGEN VIAJA VERBATIM. Solo se escribe texto nuevo donde dos
o mas origenes se funden, que es lo unico que P.19 obliga a redactar.

Uso:
    python scripts/loop/vuelta30_sellar_toque_unico.py
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
LOOP = os.path.join(RAIZ, "docs", "loop")

VERBATIM = None  # marca: el texto de este paso se copia del grafo, no se escribe


def leer(nid):
    with open(os.path.join(NODOS, nid + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
# 1. coeficiente_viral, por P.19. Blank 1 a 5, Weinberg 6 a 11 y 12 a 16, y las
#    dos versiones de Weinberg son la misma cuenta de K, la segunda con la
#    conversion descompuesta en click-through y signup.
# ---------------------------------------------------------------------------
COEFICIENTE = {
    "nodo": "coeficiente_viral",
    "fuente_queda": None,          # None = sin cambio, MULTIFUENTE LEGITIMO
    "pasos": [
        ([1, 6, 12], "Cuenta tus usuarios actuales y mide el número promedio de "
                     "invitaciones o referidos que envía cada uno (i)"),
        ([2, 7, 13, 14], "Mide qué porcentaje de esas invitaciones se convierte en "
                         "usuarios activados, y descompón la conversión en sus dos tramos "
                         "cuando el dato lo permita: de invitación a clic (click-through) "
                         "y de clic a registro o compra (signup)"),
        ([3, 8, 15], "Calcula el coeficiente: K = invitaciones x tasa de conversión, o "
                     "invitaciones x click-through x signup si la descompusiste. Es el "
                     "mismo número, los nuevos usuarios activados que genera cada usuario "
                     "existente"),
        ([9], VERBATIM),
        ([10, 16], "Identifica cuál de las variables es la más débil (invitaciones, "
                   "click-through o signup) y enfoca ahí tus pruebas A/B"),
        ([4], VERBATIM),
        ([11], VERBATIM),
        ([5], VERBATIM),
    ],
    "salidas": [],
    # La huella de cada grupo fundido: un trozo literal que HOY vive en dos o mas
    # de sus origenes. Es lo que hace que el caso positivo CAIGA antes de fundir.
    "pruebas_repeticion": [
        {"origenes": [1, 6, 12], "huella_repetida": "invitaciones enviadas por usuario"},
        {"origenes": [2, 7, 13, 14], "huella_repetida": "porcentaje de conversión"},
        {"origenes": [3, 8, 15], "huella_repetida": "K ="},
        {"origenes": [10, 16], "huella_repetida": "más débil"},
    ],
    "rastros": ["usuarios actuales", "(i)", "click-through", "signup", "coeficiente",
                "A/B", "ciclo viral", "urgencia", "semanalmente", "referido"],
    "procedencia": [
        {"libro": "The Startup Owner's Manual - Steve Blank (pasos 1 a 5 del original)",
         "pasos_del_resultado": [6, 8]},
        {"libro": "Traction - Gabriel Weinberg (pasos 6 a 11 y 12 a 16 del original, "
                  "sus dos versiones de la misma cuenta)",
         "pasos_del_resultado": [4, 5, 7]},
        {"libro": "MULTIFUENTE LEGITIMO: los dos libros dentro del mismo paso fundido "
                  "(Blank aporta el coeficiente y la activacion, Weinberg la i, la K y "
                  "la descomposicion en click-through y signup)",
         "pasos_del_resultado": [1, 2, 3]},
    ],
}

# ---------------------------------------------------------------------------
# 2. decision_de_vender_startup, por P.19. Frontera publicada 1 a 10 (Wasserman)
#    y 11 a 34 (Horowitz, declarado dos veces con dos grafias). Las seis parejas
#    duplicadas estan verificadas contra el grafo en docs/FICHA_SUBFUSION_GRADIENTE.md
#    (lote C2, punto 1), y ademas el equipo vuelve en 11, 13 y 17 y el mercado
#    real en 16, 22 y 24.
# ---------------------------------------------------------------------------
VENDER = {
    "nodo": "decision_de_vender_startup",
    "fuente_queda": None,
    "pasos": [
        ([1], VERBATIM),
        ([2, 6, 7, 12], "Analiza las amenazas de mediano plazo que pueden erosionar el "
                        "valor de tu empresa: cambios en la industria que golpeen tu "
                        "modelo de negocio, competidores que se combinen o se fusionen, y "
                        "cambios tecnológicos disruptivos que te obligarían a reinvertir "
                        "mucho tiempo sin retorno inmediato"),
        ([3, 11, 13, 17], "Diagnostica el estado de tu equipo fundador: cómo están las "
                          "relaciones (agotamiento o burnout, conflictos), cuánta energía "
                          "les queda a ti y a tus cercanos para enfrentar otro ciclo de "
                          "lucha, y pregúntales de frente qué tan dispuestos están "
                          "realmente a seguir el camino difícil o a vender"),
        ([4], VERBATIM),
        ([5], VERBATIM),
        ([16, 22, 23, 24], "Redefine cuál es tu mercado real (no el que crees que es) y "
                           "quiénes serán tus competidores futuros, evalúa con honestidad "
                           "su tamaño y cómo va a evolucionar, si es al menos diez veces "
                           "más grande que el que ya explotaste, y qué probabilidades "
                           "reales tienes de convertirte en el jugador número uno"),
        ([21], VERBATIM),
        ([8, 26], "Corre un proceso corto y discreto de sondeo de fusiones y adquisiciones "
                  "(M&A) con varios compradores potenciales, para detectar cuál es el "
                  "precio máximo que el mercado te puede dar en este momento"),
        ([14, 18], "Define un precio mínimo aceptable basado en el valor real de tu "
                   "negocio, no en la primera oferta que te hagan ni en el extra que te "
                   "ofrezcan sobre el precio actual"),
        ([15, 19, 20], "Comunica ese precio con firmeza a todos los compradores "
                       "potenciales y sostenlo, dispuesto a esperar aunque no lleguen "
                       "ofertas de inmediato"),
        ([9, 25], "Compara las ofertas de adquisición contra tu proyección de valor a 3 o "
                  "5 años si sigues independiente"),
        ([28, 29], "Define criterios objetivos y fáciles de comunicar sobre cuándo "
                   "mantendrías tu empresa independiente y cuándo la venderías, y "
                   "comunícalos a tu equipo de forma consistente para evitar que sientan "
                   "que los traicionaste"),
        ([30, 33], "Separa la decisión estratégica y la discusión sobre vender de tu "
                   "situación financiera personal"),
        ([10, 31, 34], "Toma la decisión con análisis financiero y estratégico: reconoce "
                       "abiertamente la parte emocional que hay en vender y consulta con "
                       "tu consejo (board) y asesores de confianza para equilibrarla con "
                       "el análisis racional"),
        ([27, 32], "Ajusta tu salario como CEO a valores de mercado una vez que tu empresa "
                   "se convierta en un negocio real y consolidado, y en un objetivo "
                   "atractivo de adquisición"),
    ],
    "salidas": [],
    "pruebas_repeticion": [
        {"origenes": [2, 6, 7, 12], "huella_repetida": "tecnológic"},
        {"origenes": [3, 11, 13, 17], "huella_repetida": "equipo cercano"},
        {"origenes": [16, 22, 23, 24], "huella_repetida": "mercado real"},
        {"origenes": [8, 26], "huella_repetida": "fusiones y adquisiciones (M&A)"},
        {"origenes": [14, 18], "huella_repetida": "precio mínimo"},
        {"origenes": [15, 19, 20], "huella_repetida": "Comunica ese precio con firmeza"},
        {"origenes": [9, 25], "huella_repetida": "proyección de valor a 3 o 5 años"},
        {"origenes": [28, 29], "huella_repetida": "criterios"},
        {"origenes": [30, 33], "huella_repetida": "situación financiera personal"},
        {"origenes": [10, 31, 34], "huella_repetida": "emocional"},
        {"origenes": [27, 32], "huella_repetida": "salario como CEO a valores de mercado"},
    ],
    "rastros": ["runway", "burnout", "camino difícil", "punto de inflexión", "diez veces",
                "número uno", "por talento y tecnología", "discreto", "precio máximo",
                "primera oferta", "sobre el precio actual", "esperar", "independiente",
                "traicionaste", "board", "se combinen o se fusionen"],
    "procedencia": [
        {"libro": "The Founder's Dilemmas - Noam Wasserman (pasos 1 a 10 del original)",
         "pasos_del_resultado": [1, 4, 5]},
        {"libro": "The Hard Thing About Hard Things - Ben Horowitz (pasos 11 a 34 del "
                  "original, el libro declarado DOS VECES con dos grafias)",
         "pasos_del_resultado": [6, 7, 9, 10, 12, 13, 15]},
        {"libro": "MULTIFUENTE LEGITIMO: los dos libros dentro del mismo paso fundido",
         "pasos_del_resultado": [2, 3, 8, 11, 14]},
    ],
}

# ---------------------------------------------------------------------------
# 3. viral_loop_marketing, por P.20 (un nodo, un corte) mas P.19 (la repeticion
#    del promotor) mas P.18 (los dos pasos ajenos al objeto).
# ---------------------------------------------------------------------------
VIRAL = {
    "nodo": "viral_loop_marketing",
    "fuente_queda": None,
    "pasos": [
        ([1], VERBATIM), ([2], VERBATIM), ([3], VERBATIM),
        ([4], VERBATIM), ([5], VERBATIM), ([6], VERBATIM), ([7], VERBATIM), ([8], VERBATIM),
        # "y actívalos como embajadores" NO es adorno: el origen 15 lo trae y la
        # primera redaccion lo habia perdido. Lo caso la prueba de conservacion
        # del caso positivo, con el nodo ya escrito, y por eso el corte se
        # revirtio y se rehizo. Queda declarado en el reporte.
        ([9, 15, 18], "Identifica a los clientes que ya actúan como promotores espontáneos "
                      "(menciones, reseñas y referidos orgánicos) y a los más satisfechos "
                      "de tu base, y actívalos como embajadores"),
        ([10], VERBATIM),
        ([14], VERBATIM),
        ([16, 19], "Crea contenido y facilita herramientas para que el cliente recomiende "
                   "sin fricción (links, códigos, material fácil de compartir)"),
        ([11, 17, 20], "Reconoce a quienes refieren activamente, en público o en privado "
                       "según el cliente, con reconocimiento especial cuando corresponda "
                       "(estatus VIP, merchandising, acceso anticipado)"),
        ([21], VERBATIM),
        ([22], VERBATIM), ([23], VERBATIM), ([24], VERBATIM), ([25], VERBATIM),
        ([26], VERBATIM), ([27], VERBATIM), ([28], VERBATIM), ([29], VERBATIM),
        ([30], VERBATIM),
    ],
    "pruebas_repeticion": [
        {"origenes": [9, 15, 18], "huella_repetida": "espontáne"},
        {"origenes": [16, 19], "huella_repetida": "herramientas"},
        # "Reconoc" con mayuscula y no "econoc": en minuscula la huella tambien
        # vive en el paso 22 (valoran mas alla del dinero: estatus, acceso,
        # RECONOCIMIENTO), que no es de este grupo ni entra a la fusion, asi que
        # la prueba era insatisfacible por construccion y no por un defecto del
        # corte. Con mayuscula solo vive en los origenes 17 y 20.
        {"origenes": [11, 17, 20], "huella_repetida": "Reconoc"},
    ],
    # "(viral coefficient)" y no "coeficiente viral": el paso 2 lo escribe en
    # ingles, y la guarda del sellado lo caso antes de sellar nada.
    "rastros": ["(viral coefficient)", "un solo clic", "win-win", "embajadores",
                "links, códigos", "VIP", "en privado", "Adopt", "escaso",
                "inherente, colaborativa, embebida, incentivada, social", "créditos"],
    "salidas": [
        {
            "pasos_que_salen": [12],
            "huella": "eventos exclusivos",
            "destino": {
                "tipo": "miembro",
                "nodo": "experiencias_exclusivas_vip",
                "fuente_esperada_destino": "Never Lose a Customer Again - Joey Coleman",
                "motivo_p18": (
                    "P.18 sobre la nomina de Coleman medida HOY (83 nodos vivos, 68 con "
                    "fuente unica). El paso 12 invita a los promotores a eventos exclusivos "
                    "o experiencias diferenciadas, y ese es LITERALMENTE el objeto de "
                    "experiencias_exclusivas_vip: su resumen dice ofrecer acceso a "
                    "experiencias unicas y dificiles de conseguir (eventos, encuentros, "
                    "contenido privado) a los clientes mas leales, y su entregable es el "
                    "catalogo de experiencias VIP con su mecanismo de canje. NO es el objeto "
                    "de viral_loop_marketing, que es el mecanismo de referidos y su "
                    "coeficiente: invitar a un evento no pide ni mide una referencia."
                ),
            },
        },
        {
            "pasos_que_salen": [13],
            "huella": "voz visible",
            "destino": {
                "tipo": "miembro",
                "nodo": "comunidad_tribu_marca",
                "fuente_esperada_destino": "Never Lose a Customer Again - Joey Coleman",
                "motivo_p18": (
                    "P.18 sobre la misma nomina. El paso 13 escucha el feedback del promotor "
                    "y le da voz visible DENTRO DE LA COMUNIDAD, y el objeto de "
                    "comunidad_tribu_marca es esa comunidad: su entregable es la estrategia "
                    "de comunidad de marca con espacios de conexion y narrativa de identidad, "
                    "su paso 2 crea los espacios donde los clientes leales conectan entre si "
                    "y su paso 5 celebra y amplifica las historias de los mas comprometidos. "
                    "Es el mismo acto. El otro candidato leido, construccion_tribu_de_marca, "
                    "se queda fuera porque su objeto es el ethos y el artefacto simbolico de "
                    "pertenencia (tatuaje, insignia), no la voz del cliente en el espacio."
                ),
            },
        },
    ],
    "procedencia": [
        {"libro": "The Startup Owner's Manual - Blank, Steve (pasos 1 a 3 del original)",
         "pasos_del_resultado": [1, 2, 3]},
        {"libro": "Never Lose a Customer Again - Joey Coleman (pasos 4 a 25 del original, "
                  "menos los dos que salen por P.18)",
         "pasos_del_resultado": [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]},
        {"libro": "Traction - Gabriel Weinberg (pasos 26 a 30 del original)",
         "pasos_del_resultado": [19, 20, 21, 22, 23]},
    ],
}


def sellar(ficha, operacion, regla, motivo, destino):
    d = leer(ficha["nodo"])
    pasos = list(d.get("pasos_accionables") or [])
    n = len(pasos)

    finales = []
    mapa = {}
    for i, (origenes, texto) in enumerate(ficha["pasos"], 1):
        if texto is VERBATIM:
            if len(origenes) != 1:
                raise SystemExit("paso %d: VERBATIM con %d origenes" % (i, len(origenes)))
            texto = pasos[origenes[0] - 1]
        finales.append(texto)
        mapa[str(i)] = origenes

    usados = []
    for v in mapa.values():
        usados.extend(v)
    for s in ficha["salidas"]:
        usados.extend(s["pasos_que_salen"])
    faltan = sorted(set(range(1, n + 1)) - set(usados))
    repes = sorted({i for i in usados if usados.count(i) > 1})
    if faltan or repes or sorted(set(usados)) != list(range(1, n + 1)):
        raise SystemExit("%s: cobertura rota, faltan %s, repetidos %s"
                         % (ficha["nodo"], faltan, repes))

    # GUARDA DEL CASO POSITIVO: una huella que no viva HOY en dos o mas de sus
    # origenes no hace caer nada, y una prueba que no cae no prueba nada. Se
    # comprueba al sellar, no al ejecutar, que es cuando todavia se puede
    # corregir la lectura.
    for g in (ficha.get("pruebas_repeticion") or []):
        h = g["huella_repetida"]
        cuantos = sum(1 for i in g["origenes"] if h in pasos[i - 1])
        if cuantos < 2:
            raise SystemExit("%s: la huella %r vive en %d de sus origenes %s, y hacen "
                             "falta 2 para que el caso positivo caiga"
                             % (ficha["nodo"], h, cuantos, g["origenes"]))
    for r in (ficha.get("rastros") or []):
        if not any(r in p for p in pasos):
            raise SystemExit("%s: el rastro %r no vive en ningun paso de HOY"
                             % (ficha["nodo"], r))

    plan = {
        "operacion": operacion,
        "regla": regla,
        "motivo": motivo,
        "fecha_corte": "2026-08-14",
        "nodos": [{
            "nodo": ficha["nodo"],
            "pasos_totales": n,
            "fuente_esperada": d.get("fuente"),
            "fuente_queda": ficha["fuente_queda"] or d.get("fuente"),
            "prefijos": [p[:38] for p in pasos],
            "pasos_originales": pasos,
            "pasos_finales": finales,
            "mapa_destejido": mapa,
            "procedencia": ficha["procedencia"],
            "pruebas_repeticion": ficha.get("pruebas_repeticion") or [],
            "rastros": ficha.get("rastros") or [],
            "salidas": [dict(s, pasos_que_viajan=[pasos[i - 1] for i in s["pasos_que_salen"]])
                        for s in ficha["salidas"]],
        }],
    }
    ruta = os.path.join(LOOP, destino)
    with open(ruta, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
    print("SELLADO %-34s %s: %d pasos -> %d, %d que salen"
          % (destino, ficha["nodo"], n, len(finales),
             sum(len(s["pasos_que_salen"]) for s in ficha["salidas"])))
    return plan


def main():
    # SELLA SOLO LO QUE SE PIDE. El sellado lee los pasos del grafo de HOY, asi
    # que un plan ya ejecutado no se puede volver a sellar: sus origenes ya no
    # estan. Sin este filtro, rehacer UN plan obligaba a rehacerlos los tres.
    cuales = set(sys.argv[1:]) or {"coeficiente", "vender", "viral"}

    if "coeficiente" in cuales:
        sellar(
        COEFICIENTE,
        "OP-F-04-WEI, el bloque de TOQUE UNICO de coeficiente_viral",
        "P.19 LA REPETICION INTERNA SE FUNDE, NO SE DESTEJE",
        "Los pasos 6 a 11 y 12 a 16 son la MISMA cuenta de K de Traction dicha dos veces, "
        "y los pasos 1 a 3 de Blank calculan el mismo coeficiente. No hay destino que "
        "buscar: el objeto ya estaba en el nodo. Se funde en un solo procedimiento y el "
        "nodo queda MULTIFUENTE LEGITIMO, con la procedencia declarada por bloque. Las "
        "diferencias entre versiones se reparten por la tabla de los seis motivos de "
        "perdida de linea: NOMBRE (la K de Weinberg y el coeficiente de Blank conviven en "
        "el paso 3), METODO ALTERNATIVO (la conversion agregada o descompuesta en "
        "click-through y signup entra como variante condicional dentro del paso 2) y "
        "ALCANCE (la enumeracion del eslabon debil pasa de dos variables a tres en el "
        "paso 5). Los otros tres motivos no aplican y por eso no se nombran.",
        "PLAN_V30_P19_COEFICIENTE.json")

    if "vender" in cuales:
        sellar(
        VENDER,
        "OP-F-04-HOR, el bloque de TOQUE UNICO de decision_de_vender_startup",
        "P.19 LA REPETICION INTERNA SE FUNDE, NO SE DESTEJE",
        "El peor nodo medido del catalogo: seis parejas duplicadas verificadas contra el "
        "grafo en docs/FICHA_SUBFUSION_GRADIENTE.md (lote C2, punto 1), mas el equipo en "
        "11, 13 y 17 y el mercado real en 16, 22 y 24. La repeticion cruza la frontera "
        "publicada (1 a 10 Wasserman, 11 a 34 Horowitz): las parejas 8 con 26 y 9 con 25 "
        "tienen un origen a cada lado, que es exactamente el caso que P.19 nombra al decir "
        "material de DOS O MAS FUENTES dentro de un nodo. Se funde entero y el nodo queda "
        "MULTIFUENTE LEGITIMO. Perdidas por la tabla de los seis motivos: ALCANCE (las "
        "amenazas de 2, 6, 7 y 12 entran a una sola enumeracion en el paso 2; lo mismo el "
        "mercado real en el paso 6) y DESTINO (el paso 12 del resultado se queda con a "
        "quien hay que comunicar los criterios, que solo traia el origen 29). El paso 15 "
        "del resultado NO es del objeto del nodo y entra a LA COLA DEL OBJETO AJENO, la "
        "segunda puerta de la cola de relectura post fusion: no se poda, se declara.",
        "PLAN_V30_P19_VENDER.json")

    if "viral" in cuales:
        sellar(
        VIRAL,
        "OP-F-04-COL y OP-F-04-WEI, el corte UNICO de viral_loop_marketing",
        "P.20 UN NODO, UN CORTE (mas P.19 en la repeticion y P.18 en lo ajeno)",
        "El nodo pertenece a DOS operaciones de destejido, asi que su frontera completa de "
        "TRES libros se publico primero como registro unico en docs/plan/01_FUENTES.md y el "
        "corte se ejecuta UNA sola vez, citado por las dos con correccion declarada. Dentro "
        "del mismo corte: el material del promotor que repite entre los tramos 9 a 13, 14 a "
        "17 y 18 a 21 se funde por P.19 (once origenes en seis pasos), y los dos pasos "
        "ajenos al objeto del nodo se destejen con destino por P.18. Perdidas por la tabla "
        "de los seis motivos: ALCANCE (el paso 9 del resultado junta las senales del "
        "promotor espontaneo y los clientes mas satisfechos, que eran dos enumeraciones) y "
        "METODO ALTERNATIVO (el reconocimiento del paso 13 queda como variante condicional, "
        "en publico o en privado segun el cliente, que es la diferencia entre los origenes "
        "17 y 20).",
        "PLAN_V30_P20_VIRAL_LOOP.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
