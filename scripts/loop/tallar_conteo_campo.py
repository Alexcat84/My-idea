# -*- coding: utf-8 -*-
"""tallar_conteo_campo.py . LA ESCALADA A LAS FASES MECANICAS (TAREA 3.a de la
vuelta 90, decision del fundador del 29 ago 2026, opcion a: la escalada del 26
ago 2026 que quedo sin ejecutar hasta que la racha de reporte llego a TRES
tandas seguidas, vueltas 87, 88 y 89).

TALLADOR HERMANO de scripts/loop/tallar_cabecera_reporte.py: aquel talla LA
CABECERA (censo, Gate 0, aristas, motor, web, tsc, identidad); este talla
CUALQUIER CIFRA O TABLA DE COMPOSICION DE UN FICHERO JSONL EN LAS FASES
MECANICAS (longitud de un campo, o cuenta de un valor exacto), que es la clase
de afirmacion que EJECUTOR.md regla 1 ("LA TABLA SE CUENTA DE SU FICHERO")
alcanza y que la cabecera NUNCA cubrio, porque la cabecera solo lee salidas de
GATE 0 / MOTOR / WEB / TSC / MARCADOR, no un JSONL de plan cualquiera.

POR QUE NACE, CON EL EJEMPLAR DELANTE (acta de la vuelta 89, seccion 3.1,
`docs/loop/ACTA_AUDITOR.md` lineas 30167 a 30208). El reporte de la vuelta 89
publico que el campo `frase` de `docs/plan/COSECHA_RAZONES_D.jsonl` estaba
"truncado a 200 caracteres exactos... VERIFICADO", con siete puestos de
ejemplo (1134, 1149, 1995, 2023, 2082, 2106, 2038). DOS de los siete (2023 y
2082) median 305 y 263 caracteres, no 200: la palabra "verificado" describia
una lectura tecleada, no una salida de instrumento. Este tallador es ese
instrumento: LA CIFRA Y LA LISTA DE EJEMPLOS SALEN DE AQUI, o no se publican.

QUE MIDE, EXACTO Y NADA MAS (TAREA 3.a, la vara de alcance de la decision del
fundador): dado un fichero JSONL y un CAMPO, cuenta cuantas filas tienen
`len(campo)` igual, mayor o menor que una LONGITUD DE REFERENCIA, y el maximo
del campo en todo el fichero. Con --verificar-puestos, ademas COTEJA una
lista de puestos citables (los que un reporte quisiera poner de ejemplo)
contra su `len(campo)` REAL, fila por fila: es el modo que habria atrapado el
2023 y el 2082 antes de que el reporte los publicara como ejemplo de 200.

MECANICA DE ROJO, identica a la del resto de esta familia de talladores: si
el fichero no existe, si el campo no aparece en una fila, o si un puesto
pedido por --verificar-puestos no esta en el fichero, NO TALLA NADA y sale
con exit 1. Nunca inventa una cifra ni una fila.

USO:
  python scripts/loop/tallar_conteo_campo.py --fichero docs/plan/COSECHA_RAZONES_D.jsonl --campo frase --longitud-exacta 200
  python scripts/loop/tallar_conteo_campo.py --fichero docs/plan/COSECHA_RAZONES_D.jsonl --campo frase --longitud-exacta 200 --verificar-puestos 1134,1149,1995,2023,2082,2106,2038

CASO OBLIGATORIO (vuelta 90), contra el ejemplar de la vuelta 89: tallar
`docs/plan/COSECHA_RAZONES_D.jsonl` con `--campo frase --longitud-exacta 200`
tiene que dar **397 filas, 270 con `len` exactamente 200, 23 por encima
(maximo 335), 104 por debajo**, y `--verificar-puestos` sobre los siete
ejemplos de la vuelta 89 tiene que marcar 2023 y 2082 como DISTINTOS de 200
(305 y 263), no como "verificado".
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def clasifica_longitud(fila, campo, n):
    """LA UNICA PIEZA DE JUICIO DE ESTE TALLADOR, aislada a proposito para que
    su propio caso rojo se pueda probar por mutacion (TAREA 3.b, vuelta 90):
    dado el CAMPO de una fila y la longitud de referencia N, dice si mide
    IGUAL, MAYOR o MENOR. `--verificar-puestos` y el conteo de la tabla llaman
    a esta misma funcion; no hay una segunda cuenta paralela que pudiera
    divergir de ella."""
    L = len(fila[campo])
    if L == n:
        return "IGUAL"
    return "MAYOR" if L > n else "MENOR"


def cargar_jsonl(ruta, fallos):
    ruta_abs = ruta if os.path.isabs(ruta) else os.path.join(RAIZ, ruta)
    if not os.path.exists(ruta_abs):
        fallos.append("no existe el fichero %s" % ruta)
        return None
    filas = []
    with io.open(ruta_abs, encoding="utf-8") as f:
        for n, linea in enumerate(f, 1):
            if not linea.strip():
                continue
            try:
                filas.append(json.loads(linea))
            except ValueError as e:
                fallos.append("linea %d de %s no es JSON valido: %s" % (n, ruta, e))
                return None
    return filas


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fichero", required=True, help="ruta al JSONL, relativa a la raiz del repo")
    ap.add_argument("--campo", required=True, help="el campo cuya longitud se mide")
    ap.add_argument("--longitud-exacta", type=int, required=True, metavar="N",
                    help="la longitud de referencia (p.ej. 200 para un truncado a 200 caracteres)")
    ap.add_argument("--clave-puesto", default="puesto",
                    help="el campo que identifica cada fila para --verificar-puestos (por defecto 'puesto')")
    ap.add_argument("--verificar-puestos", default=None,
                    help="lista separada por comas de valores de --clave-puesto a cotejar fila por fila")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    fallos = []
    filas = cargar_jsonl(a.fichero, fallos)
    if fallos:
        print("ROJO, %d cosa(s) no se pudieron leer y NO se talla nada:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    sin_campo = [f for f in filas if a.campo not in f]
    if sin_campo:
        print("ROJO: %d fila(s) de %s no traen el campo '%s'. NO SE TALLA NADA."
              % (len(sin_campo), a.fichero, a.campo))
        return 1

    # PULIDO (acta de la vuelta 90, seccion 1.11): la existencia de los
    # puestos pedidos por --verificar-puestos se valida AQUI, ANTES de
    # imprimir nada, para que un ROJO por puesto inexistente no imprima
    # primero la tabla de distribucion y diga "NO SE TALLA NADA" despues.
    # Si cae en ROJO, no se imprime ni una linea de tabla: las palabras y
    # la salida dicen lo mismo.
    pedidos_txt = []
    indice = {}
    if a.verificar_puestos:
        pedidos_txt = [p.strip() for p in a.verificar_puestos.split(",") if p.strip()]
        indice = {str(f.get(a.clave_puesto)): f for f in filas}
        faltantes = [p for p in pedidos_txt if p not in indice]
        if faltantes:
            print("ROJO: %d %s(s) pedido(s) no existen en %s: %s. NO SE TALLA NADA."
                  % (len(faltantes), a.clave_puesto, a.fichero, ", ".join(faltantes)))
            return 1

    n = a.longitud_exacta
    clases = [clasifica_longitud(f, a.campo, n) for f in filas]
    iguales = clases.count("IGUAL")
    mayores = clases.count("MAYOR")
    menores = clases.count("MENOR")
    maximo = max(len(f[a.campo]) for f in filas) if filas else 0

    print("=" * 78)
    print("TALLA DE CONTEO DE CAMPO. Cada cifra sale de %s, campo '%s'; ninguna tecleada." % (a.fichero, a.campo))
    print("=" * 78)
    print()
    print("| | |")
    print("|---|---:|")
    print("| filas totales | %d |" % len(filas))
    print("| con `len(%s)` == %d | %d |" % (a.campo, n, iguales))
    print("| con `len(%s)` > %d (maximo %d) | %d |" % (a.campo, n, maximo, mayores))
    print("| con `len(%s)` < %d | %d |" % (a.campo, n, menores))
    print()

    resultado = 0
    if a.verificar_puestos:
        print("--- COTEJO DE PUESTOS CITADOS CONTRA SU `len(%s)` REAL ---" % a.campo)
        print()
        print("| %s citado | `len(%s)` medido | == %d |" % (a.clave_puesto, a.campo, n))
        print("|---:|---:|---|")
        distintos = 0
        for p in pedidos_txt:
            fila = indice[p]
            L = len(fila[a.campo])
            clase = clasifica_longitud(fila, a.campo, n)
            marca = "SI" if clase == "IGUAL" else "**NO, DISTINTO**"
            if clase != "IGUAL":
                distintos += 1
            print("| %s | %d | %s |" % (p, L, marca))
        print()
        print("cotejados: %d | con `len` DISTINTO de %d: %d" % (len(pedidos_txt), n, distintos))
        if distintos:
            print("AVISO: %d de los %d puestos citados NO tienen `len(%s)` == %d: "
                  "publicarlos como ejemplo de esa cifra seria la caida de la vuelta 89."
                  % (distintos, len(pedidos_txt), a.campo, n))
            resultado = 0  # el tallador informa, no decide si el reporte los usa o no

    print()
    print("FIN")
    return resultado


if __name__ == "__main__":
    raise SystemExit(main())
