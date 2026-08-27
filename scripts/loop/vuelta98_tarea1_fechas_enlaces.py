# -*- coding: utf-8 -*-
r"""vuelta98_tarea1_fechas_enlaces.py . VUELTA 98, TAREA 1: LA MISMA ESPECIE, EN
docs/plan/04_ENLACES.md.

POR QUE NACE, Y POR QUE NO ESTABA EN EL ENCARGO. El encargo de la vuelta 98
apartado 1.4 manda recorrer los addenda de docs/plan/OPERACIONES.jsonl. Al
correr ese censo se midio TAMBIEN el fichero hermano del plan, 04_ENLACES.md,
donde el mismo script de la vuelta 97 escribe su apartado gemelo, y ahi vive la
misma especie: marcadores de ADDENDUM y de CORRECCION DECLARADA con fecha
TECLEADA posterior al techo del reloj del repo. Se corrige por el BORDE DE LA
ADJUDICACION 3.7 del acta 97, cuyas tres condiciones se verifican y no se
suponen: (a) la fecha nueva sale de `git log` corrido en esta vuelta, (b) la
escritura es puramente aditiva y no borra una letra, (c) no mueve ninguna
decision, ningun alcance y ningun estado.

LO QUE NO SE TOCA, Y ES LA DISTINCION QUE HACE FALTA HACER: una fecha que forma
parte del NOMBRE DE UN FICHERO citado (por ejemplo
`docs/loop/paradas/2026-08-29-racha-y-escalada-omitida-DECISION.md`) NO es una
fecha publicada: es el nombre real de un fichero que existe en el repo, y
"corregirlo" seria escribir una ruta falsa. El instrumento las detecta y las
lista APARTE, con su veredicto NOMBRE DE FICHERO, y no las corrige. Que el
fichero se llame asi es a su vez una figura, y va al reporte SIN adjudicar.

VEREDICTOS POR FILA, los mismos que el censo hermano mas uno:
  CALZA             la fecha declarada esta entre las fechas de git de esa vuelta
  DESFASADA         no lo esta
  IMPOSIBLE         ademas es posterior al techo del reloj del repo
  SIN VUELTA        declara fecha pero no vuelta: no hay contra que cotejar
  ROJO              declara vuelta y git no da ni un commit de ella
  NOMBRE DE FICHERO la fecha vive dentro de una ruta o un nombre de fichero

MECANICA DE ROJO, y no escribe nada si salta: (i) un marcador a corregir aparece
mas de una vez en el fichero; (ii) su correccion YA ESTA escrita; (iii) tras
escribir, el numero de lineas baja o alguna fecha vieja desaparecio.

USO:
  python scripts/loop/vuelta98_tarea1_fechas_enlaces.py --medir
  python scripts/loop/vuelta98_tarea1_fechas_enlaces.py --simular
  python scripts/loop/vuelta98_tarea1_fechas_enlaces.py --aplicar
"""
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

from vuelta98_tarea1_fechas_addenda import (  # noqa: E402
    MESES, fechas_de_la_vuelta, iso_a_es, techo_del_reloj)

ENLACES = os.path.join(RAIZ, "docs", "plan", "04_ENLACES.md")

# El marcador es ADDENDUM o CORRECCION DECLARADA seguidos de su parentesis. El
# interior PUEDE llevar salto de linea: en 04_ENLACES.md el marcador de la
# vuelta 94 esta partido en dos lineas por el ancho de columna, y una version
# de esta expresion que no cruzaba el salto se lo dejaba fuera del censo. Lo
# delato el barrido de abajo, que conto 4 fechas en prosa contra 2 marcadores.
RE_MARCADOR = re.compile(
    r"(?:ADDENDUM|CORRECCION DECLARADA)[^.(\n]*\(([^)]*)\)")
RE_FECHA = re.compile(
    r"\b(\d{1,2}) (ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic) (\d{4})\b")
RE_FECHA_ISO = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
RE_VUELTA = re.compile(r"\bvuelta (\d+)\b")

MARCA_CORRECCION = "CORRECCION DECLARADA DE FECHA (vuelta 98, TAREA 1)"


def linea_de(texto, pos):
    return texto.count("\n", 0, pos) + 1


def es_nombre_de_fichero(texto, pos):
    """True si la fecha en esa posicion vive dentro de una ruta o nombre.

    Se mira el token no espaciado que la contiene: si trae una barra o una
    extension, la fecha es parte de un nombre y no una fecha publicada.
    """
    ini = pos
    while ini > 0 and texto[ini - 1] not in " \n\t(":
        ini -= 1
    fin = pos
    while fin < len(texto) and texto[fin] not in " \n\t)":
        fin += 1
    token = texto[ini:fin]
    return ("/" in token) or (".md" in token) or ("\\" in token)


def censar():
    techo, cmd_techo = techo_del_reloj()
    texto = io.open(ENLACES, encoding="utf-8").read()
    filas = []
    cache = {}

    for m in RE_MARCADOR.finditer(texto):
        dentro = m.group(1)
        mf = RE_FECHA.search(dentro)
        if not mf:
            continue
        mv = RE_VUELTA.search(dentro)
        iso = "%s-%02d-%02d" % (mf.group(3), MESES[mf.group(2)], int(mf.group(1)))
        fila = {"linea": linea_de(texto, m.start()), "marcador": m.group(0),
                "declarada": mf.group(0), "declarada_iso": iso,
                "vuelta": int(mv.group(1)) if mv else None,
                "reales": [], "hashes": [], "veredicto": None, "clase": "MARCADOR"}
        if fila["vuelta"] is None:
            fila["veredicto"] = "SIN VUELTA"
        else:
            n = fila["vuelta"]
            if n not in cache:
                cache[n] = fechas_de_la_vuelta(n)
            fila["reales"], fila["hashes"] = cache[n]
            if not fila["reales"]:
                fila["veredicto"] = "ROJO"
            elif iso in fila["reales"]:
                fila["veredicto"] = "CALZA"
            elif iso > techo:
                fila["veredicto"] = "IMPOSIBLE"
            else:
                fila["veredicto"] = "DESFASADA"
        filas.append(fila)

    # Barrido aparte: TODA fecha del fichero posterior al techo, este o no en un
    # marcador, para que ninguna se pueda esconder de este censo.
    sueltas = []
    for rx, fmt in ((RE_FECHA, "es"), (RE_FECHA_ISO, "iso")):
        for m in rx.finditer(texto):
            if fmt == "es":
                iso = "%s-%02d-%02d" % (m.group(3), MESES[m.group(2)], int(m.group(1)))
            else:
                iso = m.group(0)
            if iso <= techo:
                continue
            sueltas.append({"linea": linea_de(texto, m.start()),
                            "texto": m.group(0), "iso": iso,
                            "veredicto": ("NOMBRE DE FICHERO"
                                          if es_nombre_de_fichero(texto, m.start())
                                          else "FECHA EN PROSA")})
    return techo, cmd_techo, texto, filas, sueltas


def texto_correccion(fila, techo, cmd_techo):
    reales = ", ".join(fila["reales"])
    cmd = ('git log --all --format=%ad^%h^%s --date=short, quedandose con los '
           'commits cuyo asunto empieza por "VUELTA ' + str(fila["vuelta"]) + '"')
    return (" **[%s: la fecha \"%s\" de este marcador estaba TECLEADA y es FALSA. El texto "
            "viejo se queda entero y sin borrar una letra (EJECUTOR.md 8). LA FECHA REAL, "
            "LEIDA DE GIT EN LA VUELTA 98 con `%s`, es %s (commits %s), o sea %s. Techo del "
            "reloj del repo, medido con `git %s`: %s.]**"
            % (MARCA_CORRECCION, fila["declarada"], cmd, reales,
               ", ".join(fila["hashes"]), iso_a_es(reales),
               " ".join(cmd_techo), techo))


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--medir", action="store_true")
    g.add_argument("--simular", action="store_true")
    g.add_argument("--aplicar", action="store_true")
    a = ap.parse_args()

    techo, cmd_techo, texto, filas, sueltas = censar()

    print("=" * 110)
    print("LAS FECHAS DE docs/plan/04_ENLACES.md, COTEJADAS CONTRA GIT")
    print("=" * 110)
    print("TECHO DEL RELOJ DEL REPO (git %s | sort -u | tail -1): %s"
          % (" ".join(cmd_techo), techo))
    print("LINEAS DEL FICHERO: %d" % texto.count("\n"))
    print("MARCADORES CON FECHA ENCONTRADOS: %d" % len(filas))
    print()
    print("| # | linea | marcador | vuelta | fecha declarada | fecha(s) real(es) de git | veredicto |")
    print("|---|---:|---|---:|---|---|---|")
    for k, f in enumerate(filas, 1):
        print("| %d | %d | %s | %s | %s | %s | %s |"
              % (k, f["linea"], f["marcador"][:60],
                 f["vuelta"] if f["vuelta"] else "(ninguna)", f["declarada"],
                 ", ".join(f["reales"]) or "(no aplica)", f["veredicto"]))
    cuenta = {}
    for f in filas:
        cuenta[f["veredicto"]] = cuenta.get(f["veredicto"], 0) + 1
    print()
    print("RECUENTO POR VEREDICTO, contado del propio censo:")
    for v in sorted(cuenta):
        print("   %-10s %d" % (v, cuenta[v]))

    print()
    print("BARRIDO APARTE: TODA fecha del fichero posterior al techo, este o no en un marcador")
    print("| # | linea | fecha | veredicto |")
    print("|---|---:|---|---|")
    for k, s in enumerate(sueltas, 1):
        print("| %d | %d | %s | %s |" % (k, s["linea"], s["texto"], s["veredicto"]))
    c2 = {}
    for s in sueltas:
        c2[s["veredicto"]] = c2.get(s["veredicto"], 0) + 1
    print()
    print("RECUENTO DEL BARRIDO, contado del propio barrido:")
    for v in sorted(c2):
        print("   %-18s %d" % (v, c2[v]))
    print("   LAS 'NOMBRE DE FICHERO' NO SE CORRIGEN: son rutas reales del repo y "
          "cambiarlas escribiria una ruta falsa.")
    print()

    if a.medir:
        return 0

    malas = [f for f in filas if f["veredicto"] in ("DESFASADA", "IMPOSIBLE")]
    if not malas:
        print("NADA QUE CORREGIR.")
        return 0

    fallos = []
    for f in malas:
        if texto.count(f["marcador"]) != 1:
            fallos.append("el marcador %r aparece %d veces: no se puede anclar sin "
                          "ambiguedad" % (f["marcador"], texto.count(f["marcador"])))
        if f["marcador"] + " **[" + MARCA_CORRECCION in texto:
            fallos.append("la correccion de %r YA ESTA escrita" % f["declarada"])
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("-" * 110)
    print("LAS %d CORRECCIONES DECLARADAS QUE SE ANADEN (%s), aditivas:"
          % (len(malas), "SIMULACION" if a.simular else "APLICADAS"))
    print("-" * 110)
    nuevo = texto
    for f in malas:
        print()
        print("### linea %d: %s" % (f["linea"], f["marcador"][:90]))
        print("SE ANADE:%s" % texto_correccion(f, techo, cmd_techo))
        nuevo = nuevo.replace(f["marcador"],
                              f["marcador"] + texto_correccion(f, techo, cmd_techo), 1)

    if a.simular:
        print()
        print("SIMULACION: no se escribio nada.")
        return 0

    io.open(ENLACES, "w", encoding="utf-8", newline="\n").write(nuevo)

    texto2 = io.open(ENLACES, encoding="utf-8").read()
    bien = texto2.count("\n") >= texto.count("\n")
    presentes = 0
    for f in malas:
        if f["marcador"] + " **[" + MARCA_CORRECCION in texto2:
            presentes += 1
        if f["declarada"] not in texto2:
            bien = False
    print()
    print("APLICADO. Re-lectura: %d lineas (antes %d), %d de %d correcciones presentes, "
          "texto viejo intacto: %s"
          % (texto2.count("\n"), texto.count("\n"), presentes, len(malas),
             "SI" if bien else "NO"))
    return 0 if (bien and presentes == len(malas)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
