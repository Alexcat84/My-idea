# -*- coding: utf-8 -*-
"""vuelta107_registro_operaciones_nota.py . Anade el registro de la vuelta 107
al campo `nota` de OP-E-03 en docs/plan/OPERACIONES.jsonl, sin borrar una
letra de lo que ya hay (EJECUTOR.md 8). Uno de los tres sitios aditivos.

USO:
  python scripts/loop/vuelta107_registro_operaciones_nota.py
"""
import json

RUTA = "docs/plan/OPERACIONES.jsonl"

AGREGADO = (
    " CORRECCION DECLARADA (vuelta 107, TAREA 3, relectura conjunta con el auditor del "
    "discutible 145, acta de la vuelta 106). CEDO: correccion_v106 se revierte con "
    "correccion_v107 (sin borrarla). Los dos nodos releidos enteros: el resumen de la madre "
    "('La accion debe ser voluntaria y comprometer a todo el organismo, no un mero movimiento "
    "mecanico') y su paso 3 ('Asegurar que la accion sea genuina y comprometida [...], no un "
    "gesto mecanico vacio') hacen la MISMA advertencia que el paso 4 del hijo ('Evitar sustituir "
    "el pensamiento profundo por mera accion fisica [...] como escape de la incertidumbre'): no es "
    "material ajeno a la madre, es su propia cautela mirada desde el pensamiento. El acta 98 3.5 "
    "manda sobre este puesto (adjudicado a ciegas por su numero: tension en OTRA linea, paso 4 "
    "contra paso 1 de la madre, es caveat y no rompe la casada). Recontado con "
    "scripts/loop/contar_cierre_efectivo.py (docs/loop/SALIDA_V107_TAREA3_CIERRE_EFECTIVO.txt): "
    "clase A 3, B 2, C 1 (par 111), D 177; direccion leida y afirmada 74, NO RESUELTA 109 (59,6%); "
    "invertidas 2 (pares 16, 114). LA CIFRA VIGENTE ES 74 / 109 (59,6%). REGISTRO Y JUICIO, NO "
    "CIRUGIA: estado no se toca, no se escribe ni retira ninguna arista."
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
