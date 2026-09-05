# -*- coding: utf-8 -*-
r"""vuelta179_tarea2_los_diez.py . LOS PARES REALES QUE QUEDAN EN LOS ACTOS QUE
NADIE HA MIRADO, LOCALIZADOS POR EL INSTRUMENTO Y NO ELEGIDOS A MANO.

TAREA 2 de la vuelta 179. El encargo dice que de los **73 pares** que el
instrumento viejo da quedan **18 reales**, que **8 los leyo la 177** y que
**quedan 10** en los **34 actos** que nadie ha mirado. NINGUNA DE ESAS CIFRAS SE
COPIA AQUI: se llaman las funciones de `backlog_l03_resuelto.py`, que es el
instrumento que la casa reconoce, y se imprime lo que salga (`EJECUTOR.md` 2).

SOLO LECTURA. Este fichero no escribe veredictos, ni el registro de `OP-L-03`, ni
la ficha, ni nodos. Localiza y publica, para que la lectura de despues se haga
sobre una lista que salio de un instrumento y no de una eleccion.

QUE PUBLICA POR CADA PAR, para que la vara del banco se pueda aplicar sin volver
a buscar nada: los dos extremos ya RESUELTOS por `P.1`, el acto del que salen, si
alguno de los dos extremos tiene PUESTO EN LA COLA, y los `pasos_accionables` de
cada extremo medidos del grafo.

POR QUE IMPORTA EL PUESTO, Y ES LA DISTINCION DEL PUNTO 7.8 DEL ACTA 178 QUE NO
SE DIFUMINA: un par que TIENE puesto en la cola escribe su veredicto en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`; uno que NO lo tiene NO SE INVENTA UN
PUESTO, y su clase y su razon van al registro de `OP-L-03`, en el campo
`clases_de_los_pares_por_leer`, que es donde la 177 las puso y donde son
trazables.

USO:
  python scripts/loop/vuelta179_tarea2_los_diez.py
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import backlog_l03_resuelto as B   # noqa: E402
import vuelta166_tarea2_correccion_op_l_01 as T   # noqa: E402

NL = chr(10)
RAIZ = B.RAIZ
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")


def puestos_por_nodo():
    """{id de nodo: [puestos en los que ese NODO aparece]}. Del archivo de
    veredictos, que es donde vive la cola.

    OJO CON LO QUE ESTO MIDE, Y SE DICE AQUI PARA NO CONFUNDIRLO: mide en que
    puestos aparece CADA EXTREMO, no si EL PAR tiene puesto. Sirve para la
    lectura (saber contra quien mas se ha juzgado cada nodo) y NO para decidir
    donde va el veredicto. Esa decision la toma `el_par_tiene_puesto()`."""
    idx = {}
    for linea in io.open(VEREDICTOS, encoding="utf-8"):
        if not linea.strip():
            continue
        d = json.loads(linea)
        for k in ("nodo_a", "nodo_b"):
            n = d.get(k)
            if n:
                idx.setdefault(n, []).append(d.get("puesto_intra"))
    return idx


def el_par_tiene_puesto(idx_por_par, a, b):
    """SI EL PAR, RESUELTO, TIENE PUESTO EN LA COLA. PURA: recibe el indice de
    veredictos por par resuelto.

    Y ES LA MEDICION QUE DECIDE DONDE VA EL VEREDICTO, que es la distincion del
    punto 7.8 del acta 178. Un par CON puesto escribe en
    `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`; uno SIN puesto NO SE INVENTA UNO y va
    al registro de `OP-L-03`.

    LO QUE SALE DE MEDIRLO ASI, Y HAY QUE DECIRLO EN VEZ DE ESCONDERLO: un PAR
    REAL nunca puede tener puesto, PORQUE `medir_acto()` define par real como
    el que NO esta ya en el archivo. La condicion es decidible y su respuesta es
    siempre NO. No es una casualidad de estos diez: es la forma de la definicion,
    y explica por que los OCHO que la 177 leyo tambien fueron todos al registro.
    Se mide igualmente y se publica, porque una guarda que solo se mira cuando
    difiere no se puede auditar el dia que difiera."""
    return frozenset((a, b)) in idx_por_par


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("LOS PARES REALES DE LOS ACTOS QUE NADIE HA MIRADO (vuelta 179, TAREA 2)")
    print("=" * 78)
    print("")

    print("A) EL UNIVERSO, RECOMPUTADO Y NO COPIADO DEL ENCARGO")
    actos, _salida, _codigo = B.actos_del_instrumento()
    mapa, n_nodos = T.mapa_de_alias()
    vivos_grafo = B.vivos_por_grafo()
    idx = B.veredictos_por_par(mapa)
    print("   CIFRA ficheros de dataset/nodos/ leidos por el resolutor: %d" % n_nodos)
    print("   CIFRA alias del mapa: %d" % len(mapa))
    print("   CIFRA actos que el instrumento da: %d" % len(actos))
    print("   CIFRA pares que el instrumento da, sumados: %d"
          % sum(pares_i for _tam, pares_i, _m in actos))
    print("   CIFRA pares distintos que ya tienen veredicto: %d" % len(idx))
    print("")

    print("B) LOS ACTOS QUE EL REGISTRO DICE LEIDOS, CONTADOS DE SU FICHERO")
    leidos = set()
    if os.path.exists(B.REGISTRO):
        for linea in io.open(B.REGISTRO, encoding="utf-8"):
            if linea.strip():
                leidos.add(json.loads(linea).get("acto"))
    print("   docs/plan/OP_L_03_LECTURAS.jsonl")
    print("   CIFRA actos que el registro dice leidos: %d" % len(leidos))
    for n in sorted(leidos):
        print("      LEIDO: %s" % n)
    print("")

    print("C) LOS PARES REALES, PARTIDOS POR SI SU ACTO SE LEYO O NO")
    medidas = []
    for tam, pares_i, miembros in actos:
        m = B.medir_acto(miembros, pares_i, mapa, vivos_grafo, idx)
        medidas.append((miembros[0], m))
    de_leidos = [(n, m) for n, m in medidas if n in leidos]
    del_resto = [(n, m) for n, m in medidas if n not in leidos]
    r_leidos = sum(m["cifra_pares_reales"] for _n, m in de_leidos)
    r_resto = sum(m["cifra_pares_reales"] for _n, m in del_resto)
    print("| tramo | actos | pares del instrumento | pares reales |")
    print("|---|---:|---:|---:|")
    print("| actos QUE LA 177 LEYO | %d | %d | **%d** |"
          % (len(de_leidos), sum(m["pares_del_instrumento"] for _n, m in de_leidos), r_leidos))
    print("| actos QUE NADIE HA MIRADO | %d | %d | **%d** |"
          % (len(del_resto), sum(m["pares_del_instrumento"] for _n, m in del_resto), r_resto))
    print("| **todo el backlog** | %d | %d | **%d** |"
          % (len(medidas), sum(m["pares_del_instrumento"] for _n, m in medidas),
             r_leidos + r_resto))
    print("")
    print("   CIFRA pares reales EN LOS ACTOS SIN LEER, que son el trabajo de hoy: %d"
          % r_resto)
    print("")

    print("D) LOS PARES, UNO A UNO, CON TODO LO QUE HACE FALTA PARA LEERLOS")
    nodos = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    porque = puestos_por_nodo()
    filas = []
    for nombre, m in del_resto:
        for par in m["pares_reales"]:
            x, y = sorted(par)
            px = sorted(set(q for q in porque.get(x, []) if q is not None))
            py = sorted(set(q for q in porque.get(y, []) if q is not None))
            filas.append({
                "acto": nombre, "a": x, "b": y,
                "puestos_de_a": px, "puestos_de_b": py,
                "puestos_en_que_aparece_a": len(px),
                "puestos_en_que_aparece_b": len(py),
                "tiene_puesto": el_par_tiene_puesto(idx, x, y),
                "pasos_a": len(nodos.get(x, {}).get("pasos_accionables") or []),
                "pasos_b": len(nodos.get(y, {}).get("pasos_accionables") or []),
            })
    for i, f in enumerate(filas, 1):
        print("")
        print("   PAR %d de %d | acto `%s`" % (i, len(filas), f["acto"]))
        print("      a: %-52s pasos_accionables %d" % (f["a"], f["pasos_a"]))
        print("      b: %-52s pasos_accionables %d" % (f["b"], f["pasos_b"]))
        print("      puestos en que aparece a (contra OTROS nodos): %s"
              % (", ".join(str(q) for q in f["puestos_de_a"]) or "(ninguno)"))
        print("      puestos en que aparece b (contra OTROS nodos): %s"
              % (", ".join(str(q) for q in f["puestos_de_b"]) or "(ninguno)"))
        print("      EL PAR TIENE PUESTO EN LA COLA: %s"
              % ("SI" if f["tiene_puesto"] else "NO"))
    print("")

    print("E) EL REPARTO POR PUESTO, QUE DECIDE DONDE VA CADA VEREDICTO")
    con = [f for f in filas if f["tiene_puesto"]]
    sin = [f for f in filas if not f["tiene_puesto"]]
    print("| donde va el veredicto | pares |")
    print("|---|---:|")
    print("| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (TIENEN puesto) | **%d** |" % len(con))
    print("| `docs/plan/OP_L_03_LECTURAS.jsonl` (NO tienen puesto) | **%d** |" % len(sin))
    print("| **total** | **%d** |" % len(filas))
    print("   LA RESTA: %d mas %d = %d, y el total es %d. CALZA: %s"
          % (len(con), len(sin), len(con) + len(sin), len(filas),
             "SI" if len(con) + len(sin) == len(filas) else "NO"))
    print("")
    print("   Y NO SE INVENTA NINGUN PUESTO: la distincion es la del punto 7.8 del")
    print("   acta 178 y no se difumina.")
    print("")
    print("   LO QUE SALE DE MEDIRLO BIEN, Y SE DICE EN VEZ DE ESCONDERSE: un PAR")
    print("   REAL no puede tener puesto, porque `medir_acto()` define par real")
    print("   como el que NO esta ya en el archivo. La condicion es decidible y su")
    print("   respuesta es siempre NO. Eso explica por que los OCHO que la 177 leyo")
    print("   tambien fueron todos al registro de OP-L-03 y ninguno al archivo.")
    todos = sorted(q for q in (v for vs in porque.values() for v in vs) if q is not None)
    unicos = sorted(set(todos))
    print("   Y NO HAY PUESTO LIBRE QUE ASIGNAR, contado del propio archivo:")
    print("      CIFRA puestos distintos ocupados: %d | menor %s | mayor %s"
          % (len(unicos), unicos[0] if unicos else "(ninguno)",
             unicos[-1] if unicos else "(ninguno)"))
    print("      CIFRA huecos en el rango (puestos que faltarian): %d"
          % ((unicos[-1] - unicos[0] + 1 - len(unicos)) if unicos else 0))
    print("      CIFRA pares distintos tras resolver, que es OTRA cifra: %d" % len(idx))
    print("")

    print("F) LOS ACTOS DE ESOS PARES, QUE SON LOS QUE HAY QUE CERRAR CON SU FORMA")
    for n in sorted({f["acto"] for f in filas}):
        de_este = [f for f in filas if f["acto"] == n]
        m = dict(medidas)[n]
        print("   acto `%s`" % n)
        print("      miembros escritos %d | vivos por el resolutor %d | vivos por el grafo %d"
              % (m["cifra_miembros"], m["cifra_vivos_por_resolutor"],
                 m["cifra_vivos_por_grafo"]))
        print("      pares del instrumento %d | pares reales %d | disueltos %d | ya con veredicto %d"
              % (m["pares_del_instrumento"], m["cifra_pares_reales"],
                 m["cifra_pares_disueltos"], m["cifra_pares_con_veredicto"]))
        print("      pares de este acto en la lista de hoy: %d" % len(de_este))
    print("   CIFRA actos implicados: %d" % len({f["acto"] for f in filas}))
    print("")

    io.open(os.path.join(RAIZ, "docs", "loop", "SALIDA_V179_T2_LOS_DIEZ.json"),
            "w", encoding="utf-8", newline=NL).write(
        json.dumps(filas, ensure_ascii=False, indent=1) + NL)
    print("   la lista, en json para la lectura: docs/loop/SALIDA_V179_T2_LOS_DIEZ.json")
    print("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
