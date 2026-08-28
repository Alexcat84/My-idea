# -*- coding: utf-8 -*-
"""vuelta107_tarea4_registro_operaciones_nota.py . Anade el registro de la
TAREA 4 de la vuelta 107 al campo `nota` de OP-E-03 en
docs/plan/OPERACIONES.jsonl, sin borrar una letra de lo que ya hay.

USO:
  python scripts/loop/vuelta107_tarea4_registro_operaciones_nota.py
"""
import json

RUTA = "docs/plan/OPERACIONES.jsonl"

AGREGADO = (
    " REGISTRO (vuelta 107, TAREA 4, el 109 a lectura entera mas el tramo 3 al doble). "
    "SIN CORRECCION: direccion_leida no cambia en ningun puesto. (4.1) El caso gramatical del "
    "auditor sobre el 109 se confirma: 'socios' vive en el complemento instrumental del paso 1 "
    "de la madre, no en el objeto directo ('el canvas inicial'); reclasificado SATELITE. (4.2) "
    "Lectura entera a ciegas (docs/loop/SALIDA_V107_TAREA4_1_2_LECTURA_ENTERA_109.md): el "
    "contra-caso del auditor gana (paso 6 del hijo PLANEA, no ejecuta, la validacion; pasos 1 a 4 "
    "desarrollan el item socios en procedimiento completo, patron 9.6.2 igual que 123 y 127; paso "
    "5 es entrega de vuelta, patron 2.215). 109 SOSTIENE. (4.3) Pregunta de tres vias sobre las "
    "RESUELTA vivas del tramo 3 (docs/loop/SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md, contada con "
    "scripts/loop/vuelta107_contar_tres_vias.py): DISCREPANCIA DECLARADA, el encargo citaba 18, "
    "contadas hoy son 19 (la TAREA 3 de esta vuelta revirtio el 145 a RESUELTA); barridas las 19: "
    "18 OBJETO, 1 SATELITE (el propio 109, nuevo), 0 NO_OBJETO. (4.4) Cero satelites nuevos "
    "ademas del 109 (123 sostenido en la 106, 145 resuelto por la TAREA 3 de esta vuelta). Cifra "
    "de cierre sin cambio: 74 / 109 (59,6%). REGISTRO Y JUICIO, NO CIRUGIA: estado no se toca, no "
    "se escribe ni retira ninguna arista."
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
