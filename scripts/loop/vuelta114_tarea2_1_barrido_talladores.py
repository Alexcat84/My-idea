# -*- coding: utf-8 -*-
r"""vuelta114_tarea2_1_barrido_talladores.py . TAREA 2.1 de la vuelta 114
(encargo del auditor, acta de la vuelta 113, seccion 4.1: "EL BARRIDO QUE
VENIA A CURAR UNA PROMESA DE COMPLETITUD SE EXCLUYE A SI MISMO DEL RECUENTO
SIN DECIRLO EN LA SALIDA"). vuelta113_tarea2_6_barrido_talladores.py es
HISTORIA y NO SE TOCA: este es un fichero NUEVO, de esta vuelta.

QUE CURA. El barrido de la 113 excluia PROPIO_NOMBRE de sus tres busquedas
(legitimo: el fichero cita las tres cadenas literales que busca y se
envenenaria solo, la misma trampa que verificar_apertura_sellada.py ya
documenta) pero la SALIDA nunca decia que habia excluido nada: encabezaba
"cada una con su recuento" y "clasificados TODOS, sin excepcion" sin nombrar
la exclusion. Este fichero repite la MISMA exclusion necesaria (este mismo
script tambien cita "RE_CITA", "LOOP = os.path.join(" y el patron de
extension en su propio texto, y se envenenaria igual sin ella) pero la
publica sin tapujos: imprime el RECUENTO CRUDO (sin excluir nada, este
fichero incluido) Y el RECUENTO NETO (tras la exclusion), mas una seccion
EXCLUSIONES que nombra cada fichero excluido con su motivo.

Como el CRUDO de HOY se mide con este fichero YA EN EL ARBOL (a diferencia
del crudo que corrio el auditor sobre la vuelta 113, medido ANTES de que este
fichero existiera), el crudo de hoy puede diferir del crudo del auditor
exactamente en lo que este fichero mismo aporte. Por eso la comparacion
valida contra el contraste del auditor (RE_CITA 15, txt|md 4, LOOP= 58, union
72) es el NETO (que excluye este fichero), no el crudo de hoy: se imprimen
los dos, con la aclaracion, para que nadie tenga que adivinar cual comparar.

MUTACION Y (TAREA 2.2): con --sin-exclusion, la exclusion de PROPIO_NOMBRE se
desactiva: el crudo y el "neto" salen IGUALES (ninguna exclusion aplicada) y
el fichero antes excluido aparece nombrado en la union. Sirve para probar que
la cura efectivamente cura algo: si la salida fuera igual con y sin
exclusion, la exclusion no estaria haciendo nada.

USO:
  python scripts/loop/vuelta114_tarea2_1_barrido_talladores.py
  python scripts/loop/vuelta114_tarea2_1_barrido_talladores.py --sin-exclusion
"""
import argparse
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP_DIR = os.path.join(RAIZ, "scripts", "loop")

RE_RE_CITA = re.compile(r"RE_CITA")
RE_EXT_PATTERN = re.compile(r"txt\|md")
RE_LOOP_JOIN = re.compile(r"LOOP = os\.path\.join\(")

PROPIO_NOMBRE = os.path.basename(os.path.abspath(__file__))

MOTIVO_PROPIO = ("PROPIO_NOMBRE: este mismo fichero cita, en su docstring y en su "
                  "codigo, las tres cadenas literales que busca (RE_CITA, "
                  "'txt|md', 'LOOP = os.path.join('), asi que sin esta exclusion "
                  "se envenenaria a si mismo en las tres busquedas (misma trampa "
                  "que verificar_apertura_sellada.py ya documenta como 'LA GUARDA "
                  "QUE SE ENVENENA SOLA'). Declarada aqui, con su motivo, EN LA "
                  "PROPIA SALIDA: la caida de la vuelta 113 (acta 113, 4.1) no fue "
                  "excluir, fue callarlo.")


def buscar(patron, excluir):
    hallados = []
    for nombre in sorted(os.listdir(LOOP_DIR)):
        if not nombre.endswith(".py"):
            continue
        if nombre in excluir:
            continue
        ruta = os.path.join(LOOP_DIR, nombre)
        with open(ruta, encoding="utf-8", errors="replace") as f:
            texto = f.read()
        if patron.search(texto):
            hallados.append(nombre)
    return hallados


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sin-exclusion", action="store_true",
                    help="MUTACION Y: desactiva la exclusion de PROPIO_NOMBRE")
    a = ap.parse_args()

    excluir_neto = set() if a.sin_exclusion else {PROPIO_NOMBRE}

    print("BARRIDO TAREA 2.1, VUELTA 114 (publica sus propias exclusiones).")
    if a.sin_exclusion:
        print("MODO --sin-exclusion (MUTACION Y): la exclusion de PROPIO_NOMBRE esta DESACTIVADA.")
    print("=" * 78)
    print()

    resultados = []
    for etiqueta, patron in (
        ("RE_CITA en scripts/loop/*.py", RE_RE_CITA),
        ("patron de extension 'txt|md' entre backticks", RE_EXT_PATTERN),
        ("'LOOP = os.path.join(' en scripts/loop/*.py", RE_LOOP_JOIN),
    ):
        crudo = buscar(patron, excluir=set())
        neto = buscar(patron, excluir=excluir_neto)
        resultados.append((etiqueta, crudo, neto))
        print("%s:" % etiqueta)
        print("   RECUENTO CRUDO (sin excluir nada, este fichero incluido): %d" % len(crudo))
        print("   RECUENTO NETO (tras EXCLUSIONES, ver abajo): %d" % len(neto))
        print()

    union_crudo = sorted(set().union(*[set(c) for _, c, _ in resultados]))
    union_neto = sorted(set().union(*[set(n) for _, _, n in resultados]))
    print("UNION crudo: %d ficheros. UNION neto: %d ficheros." % (len(union_crudo), len(union_neto)))
    print()

    print("--- EXCLUSIONES ---")
    if a.sin_exclusion:
        print("NINGUNA (modo --sin-exclusion): %s permanece en la union, "
              "aunque motivaria la exclusion de arriba." % PROPIO_NOMBRE)
    else:
        print("%s: %s" % (PROPIO_NOMBRE, MOTIVO_PROPIO))
    print()

    print("COMPARABLE AL CONTRASTE DEL AUDITOR (RE_CITA 15, txt|md 4, LOOP= 58, union 72), "
          "medido por el ANTES de que este fichero existiera: el NETO de arriba, no el crudo de hoy")
    print("(el crudo de hoy incluye este mismo fichero, recien creado, y por eso puede diferir).")
    print()

    if a.sin_exclusion:
        iguales = all(len(c) == len(n) for _, c, n in resultados) and union_crudo == union_neto
        print("Crudo == neto: %s (esperado True con --sin-exclusion: ninguna exclusion aplicada)."
              % iguales)
    else:
        distintos = any(len(c) != len(n) for _, c, n in resultados) or union_crudo != union_neto
        print("Crudo != neto en al menos una busqueda: %s (esperado True: la exclusion cura algo)."
              % distintos)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
