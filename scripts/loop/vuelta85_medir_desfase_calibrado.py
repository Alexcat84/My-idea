# -*- coding: utf-8 -*-
"""vuelta85_medir_desfase_calibrado.py . TAREA 3.b de la vuelta 85.

POR QUE NACE (acta de la vuelta 84, seccion 4.2 y adjudicacion 6.4): el
reporte de la vuelta 84 afirmo en prosa suelta que "el calibrado queda sin
desfase" cuando en realidad quedaba TRES FILAS por detras del grafo (las tres
aristas de su propia TAREA 3, escritas DESPUES de que el fichero se
recalibrara). La cifra era medible en una linea y no se tallaba: es la misma
especie de caida que la cabecera ya remedia para otras seis filas.

QUE MIDE: cuantas filas de docs/plan/PASO_NODO_CALIBRADO.jsonl tienen el
campo "arista" (True/False) DISTINTO de lo que dice el grafo DE HOY (en las
dos vistas, nodos_siguientes de la madre Y nodos_previos del hijo). El
desfase es ESPERADO y CORRECTO cuando el fichero se commitea "tal como quedo"
tras una escritura posterior a su propia recalibracion (adjudicacion 5.7 del
acta 82): esta medicion no dice si el desfase esta bien o mal, solo lo cuenta
y lo nombra, para que la prosa del reporte no pueda negarlo cuando existe.

USO:
  python scripts/loop/vuelta85_medir_desfase_calibrado.py WORK
  python scripts/loop/vuelta85_medir_desfase_calibrado.py <commit>

Con un commit de git, lee tanto el calibrado como el grafo de ESE commit (los
dos ficheros del mismo arbol, para que la comparacion sea consistente consigo
misma). SALIDA: una linea "DESFASE DEL CALIBRADO RASTREADO: N fila(s)" y, si
N es chico, la lista de pares con su arista guardada y su arista real.
"""
import json
import subprocess
import sys

RUTA_CALIBRADO = "docs/plan/PASO_NODO_CALIBRADO.jsonl"
RUTA_GRAFO = "dataset/metadata/master_graph.json"


def leer_texto(ref, ruta):
    if ref == "WORK":
        with open(ruta, encoding="utf-8") as f:
            return f.read()
    r = subprocess.run(["git", "show", "%s:%s" % (ref, ruta)], capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO: no se pudo leer %s en %s" % (ruta, ref))
    return r.stdout.decode("utf-8")


def cargar_calibrado(ref):
    filas = []
    for linea in leer_texto(ref, RUTA_CALIBRADO).splitlines():
        linea = linea.strip()
        if linea:
            filas.append(json.loads(linea))
    return filas


def cargar_grafo(ref):
    return json.loads(leer_texto(ref, RUTA_GRAFO))["nodos"]


def construir_vecinos(nodos):
    """MISMA DEFINICION que scripts/plan/paso_contra_nodo_calibrado.py (funcion
    vecinos()): union de nodos_siguientes y nodos_previos, resuelta por alias,
    sin contar el propio nodo. "arista" en el calibrado es hijo en
    vecinos(madre) O madre en vecinos(hijo): CONEXION EN CUALQUIER DIRECCION,
    no el chequeo estricto madre->hijo en las dos vistas. Replicar cualquier
    otra definicion mediria un desfase que no es el que el calibrado declara."""
    dep = {k for k, v in nodos.items() if v.get("deprecado")}
    alias = {a: k for k, v in nodos.items() for a in (v.get("ids_alias") or [])}

    def vivo(x):
        if x in nodos and x not in dep:
            return x
        y = alias.get(x)
        return y if y in nodos and y not in dep else None

    cache = {}

    def vecinos(n):
        if n in cache:
            return cache[n]
        out = set()
        for campo in ("nodos_siguientes", "nodos_previos"):
            for y in (nodos.get(n, {}).get(campo) or []):
                r = vivo(y)
                if r and r != n:
                    out.add(r)
        cache[n] = out
        return out

    return vecinos


def main():
    if len(sys.argv) != 2:
        raise SystemExit("uso: vuelta85_medir_desfase_calibrado.py <WORK|commit>")
    ref = sys.argv[1]
    filas = cargar_calibrado(ref)
    nodos = cargar_grafo(ref)
    vecinos = construir_vecinos(nodos)

    desfasadas = []
    for fila in filas:
        guardada = bool(fila.get("arista"))
        real = fila["hijo"] in vecinos(fila["madre"]) or fila["madre"] in vecinos(fila["hijo"])
        if guardada != real:
            desfasadas.append((fila["madre"], fila["hijo"], guardada, real))

    print("REF: %s" % ref)
    print("FILAS EN EL CALIBRADO: %d" % len(filas))
    print("DESFASE DEL CALIBRADO RASTREADO: %d fila(s)" % len(desfasadas))
    for madre, hijo, guardada, real in desfasadas:
        print("  %s -> %s | arista guardada=%s | arista real hoy=%s" % (madre, hijo, guardada, real))


if __name__ == "__main__":
    main()
