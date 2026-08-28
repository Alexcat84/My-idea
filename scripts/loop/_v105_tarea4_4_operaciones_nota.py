import json

AGREGADO = (
    " CORRECCION DECLARADA (vuelta 105, TAREA 4.1 a 4.4, re-barrido de los 41 con la pregunta de "
    "tres respuestas y lectura entera a ciegas de los SATELITE). Censo de la especie del 46 en los "
    "cuatro tramos: 2 puestos (46 tramo2, 147 tramo3). Re-barrido de los 41 OBJETO de la vuelta 104: "
    "el 46 salta por la guarda del paso mal casado; de los 40 restantes, 33 OBJETO, 7 SATELITE "
    "(20, 21, 38, 66, 87, 91, 93), 0 NO_OBJETO. Lectura entera a ciegas de los 7 SATELITE (los 5 no "
    "cubiertos por la TAREA 3, mas el 20 y el 93 de la TAREA 3): 5 se mueven (20, 21, 38, 66, 93), "
    "2 sostienen (87, 91: evaluar/establecer CON el complemento exige desplegarlo). `correccion_v105` "
    "en los cinco puestos que se mueven, campo `direccion_leida` a null; clase D no cambia en "
    "ninguno. Recontado con `scripts/loop/contar_cierre_efectivo.py` "
    "(`docs/loop/SALIDA_V105_TAREA4_4_CIERRE_EFECTIVO.txt`): clase A 3, B 2, C 1 (par 111), D 177; "
    "direccion leida y afirmada 74, NO RESUELTA 109 (59,6%); invertidas 2 (pares 16, 114). LA CIFRA "
    "VIGENTE ES 74 / 109 (59,6%). REGISTRO Y JUICIO, NO CIRUGIA: estado no se toca, no se escribe "
    "ni retira ninguna arista."
)


def main():
    with open("docs/plan/OPERACIONES.jsonl", encoding="utf-8") as f:
        filas = [json.loads(l) for l in f if l.strip()]

    antes = len(filas)
    tocadas = 0
    for fila in filas:
        if fila.get("id_op") == "OP-E-03":
            fila["nota"] = fila["nota"] + AGREGADO
            tocadas += 1
    assert tocadas == 1, tocadas

    with open("docs/plan/OPERACIONES.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    print("filas antes=%d despues=%d tocadas=%d" % (antes, len(filas), tocadas))


if __name__ == "__main__":
    main()
