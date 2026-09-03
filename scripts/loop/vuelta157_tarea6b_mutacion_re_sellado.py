# -*- coding: utf-8 -*-
"""vuelta157_tarea6b_mutacion_re_sellado.py . TAREA 6.b DE LA VUELTA 157.

EL CASO POSITIVO POR MUTACION DE `scripts/loop/verificar_re_sellado.py`
(adjudicacion 6.10 del acta 157), Y SU SUJETO ES REAL, NO FABRICADO: el fichero
que el auditor pillo re sellado en silencio, `SALIDA_V156_T4C_CIFRAS.txt`.

EJERCE EL CODIGO DE LA GUARDA, NO UNA COPIA: importa `analizar` y
`las_que_faltan` del propio fichero de la guarda y los llama.

LAS CUATRO COMPROBACIONES:
  (A) EL SUJETO ESTA RE SELLADO DE VERDAD. `analizar` sobre el fichero del
      auditor tiene que devolver estado RE SELLADO, con su commit de tarea leido
      de git, su numstat computado y su lista de lineas CIFRA movidas.
  (B) CASO ROJO. Un texto de reporte que CITA el fichero pero NO trae la linea
      declarada tiene que dejar UNA fila sin declarar.
  (C) CASO VERDE. El MISMO texto mas la linea que la guarda computo tiene que
      dejar CERO filas sin declarar. La linea no se teclea aqui: se toma de lo
      que devuelve `analizar`.
  (D) CONTROL: un fichero SIN RE SELLAR (elegido POR COMPUTO, recorriendo
      docs/loop/ hasta encontrar el primero) NO puede ser rojo ni aunque el
      reporte no diga nada de el. Una guarda que tambien acusa a los limpios no
      sirve.

PRUEBA DE MUTACION DE ESTE MISMO CASO (regla del ejecutor, 29 ago 2026): con
`--mutar` se le da la vuelta al valor esperado de (B) (se exige que el caso rojo
salga limpio) y esto tiene que CAER con exit 1.

USO:  python scripts/loop/vuelta157_tarea6b_mutacion_re_sellado.py
      python scripts/loop/vuelta157_tarea6b_mutacion_re_sellado.py --mutar
"""
import argparse
import importlib.util
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_re_sellado.py")
DOCS_LOOP = os.path.join(RAIZ, "docs", "loop")

SUJETO = "docs/loop/SALIDA_V156_T4C_CIFRAS.txt"


def importar():
    spec = importlib.util.spec_from_file_location("guarda_re_sellado", GUARDA)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def primer_limpio(mod):
    """UN fichero SIN RE SELLAR, elegido por COMPUTO recorriendo docs/loop/ en
    orden. No se teclea ninguno: el dia que ese fichero cambie, este caso
    escoge otro solo."""
    for n in sorted(os.listdir(DOCS_LOOP)):
        if not (n.startswith("SALIDA_") and n.endswith(".txt")):
            continue
        f = mod.analizar("docs/loop/%s" % n)
        if f["estado"] == "SIN RE SELLAR":
            return f
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar", action="store_true",
                    help="le da la vuelta al valor esperado de (B): tiene que salir ROJO")
    a = ap.parse_args()

    print("=" * 78)
    print("VUELTA 157, TAREA 6.b: CASO POSITIVO POR MUTACION DE verificar_re_sellado.py")
    print("=" * 78)
    print("")

    mod = importar()
    print("  guarda importada de: scripts/loop/verificar_re_sellado.py")
    print("  sujeto (el fichero que el auditor pillo): %s" % os.path.basename(SUJETO))
    print("")

    print("(A) EL SUJETO ESTA RE SELLADO DE VERDAD?")
    f = mod.analizar(SUJETO)
    print("    estado             : %s" % f["estado"])
    a_ok = f["estado"] == "RE SELLADO"
    if a_ok:
        print("    commit de su tarea : %s" % f["tarea"][:12])
        print("    numstat contra HEAD: +%d/-%d" % (f["mas"], f["menos"]))
        print("    CIFRA lineas CIFRA cuyo VALOR cambio: %d" % len(f["movidas"]))
        for k in f["movidas"]:
            print("       %s: %r -> %r"
                  % (k, f["antes"].get(k, "(no estaba)"), f["despues"].get(k, "(ya no esta)")))
        print("    la linea que la guarda EXIGE, computada:")
        print("       %s" % f["linea"])
    print("    VEREDICTO (A): %s" % ("RE SELLADO, el sujeto sirve" if a_ok else "NO SIRVE"))
    print("")
    if not a_ok:
        print("ROJO PREVIO: el sujeto ya no esta re sellado y este caso no puede probar nada.")
        print("FIN")
        return 1

    texto_sin = ("REPORTE DE MENTIRA. Cita %s y no declara nada de el.\n"
                 % os.path.basename(SUJETO))
    texto_con = texto_sin + f["linea"] + "\n"

    print("(B) CASO ROJO: el reporte lo cita y NO lo declara")
    faltan_sin = mod.las_que_faltan([f], texto_sin)
    print("    CIFRA filas sin declarar: %d (%s)"
          % (len(faltan_sin),
             ", ".join(os.path.basename(x["fichero"]) for x in faltan_sin) or "ninguna"))
    b_ok = len(faltan_sin) == 1
    print("    VEREDICTO (B): %s" % ("ROJO, como tiene que ser" if b_ok else "NO MUERDE"))
    print("")

    print("(C) CASO VERDE: el mismo reporte MAS la linea que la guarda computo")
    faltan_con = mod.las_que_faltan([f], texto_con)
    print("    CIFRA filas sin declarar: %d" % len(faltan_con))
    c_ok = len(faltan_con) == 0
    print("    VEREDICTO (C): %s" % ("VERDE" if c_ok else "SIGUE ROJO Y NO DEBERIA"))
    print("")

    print("(D) CONTROL: un fichero SIN RE SELLAR no puede ser rojo")
    limpio = primer_limpio(mod)
    if limpio is None:
        print("    ROJO PREVIO: no se encontro en docs/loop/ ningun SALIDA_* sin re sellar.")
        print("FIN")
        return 1
    print("    elegido por computo: %s (%s)"
          % (os.path.basename(limpio["fichero"]), limpio["estado"]))
    faltan_limpio = mod.las_que_faltan([limpio], texto_sin)
    print("    CIFRA filas sin declarar: %d" % len(faltan_limpio))
    d_ok = len(faltan_limpio) == 0
    print("    VEREDICTO (D): %s" % ("no lo acusa" if d_ok else "ACUSA A UN LIMPIO"))
    print("")

    esperado_b = True
    if a.mutar:
        esperado_b = False
        print("  MUTACION ACTIVA: se le da la vuelta al valor esperado de (B). Ahora se")
        print("  exige que el caso ROJO salga limpio, que es falso, y esto tiene que CAER.")
        print("")

    print("  (A) esperado True, medido %s" % a_ok)
    print("  (B) esperado %s, medido %s" % (esperado_b, b_ok))
    print("  (C) esperado True, medido %s" % c_ok)
    print("  (D) esperado True, medido %s" % d_ok)
    print("")
    if a_ok and (b_ok == esperado_b) and c_ok and d_ok:
        print("VERDE: sobre el fichero que el auditor pillo, la guarda muerde cuando el")
        print("reporte calla, calla cuando el reporte declara, y no acusa a los limpios.")
        print("FIN")
        return 0
    print("ROJO: alguna de las cuatro condiciones no se cumple.")
    print("FIN")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
