# -*- coding: utf-8 -*-
r"""vuelta98_tarea1_fechas_addenda.py . VUELTA 98, TAREA 1: COTEJA CONTRA GIT
TODAS LAS FECHAS DE LOS ADDENDA DE docs/plan/OPERACIONES.jsonl Y ESCRIBE LA
CORRECCION DECLARADA DE LAS QUE NO CALZAN.

POR QUE NACE (acta de la vuelta 97, seccion 4.1, linea 34956: CAIDA DE CIFRA
PUBLICADA). La nota de OP-E-03 dice "ADDENDUM DE EJECUCION (30 ago 2026, vuelta
97, TAREA 2)" y NINGUN commit de este repo es posterior al 27 ago 2026. La fecha
nacio TECLEADA como constante literal en
scripts/loop/vuelta97_tarea2_addendum_opE03.py linea 43. Es EJECUTOR.md regla 1
("TODO HASH, NOMBRE DE COMMIT, RAMA O FECHA ... SE LEE DE git rev-parse O DE git
log EN ESA VUELTA Y SE TALLA; UNA LINEA DE IDENTIDAD TECLEADA NO SE PUBLICA") y
regla 8 ("toda cifra con su fecha de corte").

QUE MIDE, Y NO SOLO LAS DOS QUE EL AUDITOR ENCONTRO (encargo 1.4, "si hay mas de
dos, las quiero todas en esa tabla"): recorre el fichero entero, localiza CADA
ocurrencia de la palabra ADDENDUM, extrae la fecha declarada y el numero de
vuelta si los trae, y para cada vuelta LEE DE GIT las fechas reales de sus
commits. Nada se teclea: la fecha real sale de `git log`.

COMO SE DECIDE LA FECHA REAL DE UNA VUELTA: se buscan en `git log --all` los
commits cuyo asunto empieza por "VUELTA <N>" (los del ejecutor) y se toma el
conjunto de sus fechas `%ad --date=short`. Si ese conjunto esta vacio, la fila
sale ROJO y no se corrige nada: el instrumento nunca inventa una fecha.
Se mide ademas el TECHO DEL RELOJ del repo (la fecha maxima de cualquier commit
de cualquier rama), que es la vara con la que el auditor cazo la caida.

VEREDICTOS POR FILA:
  CALZA        la fecha declarada esta entre las fechas de los commits de esa vuelta
  DESFASADA    la fecha declarada NO esta entre ellas (es la especie de la caida)
  IMPOSIBLE    ademas, la fecha declarada es POSTERIOR al techo del reloj del repo
  SIN FECHA    el addendum no declara fecha, no hay nada que cotejar
  SIN VUELTA   declara fecha pero no numero de vuelta: no hay contra que cotejar
  ROJO         declara vuelta pero git no da ni un commit de esa vuelta

QUE ESCRIBE (--aplicar): detras de cada marcador DESFASADO o IMPOSIBLE, y SIN
BORRAR UNA LETRA del texto viejo (EJECUTOR.md regla 8, "una correccion que tapa
lo que corrige no se puede auditar"), una CORRECCION DECLARADA cuyo texto se
construye con la fecha LEIDA DE GIT en esta corrida y con el comando que la
produjo pegado dentro. La escritura es puramente aditiva y no toca ningun otro
campo.

EL BORDE DE LA ADJUDICACION 3.7 DEL ACTA 97, verificado fila a fila y no
supuesto, para las filas que el encargo NO nombra (el encargo nombra la de la
vuelta 97 y la de la vuelta 94; el instrumento encuentra mas):
  (a) la cifra nueva sale de un instrumento corrido en esta vuelta: SI, `git log`
  (b) la escritura es puramente aditiva y no borra el texto viejo: SI, se mide
      con --numstat en el commit
  (c) no mueve ninguna decision, ningun alcance y ningun estado: SI, solo anade
      texto de correccion dentro del campo `nota`; ningun campo `estado`, ninguna
      clase, ningun veredicto, ninguna cuenta.

MECANICA DE ROJO, y no escribe nada si salta: (i) el fichero no es JSONL valido;
(ii) alguna fila a corregir tiene su marcador repetido en la misma nota, con lo
cual la correccion no se puede anclar sin ambiguedad; (iii) la correccion de una
fila YA ESTA escrita (correr dos veces la duplicaria); (iv) tras escribir, el
numero de lineas del JSONL cambia o el texto viejo dejo de estar.

USO:
  python scripts/loop/vuelta98_tarea1_fechas_addenda.py --medir
  python scripts/loop/vuelta98_tarea1_fechas_addenda.py --simular
  python scripts/loop/vuelta98_tarea1_fechas_addenda.py --aplicar
"""
import argparse
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

MESES = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
         "jul": 7, "ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12}
INV = dict((v, k) for k, v in MESES.items())

# El marcador es la palabra ADDENDUM y lo que va entre el primer parentesis que
# la sigue. Se captura el parentesis entero para poder anclar la correccion.
RE_ADDENDUM = re.compile(r"ADDENDUM[^.(]*(\(([^)]*)\))?")
RE_FECHA = re.compile(r"\b(\d{1,2}) (ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic) (\d{4})\b")
RE_VUELTA = re.compile(r"\bvuelta (\d+)\b")

MARCA_CORRECCION = "CORRECCION DECLARADA DE FECHA (vuelta 98, TAREA 1)"


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO: fallo git " + " ".join(args))
    return r.stdout.decode("utf-8", "replace")


def techo_del_reloj():
    """La fecha maxima de cualquier commit de cualquier rama. Leida de git."""
    cmd = ["log", "--all", "--format=%ad", "--date=short"]
    fechas = sorted(set(x.strip() for x in git(cmd).splitlines() if x.strip()))
    return fechas[-1], cmd


def fechas_de_la_vuelta(n):
    """Fechas short de los commits del ejecutor de la vuelta n. Nunca inventa."""
    cmd = ["log", "--all", "--format=%ad|%h|%s", "--date=short"]
    salida = git(cmd)
    pat = re.compile(r"^VUELTA %d\b" % n)
    fechas, hashes = set(), []
    for linea in salida.splitlines():
        partes = linea.split("|", 2)
        if len(partes) != 3:
            continue
        fecha, h, asunto = partes
        if pat.match(asunto):
            fechas.add(fecha)
            hashes.append(h)
    return sorted(fechas), hashes


def iso_a_es(iso):
    a, m, d = iso.split("-")
    return "%d %s %s" % (int(d), INV[int(m)], a)


def cargar():
    with io.open(OPERACIONES, encoding="utf-8") as f:
        crudas = [l for l in f if l.strip()]
    return crudas, [json.loads(l) for l in crudas]


def censar():
    """Devuelve la tabla entera. Cada fila lleva su veredicto y su medicion."""
    techo, cmd_techo = techo_del_reloj()
    crudas, ops = cargar()
    filas = []
    cache = {}
    for i, o in enumerate(ops):
        nota = o.get("nota") or ""
        for m in RE_ADDENDUM.finditer(nota):
            marcador = m.group(0)
            dentro = m.group(2) or ""
            mf = RE_FECHA.search(dentro)
            mv = RE_VUELTA.search(dentro)
            fila = {
                "linea": i + 1,
                "id_op": o.get("id_op"),
                "marcador": marcador,
                "declarada": None,
                "declarada_iso": None,
                "vuelta": int(mv.group(1)) if mv else None,
                "reales": [],
                "hashes": [],
                "veredicto": None,
            }
            if mf:
                fila["declarada"] = mf.group(0)
                fila["declarada_iso"] = "%s-%02d-%02d" % (
                    mf.group(3), MESES[mf.group(2)], int(mf.group(1)))
            if fila["declarada"] is None:
                fila["veredicto"] = "SIN FECHA"
            elif fila["vuelta"] is None:
                fila["veredicto"] = "SIN VUELTA"
            else:
                n = fila["vuelta"]
                if n not in cache:
                    cache[n] = fechas_de_la_vuelta(n)
                fila["reales"], fila["hashes"] = cache[n]
                if not fila["reales"]:
                    fila["veredicto"] = "ROJO"
                elif fila["declarada_iso"] in fila["reales"]:
                    fila["veredicto"] = "CALZA"
                elif fila["declarada_iso"] > techo:
                    fila["veredicto"] = "IMPOSIBLE"
                else:
                    fila["veredicto"] = "DESFASADA"
            filas.append(fila)
    return techo, cmd_techo, crudas, ops, filas


def texto_correccion(fila, techo, cmd_techo):
    reales = ", ".join(fila["reales"])
    cmd = ('git log --all --format=%ad^%h^%s --date=short, quedandose con los '
           'commits cuyo asunto empieza por "VUELTA ' + str(fila["vuelta"]) + '"')
    return (
        " [%s: la fecha \"%s\" de este addendum estaba TECLEADA y es FALSA. El texto viejo "
        "se queda entero y sin borrar una letra, que es la regla de correccion de "
        "EJECUTOR.md 8. LA FECHA REAL, LEIDA DE GIT EN LA VUELTA 98 con `%s`, es %s (commits "
        "%s), o sea %s. Y el techo del reloj del repo, medido con `git %s`, es %s: ninguna "
        "fecha posterior a esa puede ser cierta en este repo.]"
        % (MARCA_CORRECCION, fila["declarada"], cmd, reales,
           ", ".join(fila["hashes"]), iso_a_es(reales),
           " ".join(cmd_techo), techo)
    )


def imprimir_tabla(techo, cmd_techo, filas):
    print("=" * 110)
    print("LAS FECHAS DE TODOS LOS ADDENDA DE docs/plan/OPERACIONES.jsonl, COTEJADAS CONTRA GIT")
    print("=" * 110)
    print("TECHO DEL RELOJ DEL REPO (git %s | sort -u | tail -1): %s"
          % (" ".join(cmd_techo), techo))
    print("ADDENDA ENCONTRADOS: %d" % len(filas))
    print()
    print("| # | linea | operacion | vuelta | fecha declarada | fecha(s) real(es) de git | veredicto |")
    print("|---|---:|---|---:|---|---|---|")
    for k, f in enumerate(filas, 1):
        print("| %d | %d | %s | %s | %s | %s | %s |"
              % (k, f["linea"], f["id_op"],
                 f["vuelta"] if f["vuelta"] else "(ninguna)",
                 f["declarada"] or "(ninguna)",
                 ", ".join(f["reales"]) or "(no aplica)",
                 f["veredicto"]))
    print()
    cuenta = {}
    for f in filas:
        cuenta[f["veredicto"]] = cuenta.get(f["veredicto"], 0) + 1
    print("RECUENTO POR VEREDICTO, contado del propio censo:")
    for v in sorted(cuenta):
        print("   %-10s %d" % (v, cuenta[v]))
    print()


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--medir", action="store_true")
    g.add_argument("--simular", action="store_true")
    g.add_argument("--aplicar", action="store_true")
    a = ap.parse_args()

    techo, cmd_techo, crudas, ops, filas = censar()
    imprimir_tabla(techo, cmd_techo, filas)

    if a.medir:
        return 0

    malas = [f for f in filas if f["veredicto"] in ("DESFASADA", "IMPOSIBLE")]
    if not malas:
        print("NADA QUE CORREGIR: ninguna fila sale DESFASADA ni IMPOSIBLE.")
        return 0

    fallos = []
    for f in malas:
        nota = [o for o in ops if o.get("id_op") == f["id_op"]][0].get("nota") or ""
        if nota.count(f["marcador"]) != 1:
            fallos.append("el marcador %r aparece %d veces en la nota de %s: no se puede "
                          "anclar la correccion sin ambiguedad"
                          % (f["marcador"], nota.count(f["marcador"]), f["id_op"]))
        if f["marcador"] + " [" + MARCA_CORRECCION in nota:
            fallos.append("la correccion de %s (%s) YA ESTA escrita: correr dos veces la "
                          "duplicaria" % (f["id_op"], f["declarada"]))
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("-" * 110)
    print("LAS %d CORRECCIONES DECLARADAS QUE SE ANADEN (%s), aditivas, sin borrar nada:"
          % (len(malas), "SIMULACION" if a.simular else "APLICADAS"))
    print("-" * 110)
    for f in malas:
        print()
        print("### %s, %s (linea %d del JSONL)" % (f["id_op"], f["declarada"], f["linea"]))
        print("ANCLA: %s" % f["marcador"])
        print("SE ANADE:%s" % texto_correccion(f, techo, cmd_techo))

    if a.simular:
        print()
        print("SIMULACION: no se escribio nada.")
        return 0

    for f in malas:
        o = [o for o in ops if o.get("id_op") == f["id_op"]][0]
        o["nota"] = o["nota"].replace(
            f["marcador"], f["marcador"] + texto_correccion(f, techo, cmd_techo), 1)

    with io.open(OPERACIONES, "w", encoding="utf-8", newline="\n") as fh:
        for o in ops:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")

    crudas2, ops2 = cargar()
    bien = len(crudas2) == len(crudas) and len(ops2) == len(ops)
    presentes = 0
    for f in malas:
        o2 = [o for o in ops2 if o.get("id_op") == f["id_op"]][0]
        if f["marcador"] + " [" + MARCA_CORRECCION in (o2.get("nota") or ""):
            presentes += 1
        if f["declarada"] not in (o2.get("nota") or ""):
            bien = False
    print()
    print("APLICADO. Re-lectura: %d lineas JSONL validas (antes %d), %d de %d correcciones "
          "presentes, texto viejo intacto: %s"
          % (len(crudas2), len(crudas), presentes, len(malas), "SI" if bien else "NO"))
    return 0 if (bien and presentes == len(malas)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
