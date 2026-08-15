"""Vuelta 32, OP-D-01 paso 1: CONSTRUYE el plan del destejido de producto_minimo_viable.

Como el plan del 14vo, este NO se teclea: los prefijos y los textos originales se
leen del grafo y las guardas escritas para caer cotejan todo lo que si es mio.

LA LECTURA QUE LO SOSTIENE, y toda ella esta escrita antes de esta vuelta:

* docs/FICHA_SUBFUSION_GRADIENTE.md, seccion a: los CINCO bloques (1 a 5, 6 a 9,
  10 a 14, 15 a 18, 19 a 22), las instrucciones repetidas con sus posiciones, y
  la medicion del 10 ago 2026 que anade la cuarta repeticion (el paso 4, que dice
  early adopters donde los otros dicen earlyvangelists) y las DIEZ CONDICIONES
  para cinco cosas, con sus grupos.
* docs/plan/02_DESTEJIDOS.md, OP-D-01: 'su material sobrante ya esta localizado
  paso por paso, asi que el destejido deja de ser un juicio y pasa a ser una
  lista de borrados'.
* docs/INTRA_DOMINIO_INFORME.md, 494: la tabla de la perdida deja la celda del
  emblema VACIA en la columna de lo que se va, y en la de lo que hay que salvar
  escribe 'lo que quede tras colapsar sus cinco narraciones, que hoy no se puede
  nombrar'.

EL CRITERIO DEL SUPERVIVIENTE, escrito antes de aplicarlo para que se pueda
auditar: de cada grupo de repeticion sobrevive EL DE INDICE MAS BAJO, verbatim.
No es una preferencia estetica: es el unico criterio que no exige elegir entre
frases que la ficha ya declaro equivalentes, y deja el orden propio del nodo en
pie. El resultado cae exactamente sobre la NARRACION 1 (pasos 1 a 5) mas el
primer paso de la sexta cosa (el 8), y la narracion 1 es la que el propio
entregable del nodo ya narra.

LAS PERDIDAS VAN REPARTIDAS POR LA TABLA DE LOS SEIS MOTIVOS (AUDITOR.md seccion
3 lo exige por operacion), y por eso cuatro de los seis supervivientes llevan
adosada la linea que su grupo traia y ellos no.

Uso: python scripts/loop/vuelta32_plan_opd01.py
Escribe docs/loop/PLAN_V32_OPD01_EMBLEMA.json
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop", "PLAN_V32_OPD01_EMBLEMA.json")

NODO = "producto_minimo_viable"

# LOS SEIS GRUPOS DE LA COSTURA DE PASOS, cada uno con sus posiciones medidas y
# el texto del superviviente. VERBATIM significa que el texto sale del grafo sin
# tocar; cuando hay remedio, el texto va escrito aqui y la guarda comprueba que
# empieza por el paso de indice mas bajo del grupo.
GRUPOS_PASOS = [
    {"origenes": [1, 10],
     "cosa": "identificar la hipotesis critica y el problema minimo que se valida",
     "texto": "Identifica la hipótesis de negocio más crítica que necesitas validar, "
              "de valor o de crecimiento, y bájala al problema central más pequeño "
              "que un cliente pagaría por resolver.",
     "motivo": "SALVAGUARDA: el superviviente manda identificar la hipotesis y no dice "
               "contra que sesgo se decide cual es la critica. El paso 10 trae la "
               "prueba (que alguien PAGARIA por resolverlo) y el inciso se adosa al "
               "paso que protege."},
    {"origenes": [2, 6, 11, 15, 16, 19],
     "cosa": "disenar la version mas simple, con el conjunto minimo definido desde la vision",
     "texto": "Diseña la versión más simple del producto que te permita probar esa "
              "hipótesis, definiendo el conjunto mínimo de características a partir "
              "de tu propia visión y no de una lista larga de pedidos.",
     "motivo": "SALVAGUARDA: el superviviente manda disenar lo mas simple y no dice "
               "contra que sesgo (la lista larga de pedidos). Los pasos 6, 15 y 19 "
               "nombran el sesgo y el inciso se adosa al paso que protege."},
    {"origenes": [3, 9, 13, 18],
     "cosa": "no agregar funciones extra, y la excepcion que las justifica",
     "texto": "Evita agregar funciones extra que no sean estrictamente necesarias "
              "para aprender; agrega una solo por excepción, cuando sin ella no sea "
              "posible vender.",
     "motivo": "ALCANCE: el superviviente trae UN criterio para la excepcion (que sirva "
               "para aprender) y el paso 13 trae el segundo (que sin ella no se pueda "
               "vender). El segundo entra a la enumeracion que el superviviente ya "
               "tiene, que es el remedio escrito del motivo."},
    {"origenes": [4, 7, 12, 20],
     "cosa": "lanzar solo a los primeros usuarios y no al mercado masivo",
     "texto": "Lanza tu primera versión a tus primeros usuarios (early adopters o "
              "earlyvangelists), no al mercado masivo.",
     "motivo": "NOMBRE: el superviviente dice early adopters y no dice earlyvangelists, "
               "que es la palabra por la que se busca y la que da nombre a dos nodos "
               "vecinos del grafo. El nombre viaja como DENOMINACION dentro del paso."},
    {"origenes": [5, 21],
     "cosa": "medir la reaccion real para validar o descartar",
     "texto": "Mide la reacción real de los usuarios, no solo su opinión, para validar "
              "o descartar tu hipótesis, no para expandir funciones.",
     "motivo": "SALVAGUARDA: el superviviente manda medir para validar y no dice contra "
               "que sesgo se lee la medicion. El paso 21 lo dice (no para expandir "
               "funciones) y el inciso se adosa al paso que protege."},
    {"origenes": [8, 14, 17, 22],
     "cosa": "iterar o cambiar de rumbo si nadie la encuentra suficiente",
     "texto": "Itera o cambia de rumbo si nadie encuentra interesante o suficiente tu "
              "solución, en ciclos cortos y de forma incremental.",
     "motivo": "ALCANCE: el superviviente manda iterar y no dice a que cadencia. Los "
               "pasos 14 y 16 traen la cadencia (ciclos cortos, incremental) y entra a "
               "la enumeracion del superviviente."},
]

# LOS CINCO GRUPOS DE LA COSTURA DE CONDICIONES, con los grupos EXACTOS que la
# ficha publico. Todos los supervivientes son VERBATIM: la ficha no declara
# ninguna linea perdida en este campo, solo repeticion.
GRUPOS_COND = [
    {"origenes": [1, 2],
     "cosa": "no se sabe cuando dejar de analizar y empezar a construir"},
    {"origenes": [3, 5, 7, 9],
     "cosa": "alguien quiere construir el producto completo con todas las funciones antes de validar"},
    {"origenes": [4],
     "cosa": "ya hay earlyvangelists listos para probar"},
    {"origenes": [6, 10],
     "cosa": "no hay evidencia todavia de que el problema sea real"},
    {"origenes": [8],
     "cosa": "no esta claro que caracteristicas priorizar"},
]

HUELLAS_PASOS = [
    {"origenes": [2, 6, 11, 15, 16, 19], "huella_repetida": "conjunto mínimo de características"},
    {"origenes": [8, 14, 17, 22], "huella_repetida": "Itera o cambia de rumbo si nadie"},
    {"origenes": [4, 7, 12, 20], "huella_repetida": "earlyvangelists"},
    {"origenes": [3, 9, 13, 18], "huella_repetida": "Agrega funciones nuevas solo"},
]
HUELLAS_COND = [
    {"origenes": [3, 5, 7, 9], "huella_repetida": "construir un producto completo"},
    {"origenes": [3, 5, 7, 9], "huella_repetida": "antes de validar"},
]
RASTROS = [
    "hipótesis", "pagaría por resolver", "tu propia visión", "para aprender",
    "posible vender", "early adopters", "earlyvangelists", "reacción real",
    "expandir funciones", "ciclos cortos", "incremental", "cambia de rumbo",
    "mercado masivo", "conjunto mínimo de características",
]

MOTIVO = (
    "OP-D-01, MOVIMIENTO 1 DE 4: el destejido del emblema. El nodo es COSTURA "
    "CONFIRMADA de fuente UNICA (bloque 80,2, el mas alto del archivo): sus 22 pasos "
    "son CINCO NARRACIONES del mismo MVP en fila (1 a 5, 6 a 9, 10 a 14, 15 a 18, 19 "
    "a 22) y sus 10 condiciones dicen CINCO cosas. No hay reparto que negociar y no "
    "se parte en dos nodos: SE PODA A UNO, que es lo que la ficha y la operacion "
    "mandan. CRITERIO DEL SUPERVIVIENTE, escrito antes de aplicarlo: de cada grupo de "
    "repeticion sobrevive EL DE INDICE MAS BAJO. El resultado cae sobre la NARRACION "
    "1 entera (pasos 1 a 5), que es la que el propio entregable del nodo ya narra, "
    "mas el paso 8, que es la SEXTA cosa (iterar o cambiar de rumbo) y no esta en la "
    "narracion 1. LAS PERDIDAS, REPARTIDAS POR LA TABLA DE LOS SEIS MOTIVOS: "
    "SALVAGUARDA en los pasos 1, 2 y 5 del resultado; ALCANCE en el 3 y en el 6; "
    "NOMBRE en el 4. DESTINO, METODO ALTERNATIVO y DIRECCION no aplican y por eso no "
    "se nombran. La fuente NO se toca (Ries, unica) y ningun bloque sale del nodo: "
    "este destejido no tiene destino, porque no hay material ajeno, solo repetido."
)


def main():
    with open(os.path.join(NODOS, NODO + ".json"), encoding="utf-8") as fh:
        d = json.load(fh)
    pasos = list(d.get("pasos_accionables") or [])
    cond = list(d.get("condiciones_activacion") or [])
    fallos = []
    if len(pasos) != 22:
        fallos.append("el nodo tiene %d pasos y el plan se escribio para 22" % len(pasos))
    if len(cond) != 10:
        fallos.append("el nodo tiene %d condiciones y el plan se escribio para 10" % len(cond))
    if fallos:
        print("PARADA: %s" % fallos)
        return 1

    # GUARDA 1: cobertura exacta de 1..22 y de 1..10, sin huecos ni repetidos.
    for nombre, grupos, total in (("pasos", GRUPOS_PASOS, 22), ("condiciones", GRUPOS_COND, 10)):
        todos = [i for g in grupos for i in g["origenes"]]
        if sorted(todos) != list(range(1, total + 1)):
            fallos.append("%s: la cobertura no es 1..%d, es %s" % (nombre, total, sorted(todos)))

    # GUARDA 2: el superviviente de cada grupo es el de indice mas bajo, y su
    # texto EMPIEZA por el texto original de ese paso (verbatim, o verbatim mas
    # el remedio adosado al final).
    finales_pasos = []
    for g in GRUPOS_PASOS:
        low = min(g["origenes"])
        original = pasos[low - 1]
        texto = g["texto"]
        raiz = original.rstrip(".").rstrip()
        if not texto.startswith(raiz[:40]):
            fallos.append("paso %d: el superviviente no empieza por el original (%r)"
                          % (low, original[:50]))
        finales_pasos.append(texto)

    finales_cond = []
    for g in GRUPOS_COND:
        low = min(g["origenes"])
        finales_cond.append(cond[low - 1])

    # GUARDA 3: cada huella vive HOY en todos sus origenes y en UNO del resultado
    # como maximo.
    for h in HUELLAS_PASOS:
        t = h["huella_repetida"]
        vive = [i for i, p in enumerate(pasos, 1) if t in p]
        if len(vive) < 2:
            fallos.append("huella de paso %r vive hoy en %s, no probaria nada" % (t, vive))
        if sum(1 for p in finales_pasos if t in p) > 1:
            fallos.append("huella de paso %r sigue en mas de un paso del resultado" % t)
    for h in HUELLAS_COND:
        t = h["huella_repetida"]
        vive = [i for i, c in enumerate(cond, 1) if t in c]
        if len(vive) < 2:
            fallos.append("huella de condicion %r vive hoy en %s, no probaria nada" % (t, vive))
        if sum(1 for c in finales_cond if t in c) > 1:
            fallos.append("huella de condicion %r sigue en mas de una del resultado" % t)

    # GUARDA 4: cada rastro vive hoy en el nodo (pasos o condiciones) y sigue
    # vivo en el resultado.
    hoy = pasos + cond
    luego = finales_pasos + finales_cond
    for r in RASTROS:
        if not any(r in x for x in hoy):
            fallos.append("rastro %r no vive en el nodo de HOY" % r)
        if not any(r in x for x in luego):
            fallos.append("rastro %r no sobrevive al destejido" % r)

    if fallos:
        print("PARADA: %d guarda(s) en rojo. NO se escribe el plan." % len(fallos))
        for x in fallos:
            print("  - %s" % x)
        return 1

    plan = {
        "operacion": "OP-D-01, movimiento 1: el destejido de producto_minimo_viable, el emblema",
        "regla": "OP-D-01 (docs/plan/02_DESTEJIDOS.md), con la perdida repartida por la "
                 "TABLA DE LOS SEIS MOTIVOS DE PERDIDA DE LINEA",
        "motivo": MOTIVO,
        "fecha_corte": "2026-08-15",
        "nodos": [{
            "nodo": NODO,
            "fuente_esperada": d.get("fuente"),
            "pasos_totales": len(pasos),
            "condiciones_totales": len(cond),
            "prefijos_pasos": [p[:34] for p in pasos],
            "prefijos_condiciones": [c[:34] for c in cond],
            "pasos_originales": pasos,
            "condiciones_originales": cond,
            "pasos_finales": finales_pasos,
            "condiciones_finales": finales_cond,
            "mapa_pasos": {str(i + 1): g["origenes"] for i, g in enumerate(GRUPOS_PASOS)},
            "mapa_condiciones": {str(i + 1): g["origenes"] for i, g in enumerate(GRUPOS_COND)},
            "grupos_pasos": GRUPOS_PASOS,
            "grupos_condiciones": GRUPOS_COND,
            "procedencia": [
                {"libro": "The Lean Startup - Eric Ries (fuente UNICA: la costura de este "
                          "nodo es de un solo libro consigo mismo, cinco narraciones en fila)",
                 "pasos_del_resultado": list(range(1, len(finales_pasos) + 1))},
            ],
            "pruebas_repeticion": HUELLAS_PASOS,
            "pruebas_repeticion_condiciones": HUELLAS_COND,
            "rastros": RASTROS,
            "salidas": [],
        }],
    }
    with open(SALIDA, "w", encoding="utf-8") as fh:
        json.dump(plan, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("ESCRITO: %s" % SALIDA)
    print("pasos %d -> %d, condiciones %d -> %d, cobertura exacta las dos"
          % (len(pasos), len(finales_pasos), len(cond), len(finales_cond)))
    for i, g in enumerate(GRUPOS_PASOS, 1):
        print("  paso %d <- %-22s %s" % (i, g["origenes"], finales_pasos[i - 1][:74]))
    for i, g in enumerate(GRUPOS_COND, 1):
        print("  cond %d <- %-22s %s" % (i, g["origenes"], finales_cond[i - 1][:74]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
