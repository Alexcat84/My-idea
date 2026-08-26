"""VUELTA 77, TAREA 1.5: lleva la nomina recomputada de OP-S-09 (script
vuelta77_op_s09_nomina.py, salida en docs/loop/SALIDA_V77_OP_S09_NOMINA.txt)
al campo `nodos` de OPERACIONES.jsonl, que es su sitio verdadero porque
OP-S-09 es RENOMBRE_CON_ALIAS: sus nodos NO se eliminan, se renombran
conservando alias. NO se toca `eliminar` ni `superviviente` (siguen [] y
null: no aplica a este tipo de operacion). El texto viejo de `adjudicacion`,
`evidencia` y `nota` NO se borra: se ANADE la correccion declarada al final.
"""
import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
RUTA = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"
NOMINA_SCRIPT = RAIZ / "scripts" / "loop" / "vuelta77_op_s09_nomina.py"


def recomputar_nomina():
    salida = subprocess.run(
        [sys.executable, str(NOMINA_SCRIPT)],
        capture_output=True, text=True, check=True, cwd=str(RAIZ),
    ).stdout
    inicio = salida.index("NOMINA_IDS_JSON_START") + len("NOMINA_IDS_JSON_START")
    fin = salida.index("NOMINA_IDS_JSON_END")
    ids = json.loads(salida[inicio:fin].strip())
    total_familias = int(salida.split("FAMILIAS: ")[1].splitlines()[0])
    return ids, total_familias


def main():
    ids, total_familias = recomputar_nomina()

    lineas = RUTA.read_text(encoding="utf-8").splitlines()
    tocada = False
    for i, linea in enumerate(lineas):
        if not linea.strip():
            continue
        op = json.loads(linea)
        if op["id_op"] != "OP-S-09":
            continue

        op["nodos"] = ids

        correccion = (
            f"CORRECCION DECLARADA (vuelta 77, TAREA 1.5, "
            f"docs/loop/paradas/2026-08-26-racha-tramo-mecanico-DECISION.md): "
            f"la nomina recomputada HOY del grafo (script "
            f"scripts/loop/vuelta77_op_s09_nomina.py, salida "
            f"docs/loop/SALIDA_V77_OP_S09_NOMINA.txt) sobre nodos VIVOS con "
            f"el mismo criterio escrito (sufijo numerico, particulas, orden "
            f"de palabras, sinonimo puro) da {total_familias} familias y "
            f"{len(ids)} nodos, NO 53 y 125. DELTA DECLARADO, no forzado: de "
            f"las cuatro familias mayores citadas en 05_SANEO.md, TODOS los "
            f"miembros que hoy faltan (accion_correctiva_5, "
            f"accion_correctiva_6, definiciones_operacionales_4, "
            f"consejo_calidad, consejo_calidad_2) estan deprecados en el "
            f"grafo de hoy, verificado por corrida propia: la nomina de 11 "
            f"ago 2026 midio antes de que otras operaciones de fusion "
            f"(fase 03) ya absorbieran una parte de estos duplicados por "
            f"otra via. La nomina de {len(ids)} ids queda escrita en el "
            f"campo nodos de esta misma operacion, campo que hasta esta "
            f"vuelta estaba vacio."
        )
        if correccion not in (op.get("nota") or ""):
            op["nota"] = (op.get("nota") or "") + " " + correccion
        vieja_adj = op.get("adjudicacion") or ""
        marca_adj = " NOMINA ESCRITA EN vuelta 77 (ver nota): recomputo NO da 53/125, ver correccion declarada."
        if marca_adj.strip() not in vieja_adj:
            op["adjudicacion"] = vieja_adj + marca_adj
        nueva_evidencia = "RECOMPUTO vuelta 77 (26 ago 2026): docs/loop/SALIDA_V77_OP_S09_NOMINA.txt"
        if nueva_evidencia not in (op.get("evidencia") or []):
            op.setdefault("evidencia", []).append(nueva_evidencia)

        lineas[i] = json.dumps(op, ensure_ascii=False)
        tocada = True

    if not tocada:
        print("OP-S-09 NO ENCONTRADA")
        return

    RUTA.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print(f"OP-S-09.nodos escrito: {len(ids)} ids, {total_familias} familias")


if __name__ == "__main__":
    main()
