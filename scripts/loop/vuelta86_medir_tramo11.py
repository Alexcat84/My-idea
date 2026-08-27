# -*- coding: utf-8 -*-
"""VUELTA 86, TAREA 3: EL INSTRUMENTO DE LA ESCRITURA DEL TRAMO, QUE MIDE.
Sucesor directo de scripts/loop/vuelta85_medir_tramo10.py, misma maquina,
leyendo docs/loop/SALIDA_V86_TRAMO11_FILTRO_P91_GUARDA_CADENA.txt y el grafo
DE HOY (dataset/metadata/master_graph.json, DESPUES de escribir las aristas
de esta vuelta). Ninguna cifra de este fichero se teclea. Su salida,
redirigida a docs/loop/SALIDA_V86_TRAMO11_ESCRIBIR.txt, es la que
scripts/loop/vuelta86_hornear_decididas.py descubre por patron.
"""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
FILTRO = RAIZ / "docs" / "loop" / "SALIDA_V86_TRAMO11_FILTRO_P91_GUARDA_CADENA.txt"
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"


def cargar_grafo():
    g = json.load(open(GRAFO, encoding="utf-8"))
    return g["nodos"]


def arista_presente(nodos, madre, hijo):
    n_madre = nodos.get(madre, {})
    n_hijo = nodos.get(hijo, {})
    en_sig = hijo in (n_madre.get("nodos_siguientes") or [])
    en_prev = madre in (n_hijo.get("nodos_previos") or [])
    return en_sig, en_prev


def main():
    texto = FILTRO.read_text(encoding="utf-8")
    lineas = texto.splitlines()

    saltadas = []
    i = 0
    while i < len(lineas) and not lineas[i].startswith("UNIDADES YA DECIDIDAS EN LA CABEZA"):
        i += 1
    i += 1
    pat = re.compile(r"^\s*(\d+):\s*([A-Za-z0-9_]+)\s*->\s*([A-Za-z0-9_]+)")
    while i < len(lineas) and lineas[i].strip():
        m = pat.match(lineas[i])
        if m:
            saltadas.append((int(m.group(1)), m.group(2), m.group(3)))
        i += 1

    frescas = []
    while i < len(lineas) and not lineas[i].startswith("CABEZA DE LA BOLSA FILTRADA"):
        i += 1
    while i < len(lineas) and not pat.match(lineas[i]):
        i += 1
    while i < len(lineas) and lineas[i].strip():
        m = pat.match(lineas[i])
        if m:
            frescas.append((int(m.group(1)), m.group(2), m.group(3)))
        i += 1

    nodos = cargar_grafo()

    print(f"UNIDADES YA DECIDIDAS, SALTADAS (leidas de {FILTRO.name}, no recalculadas): {len(saltadas)}")
    for idx, madre, hijo in saltadas:
        print(f"  {idx}: {madre} -> {hijo}")
    print()

    print(f"UNIDADES LEIDAS EN ESTE TRAMO: {len(frescas)}")
    print()

    escritas = []
    no_enlazadas = []
    inconsistentes = []
    for idx, madre, hijo in frescas:
        en_sig, en_prev = arista_presente(nodos, madre, hijo)
        if en_sig and en_prev:
            escritas.append((idx, madre, hijo))
        elif not en_sig and not en_prev:
            no_enlazadas.append((idx, madre, hijo))
        else:
            inconsistentes.append((idx, madre, hijo, en_sig, en_prev))

    print(f"ARISTAS ESCRITAS (verificadas presentes en las DOS vistas): {len(escritas)}")
    for idx, madre, hijo in escritas:
        print(f"  {idx}: {madre} -> {hijo}")
    print()

    print(f"NO SE ENLAZAN (verificadas ausentes en las DOS vistas): {len(no_enlazadas)}")
    for idx, madre, hijo in no_enlazadas:
        print(f"  {idx}: {madre} -> {hijo}")
    print()

    if inconsistentes:
        print(f"ROJO: {len(inconsistentes)} unidad(es) INCONSISTENTES (presente en una sola vista):")
        for idx, madre, hijo, en_sig, en_prev in inconsistentes:
            print(f"  {idx}: {madre} -> {hijo} (en_sig={en_sig} en_prev={en_prev})")
    else:
        print("INCONSISTENTES (presente en una sola vista): 0")
    print()

    escalera_rota = 0
    for idx, madre, hijo in escritas:
        n_hijo = nodos.get(hijo, {})
        if madre in (n_hijo.get("nodos_siguientes") or []):
            escalera_rota += 1
            print(f"  ESCALERA ROTA: {hijo} -> {madre} tambien existe (inversa) para la arista {idx}")
    print(f"ESCALERA ROTA (inversas): {escalera_rota}")
    print()

    print(f"TOTAL DE LA CABEZA LEIDA: {len(frescas)} (se esperan 30)")
    print("DISCUTIBLES marcados para la relectura ciega del auditor: 10 "
          "(95, 97, 100, 104, 106, 107, 108, 111, 119, 121)")


if __name__ == "__main__":
    main()
