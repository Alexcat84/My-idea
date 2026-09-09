# -*- coding: utf-8 -*-
r"""_v219_apertura.py . COMPUTO DE LA VUELTA 219, CON PREFIJO DE GUION BAJO,
FUERA DEL CENSO Y FUERA DE LA NOMINA (moratoria de AUDITOR.md 6.3).

QUE HACE: mide el estado del arbol ANTES DE LA PRIMERA OPERACION de la vuelta
(EJECUTOR.md 1, LA APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION) y lo sella.

IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5, linea 72517 de
docs/loop/ACTA_AUDITOR.md, LEIDA EN ESTA VUELTA Y NO RECORDADA). Este fichero
NO copia ni una linea del computo de la 218: IMPORTA _v218_apertura entero y
solo le cambia DOS cosas, EL NUMERO DE VUELTA (que se computa de mi propio
nombre de fichero y no se teclea) y LA LISTA DE SEDES que esta vuelta va a
nombrar, que es la unica parte que cambia de vuelta en vuelta.

LA 219 NO ES VUELTA DE BATERIA (cadencia de cinco de AUDITOR.md 6.1: la 215 la
corrio y la siguiente cae en la 220), asi que esta apertura no lleva sellos de
tramo. LO QUE SI LLEVA, porque esta vuelta las va a leer, son LA PAGINA 01
DONDE VIVE LA CLAUSULA DEL SEGUNDO LIBRO, LA PAGINA 05 DEL SANEO, EL
EXPEDIENTE, LA PAGINA 08 Y LA PAGINA 07 DE LA ADUANA (que NO SE TOCA, es sede
del fundador y solo se mide), mas el fichero de veredictos del cribado.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _v218_apertura as A  # noqa: E402

YO = os.path.basename(os.path.abspath(__file__))
_M = re.match(r"^_v(\d+)_", YO)
if not _M:
    raise SystemExit("ROJO: el nombre %r no dice de que vuelta es este computo, "
                     "y el numero NO SE ADIVINA." % YO)
MI_VUELTA = int(_M.group(1))

VUELTA_HEREDADA = A.VUELTA
A.VUELTA = MI_VUELTA

A.RUTAS = [
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/REPORTE.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "docs/INTRA_DOMINIO_INFORME.md",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/INVENTARIO.jsonl",
    "docs/plan/08_VERIFICACION.md",
    "docs/plan/01_FUENTES.md",
    "docs/plan/02_DESTEJIDOS.md",
    "docs/plan/03_FUSIONES.md",
    "docs/plan/05_SANEO.md",
    "docs/plan/07_ADUANA.md",
    "docs/BANCO_DE_TEXTOS.md",
    "docs/plan/BANCO_DEL_PLAN.md",
    "dataset/metadata/master_graph.json",
]

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print("EL COMPUTO IMPORTADO, NO CLONADO: %s"
          % os.path.basename(A.__file__))
    print("  vuelta que ESE fichero computa de SU nombre: %d" % VUELTA_HEREDADA)
    print("  vuelta de ESTA corrida (computada de mi nombre, no tecleada): %d"
          % MI_VUELTA)
    print("  sedes que ESTA vuelta nombra: %d" % len(A.RUTAS))
    sys.exit(A.main())
