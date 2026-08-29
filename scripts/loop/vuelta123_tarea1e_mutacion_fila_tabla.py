# -*- coding: utf-8 -*-
"""vuelta123_tarea1e_mutacion_fila_tabla.py . CASO POSITIVO del arreglo del
punto ciego de fila de tabla en verificar_citas_del_reporte.py (TAREA 1.e,
encargo de la vuelta 123, acta de la vuelta 122 seccion 4.6).

Toma docs/loop/REPORTE.md TAL COMO ESTABA COMMITEADO al cierre de la vuelta
122 (git show 128d0e5b:docs/loop/REPORTE.md, el commit del acta 122, ultimo
en tener ese contenido antes de que la vuelta 123 lo sobrescriba), le anade
AL FINAL, tal cual la escribio el encargo de la vuelta 123 (TAREA 1.e), la
fila de tabla:

  | motor de la apertura | 25/25 (`SALIDA_V122_TSC_APERTURA.txt`) | **25/25** |

que cita, CON CITA PROPIA EN LA MISMA FILA, `SALIDA_V122_TSC_APERTURA.txt`
(el tsc de la apertura de la 122, una sola linea "EXITCODE: 0", que JAMAS
contiene la cadena "TODOS LOS TESTS PASARON (25/25)": esa cadena es del
motor, no del tsc). Con el arreglo de la 123 (la fila vuelve a ser
cotejable cuando trae cita propia), la guarda tiene que caer en ROJO
nombrando ese par.

USO:
  python scripts/loop/vuelta123_tarea1e_mutacion_fila_tabla.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILA = "\n| motor de la apertura | 25/25 (`SALIDA_V122_TSC_APERTURA.txt`) | **25/25** |\n"


def texto_reporte_122():
    r = subprocess.run(["git", "show", "128d0e5b:docs/loop/REPORTE.md"], cwd=RAIZ,
                       capture_output=True, text=True, check=True, encoding="utf-8")
    return r.stdout


def mutar(texto):
    return texto + FILA


def main():
    texto = texto_reporte_122()
    mutado = mutar(texto)
    ruta = os.path.join(tempfile.gettempdir(), "REPORTE_122_MUTADO_TAREA1E_FILA.md")
    with io.open(ruta, "w", encoding="utf-8") as f:
        f.write(mutado)
    r = subprocess.run([sys.executable, os.path.join(RAIZ, "scripts", "loop",
                        "verificar_citas_del_reporte.py"), "--reporte", ruta],
                       cwd=RAIZ, capture_output=True, text=True)
    print(r.stdout)
    print(r.stderr, file=sys.stderr)
    esperado_en_salida = 'NO CUADRA "25/25" <-> `SALIDA_V122_TSC_APERTURA.txt`'
    if r.returncode == 0:
        raise SystemExit("CAIDA DE LA PRUEBA DE MUTACION: la guarda dio VERDE sobre la fila de tabla mutada")
    if esperado_en_salida not in r.stdout:
        raise SystemExit("CAIDA DE LA PRUEBA DE MUTACION: la guarda cayo en ROJO pero no nombro el par esperado")
    print("MUTACION VERIFICADA: la guarda cae en ROJO nombrando la fila de tabla mutada, como se esperaba.")
    sys.exit(0)


if __name__ == "__main__":
    main()
