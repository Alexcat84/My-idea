# -*- coding: utf-8 -*-
"""vuelta54_correcciones_910.py . LAS CELDAS QUE EL BARRIDO 9.10 DEL CIERRE DE
LA VUELTA 54 ENCONTRO ENVEJECIDAS, CORREGIDAS CON TACHADO, CONTADOR CUADRADO Y
NOTA FECHADA.

LA REGLA QUE LO MANDA (regla operativa del cierre, acta de la vuelta 49; `D7`
de la vuelta 50): quien mueve una clase o funde un acto corre el barrido 9.10
ANTES de cerrar, y quien corrige una celda con contador CUADRA EL CONTADOR y
ADOSA la nota fechada. Ninguna nota vieja se reescribe.

QUE SE MUEVE Y QUE NO, medido y dicho:

  NO SE MUEVE EL MARCADOR. Esta vuelta NO volteo ni un veredicto: los 21 actos
  que fundio son de FUSION PURA y ninguno fabrico colision, asi que `P.16` no
  tuvo nada que limpiar. `A 551, B 73, C 6, D 2.758` al abrir y al cerrar,
  medido las dos veces (`../loop/SALIDA_V54_MARCADOR_APERTURA.txt` y
  `../loop/SALIDA_V54_MARCADOR_CIERRE.txt`). Y POR LO MISMO NO SE MUEVE NINGUNA
  DE LAS DOS TABLAS POR DOMINIO HERMANAS: la `A` de cada uno de los diez
  dominios es la misma al digito. La hermandad de la TAREA 1.1 de la vuelta 53
  se cumple POR VACIO y se dice asi en vez de darla por cumplida.

  SI SE MUEVE EL RETRATO, y es la huella de la cirugia que la propia fila ya
  explica: cada acto fundido convierte su par `A` interno en un par cuyos dos
  ids resuelven al mismo nodo vivo. VEINTIUN actos fundidos, VEINTIUN colapsos
  mas (72 a 93) y VEINTIUN pares distintos menos (479 a 458).

IDEMPOTENTE: cada sustitucion comprueba primero si su resultado ya esta
escrito. Re-correrlo no duplica ninguna nota.

Uso: python scripts/loop/vuelta54_correcciones_910.py [--simular]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REC = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")

NOTA_247 = (
    " [OCTAVA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 54, barrido "
    "`9.10` del cierre): de 72 a 93, VEINTIUN colapsos mas, UNO POR CADA ACTO QUE ESTA VUELTA "
    "FUNDIO (once en el lote A y diez en el lote B del tramo 2), por el mismo motivo que las "
    "correcciones anteriores. Medido HOY con `python scripts/plan/recomputo_3388.py` y `python "
    "scripts/recomputar_marcador.py 3388` DESPUES del ultimo movimiento de la vuelta 54 "
    "(`../loop/SALIDA_V54_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V54_MARCADOR_CIERRE.txt`), "
    "paso 1]")

NOTA_248 = (
    " [UNDECIMA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 54, barrido "
    "`9.10` del cierre): de 479 a 458, que vuelve a ser la resta exacta de las dos filas de "
    "arriba (551 crudas menos 93 colapsos). LA FILA DE LAS CRUDAS NO SE MUEVE, y se dice: esta "
    "vuelta no volteo ningun veredicto, asi que la `A` global es la misma al abrir y al cerrar. "
    "Medido HOY con `python scripts/plan/recomputo_3388.py` y `python "
    "scripts/recomputar_marcador.py 3388` DESPUES del ultimo movimiento de la vuelta 54 "
    "(`../loop/SALIDA_V54_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V54_MARCADOR_CIERRE.txt`), "
    "paso 1]")

NOTA_528 = (
    " **[RE-CORRIDO EL 20 ago 2026 (vuelta 54, barrido `9.10` del cierre): SIGUE OK, ahora con "
    "458 y 458, y las dos mitades se recomputaron por separado, no se copio una en la otra. "
    "Medido HOY DESPUES del ultimo movimiento de la vuelta 54 "
    "(`../loop/SALIDA_V54_RECOMPUTO_CIERRE.txt`, bloque LAS CUATRO COMPROBACIONES, donde las "
    "cuatro salen OK)]**")

CAMBIOS = [
    ("247 colapsos, la cifra y su cadena",
     "~~**57**~~ ~~**60**~~ **72** **[CORREGIDA ~~CUATRO~~ ~~CINCO~~ ~~SEIS~~ SIETE VECES",
     "~~**57**~~ ~~**60**~~ ~~**72**~~ **93** **[CORREGIDA ~~CUATRO~~ ~~CINCO~~ ~~SEIS~~ ~~SIETE~~ OCHO VECES"),
    ("247 la nota octava, adosada al final de la celda",
     "(`../loop/SALIDA_V53_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V53_MARCADOR_CIERRE.txt`), "
     "paso 1]** |\n| pares distintos en el retrato",
     "(`../loop/SALIDA_V53_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V53_MARCADOR_CIERRE.txt`), "
     "paso 1]" + NOTA_247 + "** |\n| pares distintos en el retrato"),
    ("248 pares distintos, la cifra y su cadena",
     "~~**509**~~ ~~**503**~~ **479** **[CORREGIDA ~~SIETE~~ ~~OCHO~~ ~~NUEVE~~ DIEZ VECES",
     "~~**509**~~ ~~**503**~~ ~~**479**~~ **458** **[CORREGIDA ~~SIETE~~ ~~OCHO~~ ~~NUEVE~~ ~~DIEZ~~ ONCE VECES"),
    ("248 la nota undecima, adosada al final de la celda",
     "(551 crudas menos 72 colapsos). Medido HOY con `python scripts/plan/recomputo_3388.py` y "
     "`python scripts/recomputar_marcador.py 3388` DESPUES del ultimo movimiento de la vuelta 53 "
     "(`../loop/SALIDA_V53_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V53_MARCADOR_CIERRE.txt`), "
     "paso 1]** |",
     "(551 crudas menos 72 colapsos). Medido HOY con `python scripts/plan/recomputo_3388.py` y "
     "`python scripts/recomputar_marcador.py 3388` DESPUES del ultimo movimiento de la vuelta 53 "
     "(`../loop/SALIDA_V53_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V53_MARCADOR_CIERRE.txt`), "
     "paso 1]" + NOTA_248 + "** |"),
    ("528 el checkpoint ii, sus dos parentesis",
     "~~509~~ ~~503~~ **479**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ "
     "~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ ~~503~~ **479**)",
     "~~509~~ ~~503~~ ~~479~~ **458**) == suma de aristas A internas de las componentes (~~583~~ "
     "~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ ~~503~~ ~~479~~ **458**)"),
    ("528 la nota del re-corrido de la vuelta 54",
     "bloque LAS CUATRO COMPROBACIONES, donde las cuatro salen OK]** |",
     "bloque LAS CUATRO COMPROBACIONES, donde las cuatro salen OK]**" + NOTA_528 + " |"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("LAS CORRECCIONES DEL BARRIDO 9.10 DEL CIERRE DE LA VUELTA 54")
    print("modo: %s" % ("SIMULACION, no escribe" if a.simular else "ESCRITURA"))
    print("=" * 78)
    print()

    t = io.open(REC, encoding="utf-8").read()
    hechas = saltadas = 0
    for etiqueta, viejo, nuevo in CAMBIOS:
        if nuevo in t:
            print("  YA ESTABA   %-52s (idempotente)" % etiqueta)
            saltadas += 1
            continue
        c = t.count(viejo)
        if c != 1:
            print("  ROJO        %-52s el texto viejo aparece %d veces" % (etiqueta, c))
            return 1
        t = t.replace(viejo, nuevo, 1)
        print("  HECHA       %-52s" % etiqueta)
        hechas += 1

    if not a.simular:
        io.open(REC, "w", encoding="utf-8", newline=chr(10)).write(t)

    print()
    print("  celdas corregidas: %d | ya estaban: %d" % (hechas, saltadas))
    print("  fichero: docs/plan/RECOMPUTO_3388.md")
    print()
    print("  LAS DOS TABLAS POR DOMINIO NO SE TOCAN, y no es un olvido: la A de cada")
    print("  uno de los diez dominios es la misma al abrir y al cerrar, porque esta")
    print("  vuelta no volteo ni un veredicto. La hermandad se cumple POR VACIO.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
