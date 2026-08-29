# -*- coding: utf-8 -*-
"""vuelta128_reponer_tres_aristas_fusion.py . REPONE LAS TRES ARISTAS
FABRICADAS POR LA CAMPANA (TAREA 3.a de la vuelta 128, acta de la vuelta
127 seccion 4.1, P.16 punto 1).

QUE HACE, Y NO MAS. Repone estas TRES aristas y ninguna mas, cada una en
las DOS vistas (nodos_siguientes del origen y nodos_previos del destino):
  1. comprension_capacidades_limitaciones_ia -> division_trabajo_humano_ia
  2. ecosistema_global_emprendimiento_gee -> uso_del_us_commercial_service
  3. incentivos_reconocimiento_sostenibilidad -> vision_alineacion_sostenibilidad
Mismo mecanismo que vuelta126_reponer_arista_ops09.py, generalizado a tres
pares. Ningun otro campo de ningun nodo se toca; ningun otro nodo se toca.

GUARDAS PROPIAS, ademas de las de REGIMEN B (simulacion, mutacion negativa,
rojo real en segunda pasada), por cada par:
  - los dos nodos existen y siguen VIVOS;
  - la arista NO esta ya puesta en ninguna de las dos vistas;
  - tras anadirla, CERO auto-aristas y CERO duplicadas nuevas;
  - ningun otro campo de ninguno de los dos nodos cambia.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.
--mutacion-negativa fuerza el DESTINO del primer par a un nodo DEPRECADO
(division_trabajo_humano_ia no aplica; se usa un alias muerto real,
jagged_frontier_ia) para probar que la guarda aborta SIN ESCRIBIR NADA,
ni siquiera los otros dos pares, pase lo que pase con --ejecutar.

Uso:
  python scripts/loop/vuelta128_reponer_tres_aristas_fusion.py
  python scripts/loop/vuelta128_reponer_tres_aristas_fusion.py --ejecutar
  python scripts/loop/vuelta128_reponer_tres_aristas_fusion.py --mutacion-negativa
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

PARES = [
    ("comprension_capacidades_limitaciones_ia", "division_trabajo_humano_ia"),
    ("ecosistema_global_emprendimiento_gee", "uso_del_us_commercial_service"),
    ("incentivos_reconocimiento_sostenibilidad", "vision_alineacion_sostenibilidad"),
]


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def leer_crudo(nid):
    with io.open(ruta(nid), encoding="utf-8", newline="") as fh:
        bruto = fh.read()
    cola = ""
    while bruto and bruto[-1] in "\r\n":
        cola = bruto[-1] + cola
        bruto = bruto[:-1]
    return json.loads(bruto), cola


def escribir(nid, datos, cola):
    with io.open(ruta(nid), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    ap.add_argument("--mutacion-negativa", action="store_true",
                     help="fuerza el destino del primer par a un nodo DEPRECADO, para probar que la guarda aborta")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    pares = list(PARES)
    if a.mutacion_negativa:
        pares[0] = (pares[0][0], "jagged_frontier_ia")  # el muerto: DEPRECADO a proposito

    modo = "MUTACION NEGATIVA (nunca escribe)" if a.mutacion_negativa else ("EJECUTAR" if a.ejecutar else "SIMULAR")
    print("=" * 78)
    print("REPOSICION DE TRES ARISTAS FABRICADAS, vuelta 128 . MODO %s" % modo)
    print("=" * 78)

    cache = {}

    def cargar(nid):
        if nid not in cache:
            d, cola = leer_crudo(nid)
            cache[nid] = [d, cola, json.loads(json.dumps(d))]
        return cache[nid]

    fallos_globales = []
    planes = []

    for origen, destino in pares:
        print()
        print("par: %s -> %s" % (origen, destino))
        if not os.path.exists(ruta(origen)) or not os.path.exists(ruta(destino)):
            fallos_globales.append("%s -> %s: fichero de nodo inexistente" % (origen, destino))
            print("  [ROJO] fichero de nodo inexistente")
            continue

        d_origen, c_origen, orig_origen = cargar(origen)
        d_destino, c_destino, orig_destino = cargar(destino)

        fallos = []
        if d_origen.get("deprecado"):
            fallos.append("%s esta DEPRECADO" % origen)
        if d_destino.get("deprecado"):
            fallos.append("%s esta DEPRECADO" % destino)
        print("  guarda 1, los dos nodos existen y siguen VIVOS: %s" % ("OK" if not fallos else "ROJO %s" % fallos))

        sig_origen = list(d_origen.get("nodos_siguientes") or [])
        prev_destino = list(d_destino.get("nodos_previos") or [])
        ya_sig = destino in sig_origen
        ya_prev = origen in prev_destino
        if ya_sig or ya_prev:
            fallos.append("la arista %s -> %s YA esta puesta (nodos_siguientes=%s, nodos_previos=%s)"
                          % (origen, destino, ya_sig, ya_prev))
        print("  guarda 2, la arista NO estaba puesta todavia: %s" % ("OK" if not (ya_sig or ya_prev) else "ROJO"))

        if fallos:
            fallos_globales.extend(fallos)
            for f in fallos:
                print("  [ROJO] %s" % f)
            continue

        sig_origen_nuevo = sig_origen + [destino]
        prev_destino_nuevo = prev_destino + [origen]
        auto = destino == origen
        dup_sig = len(sig_origen_nuevo) != len(set(sig_origen_nuevo))
        dup_prev = len(prev_destino_nuevo) != len(set(prev_destino_nuevo))
        print("  guarda 3, cero auto-aristas nuevas: %s" % ("OK" if not auto else "ROJO"))
        print("  guarda 4, cero duplicadas nuevas: %s" % ("OK" if not (dup_sig or dup_prev) else "ROJO"))
        if auto or dup_sig or dup_prev:
            fallos_globales.append("%s -> %s: guarda 3/4 caida" % (origen, destino))
            continue

        planes.append((origen, destino, sig_origen_nuevo, prev_destino_nuevo))
        print("  %s.nodos_siguientes (propuesto): %s" % (origen, sig_origen_nuevo))
        print("  %s.nodos_previos (propuesto)   : %s" % (destino, prev_destino_nuevo))

    if fallos_globales:
        print()
        print("SE ABORTA SIN ESCRIBIR NADA, %d fallo(s):" % len(fallos_globales))
        for f in fallos_globales:
            print("  [ROJO] %s" % f)
        return 1

    if a.mutacion_negativa:
        print()
        print("MUTACION NEGATIVA: no debia llegar aqui con un destino DEPRECADO. CAIDA DE LA ARNES.")
        return 1

    for origen, destino, sig_nuevo, prev_nuevo in planes:
        d_origen, c_origen, orig_origen = cache[origen]
        d_destino, c_destino, orig_destino = cache[destino]
        d_origen["nodos_siguientes"] = sig_nuevo
        d_destino["nodos_previos"] = prev_nuevo

    otros_tocados = []
    for nid, (d, c, orig) in cache.items():
        for k in d:
            if k in ("nodos_siguientes", "nodos_previos"):
                continue
            if d[k] != orig.get(k):
                otros_tocados.append("%s.%s" % (nid, k))
    print()
    print("guarda 5, ningun otro campo cambia en ningun nodo tocado: %s"
          % ("OK" if not otros_tocados else "ROJO %s" % otros_tocados))
    if otros_tocados:
        print("SE ABORTA SIN ESCRIBIR: guarda 5 caida.")
        return 1

    if not a.ejecutar:
        print()
        print("SIMULACION: cero escrituras. %d par(es) listos para --ejecutar." % len(planes))
        return 0

    for nid, (d, c, orig) in cache.items():
        escribir(nid, d, c)
    print()
    print("ESCRITO. ficheros tocados: %d (%s)" % (len(cache), ", ".join(sorted(cache.keys()))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
