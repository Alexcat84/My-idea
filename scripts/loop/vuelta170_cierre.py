# -*- coding: utf-8 -*-
r"""vuelta170_cierre.py . EL BLOQUE DE CIERRE DE LA VUELTA 170.

POR QUE NACE ASI Y NO A MANO: EJECUTOR.md 1, "EL ESTADO AL CIERRE SE MIDE AL
CIERRE" (14 ago 2026, por la caida de la vuelta 28, donde la tabla del cierre
traia la medicion de APERTURA despues de que la propia vuelta la moviera). Y
porque `scripts/loop/tallar_cabecera_reporte.py --fase04` lee su columna DERECHA
de estos ficheros: sin ellos, la mitad del cabecero sale en rojo.

CLON DECLARADO de la mitad de mediciones de `scripts/loop/vuelta170_apertura.py`,
con el mismo ciclo de Gate 0 ENTERO Y EN SU ORDEN, nunca `run_phase1` suelto.
Esta vuelta ya pago una caida por correrlo suelto (el guardian del commit la
cazo con 71 nodos divergentes de `etiqueta_arbol`), asi que el orden va escrito
aqui para no volver a fiarlo a la memoria:
  1) run_phase1.py --reaplico-curaduria
  2) etiquetas_de_cara.py --aplicar
  3) sync_assets_web.py
  4) git diff HEAD --numstat -- dataset/ web/ engine/

QUE ANADE RESPECTO DEL DE APERTURA: el HEAD DE CIERRE, que el tallador exige por
su nombre (`SALIDA_V170_HEAD_CIERRE.txt`) y que se lee de `git rev-parse HEAD`
DESPUES de la ultima operacion, nunca antes.

USO:
  python scripts/loop/vuelta170_cierre.py
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
    ruta = os.path.join(LOOP, "SALIDA_V170_%s_CIERRE.txt" % nombre)
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
