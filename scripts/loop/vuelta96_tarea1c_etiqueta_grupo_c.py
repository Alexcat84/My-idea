# -*- coding: utf-8 -*-
r"""vuelta96_tarea1c_etiqueta_grupo_c.py . VUELTA 96, TAREA 1(c): REMIDE CON
CODIGO PROPIO la ETIQUETA que el acta de la vuelta 94 le puso al grupo C del
cribado de cita de linea, y que el acta de la vuelta 95 (seccion 6, punto 1)
declara FALSA para nueve de sus dieciocho.

POR QUE NACE. El acta 94 publico el grupo C como "ni citan linea ni traen forma
de indice". El acta 95 lo remidio y dijo que NUEVE de las 18 mencionan la
palabra "linea", OCHO de ellas con la formula literal "es/son UNA LINEA", y que
la causa es que el patron del grupo A casa "EN una linea" y no casa "ES una
linea". EJECUTOR.md regla 2 ("EL INSTRUMENTO MANDA") prohibe publicar esa cifra
copiandola del acta: esta corrida es la fuente y el acta 95 se cita como
CONTRASTE.

DE DONDE SALE LA BOLSA. El grupo C NO se teclea: se calcula importando
clasifica_razon() de scripts/loop/vuelta95_tarea3a_cribado_cita_de_linea.py,
el mismo instrumento cuya salida el auditor de la vuelta 95 reprodujo con una
tercera implementacion independiente (acta 95 seccion 3.1).

LAS TRES PREGUNTAS que se le hacen a cada razon del grupo C, cada una con su
regex y ninguna con juicio humano por medio:
  MENCIONA: el texto contiene la palabra "linea" o "lineas" (con o sin acento).
  FORMULA ESTRICTA: "es/son (una|dos|tres|la) linea(s)", con determinante.
  FORMULA ANCHA:    "es/son ... linea(s)", con determinante o sin el, que
            recoge ademas el plural pelado ("son lineas").
  EN UNA LINEA:     "en ... linea", la otra forma de anclar que el patron del
            grupo A del acta 94 tampoco casa cuando lleva una palabra por medio
            ("en una SOLA linea"). NO es la formula "es/son": se cuenta aparte
            justamente para no confundirlas.
  PATRON A: el patron del grupo A del acta 94 casa (tiene que dar CERO en las
            18: si casara, la fila no estaria en el grupo C, y que de cero es
            la prueba de que la bolsa es la que se dice que es).

MECANICA DE ROJO, y no se talla nada si salta: (i) una fila sin razon en
docs/INTRA_DOMINIO_VEREDICTOS.jsonl; (ii) el grupo C no tiene exactamente 18
filas; (iii) alguna de las 18 casa el patron A del acta (contradiccion con su
propia clasificacion). Probada por mutacion en
scripts/loop/vuelta96_tarea1c_prueba_mutacion.py.

USO:
  python scripts/loop/vuelta96_tarea1c_etiqueta_grupo_c.py
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

from vuelta95_tarea3a_cribado_cita_de_linea import (  # noqa: E402
    clasifica_razon, cargar_jsonl, ENTRADA, VEREDICTOS, PATRONES_A,
)

MENCIONA = re.compile(r"l[i\u00ed]neas?\b", re.IGNORECASE)
FORMULA = re.compile(r"\b(?:es|son)\s+(?:una|dos|tres|la)\s+l[i\u00ed]neas?\b", re.IGNORECASE)
FORMULA_ANCHA = re.compile(r"\b(?:es|son)\s+(?:una|dos|tres|la)?\s*l[i\u00ed]neas?\b", re.IGNORECASE)
EN_LINEA = re.compile(r"\ben\s+\w+(?:\s+\w+)?\s+l[i\u00ed]neas?\b", re.IGNORECASE)

TAMANO_ESPERADO_C = 18


def medir(tamano_esperado_c=TAMANO_ESPERADO_C):
    """Devuelve (filas, fallos). Cada fila es un dict con el puesto y las tres
    respuestas. Si fallos no esta vacio, main() no talla nada."""
    entrada = cargar_jsonl(ENTRADA)
    veredictos = {int(v["puesto_intra"]): v for v in cargar_jsonl(VEREDICTOS)}
    fallos = []
    grupo_c = []
    for fila in entrada:
        puesto = fila["puesto"]
        v = veredictos.get(puesto)
        if v is None:
            fallos.append("puesto %s no tiene puesto_intra en INTRA_DOMINIO_VEREDICTOS.jsonl" % puesto)
            continue
        if clasifica_razon(v["razon"]) == "C":
            grupo_c.append((puesto, v["razon"]))
    if len(grupo_c) != tamano_esperado_c:
        fallos.append("el grupo C trae %d filas y se esperaban %d" % (len(grupo_c), tamano_esperado_c))
    filas = []
    for puesto, razon in sorted(grupo_c):
        casa_a = any(p.search(razon) for p in PATRONES_A)
        if casa_a:
            fallos.append("el puesto %s esta en el grupo C y SI casa el patron A del acta" % puesto)
        filas.append({
            "puesto": puesto,
            "menciona": bool(MENCIONA.search(razon)),
            "formula": bool(FORMULA.search(razon)),
            "formula_ancha": bool(FORMULA_ANCHA.search(razon)),
            "en_linea": bool(EN_LINEA.search(razon)),
            "casa_a": casa_a,
        })
    return filas, fallos


def main():
    filas, fallos = medir()
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE TALLA NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    menciona = [f["puesto"] for f in filas if f["menciona"]]
    formula = [f["puesto"] for f in filas if f["formula"]]
    formula_ancha = [f["puesto"] for f in filas if f["formula_ancha"]]
    en_linea = [f["puesto"] for f in filas if f["en_linea"] and not f["formula_ancha"]]
    ni_una = [f["puesto"] for f in filas if not f["menciona"]]

    print("=" * 90)
    print("LA ETIQUETA DEL GRUPO C, REMEDIDA (vuelta 96, TAREA 1.c)")
    print("Bolsa calculada con clasifica_razon() de vuelta95_tarea3a_cribado_cita_de_linea.py;")
    print("razones de %s. Ninguna cifra tecleada." % os.path.basename(VEREDICTOS))
    print("=" * 90)
    print()
    print("| pregunta | cuantas de las %d |" % len(filas))
    print("|---|---:|")
    print("| mencionan la palabra \"linea\" en cualquier forma | %d |" % len(menciona))
    print("| lo hacen con la formula ESTRICTA \"es/son UNA LINEA\" (con determinante) | %d |" % len(formula))
    print("| lo hacen con la formula ANCHA \"es/son ... LINEA\" (con o sin determinante) | %d |" % len(formula_ancha))
    print("| anclan con \"en ... linea\" y NO con \"es/son\" | %d |" % len(en_linea))
    print("| NO mencionan la palabra \"linea\" en ninguna forma | %d |" % len(ni_una))
    print("| casan el patron A del acta 94 (tiene que ser 0) | %d |" % len([f for f in filas if f["casa_a"]]))
    print()
    print("ENUMERACION 'mencionan linea' (%d): %s" % (len(menciona), ", ".join(str(p) for p in menciona)))
    print("ENUMERACION 'formula ESTRICTA es/son UNA LINEA' (%d): %s" % (len(formula), ", ".join(str(p) for p in formula)))
    print("ENUMERACION 'formula ANCHA es/son ... LINEA' (%d): %s" % (len(formula_ancha), ", ".join(str(p) for p in formula_ancha)))
    print("ENUMERACION 'en ... linea, no es/son' (%d): %s" % (len(en_linea), ", ".join(str(p) for p in en_linea)))
    print("ENUMERACION 'no la mencionan' (%d): %s" % (len(ni_una), ", ".join(str(p) for p in ni_una)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
