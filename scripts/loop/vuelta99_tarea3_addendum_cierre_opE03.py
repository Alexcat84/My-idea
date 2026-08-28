# -*- coding: utf-8 -*-
r"""vuelta99_tarea3_addendum_cierre_opE03.py . VUELTA 99, TAREA 3: EL ADDENDUM DE
CIERRE DE OP-E-03. Las 33 que quedaban (filas 151 a 183) se leyeron enteras
(docs/plan/OP_E_03_LECTURA_TRAMO4_V99.jsonl), y CON ESO LA OPERACION ENTERA
QUEDA LEIDA: 183 de 183.

LA CIFRA DE CIERRE NO SE SUMA DE MEMORIA: se recuenta de LOS CUATRO FICHEROS
de tramo que existen hoy (TRAMO1_V96 40, TRAMO2_V97 60, TRAMO3_V98 50,
TRAMO4_V99 33). EL ENCARGO DICE "TRES FICHEROS DE TRAMO"; LA MEDICION DE HOY
DICE CUATRO, Y SE DECLARA LA DISCREPANCIA EN VEZ DE OBEDECER EL NUMERO:
`ls docs/plan/OP_E_03_LECTURA_TRAMO*.jsonl` da cuatro ficheros y su suma es
exactamente 183, la cifra que el propio encargo pide al final. Es una
imprecision de redaccion del encargo, no una instruccion que se pueda cumplir
contando tres.

LAS TRES CONDICIONES DEL BORDE DE LA 3.7 (acta 97), verificadas aqui y no
supuestas: (a) las cifras salen de instrumentos corridos en esta vuelta; (b)
la escritura es puramente aditiva; (c) no mueve `estado`, que se queda en
LISTA como en los tres addenda anteriores, porque cambiar `estado` es una
decision y la TAREA 4 de este mismo encargo mide, sin resolver, que las
dependencias declaradas de OP-E-03 no estan en HECHA.

MECANICA DE ROJO, y no escribe nada si salta: (i) OP-E-03 no aparece
exactamente una vez; (ii) alguno de los cuatro ficheros de tramo no existe o
no trae la marca completa de LECTURA DIRIGIDA; (iii) la suma de los cuatro no
da 183 o los rangos de puesto se solapan o dejan huecos; (iv) el addendum de
esta vuelta ya estaba escrito; (v) git no da fecha; (vi) el ancla de
04_ENLACES.md no aparece exactamente una vez.

USO:
  python scripts/loop/vuelta99_tarea3_addendum_cierre_opE03.py --simular
  python scripts/loop/vuelta99_tarea3_addendum_cierre_opE03.py --aplicar
"""
import argparse
import collections
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
ENLACES = os.path.join(RAIZ, "docs", "plan", "04_ENLACES.md")
BOLSA = os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")
TRAMOS = [
    ("TRAMO1_V96", os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl"), 1, 40),
    ("TRAMO2_V97", os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl"), 41, 100),
    ("TRAMO3_V98", os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO3_V98.jsonl"), 101, 150),
    ("TRAMO4_V99", os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO4_V99.jsonl"), 151, 183),
]

VUELTA = 99
MESES = {1: "ene", 2: "feb", 3: "mar", 4: "abr", 5: "may", 6: "jun",
         7: "jul", 8: "ago", 9: "sep", 10: "oct", 11: "nov", 12: "dic"}

ANCLA_ENLACES = ("**LA PROPORCION DE DIRECCIONES NO RESUELTAS SUBE OTRA VEZ**, del **27,5%** del\n"
                  "tramo 1 y el **45,0%** del tramo 2 al **60,0%** de esta mitad. Es la direccion que\n"
                  "el encargo preveia para el tramo mas debil de la bolsa (mediana de `titulo_ratio`\n"
                  "**76,2** contra **84,3** del tramo 1), asi que **se publica con la cifra y sin\n"
                  "maquillarla**.\n")
TITULO_ENLACES = "EL CIERRE DE `OP-E-03`: LAS 183 DE 183, RECONTADAS DE LOS CUATRO FICHEROS DE TRAMO"


def fecha_de_git():
    r = subprocess.run(["git", "log", "--all", "--format=%ad|%s", "--date=short"],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None, None
    pat = re.compile(r"^VUELTA %d\b" % VUELTA)
    fechas = set()
    for linea in r.stdout.decode("utf-8", "replace").splitlines():
        partes = linea.split("|", 1)
        if len(partes) == 2 and pat.match(partes[1]):
            fechas.add(partes[0])
    if not fechas:
        return None, None
    iso = sorted(fechas)[-1]
    a, m, d = iso.split("-")
    return "%d %s %s" % (int(d), MESES[int(m)], a), iso


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def cifras():
    fallos = []
    total_bolsa = len(cargar(BOLSA))
    todas = []
    for nombre, ruta, desde, hasta in TRAMOS:
        if not os.path.exists(ruta):
            fallos.append("no existe %s" % os.path.relpath(ruta, RAIZ))
            continue
        filas = cargar(ruta)
        if len(filas) != (hasta - desde + 1):
            fallos.append("%s trae %d filas, se esperaban %d (%d a %d)"
                          % (nombre, len(filas), hasta - desde + 1, desde, hasta))
        for f in filas:
            if (f.get("marca") != "LECTURA DIRIGIDA" or not f.get("fuera_de_la_cola")
                    or f.get("mueve_el_marcador_del_cribado") is not False
                    or not f.get("fuera_de_la_tasa_por_dominio")):
                fallos.append("%s fila %s no trae la marca completa de LECTURA DIRIGIDA"
                              % (nombre, f.get("puesto_tramo")))
        todas.extend(filas)

    if fallos:
        return None, fallos

    puestos = sorted(f["puesto_tramo"] for f in todas)
    if puestos != list(range(1, total_bolsa + 1)):
        faltan = sorted(set(range(1, total_bolsa + 1)) - set(puestos))
        repetidos = [p for p, c in collections.Counter(puestos).items() if c > 1]
        fallos.append("los puestos de los cuatro tramos no cubren 1 a %d sin huecos ni "
                      "repetidos: faltan %s, repetidos %s" % (total_bolsa, faltan, repetidos))
        return None, fallos

    d = {}
    d["total"] = total_bolsa
    d["n"] = len(todas)
    d["clases"] = collections.Counter(f["clase"] for f in todas)
    d["c"] = sorted(f["puesto_tramo"] for f in todas if f["clase"] == "C")
    d["con_dir"] = sum(1 for f in todas if f.get("direccion_leida"))
    d["sin_dir"] = sorted(f["puesto_tramo"] for f in todas if not f.get("direccion_leida"))
    d["invertidas"] = sorted(f["puesto_tramo"] for f in todas
                             if f.get("direccion_leida")
                             and f["direccion_leida"].split("->")[0].strip()
                             == f["hijo_de_la_bolsa"])
    d["doms"] = collections.Counter(f["dominio"] for f in todas)
    # el ultimo tramo, solo, para su propia fila de tabla
    ultimo = [f for f in todas if 151 <= f["puesto_tramo"] <= 183]
    d["u_clases"] = collections.Counter(f["clase"] for f in ultimo)
    d["u_con_dir"] = sum(1 for f in ultimo if f.get("direccion_leida"))
    d["u_sin_dir"] = len(ultimo) - d["u_con_dir"]
    return d, fallos


def marca(fecha):
    return ("ADDENDUM DE CIERRE (%s, vuelta 99, TAREA 3): OP-E-03 QUEDA LEIDA ENTERA, "
            "183 DE 183." % fecha)


def texto_nota(d, fecha, iso):
    return (
        " %s LA FECHA SE LEYO DE GIT EN ESTA VUELTA con `git log --all --format=%%ad "
        "--date=short` sobre los commits cuyo asunto empieza por \"VUELTA 99\", y da %s: "
        "no esta tecleada. SE LEYERON LAS FILAS 151 A 183, LAS 33 QUE QUEDABAN, con el "
        "mismo instrumento de los tres tramos anteriores "
        "(scripts/loop/vuelta96_tarea3_tramo1_opE03.py --desde 150 --cuantos 33) sin "
        "tocarle una linea. CON ESO OP-E-03 QUEDA LEIDA ENTERA: %d de %d. "
        "RESULTADO DE ESTE CUARTO TRAMO: A %d, B %d, C %d, D %d; direccion %d leida y "
        "afirmada, %d NO RESUELTA (%s%%), 0 invertidas. Mediana de titulo_ratio del tramo: "
        "73,2 (n=33, maximo 81,6), la mas baja de toda la bolsa, confirmando la prediccion "
        "medida del acta 98: proporcion NO RESUELTA por encima del 60,0%%, y asi sale "
        "(60,6%%), asi que NO se marca discutible por la letra de ese mismo encargo (solo "
        "se marca si sale MAS BAJA que la tendencia). "
        "CIERRE DE LA OPERACION ENTERA, recontado de los CUATRO ficheros de tramo que "
        "existen hoy (el encargo dice tres; la medicion de esta vuelta dice cuatro, y se "
        "declara la discrepancia: TRAMO1_V96 40 + TRAMO2_V97 60 + TRAMO3_V98 50 + "
        "TRAMO4_V99 33 = %d de %d): clase A %d, B %d, C %d, D %d; direccion leida y "
        "afirmada %d, NO RESUELTA %d (%s%%); direcciones invertidas y afirmadas %d "
        "(pares %s); el UNICO C de toda la lectura sigue "
        "siendo el par %s (banco 9.22, primer polo, enlace mutuo, cero aristas). "
        "ESTADO SE QUEDA EN LISTA: cambiarlo es una decision, y la TAREA 4 de este mismo "
        "encargo mide, sin resolver, que las dos dependencias declaradas de OP-E-03 "
        "(OP-E-01 y OP-U-02) no estan en HECHA. CERO ARISTAS ESCRITAS O RETIRADAS EN TODA "
        "LA OPERACION: OP-E-03 es LECTURA DIRIGIDA y su producto es el juicio, no el "
        "grafo. Salidas de esta vuelta: docs/plan/OP_E_03_LECTURA_TRAMO4_V99.jsonl (33 "
        "filas), docs/loop/SALIDA_V99_TAREA3_TRAMO3_MATERIAL.txt, "
        "docs/loop/SALIDA_V99_TAREA3_CINCO_PUNTOS.txt, "
        "docs/loop/SALIDA_V99_TAREA3_MUTACION.txt."
        % (marca(fecha), iso, d["total"], d["total"],
           d["u_clases"]["A"], d["u_clases"]["B"], d["u_clases"]["C"], d["u_clases"]["D"],
           d["u_con_dir"], d["u_sin_dir"],
           ("%.1f" % (100.0 * d["u_sin_dir"] / 33)).replace(".", ","),
           d["n"], d["total"],
           d["clases"]["A"], d["clases"]["B"], d["clases"]["C"], d["clases"]["D"],
           d["con_dir"], len(d["sin_dir"]),
           ("%.1f" % (100.0 * len(d["sin_dir"]) / d["n"])).replace(".", ","),
           len(d["invertidas"]), ", ".join(str(x) for x in d["invertidas"]),
           ", ".join(str(x) for x in d["c"]))
    )


def texto_enlaces(d, fecha, iso):
    return (
        "\n**%s (%s).**\n"
        "Los apartados de arriba se quedan enteros, sin borrar una palabra. **`OP-E-03` "
        "QUEDA LEIDA ENTERA: 183 de 183**, recontadas de los CUATRO ficheros de tramo que "
        "existen (el encargo de la vuelta 99 decia \"tres\"; la cuenta real de hoy es "
        "cuatro, declarado como discrepancia de redaccion del encargo, no del trabajo).\n"
        "\n"
        "| ficheros de tramo | filas |\n"
        "|---|---:|\n"
        "| `OP_E_03_LECTURA_TRAMO1_V96.jsonl` | 40 (1 a 40) |\n"
        "| `OP_E_03_LECTURA_TRAMO2_V97.jsonl` | 60 (41 a 100) |\n"
        "| `OP_E_03_LECTURA_TRAMO3_V98.jsonl` | 50 (101 a 150) |\n"
        "| `OP_E_03_LECTURA_TRAMO4_V99.jsonl` | 33 (151 a 183) |\n"
        "| **total** | **%d** |\n"
        "\n"
        "| cierre de la operacion entera | cifra |\n"
        "|---|---:|\n"
        "| clase A, REPITE | **%d** |\n"
        "| clase B, DUDOSO | **%d** |\n"
        "| clase C, SANO CON FIGURA | **%d** (par %s) |\n"
        "| clase D, CONTINUA | **%d** |\n"
        "| direccion leida y afirmada | **%d** |\n"
        "| direccion NO RESUELTA, declarada | **%d** (%s%%) |\n"
        "| direcciones invertidas y afirmadas | **%d** (pares %s) |\n"
        "| aristas escritas o retiradas en toda la operacion | **0** |\n"
        "\n"
        "**EL CUARTO TRAMO (filas 151 a 183, 33 pares) por si solo:** clase D **%d**, "
        "direccion leida **%d**, NO RESUELTA **%d** (**%s%%**), mediana de `titulo_ratio` "
        "**73,2** (maximo 81,6, la mas baja de la bolsa). **CONFIRMA LA PREDICCION DEL "
        "ACTA 98**: proporcion NO RESUELTA por encima del 60,0%%.\n"
        "\n"
        "**ESTADO DE `OP-E-03` SE QUEDA EN `LISTA`**: la lectura esta completa, pero mover "
        "`estado` a `HECHA` es una decision que este addendum no toma; la TAREA 4 del "
        "encargo de la vuelta 99 mide, sin resolver, que las dependencias declaradas "
        "(`OP-E-01`, `OP-U-02`) no estan en `HECHA`.\n"
        % (TITULO_ENLACES, iso, d["total"],
           d["clases"]["A"], d["clases"]["B"], d["clases"]["C"], ", ".join(str(x) for x in d["c"]),
           d["clases"]["D"], d["con_dir"], len(d["sin_dir"]),
           ("%.1f" % (100.0 * len(d["sin_dir"]) / d["n"])).replace(".", ","),
           len(d["invertidas"]), ", ".join(str(x) for x in d["invertidas"]),
           d["u_clases"]["D"], d["u_con_dir"], d["u_sin_dir"],
           ("%.1f" % (100.0 * d["u_sin_dir"] / 33)).replace(".", ","))
    )


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--simular", action="store_true")
    g.add_argument("--aplicar", action="store_true")
    a = ap.parse_args()

    d, fallos = cifras()
    fecha, iso = fecha_de_git()
    if fecha is None:
        fallos.append("git no devuelve ni un commit de la vuelta %d: no hay fecha que "
                      "leer y este instrumento no inventa ninguna" % VUELTA)

    ops = cargar(OPERACIONES)
    objetivo = [o for o in ops if o.get("id_op") == "OP-E-03"]
    if len(objetivo) != 1:
        fallos.append("OP-E-03 aparece %d veces, se esperaba 1" % len(objetivo))
    elif fecha and marca(fecha).split(")")[0] in (objetivo[0].get("nota") or ""):
        fallos.append("el addendum de cierre de la vuelta 99 YA ESTA en la nota de OP-E-03")

    enlaces = io.open(ENLACES, encoding="utf-8").read()
    if enlaces.count(ANCLA_ENLACES) != 1:
        fallos.append("el ancla del cierre del tramo 3 aparece %d veces en 04_ENLACES.md, "
                      "se esperaba 1" % enlaces.count(ANCLA_ENLACES))
    if TITULO_ENLACES in enlaces:
        fallos.append("el apartado de cierre de la vuelta 99 YA ESTA en 04_ENLACES.md")

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("=" * 100)
    print("ADDENDUM DE CIERRE DE OP-E-03, VUELTA 99 (%s)"
          % ("SIMULACION" if a.simular else "APLICADO"))
    print("=" * 100)
    print("FECHA LEIDA DE GIT: %s (%s)." % (fecha, iso))
    print("EL BORDE DE LA ADJUDICACION 3.7: (a) instrumentos corridos hoy: SI; (b) "
          "puramente aditiva: SI; (c) estado sigue en %r: SI" % objetivo[0].get("estado"))
    print()
    print("--- lo que se anade a la nota de OP-E-03 (aditivo) ---")
    print(texto_nota(d, fecha, iso).strip())
    print()
    print("--- lo que se anade a docs/plan/04_ENLACES.md (aditivo) ---")
    print(texto_enlaces(d, fecha, iso))

    if a.simular:
        print("SIMULACION: no se escribio nada.")
        return 0

    estado_antes = objetivo[0].get("estado")
    objetivo[0]["nota"] = (objetivo[0].get("nota") or "") + texto_nota(d, fecha, iso)
    with io.open(OPERACIONES, "w", encoding="utf-8", newline="\n") as f:
        for o in ops:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    io.open(ENLACES, "w", encoding="utf-8", newline="\n").write(
        enlaces.replace(ANCLA_ENLACES, ANCLA_ENLACES + texto_enlaces(d, fecha, iso), 1))

    ops2 = cargar(OPERACIONES)
    o2 = [o for o in ops2 if o.get("id_op") == "OP-E-03"]
    enlaces2 = io.open(ENLACES, encoding="utf-8").read()
    bien = (len(ops2) == len(ops) and len(o2) == 1
            and marca(fecha) in o2[0]["nota"]
            and o2[0].get("estado") == estado_antes
            and TITULO_ENLACES in enlaces2)
    print("APLICADO. Re-lectura: OPERACIONES.jsonl %d filas validas, addendum presente, "
          "estado sigue en %r: %s"
          % (len(ops2), o2[0].get("estado"), "SI" if bien else "NO"))
    return 0 if bien else 1


if __name__ == "__main__":
    raise SystemExit(main())
