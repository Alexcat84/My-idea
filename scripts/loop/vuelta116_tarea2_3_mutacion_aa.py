# -*- coding: utf-8 -*-
r"""vuelta116_tarea2_3_mutacion_aa.py . MUTACION AA (TAREA 2.3 de la vuelta
116): prueba, DEL LADO ROJO, la extension de la capa de motivo que la TAREA
2.1 le sumo a scripts/loop/vuelta116_guardas_cierre.py para los SEIS casos
que hasta la vuelta 115 quedaban fuera de ella (X, Y, TAREA2.4-v109, N, O,
P).

QUE HACE. Escribe una COPIA de vuelta116_guardas_cierre.py
(scripts/loop/_v116_mut_aa_copia.py, commiteada como pieza historica igual
que _v115_mut_z_copia.py) con UNA sola edicion, y NADA MAS: la linea
`X_MARCAS_MINIMO = 2` pasa a `X_MARCAS_MINIMO = 1` (la propiedad esperada de
X se afloja). NO se toca `ESPERADO_BASE_EXTRA["X"]` (sigue anclado en
`(1, 2)`, el valor original) ni `MOTIVOS` (no se le anade una entrada a X):
es el mismo escenario que la Mutacion Z probo para Z_SONDA, esta vez sobre
uno de los seis que la TAREA 2.1 acaba de anclar.

POR QUE SIGUE EN [CALZA] A SIMPLE VISTA. La salida real de hoy de
`tallar_cifras_de_antes.py --fichero docs/loop/_v113_mut_x/reporte_112.md`
trae EXACTAMENTE DOS marcas "sigue": aflojar el minimo de 2 a 1 no cambia el
veredicto de `caso_x()` (2 >= 1 sigue siendo verdad), asi que X sigue
imprimiendo [CALZA] igual que antes. Lo unico que cambia es que el ancla
(fija en `(1, 2)`) ya no coincide con el valor ACTUAL `(1, 1)` que la copia
usa de verdad.

LA VARA. La salida de la copia mutada NO PUEDE decir solo "[CALZA]" para X:
tiene que imprimir la linea "ALERTA: PROPIEDAD ESPERADA CAMBIADA SIN MOTIVO
DECLARADO" nombrando el caso, Y el EXIT de la guarda entera tiene que ser 1
(ROJO), aunque el caso individual (y su control AA) muestren CALZA. Se
corren las DOS versiones (el fichero real de hoy, sin mutar, y la copia
mutada) y se pegan las dos salidas completas, cada una en su fichero
nombrado:
  docs/loop/SALIDA_V116_TAREA2_3_MUTACION_AA_ANTES.txt (el real, VERDE en X y
    en AA, sin ALERTA)
  docs/loop/SALIDA_V116_TAREA2_3_MUTACION_AA_DESPUES.txt (la copia mutada, X
    sigue en [CALZA] PERO con la ALERTA, guarda entera ROJO)

USO:
  python scripts/loop/vuelta116_tarea2_3_mutacion_aa.py
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PY = sys.executable
ORIGINAL = os.path.join(RAIZ, "scripts", "loop", "vuelta116_guardas_cierre.py")
COPIA = os.path.join(RAIZ, "scripts", "loop", "_v116_mut_aa_copia.py")

ANTES_ORIG = "X_MARCAS_MINIMO = 2"
DESPUES_MUT = "X_MARCAS_MINIMO = 1"


def escribir_copia_mutada():
    with open(ORIGINAL, encoding="utf-8") as f:
        texto = f.read()
    if texto.count(ANTES_ORIG) != 1:
        raise SystemExit("ROJO: la linea de X_MARCAS_MINIMO a mutar no aparece EXACTAMENTE una vez en %s "
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

    linea_x_antes = next((l for l in out_antes.splitlines() if l.startswith("X (reporte 112")), "")
    linea_x_despues = next((l for l in out_despues.splitlines() if l.startswith("X (reporte 112")), "")
    linea_aa_antes = next((l for l in out_antes.splitlines() if l.startswith("AA (control")), "")
    linea_aa_despues = next((l for l in out_despues.splitlines() if l.startswith("AA (control")), "")
    alerta_antes = "ALERTA: PROPIEDAD ESPERADA CAMBIADA SIN MOTIVO DECLARADO" in out_antes
    alerta_despues = "ALERTA: PROPIEDAD ESPERADA CAMBIADA SIN MOTIVO DECLARADO" in out_despues

    print("=== ANTES (fichero real, sin mutar) ===")
    print("EXIT guarda entera: %d" % cod_antes)
    print("X: %s" % linea_x_antes)
    print("AA: %s" % linea_aa_antes)
    print("ALERTA presente: %s (esperado False)" % alerta_antes)
    print()
    print("=== DESPUES (copia mutada, X_MARCAS_MINIMO aflojado de 2 a 1 SIN motivo) ===")
    print("EXIT guarda entera: %d" % cod_despues)
    print("X: %s" % linea_x_despues)
    print("ALERTA presente: %s (esperado True)" % alerta_despues)
    print()

    ok_antes = "[CALZA]" in linea_x_antes and "[CALZA]" in linea_aa_antes and not alerta_antes
    ok_despues = "[CALZA]" in linea_x_despues and alerta_despues and cod_despues == 1

    print("VARA: ANTES calza en silencio y sin alerta (%s); DESPUES X sigue en [CALZA] pero la "
          "ALERTA lo delata y la guarda entera cae a ROJO (%s)." % (ok_antes, ok_despues))
    if ok_antes and ok_despues:
        print("PASA: la extension de la capa de motivo (TAREA 2.1) DELATA la propiedad esperada "
              "cambiada sin motivo en uno de los seis; no dice CALZA en silencio.")
        return 0
    print("NO PASA: la mutacion AA no se comporto como se esperaba.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
