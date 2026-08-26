"""VUELTA 78, TAREA 3.1 (donde escribirlo, cierre): anade a la
`verificacion` de OP-E-01 la linea que declara el ensanche del filtro
P.9.1 con la vara de los veredictos A vivos. No se toca ninguna linea
vieja: se ANADE una nueva al final del array.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
RUTA = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"

LINEA_NUEVA = (
    "FILTRO DE ELEGIBILIDAD P.9.1 ENSANCHADO CON LA VARA DE LOS VEREDICTOS A "
    "(adjudicado por cita, acta del auditor vuelta 77 seccion 3 D4 y seccion "
    "5 punto 5, sin doctrina nueva: P.9 puntos 1 y 2, AUDITOR.md seccion 0 "
    "punto 3): ademas de eliminar, superviviente y nodos de "
    "RENOMBRE_CON_ALIAS, el filtro cruza tambien docs/INTRA_DOMINIO_VEREDICTOS.jsonl "
    "y aparta el candidato cuyo extremo (madre o hijo) participe en un "
    "veredicto clase A donde los DOS nodos del par esten vivos hoy, tenga o "
    "no operacion escrita: un A vivo es una fusion que el plan aun no ha "
    "citado. Implementado en scripts/loop/vuelta78_filtro_p91_vara_a.py, "
    "con caso positivo en las dos direcciones y verificacion de que un A con "
    "un extremo ya deprecado no aparta nada (ya resuelto por otra via)."
)


def main():
    lineas = RUTA.read_text(encoding="utf-8").splitlines()
    tocada = False
    for i, linea in enumerate(lineas):
        if not linea.strip():
            continue
        op = json.loads(linea)
        if op["id_op"] == "OP-E-01":
            if LINEA_NUEVA not in op["verificacion"]:
                op["verificacion"].append(LINEA_NUEVA)
                lineas[i] = json.dumps(op, ensure_ascii=False)
                tocada = True
    RUTA.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print("OP-E-01.verificacion ensanchada" if tocada else "YA ESTABA (nada que tocar)")


if __name__ == "__main__":
    main()
