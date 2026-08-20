# -*- coding: utf-8 -*-
"""vuelta58_correcciones_910.py . EL BARRIDO 9.10 DEL CIERRE DE LA VUELTA 58:
LAS CELDAS VIGENTES QUE ESTA VUELTA MOVIO, CORREGIDAS CON TACHADO Y CONTADOR.

SUCESOR DECLARADO de scripts/loop/vuelta57_correcciones_910.py en su maquina:
ANCLA LITERAL UNICA (rojo si falta o se repite), TACHADO que conserva la cifra
vieja, CONTADOR de la celda cuadrado, y NOTA FECHADA dentro de la propia celda.
IDEMPOTENTE: la segunda corrida dice YA ESTABA y no escribe.

QUE MUEVE ESTA VUELTA, y por que son estas tres celdas y no mas: la TAREA 1.1
DESHIZO el acto 32 del tramo 4, y deshacer una fusion pura mueve el RETRATO pero
NO el marcador. Medido: colapsos 208 a 207, pares distintos 343 a 344, y el
checkpoint ii de 343 a 344 en sus dos parentesis. EL MARCADOR NO SE TOCA Y NO ES
UN OLVIDO: esta vuelta no volteo ni un solo veredicto (el diff del archivo de
veredictos contra la apertura es VACIO), asi que las filas del marcador del
informe y sus dos tablas por dominio hermanas se cumplen POR VACIO.

Y LA CELDA QUE NO SE TOCA, con su motivo escrito: la seccion PASO 3 de
RECOMPUTO_3388.md publica su corte con todas sus letras en su propia linea 379
(calculado sobre el retrato del paso 1, las 583 A resueltas). Es el LIMITE
DECLARADO del 9.10 y el acta 57 ya lo adjudico A FAVOR (discutible D6). No se
corrige, y se dice.

MODOS: --simular (por defecto) y --ejecutar.

Uso: python scripts/loop/vuelta58_correcciones_910.py [--ejecutar]
"""
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = "docs/plan/RECOMPUTO_3388.md"

FECHA = "20 ago 2026"
NOTA = ("Medido HOY con `python scripts/plan/recomputo_3388.py` DESPUES del ultimo "
        "movimiento de la vuelta 58, que fue DESHACER EL ACTO 32 del tramo 4 por la "
        "relectura conjunta que el acta 57 encargo "
        "(`../loop/SALIDA_V58_RECOMPUTO_CIERRE.txt`). Deshacer una fusion pura mueve "
        "el retrato y NO el marcador: esta vuelta no volteo ni un veredicto")

# (etiqueta, viejo, nuevo, contador viejo, contador nuevo)
CELDAS = [
    ("colapsos (linea 247)", "208", "207", "ONCE", "DOCE"),
    ("pares distintos (linea 248)", "343", "344", "CATORCE", "QUINCE"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("BARRIDO 9.10 DEL CIERRE, VUELTA 58 . MODO %s"
          % ("EJECUTAR" if a.ejecutar else "SIMULAR"))
    print("=" * 78)
    print()

    crudo = io.open(os.path.join(RAIZ, PAGINA), encoding="utf-8", newline="").read()
    fin = "\r\n" if crudo.count("\r\n") > crudo.count("\n") // 2 else "\n"
    L = crudo.replace("\r\n", "\n").split("\n")
    print("  %s: final de linea %s, %d lineas"
          % (PAGINA, "CRLF" if fin == "\r\n" else "LF", len(L)))
    print()

    hechos, ya, malos = [], [], []

    def celda_del(clave):
        hall = [i for i, l in enumerate(L) if l.startswith(clave)]
        return (hall[0] if len(hall) == 1 else None), len(hall)

    # --- 247 y 248: la cifra vigente pasa a tachada y entra la nueva ---
    for etiqueta, viejo, nuevo, cont_v, cont_n in CELDAS:
        clave = ("| de esas, colapsan a auto-arista al resolver"
                 if "colapsos" in etiqueta
                 else "| pares distintos en el retrato tras resolver y deduplicar")
        k, cuantas = celda_del(clave)
        if k is None:
            malos.append("%s: la celda aparece %d veces" % (etiqueta, cuantas))
            print("  ROJO        %s: aparece %d veces" % (etiqueta, cuantas))
            continue
        if ("**%s**" % nuevo) in L[k] and ("~~**%s**~~" % viejo) in L[k]:
            ya.append(etiqueta)
            print("  YA ESTABA   %s" % etiqueta)
            continue
        linea = L[k]
        # la cifra VIGENTE es la ultima **N** que no esta tachada
        marca_v = "**%s**" % viejo
        if ("~~%s~~" % marca_v) in linea or marca_v not in linea:
            malos.append("%s: no se encontro la cifra vigente %s sin tachar"
                         % (etiqueta, viejo))
            print("  ROJO        %s: no hay %s vigente" % (etiqueta, viejo))
            continue
        linea = linea.replace(marca_v, "~~%s~~ **%s**" % (marca_v, nuevo), 1)
        if cont_v in linea:
            linea = linea.replace(cont_v, "~~%s~~ %s" % (cont_v, cont_n), 1)
        else:
            malos.append("%s: no se encontro el contador %s" % (etiqueta, cont_v))
            print("  ROJO        %s: sin contador %s" % (etiqueta, cont_v))
            continue
        # la nota fechada entra dentro de la propia celda, antes del cierre
        linea = linea.replace("]** |", ". CORRECCION DE LA VUELTA 58 (%s): %s]** |"
                              % (FECHA, NOTA), 1)
        L[k] = linea
        hechos.append(etiqueta)
        print("  ESCRIBE     %s: %s a %s, contador %s a %s"
              % (etiqueta, viejo, nuevo, cont_v, cont_n))

    # --- 528: el checkpoint ii, en sus DOS parentesis ---
    k, cuantas = celda_del("| **ii** | A vigentes resueltas del retrato")
    if k is None:
        malos.append("checkpoint ii: la celda aparece %d veces" % cuantas)
        print("  ROJO        checkpoint ii: aparece %d veces" % cuantas)
    elif "**344**" in L[k] and "~~**343**~~" in L[k]:
        ya.append("checkpoint ii (linea 528)")
        print("  YA ESTABA   checkpoint ii (linea 528)")
    else:
        linea = L[k]
        n = linea.count("**343**")
        if n != 2:
            malos.append("checkpoint ii: se esperaban 2 parentesis con 343 y hay %d" % n)
            print("  ROJO        checkpoint ii: %d parentesis con 343, no 2" % n)
        else:
            linea = linea.replace("**343**", "~~**343**~~ **344**")
            linea = linea.replace("]** |", ". CORRECCION DE LA VUELTA 58 (%s): %s, "
                                           "y la comprobacion `i` pasa de 441 a 443]** |"
                                  % (FECHA, NOTA), 1)
            L[k] = linea
            hechos.append("checkpoint ii (linea 528)")
            print("  ESCRIBE     checkpoint ii: 343 a 344 en los DOS parentesis")

    print()
    if malos:
        print("  ROJO, %d fallos y NO se escribe nada:" % len(malos))
        for m in malos:
            print("     %s" % m)
        return 1
    print("  resumen: %d a escribir, %d YA ESTABAN" % (len(hechos), len(ya)))
    print()
    if not a.ejecutar:
        print("  MODO SIMULAR: no se escribe nada.")
        print("FIN")
        return 0
    if not hechos:
        print("  nada que escribir: los %d sitios YA ESTABAN. Idempotente." % len(ya))
        print("FIN")
        return 0
    io.open(os.path.join(RAIZ, PAGINA), "w", encoding="utf-8", newline="").write(
        fin.join(L))
    print("  escrito: %s" % PAGINA)
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
