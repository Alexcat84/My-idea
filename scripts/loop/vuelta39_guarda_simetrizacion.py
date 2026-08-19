# -*- coding: utf-8 -*-
"""vuelta39_guarda_simetrizacion.py

LA GUARDA QUE EL PLAN SELLADO DE LA VUELTA 38 DEJO ESCRITA PARA EL DIA DE LA
EJECUCION, corrida contra el log del ciclo y contra los ficheros de nodos.

QUE COMPRUEBA, y las tres tienen que dar verde por separado:

  1. SIMETRIZACION EXACTA. `symmetrize_added` de dataset/metadata/phase1_run_log.json
     tiene que traer EXACTAMENTE las aristas de `simulacion.simetrizacion_esperada`
     del plan para el superviviente: ni una mas ni una menos, y ninguna para otro
     nodo. El plan lo dice con esas palabras y por eso se coteja por conjunto y no
     por conteo: 16 entradas equivocadas tambien son 16.
     POR QUE SE MIDE SOBRE EL LOG: quien escribe estas aristas NO es el ejecutor de
     fusiones (el redirige a los vecinos y no toca la lista propia del
     superviviente) sino scripts/run_phase1.py en su paso 5. El precedente esta
     medido en el commit 72c718ea.
  2. LA ARISTA ESTA DE VERDAD EN EL FICHERO. Un log dice lo que el paso 5 CREE que
     hizo; el fichero dice lo que paso. Las 16 se releen en dataset/nodos.
  3. EL CUARTO MIEMBRO LLEGO SOLO. Tras el ciclo, el superviviente y el cuarto
     miembro tienen que quedar declarados CADA UNO EN EL EXTREMO DEL OTRO, medido
     sobre los DOS ficheros y no sobre el grafo compilado.

Uso:
  python scripts/loop/vuelta39_guarda_simetrizacion.py --plan <ruta> [--cuarto <id>]
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
LOG = os.path.join(RAIZ, "dataset", "metadata", "phase1_run_log.json")
CAMPOS = ("nodos_previos", "nodos_siguientes")
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}


def nodo(nid):
    return json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))


def main():
    plan_ruta = cuarto = None
    argv = sys.argv[1:]
    for i, x in enumerate(argv):
        if x == "--plan":
            plan_ruta = argv[i + 1]
        elif x == "--cuarto":
            cuarto = argv[i + 1]
    if not plan_ruta:
        sys.exit("hace falta --plan <ruta>")

    plan = json.load(io.open(plan_ruta, encoding="utf-8"))
    sup = plan["superviviente"]
    esp = plan["simulacion"]["simetrizacion_esperada"]
    aristas = esp["aristas"]

    print("PLAN        : %s" % plan_ruta)
    print("SUPERVIVIENTE: %s" % sup)
    print("LA GUARDA, tal como el plan la dejo escrita:")
    print("  %s" % esp["guarda_para_el_dia_de_la_ejecucion"])
    print("=" * 78)

    log = json.load(io.open(LOG, encoding="utf-8"))
    sa = log.get("symmetrize_added") or []

    medido = sorted((x["key"], x["added"]) for x in sa if x.get("node") == sup)
    otros = sorted((x.get("node"), x.get("key"), x.get("added")) for x in sa if x.get("node") != sup)
    esperado = sorted((a["campo"], a["vecino"]) for a in aristas)

    print("### 1. symmetrize_added DEL LOG DEL CICLO")
    print("  entradas totales en el log        : %d" % len(sa))
    print("  entradas para %-22s: %d" % (sup, len(medido)))
    print("  entradas para OTROS nodos         : %d" % len(otros))
    for o in otros:
        print("      %s" % (o,))
    print("  el plan esperaba                  : %d" % len(esperado))
    faltan = [x for x in esperado if x not in medido]
    sobran = [x for x in medido if x not in esperado]
    for campo, vecino in esperado:
        marca = "OK " if (campo, vecino) in medido else "FALTA"
        print("    [%s] %-18s %s" % (marca, campo, vecino))
    for campo, vecino in sobran:
        print("    [SOBRA] %-18s %s" % (campo, vecino))
    ok1 = (medido == esperado) and not otros
    print("  GUARDA 1, simetrizacion EXACTA (faltan %d, sobran %d, de otros nodos %d): %s"
          % (len(faltan), len(sobran), len(otros), "OK" if ok1 else "ROJO"))

    print()
    print("### 2. LAS ARISTAS RELEIDAS EN EL FICHERO DEL SUPERVIVIENTE")
    d = nodo(sup)
    en_fichero = 0
    for campo, vecino in esperado:
        hay = vecino in (d.get(campo) or [])
        en_fichero += 1 if hay else 0
        if not hay:
            print("    [ROJO] %-18s %s NO esta en el fichero" % (campo, vecino))
    print("  GUARDA 2, %d de %d aristas presentes en dataset/nodos/%s.json: %s"
          % (en_fichero, len(esperado), sup, "OK" if en_fichero == len(esperado) else "ROJO"))
    ok2 = en_fichero == len(esperado)

    ok3 = True
    if cuarto:
        print()
        print("### 3. EL CUARTO MIEMBRO, %s, DECLARADO EN LOS DOS EXTREMOS" % cuarto)
        c = nodo(cuarto)
        aqui = [k for k in CAMPOS if cuarto in (d.get(k) or [])]
        alla = [k for k in CAMPOS if sup in (c.get(k) or [])]
        print("    %-38s nombra a %-30s en %s" % (sup, cuarto, aqui or "NINGUN CAMPO"))
        print("    %-38s nombra a %-30s en %s" % (cuarto, sup, alla or "NINGUN CAMPO"))
        reciproca = bool(aqui) and bool(alla) and all(OPUESTO[k] in alla for k in aqui)
        print("  GUARDA 3, la arista esta en los dos ficheros y en campos opuestos: %s"
              % ("OK" if reciproca else "ROJO"))
        ok3 = reciproca

    print()
    print("=" * 78)
    todo = ok1 and ok2 and ok3
    print("RESULTADO: %s" % ("TODAS LAS GUARDAS VERDES" if todo else "HAY ROJO, SE PARA"))
    return 0 if todo else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
