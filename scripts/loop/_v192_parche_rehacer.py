# -*- coding: utf-8 -*-
r"""_v192_parche_rehacer.py . ANADE EL CARRIL `--rehacer` AL ESQUELETO DE LA
VUELTA 192.

CLON DECLARADO del carril que la vuelta 191 escribio en
`scripts/loop/vuelta191_esqueleto_reporte.py`, con su mismo texto y sus mismas
guardas. Se copia entero a proposito y se dice que es copia.

POR QUE HACE FALTA HOY: `cerrar_reporte.py` ESCRIBIO el reporte de la 192 y
DESPUES declaro ROJO por su guarda de las dos convenciones. El reporte del arbol
ya es un reporte CERRADO de la 192, asi que el PASO 0 del esqueleto no puede
volver a tallarlo: su archivador exigiria que un reporte de la vuelta 192 ya
estuviera archivado, y no lo esta ni debe estarlo. **El carril `--rehacer` afloja
EXACTAMENTE una cosa, el PASO 0, y a cambio exige algo que aqui es mas fuerte:
que el reporte que se va a pisar sea EL DE ESTA MISMA VUELTA y este COMMITEADO
sin cambios en el arbol.** Un reporte que vive en un commit no se pierde al
pisarlo: se recupera con `git show`.
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(RAIZ, "scripts", "loop", "vuelta192_esqueleto_reporte.py")
NL = chr(10)

ANCLA = """    # ---------------------------------------------- PASO 0.0, LA FUENTE DEL CLON"""

CARRIL = '''    # EL CARRIL `--rehacer`, CLON DECLARADO DEL DE LA VUELTA 191. QUE ES Y POR
    # QUE EXISTE HOY, MEDIDO Y NO SUPUESTO: `cerrar_reporte.py` ESCRIBIO el
    # reporte de esta vuelta y DESPUES declaro ROJO por su guarda de las dos
    # convenciones, con cuatro parejas de bytes nombradas. Arreglarlo obliga a RE
    # ESCRIBIR el reporte entero, y el PASO 0 lo impide con razon: su archivador
    # no puede archivar como vuelta 191 un REPORTE.md que ya es de la 192.
    #
    # QUE SE AFLOJA Y QUE NO. Se salta el PASO 0 y NADA MAS. A cambio se exige
    # algo que en este caso es MAS FUERTE que el archivado: que el reporte que se
    # va a pisar sea EL DE ESTA MISMA VUELTA y este COMMITEADO en git sin cambios
    # en el arbol. Un reporte parcial que vive en un commit no se pierde al
    # pisarlo: se recupera con `git show`. Si el arbol trae cambios sin commitear,
    # o si el reporte no es de esta vuelta, ESTE CARRIL CAE EN ROJO.
    if "--rehacer" in sys.argv:
        print("CARRIL --rehacer. EL PASO 0 SE SALTA Y SE DICE POR QUE.")
        rr = subprocess.run(["git", "status", "--porcelain", "--",
                             "docs/loop/REPORTE.md"], cwd=RAIZ, capture_output=True)
        sucio = rr.stdout.decode("utf-8", errors="replace").strip()
        texto_ahora = io.open(os.path.join(LOOP, "REPORTE.md"),
                              encoding="utf-8").read()
        n_ahora = vuelta_del_reporte_del_arbol(texto_ahora)
        c_last, last = git(["log", "-1", "--format=%H %s", "--",
                            "docs/loop/REPORTE.md"])
        print("   git status de docs/loop/REPORTE.md: %r" % (sucio or "(limpio)"))
        print("   vuelta del reporte que se va a pisar, leida de su cabecera: %s"
              % n_ahora)
        print("   ultimo commit que lo toca: %s" % last[:130])
        malos = []
        if sucio:
            malos.append("el reporte del arbol tiene cambios sin commitear")
        if n_ahora != VUELTA:
            malos.append("el reporte del arbol es el de la vuelta %s y no el de la %d"
                         % (n_ahora, VUELTA))
        if not last.strip():
            malos.append("ningun commit toca docs/loop/REPORTE.md")
        if malos:
            print("ROJO, el carril --rehacer NO escribe:")
            for m in malos:
                print("   " + m)
            sys.exit(1)
        print("   VERDE: lo que se va a pisar es el reporte de ESTA vuelta y vive")
        print("   entero en git. Se recupera con `git show`.")
        print("")

''' + ANCLA

VIEJO_P0 = """    ruta = os.path.join(LOOP, "REPORTE.md")
    texto_a_pisar = io.open(ruta, encoding="utf-8").read() if os.path.exists(ruta) else \"\""""
NUEVO_P0 = """    ruta = os.path.join(LOOP, "REPORTE.md")
    _rehacer = "--rehacer" in sys.argv
    texto_a_pisar = io.open(ruta, encoding="utf-8").read() if os.path.exists(ruta) else \"\""""

VIEJO_GUARDAS = '''    print("PASO 0.b. LA GUARDA SOBRE LA VUELTA ANTERIOR (%d), PUBLICADA SALGA LO"
          % (VUELTA - 1))'''
NUEVO_GUARDAS = '''    if _rehacer:
        print("PASO 0.b y 0.c: SALTADOS POR EL CARRIL --rehacer, y se dice.")
        print("")
        ok = True
    else:
        _guardas_del_paso0(n_arbol)

    print("EL DESFASE, CONTADO EN VEZ DE TECLEADO:")'''

VIEJO_DESFASE = '''    print("EL DESFASE, CONTADO EN VEZ DE TECLEADO:")'''


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    t = io.open(P, encoding="utf-8").read().replace(chr(13) + NL, NL)
    antes = len(t.encode("utf-8"))
    if "--rehacer" in t:
        print("   YA ESTABA: el carril --rehacer")
        return 0
    if ANCLA not in t or VIEJO_P0 not in t:
        print("   ROJO: no se encuentran las anclas. No se escribe nada.")
        return 1

    # 1. el carril, delante del PASO 0.0
    t = t.replace(ANCLA, CARRIL, 1)
    # 2. la bandera, en el PASO 0
    t = t.replace(VIEJO_P0, NUEVO_P0, 1)
    # 3. las guardas 0.b y 0.c, envueltas en una funcion para poder saltarlas
    i = t.index(VIEJO_GUARDAS)
    j = t.index(VIEJO_DESFASE)
    bloque = t[i:j]
    sangrado = NL.join(("    " + l) if l.strip() else l
                       for l in bloque.rstrip().split(NL))
    funcion = ('''

def _guardas_del_paso0(n_arbol):
    """LOS PASOS 0.b Y 0.c, ENVUELTOS PARA QUE EL CARRIL --rehacer PUEDA
    SALTARLOS Y NADA MAS. Su cuerpo no se toca: es el de siempre, sangrado."""
    ok = True
''' + sangrado + NL + '''    if not ok:
        print("ROJO: el esqueleto NO escribe. El reporte anterior no esta a salvo.")
        sys.exit(1)
    return ok

''')
    # la funcion va a nivel de modulo, antes del bloque __main__
    marca = 'if __name__ != "__main__":'
    if marca not in t:
        print("   ROJO: no se encuentra el bloque de modulo.")
        return 1
    t = t[:i] + NUEVO_GUARDAS + t[j + len(VIEJO_DESFASE):]
    t = t.replace(marca, funcion.lstrip(NL) + NL + marca, 1)

    io.open(P, "w", encoding="utf-8", newline=NL).write(t)
    print("   aplicado: el carril --rehacer y sus guardas envueltas")
    print("   vuelta192_esqueleto_reporte.py pasa de %d a %d bytes en disco"
          % (antes, len(t.encode("utf-8"))))
    import py_compile
    py_compile.compile(P, doraise=True)
    print("   COMPILA")
    return 0


if __name__ == "__main__":
    sys.exit(main())
