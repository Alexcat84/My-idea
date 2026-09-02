# -*- coding: utf-8 -*-
"""vuelta137_1c_mutacion.py . TAREA 1.c de la vuelta 137: las pruebas por
mutacion de las DOS reparaciones de verificar_cifras_del_reporte.py.

EJECUTOR regla 1, EL CASO ROJO SE PRUEBA POR MUTACION. Reparar una guarda para
que deje de morder cifras CORRECTAS solo vale si se prueba que sigue mordiendo
las INCORRECTAS. Las cuatro mutaciones de aqui son eso, y ninguna se corre
contra un literal: lo que se observa es `contado`, que la guarda computa
leyendo el fichero de salida real.

  MUTACION A, LA CIFRA EQUIVOCADA POR UNO. "37 grafias sin agrupar" pasa a
  "38": tiene que caer ROJO contra la linea CIFRA 'grafias sin agrupar'.

  MUTACION B, LA CIFRA DE LA ETIQUETA VECINA DEL MISMO FICHERO. "92 grafias sin
  agrupar": 92 ES una cifra real de ese fichero, pero de la OTRA etiqueta
  ('grafias en grupo'). Tiene que caer ROJO. Es la mutacion que prueba que el
  camino FUERTE (por etiqueta) no se degrada al camino DEBIL (por conjunto): si
  se degradara, esta saldria verde.

  MUTACION C, EL FALSO VERDE QUE EL DEFECTO 2 PERMITIA. "2 grafias en grupo"
  citando SALIDA_V135_4B_PELDANOS.txt, con SALIDA_V133_2E_MUTACION.txt en la
  frase siguiente. En ese fichero vecino el recuento generico da 2, asi que la
  guarda VIEJA, que tomaba la cita ALFABETICAMENTE primera, cotejaba 2 contra 2
  y daba VERDE sobre una cifra FALSA. Esta mutacion corre la version VIEJA
  (sacada de git, no descrita de palabra) para ENSENAR el falso verde, y la
  version reparada para ensenar el ROJO. El defecto 2 no solo tiraba cifras
  correctas: tambien dejaba pasar incorrectas.

  MUTACION D, LAS VIEJAS SIGUEN EN PIE. Se recorren las tres mutaciones de la
  vuelta 135 y la de la 133 contra la guarda reparada.

Salida: docs/loop/SALIDA_V137_1C_MUTACION.txt

USO:
  python scripts/loop/vuelta137_1c_mutacion.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_cifras_del_reporte.py")
SALIDA = os.path.join(LOOP, "SALIDA_V137_1C_MUTACION.txt")

# El ultimo commit ANTES de la reparacion 1.c (la TAREA 1.b de esta vuelta).
COMMIT_VIEJO = "ebdb7962"

PROPIO = "SALIDA_V135_4B_PELDANOS.txt"
VECINO = "SALIDA_V133_2E_MUTACION.txt"

VIEJAS = [
    "vuelta133_tarea2e_mutacion_cifras.py",
    "vuelta135_2e_mutacion_1.py",
    "vuelta135_2e_mutacion_2.py",
    "vuelta135_2e_mutacion_3.py",
]


def correr_guarda(texto, guarda=None):
    guarda = guarda or GUARDA
    fd, tmp = tempfile.mkstemp(suffix=".md", prefix="REPORTE_V137_1C_MUT_")
    os.close(fd)
    try:
        with io.open(tmp, "w", encoding="utf-8") as f:
            f.write(texto)
        r = subprocess.run([sys.executable, guarda, "--reporte", tmp],
                           capture_output=True, text=True, cwd=RAIZ)
    finally:
        os.remove(tmp)
    return r


def bloque(lineas, titulo, texto, r, espera_rojo, nota=""):
    lineas.append("=== %s" % titulo)
    if nota:
        lineas.append(nota)
    lineas.append("--- reporte de prueba ---")
    lineas.append(texto.strip())
    lineas.append("--- salida ---")
    lineas.append(r.stdout.rstrip())
    if r.stderr.strip():
        lineas.append(r.stderr.rstrip())
    lineas.append("EXITCODE: %d" % r.returncode)
    ok = (r.returncode == 1) if espera_rojo else (r.returncode == 0)
    lineas.append("%s: %s" % (titulo.split(",")[0],
                             "VERIFICADA" if ok else "NO VERIFICADA"))
    lineas.append("")
    return ok


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    lineas = ["PRUEBAS POR MUTACION DE LAS DOS REPARACIONES 1.c (vuelta 137)", ""]

    txt_a = ("# prueba\n\nLa tabla de peldanos (`%s`) deja 38 grafias sin agrupar.\n" % PROPIO)
    a = bloque(lineas, "MUTACION A, la cifra equivocada por uno (37 a 38)",
               txt_a, correr_guarda(txt_a), True)

    txt_b = ("# prueba\n\nLa tabla de peldanos (`%s`) deja 92 grafias sin agrupar.\n" % PROPIO)
    b = bloque(lineas, "MUTACION B, la cifra de la etiqueta VECINA del mismo fichero",
               txt_b, correr_guarda(txt_b), True,
               "92 es una cifra REAL de ese fichero, pero de la etiqueta 'grafias en "
               "grupo', no de 'grafias sin agrupar'. Si el camino fuerte se degradara al "
               "debil, esta saldria VERDE.")

    txt_c = ("# prueba\n\nLa tabla de peldanos (`%s`) deja 2 grafias en grupo.\n"
             "La mutacion de la vuelta 133 (`%s`) quedo verificada aparte.\n" % (PROPIO, VECINO))

    # La version VIEJA, sacada de git: se ENSENA el falso verde, no se describe.
    fd, guarda_vieja = tempfile.mkstemp(suffix=".py", prefix="guarda_vieja_1c_",
                                        dir=os.path.dirname(GUARDA))
    os.close(fd)
    try:
        rv = subprocess.run(["git", "show", "%s:scripts/loop/verificar_cifras_del_reporte.py"
                             % COMMIT_VIEJO], capture_output=True, text=True, cwd=RAIZ)
        with io.open(guarda_vieja, "w", encoding="utf-8") as f:
            f.write(rv.stdout)
        r_vieja = correr_guarda(txt_c, guarda_vieja)
    finally:
        os.remove(guarda_vieja)

    lineas.append("=== MUTACION C, el FALSO VERDE que el defecto 2 permitia")
    lineas.append("La cifra '2 grafias en grupo' es FALSA para su propio fichero (%s dice 92),"
                  % PROPIO)
    lineas.append("pero coincide con el recuento generico del fichero VECINO (%s)." % VECINO)
    lineas.append("--- reporte de prueba ---")
    lineas.append(txt_c.strip())
    lineas.append("--- salida de la guarda VIEJA (git show %s) ---" % COMMIT_VIEJO)
    lineas.append(r_vieja.stdout.rstrip())
    lineas.append("EXITCODE viejo: %d" % r_vieja.returncode)
    r_nueva = correr_guarda(txt_c)
    lineas.append("--- salida de la guarda REPARADA ---")
    lineas.append(r_nueva.stdout.rstrip())
    lineas.append("EXITCODE nuevo: %d" % r_nueva.returncode)
    c = (r_vieja.returncode == 0 and r_nueva.returncode == 1)
    lineas.append("MUTACION C: %s" % (
        "VERIFICADA: la vieja daba VERDE sobre una cifra falsa y la reparada cae ROJO"
        if c else "NO VERIFICADA (viejo EXIT %d, nuevo EXIT %d)"
        % (r_vieja.returncode, r_nueva.returncode)))
    lineas.append("")

    lineas.append("=== MUTACION D, las mutaciones VIEJAS contra la guarda reparada")
    lineas.append("Se distingue LA GUARDA NO MORDIO (fallo de verdad) de ANCLA PERDIDA (la")
    lineas.append("mutacion no llega a correr porque el texto que buscaba en REPORTE.md ya no")
    lineas.append("esta: REPORTE.md se sobreescribe cada vuelta). Un EXIT 1 por ancla perdida")
    lineas.append("NO es un fallo de la guarda, y contarlo como tal seria mentir en la otra")
    lineas.append("direccion. Ver el hallazgo lateral en el reporte de la vuelta 137.")
    d = True
    ancla_perdida = []
    for script in VIEJAS:
        r = subprocess.run([sys.executable, os.path.join(RAIZ, "scripts", "loop", script)],
                           capture_output=True, text=True, cwd=RAIZ)
        salida = (r.stdout or "") + (r.stderr or "")
        if r.returncode == 0:
            estado = "OK, la guarda mordio como se esperaba"
        elif "ROJO PREVIO" in salida:
            estado = "ANCLA PERDIDA, no llega a probar la guarda: %s" % salida.strip().splitlines()[0]
            ancla_perdida.append(script)
        else:
            estado = "FALLO: la guarda NO mordio"
            d = False
        lineas.append("  %s: EXIT %d, %s" % (script, r.returncode, estado))
    lineas.append("MUTACION D: %s" % (
        "VERIFICADA (ninguna mutacion vieja acusa a la guarda)" if d
        else "NO VERIFICADA"))
    if ancla_perdida:
        lineas.append("HALLAZGO LATERAL, DECLARADO: %d de las %d mutaciones viejas no pueden "
                      "correr hoy" % (len(ancla_perdida), len(VIEJAS)))
        lineas.append("  (%s)." % ", ".join(ancla_perdida))
        lineas.append("  Estan ancladas a un literal del REPORTE.md de la vuelta 134, que se")
        lineas.append("  sobreescribio. El docstring de verificar_cifras_del_reporte.py las")
        lineas.append("  sigue nombrando 'PRUEBA DE MUTACION (obligatoria)'. Medido: fallan")
        lineas.append("  IGUAL contra la guarda VIEJA (comprobado en la vuelta 137 con git")
        lineas.append("  stash), asi que NO es una regresion de esta reparacion. No las toco:")
        lineas.append("  re-anclarlas es una operacion sobre instrumentos sellados que este")
        lineas.append("  encargo no pide. Queda DISCUTIBLE en el reporte.")
    lineas.append("")

    todas = a and b and c and d
    lineas.append("RESUMEN: A %s / B %s / C %s / D %s" % (
        "OK" if a else "FALLO", "OK" if b else "FALLO",
        "OK" if c else "FALLO", "OK" if d else "FALLO"))
    lineas.append("EXITCODE: %d" % (0 if todas else 1))

    texto = "\n".join(lineas) + "\n"
    with io.open(SALIDA, "w", encoding="utf-8") as f:
        f.write(texto)
    print(texto)
    return 0 if todas else 1


if __name__ == "__main__":
    raise SystemExit(main())
