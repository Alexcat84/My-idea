# -*- coding: utf-8 -*-
r"""vuelta179_tarea2_vecinos_del_archivo.py . LO QUE EL ARCHIVO YA DICE SOBRE
LOS DOS EXTREMOS DE CADA PAR, A TRAVES DE UN TERCER NODO.

TAREA 2 de la vuelta 179, y esto va ANTES de escribir un solo veredicto. SOLO
LECTURA: no escribe veredictos, ni el registro, ni nodos.

POR QUE, Y NO ES UN ADORNO. `banco 9.3` deja escrito que una direccion de fusion
decidida sobre un par NO SOBREVIVE A SU FAMILIA, y `EJECUTOR.md` 9 manda que todo
conteo que toque ids pase por el resolutor y que nada se afirme sin mirar el
archivo. Si el archivo ya dijo que `a` REPITE con `t` y que `b` REPITE con `t`,
juzgar `a` contra `b` sin mirarlo es leer a ciegas teniendo la respuesta escrita.

QUE MIDE, Y ES MECANICO: para cada par, todos los TERCEROS nodos contra los que
el archivo ya juzgo A LOS DOS extremos, con la clase de cada lado y su puesto.
Cuando las dos clases son `A`, eso es una CADENA DE REPITE y se dice; cuando una
es `A` y la otra `D`, eso es una FRONTERA y tambien se dice. NO DECIDE NADA: la
lectura la hace el ejecutor con la vara del banco delante y esto solo le pone
delante lo que ya estaba escrito.

TODO PASA POR EL RESOLUTOR DE `P.1` antes de contar, sin excepcion.

USO:
  python scripts/loop/vuelta179_tarea2_vecinos_del_archivo.py
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta166_tarea2_correccion_op_l_01 as T   # noqa: E402

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LISTA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V179_T2_LOS_DIEZ.json")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("LO QUE EL ARCHIVO YA DICE DE CADA PAR POR UN TERCER NODO (179, TAREA 2)")
    print("=" * 78)
    print("")

    mapa, n_nodos = T.mapa_de_alias()
    filas_v = list(T.veredictos())
    print("A) EL ARCHIVO, MEDIDO ANTES DE USARLO")
    print("   CIFRA ficheros de dataset/nodos/ leidos por el resolutor: %d" % n_nodos)
    print("   CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % len(filas_v))
    print("")

    # {nodo resuelto: {otro resuelto: (clase, puesto)}}
    vecinos = {}
    for f in filas_v:
        a = T.resolver(mapa, f["nodo_a"])
        b = T.resolver(mapa, f["nodo_b"])
        if a == b:
            continue
        vecinos.setdefault(a, {})[b] = (f.get("clase"), f.get("puesto_intra"))
        vecinos.setdefault(b, {})[a] = (f.get("clase"), f.get("puesto_intra"))

    pares = json.load(io.open(LISTA, encoding="utf-8"))
    print("B) LOS TERCEROS QUE EL ARCHIVO YA JUZGO CONTRA LOS DOS EXTREMOS")
    resumen = []
    for i, p in enumerate(pares, 1):
        a, b = p["a"], p["b"]
        va, vb = vecinos.get(a, {}), vecinos.get(b, {})
        comunes = sorted(set(va) & set(vb))
        cadenas = [t for t in comunes if va[t][0] == "A" and vb[t][0] == "A"]
        fronteras = [t for t in comunes if {va[t][0], vb[t][0]} == {"A", "D"}]
        print("")
        print("   PAR %d | %s  vs  %s" % (i, a, b))
        print("      vecinos juzgados de a: %d | de b: %d | COMUNES: %d"
              % (len(va), len(vb), len(comunes)))
        for t in comunes:
            print("      tercero `%s`" % t)
            print("         a contra el: clase %s, puesto %s" % (va[t][0], va[t][1]))
            print("         b contra el: clase %s, puesto %s" % (vb[t][0], vb[t][1]))
        if not comunes:
            print("      (ningun tercero comun: el archivo no dice nada por esta via)")
        print("      CADENAS DE REPITE (los dos en A con el mismo tercero): %d %s"
              % (len(cadenas), ", ".join(cadenas) or ""))
        print("      FRONTERAS (uno en A y el otro en D con el mismo tercero): %d %s"
              % (len(fronteras), ", ".join(fronteras) or ""))
        resumen.append((i, a, b, len(comunes), len(cadenas), len(fronteras)))
    print("")

    print("C) EL RESUMEN, CONTADO DE LO DE ARRIBA")
    print("| par | a | b | terceros comunes | cadenas de REPITE | fronteras |")
    print("|---:|---|---|---:|---:|---:|")
    for i, a, b, c, ca, fr in resumen:
        print("| %d | `%s` | `%s` | %d | **%d** | **%d** |" % (i, a, b, c, ca, fr))
    print("")
    print("   CIFRA pares con al menos una CADENA DE REPITE: %d"
          % sum(1 for _i, _a, _b, _c, ca, _f in resumen if ca))
    print("   CIFRA pares con al menos una FRONTERA: %d"
          % sum(1 for _i, _a, _b, _c, _ca, fr in resumen if fr))
    print("   CIFRA pares sin ningun tercero comun: %d"
          % sum(1 for _i, _a, _b, c, _ca, _f in resumen if not c))
    print("")
    print("   ESTO NO DECIDE NINGUN VEREDICTO. Pone delante lo que el archivo ya")
    print("   dijo, que es lo que `banco 9.3` obliga a mirar antes de fijar una")
    print("   direccion de fusion sobre un par suelto.")
    print("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
