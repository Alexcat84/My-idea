# -*- coding: utf-8 -*-
r"""vuelta115_tarea2_4_mutacion_z.py . MUTACION Z (TAREA 2.4 de la vuelta
115): prueba, DEL LADO ROJO, la capa de motivo que la TAREA 2.3 le sumo a
scripts/loop/vuelta115_guardas_cierre.py.

QUE HACE. Escribe una COPIA de vuelta115_guardas_cierre.py
(scripts/loop/_v115_mut_z_copia.py, commiteada como pieza historica igual que
otras copias _v*.py de este directorio) con DOS ediciones, y NADA MAS:
  1. el comando del caso "Z_SONDA (control 2.3/2.4)" pasa de
     `sys.exit(0)` a `sys.exit(1)` (el comportamiento REAL cambia);
  2. su `esperado` en la tupla CASOS pasa de 0 a 1 (para que, a simple
     vista, el caso SIGA CALZANDO: codigo 1 == esperado 1).
NO se toca `ESPERADO_BASE` (sigue anclado en 0, el valor original) ni
`MOTIVOS` (no se le anade una entrada a Z_SONDA): es exactamente el
escenario que 2.3 vino a atajar, un esperado que se mueve en silencio para
esconder un cambio de comportamiento real.

LA VARA. La salida de la copia mutada NO PUEDE decir solo "[CALZA]" para
Z_SONDA: tiene que imprimir la linea "ALERTA: ESPERADO CAMBIADO SIN MOTIVO
DECLARADO" nombrando el caso, Y el EXIT de la guarda entera tiene que ser 1
(ROJO), aunque el caso individual muestre CALZA. Se corren las DOS versiones
(el fichero real de hoy, sin mutar, y la copia mutada) y se pegan las dos
salidas completas, cada una en su fichero nombrado:
  docs/loop/SALIDA_V115_TAREA2_4_MUTACION_Z_ANTES.txt (el real, VERDE en
    Z_SONDA, sin ALERTA)
  docs/loop/SALIDA_V115_TAREA2_4_MUTACION_Z_DESPUES.txt (la copia mutada,
    Z_SONDA en [CALZA] PERO con la ALERTA, guarda entera ROJO)

USO:
  python scripts/loop/vuelta115_tarea2_4_mutacion_z.py
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PY = sys.executable
ORIGINAL = os.path.join(RAIZ, "scripts", "loop", "vuelta115_guardas_cierre.py")
COPIA = os.path.join(RAIZ, "scripts", "loop", "_v115_mut_z_copia.py")

ANTES_ORIG = '("Z_SONDA (control 2.3/2.4)", ["-c", "import sys; sys.exit(0)"], 0),'
DESPUES_MUT = '("Z_SONDA (control 2.3/2.4)", ["-c", "import sys; sys.exit(1)"], 1),'


def escribir_copia_mutada():
    with open(ORIGINAL, encoding="utf-8") as f:
        texto = f.read()
    if texto.count(ANTES_ORIG) != 1:
        raise SystemExit("ROJO: la linea de Z_SONDA a mutar no aparece EXACTAMENTE una vez en %s "
                          "(aparece %d veces). NO SE MUTA NADA." % (ORIGINAL, texto.count(ANTES_ORIG)))
    mutado = texto.replace(ANTES_ORIG, DESPUES_MUT, 1)
    with open(COPIA, "w", encoding="utf-8") as f:
        f.write(mutado)


def correr(ruta):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([PY, ruta], cwd=RAIZ, capture_output=True, env=env)
    out = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    return r.returncode, out


def main():
    escribir_copia_mutada()

    cod_antes, out_antes = correr(ORIGINAL)
    cod_despues, out_despues = correr(COPIA)

    linea_z_antes = next((l for l in out_antes.splitlines() if l.startswith("Z_SONDA")), "")
    linea_z_despues = next((l for l in out_despues.splitlines() if l.startswith("Z_SONDA")), "")
    alerta_despues = "ALERTA: ESPERADO CAMBIADO SIN MOTIVO DECLARADO" in out_despues
    alerta_antes = "ALERTA: ESPERADO CAMBIADO SIN MOTIVO DECLARADO" in out_antes

    print("=== ANTES (fichero real, sin mutar) ===")
    print("EXIT guarda entera: %d" % cod_antes)
    print("Z_SONDA: %s" % linea_z_antes)
    print("ALERTA presente: %s (esperado False)" % alerta_antes)
    print()
    print("=== DESPUES (copia mutada, esperado de Z_SONDA cambiado SIN motivo) ===")
    print("EXIT guarda entera: %d" % cod_despues)
    print("Z_SONDA: %s" % linea_z_despues)
    print("ALERTA presente: %s (esperado True)" % alerta_despues)
    print()

    ok_antes = "[CALZA]" in linea_z_antes and not alerta_antes
    ok_despues = "[CALZA]" in linea_z_despues and alerta_despues and cod_despues == 1

    print("VARA: ANTES calza en silencio y sin alerta (%s); DESPUES sigue en [CALZA] pero la "
          "ALERTA lo delata y la guarda entera cae a ROJO (%s)." % (ok_antes, ok_despues))
    if ok_antes and ok_despues:
        print("PASA: la capa de motivo (TAREA 2.3) DELATA el esperado cambiado sin motivo; no dice CALZA en silencio.")
        return 0
    print("NO PASA: la mutacion Z no se comporto como se esperaba.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
