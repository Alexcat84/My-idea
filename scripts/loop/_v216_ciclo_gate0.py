# -*- coding: utf-8 -*-
r"""_v216_ciclo_gate0.py . EL CICLO ENTERO DE GATE 0 DE LA VUELTA 216, CON SU
CONSOLA SELLADA POR EL PROPIO INSTRUMENTO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo, fuera de la
nomina (congelada en 135), no anade guarda ni lector que se quede vigilando y
muere con la vuelta. Acta 199 `4.5`, acta 203 `4.6`, acta 205 `4.1`.

NO ES UN CLON. Los NUEVE comandos se importan de `_v205_ciclo_gate0.py`, que ya
los tiene en su orden, y LA CLASE Tee se importa de `_v215_ciclo_gate0.py`, que
es donde nacio el remedio de la `3.1` del acta 214. Aqui no se copia ni una
linea de ninguna de las dos: solo cambia EL NUMERO DE VUELTA, que se computa de
`os.path.basename(__file__)` y NO SE TECLEA. IMPORTAR NO ES CLONAR, adjudicado
como letra general por el acta 206 `6.5`.

EL REMEDIO DE LA 215 SE MANTIENE Y NO SE AFLOJA (encargo de la 216, TAREA 4.a):
la consola se escribe DENTRO del instrumento, en el nombre exacto que el
compositor busca, y el instrumento CAE EN ROJO por sus dos puertas, la del
fichero ausente y la del fichero de cero bytes.

USO:  python scripts/loop/_v216_ciclo_gate0.py APERTURA
      python scripts/loop/_v216_ciclo_gate0.py CIERRE"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import _v205_ciclo_gate0 as C          # noqa: E402
from _v215_ciclo_gate0 import Tee      # noqa: E402

NL = chr(10)
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
    lado = sys.argv[1].upper() if len(sys.argv) > 1 else ""
    tee = Tee(sys.stdout)
    sys.stdout = tee
    print("EL CICLO IMPORTADO, NO CLONADO: %s" % os.path.basename(C.__file__))
    print("  vuelta que ESE fichero computa de SU nombre: %d" % VUELTA_HEREDADA)
    print("  Tee IMPORTADA, NO CLONADA, de _v215_ciclo_gate0.py")
    print("  vuelta de ESTA corrida (computada de mi nombre, no tecleada): %d"
          % MI_VUELTA)
    codigo = C.main()
    sys.stdout = tee.original
    if lado in ("APERTURA", "CIERRE"):
        destino = os.path.join(
            C.LOOP, "SALIDA_V%d_CICLO_GATE0_%s_CONSOLA.txt" % (MI_VUELTA, lado))
        io.open(destino, "w", encoding="utf-8", newline=NL).write(tee.texto())
        if not os.path.isfile(destino):
            print("ROJO: la consola sellada NO EXISTE en disco.")
            raise SystemExit(1)
        print("CONSOLA SELLADA POR EL PROPIO INSTRUMENTO -> %s, %d bytes"
              % (os.path.basename(destino), os.path.getsize(destino)))
        if os.path.getsize(destino) == 0:
            print("ROJO: la consola sellada mide CERO BYTES y eso no cuenta "
                  "como hecha.")
            raise SystemExit(1)
    raise SystemExit(codigo)
