# -*- coding: utf-8 -*-
r"""_v212_t2_cola_relectura.py . LA COLA DE RELECTURA DE LA VUELTA 212.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo y fuera de la
nomina (congelada en 135). Moratoria de AUDITOR.md 6.3.

ESTA TAREA SOLO EXISTE SI LA `1.b` CONFIRMO, y por eso este fichero NO ARRANCA
sin leer esa confirmacion de la salida sellada de la `1.b`.

QUE HACE, Y ES LECTURA Y CITA, NO RE-CRIBADO (el encargo lo dice con esas
palabras): toma las CUATRO razones en clase `A` que nombran el cero-enlazados,
las lista con su puesto, sus dos nodos y su razon entera, y publica DE QUE
depende la clase de cada una, CITANDO LA FRASE DE SU PROPIA RAZON. No cambia ni
una clase: si alguna dependiera de la silueta, se marca DISCUTIBLE y se trae.

LA LISTA DE LOS CUATRO NO SE TECLEA: se LEE de la linea de la salida de la `1.b`
que la publica, y si esa linea no esta, este fichero cae en rojo.

TODA TABLA QUE ESTE FICHERO ARMA LEYENDO FILAS DICE, EN LA MISMA LINEA, CUANTAS
FILAS ARMO, Y AL LADO LA CIFRA DE CUANTAS DEBERIA HABER.
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402
from _v211_apertura import shas                         # noqa: E402

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
ARCHIVO = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
SALIDA_1B = "docs/loop/SALIDA_V%d_T1B_PUESTO_730.txt" % VUELTA
PUESTO_YA_CORREGIDO = 730

# LAS FRASES QUE DELATAN DE QUE CUELGA UNA CLASE. No son un juicio: son anclas
# de busqueda, y lo que se publica es LA FRASE ENTERA que cada ancla encuentra.
ANCLAS_SILUETA = [
    "la figura NO APLICA",
    "manda la regla original",
    "SIN ARISTA igual a DUPLICACION",
    "sin arista igual a duplicacion",
    "PROPORCION: CERO enlazados",
]
ANCLAS_CONTENIDO = [
    "la vara CONFIRMA",
    "es UNA LINEA",
    "REPITE ademas",
    "repite ademas",
    "LA VARA del banco 9.6.1, la linea o el procedimiento",
    "manda el contenido",
]

OUT = []


def di(s=""):
    OUT.append(s)


def frases_con(razon, anclas):
    """LAS FRASES DE UNA RAZON QUE CONTIENEN ALGUNA DE LAS ANCLAS. PURA.
    Corta por punto y devuelve (ancla, frase) sin repetir frase."""
    trozos = [t.strip() for t in razon.split(". ") if t.strip()]
    vistos = set()
    salida = []
    for a in anclas:
        for t in trozos:
            if a in t and t not in vistos:
                vistos.add(t)
                salida.append((a, t))
    return salida


def main():
    di("=" * 78)
    di("TAREA 2 DE LA VUELTA %d. LA COLA DE RELECTURA, BAJO LA REGLA QUE LA 730 DEJA."
       % VUELTA)
    di("=" * 78)
    di("")

    di("## 0. LA PUERTA: ESTA TAREA SOLO SE ABRE SI LA 1.b CONFIRMO")
    p1b = os.path.join(RAIZ, SALIDA_1B.replace("/", os.sep))
    if not os.path.isfile(p1b):
        di("ROJO: no existe %s. La tarea no se abre." % SALIDA_1B)
        return 1
    med = io.open(p1b, encoding="utf-8").read()
    _m1b = medir_en_disco(RAIZ, SALIDA_1B)
    _s1b = shas(SALIDA_1B)
    di("CIFRA sede %s: %d bytes en disco y %d normalizado a LF (%s), sha256 disco "
       "%s y sha256 LF %s" % (SALIDA_1B, _m1b[0], _m1b[1],
                              "COINCIDEN" if _m1b[0] == _m1b[1] else "NO COINCIDEN",
                              _s1b[0], _s1b[1]))
    confirma = "CONFIRMA: SI" in med
    di("CIFRA la 1.b dice CONFIRMA: SI: %s" % ("SI" if confirma else "NO"))
    if not confirma:
        di("La 1.b TUMBA el cambio: esta tarea NO EXISTE y asi se escribe en el reporte.")
        return 2
    di("")

    di("## 1. LOS CUATRO, LEIDOS DE LA LINEA DE LA 1.b QUE LOS PUBLICA")
    m = re.search(r"CIFRA razones en clase A que nombran el cero-enlazados "
                  r"\(patron holgado\): (\d+), y son ([0-9, ]+)", med)
    if not m:
        di("ROJO: la linea que publica los cuatro no esta en la salida de la 1.b.")
        return 1
    cuantos = int(m.group(1))
    cuatro = [int(x) for x in m.group(2).split(",")]
    di("   linea leida> %s" % m.group(0))
    di("CIFRA puestos leidos de esa linea: %d, y la cifra que la propia linea declara "
       "es %d (se exige que sean iguales)" % (len(cuatro), cuantos))
    if len(cuatro) != cuantos:
        di("ROJO: la lista y su cifra no calzan.")
        return 1
    di("")

    di("## 2. EL ARCHIVO, MEDIDO HOY")
    filas = [json.loads(l) for l in
             io.open(os.path.join(RAIZ, ARCHIVO.replace("/", os.sep)),
                     encoding="utf-8") if l.strip()]
    di("CIFRA filas de %s: %d" % (ARCHIVO, len(filas)))
    mm = medir_en_disco(RAIZ, ARCHIVO)
    sd, sl = shas(ARCHIVO)
    di("CIFRA sede %s: %d bytes en disco y %d normalizado a LF (%s), sha256 disco %s "
       "y sha256 LF %s" % (ARCHIVO, mm[0], mm[1],
                           "COINCIDEN" if mm[0] == mm[1] else "NO COINCIDEN", sd, sl))
    por_puesto = {f["puesto_intra"]: f for f in filas}
    di("")

    di("LA TABLA DE LOS CUATRO CON SU CLASE DE HOY: %d fila(s) armada(s), y la cifra "
       "de al lado dice que deberian ser %d" % (len(cuatro), cuantos))
    hoy_en_a = []
    for p in cuatro:
        f = por_puesto[p]
        nota = ""
        if p == PUESTO_YA_CORREGIDO:
            nota = " (era A en la apertura de esta vuelta y la 1.b lo paso a D)"
        if f["clase"] == "A":
            hoy_en_a.append(p)
        di("   cuatro> puesto %d clase HOY %s%s" % (p, f["clase"], nota))
    di("CIFRA de los %d, cuantos siguen en A despues de la 1.b: %d (%s)"
       % (len(cuatro), len(hoy_en_a),
          ", ".join(str(x) for x in hoy_en_a)))
    di("CIFRA los que quedan por mirar en esta tarea, o sea los cuatro menos el 730: "
       "%d" % len(hoy_en_a))
    di("")

    di("## 3. UNO A UNO: SU RAZON ENTERA Y DE QUE DEPENDE SU CLASE")
    di("")
    dependen_de_silueta = []
    for p in hoy_en_a:
        f = por_puesto[p]
        di("### PUESTO %d" % p)
        di("CIFRA clase %s | dominio %s | clave %s" % (f["clase"], f["dominio"], f["clave"]))
        di("CIFRA nodo_a: %s" % f["nodo_a"])
        di("CIFRA nodo_b: %s" % f["nodo_b"])
        di("CIFRA bytes de su razon: %d" % len(f["razon"].encode("utf-8")))
        di("RAZON ENTERA, pegada sin cortar:")
        di("   " + f["razon"])
        di("")
        fs = frases_con(f["razon"], ANCLAS_SILUETA)
        fc = frases_con(f["razon"], ANCLAS_CONTENIDO)
        di("LA TABLA DE FRASES DE SILUETA: %d fila(s) armada(s) sobre %d anclas "
           "buscadas" % (len(fs), len(ANCLAS_SILUETA)))
        for a, t in fs:
            di("   silueta> [%s] %s" % (a, t))
        di("LA TABLA DE FRASES DE CONTENIDO: %d fila(s) armada(s) sobre %d anclas "
           "buscadas" % (len(fc), len(ANCLAS_CONTENIDO)))
        for a, t in fc:
            di("   contenido> [%s] %s" % (a, t))
        di("")

    di("## 4. LO QUE ESTAS CIFRAS DEJAN MEDIDO, PARA QUE EL VEREDICTO NO SEA UNA")
    di("   IMPRESION")
    di("LA TABLA DEL REPARTO DE FRASES: %d fila(s) armada(s) sobre los %d puestos que "
       "quedan por mirar" % (len(hoy_en_a), len(hoy_en_a)))
    for p in hoy_en_a:
        f = por_puesto[p]
        ns = len(frases_con(f["razon"], ANCLAS_SILUETA))
        nc = len(frases_con(f["razon"], ANCLAS_CONTENIDO))
        cierra_por = "CONTENIDO" if ("la vara CONFIRMA" in f["razon"]
                                     or "REPITE ademas" in f["razon"]
                                     or "repite ademas" in f["razon"]) else "SIN CIERRE DE CONTENIDO"
        di("   reparto> puesto %d: frases de silueta %d, frases de contenido %d, "
           "y la frase que CIERRA su clase es de %s" % (p, ns, nc, cierra_por))
        if cierra_por != "CONTENIDO":
            dependen_de_silueta.append(p)
    di("CIFRA puestos cuya clase NO cierra por contenido: %d (%s)"
       % (len(dependen_de_silueta),
          ", ".join(str(x) for x in dependen_de_silueta) or "ninguno"))
    di("")
    di("CIFRA clases cambiadas por esta tarea: 0. Esta tarea NO CAMBIA NINGUNA CLASE, "
       "y el archivo sale con el mismo sha256 con el que entro a ella.")
    _sf = shas(ARCHIVO)
    di("CIFRA sha256 del archivo al cerrar la TAREA 2: %s en disco y %s normalizado "
       "a LF (el mismo que arriba: %s)"
       % (_sf[0], _sf[1], "SI" if _sf[0] == sd and _sf[1] == sl else "NO"))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    codigo = main()
    texto = NL.join(OUT) + NL
    io.open(os.path.join(RAIZ, "docs", "loop",
                         "SALIDA_V%d_T2_COLA_RELECTURA.txt" % VUELTA),
            "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write("EXITCODE: %d%s" % (codigo, NL))
    sys.exit(codigo)
