"""Vuelta 32: CONSTRUYE el plan de P.19 para el 14vo de Horowitz.

POR QUE UN CONSTRUCTOR Y NO UN JSON ESCRITO A MANO: la correccion 3 de la vuelta
31 fue exactamente eso, DIEZ HUELLAS ESCRITAS SIN ACENTOS contra un texto de
pasos que si los lleva. Los prefijos y los textos originales de este plan NO se
teclean: se leen del grafo. Y las huellas, los rastros y los pares de
convergencia, que si son mios porque son la lectura, pasan por una GUARDA QUE
ESTA ESCRITA PARA CAER: si una sola no aparece literalmente donde el plan dice
que aparece, este script NO escribe el plan.

LA LECTURA QUE SOSTIENE EL PLAN esta en la salida de
scripts/loop/vuelta32_lectura_hor14.py y en el reporte de la vuelta. En una
linea: el bloque 6 a 10 de Horowitz repite EL MISMO OBJETO que los pasos 1 a 5
de Ries (que nivel de acabado hace falta antes de lanzar, y como se aprende del
mercado real), asi que no tiene destino que buscar y va por P.19, no por P.18.

Uso: python scripts/loop/vuelta32_plan_hor14.py
Escribe docs/loop/PLAN_V32_P19_CALIDAD_MVP.json
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop", "PLAN_V32_P19_CALIDAD_MVP.json")

NODO = "principio_calidad_mvp"

# EL RESULTADO, paso a paso, y de que origenes sale cada uno.
# Los tres primeros son los fundidos; los cuatro ultimos son pasos que una sola
# version trae y que se quedan VERBATIM, sin reescribir, porque no hay con que
# fundirlos y P.19 no autoriza a retocar lo que no repite.
FUNDIDOS = [
    ([1, 6],
     "Antes de invertir en pulir una característica, pregúntate si "
     "contribuye directamente al aprendizaje que buscas, y usa esa pregunta para "
     "resistir la presión del equipo de completar todas las funcionalidades "
     "'ideales' antes de lanzar."),
    ([3, 7],
     "No asumas que el estándar de calidad de la industria, ni los "
     "requerimientos heredados de un cliente anterior, son lo que el mercado "
     "amplio valora; pruébalo empíricamente contra las necesidades reales "
     "de tus clientes."),
    ([2, 8],
     "Lanza al mercado real, lo antes posible, versiones simplificadas o 'hacky' "
     "de las features complejas, aceptando que fallarán en algunos aspectos, y "
     "mide la reacción real de los clientes."),
]
VERBATIM = [[4], [9], [5], [10]]

# LAS HUELLAS DE REPETICION, la prueba que CAE antes de fundir: cada una vive HOY
# en DOS pasos (uno de cada libro) y despues de fundir tiene que vivir en UNO.
# SOLO HAY UNA, Y SE DICE SIN ADORNARLO: esta repeticion es DE OBJETO, no DE
# LETRA. Los dos libros dicen lo mismo con palabras distintas, asi que 'Lanza'
# es el unico trozo literal que los dos bloques comparten. Por eso este plan trae
# ademas las PRUEBAS DE CONVERGENCIA de abajo, que miden la fusion sin depender
# de que las dos versiones compartan vocabulario.
HUELLAS = [
    {"origenes": [2, 8], "huella_repetida": "Lanza"},
]

# LAS PRUEBAS DE CONVERGENCIA, una por grupo fundido. Cada una es un PAR de
# trozos literales, uno de cada origen del grupo. HOY viven en pasos DISTINTOS,
# asi que CERO pasos contienen los dos; despues de fundir tiene que haber
# EXACTAMENTE UN paso que contenga los dos. Es la misma idea que la huella
# repetida (una prueba que cae antes y pasa despues), pero sirve cuando la
# repeticion es de objeto y no de letra.
CONVERGENCIAS = [
    {"origenes": [1, 6],
     "trozo_a": "aprendizaje que buscas",
     "trozo_b": "funcionalidades"},
    {"origenes": [3, 7],
     "trozo_a": "estándar de calidad de la industria",
     "trozo_b": "requerimientos heredados"},
    {"origenes": [2, 8],
     "trozo_a": "versiones simplificadas",
     "trozo_b": "mercado real"},
]

# LOS RASTROS, la conservacion: cada uno vive hoy y tiene que seguir vivo
# despues. Pasan las dos veces a proposito y por eso se cuentan aparte.
RASTROS = [
    "aprendizaje que buscas",
    "funcionalidades",
    "estándar de calidad de la industria",
    "requerimientos heredados",
    "versiones simplificadas",
    "mercado real",
    "baja fidelidad estética",
    "primeros clientes reales",
    "alta calidad tradicional",
    "suposiciones internas",
]

MOTIVO = (
    "P.19. EL BLOQUE 6 A 10 DE HOROWITZ REPITE EL OBJETO QUE LOS PASOS 1 A 5 DE "
    "RIES YA TRAEN, asi que no hay destino que buscar: el objeto ya esta en casa. "
    "LA LECTURA, par por par, hecha con el texto delante y no de antemano: el 6 "
    "(resistir la presion del equipo de completar todas las funcionalidades "
    "ideales antes de lanzar) es el 1 (antes de invertir en pulir, preguntate si "
    "contribuye al aprendizaje) con el sesgo nombrado; el 7 (distinguir "
    "requerimientos heredados de un cliente anterior de las necesidades reales del "
    "mercado amplio) es el 3 (no asumas que el estandar de la industria es lo que "
    "el cliente valora) con otra fuente del estandar falso; y el 8 (lanzar al "
    "mercado real lo antes posible aceptando que fallara) es el 2 (lanza versiones "
    "simplificadas y mide la reaccion real) dicho a escala de producto. LOS OTROS "
    "TRES PASOS DEL BLOQUE (9 y 10 de Horowitz, y el 4 y el 5 de Ries) NO REPITEN "
    "A NADIE Y SE QUEDAN VERBATIM: capturar y priorizar el aprendizaje de los "
    "primeros clientes reales, e iterar con el feedback de mercado y no con "
    "suposiciones internas, son pasos propios del mismo procedimiento, no copias. "
    "POR QUE NO P.18: la nomina vigente al dia de la familia Horowitz se leyo "
    "entera hoy (93 miembros vivos, salida en docs/loop/SALIDA_V32_HOR14_LECTURA.txt) "
    "y NINGUN miembro tiene este objeto; los candidatos mas cercanos, descartados "
    "por su nombre, son framework_good_bad_product_manager (su objeto es el ROL del "
    "product manager y su entregable un documento de expectativas del puesto), "
    "lead_bullets_no_silver_bullets y estrategia_de_balas_de_plomo (su objeto es "
    "cerrar una desventaja competitiva sin atajos, y su consejo es el contrario: "
    "trabajo sostenido de producto, no lanzar antes), "
    "respuesta_estrategica_a_amenaza_competitiva (su objeto es el pivote ante un "
    "competidor dominante, con cronograma y adquisiciones), "
    "descubrir_valor_inesperado_cliente (el dolor no contractual de UN cliente "
    "critico) y toma_decisiones_bajo_incertidumbre (decidir con informacion "
    "incompleta, que es el genero y no este objeto). Y P.18 punto 3 mandaria nodo "
    "propio, que aqui fabricaria el gemelo exacto del propio donante: es "
    "literalmente el caso que el motivo de P.19 nombra para existir. "
    "LAS DIFERENCIAS ENTRE VERSIONES, por la tabla de los SEIS MOTIVOS DE PERDIDA "
    "DE LINEA: SALVAGUARDA en el paso 1 del resultado (Ries manda decidir si el "
    "pulido sirve al aprendizaje y no dice contra que sesgo; Horowitz nombra el "
    "sesgo, la presion del equipo por las funcionalidades ideales, y el inciso se "
    "adosa al paso que protege); ALCANCE en el paso 2 (Ries trae UN ejemplo de "
    "estandar falso, el de la industria, y el de Horowitz entra a la enumeracion "
    "como segundo ejemplo, los requerimientos heredados de un cliente anterior); y "
    "ALCANCE otra vez en el paso 3 (la version de Ries lanza FEATURES y la de "
    "Horowitz lanza EL PRODUCTO al mercado real, mas la salvaguarda de aceptar que "
    "fallara). NOMBRE, DESTINO, METODO ALTERNATIVO y DIRECCION no aplican y por eso "
    "no se nombran. EL NODO QUEDA MULTIFUENTE LEGITIMO, como manda P.19 punto 2, "
    "con la procedencia declarada por bloque, igual que decision_de_vender_startup "
    "en la vuelta 30."
)


def main():
    with open(os.path.join(NODOS, NODO + ".json"), encoding="utf-8") as fh:
        d = json.load(fh)
    pasos = list(d.get("pasos_accionables") or [])
    if len(pasos) != 10:
        print("PARADA: el nodo tiene %d pasos y este plan se escribio para 10" % len(pasos))
        return 1

    grupos = FUNDIDOS + [(v, pasos[v[0] - 1]) for v in VERBATIM]
    finales = [t for _o, t in grupos]
    mapa = {str(i + 1): o for i, (o, _t) in enumerate(grupos)}

    # GUARDA ESCRITA PARA CAER 1: cobertura exacta de 1..10.
    todos = [i for o, _t in grupos for i in o]
    if sorted(todos) != list(range(1, 11)):
        print("PARADA: la cobertura no es 1..10, es %s" % sorted(todos))
        return 1

    # GUARDA ESCRITA PARA CAER 2: cada huella de repeticion vive HOY en los dos
    # pasos de origen que el plan declara, y en el texto fundido vive UNA vez.
    fallos = []
    for h in HUELLAS:
        t = h["huella_repetida"]
        for i in h["origenes"]:
            if t not in pasos[i - 1]:
                fallos.append("huella %r no esta en el paso original %d" % (t, i))
        destino = [k for k, (o, _x) in enumerate(grupos, 1) if o == h["origenes"]]
        if not destino:
            fallos.append("huella %r: su grupo %s no es un grupo del plan"
                          % (t, h["origenes"]))
        elif t not in finales[destino[0] - 1]:
            fallos.append("huella %r no esta en el paso fundido %d" % (t, destino[0]))

    # GUARDA ESCRITA PARA CAER 3: cada par de convergencia vive HOY en pasos
    # DISTINTOS (cero pasos con los dos) y en el resultado en UNO solo.
    for c in CONVERGENCIAS:
        a, b = c["trozo_a"], c["trozo_b"]
        i, j = c["origenes"]
        if a not in pasos[i - 1]:
            fallos.append("convergencia: %r no esta en el paso original %d" % (a, i))
        if b not in pasos[j - 1]:
            fallos.append("convergencia: %r no esta en el paso original %d" % (b, j))
        juntos_antes = sum(1 for p in pasos if a in p and b in p)
        if juntos_antes:
            fallos.append("convergencia %r + %r: ya viven juntos en %d paso(s) HOY, "
                          "la prueba no probaria nada" % (a, b, juntos_antes))
        juntos_despues = sum(1 for p in finales if a in p and b in p)
        if juntos_despues != 1:
            fallos.append("convergencia %r + %r: viven juntos en %d paso(s) del "
                          "resultado, se esperaba 1" % (a, b, juntos_despues))

    # GUARDA ESCRITA PARA CAER 4: cada rastro vive hoy y sigue vivo despues.
    for r in RASTROS:
        if not any(r in p for p in pasos):
            fallos.append("rastro %r no vive en el nodo de HOY" % r)
        if not any(r in p for p in finales):
            fallos.append("rastro %r no sobrevive en el resultado" % r)

    if fallos:
        print("PARADA: %d guarda(s) en rojo. NO se escribe el plan." % len(fallos))
        for x in fallos:
            print("  - %s" % x)
        return 1

    plan = {
        "operacion": "OP-F-04-HOR, el 14vo nodo: el bloque de Horowitz de principio_calidad_mvp",
        "regla": "P.19 LA REPETICION INTERNA SE FUNDE, NO SE DESTEJE",
        "motivo": MOTIVO,
        "fecha_corte": "2026-08-15",
        "nodos": [{
            "nodo": NODO,
            "pasos_totales": len(pasos),
            "fuente_esperada": d.get("fuente"),
            "fuente_queda": d.get("fuente"),
            "prefijos": [p[:34] for p in pasos],
            "pasos_originales": pasos,
            "pasos_finales": finales,
            "mapa_destejido": mapa,
            "procedencia": [
                {"libro": "The Lean Startup - Eric Ries (pasos 1 a 5 del original)",
                 "pasos_del_resultado": [4, 6]},
                {"libro": "The Hard Thing About Hard Things - Ben Horowitz "
                          "(pasos 6 a 10 del original, el bloque del 14vo)",
                 "pasos_del_resultado": [5, 7]},
                {"libro": "MULTIFUENTE LEGITIMO: los dos libros dentro del mismo paso "
                          "fundido (Ries pone el criterio del aprendizaje y Horowitz "
                          "el sesgo que lo estorba, la segunda fuente del estandar "
                          "falso y la escala de producto del lanzamiento)",
                 "pasos_del_resultado": [1, 2, 3]},
            ],
            "pruebas_repeticion": HUELLAS,
            "pruebas_convergencia": CONVERGENCIAS,
            "rastros": RASTROS,
            "salidas": [],
        }],
    }

    with open(SALIDA, "w", encoding="utf-8") as fh:
        json.dump(plan, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("ESCRITO: %s" % SALIDA)
    print("pasos %d -> %d, cobertura 1..10 exacta, %d huella(s) de repeticion, "
          "%d prueba(s) de convergencia, %d rastro(s)"
          % (len(pasos), len(finales), len(HUELLAS), len(CONVERGENCIAS), len(RASTROS)))
    for i, (o, t) in enumerate(grupos, 1):
        print("  %2d <- %-10s %s" % (i, o, t[:86]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
