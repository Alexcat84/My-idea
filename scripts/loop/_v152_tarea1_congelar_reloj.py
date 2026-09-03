# -*- coding: utf-8 -*-
"""VUELTA 152, TAREA 1: CONGELAR EL RELOJ DE GIT EN LAS DOS VARAS QUE SE
CUENTAN A SI MISMAS.

Parchea POR SUSTITUCION EXACTA, sin borrar el texto viejo de los docstrings:
cada bloque nuevo se ANADE con su CORRECCION DECLARADA.

  (1) scripts/loop/vuelta150_3_relectura_expediente.py, pierna P3: el `git log`
      pasa a ir cortado en un `--corte` obligatorio, y nace una guarda que
      compara DOS CONJUNTOS COMPUTADOS (los commits contados y los commits de
      la propia vuelta) y CAE si se cruzan.
  (2) scripts/loop/vuelta150_4_tabla_por_fase.py, fila 0 CODIGO: la lista de
      ficheros SALIDA_*.txt deja de leerse del arbol de trabajo y se lee del
      arbol del `--corte` con git ls-tree, con la misma guarda de dos
      conjuntos computados sobre los ficheros ANADIDOS por la propia vuelta.

USO:
  python scripts/loop/_v152_tarea1_congelar_reloj.py
"""
import io
import os
import py_compile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Q = '"' * 3


def sustituir(ruta, viejo, nuevo, etiqueta):
    p = os.path.join(RAIZ, ruta)
    t = io.open(p, encoding="utf-8").read()
    assert t.count(viejo) == 1, "%s: el ancla no aparece exactamente una vez (%d)" % (
        etiqueta, t.count(viejo))
    t2 = t.replace(viejo, nuevo)
    assert t2 != t
    io.open(p, "w", encoding="utf-8", newline="\n").write(t2)
    print("  [OK] %s :: %s" % (ruta, etiqueta))


# ---------------------------------------------------------------- vuelta150_3
R3 = "scripts/loop/vuelta150_3_relectura_expediente.py"

sustituir(R3, """USO:
  python scripts/loop/vuelta150_3_relectura_expediente.py
""" + Q + """
import io
import json
import os
import re
import subprocess
""", """CORRECCION DECLARADA (2026-09-02, vuelta 152, TAREA 1; hallazgo del acta 151,
seccion de hallazgos fuera de lo marcado. NADA DEL TEXTO ANTERIOR SE BORRA,
estas lineas se anaden). LA P3 SE CONTABA A SI MISMA: pedia "un commit que
NOMBRA el id_op y ademas toca dataset/, scripts/, engine/ o web/", y el commit
con el que la PROPIA VUELTA publica que una ficha no tiene prueba de ejecucion
nombra esa ficha y toca scripts/, asi que el papeleo de la vuelta se convertia
en la prueba del trabajo de la vuelta. Medido por el auditor: las dos fichas
que la vuelta 150 declaro SIN NINGUNA PRUEBA (OP-V-01 y OP-L-01) tenian una al
dia siguiente, y era el commit que dijo que no la tenian.

LA REPARACION: EL RELOJ DE GIT SE CONGELA. `git log` va cortado en `--corte`,
que es OBLIGATORIO y que por regla es EL HEAD DE APERTURA DE LA VUELTA, o sea
el commit anterior al primero que la vuelta escribe. Y no basta con congelar:
una GUARDA compara dos conjuntos COMPUTADOS, los commits que la P3 cuenta y los
commits del rango `--apertura`..HEAD, y CAE si se cruzan. Su prueba de mutacion
esta en scripts/loop/_v152_tarea1_mutacion_reloj.py.

USO:
  python scripts/loop/vuelta150_3_relectura_expediente.py --corte <REF> [--apertura <REF>]

  --corte     ref donde se para el reloj de git. Obligatorio: sin el la vara
              vuelve a contarse a si misma, y una vara que se cuenta a si misma
              en silencio es peor que una que no corre.
  --apertura  HEAD de apertura de la vuelta, que define el rango prohibido para
              la guarda. Por defecto, el mismo valor de --corte.
""" + Q + """
import argparse
import io
import json
import os
import re
import subprocess
""", "docstring y argparse")

sustituir(R3, """def p3_huella_en_git(ids):
    """ + Q + """Commits de la rama activa cuyo mensaje nombra el id_op Y que tocan
    dataset/, scripts/, engine/ o web/.""" + Q + """
    hits = {}
    for i in ids:
        # MISMA FRONTERA DE PALABRA que en P2, por el mismo motivo: sin ella
        # `OP-M-01` heredaria los commits de `OP-M-01-FUSION`.
        r = subprocess.run(["git", "log", "--format=%H", "-E", "--grep",
                            re.escape(i) + "([^A-Za-z0-9_-]|$)"], capture_output=True, cwd=RAIZ)""",
             """def p3_huella_en_git(ids, corte):
    """ + Q + """Commits de la rama activa cuyo mensaje nombra el id_op Y que tocan
    dataset/, scripts/, engine/ o web/.

    CON EL RELOJ PARADO EN `corte` (correccion declarada de la vuelta 152): el
    `git log` no ve un solo commit posterior, asi que ningun commit de la propia
    vuelta puede servirle de prueba a la propia vuelta.""" + Q + """
    hits = {}
    for i in ids:
        # MISMA FRONTERA DE PALABRA que en P2, por el mismo motivo: sin ella
        # `OP-M-01` heredaria los commits de `OP-M-01-FUSION`.
        r = subprocess.run(["git", "log", corte, "--format=%H", "-E", "--grep",
                            re.escape(i) + "([^A-Za-z0-9_-]|$)"], capture_output=True, cwd=RAIZ)""",
             "p3 con corte")

sustituir(R3, """def declara_su_estado(f):""", """def guarda_reloj_congelado(v3, apertura):
    """ + Q + """LA GUARDA DEL RELOJ. Compara DOS CONJUNTOS COMPUTADOS y no una constante:

      `contados`  los commits que la P3 esta usando como prueba, sacados de su
                  propia salida.
      `propios`   los commits del rango `apertura`..HEAD, o sea LOS QUE LA
                  PROPIA VUELTA HA ESCRITO, sacados de git rev-list.

    Si se cruzan, la vara se esta contando a si misma y la guarda CAE. Los dos
    lados se calculan en esta corrida: no hay un literal esperado que comparar
    consigo mismo (EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION).""" + Q + """
    r = subprocess.run(["git", "rev-list", "%s..HEAD" % apertura],
                       capture_output=True, cwd=RAIZ)
    propios = {c[:8] for c in r.stdout.decode().split() if c}
    contados = set()
    for i in v3:
        contados.update(v3[i][1])
    intrusos = sorted(contados & propios)
    return propios, contados, intrusos


def declara_su_estado(f):""", "guarda del reloj")

sustituir(R3, """def main():
    F = fichas()
    ids = [f["id_op"] for f in F]
    print("FICHAS EN docs/plan/OPERACIONES.jsonl: %d" % len(F))
    assert len(set(ids)) == len(ids), "hay ids duplicados"
""", """def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corte", required=True)
    ap.add_argument("--apertura", default=None)
    args = ap.parse_args()
    corte = args.corte
    apertura = args.apertura or corte
    corte_h = subprocess.run(["git", "rev-parse", "--short=8", corte],
                             capture_output=True, cwd=RAIZ).stdout.decode().strip()
    apertura_h = subprocess.run(["git", "rev-parse", "--short=8", apertura],
                                capture_output=True, cwd=RAIZ).stdout.decode().strip()
    print("RELOJ DE GIT CONGELADO EN --corte %s (%s). RANGO PROPIO DE LA VUELTA: %s..HEAD (%s)"
          % (corte, corte_h, apertura, apertura_h))

    F = fichas()
    ids = [f["id_op"] for f in F]
    print("FICHAS EN docs/plan/OPERACIONES.jsonl: %d" % len(F))
    assert len(set(ids)) == len(ids), "hay ids duplicados"
""", "main con corte")

sustituir(R3, """    v1 = p1_vara_de_grafo()
    v2 = p2_vara_de_codigo(ids)
    v3 = p3_huella_en_git(ids)
""", """    v1 = p1_vara_de_grafo()
    v2 = p2_vara_de_codigo(ids)
    v3 = p3_huella_en_git(ids, corte)

    propios, contados, intrusos = guarda_reloj_congelado(v3, apertura)
    print("GUARDA DEL RELOJ: commits propios de la vuelta %d | commits contados por P3 %d | INTRUSOS %d"
          % (len(propios), len(contados), len(intrusos)))
    if intrusos:
        print("  INTRUSOS: %s" % ", ".join(intrusos))
    assert not intrusos, (
        "LA VARA SE CUENTA A SI MISMA: la P3 esta usando como prueba %d commit(s) "
        "escritos por la propia vuelta (%s)" % (len(intrusos), ", ".join(intrusos)))
""", "llamada a la guarda")

# ---------------------------------------------------------------- vuelta150_4
R4 = "scripts/loop/vuelta150_4_tabla_por_fase.py"

sustituir(R4, """USO:
  python scripts/loop/vuelta150_4_tabla_por_fase.py
""" + Q + """
import io
import json
import os
import re
import subprocess
""", """CORRECCION DECLARADA (2026-09-02, vuelta 152, TAREA 1; hallazgo del acta 151.
NADA DEL TEXTO ANTERIOR SE BORRA, estas lineas se anaden). LA FILA 0 CODIGO SE
CONTABA A SI MISMA: buscaba en docs/loop/ una salida COMMITEADA que nombrase el
id_op y trajese una marca de ROJO, y la leia con os.listdir DEL ARBOL DE
TRABAJO, o sea incluyendo las salidas que la PROPIA VUELTA acababa de escribir.
El papeleo de la vuelta contaba como prueba historica de que la guarda se cayo
antes del arreglo. Medido por el auditor: la cifra de la fila se movio de 58/13
a 60/11 sin que nadie tocase un nodo.

LA REPARACION, LA MISMA QUE EN LA P3: el catalogo de salidas se lee del ARBOL
DEL `--corte` con git ls-tree y el contenido con git show, y una GUARDA compara
dos conjuntos COMPUTADOS (las salidas usadas y las salidas ANADIDAS en el rango
`--apertura`..HEAD) y CAE si se cruzan.

TAMBIEN SE PARAMETRIZA LA SALIDA DE GATE 0 (`--gate0`), que estaba clavada en el
fichero de la vuelta 150: una tabla del cierre se mide al cierre (EJECUTOR.md 1)
y no con el Gate 0 de otra vuelta.

USO:
  python scripts/loop/vuelta150_4_tabla_por_fase.py --corte <REF> [--apertura <REF>] [--gate0 <RUTA>]
""" + Q + """
import argparse
import io
import json
import os
import re
import subprocess
""", "docstring y argparse")

sustituir(R4, """def gate0_checks():
    """ + Q + """Lee la salida de Gate 0 de la apertura de esta vuelta, ya commiteada.""" + Q + """
    ruta = os.path.join(RAIZ, "docs", "loop", "SALIDA_V150_GATE0_CMD1_APERTURA.txt")
    out = []""", """def gate0_checks(ruta=None):
    """ + Q + """Lee la salida de Gate 0 de la apertura de esta vuelta, ya commiteada.

    CORRECCION DECLARADA de la vuelta 152: la ruta deja de estar clavada en el
    fichero de la vuelta 150 y entra por --gate0. El defecto se conserva para
    que una corrida sin bandera reproduzca la de la 150 al digito.""" + Q + """
    if ruta is None:
        ruta = os.path.join(RAIZ, "docs", "loop", "SALIDA_V150_GATE0_CMD1_APERTURA.txt")
    out = []""", "gate0 parametrizado")

sustituir(R4, """def salidas_del_bucle():
    d = os.path.join(RAIZ, "docs", "loop")
    return [os.path.join(d, x) for x in os.listdir(d)
            if x.startswith("SALIDA_") and x.endswith(".txt")]
""", """def salidas_del_bucle(corte):
    """ + Q + """El catalogo de SALIDA_*.txt LEIDO DEL ARBOL DEL CORTE, no del de trabajo.

    Devuelve [(ruta_relativa, texto)]. Con el reloj parado aqui, una salida que
    la propia vuelta escriba no existe para esta vara.""" + Q + """
    r = subprocess.run(["git", "ls-tree", "-r", "--name-only", corte, "--", "docs/loop"],
                       capture_output=True, cwd=RAIZ)
    rutas = [x for x in r.stdout.decode("utf-8", "replace").splitlines()
             if x.startswith("docs/loop/SALIDA_") and x.endswith(".txt")]
    out = []
    for x in rutas:
        b = subprocess.run(["git", "show", "%s:%s" % (corte, x)], capture_output=True, cwd=RAIZ)
        if b.returncode:
            continue
        out.append((x, b.stdout.decode("utf-8", "replace")))
    return out


def guarda_salidas_congeladas(usadas, apertura):
    """ + Q + """LA GUARDA DE LA FILA 0, hermana de la del reloj de la P3 y con la misma
    forma: DOS CONJUNTOS COMPUTADOS, ninguno tecleado.

      `usadas`   las salidas que la fila esta usando como prueba.
      `propias`  las salidas ANADIDAS en `apertura`..HEAD, o sea las que la
                 propia vuelta ha escrito, sacadas de git diff --diff-filter=A.

    Si se cruzan, la fila se cuenta a si misma y la guarda CAE.""" + Q + """
    r = subprocess.run(["git", "diff", "--name-only", "--diff-filter=A",
                        "%s..HEAD" % apertura, "--", "docs/loop"],
                       capture_output=True, cwd=RAIZ)
    propias = {x for x in r.stdout.decode("utf-8", "replace").splitlines()
               if x.startswith("docs/loop/SALIDA_") and x.endswith(".txt")}
    intrusas = sorted(set(usadas) & propias)
    return propias, intrusas
""", "salidas del corte y su guarda")

sustituir(R4, """def main():
    filas = celdas_de_la_tabla()""", """def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corte", required=True)
    ap.add_argument("--apertura", default=None)
    ap.add_argument("--gate0", default=None)
    args = ap.parse_args()
    corte = args.corte
    apertura = args.apertura or corte
    corte_h = subprocess.run(["git", "rev-parse", "--short=8", corte],
                             capture_output=True, cwd=RAIZ).stdout.decode().strip()
    print("RELOJ DE GIT CONGELADO EN --corte %s (%s). RANGO PROPIO: %s..HEAD"
          % (corte, corte_h, apertura))
    print("SALIDA DE GATE 0 LEIDA DE: %s"
          % (args.gate0 or "docs/loop/SALIDA_V150_GATE0_CMD1_APERTURA.txt (defecto)"))

    filas = celdas_de_la_tabla()""", "main con corte")

sustituir(R4, """    checks = gate0_checks()""", """    checks = gate0_checks(args.gate0)""",
             "checks con ruta")

sustituir(R4, """    rutas = salidas_del_bucle()
    print("ficheros SALIDA_*.txt en docs/loop: %d" % len(rutas))
    con_rojo = {}
    for ruta in rutas:
        try:
            texto = io.open(ruta, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        tiene_rojo = bool(re.search(r"\\[FALLO\\]|EXITCODE: 1|EXIT=1| CAE\\.|ROJO", texto))
        if not tiene_rojo:
            continue
        for x in fase00:
            if re.search(re.escape(x["id_op"]) + r"(?![A-Za-z0-9_-])", texto):
                con_rojo.setdefault(x["id_op"], []).append(os.path.basename(ruta))""",
             """    rutas = salidas_del_bucle(corte)
    print("ficheros SALIDA_*.txt en docs/loop EN EL ARBOL DEL CORTE: %d" % len(rutas))
    con_rojo = {}
    usadas = set()
    for ruta, texto in rutas:
        tiene_rojo = bool(re.search(r"\\[FALLO\\]|EXITCODE: 1|EXIT=1| CAE\\.|ROJO", texto))
        if not tiene_rojo:
            continue
        for x in fase00:
            if re.search(re.escape(x["id_op"]) + r"(?![A-Za-z0-9_-])", texto):
                con_rojo.setdefault(x["id_op"], []).append(os.path.basename(ruta))
                usadas.add(ruta)
    propias, intrusas = guarda_salidas_congeladas(usadas, apertura)
    print("GUARDA DE SALIDAS: salidas anadidas por la propia vuelta %d | usadas como prueba %d | INTRUSAS %d"
          % (len(propias), len(usadas), len(intrusas)))
    if intrusas:
        print("  INTRUSAS: %s" % ", ".join(intrusas))
    assert not intrusas, (
        "LA VARA SE CUENTA A SI MISMA: la fila 0 CODIGO esta usando como prueba %d "
        "salida(s) escritas por la propia vuelta (%s)" % (len(intrusas), ", ".join(intrusas)))""",
             "fila 0 con corte y guarda")

print("")
print("LOS DOS FICHEROS PARCHEADOS. Comprobacion de sintaxis:")
for r in (R3, R4):
    py_compile.compile(os.path.join(RAIZ, r), doraise=True)
    print("  [OK] compila: %s" % r)
