"""Metodos validados (decision del fundador, 6 oct 2026; docs/REGLAS_DE_LA_CASA.md, M1).

La calculadora y el estimador de esfuerzo son METODOS VALIDADOS: sus resultados cuentan como material permitido en
todos los prompts, y ningun cambio a sus formulas, criterios, rangos o pruebas se hace sin el visto del fundador.

Este modulo calcula la huella de cada pieza protegida. El registro sellado vive en docs/metodos_validados.json, y la
guarda es engine/test_metodos_validados.py. Para resellar tras un cambio aprobado:

    python scripts/metodos_validados.py --visto "fecha y nota del visto del fundador"

y el commit lleva "VISTO DEL FUNDADOR" en el mensaje (lo exige .githooks/commit-msg).
"""
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
REGISTRO = BASE / "docs" / "metodos_validados.json"

PROTEGIDOS = (
    "engine/calculadora.py",
    "engine/test_calculadora.py",
    "web/lib/calculadora.ts",
    "web/lib/calculadora.test.ts",
    "web/lib/engine/estimacion.ts",
    "web/lib/engine/estimacion.test.ts",
    "web/lib/engine/rangoBanda.ts",
    "web/lib/prompts.ts#SYSTEM_ESTIMACION_BANDA",
)


def leer(clave):
    ruta, _, bloque = clave.partition("#")
    texto = (BASE / ruta).read_text(encoding="utf-8").replace("\r\n", "\n")
    if not bloque:
        return texto
    m = re.search(r"export const %s = \[.*?\n\]\.join\(\"\\n\"\);" % re.escape(bloque), texto, re.S)
    if not m:
        raise SystemExit("no encuentro el bloque %s en %s" % (bloque, ruta))
    return m.group(0)


def sha(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def huellas():
    return {k: sha(leer(k)) for k in PROTEGIDOS}


def sellar(nota):
    reg = json.loads(REGISTRO.read_text(encoding="utf-8")) if REGISTRO.exists() else {
        "_nota": "Registro sellado de los metodos validados (REGLAS M1). Solo se resella con el visto del fundador: "
                 "python scripts/metodos_validados.py --visto \"...\"; el commit lleva VISTO DEL FUNDADOR.",
        "huellas": {}, "visto": []}
    reg["huellas"] = huellas()
    reg["visto"].append({"fecha": date.today().isoformat(), "nota": nota})
    REGISTRO.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("registro sellado:", len(reg["huellas"]), "piezas")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "--visto" or not sys.argv[2].strip():
        raise SystemExit('uso: python scripts/metodos_validados.py --visto "nota del visto del fundador"')
    sellar(sys.argv[2])
