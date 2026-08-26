"""VUELTA 77, TAREA 1.5 (donde escribirlos, cierre): anade a la
`verificacion` de OP-E-01 la linea que declara el ensanche del filtro
P.9.1 a las operaciones RENOMBRE_CON_ALIAS (campo `nodos`). No se toca
ninguna linea vieja: se ANADE una nueva al final del array.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
RUTA = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"

LINEA_NUEVA = (
    "FILTRO DE ELEGIBILIDAD P.9.1 ENSANCHADO (correccion declarada, vuelta "
    "77, docs/loop/paradas/2026-08-26-racha-tramo-mecanico-DECISION.md): "
    "ademas de eliminar y superviviente, el filtro cruza tambien el campo "
    "nodos de las operaciones NO EJECUTADAS de tipo RENOMBRE_CON_ALIAS (hoy "
    "solo OP-S-09). Si la madre o el hijo del candidato esta en ese campo, "
    "el par se aparta igual que si muriera por eliminar: sus nodos NO se "
    "eliminan pero SI cambian de id, y P.9 exige que la arista se escriba "
    "con el id que estara vivo el dia de su escritura. Implementado en "
    "scripts/loop/vuelta77_filtro_p91_ensanchado.py, con caso positivo en "
    "las dos direcciones"
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
