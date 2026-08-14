"""Vuelta 27: EL CASO POSITIVO de cada operacion de la fase 01.

El criterio de HECHO de docs/plan/08_VERIFICACION.md es uno solo: *una fase esta
hecha cuando su verificacion SE CAERIA si el fallo volviera*, y su comprobacion
barata es correr la prueba ANTES del arreglo: si pasa, no prueba nada.

Este script es esa prueba. Se corre DOS veces: antes del corte (tiene que CAER)
y despues (tiene que PASAR). No escribe nada.

Uso:
    python scripts/loop/vuelta27_caso_positivo.py opf02
    python scripts/loop/vuelta27_caso_positivo.py opf03
    python scripts/loop/vuelta27_caso_positivo.py opf04
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
PLANES = os.path.join(RAIZ, "docs", "loop")


def cargar():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            with open(os.path.join(NODOS, nombre), encoding="utf-8") as fh:
                d = json.load(fh)
            fuera[d["node_id"]] = d
    return fuera


def vivo(d):
    return not d.get("deprecado") and not d.get("deprecated")


def texto_pasos(d):
    return " || ".join(d.get("pasos_accionables") or [])


def planes(nombres):
    fuera = []
    for n in nombres:
        p = os.path.join(PLANES, n)
        if os.path.exists(p):
            fuera.append(json.load(open(p, encoding="utf-8")))
    return fuera


def comprobar(nombre, ok, detalle):
    print("  [%s] %s" % ("PASA" if ok else "CAE ", nombre))
    if detalle:
        print("         %s" % detalle)
    return ok


def corre(id_plan, ficheros, libro_injertado, familia_destino):
    """Las dos pruebas que valen para las tres operaciones de fuente:
    1. NINGUN nodo de origen declara ya el libro injertado.
    2. El material del bloque APARECE en el grafo, fuera del nodo de origen,
       en un nodo de la familia de destino. No se poda: se reune."""
    nodos = cargar()
    todo_ok = True
    for plan in planes(ficheros):
        print("\nPLAN %s (%d cortes)" % (plan["operacion"], len(plan["cortes"])))
        for c in plan["cortes"]:
            origen = c["origen"]
            d = nodos.get(origen)
            if d is None:
                todo_ok = comprobar("%s existe" % origen, False, "AUSENTE") and todo_ok
                continue
            fuente = d.get("fuente") or ""
            ok1 = libro_injertado.lower() not in fuente.lower()
            todo_ok = comprobar("%s ya no declara %s" % (origen, libro_injertado),
                                ok1, "fuente: %s" % fuente) and todo_ok

            # la huella del bloque: el trozo mas distintivo del ultimo paso que sale
            huella = c["huella"]
            portadores = [k for k, n in nodos.items()
                          if k != origen and vivo(n) and huella.lower() in texto_pasos(n).lower()]
            en_familia = [k for k in portadores
                          if familia_destino.lower() in (nodos[k].get("fuente") or "").lower()]
            ok2 = bool(en_familia)
            todo_ok = comprobar(
                "el material de %s vive fuera de el, en la familia de destino" % origen,
                ok2, "huella %r -> portadores %s (en familia: %s)"
                % (huella, portadores or "NINGUNO", en_familia or "NINGUNO")) and todo_ok
    return todo_ok


def main():
    cual = sys.argv[1] if len(sys.argv) > 1 else ""
    print("CASO POSITIVO: %s" % cual)
    print("=" * 78)
    if cual == "opf02":
        ok = corre("OP-F-02", ["PLAN_V27_OPF02.json"],
                   "Mollick", "Mollick")
    elif cual == "opf03":
        ok = corre("OP-F-03", ["PLAN_V27_OPF03_CADENA.json", "PLAN_V27_OPF03_SISTEMAS.json"],
                   "Hugos", "Hugos")
    elif cual == "opf04":
        ok = True
        for f, libro in (("PLAN_V27_OPF04_COL.json", "Never Lose a Customer"),
                         ("PLAN_V27_OPF04_HOR.json", "Hard Thing"),
                         ("PLAN_V27_OPF04_WEI.json", "Traction"),
                         ("PLAN_V27_OPF04_RAC.json", "SPIN")):
            ok = corre("OP-F-04", [f], libro, libro) and ok
    else:
        print(__doc__)
        return 2
    print("\n" + "=" * 78)
    print("RESULTADO: %s" % ("TODO PASA" if ok else "HAY PRUEBAS QUE CAEN"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
