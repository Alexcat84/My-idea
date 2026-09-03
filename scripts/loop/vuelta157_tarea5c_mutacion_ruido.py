# -*- coding: utf-8 -*-
"""vuelta157_tarea5c_mutacion_ruido.py . TAREA 5.c DE LA VUELTA 157.

EL CASO POSITIVO POR MUTACION DE LA ADJUDICACION 6.9 DEL ACTA 157, y su sujeto
NO ES INVENTADO: es la caida 2 del auditor, sellada en
`docs/loop/_auditor_v157_mutaciones.txt` (la roja) y
`_auditor_v157_mutaciones2.txt` (la verde).

EL ESCENARIO, RECONSTRUIDO EN UN DIRECTORIO TEMPORAL Y SIN TOCAR `docs/loop/`:
un script de mentira que escribe SIEMPRE su propia salida sellada y SIEMPRE
IGUAL, y que en su SEGUNDA invocacion ve aparecer al lado un `.txt` que EL NO
ESCRIBE. Eso es exactamente lo que le paso al auditor: dos ficheros suyos
nacidos ENTRE las dos corridas de la bateria, colgados a dos scripts que la
propia salida declaraba como "salidas selladas que escribe: ninguna".

  El vecino se escribe desde el propio proceso de mentira porque es la unica
  forma determinista de hacerlo aparecer ENTRE las dos corridas; para
  `correr_dos_veces` es indistinguible de un fichero de otro proceso, porque lo
  unico que esa funcion puede ver es que en la corrida 1 NO estaba en `escritos`
  y en la corrida 2 apareció. El contador vive en un fichero que NO es `.txt`,
  asi que `estado_de` no lo mira y no ensucia la medicion.

LAS DOS MITADES QUE EL ENCARGO PIDE, Y LAS DOS SE MIDEN:
  (A) LA GUARDA NUEVA SALE VERDE NOMBRANDO EL RUIDO APARTE: `inestables` VACIA y
      `ruido` con el vecino dentro. Ningun script cae en NO REPRODUCIBLE.
  (B) LA VIEJA, SACADA DEL COMMIT DE APERTURA DE ESTA VUELTA, SIGUE SALIENDO
      ROJA: su `correr_dos_veces` se importa con `git show` del commit del acta
      157 y sobre EL MISMO escenario devuelve `inestables` NO VACIA. No se
      teclea su comportamiento: se corre.
  (C) Y ADEMAS, en la version nueva y en el mismo proceso, `cenir=False`
      reproduce el comportamiento viejo y tambien sale ROJO. Es la contraprueba
      barata de que la unica diferencia es el cenido.
  (D) LAS 23 SIGUEN SIENDO 23: `len(VIEJAS)` se cuenta, no se teclea.

PRUEBA DE MUTACION DE ESTE MISMO CASO (regla del ejecutor, 29 ago 2026): con
`--mutar` se le da la vuelta al valor esperado de (A) y esta guarda tiene que
CAER con exit 1. Ninguno de los veredictos es una constante literal.

USO:  python scripts/loop/vuelta157_tarea5c_mutacion_ruido.py
      python scripts/loop/vuelta157_tarea5c_mutacion_ruido.py --mutar
"""
import argparse
import importlib.util
import io
import os
import shutil
import subprocess
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUARDA_REL = "scripts/loop/verificar_mutaciones_viejas.py"
GUARDA = os.path.join(RAIZ, GUARDA_REL)

SCRIPT_CON_VECINO = r'''# -*- coding: utf-8 -*-
"""Script de mentira. Escribe SIEMPRE su propia salida sellada y SIEMPRE IGUAL.
En su SEGUNDA invocacion escribe ademas un .txt que en la primera no existia:
ese es el vecino que no es suyo a ojos de `correr_dos_veces`, porque no estaba
en `escritos`. El contador NO es .txt, asi que `estado_de` no lo mira."""
import io, os
d = os.path.dirname(os.path.abspath(__file__))
c = os.path.join(d, "contador.dat")
n = int(io.open(c).read().strip()) + 1 if os.path.exists(c) else 1
io.open(c, "w").write(str(n))
io.open(os.path.join(d, "SALIDA_PROPIA_SELLADA.txt"), "w",
        encoding="utf-8", newline="\n").write("linea estable\nsiempre la misma\n")
if n >= 2:
    io.open(os.path.join(d, "_vecino_de_otro.txt"), "w",
            encoding="utf-8", newline="\n").write("nacido en la corrida %d\n" % n)
'''


def importar(ruta, nombre):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def commit_de_apertura():
    """El commit del acta 157, leido de git y NO tecleado (regla LA IDENTIDAD SE
    LEE DE GIT)."""
    r = subprocess.run(["git", "log", "--format=%H", "-1",
                        "--grep=^ACTA DE LA VUELTA 157 DEL AUDITOR"],
                       cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", "replace").strip()


def montar_escenario(tmp):
    io.open(os.path.join(tmp, "script_con_vecino.py"), "w", encoding="utf-8",
            newline="\n").write(SCRIPT_CON_VECINO)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar", action="store_true",
                    help="le da la vuelta al valor esperado de (A): tiene que salir ROJO")
    a = ap.parse_args()

    print("=" * 78)
    print("VUELTA 157, TAREA 5.c: CASO POSITIVO POR MUTACION DEL RUIDO DE CONCURRENCIA")
    print("=" * 78)
    print("")

    nueva = importar(GUARDA, "guarda_nueva")
    print("  CIFRA mutaciones en la nomina VIEJAS (contadas, no tecleadas): %d"
          % len(nueva.VIEJAS))
    las_23 = len(nueva.VIEJAS) == 23
    print("  (D) LAS 23 SIGUEN SIENDO 23: %s" % las_23)
    print("")

    apertura = commit_de_apertura()
    if not apertura:
        print("ROJO PREVIO: no se pudo leer de git el commit del acta 157.")
        print("FIN")
        return 1
    print("  commit de apertura, leido de git log: %s" % apertura)

    tmp_viejo = tempfile.mkdtemp(prefix="v157_5c_vieja_")
    ruta_vieja = os.path.join(tmp_viejo, "guarda_vieja.py")
    r = subprocess.run(["git", "show", "%s:%s" % (apertura, GUARDA_REL)],
                       cwd=RAIZ, capture_output=True)
    if r.returncode:
        shutil.rmtree(tmp_viejo, ignore_errors=True)
        print("ROJO PREVIO: no se pudo sacar la guarda vieja del commit de apertura.")
        print("FIN")
        return 1
    io.open(ruta_vieja, "wb").write(r.stdout)
    vieja = importar(ruta_vieja, "guarda_vieja")
    print("  guarda VIEJA importada del commit de apertura, %d bytes" % len(r.stdout))
    print("  la vieja trae el parametro `cenir`: %s"
          % ("cenir" in vieja.correr_dos_veces.__code__.co_varnames))
    print("")

    resultados = {}
    try:
        # (A) LA NUEVA, CENIDA
        tmp = tempfile.mkdtemp(prefix="v157_5c_nueva_")
        try:
            montar_escenario(tmp)
            salida = nueva.correr_dos_veces("script_con_vecino.py", tmp, base=tmp)
            _c, _s, escritos, inestables, ruido = salida
            resultados["A_escritos"] = escritos
            resultados["A_inestables"] = [x[0] for x in inestables]
            resultados["A_ruido"] = [x[0] for x in ruido]
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

        # (C) LA NUEVA CON cenir=False, o sea el comportamiento viejo en proceso
        tmp = tempfile.mkdtemp(prefix="v157_5c_cenir_")
        try:
            montar_escenario(tmp)
            _c, _s, esc2, inest2, ruido2 = nueva.correr_dos_veces(
                "script_con_vecino.py", tmp, base=tmp, cenir=False)
            resultados["C_inestables"] = [x[0] for x in inest2]
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

        # (B) LA VIEJA DE VERDAD, SACADA DEL COMMIT DE APERTURA
        tmp = tempfile.mkdtemp(prefix="v157_5c_viejo_")
        try:
            montar_escenario(tmp)
            _c, _s, esc3, inest3 = vieja.correr_dos_veces(
                "script_con_vecino.py", tmp, base=tmp)
            resultados["B_escritos"] = esc3
            resultados["B_inestables"] = [x[0] for x in inest3]
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    finally:
        shutil.rmtree(tmp_viejo, ignore_errors=True)
        print("  P.16, QUIEN FABRICA LIMPIA: los directorios temporales se retiran.")
        print("")

    print("(A) LA GUARDA NUEVA, CENIDA A LO QUE EL SCRIPT ESCRIBE")
    print("    salidas selladas que ESCRIBE (corrida 1) : %s"
          % (", ".join(resultados["A_escritos"]) or "ninguna"))
    print("    CIFRA inestables (rojo del script)       : %d (%s)"
          % (len(resultados["A_inestables"]),
             ", ".join(resultados["A_inestables"]) or "ninguno"))
    print("    CIFRA ruido de concurrencia (aparte)     : %d (%s)"
          % (len(resultados["A_ruido"]), ", ".join(resultados["A_ruido"]) or "ninguno"))
    a_ok = (not resultados["A_inestables"]) and resultados["A_ruido"] == ["_vecino_de_otro.txt"]
    print("    VEREDICTO (A): %s"
          % ("VERDE, y el ruido va nombrado APARTE" if a_ok else "NO SE COMPORTA"))
    print("")

    print("(B) LA GUARDA VIEJA, SACADA DEL COMMIT DE APERTURA %s" % apertura[:8])
    print("    salidas selladas que ESCRIBE (corrida 1) : %s"
          % (", ".join(resultados["B_escritos"]) or "ninguna"))
    print("    CIFRA inestables que le cuelga al script : %d (%s)"
          % (len(resultados["B_inestables"]),
             ", ".join(resultados["B_inestables"]) or "ninguno"))
    b_ok = resultados["B_inestables"] == ["_vecino_de_otro.txt"]
    print("    VEREDICTO (B): %s"
          % ("SIGUE SALIENDO ROJA, y acusa a quien no fue" if b_ok else "NO SE COMPORTA"))
    print("    Y ESTE ES EL DEFECTO ENTERO EN UNA LINEA: el fichero que la vieja le")
    print("    cuelga al script NO ESTA en la lista de lo que el script escribe.")
    print("")

    print("(C) LA NUEVA CON cenir=False, o sea el comportamiento viejo en proceso")
    print("    CIFRA inestables: %d (%s)"
          % (len(resultados["C_inestables"]),
             ", ".join(resultados["C_inestables"]) or "ninguno"))
    c_ok = resultados["C_inestables"] == ["_vecino_de_otro.txt"]
    print("    VEREDICTO (C): %s" % ("ROJO, como la vieja" if c_ok else "NO SE COMPORTA"))
    print("")

    esperado_a = True
    if a.mutar:
        esperado_a = False
        print("  MUTACION ACTIVA: se le da la vuelta al valor esperado de (A). Ahora se")
        print("  exige que la guarda NUEVA siga colgandole el vecino al script, que es")
        print("  falso, y este caso tiene que CAER. Si no cae, no probaba nada.")
        print("")

    print("  (A) esperado %s, medido %s" % (esperado_a, a_ok))
    print("  (B) esperado True, medido %s" % b_ok)
    print("  (C) esperado True, medido %s" % c_ok)
    print("  (D) esperado True, medido %s" % las_23)
    print("")
    if (a_ok == esperado_a) and b_ok and c_ok and las_23:
        print("VERDE: sobre el mismo escenario la guarda vieja acusa al script equivocado y")
        print("la nueva sale limpia nombrando el ruido aparte. Y las 23 siguen siendo 23.")
        print("FIN")
        return 0
    print("ROJO: alguna de las cuatro condiciones no se cumple.")
    print("FIN")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
