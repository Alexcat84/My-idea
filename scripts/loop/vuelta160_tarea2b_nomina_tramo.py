# -*- coding: utf-8 -*-
"""vuelta160_tarea2b_nomina_tramo.py . TAREA 2.b DE LA VUELTA 160, LA NOMINA DEL
TRAMO AL DOBLE.

LA CIFRA NO SE TECLEA Y NO SE CREE. El encargo y la adjudicacion 6.4 del acta
159 dicen 37, de las cuales 8 en C y 29 en D. ESTE INSTRUMENTO LO RECOMPUTA. Si
no da 37, SALE ROJO Y NO SE LEE NADA.

QUE ES EL TRAMO AL DOBLE, DICHO COMO SE COMPUTA: las lecturas del LOTE 2 que
NADIE HA VUELTO A MIRAR, o sea el lote 2 menos las que el auditor releyo en su
ciega de la vuelta 159.

LAS TRES FUENTES, Y NINGUNA ES PROSA:
  (a) EL LOTE 2, de su fichero sellado `docs/loop/NOMINA_V159_LOTE2.json`, que
      es el que la TAREA 3 de la vuelta 159 uso para leerlo.
  (b) LAS 16 QUE EL AUDITOR RELEYO, de SU PROPIO fichero de computo
      `docs/loop/_auditor_v159_tramo_al_doble.txt`, no de la prosa del acta ni
      del encargo. La linea de la que salen se imprime literal al lado.
  (c) LAS 37 QUE EL AUDITOR PUBLICO, del MISMO fichero, para cotejar contra la
      resta que hace este instrumento. Es un cotejo, no la fuente: la nomina
      que se usa es (a) menos (b).

Y ADEMAS SE COMPRUEBAN TRES COSAS QUE PODRIAN ROMPER LA CUENTA SIN QUE SE VEA:
  (i)   que las 16 esten TODAS dentro del lote 2 (si el auditor releyo algo de
        fuera, la resta seria otra);
  (ii)  que la resta y la nomina publicada por el auditor coincidan ELEMENTO A
        ELEMENTO, no solo en el total;
  (iii) que las clases vigentes de las 37, CONTADAS DEL REGISTRO DE HOY, den 8
        en C y 29 en D. Esta es la unica de las tres que puede haberse movido
        legitimamente: la TAREA 2.a de esta vuelta acaba de mover
        `LD-OPC05-100` de C a D, y la `100` esta entre las 16 del auditor, o
        sea FUERA de las 37. Si el reparto cambia, se dice en vez de callarlo.

USO:  python scripts/loop/vuelta160_tarea2b_nomina_tramo.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
NOMINA_LOTE2 = os.path.join(LOOP, "NOMINA_V159_LOTE2.json")
COMPUTO_AUDITOR = os.path.join(LOOP, "_auditor_v159_tramo_al_doble.txt")
SALIDA = os.path.join(LOOP, "NOMINA_V160_TRAMO.json")


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def ld_de(e):
    return e["cita"].split(",")[0].strip()


def entradas():
    return [json.loads(x) for x in leer(REGISTRO).splitlines() if x.strip()]


def lista_tras(texto, rotulo):
    """Devuelve la lista de LD que sigue a la linea que empieza por ROTULO en el
    fichero de computo del auditor. Los numeros van en la linea de despues,
    separados por comas."""
    lineas = texto.splitlines()
    for i, l in enumerate(lineas):
        if l.startswith(rotulo):
            crudo = lineas[i + 1].strip()
            return ["LD-OPC05-%s" % x.strip() for x in crudo.split(",") if x.strip()]
    raise AssertionError("no se hallo el rotulo %r en %s" % (rotulo, COMPUTO_AUDITOR))


def cifra_tras(texto, rotulo):
    for l in texto.splitlines():
        if l.startswith(rotulo):
            m = re.search(r"(\d+)\s*$", l.strip())
            if m:
                return int(m.group(1))
    raise AssertionError("no se hallo la cifra de %r" % rotulo)


def main():
    print("=" * 78)
    print("VUELTA 160, TAREA 2.b: LA NOMINA DEL TRAMO AL DOBLE, RECOMPUTADA")
    print("=" * 78)
    print("")

    lote2 = json.load(io.open(NOMINA_LOTE2, encoding="utf-8"))["lote"]
    print("A) EL LOTE 2, DE SU FICHERO SELLADO")
    print("   fuente: docs/loop/NOMINA_V159_LOTE2.json")
    print("   CIFRA lote 2: %d" % len(lote2))

    texto = leer(COMPUTO_AUDITOR)
    print("")
    print("B) LAS 16 RELEIDAS POR EL AUDITOR, DE SU PROPIO FICHERO DE COMPUTO")
    print("   fuente: docs/loop/_auditor_v159_tramo_al_doble.txt, pegado entero:")
    for l in texto.splitlines():
        print("      | %s" % l)
    releidas = lista_tras(texto, "CIFRA del lote 2 releidos por el auditor")
    n_releidas = cifra_tras(texto, "CIFRA del lote 2 releidos por el auditor")
    print("   CIFRA releidas leidas de la lista: %d" % len(releidas))
    print("   CIFRA releidas que el fichero declara: %d" % n_releidas)
    assert len(releidas) == n_releidas, "la lista y la cifra del auditor no calzan"

    fuera = [x for x in releidas if x not in lote2]
    print("   CIFRA de las 16 que NO estan en el lote 2: %d" % len(fuera))
    assert not fuera, "el auditor releyo fuera del lote 2: %s" % ", ".join(fuera)
    print("   LAS 16 ESTAN TODAS DENTRO DEL LOTE 2.")

    tramo = [x for x in lote2 if x not in set(releidas)]
    print("")
    print("C) LA RESTA, Y SU COTEJO ELEMENTO A ELEMENTO")
    print("   CIFRA lote 2 menos releidas: %d menos %d da %d"
          % (len(lote2), len(releidas), len(tramo)))
    publicadas = lista_tras(texto, "CIFRA del lote 2 SIN SEGUNDA LECTURA")
    n_publicadas = cifra_tras(texto, "CIFRA del lote 2 SIN SEGUNDA LECTURA")
    print("   CIFRA que el auditor publica: %d" % n_publicadas)
    assert len(publicadas) == n_publicadas, "la lista y la cifra del auditor no calzan"
    if sorted(tramo) != sorted(publicadas):
        print("   ROJO: LA RESTA Y LA NOMINA DEL AUDITOR NO COINCIDEN.")
        print("      solo en mi resta : %s" % ", ".join(sorted(set(tramo) - set(publicadas))))
        print("      solo en la suya  : %s" % ", ".join(sorted(set(publicadas) - set(tramo))))
        print("   PARADA: no se lee nada.")
        return 1
    print("   LAS DOS NOMINAS SALEN IDENTICAS, ELEMENTO A ELEMENTO.")
    assert len(tramo) == 37, "EL TRAMO NO DA 37: da %d. PARADA, no se lee nada." % len(tramo)
    print("   Y DA 37, que es lo que la 6.4 del acta 159 encarga.")

    E = {ld_de(e): e for e in entradas()}
    reparto = {}
    for ld in tramo:
        c = E[ld]["clase"]
        reparto[c] = reparto.get(c, 0) + 1
    print("")
    print("D) EL REPARTO POR CLASE VIGENTE, CONTADO DEL REGISTRO DE HOY")
    print("   CIFRA por clase: %s" % json.dumps(reparto, sort_keys=True))
    print("   CIFRA que la 6.4 del acta 159 declara: 8 en C y 29 en D")
    if reparto != {"C": 8, "D": 29}:
        print("   DISCREPANCIA DECLARADA: el reparto de hoy no es el del acta.")
    else:
        print("   REPRODUCE AL DIGITO.")
    print("   Y SE DICE LO QUE NO CAMBIA LA CUENTA: la TAREA 2.a de esta vuelta")
    print("   movio LD-OPC05-100 de C a D, pero la 100 esta entre las 16 del")
    print("   auditor, o sea FUERA de las 37, y por eso este reparto no la ve.")

    print("")
    print("E) LA NOMINA, UNA A UNA, CON SU CLASE VIGENTE")
    for i, ld in enumerate(tramo, 1):
        print("   %2d. %-16s clase %s" % (i, ld, E[ld]["clase"]))

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        json.dump({"tramo": tramo,
                   "reparto": reparto,
                   "lote2": len(lote2),
                   "releidas_por_el_auditor": sorted(releidas)},
                  fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("")
    print("SELLADA en docs/loop/NOMINA_V160_TRAMO.json")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
