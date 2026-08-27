# -*- coding: utf-8 -*-
"""tallar_barrido_cifras.py . TALLADOR NUEVO (TAREA 2.a de la vuelta 95,
encargo del auditor, acta de la vuelta 94, la ESCALADA DE CODIGO obligatoria
por la racha de reporte llegando a DOS DE TRES: EJECUTOR.md regla 1, "Y LA
ESCALADA").

POR QUE NACE, CON EL EJEMPLAR DELANTE (acta de la vuelta 94, seccion 3, sobre
`docs/loop/SALIDA_V94_TAREA2A_BARRIDO.txt`). El reporte de la vuelta 94
publico "8 aciertos de las tres cifras en docs/plan/ (todos en
04_ENLACES.md), de los cuales 7 ya llevaban su salvedad y 1 no la llevaba",
CONTADO A OJO sobre un barrido de cifras de OP-E-07. La cuenta real, tallada
con el instrumento hermano `tallar_composicion_salida.py` clasificando por
fichero: 14 filas, 11 en `docs/plan/04_ENLACES.md` y 3 en OTROS ficheros, y
ningun criterio reconstruible producia "8, todos en 04_ENLACES.md, 7 mas 1".
Aquel tallador no sirve para ESTA cifra: mide la COMPOSICION de un fichero de
salida YA ESCRITO por un barrido anterior (`grep -rn ... > fichero`), no
CORRE el barrido el mismo, y no sabe nada de SALVEDAD (una marca de vuelta o
de corte cerca de la cifra). Este instrumento es ese remedio: CORRE el
barrido el mismo (no lee la salida de texto de un barrido ajeno) y TALLA,
ademas del conteo por fichero, cuantos aciertos LLEVAN salvedad cerca y
cuantos no.

QUE MIDE, EXACTO Y NADA MAS.

  (1) EL BARRIDO: --patrones es una lista separada por comas de fragmentos de
      expresion regular; se combinan con "|" (alternancia), EXACTAMENTE como
      grep -rn "A\\|B\\|C" combina sus alternativas, y se buscan sobre el
      TEXTO COMPLETO de cada fichero bajo --raices (una lista separada por
      comas de rutas, cada una fichero o directorio; un directorio se recorre
      entero, TODO fichero que se pueda decodificar como utf-8; los que no se
      puedan se listan aparte como "binarios o no utf-8, omitidos" y no
      cuentan ni como acierto ni como fallo).

  (2) EL CONTEO Y LA ENUMERACION: cuantos aciertos en total, cuantos por
      fichero (con la enumeracion de sus lineas, numero de linea 1-based
      contando saltos de linea hasta la posicion del acierto).

  (3) LA SALVEDAD: --patron-salvedad (una expresion regular; por defecto
      "hasta la vuelta \\d+|desde la vuelta \\d+|CORRECCION DECLARADA|cifra
      vigente hasta", los CUATRO ejemplos literales del encargo) se busca
      DENTRO DE UNA VENTANA de --ventana caracteres (por defecto 200) A CADA
      LADO de la posicion del acierto, sobre el TEXTO COMPLETO del fichero
      (no la linea sola a proposito: una salvedad puede vivir en la frase
      siguiente de la misma celda de una tabla, y una ventana de una sola
      linea la perderia). 200 se declara aqui, no se esconde: es, a ojo
      generoso, la mitad de una celda larga de la tabla de
      docs/plan/04_ENLACES.md (las filas de esa tabla, medidas en esta
      vuelta, rondan los 400 a 600 caracteres). --ventana la puede mover
      quien la use.

MECANICA DE ROJO, identica a la familia: si una raiz de --raices no existe,
si --patrones o --patron-salvedad no compilan, o si el barrido no caso NINGUN
acierto en NINGUN fichero, NO SE TALLA NADA (exit 1, sin imprimir tabla).

LA UNICA PIEZA DE JUICIO, aislada para la prueba de mutacion (EJECUTOR.md
regla 1, "EL CASO ROJO SE PRUEBA POR MUTACION"): `tiene_salvedad(contexto,
patron_salvedad)`, que dice si CONTEXTO (la ventana de caracteres alrededor
de un acierto) trae alguna marca de salvedad. El conteo con/sin y las dos
enumeraciones llaman todos a esta misma funcion; no hay una segunda cuenta
paralela que pudiera divergir de ella. Su prueba de mutacion vive en
scripts/loop/vuelta95_tarea2a_prueba_mutacion_barrido.py.

USO (el barrido rehecho de la vuelta 94, mismos patrones y mismas raices que
`docs/loop/SALIDA_V94_TAREA2A_BARRIDO.txt`, primer comando de ese fichero):
  python scripts/loop/tallar_barrido_cifras.py \\
    --raices docs/plan,docs/BANCO_DE_TEXTOS.md \\
    --patrones "85 ESCRITA,87 con direccion,cifra vigente"

CASO OBLIGATORIO (vuelta 95, contra el barrido de la vuelta 94): corrido con
el comando de arriba tiene que dar la cuenta REAL en vez de "8, 7+1", citada
como CORRECCION DECLARADA de esa frase en docs/loop/REPORTE.md y en
docs/PENDIENTES.md, sin borrar la frase vieja.
"""
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PATRON_SALVEDAD_DEFECTO = r"hasta la vuelta \d+|desde la vuelta \d+|CORRECCION DECLARADA|cifra vigente hasta"


def tiene_salvedad(contexto, patron_salvedad):
    """LA UNICA PIEZA DE JUICIO de este tallador, aislada a proposito para que
    su propio caso rojo se pueda probar por mutacion: dado CONTEXTO (la
    ventana de caracteres alrededor de un acierto, texto crudo) y
    PATRON_SALVEDAD (una expresion regular ya compilada), dice si el contexto
    trae alguna marca de salvedad. El conteo con/sin y las dos enumeraciones
    llaman todos a esta misma funcion."""
    return bool(patron_salvedad.search(contexto))


def recolectar_ficheros(raiz, fallos):
    ruta_abs = raiz if os.path.isabs(raiz) else os.path.join(RAIZ, raiz)
    if not os.path.exists(ruta_abs):
        fallos.append("no existe la raiz %s" % raiz)
        return []
    if os.path.isfile(ruta_abs):
        return [ruta_abs]
    encontrados = []
    for base, dirs, nombres in os.walk(ruta_abs):
        dirs[:] = [d for d in dirs if d != ".git"]
        for nombre in sorted(nombres):
            encontrados.append(os.path.join(base, nombre))
    return encontrados


def relpath(ruta_abs):
    return os.path.relpath(ruta_abs, RAIZ).replace("\\", "/")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raices", required=True, help="lista separada por comas de ficheros o directorios, relativos a la raiz del repo")
    ap.add_argument("--patrones", required=True, help="lista separada por comas de fragmentos de regex, combinados con |")
    ap.add_argument("--patron-salvedad", default=PATRON_SALVEDAD_DEFECTO, help="regex de las marcas de salvedad")
    ap.add_argument("--ventana", type=int, default=200, help="caracteres a cada lado del acierto donde buscar la salvedad (por defecto 200)")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    fallos = []

    fragmentos = [p.strip() for p in a.patrones.split(",") if p.strip()]
    if not fragmentos:
        print("ROJO: --patrones no trae ningun fragmento. NO SE TALLA NADA.")
        return 1
    patron_cifra_txt = "|".join("(?:%s)" % p for p in fragmentos)
    try:
        patron_cifra = re.compile(patron_cifra_txt)
    except re.error as e:
        print("ROJO: --patrones no compila como regex (%s): %s. NO SE TALLA NADA." % (patron_cifra_txt, e))
        return 1

    try:
        patron_salvedad = re.compile(a.patron_salvedad)
    except re.error as e:
        print("ROJO: --patron-salvedad no compila (%s): %s. NO SE TALLA NADA." % (a.patron_salvedad, e))
        return 1

    raices = [r.strip() for r in a.raices.split(",") if r.strip()]
    if not raices:
        print("ROJO: --raices no trae ninguna ruta. NO SE TALLA NADA.")
        return 1

    ficheros = []
    vistos = set()
    for raiz in raices:
        for f in recolectar_ficheros(raiz, fallos):
            if f not in vistos:
                vistos.add(f)
                ficheros.append(f)
    if fallos:
        print("ROJO, %d cosa(s) no se pudieron leer y NO SE TALLA NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    omitidos = []
    aciertos_por_fichero = {}
    total_con = 0
    total_sin = 0
    lista_con = []
    lista_sin = []

    for ruta_abs in ficheros:
        try:
            texto = io.open(ruta_abs, encoding="utf-8").read()
        except (UnicodeDecodeError, IsADirectoryError):
            omitidos.append(relpath(ruta_abs))
            continue
        rel = relpath(ruta_abs)
        for m in patron_cifra.finditer(texto):
            linea = texto.count("\n", 0, m.start()) + 1
            contexto = texto[max(0, m.start() - a.ventana):m.end() + a.ventana]
            con = tiene_salvedad(contexto, patron_salvedad)
            aciertos_por_fichero.setdefault(rel, []).append((linea, con))
            etiqueta = "%s:%d" % (rel, linea)
            if con:
                total_con += 1
                lista_con.append(etiqueta)
            else:
                total_sin += 1
                lista_sin.append(etiqueta)

    total = total_con + total_sin
    if total == 0:
        print("ROJO: el barrido no caso NINGUN acierto en ningun fichero de %s. NO SE TALLA NADA." % ", ".join(raices))
        return 1

    print("=" * 90)
    print("TALLA DE BARRIDO DE CIFRAS. Cada cifra sale de correr --patrones sobre --raices EN ESTA")
    print("CORRIDA; ninguna sale de leer un fichero de salida de un barrido ajeno.")
    print("=" * 90)
    print()
    print("raices: %s" % ", ".join(raices))
    print("patrones combinados: %s" % patron_cifra_txt)
    print("patron de salvedad: %s (ventana %d caracteres a cada lado)" % (a.patron_salvedad, a.ventana))
    print()
    print("aciertos totales: %d" % total)
    print()
    print("| fichero | aciertos |")
    print("|---|---:|")
    for rel in sorted(aciertos_por_fichero):
        print("| %s | %d |" % (rel, len(aciertos_por_fichero[rel])))
    print()
    for rel in sorted(aciertos_por_fichero):
        lineas = ", ".join(str(l) for l, _c in aciertos_por_fichero[rel])
        print("ENUMERACION de %s (%d): lineas %s" % (rel, len(aciertos_por_fichero[rel]), lineas))
    print()
    print("CON salvedad: %d" % total_con)
    print("ENUMERACION CON salvedad: %s" % (", ".join(lista_con) if lista_con else "(ninguno)"))
    print()
    print("SIN salvedad: %d" % total_sin)
    print("ENUMERACION SIN salvedad: %s" % (", ".join(lista_sin) if lista_sin else "(ninguno)"))
    print()
    if omitidos:
        print("binarios o no utf-8, omitidos (%d): %s" % (len(omitidos), ", ".join(omitidos)))
        print()

    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
