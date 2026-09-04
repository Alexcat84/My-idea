# -*- coding: utf-8 -*-
r"""vuelta167_tarea4_censo_poblaciones.py . LAS TRES POBLACIONES DEL ROTULO
ANCHO, MEDIDAS AQUI ANTES DE ESCRIBIR NADA (TAREA 4 de la vuelta 167;
adjudicacion 6.6 del acta 166, por su hallazgo 4.3).

POR QUE. La fila del `PASO 1` de `docs/plan/RECOMPUTO_3388.md` se llama *"pares
con mas de un veredicto crudo apuntando al mismo par resuelto"* y esta vuelta
pasada la movio de `0` a `4`. El rotulo NO DICE DE QUE UNIVERSO HABLA, y al lado
de otras dos cifras parecidas (`221` y `13`) se lee como contradiccion cuando no
la hay. El encargo manda RECOMPROBARLO EN LA FUENTE antes de escribirlo, y si la
lectura del auditor fuese falsa, mandar la mia.

LAS TRES POBLACIONES, Y SON TRES Y NO UNA:
  (1) EL `4`. Sobre el RETRATO, que `scripts/plan/recomputo_3388.py:106` filtra
      a `clase == "A"` antes de agrupar: pares resueltos, sin colapsos, CON MAS
      DE UNA FILA `A`.
  (2) EL `221`. Sobre TODAS las filas del archivo, sin filtrar clase: pares
      resueltos distintos, sin colapsos, CON MAS DE UNA FILA de cualquier clase.
  (3) EL `13`. Los de (2) que ademas llevan MAS DE UNA CLASE DISTINTA.

Y SE COMPRUEBA LA LECTURA DEL CODIGO, no solo las cifras: se lee la linea del
filtro en la fuente y se imprime literal, para que quien audite vea de donde
sale la afirmacion de que el retrato es solo de `A`.

CERO ESCRITURAS: solo imprime.

USO:  python scripts/loop/vuelta167_tarea4_censo_poblaciones.py
"""
import collections
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
FUENTE = os.path.join(RAIZ, "scripts", "plan", "recomputo_3388.py")


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
    corte = max(r["puesto_intra"] for r in V)

    print("=" * 78)
    print("VUELTA 167, TAREA 4: LAS TRES POBLACIONES DEL ROTULO, MEDIDAS POR MI")
    print("=" * 78)
    print("")
    print("A) EL INSUMO Y EL CORTE")
    print("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d filas, puesto mayor %d"
          % (len(V), corte))
    print("   reparto por clase: %s"
          % dict(sorted(collections.Counter(r["clase"] for r in V).items())))
    print("")

    print("B) LA LECTURA DEL CODIGO, COMPROBADA EN LA FUENTE Y NO SUPUESTA")
    lineas = io.open(FUENTE, encoding="utf-8").read().split("\n")
    for n in range(105, 113):
        print("   recomputo_3388.py:%d| %s" % (n, lineas[n - 1]))
    filtro = [n for n in range(1, len(lineas) + 1)
              if 'a_crudas = [r for r in V if r["clase"] == "A"]' in lineas[n - 1]]
    print("   CIFRA veces que el filtro de clase A aparece en la fuente: %d"
          % len(filtro))
    print("   lineas: %s" % filtro)
    print("   VEREDICTO SOBRE LA LECTURA DEL AUDITOR (4.3 del acta 166): el")
    print("   `retrato` se construye SOLO con filas de clase A. CONFIRMADO: %s"
          % ("SI" if len(filtro) == 1 else "NO, y entonces manda mi lectura"))
    print("")

    print("C) POBLACION 1, EL 4: SOBRE EL RETRATO, SOLO FILAS A")
    a_crudas = [r for r in V if r["clase"] == "A"]
    retrato = {}
    colapsos_a = 0
    for r in a_crudas:
        ra, rb = res(r["nodo_a"]), res(r["nodo_b"])
        if ra == rb:
            colapsos_a += 1
            continue
        retrato.setdefault(frozenset((ra, rb)), []).append(r)
    multi_a = {k: v for k, v in retrato.items() if len(v) > 1}
    print("   A crudas: %d | colapsan a auto par: %d | pares distintos: %d"
          % (len(a_crudas), colapsos_a, len(retrato)))
    print("   CIFRA pares con MAS DE UNA FILA A: %d" % len(multi_a))
    for k, v in sorted(multi_a.items(), key=lambda kv: sorted(kv[0])):
        print("      %s: puestos %s"
              % (sorted(k), sorted(r["puesto_intra"] for r in v)))
    print("")

    print("D) POBLACION 2, EL 221: SOBRE TODAS LAS FILAS, SIN FILTRAR CLASE")
    todos = collections.defaultdict(list)
    colapsos_todos = 0
    for r in V:
        ra, rb = res(r["nodo_a"]), res(r["nodo_b"])
        if ra == rb:
            colapsos_todos += 1
            continue
        todos[frozenset((ra, rb))].append(r)
    multi = {k: v for k, v in todos.items() if len(v) > 1}
    print("   filas: %d | colapsan a auto par: %d | pares resueltos distintos: %d"
          % (len(V), colapsos_todos, len(todos)))
    print("   CIFRA pares con MAS DE UNA FILA de cualquier clase: %d" % len(multi))
    print("")

    print("E) POBLACION 3, EL 13: LOS DE (D) CON CLASES DISTINTAS")
    conflicto = {k: v for k, v in multi.items()
                 if len(set(r["clase"] for r in v)) > 1}
    print("   CIFRA pares con MAS DE UNA CLASE distinta: %d" % len(conflicto))
    reparto = collections.Counter(
        "".join(sorted(set(r["clase"] for r in v))) for v in conflicto.values())
    print("   reparto por juego de clases: %s" % dict(sorted(reparto.items())))
    print("")

    print("F) LAS TRES, UNA AL LADO DE LA OTRA, QUE ES LO QUE EL ROTULO NO DICE")
    print("   %-72s %d" % ("(1) pares del RETRATO (solo A) con mas de una fila A",
                           len(multi_a)))
    print("   %-72s %d" % ("(2) pares resueltos con mas de una fila, cualquier clase",
                           len(multi)))
    print("   %-72s %d" % ("(3) de esos, los que llevan clases distintas",
                           len(conflicto)))
    print("   SON SUBCONJUNTOS ENCAJADOS: (1) dentro de (2) por construccion.")
    print("   CIFRA de (1) que ademas estan en (2): %d de %d"
          % (len([k for k in multi_a if k in multi]), len(multi_a)))
    print("   CIFRA de (1) que ademas estan en (3): %d de %d"
          % (len([k for k in multi_a if k in conflicto]), len(multi_a)))
    print("")
    print("G) EL CONTRASTE CON EL ACTA 166, AL FINAL Y COMO CONTRASTE")
    print("   el acta dice 4, 221 y 13. Mi medicion de hoy dice %d, %d y %d."
          % (len(multi_a), len(multi), len(conflicto)))
    print("   COINCIDEN: %s"
          % ("SI" if (len(multi_a), len(multi), len(conflicto)) == (4, 221, 13)
             else "NO. MANDA LA MIA Y LA DIFERENCIA QUEDA DECLARADA."))
    print("")
    print("CENSO COMPLETO. Esta salida NO escribe en docs/plan/: solo mide.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
