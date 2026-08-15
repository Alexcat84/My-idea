# -*- coding: utf-8 -*-
"""vuelta33_barrido_910.py

EL BARRIDO QUE EL BANCO 9.10 EXIGE EN EL MISMO ACTO DEL VOLTEO: toda tabla que
cita un veredicto por numero se recomputa del archivo, y todo volteo en bloque
barre las tablas derivadas EN EL MISMO ACTO, no despues.

Barre buscando DOS familias de cita, y las dos van con su contexto para que la
adjudicacion sea de lectura y no de conteo:

  1. EL MARCADOR VIEJO: las cifras A 583, B 89, C 7, D 2709 (con punto de millar o
     sin el) en lineas que ademas hablan de marcador, de clases o de tasa de A.
  2. LOS TRES PUESTOS VOLTEADOS: 494, 592 y 830 citados como numero de veredicto.

DE SOLO LECTURA. No corrige nada: LISTA. La correccion de cada sitio es de
lectura, porque una cifra con su fecha de corte declarada NO es una tabla
envejecida, y una que se presenta como vigente SI lo es. Esa diferencia no la
sabe una expresion regular, y por eso este instrumento no la finge: imprime todo
lo que encuentra, con su linea, y no oculta nada bajo un tope.

NADA SE TRUNCA. Si la lista sale larga, sale larga.

Uso: python scripts/loop/vuelta33_barrido_910.py
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Las carpetas de papel. docs/loop queda FUERA a proposito y se dice por que: son
# salidas de instrumento y actas fechadas de vueltas pasadas, y una salida vieja se
# contrasta, no se maquilla. El REPORTE.md de la vuelta lo reescribe la vuelta.
CARPETAS = [
    os.path.join(RAIZ, "docs"),
    os.path.join(RAIZ, "docs", "plan"),
]

PUESTOS = (494, 592, 830)

# Cifras del marcador viejo. El 7 y el 89 solos son demasiado comunes para buscarlos
# sueltos, asi que la vara es: la linea trae el 583 o el 2709/2.709, O trae dos o mas
# de las cuatro cifras del marcador juntas.
RE_583 = re.compile(r"\b583\b")
RE_2709 = re.compile(r"\b2[.,]?709\b")
RE_MARCADOR_JUNTO = re.compile(
    r"583\s*[/,|]\s*89\s*[/,|]\s*7\s*[/,|]\s*2[.,]?709"
    r"|A\s*583.{0,10}B\s*89.{0,10}C\s*7.{0,10}D\s*2[.,]?709",
    re.IGNORECASE,
)
PALABRAS_MARCADOR = ("marcador", "tasa de a", "clase", "clases", "a crudas",
                     "total de a", "veredicto", "a / b / c / d", "abcd")


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
    print("BARRIDO DEL BANCO 9.10, vuelta 33: el volteo de 494, 592 y 830")
    print("=" * 78)
    print()

    marcador = []
    puestos = {p: [] for p in PUESTOS}

    for ruta in ficheros():
        try:
            lineas = open(ruta, encoding="utf-8").read().splitlines()
        except UnicodeDecodeError:
            print("NO SE PUDO LEER (codificacion): %s" % rel(ruta))
            continue
        # El propio archivo de veredictos no es una tabla derivada: es LA fuente.
        es_fuente = rel(ruta) == "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
        for i, linea in enumerate(lineas, 1):
            bajo = linea.lower()
            if not es_fuente:
                junto = RE_MARCADOR_JUNTO.search(linea)
                # La vara suelta se abre a las FILAS DE TABLA (la linea empieza por
                # barra) ademas de a las palabras del marcador. Motivo medido en esta
                # misma vuelta: la tabla del marcador de INTRA_DOMINIO_INFORME.md
                # escribe la fila como '| **A** | **583** (17,2 %) |', sin ninguna de
                # las palabras, y la primera version de este barrido no la veia. Una
                # tabla derivada que el barrido de tablas derivadas no ve es
                # exactamente la averia que el banco 9.10 nombra.
                suelto = (RE_583.search(linea) or RE_2709.search(linea)) and (
                    any(w in bajo for w in PALABRAS_MARCADOR)
                    or linea.lstrip().startswith("|")
                )
                if junto or suelto:
                    marcador.append((rel(ruta), i, linea.strip()))
            for p in PUESTOS:
                if re.search(r"\b%d\b" % p, linea) and (
                    "puesto" in bajo or "veredicto" in bajo or "|" in linea
                    or "congelad" in bajo
                ):
                    puestos[p].append((rel(ruta), i, linea.strip()))

    print("--- FAMILIA 1: EL MARCADOR VIEJO (A 583, B 89, C 7, D 2709) ---")
    print("  candidatos: %d" % len(marcador))
    for f, i, t in marcador:
        print("  %s:%d" % (f, i))
        print("      %s" % (t[:200] + ("..." if len(t) > 200 else "")))
    print()

    print("--- FAMILIA 2: LOS TRES PUESTOS VOLTEADOS ---")
    for p in PUESTOS:
        print("  PUESTO %d: %d candidatos" % (p, len(puestos[p])))
        for f, i, t in puestos[p]:
            print("    %s:%d" % (f, i))
            print("        %s" % (t[:200] + ("..." if len(t) > 200 else "")))
        print()

    total = len(marcador) + sum(len(v) for v in puestos.values())
    print("=" * 78)
    print("CANDIDATOS TOTALES: %d. Ninguno se oculta y ninguno se corrige aqui:" % total)
    print("este instrumento LISTA, y la adjudicacion de cada sitio es de lectura.")
    print("LIMITE DECLARADO: es una busqueda lexica. Una tabla puede citar el")
    print("marcador con otras palabras y este barrido no la veria; y una cifra con")
    print("su fecha de corte declarada aparece aqui sin estar envejecida.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
