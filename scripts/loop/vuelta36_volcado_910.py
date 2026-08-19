# -*- coding: utf-8 -*-
"""vuelta36_volcado_910.py - EL VOLCADO DE LAS CINCO RELECTURAS DE P.5 SOBRE OP-D-03.

SUCESOR DECLARADO de scripts/loop/vuelta34_volcado_910.py, y lo que cambia va
dicho (EJECUTOR.md regla 2): aquel construia el texto de las razones dentro del
propio script; este NO ESCRIBE NI UNA LETRA DE RAZON. Las cinco razones ya
existen, escritas y selladas por la vuelta 35 en docs/loop/PROPUESTA_V35_RELECTURAS.json,
y este instrumento SOLO LAS LEE DE AHI Y LAS REVERIFICA CONTRA EL ARCHIVO DE HOY.

POR QUE ESE CAMBIO Y NO OTRO: la vuelta 35 paro por la regla 5 de EJECUTOR.md
(lo que contradice una cifra publicada no lo arregla el ejecutor) y el fundador
decidio el 15 ago 2026, en docs/loop/paradas/2026-08-15-p5-rancios-opd03-DECISION.md,
que las cinco se vuelcan. Reescribir aqui el texto que aquella vuelta sello seria
volcar OTRA cosa que la que el fundador aprobo.

  277  A -> D   funnel_get_customers_optimizacion contra optimizacion_embudo_get_customers
  374  A -> D   split_testing contra split_testing_experimentos_ab
  452  A -> D   ab_testing_optimizacion contra split_testing
  1571 A -> D   split_testing_experimentos_ab contra test_ab_precio
  1575 A -> D   ab_testing_optimizacion contra test_ab_precio

LAS GUARDAS SE VUELVEN A CORRER HOY, NO SE HEREDAN DE LA PROPUESTA. Una guarda
verde el 15 de agosto no dice nada del 18: EJECUTOR.md regla 2, el instrumento
manda y se corre EN ESTA VUELTA.

  1. los seis nodos del acto tienen HOY los pasos que las razones afirman.
  2. cada puesto sigue registrado y sigue en la clase A que la propuesta espera.
  3. LA RAZON VIEJA DEL ARCHIVO DE HOY queda LITERAL dentro de la razon nueva de
     la propuesta. Es la guarda que prueba que la propuesta se sello contra ESTE
     archivo y no contra otro: si alguien hubiera tocado esas cinco razones desde
     el 15 de agosto, esta guarda cae.
  4. las aristas internas, buscadas EN LOS DOS SENTIDOS contra el grafo, siguen
     sin existir, tal como las cinco razones afirman.
  5. el par 643 NO entra en el lote: es la lectura dirigida de la TAREA 2 y va
     por su propio carril.
  6. el marcador esperado tras el volcado se imprime ANTES de volcar, y el
     encargo del fundador lo fija en A 576 / B 83 / C 8 / D 2721 con n 3388.
     Si el conteo de aqui no da eso, ABORTA.

Uso: python scripts/loop/vuelta36_volcado_910.py
Salida: docs/loop/_lote_v36.jsonl. El archivo lo escribe scripts/corregir_veredicto.py.
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
PROPUESTA = os.path.join(RAIZ, "docs", "loop", "PROPUESTA_V35_RELECTURAS.json")
LOTE = os.path.join(RAIZ, "docs", "loop", "_lote_v36.jsonl")

# Los seis nodos del acto y los pasos que las razones de la propuesta afirman.
PASOS_HOY = {
    "ab_testing_optimizacion": 5,
    "optimizacion_embudo_get_customers": 5,
    "split_testing_experimentos_ab": 5,
    "funnel_get_customers_optimizacion": 7,
    "split_testing": 4,
    "test_ab_precio": 5,
}

# Los pares cuya razon afirma NO HAY NINGUNA ARISTA, buscados en los dos sentidos.
SIN_ARISTA = {
    277: ("funnel_get_customers_optimizacion", "optimizacion_embudo_get_customers"),
    374: ("split_testing", "split_testing_experimentos_ab"),
    452: ("ab_testing_optimizacion", "split_testing"),
    1571: ("split_testing_experimentos_ab", "test_ab_precio"),
    1575: ("ab_testing_optimizacion", "test_ab_precio"),
}

CLASE_VIEJA = "A"
CLASE_NUEVA = "D"

# La cifra que el encargo del fundador fija, escrita AQUI y no leida de ningun
# reporte: si el conteo del archivo de hoy no la produce, se para.
ESPERADO = {"n": 3388, "A": 576, "B": 83, "C": 8, "D": 2721}


def leer_nodo(nid):
    return json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))


def main():
    prop = json.load(io.open(PROPUESTA, encoding="utf-8"))
    filas_prop = {f["puesto"]: f for f in prop["filas"]}
    print("=" * 78)
    print("LA PROPUESTA SELLADA, leida y no reescrita: %s"
          % os.path.relpath(PROPUESTA, RAIZ).replace("\\", "/"))
    print("  vuelta %s, fecha %s, filas %d" % (prop["vuelta"], prop["fecha"], len(prop["filas"])))
    print("  estado que traia: %s" % prop["estado"])
    print()

    if sorted(filas_prop) != sorted(SIN_ARISTA):
        print("ABORTA: la propuesta trae los puestos %s y este volcado espera %s"
              % (sorted(filas_prop), sorted(SIN_ARISTA)))
        return 1
    if 643 in filas_prop:
        print("ABORTA: el 643 no va en este lote, va por la lectura dirigida de la TAREA 2")
        return 1
    print("  GUARDA 5: el 643 NO esta en el lote. OK")

    print("\n" + "=" * 78)
    print("GUARDA 1: los pasos de HOY, contra lo que las razones de la propuesta afirman")
    print("=" * 78)
    G = {}
    for nid, esperado in sorted(PASOS_HOY.items()):
        d = leer_nodo(nid)
        G[nid] = d
        real = len(d.get("pasos_accionables") or [])
        print("  %-38s %2d pasos (la razon dice %d)  %s"
              % (nid, real, esperado, "OK" if real == esperado else "ABORTA"))
        if real != esperado:
            return 1

    print("\n" + "=" * 78)
    print("GUARDA 4: las aristas internas, buscadas EN LOS DOS SENTIDOS contra el grafo")
    print("=" * 78)
    for puesto in sorted(SIN_ARISTA):
        a, b = SIN_ARISTA[puesto]
        da, db = G[a], G[b]
        hay = (b in (da.get("nodos_siguientes") or []) or b in (da.get("nodos_previos") or [])
               or a in (db.get("nodos_siguientes") or []) or a in (db.get("nodos_previos") or []))
        print("  %-5d %-36s contra %-36s arista: %s  %s"
              % (puesto, a, b, "SI" if hay else "NO", "ABORTA" if hay else "OK"))
        if hay:
            print("       la razon sellada afirma que NO hay ninguna, y el grafo dice que si.")
            return 1

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_puesto = {v["puesto_intra"]: v for v in V}

    print("\n" + "=" * 78)
    print("GUARDAS 2 y 3: la clase de hoy, y la razon vieja DEL ARCHIVO DE HOY dentro")
    print("=" * 78)
    filas = []
    for puesto in sorted(filas_prop):
        v = por_puesto.get(puesto)
        if v is None:
            print("ABORTA: el puesto %d no esta registrado en el archivo" % puesto)
            return 1
        if v["clase"] != CLASE_VIEJA:
            print("ABORTA: el puesto %d esta en %r y la propuesta esperaba %r"
                  % (puesto, v["clase"], CLASE_VIEJA))
            return 1
        fila = filas_prop[puesto]
        if fila["clase"] != CLASE_NUEVA:
            print("ABORTA: la propuesta lleva el %d a %r y este volcado espera %r"
                  % (puesto, fila["clase"], CLASE_NUEVA))
            return 1
        razon_vieja_hoy = v["razon"]
        if razon_vieja_hoy not in fila["razon"]:
            print("ABORTA: la razon vieja del %d, LEIDA DEL ARCHIVO DE HOY, no esta literal "
                  "dentro de la razon sellada. La propuesta se sello contra otro archivo."
                  % puesto)
            return 1
        filas.append({"puesto": puesto, "clase": fila["clase"], "razon": fila["razon"]})
        print("  %-5d %s -> %s  %-36s contra %-36s  vieja %5d car. literal dentro de %5d  OK"
              % (puesto, v["clase"], fila["clase"], v["nodo_a"], v["nodo_b"],
                 len(razon_vieja_hoy), len(fila["razon"])))

    print("\n" + "=" * 78)
    print("GUARDA 6: el marcador, contado AQUI y contrastado con la cifra del encargo")
    print("=" * 78)
    conteo = {}
    for v in V:
        conteo[v["clase"]] = conteo.get(v["clase"], 0) + 1
    ahora = {"n": len(V), "A": conteo.get("A", 0), "B": conteo.get("B", 0),
             "C": conteo.get("C", 0), "D": conteo.get("D", 0)}
    tras = {"n": ahora["n"], "A": ahora["A"] - len(filas), "B": ahora["B"],
            "C": ahora["C"], "D": ahora["D"] + len(filas)}
    print("  MARCADOR DE AHORA, contado aqui:  n %d, A %d, B %d, C %d, D %d"
          % (ahora["n"], ahora["A"], ahora["B"], ahora["C"], ahora["D"]))
    print("  MARCADOR TRAS EL VOLCADO:         n %d, A %d, B %d, C %d, D %d"
          % (tras["n"], tras["A"], tras["B"], tras["C"], tras["D"]))
    print("  EL QUE FIJA EL ENCARGO:           n %d, A %d, B %d, C %d, D %d"
          % (ESPERADO["n"], ESPERADO["A"], ESPERADO["B"], ESPERADO["C"], ESPERADO["D"]))
    if tras != ESPERADO:
        print("  ABORTA: no coinciden. El encargo manda PARAR si da otra cosa.")
        return 1
    print("  COINCIDEN. OK")

    with io.open(LOTE, "w", encoding="utf-8") as fh:
        for f in filas:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")
    print("\nESCRITO el lote: %s (%d filas). El archivo lo escribe "
          "scripts/corregir_veredicto.py, y despues se recomputa el marcador con "
          "scripts/loop/vuelta31_estado.py. Si aquel diera otra cosa que la de arriba, SE PARA."
          % (os.path.relpath(LOTE, RAIZ).replace("\\", "/"), len(filas)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
