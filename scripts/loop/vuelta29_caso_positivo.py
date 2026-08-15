"""Vuelta 29: EL CASO POSITIVO de un plan de cortes con huella declarada.

El criterio de HECHO de docs/plan/08_VERIFICACION.md es uno solo: *una fase esta
hecha cuando su verificacion SE CAERIA si el fallo volviera*, y su comprobacion
barata es correr la prueba ANTES del arreglo: si pasa, no prueba nada.

Se corre DOS veces: antes del corte (tiene que CAER) y despues (tiene que
PASAR). No escribe nada.

Las tres pruebas por corte:
  1. el nodo del que sale el bloque YA NO lleva su huella
  2. el destino escrito SI la lleva
  3. CERO PERDIDA y CERO GEMELO: la huella vive en EXACTAMENTE un nodo vivo

Uso:
    python scripts/loop/vuelta29_caso_positivo.py <plan.json>
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


def lleva(d, huella):
    return any(huella in p for p in d.get("pasos_accionables") or [])


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    plan = json.load(open(sys.argv[1], encoding="utf-8"))
    grafo = cargar()
    print("CASO POSITIVO: %s" % plan["operacion"])
    print("=" * 78)
    caen = 0
    pasan = 0
    for c in plan["cortes"]:
        origen = c["origen"]
        huella = c["huella"]
        dest = c["destino"]
        destino_id = dest.get("nodo") or dest["nuevo"]["node_id"]
        print("\n%s -> %s   huella %r" % (origen, destino_id, huella))

        d_ori = grafo.get(origen)
        ok1 = d_ori is not None and not lleva(d_ori, huella)
        print("  [%s] %s ya no lleva la huella" % ("PASA" if ok1 else "CAE ", origen))

        d_des = grafo.get(destino_id)
        ok2 = d_des is not None and lleva(d_des, huella)
        print("  [%s] %s si la lleva" % ("PASA" if ok2 else "CAE ", destino_id))
        if d_des is None:
            print("         el destino AUN NO EXISTE")

        portadores = sorted(nid for nid, dd in grafo.items() if vivo(dd) and lleva(dd, huella))
        ok3 = len(portadores) == 1
        print("  [%s] la huella vive en exactamente UN nodo vivo" % ("PASA" if ok3 else "CAE "))
        print("         portadores: %s" % portadores)

        for ok in (ok1, ok2, ok3):
            if ok:
                pasan += 1
            else:
                caen += 1

    print("\n" + "=" * 78)
    print("RESULTADO: %d PASAN, %d CAEN" % (pasan, caen))
    print("TODO PASA" if caen == 0 else "HAY PRUEBAS QUE CAEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
