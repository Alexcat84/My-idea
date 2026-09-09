# -*- coding: utf-8 -*-
r"""_v216_t1_registros.py . LA TAREA 1 DE LA VUELTA 216: LOS REGISTROS DEL ACTA
DE LA 215, CON LA LINEA DE DONDE SALE CADA UNO.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO (moratoria de AUDITOR.md 6.3).
No vigila nada y muere con la vuelta.

NO ES UN CLON. lineas_del_acta, rango_del_acta y entradas se IMPORTAN de
_v215_t1_registros.py, que es donde nacieron; aqui NO se copia ni una linea de
esas tres funciones. Lo unico que cambia es QUE ACTA SE LEE (la 215, computada
de mi propio nombre y no tecleada), CUANTAS adjudicaciones se exigen (OCHO, de
la 5.1 a la 5.8) y CUALES son las CUATRO que obligan. IMPORTAR NO ES CLONAR,
acta 206 adjudicacion 6.5.

QUE ANADE ESTA VUELTA, Y ES LO QUE SU ENCARGO PIDE ADEMAS: los TRES ANCLAJES de
la 1.b y la 1.c, o sea las DOS CORRECCIONES DECLARADAS del auditor y su UNICA
CIFRA MALA, localizados POR SU TEXTO dentro del acta y publicados CON SU LINEA
ABSOLUTA. Ninguno se teclea: los tres salen de enumerate() sobre el fichero, y
si alguno no aparece el instrumento CAE EN ROJO.

Y ANADE EL RECUENTO DE LA SECCION 6, que es la lista de lo que sube a la
auditoria integral: se cuenta, no se recuerda.

LA GUARDA QUE PUEDE CAER, Y SE PRUEBA POR MUTACION (EJECUTOR.md 1, EL CASO ROJO
SE PRUEBA POR MUTACION): se exige que las adjudicaciones sean OCHO y que sus
etiquetas vayan de 5.1 a 5.8 sin huecos ni repeticiones; que las CUATRO que
obligan esten entre ellas; que los hallazgos de la seccion 3 sean CUATRO; y que
los TRES anclajes aparezcan una sola vez cada uno. Si algo de eso falla, el
instrumento cae en ROJO y no publica.

USO:  python scripts/loop/_v216_t1_registros.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v215_t1_registros import (  # noqa: E402
    lineas_del_acta, rango_del_acta, entradas)

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
ACTA_QUE_SE_LEE = VUELTA - 1

# LAS CUATRO QUE EL ENCARGO DICE QUE ME OBLIGAN A ALGO. No es una lista de
# resultados: es la lista de lo que hay que ENCONTRAR, y si alguna falta el
# instrumento cae en rojo.
LAS_CUATRO_QUE_OBLIGAN = ("5.1", "5.2", "5.4", "5.7")

# LOS TRES ANCLAJES DE LA 1.b Y LA 1.c, CADA UNO POR UN TROZO DE TEXTO QUE ES
# SUYO Y DE NADIE MAS DENTRO DEL ACTA. La etiqueta de la izquierda es mia; el
# texto de la derecha es del auditor y se busca literal.
ANCLAJES = (
    ("CORRECCION 1 (su 5.8): las fichas en HECHA SIN NINGUNA PRUEBA son CUATRO",
     "Medido hoy por mi con la misma vara y con los dos cortes:"),
    ("CORRECCION 2 (su 3.1): mi racha de caida de reporte VUELVE A CERO",
     "SU RACHA DE CAIDA DE REPORTE, QUE LA 214 DEJO EN UNO, VUELVE A"),
    ("SU UNICA CIFRA MALA, QUE ES SUYA (su seccion 7)",
     "mi ciega sale 67 de 80"),
)


def anclar(lineas, ini, fin, aguja):
    """DONDE VIVE UN TROZO DE TEXTO DENTRO DEL ACTA, CON SU LINEA ABSOLUTA.
    PURA: recibe las lineas y no lee ni escribe nada. Devuelve la lista de
    (linea, texto), para que el que llama pueda exigir que sea UNA."""
    return [(i + 1, lineas[i].strip())
            for i in range(ini, fin) if aguja in lineas[i]]


def items_de_la_seccion_6(lineas, ini, fin):
    """LOS PUNTOS NUMERADOS DE LA SECCION 6 DEL ACTA, CON SU LINEA. PURA."""
    cab = re.compile(r"^## (\d+)\.")
    dentro = False
    fuera = []
    for i in range(ini, fin):
        m = cab.match(lineas[i])
        if m:
            dentro = (m.group(1) == "6")
            continue
        if not dentro:
            continue
        m2 = re.match(r"^(\d+)\. \*\*(.+)$", lineas[i])
        if m2:
            fuera.append((int(m2.group(1)), i + 1, lineas[i].strip()))
    return fuera


def juzgar(adj, hall, anclados, items6):
    """LAS GUARDAS, EN UNA FUNCION PURA PARA QUE SE PUEDAN MUTAR SIN TOCAR EL
    ACTA. Recibe lo hallado y devuelve (fallos, informe)."""
    fallos = 0
    informe = []
    etiquetas = [e[0] for e in adj]
    esperadas = ["5.%d" % k for k in range(1, 9)]
    informe.append("CIFRA adjudicaciones halladas: %d | CIFRA que el encargo "
                   "dice: 8" % len(adj))
    if len(adj) != 8:
        fallos += 1
    informe.append("CIFRA etiquetas correlativas de 5.1 a 5.8: %s (se exige SI)"
                   % ("SI" if etiquetas == esperadas else "NO"))
    if etiquetas != esperadas:
        fallos += 1
    faltan = [c for c in LAS_CUATRO_QUE_OBLIGAN if c not in etiquetas]
    informe.append("CIFRA de las CUATRO que me obligan que NO aparecen: %d %s"
                   % (len(faltan), faltan))
    if faltan:
        fallos += 1
    informe.append("CIFRA hallazgos de la seccion 3: %d | CIFRA que se exige: 4"
                   % len(hall))
    if len(hall) != 4:
        fallos += 1
    for etiqueta, halladas in anclados:
        informe.append("CIFRA veces que aparece el anclaje %r: %d "
                       "(se exige 1)" % (etiqueta[:44], len(halladas)))
        if len(halladas) != 1:
            fallos += 1
    informe.append("CIFRA puntos numerados de la seccion 6: %d "
                   "(se exige 1 o mas)" % len(items6))
    if len(items6) < 1:
        fallos += 1
    return fallos, informe


def main():
    lineas = lineas_del_acta()
    print("EL ACTA, LEIDA HOY Y NO RECORDADA")
    print("CIFRA lineas de docs/loop/ACTA_AUDITOR.md: %d" % len(lineas))
    ini, fin = rango_del_acta(lineas, ACTA_QUE_SE_LEE)
    if ini is None:
        print("ROJO: no encuentro el acta de la vuelta %d." % ACTA_QUE_SE_LEE)
        return 1
    print("CIFRA linea donde ABRE el acta de la vuelta %d: %d"
          % (ACTA_QUE_SE_LEE, ini + 1))
    print("CIFRA linea donde ACABA (ultima del fichero o cabecera siguiente): %d"
          % fin)
    print("PRIMERA LINEA DE ESA ACTA, LEIDA: %s" % lineas[ini])
    print("")

    todas = entradas(lineas, ini, fin)
    print("LAS ENTRADAS NUMERADAS DE ESA ACTA, CON SU LINEA ABSOLUTA")
    print("CIFRA entradas halladas en el acta entera: %d" % len(todas))
    adj = [e for e in todas if e[0].startswith("5.")]
    hall = [e for e in todas if e[0].startswith("3.")]
    print("CIFRA adjudicaciones (seccion 5): %d | CIFRA hallazgos (seccion 3): %d"
          % (len(adj), len(hall)))
    print("")

    print("LAS OCHO ADJUDICACIONES, UNA POR LINEA, CON SU LINEA DELANTE")
    for etiqueta, linea, texto in adj:
        obliga = "OBLIGA" if etiqueta in LAS_CUATRO_QUE_OBLIGAN else "registro"
        print("ADJUDICACION %s | linea %d | %s | %s"
              % (etiqueta, linea, obliga, texto[:210]))
    print("")
    print("LOS HALLAZGOS DE LA SECCION 3, IGUAL")
    for etiqueta, linea, texto in hall:
        print("HALLAZGO %s | linea %d | %s" % (etiqueta, linea, texto[:210]))
    print("")

    print("LOS TRES ANCLAJES DE LA 1.b Y LA 1.c, LOCALIZADOS POR SU TEXTO")
    anclados = []
    for etiqueta, aguja in ANCLAJES:
        halladas = anclar(lineas, ini, fin, aguja)
        anclados.append((etiqueta, halladas))
        for linea, texto in halladas:
            print("ANCLAJE | %s | linea %d | %s" % (etiqueta, linea, texto[:210]))
        if not halladas:
            print("ANCLAJE | %s | NO APARECE (ausencia, no cero)" % etiqueta)
    print("")

    items6 = items_de_la_seccion_6(lineas, ini, fin)
    print("LA SECCION 6, LO QUE SUBE A LA AUDITORIA INTEGRAL, CONTADA Y NO RECORDADA")
    print("CIFRA puntos numerados de la seccion 6: %d" % len(items6))
    for n, linea, texto in items6:
        print("SECCION6 punto %d | linea %d | %s" % (n, linea, texto[:210]))
    print("")

    print("LAS GUARDAS, Y CADA UNA CON SU CIFRA A LOS DOS LADOS")
    fallos, informe = juzgar(adj, hall, anclados, items6)
    for l in informe:
        print(l)
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: el registro no se publica.")
        return 1
    print("VERDE: las ocho adjudicaciones, los cuatro hallazgos, los tres "
          "anclajes y la seccion 6 estan, con su linea.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
