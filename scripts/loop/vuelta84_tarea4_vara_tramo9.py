# -*- coding: utf-8 -*-
"""VUELTA 84, TAREA 4: la vara del tramo 9 de OP-E-01, corrida con
instrumento PROPIO de esta vuelta (EJECUTOR.md regla 2, el instrumento
manda). Sucesor directo de scripts/loop/vuelta83_tarea4_vara_tramo7.py,
mismo metodo, tramo y vuelta cambiados.

(4.a) Cruza las 30 unidades frescas del tramo 9 (indices 48 a 77 de la
cabeza de la bolsa filtrada V84) contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl
SIN DIRECCION (el par no dirigido {a, b}).
(4.b) Cruza las mismas 30 contra la bolsa filtrada de la vuelta 83
(docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V83.jsonl) buscando la reciproca
(el par al reves).

Los pares se LEEN de docs/loop/SALIDA_V84_TRAMO9_FILTRO_P91_GUARDA_CADENA.txt,
nunca tecleados.
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILTRO = os.path.join(RAIZ, "docs", "loop", "SALIDA_V84_TRAMO9_FILTRO_P91_GUARDA_CADENA.txt")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
BOLSA = os.path.join(RAIZ, "docs", "plan", "PASO_NODO_CALIBRADO_FILTRADO_V83.jsonl")

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
    frescas = [u for u in unidades if u[0] >= 48]
    print("unidades leidas del filtro: %d | frescas (48..77): %d" % (len(unidades), len(frescas)))
    assert len(frescas) == 30, "no son 30 frescas"

    veredictos, total = leer_veredictos()
    print("veredictos leidos: %d | pares no dirigidos unicos: %d" % (total, len(veredictos)))

    bolsa = leer_bolsa()
    print("bolsa filtrada V83: %d unidades" % len(bolsa))

    pares_bolsa = set()
    for fila in bolsa:
        p = par_de(fila)
        if p:
            pares_bolsa.add(p)

    print()
    print("| # | par | veredicto sin direccion (4.a) | reciproca en la bolsa V83 (4.b) |")
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
    print("RESUMEN: %d de 30 con veredicto, %d de 30 con reciproca" % (con_veredicto, con_reciproca))


if __name__ == "__main__":
    main()
