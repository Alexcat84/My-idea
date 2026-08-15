"""Vuelta 32, OP-D-01 movimiento 2: MIDE la costura interna que queda en pie.

ESTRICTAMENTE DE SOLO LECTURA. No toca ningun nodo y no escribe en docs/: lo
unico que hace es imprimir.

POR QUE NO SE CORRE scripts/costuras_internas.py A SECAS: ese instrumento barre
el catalogo ENTERO y REESCRIBE sus dos salidas en docs/, y esta vuelta no tiene
encargo de recomputar el censo de costuras del archivo. Lo que hace falta aqui es
la misma medicion sobre DOS nodos. Asi que este script IMPORTA sus dos funciones
y sus dos umbrales del fichero original en vez de copiarlos: si manana el umbral
cambia alli, cambia aqui solo, y las dos cifras siguen siendo comparables con las
publicadas.

  SENAL 1, PAREJA DE PASOS: token_sort_ratio entre cada dos pasos del nodo,
  umbral 80. Caza el paso repetido casi literal.
  SENAL 2, ALINEACION DE BLOQUES: el mejor corte de la lista, umbral 44. Caza el
  bloque reiniciado y dice donde esta el corte.

Uso: python scripts/loop/vuelta32_costura_opd01.py [nodo ...]
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

import costuras_internas as CI  # noqa: E402

POR_DEFECTO = ["producto_minimo_viable", "principio_calidad_mvp"]


def main():
    from rapidfuzz.fuzz import token_sort_ratio as ratio

    nombres = sys.argv[1:] or POR_DEFECTO
    print("=" * 78)
    print("COSTURA INTERNA QUE QUEDA EN PIE, medida HOY")
    print("umbrales importados de scripts/costuras_internas.py: PAREJA %d, BLOQUE %d"
          % (CI.UMBRAL_PAREJA, CI.UMBRAL_BLOQUE))
    print("=" * 78)
    for nid in nombres:
        ruta = os.path.join(NODOS, nid + ".json")
        if not os.path.exists(ruta):
            print("\n%s: AUSENTE" % nid)
            continue
        with open(ruta, encoding="utf-8") as fh:
            d = json.load(fh)
        pasos = list(d.get("pasos_accionables") or [])
        cond = list(d.get("condiciones_activacion") or [])
        print()
        print("-" * 78)
        print("NODO %s" % nid)
        print("  fuente     : %s" % d.get("fuente"))
        print("  pasos      : %d      condiciones: %d" % (len(pasos), len(cond)))
        for i, p in enumerate(pasos, 1):
            print("    %2d. %s" % (i, p))

        pareja = CI.peor_pareja(ratio, pasos)
        bloque = CI.mejor_bloque(ratio, pasos)
        print()
        print("  SENAL 1, mejor pareja de pasos : %s" % (pareja,))
        print("  SENAL 2, mejor alineacion bloque: %s" % (bloque,))
        v1 = pareja[0] if pareja else 0
        v2 = bloque[0] if bloque else 0
        dispara = (v1 >= CI.UMBRAL_PAREJA) or (v2 >= CI.UMBRAL_BLOQUE)
        print("  DISPARA ALGUNA SENAL: %s" % ("SI, sigue siendo CITA PARA LEER"
                                              if dispara else "NO"))
    print()
    print("=" * 78)
    print("FIN. Este instrumento CITA, no juzga: la lectura la hace el ejecutor.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
