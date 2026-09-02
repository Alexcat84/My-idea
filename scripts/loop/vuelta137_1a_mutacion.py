# -*- coding: utf-8 -*-
"""vuelta137_1a_mutacion.py . TAREA 1.a de la vuelta 137: las pruebas por
mutacion de la reparacion de verificar_cabecera_mapeo.py (parada del 29 ago
2026, puntos 1 y 2).

EJECUTOR regla 1, EL CASO ROJO SE PRUEBA POR MUTACION: las tres se corren
sobre variables QUE EL CODIGO COMPUTA, ninguna sobre un literal.

  MUTACION A, EL SELLO ES REAL, NO DECORADO. Se le cambia a la guarda el arbol
  contra el que recomputa (--sello al commit de DESPUES de la escritura de
  OP-S-11) y se comprueba que CAE ROJO con los seis peldanos en 54. Lo que se
  muta es el arbol de entrada; lo que se observa es `rec["peldanos"]`, que la
  guarda COMPUTA corriendo el union-find sobre ese arbol. Si el recomputo
  estuviera clavado a una constante, esta mutacion saldria verde y la
  reparacion seria decorativa.

  MUTACION B, LA CABECERA SIGUE VIGILADA. La de la vuelta 135 (borrar el
  peldano `**54 grupos**` de una copia de la tabla) tiene que seguir cayendo
  ROJO nombrandolo: la reparacion fija el arbol, NO afloja la comparacion.

  MUTACION C, LA PROTECCION DEL SEGUNDO FICHERO ES REAL. Se corre el script de
  recomputo POR SU CUENTA (sin la guarda, o sea sin la foto y restauracion) y
  se comprueba que SI ensucia docs/loop/SALIDA_V135_4B_PELDANOS.txt; luego se
  restaura y se corre la guarda, que NO lo ensucia. El control positivo es
  necesario: sin el, un fichero limpio no prueba que la lista protege nada,
  solo que nadie escribio.

Salida: docs/loop/SALIDA_V137_1A_MUTACION.txt

USO:
  python scripts/loop/vuelta137_1a_mutacion.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
GUARDA = os.path.join(LOOP, "verificar_cabecera_mapeo.py")
RECOMPUTO = os.path.join(LOOP, "vuelta135_tabla_mapeo_propuesto.py")
TABLA_REAL = os.path.join(RAIZ, "docs", "plan", "OP_S_11_MAPEO_PROPUESTO.md")
PELDANOS = os.path.join(RAIZ, "docs", "loop", "SALIDA_V135_4B_PELDANOS.txt")
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V137_1A_MUTACION.txt")

# El commit de DESPUES de la escritura de OP-S-11 (vuelta 136, TAREA 3.e), que
# es el arbol cuyo censo ya esta canonizado y por tanto colapsa a 54.
SELLO_DESPUES = "9f9e6892f8c5852cad618f447dd29e8f1c6acd0b"

VIEJO = "usa la cola, agrupamiento POR IGUALDAD y PREFIJO sobre la recortada: **54 grupos**."
NUEVO = "usa la cola, agrupamiento POR IGUALDAD y PREFIJO sobre la recortada."


def correr(*args):
    return subprocess.run([sys.executable] + list(args),
                          capture_output=True, text=True, cwd=RAIZ)


def leer_bytes(ruta):
    with io.open(ruta, "rb") as f:
        return f.read()


def mutacion_a(lineas):
    lineas.append("=== MUTACION A: se le fija a la guarda el arbol de DESPUES de la escritura")
    lineas.append("    (--sello %s) en vez del sello de apertura." % SELLO_DESPUES)
    r = correr(GUARDA, "--sello", SELLO_DESPUES)
    lineas.append("--- salida ---")
    lineas.append(r.stdout.rstrip())
    if r.stderr.strip():
        lineas.append(r.stderr.rstrip())
    lineas.append("EXITCODE: %d" % r.returncode)
    ok = (r.returncode == 1 and "peldanos [54, 54, 54, 54, 54, 54]" in r.stdout)
    lineas.append("MUTACION A %s: la guarda cae ROJO y sus seis peldanos recomputados salen"
                  % ("VERIFICADA" if ok else "NO VERIFICADA"))
    lineas.append("  [54,54,54,54,54,54] sobre ese arbol, o sea que el recomputo SIGUE al arbol")
    lineas.append("  que se le fija y no es una constante." if ok else
                  "  ESPERADO Y NO OBTENIDO.")
    lineas.append("")
    return ok


def mutacion_b(lineas):
    lineas.append("=== MUTACION B: sobre copia de la tabla real se BORRA el peldano")
    lineas.append("    '**54 grupos**' de la cabecera (la mutacion de la vuelta 135).")
    with io.open(TABLA_REAL, encoding="utf-8") as f:
        texto = f.read()
    if texto.count(VIEJO) != 1:
        lineas.append("ROJO PREVIO: el ancla del peldano 6 no aparece exactamente una vez.")
        lineas.append("")
        return False
    fd, tmp = tempfile.mkstemp(suffix=".md", prefix="OP_S_11_MUTADO_137_1A_")
    os.close(fd)
    try:
        with io.open(tmp, "w", encoding="utf-8") as f:
            f.write(texto.replace(VIEJO, NUEVO))
        r = correr(GUARDA, "--tabla", tmp)
        lineas.append("--- salida ---")
        lineas.append(r.stdout.rstrip())
        if r.stderr.strip():
            lineas.append(r.stderr.rstrip())
        lineas.append("EXITCODE: %d" % r.returncode)
        ok = (r.returncode == 1 and "peldano 54" in r.stdout)
    finally:
        os.remove(tmp)
    lineas.append("MUTACION B %s: la guarda sigue nombrando el peldano 54 que falta."
                  % ("VERIFICADA" if ok else "NO VERIFICADA"))
    lineas.append("")
    return ok


def mutacion_c(lineas):
    lineas.append("=== MUTACION C: control positivo de la proteccion del segundo fichero.")
    antes = leer_bytes(PELDANOS)

    r = correr(RECOMPUTO)
    sucio_sin_guarda = (leer_bytes(PELDANOS) != antes)
    lineas.append("corrido el recomputo POR SU CUENTA (sin la guarda, EXIT %d):" % r.returncode)
    lineas.append("  SALIDA_V135_4B_PELDANOS.txt %s" %
                  ("CAMBIA (control positivo: hay quien lo escriba)" if sucio_sin_guarda
                   else "NO cambia (control positivo FALLIDO)"))

    # Se restauran los DOS ficheros que el recomputo suelto acaba de escribir.
    with io.open(PELDANOS, "wb") as f:
        f.write(antes)
    subprocess.run(["git", "checkout", "--", "docs/plan/OP_S_11_MAPEO_PROPUESTO.md"], cwd=RAIZ)

    antes2 = leer_bytes(PELDANOS)
    r2 = correr(GUARDA)
    limpio_con_guarda = (leer_bytes(PELDANOS) == antes2)
    lineas.append("corrida la GUARDA (EXIT %d):" % r2.returncode)
    lineas.append("  SALIDA_V135_4B_PELDANOS.txt %s" %
                  ("NO cambia: la lista de ficheros protegidos lo cubre"
                   if limpio_con_guarda else "CAMBIA: la proteccion NO funciona"))
    ok = sucio_sin_guarda and limpio_con_guarda
    lineas.append("MUTACION C %s." % ("VERIFICADA" if ok else "NO VERIFICADA"))
    lineas.append("")
    return ok


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    lineas = ["PRUEBAS POR MUTACION DE LA REPARACION 1.a (vuelta 137)", ""]
    a = mutacion_a(lineas)
    b = mutacion_b(lineas)
    c = mutacion_c(lineas)
    todas = a and b and c
    lineas.append("RESUMEN: A %s / B %s / C %s" %
                  ("OK" if a else "FALLO", "OK" if b else "FALLO", "OK" if c else "FALLO"))
    lineas.append("EXITCODE: %d" % (0 if todas else 1))
    texto = "\n".join(lineas) + "\n"
    with io.open(SALIDA, "w", encoding="utf-8") as f:
        f.write(texto)
    print(texto)
    return 0 if todas else 1


if __name__ == "__main__":
    raise SystemExit(main())
