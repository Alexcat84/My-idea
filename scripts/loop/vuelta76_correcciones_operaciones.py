"""VUELTA 76, TAREA 1.3.b y 1.3.c: dos correcciones declaradas sobre
docs/plan/OPERACIONES.jsonl, adjudicadas por el auditor en el acta de la
vuelta 75 (secciones 4.3 y 4.4). No se reescribe nada del texto viejo: se
ANADE el campo o la linea que faltaba.

1.3.b OP-E-01: le falta el filtro de elegibilidad P.9.1 en su verificacion.
1.3.c OP-E-05: su depende_de no nombra la fusion de la que depende de verdad.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
RUTA = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"

FILTRO_P91 = (
    "FILTRO DE ELEGIBILIDAD P.9.1, OBLIGATORIO ANTES DE ESCRIBIR (correccion "
    "declarada, vuelta 76, adjudicada por el auditor acta vuelta 75 seccion "
    "4.4): todo candidato de la bolsa se cruza contra los campos eliminar y "
    "superviviente de las operaciones NO EJECUTADAS. Si el destino o la madre "
    "muere en una operacion pendiente, el par NO se lee para escribir: se "
    "aparta con el id de esa operacion escrito al lado y espera su turno"
)


def main():
    lineas = RUTA.read_text(encoding="utf-8").splitlines()
    tocadas = []
    for i, linea in enumerate(lineas):
        if not linea.strip():
            continue
        op = json.loads(linea)
        if op["id_op"] == "OP-E-01":
            if FILTRO_P91 not in op["verificacion"]:
                op["verificacion"].append(FILTRO_P91)
                lineas[i] = json.dumps(op, ensure_ascii=False)
                tocadas.append("OP-E-01: filtro P.9.1 anadido a verificacion")
        elif op["id_op"] == "OP-E-05":
            nuevo = ["OP-M-01", "OP-M-01-FUSION"]
            if op["depende_de"] != nuevo:
                viejo = list(op["depende_de"])
                op["depende_de"] = nuevo
                lineas[i] = json.dumps(op, ensure_ascii=False)
                tocadas.append(f"OP-E-05: depende_de {viejo} -> {nuevo}")

    RUTA.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    for t in tocadas:
        print(t)
    if not tocadas:
        print("NADA QUE TOCAR (ya aplicado)")


if __name__ == "__main__":
    main()
