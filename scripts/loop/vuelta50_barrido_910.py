# -*- coding: utf-8 -*-
"""vuelta50_barrido_910.py

SUCESOR DECLARADO de scripts/loop/vuelta49_barrido_910.py, al que NO reemplaza.

POR QUE NACE, y el motivo esta MEDIDO en esta misma vuelta antes de escribir una
linea: el instrumento de la vuelta 49 acepta --viejo pero NO LO USA PARA BUSCAR.
Sus dos expresiones regulares estan clavadas a 583 y a 2709 (las cifras del
marcador de la vuelta 14) y el argumento --viejo solo cambia la CABECERA que se
imprime. Corrido hoy con --viejo 574,77,8,2729 devuelve 22 candidatos de la
familia 1, y los devuelve porque esas celdas arrastran el 583 en su cadena de
tachados, NO porque el barrido sepa buscar el 574. Una celda NUEVA escrita hoy
con la cifra vigente y sin cadena de tachados seria INVISIBLE para aquel
instrumento. Esa es exactamente la especie de la caida de la vuelta 49 (acta 49
seccion 3), y un barrido que no ve la cifra que se le pide es un barrido que
tranquiliza sin mirar.

LO QUE CAMBIA, y es lo unico:
  1. --viejo AHORA BUSCA DE VERDAD. Las cifras A y D que se le pasen se compilan
     a expresion regular (con punto o coma de millar opcional) y se buscan con la
     MISMA vara del instrumento anterior: la linea trae la cifra Y ademas es fila
     de tabla o dice una palabra del marcador.
  2. LA FAMILIA LEGADO SE QUEDA. El 583 y el 2709 se siguen barriendo aparte,
     porque las cadenas de tachado historicas los llevan y son el rastro que
     encuentra las tablas viejas del catalogo.
  3. --retrato barre las dos cifras del RETRATO DE LAS A (colapsos a auto-arista
     y pares distintos tras resolver), que son las que la vuelta 49 dejo atras
     junto al marcador y que ningun barrido anterior miraba.

LAS DOS VARAS Y EL LIMITE DECLARADO SON LOS MISMOS, palabra por palabra: este
instrumento LISTA y no corrige, nada se trunca, y una cifra con su fecha de corte
declarada aparece aqui SIN estar envejecida. La separacion entre lo vigente y el
estado de un dia es de LECTURA y este instrumento no la finge.

Uso:
  python scripts/loop/vuelta50_barrido_910.py --viejo 574,77,8,2729 \
      --retrato 41,533 --puestos 305

El docstring del instrumento del que este desciende sigue entero debajo, porque
explica la vara:

vuelta49_barrido_910.py

SUCESOR DECLARADO de scripts/loop/vuelta33_barrido_910.py, al que NO reemplaza.
Lo unico que cambia son las CIFRAS DEL MARCADOR VIEJO, que alli estaban clavadas
a 583/89/7/2709 y aqui se pasan por linea de comandos, y el juego de puestos por
defecto. La logica de busqueda, sus dos varas y su LIMITE DECLARADO son los
mismos, palabra por palabra, para que las dos corridas sigan siendo comparables.

vuelta33_barrido_910.py

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
"""
import argparse
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

_ap = argparse.ArgumentParser()
_ap.add_argument("--viejo", default="574,77,8,2729",
                 help="las cuatro cifras del marcador VIEJO: A,B,C,D. AHORA SE BUSCAN.")
_ap.add_argument("--retrato", default="",
                 help="las dos cifras VIEJAS del retrato de las A: colapsos,pares")
_ap.add_argument("--puestos", default="305")
_ARGS = _ap.parse_args()
_A, _B, _C, _D = (int(x) for x in _ARGS.viejo.split(","))
PUESTOS = tuple(int(p) for p in _ARGS.puestos.split(",")) if _ARGS.puestos else ()
RETRATO = tuple(int(x) for x in _ARGS.retrato.split(",")) if _ARGS.retrato else ()


def re_cifra(n):
    """La cifra con punto o coma de millar OPCIONAL, como entero suelto."""
    s = str(n)
    if len(s) > 3:
        cabeza, cola = s[:-3], s[-3:]
        return re.compile(r"\b%s[.,]?%s\b" % (re.escape(cabeza), re.escape(cola)))
    return re.compile(r"\b%s\b" % re.escape(s))


# FAMILIA 1: las cifras que se le pasan por --viejo. La vara es la del instrumento
# anterior: A y D son las distintivas; B y C solos son demasiado comunes para
# buscarlos sueltos, y se buscan SOLO dentro del patron junto.
RE_VIEJO_A = re_cifra(_A)
RE_VIEJO_D = re_cifra(_D)
RE_VIEJO_JUNTO = re.compile(
    r"%d\s*[/,|]\s*%d\s*[/,|]\s*%d\s*[/,|]\s*%s"
    % (_A, _B, _C, re_cifra(_D).pattern.replace(r"\b", "")),
    re.IGNORECASE,
)

# FAMILIA LEGADO: el marcador de la vuelta 14, que vive en las cadenas de tachado.
RE_583 = re.compile(r"\b583\b")
RE_2709 = re.compile(r"\b2[.,]?709\b")
RE_LEGADO_JUNTO = re.compile(
    r"583\s*[/,|]\s*89\s*[/,|]\s*7\s*[/,|]\s*2[.,]?709"
    r"|A\s*583.{0,10}B\s*89.{0,10}C\s*7.{0,10}D\s*2[.,]?709",
    re.IGNORECASE,
)

PALABRAS_MARCADOR = ("marcador", "tasa de a", "clase", "clases", "a crudas",
                     "total de a", "veredicto", "a / b / c / d", "abcd")
PALABRAS_RETRATO = ("retrato", "auto-arista", "auto arista", "colapsa", "colapsan",
                    "pares distintos", "resolver", "a vigentes")


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


def imprimir(titulo, filas):
    print("--- %s ---" % titulo)
    print("  candidatos: %d" % len(filas))
    for f, i, t in filas:
        print("  %s:%d" % (f, i))
        print("      %s" % (t[:220] + ("..." if len(t) > 220 else "")))
    print()


def main():
    print("=" * 78)
    print("BARRIDO DEL BANCO 9.10, vuelta 50 (sucesor: --viejo AHORA BUSCA)")
    print("marcador viejo buscado: A %d B %d C %d D %d" % (_A, _B, _C, _D))
    print("retrato viejo buscado : %s"
          % (", ".join(str(x) for x in RETRATO) or "(ninguno)"))
    print("puestos corregidos    : %s"
          % (", ".join(str(p) for p in PUESTOS) or "(ninguno)"))
    print("=" * 78)
    print()

    fam_viejo, fam_legado, fam_retrato = [], [], []
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
            fila_o_palabra_m = (any(w in bajo for w in PALABRAS_MARCADOR)
                                or linea.lstrip().startswith("|"))
            if not es_fuente:
                if RE_VIEJO_JUNTO.search(linea) or (
                        (RE_VIEJO_A.search(linea) or RE_VIEJO_D.search(linea))
                        and fila_o_palabra_m):
                    fam_viejo.append((rel(ruta), i, linea.strip()))
                if RE_LEGADO_JUNTO.search(linea) or (
                        (RE_583.search(linea) or RE_2709.search(linea))
                        and fila_o_palabra_m):
                    fam_legado.append((rel(ruta), i, linea.strip()))
                if RETRATO:
                    fila_o_palabra_r = (any(w in bajo for w in PALABRAS_RETRATO)
                                        or linea.lstrip().startswith("|"))
                    if fila_o_palabra_r and any(
                            re_cifra(n).search(linea) for n in RETRATO):
                        fam_retrato.append((rel(ruta), i, linea.strip()))
            for p in PUESTOS:
                if re.search(r"\b%d\b" % p, linea) and (
                    "puesto" in bajo or "veredicto" in bajo or "|" in linea
                    or "congelad" in bajo
                ):
                    puestos[p].append((rel(ruta), i, linea.strip()))

    imprimir("FAMILIA 1: EL MARCADOR VIEJO QUE SE PIDIO (A %d, D %d)" % (_A, _D),
             fam_viejo)
    imprimir("FAMILIA LEGADO: EL MARCADOR DE LA VUELTA 14 (583 / 2.709)", fam_legado)
    if RETRATO:
        imprimir("FAMILIA RETRATO: LAS CIFRAS VIEJAS DEL RETRATO DE LAS A (%s)"
                 % ", ".join(str(x) for x in RETRATO), fam_retrato)

    print("--- FAMILIA 2: LOS PUESTOS CORREGIDOS ---")
    for p in PUESTOS:
        print("  PUESTO %d: %d candidatos" % (p, len(puestos[p])))
        for f, i, t in puestos[p]:
            print("    %s:%d" % (f, i))
            print("        %s" % (t[:220] + ("..." if len(t) > 220 else "")))
        print()

    total = (len(fam_viejo) + len(fam_legado) + len(fam_retrato)
             + sum(len(v) for v in puestos.values()))
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
