# -*- coding: utf-8 -*-
"""vuelta160_tarea3_remedio_p16.py . TAREA 3.a DE LA VUELTA 160.

APLICA EL REMEDIO DEL CHECK DE P.16 A LOS DOCE FICHEROS DEL ALCANCE, que la
adjudicacion 6.1 del acta 159 fijo en DOCE y con la vara de la LECTURA B. El
defecto lo describe la 6.7 del acta 158: el docstring promete CONTENIDO y el
instrumento es `git status`, que ve ademas FIN DE LINEA y SUCIEDAD ANTERIOR AL
ARRANQUE. El remedio es una HUELLA DE CONTENIDO tomada ANTES y DESPUES de las
mutaciones DENTRO DEL PROPIO SCRIPT y COMPARADA CONSIGO MISMA, y vive en
`scripts/loop/huella_de_contenido.py`.

LA MANO NO ESCRIBE, ESCRIBE EL INSTRUMENTO. Doce ficheros distintos con seis
formas distintas de invocar el check son doce ocasiones de que se cuele una
diferencia entre lo que se hizo y lo que se cuenta. Aqui cada edicion es un par
(texto viejo literal, texto nuevo literal) y el instrumento PARA si el texto
viejo no aparece EXACTAMENTE una vez.

LA LINEA VIEJA NO SE BORRA NUNCA: queda TACHADA Y LEGIBLE en un comentario, que
es la costumbre de la casa desde la vuelta 156 (`verificar_apertura_sellada.py`
lleva asi la linea de la 6.7 del acta 153). Y ESO TIENE UNA CONSECUENCIA QUE SE
DECLARA EN VEZ DE CALLARSE: como el texto viejo sobrevive, LOS DOCE SIGUEN
CASANDO CON EL PATRON LITERAL de la lectura B y el alcance sigue siendo DOCE
despues del remedio. Si la linea vieja se hubiera borrado, la nomina de la 6.1
habria bajado sola y nadie podria volver a auditarla.

TRES FORMAS DE REMEDIO, SEGUN LA FORMA QUE TENIA CADA UNO, Y LAS TRES SE
DECLARAN:

  FORMA 1, LOS QUE NO TENIAN TOMA PREVIA (142_2c, 143_2a, 143_2c, 144_3a). Se
  les anade la toma ANTES al principio de `main` y la comparacion DESPUES en el
  sitio del check. El veredicto pasa a la huella; la salida de `git status` se
  sigue imprimiendo como INFORME.

  FORMA 2, LOS QUE YA COMPARABAN ANTES CONTRA DESPUES (144_2b, 144_3b_giro,
  144_3b_negativa, 146_3c, 147_3d, 147_3e, 89_tarea4). Ya tenian la figura
  correcta y lo que fallaba era el instrumento: se cambia lo que devuelve la
  toma, de la salida de `git status` a la huella. En los cinco que lo hacen con
  una funcion, el cambio es de una funcion y alcanza a todas sus llamadas.

  FORMA 3, EL QUE ESCRIBE A PROPOSITO (143_3c_girar_arista). Este NO es un
  arnes de mutacion: es la operacion que gira una arista y ESCRIBE dos ficheros
  de nodo. Su `git status` nunca fue un veredicto, era un informe de lo que
  acababa de escribir. Se le anade la huella igual, tomada antes y despues, y
  se declara EN SU PROPIA SALIDA que aqui la huella DEBE cambiar y que sigue
  siendo informe y no vara. Decir que este es un caso distinto vale mas que
  fabricarle un veredicto que no le corresponde.

Y UNA CONSECUENCIA DE LA FORMA 2 QUE TAMBIEN SE DECLARA: en
`vuelta89_tarea4_guarda_op_c05.py` el remedio RETIRA UNA PARADA. Ese script
abortaba si `dataset/` venia sucio ANTES de arrancar, que es el ancla 2 en su
forma mas pura: se negaba a correr por suciedad que no era suya. Como no
escribe en `dataset/` ni una vez (su caso rojo vive entero en un directorio
temporal), la suciedad anterior no puede falsear su medicion, y lo que hay que
probar (que EL no escribio) lo prueba la huella comparada consigo misma. La
suciedad anterior se sigue imprimiendo.

ES IDEMPOTENTE: si la marca ya esta escrita, el fichero se salta y se dice.

USO:  python scripts/loop/vuelta160_tarea3_remedio_p16.py
"""
import io
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
SALIDA_ALCANCE = os.path.join(RAIZ, "docs", "loop", "SALIDA_V159_T5_ALCANCE.txt")

MARCA = "REMEDIO DEL CHECK DE P.16 (vuelta 160"


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)


def nomina_del_fichero_de_salida():
    """LA NOMINA, CONTADA DE SU FICHERO (EJECUTOR.md 1). Seccion C de
    SALIDA_V159_T5_ALCANCE.txt, que es la medicion con que el acta 159 adjudico
    el alcance en doce."""
    dentro = False
    salida = []
    for linea in leer(SALIDA_ALCANCE).splitlines():
        if linea.startswith("C) LA NOMINA PRINCIPAL"):
            dentro = True
            continue
        if dentro:
            if linea.strip().startswith("CIFRA") or linea.startswith("D)"):
                break
            campos = linea.split()
            if campos and campos[0].endswith(".py"):
                salida.append(campos[0])
    return sorted(salida)


PREAMBULO = '''
# --- REMEDIO DEL CHECK DE P.16 (vuelta 160, TAREA 3.a; adjudicacion 6.7 del
# acta 158 y 6.1 del acta 159). La huella NO MIRA A GIT: compara el disco contra
# el disco, y por eso ni el estado de fin de linea ni la suciedad anterior al
# arranque pueden moverla. Ver scripts/loop/huella_de_contenido.py ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import huella_de_contenido as _HC  # noqa: E402
_P16_RUTAS = %s
'''


# --------------------------------------------------------------------------
# LAS EDICIONES, UNA A UNA. Cada entrada es (fichero, [(viejo, nuevo), ...]).
# El texto viejo tiene que aparecer EXACTAMENTE UNA VEZ o el instrumento para.
# --------------------------------------------------------------------------

EDICIONES = []


def _forma1(fichero, rutas, anclaje_antes, viejo_check, nuevo_check):
    """FORMA 1: se anade la toma ANTES tras el anclaje y se cambia el check."""
    EDICIONES.append((fichero, [
        (anclaje_antes,
         anclaje_antes + PREAMBULO.replace("\n#", "\n    #").replace(
             "\nsys.path", "\n    sys.path").replace(
             "\nimport huella", "\n    import huella").replace(
             "\n_P16_RUTAS", "\n    _P16_RUTAS") % rutas
         + "    _p16_antes = _HC.huella(*_P16_RUTAS)\n"),
        (viejo_check, nuevo_check),
    ]))


def _preambulo_modulo(rutas):
    return PREAMBULO % rutas


# ==========================================================================
# 1. vuelta142_2c_mutaciones.py  (FORMA 1, dataset/ y docs/plan/)
# ==========================================================================
_forma1(
    "vuelta142_2c_mutaciones.py",
    '("dataset/", "docs/plan/")',
    '    ap.add_argument("--fase", default="03_FUSIONES")\n'
    '    a = ap.parse_args()\n'
    '    sys.stdout.reconfigure(encoding="utf-8")\n',
    '''    ok = (sucio == "")
    resultados.append(("P.16 dataset/ y docs/plan/ SIN TOCAR tras las mutaciones", ok))
    print("")
    print("git status --porcelain -- dataset/ docs/plan/ : %r" % sucio)
''',
    '''    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LA LINEA VIEJA QUEDA AQUI,
    # TACHADA Y LEGIBLE, porque el veredicto de las vueltas 142 a 159 se dio con
    # ella y taparla impediria auditarlo:
    #     ~~ok = (sucio == "")~~
    #     ~~print("git status --porcelain -- dataset/ docs/plan/ : %r" % sucio)~~
    # EL VEREDICTO PASA A LA HUELLA DE CONTENIDO. La salida de git status SE
    # SIGUE IMPRIMIENDO, ahora como INFORME y no como vara.
    _p16_despues = _HC.huella(*_P16_RUTAS)
    ok, _p16_linea = _HC.comparar(_p16_antes, _p16_despues, *_P16_RUTAS)
    resultados.append(("P.16 dataset/ y docs/plan/ SIN TOCAR tras las mutaciones", ok))
    print("")
    print(_p16_linea)
    print("git status --porcelain -- dataset/ docs/plan/ (INFORME, no vara) : %r" % sucio)
''')

# ==========================================================================
# 2. vuelta143_2a_mutaciones.py  (FORMA 1, dataset/ y docs/plan/)
# ==========================================================================
_forma1(
    "vuelta143_2a_mutaciones.py",
    '("dataset/", "docs/plan/")',
    '    ap.add_argument("--fase", default="06_MESAS")\n'
    '    a = ap.parse_args()\n'
    '    sys.stdout.reconfigure(encoding="utf-8")\n',
    '''    ok = (sucio == "")
    resultados.append(("P.16 dataset/ y docs/plan/ SIN TOCAR tras las mutaciones", ok))
    print("")
    print("git status --porcelain -- dataset/ docs/plan/ : %r" % sucio)
''',
    '''    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LA LINEA VIEJA QUEDA AQUI,
    # TACHADA Y LEGIBLE:
    #     ~~ok = (sucio == "")~~
    #     ~~print("git status --porcelain -- dataset/ docs/plan/ : %r" % sucio)~~
    # EL VEREDICTO PASA A LA HUELLA DE CONTENIDO. La salida de git status SE
    # SIGUE IMPRIMIENDO, ahora como INFORME y no como vara.
    _p16_despues = _HC.huella(*_P16_RUTAS)
    ok, _p16_linea = _HC.comparar(_p16_antes, _p16_despues, *_P16_RUTAS)
    resultados.append(("P.16 dataset/ y docs/plan/ SIN TOCAR tras las mutaciones", ok))
    print("")
    print(_p16_linea)
    print("git status --porcelain -- dataset/ docs/plan/ (INFORME, no vara) : %r" % sucio)
''')

# ==========================================================================
# 3. vuelta143_2c_mutacion_positivo.py  (FORMA 1, dataset/ y docs/plan/)
# ==========================================================================
_forma1(
    "vuelta143_2c_mutacion_positivo.py",
    '("dataset/", "docs/plan/")',
    'def main():\n'
    '    sys.stdout.reconfigure(encoding="utf-8")\n'
    '    resultados = []\n',
    '''    resultados.append(("P.16 dataset/ y docs/plan/ SIN TOCAR tras la mutacion", sucio == ""))
    print("")
    print("git status --porcelain -- dataset/ docs/plan/ : %r" % sucio)
''',
    '''    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LA LINEA VIEJA QUEDA AQUI,
    # TACHADA Y LEGIBLE:
    #     ~~resultados.append(("P.16 dataset/ y docs/plan/ SIN TOCAR tras la mutacion", sucio == ""))~~
    #     ~~print("git status --porcelain -- dataset/ docs/plan/ : %r" % sucio)~~
    # EL VEREDICTO PASA A LA HUELLA DE CONTENIDO. git status queda como INFORME.
    _p16_despues = _HC.huella(*_P16_RUTAS)
    _p16_ok, _p16_linea = _HC.comparar(_p16_antes, _p16_despues, *_P16_RUTAS)
    resultados.append(("P.16 dataset/ y docs/plan/ SIN TOCAR tras la mutacion", _p16_ok))
    print("")
    print(_p16_linea)
    print("git status --porcelain -- dataset/ docs/plan/ (INFORME, no vara) : %r" % sucio)
''')

# ==========================================================================
# 4. vuelta144_3a_mutaciones.py  (FORMA 1, dataset/ y docs/plan/)
# ==========================================================================
_forma1(
    "vuelta144_3a_mutaciones.py",
    '("dataset/", "docs/plan/")',
    'def main():\n'
    '    op = ficha("OP-M-04")\n',
    '''    print("")
    print("P.16, dataset/ y docs/plan/ SIN TOCAR tras las mutaciones: %s" % (not sucio))
    if sucio:
        for ln in sucio.splitlines():
            print("   %s" % ln)
    print("")
    print("MUTACIONES QUE MUERDEN: %d de %d" % (buenas, len(resultados)))
    return 0 if buenas == len(resultados) and not sucio else 1
''',
    '''    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS QUEDAN
    # AQUI, TACHADAS Y LEGIBLES:
    #     ~~print("P.16, dataset/ y docs/plan/ SIN TOCAR tras las mutaciones: %s" % (not sucio))~~
    #     ~~return 0 if buenas == len(resultados) and not sucio else 1~~
    # EL VEREDICTO PASA A LA HUELLA DE CONTENIDO. git status queda como INFORME.
    _p16_despues = _HC.huella(*_P16_RUTAS)
    _p16_ok, _p16_linea = _HC.comparar(_p16_antes, _p16_despues, *_P16_RUTAS)
    print("")
    print(_p16_linea)
    print("git status --porcelain -- dataset/ docs/plan/ (INFORME, no vara): %s" % (not sucio))
    if sucio:
        for ln in sucio.splitlines():
            print("   %s" % ln)
    print("")
    print("MUTACIONES QUE MUERDEN: %d de %d" % (buenas, len(resultados)))
    return 0 if buenas == len(resultados) and _p16_ok else 1
''')

# ==========================================================================
# 5. vuelta143_3c_girar_arista.py  (FORMA 3, el que escribe a proposito)
# ==========================================================================
_forma1(
    "vuelta143_3c_girar_arista.py",
    '("dataset/nodos/",)',
    '    ap.add_argument("--mutacion-negativa", action="store_true", dest="mutacion")\n'
    '    arg = ap.parse_args()\n'
    '    sys.stdout.reconfigure(encoding="utf-8")\n',
    '''    print("git status --porcelain -- dataset/nodos/ tras el giro:")
    for ln in sucio.splitlines():
        print("   %s" % ln)
    return 0
''',
    '''    # REMEDIO DE LA FORMA 3 (vuelta 160, TAREA 3.a), Y SE DECLARA POR QUE ES
    # DISTINTO: este fichero NO es un arnes de mutacion, es LA OPERACION que
    # gira la arista y ESCRIBE dos ficheros de nodo. Su git status nunca fue un
    # veredicto: era el informe de lo que acababa de escribir. La huella se
    # toma igual, antes y despues, PERO AQUI DEBE CAMBIAR, y por eso se imprime
    # como informe y no como vara. Fabricarle un veredicto que no le
    # corresponde seria peor que decir que este caso es distinto.
    _p16_despues = _HC.huella(*_P16_RUTAS)
    _p16_igual, _p16_linea = _HC.comparar(_p16_antes, _p16_despues, *_P16_RUTAS)
    print("P.16 (INFORME, NO VARA: este script escribe A PROPOSITO, asi que la huella")
    print("     TIENE que cambiar cuando se corre con --ejecutar): huella igual = %s"
          % _p16_igual)
    print("     %s" % _p16_linea)
    print("git status --porcelain -- dataset/nodos/ tras el giro:")
    for ln in sucio.splitlines():
        print("   %s" % ln)
    return 0
''')

# ==========================================================================
# 6. vuelta144_2b_mutacion_giro.py  (FORMA 2, funcion estado_dataset)
# ==========================================================================
EDICIONES.append(("vuelta144_2b_mutacion_giro.py", [
    ('''def estado_dataset():
    return subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                          cwd=RAIZ, capture_output=True, text=True).stdout
''',
     _preambulo_modulo('("dataset/",)') + '''

def estado_dataset():
    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS QUEDAN
    # AQUI, TACHADAS Y LEGIBLES:
    #     ~~return subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],~~
    #     ~~                      cwd=RAIZ, capture_output=True, text=True).stdout~~
    # ESTA FUNCION SE LLAMA ANTES Y DESPUES DE CADA MUTACION, o sea que la
    # figura ya era la correcta y lo que fallaba era el instrumento. Devuelve la
    # HUELLA DE CONTENIDO y con eso el arnes deja de depender del fin de linea y
    # de la suciedad anterior al arranque, que son las dos anclas de la 6.7.
    return _HC.huella(*_P16_RUTAS)
'''),
    ('''    print("ESTADO FINAL DE dataset/: %d fila(s) en git status, identico al de la apertura "
          "del arnes: %s" % (len(final.splitlines()), final == antes))
''',
     '''    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LA LINEA VIEJA, TACHADA:
    #     ~~print("ESTADO FINAL DE dataset/: %d fila(s) en git status, identico al de la apertura "~~
    #     ~~      "del arnes: %s" % (len(final.splitlines()), final == antes))~~
    # La huella no devuelve filas de git status, devuelve (sha256, conteo).
    _, _p16_linea = _HC.comparar(antes, final, *_P16_RUTAS)
    print("ESTADO FINAL DE dataset/: %d fichero(s) bajo la huella, identico al de la "
          "apertura del arnes: %s" % (final[1], final == antes))
    print("   %s" % _p16_linea)
'''),
]))

# ==========================================================================
# 7. vuelta144_3b_giro_sin_flecha.py  (FORMA 2, dos tomas sueltas)
# ==========================================================================
EDICIONES.append(("vuelta144_3b_giro_sin_flecha.py", [
    ('''import vuelta143_3c_girar_arista as G  # noqa: E402
''',
     '''import vuelta143_3c_girar_arista as G  # noqa: E402
''' + _preambulo_modulo('("dataset/",)')),
    ('''    antes_disco = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                                 cwd=RAIZ, capture_output=True, text=True).stdout
''',
     '''    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS, TACHADAS:
    #     ~~antes_disco = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],~~
    #     ~~                             cwd=RAIZ, capture_output=True, text=True).stdout~~
    # Este arnes YA comparaba antes contra despues: la figura era correcta y el
    # instrumento no. La huella no mira a git.
    antes_disco = _HC.huella(*_P16_RUTAS)
'''),
    ('''    despues_disco = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                                   cwd=RAIZ, capture_output=True, text=True).stdout
''',
     '''    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS, TACHADAS:
    #     ~~despues_disco = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],~~
    #     ~~                               cwd=RAIZ, capture_output=True, text=True).stdout~~
    despues_disco = _HC.huella(*_P16_RUTAS)
'''),
    ('''    print("CERO ESCRITURAS en dataset/: %s" % sin_escrituras)
''',
     '''    print("CERO ESCRITURAS en dataset/: %s" % sin_escrituras)
    print("   %s" % _HC.comparar(antes_disco, despues_disco, *_P16_RUTAS)[1])
'''),
]))

# ==========================================================================
# 8. vuelta144_3b_mutacion_negativa.py  (FORMA 2, funcion estado)
# ==========================================================================
EDICIONES.append(("vuelta144_3b_mutacion_negativa.py", [
    ('''def estado():
    return subprocess.run(["git", "status", "--porcelain", "--", "dataset/", "docs/loop/"],
                          cwd=RAIZ, capture_output=True, text=True).stdout
''',
     _preambulo_modulo('("dataset/", "docs/loop/")') + '''

def estado():
    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS, TACHADAS:
    #     ~~return subprocess.run(["git", "status", "--porcelain", "--", "dataset/", "docs/loop/"],~~
    #     ~~                      cwd=RAIZ, capture_output=True, text=True).stdout~~
    #     ~~print("CERO ESCRITURAS: git status -- dataset/ docs/loop/ identico al de la apertura "~~
    #     ~~      "del arnes: %s" % igual)~~
    # Se llama ANTES y DESPUES: la figura era correcta y el instrumento no.
    return _HC.huella(*_P16_RUTAS)
'''),
    ('''    print("CERO ESCRITURAS: git status -- dataset/ docs/loop/ identico al de la apertura "
          "del arnes: %s" % igual)
''',
     '''    print("CERO ESCRITURAS: huella de CONTENIDO de dataset/ y docs/loop/ identica a la "
          "de la apertura del arnes: %s" % igual)
    print("   %s" % _HC.comparar(antes, despues, *_P16_RUTAS)[1])
'''),
]))

# ==========================================================================
# 9. vuelta146_3c_mutacion_aduana.py  (FORMA 2, funcion estado_dataset)
# ==========================================================================
EDICIONES.append(("vuelta146_3c_mutacion_aduana.py", [
    ('''def estado_dataset():
    r = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                       cwd=RAIZ, capture_output=True, text=True)
    return r.stdout
''',
     _preambulo_modulo('("dataset/",)') + '''

def estado_dataset():
    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS, TACHADAS:
    #     ~~r = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],~~
    #     ~~                   cwd=RAIZ, capture_output=True, text=True)~~
    #     ~~return r.stdout~~
    # Se llama ANTES y DESPUES: la figura era correcta y el instrumento no.
    return _HC.huella(*_P16_RUTAS)
'''),
    ('''    print("dataset/ IDENTICO antes y despues (cero escrituras): %s" % dataset_intacto)
''',
     '''    print("dataset/ IDENTICO antes y despues (cero escrituras): %s" % dataset_intacto)
    print("   %s" % _HC.comparar(antes, despues, *_P16_RUTAS)[1])
'''),
]))

# ==========================================================================
# 10. vuelta147_3d_mutacion_nomina.py  (FORMA 2, funcion estado_dataset)
# ==========================================================================
EDICIONES.append(("vuelta147_3d_mutacion_nomina.py", [
    ('''def estado_dataset():
    r = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"], cwd=RAIZ,
                       capture_output=True, text=True)
    return r.stdout
''',
     _preambulo_modulo('("dataset/",)') + '''

def estado_dataset():
    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS, TACHADAS:
    #     ~~r = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"], cwd=RAIZ,~~
    #     ~~                   capture_output=True, text=True)~~
    #     ~~return r.stdout~~
    # Se llama ANTES y DESPUES: la figura era correcta y el instrumento no.
    return _HC.huella(*_P16_RUTAS)
'''),
    ('''    print("  dataset/ ANTES  : %s" % (antes.strip() or "(sin cambios)"))
    print("  dataset/ DESPUES: %s" % (despues.strip() or "(sin cambios)"))
''',
     '''    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS, TACHADAS:
    #     ~~print("  dataset/ ANTES  : %s" % (antes.strip() or "(sin cambios)"))~~
    #     ~~print("  dataset/ DESPUES: %s" % (despues.strip() or "(sin cambios)"))~~
    # La huella no devuelve texto de git status, devuelve (sha256, conteo).
    print("  dataset/ ANTES  : sha256 %s sobre %d fichero(s)" % (antes[0][:16], antes[1]))
    print("  dataset/ DESPUES: sha256 %s sobre %d fichero(s)" % (despues[0][:16], despues[1]))
    print("  %s" % _HC.comparar(antes, despues, *_P16_RUTAS)[1])
'''),
]))

# ==========================================================================
# 11. vuelta147_3e_simular_a26.py  (FORMA 2, funcion estado_dataset)
# ==========================================================================
EDICIONES.append(("vuelta147_3e_simular_a26.py", [
    ('''def estado_dataset():
    r = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"], cwd=RAIZ,
                       capture_output=True, text=True)
    return r.stdout
''',
     _preambulo_modulo('("dataset/",)') + '''

def estado_dataset():
    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS, TACHADAS:
    #     ~~r = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"], cwd=RAIZ,~~
    #     ~~                   capture_output=True, text=True)~~
    #     ~~return r.stdout~~
    # Se llama ANTES y DESPUES: la figura era correcta y el instrumento no.
    return _HC.huella(*_P16_RUTAS)
'''),
    ('''    print("  dataset/ ANTES  : %s" % (antes.strip() or "(sin cambios)"))
    print("  dataset/ DESPUES: %s" % (despues.strip() or "(sin cambios)"))
''',
     '''    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS, TACHADAS:
    #     ~~print("  dataset/ ANTES  : %s" % (antes.strip() or "(sin cambios)"))~~
    #     ~~print("  dataset/ DESPUES: %s" % (despues.strip() or "(sin cambios)"))~~
    print("  dataset/ ANTES  : sha256 %s sobre %d fichero(s)" % (antes[0][:16], antes[1]))
    print("  dataset/ DESPUES: sha256 %s sobre %d fichero(s)" % (despues[0][:16], despues[1]))
    print("  %s" % _HC.comparar(antes, despues, *_P16_RUTAS)[1])
'''),
]))

# ==========================================================================
# 12. vuelta89_tarea4_guarda_op_c05.py  (FORMA 2, y RETIRA UNA PARADA)
# ==========================================================================
EDICIONES.append(("vuelta89_tarea4_guarda_op_c05.py", [
    ('''RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
''',
     '''RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
''' + _preambulo_modulo('("dataset/",)')),
    ('''    r_antes = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                             cwd=RAIZ, capture_output=True, text=True)
    print("git status --porcelain -- dataset/ ANTES: %r" % r_antes.stdout)
    if r_antes.stdout.strip():
        raise SystemExit("ROJO: dataset/ ya tenia cambios antes del caso rojo: no se corre "
                          "sobre un arbol sucio")
''',
     '''    _p16_antes = _HC.huella(*_P16_RUTAS)
    r_antes = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                             cwd=RAIZ, capture_output=True, text=True)
    print("P.16 huella de CONTENIDO de dataset/ ANTES: sha256 %s sobre %d fichero(s)"
          % (_p16_antes[0][:16], _p16_antes[1]))
    print("git status --porcelain -- dataset/ ANTES (INFORME, no vara): %r" % r_antes.stdout)
    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS QUEDAN
    # AQUI, TACHADAS Y LEGIBLES, y esta es LA PARADA QUE EL REMEDIO RETIRA:
    #     ~~print("git status --porcelain -- dataset/ ANTES: %r" % r_antes.stdout)~~
    #     ~~if r_antes.stdout.strip():~~
    #     ~~    raise SystemExit("ROJO: dataset/ ya tenia cambios antes del caso rojo: no se corre "~~
    #     ~~                      "sobre un arbol sucio")~~
    # ERA EL ANCLA 2 DE LA 6.7 EN SU FORMA MAS PURA: el caso rojo se negaba a
    # correr por suciedad QUE NO ERA SUYA. Este script no escribe en dataset/ ni
    # una vez (su caso rojo vive entero en un directorio temporal), asi que la
    # suciedad anterior no puede falsear su medicion; lo que hay que probar es
    # que EL no escribio, y eso lo prueba la huella comparada consigo misma al
    # final. La suciedad anterior SE SIGUE IMPRIMIENDO, como informe.
'''),
    ('''    r_despues = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                               cwd=RAIZ, capture_output=True, text=True)
    print("git status --porcelain -- dataset/ DESPUES: %r" % r_despues.stdout)
    if r_despues.stdout.strip():
        raise SystemExit("ROJO: dataset/ quedo con cambios tras el caso rojo: el caso rojo "
                          "tiene que ser puramente en memoria")
''',
     '''    _p16_despues = _HC.huella(*_P16_RUTAS)
    r_despues = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                               cwd=RAIZ, capture_output=True, text=True)
    print("git status --porcelain -- dataset/ DESPUES (INFORME, no vara): %r" % r_despues.stdout)
    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS, TACHADAS:
    #     ~~print("git status --porcelain -- dataset/ DESPUES: %r" % r_despues.stdout)~~
    #     ~~if r_despues.stdout.strip():~~
    #     ~~    raise SystemExit("ROJO: dataset/ quedo con cambios tras el caso rojo: el caso rojo "~~
    #     ~~                      "tiene que ser puramente en memoria")~~
    # EL VEREDICTO PASA A LA HUELLA, comparada consigo misma: SIGUE SALIENDO
    # ROJO si este script escribio, y ya no cae por lo que otro dejo sucio ni
    # por un fin de linea.
    _p16_ok, _p16_linea = _HC.comparar(_p16_antes, _p16_despues, *_P16_RUTAS)
    print(_p16_linea)
    if not _p16_ok:
        raise SystemExit("ROJO: dataset/ quedo con cambios tras el caso rojo: el caso rojo "
                          "tiene que ser puramente en memoria")
'''),
]))


def numstat(ruta_rel):
    r = subprocess.run(["git", "diff", "--numstat", "--", ruta_rel],
                       cwd=RAIZ, capture_output=True)
    linea = r.stdout.decode("utf-8", "replace").strip()
    if not linea:
        return 0, 0
    campos = linea.split("\t")
    return int(campos[0]), int(campos[1])


def main():
    print("=" * 78)
    print("VUELTA 160, TAREA 3.a: EL REMEDIO DEL CHECK DE P.16, EN LOS DOCE")
    print("=" * 78)
    print("")

    esperados = nomina_del_fichero_de_salida()
    editados = sorted(f for f, _ in EDICIONES)
    print("A) EL ALCANCE, CONTADO DE SU FICHERO ANTES DE TOCAR NADA")
    print("   fuente: docs/loop/SALIDA_V159_T5_ALCANCE.txt, seccion C")
    print("   CIFRA ficheros del alcance: %d" % len(esperados))
    print("   CIFRA ficheros que este instrumento edita: %d" % len(editados))
    assert esperados == editados, (
        "EL ALCANCE Y LAS EDICIONES NO CALZAN.\n  del fichero: %s\n  editados: %s"
        % (esperados, editados))
    print("   LAS DOS NOMINAS SALEN IDENTICAS, ELEMENTO A ELEMENTO.")
    assert len(editados) == 12, "no son doce: son %d" % len(editados)
    print("   Y SON DOCE, que es lo que la 6.1 del acta 159 adjudica.")
    print("")

    print("B) LAS EDICIONES, UNA A UNA. El texto viejo tiene que aparecer")
    print("   EXACTAMENTE UNA VEZ o el instrumento para.")
    hechos, ya = [], []
    for fichero, pares in EDICIONES:
        ruta = os.path.join(LOOP, fichero)
        texto = leer(ruta)
        if MARCA in texto:
            ya.append(fichero)
            print("   %-46s YA ESTABA" % fichero)
            continue
        for i, (viejo, nuevo) in enumerate(pares, 1):
            n = texto.count(viejo)
            assert n == 1, ("%s, edicion %d: el texto viejo aparece %d veces y "
                            "tiene que aparecer 1. PARADA, no se escribe nada.\n%r"
                            % (fichero, i, n, viejo[:120]))
            texto = texto.replace(viejo, nuevo)
        escribir(ruta, texto)
        hechos.append(fichero)
        print("   %-46s REMEDIADO  (%d edicion(es))" % (fichero, len(pares)))
    print("")
    print("CIFRA ficheros remediados en esta corrida: %d" % len(hechos))
    print("CIFRA ficheros que ya estaban: %d" % len(ya))
    print("")

    print("C) LA CONSECUENCIA QUE SE DECLARA: EL ALCANCE NO SE MUEVE")
    print("   La linea vieja no se borra, queda TACHADA en un comentario, asi que")
    print("   los doce SIGUEN casando con el patron literal de la lectura B.")
    patron = '"--porcelain", "--", "dataset/'
    siguen = [f for f, _ in EDICIONES if patron in leer(os.path.join(LOOP, f))]
    print("   CIFRA de los doce que siguen casando con el patron: %d" % len(siguen))
    assert len(siguen) == 12, ("el remedio saco a %d fichero(s) del alcance: %s"
                               % (12 - len(siguen),
                                  [f for f, _ in EDICIONES if f not in siguen]))
    print("   LOS DOCE. El alcance de la 6.1 sigue siendo doce despues del remedio.")
    print("")

    print("D) QUE CAMBIO EN CADA UNO, con git diff --numstat")
    mas_total = menos_total = 0
    for fichero, _ in EDICIONES:
        mas, menos = numstat("scripts/loop/" + fichero)
        mas_total += mas
        menos_total += menos
        print("   %-46s mas %-5d menos %d" % (fichero, mas, menos))
    print("   CIFRA lineas anadidas: %d" % mas_total)
    print("   CIFRA lineas retiradas: %d" % menos_total)
    print("   LAS RETIRADAS NO SON BORRADOS SILENCIOSOS: cada una de las lineas")
    print("   que dejo de ejecutarse esta escrita ARRIBA, TACHADA Y LEGIBLE, en el")
    print("   comentario de su propia correccion declarada. Eso se comprueba en la")
    print("   seccion E y no se promete.")
    print("")

    print("E) LA COMPROBACION DE QUE NINGUNA LINEA SE PERDIO SIN TACHAR")
    print("   Toda linea que el diff retira tiene que aparecer, en el mismo")
    print("   fichero, dentro de un comentario con la marca ~~ de tachado.")
    huerfanas = []
    for fichero, _ in EDICIONES:
        rel = "scripts/loop/" + fichero
        r = subprocess.run(["git", "diff", "-U0", "--", rel], cwd=RAIZ,
                           capture_output=True)
        diff = r.stdout.decode("utf-8", "replace")
        texto = leer(os.path.join(LOOP, fichero))
        tachadas = [l for l in texto.splitlines()
                    if l.strip().startswith("#") and "~~" in l]
        cuerpo_tachado = "\n".join(tachadas)
        for linea in diff.splitlines():
            if not linea.startswith("-") or linea.startswith("---"):
                continue
            quitada = linea[1:].strip()
            if not quitada:
                continue
            if quitada not in cuerpo_tachado:
                huerfanas.append((fichero, quitada))
    print("   CIFRA lineas retiradas SIN su copia tachada: %d" % len(huerfanas))
    for f, l in huerfanas:
        print("      %s :: %s" % (f, l[:100]))
    assert not huerfanas, "hay lineas retiradas sin tachar: la aditividad esta rota"
    print("   NINGUNA. Todo lo que dejo de ejecutarse sigue legible en su fichero.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
