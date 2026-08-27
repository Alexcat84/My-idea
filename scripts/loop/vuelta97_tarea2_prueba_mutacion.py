# -*- coding: utf-8 -*-
r"""vuelta97_tarea2_prueba_mutacion.py . VUELTA 97, TAREA 2: LA PRUEBA POR
MUTACION de las guardas de los dos instrumentos de esta tarea.

POR QUE EXISTE (EJECUTOR.md regla 1, "EL CASO ROJO SE PRUEBA POR MUTACION",
escrita el 29 ago 2026 por la caida 2 de la vuelta 89, donde un caso rojo
comparaba una constante literal consigo misma y no podia fallar nunca):
NINGUNA guarda de esta vuelta se publica como prueba sin haber corrido antes su
prueba de mutacion. Se cambia el valor esperado y se comprueba que el caso CAE.

LO QUE SE PRUEBA, Y LO QUE SE DECLARA SIN PROBAR. Se prueban SEIS mecanicas, y
las seis tienen que CAER al mutarlas. Y se DECLARA, en vez de fabricarle un rojo
que se apruebe solo: LA CLASE (A, B, C, D) Y LA DIRECCION DE CADA UNO DE LOS 60
PARES SON UNA TABLA A MANO, escritas por la lectura del ejecutor sobre el
material impreso, y NO TIENEN CASO ROJO AUTOMATICO. No hay nada que mutar ahi:
no existe una segunda fuente contra la que contrastarlas dentro del repo. Lo que
si tiene mecanica, y es lo que se prueba, es el ARMAZON que las sostiene y las
DOS AFIRMACIONES medidas sobre la senial de la bolsa.

  MUTACION 1 (armazon, clase fuera del alfabeto): una clase pasa a "X".
  MUTACION 2 (armazon, par repetido): un puesto aparece dos veces.
  MUTACION 3 (armazon, direccion que no nombra los nodos de su fila): la
      direccion de un par se cambia por dos ids de OTRA fila.
  MUTACION 4 (armazon, tabla incompleta): se quita un veredicto de los 60.
  MUTACION 5 (afirmacion 2 de la senial): normaliza_fuente se muta a constante,
      con lo que TODAS las filas pasan a ser de la misma fuente y el
      "estrictamente menor" entre los dos grupos deja de cumplirse.
  MUTACION 6 (afirmacion 1 de la senial): se sube el titulo_ratio del tramo 2 por
      encima del del tramo 1, y la mediana deja de ser menor.

CONTROL VERDE ANTES Y DESPUES de las mutaciones, para que se vea que lo que cae
es la mutacion y no el instrumento.

USO:
  python scripts/loop/vuelta97_tarea2_prueba_mutacion.py
"""
import copy
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

from vuelta96_tarea3_veredictos_tramo1 import construir_filas  # noqa: E402
import vuelta97_tarea2_veredictos_tramo2 as V97  # noqa: E402
import vuelta97_tarea2_senal_de_la_bolsa as SEN  # noqa: E402

BOLSA = os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")
LECTURA = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

resultados = []


def anota(nombre, esperado_cae, cayo, detalle):
    ok = (cayo == esperado_cae)
    resultados.append((esperado_cae, ok))
    print("  %-58s %s   %s"
          % (nombre, "CAE" if cayo else "no cae", "OK" if ok else "*** LA PRUEBA FALLA ***"))
    if detalle:
        print("      %s" % detalle)


def corre_armazon(tabla):
    filas, fallos, _ = construir_filas(tabla, V97.DESDE, V97.CUANTOS)
    return fallos


def main():
    print("=" * 100)
    print("PRUEBA POR MUTACION, VUELTA 97 TAREA 2")
    print("=" * 100)
    print()

    print("CONTROL VERDE ANTES (la tabla real, sin tocar):")
    fallos = corre_armazon(V97.VEREDICTOS)
    anota("armazon con la tabla real", False, bool(fallos), "fallos: %r" % (fallos or "ninguno"))
    print()

    print("MUTACIONES DEL ARMAZON (cada una sobre una COPIA de la tabla, nunca sobre la real):")

    # --- 1: clase fuera del alfabeto ---
    t = copy.deepcopy(V97.VEREDICTOS)
    n, _, d, r = t[0]
    t[0] = (n, "X", d, r)
    fallos = corre_armazon(t)
    anota("1. una clase pasa a 'X'", True, bool(fallos), (fallos or [""])[0])

    # --- 2: par repetido ---
    t = copy.deepcopy(V97.VEREDICTOS)
    n0, c0, d0, r0 = t[0]
    n1, c1, d1, r1 = t[1]
    t[1] = (n0, c1, None, r1)
    fallos = corre_armazon(t)
    anota("2. el puesto %d aparece dos veces" % n0, True, bool(fallos), (fallos or [""])[0])

    # --- 3: direccion que no nombra los nodos de su fila ---
    t = copy.deepcopy(V97.VEREDICTOS)
    n, c, _, r = t[4]          # el par 45, que SI tiene direccion
    t[4] = (n, c, "takt_time -> smed_setup_reduction", r)
    fallos = corre_armazon(t)
    anota("3. la direccion del par %d nombra otros dos nodos" % n, True, bool(fallos), (fallos or [""])[0])

    # --- 4: tabla incompleta ---
    t = copy.deepcopy(V97.VEREDICTOS)
    quitado = t.pop(30)
    fallos = corre_armazon(t)
    anota("4. se quita el veredicto del par %d" % quitado[0], True, bool(fallos), (fallos or [""])[0])
    print()

    print("MUTACIONES DE LAS DOS AFIRMACIONES DE LA SENIAL:")

    nodos = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    res = SEN.construir_resolutor(nodos)
    bolsa = [json.loads(l) for l in io.open(BOLSA, encoding="utf-8") if l.strip()]
    lectura = [json.loads(l) for l in io.open(LECTURA, encoding="utf-8") if l.strip()]
    por_puesto = {x["puesto_tramo"]: x for x in lectura}
    tramo1, tramo2 = bolsa[0:40], bolsa[40:100]
    leidas = [r for i, r in enumerate(tramo2, start=41) if por_puesto[i].get("direccion_leida")]
    no_res = [r for i, r in enumerate(tramo2, start=41) if not por_puesto[i].get("direccion_leida")]

    def af1(t1, t2):
        a = SEN.medir(t1, nodos, res, [], "t1")
        b = SEN.medir(t2, nodos, res, [], "t2")
        return b["mediana_ratio"] < a["mediana_ratio"], a["mediana_ratio"], b["mediana_ratio"]

    def af2():
        a = SEN.medir(leidas, nodos, res, [], "leidas")
        b = SEN.medir(no_res, nodos, res, [], "no_res")
        return b["pct_misma_fuente"] < a["pct_misma_fuente"], a["pct_misma_fuente"], b["pct_misma_fuente"]

    ok1, v1a, v1b = af1(tramo1, tramo2)
    anota("control verde: afirmacion 1 con los datos reales", False, not ok1,
          "mediana tramo 1 %.1f, tramo 2 %.1f" % (v1a, v1b))
    ok2, v2a, v2b = af2()
    anota("control verde: afirmacion 2 con los datos reales", False, not ok2,
          "misma fuente LEIDA %.1f%%, NO RESUELTA %.1f%%" % (v2a, v2b))

    # --- 5: normaliza_fuente a constante ---
    original = SEN.normaliza_fuente
    try:
        SEN.normaliza_fuente = lambda s: "IGUAL PARA TODOS"
        ok, a, b = af2()
        anota("5. normaliza_fuente mutada a constante", True, not ok,
              "misma fuente LEIDA %.1f%%, NO RESUELTA %.1f%%: ya no es estrictamente menor" % (a, b))
    finally:
        SEN.normaliza_fuente = original

    # --- 6: titulo_ratio del tramo 2 subido por encima del tramo 1 ---
    t2_mutado = copy.deepcopy(tramo2)
    for r in t2_mutado:
        r["titulo_ratio"] = 99.0
    ok, a, b = af1(tramo1, t2_mutado)
    anota("6. el titulo_ratio del tramo 2 se sube a 99,0", True, not ok,
          "mediana tramo 1 %.1f, tramo 2 mutado %.1f: ya no es menor" % (a, b))
    print()

    print("CONTROL VERDE DESPUES (la tabla real y los datos reales, otra vez):")
    fallos = corre_armazon(V97.VEREDICTOS)
    anota("armazon con la tabla real", False, bool(fallos), "fallos: %r" % (fallos or "ninguno"))
    ok1b, _, _ = af1(tramo1, tramo2)
    anota("afirmacion 1 con los datos reales", False, not ok1b, "")
    ok2b, _, _ = af2()
    anota("afirmacion 2 con los datos reales", False, not ok2b, "")
    print()

    print("=" * 100)
    print("LO QUE NO SE PRUEBA, Y SE DECLARA EN VEZ DE FABRICARLE UN ROJO QUE SE APRUEBE SOLO")
    print("=" * 100)
    print("LA CLASE Y LA DIRECCION DE CADA UNO DE LOS 60 PARES SON UNA TABLA A MANO.")
    print("NO TIENEN CASO ROJO AUTOMATICO: no hay dentro del repo una segunda fuente")
    print("independiente contra la que contrastarlas, asi que no hay nada que mutar.")
    print("Su control es la relectura ciega del auditor, no un assert.")
    print()

    # LAS TRES CIFRAS DEL PIE SE CUENTAN DE resultados, NO SE TECLEAN
    # (EJECUTOR.md regla 1, "LA TABLA SE IMPRIME, NO SE TECLEA").
    total = len(resultados)
    buenas = sum(1 for _, ok in resultados if ok)
    mutaciones = sum(1 for esperado_cae, _ in resultados if esperado_cae)
    controles = total - mutaciones
    print("=" * 100)
    print("RESULTADO: %d de %d comprobaciones se comportan como deben." % (buenas, total))
    print("Mutaciones que TENIAN que caer: %d. Controles verdes: %d." % (mutaciones, controles))
    print("=" * 100)
    return 0 if buenas == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
