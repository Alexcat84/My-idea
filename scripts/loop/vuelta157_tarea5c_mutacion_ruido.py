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
  (D) LA NOMINA NO MENGUA: las entradas que la guarda tenia en el commit de
      apertura de la vuelta 157 siguen TODAS dentro de la de hoy. Se mide
      por contencion contra un ref fijo y computado, no contra un literal.

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
    print("  (D) se mide mas abajo, con la nomina del commit de apertura delante.")
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

    # --- (D), ARREGLADO EN LA VUELTA 164, TAREA 2.a ---------------------------
    #
    # LO QUE HABIA AQUI, Y NO SE BORRA: `las_23 = len(nueva.VIEJAS) == 23`, una
    # CONSTANTE LITERAL comparada contra el tamano de la nomina. Caduco el dia que
    # la vuelta 163 hizo crecer la nomina de 23 a 51 por la adjudicacion 6.8 del
    # acta 162, o sea que este caso llevaba ROJO desde entonces y nadie lo vio
    # porque la bateria de la 163 nunca termino (acta 163, seccion 5.3). Hoy la
    # nomina tiene mas todavia y seguia rojo. Es la misma enfermedad de siempre:
    # un esperado clavado a un estado que otra vuelta mueve legitimamente.
    #
    # QUE QUERIA DECIR DE VERDAD, Y ES LO QUE SE MIDE AHORA: que LA NOMINA NO
    # MENGUA. Una nomina que encoge es una guarda que dejo de mirar, y eso si es
    # rojo; que crezca es exactamente lo que la regla de la vuelta 144 manda. Se
    # mide como CONTENCION contra un REF FIJO Y COMPUTADO: las entradas que la
    # guarda tenia EN EL COMMIT DE APERTURA DE LA VUELTA 157 (que son las 23 de
    # entonces, leidas de git y no tecleadas) tienen que seguir TODAS dentro de la
    # nomina de hoy. No puede volver a caducar por crecer.
    originales = [s for s, _a in vieja.VIEJAS]
    hoy = {s for s, _a in nueva.VIEJAS}
    perdidas = sorted(s for s in originales if s not in hoy)
    las_23 = (not perdidas) and len(nueva.VIEJAS) >= len(originales)
    print("  (D) LA NOMINA NO MENGUA, MEDIDO CONTRA EL COMMIT DE APERTURA")
    print("      CIFRA entradas en la nomina DEL COMMIT DE APERTURA %s: %d"
          % (apertura[:8], len(originales)))
    print("      CIFRA entradas en la nomina DE HOY: %d" % len(nueva.VIEJAS))
    print("      CIFRA de las originales que YA NO ESTAN: %d (%s)"
          % (len(perdidas), ", ".join(perdidas) or "ninguna"))
    print("      (D) VEREDICTO: %s" % las_23)
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
        print("la nueva sale limpia nombrando el ruido aparte. Y LA NOMINA NO MENGUA:")
        print("ninguna de las entradas del commit de apertura se ha perdido.")
        print("FIN")
        return 0
    print("ROJO: alguna de las cuatro condiciones no se cumple.")
    print("FIN")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
