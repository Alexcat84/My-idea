# -*- coding: utf-8 -*-
"""vuelta134_2d_mutacion_2.py . TAREA 2.d, MUTACION 2 de la vuelta 134. ESTA
ES LA MUTACION QUE HABRIA CAZADO EL CONTRATO VIEJO DE 2.e (acta 133, 4.4).

Copia el REPORTE.md REAL que hay en el arbol (no uno fabricado), BORRA la
cita del fichero de salida que acompana a "0 pares" (la frase
"(`SALIDA_V133_1E_GUARDAS.txt`, `_1F_`, `_1G_`)") y comprueba que
verificar_cifras_del_reporte.py cae en ROJO por la regla nueva de 2.b (cifra
sin fichero en su ventana, no exenta), en vez de listarla y quedarse en
VERDE/EXIT 0 como hacia el contrato viejo.

USO:
  python scripts/loop/vuelta134_2d_mutacion_2.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE_REAL = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_cifras_del_reporte.py")

CITA_A_BORRAR = "(`SALIDA_V133_1E_GUARDAS.txt`, `_1F_`, `_1G_`)."


def main():
    with io.open(REPORTE_REAL, encoding="utf-8") as f:
        texto = f.read()
    if CITA_A_BORRAR not in texto:
        print("ROJO PREVIO: no encuentro la cita a borrar en el reporte real, cambia el anclaje.")
        return 1
    mutado = texto.replace(CITA_A_BORRAR, ".")

    fd, ruta_tmp = tempfile.mkstemp(suffix=".md", prefix="REPORTE_134_MUTADO_2D2_")
    os.close(fd)
    with io.open(ruta_tmp, "w", encoding="utf-8") as f:
        f.write(mutado)

    try:
        r = subprocess.run([sys.executable, GUARDA, "--reporte", ruta_tmp],
                            capture_output=True, text=True)
        print("--- copia mutada: cita de SALIDA_V133_1E_GUARDAS.txt BORRADA junto a '0 pares' ---")
        print(r.stdout)
        print(r.stderr)
        print("EXITCODE proceso: %d" % r.returncode)
        if r.returncode == 1 and "0 pares" in r.stdout and "SIN fichero de salida" in r.stdout:
            print("MUTACION 2 VERIFICADA: la guarda cae en ROJO por la regla nueva de 2.b, "
                  "en vez de listarla y quedarse en VERDE como el contrato viejo.")
            return 0
        print("MUTACION 2 NO VERIFICADA: la guarda no cayo como se esperaba.")
        return 1
    finally:
        os.remove(ruta_tmp)


if __name__ == "__main__":
    raise SystemExit(main())
