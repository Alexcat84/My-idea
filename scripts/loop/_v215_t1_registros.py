# -*- coding: utf-8 -*-
r"""_v215_t1_registros.py . LA TAREA 1 DE LA VUELTA 215: LOS REGISTROS DEL ACTA
DE LA 214, CON LA LINEA DE DONDE SALE CADA UNO.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO (moratoria de AUDITOR.md 6.3).
No vigila nada y muere con la vuelta.

QUE HACE, Y LO QUE NO HACE. LEE docs/loop/ACTA_AUDITOR.md, localiza el acta de
la vuelta 214 por su cabecera, y saca de sus secciones 3 y 5 las adjudicaciones
y los hallazgos CON SU NUMERO DE LINEA ABSOLUTO Y SU TITULO VERBATIM. NINGUNA
LINEA SE TECLEA: todas salen de enumerate() sobre el fichero. NO escribe en el
acta ni en ninguna sede del auditor: solo imprime su salida, que se sella.

POR QUE ASI. EJECUTOR.md 1, LA CITA LLEVA SU LINEA, y la obligacion de dictado
del 6.6 del acta 210: toda cita de un acta anterior lleva LA LINEA donde vive el
texto citado, y la linea se LEE, no se recuerda. Un numero de linea recordado es
exactamente la especie de cifra que esta casa lleva vueltas cazando.

LA GUARDA QUE PUEDE CAER, Y SE PRUEBA POR MUTACION (EJECUTOR.md 1, EL CASO ROJO
SE PRUEBA POR MUTACION): se exige que las adjudicaciones halladas sean NUEVE,
que sus etiquetas sean exactamente de 5.1 a 5.9 sin huecos ni repeticiones, que
las CINCO que el encargo manda aplicar esten entre ellas, y que el hallazgo 3.1
aparezca. Si algo de eso no se cumple, el instrumento CAE EN ROJO y no escribe.

USO:  python scripts/loop/_v215_t1_registros.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
ACTA_QUE_SE_LEE = VUELTA - 1

# LAS CINCO QUE EL ENCARGO MANDA APLICAR COMO ORDEN. No es una lista de
# resultados: es la lista de lo que hay que ENCONTRAR, y si alguna falta el
# instrumento cae en rojo.
LAS_CINCO_DEL_ENCARGO = ("5.1", "5.2", "5.3", "5.4", "5.5")


def lineas_del_acta():
    return io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL).split(NL)


def rango_del_acta(lineas, n):
    """DONDE EMPIEZA Y DONDE ACABA EL ACTA DE LA VUELTA n, LOCALIZADA POR SU
    CABECERA. PURA: recibe las lineas y no lee nada."""
    patron = re.compile(r"^# ACTA DEL AUDITOR, VUELTA (\d+)\b")
    inicio = None
    for i, l in enumerate(lineas):
        m = patron.match(l)
        if not m:
            continue
        if int(m.group(1)) == n:
            inicio = i
        elif inicio is not None:
            return inicio, i
    return inicio, len(lineas) if inicio is not None else (None, None)


def entradas(lineas, ini, fin):
    """LAS ENTRADAS NUMERADAS DEL ACTA, CON SU LINEA ABSOLUTA (1 A N) Y SU
    TITULO. PURA."""
    patron = re.compile(r"^\*\*`(\d+\.\d+)`")
    fuera = []
    for i in range(ini, fin):
        m = patron.match(lineas[i])
        if not m:
            continue
        # EL TITULO ES LO QUE VA HASTA EL PRIMER PUNTO FINAL EN NEGRITA, y si
        # la frase sigue en la linea de abajo se cose, porque el acta parte sus
        # parrafos a 88 columnas y una etiqueta cortada no es una cita.
        trozo = lineas[i]
        j = i
        while "**" not in trozo[len(m.group(0)):] and j + 1 < fin:
            j += 1
            trozo = trozo + " " + lineas[j].strip()
        fuera.append((m.group(1), i + 1, trozo.strip()))
    return fuera


def juzgar(adj, hall):
    """LAS CUATRO GUARDAS, EN UNA FUNCION PURA PARA QUE SE PUEDAN MUTAR SIN
    TOCAR EL ACTA. Recibe las dos listas de entradas y devuelve
    (fallos, informe). No lee ni escribe nada."""
    fallos = 0
    informe = []
    etiquetas = [e[0] for e in adj]
    esperadas = ["5.%d" % k for k in range(1, 10)]
    informe.append("CIFRA adjudicaciones halladas: %d | CIFRA que el encargo "
                   "dice: 9" % len(adj))
    if len(adj) != 9:
        fallos += 1
    informe.append("CIFRA etiquetas correlativas de 5.1 a 5.9: %s (se exige SI)"
                   % ("SI" if etiquetas == esperadas else "NO"))
    if etiquetas != esperadas:
        fallos += 1
    faltan = [c for c in LAS_CINCO_DEL_ENCARGO if c not in etiquetas]
    informe.append("CIFRA de las CINCO que el encargo manda aplicar que NO "
                   "aparecen: %d %s" % (len(faltan), faltan))
    if faltan:
        fallos += 1
    tiene_31 = any(e[0] == "3.1" for e in hall)
    informe.append("CIFRA el hallazgo 3.1 aparece: %s (se exige SI)"
                   % ("SI" if tiene_31 else "NO"))
    if not tiene_31:
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

    fallos = 0
    print("LAS ADJUDICACIONES, UNA POR LINEA, CON SU LINEA DELANTE")
    for etiqueta, linea, texto in adj:
        print("ADJUDICACION %s | linea %d | %s" % (etiqueta, linea, texto[:150]))
    print("")
    print("LOS HALLAZGOS DE LA SECCION 3, IGUAL")
    for etiqueta, linea, texto in hall:
        print("HALLAZGO %s | linea %d | %s" % (etiqueta, linea, texto[:150]))
    print("")

    print("LAS GUARDAS, Y CADA UNA CON SU CIFRA A LOS DOS LADOS")
    fallos, informe = juzgar(adj, hall)
    for l in informe:
        print(l)
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: el registro no se publica.")
        return 1
    print("VERDE: las nueve adjudicaciones y el hallazgo estan, con su linea.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
