# -*- coding: utf-8 -*-
r"""_v219_suites_y_cifras.py . LAS TRES SUITES SOLAS Y LAS DOS CIFRAS DEL
CIERRE DE LA VUELTA 219, SELLADAS EN LOS NOMBRES QUE EL CIERRE INTEGRAL BUSCA.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). No vigila nada y muere con la vuelta.

POR QUE EXISTE, DICHO SIN ADORNO: _v218_cierre_integral.py lee CINCO ficheros
que ningun otro instrumento escribe (las tres suites solas, el marcador y el
conteo de aristas), y en la 218 los escribio la propia tarea que corria las
suites. Esta vuelta es de LECTURA y sus dos tareas no corren suites, asi que
los cinco los escribe esto, con el mismo nombre exacto y el mismo formato que
ese lector exige (la marca EXITCODE dentro del propio fichero).

LOS COMANDOS NO SE ELIGEN AQUI: son los mismos tres de las suites del ciclo y
los dos del marcador y las aristas que la casa ya corre en cada vuelta.

USO:  python scripts/loop/_v219_suites_y_cifras.py
"""
import io
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))


def correr(cmd, shell=False, cwd=None):
    r = subprocess.run(cmd, cwd=cwd or RAIZ, shell=shell, capture_output=True)
    o = (r.stdout + r.stderr).decode("utf-8", errors="replace").replace(
        chr(13) + NL, NL)
    return r.returncode, o


def sellar(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, nombre))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    return ruta, os.path.getsize(ruta)


def main():
    fallos = 0
    print("=" * 78)
    print("VUELTA %d. LAS TRES SUITES SOLAS Y LAS DOS CIFRAS DEL CIERRE"
          % VUELTA)
    print("=" * 78)

    c, o = correr([PY, "engine/run_all_tests.py"])
    ruta, b = sellar("T2_SUITE_MOTOR", o + NL + "EXITCODE: %d" % c + NL)
    print("   motor  EXITCODE %d | %d bytes -> %s"
          % (c, b, os.path.basename(ruta)))
    fallos += 1 if c or b == 0 else 0

    c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True,
                  cwd=os.path.join(RAIZ, "web"))
    ruta, b = sellar("T2_SUITE_TSC",
                     "TSC EXIT=%d" % c + NL + (o if o.strip() else "")
                     + NL + "EXITCODE: %d" % c + NL)
    print("   tsc    EXITCODE %d | %d bytes -> %s"
          % (c, b, os.path.basename(ruta)))
    fallos += 1 if c or b == 0 else 0

    c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
    ruta, b = sellar("T2_SUITE_WEB", o + NL + "EXITCODE: %d" % c + NL)
    print("   web    EXITCODE %d | %d bytes -> %s"
          % (c, b, os.path.basename(ruta)))
    fallos += 1 if c or b == 0 else 0

    c, o = correr([PY, "scripts/recomputar_marcador.py", "3388"])
    ruta, b = sellar("T2_MARCADOR", o)
    print("   marcador EXITCODE %d | %d bytes -> %s"
          % (c, b, os.path.basename(ruta)))
    fallos += 1 if c or b == 0 else 0

    c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
    ruta, b = sellar("T2_ARISTAS", o)
    print("   aristas  EXITCODE %d | %d bytes -> %s"
          % (c, b, os.path.basename(ruta)))
    fallos += 1 if c or b == 0 else 0

    print("CIFRA comprobaciones que fallan: %d" % fallos)
    print("VERDE: los cinco ficheros quedan sellados." if not fallos
          else "ROJO: algo salio en rojo o midio cero bytes.")
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
