"""Vuelta 28: EL CASO POSITIVO de la relectura conjunta y de las mudanzas.

El criterio de HECHO de docs/plan/08_VERIFICACION.md es uno solo: *una fase esta
hecha cuando su verificacion SE CAERIA si el fallo volviera*, y su comprobacion
barata es correr la prueba ANTES: si pasa, no prueba nada.

Se corre DOS veces: antes de la mudanza (tiene que CAER) y despues (tiene que
PASAR). No escribe nada.

Las tres pruebas por mudanza:
  1. el nodo del que sale el bloque YA NO lleva su huella
  2. el destino escrito SI la lleva
  3. CERO PERDIDA y CERO GEMELO: la huella vive en EXACTAMENTE un nodo vivo

Uso:
    python scripts/loop/vuelta28_caso_positivo.py <plan.json>
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


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


def comprobar(nombre, ok, detalle=""):
    print("  [%s] %s" % ("PASA" if ok else "CAE ", nombre))
    if detalle:
        print("         %s" % detalle)
    return ok


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    plan = json.load(open(sys.argv[1], encoding="utf-8"))
    nodos = cargar()
    print("CASO POSITIVO: %s" % plan["operacion"])
    print("=" * 78)
    todo = True

    # ESQUEMA DE CORTES (el de vuelta27_cortar.py): un bloque sale de su nodo de
    # origen hacia un miembro. Las tres pruebas son las mismas de la tanda RAC:
    # el origen ya no declara el libro injertado, el material vive en el destino,
    # y el origen ya no lo lleva.
    if "cortes" in plan:
        for c in plan["cortes"]:
            origen, huella = c["origen"], c["huella"]
            destino = c["destino"]["nodo"]
            print("\n%s pasos %s -> %s   huella %r"
                  % (origen, c["pasos_que_salen"], destino, huella))
            d = nodos.get(origen)
            fuente = (d or {}).get("fuente") or ""
            ok0 = d is not None and fuente == c["fuente_queda"]
            todo = comprobar("%s declara solo %r" % (origen, c["fuente_queda"]),
                             ok0, "fuente de hoy: %r" % fuente) and todo
            ok1 = d is not None and huella.lower() not in texto_pasos(d).lower()
            todo = comprobar("%s ya no lleva la huella" % origen, ok1) and todo
            t = nodos.get(destino)
            ok2 = t is not None and vivo(t) and huella.lower() in texto_pasos(t).lower()
            todo = comprobar("%s si la lleva" % destino, ok2) and todo
        print("\n" + "=" * 78)
        print("RESULTADO: %s" % ("TODO PASA" if todo else "HAY PRUEBAS QUE CAEN"))
        return 0 if todo else 1

    for m in plan["mudanzas"]:
        huella = m["huella"]
        desde = m["desde"]
        destino = m["destino"].get("nodo") or m["destino"]["nuevo"]["node_id"]
        print("\n%s: %s -> %s   huella %r" % (m["caso"], desde, destino, huella))

        d = nodos.get(desde)
        ok1 = d is not None and huella.lower() not in texto_pasos(d).lower()
        todo = comprobar("%s ya no lleva la huella" % desde, ok1) and todo

        t = nodos.get(destino)
        ok2 = t is not None and vivo(t) and huella.lower() in texto_pasos(t).lower()
        todo = comprobar("%s si la lleva" % destino, ok2,
                         "" if t is not None else "el destino AUN NO EXISTE") and todo

        portadores = sorted(k for k, n in nodos.items()
                            if vivo(n) and huella.lower() in texto_pasos(n).lower())
        ok3 = len(portadores) == 1
        todo = comprobar("la huella vive en exactamente UN nodo vivo", ok3,
                         "portadores: %s" % (portadores or "NINGUNO")) and todo

    print("\n" + "=" * 78)
    print("RESULTADO: %s" % ("TODO PASA" if todo else "HAY PRUEBAS QUE CAEN"))
    return 0 if todo else 1


if __name__ == "__main__":
    sys.exit(main())
