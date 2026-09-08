# -*- coding: utf-8 -*-
r"""_v208_ciclo_gate0.py . EL CICLO ENTERO DE GATE 0 DE LA VUELTA 208.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo, fuera de la
nomina (congelada en 135), no anade guarda ni lector que se quede vigilando y
muere con la vuelta. Acta 199 `4.5`, acta 203 `4.6`, acta 205 `4.1`.

NO ES UN CLON Y NO COPIA NI UNA LINEA. Importa `_v205_ciclo_gate0.py`, que ya
tiene los ocho comandos en su orden, y le corrige EL DATO que ese fichero computa
de su propio nombre: el numero de vuelta. **IMPORTAR NO ES CLONAR**, adjudicado
como letra general por el acta 206 `6.5`, que ademas dice *"ya no lo preguntes"*.

EL NUMERO NO SE TECLEA AQUI TAMPOCO: sale de `os.path.basename(__file__)` con el
patron `^_v(\d+)_`.

USO:  python scripts/loop/_v208_ciclo_gate0.py APERTURA
      python scripts/loop/_v208_ciclo_gate0.py CIERRE"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import _v205_ciclo_gate0 as C   # noqa: E402

YO = os.path.basename(os.path.abspath(__file__))
_M = re.match(r"^_v(\d+)_", YO)
if not _M:
    raise SystemExit("ROJO: el nombre %r no dice de que vuelta es este computo, "
                     "y el numero NO SE ADIVINA." % YO)
MI_VUELTA = int(_M.group(1))

VUELTA_HEREDADA = C.VUELTA
C.VUELTA = MI_VUELTA

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print("EL CICLO IMPORTADO, NO CLONADO: %s" % os.path.basename(C.__file__))
    print("  vuelta que ESE fichero computa de SU nombre: %d" % VUELTA_HEREDADA)
    print("  vuelta de ESTA corrida (computada de mi nombre, no tecleada): %d"
          % MI_VUELTA)
    raise SystemExit(C.main())
