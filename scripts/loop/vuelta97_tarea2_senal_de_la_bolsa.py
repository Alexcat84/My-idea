# -*- coding: utf-8 -*-
r"""vuelta97_tarea2_senal_de_la_bolsa.py . VUELTA 97, TAREA 2: MIDE LA SENIAL DE
LA BOLSA POR TRAMO, Y CRUZA ESA SENIAL CONTRA LOS VEREDICTOS DE DIRECCION QUE LA
LECTURA YA ESCRIBIO.

POR QUE NACE, y se dice sin adornarlo. El tramo 1 (vuelta 96) dejo 11 de 40
direcciones NO RESUELTAS, 27,5 por ciento, y el acta de la vuelta 96 seccion 4.4
(docs/loop/ACTA_AUDITOR.md linea 34367) adjudico que ese umbral ESTA BIEN PUESTO
Y NO SE TOCA. El encargo de la vuelta 97 anadio la letra que este instrumento
sirve: "Si el segundo tramo da otra proporcion parecida, es la bolsa, no tu
vara". EL TRAMO 2 NO DA UNA PROPORCION PARECIDA: da mas. Este instrumento existe
para que esa frase se pueda MEDIR en vez de opinarse, y para que si la medicion
no sostiene la explicacion, se vea.

QUE MIDE, EXACTO Y NADA MAS. Dos cosas, y las dos sobre datos que ya existen:

  (1) LA SENIAL DE LA BOLSA POR TRAMO. Para cada tramo de
      docs/plan/DIFERENCIA_CONTRA_COLA.jsonl (1 a 40, 41 a 100, 101 a 183), la
      MEDIANA de titulo_ratio y el porcentaje de filas cuya madre y cuyo hijo
      salen de la MISMA fuente bibliografica. Los ids pasan por el RESOLUTOR
      antes de leer nada del grafo (P.1).

  (2) EL CRUCE CONTRA LA LECTURA. Dentro del tramo 2, parte las 60 filas en las
      que la lectura dejo con DIRECCION LEIDA y las que dejo NO RESUELTA (leidas
      de docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl, no de una lista tecleada) y
      mide las MISMAS dos cifras en cada mitad.

LAS DOS AFIRMACIONES QUE COMPRUEBA, y las dos PUEDEN SALIR EN ROJO:

  AFIRMACION 1, sobre la bolsa: la mediana de titulo_ratio del tramo 2 es
    ESTRICTAMENTE MENOR que la del tramo 1. Si sale falsa, la bolsa no se debilita
    y la explicacion "es la bolsa" pierde su primera pata.
  AFIRMACION 2, sobre el cruce: entre las filas del tramo 2, el porcentaje de
    MISMA FUENTE es ESTRICTAMENTE MENOR en el grupo NO RESUELTA que en el grupo
    LEIDA. Si sale falsa, la senial no predice la lectura y "es la bolsa" pierde
    su segunda pata.

LO QUE ESTE INSTRUMENTO NO PRUEBA, Y SE DICE PARA QUE NADIE LO LEA DE MAS: NO
prueba que el umbral del ejecutor sea el correcto. Una vara demasiado estricta
aplicada a una bolsa que se debilita produciria exactamente estas mismas dos
seniales. Lo unico que mide es si la bolsa se debilita y si la senial objetiva
acompania a la lectura; la correccion del umbral la adjudica el auditor, no este
fichero.

MECANICA DE ROJO: si falta un fichero, si un id no existe en el grafo tras
resolver, o si el fichero de lectura no tiene exactamente las 60 filas del tramo,
NO SE TALLA NADA y sale con exit 1. Las dos afirmaciones se imprimen con su
veredicto (VERIFICADA o NO SE SOSTIENE) y NO abortan: son medicion, no guarda.
Su caso rojo se prueba por mutacion en
scripts/loop/vuelta97_tarea2_prueba_mutacion.py.

USO:
  python scripts/loop/vuelta97_tarea2_senal_de_la_bolsa.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
BOLSA = os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")
LECTURA = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl")

TRAMOS = [("tramo 1 (filas 1 a 40)", 0, 40),
          ("tramo 2 (filas 41 a 100)", 40, 100),
          ("sin leer (filas 101 a 183)", 100, None)]


def cargar_jsonl(ruta, fallos):
    if not os.path.exists(ruta):
        fallos.append("no existe %s" % os.path.relpath(ruta, RAIZ).replace("\\", "/"))
        return []
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def construir_resolutor(nodos):
    """P.1, misma semantica de resolverId que el resto del bucle."""
    alias = {a: k for k, v in nodos.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x
    return res


def normaliza_fuente(s):
    """LA UNICA PIEZA DE JUICIO DE ESTE INSTRUMENTO, aislada para que su rojo se
    pueda probar por mutacion. El campo fuente del grafo trae la misma obra
    escrita de formas distintas ('Juran's Quality Handbook_ The C - Joseph A.
    Defeo' y variantes), asi que se corta por el primer separador y se recorta,
    que es lo que hace comparables dos filas de la MISMA obra sin fundir obras
    distintas."""
    s = (s or "").split(" - ")[0].split("_")[0].strip().lower()
    return s[:22]


def mediana(xs):
    if not xs:
        return 0.0
    ys = sorted(xs)
    n = len(ys)
    if n % 2:
        return float(ys[n // 2])
    return (ys[n // 2 - 1] + ys[n // 2]) / 2.0


def medir(filas, nodos, res, fallos, etiqueta):
    ratios, misma = [], 0
    for r in filas:
        m, h = res(r["madre"]), res(r["hijo"])
        for crudo, resuelto in ((r["madre"], m), (r["hijo"], h)):
            if resuelto not in nodos:
                fallos.append("%s: el nodo %r (resuelto %r) no existe en el grafo"
                              % (etiqueta, crudo, resuelto))
                return None
        ratios.append(r.get("titulo_ratio") or 0.0)
        if normaliza_fuente(nodos[m].get("fuente")) == normaliza_fuente(nodos[h].get("fuente")):
            misma += 1
    n = len(filas)
    return {"n": n, "mediana_ratio": mediana(ratios),
            "misma_fuente": misma,
            "pct_misma_fuente": (100.0 * misma / n) if n else 0.0}


def main():
    fallos = []
    if not os.path.exists(GRAFO):
        print("ROJO: no existe el grafo")
        return 1
    nodos = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    res = construir_resolutor(nodos)

    bolsa = cargar_jsonl(BOLSA, fallos)
    lectura = cargar_jsonl(LECTURA, fallos)
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE TALLA NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    tramo2 = bolsa[40:100]
    if len(lectura) != len(tramo2):
        print("ROJO: el fichero de lectura trae %d filas y el tramo 2 tiene %d."
              % (len(lectura), len(tramo2)))
        return 1

    # (1) LA SENIAL DE LA BOLSA POR TRAMO
    medidas = []
    for nombre, a, b in TRAMOS:
        sl = bolsa[a:b] if b is not None else bolsa[a:]
        m = medir(sl, nodos, res, fallos, nombre)
        if m is None:
            break
        medidas.append((nombre, m))
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE TALLA NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    print("=" * 100)
    print("LA SENIAL DE LA BOLSA POR TRAMO (vuelta 97, TAREA 2)")
    print("Fuente: docs/plan/DIFERENCIA_CONTRA_COLA.jsonl (%d filas) mas el grafo." % len(bolsa))
    print("Ids resueltos por el RESOLUTOR antes de leer la fuente de cada nodo (P.1).")
    print("=" * 100)
    print()
    print("| tramo | filas | mediana de titulo_ratio | madre e hijo de la MISMA fuente |")
    print("|---|---:|---:|---:|")
    for nombre, m in medidas:
        print("| %s | %d | %.1f | %d de %d (%.1f%%) |"
              % (nombre, m["n"], m["mediana_ratio"], m["misma_fuente"], m["n"], m["pct_misma_fuente"]))
    print()

    # (2) EL CRUCE CONTRA LA LECTURA YA ESCRITA
    por_puesto = {r["puesto_tramo"]: r for r in lectura}
    leidas, no_resueltas = [], []
    for i, r in enumerate(tramo2, start=41):
        v = por_puesto.get(i)
        if v is None:
            print("ROJO: falta el veredicto del puesto %d en el fichero de lectura." % i)
            return 1
        (leidas if v.get("direccion_leida") else no_resueltas).append(r)

    m_leidas = medir(leidas, nodos, res, fallos, "LEIDA")
    m_no = medir(no_resueltas, nodos, res, fallos, "NO RESUELTA")
    if fallos:
        print("ROJO, %d cosa(s) no cuadran:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    print("=" * 100)
    print("EL CRUCE: LA SENIAL DE CADA MITAD DEL TRAMO 2, PARTIDA POR LO QUE LA LECTURA DECIDIO")
    print("Las mitades salen de docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl, no de una lista tecleada.")
    print("=" * 100)
    print()
    print("| grupo del tramo 2 | filas | mediana de titulo_ratio | madre e hijo de la MISMA fuente |")
    print("|---|---:|---:|---:|")
    for nombre, m in (("direccion LEIDA", m_leidas), ("direccion NO RESUELTA", m_no)):
        print("| %s | %d | %.1f | %d de %d (%.1f%%) |"
              % (nombre, m["n"], m["mediana_ratio"], m["misma_fuente"], m["n"], m["pct_misma_fuente"]))
    print()

    # LAS DOS AFIRMACIONES, COMPUTADAS Y NO DECLARADAS
    m1 = dict(medidas)["tramo 1 (filas 1 a 40)"]
    m2 = dict(medidas)["tramo 2 (filas 41 a 100)"]
    af1 = m2["mediana_ratio"] < m1["mediana_ratio"]
    af2 = m_no["pct_misma_fuente"] < m_leidas["pct_misma_fuente"]

    print("=" * 100)
    print("LAS DOS AFIRMACIONES, con su veredicto COMPUTADO de las tablas de arriba")
    print("=" * 100)
    print()
    print("AFIRMACION 1 (la bolsa se debilita): mediana del tramo 2 (%.1f) MENOR que la del tramo 1 (%.1f)"
          % (m2["mediana_ratio"], m1["mediana_ratio"]))
    print("   -> %s" % ("VERIFICADA" if af1 else "NO SE SOSTIENE"))
    print()
    print("AFIRMACION 2 (la senial acompania a la lectura): misma fuente en NO RESUELTA (%.1f%%) MENOR que en LEIDA (%.1f%%)"
          % (m_no["pct_misma_fuente"], m_leidas["pct_misma_fuente"]))
    print("   -> %s" % ("VERIFICADA" if af2 else "NO SE SOSTIENE"))
    print()
    print("LO QUE ESTO NO PRUEBA, dicho aqui y no solo en el docstring: NO prueba que el umbral")
    print("de direccion del ejecutor sea el correcto. Una vara demasiado estricta sobre una bolsa")
    print("que se debilita daria estas dos mismas seniales. La correccion del umbral la adjudica")
    print("el auditor.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
