# -*- coding: utf-8 -*-
r"""vuelta192_cierre.py . EL BLOQUE DE CIERRE DE LA VUELTA 192.

CLON DECLARADO de scripts/loop/vuelta191_cierre.py. Cambia UNICAMENTE el numero
de vuelta del prefijo de las salidas y este docstring. El cotejo del clon lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte con lo
que salga: AQUI NO SE AFIRMA QUE NINGUN DIFF SALGA VACIO.

POR QUE EXISTE: EJECUTOR.md 1, "EL ESTADO AL CIERRE SE MIDE AL CIERRE". Y porque
scripts/loop/tallar_cabecera_reporte.py --fase04 lee su columna DERECHA de estos
ficheros: sin ellos, la mitad del cabecero sale en rojo.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, nunca run_phase1 suelto:
  1) run_phase1.py --reaplico-curaduria
  2) etiquetas_de_cara.py --aplicar
  3) sync_assets_web.py
  4) git diff HEAD --numstat -- dataset/ web/ engine/

EL HEAD DE CIERRE se lee de git rev-parse HEAD DESPUES de la ultima operacion,
nunca antes.

Y LO QUE ESTE FICHERO NO HACE: NO CIERRA EL REPORTE. Solo mide y escribe ficheros
SALIDA_V192_*_CIERRE.txt. El cierre lo hace scripts/loop/cerrar_reporte.py.

USO:
  python scripts/loop/vuelta192_cierre.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env, shell=shell)
    out = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    return r.returncode, out


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V192_%s_CIERRE.txt" % nombre)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)" % (os.path.basename(ruta), len(texto.encode("utf-8"))))


# 1. HEAD DE CIERRE, leido de git DESPUES de la ultima operacion
c, o = correr(["git", "rev-parse", "HEAD"])
escribir("HEAD", o)

# 2. GATE 0, paso 1 del ciclo
c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
escribir("GATE0_CMD1", o + "\nEXITCODE: %d\n" % c)

# 3. ciclo, paso 2
c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
escribir("CICLO_ETIQUETAS", o + "\nEXITCODE: %d\n" % c)

# 4. ciclo, paso 3
c, o = correr([PY, "scripts/sync_assets_web.py"])
escribir("CICLO_SYNC", o + "\nEXITCODE: %d\n" % c)

# 5. ciclo, paso 4: el numstat, DESPUES de los tres anteriores
c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/", "engine/"])
escribir("CICLO_NUMSTAT", o + "\nEXITCODE: %d\n" % c)

# 6. censo y aristas
c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
escribir("CONTEO", o + "\nEXITCODE: %d\n" % c)

# 7. desfase del calibrado
c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + "\nEXITCODE: %d\n" % c)

# 8. motor
c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

# 9. tsc
c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d\n" % c)

# 10. suites de la web
c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + "\nEXITCODE: %d\n" % c)

print("BLOQUE DE CIERRE COMPLETO")
