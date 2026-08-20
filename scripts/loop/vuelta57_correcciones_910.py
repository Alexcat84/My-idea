# -*- coding: utf-8 -*-
"""vuelta57_correcciones_910.py . LAS CELDAS QUE EL BARRIDO 9.10 DEL CIERRE DE
LA VUELTA 57 ENCONTRO ENVEJECIDAS, CORREGIDAS CON TACHADO, CONTADOR CUADRADO Y
NOTA FECHADA.

LA REGLA QUE LO MANDA (regla operativa del cierre, acta de la vuelta 49; `D7`
de la vuelta 50): quien mueve una clase o funde un acto corre el barrido 9.10
ANTES de cerrar, y quien corrige una celda con contador CUADRA EL CONTADOR y
ADOSA la nota fechada. Ninguna nota vieja se reescribe.

QUE SE MUEVE Y QUE NO, medido y dicho:

  EL MARCADOR NO SE MUEVE, Y NO ES UN OLVIDO. Esta vuelta NO volteo ni un solo
  veredicto: las colisiones esperadas del tramo 4 entero salieron CERO sobre
  cien combinaciones simuladas, asi que no hubo relectura de filo que hacer y
  `P.16` no tuvo nada que limpiar. `A` sigue en 551, `B` en 72, `C` en 5 y `D`
  en 2.760, medido las dos veces (`../loop/SALIDA_V57_MARCADOR_APERTURA.txt` y
  `../loop/SALIDA_V57_MARCADOR_CIERRE.txt`). POR ESO LAS FILAS DEL MARCADOR DEL
  INFORME Y LAS DOS TABLAS POR DOMINIO HERMANAS NO SE TOCAN: la hermandad se
  cumple POR VACIO y se dice asi en vez de darse por cumplida.

  SI SE MUEVE EL RETRATO, y es la huella de la cirugia que la propia fila ya
  explica: cada acto fundido convierte su par `A` interno en un par cuyos dos
  ids resuelven al mismo nodo vivo. CUARENTA Y CUATRO colapsos mas (164 a 208)
  y CUARENTA Y CUATRO pares distintos menos (387 a 343), UNO POR CADA ACTO QUE
  ESTA VUELTA FUNDIO (catorce en el lote A, catorce en el B y dieciseis en el
  C). La resta sigue exacta: 551 crudas menos 208 colapsos son 343.

  LO QUE NO SE TOCA Y SE DICE POR QUE: la seccion PASO 3 de `RECOMPUTO_3388.md`
  publica 852 nodos con `A` y 334 componentes, y hoy el instrumento da otras
  cifras. NO se corrige, y el motivo esta escrito en la propia seccion: dice
  literalmente que esta *calculado sobre el retrato del paso 1 (las 583 A
  resueltas)*, o sea que es EL RETRATO DE UN DIA CON SU CORTE DECLARADO, y una
  cifra con su corte declarado no es una tabla envejecida. Es la misma
  distincion que el LIMITE DECLARADO del barrido 9.10 nombra, y por eso se deja
  como esta en vez de maquillarla.

IDEMPOTENTE: cada sustitucion comprueba primero si su resultado ya esta
escrito. Re-correrlo no duplica ninguna nota.

Uso: python scripts/loop/vuelta57_correcciones_910.py [--simular]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REC = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")

MEDIDO = ("Medido HOY con `python scripts/plan/recomputo_3388.py` y "
          "`python scripts/recomputar_marcador.py 3388` DESPUES del ultimo movimiento de la "
          "vuelta 57 (`../loop/SALIDA_V57_RECOMPUTO_CIERRE.txt` y "
          "`../loop/SALIDA_V57_MARCADOR_CIERRE.txt`), paso 1]")

NOTA_247 = (
    " [UNDECIMA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 57, barrido "
    "`9.10` del cierre): de 164 a 208, CUARENTA Y CUATRO colapsos mas, UNO POR CADA ACTO QUE "
    "ESTA VUELTA FUNDIO (catorce en el lote A, catorce en el lote B y dieciseis en el lote C "
    "del tramo 4), por el mismo motivo que las correcciones anteriores. LA CUENTA ES EXACTA Y "
    "SE DICE, igual que en la vuelta 56: esta vuelta tampoco deshizo ninguna fusion previa, asi "
    "que 164 mas 44 son 208 sin resta intermedia. " + MEDIDO)

NOTA_248 = (
    " [DECIMOCUARTA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 57, "
    "barrido `9.10` del cierre): de 387 a 343, que vuelve a ser la resta exacta de las dos filas "
    "de arriba (551 crudas menos 208 colapsos). LA FILA DE LAS CRUDAS NO SE MUEVE, y aqui el "
    "motivo es MAS FUERTE que en la vuelta 56 y por eso se dice: esta vuelta NO VOLTEO NI UN "
    "SOLO VEREDICTO. Las colisiones esperadas del tramo 4 entero se midieron ANTES de tocar un "
    "nodo y salieron CERO sobre cien combinaciones simuladas "
    "(`../loop/SALIDA_V57_COLISIONES_ESPERADAS_TRAMO4.txt`), asi que no hubo relectura de filo "
    "que hacer y `P.16` no tuvo nada que limpiar. El marcador entero queda igual al abrir y al "
    "cerrar: `A` 551, `B` 72, `C` 5 y `D` 2.760. " + MEDIDO)

NOTA_528 = (
    " [RE-CORRIDO EL 20 ago 2026 (vuelta 57, barrido `9.10` del cierre): sigue OK con 343 y "
    "343, y las dos mitades se recomputaron por separado, no se copio una en la otra. Medido "
    "HOY DESPUES del ultimo movimiento de la vuelta 57 "
    "(`../loop/SALIDA_V57_RECOMPUTO_CIERRE.txt`, bloque LAS CUATRO COMPROBACIONES, donde las "
    "cuatro salen OK, con la comprobacion `i` en 441 igual a 441)]")

# (fichero, viejo, nuevo, etiqueta). El viejo tiene que aparecer EXACTAMENTE UNA
# vez: si no aparece o aparece mas veces, es rojo y no se escribe nada.
CAMBIOS = [
    (REC,
     "~~CUATRO~~ ~~CINCO~~ ~~SEIS~~ ~~SIETE~~ ~~OCHO~~ ~~NUEVE~~ DIEZ VECES",
     "~~CUATRO~~ ~~CINCO~~ ~~SEIS~~ ~~SIETE~~ ~~OCHO~~ ~~NUEVE~~ ~~DIEZ~~ ONCE VECES",
     "247, contador de colapsos de DIEZ a ONCE"),
    (REC,
     "~~**93**~~ ~~**117**~~ **164** ",
     "~~**93**~~ ~~**117**~~ ~~**164**~~ **208** ",
     "247, la cifra de colapsos de 164 a 208"),
    (REC,
     "~~ONCE~~ ~~DOCE~~ TRECE VECES",
     "~~ONCE~~ ~~DOCE~~ ~~TRECE~~ CATORCE VECES",
     "248, contador de pares distintos de TRECE a CATORCE"),
    (REC,
     "~~**458**~~ ~~**434**~~ **387** ",
     "~~**458**~~ ~~**434**~~ ~~**387**~~ **343** ",
     "248, la cifra de pares distintos de 387 a 343"),
    (REC,
     "~~479~~ ~~458~~ ~~434~~ **387**) == suma de aristas A internas de las componentes "
     "(~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ ~~503~~ ~~479~~ ~~458~~ ~~434~~ **387**)",
     "~~479~~ ~~458~~ ~~434~~ ~~387~~ **343**) == suma de aristas A internas de las componentes "
     "(~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ ~~503~~ ~~479~~ ~~458~~ ~~434~~ ~~387~~ **343**)",
     "528, el checkpoint ii en sus dos parentesis"),
]

# Las notas van ADOSADAS al final de su celda, detras del cierre de la cadena.
ADOSADOS = [
    (REC, "117 mas 47 son 164 sin resta intermedia. " + MEDIDO.replace("57", "56"),
     NOTA_247, "247, la nota fechada de la undecima correccion"),
    (REC, "lo que se movio son `C` (6 a 5) y `D` (2.759 a 2.760). " + MEDIDO.replace("57", "56"),
     NOTA_248, "248, la nota fechada de la decimocuarta correccion"),
    (REC, "(`../loop/SALIDA_V56_RECOMPUTO_CIERRE.txt`, bloque LAS CUATRO COMPROBACIONES, "
          "donde las cuatro salen OK)]",
     NOTA_528, "528, la nota fechada del re-corrido"),
]


def sustituir(ruta, viejo, nuevo, etiqueta, simular, estado):
    with io.open(ruta, encoding="utf-8", newline="") as fh:
        t = fh.read()
    if "\r\n" in t:
        viejo = viejo.replace("\r\n", "\n").replace("\n", "\r\n")
        nuevo = nuevo.replace("\r\n", "\n").replace("\n", "\r\n")
    if nuevo in t:
        estado.append((etiqueta, "YA ESTABA"))
        return 0
    veces = t.count(viejo)
    if veces != 1:
        estado.append((etiqueta, "ROJO: el texto viejo aparece %d veces" % veces))
        return 1
    if not simular:
        with io.open(ruta, "w", encoding="utf-8", newline="") as fh:
            fh.write(t.replace(viejo, nuevo))
    estado.append((etiqueta, "CORREGIDA"))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("LAS CELDAS DEL BARRIDO 9.10 DEL CIERRE DE LA VUELTA 57")
    print("MODO %s" % ("SIMULAR" if a.simular else "ESCRIBIR"))
    print("=" * 78)
    print()

    estado, rojo = [], 0
    for ruta, viejo, nuevo, etq in CAMBIOS:
        rojo += sustituir(ruta, viejo, nuevo, etq, a.simular, estado)
    for ruta, ancla, nota, etq in ADOSADOS:
        rojo += sustituir(ruta, ancla, ancla + nota, etq, a.simular, estado)

    for etq, res in estado:
        print("  %-62s %s" % (etq, res))
    print()
    if rojo:
        print("  ROJO en %d celdas. Revisa antes de seguir." % rojo)
        return 1
    print("  LA FILA 246 (`A` crudas) NO SE TOCA Y NO ES UN OLVIDO, y aqui el motivo es")
    print("  MAS FUERTE que en la vuelta 56: esta vuelta NO VOLTEO NI UN SOLO VEREDICTO,")
    print("  porque las colisiones esperadas del tramo entero salieron CERO. El marcador")
    print("  es identico al abrir y al cerrar en las CUATRO clases, medido dos veces.")
    print("  LAS FILAS DEL MARCADOR DEL INFORME Y LAS DOS TABLAS POR DOMINIO HERMANAS")
    print("  TAMPOCO SE TOCAN, por lo mismo: la hermandad se cumple POR VACIO y se dice.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
