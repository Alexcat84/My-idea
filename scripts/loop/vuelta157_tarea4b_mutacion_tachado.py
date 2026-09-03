# -*- coding: utf-8 -*-
"""vuelta157_tarea4b_mutacion_tachado.py . TAREA 4.b DE LA VUELTA 157.

EL CASO POSITIVO POR MUTACION DEL LECTOR ENSANCHADO (adjudicacion 6.8 del acta
157). Prueba las TRES cosas que el encargo pide, y las tres sobre el LECTOR DE
VERDAD, importado de `scripts/loop/vuelta152_registro_de_citas_opc05.py`, no
sobre una copia del patron tecleada aqui:

  (A) CON EL LECTOR VIEJO LA FILA TACHADA DESAPARECE. Se tacha EN MEMORIA la
      celda de clase de la fila 97 (`D` pasa a `~~C~~ D`) y se exige que el par
      juran_rcca_metodo <-> viaje_diagnostico_remedial NO ESTE en lo que el
      patron viejo recoge.
  (B) CON EL LECTOR NUEVO LA FILA APARECE CON LA CLASE BUENA, o sea con la
      ULTIMA clase escrita en la celda, que es D.
  (C) EL CONTEO DE PARES DEL REGISTRO SALE IDENTICO ANTES Y DESPUES SOBRE EL
      FICHERO SIN TACHAR. Si se mueve, esto sale ROJO y el encargo manda parar:
      ensanchar el patron no puede cambiar lo que se lee de un fichero que
      todavia no tiene un solo tachado.

EL FICHERO DEL REPO NO SE TOCA. Todo pasa sobre el texto en memoria, que es la
unica forma de probar el lector viejo sin romper Gate 0 de verdad.

LA PRUEBA DE MUTACION DE ESTE MISMO CASO (regla del ejecutor, 29 ago 2026, EL
CASO ROJO SE PRUEBA POR MUTACION): con `--mutar` se le da la vuelta al valor
esperado de (A) (se exige que el lector VIEJO conserve la fila tachada) y esta
guarda tiene que CAER en ROJO con exit 1. Ninguno de los veredictos de aqui es
una constante literal: los tres salen de correr el lector.

USO:  python scripts/loop/vuelta157_tarea4b_mutacion_tachado.py
      python scripts/loop/vuelta157_tarea4b_mutacion_tachado.py --mutar
"""
import argparse
import importlib.util
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LECTOR = os.path.join(RAIZ, "scripts", "loop", "vuelta152_registro_de_citas_opc05.py")
LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")

PAR_97 = ("juran_rcca_metodo", "viaje_diagnostico_remedial")
CELDA_LIMPIA = "| juran_rcca_metodo <-> viaje_diagnostico_remedial | D |"
CELDA_TACHADA = "| juran_rcca_metodo <-> viaje_diagnostico_remedial | ~~C~~ D |"


def cargar_lector():
    """Importa el lector de verdad. `vuelta152_registro_de_citas_opc05.py` llama
    a `main()` al final del modulo, asi que se le tapa la salida y se le deja un
    `sys.argv` limpio: lo que interesa son sus funciones y sus dos patrones, no
    su informe."""
    spec = importlib.util.spec_from_file_location("lector_opc05", LECTOR)
    mod = importlib.util.module_from_spec(spec)
    argv, salida = sys.argv, sys.stdout
    sys.argv = [LECTOR]
    sys.stdout = io.StringIO()
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv, sys.stdout = argv, salida
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar", action="store_true",
                    help="le da la vuelta al valor esperado de (A): tiene que salir ROJO")
    a = ap.parse_args()

    print("=" * 78)
    print("VUELTA 157, TAREA 4.b: CASO POSITIVO POR MUTACION DEL LECTOR ENSANCHADO")
    print("=" * 78)
    print("")

    mod = cargar_lector()
    N = mod.cargar("WORK")
    r = mod.hacer_resolver(N)
    print("  lector importado de: %s" % os.path.relpath(LECTOR, RAIZ).replace("\\", "/"))
    print("  patron VIEJO: %s" % mod.PATRON_FILA_LD_VIEJO.pattern[-64:])
    print("  patron NUEVO: %s" % mod.PATRON_FILA_LD.pattern[-64:])
    print("")

    texto = io.open(LD, encoding="utf-8").read()
    if CELDA_LIMPIA not in texto:
        print("ROJO PREVIO: la fila 97 no viene con la celda limpia esperada.")
        print("FIN")
        return 1
    tachado = texto.replace(CELDA_LIMPIA, CELDA_TACHADA, 1)

    limpio_viejo = mod.citas_de_lectura_dirigida_de_texto(texto, r, mod.PATRON_FILA_LD_VIEJO)
    limpio_nuevo = mod.citas_de_lectura_dirigida_de_texto(texto, r, mod.PATRON_FILA_LD)
    tach_viejo = mod.citas_de_lectura_dirigida_de_texto(tachado, r, mod.PATRON_FILA_LD_VIEJO)
    tach_nuevo = mod.citas_de_lectura_dirigida_de_texto(tachado, r, mod.PATRON_FILA_LD)

    clave = tuple(sorted((r(PAR_97[0]), r(PAR_97[1]))))

    print("(C) EL CONTEO SOBRE EL FICHERO SIN TACHAR, QUE ES LO QUE NO SE PUEDE MOVER")
    print("    CIFRA pares que recoge el lector VIEJO: %d" % len(limpio_viejo))
    print("    CIFRA pares que recoge el lector NUEVO: %d" % len(limpio_nuevo))
    mismas_claves = set(limpio_viejo) == set(limpio_nuevo)
    mismas_clases = all(limpio_viejo[k]["clase"] == limpio_nuevo[k]["clase"]
                        for k in limpio_viejo if k in limpio_nuevo)
    print("    mismas claves: %s | mismas clases: %s" % (mismas_claves, mismas_clases))
    conteo_ok = (len(limpio_viejo) == len(limpio_nuevo)) and mismas_claves and mismas_clases
    print("    VEREDICTO (C): %s" % ("IDENTICO" if conteo_ok else "SE MOVIO"))
    print("")

    print("(A) EL LECTOR VIEJO SOBRE LA FILA 97 TACHADA")
    a_viejo_pierde = clave not in tach_viejo
    print("    CIFRA pares que recoge el lector VIEJO sobre el texto tachado: %d"
          % len(tach_viejo))
    print("    la fila 97 esta en lo que recoge el VIEJO: %s" % (clave in tach_viejo))
    print("    coincidencias del patron VIEJO en la fila 97: %d"
          % (1 if clave in tach_viejo else 0))
    print("    VEREDICTO (A): %s" % ("LA FILA DESAPARECE" if a_viejo_pierde else "LA CONSERVA"))
    print("")

    print("(B) EL LECTOR NUEVO SOBRE LA MISMA FILA 97 TACHADA")
    clase_nueva = tach_nuevo.get(clave, {}).get("clase")
    b_ok = clave in tach_nuevo and clase_nueva == "D"
    print("    CIFRA pares que recoge el lector NUEVO sobre el texto tachado: %d"
          % len(tach_nuevo))
    print("    la fila 97 esta en lo que recoge el NUEVO: %s" % (clave in tach_nuevo))
    print("    clase que le asigna (la ULTIMA escrita en la celda): %r" % clase_nueva)
    print("    VEREDICTO (B): %s" % ("APARECE CON LA CLASE BUENA" if b_ok else "NO APARECE BIEN"))
    print("")

    esperado_a = True
    if a.mutar:
        esperado_a = False
        print("  MUTACION ACTIVA: se le da la vuelta al valor esperado de (A). Ahora se")
        print("  exige que el lector VIEJO CONSERVE la fila tachada, que es falso, y este")
        print("  caso tiene que CAER. Si no cae, el caso no probaba nada.")
        print("")

    bien = (a_viejo_pierde == esperado_a) and b_ok and conteo_ok
    print("  (A) esperado %s, medido %s" % (esperado_a, a_viejo_pierde))
    print("  (B) esperado True, medido %s" % b_ok)
    print("  (C) esperado True, medido %s" % conteo_ok)
    print("")
    if bien:
        print("VERDE: el lector viejo pierde la fila tachada, el nuevo la recupera con la")
        print("clase D, y el conteo sobre el fichero sin tachar no se mueve.")
        print("FIN")
        return 0
    print("ROJO: alguna de las tres condiciones no se cumple.")
    print("FIN")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
