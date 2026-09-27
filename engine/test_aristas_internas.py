# -*- coding: utf-8 -*-
"""scripts/aplicar_aristas_internas.py: las aristas internas de un mundo se escriben reciprocas, una sola vez, y se
rechazan si nombran un nodo fuera del pack, si no traen su por que o si cierran un ciclo dirigido.

Caso a mano, pack de tres nodos A, B y C sin aristas:
  aristas A->B y B->C (con por que)
    A.nodos_siguientes = [B]          A.nodos_previos = []
    B.nodos_siguientes = [C]          B.nodos_previos = [A]
    C.nodos_siguientes = []           C.nodos_previos = [B]
    -> 2 aristas nuevas en 3 nodos (A, B y C tocados)
  segunda corrida con el mismo fichero -> 0 nuevas, ficheros iguales
  arista C->A sobre ese grafo: A->B->C->A es un ciclo -> rechazo, codigo 1, nada escrito
  arista A->Z (Z no esta en el pack) -> rechazo, codigo 1
  arista C->A sin por que (sobre un pack sin aristas) -> rechazo, codigo 1

    python engine/test_aristas_internas.py
"""
import json
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(RAIZ, "scripts", "aplicar_aristas_internas.py")


def pack(carpeta, ids):
    for i in ids:
        with open(os.path.join(carpeta, i + ".json"), "w", encoding="utf-8") as f:
            json.dump({"node_id": i, "titulo_concepto": i, "nodos_previos": [], "nodos_siguientes": []}, f)


def leer(carpeta, i):
    with open(os.path.join(carpeta, i + ".json"), encoding="utf-8") as f:
        return json.load(f)


def correr(aristas, carpeta, *extra):
    ruta = os.path.join(carpeta, "..", "aristas.json")
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump({"aristas": aristas}, f)
    r = subprocess.run([sys.executable, SCRIPT, ruta, "--nodos", carpeta, *extra], capture_output=True, text=True)
    return r.returncode, r.stdout


def main():
    fallos = []
    with tempfile.TemporaryDirectory() as t:
        nodos = os.path.join(t, "nodos")
        os.mkdir(nodos)
        pack(nodos, ["A", "B", "C"])
        base = [{"de": "A", "a": "B", "por_que": "B usa lo que deja A"}, {"de": "B", "a": "C", "por_que": "C continua B"}]
        codigo, salida = correr(base, nodos)
        if codigo != 0 or "2 nuevas en 3 nodos" not in salida:
            fallos.append("primera corrida: %r %r" % (codigo, salida))
        esperado = {"A": ([], ["B"]), "B": (["A"], ["C"]), "C": (["B"], [])}
        for i, (prev, sig) in esperado.items():
            n = leer(nodos, i)
            if (n["nodos_previos"], n["nodos_siguientes"]) != (prev, sig):
                fallos.append("%s: previos %r siguientes %r" % (i, n["nodos_previos"], n["nodos_siguientes"]))
        antes = {i: leer(nodos, i) for i in "ABC"}
        codigo, salida = correr(base, nodos)
        if codigo != 0 or "0 nuevas" not in salida or {i: leer(nodos, i) for i in "ABC"} != antes:
            fallos.append("segunda corrida no es idempotente: %r %r" % (codigo, salida))
        codigo, _ = correr(base + [{"de": "C", "a": "A", "por_que": "cierra"}], nodos)
        if codigo != 1 or {i: leer(nodos, i) for i in "ABC"} != antes:
            fallos.append("el ciclo A->B->C->A no se rechazo o escribio algo")
        codigo, _ = correr([{"de": "A", "a": "Z", "por_que": "Z no existe"}], nodos)
        if codigo != 1:
            fallos.append("la arista a un nodo fuera del pack no se rechazo")
    with tempfile.TemporaryDirectory() as t:
        nodos = os.path.join(t, "nodos")
        os.mkdir(nodos)
        pack(nodos, ["A", "C"])
        codigo, _ = correr([{"de": "C", "a": "A", "por_que": "  "}], nodos)
        if codigo != 1 or leer(nodos, "C")["nodos_siguientes"] != []:
            fallos.append("la arista sin por que no se rechazo")
    if fallos:
        print("ROJO: %d fallos" % len(fallos), *fallos, sep="\n  ")
        sys.exit(1)
    print("VERDE: aristas internas reciprocas, idempotentes y sin ciclos")


if __name__ == "__main__":
    main()
