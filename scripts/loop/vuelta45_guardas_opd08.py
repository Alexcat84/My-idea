# -*- coding: utf-8 -*-
"""vuelta45_guardas_opd08.py - EL CASO POSITIVO Y LAS GUARDAS DE OP-D-08.

ESTRICTAMENTE DE SOLO LECTURA.

Se corre DOS VECES, ANTES y DESPUES del acto, con la misma invocacion, y las dos
salidas se sellan. Es la forma de la casa: un caso positivo sirve si CAE antes y
PASA despues; si pasa las dos veces no estaba midiendo la cirugia.

DOS FAMILIAS DE COMPROBACION, y se imprimen separadas a proposito:

  (A) EL CASO POSITIVO: lo que la operacion existe para arreglar. Tiene que
      CAER antes y PASAR despues. Su cabeza es la que el campo verificacion
      nombra: EL PAR 784 SE DESCONGELA Y SE JUZGA, y lo que lo bloqueaba es
      medible, porque su razon dice por que no se juzga (el solape cruza las
      CUATRO junturas a la vez).

  (B) LAS INVARIANTES: lo que NO puede moverse. Tienen que PASAR las dos veces.
      Cero movimiento de grafo, las anclas de los veredictos 1434 y 1136 vivas,
      las tres aristas paso a nodo en las que este nodo es HIJO, y el
      entregable_esperado siguiendo siendo cierto del texto que quede.

Uso: python scripts/loop/vuelta45_guardas_opd08.py <ANTES|DESPUES>
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")
NODO = "lienzo_modelo_negocio"

# LOS NUEVE BLOQUES DEL CANVAS, con la palabra por la que se busca cada uno.
BLOQUES = (u"segmento", u"propuesta de valor", u"canales", u"relaciones",
           u"ingresos", u"recursos", u"actividades", u"asociaciones", u"costos")

# LAS TRES MADRES de las aristas paso a nodo en las que este nodo es HIJO,
# con el paso de la madre del que cuelga cada una.
MADRES = (("tipo_de_mercado_estrategia_competitiva", 5),
          ("customer_discovery_overview", 1),
          ("unbundling_business_models", 4))


def leer(nid):
    return json.loads(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8").read())


def main():
    etiqueta = sys.argv[1] if len(sys.argv) > 1 else "SIN ETIQUETA"
    d = leer(NODO)
    pasos = list(d.get("pasos_accionables") or [])
    cond = list(d.get("condiciones_activacion") or [])
    bajo = [p.lower() for p in pasos]

    print("=" * 78)
    print("GUARDAS DE OP-D-08, MEDICION DE %s" % etiqueta)
    print("=" * 78)
    print()
    print("  nodo: %s | pasos: %d | condiciones: %d" % (NODO, len(pasos), len(cond)))
    print()

    # ------------------------------------------------------------------
    print("### (A) EL CASO POSITIVO: tiene que CAER antes y PASAR despues")
    print()
    positivos = []

    # A1: cuantas NARRACIONES ordenan completar el lienzo.
    #     Se cuentan por su firma, no por la cifra: la del post-it, la de la
    #     solucion disenada, la de la sesion de equipo, y la enumeracion.
    n1 = sum(1 for p in bajo if u"9 bloques" in p and u"post-it" in p)
    n2 = sum(1 for p in bajo if u"9 bloques" in p and u"soluci" in p)
    n3 = sum(1 for p in bajo if u"completar las secciones del canvas" in p)
    n4 = 1 if sum(1 for p in bajo if any(b in p for b in BLOQUES)) >= 5 else 0
    narraciones = n1 + n2 + n3 + n4
    positivos.append((
        "A1 UNA SOLA ORDEN DE COMPLETAR LOS NUEVE BLOQUES (el recuento que "
        "cierra la cirugia)", narraciones == 1,
        "narraciones que la dan: %d (post-it %d, solucion disenada %d, "
        "sesion de equipo %d, enumeracion %d)" % (narraciones, n1, n2, n3, n4)))

    # A2: el literal exacto que la ficha localizo en los pasos 2 y 5.
    lit = [i + 1 for i, p in enumerate(bajo) if u"cada uno de los 9 bloques" in p]
    positivos.append((
        "A2 EL LITERAL 'cada uno de los 9 bloques' YA NO SE REPITE",
        len(lit) <= 1, "pasos que lo llevan: %s (son %d)" % (lit or "ninguno", len(lit))))

    # A3: la orden de imprimir, que el archivo declara DOS veces.
    imp = [i + 1 for i, p in enumerate(bajo) if u"imprimir" in p]
    positivos.append((
        "A3 EL LIENZO SE MANDA IMPRIMIR UNA SOLA VEZ",
        len(imp) == 1, "pasos que lo mandan: %s (son %d)" % (imp, len(imp))))

    # A4: el solape del 784 cruza las CUATRO junturas a la vez. Con una sola
    #     narracion no hay junturas que cruzar y el par se puede juzgar.
    junturas = max(0, narraciones - 1)
    positivos.append((
        "A4 CERO JUNTURAS ENTRE NARRACIONES, que es lo que el 784 declara "
        "como causa de no poder juzgarse", junturas == 0,
        "junturas entre narraciones: %d" % junturas))

    caen = 0
    for nombre, ok, detalle in positivos:
        print("  [%s] %s" % ("PASA" if ok else "CAE ", nombre))
        print("         %s" % detalle)
        caen += 0 if ok else 1
    print()
    print("  RESULTADO DEL CASO POSITIVO: %d PASAN y %d CAEN"
          % (len(positivos) - caen, caen))

    # ------------------------------------------------------------------
    print()
    print("### (B) LAS INVARIANTES: tienen que PASAR las dos veces")
    print()
    inv = []

    prev = d.get("nodos_previos") or []
    sig = d.get("nodos_siguientes") or []
    inv.append(("B1 CERO MOVIMIENTO: los vecinos del nodo",
                len(prev) + len(sig) == 91,
                "previos %d + siguientes %d = %d (la operacion declara 91)"
                % (len(prev), len(sig), len(prev) + len(sig))))

    total = 0
    ficheros = 0
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            ficheros += 1
            x = json.loads(io.open(os.path.join(NODOS, nombre), encoding="utf-8").read())
            for c in CAMPOS:
                total += len(x.get(c) or [])
    inv.append(("B2 CERO MOVIMIENTO: las entradas de arista del grafo entero",
                total == 16898,
                "%d entradas sobre %d ficheros. LA CIFRA ESCRITA EN LA OPERACION "
                "(16.866) ES DE OTRO CORTE, el de la vuelta 17, y se cita como "
                "contraste: la guarda es que la de HOY no se mueva" % (total, ficheros)))

    ancla_1434 = any(u"propuesta de valor para cada segmento" in p for p in bajo)
    inv.append(("B3 EL ANCLA DEL VEREDICTO 1434 SIGUE VIVA (paso intocable)",
                ancla_1434, "'definir la propuesta de valor para cada segmento': %s"
                % ("presente" if ancla_1434 else "AUSENTE")))

    ancla_1136 = any((u"post-it" in p or u"adhesiv" in p) for p in bajo)
    inv.append(("B4 EL ANCLA DEL VEREDICTO 1136 SIGUE VIVA (las notas adhesivas)",
                ancla_1136, "clausula de las notas post-it: %s"
                % ("presente" if ancla_1136 else "AUSENTE")))

    ok_madres = True
    detalle_madres = []
    for madre, paso in MADRES:
        m = leer(madre)
        tiene = paso <= len(m.get("pasos_accionables") or [])
        cita = NODO in (m.get("nodos_siguientes") or []) or NODO in (m.get("nodos_previos") or [])
        ok_madres = ok_madres and tiene and cita
        detalle_madres.append("%s paso %d existe %s y cita %s" % (madre, paso, tiene, cita))
    inv.append(("B5 LAS TRES ARISTAS PASO A NODO EN LAS QUE ESTE NODO ES HIJO",
                ok_madres, " | ".join(detalle_madres)))

    vivos = [b for b in BLOQUES if any(b in p for p in bajo)]
    inv.append(("B6 EL ENTREGABLE SIGUE SIENDO CIERTO: los 9 bloques definidos",
                len(vivos) == 9, "bloques nombrados en los pasos: %d de 9 (%s)"
                % (len(vivos), ", ".join(vivos))))

    coherencia = any(u"coherencia" in p for p in bajo)
    inv.append(("B7 EL ENTREGABLE SIGUE SIENDO CIERTO: y coherentes entre si",
                coherencia, "linea de coherencia entre bloques: %s"
                % ("presente" if coherencia else "AUSENTE")))

    inv.append(("B8 LA FUENTE NO SE TOCA",
                d.get("fuente") == "Business Model Generation - Osterwalder",
                repr(d.get("fuente"))))

    inv.append(("B9 LAS CONDICIONES NO SE TOCAN", len(cond) == 7,
                "%d condiciones, y la 3 (la que sostiene la lectura del marco) "
                "dice: %r" % (len(cond), cond[2] if len(cond) > 2 else None)))

    rojo = 0
    for nombre, ok, detalle in inv:
        print("  [%s] %s" % ("OK  " if ok else "ROJO", nombre))
        print("         %s" % detalle)
        rojo += 0 if ok else 1
    print()
    print("  RESULTADO DE LAS INVARIANTES: %d en OK y %d en ROJO"
          % (len(inv) - rojo, rojo))
    print()
    print("=" * 78)
    print("FIN DE LAS GUARDAS, MEDICION DE %s" % etiqueta)
    print("=" * 78)
    return 0


raise SystemExit(main())
