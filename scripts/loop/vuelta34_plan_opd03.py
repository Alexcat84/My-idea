# -*- coding: utf-8 -*-
"""vuelta34_plan_opd03.py - CONSTRUYE el plan sellado del destejido de OP-D-03.

NO ESCRIBE NI UN NODO. Escribe un plan JSON que despues ejecuta el instrumento
sellado de la casa, `scripts/loop/vuelta32_podar.py`.

LOS TEXTOS SE LEEN DEL GRAFO, NO SE TECLEAN (EJECUTOR.md regla 1, cuarto
renglon): los pasos originales, los prefijos y la fuente salen de
`dataset/nodos/`, y lo unico escrito a mano aqui son los pasos FINALES y los
motivos, que es lo que la lectura aporta y ningun instrumento puede sacar solo.

QUE DESTEJE Y POR QUE ESE Y NO OTRO. `OP-D-03` declara TRES costuras
(`02_DESTEJIDOS.md`: *Costuras: ab_testing_optimizacion,
optimizacion_embudo_get_customers, split_testing_experimentos_ab*). Medidas hoy,
DOS ya estan consumidas por operaciones de la fase 01 y la tercera es esta. El
censo de las tres, con su medicion, lo imprime
`scripts/loop/vuelta34_costuras_opd03.py`.

LA COSTURA, y su frontera NO la invento yo: esta escrita en `01_FUENTES.md`
linea 947, en la propia tabla de fronteras de `OP-F-04-WEI`:

    "Nota de costura: los pasos 1 a 5 y 6 a 10 dicen la misma prueba A/B dos
     veces, y eso es material de la fase 02, no de esta"

EL CRITERIO DEL SUPERVIVIENTE ES EL MISMO QUE EL DE `OP-D-01`, citado y no
inventado: de cada grupo de repeticion sobrevive EL DE INDICE MAS BAJO. Aqui cae
entero sobre el bloque 1 a 5, que es ademas la narracion del libro que el nodo
declara como fuente UNICA.

Uso: python scripts/loop/vuelta34_plan_opd03.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop", "PLAN_V34_OPD03_AB.json")

NODO = "ab_testing_optimizacion"

# El mapa destino <- origenes. Es lo que la lectura decide, y va aqui arriba
# para que se pueda discutir de una sola mirada.
MAPA = {1: [1, 6, 9], 2: [2, 7], 3: [3, 8], 4: [4], 5: [5, 10]}

FINALES = [
    "Identificar los elementos clave de la landing page que impulsan la "
    "activación (botones, titulares, imágenes, ofertas), eligiendo antes la "
    "métrica clave a mejorar (ej. tasa de registro) y contando también la "
    "ubicación de CTA, el copy, la prueba social y el número de campos de "
    "formulario.",
    "Diseñar dos versiones (A y B) cambiando un solo elemento a la vez, "
    "generando las hipótesis de cambios grandes antes que las de pequeños "
    "ajustes.",
    "Dividir el tráfico de manera aleatoria y equitativa entre ambas versiones "
    "(o 80/20 en páginas de alto tráfico), y dejar correr la prueba durante "
    "semanas enfocándose en una sola métrica a la vez.",
    "Medir resultados de conversión/activación para cada versión",
    "Implementar la versión ganadora y repetir el proceso con nuevos elementos, "
    "documentando los resultados y pasando a la siguiente métrica cuando se "
    "agoten las ideas.",
]

MOTIVOS = {
    1: ("ALCANCE: el superviviente SI nombra los elementos que impulsan la metrica "
        "(botones, titulares, imagenes, ofertas) pero trae UN solo juego de ejemplos y "
        "la metrica ya fijada de antemano. El paso 6 trae la metrica como ELECCION (ej. "
        "tasa de registro) y el paso 9 trae cuatro elementos mas (ubicacion de CTA, "
        "copy, prueba social, numero de campos de formulario). Los dos entran a la "
        "enumeracion que el superviviente ya tiene, que es el remedio escrito del "
        "motivo."),
    2: ("SALVAGUARDA: el superviviente manda disenar dos versiones cambiando un solo "
        "elemento a la vez y NO dice contra que sesgo se elige QUE cambiar; sin eso el "
        "paso se resuelve por el sesgo por defecto, probar el ajuste mas pequeno y mas "
        "facil. El paso 7 dice contra que (hipotesis de cambios grandes antes que "
        "pequenos ajustes) y el inciso se adosa al paso que protege, que es un paso de "
        "DECISION y no de ejecucion, que es la firma escrita de la clase."),
    3: ("ALCANCE: el superviviente dice como se reparte el trafico y no dice CUANTO dura "
        "la prueba ni sobre cuantas metricas a la vez se lee. El paso 8 lo trae (durante "
        "semanas, una sola metrica a la vez) y entra al paso. Es la misma lectura de "
        "cadencia que OP-D-01 aplico en el sexto paso de su tabla, y se cita para que el "
        "criterio sea el mismo."),
    4: "VERBATIM: el superviviente conserva su paso entero y el bloque repetido no le anade nada.",
    5: ("DESTINO: el superviviente produce el resultado (implementar la ganadora y repetir) "
        "y NO dice que hacer con el. El paso 10 lo dice, y son las dos cosas que el "
        "entregable del nodo ya prometia sin que ningun paso las mandara: DOCUMENTAR los "
        "resultados, y el criterio de cuando se pasa a la siguiente metrica (cuando se "
        "agoten las ideas). La linea de destino entra en el paso FINAL, que es el remedio "
        "escrito del motivo."),
}

COSAS = {
    1: "elegir que se prueba y contra que metrica",
    2: "disenar la variacion",
    3: "repartir el trafico y dejar correr la prueba",
    4: "medir el resultado de cada version",
    5: "cerrar el ciclo y volver a empezar",
}

# HUELLAS REPETIDAS: trozos literales que HOY viven en dos pasos y despues del
# destejido tienen que vivir en UNO como maximo.
REPETICION = [
    {"origenes": [1, 9], "huella_repetida": "botones"},
]

# CONVERGENCIA: un par de trozos, uno de cada origen del grupo. ANTES viven en
# pasos DISTINTOS (cero pasos con los dos) y DESPUES tienen que vivir en
# EXACTAMENTE UN paso. Es la prueba que no depende de que los dos bloques usen el
# mismo vocabulario, y aqui hace falta: son parafrasis, no copias.
CONVERGENCIA = [
    {"origenes": [1, 6], "trozo_a": "impulsan la activación", "trozo_b": "tasa de registro"},
    {"origenes": [1, 9], "trozo_a": "titulares", "trozo_b": "prueba social"},
    {"origenes": [2, 7], "trozo_a": "un solo elemento a la vez", "trozo_b": "cambios grandes"},
    {"origenes": [3, 8], "trozo_a": "80/20", "trozo_b": "durante semanas"},
    {"origenes": [5, 10], "trozo_a": "versión ganadora", "trozo_b": "se agoten las ideas"},
]

RASTROS = [
    "impulsan la activación", "botones, titulares, imágenes, ofertas",
    "tasa de registro", "ubicación de CTA", "prueba social",
    "número de campos de formulario", "un solo elemento a la vez",
    "cambios grandes", "pequeños ajustes", "aleatoria y equitativa", "80/20",
    "durante semanas", "una sola métrica a la vez", "conversión/activación",
    "versión ganadora", "nuevos elementos", "se agoten las ideas",
]


def main():
    d = json.load(io.open(os.path.join(NODOS, NODO + ".json"), encoding="utf-8"))
    pasos = list(d.get("pasos_accionables") or [])
    cond = list(d.get("condiciones_activacion") or [])

    print("CONSTRUCTOR DEL PLAN DE OP-D-03")
    print("=" * 78)
    print("  nodo   : %s" % NODO)
    print("  fuente : %r" % d.get("fuente"))
    print("  pasos  : %d" % len(pasos))
    print("  condiciones: %d  (NO se tocan: no hay repeticion medida entre ellas)" % len(cond))

    # GUARDA 1: el mapa cubre 1..N exactamente una vez.
    todos = [i for v in MAPA.values() for i in v]
    if sorted(todos) != list(range(1, len(pasos) + 1)):
        print("ABORTA (guarda 1): el mapa no cubre 1..%d exacto: %s" % (len(pasos), sorted(todos)))
        return 1
    print("  guarda 1 OK: el mapa cubre los %d origenes, sin huecos ni repetidos" % len(pasos))

    # GUARDA 2: un motivo y una cosa por destino.
    if sorted(MAPA) != sorted(MOTIVOS) or sorted(MAPA) != sorted(COSAS):
        print("ABORTA (guarda 2): falta motivo o cosa para algun destino")
        return 1
    print("  guarda 2 OK: los %d destinos llevan motivo y cosa" % len(MAPA))

    # GUARDA 3: cada trozo de convergencia vive HOY en el paso que dice, y los
    # dos NO viven juntos en ninguno. Si ya vivieran juntos, la prueba no
    # probaria nada.
    for c in CONVERGENCIA:
        oa, ob = c["origenes"]
        if c["trozo_a"] not in pasos[oa - 1]:
            print("ABORTA (guarda 3): %r no esta en el paso %d" % (c["trozo_a"], oa))
            return 1
        if c["trozo_b"] not in pasos[ob - 1]:
            print("ABORTA (guarda 3): %r no esta en el paso %d" % (c["trozo_b"], ob))
            return 1
        juntos = sum(1 for p in pasos if c["trozo_a"] in p and c["trozo_b"] in p)
        if juntos:
            print("ABORTA (guarda 3): %r y %r YA viven juntos en %d paso(s)"
                  % (c["trozo_a"], c["trozo_b"], juntos))
            return 1
    print("  guarda 3 OK: las %d convergencias caen HOY y ninguna esta ya cumplida"
          % len(CONVERGENCIA))

    # GUARDA 4: cada huella de repeticion vive HOY en dos pasos o mas.
    for r in REPETICION:
        c = sum(1 for p in pasos if r["huella_repetida"] in p)
        if c < 2:
            print("ABORTA (guarda 4): la huella %r vive en %d paso(s), hacen falta 2 o mas"
                  % (r["huella_repetida"], c))
            return 1
    print("  guarda 4 OK: las %d huellas de repeticion viven hoy en dos pasos o mas"
          % len(REPETICION))

    # GUARDA 5: todo rastro declarado sobrevive LITERAL en los pasos finales.
    muertos = [r for r in RASTROS if not any(r in p for p in FINALES)]
    if muertos:
        print("ABORTA (guarda 5): %d rastro(s) no sobreviven literales: %s"
              % (len(muertos), muertos))
        return 1
    print("  guarda 5 OK: los %d rastros sobreviven LITERALES en los pasos finales"
          % len(RASTROS))

    # GUARDA 6: cada final empieza por el texto del superviviente de su grupo,
    # salvo que el remedio lo abra por delante. Aqui se exige el prefijo entero
    # del superviviente hasta su primera coma, que es lo que hace auditable que
    # el texto viejo NO se reescribio.
    for destino, origenes in sorted(MAPA.items()):
        sup = pasos[origenes[0] - 1]
        cabeza = sup.split(",")[0]
        if not FINALES[destino - 1].startswith(cabeza):
            print("ABORTA (guarda 6): el final %d no empieza por la cabeza de su "
                  "superviviente\n    cabeza: %r\n    final : %r"
                  % (destino, cabeza, FINALES[destino - 1][:90]))
            return 1
    print("  guarda 6 OK: los %d finales conservan la cabeza de su superviviente" % len(MAPA))

    # GUARDA 7: el resultado, dentro del estandar de 3 a 6 pasos.
    if not (3 <= len(FINALES) <= 6):
        print("ABORTA (guarda 7): el resultado tiene %d pasos, fuera del estandar" % len(FINALES))
        return 1
    print("  guarda 7 OK: el resultado tiene %d pasos, dentro del estandar de 3 a 6" % len(FINALES))

    plan = {
        "operacion": ("OP-D-03: el destejido que queda del acto de las pruebas A/B. "
                      "ab_testing_optimizacion dice la misma prueba A/B dos veces"),
        "regla": ("OP-D-03 (docs/plan/02_DESTEJIDOS.md), con la frontera escrita en "
                  "docs/plan/01_FUENTES.md linea 947 y la perdida repartida por LA TABLA "
                  "DE LOS SEIS MOTIVOS DE PERDIDA DE LINEA. Superviviente por el criterio "
                  "de OP-D-01: de cada grupo sobrevive el de INDICE MAS BAJO."),
        "motivo": ("De las TRES costuras que OP-D-03 declara, dos estan CONSUMIDAS por la "
                   "fase 01 y medidas hoy (optimizacion_embudo_get_customers perdio su "
                   "bloque 6 a 10 con OP-F-04-WEI, split_testing_experimentos_ab perdio su "
                   "bloque 6 a 9 con OP-F-04-RAC). Queda esta, que ninguna operacion de la "
                   "fase 01 podia tocar porque no es material ajeno con destino: es el "
                   "mismo nodo diciendo su procedimiento dos veces, y su propia tabla de "
                   "fronteras lo mando a la fase 02."),
        "fecha_corte": "2026-08-15",
        "nodos": [{
            "nodo": NODO,
            "fuente_esperada": d.get("fuente"),
            "pasos_totales": len(pasos),
            "prefijos_pasos": [p[:34] for p in pasos],
            "pasos_originales": pasos,
            "pasos_finales": FINALES,
            "mapa_pasos": {str(k): v for k, v in sorted(MAPA.items())},
            "grupos_pasos": [
                {"origenes": MAPA[k], "cosa": COSAS[k], "texto": FINALES[k - 1],
                 "motivo": MOTIVOS[k]}
                for k in sorted(MAPA)
            ],
            "procedencia": [{
                "libro": ("The Startup Owner's Manual - Steve Blank (fuente UNICA declarada "
                          "por el nodo hoy; la atribucion a Traction salio con el bloque 11 a "
                          "15 en OP-F-04-WEI, y eso va DECLARADO como discutible en el "
                          "reporte de la vuelta 34, no escondido aqui)"),
                "pasos_del_resultado": list(range(1, len(FINALES) + 1)),
            }],
            "pruebas_repeticion": REPETICION,
            "pruebas_convergencia": CONVERGENCIA,
            "rastros": RASTROS,
            "salidas": [],
        }],
    }

    with io.open(SALIDA, "w", encoding="utf-8") as fh:
        json.dump(plan, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("\nESCRITO: %s" % os.path.relpath(SALIDA, RAIZ))
    print("\nEL MAPA, destino <- origenes:")
    for k in sorted(MAPA):
        print("  %d <- %-12s %s" % (k, MAPA[k], FINALES[k - 1][:88]))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
