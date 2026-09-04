# -*- coding: utf-8 -*-
r"""vuelta167_tarea3_medir_ii.py . LA MEDICION PROPIA DE LA CAUSA DE LA
COMPROBACION ii, ANTES DE TOCAR LA FUENTE (TAREA 3 de la vuelta 167,
adjudicacion 6.5 del acta 166, por su hallazgo 4.2).

POR QUE ESTE FICHERO EXISTE Y NO SE COPIA LA CAUSA DEL ENCARGO. El encargo dice
con todas sus letras *"MIDELO TU PRIMERO CON INSTRUMENTO PROPIO Y PUBLICA TU
CIFRA; si difiere de la mia, MANDA LA TUYA Y DECLARAS LA DIFERENCIA"*, y
`EJECUTOR.md` 2 dice que un acta previa nunca es fuente de una cifra nueva. Asi
que aqui no se lee ni una cifra del acta: se recomputan las dos poblaciones
sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y el grafo, con el resolutor puesto
(`P.1`), y el contraste con el acta se imprime AL FINAL y como contraste.

QUE MIDE, Y ES EXACTAMENTE LA RESTA QUE FALLA:
  (a) EL RETRATO: pares resueltos distintos que tienen AL MENOS UNA fila de
      clase `A` y que NO colapsan a auto par. Es `len(retrato)` del PASO 1.
  (b) EL ULTIMO GANA: el diccionario `leido` del PASO 4 guarda UNA fila por par
      resuelto, la ULTIMA del fichero, SIN MIRAR LA CLASE; las aristas `A`
      internas se cuentan sobre esa fila guardada.
  (c) LA DIFERENCIA: los pares del retrato cuya fila guardada por (b) NO es `A`.
      Esos son los que el retrato cuenta y las componentes no.

NO TOCA NADA: cero escrituras fuera de su propia salida por stdout, cero nodos,
cero veredictos.

USO:  python scripts/loop/vuelta167_tarea3_medir_ii.py
"""
import collections
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        visto = set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]

    print("=" * 78)
    print("VUELTA 167, TAREA 3: LA CAUSA DE LA COMPROBACION ii, MEDIDA POR MI")
    print("=" * 78)
    print("")
    print("A) EL INSUMO, CONTADO Y NO SUPUESTO")
    print("   fichero de veredictos: docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    print("   CIFRA filas: %d" % len(V))
    print("   CIFRA puesto mayor (corte): %d" % max(r["puesto_intra"] for r in V))
    print("   CIFRA nodos del grafo: %d" % len(G))
    print("   CIFRA entradas de alias: %d" % len(ALIAS))
    print("")

    print("B) EL RETRATO DE LAS A, RECOMPUTADO AQUI (poblacion (a))")
    a_crudas = [r for r in V if r["clase"] == "A"]
    retrato = {}
    colapsos = []
    for r in a_crudas:
        ra, rb = res(r["nodo_a"]), res(r["nodo_b"])
        if ra == rb:
            colapsos.append(r)
            continue
        retrato.setdefault(frozenset((ra, rb)), []).append(r)
    print("   CIFRA A crudas: %d" % len(a_crudas))
    print("   CIFRA que colapsan a auto par tras resolver: %d" % len(colapsos))
    print("   CIFRA pares distintos en el retrato: %d" % len(retrato))
    print("")

    print("C) EL ULTIMO GANA DEL PASO 4, REPRODUCIDO AQUI (poblacion (b))")
    print("   regla reproducida: un solo registro por par resuelto, el ULTIMO")
    print("   del fichero, y SIN mirar la clase.")
    leido = {}
    todas_las_filas = collections.defaultdict(list)
    for r in V:
        ra, rb = res(r["nodo_a"]), res(r["nodo_b"])
        if ra == rb:
            continue
        k = frozenset((ra, rb))
        leido[k] = r
        todas_las_filas[k].append(r)
    a_internas = len([k for k in retrato if leido.get(k, {}).get("clase") == "A"])
    print("   CIFRA pares resueltos distintos en `leido`: %d" % len(leido))
    print("   CIFRA pares del retrato cuya fila guardada SI es A: %d" % a_internas)
    print("")

    print("D) LA DIFERENCIA, NOMBRADA UNO POR UNO (poblacion (c))")
    perdidos = [k for k in retrato if leido.get(k, {}).get("clase") != "A"]
    print("   CIFRA pares del retrato que el ultimo gana pierde: %d" % len(perdidos))
    print("   CIFRA de la resta: %d menos %d son %d"
          % (len(retrato), len(perdidos), len(retrato) - len(perdidos)))
    print("")
    for k in sorted(perdidos, key=lambda s: sorted(s)):
        nom = sorted(k)
        filas = todas_las_filas[k]
        crudas = ", ".join("(%d %s)" % (r["puesto_intra"], r["clase"])
                           for r in sorted(filas, key=lambda r: r["puesto_intra"]))
        print("   %s con %s" % (nom[0], nom[1]))
        print("      filas crudas: %s" % crudas)
        print("      la que el ultimo gana guarda: %d %s (ultima del FICHERO, no del puesto)"
              % (leido[k]["puesto_intra"], leido[k]["clase"]))
    print("")

    print("E) EL CONTRASTE CON EL ACTA 166, QUE VA AL FINAL Y COMO CONTRASTE")
    print("   el acta 166 (4.2) dice retrato 149, aristas A internas 146 y TRES")
    print("   pares perdidos. MI MEDICION DE HOY dice retrato %d, aristas A"
          % len(retrato))
    print("   internas %d y %d pares perdidos." % (a_internas, len(perdidos)))
    coincide = (len(retrato), a_internas, len(perdidos)) == (149, 146, 3)
    print("   COINCIDEN: %s" % ("SI" if coincide else
                                "NO. MANDA LA MIA Y LA DIFERENCIA QUEDA DECLARADA."))
    nombres_acta = {
        frozenset(("customer_development_modelo", "customer_discovery")),
        frozenset(("formalizar_junta_asesora", "identificar_consejo_asesores")),
        frozenset(("customer_validation", "earlyvangelists_ventas_tempranas")),
    }
    mismos = set(perdidos) == nombres_acta
    print("   Y LOS NOMBRES: los tres pares que el acta nombra son los mismos")
    print("   tres que yo mido: %s" % ("SI" if mismos else "NO"))
    if not mismos:
        print("   solo mios: %s" % sorted(sorted(s) for s in (set(perdidos) - nombres_acta)))
        print("   solo del acta: %s" % sorted(sorted(s) for s in (nombres_acta - set(perdidos))))
    print("")
    print("MEDICION PROPIA COMPLETA. Esta salida NO arregla nada: solo mide.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
