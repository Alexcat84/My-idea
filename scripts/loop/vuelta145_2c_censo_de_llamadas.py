# -*- coding: utf-8 -*-
r"""vuelta145_2c_censo_de_llamadas.py . EL CENSO DE LLAMADAS A
`pares_exceptuados_de`, VUELTA 145, TAREA 2.c.

POR QUE NACE (acta 144, caida 4.1 del auditor, LA UNICA DEL EJECUTOR QUE
ACUMULA). El reporte de la vuelta 144 publico una tabla de SEIS ficheros, con
los numeros de linea de ANTES de sus propias reparaciones, cuando el grep del
dia daba OCHO. Una tabla tecleada envejece entre que se mide y que se pega
(EJECUTOR.md 1, "LA TABLA SE IMPRIME, NO SE TECLEA" y "LA TABLA SE CUENTA DE
SU FICHERO"). Este instrumento la imprime.

QUE MIDE, sobre `scripts/` entero y con los numeros de linea DE HOY:
  - TODA aparicion del nombre `pares_exceptuados_de`, clasificada en:
      DEFINICION  . un `def pares_exceptuados_de(...)`.
      LLAMADA     . una invocacion de verdad.
      MENCION     . el nombre en un comentario, un docstring o una ruta: NO es
                    una llamada, y contarla como tal es mezclar dos unidades en
                    una columna.
  - Para cada LLAMADA, QUE HACE CON SUS FALLOS, leido del tercer argumento:
      LOS RECOGE  . pasa un nombre (una lista que despues se mira).
      LOS TIRA    . pasa un literal `[]`: la lista muere en la llamada.
    Y si los tira, si el codigo lo DECLARA (un comentario en la misma linea que
    diga que es a proposito) o si los tira EN SILENCIO.

LA CLASIFICACION SE HACE CON `ast`, NO CON UNA EXPRESION REGULAR, y esto es
una CORRECCION DECLARADA DENTRO DE LA MISMA VUELTA: la primera version de este
instrumento clasificaba por texto de la linea, y su propia primera corrida se
delato sola dando ROJO en dos sitios que no son llamadas, la linea 6 de
`vuelta144_2b_mutacion_giro.py` (un docstring que CITA el codigo viejo) y la
linea 14 de este mismo fichero (su propio docstring). Un docstring que nombra
una llamada no es una llamada; `ast` lo sabe y una expresion regular no.

LA UNIDAD SE DICE EN EL ROTULO, que es la caida 4.7 del acta 144 en su otra
cara: se publica el numero de FICHEROS CON APARICION y el de FICHEROS CON
LLAMADA por separado, porque no son la misma cifra.

USO:
  python scripts/loop/vuelta145_2c_censo_de_llamadas.py
"""
import ast
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPTS = os.path.join(RAIZ, "scripts")
NOMBRE = "pares_exceptuados_de"


def _nombre_llamado(nodo):
    """El nombre invocado en un `ast.Call`: `f(...)` da 'f' y `T.f(...)` da 'f'."""
    f = nodo.func
    if isinstance(f, ast.Attribute):
        return f.attr
    if isinstance(f, ast.Name):
        return f.id
    return None


def hechos_del_fichero(texto):
    """{linea: (clase, detalle)} para las lineas donde `ast` ve una DEFINICION o
    una LLAMADA de verdad. Lo que no salga aqui y traiga el nombre es MENCION."""
    hechos = {}
    try:
        arbol = ast.parse(texto)
    except SyntaxError:
        return None
    for nodo in ast.walk(arbol):
        if isinstance(nodo, ast.FunctionDef) and nodo.name == NOMBRE:
            hechos[nodo.lineno] = ("DEFINICION", "")
        elif isinstance(nodo, ast.Call) and _nombre_llamado(nodo) == NOMBRE:
            if len(nodo.args) < 3:
                hechos[nodo.lineno] = ("LLAMADA", "menos de tres argumentos posicionales")
                continue
            tercero = nodo.args[2]
            if isinstance(tercero, ast.List) and not tercero.elts:
                hechos[nodo.lineno] = ("LLAMADA", "LOS TIRA")
            elif isinstance(tercero, ast.Name):
                hechos[nodo.lineno] = ("LLAMADA", "LOS RECOGE en %s" % tercero.id)
            else:
                hechos[nodo.lineno] = ("LLAMADA", "tercer argumento: %s"
                                       % type(tercero).__name__)
    return hechos


def declarado_en_la_linea(linea):
    """Un `[]` es LEGITIMO si el codigo DICE en la propia linea que tira los
    fallos a proposito. Lo dice o no lo dice; no se supone."""
    return "#" in linea and ("proposito" in linea.lower() or "tirad" in linea.lower())


def ficheros():
    for base, _dirs, nombres in os.walk(SCRIPTS):
        if "__pycache__" in base:
            continue
        for n in sorted(nombres):
            if n.endswith(".py"):
                yield os.path.join(base, n)


def main():
    filas = []
    for ruta in sorted(ficheros()):
        rel = os.path.relpath(ruta, RAIZ).replace(os.sep, "/")
        try:
            texto = io.open(ruta, encoding="utf-8").read()
        except (IOError, UnicodeDecodeError):
            continue
        if NOMBRE not in texto:
            continue
        hechos = hechos_del_fichero(texto)
        if hechos is None:
            filas.append((rel, 0, "NO PARSEA", "el fichero no compila: no se clasifica"))
            continue
        lineas = texto.split("\n")
        for i, linea in enumerate(lineas, 1):
            if NOMBRE not in linea and i not in hechos:
                continue
            clase, detalle = hechos.get(i, ("MENCION", "el nombre fuera de toda llamada"))
            if detalle == "LOS TIRA":
                detalle = ("LOS TIRA, Y LO DECLARA en la propia linea"
                           if declarado_en_la_linea(linea) else "LOS TIRA EN SILENCIO")
            filas.append((rel, i, clase, detalle))

    ancho = max([len(f[0]) for f in filas] or [10])
    print("CENSO DE `%s` EN scripts/, CON LOS NUMEROS DE LINEA DE HOY" % NOMBRE)
    print("=" * 78)
    print("%-*s %6s  %-10s %s" % (ancho, "FICHERO", "LINEA", "CLASE", "QUE HACE CON SUS FALLOS"))
    for rel, i, clase, detalle in filas:
        print("%-*s %6d  %-10s %s" % (ancho, rel, i, clase, detalle))
    print("")

    con_aparicion = sorted(set(f[0] for f in filas))
    con_llamada = sorted(set(f[0] for f in filas if f[2] == "LLAMADA"))
    solo_mencion = [f for f in con_aparicion if f not in con_llamada]
    llamadas = [f for f in filas if f[2] == "LLAMADA"]
    tiran_silencio = [f for f in llamadas if f[3] == "LOS TIRA EN SILENCIO"]
    tiran_declarado = [f for f in llamadas if f[3].startswith("LOS TIRA, Y LO DECLARA")]
    recogen = [f for f in llamadas if f[3].startswith("LOS RECOGE")]

    print("FICHEROS CON APARICION DEL NOMBRE : %d" % len(con_aparicion))
    print("FICHEROS CON LLAMADA DE VERDAD    : %d" % len(con_llamada))
    # LINEAS CIFRA, para que el reporte pueda cotejar estas dos unidades contra
    # este fichero en vez de dejarlas sin nada que contar. SON DOS UNIDADES
    # DISTINTAS y por eso llevan dos etiquetas distintas (CORRECCION 18).
    print("CIFRA ficheros con aparicion del nombre: %d ficheros" % len(con_aparicion))
    print("CIFRA ficheros con llamada de verdad: %d ficheros" % len(con_llamada))
    print("FICHEROS QUE SOLO LO MENCIONAN    : %d %s"
          % (len(solo_mencion), solo_mencion or ""))
    print("LLAMADAS EN TOTAL                 : %d" % len(llamadas))
    print("  que RECOGEN sus fallos          : %d" % len(recogen))
    print("  que los TIRAN Y LO DECLARAN     : %d %s"
          % (len(tiran_declarado), ["%s:%d" % (f[0], f[1]) for f in tiran_declarado]))
    print("  que los TIRAN EN SILENCIO       : %d %s"
          % (len(tiran_silencio), ["%s:%d" % (f[0], f[1]) for f in tiran_silencio]))
    print("")
    if tiran_silencio:
        print("ROJO: quedan %d llamada(s) que tiran sus fallos sin declararlo"
              % len(tiran_silencio))
        return 1
    print("VERDE: ninguna llamada tira sus fallos en silencio")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
