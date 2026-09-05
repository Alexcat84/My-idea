# -*- coding: utf-8 -*-
r"""guarda_de_la_fuente_del_clon.py . SI UN FICHERO CLONA UNA FUNCION DE OTRO,
EL DIA QUE ESE OTRO DESAPAREZCA HAY QUE ENTERARSE.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como `paso0_archivar_anterior.py`,
`archivar_reporte.py`, `anexar_tarea_al_reporte.py`, `cerrar_reporte.py`,
`cotejar_clon_declarado.py` y `sujeto_congelado_de_git.py`: el esqueleto de cada
vuelta la IMPORTA y le pasa su fuente. **NO SE CLONA**, que seria la broma.

POR QUE NACE, Y LLEVA VUELTAS SUBIENDO (vuelta 180, TAREA 4.b; es el punto 3 de
la TAREA 5 de la 179 y estaba en su `D.4` desde la 174). El esqueleto de cada
vuelta **CLONA** `vuelta_del_reporte_del_arbol()` de
`scripts/loop/vuelta174_esqueleto_reporte.py` en vez de importarla. Clonar en vez
de importar fue una decision con motivo escrito: importar crearia una dependencia
sobre un fichero NUMERADO, y los ficheros numerados de esta casa se borran por
viejos. **Pero la decision dejo un agujero y estaba declarado en el docstring del
propio esqueleto desde la 174: NADA AVISA SI EL FICHERO DEL QUE SE CLONO
DESAPARECE.** Y si desaparece, el clon sigue funcionando y el arnes de la funcion
original (`scripts/loop/vuelta174_tarea1b_mutacion_esqueleto.py`) deja de poder
correr, o sea que **la funcion se queda sin prueba de mutacion y nadie lo nota**.
Es la especie del `banco 9`: no falla, deja de mirar.

QUE COMPRUEBA, Y CAE EN ROJO NOMBRANDO LO QUE FALTA:

  (a) que el fichero fuente del clon EXISTA;
  (b) que ese fichero DEFINA la funcion que se dice clonada, buscada en su arbol
      de sintaxis y no con un `in` sobre el texto, que acertaria con una mencion
      en un comentario;
  (c) que el fichero fuente PARSEE, porque un fichero roto no define nada.

LO QUE NO COMPRUEBA, Y SE DICE EN VEZ DE INSINUARLO: **NO compara los dos
cuerpos**. Que el clon siga siendo byte a byte el original es otra pregunta y
tiene otro instrumento, `scripts/loop/cotejar_clon_declarado.py`. Esta guarda
responde una sola cosa: **si la fuente sigue estando**.

PURA SALVO POR LEER, y con los caminos por parametro para que su caso positivo
por mutacion pueda apuntarla a una ruta fabricada que no existe sin tocar el repo.

USO (desde el esqueleto de la vuelta N):
    import guarda_de_la_fuente_del_clon as CLON
    ok, informe = CLON.exigir_fuente_del_clon(
        "scripts/loop/vuelta174_esqueleto_reporte.py", "vuelta_del_reporte_del_arbol")
    for l in informe:
        print(l)
    if not ok:
        sys.exit(1)
"""
import ast
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)


def funciones_definidas(texto):
    """LOS NOMBRES DE FUNCION QUE ESE TEXTO DEFINE, leidos del arbol de sintaxis.
    PURA. Devuelve None si el texto no parsea, que NO es lo mismo que una lista
    vacia y por eso se distingue."""
    try:
        arbol = ast.parse(texto)
    except (SyntaxError, ValueError):
        return None
    return sorted(n.name for n in ast.walk(arbol)
                  if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)))


def exigir_fuente_del_clon(ruta_fuente, nombre_funcion, raiz=None):
    """(ok, informe). El informe es una lista de lineas, y CADA MOTIVO SE NOMBRA.

    `ruta_fuente` va relativa a la raiz del repo, con barras normales.
    `raiz` va por parametro para que el caso positivo por mutacion pueda
    apuntarla a un directorio fabricado."""
    base = raiz or RAIZ
    informe = []
    w = informe.append
    motivos = []

    w("GUARDA DE LA FUENTE DEL CLON (vuelta 180, TAREA 4.b)")
    w("   este fichero CLONA %r de %s" % (nombre_funcion, ruta_fuente))

    ruta = os.path.join(base, ruta_fuente.replace("/", os.sep))
    if not os.path.isfile(ruta):
        motivos.append("(a) LA FUENTE DEL CLON NO EXISTE: %s. La funcion %r se "
                       "clono de ahi y ese fichero ya no esta, asi que su arnes "
                       "de mutacion no puede correr y la funcion se quedaria sin "
                       "prueba." % (ruta_fuente, nombre_funcion))
        w("   %s -> NO EXISTE" % ruta_fuente)
        return (False, informe + _cierre(motivos))

    texto = io.open(ruta, encoding="utf-8", errors="replace").read()
    w("   %s -> %d bytes, %d lineas"
      % (ruta_fuente, len(texto.replace(chr(13) + NL, NL).encode("utf-8")),
         texto.count(NL)))

    nombres = funciones_definidas(texto)
    if nombres is None:
        motivos.append("(c) LA FUENTE DEL CLON NO PARSEA: %s. Un fichero roto no "
                       "define nada, y no se puede afirmar que %r siga ahi."
                       % (ruta_fuente, nombre_funcion))
        w("   el fichero NO PARSEA")
        return (False, informe + _cierre(motivos))

    w("   CIFRA funciones que define: %d" % len(nombres))
    if nombre_funcion not in nombres:
        motivos.append("(b) LA FUENTE DEL CLON YA NO DEFINE %r: %s. El fichero "
                       "sigue ahi pero la funcion se fue, y el arnes que la "
                       "prueba apunta a algo que no existe."
                       % (nombre_funcion, ruta_fuente))
        w("   define %r: NO" % nombre_funcion)
    else:
        w("   define %r: SI" % nombre_funcion)

    return (not motivos, informe + _cierre(motivos))


def _cierre(motivos):
    cola = []
    if motivos:
        cola.append("   ROJO, %d motivo(s). LA FUENTE DEL CLON NO ESTA EN SU SITIO:"
                    % len(motivos))
        for m in motivos:
            cola.append("      " + m)
    else:
        cola.append("   VERDE: la fuente del clon existe, parsea y sigue definiendo")
        cola.append("   la funcion clonada. El arnes de la original puede correr.")
    return cola
