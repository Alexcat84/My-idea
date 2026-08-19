# -*- coding: utf-8 -*-
"""vuelta37_barrido_910.py - EL BARRIDO DEL 9.10 PARA EL ACTO DE OP-D-04.

SUCESOR DECLARADO de scripts/loop/vuelta36_barrido_910.py. LO QUE CAMBIA VA
DICHO (EJECUTOR.md regla 2), y no es poco:

  1. AQUEL CAZABA UN MARCADOR VIEJO. Este NO, y por un motivo medido: las cuatro
     relecturas de esta vuelta NO CAMBIAN DE CLASE (823, 834 y 844 siguen en A;
     585 sigue en D), asi que el marcador queda EXACTAMENTE donde estaba
     (n 3.388, A 575, B 83, C 8, D 2.722) y ninguna tabla que lo cite envejece.
     Buscar un marcador viejo que no existe seria teatro. Se dice en vez de
     dejar la familia vacia sin explicacion.
  2. LO QUE SI ENVEJECE ES OTRA COSA, y es lo que este barrido caza: TODA TABLA O
     FRASE QUE DESCRIBA brainstorming_divergente COMO UN NODO DE OCHO PASOS O
     COMO COSTURA VIVA. El nodo tiene CUATRO pasos desde el 14 ago 2026 y su
     costura quedo consumada por el corte de OP-F-02, medido hoy en
     scripts/loop/vuelta37_destejido_opd04.py. Una pagina que siga llamandolo
     costura confirmada de ocho pasos es papel que envejece.
  3. Y LA TERCERA FAMILIA es la de siempre: los cuatro puestos releidos, para que
     ninguna tabla derivada cite su razon vieja como vigente.

DE SOLO LECTURA. No corrige nada: LISTA. La correccion de cada sitio es de
lectura, porque una cifra con su fecha de corte declarada NO es una tabla
envejecida, y una que se presenta como vigente SI lo es.

NADA SE TRUNCA. Si la lista sale larga, sale larga.

Uso: python scripts/loop/vuelta37_barrido_910.py
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Las carpetas de papel. docs/loop queda FUERA a proposito y se dice por que: son
# salidas de instrumento y actas fechadas de vueltas pasadas, y una salida vieja
# se contrasta, no se maquilla.
CARPETAS = [
    os.path.join(RAIZ, "docs"),
    os.path.join(RAIZ, "docs", "plan"),
]

PUESTOS = (585, 823, 834, 844)
NODO = "brainstorming_divergente"

# FAMILIA 2: el nodo descrito como de OCHO pasos o como costura viva.
RE_OCHO = re.compile(r"\b(ocho|8)\b", re.IGNORECASE)
RE_COSTURA = re.compile(r"costura", re.IGNORECASE)
RE_JUNTURA = re.compile(r"juntura|1 a 4 / 5 a 8|5 a 8", re.IGNORECASE)


def ficheros():
    vistos = set()
    for carpeta in CARPETAS:
        if not os.path.isdir(carpeta):
            continue
        for nombre in sorted(os.listdir(carpeta)):
            ruta = os.path.join(carpeta, nombre)
            if not os.path.isfile(ruta):
                continue
            if not (nombre.endswith(".md") or nombre.endswith(".jsonl")):
                continue
            if ruta in vistos:
                continue
            vistos.add(ruta)
            yield ruta


def rel(ruta):
    return os.path.relpath(ruta, RAIZ).replace("\\", "/")


def main():
    print("=" * 78)
    print("BARRIDO DEL BANCO 9.10, vuelta 37: el acto de OP-D-04")
    print("=" * 78)
    print("")
    print("EL MARCADOR NO SE BUSCA, y aqui esta el motivo medido: las cuatro")
    print("relecturas de esta vuelta NO cambian de clase, asi que n, A, B, C y D")
    print("quedan donde estaban y ninguna tabla que los cite envejece por esto.")
    print("")

    nodo_viejo = []
    puestos = dict((p, []) for p in PUESTOS)

    for ruta in ficheros():
        try:
            lineas = open(ruta, encoding="utf-8").read().splitlines()
        except UnicodeDecodeError:
            print("NO SE PUDO LEER (codificacion): %s" % rel(ruta))
            continue
        es_fuente = rel(ruta) == "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
        for i, linea in enumerate(lineas, 1):
            bajo = linea.lower()
            if NODO in linea and not es_fuente:
                if RE_OCHO.search(linea) or RE_COSTURA.search(linea) or RE_JUNTURA.search(linea):
                    nodo_viejo.append((rel(ruta), i, linea.strip()))
            for p in PUESTOS:
                if re.search(r"\b%d\b" % p, linea) and (
                    "puesto" in bajo or "veredicto" in bajo or "|" in linea
                    or "congelad" in bajo
                ):
                    puestos[p].append((rel(ruta), i, linea.strip()))

    print("--- FAMILIA 1: %s DESCRITO COMO DE OCHO PASOS O COMO COSTURA VIVA ---" % NODO)
    print("  candidatos: %d" % len(nodo_viejo))
    for f, i, t in nodo_viejo:
        print("  %s:%d" % (f, i))
        print("      %s" % (t[:220] + ("..." if len(t) > 220 else "")))
    print("")

    print("--- FAMILIA 2: LOS CUATRO PUESTOS RELEIDOS ---")
    for p in PUESTOS:
        print("  PUESTO %d: %d candidatos" % (p, len(puestos[p])))
        for f, i, t in puestos[p]:
            print("    %s:%d" % (f, i))
            print("        %s" % (t[:220] + ("..." if len(t) > 220 else "")))
        print("")

    total = len(nodo_viejo) + sum(len(v) for v in puestos.values())
    print("=" * 78)
    print("CANDIDATOS TOTALES: %d. Ninguno se oculta y ninguno se corrige aqui:" % total)
    print("este instrumento LISTA, y la adjudicacion de cada sitio es de lectura.")
    print("LIMITE DECLARADO: es una busqueda lexica. Una pagina puede describir el")
    print("nodo con otras palabras y este barrido no la veria; y una descripcion")
    print("con su fecha de corte declarada aparece aqui sin estar envejecida.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
