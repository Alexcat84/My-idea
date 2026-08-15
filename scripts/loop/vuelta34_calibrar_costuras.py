# -*- coding: utf-8 -*-
"""vuelta34_calibrar_costuras.py - LA MEDICION de la recalibracion, ANTES de tocar el instrumento.

ESTRICTAMENTE DE SOLO LECTURA. No toca scripts/costuras_internas.py, no toca un
nodo, no escribe ninguna cola. Solo mide e imprime.

POR QUE EXISTE. La decision del fundador del 15 ago 2026 manda `MIN_BLOQUE` a 2
con senal para todo nodo de cuatro pasos o mas. `MIN_BLOQUE` no es un solo dial:
vive en TRES sitios de la senal de bloque y cambiarlo cambia la ESCALA del
puntaje, no solo el rango de cortes:

  1. `range(MIN_BLOQUE, n - MIN_BLOQUE + 1)`  -> que cortes se prueban
  2. `if len(puntajes) >= MIN_BLOQUE`          -> cuantos emparejamientos exige
  3. `sum(sorted(...)[:MIN_BLOQUE]) / MIN_BLOQUE` -> promedio de las MEJORES K

El punto 3 es el que mueve la vara: promediar las DOS mejores en vez de las TRES
sube el puntaje de TODO el catalogo, y el umbral 44 se queda donde estaba. El
costo de eso se mide AQUI y se publica ANTES de aplicar nada, porque una baranda
que caza lo correcto no es estricta, esta rota, y esa frase la escribio el propio
instrumento.

Uso: python scripts/loop/vuelta34_calibrar_costuras.py
"""
import io
import json
import os
import statistics
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

UMBRAL_PAREJA = 80.0
UMBRAL_BLOQUE = 44.0

CALIBRACION = ("plan_mejora_procesos", "economia_circular_como_modelo_de_negocio")
SEIS_OPD03 = ("ab_testing_optimizacion", "funnel_get_customers_optimizacion",
              "optimizacion_embudo_get_customers", "split_testing",
              "split_testing_experimentos_ab", "test_ab_precio")
APOYO_ACTA32 = ("principio_calidad_mvp",)
EL_FALSO_NEGATIVO = ("propuesta_gasto_capital",)


def peor_pareja(ratio, pasos):
    mejor = (0.0, 0, 0)
    for a in range(len(pasos)):
        for b in range(a + 1, len(pasos)):
            s = ratio(pasos[a], pasos[b])
            if s > mejor[0]:
                mejor = (s, a + 1, b + 1)
    return mejor


def mejor_bloque(ratio, pasos, minimo):
    """La senal de bloque con MIN_BLOQUE parametrizado. Copia literal de la de
    scripts/costuras_internas.py salvo que el minimo entra por argumento."""
    mejor = (0.0, 0)
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
            if score > mejor[0]:
                mejor = (score, corte)
    return mejor


def main():
    from rapidfuzz.fuzz import token_sort_ratio as ratio

    nodos = json.loads(io.open(GRAFO, encoding="utf-8").read())["nodos"]
    activos = {k: v for k, v in nodos.items() if not v.get("deprecado")}
    print("GRAFO: %d nodos, %d activos" % (len(nodos), len(activos)))
    print("Umbrales SIN TOCAR: pareja %.0f, bloque %.0f" % (UMBRAL_PAREJA, UMBRAL_BLOQUE))
    print("=" * 78)

    filas = []
    for nid, n in sorted(activos.items()):
        pasos = n.get("pasos_accionables") or []
        if len(pasos) < 2:
            continue
        s_par = peor_pareja(ratio, pasos)[0]
        v = mejor_bloque(ratio, pasos, 3) if len(pasos) >= 6 else (0.0, 0)
        nu = mejor_bloque(ratio, pasos, 2) if len(pasos) >= 4 else (0.0, 0)
        filas.append({
            "id": nid, "pasos": len(pasos), "pareja": s_par,
            "viejo": v[0], "corte_viejo": v[1],
            "nuevo": nu[0], "corte_nuevo": nu[1],
            "aplica_viejo": len(pasos) >= 6, "aplica_nuevo": len(pasos) >= 4,
        })

    def cola(clave, aplica):
        return [f for f in filas
                if f["pareja"] >= UMBRAL_PAREJA
                or (f[aplica] and f[clave] >= UMBRAL_BLOQUE)]

    cv, cn = cola("viejo", "aplica_viejo"), cola("nuevo", "aplica_nuevo")
    solo_p = [f for f in filas if f["pareja"] >= UMBRAL_PAREJA]
    print("\n--- EL COSTO DEL CAMBIO, medido sobre el catalogo entero ---")
    print("  nodos evaluados (2 pasos o mas)        : %d" % len(filas))
    print("  con senal de bloque VIEJA (n>=6)       : %d" % sum(1 for f in filas if f["aplica_viejo"]))
    print("  con senal de bloque NUEVA (n>=4)       : %d" % sum(1 for f in filas if f["aplica_nuevo"]))
    print("  NO APLICA con la nueva (n<4)           : %d" % sum(1 for f in filas if not f["aplica_nuevo"]))
    print("  cola por PAREJA sola (no cambia)       : %d" % len(solo_p))
    print("  COLA CON LA REGLA VIEJA (MIN_BLOQUE 3) : %d" % len(cv))
    print("  COLA CON LA REGLA NUEVA (MIN_BLOQUE 2) : %d   (%.1f por ciento del catalogo activo)"
          % (len(cn), 100.0 * len(cn) / len(activos)))
    print("  citas NUEVAS que entran                : %d" % len(set(f["id"] for f in cn) - set(f["id"] for f in cv)))
    print("  citas que SALEN                        : %d" % len(set(f["id"] for f in cv) - set(f["id"] for f in cn)))

    bv = [f["viejo"] for f in filas if f["aplica_viejo"] and f["corte_viejo"]]
    bn = [f["nuevo"] for f in filas if f["aplica_nuevo"] and f["corte_nuevo"]]
    print("\n--- LA ESCALA DEL PUNTAJE, que es lo que de verdad se mueve ---")
    for etiqueta, datos in (("VIEJA (media de las 3 mejores)", bv),
                            ("NUEVA (media de las 2 mejores)", bn)):
        q = statistics.quantiles(datos, n=100)
        print("  %-32s n=%4d  p50 %.1f  p90 %.1f  p99 %.1f  max %.1f"
              % (etiqueta, len(datos), q[49], q[89], q[98], max(datos)))

    print("\n--- LOS NODOS QUE MANDA MIRAR LA DECISION, uno por uno ---")
    print("  %-46s %5s %7s %14s %14s" % ("nodo", "pasos", "pareja", "bloque VIEJO", "bloque NUEVO"))
    for grupo, titulo in ((CALIBRACION, "LA CALIBRACION CONOCIDA"),
                          (APOYO_ACTA32, "EL APOYO DEL MOVIMIENTO 2 DEL ACTA 32"),
                          (EL_FALSO_NEGATIVO, "EL FALSO NEGATIVO QUE BAJO EL UMBRAL A 44"),
                          (SEIS_OPD03, "LOS SEIS NODOS DE OP-D-03")):
        print("  --- %s" % titulo)
        for nid in grupo:
            f = next((x for x in filas if x["id"] == nid), None)
            if f is None:
                print("  %-46s AUSENTE o con menos de dos pasos" % nid)
                continue
            vt = ("%.1f (corte %d)" % (f["viejo"], f["corte_viejo"])) if f["aplica_viejo"] else "NO APLICA"
            nt = ("%.1f (corte %d)" % (f["nuevo"], f["corte_nuevo"])) if f["aplica_nuevo"] else "NO APLICA"
            print("  %-46s %5d %7.1f %14s %14s" % (nid, f["pasos"], f["pareja"], vt, nt))

    print("\n--- LA PUERTA DE CALIBRACION, con la regla nueva ---")
    for nid in CALIBRACION:
        f = next(x for x in filas if x["id"] == nid)
        entra = (f["pareja"] >= UMBRAL_PAREJA
                 or (f["aplica_nuevo"] and f["nuevo"] >= UMBRAL_BLOQUE))
        print("  %-46s %s" % (nid, "ENTRA EN LA COLA" if entra else "NO ENTRA: la puerta seguiria roja"))

    print("\n--- LOS VEINTE PRIMEROS DE LA COLA NUEVA, por la senal mas fuerte ---")
    cn.sort(key=lambda f: max(f["pareja"] / 100, f["nuevo"] / 100), reverse=True)
    for i, f in enumerate(cn[:20], 1):
        print("  %2d %-46s pasos %2d pareja %5.1f bloque %5.1f corte %d"
              % (i, f["id"], f["pasos"], f["pareja"], f["nuevo"], f["corte_nuevo"]))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
