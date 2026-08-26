"""VUELTA 78, TAREA 1.5: lleva el toque unico (banco 9.4, tercer caso) al
campo `nodos` de OP-S-09 en OPERACIONES.jsonl. Los dos ids
(estructura_de_gates, estructura_gates) estan en el `eliminar` de
OP-M-01-FUSION, que corre antes (fase 03_FUSIONES, orden 5) que OP-S-09
(fase 05_SANEO, orden 8): el toque unico los remite a la fusion, que ya los
condena, y OP-S-09 deja de nombrarlos en su nomina de renombre.

El texto viejo de `nota` y `adjudicacion` NO se borra: se ANADE la
correccion declarada al final, igual que hizo vuelta77_op_s09_escribir_nomina.py.
"""
import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
RUTA = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"
SCRIPT_MEDICION = RAIZ / "scripts" / "loop" / "vuelta78_tarea15_toque_unico.py"


def recomputar():
    salida = subprocess.run(
        [sys.executable, str(SCRIPT_MEDICION)],
        capture_output=True, text=True, check=True, cwd=str(RAIZ),
    ).stdout
    inicio = salida.index("NOMINA_NUEVA_JSON_START") + len("NOMINA_NUEVA_JSON_START")
    fin = salida.index("NOMINA_NUEVA_JSON_END")
    ids = json.loads(salida[inicio:fin].strip())
    return ids


def main():
    ids = recomputar()
    assert len(ids) == 67, f"esperaba 67, obtuve {len(ids)}"

    lineas = RUTA.read_text(encoding="utf-8").splitlines()
    tocada = False
    for i, linea in enumerate(lineas):
        if not linea.strip():
            continue
        op = json.loads(linea)
        if op["id_op"] != "OP-S-09":
            continue

        nomina_vieja = op.get("nodos") or []
        assert len(nomina_vieja) == 69, f"la nomina en ficha no tiene 69, tiene {len(nomina_vieja)}"
        op["nodos"] = ids

        correccion = (
            "CORRECCION DECLARADA (vuelta 78, TAREA 1.5, tercer caso de EL "
            "TOQUE UNICO, banco 9.4, adjudicado por el auditor en el acta "
            "77 seccion 5 punto 9): 2 de los 69 ids de la nomina "
            "(estructura_de_gates, estructura_gates) estan en el campo "
            "eliminar de OP-M-01-FUSION, que corre antes (fase 03_FUSIONES, "
            "orden 5) que esta operacion (fase 05_SANEO, orden 8). Los dos "
            "forman por si solos la familia [PARTICULAS] de la nomina de la "
            "vuelta 77: al remitirlos a la fusion que ya los condena, la "
            "familia desaparece entera. La nomina de renombre queda en 67 "
            "ids, NO 69, medido por scripts/loop/vuelta78_tarea15_toque_unico.py "
            "(docs/loop/SALIDA_V78_TAREA15_TOQUE_UNICO.txt)."
        )
        if correccion not in (op.get("nota") or ""):
            op["nota"] = (op.get("nota") or "") + " " + correccion
        vieja_adj = op.get("adjudicacion") or ""
        marca_adj = (" TOQUE UNICO vuelta 78 (ver nota): 2 ids remitidos a "
                     "OP-M-01-FUSION, nomina queda en 67.")
        if marca_adj.strip() not in vieja_adj:
            op["adjudicacion"] = vieja_adj + marca_adj
        nueva_evidencia = ("TOQUE UNICO vuelta 78 (26 ago 2026): "
                            "docs/loop/SALIDA_V78_TAREA15_TOQUE_UNICO.txt")
        if nueva_evidencia not in (op.get("evidencia") or []):
            op.setdefault("evidencia", []).append(nueva_evidencia)

        lineas[i] = json.dumps(op, ensure_ascii=False)
        tocada = True

    if not tocada:
        print("OP-S-09 NO ENCONTRADA")
        return

    RUTA.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print(f"OP-S-09.nodos re-escrito: {len(ids)} ids (69 menos los 2 del toque unico)")


if __name__ == "__main__":
    main()
