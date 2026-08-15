"""Vuelta 32, TAREA 2.1: LA LECTURA del 14vo de Horowitz, ANTES de decidir nada.

El nodo es principio_calidad_mvp y su frontera esta publicada desde la vuelta 20
(01_FUENTES.md, LA NOMINA DE LOS 14 DE HOROWITZ): 1 a 5 Ries, 6 a 10 Horowitz.

Este script NO decide: IMPRIME. Imprime el nodo entero con sus dos bloques, y
imprime la NOMINA VIGENTE AL DIA de la familia Horowitz con el titulo y el
entregable de cada miembro, que es lo que P.18 punto 1 obliga a leer (la nomina
del dia de la ejecucion, no una publicada en otra fecha). La decision entre
P.18 (destino) y P.19 (fundido) se toma con este texto delante y se escribe
despues, como correccion declarada.

El trozo de fuente de la familia es 'Hard Thing', el mismo de
scripts/loop/vuelta31_estado.py y de vuelta27_medir.py, y por el mismo motivo:
con el titulo completo la nomina sale distinta porque el grafo tiene dos
grafias del libro.

Uso: python scripts/loop/vuelta32_lectura_hor14.py
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

NODO = "principio_calidad_mvp"
TROZO = "Hard Thing"
FRONTERA = (5, 10)  # 1 a 5 Ries, 6 a 10 Horowitz


def cargar():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        with open(os.path.join(NODOS, nombre), encoding="utf-8") as fh:
            d = json.load(fh)
        fuera[d["node_id"]] = d
    return fuera


def vivo(d):
    return not d.get("deprecado") and not d.get("deprecated")


def main():
    nodos = cargar()
    ops = []
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                ops.append(json.loads(linea))
    hor = [o for o in ops if o["id_op"] == "OP-F-04-HOR"][0]

    print("=" * 78)
    print("LECTURA DEL 14vo DE HOROWITZ, vuelta 32. NADA SE DECIDE AQUI.")
    print("=" * 78)
    print()
    print("NOMINA DE OP-F-04-HOR, medida hoy en el fichero: %d nodos" % len(hor["nodos"]))
    print("El 14vo esta en la nomina: %s" % (NODO in hor["nodos"]))
    print()

    d = nodos[NODO]
    pasos = d.get("pasos_accionables") or []
    print("-" * 78)
    print("EL NODO: %s" % NODO)
    print("-" * 78)
    print("titulo    : %s" % d.get("titulo_concepto"))
    print("fuente    : %s" % d.get("fuente"))
    print("dominio   : %s   fase: %s" % (d.get("dominio"), d.get("fase_proyecto")))
    print("pasos     : %d" % len(pasos))
    print("etiqueta  : %s" % d.get("etiqueta_arbol"))
    print()
    print("resumen_teorico:")
    print("  %s" % d.get("resumen_teorico"))
    print()
    print("entregable_esperado:")
    print("  %s" % d.get("entregable_esperado"))
    print()
    print("BLOQUE 1 a %d (Ries, lo que el nodo ya era):" % FRONTERA[0])
    for i, s in enumerate(pasos[:FRONTERA[0]], 1):
        print("  %2d. %s" % (i, s))
    print()
    print("BLOQUE %d a %d (Horowitz, EL BLOQUE A RESOLVER):" % (FRONTERA[0] + 1, FRONTERA[1]))
    for i, s in enumerate(pasos[FRONTERA[0]:FRONTERA[1]], FRONTERA[0] + 1):
        print("  %2d. %s" % (i, s))
    print()

    fam = sorted([k for k, x in nodos.items()
                  if TROZO.lower() in str(x.get("fuente") or "").lower() and vivo(x)])
    print("-" * 78)
    print("LA NOMINA VIGENTE AL DIA DE LA FAMILIA HOROWITZ (P.18 punto 1)")
    print("trozo de fuente: '%s'    miembros vivos: %d" % (TROZO, len(fam)))
    print("-" * 78)
    for k in fam:
        x = nodos[k]
        marca = "  <-- ES EL DONANTE" if k == NODO else ""
        print()
        print("* %s%s" % (k, marca))
        print("    titulo    : %s" % x.get("titulo_concepto"))
        print("    fuente    : %s" % x.get("fuente"))
        print("    pasos     : %d" % len(x.get("pasos_accionables") or []))
        print("    entregable: %s" % x.get("entregable_esperado"))
    print()
    print("=" * 78)
    print("FIN DE LA LECTURA. La decision se escribe fuera de este script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
