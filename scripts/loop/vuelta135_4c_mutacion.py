# -*- coding: utf-8 -*-
"""vuelta135_4c_mutacion.py . TAREA 4.c de la vuelta 135, prueba de
mutacion obligatoria de la extension a SEIS peldanos de
verificar_cabecera_mapeo.py. Sobre una COPIA de
docs/plan/OP_S_11_MAPEO_PROPUESTO.md (real, tal como esta en el arbol),
BORRA el peldano `**54 grupos**` de la cabecera y comprueba que la guarda
cae ROJO EXIT 1 nombrandolo (numero y etiqueta).

AVISO MEDIDO POR EL AUDITOR EN LA 134: esta guarda ya aguanto tres
mutaciones del auditor que el ejecutor de la 134 no probo (una cifra de
cierre, otro peldano y los colapsos); esta prueba NO la afloja al
extenderla a seis: usa el MISMO mecanismo (peldanos como multiconjunto de
`**N grupos**`) que ya paso esas tres, solo que ahora con seis miembros en
vez de cinco.

Salida: docs/loop/SALIDA_V135_4C_MUTACION.txt

USO:
  python scripts/loop/vuelta135_4c_mutacion.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TABLA_REAL = os.path.join(RAIZ, "docs", "plan", "OP_S_11_MAPEO_PROPUESTO.md")
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_cabecera_mapeo.py")
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V135_4C_MUTACION.txt")

VIEJO = "usa la cola, agrupamiento POR IGUALDAD y PREFIJO sobre la recortada: **54 grupos**."
NUEVO = "usa la cola, agrupamiento POR IGUALDAD y PREFIJO sobre la recortada."


def main():
    with io.open(TABLA_REAL, encoding="utf-8") as f:
        texto = f.read()
    if texto.count(VIEJO) != 1:
        print("ROJO PREVIO: el ancla del peldano 6 no aparece exactamente una vez.")
        return 1
    mutado = texto.replace(VIEJO, NUEVO)

    fd, ruta_tmp = tempfile.mkstemp(suffix=".md", prefix="OP_S_11_MUTADO_4C_")
    os.close(fd)
    with io.open(ruta_tmp, "w", encoding="utf-8") as f:
        f.write(mutado)

    try:
        r = subprocess.run([sys.executable, GUARDA, "--tabla", ruta_tmp],
                            capture_output=True, text=True)
        salida_txt = (
            "MUTACION 4.c: se borra el peldano '**54 grupos**' de la cabecera, sobre "
            "copia de docs/plan/OP_S_11_MAPEO_PROPUESTO.md (real).\n"
            "--- salida de verificar_cabecera_mapeo.py ---\n%s\n%s\n"
            "EXITCODE proceso: %d\n" % (r.stdout, r.stderr, r.returncode)
        )
        verificada = (r.returncode == 1 and "peldano 54" in r.stdout)
        salida_txt += ("MUTACION VERIFICADA: cayo ROJO nombrando el peldano 54 que falta, "
                        "como se esperaba.\n" if verificada else
                        "MUTACION NO VERIFICADA: no cayo como se esperaba.\n")
        salida_txt += "EXITCODE: %d\n" % (0 if verificada else 1)
    finally:
        os.remove(ruta_tmp)

    with io.open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write(salida_txt)
    print(salida_txt)
    return 0 if verificada else 1


if __name__ == "__main__":
    raise SystemExit(main())
