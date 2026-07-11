# -*- coding: utf-8 -*-
"""Hygiene v1.3.1 — el validador de esquema debe RECHAZAR (exit 1) cualquier
nodo con campos fuera de la lista blanca o con obligatorios vacíos, y aceptar
(exit 0) un nodo conforme. Nace de la auditoría v1.3: garantía permanente de
que un campo renegado (p.ej. un resumen_keorico o un titulo inventado) jamás
vuelve a entrar en silencio.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
VALIDADOR = BASE / "scripts" / "expansion" / "validar_esquema.py"

NODO_LIMPIO = {
    "node_id": "nodo_sintetico_limpio",
    "fase_proyecto": "ideacion",
    "dominio": "core",
    "titulo_concepto": "Nodo Sintético Limpio",
    "fuente": "Test",
    "resumen_teorico": "Resumen de prueba.",
    "pasos_accionables": ["Paso 1"],
    "entregable_esperado": "Nada",
    "nodos_previos": [],
    "nodos_siguientes": [],
    "condiciones_activacion": ["Siempre"],
}


def correr(carpeta):
    return subprocess.run([sys.executable, str(VALIDADOR), str(carpeta)],
                          capture_output=True, text=True).returncode


def main():
    with tempfile.TemporaryDirectory() as tmp:
        carpeta = Path(tmp)

        # 1) nodo conforme -> exit 0
        (carpeta / "nodo_sintetico_limpio.json").write_text(
            json.dumps(NODO_LIMPIO, ensure_ascii=False, indent=2), encoding="utf-8")
        rc = correr(carpeta)
        assert rc == 0, f"nodo limpio debio pasar (exit 0), dio {rc}"

        # 2) campo renegado (el fantasma reincidente) -> exit 1
        renegado = dict(NODO_LIMPIO, node_id="nodo_sintetico_renegado")
        renegado["titulo"] = "Campo que no existe en el esquema"
        renegado["resumen_keorico"] = "typo clasico"
        (carpeta / "nodo_sintetico_renegado.json").write_text(
            json.dumps(renegado, ensure_ascii=False, indent=2), encoding="utf-8")
        rc = correr(carpeta)
        assert rc == 1, f"nodo renegado debio RECHAZARSE (exit 1), dio {rc}"
        (carpeta / "nodo_sintetico_renegado.json").unlink()

        # 3) obligatorio vacio -> exit 1
        vacio = dict(NODO_LIMPIO, node_id="nodo_sintetico_vacio", resumen_teorico="  ")
        (carpeta / "nodo_sintetico_vacio.json").write_text(
            json.dumps(vacio, ensure_ascii=False, indent=2), encoding="utf-8")
        rc = correr(carpeta)
        assert rc == 1, f"obligatorio vacio debio RECHAZARSE (exit 1), dio {rc}"

    print("OK: el validador rechaza renegados y vacios, y acepta nodos conformes.")


if __name__ == "__main__":
    main()
