# -*- coding: utf-8 -*-
"""vuelta40_calibrar_costuras.py - LA MEDICION que elige el fixture nuevo de la
puerta de calibracion de scripts/costuras_internas.py, ANTES de tocar nada.

ESTRICTAMENTE DE SOLO LECTURA. No toca el instrumento, no toca un nodo, no
escribe ninguna cola. Solo mide e imprime.

SUCEDE A `vuelta34_calibrar_costuras.py`, que midio el costo de mover
`MIN_BLOQUE`. Este NO mueve ningun dial: los umbrales quedan donde estan
(pareja 80, bloque 44) y lo unico que se elige es CONTRA QUE NODOS se comprueba
que el instrumento sigue cazando lo que se construyo para cazar.

POR QUE MIDE CON LAS SENALES PRIVADAS (`_peor_pareja`, `_mejor_bloque`). Las
publicas llevan la puerta delante, y la puerta es justo lo que esta caido: usar
las publicas aqui seria pedirle al instrumento que se autorice a si mismo antes
de saber con que. Es el mismo camino que su propia `medir_calibracion` toma, y
por eso las privadas existen.

Uso: python scripts/loop/vuelta40_calibrar_costuras.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))

from costuras_internas import (  # noqa: E402
    UMBRAL_PAREJA, UMBRAL_BLOQUE, MIN_PASOS_BLOQUE, CALIBRACION,
    NoAplica, _peor_pareja, _mejor_bloque,
)

GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

# Los que el reporte de la vuelta 39 y el acta de la vuelta 39 nombran, para que
# la medicion de hoy se pueda contrastar con lo que cada uno publico. NO se
# citan como fuente de cifra: se re-miden aqui (regla 2 del EJECUTOR).
NOMBRADOS = ("reglas_brainstorming", "pensamiento_convergente_divergente",
             "errores_comunes_asignacion_roles", "seleccion_ceo_fundador",
             "asignacion_de_titulos_ejecutivos", "propuesta_gasto_capital")


def ficha(ratio, nid, nodos):
    n = nodos.get(nid) or {}
    pasos = n.get("pasos_accionables") or []
    sp = _peor_pareja(ratio, pasos)
    sb = _mejor_bloque(ratio, pasos)
    aplica = not isinstance(sb[0], NoAplica)
    disp_p = sp[0] >= UMBRAL_PAREJA
    disp_b = bool(aplica and sb[1] and sb[0] >= UMBRAL_BLOQUE)
    return {
        "id": nid, "vive": bool(n) and not n.get("deprecado"),
        "existe": bool(n), "dominio": n.get("dominio"),
        "pasos": len(pasos), "pareja": sp[0], "par_ij": (sp[1], sp[2]),
        "bloque": (sb[0] if aplica else None), "corte": sb[1],
        "aplica_bloque": aplica,
        "disparo_pareja": disp_p, "disparo_bloque": disp_b,
        "entra": disp_p or disp_b,
        "margen": (sb[0] - UMBRAL_BLOQUE) if aplica else None,
    }


def linea(f):
    b = ("NO APLICA" if not f["aplica_bloque"]
         else "%5.1f (corte tras %d, margen %+.1f)" % (f["bloque"], f["corte"], f["margen"]))
    por = " y ".join([p for p, v in (("pareja", f["disparo_pareja"]),
                                     ("bloque", f["disparo_bloque"])) if v]) or "NINGUNA"
    return ("  %-45s %-16s %d pasos | pareja %5.1f (%d y %d) | bloque %-34s | entra por %s"
            % (f["id"], (f["dominio"] or "?"), f["pasos"], f["pareja"],
               f["par_ij"][0], f["par_ij"][1], b, por))


def main():
    from rapidfuzz.fuzz import token_sort_ratio as ratio

    nodos = json.loads(io.open(GRAFO, encoding="utf-8").read())["nodos"]
    activos = {k: v for k, v in nodos.items() if not v.get("deprecado")}

    print("MEDICION DE LA PUERTA DE CALIBRACION, vuelta 40, 19 ago 2026")
    print("Umbrales VIGENTES y NO tocados: pareja %s, bloque %s. MIN_PASOS_BLOQUE %d."
          % (UMBRAL_PAREJA, UMBRAL_BLOQUE, MIN_PASOS_BLOQUE))
    print("Grafo: %d nodos, %d activos." % (len(nodos), len(activos)))
    print("")

    print("1. LA CALIBRACION VIEJA, medida hoy contra el grafo de hoy")
    viejos = [ficha(ratio, nid, nodos) for nid in CALIBRACION]
    for f in viejos:
        print(linea(f))
    faltan = [f["id"] for f in viejos if not f["entra"]]
    print("  NO ENTRAN EN LA COLA HOY: %s" % (faltan or "ninguno"))
    print("")

    print("2. LOS NOMBRADOS por el reporte y el acta de la vuelta 39, RE-MEDIDOS")
    for nid in NOMBRADOS:
        print(linea(ficha(ratio, nid, nodos)))
    print("")

    print("3. EL BARRIDO ENTERO del catalogo activo, para elegir con la vara delante")
    filas = []
    for nid, n in sorted(activos.items()):
        pasos = n.get("pasos_accionables") or []
        if len(pasos) < 2:
            continue
        filas.append(ficha(ratio, nid, nodos))
    cola = [f for f in filas if f["entra"]]
    por_bloque = sorted([f for f in cola if f["disparo_bloque"]],
                        key=lambda f: -f["bloque"])
    print("  evaluados: %d | en la cola: %d | por bloque: %d | por pareja: %d"
          % (len(filas), len(cola), len(por_bloque),
             len([f for f in cola if f["disparo_pareja"]])))
    print("")
    print("  LOS VEINTE DE BLOQUE MAS ALTO (candidatos a fixture):")
    for f in por_bloque[:20]:
        print(linea(f))
    print("")
    print("  LOS QUE ROZAN EL UMBRAL (margen menor que 1,0), o sea los FRAGILES:")
    for f in por_bloque:
        if f["margen"] < 1.0:
            print(linea(f))
    print("")
    print("4. CUANTOS NUCLEO entre los veinte de bloque mas alto: %d"
          % len([f for f in por_bloque[:20] if f["dominio"] == "core"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
