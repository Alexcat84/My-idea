# -*- coding: utf-8 -*-
"""vuelta107_tarea5_registro_operaciones_nota.py . Anade el registro de la
TAREA 5 (cierre de la bolsa) de la vuelta 107 al campo `nota` de OP-E-03 en
docs/plan/OPERACIONES.jsonl, sin borrar una letra de lo que ya hay.

USO:
  python scripts/loop/vuelta107_tarea5_registro_operaciones_nota.py
"""
import json

RUTA = "docs/plan/OPERACIONES.jsonl"

AGREGADO = (
    " REGISTRO (vuelta 107, TAREA 5, EL CIERRE DE LA BOLSA). SIN CORRECCION: ningun puesto se "
    "mueve. (5.1) Recuento propio del lote (docs/loop/SALIDA_V107_TAREA5_1_RECUENTO_LOTE.md): "
    "discrepancia de procedimiento declarada, el 148 ya paso por la pregunta de tres vias en la "
    "TAREA 4.3 de esta misma vuelta, asi que el lote vigente es DIEZ (3, 5, 7, 10, 13, 16, 19, 27, "
    "30, 33, tramo1), no once. (5.2) Guarda del paso mal casado sobre los cuatro tramos: los "
    "mismos dos de siempre (46, 147). (5.3) Pregunta de tres vias sobre los diez, formato de tres "
    "campos: 10 OBJETO, 0 SATELITE, 0 NO_OBJETO. (5.4) Nadie se mueve. (5.5) CIFRA FINAL CON LAS "
    "DOS DEFINICIONES, medida hoy (docs/loop/SALIDA_V107_TAREA5_5_CIFRA_FINAL_BOLSA.txt): de las "
    "74 RESUELTA vivas, 74 han pasado por la pregunta de tres vias (74/74), 0 no han pasado por "
    "ningun instrumento (0/74). LA BOLSA QUEDA CERRADA. Cifra de cierre sin cambio: 74 / 109 "
    "(59,6%). REGISTRO Y JUICIO, NO CIRUGIA: estado no se toca, no se escribe ni retira ninguna "
    "arista."
)


def main():
    with open(RUTA, encoding="utf-8") as f:
        filas = [json.loads(l) for l in f if l.strip()]

    antes = len(filas)
    tocadas = 0
    for fila in filas:
        if fila.get("id_op") == "OP-E-03":
            fila["nota"] = fila["nota"] + AGREGADO
            tocadas += 1
    assert tocadas == 1, tocadas

    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    print("filas antes=%d despues=%d tocadas=%d" % (antes, len(filas), tocadas))


if __name__ == "__main__":
    main()
