# -*- coding: utf-8 -*-
"""vuelta56_correcciones_910.py . LAS CELDAS QUE EL BARRIDO 9.10 DEL CIERRE DE
LA VUELTA 56 ENCONTRO ENVEJECIDAS, CORREGIDAS CON TACHADO, CONTADOR CUADRADO Y
NOTA FECHADA.

LA REGLA QUE LO MANDA (regla operativa del cierre, acta de la vuelta 49; `D7`
de la vuelta 50): quien mueve una clase o funde un acto corre el barrido 9.10
ANTES de cerrar, y quien corrige una celda con contador CUADRA EL CONTADOR y
ADOSA la nota fechada. Ninguna nota vieja se reescribe.

QUE SE MUEVE Y QUE NO, medido y dicho:

  EL MARCADOR SE MUEVE EN `C` Y EN `D`, Y NO EN `A` NI EN `B`: la relectura del
  filo del acto 15 corrigio el puesto 203 de `C` a `D`, asi que `C` baja de 6 a
  5 y `D` sube de 2.759 a 2.760. `A` sigue en 551 y `B` en 72, medido las dos
  veces (`../loop/SALIDA_V56_MARCADOR_APERTURA.txt` y
  `../loop/SALIDA_V56_MARCADOR_CIERRE.txt`).

  LAS DOS TABLAS POR DOMINIO HERMANAS NO SE MUEVEN, Y NO ES UN OLVIDO: esas
  tablas publican la `A` de cada dominio, y la correccion del 203 fue de `C` a
  `D`, o sea que NINGUNA `A` cambio. La `A` de cada uno de los diez dominios es
  la misma al digito en las dos corridas del marcador. La hermandad de la TAREA
  1.1 de la vuelta 53 se cumple POR VACIO y se dice asi en vez de darla por
  cumplida.

  SI SE MUEVE EL RETRATO, y es la huella de la cirugia que la propia fila ya
  explica: cada acto fundido convierte su par `A` interno en un par cuyos dos
  ids resuelven al mismo nodo vivo. CUARENTA Y SIETE colapsos mas (117 a 164) y
  CUARENTA Y SIETE pares distintos menos (434 a 387), UNO POR CADA ACTO QUE
  ESTA VUELTA FUNDIO. La resta sigue exacta: 551 crudas menos 164 colapsos son
  387.

IDEMPOTENTE: cada sustitucion comprueba primero si su resultado ya esta
escrito. Re-correrlo no duplica ninguna nota.

Uso: python scripts/loop/vuelta56_correcciones_910.py [--simular]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REC = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")
INFORME = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_INFORME.md")

MEDIDO = ("Medido HOY con `python scripts/plan/recomputo_3388.py` y "
          "`python scripts/recomputar_marcador.py 3388` DESPUES del ultimo movimiento de la "
          "vuelta 56 (`../loop/SALIDA_V56_RECOMPUTO_CIERRE.txt` y "
          "`../loop/SALIDA_V56_MARCADOR_CIERRE.txt`), paso 1]")

NOTA_247 = (
    " [DECIMA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 56, barrido "
    "`9.10` del cierre): de 117 a 164, CUARENTA Y SIETE colapsos mas, UNO POR CADA ACTO QUE "
    "ESTA VUELTA FUNDIO (diecisiete en el lote A, dieciseis en el lote B y catorce en el lote "
    "C del tramo 3), por el mismo motivo que las correcciones anteriores. AQUI LA CUENTA SI ES "
    "EXACTA Y SE DICE, porque en la vuelta 55 no lo fue: esta vuelta no deshizo ninguna fusion "
    "previa, asi que 117 mas 47 son 164 sin resta intermedia. " + MEDIDO)

NOTA_248 = (
    " [DECIMOTERCERA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 56, "
    "barrido `9.10` del cierre): de 434 a 387, que vuelve a ser la resta exacta de las dos "
    "filas de arriba (551 crudas menos 164 colapsos). LA FILA DE LAS CRUDAS NO SE MUEVE, y se "
    "dice: esta vuelta si volteo un veredicto (el puesto 203, de `C` a `D`, por la relectura "
    "del filo del acto 15 del tramo 3), pero ese volteo NO toca la `A`, asi que la `A` global "
    "sigue en 551 al abrir y al cerrar; lo que se movio son `C` (6 a 5) y `D` (2.759 a 2.760). "
    + MEDIDO)

NOTA_528 = (
    " [RE-CORRIDO EL 20 ago 2026 (vuelta 56, barrido `9.10` del cierre): sigue OK con 387 y "
    "387, y las dos mitades se recomputaron por separado, no se copio una en la otra. Medido "
    "HOY DESPUES del ultimo movimiento de la vuelta 56 "
    "(`../loop/SALIDA_V56_RECOMPUTO_CIERRE.txt`, bloque LAS CUATRO COMPROBACIONES, donde las "
    "cuatro salen OK)]")

NOTA_INFORME = (
    "\n\n> **CORRECCION DECLARADA (20 ago 2026, vuelta 56, barrido `9.10` del cierre, corrido "
    "DESPUES del ultimo movimiento de la vuelta). SE MUEVEN `C` Y `D`, Y NO SE MUEVEN `A` NI "
    "`B`.** La vuelta 56 corrigio UN veredicto por la RELECTURA DEL FILO que el acto 15 del "
    "tramo 3 de `OP-U-01` obligaba: el **puesto 203** (`dso_dpo_gestion_capital_trabajo` contra "
    "`gestion_cuentas_por_pagar_dpo`) pasa de `C` a `D`, con la razon vieja entera pegada por "
    "maquina dentro de la nueva. **`C` baja de 6 a 5 y `D` sube de 2.759 a 2.760.** **Las "
    "CUARENTA Y SIETE fusiones de la vuelta NO movieron el marcador por si solas**: son de "
    "fusion pura y ninguna fabrico colision, asi que `P.16` no tuvo nada que limpiar. **La `A` "
    "sigue en 551 y por eso las dos tablas por dominio hermanas tampoco se mueven, medido y no "
    "supuesto.** Medido con `python scripts/recomputar_marcador.py 3388` en "
    "[`../loop/SALIDA_V56_MARCADOR_CIERRE.txt`](../loop/SALIDA_V56_MARCADOR_CIERRE.txt).\n")

# (fichero, viejo, nuevo, etiqueta). El viejo tiene que aparecer EXACTAMENTE UNA
# vez: si no aparece o aparece mas veces, es rojo y no se escribe nada.
CAMBIOS = [
    (REC,
     "~~OCHO~~ NUEVE VECES, el 15 ago 2026 y el 19 ago 2026 (vueltas 49 y 50)",
     "~~OCHO~~ ~~NUEVE~~ DIEZ VECES, el 15 ago 2026 y el 19 ago 2026 (vueltas 49 y 50)",
     "247, contador de colapsos de NUEVE a DIEZ"),
    (REC,
     "~~**72**~~ ~~**93**~~ **117** ",
     "~~**72**~~ ~~**93**~~ ~~**117**~~ **164** ",
     "247, la cifra de colapsos de 117 a 164"),
    (REC,
     "~~ONCE~~ DOCE VECES, las dos ultimas el 19 ago 2026",
     "~~ONCE~~ ~~DOCE~~ TRECE VECES, las dos ultimas el 19 ago 2026",
     "248, contador de pares distintos de DOCE a TRECE"),
    (REC,
     "~~**479**~~ ~~**458**~~ **434** ",
     "~~**479**~~ ~~**458**~~ ~~**434**~~ **387** ",
     "248, la cifra de pares distintos de 434 a 387"),
    (REC,
     "~~479~~ ~~458~~ **434**) == suma de aristas A internas de las componentes "
     "(~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ ~~503~~ ~~479~~ ~~458~~ **434**)",
     "~~479~~ ~~458~~ ~~434~~ **387**) == suma de aristas A internas de las componentes "
     "(~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ ~~503~~ ~~479~~ ~~458~~ ~~434~~ **387**)",
     "528, el checkpoint ii en sus dos parentesis"),
    (INFORME,
     "| **C** | ~~7~~ ~~8~~ ~~7~~ **6** |",
     "| **C** | ~~7~~ ~~8~~ ~~7~~ ~~6~~ **5** |",
     "informe, la fila C del marcador publicado"),
    (INFORME,
     "~~2.758~~ **2.759** (81,4 %) |",
     "~~2.758~~ ~~2.759~~ **2.760** (81,5 %) |" + NOTA_INFORME,
     "informe, la fila D del marcador publicado mas su nota fechada"),
]

# Las notas van ADOSADAS al final de su celda, detras del cierre de la cadena.
ADOSADOS = [
    (REC, "(`../loop/SALIDA_V55_RECOMPUTO_CIERRE.txt` y "
          "`../loop/SALIDA_V55_MARCADOR_CIERRE.txt`), paso 1]** |\n| pares distintos",
     NOTA_247, "247, la nota fechada"),
]


def sustituir(ruta, viejo, nuevo, etiqueta, simular, estado):
    with io.open(ruta, encoding="utf-8", newline="") as fh:
        t = fh.read()
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
    print("LAS CELDAS DEL BARRIDO 9.10 DEL CIERRE DE LA VUELTA 56")
    print("MODO %s" % ("SIMULAR" if a.simular else "ESCRIBIR"))
    print("=" * 78)
    print()

    estado, rojo = [], 0
    for ruta, viejo, nuevo, etq in CAMBIOS:
        rojo += sustituir(ruta, viejo, nuevo, etq, a.simular, estado)

    # LAS NOTAS FECHADAS, adosadas al final de la cadena de su celda.
    for ruta, ancla, nota, etq in [
        (REC, "93 menos 1 mas 25 son 117. " + (
            "Medido HOY con `python scripts/plan/recomputo_3388.py` y "
            "`python scripts/recomputar_marcador.py 3388` DESPUES del ultimo movimiento de la "
            "vuelta 55 (`../loop/SALIDA_V55_RECOMPUTO_CIERRE.txt` y "
            "`../loop/SALIDA_V55_MARCADOR_CIERRE.txt`), paso 1]"), NOTA_247,
         "247, la nota fechada de la decima correccion"),
        (REC, "lo que se movio son `B` (73 a 72) y `D` (2.758 a 2.759). " + (
            "Medido HOY con `python scripts/plan/recomputo_3388.py` y "
            "`python scripts/recomputar_marcador.py 3388` DESPUES del ultimo movimiento de la "
            "vuelta 55 (`../loop/SALIDA_V55_RECOMPUTO_CIERRE.txt` y "
            "`../loop/SALIDA_V55_MARCADOR_CIERRE.txt`), paso 1]"), NOTA_248,
         "248, la nota fechada de la decimotercera correccion"),
        (REC, "(`../loop/SALIDA_V55_RECOMPUTO_CIERRE.txt`, bloque LAS CUATRO COMPROBACIONES, "
              "donde las cuatro salen OK)]", NOTA_528,
         "528, la nota fechada del re-corrido"),
    ]:
        rojo += sustituir(ruta, ancla, ancla + nota, etq, a.simular, estado)

    for etq, res in estado:
        print("  %-62s %s" % (etq, res))
    print()
    if rojo:
        print("  ROJO en %d celdas. Revisa antes de seguir." % rojo)
        return 1
    print("  LA FILA 246 (`A` crudas) NO SE TOCA Y NO ES UN OLVIDO: el unico veredicto")
    print("  que esta vuelta movio paso de `C` a `D`, y ese volteo no toca la `A`.")
    print("  LAS DOS TABLAS POR DOMINIO HERMANAS TAMPOCO, por lo mismo: publican la `A`")
    print("  de cada dominio y la `A` de los diez es identica al digito en las dos")
    print("  corridas del marcador. La hermandad se cumple POR VACIO y se dice.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
