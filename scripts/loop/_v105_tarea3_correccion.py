import json

AGREGADO = (
    " CORRECCION DECLARADA (vuelta 105, TAREA 3, relectura conjunta con el auditor de los "
    "pares 20 y 93, acta de la vuelta 104, discutibles 1 y 2). Leidos los cuatro nodos enteros y "
    "9.6.2/9.6.3 enteros. Par 20 (waterfall_vs_agile_development -> modelo_customer_development, "
    "paso 3): primer brazo del 9.6.2 falla (coordinacion, no ejecucion del modelo; el hijo que si "
    "despliega la alineacion es el par 13), senal de entregables confirma (decision de metodologia "
    "contra diagrama de estado de CD). Par 93 (estandares_voluntarios -> "
    "definiciones_operacionales_de_calidad, paso 3): primer brazo del 9.6.2 falla (estandar de "
    "industria por consenso contra acuerdo bilateral con cartas de control compartidas de forma "
    "continua, sin contraparte en la madre), 9.6.3 confirma SANO. Los dos contra-casos del auditor "
    "examinados y NO ganados. `correccion_v105` en `docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl` "
    "puesto 20 y `docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl` puesto 93, campo `direccion_leida` a "
    "null en los dos; clase D no cambia. Recontado con `scripts/loop/contar_cierre_efectivo.py` "
    "(`docs/loop/SALIDA_V105_TAREA3_CIERRE_EFECTIVO.txt`): clase A 3, B 2, C 1 (par 111), D 177; "
    "direccion leida y afirmada 77, NO RESUELTA 106 (57,9%); invertidas 2 (pares 16, 114). LA CIFRA "
    "VIGENTE ES 77 / 106 (57,9%). REGISTRO Y JUICIO, NO CIRUGIA: estado no se toca, no se escribe "
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
