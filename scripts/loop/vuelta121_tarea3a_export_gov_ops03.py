# -*- coding: utf-8 -*-
"""vuelta121_tarea3a_export_gov_ops03.py . VUELTA 121, TAREA 3.a: cierra
`OP-S-03` (`docs/plan/05_SANEO.md`), export.gov a trade.gov.

NOMINA, remedida contra el grafo de hoy antes de escribir (los tres, vivos,
`deprecado` None): `calculo_de_aranceles_importacion`,
`evaluacion_preparacion_empresa_exportar`, `reglas_de_origen_fta_2`.

CUATRO menciones, no tres: `calculo_de_aranceles_importacion` nombra
export.gov DOS VECES (`resumen_teorico` y `pasos_accionables[1]`); los otros
dos nodos, una vez cada uno (`pasos_accionables[5]` y `pasos_accionables[3]`
respectivamente). `reglas_de_origen_fta_2` tambien cita `export.customsinfo.com`
en su paso 1: ES OTRO DOMINIO, fuera del alcance literal de esta operacion
("Solo pide cambiar el dominio", `05_SANEO.md` OP-S-03), y no se toca.

QUE ESCRIBE. Solo el texto de dominio, `export.gov` -> `trade.gov`, byte a
byte dentro del campo, en los cuatro puntos exactos de arriba. CORRECCION
DECLARADA con guarda de ancla por campo: si el texto vivo de hoy no calza
byte a byte con el ANCLA esperada, ROJO y no se escribe nada de ese nodo
(mismo patron que `vuelta120_tarea3a_incoterms_ops02.py`).

`dataset/metadata/master_graph.json` y su espejo de `web/` se recompilan
aparte, con el ciclo de tres, NUNCA por este script.

USO:
  python scripts/loop/vuelta121_tarea3a_export_gov_ops03.py --simular
  python scripts/loop/vuelta121_tarea3a_export_gov_ops03.py --mutacion-negativa
  python scripts/loop/vuelta121_tarea3a_export_gov_ops03.py
"""
import argparse
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

# (nid, campo, indice o None si el campo no es lista, ancla vieja, ancla nueva)
PUNTOS = [
    (
        "calculo_de_aranceles_importacion", "resumen_teorico", None,
        "Los aranceles, tarifas portuarias e impuestos afectan significativamente el "
        "costo final del producto en el mercado extranjero. Aunque típicamente el "
        "importador paga los aranceles, estos costos influyen en cuánto está dispuesto "
        "a pagar el comprador. Es esencial calcular estos costos usando herramientas "
        "como la base de datos de export.gov para determinar la viabilidad y "
        "competitividad del precio final. Puntero jurisdiccional-temporal: esta "
        "mecánica refleja la normativa de EE.UU. y los acuerdos vigentes a la fecha de "
        "la fuente; verifica el acuerdo y la regulación vigente en tu jurisdicción "
        "antes de actuar.",
        "Los aranceles, tarifas portuarias e impuestos afectan significativamente el "
        "costo final del producto en el mercado extranjero. Aunque típicamente el "
        "importador paga los aranceles, estos costos influyen en cuánto está dispuesto "
        "a pagar el comprador. Es esencial calcular estos costos usando herramientas "
        "como la base de datos de trade.gov para determinar la viabilidad y "
        "competitividad del precio final. Puntero jurisdiccional-temporal: esta "
        "mecánica refleja la normativa de EE.UU. y los acuerdos vigentes a la fecha de "
        "la fuente; verifica el acuerdo y la regulación vigente en tu jurisdicción "
        "antes de actuar.",
    ),
    (
        "calculo_de_aranceles_importacion", "pasos_accionables", 1,
        "Consultar la base de datos de aranceles en export.gov para el país de destino "
        "específico.",
        "Consultar la base de datos de aranceles en trade.gov para el país de destino "
        "específico.",
    ),
    (
        "evaluacion_preparacion_empresa_exportar", "pasos_accionables", 5,
        "Realiza la evaluación formal de preparación exportadora en "
        "export.gov/begin/assessment.asp",
        "Realiza la evaluación formal de preparación exportadora en "
        "trade.gov/begin/assessment.asp",
    ),
    (
        "reglas_de_origen_fta_2", "pasos_accionables", 3,
        "Consultar la regla de origen específica del producto en el capítulo de ROOs "
        "del FTA correspondiente (export.gov/fta)",
        "Consultar la regla de origen específica del producto en el capítulo de ROOs "
        "del FTA correspondiente (trade.gov/fta)",
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
    """Lee los tres nodos y comprueba que cada ANCLA_VIEJA calza byte a byte.
    Si mutar_ancla se da, se aplica esa funcion a cada ancla vieja antes de
    comparar (para la mutacion negativa)."""
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
    print("VUELTA 121, TAREA 3.a: OP-S-03, export.gov A trade.gov")
    print("=" * 78)
    print("nomina: calculo_de_aranceles_importacion (x2), "
          "evaluacion_preparacion_empresa_exportar (x1), reglas_de_origen_fta_2 (x1)")

    if a.mutacion_negativa:
        mutar = lambda s: s.replace("export.gov", "EXPORT_GOV_QUE_NO_EXISTE")
        resultado, _cache = calzar_todos(mutar_ancla=mutar)
        print("MUTACION NEGATIVA: ancla deliberadamente distinta de la real, en los "
              "cuatro puntos.")
        alguno_calza = False
        for nid, campo, idx, calza, _v, _n in resultado:
            print("  %s.%s%s calza (deberia ser False): %s" %
                  (nid, campo, ("[%d]" % idx) if idx is not None else "", calza))
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
        etiqueta = "%s.%s%s" % (nid, campo, ("[%d]" % idx) if idx is not None else "")
        print("%s calza con el ANCLA esperada: %s" % (etiqueta, calza))
        todos_calzan = todos_calzan and calza
    if not todos_calzan:
        raise SystemExit("ROJO: al menos un campo vivo de hoy no calza byte a byte con su "
                          "ANCLA esperada. NO SE ESCRIBE NADA de esta operacion: no se pisa "
                          "un estado distinto al medido en esta vuelta.")

    print()
    print("CORRECCION DECLARADA (vuelta 121, OP-S-03, docs/plan/05_SANEO.md): domain "
          "swap export.gov -> trade.gov en los cuatro puntos exactos, ningun otro "
          "campo tocado.")
    for nid, campo, idx, _calza, ancla_vieja, ancla_nueva in resultado:
        print("  %s.%s%s" % (nid, campo, ("[%d]" % idx) if idx is not None else ""))
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
    print("ESCRITO: los tres nodos de la nomina, cuatro campos en total, ningun otro "
          "campo tocado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
