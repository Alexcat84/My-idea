# -*- coding: utf-8 -*-
"""tallar_composicion_salida.py . LA SEGUNDA MITAD DE LA ESCALADA A LAS FASES
MECANICAS (TAREA 3 de la vuelta 91, encargo del auditor, seccion 3.2 y 6.1 del
acta de la vuelta 90).

TALLADOR HERMANO de scripts/loop/tallar_conteo_campo.py: aquel talla LA
LONGITUD de un campo de un JSONL. Este talla CIFRAS DE COMPOSICION DE UNA
SALIDA DE TEXTO: dado un fichero de salida y un patron de clasificacion,
cuenta CUANTAS FILAS caen en cada clase, ENUMERA LOS PUESTOS de cada clase, y
COTEJA esa enumeracion contra una lista citada, marcando lo que SOBRA (citado
pero no es de esa clase) y lo que FALTA (es de esa clase pero no esta
citado).

POR QUE NACE, CON EL EJEMPLAR DELANTE (acta de la vuelta 90, seccion 3.1 y
3.2, `docs/loop/ACTA_AUDITOR.md` lineas 30729 a 30784). El reporte de la
vuelta 90 publico que "Cinco pares" se habian escrito resolviendo un alias,
con una lista de once puestos de ejemplo. La cifra real: CATORCE filas,
ONCE pares de alias DISTINTOS, y la lista de ejemplo OMITIA DOS puestos
(1207 y 1535) sin nombrarlos en ningun sitio. `tallar_conteo_campo.py` solo
mide LONGITUD de un campo de un JSONL: no puede tallar "cuantas filas de esta
salida de texto se resolvieron por alias", que es justo la cifra que fallo.
Este instrumento es ese remedio.

QUE MIDE, EXACTO Y NADA MAS.

  (1) CLASIFICACION: --patron es una expresion regular con GRUPOS NOMBRADOS,
      aplicada LINEA A LINEA sobre --fichero. Cada linea que la casa es una
      FILA; las que no la casan (cabeceras, separadores, el resumen del pie)
      se ignoran. El grupo nombrado por --clave identifica la fila (por
      defecto "puesto"); el grupo nombrado por --campo-clase decide la
      clase: si su valor es IGUAL a --valor-base, la fila cae en
      --etiqueta-base; si no, cae en --etiqueta-otra.

  (2) EL CONTEO Y LA ENUMERACION: cuantas filas en cada etiqueta, y la lista
      de --clave de cada una, ordenada.

  (3) EL COTEJO: si se da --lista-citada (una lista separada por comas de
      valores de --clave) y --clase-cotejo (cual de las dos etiquetas se
      coteja), se compara la enumeracion REAL de esa clase contra la lista
      citada: SOBRAN (citados que la medicion real NO clasifica en esa
      clase) y FALTAN (de esa clase segun la medicion real, pero AUSENTES de
      la lista citada).

  (4) OPCIONAL, PARES DISTINTOS DE SUSTITUCION: cuando la clase que interesa
      es "un campo cambio de un id a otro" (el caso de los alias), una fila
      puede repetir la MISMA sustitucion de nodo que otra (cinco filas
      distintas pueden compartir el mismo alias resuelto), asi que "filas"
      y "pares distintos" son dos cifras DISTINTAS y las dos hacen falta.
      Con --par-escrito "GRUPO_A,GRUPO_B" y --par-crudo-campo GRUPO mas
      --par-crudo-separador (por defecto " -> "), el tallador compara,
      POSICION A POSICION, el par ESCRITO (lo que quedo grabado) contra el
      par CRUDO (la forma cruda de la que partio la razon) de cada fila de
      --clase-cotejo, y cuenta las sustituciones de nodo (crudo, escrito)
      DISTINTAS que aparecen. Una fila cuyos DOS extremos cambiaron aporta
      DOS sustituciones.

MECANICA DE ROJO, identica a la del resto de esta familia de talladores: si
el fichero no existe, si --patron no casa NINGUNA linea, o si --campo-clase
o --clave no aparecen entre los grupos nombrados de --patron, NO SE TALLA
NADA (no se imprime tabla ninguna) y sale con exit 1. El pulido de la vuelta
90 (seccion 1.11 del acta) se aplica aqui desde el primer commit: cuando cae
en ROJO, la palabra y la salida dicen lo mismo.

USO (el caso duro de la vuelta 91, el que la vuelta 90 no pudo tallar):
  python scripts/loop/tallar_composicion_salida.py \\
    --fichero docs/loop/SALIDA_V90_TAREA4_ESCRITURA.txt \\
    --patron "^puesto (?P<puesto>\\d+)\\s*\\|\\s*(?P<estado>\\S+)\\s*\\|\\s*(?P<escrito_a>[a-z0-9_]+)\\s*->\\s*(?P<escrito_b>[a-z0-9_]+)\\s*\\(resuelto:\\s*(?P<crudo>.+)\\)\\s*$" \\
    --clave puesto --campo-clase crudo --valor-base "sin alias" \\
    --etiqueta-base "sin alias" --etiqueta-otra "resuelto por alias" \\
    --clase-cotejo "resuelto por alias" \\
    --lista-citada 956,1012,1013,1160,1169,1270,1286,1345,1472,1545,1546 \\
    --par-escrito escrito_a,escrito_b --par-crudo-campo crudo

VARA DE SI ALCANZA (dura, la del encargo de la vuelta 91): corrido con el
comando de arriba, tiene que dar CATORCE filas en "resuelto por alias",
ONCE pares de sustitucion distintos, y el cotejo tiene que marcar 1207 y
1535 como FALTAN (ausentes de la lista citada).
"""
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def clasifica_fila(valores, campo_clase, valor_base, etiqueta_base, etiqueta_otra):
    """LA UNICA PIEZA DE JUICIO DE ESTE TALLADOR, aislada a proposito para que
    su propio caso rojo se pueda probar por mutacion (regla de EJECUTOR.md,
    "EL CASO ROJO SE PRUEBA POR MUTACION"): dado el diccionario de grupos
    nombrados de UNA fila ya casada por --patron, dice si su --campo-clase
    es IGUAL a --valor-base (etiqueta_base) o DISTINTO (etiqueta_otra). El
    conteo, la enumeracion y el cotejo llaman todos a esta misma funcion; no
    hay una segunda cuenta paralela que pudiera divergir de ella."""
    if valores[campo_clase] == valor_base:
        return etiqueta_base
    return etiqueta_otra


def cargar_lineas(ruta, fallos):
    ruta_abs = ruta if os.path.isabs(ruta) else os.path.join(RAIZ, ruta)
    if not os.path.exists(ruta_abs):
        fallos.append("no existe el fichero %s" % ruta)
        return None
    with io.open(ruta_abs, encoding="utf-8") as f:
        return f.readlines()


def parsear_filas(lineas, patron, fallos):
    try:
        rx = re.compile(patron)
    except re.error as e:
        fallos.append("el --patron no es una expresion regular valida: %s" % e)
        return None
    filas = []
    for n, linea in enumerate(lineas, 1):
        m = rx.match(linea.rstrip("\n"))
        if m:
            filas.append((n, m.groupdict()))
    return filas


def sustituciones_de_par(escrito, crudo):
    """Compara POSICION A POSICION el par ESCRITO (a, b) contra el par CRUDO
    (a, b) y devuelve la lista de sustituciones (crudo, escrito) DISTINTAS de
    cada posicion donde difieren. Un par con los dos extremos distintos
    aporta DOS sustituciones."""
    subs = []
    for e, c in zip(escrito, crudo):
        if e != c:
            subs.append((c, e))
    return subs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fichero", required=True, help="ruta al fichero de salida, relativa a la raiz del repo")
    ap.add_argument("--patron", required=True, help="regex con grupos nombrados, aplicada linea a linea")
    ap.add_argument("--clave", default="puesto", help="grupo nombrado que identifica cada fila (por defecto 'puesto')")
    ap.add_argument("--campo-clase", required=True, help="grupo nombrado cuyo valor decide la clase")
    ap.add_argument("--valor-base", required=True, help="el valor de --campo-clase que cae en --etiqueta-base")
    ap.add_argument("--etiqueta-base", required=True, help="nombre de la clase cuando --campo-clase == --valor-base")
    ap.add_argument("--etiqueta-otra", required=True, help="nombre de la clase cuando --campo-clase != --valor-base")
    ap.add_argument("--clase-cotejo", default=None, help="cual de las dos etiquetas se coteja contra --lista-citada")
    ap.add_argument("--lista-citada", default=None, help="lista separada por comas de valores de --clave a cotejar")
    ap.add_argument("--par-escrito", default=None, metavar="GRUPO_A,GRUPO_B",
                    help="dos grupos nombrados con el par ESCRITO, para contar sustituciones distintas")
    ap.add_argument("--par-crudo-campo", default=None, metavar="GRUPO",
                    help="grupo nombrado con el par CRUDO completo ('a -> b'), a partir con --par-crudo-separador")
    ap.add_argument("--par-crudo-separador", default=" -> ", help="separador del par crudo (por defecto ' -> ')")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    fallos = []
    lineas = cargar_lineas(a.fichero, fallos)
    if fallos:
        print("ROJO, %d cosa(s) no se pudieron leer y NO SE TALLA NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    filas = parsear_filas(lineas, a.patron, fallos)
    if fallos:
        print("ROJO, %d cosa(s) no se pudieron leer y NO SE TALLA NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    if not filas:
        print("ROJO: --patron no caso NINGUNA linea de %s. NO SE TALLA NADA." % a.fichero)
        return 1

    grupos_vistos = set(filas[0][1].keys())
    faltan_grupos = [g for g in (a.clave, a.campo_clase) if g not in grupos_vistos]
    if faltan_grupos:
        print("ROJO: --patron no trae el/los grupo(s) nombrado(s) %s. NO SE TALLA NADA."
              % ", ".join(faltan_grupos))
        return 1

    # --- (1) y (2): CLASIFICACION, CONTEO Y ENUMERACION ---
    por_clase = {a.etiqueta_base: [], a.etiqueta_otra: []}
    for n, valores in filas:
        clase = clasifica_fila(valores, a.campo_clase, a.valor_base, a.etiqueta_base, a.etiqueta_otra)
        por_clase[clase].append((valores[a.clave], valores))

    print("=" * 90)
    print("TALLA DE COMPOSICION. Cada cifra sale de %s, patron citado arriba; ninguna tecleada."
          % a.fichero)
    print("=" * 90)
    print()
    print("filas totales casadas por --patron: %d" % len(filas))
    print()
    print("| clase | filas |")
    print("|---|---:|")
    for etiqueta in (a.etiqueta_base, a.etiqueta_otra):
        print("| %s | %d |" % (etiqueta, len(por_clase[etiqueta])))
    print()
    for etiqueta in (a.etiqueta_base, a.etiqueta_otra):
        claves = sorted((c for c, _ in por_clase[etiqueta]), key=lambda x: (len(x), x))
        print("ENUMERACION de '%s' (%d): %s" % (etiqueta, len(claves), ", ".join(claves) if claves else "(ninguna)"))
    print()

    # --- (3) EL COTEJO ---
    if a.clase_cotejo is not None:
        if a.clase_cotejo not in por_clase:
            print("ROJO: --clase-cotejo %r no es --etiqueta-base ni --etiqueta-otra. NO SE TALLA NADA."
                  % a.clase_cotejo)
            return 1
        reales = set(c for c, _ in por_clase[a.clase_cotejo])
        citados = set(p.strip() for p in (a.lista_citada or "").split(",") if p.strip())
        sobran = sorted(citados - reales, key=lambda x: (len(x), x))
        faltan = sorted(reales - citados, key=lambda x: (len(x), x))
        print("--- COTEJO de la clase '%s' (%d reales) contra la lista citada (%d citados) ---"
              % (a.clase_cotejo, len(reales), len(citados)))
        print("SOBRAN en la lista citada (citados que NO son de esta clase): %s"
              % (", ".join(sobran) if sobran else "NINGUNO"))
        print("FALTAN en la lista citada (de esta clase pero AUSENTES de lo citado): %s"
              % (", ".join(faltan) if faltan else "NINGUNO"))
        print()

    # --- (4) PARES DISTINTOS DE SUSTITUCION, OPCIONAL ---
    if a.par_escrito and a.par_crudo_campo:
        grupo_a, _, grupo_b = a.par_escrito.partition(",")
        grupo_a, grupo_b = grupo_a.strip(), grupo_b.strip()
        faltan_grupos_par = [g for g in (grupo_a, grupo_b, a.par_crudo_campo) if g not in grupos_vistos]
        if faltan_grupos_par:
            print("ROJO: --par-escrito / --par-crudo-campo nombran grupo(s) que --patron no trae: %s. "
                  "NO SE TALLA NADA." % ", ".join(faltan_grupos_par))
            return 1
        clase_para_pares = a.clase_cotejo or a.etiqueta_otra
        subs_vistas = {}
        for clave, valores in por_clase[clase_para_pares]:
            escrito = (valores[grupo_a], valores[grupo_b])
            crudo = tuple(p.strip() for p in valores[a.par_crudo_campo].split(a.par_crudo_separador))
            if len(crudo) != 2:
                print("ROJO: la fila %s='%s' no parte en dos con el separador %r. NO SE TALLA NADA."
                      % (a.clave, clave, a.par_crudo_separador))
                return 1
            for sub in sustituciones_de_par(escrito, crudo):
                subs_vistas.setdefault(sub, []).append(valores[a.clave])
        print("--- PARES DISTINTOS DE SUSTITUCION en '%s' (comparando %s,%s contra %s) ---"
              % (clase_para_pares, grupo_a, grupo_b, a.par_crudo_campo))
        print("pares de sustitucion (crudo -> escrito) DISTINTOS: %d" % len(subs_vistas))
        for (crudo_id, escrito_id), claves in sorted(subs_vistas.items()):
            print("  %s -> %s (en %d fila(s): %s)" % (crudo_id, escrito_id, len(claves), ", ".join(claves)))
        print()

    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
