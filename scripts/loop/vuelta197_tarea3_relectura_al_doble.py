# -*- coding: utf-8 -*-
r"""vuelta197_tarea3_relectura_al_doble.py . EL SUJETO DE LA RELECTURA AL DOBLE
DEL TRAMO DE LA TANDA DEL AUDITOR DE LA 197, ELEGIDO Y AISLADO ANTES DE QUE NADIE
MIRE NADA.

QUIEN LA ENCARGA Y CON QUE PALABRAS. **La encarga el AUDITOR y es DEUDA SUYA**:
`AUDITOR.md` 1.2, y **CINCO** discrepancias suyas (`655`, `719`, `976`, `1809`,
`1810`) cayeron FUERA de su marcado, asi que el credito de su tanda baja y el
tramo se relee al doble. Quien la paga es el ejecutor, con el instrumento.

**SON DOSCIENTOS CUARENTA PARES**, 120 del tramo y 120 del doble, y la serie
medida va 30, 60, 120 y ahora 240.

CLON DECLARADO de `scripts/loop/vuelta196_tarea2_relectura_al_doble.py`. Cambia el
TRAMO, la SELLADA, los `PUESTOS_DEL_ACTA` (de UNO a CINCO), el
`UNIVERSO_CONSUMIDO` (de CATORCE ficheros a DIECISEIS), el CRITERIO, la lista de
QUEMADOS, los dos errores que van dentro del criterio, y este docstring.
**Y `vecinos()`, `puestos_de()`, `numeros_de()` y `UNIVERSO_CONSUMIDO` SE IMPORTAN
Y NO SE COPIAN**, que es lo que el encargo manda con esas palabras.

LA TRAMPA QUE EL AUDITOR PISO Y DECLARO EN SU `C.A5`, Y QUE AQUI SE ESQUIVA CON SU
CIFRA DELANTE: **los dos `_exclusion.txt` guardan ENTEROS SUELTOS y se leen con
`numeros_de()`, no con el patron de `puesto_intra`**. Con un solo patron para
todos, el universo sale **300** en vez de **681**, y el "solape 0 por
construccion" seria falso. El reparto por fichero se publica entero, con el lector
que le toca a cada uno nombrado al lado.

LOS DOS ERRORES QUE VAN DENTRO DEL CRITERIO SON LOS QUE EL COTEJO DEL AUDITOR
MIDIO, Y NO UNA SOSPECHA:
  . **LA VARA ES EL SUELO Y NO EL TECHO.** Es la especie del `719` (la regla del
    puesto 595: el mismo instrumento en dos ocasiones distintas es sano) y la del
    `976` (la familia del sub-puro 7, cuatro pares leidos y los cuatro en `A`).
  . **LA CONTENCION SE MIDE SOBRE EL CONTENIDO, NO SOBRE EL CONTENEDOR.** Es la
    especie del `2838`: si el nodo corto cabe ENTERO en el largo y no trae ni un
    paso propio, es `A` por contencion, por mucho que el largo traiga ademas un
    procedimiento entero.

LO QUE ESTE FICHERO ESTRENA, Y SON LAS PIEZAS (e), (f) Y (g) DEL ENCARGO
ADELANTADAS AL SUJETO, todas ANTES de leer nada:
  . **LOS QUEMADOS** (g), con su sede citada uno por uno.
  . **LOS INALCANZABLES A CIEGAS** (f), contados por un barrido que mira SOLO si
    la razon cita un racimo censado o una correccion declarada, y que **NO imprime
    ni la clase ni el texto de la razon**: solo el numero del puesto y la cuenta.
  . **EL REPARTO DEL MARCADO** (e), que el hallazgo `5.2` obliga: cuantos de los
    240 llevan el literal `DISCUTIBLE MARCADO` y como se reparten por puesto.

LO QUE ESTE FICHERO NO HACE, Y ES LA MITAD QUE IMPORTA: **NO TOCA NINGUNA CLASE**.
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre en modo lectura y su `sha256` LF se
mide al entrar y al salir. Y **NO LEE EL DESTAPE**: lo escribe y lo deja cerrado.

USO:
  python scripts/loop/vuelta197_tarea3_relectura_al_doble.py
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta182_tarea1c_relectura_al_doble import vecinos   # noqa: E402
from vuelta196_tarea2_relectura_al_doble import (           # noqa: E402
    puestos_de, numeros_de, UNIVERSO_CONSUMIDO as UNIVERSO_DE_LA_196)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
PY = sys.executable
VUELTA = 197

ARCHIVO = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
TRAMO = "docs/loop/_auditor_v197_ciega_blind.txt"
SELLADA_DEL_DOBLE = "docs/loop/_auditor_v197_doble_para_la_198.txt"

# LOS CINCO PUESTOS QUE CAYERON FUERA DEL MARCADO DEL AUDITOR Y QUE DISPARAN
# AUDITOR.md 1.2. Leidos de la fila de credito del acta 197, no elegidos aqui.
PUESTOS_DEL_ACTA = [655, 719, 976, 1809, 1810]

# EL UNIVERSO YA CONSUMIDO. SE HEREDA EL DE LA 196 Y SE LE ANADEN LOS DOS DE ESTA
# VUELTA: la lista NO se copia, se importa y se extiende, para que si la 196
# cambia la suya esta la vea.
UNIVERSO_CONSUMIDO = list(UNIVERSO_DE_LA_196) + [
    "docs/loop/SALIDA_V196_T2_CIEGA.txt",
    "docs/loop/_auditor_v197_ciega_blind.txt",
]

# LOS LECTORES QUE LE TOCAN A CADA FICHERO, Y ES LA `C.A5` DEL AUDITOR HECHA
# CODIGO: un fichero de exclusion guarda ENTEROS SUELTOS y se lee con
# `numeros_de()`; una ciega guarda `puesto_intra` y se lee con `puestos_de()`.
def lector_de(rel):
    """QUE LECTOR LE TOCA A UN FICHERO DEL UNIVERSO. PURA. Devuelve el nombre.

    NO ES UNA PREFERENCIA: es la `C.A5` del acta 197, donde el auditor midio que
    con un solo patron para todos el universo sale 300 en vez de 681."""
    return "numeros_de" if "exclusion" in rel else "puestos_de"


# LOS QUEMADOS, DECLARADOS ANTES DE LEER Y CON SU SEDE. Cada uno dice DONDE se
# publico su clase o de donde se deriva, para que la declaracion se pueda
# comprobar y no haya que creersela.
#
# **VAN CATORCE Y NO NUEVE, Y LA DIFERENCIA VA CONTRA MI.** El encargo nombra
# NUEVE (los de la `4.1` y la `5.3`). Los otros CINCO salen de la `4.2` y de la
# `5.3` leidas por mi, y los declaro igual porque el criterio del encargo es
# "los que lleguen con su clase YA SABIDA", no "los que el encargo liste".
QUEMADOS = {
    655: "acta 197, adjudicacion 4.1: una de las NUEVE discrepancias limpias, "
         "las nueve adjudicadas A FAVOR DEL ARCHIVO",
    719: "acta 197, adjudicacion 4.1, Y ADEMAS con su razon: el archivo cita la "
         "REGLA PROPIA del puesto 595, el mismo instrumento en dos ocasiones",
    976: "acta 197, adjudicacion 4.1, Y ADEMAS con su razon: la familia del "
         "sub-puro 7, cuatro pares leidos y los cuatro en A",
    1809: "acta 197, adjudicacion 4.1: discrepancia limpia adjudicada a favor "
          "del archivo",
    1810: "acta 197, adjudicacion 4.1: discrepancia limpia adjudicada a favor "
          "del archivo",
    2838: "acta 197, adjudicacion 4.1, Y ADEMAS con su razon: contencion "
          "invertida, el corto cabe entero en el largo y no trae paso propio",
    2916: "acta 197, adjudicacion 4.1: discrepancia limpia adjudicada a favor "
          "del archivo",
    3072: "acta 197, adjudicacion 4.1: discrepancia limpia adjudicada a favor "
          "del archivo",
    3173: "acta 197, adjudicacion 4.1 y hallazgo 5.3: TRES lectores "
          "independientes contra el archivo, y el acta lo nombra",
    616: "acta 197, adjudicacion 4.2: una de las CUATRO discrepancias quemadas "
         "que el acta publica. NO lo nombra el encargo: lo anado yo",
    2429: "acta 197, adjudicacion 4.2: discrepancia quemada publicada. NO lo "
          "nombra el encargo: lo anado yo",
    2430: "acta 197, adjudicacion 4.2: discrepancia quemada publicada. NO lo "
          "nombra el encargo: lo anado yo",
    2662: "acta 197, adjudicacion 4.2 y hallazgo 5.3: quemada publicada Y tres "
          "lectores contra el archivo. NO lo nombra el encargo: lo anado yo",
    2428: "acta 197, hallazgo 5.3: dice que el auditor COINCIDE con el archivo "
          "en el 2428, o sea publica su clase por la via de la coincidencia. "
          "NO lo nombra el encargo: lo anado yo",
}

CIEGA = "docs/loop/SALIDA_V%d_T3_CIEGA.txt" % VUELTA
DESTAPE = "docs/loop/SALIDA_V%d_T3_DESTAPE.txt" % VUELTA

VARA_DEL_BANCO = (
    "docs/BANCO_DE_TEXTOS.md 9.6.1, LA VARA DE LA RAMA CONTENIDO-MANDA: "
    "LA LINEA O EL PROCEDIMIENTO. Literal: \"Si lo que el hijo añade a lo "
    "que la madre ya dice CABE EN UNA LÍNEA, REPITE. Si trae un "
    "PROCEDIMIENTO que la madre no tiene, CONTINÚA.\"")

LA_VARA_ES_EL_SUELO = (
    "PRIMERO: LA VARA DE CONTENIDO-MANDA ES EL SUELO, NO EL TECHO. ANTES de "
    "aplicarla se pregunta si el par pertenece a una familia con REGLA PROPIA YA "
    "FIJADA, porque entonces manda la especifica. ES LA ESPECIE DEL 719 (la regla "
    "del puesto 595: el mismo instrumento en dos ocasiones distintas es sano) Y "
    "LA DEL 976 (la familia del sub-puro 7, cuatro pares leidos y los cuatro en "
    "A). Consultar la familia NO quema nada, porque las clases de OTROS puestos "
    "no son el sujeto sellado.")

LA_CONTENCION_ES_DEL_CONTENIDO = (
    "SEGUNDO: LA CONTENCION SE MIDE SOBRE EL CONTENIDO, NO SOBRE EL CONTENEDOR. "
    "Si el nodo corto cabe ENTERO en el largo y NO trae ni un paso propio, es A "
    "por contencion, POR MUCHO QUE EL LARGO TRAIGA ADEMAS UN PROCEDIMIENTO "
    "ENTERO. Preguntarse 'el hijo trae procedimiento, luego CONTINUA' mirando el "
    "RESIDUO DEL CONTENEDOR en vez del residuo del contenido es la especie del "
    "2838. La pregunta correcta es QUE QUEDA DEL CORTO si se le quita lo que el "
    "largo ya dijo, y no que le sobra al largo.")

LOS_IDS_NO_DECIDEN = (
    "TERCERO, HEREDADO Y NO RETIRADO: LA SEMEJANZA DE LOS IDS NO DECIDE. El banco "
    "9.6.3 dice que el TAMANO DEL SOLAPE NO DECIDE y que se pesa EL RESTO Y EN "
    "QUE LADO.")

LA_B_EN_SU_SITIO = (
    "LA CLASE B NI SE SALTA NI SE SOBRE EMITE, y el sesgo esta medido en LAS DOS "
    "direcciones y las dos son perdida. B es el par que se pisa sin arista y sin "
    "que ninguno nombre al otro, no un comodin para la duda. La tabla de LOS DOS "
    "POLOS del banco 9.22 va delante de esta lectura.")

CRITERIO = ("relectura AL DOBLE del tramo de la tanda del AUDITOR de la vuelta "
            "197 (AUDITOR.md 1.2, y es DEUDA DEL AUDITOR que paga el ejecutor "
            "con el instrumento): los 120 puestos de "
            "_auditor_v197_ciega_blind.txt MAS sus 120 vecinos deterministas, o "
            "sea DOSCIENTOS CUARENTA pares. EL MOTIVO: CINCO discrepancias del "
            "auditor (655, 719, 976, 1809, 1810) cayeron FUERA de su marcado, "
            "asi que el credito de su tanda baja y el tramo se relee al doble. "
            "La serie medida va 30, 60, 120 y ahora 240. "
            "Los vecinos, elegidos con vecinos() importada de "
            "vuelta182_tarea1c_relectura_al_doble.py sobre el conjunto evitar de "
            "todo lo ya consumido, contado de sus dieciseis ficheros con el "
            "lector que le toca a cada uno, para que el solape con el tramo y "
            "con el universo salga por construccion y no por suerte. "
            "LA VARA CON LA QUE SE LEE, CITADA POR NUMERO Y NO PARAFRASEADA: "
            + VARA_DEL_BANCO + " Y CON SUS PRECISIONES 9.6.2 y 9.6.3 y la tabla "
            "de LOS DOS POLOS del 9.22. "
            + LA_VARA_ES_EL_SUELO + " " + LA_CONTENCION_ES_DEL_CONTENIDO + " "
            + LOS_IDS_NO_DECIDEN + " " + LA_B_EN_SU_SITIO +
            " COMO SE APLICA, y es deliberadamente mecanico: primero se pregunta "
            "si hay regla propia de familia; si no la hay, se lee el paso de la "
            "madre que el hijo desarrolla y se pregunta si es una linea o si ya "
            "trae el procedimiento; se lee el nodo hijo entero y se pregunta que "
            "queda si se le quita lo que la madre ya dijo; y de lo que queda se "
            "pregunta si cabe en una linea o si es una secuencia de acciones con "
            "su propia logica.")

# LOS DOS LITERALES QUE EL BARRIDO DE (f) BUSCA EN LA RAZON, Y NADA MAS.
LITERALES_INALCANZABLE = ("RACIMO", "CORRECCION DECLARADA", "CORRECCIÓN DECLARADA")
LITERAL_MARCADO = "DISCUTIBLE MARCADO"


def sha_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    datos = io.open(p, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest(),
            hashlib.sha256(datos).hexdigest())


def doble_de_la_sellada(rel=None):
    """LOS VECINOS QUE LA SELLADA DEL AUDITOR PUBLICA. PURA salvo por leer el
    fichero. Se lee SOLO la linea que empieza por `EL DOBLE:`, **CON SUS DOS
    PUNTOS**, y esa es la diferencia con el lector de la 196.

    POR QUE HIZO FALTA CAMBIARLO, MEDIDO Y NO SUPUESTO: la sellada de la 197 se
    TITULA *"EL DOBLE DEL TRAMO DEL AUDITOR 197, CERRADO HOY..."*, o sea que su
    PRIMERA LINEA tambien empieza por `EL DOBLE`. El lector de la 196 casa con esa
    primera linea, no encuentra dos puntos en ella, devuelve la lista VACIA y se
    para ahi. **Resultado: cero vecinos leidos de una sellada que publica 120**, y
    el cotejo habria publicado un `NO CALZA` falso contra una sellada correcta.
    ESA CIFRA SE PUBLICA AL LADO DEL COTEJO: las dos lecturas se corren."""
    p = os.path.join(RAIZ, (rel or SELLADA_DEL_DOBLE).replace("/", os.sep))
    if not os.path.isfile(p):
        return []
    for l in io.open(p, encoding="utf-8", errors="replace"):
        if l.strip().startswith("EL DOBLE:"):
            crudo = l.split(":", 1)[1]
            return sorted(int(x) for x in re.findall(r"\d+", crudo))
    return []


def doble_de_la_sellada_lector_196(rel=None):
    """EL LECTOR DE LA 196, TAL CUAL, PARA PODER PUBLICAR SU CIFRA AL LADO.
    NO SE RETIRA NINGUNO: las dos lecturas se corren y las dos se publican."""
    p = os.path.join(RAIZ, (rel or SELLADA_DEL_DOBLE).replace("/", os.sep))
    if not os.path.isfile(p):
        return []
    for l in io.open(p, encoding="utf-8", errors="replace"):
        if l.strip().startswith("EL DOBLE"):
            crudo = l.split(":", 1)[1] if ":" in l else ""
            return sorted(int(x) for x in re.findall(r"\d+", crudo))
    return []


def barrido_de_razones(filas, universo, literales):
    """LOS PUESTOS DEL UNIVERSO CUYA RAZON CITA ALGUNO DE LOS LITERALES. PURA.

    **NO DEVUELVE NI LA CLASE NI EL TEXTO DE LA RAZON**, y eso es lo unico que
    permite correrlo antes de leer: lo que sale es el NUMERO del puesto y nada
    mas. Un barrido que devolviera la razon seria un destape con otro nombre."""
    dentro = set(universo)
    salida = []
    for f in filas:
        p = f.get("puesto_intra")
        if p not in dentro:
            continue
        razon = (f.get("razon") or "").upper()
        if any(lit.upper() in razon for lit in literales):
            salida.append(p)
    return sorted(salida)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 3: EL SUJETO DE LA RELECTURA AL DOBLE DEL TRAMO DEL"
      % VUELTA)
    w("AUDITOR DE LA 197. Deuda suya por AUDITOR.md 1.2, pagada con instrumento.")
    w("SON DOSCIENTOS CUARENTA PARES: la serie medida va 30, 60, 120 y ahora 240.")
    w("=" * 78)
    w("")

    w("A) EL ARCHIVO, MEDIDO AL ENTRAR Y ABIERTO SOLO EN LECTURA")
    a = sha_de(ARCHIVO)
    w("   %s -> disco %d bytes | LF %d bytes" % (ARCHIVO, a[0], a[1]))
    w("   sha256 LF    : %s" % a[2])
    w("   sha256 disco : %s" % a[3])
    filas = [json.loads(l) for l in
             io.open(os.path.join(RAIZ, ARCHIVO.replace("/", os.sep)),
                     encoding="utf-8") if l.strip()]
    puestos_archivo = sorted(f.get("puesto_intra") for f in filas)
    w("   CIFRA filas: %d | MIN %d | MAX %d"
      % (len(filas), puestos_archivo[0], puestos_archivo[-1]))
    w("")

    w("B) EL TRAMO, CONTADO DE SU FICHERO Y NO TECLEADO")
    tramo = puestos_de(TRAMO)
    t = sha_de(TRAMO)
    w("   %s" % TRAMO)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s" % (t[0], t[1], t[2][:16]))
    w("   CIFRA puestos del tramo: %d" % len(tramo))
    w("   %s" % ", ".join(str(x) for x in tramo))
    fuera_del_tramo = [p for p in PUESTOS_DEL_ACTA if p not in tramo]
    for p in PUESTOS_DEL_ACTA:
        w("   EL PUESTO %d, DE LOS CINCO FUERA DEL MARCADO: %s del tramo"
          % (p, "DENTRO" if p in tramo else "FUERA"))
    if fuera_del_tramo:
        w("   PARADA: los puestos %s que el acta nombra no estan en el tramo."
          % ", ".join(str(x) for x in fuera_del_tramo))
        print(NL.join(L))
        return 1
    w("")

    w("C) EL UNIVERSO YA CONSUMIDO, CONTADO DE SUS DIECISEIS FICHEROS, Y CON EL")
    w("   LECTOR QUE LE TOCA A CADA UNO. ES LA `C.A5` DEL AUDITOR ESQUIVADA CON")
    w("   SU CIFRA DELANTE: con un solo patron el universo sale 300 en vez de 681.")
    evitar = set()
    vistos = 0
    con_un_solo_patron = set()
    for rel in UNIVERSO_CONSUMIDO:
        s = sha_de(rel)
        if s is None:
            w("   %-48s NO EXISTE" % rel)
            continue
        vistos += 1
        cual = lector_de(rel)
        nums = numeros_de(rel) if cual == "numeros_de" else puestos_de(rel)
        dentro = [x for x in nums if 1 <= x <= puestos_archivo[-1]]
        evitar |= set(dentro)
        con_un_solo_patron |= set(x for x in puestos_de(rel)
                                  if 1 <= x <= puestos_archivo[-1])
        w("   %-48s %7d bytes | %-11s | %4d dentro"
          % (rel, s[0], cual, len(dentro)))
    w("   CIFRA ficheros del universo que EXISTEN: %d de %d"
      % (vistos, len(UNIVERSO_CONSUMIDO)))
    w("   CIFRA universo consumido, CON EL LECTOR QUE LE TOCA A CADA UNO: %d"
      % len(evitar))
    w("   CIFRA universo consumido, CON UN SOLO PATRON PARA TODOS: %d"
      % len(con_un_solo_patron))
    w("   ESA ES LA TRAMPA DE LA `C.A5`, MEDIDA AQUI Y NO CREIDA: la diferencia")
    w("   es de %d puestos, y con la cifra corta el `solape 0 por construccion`"
      % (len(evitar) - len(con_un_solo_patron)))
    w("   seria falso.")
    w("   LA SELLADA DEL AUDITOR DICE 681 -> %s"
      % ("CALZA" if len(evitar) == 681 else "NO CALZA, y manda la mia"))
    sin_puestos = len(evitar - set(tramo))
    w("   CIFRA universo menos los %d puestos del tramo, POR DIFERENCIA DE"
      % len(tramo))
    w("   CONJUNTOS: %d" % sin_puestos)
    w("   LA SELLADA DEL AUDITOR DICE 561 -> %s"
      % ("CALZA" if sin_puestos == 561 else "NO CALZA, y manda la mia"))
    w("")

    w("D) LOS VECINOS DETERMINISTAS, CON vecinos() IMPORTADA Y NO COPIADA")
    elegidos = vecinos(tramo, puestos_archivo[-1], evitar=evitar)
    w("   CIFRA vecinos elegidos: %d" % len(elegidos))
    w("   %s" % ", ".join(str(x) for x in elegidos))
    w("   AL DOBLE: %d del tramo mas %d vecinos = %d puestos"
      % (len(tramo), len(elegidos), len(tramo) + len(elegidos)))
    w("   ES EL DOBLE EXACTO: %s" % ("SI" if len(elegidos) == len(tramo) else "NO"))
    w("   SOLAPE de los vecinos con el propio tramo: %d"
      % len(set(elegidos) & set(tramo)))
    w("   SOLAPE de los vecinos con el universo consumido: %d"
      % len(set(elegidos) & evitar))
    w("   (los dos ceros salen POR CONSTRUCCION: `evitar` va DENTRO de la")
    w("    llamada, no comprobado despues)")
    todos_existen = all(p in set(puestos_archivo) for p in elegidos)
    w("   TODOS los vecinos existen en el archivo: %s"
      % ("SI" if todos_existen else "NO"))
    if not elegidos or not todos_existen:
        w("   PARADA: la seleccion sale vacia o nombra un puesto que no existe.")
        print(NL.join(L))
        return 1
    w("")

    w("D.1) EL COTEJO CONTRA LA SELLADA DEL AUDITOR, QUE NO SE COPIA")
    sellado = doble_de_la_sellada()
    sellado_196 = doble_de_la_sellada_lector_196()
    s = sha_de(SELLADA_DEL_DOBLE)
    w("   %s" % SELLADA_DEL_DOBLE)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s"
      % (s[0], s[1], s[2][:16]) if s else "      NO EXISTE")
    w("   CIFRA vecinos que la sellada publica, CON EL LECTOR DE LA 196: %d"
      % len(sellado_196))
    w("   CIFRA vecinos que la sellada publica, CON EL LECTOR DE ESTA VUELTA: %d"
      % len(sellado))
    w("   POR QUE HUBO QUE ESCRIBIR UN LECTOR, Y ES UNA MEDICION: la sellada de")
    w("   la 197 SE TITULA `EL DOBLE DEL TRAMO DEL AUDITOR 197...`, asi que su")
    w("   PRIMERA LINEA tambien empieza por `EL DOBLE`. El lector de la 196 casa")
    w("   con el titulo, no encuentra dos puntos, y devuelve la lista VACIA: el")
    w("   cotejo habria publicado un NO CALZA FALSO contra una sellada correcta.")
    w("   El lector de esta vuelta exige `EL DOBLE:` con sus dos puntos. LAS DOS")
    w("   CIFRAS SE PUBLICAN Y NINGUN LECTOR SE RETIRA.")
    calza = set(sellado) == set(elegidos)
    w("   MI RECOMPUTACION Y LA SELLADA SON EL MISMO CONJUNTO: %s"
      % ("SI" if calza else "NO"))
    if not calza:
        w("   SOLO EN LA SELLADA: %s"
          % ", ".join(str(x) for x in sorted(set(sellado) - set(elegidos))))
        w("   SOLO EN LA MIA:     %s"
          % ", ".join(str(x) for x in sorted(set(elegidos) - set(sellado))))
        w("   SE PUBLICA LA MIA CON SUS FICHEROS, Y LA DISCREPANCIA SE DECLARA")
        w("   EN VEZ DE RESOLVERSE COPIANDO (EJECUTOR.md 2).")
    w("")

    universo = sorted(set(tramo) | set(elegidos))

    w("D.2) LOS QUEMADOS (pieza `g`), DECLARADOS AQUI Y NO DESPUES DE COTEJAR")
    w("   UN PUESTO CUYA CLASE YA ME DIJERON NO PRUEBA QUE YO LEA BIEN, asi que")
    w("   SALE DEL CREDITO. Se lee igual y su clase se publica igual.")
    w("   VAN CATORCE Y EL ENCARGO NOMBRA NUEVE, Y LA DIFERENCIA VA CONTRA MI:")
    w("   los cinco de mas salen de la `4.2` y la `5.3` leidas por mi. El")
    w("   criterio es 'los que lleguen con su clase YA SABIDA', no 'los que el")
    w("   encargo liste'.")
    quemados_dentro = sorted(k for k in QUEMADOS if k in set(universo))
    quemados_fuera = sorted(k for k in QUEMADOS if k not in set(universo))
    for k in sorted(QUEMADOS):
        w("   %-5d %s -> %s" % (k, "DENTRO" if k in set(universo) else "FUERA",
                                QUEMADOS[k]))
    w("   CIFRA quemados declarados: %d" % len(QUEMADOS))
    w("   CIFRA quemados DENTRO de los %d: %d"
      % (len(universo), len(quemados_dentro)))
    w("   CIFRA quemados FUERA: %d" % len(quemados_fuera))
    w("   CIFRA los NUEVE que el encargo nombra y que estan dentro: %d"
      % len([k for k in (655, 719, 976, 1809, 1810, 2838, 2916, 3072, 3173)
             if k in set(universo)]))
    w("")

    w("D.3) LOS INALCANZABLES A CIEGAS (pieza `f`), CONTADOS ANTES DE LEER")
    w("   EL BARRIDO MIRA SOLO SI LA RAZON CITA UN RACIMO O UNA CORRECCION")
    w("   DECLARADA, Y NO DEVUELVE NI LA CLASE NI EL TEXTO DE LA RAZON. Lo que")
    w("   sale es el NUMERO del puesto y la cuenta, y nada mas: un barrido que")
    w("   devolviera la razon seria un destape con otro nombre.")
    w("   Y NO SE ENSANCHA LA LISTA BLANCA DEL AISLADOR, que entregaria la")
    w("   respuesta: eso lo prohibe la adjudicacion `4.4` del acta 197.")
    racimo = barrido_de_razones(filas, universo, ("RACIMO",))
    correccion = barrido_de_razones(filas, universo,
                                    ("CORRECCION DECLARADA",
                                     "CORRECCIÓN DECLARADA"))
    inalcanzables = sorted(set(racimo) | set(correccion))
    w("   CIFRA razones de los %d que citan un RACIMO: %d" % (len(universo), len(racimo)))
    w("      %s" % (", ".join(str(x) for x in racimo) or "(ninguno)"))
    w("   CIFRA razones que citan una CORRECCION DECLARADA: %d" % len(correccion))
    w("      %s" % (", ".join(str(x) for x in correccion) or "(ninguno)"))
    w("   CIFRA INALCANZABLES A CIEGAS, union de los dos: %d" % len(inalcanzables))
    w("   SOBRE LOS 120 DE LA 197 EL AUDITOR MIDIO 6 Y 3. Aqui son %d y %d sobre"
      % (len(racimo), len(correccion)))
    w("   %d puestos, y la comparacion se publica sin resolverla." % len(universo))
    w("")

    w("D.4) EL REPARTO DEL MARCADO (pieza `e`), QUE EL HALLAZGO `5.2` OBLIGA")
    w("   EL HALLAZGO DICE: de los 120 del auditor, 14 llevan el literal")
    w("   `DISCUTIBLE MARCADO` y LOS 14 SON DEL 2662 PARA ARRIBA, con 0 en los 89")
    w("   puestos por debajo. Si el reparto sale igual sobre estos %d, LA METRICA"
      % len(universo))
    w("   DE DENTRO-O-FUERA NO ES COMPARABLE ENTRE TRAMOS, y esa cifra tiene que")
    w("   estar PUBLICADA y no deducida.")
    marcados = barrido_de_razones(filas, universo, (LITERAL_MARCADO,))
    w("   CIFRA de los %d que llevan %r: %d"
      % (len(universo), LITERAL_MARCADO, len(marcados)))
    w("   cuales: %s" % (", ".join(str(x) for x in marcados) or "(ninguno)"))
    corte = 2662
    arriba = [x for x in marcados if x >= corte]
    abajo = [x for x in marcados if x < corte]
    bajo_total = [x for x in universo if x < corte]
    alto_total = [x for x in universo if x >= corte]
    w("   REPARTO POR PUESTO, con el corte del hallazgo (%d):" % corte)
    w("      del %d PARA ARRIBA: %d marcados de %d puestos"
      % (corte, len(arriba), len(alto_total)))
    w("      por DEBAJO del %d : %d marcados de %d puestos"
      % (corte, len(abajo), len(bajo_total)))
    w("   EL REPARTO SALE IGUAL QUE EL DEL AUDITOR (todo arriba, cero abajo): %s"
      % ("SI" if abajo == [] and arriba else "NO"))
    w("")

    w("E) EL AISLAMIENTO DE LOS %d, CON aislador_de_ciega.py" % len(universo))
    w("   CIFRA puestos que van a la ciega: %d" % len(universo))
    lista = ",".join(str(x) for x in universo)
    cmd = [PY, "scripts/loop/aislador_de_ciega.py",
           "--criterio", CRITERIO,
           "--ciega", CIEGA, "--destape", DESTAPE,
           "--puestos", lista]
    w("   comando: aislador_de_ciega.py --criterio <el de arriba> --ciega %s" % CIEGA)
    w("            --destape %s --puestos <los %d puestos>" % (DESTAPE, len(universo)))
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, env=env)
    salida = (r.stdout.decode("utf-8", errors="replace")
              + r.stderr.decode("utf-8", errors="replace"))
    for l in salida.replace(chr(13) + NL, NL).split(NL):
        if l.strip():
            w("      | " + l.rstrip())
    w("   exitcode del aislador: %d" % r.returncode)
    if r.returncode != 0:
        w("   PARADA: el aislador cayo en rojo. No se lee nada.")
        print(NL.join(L))
        return 1
    for rel in (CIEGA, DESTAPE):
        m = sha_de(rel)
        if m is None:
            w("   ROJO: %s NO EXISTE tras el aislador" % rel)
        else:
            w("   %s -> disco %d bytes | LF %d bytes | sha256 LF %s"
              % (rel, m[0], m[1], m[2][:16]))
            w("      LA RUTA QUE PROMETE PRUEBA ES CIFRA: no esta vacia: %s"
              % ("SI" if m[0] > 0 else "NO, CERO BYTES"))
    w("")

    w("F) EL ARCHIVO AL SALIR, REMEDIDO Y NO SUPUESTO")
    b = sha_de(ARCHIVO)
    w("   sha256 LF al entrar: %s" % a[2][:16])
    w("   sha256 LF al salir : %s" % b[2][:16])
    w("   NO SE MOVIO NINGUN VEREDICTO: %s" % ("SI" if a[2] == b[2] else "NO"))
    w("")
    w("G) LO QUE FALTA, Y LO HACE EL EJECUTOR CON LAS MANOS")
    w("   Este fichero NO LEE EL DESTAPE. Escribe la ciega y el destape y los")
    w("   deja cerrados. Las clases se escriben en un tercer fichero ANTES de")
    w("   abrir el destape, y ese orden es lo unico que hace que el cotejo valga.")
    w("")
    w("FIN")

    texto = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T3_SUJETO.txt" % VUELTA)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(texto.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
