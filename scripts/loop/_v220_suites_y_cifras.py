# -*- coding: utf-8 -*-
r"""_v220_suites_y_cifras.py . LAS TRES SUITES SOLAS Y LAS DOS CIFRAS DEL
CIERRE DE LA VUELTA 220, SELLADAS EN LOS NOMBRES QUE EL CIERRE INTEGRAL BUSCA.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). No vigila nada y muere con la vuelta.

POR QUE EXISTE, DICHO SIN ADORNO: _v220_cierre_integral.py lee CINCO ficheros
que ningun otro instrumento escribe (las tres suites solas, el marcador y el
conteo de aristas), y las dos tareas de esta vuelta no los escriben: la 1 es
lectura y la 2 es la bateria.

IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5, linea 72517 de
docs/loop/ACTA_AUDITOR.md). Aqui NO se copia ni una linea del de la 219: se
IMPORTA entero y solo se le cambia EL NUMERO DE VUELTA, que se computa de mi
propio nombre de fichero y no se teclea. Los comandos son los mismos y no se
eligen aqui.

USO:  python scripts/loop/_v220_suites_y_cifras.py
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import _v219_suites_y_cifras as S  # noqa: E402

YO = os.path.basename(os.path.abspath(__file__))
_M = re.match(r"^_v(\d+)_", YO)
if not _M:
    raise SystemExit("ROJO: el nombre %r no dice de que vuelta es este computo, "
                     "y el numero NO SE ADIVINA." % YO)
MI_VUELTA = int(_M.group(1))

VUELTA_HEREDADA = S.VUELTA
S.VUELTA = MI_VUELTA


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print("EL COMPUTO IMPORTADO, NO CLONADO: %s" % os.path.basename(S.__file__))
    print("  vuelta que ESE fichero computa de SU nombre: %d" % VUELTA_HEREDADA)
    print("  vuelta de ESTA corrida (computada de mi nombre, no tecleada): %d"
          % MI_VUELTA)
    sys.exit(S.main())
