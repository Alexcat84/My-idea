# -*- coding: utf-8 -*-
"""vuelta40_registro_opd05.py - ESCRIBE EN docs/plan/02_DESTEJIDOS.md el registro
de OP-D-05, GENERADO desde el plan sellado y no tecleado (EJECUTOR.md regla 1).

Dos secciones, y se piden por separado porque se escriben en momentos distintos:

  --sellado   el estado ANTES de ejecutar: el destejido declarado sin costura, la
              eleccion de P.8 con su lectura, y LA TABLA DE MAPA DE MOVIMIENTO,
              que es la que scripts/loop/verificar_mapas_destejido.py valida celda
              a celda contra el plan JSON.
  --cierre    el estado DESPUES de ejecutar, con el censo y la verificacion punto
              por punto. Sus cifras se le pasan por la linea de ordenes desde las
              salidas selladas, para que nada se teclee de memoria.

Uso:
  python scripts/loop/vuelta40_registro_opd05.py --sellado
  python scripts/loop/vuelta40_registro_opd05.py --cierre
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MD = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")
PLAN = os.path.join(RAIZ, "docs", "loop", "PLAN_V40_OPD05.json")
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def leer_plan():
    return json.loads(io.open(PLAN, encoding="utf-8").read())


def sellado(p):
    L = []
    A = L.append
    A("")
    A("## `OP-D-05` SELLADA: **LA FUSION UNICA DE LA SELECCION DEL CEO** "
      "(19 ago 2026, vuelta 40)")
    A("")
    A("**ESTA SECCION SE ESCRIBE ANTES DE EJECUTAR Y NO SE REESCRIBE DESPUES.** "
      "Lo que pase al ejecutar va en su propia seccion de cierre, debajo, para que "
      "el plan y su resultado se puedan comparar sin que uno tape al otro.")
    A("")
    A("### EL DESTEJIDO: **NO HAY COSTURA QUE DESTEJER**, y va medido")
    A("")
    A("La tabla de orden de este mismo fichero le cuenta a `OP-D-05` **UN "
      "destejido** y le pone de ancla `seleccion_ceo_fundador`. **Ese destejido "
      "tenia sujeto escrito**, aunque no en la seccion de la operacion sino en las "
      "razones de sus propios pares: la del puesto **673** dice que "
      "`seleccion_ceo_fundador` es **costura CONFIRMADA** en "
      "`docs/FICHA_SUBFUSION_GRADIENTE.md`, **doce pasos** y corte **1 a 4 contra "
      "5 a 12**, y la del **492** describe el mismo corte.")
    A("")
    A("**MEDIDO CONTRA EL NODO DE HOY** (`scripts/loop/vuelta40_destejido_opd05.py`, "
      "salida en `docs/loop/SALIDA_V40_OPD05_DESTEJIDO.txt`): el nodo tiene **cuatro "
      "pasos** y **una sola fuente**, y de las **seis huellas** del bloque 5 a 12 "
      "(mentor, brecha, CEO profesional, control, autoevaluacion, clausula) "
      "**sobreviven CERO**. **Ya se lo llevo `OP-F-04-HOR`**, commit **`2bd8dd76`**, "
      "medido con `git log --follow` y no supuesto. **Es el mismo caso que "
      "`OP-D-03`**, cuya celda de esa tabla dice que **dos de sus tres costuras "
      "estaban CONSUMIDAS por la fase 01**.")
    A("")
    A("**Y EL INSTRUMENTO DE LA CASA, YA VIVO, DICE LO SUYO.** "
      "`scripts/costuras_internas.py` se reparo en esta misma vuelta y entrega con "
      "`exit 0`. De los tres nodos **cita UNO**, "
      "`errores_comunes_asignacion_roles` (bloque **45,5**, corte tras el paso 2), "
      "y **no cita** a los otros dos. **La cita se leyo con el texto delante**: los "
      "cinco pasos de ese nodo son **cinco errores distintos**, y por **`P.11`** "
      "son **advertencias y no procedimientos** (quitadas las frases que empiezan "
      "por NO, por EVITA o por DE VERDAD, lo que queda es una lista de punteros). "
      "**Comparten tema, no narracion**, que es lo que la senal de bloque no puede "
      "distinguir y su propio encabezado declara. **El instrumento CITA y NO JUZGA: "
      "aqui cito, se leyo, y la lectura dice que no hay costura.**")
    A("")
    A("### `P.5` CON EL TEXTO YA ESTABLE: **UNA familia, no dos**")
    A("")
    A("`scripts/loop/vuelta39_acto.py --op OP-D-05`, salida en "
      "`docs/loop/SALIDA_V40_OPD05_ACTO.txt`, corrida hoy:")
    A("")
    A("| | medido el 19 ago 2026 |")
    A("|---|---|")
    A("| pares | **3 de 3 con clase, los tres `A` y los tres del ARCHIVO** "
      "(puestos **492**, **673** y **833**), cero lecturas dirigidas |")
    A("| nodos puente (`P.10`) | **CERO** |")
    A("| subconjuntos cerrados | **1, y es el acto entero**: la respuesta a `P.5` "
      "es **UNA familia** |")
    A("| aristas cojas | **CERO en los tres**: elegir superviviente **no cuesta ni "
      "una arista** |")
    A("| fuente | **los tres de *The Founder's Dilemmas***: **NO es acto de fuente "
      "mixta**, al contrario que los dos de `OP-D-04` |")
    A("| `9.3.1` sobre los pares `A` | de 3, **UNO** nombra ganador (el 673). **No "
      "hay GANADOR POR DERECHO**: la especie es **POR ELEGIR** |")
    A("")
    A("**Los tres pares ya tenian clase del archivo y el destejido no los dejo "
      "rancios** (no hubo destejido), asi que **`P.5` se contesta sobre texto ya "
      "estable sin releer ni un par**, que es exactamente la condicion que la nota "
      "de la operacion pone.")
    A("")
    A("### `P.8`: **DECIDE EL CONTENIDO**, y el cableado solo acompaña")
    A("")
    e = p["eleccion_p8"]
    A("**SUPERVIVIENTE: `%s`.**" % e["elegido"])
    A("")
    for linea in e["lectura_de_contenido"]:
        A("- %s" % linea)
    A("")
    c = e["cableado_solo_como_desempate"]
    A("**EL CABLEADO, citado y NO usado para decidir:** `%s` **%d**, `%s` **%d**, "
      "`%s` **%d**. %s"
      % (e["elegido"], c["grados_medidos_hoy"][e["elegido"]],
         p["absorbidos"][0], c["grados_medidos_hoy"][p["absorbidos"][0]],
         p["absorbidos"][1], c["grados_medidos_hoy"][p["absorbidos"][1]],
         c["lectura"]))
    A("")
    A("> **Y EL COSTE DE LA ELECCION ESTA MEDIDO: %s** %s"
      % (c["coste_medido_de_la_eleccion"].split(".")[0] + ".",
         ".".join(c["coste_medido_de_la_eleccion"].split(".")[1:]).strip()))
    A("")
    A("### EL MAPA DE MOVIMIENTO, celda a celda")
    A("")
    A("**Prefijos:** `S` = `%s` (superviviente), `T` = `%s`, `E` = `%s`."
      % (p["superviviente"], p["absorbidos"][0], p["absorbidos"][1]))
    A("")
    A("| paso del resultado | de que origenes sale | motivo |")
    A("|---:|---|---|")
    for i, g in enumerate(p["grupos_pasos"], 1):
        A("| %d | %s | %s |" % (i, ", ".join(g["origenes"]), g["motivo"]))
    A("")
    A("| condicion del resultado | de que origenes sale | motivo |")
    A("|---:|---|---|")
    for i, g in enumerate(p["grupos_condiciones"], 1):
        A("| %d | %s | %s |" % (i, ", ".join(g["origenes"]), g["motivo"]))
    A("")
    viajan = [f for f in p["tabla_perdidas_p13"] if f["clase"] == "VIAJA"]
    A("**LA TABLA DE PERDIDAS DE `P.13`, derivada de los grupos: %d de %d piezas "
      "VIAJAN y CERO se pierden.** La regla de reparto adjudicada el 11 ago 2026 "
      "manda cada perdida al bloque del que proviene y la que no tenga bloque al "
      "superviviente; **con cero perdidas no hay nada que repartir, y eso se "
      "comprueba al cierre en vez de suponerse.**"
      % (len(viajan), len(p["tabla_perdidas_p13"])))
    A("")
    A("### LO QUE LA SIMULACION DICE QUE VA A PASAR, sellado antes de ejecutar")
    A("")
    s = p["simulacion"]
    A("| | esperado |")
    A("|---|---|")
    A("| redirecciones sobre nodos vivos | **%d** |" % len(s["redirecciones_esperadas"]))
    A("| deprecados que nombran y NO se tocan | **%d** |"
      % len(s["redirecciones_no_tocadas_por_deprecadas"]))
    A("| duplicadas que la fusion fabrica (`P.16`) | **%d**, y las limpia la misma "
      "operacion |" % len(s["duplicadas_nuevas_esperadas"]))
    A("| aristas de simetrizacion que el paso 5 tiene que anadir | **%d**, ni una "
      "mas ni una menos |" % len(s["simetrizacion_esperada"]["aristas"]))
    A("| pasos del resultado | **%d**, **DENTRO del estandar de 3 a 6**: esta "
      "operacion **no necesita la excepcion de clase** que `OP-D-04` si necesito |"
      % len(p["pasos_finales"]))
    A("")
    r = s["registros_que_no_son_el_grafo"]
    A("**LOS REGISTROS QUE NO SON EL GRAFO, ENUMERADOS ANTES Y NO DESPUES.** %s "
      "El barrido (`%s`) da **CERO registros vivos** que nombren a alguno de los "
      "tres, y la comprobacion dirigida sobre **los nueve "
      "`bridges_aprobados.json`** da **cero apariciones en los nueve**. **Aun asi "
      "se corre `reanclar_por_resolutor.py` entre la fusion y `run_phase1`**: es la "
      "practica que el acta de la vuelta 39 adjudico para toda fusion futura, y "
      "**una guarda que solo se corre cuando se sospecha no es una guarda.**"
      % (r["por_que_va_en_el_plan"][0].upper() + r["por_que_va_en_el_plan"][1:],
         r["instrumento"].split(",")[0]))
    A("")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sellado", action="store_true")
    a = ap.parse_args()
    p = leer_plan()
    if a.sellado:
        texto = sellado(p)
    else:
        sys.exit("hace falta --sellado")
    with io.open(MD, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)
    print("escrito en %s: %d lineas"
          % (os.path.relpath(MD, RAIZ).replace("\\", "/"), texto.count("\n")))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
