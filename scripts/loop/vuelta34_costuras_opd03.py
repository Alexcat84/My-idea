# -*- coding: utf-8 -*-
"""vuelta34_costuras_opd03.py - LAS TRES COSTURAS DE OP-D-03, MEDIDAS HOY.

ESTRICTAMENTE DE SOLO LECTURA.

DOS COSAS QUE ESTE INSTRUMENTO SEPARA A PROPOSITO, porque confundirlas fue la
parada de la vuelta 33:

  (a) DE DONDE SALE LA NOMINA DE LAS TRES. No sale del instrumento de costuras:
      esta ESCRITA POR SU NOMBRE en el plan sellado, docs/plan/02_DESTEJIDOS.md,
      seccion OP-D-03: "Acto 2. SEIS nodos y TRES destejidos. Costuras:
      ab_testing_optimizacion, optimizacion_embudo_get_customers,
      split_testing_experimentos_ab". Este script COMPRUEBA que esa linea sigue
      ahi, en vez de fiarse de que alguien la leyo.

  (b) QUE MIDE LA SENAL RECALIBRADA sobre los seis, que es CONTRASTE y no
      nomina. La senal se reimplementa aqui, copiada literal de
      scripts/costuras_internas.py, porque el instrumento sellado se niega a
      entregar y a ser importado mientras su puerta este roja. Va dicho en cada
      linea de salida: esto NO es el veredicto del instrumento sellado.

Y LO TERCERO, que es lo que decide el trabajo: EL ESTADO DE CADA COSTURA HOY,
medido contra la frontera escrita en docs/plan/01_FUENTES.md y contra el texto
del nodo, para saber cual sigue en pie y cual ya se la llevo la fase 01.

Uso: python scripts/loop/vuelta34_costuras_opd03.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
DESTEJIDOS = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")
FUENTES = os.path.join(RAIZ, "docs", "plan", "01_FUENTES.md")

UMBRAL_PAREJA = 80.0
UMBRAL_BLOQUE = 44.0
MIN_BLOQUE = 2

ACTO = ["ab_testing_optimizacion", "funnel_get_customers_optimizacion",
        "optimizacion_embudo_get_customers", "split_testing",
        "split_testing_experimentos_ab", "test_ab_precio"]

COSTURAS = ["ab_testing_optimizacion", "optimizacion_embudo_get_customers",
            "split_testing_experimentos_ab"]

# La frontera escrita de cada costura, con el numero de pasos que el plan le
# contaba el dia que la escribio y la operacion de la fase 01 que se llevo el
# bloque. Nada de esto se supone: se comprueba contra el nodo de hoy.
FRONTERAS = {
    "ab_testing_optimizacion": {
        "pasos_cuando_se_escribio": 15,
        "frontera": "1 a 10 / 11 a 15",
        "se_lo_llevo": "OP-F-04-WEI (bloque 11 a 15, a anillo_interior_explotar_el_canal_nucleo)",
        "huella_del_bloque_ido": "punto de saturación",
        "queda_costura": "SI, y su frontera esta escrita: los pasos 1 a 5 y 6 a 10 dicen la misma prueba A/B dos veces",
    },
    "optimizacion_embudo_get_customers": {
        "pasos_cuando_se_escribio": 10,
        "frontera": "1 a 5 / 6 a 10",
        "se_lo_llevo": "OP-F-04-WEI (bloque 6 a 10, a anillo_interior_explotar_el_canal_nucleo)",
        "huella_del_bloque_ido": "middle ring testing",
        "queda_costura": "NO: el bloque que la formaba ya salio",
    },
    "split_testing_experimentos_ab": {
        "pasos_cuando_se_escribio": 9,
        "frontera": "1 a 5 / 6 a 9",
        "se_lo_llevo": "OP-F-04-RAC (bloque 6 a 9, a metodologia_evaluacion_entrenamiento_ventas)",
        "huella_del_bloque_ido": "cambio porcentual",
        "queda_costura": "NO: el bloque que la formaba ya salio",
    },
}

# El campo `preservar` de OP-D-03, comprobado donde vive HOY.
PRESERVAR = [
    {"que": "la significancia estadistica del 95 por ciento, del nodo chico de split_testing",
     "huella": "significancia estadística superior al 95", "esperado_en": "split_testing"},
    {"que": "el cambio porcentual, que se fue con el bloque de Rackham",
     "huella": "cambio porcentual", "esperado_en": "metodologia_evaluacion_entrenamiento_ventas"},
    {"que": "el grupo de control con desempeno inicial similar, idem",
     "huella": "nivel de desempeño inicial similar",
     "esperado_en": "metodologia_evaluacion_entrenamiento_ventas"},
]


def peor_pareja(ratio, pasos):
    mejor = (0.0, 0, 0)
    for a in range(len(pasos)):
        for b in range(a + 1, len(pasos)):
            s = ratio(pasos[a], pasos[b])
            if s > mejor[0]:
                mejor = (s, a + 1, b + 1)
    return mejor


def bloques(ratio, pasos, minimo=MIN_BLOQUE):
    """Todos los cortes con su puntaje. NO APLICA si la lista no llega al minimo."""
    if len(pasos) < minimo * 2:
        return None
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
            fuera.append((corte, sum(sorted(puntajes, reverse=True)[:minimo]) / minimo))
        else:
            fuera.append((corte, None))
    return fuera


def cargar_todo():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
            fuera[d["node_id"]] = d
    return fuera


def main():
    from rapidfuzz.fuzz import token_sort_ratio as ratio
    G = cargar_todo()

    print("(a) LA NOMINA DE LAS TRES, COMPROBADA EN EL PLAN SELLADO")
    print("=" * 78)
    texto = io.open(DESTEJIDOS, encoding="utf-8").read()
    linea = "**Acto 2. SEIS nodos y TRES destejidos.** Costuras:"
    if linea not in texto:
        print("  ABORTA: la linea que nombra las tres costuras NO esta en 02_DESTEJIDOS.md")
        return 1
    trozo = texto[texto.index(linea):texto.index(linea) + 260].split("\n\n")[0]
    print("  CITADA LITERAL del plan:")
    for l in trozo.splitlines():
        print("    %s" % l)
    fallan = [c for c in COSTURAS if c not in trozo]
    if fallan:
        print("  ABORTA: %s no aparece en la linea" % fallan)
        return 1
    print("  LAS TRES ESTAN ESCRITAS POR SU NOMBRE. La nomina NO sale del instrumento.")

    print()
    print("(b) EL ESTADO DE CADA COSTURA HOY, contra su frontera escrita en 01_FUENTES.md")
    print("=" * 78)
    fuentes = io.open(FUENTES, encoding="utf-8").read()
    for nid in COSTURAS:
        f = FRONTERAS[nid]
        d = G[nid]
        pasos = d.get("pasos_accionables") or []
        ido = not any(f["huella_del_bloque_ido"] in p for p in pasos)
        print("\n  %s" % nid)
        print("    frontera escrita        : %s   (sobre %d pasos)"
              % (f["frontera"], f["pasos_cuando_se_escribio"]))
        print("    frontera hallada en 01_FUENTES.md: %s"
              % ("SI" if ("`%s`" % nid) in fuentes else "NO"))
        print("    pasos HOY               : %d" % len(pasos))
        print("    huella del bloque ido   : %r -> %s"
              % (f["huella_del_bloque_ido"], "YA NO ESTA" if ido else "SIGUE DENTRO"))
        print("    se lo llevo             : %s" % f["se_lo_llevo"])
        print("    QUEDA COSTURA           : %s" % f["queda_costura"])

    print()
    print("(c) EL CAMPO preservar DE OP-D-03, comprobado donde vive HOY")
    print("=" * 78)
    for p in PRESERVAR:
        d = G.get(p["esperado_en"])
        vive = d is not None and any(p["huella"] in x for x in (d.get("pasos_accionables") or []))
        donde = sorted(k for k, dd in G.items()
                       if not dd.get("deprecado")
                       and any(p["huella"] in x for x in (dd.get("pasos_accionables") or [])))
        print("  [%s] %s" % ("OK  " if vive else "CAE ", p["que"]))
        print("        huella %r, esperada en %s" % (p["huella"], p["esperado_en"]))
        print("        vive hoy en los nodos vivos: %s" % donde)

    print()
    print("(d) LA SENAL RECALIBRADA SOBRE LOS SEIS. ES CONTRASTE, NO NOMINA")
    print("    (senales reimplementadas: el instrumento sellado no entrega con la puerta rota)")
    print("=" * 78)
    print("    %-38s %5s %7s %8s %6s %9s" % ("nodo", "pasos", "pareja", "bloque", "corte", "dispara"))
    for nid in ACTO:
        pasos = G[nid].get("pasos_accionables") or []
        sp = peor_pareja(ratio, pasos)
        bs = bloques(ratio, pasos)
        if bs is None:
            print("    %-38s %5d %7.1f %8s %6s %9s"
                  % (nid, len(pasos), sp[0], "NO APLICA", "", "no"))
            continue
        mejor = (0.0, 0)
        for corte, score in bs:
            if score is not None and score > mejor[0]:
                mejor = (score, corte)
        dispara = (sp[0] >= UMBRAL_PAREJA) or (mejor[0] >= UMBRAL_BLOQUE)
        print("    %-38s %5d %7.1f %8.1f %6d %9s"
              % (nid, len(pasos), sp[0], mejor[0], mejor[1], "SI" if dispara else "no"))

    print()
    print("    CORTE POR CORTE del nodo que se desteje, para poder comparar el corte")
    print("    que propone la senal con el que dice la frontera escrita (tras el 5):")
    pasos = G["ab_testing_optimizacion"].get("pasos_accionables") or []
    for corte, score in bloques(ratio, pasos):
        marca = "   <-- el corte de la FRONTERA ESCRITA" if corte == 5 else ""
        print("      corte tras %2d: %s%s"
              % (corte, ("%.1f" % score) if score is not None else "SIN PUNTAJE", marca))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
