# -*- coding: utf-8 -*-
"""vuelta36_barrido_910_b.py - EL BARRIDO DEL 9.10 PARA EL SEGUNDO VOLTEO DE LA VUELTA 36.

SUCESOR DECLARADO de scripts/loop/vuelta36_barrido_910.py, de esta misma vuelta, y
lo que cambia va dicho (EJECUTOR.md regla 2): la maquinaria es la MISMA, linea por
linea, y lo unico que se mueve son LAS CIFRAS DEL MARCADOR VIEJO que hay que cazar
y EL PUESTO que este segundo volteo mueve. Aquel buscaba el marcador de antes del
primer volteo de la vuelta y este busca el que aquel mismo volteo dejo publicado
hace un rato, porque una cifra que esta vuelta escribio hace media hora envejece
igual que una de hace un mes: el banco 9.10 no da plazo de gracia.

  643:  A -> D  (la lectura dirigida LD-82, la sexta y ultima del acto)
  marcador: A 576 -> 575, B 83 (quieto), C 8 (quieto), D 2721 -> 2722

DE SOLO LECTURA. No corrige nada: LISTA. La correccion de cada sitio es de
lectura, porque una cifra con su fecha de corte declarada NO es una tabla
envejecida, y una que se presenta como vigente SI lo es.

NADA SE TRUNCA. Si la lista sale larga, sale larga.

Uso: python scripts/loop/vuelta36_barrido_910_b.py
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Las carpetas de papel. docs/loop queda FUERA a proposito y se dice por que: son
# salidas de instrumento y actas fechadas de vueltas pasadas, y una salida vieja se
# contrasta, no se maquilla.
CARPETAS = [
    os.path.join(RAIZ, "docs"),
    os.path.join(RAIZ, "docs", "plan"),
]

PUESTOS = tuple(int(x) for x in (
    [a for a in sys.argv[1:] if a.isdigit()] or [643]))

# Cifras del marcador viejo de ESTA vuelta. El 8 y el 83 solos son demasiado
# comunes, asi que la vara es: la linea trae el 576 o el 2721/2.721, O trae el
# marcador entero junto.
RE_576 = re.compile(r"\b576\b")
RE_2721 = re.compile(r"\b2[.,]?721\b")
RE_MARCADOR_JUNTO = re.compile(
    r"576\s*[/,|]\s*83\s*[/,|]\s*8\s*[/,|]\s*2[.,]?721"
    r"|A\s*576.{0,10}B\s*83.{0,10}C\s*8.{0,10}D\s*2[.,]?721",
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
    print("BARRIDO DEL BANCO 9.10, vuelta 36 (SEGUNDO VOLTEO): el volteo de %s"
          % ", ".join(str(p) for p in PUESTOS))
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
        es_fuente = rel(ruta) == "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
        for i, linea in enumerate(lineas, 1):
            bajo = linea.lower()
            if not es_fuente:
                junto = RE_MARCADOR_JUNTO.search(linea)
                suelto = (RE_576.search(linea) or RE_2721.search(linea)) and (
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

    print("--- FAMILIA 1: EL MARCADOR VIEJO (A 576, B 83, C 8, D 2721) ---")
    print("  candidatos: %d" % len(marcador))
    for f, i, t in marcador:
        print("  %s:%d" % (f, i))
        print("      %s" % (t[:200] + ("..." if len(t) > 200 else "")))
    print()

    print("--- FAMILIA 2: LOS PUESTOS VOLTEADOS ---")
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
