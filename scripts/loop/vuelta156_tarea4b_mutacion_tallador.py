# -*- coding: utf-8 -*-
"""vuelta156_tarea4b_mutacion_tallador.py . TAREA 4.b DE LA VUELTA 156.

EL CASO POSITIVO POR MUTACION DE LA PUERTA DEL NOMBRE DE FASE (adjudicacion 6.10
del acta 155), CON LAS DOS SALIDAS Y CON LOS DOS TALLADORES.

QUE PRUEBA, Y POR QUE ASI. Un assert que compare un literal con el mismo literal
no puede caer nunca (EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION). Aqui la
mutacion es EL PROPIO INSTRUMENTO: se corre la vara NUEVA (el arbol de trabajo) y
la vara VIEJA (sacada del COMMIT DE APERTURA de esta vuelta con `git show`, no de
HEAD, porque HEAD avanza y una contraprueba anclada a HEAD se cae en cuanto se
commitea el arreglo, que es la caida 5 que el ejecutor declaro en la vuelta 154).

LOS CUATRO CASOS:
  A  vara NUEVA, `--fase 06`        -> ROJO, exit distinto de 0
  B  vara VIEJA, `--fase 06`        -> VERDE, exit 0, 11 del catalogo. ES LA
                                       CONTRAPRUEBA: sin el arreglo el verde sale
  C  vara NUEVA, `--fase 06_MESAS`  -> VERDE, exit 0, y con las MISMAS 16 de 16
                                       que se midieron ANTES del arreglo
  D  vara NUEVA, `--fase NO_EXISTE` -> ROJO, exit distinto de 0 (la red de atras,
                                       la del catalogo vacio, sigue puesta)

EL 16 NO SE TECLEA: se lee de docs/loop/SALIDA_V156_T4_ANTES.txt, la medicion
sellada ANTES del arreglo. Si el arreglo hubiera movido el conteo, este arnes cae:
el arreglo tenia que tocar LA PUERTA, no el conteo.

USO:  python scripts/loop/vuelta156_tarea4b_mutacion_tallador.py
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ANTES = os.path.join(LOOP, "SALIDA_V156_T4_ANTES.txt")
NUEVO_REL = "scripts/loop/tallar_estado_de_fase.py"
VIEJO_REL = "scripts/loop/_v156_tallador_viejo_copia.py"
VIEJO = os.path.join(RAIZ, VIEJO_REL)

P_CIFRA = re.compile(
    r"CIFRA: operaciones del catalogo: (\d+) \| con destino cumplido: (\d+) \| "
    r"sin cumplir: (\d+)")


def commit_de_apertura():
    """EL COMMIT DE APERTURA SE LEE DE SU FICHERO SELLADO, no de HEAD ni de un
    literal: docs/loop/SALIDA_V156_HEAD_APERTURA.txt lo trae en una linea."""
    ruta = os.path.join(LOOP, "SALIDA_V156_HEAD_APERTURA.txt")
    h = io.open(ruta, encoding="utf-8").read().strip()
    assert re.fullmatch(r"[0-9a-f]{40}", h), "el HEAD de apertura sellado no es un hash"
    return h


def sacar_vara_vieja(commit):
    r = subprocess.run(["git", "show", "%s:%s" % (commit, NUEVO_REL)],
                       cwd=RAIZ, capture_output=True)
    assert r.returncode == 0, "no se pudo sacar la vara vieja de %s" % commit[:8]
    datos = r.stdout.decode("utf-8")
    assert "nombres_de_fase" not in datos, (
        "la copia sacada de %s YA TRAE EL ARREGLO: no serviria de contraprueba" % commit[:8])
    with io.open(VIEJO, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(datos)
    return len(datos.splitlines())


def correr(script_rel, fase):
    entorno = dict(os.environ)
    entorno["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, os.path.join(RAIZ, script_rel), "--fase", fase],
                       cwd=RAIZ, capture_output=True, env=entorno)
    salida = r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace")
    m = P_CIFRA.search(salida)
    cifra = tuple(int(x) for x in m.groups()) if m else None
    rojo = "\nROJO," in salida or salida.startswith("ROJO,")
    return r.returncode, rojo, cifra, salida


def cifra_sellada_de_antes(fase):
    """El 16 de 16 no se teclea: se lee del fichero sellado antes del arreglo."""
    texto = io.open(ANTES, encoding="utf-8").read()
    bloque = texto.split("--- --fase %s ---" % fase, 1)
    assert len(bloque) == 2, "no hay bloque de --fase %s en %s" % (fase, ANTES)
    m = P_CIFRA.search(bloque[1])
    assert m, "no hay linea CIFRA en el bloque de --fase %s" % fase
    return tuple(int(x) for x in m.groups())


def main():
    print("=" * 100)
    print("VUELTA 156, TAREA 4.b: EL CASO POSITIVO POR MUTACION DE LA PUERTA DEL NOMBRE")
    print("=" * 100)
    commit = commit_de_apertura()
    print("Vara VIEJA sacada de %s (el HEAD de apertura sellado, no de HEAD)" % commit[:8])
    n = sacar_vara_vieja(commit)
    print("Copia escrita en %s (%d lineas), y se comprueba que NO trae el arreglo." % (VIEJO_REL, n))
    print("")

    fallos = []

    print("-" * 100)
    print("CASO A: vara NUEVA, --fase 06. SE ESPERA ROJO Y EXIT DISTINTO DE 0")
    print("-" * 100)
    ec, rojo, cifra, salida = correr(NUEVO_REL, "06")
    print("  EXITCODE: %d | ROJO: %s | cifra: %s" % (ec, rojo, cifra))
    linea = [x for x in salida.splitlines() if "NO CALZA" in x]
    print("  motivo: %s" % (linea[0].strip()[:150] if linea else "(no lo dice)"))
    if not (ec != 0 and rojo):
        fallos.append("CASO A: la vara nueva no cae en rojo con --fase 06")

    print("")
    print("-" * 100)
    print("CASO B, LA CONTRAPRUEBA: vara VIEJA, --fase 06. SE ESPERA VERDE Y EXIT 0")
    print("-" * 100)
    ec_b, rojo_b, cifra_b, _s = correr(VIEJO_REL, "06")
    print("  EXITCODE: %d | ROJO: %s | cifra (catalogo, cumplido, sin cumplir): %s"
          % (ec_b, rojo_b, cifra_b))
    if not (ec_b == 0 and not rojo_b and cifra_b is not None and cifra_b[0] == 11):
        fallos.append("CASO B: la vara vieja no reproduce el verde sobre 11 con --fase 06")
    else:
        print("  LA MUTACION MUERDE: sobre LA MISMA ORDEN, la vieja da verde sobre 11 del")
        print("  catalogo y la nueva cae en rojo. La contraprueba ataca el punto que era ciego.")

    print("")
    print("-" * 100)
    print("CASO C: vara NUEVA, --fase 06_MESAS. SE ESPERA VERDE Y LA MISMA CIFRA DE ANTES")
    print("-" * 100)
    esperada = cifra_sellada_de_antes("06_MESAS")
    ec_c, rojo_c, cifra_c, _s = correr(NUEVO_REL, "06_MESAS")
    print("  cifra SELLADA antes del arreglo (leida de SALIDA_V156_T4_ANTES.txt): %s" % (esperada,))
    print("  cifra de HOY con la vara nueva:                                     %s" % (cifra_c,))
    print("  EXITCODE: %d | ROJO: %s | IDENTICAS: %s" % (ec_c, rojo_c, cifra_c == esperada))
    if not (ec_c == 0 and not rojo_c and cifra_c == esperada):
        fallos.append("CASO C: el arreglo movio el conteo de 06_MESAS o lo puso en rojo")

    print("")
    print("-" * 100)
    print("CASO D: vara NUEVA, --fase NO_EXISTE. LA RED DE ATRAS SIGUE PUESTA")
    print("-" * 100)
    ec_d, rojo_d, _c, _s = correr(NUEVO_REL, "NO_EXISTE")
    print("  EXITCODE: %d | ROJO: %s" % (ec_d, rojo_d))
    if not (ec_d != 0 and rojo_d):
        fallos.append("CASO D: el catalogo inexistente dejo de cazarse")

    print("")
    print("=" * 100)
    if fallos:
        print("ROJO, %d caso(s) no cuadran:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1
    print("VERDE: los CUATRO casos salen como se esperaba.")
    print("CIFRA casos del arnes en verde: 4 comprobacion(es)")
    print("CIFRA operaciones del catalogo de 06_MESAS, antes y despues: %d y %d"
          % (esperada[0], cifra_c[0]))
    print("=" * 100)
    return 0


raise SystemExit(main())
