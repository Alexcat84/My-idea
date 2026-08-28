# -*- coding: utf-8 -*-
"""vuelta121_tarea3b_herramientas_muertas_ops04.py . VUELTA 121, TAREA 3.b:
cierra `OP-S-04` (`docs/plan/05_SANEO.md`, `REMEDIO ESPEJO`), las seis
herramientas muertas.

NOMINA, remedida contra el grafo de hoy antes de escribir (los cinco, vivos,
`deprecado` None): `analisis_trafico_competitivo`,
`capturar_conocimiento_de_mercado`, `medicion_resultados_marketing_franquicia`,
`retargeting_display`, `seo_long_tail`.

REMEDIO ESPEJO: en los cinco nodos la herramienta muerta es EJEMPLO, no
OBJETO, asi que NINGUNO abre ficha de vigencia; la linea se vuelve generica y
conserva un ejemplo VIVO de la nomina ya verificada (AdRoll, MixRank, Adbeat,
BuySellAds, InnoCentive). Ninguna herramienta nueva se verifica por cuenta
propia.

OCHO PUNTOS, no seis: las seis muertas (Alexa, Compete, Perfect Audience, The
Deck, oDesk, Elance) viven repartidas en OCHO campos porque tres nodos las
nombran mas de una vez (`analisis_trafico_competitivo` dos veces,
`retargeting_display` tres veces).

DISCUTIBLE MARCADO (para la relectura ciega del auditor, antes de saber si
acierta): el punto 8 (`seo_long_tail.pasos_accionables[4]`, oDesk/Elance) NO
lleva ejemplo vivo verificado sustituto. La nomina de vivas verificada
(AdRoll, MixRank, Adbeat, BuySellAds, InnoCentive) es toda de trafico,
publicidad o innovacion; NINGUNA es una plataforma de freelancers, la
categoria de oDesk/Elance. La linea se generaliza SIN nombre propio (no se
inventa ni se verifica Upwork por cuenta propia, aunque el propio
`OPERACIONES.jsonl` ya documenta que absorbio a las dos). La clausula de
verificacion de `OP-S-04` ("toda linea generalizada conserva AL MENOS UN
ejemplo vivo verificado") NO se cumple LITERAL en este punto: PENDIENTE DE
DOCTRINA, traido a la mesa en el reporte.

QUE ESCRIBE. Solo el texto de las lineas con la herramienta muerta, byte a
byte, en los ocho puntos exactos de arriba. CORRECCION DECLARADA con guarda
de ancla por campo: si el texto vivo de hoy no calza byte a byte con el
ANCLA esperada, ROJO y no se escribe nada de ese nodo (mismo patron que
`vuelta121_tarea3a_export_gov_ops03.py`).

`dataset/metadata/master_graph.json` y su espejo de `web/` se recompilan
aparte, con el ciclo de tres, NUNCA por este script.

USO:
  python scripts/loop/vuelta121_tarea3b_herramientas_muertas_ops04.py --simular
  python scripts/loop/vuelta121_tarea3b_herramientas_muertas_ops04.py --mutacion-negativa
  python scripts/loop/vuelta121_tarea3b_herramientas_muertas_ops04.py
"""
import argparse
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

# (nid, campo, indice o None, ancla vieja, ancla nueva)
PUNTOS = [
    (
        "analisis_trafico_competitivo", "resumen_teorico", None,
        "Consiste en usar herramientas gratuitas de medición de tráfico (Alexa, "
        "Compete) y tiendas de aplicaciones para entender cómo los competidores "
        "atraen y retienen usuarios, identificando tendencias, fuentes de tráfico y "
        "posicionamiento en el mercado.",
        "Consiste en usar herramientas de medición de tráfico (por ejemplo, AdRoll o "
        "Adbeat) y tiendas de aplicaciones para entender cómo los competidores atraen "
        "y retienen usuarios, identificando tendencias, fuentes de tráfico y "
        "posicionamiento en el mercado.",
    ),
    (
        "analisis_trafico_competitivo", "pasos_accionables", 0,
        "Buscar y comparar tráfico de competidores con herramientas como Alexa o "
        "Compete",
        "Buscar y comparar tráfico de competidores con herramientas como AdRoll o "
        "Adbeat",
    ),
    (
        "capturar_conocimiento_de_mercado", "resumen_teorico", None,
        "Una vez entendido el cliente, hay que entender el mercado completo: "
        "tendencias, jugadores clave, necesidades no resueltas e innovadores. Para "
        "canales físicos esto implica reunirse con actores de mercados adyacentes, "
        "analistas y asistir a ferias. Para web/mobile, se usan herramientas de "
        "medición de tráfico (Alexa, Compete), tiendas de apps y sitios como Quora "
        "para mapear competencia y posicionarse mediante una grilla competitiva y un "
        "mapa de mercado.",
        "Una vez entendido el cliente, hay que entender el mercado completo: "
        "tendencias, jugadores clave, necesidades no resueltas e innovadores. Para "
        "canales físicos esto implica reunirse con actores de mercados adyacentes, "
        "analistas y asistir a ferias. Para web/mobile, se usan herramientas de "
        "medición de tráfico (por ejemplo, AdRoll o Adbeat), tiendas de apps y sitios "
        "como Quora para mapear competencia y posicionarse mediante una grilla "
        "competitiva y un mapa de mercado.",
    ),
    (
        "medicion_resultados_marketing_franquicia", "pasos_accionables", 2,
        "Usa herramientas como TrafficEstimate.com, Alexa y Google Analytics para "
        "estimar la calidad del tráfico que llega a tu web",
        "Usa herramientas como TrafficEstimate.com, AdRoll y Google Analytics para "
        "estimar la calidad del tráfico que llega a tu web",
    ),
    (
        "retargeting_display", "resumen_teorico", None,
        "El retargeting muestra anuncios a personas que ya visitaron el sitio pero no "
        "completaron una conversión (ej. carrito abandonado), aprovechando que ya "
        "tienen interés previo, lo que genera CTRs 3x a 10x más altos que anuncios "
        "normales. La publicidad display, por su parte, se distribuye a través de "
        "redes de anuncios (Google Display Network, AdRoll, Perfect Audience) que "
        "permiten llegar a audiencias amplias basadas en intereses relacionados, no "
        "solo búsquedas directas. Ambos canales complementan al SEM tradicional para "
        "reforzar la conversión y el reconocimiento de marca.",
        "El retargeting muestra anuncios a personas que ya visitaron el sitio pero no "
        "completaron una conversión (ej. carrito abandonado), aprovechando que ya "
        "tienen interés previo, lo que genera CTRs 3x a 10x más altos que anuncios "
        "normales. La publicidad display, por su parte, se distribuye a través de "
        "redes de anuncios (por ejemplo, Google Display Network o AdRoll) que "
        "permiten llegar a audiencias amplias basadas en intereses relacionados, no "
        "solo búsquedas directas. Ambos canales complementan al SEM tradicional para "
        "reforzar la conversión y el reconocimiento de marca.",
    ),
    (
        "retargeting_display", "pasos_accionables", 0,
        "Instalar píxeles de retargeting (Google AdWords, AdRoll, Perfect Audience) "
        "en el sitio",
        "Instalar píxeles de retargeting (por ejemplo, Google AdWords o AdRoll) en el "
        "sitio",
    ),
    (
        "retargeting_display", "pasos_accionables", 3,
        "Evaluar redes de display generales (Google Display Network) vs nicho (The "
        "Deck, BuySellAds)",
        "Evaluar redes de display generales (Google Display Network) vs nicho (por "
        "ejemplo, BuySellAds)",
    ),
    (
        "seo_long_tail", "pasos_accionables", 4,
        "Contratar freelancers (oDesk/Elance) para crear contenido específico por "
        "término",
        "Contratar freelancers en una plataforma de trabajo remoto para crear "
        "contenido específico por término",
    ),
]


def leer_crudo(nid):
    with io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8", newline="") as fh:
        bruto = fh.read()
    cola = ""
    while bruto and bruto[-1] in "\r\n":
        cola = bruto[-1] + cola
        bruto = bruto[:-1]
    return json.loads(bruto), cola


def escribir(nid, datos, cola):
    with io.open(os.path.join(NODOS, nid + ".json"), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def valor_actual(datos, campo, idx):
    v = datos.get(campo)
    if idx is None:
        return v
    return v[idx] if v is not None and 0 <= idx < len(v) else None


def poner_valor(datos, campo, idx, nuevo):
    if idx is None:
        datos[campo] = nuevo
    else:
        datos[campo][idx] = nuevo


def calzar_todos(mutar_ancla=None):
    resultado = []
    nodos_cache = {}
    for nid, campo, idx, ancla_vieja, ancla_nueva in PUNTOS:
        if nid not in nodos_cache:
            nodos_cache[nid] = leer_crudo(nid)
        datos, _cola = nodos_cache[nid]
        actual = valor_actual(datos, campo, idx)
        ancla_a_probar = mutar_ancla(ancla_vieja) if mutar_ancla else ancla_vieja
        calza = actual == ancla_a_probar
        resultado.append((nid, campo, idx, calza, ancla_vieja, ancla_nueva))
    return resultado, nodos_cache


def etiqueta(nid, campo, idx):
    return "%s.%s%s" % (nid, campo, ("[%d]" % idx) if idx is not None else "")


def main():
    ap = argparse.ArgumentParser()
    modo = ap.add_mutually_exclusive_group()
    modo.add_argument("--simular", action="store_true",
                       help="solo imprime el antes/despues, no escribe")
    modo.add_argument("--mutacion-negativa", action="store_true",
                       help="caso rojo: usa un ancla deliberadamente distinta y comprueba "
                            "que el script NO escribe")
    a = ap.parse_args()

    print("=" * 78)
    print("VUELTA 121, TAREA 3.b: OP-S-04, LAS SEIS HERRAMIENTAS MUERTAS (REMEDIO ESPEJO)")
    print("=" * 78)
    print("nomina: analisis_trafico_competitivo, capturar_conocimiento_de_mercado, "
          "medicion_resultados_marketing_franquicia, retargeting_display, seo_long_tail")

    if a.mutacion_negativa:
        mutar = lambda s: s.replace("Alexa", "ALEXA_QUE_NO_EXISTE").replace(
            "Compete", "COMPETE_QUE_NO_EXISTE").replace(
            "Perfect Audience", "PERFECT_AUDIENCE_QUE_NO_EXISTE").replace(
            "The Deck", "THE_DECK_QUE_NO_EXISTE").replace(
            "oDesk/Elance", "ODESK_ELANCE_QUE_NO_EXISTE")
        resultado, _cache = calzar_todos(mutar_ancla=mutar)
        print("MUTACION NEGATIVA: ancla deliberadamente distinta de la real, en los "
              "ocho puntos.")
        alguno_calza = False
        for nid, campo, idx, calza, _v, _n in resultado:
            print("  %s calza (deberia ser False): %s" % (etiqueta(nid, campo, idx), calza))
            alguno_calza = alguno_calza or calza
        if alguno_calza:
            raise SystemExit("ROJO DE LA PRUEBA: la mutacion negativa deberia NO calzar en "
                              "ningun punto y calzo en al menos uno. La guarda no muerde.")
        print("VERDE DE LA PRUEBA: ningun punto calza con el ancla mutada, como se "
              "espera; el caso real (mas abajo) no se corrio con este ancla, asi que no "
              "se escribio nada.")
        return 0

    resultado, cache = calzar_todos()
    todos_calzan = True
    for nid, campo, idx, calza, ancla_vieja, ancla_nueva in resultado:
        print("%s calza con el ANCLA esperada: %s" % (etiqueta(nid, campo, idx), calza))
        todos_calzan = todos_calzan and calza
    if not todos_calzan:
        raise SystemExit("ROJO: al menos un campo vivo de hoy no calza byte a byte con su "
                          "ANCLA esperada. NO SE ESCRIBE NADA de esta operacion: no se pisa "
                          "un estado distinto al medido en esta vuelta.")

    print()
    print("CORRECCION DECLARADA (vuelta 121, OP-S-04, docs/plan/05_SANEO.md, REMEDIO "
          "ESPEJO): las seis herramientas muertas se generalizan con ejemplo vivo, "
          "ningun otro campo tocado. DISCUTIBLE en el punto 8 (seo_long_tail): sin "
          "ejemplo vivo verificado de su categoria, ver docstring.")
    for nid, campo, idx, _calza, ancla_vieja, ancla_nueva in resultado:
        print("  %s" % etiqueta(nid, campo, idx))
        print("    VIEJO -> %r" % ancla_vieja)
        print("    NUEVO -> %r" % ancla_nueva)

    if a.simular:
        print()
        print("SIMULACION: no se escribe nada (--simular).")
        return 0

    for nid, campo, idx, _calza, _ancla_vieja, ancla_nueva in resultado:
        datos, cola = cache[nid]
        poner_valor(datos, campo, idx, ancla_nueva)

    for nid, (datos, cola) in cache.items():
        escribir(nid, datos, cola)

    print()
    print("ESCRITO: los cinco nodos de la nomina, ocho campos en total, ningun otro "
          "campo tocado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
