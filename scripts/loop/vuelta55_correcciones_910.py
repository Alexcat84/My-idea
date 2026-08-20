# -*- coding: utf-8 -*-
"""vuelta55_correcciones_910.py . LAS CELDAS QUE EL BARRIDO 9.10 DEL CIERRE DE
LA VUELTA 55 ENCONTRO ENVEJECIDAS, CORREGIDAS CON TACHADO, CONTADOR CUADRADO Y
NOTA FECHADA.

LA REGLA QUE LO MANDA (regla operativa del cierre, acta de la vuelta 49; `D7`
de la vuelta 50): quien mueve una clase o funde un acto corre el barrido 9.10
ANTES de cerrar, y quien corrige una celda con contador CUADRA EL CONTADOR y
ADOSA la nota fechada. Ninguna nota vieja se reescribe.

QUE SE MUEVE Y QUE NO, medido y dicho:

  EL MARCADOR SI SE MUEVE ESTA VEZ, y es la diferencia con la vuelta 54: la
  relectura del filo del acto 44 corrigio el puesto 218 de `B` a `D`, asi que
  `B` baja de 73 a 72 y `D` sube de 2.758 a 2.759. `A` y `C` NO se mueven
  (551 y 6), medido las dos veces (`../loop/SALIDA_V55_MARCADOR_APERTURA.txt` y
  `../loop/SALIDA_V55_MARCADOR_CIERRE.txt`).

  LAS DOS TABLAS POR DOMINIO HERMANAS NO SE MUEVEN, Y NO ES UN OLVIDO: esas
  tablas publican la `A` de cada dominio, y la correccion del 218 fue de `B` a
  `D`, o sea que NINGUNA `A` cambio. La `A` de cada uno de los diez dominios es
  la misma al digito en las dos corridas del marcador. La hermandad de la TAREA
  1.1 de la vuelta 53 se cumple POR VACIO y se dice asi en vez de darla por
  cumplida.

  SI SE MUEVE EL RETRATO, y es la huella de la cirugia que la propia fila ya
  explica: cada acto fundido convierte su par `A` interno en un par cuyos dos
  ids resuelven al mismo nodo vivo. VEINTICUATRO colapsos mas (93 a 117) y
  VEINTICUATRO pares distintos menos (458 a 434). La cuenta cuadra al digito y
  se deja escrita porque no es 25: esta vuelta EJECUTO veinticinco fusiones,
  pero una de ellas (el acto 23) es una fusion REHECHA sobre un acto que ya
  estaba colapsado en la apertura, y su deshacer resto uno antes de sumar los
  veinticinco. 93 menos 1 mas 25 son 117.

IDEMPOTENTE: cada sustitucion comprueba primero si su resultado ya esta
escrito. Re-correrlo no duplica ninguna nota.

Uso: python scripts/loop/vuelta55_correcciones_910.py [--simular]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REC = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")
INFORME = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_INFORME.md")

NOTA_247 = (
    " [NOVENA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 55, barrido "
    "`9.10` del cierre): de 93 a 117, VEINTICUATRO colapsos mas, por el mismo motivo que las "
    "correcciones anteriores. LA CUENTA NO ES 25 Y SE DICE POR QUE: esta vuelta EJECUTO "
    "veinticinco fusiones (dos en el lote T1, once en el lote A y doce en el lote B), pero una "
    "de ellas es el acto 23 REHECHO, que ya estaba colapsado en la apertura y cuyo deshacer "
    "resto uno antes de sumar los veinticinco. 93 menos 1 mas 25 son 117. Medido HOY con "
    "`python scripts/plan/recomputo_3388.py` y `python scripts/recomputar_marcador.py 3388` "
    "DESPUES del ultimo movimiento de la vuelta 55 "
    "(`../loop/SALIDA_V55_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V55_MARCADOR_CIERRE.txt`), "
    "paso 1]")

NOTA_248 = (
    " [DUODECIMA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 55, barrido "
    "`9.10` del cierre): de 458 a 434, que vuelve a ser la resta exacta de las dos filas de "
    "arriba (551 crudas menos 117 colapsos). LA FILA DE LAS CRUDAS NO SE MUEVE, y se dice: esta "
    "vuelta si volteo un veredicto (el puesto 218, de `B` a `D`, por la relectura del filo del "
    "acto 44), pero ese volteo NO toca la `A`, asi que la `A` global sigue en 551 al abrir y al "
    "cerrar; lo que se movio son `B` (73 a 72) y `D` (2.758 a 2.759). Medido HOY con `python "
    "scripts/plan/recomputo_3388.py` y `python scripts/recomputar_marcador.py 3388` DESPUES del "
    "ultimo movimiento de la vuelta 55 (`../loop/SALIDA_V55_RECOMPUTO_CIERRE.txt` y "
    "`../loop/SALIDA_V55_MARCADOR_CIERRE.txt`), paso 1]")

NOTA_528 = (
    " **[RE-CORRIDO EL 20 ago 2026 (vuelta 55, barrido `9.10` del cierre): SIGUE OK, ahora con "
    "434 y 434, y las dos mitades se recomputaron por separado, no se copio una en la otra. "
    "Medido HOY DESPUES del ultimo movimiento de la vuelta 55 "
    "(`../loop/SALIDA_V55_RECOMPUTO_CIERRE.txt`, bloque LAS CUATRO COMPROBACIONES, donde las "
    "cuatro salen OK)]**")

NOTA_MARCADOR = (
    "\n\n> **CORRECCION DECLARADA (20 ago 2026, vuelta 55, barrido `9.10` del cierre, corrido "
    "DESPUES del ultimo movimiento de la vuelta). SE MUEVEN `B` Y `D`, Y NO SE MUEVEN `A` NI "
    "`C`.** La vuelta 55 corrigio UN veredicto por la RELECTURA DEL FILO que el acto 44 del "
    "tramo 2 de `OP-U-01` obligaba: el **puesto 218** (`reparto_inicial_equity` contra "
    "`timing_equity_split`) paso de **`B` a `D`** con correccion declarada y la razon vieja "
    "entera pegada por maquina. **`B` baja de 73 a 72 y `D` sube de 2.758 a 2.759**; **`A` "
    "sigue en 551 y `C` en 6**, porque un volteo de `B` a `D` no toca ninguna de las dos. "
    "**POR ESO LAS DOS TABLAS POR DOMINIO HERMANAS NO SE MUEVEN Y NO ES UN OLVIDO:** esas "
    "tablas publican la `A` de cada dominio, y la `A` de los diez es la misma al digito en "
    "las dos corridas del marcador de esta vuelta. **La hermandad se cumple POR VACIO y se "
    "dice, en vez de darse por cumplida.** Medido con `python scripts/recomputar_marcador.py "
    "3388` ([`loop/SALIDA_V55_MARCADOR_CIERRE.txt`](loop/SALIDA_V55_MARCADOR_CIERRE.txt)). "
    "**Las veinticinco fusiones de esta vuelta NO movieron el marcador por si solas: son de "
    "fusion pura y ninguna fabrico colision, asi que `P.16` no tuvo nada que limpiar.**\n")

CAMBIOS_REC = [
    ("247 colapsos, la cifra y su cadena",
     "~~**60**~~ ~~**72**~~ **93** **[CORREGIDA ~~CUATRO~~ ~~CINCO~~ ~~SEIS~~ ~~SIETE~~ OCHO VECES",
     "~~**60**~~ ~~**72**~~ ~~**93**~~ **117** **[CORREGIDA ~~CUATRO~~ ~~CINCO~~ ~~SEIS~~ ~~SIETE~~ ~~OCHO~~ NUEVE VECES"),
    ("247 la nota novena, adosada al final de la celda",
     "(`../loop/SALIDA_V54_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V54_MARCADOR_CIERRE.txt`), "
     "paso 1]** |\n| pares distintos en el retrato",
     "(`../loop/SALIDA_V54_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V54_MARCADOR_CIERRE.txt`), "
     "paso 1]" + NOTA_247 + "** |\n| pares distintos en el retrato"),
    ("248 pares distintos, la cifra y su cadena",
     "~~**503**~~ ~~**479**~~ **458** **[CORREGIDA ~~SIETE~~ ~~OCHO~~ ~~NUEVE~~ ~~DIEZ~~ ONCE VECES",
     "~~**503**~~ ~~**479**~~ ~~**458**~~ **434** **[CORREGIDA ~~SIETE~~ ~~OCHO~~ ~~NUEVE~~ ~~DIEZ~~ ~~ONCE~~ DOCE VECES"),
    ("248 la nota duodecima, adosada al final de la celda",
     "(`../loop/SALIDA_V54_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V54_MARCADOR_CIERRE.txt`), "
     "paso 1]** |",
     "(`../loop/SALIDA_V54_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V54_MARCADOR_CIERRE.txt`), "
     "paso 1]" + NOTA_248 + "** |"),
    ("528 el checkpoint ii, sus dos parentesis",
     "~~503~~ ~~479~~ **458**) == suma de aristas A internas de las componentes (~~583~~ "
     "~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ ~~503~~ ~~479~~ **458**)",
     "~~503~~ ~~479~~ ~~458~~ **434**) == suma de aristas A internas de las componentes (~~583~~ "
     "~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ ~~503~~ ~~479~~ ~~458~~ **434**)"),
    ("528 la nota del re-corrido de la vuelta 55",
     "(`../loop/SALIDA_V54_RECOMPUTO_CIERRE.txt`, bloque LAS CUATRO COMPROBACIONES, donde las "
     "cuatro salen OK)]** |",
     "(`../loop/SALIDA_V54_RECOMPUTO_CIERRE.txt`, bloque LAS CUATRO COMPROBACIONES, donde las "
     "cuatro salen OK)]**" + NOTA_528 + " |"),
]

CAMBIOS_INFORME = [
    ("la fila B del marcador publicado",
     "| **B** | ~~89~~ ~~87~~ ~~84~~ ~~83~~ ~~82~~ ~~81~~ ~~80~~ ~~79~~ ~~77~~ ~~75~~ **73** |",
     "| **B** | ~~89~~ ~~87~~ ~~84~~ ~~83~~ ~~82~~ ~~81~~ ~~80~~ ~~79~~ ~~77~~ ~~75~~ ~~73~~ **72** |"),
    ("la fila D del marcador publicado",
     "~~2.737 (80,8 %)~~ ~~2.743 (81,0 %)~~ **2.758** (81,4 %) |",
     "~~2.737 (80,8 %)~~ ~~2.743 (81,0 %)~~ ~~2.758~~ **2.759** (81,4 %) |" + NOTA_MARCADOR),
]


def aplicar(ruta, cambios, etiqueta_fichero, simular):
    t = io.open(ruta, encoding="utf-8").read()
    hechas = saltadas = 0
    for etiqueta, viejo, nuevo in cambios:
        if nuevo in t:
            print("  YA ESTABA   %-52s (idempotente)" % etiqueta)
            saltadas += 1
            continue
        c = t.count(viejo)
        if c != 1:
            print("  ROJO        %-52s el texto viejo aparece %d veces" % (etiqueta, c))
            return None, hechas, saltadas
        t = t.replace(viejo, nuevo, 1)
        print("  HECHA       %-52s" % etiqueta)
        hechas += 1
    if not simular:
        io.open(ruta, "w", encoding="utf-8", newline=chr(10)).write(t)
    print("  fichero: %s" % etiqueta_fichero)
    print()
    return t, hechas, saltadas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("LAS CORRECCIONES DEL BARRIDO 9.10 DEL CIERRE DE LA VUELTA 55")
    print("modo: %s" % ("SIMULACION, no escribe" if a.simular else "ESCRITURA"))
    print("=" * 78)
    print()

    print("--- LAS TRES CELDAS DEL RETRATO, en docs/plan/RECOMPUTO_3388.md ---")
    t1, h1, s1 = aplicar(REC, CAMBIOS_REC, "docs/plan/RECOMPUTO_3388.md", a.simular)
    if t1 is None:
        return 1

    print("--- LAS DOS FILAS DEL MARCADOR, en docs/INTRA_DOMINIO_INFORME.md ---")
    t2, h2, s2 = aplicar(INFORME, CAMBIOS_INFORME, "docs/INTRA_DOMINIO_INFORME.md", a.simular)
    if t2 is None:
        return 1

    print("  celdas corregidas: %d | ya estaban: %d" % (h1 + h2, s1 + s2))
    print()
    print("  LA FILA DE LAS A CRUDAS NO SE TOCA Y LAS DOS TABLAS POR DOMINIO TAMPOCO,")
    print("  y no es un olvido: el unico veredicto que esta vuelta movio paso de B a D")
    print("  (puesto 218, relectura del filo del acto 44), y ese volteo no toca la A.")
    print("  La A global sigue en 551 y la de cada uno de los diez dominios es la misma")
    print("  al digito en las dos corridas del marcador. La hermandad se cumple POR VACIO.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
