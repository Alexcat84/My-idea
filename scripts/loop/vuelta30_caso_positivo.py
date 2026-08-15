"""Vuelta 30: EL CASO POSITIVO de un plan de FUSION INTERNA (`P.19` y `P.20`).

El criterio de HECHO de docs/plan/08_VERIFICACION.md es uno solo: *una fase esta
hecha cuando su verificacion SE CAERIA si el fallo volviera*, y su comprobacion
barata es correr la prueba ANTES: si pasa, no prueba nada.

Se corre DOS veces, antes de fundir (tiene que CAER) y despues (tiene que PASAR).
No escribe nada.

LAS PRUEBAS, y son de dos clases distintas que se cuentan aparte:

  A) LA REPETICION ESTA MUERTA (esta es la prueba de verdad, la que CAE antes):
     por cada grupo fundido de dos o mas origenes, su huella repetida vive en
     COMO MAXIMO UN paso del nodo. Antes de fundir vive en dos o mas.
     Mas la del conteo: el nodo tiene exactamente los pasos que el plan deja.
     Mas, en las salidas de `P.18`: el nodo ya no lleva la huella del tramo
     ajeno y el destino si la lleva, y la huella vive en UN solo nodo vivo.

  B) NADA SE PODA (conservacion): cada rastro declarado sigue vivo en algun paso
     del nodo. ESTAS PASAN LAS DOS VECES A PROPOSITO y por eso van contadas
     aparte: no prueban que la fusion ocurrio, prueban que no se llevo material
     por delante. Contarlas con las otras inflaria el marcador del caso positivo.

Uso:
    python scripts/loop/vuelta30_caso_positivo.py <plan.json>
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


def cuantos(d, huella):
    return sum(1 for p in (d.get("pasos_accionables") or []) if huella in p)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    plan = json.load(open(sys.argv[1], encoding="utf-8"))
    grafo = cargar()
    print("CASO POSITIVO: %s" % plan["operacion"])
    print("REGLA        : %s" % plan.get("regla", "?"))
    print("=" * 78)
    caen = pasan = 0
    conserva_si = conserva_no = 0

    for f in plan["nodos"]:
        nid = f["nodo"]
        d = grafo.get(nid)
        print("\nNODO %s" % nid)
        if d is None:
            print("  AUSENTE DEL GRAFO")
            caen += 1
            continue

        n = len(d.get("pasos_accionables") or [])
        esperados = len(f["pasos_finales"])
        ok = n == esperados
        print("  [%s] el nodo tiene %d pasos, los %d que el plan deja"
              % ("PASA" if ok else "CAE ", n, esperados))
        pasan, caen = (pasan + 1, caen) if ok else (pasan, caen + 1)

        for grupo in f.get("pruebas_repeticion") or []:
            h = grupo["huella_repetida"]
            c = cuantos(d, h)
            ok = c <= 1
            print("  [%s] la repeticion %r vive en %d paso(s), maximo 1  (origenes %s)"
                  % ("PASA" if ok else "CAE ", h, c, grupo["origenes"]))
            pasan, caen = (pasan + 1, caen) if ok else (pasan, caen + 1)

        for r in f.get("rastros") or []:
            c = cuantos(d, r)
            ok = c >= 1
            print("  (conservacion) [%s] el rastro %r sigue vivo en %d paso(s)"
                  % ("SI" if ok else "NO", r, c))
            conserva_si, conserva_no = (conserva_si + 1, conserva_no) if ok \
                else (conserva_si, conserva_no + 1)

        for s in f.get("salidas") or []:
            h = s.get("huella")
            if not h:
                continue
            mid = s["destino"]["nodo"]
            m = grafo.get(mid)
            ok1 = cuantos(d, h) == 0
            print("  [%s] %s ya no lleva %r" % ("PASA" if ok1 else "CAE ", nid, h))
            ok2 = m is not None and cuantos(m, h) >= 1
            print("  [%s] %s si la lleva" % ("PASA" if ok2 else "CAE ", mid))
            port = sorted(k for k, dd in grafo.items() if vivo(dd) and cuantos(dd, h))
            ok3 = len(port) == 1
            print("  [%s] la huella vive en UN solo nodo vivo: %s"
                  % ("PASA" if ok3 else "CAE ", port))
            for o in (ok1, ok2, ok3):
                pasan, caen = (pasan + 1, caen) if o else (pasan, caen + 1)

    print("\n" + "=" * 78)
    print("RESULTADO: %d PASAN, %d CAEN" % (pasan, caen))
    print("CONSERVACION (pasa las dos veces a proposito): %d si, %d no"
          % (conserva_si, conserva_no))
    print("TODO PASA" if caen == 0 else "HAY PRUEBAS QUE CAEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
