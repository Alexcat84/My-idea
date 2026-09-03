# -*- coding: utf-8 -*-
"""vuelta159_tarea6c_mutacion_exencion.py . TAREA 6.c DE LA VUELTA 159.

EL CASO POSITIVO POR MUTACION DE LA EXENCION DE LA ADJUDICACION 6.8 DEL ACTA
158, sobre `scripts/loop/verificar_re_sellado.py`.

QUE TIENE QUE PROBAR, Y ES LO QUE EL ENCARGO PIDE CON ESAS PALABRAS: "un fichero
de tarea NORMAL re sellado y no declarado TIENE QUE SEGUIR SALIENDO ROJO". O
sea: la exencion no puede haber apagado la guarda.

EJERCE EL CODIGO DE LA GUARDA, NO UNA COPIA: importa `analizar`, `es_exento`,
`exentos_de`, `linea_de_exencion` y `las_que_faltan` del propio fichero.

LOS SUJETOS SE ELIGEN POR COMPUTO, NO SE TECLEAN: se recorre `docs/loop/` en
orden y se toma el PRIMER `SALIDA_*.txt` RE SELLADO que NO sea exento (el sujeto
normal) y el PRIMER `SALIDA_*_RE_SELLADO.txt` o `SALIDA_*_CIFRAS_REPORTE.txt`
que este RE SELLADO (el sujeto exento). El dia que esos ficheros cambien, este
caso escoge otros solo.

LAS CUATRO COMPROBACIONES:
  (A) EL SUJETO NORMAL ESTA RE SELLADO Y NO ES EXENTO.
  (B) CASO ROJO, Y ES EL QUE EL ENCARGO EXIGE: un reporte que cita al sujeto
      NORMAL y no lo declara deja UNA fila sin declarar. LA EXENCION NO APAGO
      LA GUARDA.
  (C) CASO VERDE DE LA EXENCION: un reporte que cita al sujeto EXENTO y no lo
      declara deja CERO filas sin declarar, Y la linea de exencion computada
      NOMBRA ese fichero. Una exencion que no se imprime es un agujero.
  (D) CONTROL: el sujeto normal declarado con su linea deja CERO.

PRUEBA DE MUTACION DE ESTE MISMO CASO (regla del ejecutor, 29 ago 2026): con
`--mutar` se le da la vuelta al valor esperado de (B), se exige que el caso rojo
salga limpio, y esto TIENE QUE CAER con exit 1. Sin esa corrida, el caso rojo de
aqui seria un assert que se aprueba solo.

USO:  python scripts/loop/vuelta159_tarea6c_mutacion_exencion.py
      python scripts/loop/vuelta159_tarea6c_mutacion_exencion.py --mutar
"""
import argparse
import importlib.util
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_re_sellado.py")
DOCS_LOOP = os.path.join(RAIZ, "docs", "loop")


def importar():
    spec = importlib.util.spec_from_file_location("guarda_re_sellado", GUARDA)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def primero(mod, quiero_exento):
    for n in sorted(os.listdir(DOCS_LOOP)):
        if not (n.startswith("SALIDA_") and n.endswith(".txt")):
            continue
        if mod.es_exento(n) != quiero_exento:
            continue
        f = mod.analizar("docs/loop/%s" % n)
        if f["estado"] == "RE SELLADO":
            return f
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar", action="store_true",
                    help="le da la vuelta al valor esperado de (B): tiene que caer")
    a = ap.parse_args()

    print("=" * 78)
    print("VUELTA 159, TAREA 6.c: CASO POSITIVO POR MUTACION DE LA EXENCION 6.8")
    print("=" * 78)
    print("")
    mod = importar()
    print("  guarda importada de: scripts/loop/verificar_re_sellado.py")
    print("  patron de exencion declarado en la guarda: %s" % mod.PATRON_EXENTO.pattern)
    print("")

    normal = primero(mod, quiero_exento=False)
    exento = primero(mod, quiero_exento=True)

    print("(A) EL SUJETO NORMAL, ELEGIDO POR COMPUTO")
    if normal is None:
        print("    ROJO PREVIO: no hay ningun SALIDA_* NO exento RE SELLADO hoy.")
        print("    Este caso no puede probar nada y NO se aprueba solo.")
        print("FIN")
        return 1
    print("    fichero            : %s" % os.path.basename(normal["fichero"]))
    print("    estado             : %s" % normal["estado"])
    print("    es exento?         : %s" % mod.es_exento(normal["fichero"]))
    print("    commit de su tarea : %s" % normal["tarea"][:12])
    print("    numstat contra HEAD: +%d/-%d" % (normal["mas"], normal["menos"]))
    a_ok = normal["estado"] == "RE SELLADO" and not mod.es_exento(normal["fichero"])
    print("    VEREDICTO (A): %s" % ("sirve" if a_ok else "NO SIRVE"))
    print("")

    texto_sin = ("REPORTE DE MENTIRA. Cita %s y no declara nada de el.\n"
                 % os.path.basename(normal["fichero"]))
    print("(B) CASO ROJO: EL FICHERO NORMAL RE SELLADO Y NO DECLARADO SIGUE ROJO")
    faltan = mod.las_que_faltan([normal], texto_sin)
    print("    CIFRA filas sin declarar: %d (%s)"
          % (len(faltan),
             ", ".join(os.path.basename(x["fichero"]) for x in faltan) or "ninguna"))
    esperado_b = 0 if a.mutar else 1
    if a.mutar:
        print("    MUTADO: se exige 0 filas sin declarar, o sea que el caso rojo")
        print("    salga limpio. Si la guarda muerde, esto CAE, que es el punto.")
    b_ok = len(faltan) == esperado_b
    print("    esperado: %d, medido: %d" % (esperado_b, len(faltan)))
    print("    VEREDICTO (B): %s"
          % ("ROJO, la exencion NO apago la guarda" if b_ok and not a.mutar
             else ("CAE, como tiene que caer" if not b_ok and a.mutar else "NO MUERDE")))
    print("")

    print("(C) CASO VERDE DE LA EXENCION, Y CON SU LINEA IMPRESA")
    if exento is None:
        print("    NO HAY sujeto exento RE SELLADO hoy, y se dice en vez de fingirlo.")
        print("    La linea de exencion se computa igual sobre la lista vacia:")
        print("    %s" % mod.linea_de_exencion([]))
        c_ok = True
    else:
        print("    fichero            : %s" % os.path.basename(exento["fichero"]))
        print("    numstat contra HEAD: +%d/-%d" % (exento["mas"], exento["menos"]))
        texto_ex = ("REPORTE DE MENTIRA. Cita %s y no declara nada de el.\n"
                    % os.path.basename(exento["fichero"]))
        faltan_ex = mod.las_que_faltan([exento], texto_ex)
        linea = mod.linea_de_exencion([exento])
        print("    CIFRA filas sin declarar: %d" % len(faltan_ex))
        print("    linea de exencion computada:")
        print("       %s" % linea)
        c_ok = (len(faltan_ex) == 0
                and os.path.basename(exento["fichero"]) in linea)
        print("    VEREDICTO (C): %s"
              % ("EXENTO Y NOMBRADO" if c_ok else "LA EXENCION NO SE IMPRIME O NO APLICA"))
    print("")

    print("(D) CONTROL: el sujeto NORMAL declarado con su linea deja cero")
    faltan_con = mod.las_que_faltan([normal], texto_sin + normal["linea"] + "\n")
    print("    CIFRA filas sin declarar: %d" % len(faltan_con))
    d_ok = len(faltan_con) == 0
    print("    VEREDICTO (D): %s" % ("VERDE" if d_ok else "SIGUE ROJO Y NO DEBERIA"))
    print("")

    todo = a_ok and b_ok and c_ok and d_ok
    print("RESULTADO: %s" % ("VERDE, las cuatro se comportan" if todo else "ROJO"))
    print("FIN")
    return 0 if todo else 1


if __name__ == "__main__":
    raise SystemExit(main())
