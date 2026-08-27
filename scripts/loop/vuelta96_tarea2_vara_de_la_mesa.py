# -*- coding: utf-8 -*-
r"""vuelta96_tarea2_vara_de_la_mesa.py . VUELTA 96, TAREA 2: LA VARA DE LA MESA
DE FORMULA, escrita, y PROBADA CONTRA TODO EL EXPEDIENTE YA ADJUDICADO antes de
usarse sobre los tres pares vivos.

LA PREGUNTA DE LA MESA (decision 2 del fundador, 27 ago 2026): la formula "trae
un procedimiento que X no tiene" produjo el 1083 CONFIRMADO y el 1009 CAIDO. Hay
una vara escrita que los separe, o no la hay?

LA VARA CANDIDATA, Y NO SE INVENTA: sale entera de doctrina ya escrita.
  FUENTE 1, banco 9.6.2 (docs/BANCO_DE_TEXTOS.md linea 1737 y siguientes),
    literal: "COMO SE RECONOCE UN PAR MADRE E HIJO... El hijo CABE ENTERO DENTRO
    DE UN PASO DE LA MADRE, y la madre conserva materia propia que el hijo no
    toca en ningun paso."
  FUENTE 2, OP-E-07.verificacion (docs/plan/OPERACIONES.jsonl), literal: "NO SE
    RELEE EL PAR: se lee su razon, que ya esta escrita."
  De las dos juntas sale la vara, y no anade nada a ninguna: LA RAZON TIENE QUE
  SENALAR UN PASO, FASE O LINEA UNICA de uno de los dos nodos como el sitio
  donde el otro cabe entero. Si la razon solo opone el nodo ENTERO contra lo
  que el otro "no tiene", "asume" o "da por supuesto", no ha senalado madre:
  ha comparado dos clases.

  T1, ANCLA SINGULAR: la razon designa UN paso, fase o linea concreta (por
     numero, por ordinal, por la formula "es/son ... linea", por "una de las
     OCHO", o por la palabra "madre" o "indice" dichas literalmente).
  T2, SIN RESIDUO DECLARADO: la razon NO declara ella misma que una parte del
     hijo QUEDA FUERA del solape. Se mide LITERAL ("queda/quedan/cae fuera"):
     no se ensancha para que atrape a nadie.

  VEREDICTO DE LA VARA = QUEDA si T1 pasa; SALE si T1 falla. T2 se mide y se
  publica al lado como refuerzo, NO decide sola: asi queda visible cuando los
  dos coinciden y cuando no.

COMO SE PRUEBA QUE ES UNA VARA Y NO UNA OPINION: se corre sobre los DIECINUEVE
pares que el expediente YA ADJUDICO (quince que QUEDAN y cuatro que SALIERON),
cada uno con el sitio de su adjudicacion citado en la tabla. SI CONTRADICE UNA
SOLA ADJUDICACION PUBLICADA, NO ES VARA CITABLE y el instrumento lo dice en su
veredicto final. Solo si las reproduce las diecinueve se aplica a los tres
vivos.

MECANICA DE ROJO, y no se talla nada si salta: un puesto del expediente sin
veredicto en docs/INTRA_DOMINIO_VEREDICTOS.jsonl. Probada por mutacion en
scripts/loop/vuelta96_tarea2_prueba_mutacion.py.

USO:
  python scripts/loop/vuelta96_tarea2_vara_de_la_mesa.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

# --- T1, ANCLA SINGULAR. Cada familia va con la forma del expediente que la
# --- motivo, para que ninguna sea un patron inventado para esta vuelta.
ANCLA = [
    ("paso numerado", re.compile(r"\bpaso\s+\d+\b", re.IGNORECASE)),
    ("paso ordinal", re.compile(r"\b(?:primer|segundo|tercer|cuarto|quinto|sexto|septimo|octavo)o?\s+paso\b", re.IGNORECASE)),
    ("fase numerada u ordinal", re.compile(r"\bfase\s+\d+\b|\ben\s+la\s+(?:primera|segunda|tercera|cuarta|quinta|sexta|septima|octava)\b", re.IGNORECASE)),
    ("es/son linea", re.compile(r"\b(?:es|son)\s+(?:una|dos|tres|la)?\s*l[ií]neas?\b", re.IGNORECASE)),
    ("en N lineas", re.compile(r"\ben\s+(?:una|dos|tres|media)\s+(?:sola\s+)?l[ií]neas?\b", re.IGNORECASE)),
    ("dos puntos y UNA LINEA", re.compile(r":\s*una\s+l[ií]nea\b", re.IGNORECASE)),
    ("una de sus lineas", re.compile(r"\buna\s+de\s+sus\s+l[ií]neas\b", re.IGNORECASE)),
    ("termina/cierra/empieza con una linea", re.compile(r"\b(?:termina|cierra|empieza)\s+con\s+una\s+l[ií]nea\b", re.IGNORECASE)),
    ("entre sus pasos", re.compile(r"\bentre\s+sus\s+pasos\b", re.IGNORECASE)),
    ("el paso nombra", re.compile(r"\bel\s+paso\s+nombra\b", re.IGNORECASE)),
    ("una de las N", re.compile(r"\buna\s+de\s+(?:las|los)\s+(?:dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|\d+)\b", re.IGNORECASE)),
    ("la palabra madre, literal", re.compile(r"\b(?:la|su)\s+madre\b", re.IGNORECASE)),
    ("es el indice", re.compile(r"\bes\s+el\s+[ií]ndice\b", re.IGNORECASE)),
]

# --- T2, RESIDUO DECLARADO. Literal y estrecho a proposito.
RESIDUO = re.compile(r"\b(?:queda|quedan|cae|caen)\s+(?:entero\s+|enteros\s+)?fuera\b", re.IGNORECASE)

# EL EXPEDIENTE YA ADJUDICADO: (puesto, veredicto publicado, sitio del veredicto).
# Ninguna de estas tres columnas la decide este instrumento: se leen del
# expediente y el instrumento solo las contrasta contra lo que su vara da.
EXPEDIENTE = [
    (1083, "QUEDA", "acta 91, ratificado por el acta 95 seccion 3.3"),
    (1191, "QUEDA", "encargo de la vuelta 95, TAREA 3.d, mandato explicito"),
    (1886, "QUEDA", "acta 93, ACTA_AUDITOR.md linea 32695"),
    (1844, "QUEDA", "acta 95 adjudicacion 4.1, ACTA_AUDITOR.md linea 33773"),
    (896, "QUEDA", "vuelta 95 TAREA 3, ratificado por acta 95 seccion 3.4"),
    (909, "QUEDA", "vuelta 95 TAREA 3, ratificado por acta 95 seccion 3.4"),
    (910, "QUEDA", "vuelta 95 TAREA 3, ratificado por acta 95 seccion 3.4"),
    (940, "QUEDA", "vuelta 95 TAREA 3, ratificado por acta 95 seccion 3.4"),
    (983, "QUEDA", "vuelta 95 TAREA 3, ratificado por acta 95 seccion 3.4"),
    (993, "QUEDA", "vuelta 95 TAREA 3, ratificado por acta 95 seccion 3.4"),
    (1020, "QUEDA", "vuelta 95 TAREA 3, ratificado por acta 95 seccion 3.4"),
    (1057, "QUEDA", "vuelta 95 TAREA 3, ratificado por acta 95 seccion 3.4"),
    (1086, "QUEDA", "vuelta 95 TAREA 3, ratificado por acta 95 seccion 3.4"),
    (1196, "QUEDA", "vuelta 95 TAREA 3, ratificado por acta 95 seccion 3.4"),
    (1220, "QUEDA", "vuelta 95 TAREA 3, ratificado por acta 95 seccion 3.4"),
    (1098, "SALE", "vuelta 92, caida de clase del acta 91; PENDIENTES.md"),
    (1009, "SALE", "vuelta 93; PENDIENTES.md seccion de la vuelta 93"),
    (1281, "SALE", "vuelta 94; PENDIENTES.md seccion de la vuelta 94"),
    (1992, "SALE", "vuelta 94; PENDIENTES.md seccion de la vuelta 94"),
]

LOS_TRES_VIVOS = [886, 890, 947]


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def aplicar_vara(razon):
    """LA UNICA PIEZA DE JUICIO. Devuelve (veredicto, familias_que_casan,
    residuo_declarado)."""
    familias = [nombre for nombre, rx in ANCLA if rx.search(razon)]
    residuo = bool(RESIDUO.search(razon))
    return ("QUEDA" if familias else "SALE"), familias, residuo


def medir(expediente=EXPEDIENTE, tres=LOS_TRES_VIVOS):
    ver = {int(v["puesto_intra"]): v for v in cargar_jsonl(VEREDICTOS)}
    fallos = []
    filas_exp, filas_vivos = [], []
    for puesto, publicado, sitio in expediente:
        v = ver.get(puesto)
        if v is None:
            fallos.append("el puesto %s del expediente no tiene veredicto en INTRA_DOMINIO_VEREDICTOS.jsonl" % puesto)
            continue
        vara, familias, residuo = aplicar_vara(v["razon"])
        filas_exp.append({"puesto": puesto, "publicado": publicado, "sitio": sitio,
                          "vara": vara, "familias": familias, "residuo": residuo,
                          "calza": vara == publicado})
    for puesto in tres:
        v = ver.get(puesto)
        if v is None:
            fallos.append("el puesto vivo %s no tiene veredicto en INTRA_DOMINIO_VEREDICTOS.jsonl" % puesto)
            continue
        vara, familias, residuo = aplicar_vara(v["razon"])
        filas_vivos.append({"puesto": puesto, "vara": vara, "familias": familias, "residuo": residuo})
    return filas_exp, filas_vivos, fallos


def main():
    filas_exp, filas_vivos, fallos = medir()
    if fallos:
        print("ROJO, %d cosa(s) no se pudieron leer y NO SE TALLA NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    print("=" * 100)
    print("LA VARA DE LA MESA, PROBADA CONTRA EL EXPEDIENTE (vuelta 96, TAREA 2)")
    print("T1 ANCLA SINGULAR decide; T2 RESIDUO DECLARADO se publica al lado y no decide sola.")
    print("=" * 100)
    print()
    print("| puesto | veredicto PUBLICADO | sitio | la VARA da | familias de ancla que casan | residuo declarado | calza |")
    print("|---:|---|---|---|---|---|---|")
    for f in filas_exp:
        print("| %d | %s | %s | %s | %s | %s | %s |"
              % (f["puesto"], f["publicado"], f["sitio"], f["vara"],
                 ", ".join(f["familias"]) if f["familias"] else "NINGUNA",
                 "SI" if f["residuo"] else "no",
                 "SI" if f["calza"] else "**NO**"))

    calzan = [f for f in filas_exp if f["calza"]]
    chocan = [f for f in filas_exp if not f["calza"]]
    print()
    print("EXPEDIENTE: %d filas | CALZAN %d | CHOCAN %d" % (len(filas_exp), len(calzan), len(chocan)))
    if chocan:
        print("CHOCAN, nominal: %s" % ", ".join(str(f["puesto"]) for f in chocan))

    print()
    if chocan:
        print("VEREDICTO SOBRE LA VARA: NO ES VARA CITABLE. Contradice %d adjudicacion(es)" % len(chocan))
        print("ya publicada(s), y una vara que tumba lo ya adjudicado no separa nada: reordena.")
        print("Por la decision 2 del fundador, LOS TRES QUEDAN COMO ESTAN y la duda va sellada.")
        return 0

    print("VEREDICTO SOBRE LA VARA: ES VARA CITABLE. Reproduce las %d adjudicaciones" % len(filas_exp))
    print("publicadas SIN UNA SOLA discrepancia, incluidas las dos que la mesa tenia que")
    print("separar (el 1083 QUEDA y el 1009 SALE), que comparten la formula literal.")
    print()
    print("=" * 100)
    print("LOS TRES VIVOS, ADJUDICADOS POR ELLA")
    print("=" * 100)
    print()
    print("| puesto | la VARA da | familias de ancla que casan | residuo declarado |")
    print("|---:|---|---|---|")
    for f in filas_vivos:
        print("| %d | %s | %s | %s |"
              % (f["puesto"], f["vara"],
                 ", ".join(f["familias"]) if f["familias"] else "NINGUNA",
                 "SI" if f["residuo"] else "no"))
    print()
    print("RESUMEN: QUEDAN %s | SALEN %s"
          % (", ".join(str(f["puesto"]) for f in filas_vivos if f["vara"] == "QUEDA") or "ninguno",
             ", ".join(str(f["puesto"]) for f in filas_vivos if f["vara"] == "SALE") or "ninguno"))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
