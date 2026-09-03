# -*- coding: utf-8 -*-
"""vuelta160_tarea6b_mutacion_puerta.py . TAREA 6.b DE LA VUELTA 160.

EL CASO POSITIVO POR MUTACION DE LA ADJUDICACION 6.9 DEL ACTA 159: la puerta del
corredor no puede decir `(no hallado)` de un commit que hallo.

EL ENCARGO PIDE DOS COSAS Y VAN LAS DOS, MAS DOS QUE ANADO YO PARA QUE LA PRUEBA
SIGNIFIQUE ALGO:

  CASO 1, EL ROJO QUE TIENE QUE SEGUIR CAYENDO Y AHORA ADEMAS NOMBRAR. Una
  corrida SIN ficheros de apertura tiene que SEGUIR SALIENDO ROJO, y su cabecera
  tiene que NOMBRAR el commit del acta en vez de decir `(no hallado)`.

  CASO 2, EL `(no hallado)` QUE TIENE QUE SOBREVIVIR. Una corrida en un estado
  donde el acta DE VERDAD no existe tiene que seguir diciendo `(no hallado)`. Si
  el remedio matara esa palabra, habria cambiado una mentira por otra.

  CASO 3, EL CONTRASTE CONTRA EL CODIGO VIEJO, Y NO SE AFIRMA, SE CORRE. La
  version ANTERIOR de la guarda se saca de git (`git show HEAD:...`), se carga
  como modulo aparte y se le da EL MISMO ESCENARIO del caso 1. Tiene que
  imprimir `(no hallado)`. Sin esto, el caso 1 no probaria que se remedio nada:
  probaria solo que hoy funciona.

  CASO 4, QUE NINGUN VEREDICTO SE MOVIO. El remedio dice que no toca ningun
  veredicto. Se comprueba corriendo la guarda de verdad sobre la vuelta 160 (que
  es VERDE) y sobre la vuelta 100 (que es el ROJO historico de esta guarda, ocho
  ficheros nacidos en el ultimo commit de su vuelta) y cotejando los dos codigos
  de salida contra los que la version vieja da sobre los mismos dos.

COMO SE MUTA, Y SE DECLARA: `ficheros_apertura` se sustituye por una que
devuelve la lista vacia (caso 1 y 3) y `commit_acta` por una que devuelve None
(caso 2). No se toca ningun fichero del arbol: la mutacion vive en memoria y las
dos funciones se restauran en un `finally`.

--- DOS CAIDAS MIAS EN LA PRIMERA CORRIDA DE ESTE ARNES, DECLARADAS AQUI EN VEZ
    DE ARREGLADAS EN SILENCIO ---

CAIDA 1, DE MUTACION MAL FABRICADA (caso 2). Mi primera mutacion de
`commit_acta` devolvia `None` SIN ANADIR NADA A `fallos`, y con eso la guarda
salia VERDE (exit 0) y el caso 2 caia. Pero ESE ESTADO NO EXISTE EN EL CODIGO
REAL: leido `commit_acta` entero, sus dos salidas con `None` anaden su fallo
antes de volver, asi que la guarda nunca puede quedarse verde por ahi. LA
MUTACION ESTABA MAL, NO EL CODIGO. Se corrige la mutacion para que respete el
contrato de la funcion real (anade su fallo y devuelve None) y se dice de donde
salio. Una mutacion que fabrica un estado imposible no prueba nada.

CAIDA 2, DE ARNES, Y ESTA HABRIA HECHO PASAR UN CASO POR EL MOTIVO EQUIVOCADO
(casos 3 y 4). La version vieja se carga desde un fichero temporal, y su `RAIZ`
se computa de SU PROPIO `__file__`: apuntaba al directorio temporal, no al repo.
Con eso el modulo viejo no encontraba NADA, y su `(no hallado)` del caso 3 podia
venir de la ruta rota y no del defecto que se queria reproducir. El caso 4 lo
delato al dar exit 1 sobre la vuelta 160, que es VERDE. Se corrige forzando
`RAIZ` y `LOOP` del modulo cargado a los del repo, y se declara: sin esta
correccion, el caso 3 habria salido OK POR EL MOTIVO EQUIVOCADO.

--- CORRECCION DECLARADA (vuelta 163, TAREA 2; adjudicacion 6.8 del acta 162) ---

EL CASO 3 ESTABA ANCLADO A `HEAD` Y ESO ES UN FALSO VERDE ESPERANDO SU DIA, con
esas palabras y en este mismo repo: lo escribio
`scripts/loop/vuelta154_tarea2d_mutacion_guarda.py` en su propia cabecera seis
vueltas antes. Este arnes nace en `e8a30e83`, que es EL COMMIT DEL REMEDIO, y
saca su "version vieja" de `git show HEAD:...`. El dia que nacio, `HEAD` todavia
era la guarda de antes y el caso 3 mordia; desde el commit siguiente `HEAD` ES
LA GUARDA NUEVA, asi que el caso 3 comparaba el remedio consigo mismo y salia
`ROJO: 1 de 4 no se comportan`. Otro arnes caducado dentro de su propio commit.

EL ARREGLO ES EL DE LA 154, Y SE COPIA A PROPOSITO: la version vieja se saca de
una REFERENCIA FIJA Y COMPUTADA, el HEAD DE APERTURA de la vuelta 160 leido de
`docs/loop/SALIDA_V160_HEAD_APERTURA.txt`, que es el arbol de ANTES del remedio
y que ningun commit posterior puede mover. Ni un hash tecleado: el ref sale del
fichero sellado. Si ese fichero faltara, el arnes PARA en vez de caer hacia
`HEAD` y fingir un contraste.

USO:  python scripts/loop/vuelta160_tarea6b_mutacion_puerta.py
"""
import importlib.util
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import verificar_apertura_sellada as G  # noqa: E402

REL = "scripts/loop/verificar_apertura_sellada.py"


class Capturada(object):
    def __init__(self):
        self.trozos = []

    def write(self, s):
        self.trozos.append(s)
        return len(s)

    def flush(self):
        pass

    def valor(self):
        return "".join(self.trozos)


def correr(modulo, vuelta, sin_ficheros=False, sin_acta=False):
    """Corre modulo.main() con --vuelta VUELTA y las mutaciones pedidas.
    Devuelve (codigo, salida). Las funciones se restauran siempre."""
    real_ficheros = modulo.ficheros_apertura
    real_acta = modulo.commit_acta
    real_argv, real_out = sys.argv, sys.stdout
    buf = Capturada()
    try:
        if sin_ficheros:
            modulo.ficheros_apertura = lambda v: []
        if sin_acta:
            # LA MUTACION RESPETA EL CONTRATO DE LA FUNCION REAL (ver la caida 1
            # declarada arriba): `commit_acta` NUNCA devuelve None sin anadir su
            # fallo, asi que la mutacion tampoco.
            def _sin_acta(v, r, f):
                f.append("MUTACION DEL ARNES: se simula que git log no trae "
                         "ningun commit 'ACTA DE LA VUELTA %d DEL AUDITOR'" % (v - 1))
                return None
            modulo.commit_acta = _sin_acta
        sys.argv = ["verificar_apertura_sellada.py", "--vuelta", str(vuelta)]
        sys.stdout = buf
        try:
            codigo = modulo.main()
        except SystemExit as e:
            codigo = e.code if isinstance(e.code, int) else 1
    finally:
        modulo.ficheros_apertura = real_ficheros
        modulo.commit_acta = real_acta
        sys.argv, sys.stdout = real_argv, real_out
    return codigo, buf.valor()


# EL REF FIJO DEL CONTRASTE, Y NO SE TECLEA: sale del HEAD DE APERTURA sellado
# de la vuelta 160, que es el arbol de ANTES del remedio (el remedio es e8a30e83,
# de esa misma vuelta). `HEAD` no vale: ver la correccion declarada de la
# cabecera.
SELLO_APERTURA_160 = os.path.join(RAIZ, "docs", "loop", "SALIDA_V160_HEAD_APERTURA.txt")


def ref_del_contraste():
    """El ref FIJO del que se saca la guarda vieja, leido del sello de apertura
    de la vuelta 160. Devuelve None si no se puede leer: sin ref fijo NO se cae
    hacia HEAD, se para."""
    if not os.path.exists(SELLO_APERTURA_160):
        return None
    ref = io.open(SELLO_APERTURA_160, encoding="utf-8").read().strip().split()[0]
    return ref or None


def cargar_version_vieja():
    """La version ANTERIOR de la guarda, sacada de git EN UN REF FIJO y cargada
    como modulo aparte. No se toca el arbol de trabajo."""
    ref = ref_del_contraste()
    if not ref:
        return None, None
    r = subprocess.run(["git", "show", "%s:%s" % (ref, REL)], cwd=RAIZ,
                       capture_output=True)
    if r.returncode != 0:
        return None, None
    fuente = r.stdout.decode("utf-8", "replace")
    tmp = tempfile.mkdtemp()
    ruta = os.path.join(tmp, "_v160_guarda_vieja.py")
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(fuente)
    spec = importlib.util.spec_from_file_location("_v160_guarda_vieja", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # SIN ESTAS DOS LINEAS EL CONTRASTE NO VALE (ver la caida 2 declarada
    # arriba): el modulo cargado computa su RAIZ de su propio __file__, que esta
    # en un directorio temporal, y entonces no halla ni el repo ni las salidas.
    # Su (no hallado) vendria de la ruta rota y no del defecto.
    mod.RAIZ = RAIZ
    mod.LOOP = os.path.join(RAIZ, "docs", "loop")
    return mod, fuente


def commit_acta_real():
    """El hash del acta 159, leido de git y no tecleado."""
    r = subprocess.run(["git", "log", "--format=%H %s", "-n", "500"], cwd=RAIZ,
                       capture_output=True)
    for linea in r.stdout.decode("utf-8", "replace").splitlines():
        h, _, asunto = linea.partition(" ")
        if asunto.startswith("ACTA DE LA VUELTA 159 DEL AUDITOR"):
            return h
    return None


def main():
    print("=" * 78)
    print("VUELTA 160, TAREA 6.b: CASO POSITIVO POR MUTACION DE LA PUERTA DEL CORREDOR")
    print("=" * 78)
    print("")

    acta = commit_acta_real()
    print("EL COMMIT DEL ACTA 159, LEIDO DE git log Y NO TECLEADO: %s" % acta)
    assert acta, "no se hallo el acta 159 en la rama: el arnes no puede probar nada"
    corto = acta[:8]
    print("")

    ref = ref_del_contraste()
    viejo, _ = cargar_version_vieja()
    print("EL REF FIJO DEL CONTRASTE, LEIDO DE docs/loop/SALIDA_V160_HEAD_APERTURA.txt")
    print("Y NO TECLEADO: %s" % ref)
    print("LA VERSION VIEJA, SACADA DE git show %s:%s : %s"
          % ((ref or "(sin ref)")[:8], REL, "cargada" if viejo else "NO SE PUDO CARGAR"))
    assert viejo is not None, "sin la version vieja no hay contraste que correr"
    print("")

    resultados = []

    # ----------------------------------------------------------------------
    print("CASO 1: SIN FICHEROS DE APERTURA, SIGUE ROJO Y AHORA NOMBRA EL ACTA")
    print("-" * 78)
    c1, s1 = correr(G, 160, sin_ficheros=True)
    rojo1 = c1 != 0
    nombra1 = ("COMMIT DEL ACTA %s" % corto) in s1
    miente1 = "COMMIT DEL ACTA (no hallado)" in s1
    ok1 = rojo1 and nombra1 and not miente1
    print("   codigo de salida: %r (ROJO: %s)" % (c1, rojo1))
    print("   la cabecera NOMBRA el acta %s: %s" % (corto, nombra1))
    print("   la cabecera dice (no hallado): %s" % miente1)
    for ln in s1.splitlines()[:2] + [l for l in s1.splitlines() if l.startswith("ROJO")]:
        print("      | %s" % ln[:140])
    print("   VEREDICTO: %s" % ("OK" if ok1 else "ROJO"))
    resultados.append(("CASO 1, sin ficheros: sigue ROJO y nombra el acta", ok1))
    print("")

    # ----------------------------------------------------------------------
    print("CASO 2: CON UN ACTA QUE DE VERDAD NO EXISTE, SIGUE DICIENDO (no hallado)")
    print("-" * 78)
    c2, s2 = correr(G, 160, sin_acta=True)
    rojo2 = c2 != 0
    dice2 = "COMMIT DEL ACTA (no hallado)" in s2
    ok2 = rojo2 and dice2
    print("   codigo de salida: %r (ROJO: %s)" % (c2, rojo2))
    print("   la cabecera dice (no hallado), que aqui es la verdad: %s" % dice2)
    for ln in s2.splitlines()[:2]:
        print("      | %s" % ln[:140])
    print("   VEREDICTO: %s" % ("OK" if ok2 else "ROJO"))
    resultados.append(("CASO 2, sin acta de verdad: (no hallado) sobrevive", ok2))
    print("")

    # ----------------------------------------------------------------------
    print("CASO 3: EL CODIGO VIEJO, MISMO ESCENARIO DEL CASO 1, TIENE QUE MENTIR")
    print("-" * 78)
    c3, s3 = correr(viejo, 160, sin_ficheros=True)
    miente3 = "COMMIT DEL ACTA (no hallado)" in s3
    rojo3 = c3 != 0
    ok3 = miente3 and rojo3
    print("   codigo de salida del VIEJO: %r (ROJO: %s)" % (c3, rojo3))
    print("   el VIEJO dice (no hallado) sobre un acta que SI hallo: %s" % miente3)
    for ln in s3.splitlines()[:2]:
        print("      | %s" % ln[:140])
    print("   EL DEFECTO SE REPRODUCE EN EL CODIGO VIEJO Y NO EN EL NUEVO, que es")
    print("   lo que convierte al caso 1 en prueba de un remedio y no en un")
    print("   VERDE que no dice nada.")
    print("   VEREDICTO: %s" % ("OK" if ok3 else "ROJO"))
    resultados.append(("CASO 3, el codigo viejo reproduce el defecto", ok3))
    print("")

    # ----------------------------------------------------------------------
    print("CASO 4: NINGUN VEREDICTO SE MOVIO, COTEJADO VIEJO CONTRA NUEVO")
    print("-" * 78)
    iguales = True
    for vuelta in (160, 100):
        cn, sn = correr(G, vuelta)
        cv, sv = correr(viejo, vuelta)
        igual = (cn == cv)
        iguales = iguales and igual
        print("   vuelta %d: nuevo exit %r | viejo exit %r | igual: %s"
              % (vuelta, cn, cv, igual))
        cabecera_n = sn.splitlines()[3] if len(sn.splitlines()) > 3 else ""
        print("      nuevo, primera linea de veredicto: %s" % cabecera_n[:120])
    print("   VEREDICTO: %s" % ("OK" if iguales else "ROJO"))
    resultados.append(("CASO 4, los codigos de salida no se movieron", iguales))
    print("")

    # ----------------------------------------------------------------------
    print("=" * 78)
    buenas = sum(1 for _, ok in resultados if ok)
    for nombre, ok in resultados:
        print("  %-5s %s" % ("OK" if ok else "ROJO", nombre))
    print("")
    print("CIFRA casos del arnes: %d" % len(resultados))
    print("CIFRA casos que se comportan: %d" % buenas)
    print("=" * 78)
    if buenas != len(resultados):
        print("ROJO: %d de %d no se comportan." % (len(resultados) - buenas, len(resultados)))
        return 1
    print("VERDE: los %d se comportan. LA PUERTA YA NO DICE (no hallado) DE UN"
          % buenas)
    print("COMMIT QUE HALLO, Y LO SIGUE DICIENDO CUANDO DE VERDAD NO LO HALLA.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
