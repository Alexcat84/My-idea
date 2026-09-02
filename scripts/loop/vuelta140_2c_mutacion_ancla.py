# -*- coding: utf-8 -*-
r"""vuelta140_2c_mutacion_ancla.py . LA PRUEBA DE QUE EL ANCLA CLAVADA CAE
CUANDO SE PIERDE (TAREA 2.c de la vuelta 140, acta de la vuelta 139, caida 4.2).

QUE PRUEBA. La 2.c clavo el sujeto del bloque (iii) de
`vuelta139_2b_mutaciones.py` por su blob (`23bde6cd:docs/loop/REPORTE.md`) con
su sha256 cotejado en cada corrida, y metio ese script en la nomina de
`verificar_mutaciones_viejas.py`. Falta demostrar que eso SIRVE DE ALGO: que si
el ancla se pierde, la bateria lo clasifica como ANCLA PERDIDA y NO como verde.

COMO. Se hace una COPIA del script en `scripts/loop/` (ahi, y no en un temporal,
porque el script resuelve la raiz del repo desde su propio `__file__`), se le
cambia UNA COSA: el sha256 esperado, por otro que no cuadra. Se corre la copia y
se pasa su salida por `clasificar()`, LA FUNCION DE VERDAD de la bateria, no una
reimplementacion. Tiene que salir `ANCLA PERDIDA`.

CONTRAPRUEBA: la misma copia SIN tocar el sha256 tiene que salir `OK`. Si las
dos salieran igual, el caso no probaria nada.

NINGUN VEREDICTO ES UN LITERAL: los dos se computan llamando a `clasificar()`
sobre la salida real de cada corrida.

LA COPIA SE RETIRA SIEMPRE (P.16, quien fabrica limpia), pase lo que pase.

USO:
  python scripts/loop/vuelta140_2c_mutacion_ancla.py
"""
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as B  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP_SCRIPTS = os.path.join(RAIZ, "scripts", "loop")
ORIGINAL = os.path.join(LOOP_SCRIPTS, "vuelta139_2b_mutaciones.py")
COPIA = os.path.join(LOOP_SCRIPTS, "_v140_copia_mutacion_ancla.py")


def correr(ruta):
    """Se corre con LOOP_BATERIA_EN_CURSO puesto a proposito, para que la copia
    NO relance la bateria entera (el cortacircuitos de la 2.c). Lo unico que
    este caso mide es el bloque del ancla."""
    entorno = dict(os.environ)
    entorno["LOOP_BATERIA_EN_CURSO"] = "1"
    r = subprocess.run([sys.executable, ruta], cwd=RAIZ, capture_output=True,
                       text=True, env=entorno)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    fuente = io.open(ORIGINAL, encoding="utf-8").read()
    sha_real = B and None  # placeholder para que quede claro que no se teclea
    linea = [l for l in fuente.splitlines() if l.startswith("SHA256_REPORTE_138 =")]
    if len(linea) != 1:
        print("ARNES ROTO: se esperaba UNA linea SHA256_REPORTE_138 y hay %d" % len(linea))
        return 1
    sha_real = linea[0].split("=", 1)[1].strip().strip('"')
    print("SHA256 CLAVADO EN EL SCRIPT (leido, no tecleado): %s" % sha_real)

    try:
        # ---- CONTRAPRUEBA: la copia SIN tocar nada.
        io.open(COPIA, "w", encoding="utf-8", newline="\n").write(fuente)
        cod_c, txt_c = correr(COPIA)
        clase_c = B.clasificar(cod_c, txt_c)
        print("")
        print("CONTRAPRUEBA (copia intacta): exit %d, clasificada por la bateria como %s"
              % (cod_c, clase_c))

        # ---- MUTACION: se pierde el ancla.
        falso = "0" * 64
        mutado = fuente.replace('SHA256_REPORTE_138 = "%s"' % sha_real,
                                'SHA256_REPORTE_138 = "%s"' % falso)
        if mutado == fuente:
            print("ARNES ROTO: la sustitucion del sha256 no cambio nada")
            return 1
        io.open(COPIA, "w", encoding="utf-8", newline="\n").write(mutado)
        cod_m, txt_m = correr(COPIA)
        clase_m = B.clasificar(cod_m, txt_m)
        print("MUTADA (sha256 cambiado a %s...): exit %d, clasificada como %s"
              % (falso[:8], cod_m, clase_m))
        for l in txt_m.splitlines():
            if "ROJO PREVIO" in l or "ANCLA PERDIDA" in l:
                print("   %s" % l.strip())

        ok = (clase_c == "OK" and clase_m == "ANCLA PERDIDA")
        print("")
        print("EL ANCLA PERDIDA SE CLASIFICA COMO TAL Y NO COMO VERDE: %s" % ok)
        print("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
        return 0 if ok else 1
    finally:
        if os.path.exists(COPIA):
            os.remove(COPIA)
        print("P.16, copia retirada: %s" % ("SI" if not os.path.exists(COPIA) else "NO"))


if __name__ == "__main__":
    raise SystemExit(main())
