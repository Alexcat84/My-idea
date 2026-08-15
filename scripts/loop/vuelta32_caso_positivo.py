"""Vuelta 32: EL CASO POSITIVO de una fusion P.19, sucesor de vuelta30_caso_positivo.py.

SUCESOR DECLARADO, con el cambio y su motivo dentro (EJECUTOR.md regla 2). Todo
lo que el de la vuelta 30 media se mide igual, digito a digito: el conteo, las
huellas repetidas, los rastros de conservacion y las salidas de P.18.

LO QUE SE ANADE, Y NADA MAS QUE ESO: UNA TERCERA CLASE DE PRUEBA, LA DE
CONVERGENCIA. El motivo, con la medicion que lo levanto: la prueba de huella
repetida del instrumento viejo exige que las dos versiones del mismo objeto
COMPARTAN UN TROZO LITERAL de texto. Eso valia para coeficiente_viral, donde los
dos libros escribian la misma cuenta con las mismas palabras (la K, las
invitaciones, el click-through). NO VALE para principio_calidad_mvp, medido hoy:
Ries y Horowitz dicen el mismo objeto con vocabulario distinto y el unico trozo
literal que los dos bloques comparten es 'Lanza'. Con el instrumento viejo, una
fusion legitima quedaria probada por UNA sola prueba y por el conteo.

LA PRUEBA DE CONVERGENCIA mide la fusion sin depender del vocabulario: por cada
grupo fundido se declara un PAR de trozos literales, uno de cada origen. ANTES de
fundir viven en pasos DISTINTOS, asi que CERO pasos contienen los dos y la prueba
CAE. DESPUES tiene que haber EXACTAMENTE UN paso que contenga los dos, y pasa.
Cae antes y pasa despues, que es la vara del criterio de HECHO de
docs/plan/08_VERIFICACION.md. No se afloja ninguna prueba vieja y no se mete
ninguna excepcion por nombre de nodo: un plan sin pruebas_convergencia se mide
exactamente como lo medía el instrumento de la vuelta 30.

Uso:
    python scripts/loop/vuelta32_caso_positivo.py <plan.json>
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


def juntos(d, a, b):
    return sum(1 for p in (d.get("pasos_accionables") or []) if a in p and b in p)


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

        for c in f.get("pruebas_convergencia") or []:
            a, b = c["trozo_a"], c["trozo_b"]
            k = juntos(d, a, b)
            ok = k == 1
            print("  [%s] convergencia: %r y %r viven juntos en %d paso(s), "
                  "se espera 1  (origenes %s)"
                  % ("PASA" if ok else "CAE ", a, b, k, c["origenes"]))
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
