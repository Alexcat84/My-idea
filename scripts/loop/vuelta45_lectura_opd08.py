# -*- coding: utf-8 -*-
"""vuelta45_lectura_opd08.py - LA LECTURA DE CERO DEL NODO DE OP-D-08.
ESTRICTAMENTE DE SOLO LECTURA.

Imprime lienzo_modelo_negocio ENTERO (titulo, fuente, entregable, resumen, los
17 pasos uno a uno, condiciones y el censo de aristas) para que la lectura del
acto se haga sobre el TEXTO y no sobre un resumen, que es lo que P.5 y el modo
continuo obligan.

Y mide LA LINEA BASE DE CERO MOVIMIENTO DE GRAFO que el campo verificacion
exige: vecinos del nodo en sus dos campos, y entradas de arista del grafo
entero. SE MIDE HOY: las cifras que la operacion trae escritas son del corte de
la vuelta 17 y se citan como contraste, no como fuente (EJECUTOR.md regla 2).

Uso: python scripts/loop/vuelta45_lectura_opd08.py <node_id>
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")


def main():
    nid = sys.argv[1] if len(sys.argv) > 1 else "lienzo_modelo_negocio"
    d = json.loads(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8").read())

    print("=" * 78)
    print("EL NODO %s, LEIDO DE CERO Y ENTERO (vuelta 45)" % nid)
    print("=" * 78)
    print()
    print("node_id           : %s" % d["node_id"])
    print("titulo_concepto   : %s" % d.get("titulo_concepto"))
    print("dominio           : %s" % d.get("dominio"))
    print("fase_proyecto     : %s" % d.get("fase_proyecto"))
    print("etiqueta_arbol    : %s" % d.get("etiqueta_arbol"))
    print("fuente            : %s" % d.get("fuente"))
    print("deprecado         : %s" % bool(d.get("deprecado") or d.get("deprecated")))
    print()
    print("entregable_esperado:")
    print("  %s" % d.get("entregable_esperado"))
    print()
    print("resumen_teorico:")
    print("  %s" % d.get("resumen_teorico"))
    print()
    print("condiciones_activacion (%d):" % len(d.get("condiciones_activacion") or []))
    for i, c in enumerate(d.get("condiciones_activacion") or [], 1):
        print("  (%d) %s" % (i, c))
    print()
    pasos = d.get("pasos_accionables") or []
    print("pasos_accionables: %d" % len(pasos))
    print("-" * 78)
    for i, p in enumerate(pasos, 1):
        print("PASO %2d: %s" % (i, p))
        print()
    print("-" * 78)
    print()
    print("### LA LINEA BASE DE CERO MOVIMIENTO DE GRAFO, MEDIDA HOY")
    print()
    prev = d.get("nodos_previos") or []
    sig = d.get("nodos_siguientes") or []
    print("  vecinos declarados por el nodo: previos %d + siguientes %d = %d"
          % (len(prev), len(sig), len(prev) + len(sig)))

    total = 0
    ficheros = 0
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        ficheros += 1
        x = json.loads(io.open(os.path.join(NODOS, nombre), encoding="utf-8").read())
        for c in CAMPOS:
            total += len(x.get(c) or [])
    print("  ficheros del grafo            : %d" % ficheros)
    print("  entradas de arista del grafo  : %d (previos mas siguientes de todos)" % total)
    print()
    print("  CONTRASTE con lo que la operacion trae ESCRITO (corte de la vuelta 17,")
    print("  14 ago 2026), que se cita y NO se usa como fuente (EJECUTOR.md regla 2):")
    print("    la operacion dice 91 vecinos y 16.866 entradas de arista.")
    print("    Si mi medicion de hoy difiere, la DISCREPANCIA se declara, no se copia:")
    print("    lo que la guarda exige es CERO MOVIMIENTO, o sea que el par de cifras")
    print("    de HOY sea el MISMO antes y despues del acto.")
    print()
    print("### LAS ARISTAS PASO A NODO EN LAS QUE ESTE NODO ES HIJO")
    print()
    for madre, paso in (("tipo_de_mercado_estrategia_competitiva", 5),
                        ("customer_discovery_overview", 1),
                        ("unbundling_business_models", 4)):
        ruta = os.path.join(NODOS, madre + ".json")
        if not os.path.exists(ruta):
            print("  %-46s NO EXISTE EL FICHERO" % madre)
            continue
        m = json.loads(io.open(ruta, encoding="utf-8").read())
        mp = m.get("pasos_accionables") or []
        cita = nid in (m.get("nodos_siguientes") or []) or nid in (m.get("nodos_previos") or [])
        print("  madre %-42s pasos %-3d paso %d existe: %s | la madre cita a %s: %s"
              % (madre, len(mp), paso, paso <= len(mp), nid, cita))
    print()
    print("=" * 78)
    print("FIN DE LA LECTURA")
    print("=" * 78)


main()
