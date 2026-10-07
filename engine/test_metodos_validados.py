"""Metodos validados: la calculadora y el estimador de esfuerzo (decision del fundador, 6 oct 2026; REGLAS M1).

Sus formulas, criterios, rangos y pruebas no cambian sin el visto del fundador. Esta guarda compara la huella de cada
fichero protegido (y del bloque SYSTEM_ESTIMACION_BANDA) con el registro sellado docs/metodos_validados.json. Si algo
cambio, falla: el cambio solo entra resellando el registro con `python scripts/metodos_validados.py --visto "..."`, y
el hook commit-msg exige entonces "VISTO DEL FUNDADOR" en el mensaje del commit. Prueba en rojo primero.
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import metodos_validados as mv  # noqa: E402


def test_el_registro_existe_y_tiene_visto():
    reg = json.loads((BASE / "docs" / "metodos_validados.json").read_text(encoding="utf-8"))
    assert reg["visto"], "el registro no tiene ninguna nota de visto"
    assert set(reg["huellas"]) == set(mv.PROTEGIDOS), "el registro no cubre exactamente los protegidos"


def test_ningun_metodo_validado_cambio_sin_visto():
    reg = json.loads((BASE / "docs" / "metodos_validados.json").read_text(encoding="utf-8"))
    cambiados = [k for k, h in mv.huellas().items() if reg["huellas"].get(k) != h]
    assert cambiados == [], (
        "metodos validados cambiados sin visto del fundador: %s. Si el fundador lo aprobo, resella con "
        "python scripts/metodos_validados.py --visto \"<nota>\" y pon VISTO DEL FUNDADOR en el commit." % cambiados)


def test_la_huella_detecta_un_cambio():
    # caso negativo: el bloque del estimador se extrae entero; tocar una letra cambia su huella
    texto = mv.leer("web/lib/prompts.ts#SYSTEM_ESTIMACION_BANDA")
    assert "SYSTEM_ESTIMACION_BANDA" in texto and len(texto) > 200
    assert mv.sha(texto) != mv.sha(texto + " ")


if __name__ == "__main__":
    fallos = 0
    for nombre, f in list(globals().items()):
        if nombre.startswith("test_") and callable(f):
            try:
                f()
                print("OK  ", nombre)
            except Exception as e:  # noqa: BLE001
                fallos += 1
                print("FALLA", nombre, repr(e)[:300])
    sys.exit(1 if fallos else 0)
