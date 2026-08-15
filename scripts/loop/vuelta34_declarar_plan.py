# -*- coding: utf-8 -*-
"""vuelta34_declarar_plan.py - la CORRECCION DECLARADA en el plan de la fusion.

EJECUTOR.md regla 8: una correccion que tapa lo que corrige no se puede auditar.
Nada del plan sellado se reescribe; se le ANADE una entrada al bloque
`correcciones_declaradas` que ya existe, con la cifra vieja dentro.

QUE DECLARA: el plan de la fusion de OP-D-02 se sello el 15 ago 2026 dando por
cerrada la redireccion de tres sitios vivos, y su caso positivo la midio verde
ANTES del Gate 0 y en rojo DESPUES (22 de 23). El plan no estaba mal: le faltaba
una pieza que no era suya, la del paso 5 del Gate. Con la decision del fundador
aplicada, la redireccion se rehizo y el mismo caso positivo da 23 de 23 DESPUES
del Gate 0, que es la unica medicion que prueba estabilidad.

Uso:
  python scripts/loop/vuelta34_declarar_plan.py            (simulacion)
  python scripts/loop/vuelta34_declarar_plan.py --aplicar
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "loop", "PLAN_V33_OPD02_FUSION.json")

MARCA = "2026-08-15, vuelta 34"

ENTRADA = {
    "fecha": "2026-08-15",
    "vuelta": 34,
    "campo": "redirecciones_esperadas (la medicion que las acompanaba, no el campo)",
    "que_se_corrige": (
        "El plan se sello con TRES redirecciones vivas y su caso positivo dio 23 de 23 "
        "ANTES de correr el Gate 0 y 22 de 23 DESPUES (la prueba que caia era 'ningun "
        "nodo VIVO sigue nombrando a enfoque_mercado_voc: quedan 3'). LA CIFRA VIEJA SE "
        "QUEDA ESCRITA: 22 de 23 tras Gate 0, publicada en rojo por el reporte de la "
        "vuelta 33, seccion 6.1."
    ),
    "la_causa_no_era_del_plan": (
        "El paso 5 de scripts/run_phase1.py reciprocaba las aristas que nacen en nodos "
        "deprecados, y el absorbido conserva las suyas: el Gate devolvia el id del muerto "
        "a los tres vivos de los que la fusion lo habia quitado."
    ),
    "que_se_hizo": (
        "Decision del fundador del 15 ago 2026, opcion a de "
        "docs/loop/paradas/2026-08-15-cableado-deprecado-y-costuras.md: el deprecado "
        "conserva su cableado como archivo y el Gate deja de reciprocar lo que nace en el. "
        "Con el paso 5 ya corregido se rehizo la redireccion con "
        "scripts/loop/vuelta34_redirigir.py (seis guardas, ninguna toca texto de nodo)."
    ),
    "la_cifra_de_hoy": (
        "23 PASAN, 0 CAEN, medido DESPUES del ciclo entero de Gate 0 "
        "(docs/loop/SALIDA_V34_OPD02_CASO_TRAS_GATE0.txt), y el paso 5 de esa corrida "
        "reporta 0 nodos actualizados: ya no hay nada que devolver."
    ),
    "lo_que_esto_no_dice": (
        "No dice que el caso positivo de la vuelta 33 estuviera mal medido. Estaba bien "
        "medido y por eso se publico en rojo. Lo que cambio es el instrumento debajo."
    ),
}


def main():
    aplicar = "--aplicar" in sys.argv
    plan = json.load(io.open(PLAN, encoding="utf-8"))
    previas = plan.get("correcciones_declaradas") or []
    print("PLAN: %s" % os.path.basename(PLAN))
    print("correcciones declaradas ANTES: %d" % len(previas))
    for c in previas:
        print("  - vuelta %s, campo %s" % (c.get("vuelta"), c.get("campo")))
    if any(c.get("vuelta") == 34 for c in previas):
        print("YA APLICADA: el plan ya trae la correccion de la vuelta 34.")
        return 0

    print("\nENTRADA NUEVA:")
    print(json.dumps(ENTRADA, ensure_ascii=False, indent=2))
    if not aplicar:
        print("\n(simulacion: sin --aplicar no se escribe nada)")
        return 0

    plan["correcciones_declaradas"] = previas + [ENTRADA]
    with io.open(PLAN, "w", encoding="utf-8") as fh:
        json.dump(plan, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    de_vuelta = json.load(io.open(PLAN, encoding="utf-8"))
    print("\nVERIFICADO TRAS ESCRIBIR: %d claves, %d correcciones declaradas, "
          "y los campos operativos intactos (superviviente=%s, absorbido=%s, "
          "redirecciones_esperadas=%d)"
          % (len(de_vuelta), len(de_vuelta["correcciones_declaradas"]),
             de_vuelta["superviviente"], de_vuelta["absorbido"],
             len(de_vuelta["redirecciones_esperadas"])))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
