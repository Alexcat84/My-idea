# -*- coding: utf-8 -*-
r"""_v215_ciclo_gate0.py . EL CICLO ENTERO DE GATE 0 DE LA VUELTA 215, CON SU
CONSOLA SELLADA POR EL PROPIO INSTRUMENTO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo, fuera de la
nomina (congelada en 135), no anade guarda ni lector que se quede vigilando y
muere con la vuelta. Acta 199 `4.5`, acta 203 `4.6`, acta 205 `4.1`.

NO ES UN CLON Y NO COPIA NI UNA LINEA DE LOS OCHO COMANDOS. Importa
`_v205_ciclo_gate0.py`, que ya los tiene en su orden, y le corrige EL DATO que
ese fichero computa de su propio nombre: el numero de vuelta. IMPORTAR NO ES
CLONAR, adjudicado como letra general por el acta 206 `6.5`.

LO QUE ESTA VUELTA ANADE, Y ES EL REMEDIO DE LA `3.1` DEL ACTA 214: EL CICLO
SELLA SU PROPIA CONSOLA. En la 214 el ciclo imprimio su consola por `stdout`,
nadie la redirigio, y la seccion 3.1 del reporte salio publicada VACIA porque
el fichero que el compositor busca NUNCA EXISTIO. Acordarse de redirigir es
justo lo que esta casa lleva vueltas demostrando que no funciona: aqui la
consola se escribe DENTRO del instrumento, en el nombre exacto que el
compositor busca, y ademas se sigue imprimiendo por pantalla.

EL NOMBRE DEL FICHERO NO SE TECLEA: se compone del numero de vuelta que sale de
`os.path.basename(__file__)` y del lado que llega por argumento.

USO:  python scripts/loop/_v215_ciclo_gate0.py APERTURA
      python scripts/loop/_v215_ciclo_gate0.py CIERRE"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import _v205_ciclo_gate0 as C   # noqa: E402

NL = chr(10)
YO = os.path.basename(os.path.abspath(__file__))
_M = re.match(r"^_v(\d+)_", YO)
if not _M:
    raise SystemExit("ROJO: el nombre %r no dice de que vuelta es este computo, "
                     "y el numero NO SE ADIVINA." % YO)
MI_VUELTA = int(_M.group(1))

VUELTA_HEREDADA = C.VUELTA
C.VUELTA = MI_VUELTA


class Tee(object):
    """LO QUE SE IMPRIME SE GUARDA. No sustituye la pantalla: la duplica."""

    def __init__(self, original):
        self.original = original
        self.trozos = []

    def write(self, s):
        self.trozos.append(s)
        self.original.write(s)
        return len(s)

    def flush(self):
        self.original.flush()

    def reconfigure(self, **kw):
        """EL CICLO IMPORTADO LLAMA A reconfigure() SOBRE stdout. Se le pasa
        al original en vez de reventar: duplicar la salida no puede cambiar lo
        que el ciclo hace."""
        return self.original.reconfigure(**kw)

    def texto(self):
        return "".join(self.trozos).replace(chr(13) + NL, NL)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    lado = sys.argv[1].upper() if len(sys.argv) > 1 else ""
    tee = Tee(sys.stdout)
    sys.stdout = tee
    print("EL CICLO IMPORTADO, NO CLONADO: %s" % os.path.basename(C.__file__))
    print("  vuelta que ESE fichero computa de SU nombre: %d" % VUELTA_HEREDADA)
    print("  vuelta de ESTA corrida (computada de mi nombre, no tecleada): %d"
          % MI_VUELTA)
    codigo = C.main()
    sys.stdout = tee.original
    if lado in ("APERTURA", "CIERRE"):
        destino = os.path.join(
            C.LOOP, "SALIDA_V%d_CICLO_GATE0_%s_CONSOLA.txt" % (MI_VUELTA, lado))
        io.open(destino, "w", encoding="utf-8", newline=NL).write(tee.texto())
        print("CONSOLA SELLADA POR EL PROPIO INSTRUMENTO -> %s, %d bytes"
              % (os.path.basename(destino), os.path.getsize(destino)))
        if os.path.getsize(destino) == 0:
            print("ROJO: la consola sellada mide CERO BYTES y eso no cuenta "
                  "como hecha.")
            raise SystemExit(1)
    raise SystemExit(codigo)
