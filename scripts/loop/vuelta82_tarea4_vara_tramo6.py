# -*- coding: utf-8 -*-
"""VUELTA 82, TAREA 4: la vara del tramo 6 de OP-E-01, corrida con
instrumento PROPIO de esta vuelta (EJECUTOR.md regla 2, el instrumento
manda: una cifra de un acta vieja nunca es fuente de una cifra nueva, se
corre de nuevo). Reducida porque el auditor ya la corrio entera en el acta
de la vuelta 81, seccion 3, pero no suprimida.

(4.a) Cruza las 10 unidades frescas del tramo 6 (indices 20 a 29 de la
cabeza de la bolsa filtrada) contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl SIN
DIRECCION (el par no dirigido {a, b}).
(4.b) Cruza las mismas 10 contra la bolsa filtrada de la vuelta 80
(docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V80.jsonl) buscando la reciproca
(el par al reves).

Los pares se LEEN de docs/loop/SALIDA_V80_TRAMO6_FILTRO_P91_GUARDA_CADENA.txt,
nunca tecleados.
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILTRO = os.path.join(RAIZ, "docs", "loop", "SALIDA_V80_TRAMO6_FILTRO_P91_GUARDA_CADENA.txt")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
BOLSA = os.path.join(RAIZ, "docs", "plan", "PASO_NODO_CALIBRADO_FILTRADO_V80.jsonl")

RE_UNIDAD = re.compile(r"^\s*(\d+):\s*(.+?)\s*->\s*(.+?)\s*\(paso\s*(.+?),\s*dominio\s*(.+?)\)\s*\|")


def leer_unidades():
    unidades = []
    for linea in io.open(FILTRO, encoding="utf-8"):
        m = RE_UNIDAD.match(linea)
        if m:
            idx, madre, hijo, paso, dominio = m.groups()
            unidades.append((int(idx), madre, hijo, paso, dominio))
    return unidades


def leer_veredictos():
    veredictos = {}
    total = 0
    for linea in io.open(VEREDICTOS, encoding="utf-8"):
        linea = linea.strip()
        if not linea:
            continue
        d = json.loads(linea)
        total += 1
        veredictos[frozenset((d["nodo_a"], d["nodo_b"]))] = d
    return veredictos, total


def leer_bolsa():
    filas = []
    if os.path.exists(BOLSA):
        for linea in io.open(BOLSA, encoding="utf-8"):
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))
    return filas


def par_de(fila):
    for clave_a, clave_b in (("madre", "hijo"), ("nodo_a", "nodo_b"),
                              ("origen", "destino"), ("desde", "hasta"), ("a", "b")):
        if clave_a in fila and clave_b in fila:
            return fila[clave_a], fila[clave_b]
    return None


def main():
    unidades = leer_unidades()
    frescas = [u for u in unidades if u[0] >= 20]
    print("unidades leidas del filtro: %d | frescas (20..29): %d" % (len(unidades), len(frescas)))
    assert len(frescas) == 10, "no son 10 frescas"

    veredictos, total = leer_veredictos()
    print("veredictos leidos: %d | pares no dirigidos unicos: %d" % (total, len(veredictos)))

    bolsa = leer_bolsa()
    print("bolsa filtrada V80: %d unidades" % len(bolsa))

    pares_bolsa = set()
    for fila in bolsa:
        p = par_de(fila)
        if p:
            pares_bolsa.add(p)

    print()
    print("| # | par | veredicto sin direccion (4.a) | reciproca en la bolsa V80 (4.b) |")
    print("|---:|---|---|---|")
    con_veredicto = 0
    con_reciproca = 0
    for idx, madre, hijo, paso, dominio in frescas:
        v = veredictos.get(frozenset((madre, hijo)))
        if v:
            con_veredicto += 1
            celda = "%s puesto %d (%s), dirigido %s -> %s" % (
                v["clase"], v["puesto_intra"], v["dominio"], v["nodo_a"], v["nodo_b"])
        else:
            celda = "sin veredicto"
        reciproca = (hijo, madre) in pares_bolsa
        if reciproca:
            con_reciproca += 1
        print("| %d | `%s -> %s` (paso %s, dominio %s) | %s | %s |"
              % (idx, madre, hijo, paso, dominio, celda, "SI" if reciproca else "no"))

    print()
    print("RESUMEN: %d de 10 con veredicto, %d de 10 con reciproca" % (con_veredicto, con_reciproca))


if __name__ == "__main__":
    main()
