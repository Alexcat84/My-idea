# -*- coding: utf-8 -*-
"""vuelta134_2f_mutacion.py . TAREA 2.f, prueba de mutacion obligatoria.

verificar_cabecera_mapeo.py se escribe EN TAREA 2, antes de que TAREA 3.c
reponga el peldano 106 en la cabecera real. Como todavia no existe una
cabecera real que YA tenga el 106 (para poder "borrarlo" y ver el ROJO), esta
prueba primero construye, sobre una COPIA de la tabla real, la MISMA frase de
adicion que 3.c va a pegar en el fichero real (paso 1, y de paso pre valida
ese texto), comprueba VERDE, y LUEGO la borra de esa copia (paso 2, la
mutacion pedida por el contrato) para comprobar que cae ROJO nombrando el
106.

USO:
  python scripts/loop/vuelta134_2f_mutacion.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TABLA_REAL = os.path.join(RAIZ, "docs", "plan", "OP_S_11_MAPEO_PROPUESTO.md")
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_cabecera_mapeo.py")

ANCLA = "VIGENTE Y SIN CASO en este corte: 0 canonicas SINTETICAS)."

FRASE_106 = (
    " PELDANO INTERMEDIO REPUESTO EN LA VUELTA 134 (adjudicado por el "
    "auditor, acta 133, 4.1: el 106 quedaba plegado dentro del peldano (3) "
    "y el reporte no declaro el apartamiento del encargo): entre (2) y (3), "
    "SOLO `vuelta132_grupos_por_localizador.py` (localizador con la cola "
    "VIEJA, SIN la extension a `Apendice` de la 133): **106 grupos**."
)


def correr(ruta_tabla):
    r = subprocess.run([sys.executable, GUARDA, "--tabla", ruta_tabla],
                        capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main():
    with io.open(TABLA_REAL, encoding="utf-8") as f:
        texto = f.read()
    if ANCLA not in texto:
        print("ROJO PREVIO: no encuentro el ancla en la tabla real, cambia el anclaje.")
        return 1

    con_106 = texto.replace(ANCLA, ANCLA + FRASE_106)

    fd, ruta_tmp = tempfile.mkstemp(suffix=".md", prefix="OP_S_11_MUTADO_2F_")
    os.close(fd)
    try:
        with io.open(ruta_tmp, "w", encoding="utf-8") as f:
            f.write(con_106)

        print("--- (1) copia CON el peldano 106 anadido por adicion: esperado VERDE ---")
        ec1, out1 = correr(ruta_tmp)
        print(out1)
        print("EXITCODE: %d" % ec1)
        if ec1 != 0:
            print("MUTACION NO VERIFICADA: el paso (1) no dio VERDE, no puedo seguir a (2).")
            return 1

        sin_106 = con_106.replace(FRASE_106, "")
        with io.open(ruta_tmp, "w", encoding="utf-8") as f:
            f.write(sin_106)

        print("\n--- (2) misma copia, peldano 106 BORRADO de nuevo: esperado ROJO nombrandolo ---")
        ec2, out2 = correr(ruta_tmp)
        print(out2)
        print("EXITCODE: %d" % ec2)
        if ec2 == 1 and "106" in out2 and "cola VIEJA" in out2:
            print("\nMUTACION 2.f VERIFICADA: (1) VERDE con el 106 puesto, (2) ROJO nombrando "
                  "el 106 al borrarlo, como se esperaba.")
            return 0
        print("\nMUTACION NO VERIFICADA: el paso (2) no cayo ROJO nombrando el 106.")
        return 1
    finally:
        os.remove(ruta_tmp)


if __name__ == "__main__":
    raise SystemExit(main())
