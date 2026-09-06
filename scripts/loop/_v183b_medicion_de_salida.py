# -*- coding: utf-8 -*-
r"""_v183b_medicion_de_salida.py . EL CICLO DE GATE 0 ENTERO AL SALIR DE ESTA
SESION, MEDIDO DESPUES DE LA ULTIMA OPERACION.

POR QUE NO SE LLAMA CIERRE, Y ES LA MITAD QUE IMPORTA. La vuelta 183 **NO
CIERRA** en esta sesion: su bateria paro en el TRAMO 5 DE 9 con un arnes en rojo,
`--componer` no puede armar `docs/loop/SALIDA_V183_BATERIA.txt` y sin esa pieza
`scripts/loop/cerrar_reporte.py` no puede cerrar el reporte. Por eso estas
salidas se llaman `SALIDA_V183B_*_SALIDA.txt` y **NO** `SALIDA_V183_*_CIERRE.txt`:
si llevaran el nombre del cierre, `tallar_cabecera_reporte.py` las tragaria y
tallaria una columna de CIERRE de una vuelta que no ha cerrado, que es la caida
de la vuelta 28 al reves (medir temprano y publicar tarde).

QUE SI SOSTIENEN: que el arbol que esta sesion deja esta medido y no supuesto,
despues de tocar el lanzador de la bateria, la nomina y cuatro instrumentos
nuevos. La columna de CIERRE de verdad la medira la vuelta que cierre.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

USO:
  python scripts/loop/_v183b_medicion_de_salida.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
SUFIJO = "183B"


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env, shell=shell)
    out = (r.stdout.decode("utf-8", errors="replace")
           + r.stderr.decode("utf-8", errors="replace"))
    return r.returncode, out


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%s_%s_SALIDA.txt" % (SUFIJO, nombre))
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)"
          % (os.path.basename(ruta), len(texto.encode("utf-8"))))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    c, o = correr(["git", "rev-parse", "HEAD"])
    escribir("HEAD", o)
    print("HEAD tras la ultima operacion: %s" % o.strip())

    c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
    escribir("GATE0_CMD1", o + "\nEXITCODE: %d\n" % c)

    c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
    escribir("CICLO_ETIQUETAS", o + "\nEXITCODE: %d\n" % c)

    c, o = correr([PY, "scripts/sync_assets_web.py"])
    escribir("CICLO_SYNC", o + "\nEXITCODE: %d\n" % c)

    c, o = correr(["git", "diff", "HEAD", "--numstat", "--",
                   "dataset/", "web/", "engine/"])
    escribir("CICLO_NUMSTAT", o + "\nEXITCODE: %d\n" % c)

    c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
    escribir("CONTEO", o + "\nEXITCODE: %d\n" % c)

    c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
    escribir("DESFASE_CALIBRADO", o + "\nEXITCODE: %d\n" % c)

    c, o = correr([PY, "engine/run_all_tests.py"])
    escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

    c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True,
                  cwd=os.path.join(RAIZ, "web"))
    escribir("TSC", (o if o.strip() else "") + "EXIT=%d\n" % c)

    c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
    escribir("WEB", o + "\nEXITCODE: %d\n" % c)

    c, o = correr(["git", "diff", "--numstat", "--", "dataset/"])
    filas = len([l for l in o.splitlines() if l.strip() and not l.startswith("warning")])
    escribir("NUMSTAT_DATASET", o + "\nCIFRA filas: %d\n" % filas)
    print("CIFRA filas de git diff --numstat -- dataset/ AL SALIR: %d" % filas)
    print("MEDICION DE SALIDA COMPLETA")
    return 0


if __name__ == "__main__":
    sys.exit(main())
