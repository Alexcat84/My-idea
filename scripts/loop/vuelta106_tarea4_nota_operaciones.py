# -*- coding: utf-8 -*-
r"""vuelta106_tarea4_nota_operaciones.py . VUELTA 106, TAREA 4: anade, al
final del campo `nota` de OP-E-03 en docs/plan/OPERACIONES.jsonl, el
registro de la pregunta de tres vias sobre los tramos 3 y 4. Solo esa linea
del jsonl se re-serializa; las demas quedan byte a byte identicas. Aditivo:
el texto viejo no se toca ni una letra.

USO:
  python scripts/loop/vuelta106_tarea4_nota_operaciones.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

ANADIDO = (
    " CORRECCION DECLARADA (vuelta 106, TAREA 4.1 a 4.4, pregunta de tres vias sobre los "
    "tramos 3 y 4, acta de la vuelta 105, TAREA 4). Censo propio del lote (SALIDA_V106_TAREA4_1_"
    "CENSO.txt): 28 RESUELTA en tramo3+tramo4 (19 tramo3, 9 tramo4), 27 sin correccion ni "
    "relectura (no 26: el 147 no pertenece al conjunto RESUELTA, su direccion ya esta anulada "
    "por correccion_v99; el 110, sin correccion ni relectura, si pertenece y no estaba en el "
    "lote del encargo; discrepancia declarada, no resuelta copiando). Guarda del paso mal "
    "casado sobre los cuatro tramos (SALIDA_V106_TAREA4_2_GUARDA_PASO_MAL_CASADO.txt): 2 "
    "puestos (46 tramo2, 147 tramo3), sin cifra viva que toquen. Pregunta de tres vias sobre "
    "los 27 (SALIDA_V106_TAREA4_3_TRES_VIAS.txt): 24 OBJETO, 3 SATELITE (123, 145, 154), 0 "
    "NO_OBJETO. Lectura entera a ciegas de los 3 SATELITE (SALIDA_V106_TAREA4_4_LECTURA_ENTERA."
    "md): 1 sostiene limpio (123, entregables confirman la direccion), 1 se mueve DISCUTIBLE "
    "(145, el paso propio del hijo tensiona con la tesis de la madre) y 1 sostiene DISCUTIBLE "
    "(154, entregable agregado de la madre distinto del entregable del paso casado). "
    "`correccion_v106` en el puesto 145 (direccion_leida a null; clase D sin cambio). Recontado "
    "con scripts/loop/contar_cierre_efectivo.py (SALIDA_V106_TAREA4_CIERRE_EFECTIVO.txt): "
    "clase A 3, B 2, C 1 (par 111), D 177; direccion leida y afirmada 73, NO RESUELTA 110 "
    "(60,1%); invertidas 2 (pares 16, 114). LA CIFRA VIGENTE ES 73 / 110 (60,1%). CIERRE DE LA "
    "BOLSA: NO SON TODAS. Contadas hoy las RESUELTA de los cuatro tramos que ya pasaron por la "
    "pregunta de tres vias, faltan 2, los dos en tramo1: puesto 3 (medicion_servicios -> "
    "programa_make_certain_3) y puesto 16 (proceso_llamada_inicial_venta -> "
    "proceso_venta_franquicias), ninguno cubierto por los barridos de las vueltas 104 o 105. "
    "REGISTRO Y JUICIO, NO CIRUGIA: estado no se toca, no se escribe ni retira ninguna arista."
)


def main():
    with io.open(RUTA, encoding="utf-8") as f:
        lineas = f.readlines()

    tocado = False
    nuevas = []
    for linea in lineas:
        if not linea.strip():
            nuevas.append(linea)
            continue
        fila = json.loads(linea)
        if fila.get("id_op") == "OP-E-03":
            if "TAREA 4.1 a 4.4, pregunta de tres vias sobre los tramos 3 y 4" in fila.get("nota", ""):
                raise SystemExit("ROJO: la nota de OP-E-03 ya trae el registro de esta vuelta")
            fila["nota"] = fila.get("nota", "") + ANADIDO
            nuevas.append(json.dumps(fila, ensure_ascii=False) + "\n")
            tocado = True
        else:
            nuevas.append(linea)

    if not tocado:
        raise SystemExit("ROJO: no se encontro OP-E-03 en %s" % RUTA)

    with io.open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.writelines(nuevas)
    print("OK: nota de OP-E-03 anadida en %s" % os.path.relpath(RUTA, RAIZ))


if __name__ == "__main__":
    main()
