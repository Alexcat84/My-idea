# -*- coding: utf-8 -*-
"""vuelta34_mov2.py - EL RECOMPUTO DEL APOYO del MOVIMIENTO 2 de OP-D-01.

ESTRICTAMENTE DE SOLO LECTURA.

QUE RECOMPUTA. El movimiento 2 de `OP-D-01` (acta y reporte de la vuelta 32)
concluye que `principio_calidad_mvp` no tiene costura interna que destejer, y lo
sostiene en DOS cifras: mejor pareja 51,2 contra 80, y mejor alineacion de
bloques 0,0 contra 44. LA SEGUNDA NO MEDIA LO QUE DECIA MEDIR: con MIN_BLOQUE en
3 y un nodo de siete pasos el rango existia, pero el emparejamiento monotono no
llegaba a las TRES parejas que el promedio exigia, asi que devolvia 0,0. Con la
recalibracion del 15 ago 2026 la senal si aplica, y hay que volver a medir.

DE DONDE SALE LA CIFRA, dicho antes de darla, porque es lo delicado. El
instrumento sellado `scripts/costuras_internas.py` SE NIEGA A ENTREGAR y desde
hoy tambien se niega a que le importen las senales (la puerta se mudo a ellas).
Asi que la cifra de contraste NO se le pide a el: se mide con las senales
REIMPLEMENTADAS aqui, copiadas literales de las suyas. ESO NO ES SALTARSE LA
BARANDA Y SE DICE POR QUE: la baranda existe para impedir que se publique como
veredicto la salida de un instrumento descalibrado, y esto no publica un
veredicto, publica LA MEDICION DE LA PROPIA DESCALIBRACION, que es lo unico que
no se puede medir con la puerta puesta. Va marcado en cada linea de salida.

Y LA VARA FINAL NO ES ESTA: es la lectura del nodo ENTERO, que se imprime abajo.
Ninguna cola sustituye a leer el nodo.

Uso: python scripts/loop/vuelta34_mov2.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

NODO = "principio_calidad_mvp"
UMBRAL_PAREJA = 80.0
UMBRAL_BLOQUE = 44.0
MIN_BLOQUE_VIEJO = 3
MIN_BLOQUE_NUEVO = 2


def peor_pareja(ratio, pasos):
    mejor = (0.0, 0, 0)
    for a in range(len(pasos)):
        for b in range(a + 1, len(pasos)):
            s = ratio(pasos[a], pasos[b])
            if s > mejor[0]:
                mejor = (s, a + 1, b + 1)
    return mejor


def bloques(ratio, pasos, minimo):
    """Todos los cortes con su puntaje, no solo el mejor: asi se ve DONDE dice la
    senal que esta la costura, que es la mitad util de esta senal."""
    fuera = []
    n = len(pasos)
    for corte in range(minimo, n - minimo + 1):
        a, b = pasos[:corte], pasos[corte:]
        j, puntajes = 0, []
        for paso in b:
            candidatos = [(ratio(a[k], paso), k) for k in range(j, len(a))]
            if not candidatos:
                break
            s, k = max(candidatos)
            puntajes.append(s)
            j = k + 1
        if len(puntajes) >= minimo:
            score = sum(sorted(puntajes, reverse=True)[:minimo]) / minimo
            fuera.append((corte, score, len(puntajes)))
        else:
            fuera.append((corte, None, len(puntajes)))
    return fuera


def main():
    from rapidfuzz.fuzz import token_sort_ratio as ratio
    d = json.load(io.open(os.path.join(NODOS, NODO + ".json"), encoding="utf-8"))
    pasos = d.get("pasos_accionables") or []

    print("EL NODO ENTERO, que es la vara final")
    print("=" * 78)
    print("  id        : %s" % NODO)
    print("  titulo    : %s" % d.get("titulo_concepto"))
    print("  fuente    : %s" % d.get("fuente"))
    print("  deprecado : %s" % bool(d.get("deprecado")))
    print("  PASOS (%d):" % len(pasos))
    for i, p in enumerate(pasos, 1):
        print("    %2d. %s" % (i, p))
    for i, c in enumerate(d.get("condiciones_activacion") or [], 1):
        print("  cond %d: %s" % (i, c))
    print("  entregable: %s" % d.get("entregable_esperado"))

    print()
    print("LA MEDICION DE CONTRASTE (senales REIMPLEMENTADAS, no importadas:")
    print("el instrumento sellado se niega a entregar y a ser importado)")
    print("=" * 78)
    sp = peor_pareja(ratio, pasos)
    print("  SENAL 1, pareja de pasos : %.1f (pasos %d y %d) contra umbral %.0f  -> %s"
          % (sp[0], sp[1], sp[2], UMBRAL_PAREJA,
             "DISPARA" if sp[0] >= UMBRAL_PAREJA else "no dispara"))
    print("     (la vuelta 32 publico 51,2: %s)"
          % ("SE REPRODUCE" if abs(sp[0] - 51.2) < 0.05 else "NO SE REPRODUCE"))
    for etiqueta, minimo in (("VIEJA (MIN_BLOQUE 3)", MIN_BLOQUE_VIEJO),
                             ("NUEVA (MIN_BLOQUE 2)", MIN_BLOQUE_NUEVO)):
        print("\n  SENAL 2 con la regla %s, CORTE POR CORTE:" % etiqueta)
        filas = bloques(ratio, pasos, minimo)
        if not filas:
            print("     NO APLICA: el nodo no llega al minimo de %d pasos" % (minimo * 2))
            continue
        mejor = (0.0, 0)
        for corte, score, emparejados in filas:
            if score is None:
                print("     corte tras %2d: SIN PUNTAJE (solo %d emparejamientos monotonos, "
                      "hacen falta %d)" % (corte, emparejados, minimo))
            else:
                print("     corte tras %2d: %.1f  (%d emparejamientos)" % (corte, score, emparejados))
                if score > mejor[0]:
                    mejor = (score, corte)
        print("     MEJOR: %.1f con corte tras %d  contra umbral %.0f  -> %s"
              % (mejor[0], mejor[1], UMBRAL_BLOQUE,
                 "DISPARA" if mejor[0] >= UMBRAL_BLOQUE else "no dispara"))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
