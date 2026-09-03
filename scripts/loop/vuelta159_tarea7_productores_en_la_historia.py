# -*- coding: utf-8 -*-
"""vuelta159_tarea7_productores_en_la_historia.py . TAREA 7 DE LA VUELTA 159.

LAS DOS SALIDAS SIN PRODUCTOR, BUSCADAS EN LA HISTORIA DE GIT (adjudicacion 6.9
del acta 158).

DE DONDE VIENE. La vuelta 157 barrio 998 `.py` POR SU TEXTO sobre EL ARBOL DE
HOY y no hallo quien escriba `SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt` ni
`SALIDA_V136_3D_MUTACION.txt`, las dos citadas por fichas cuya P3b se sostiene
en ellas. El acta concede que el barrido fue correcto y senala el angulo que
faltaba: UN PRODUCTOR PUDO MORIR O CAMBIAR DE NOMBRE, y un barrido del arbol de
hoy no lo ve.

LOS TRES ANGULOS QUE ESTE INSTRUMENTO CORRE, Y LOS TRES SE PUBLICAN:
  (1) `git log --all -S "<nombre del fichero>"` sobre `*.py`: que commit
      introdujo o quito el NOMBRE del fichero en algun `.py` de la historia.
  (2) `git log --all -S "<un trozo literal del CONTENIDO>"` sobre `*.py`: que
      commit introdujo o quito ese TEXTO en algun `.py`. Es el angulo que el
      encargo nombra, y es el que caza a un productor que imprima el texto
      aunque nunca escriba el nombre del fichero.
  (3) Para cada commit que aparezca, se listan los `.py` de ESE ARBOL que
      contienen el rastro, con `git grep` sobre el commit. Ahi esta el nombre
      del candidato a productor, si existe.

QUE SE PUBLICA Y QUE NO SE INVENTA: si aparece un `.py` que lo escribe, SE
NOMBRA. Si no aparece ninguno, LA CITA QUEDA DECLARADA ARTEFACTO HUERFANO y esa
declaracion es la que se publica. LA CITA NO SE BORRA: SE MARCA. Una busqueda
negativa se re verifica antes de citarla (EJECUTOR 9), y por eso van tres
angulos y no uno.

UN TROZO DE CONTENIDO SE ELIGE POR COMPUTO, NO A OJO: la linea mas larga del
fichero que no sea una ruta ni una cifra suelta, recortada a 60 caracteres, para
que `-S` tenga un pico literal donde morder.

--- (4) EL ANGULO QUE FALTABA, Y CORRIGE EL VEREDICTO DE MI PROPIA PRIMERA
CORRIDA. CORRECCION DECLARADA, Y EL TEXTO VIEJO NO SE BORRA ---

QUE PUBLICO LA PRIMERA CORRIDA DE ESTE INSTRUMENTO, Y ESTABA MAL: con los
angulos (1), (2) y (3) los dos sujetos salieron ARTEFACTO HUERFANO, con
"CIFRA sujetos con productor hallado: 0". ESO ERA FALSO, y lo era por un defecto
del instrumento, no del repo.

POR QUE FALLABAN LOS TRES ANGULOS, Y ES LA MISMA CAUSA QUE HIZO FALLAR EL
BARRIDO DE 998 `.py` DE LA VUELTA 157: EL PRODUCTOR NO ESCRIBE EL FICHERO,
IMPRIME POR STDOUT, y el `.txt` es una REDIRECCION DE SHELL. Por eso ningun
`.py` contiene el NOMBRE del fichero (angulo 1) y ninguno contiene su TEXTO
LITERAL (angulo 2): en el fuente ese texto esta CON MARCADORES DE FORMATO
(`"FICHEROS DE ENTRADA (declarados en FICHEROS_VEREDICTO, %d):"`), asi que
buscar la linea ya interpolada no puede casar nunca.

EL ANGULO (4), QUE SI CASA: para cada linea de la salida se prueban PREFIJOS
LITERALES cada vez mas cortos, palabra a palabra desde la izquierda, y se busca
cada prefijo con `git grep -F` sobre los `.py` de HEAD. Se publica EL PREFIJO
MAS LARGO QUE CASA, que es lo que separa una coincidencia real de una casual.

LA LECCION, PORQUE VALE MAS QUE EL CASO: UNA BUSQUEDA NEGATIVA NO SE PUEDE CITAR
(EJECUTOR 9). El barrido de la 157 y mis tres primeros angulos son todos
busquedas negativas sobre TEXTO YA INTERPOLADO, y ninguna podia hallar un
productor que interpola. La cuarta lo halla en los dos casos.

USO:  python scripts/loop/vuelta159_tarea7_productores_en_la_historia.py
"""
import io
import os
import re
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SUJETOS = [
    "SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt",
    "SALIDA_V136_3D_MUTACION.txt",
]


def git(*args):
    r = subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def pico_de_contenido(nombre):
    """La linea mas larga del fichero, recortada. Elegida por computo."""
    ruta = os.path.join(RAIZ, "docs", "loop", nombre)
    if not os.path.exists(ruta):
        return None
    lineas = [l.strip() for l in io.open(ruta, encoding="utf-8").read().splitlines()]
    lineas = [l for l in lineas if len(l) > 12 and not l.startswith("SALIDA_")]
    if not lineas:
        return None
    return max(lineas, key=len)[:60]


def commits_con(cadena, glob):
    codigo, salida = git("log", "--all", "--oneline", "-S", cadena, "--", glob)
    if codigo:
        return []
    return [l for l in salida.splitlines() if l.strip()]


def py_con_rastro(commit, cadena):
    codigo, salida = git("grep", "-l", "-F", cadena, commit, "--", "*.py")
    if codigo:
        return []
    return [l.split(":", 1)[-1] for l in salida.splitlines() if l.strip()]


def lineas_de(nombre):
    ruta = os.path.join(RAIZ, "docs", "loop", nombre)
    if not os.path.exists(ruta):
        return []
    return [l.strip() for l in io.open(ruta, encoding="utf-8").read().splitlines()
            if len(l.strip()) >= 20]


def prefijo_mas_largo_que_casa(linea, minimo=20):
    """Prueba prefijos literales cada vez mas cortos, palabra a palabra desde la
    izquierda, y devuelve (prefijo, [ficheros]) del PRIMERO que case en los .py
    de HEAD. Es el angulo (4): un productor que INTERPOLA no puede casar con la
    linea entera, pero si con su cabecera literal."""
    palabras = linea.split()
    for k in range(len(palabras), 2, -1):
        pref = " ".join(palabras[:k])
        if len(pref) < minimo:
            break
        ficheros = py_con_rastro("HEAD", pref)
        if ficheros:
            return pref, ficheros
    return None, []


def main():
    print("=" * 78)
    print("VUELTA 159, TAREA 7: LOS PRODUCTORES, BUSCADOS EN LA HISTORIA DE GIT")
    print("=" * 78)
    print("")

    veredictos = {}
    for nombre in SUJETOS:
        print("=" * 78)
        print("SUJETO: %s" % nombre)
        print("=" * 78)
        candidatos = set()

        print("(1) ANGULO DEL NOMBRE: git log --all -S %r -- *.py" % nombre)
        cs = commits_con(nombre, "*.py")
        print("    CIFRA commits que mueven ese nombre en algun .py: %d" % len(cs))
        for c in cs:
            print("       %s" % c[:100])
            h = c.split()[0]
            for f in py_con_rastro(h, nombre):
                print("          contiene el nombre: %s" % f)
                candidatos.add(f)
        print("")

        pico = pico_de_contenido(nombre)
        print("(2) ANGULO DEL CONTENIDO, que es el que el encargo nombra")
        if pico is None:
            print("    el fichero no existe en el arbol y no hay pico que buscar.")
        else:
            print("    pico literal elegido por computo (linea mas larga, 60 chars):")
            print("       %r" % pico)
            cs2 = commits_con(pico, "*.py")
            print("    CIFRA commits que mueven ese texto en algun .py: %d" % len(cs2))
            for c in cs2:
                print("       %s" % c[:100])
                h = c.split()[0]
                for f in py_con_rastro(h, pico):
                    print("          contiene el texto: %s" % f)
                    candidatos.add(f)
        print("")

        print("(4) ANGULO DE LA CABECERA LITERAL, EL QUE CAZA AL QUE INTERPOLA")
        por_linea = []
        for linea in lineas_de(nombre):
            pref, ficheros = prefijo_mas_largo_que_casa(linea)
            por_linea.append((linea, pref, ficheros))
            if pref:
                print("    linea  : %r" % linea[:70])
                print("      prefijo literal mas largo que casa (%d chars): %r"
                      % (len(pref), pref))
                for f in ficheros:
                    print("      lo imprime: %s" % f)
                    candidatos.add(f)
            else:
                print("    linea  : %r  SIN CABECERA QUE CASE" % linea[:70])
        con_hit = [x for x in por_linea if x[2]]
        print("    CIFRA lineas del fichero probadas: %d" % len(por_linea))
        print("    CIFRA lineas con cabecera literal hallada en un .py: %d" % len(con_hit))
        print("")

        print("(3) LOS CANDIDATOS A PRODUCTOR, REUNIDOS DE LOS ANGULOS")
        # se descartan los ficheros que solo NOMBRAN el artefacto para hablar de
        # el (adjudicaciones, barridos, este mismo instrumento): un productor es
        # el que lo ESCRIBE, y eso se distingue por llevar una escritura
        # (`open(`, `io.open(`, `>` de shell) junto al nombre. Se dice cual se
        # descarta y por que, en vez de callarlo.
        reales = []
        imprimen = {f for _, _, fs in por_linea for f in fs}
        for f in sorted(candidatos):
            codigo, cuerpo = git("show", "HEAD:%s" % f)
            if codigo:
                estado = "YA NO ESTA EN HEAD"
                cuerpo = ""
            else:
                estado = "vivo en HEAD"
            escribe = bool(re.search(r"(io\.)?open\([^)]*%s" % re.escape(nombre), cuerpo))
            cuantas = sum(1 for _, _, fs in por_linea if f in fs)
            print("    %-58s %-18s escribe a disco: %-3s imprime %d de %d linea(s)"
                  % (f, estado, "SI" if escribe else "no", cuantas, len(con_hit)))
            # LA REGLA DE PRODUCTOR, CORREGIDA EN ESTA MISMA CORRIDA Y DECLARADA:
            # la primera version pedia `cuantas >= 2`, y esa regla es FALSA para
            # un fichero de UNA SOLA LINEA como SALIDA_V136_3D_MUTACION.txt, que
            # con ella salia ARTEFACTO HUERFANO teniendo productor vivo. La regla
            # correcta no es un numero absoluto: ES PRODUCTOR EL QUE DA CUENTA DE
            # TODAS LAS LINEAS QUE CASARON, sea una o sean cinco. Un fichero que
            # solo comparte una cabecera de cinco es un primo, no el padre.
            if escribe or (con_hit and cuantas == len(con_hit)):
                reales.append((f, escribe, cuantas))
        print("")

        if reales:
            veredictos[nombre] = ("PRODUCTOR HALLADO",
                                  [x[0] for x in reales])
            print("VEREDICTO: PRODUCTOR HALLADO.")
            for f, escribe, cuantas in reales:
                print("   %s" % f)
                print("      via: %s" % ("escribe el fichero a disco" if escribe
                                         else "IMPRIME POR STDOUT y el .txt es una "
                                              "REDIRECCION DE SHELL"))
                print("      evidencia: %d linea(s) de la salida salen de sus print"
                      % cuantas)
            print("   LA FICHA PUEDE CITARLO. NO ES ARTEFACTO HUERFANO.")
        else:
            veredictos[nombre] = ("ARTEFACTO HUERFANO", [])
            print("VEREDICTO: ARTEFACTO HUERFANO. Los cuatro angulos corridos y NINGUN")
            print("`.py`, ni vivo ni muerto, lo escribe ni lo imprime. La cita NO se")
            print("borra: se marca con esa letra junto a la funcion de la P3b.")
        print("")

    print("=" * 78)
    print("RESUMEN")
    print("=" * 78)
    for nombre in SUJETOS:
        est, reales = veredictos[nombre]
        print("  %-46s %s%s" % (nombre, est,
                                (": " + ", ".join(reales)) if reales else ""))
    print("  CIFRA sujetos con productor hallado: %d"
          % sum(1 for n in SUJETOS if veredictos[n][1]))
    print("  CIFRA sujetos declarados ARTEFACTO HUERFANO: %d"
          % sum(1 for n in SUJETOS if not veredictos[n][1]))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
