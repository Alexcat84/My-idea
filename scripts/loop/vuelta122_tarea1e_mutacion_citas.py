# -*- coding: utf-8 -*-
"""vuelta122_tarea1e_mutacion_citas.py . CASO ROJO POR MUTACION de
verificar_citas_del_reporte.py (TAREA 1.e, encargo de la vuelta 122).

Toma docs/loop/REPORTE.md TAL COMO ESTABA COMMITEADO al cierre de la vuelta
121 (git show ed916471:docs/loop/REPORTE.md, el commit del acta 121, que es
el ultimo en tener ese contenido antes de que esta vuelta lo sobrescriba), le
inyecta UNA mutacion (la frase "vacio" del git status pasa a citar, SIN
ABREVIAR, `SALIDA_V121_OPS03_ROJO_SEGUNDA_PASADA.txt`, fichero que trae tres
lineas " M dataset/...json" y por tanto NO esta vacio) y corre la guarda sobre
la copia mutada. Tiene que caer en ROJO nombrando exactamente ese par.

USO:
  python scripts/loop/vuelta122_tarea1e_mutacion_citas.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def texto_reporte_121():
    r = subprocess.run(["git", "show", "ed916471:docs/loop/REPORTE.md"], cwd=RAIZ,
                       capture_output=True, text=True, check=True, encoding="utf-8")
    return r.stdout


def mutar(texto):
    original = ("`git status\n--porcelain` vacio tras el rojo (sin escritura nueva).")
    mutado = ("`git status\n--porcelain` vacio tras el rojo (sin escritura nueva), "
              "ver `SALIDA_V121_OPS03_ROJO_SEGUNDA_PASADA.txt`.")
    if original not in texto:
        raise SystemExit("ROJO (del propio arnes): la frase a mutar no aparece en el REPORTE.md de ed916471")
    return texto.replace(original, mutado)


def main():
    texto = texto_reporte_121()
    mutado = mutar(texto)
    ruta = os.path.join(tempfile.gettempdir(), "REPORTE_121_MUTADO_TAREA1E.md")
    with io.open(ruta, "w", encoding="utf-8") as f:
        f.write(mutado)
    r = subprocess.run([sys.executable, os.path.join(RAIZ, "scripts", "loop",
                        "verificar_citas_del_reporte.py"), "--reporte", ruta],
                       cwd=RAIZ, capture_output=True, text=True)
    print(r.stdout)
    print(r.stderr, file=sys.stderr)
    esperado_en_salida = 'NO CUADRA "vacio" <-> `SALIDA_V121_OPS03_ROJO_SEGUNDA_PASADA.txt`'
    if r.returncode == 0:
        raise SystemExit("CAIDA DE LA PRUEBA DE MUTACION: la guarda dio VERDE sobre la copia mutada")
    if esperado_en_salida not in r.stdout:
        raise SystemExit("CAIDA DE LA PRUEBA DE MUTACION: la guarda cayo en ROJO pero no nombro el par esperado")
    print("MUTACION VERIFICADA: la guarda cae en ROJO nombrando el par mutado, como se esperaba.")
    sys.exit(0)


if __name__ == "__main__":
    main()
