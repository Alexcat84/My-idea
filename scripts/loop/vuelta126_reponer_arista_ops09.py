# -*- coding: utf-8 -*-
"""vuelta126_reponer_arista_ops09.py . REPONE LA ARISTA UNICA QUE LA FUSION DE
OP-S-09 CORTO Y NO DECLARO (TAREA 3.a de la vuelta 126, acta de la vuelta 125,
seccion 4.1 y 4.2).

QUE HACE, Y NO MAS. Repone UNA arista y UNA sola:
    dia_cero_defectos_2 -> eliminacion_causas_error_4
en las DOS vistas: anade 'eliminacion_causas_error_4' a nodos_siguientes de
dia_cero_defectos_2 y anade 'dia_cero_defectos_2' a nodos_previos de
eliminacion_causas_error_4. Ningun otro campo de ninguno de los dos nodos se
toca; ningun otro nodo del catalogo se toca. No es una fusion (no hay actos,
no hay absorbidos): es la reposicion puntual que fundir_por_plan.py no pudo
ver porque el citante original (dia_cero_defectos_3, absorbido en la MISMA
operacion) ya estaba deprecado cuando la pasada de redireccion corrio.

GUARDAS PROPIAS, ademas de las de REGIMEN B (simulacion, mutacion negativa,
rojo real en segunda pasada):
  - los dos nodos existen y siguen VIVOS;
  - la arista NO esta ya puesta en ninguna de las dos vistas (si lo estuviera,
    ROJO: no hay nada que reponer y una segunda escritura fabricaria una
    duplicada);
  - tras anadirla, CERO auto-aristas (ORIGEN != DESTINO, trivial aqui) y CERO
    duplicadas (la arista no estaba, se anade una vez en cada vista);
  - ningun otro campo de ninguno de los dos nodos cambia (se compara el resto
    del dict antes/despues).

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.
--mutacion-negativa fuerza el DESTINO a un nodo DEPRECADO (el propio muerto,
eliminacion_causas_error) para probar que la guarda aborta SIN ESCRIBIR,
pase lo que pase con --ejecutar (la mutacion nunca escribe, es la prueba
negativa).

Uso:
  python scripts/loop/vuelta126_reponer_arista_ops09.py
  python scripts/loop/vuelta126_reponer_arista_ops09.py --ejecutar
  python scripts/loop/vuelta126_reponer_arista_ops09.py --mutacion-negativa
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
ORIGEN = "dia_cero_defectos_2"
DESTINO = "eliminacion_causas_error_4"


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
                     help="fuerza el destino a un nodo DEPRECADO, para probar que la guarda aborta")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    destino = DESTINO
    if a.mutacion_negativa:
        destino = "eliminacion_causas_error"  # el muerto: DEPRECADO a proposito

    modo = "MUTACION NEGATIVA (nunca escribe)" if a.mutacion_negativa else ("EJECUTAR" if a.ejecutar else "SIMULAR")
    print("=" * 78)
    print("REPOSICION DE ARISTA UNICA, OP-S-09 (vuelta 126) . MODO %s" % modo)
    print("arista: %s -> %s" % (ORIGEN, destino))
    print("=" * 78)

    d_origen, c_origen = leer_crudo(ORIGEN)
    d_destino, c_destino = leer_crudo(destino)
    orig_origen = json.loads(json.dumps(d_origen))
    orig_destino = json.loads(json.dumps(d_destino))

    fallos = []
    if d_origen.get("deprecado"):
        fallos.append("%s esta DEPRECADO" % ORIGEN)
    if d_destino.get("deprecado"):
        fallos.append("%s esta DEPRECADO" % destino)

    sig_origen = list(d_origen.get("nodos_siguientes") or [])
    prev_destino = list(d_destino.get("nodos_previos") or [])
    ya_sig = destino in sig_origen
    ya_prev = ORIGEN in prev_destino
    print("guarda 1, los dos nodos existen y siguen VIVOS: %s" % ("OK" if not fallos else "ROJO %s" % fallos))
    if ya_sig or ya_prev:
        fallos.append("la arista %s -> %s YA esta puesta (nodos_siguientes=%s, nodos_previos=%s): "
                      "no hay nada que reponer" % (ORIGEN, destino, ya_sig, ya_prev))
    print("guarda 2, la arista NO estaba puesta todavia: %s"
          % ("OK" if not (ya_sig or ya_prev) else "ROJO"))

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    # --- construir sobre copia en memoria ---
    sig_origen.append(destino)
    prev_destino.append(ORIGEN)
    d_origen["nodos_siguientes"] = sig_origen
    d_destino["nodos_previos"] = prev_destino

    auto = destino == ORIGEN
    dup_sig = len(sig_origen) != len(set(sig_origen))
    dup_prev = len(prev_destino) != len(set(prev_destino))
    print("guarda 3, cero auto-aristas nuevas: %s" % ("OK" if not auto else "ROJO"))
    print("guarda 4, cero duplicadas nuevas (nodos_siguientes de %s, nodos_previos de %s): %s"
          % (ORIGEN, destino, "OK" if not (dup_sig or dup_prev) else "ROJO"))
    if auto or dup_sig or dup_prev:
        fallos.append("guarda 3/4 caida")

    otros_origen = [k for k in d_origen if k != "nodos_siguientes" and d_origen[k] != orig_origen.get(k)]
    otros_destino = [k for k in d_destino if k != "nodos_previos" and d_destino[k] != orig_destino.get(k)]
    print("guarda 5, ningun otro campo cambia: %s"
          % ("OK" if not (otros_origen or otros_destino) else "ROJO %s %s" % (otros_origen, otros_destino)))
    if otros_origen or otros_destino:
        fallos.append("guarda 5 caida: campos tocados de mas %s %s" % (otros_origen, otros_destino))

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    print()
    print("%s.nodos_siguientes: %s" % (ORIGEN, sig_origen))
    print("%s.nodos_previos   : %s" % (destino, prev_destino))

    if a.mutacion_negativa:
        print()
        print("MUTACION NEGATIVA: no debia llegar aqui con destino DEPRECADO. CAIDA DE LA ARNES.")
        return 1

    if not a.ejecutar:
        print()
        print("SIMULACION: cero escrituras.")
        return 0

    escribir(ORIGEN, d_origen, c_origen)
    escribir(destino, d_destino, c_destino)
    print()
    print("ESCRITO. ficheros tocados: 2 (%s, %s)" % (ORIGEN, destino))
    return 0


if __name__ == "__main__":
    sys.exit(main())
