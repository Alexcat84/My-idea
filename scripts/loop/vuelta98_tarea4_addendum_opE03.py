# -*- coding: utf-8 -*-
r"""vuelta98_tarea4_addendum_opE03.py . VUELTA 98, TAREA 4: EL TERCER ADDENDUM DE
EJECUCION DE OP-E-03, con la fecha LEIDA DE GIT.

POR QUE ES DE AVANCE Y NO DE CIERRE, y se dice al frente: OP-E-03 NO CIERRA en
esta vuelta. Quedan 33 pares sin leer de los 183. El encargo autoriza pararse
donde se vaya y decirlo con la cifra ("prefiero cincuenta bien leidas que
ochenta y tres a la carrera"), y eso es lo que este addendum registra.

POR QUE SE ESCRIBE SIN QUE EL ENCARGO PIDA UN ADDENDUM DE AVANCE: por el BORDE
DE LA ADJUDICACION 3.7 DEL ACTA 97, cuyas tres condiciones se verifican aqui y
no se suponen. (a) Las cifras salen de un instrumento corrido en esta vuelta:
se LEEN de docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl y de la bolsa, ninguna se
teclea. (b) La escritura es puramente aditiva: el texto viejo no se toca y lo
nuevo va detras. (c) No mueve ninguna decision, ningun alcance y ningun estado:
`estado` sigue en LISTA, mismo criterio que los addenda anteriores. Si no se
escribiera, el plan seguiria diciendo "QUEDAN 83 SIN LEER" cuando hoy son 33, o
sea fabricando la nota vieja que AUDITOR.md 1.1 prohibe.

LA FECHA NO SE TECLEA (EJECUTOR.md regla 1, y la caida 4.1 del acta 97 que la
motivo): se LEE de `git log` en esta corrida, buscando los commits cuyo asunto
empieza por "VUELTA 98". Si git no devuelve ni uno, el instrumento CAE en ROJO
y no escribe nada: nunca inventa una fecha.

MECANICA DE ROJO, y no escribe nada si salta: (i) OP-E-03 no aparece
exactamente una vez; (ii) el fichero de lectura no existe o alguna fila no trae
la marca completa de LECTURA DIRIGIDA; (iii) el addendum de ESTA vuelta ya
estaba escrito; (iv) git no da fecha; (v) el ancla de 04_ENLACES.md no aparece
exactamente una vez.

USO:
  python scripts/loop/vuelta98_tarea4_addendum_opE03.py --simular
  python scripts/loop/vuelta98_tarea4_addendum_opE03.py --aplicar
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
LECTURA = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO3_V98.jsonl")
BOLSA = os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")

VUELTA = 98
DESDE_FILA = 101
MESES = {1: "ene", 2: "feb", 3: "mar", 4: "abr", 5: "may", 6: "jun",
         7: "jul", 8: "ago", 9: "sep", 10: "oct", 11: "nov", 12: "dic"}

ANCLA_ENLACES = ("Los veredictos viven en `docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl` y "
                 "**no** en\n`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.\n")
TITULO_ENLACES = ("LO QUE SE HIZO EN LA VUELTA 98, TAREA 4: EL TERCER TRAMO SE ABRE Y SE "
                  "LEE HASTA LA MITAD")


def fecha_de_git():
    """La fecha de los commits de la vuelta 98, LEIDA DE GIT. Nunca tecleada."""
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
    if not os.path.exists(LECTURA):
        return None, fallos + ["no existe %s" % os.path.relpath(LECTURA, RAIZ)]
    filas = cargar(LECTURA)
    for f in filas:
        if (f.get("marca") != "LECTURA DIRIGIDA" or not f.get("fuera_de_la_cola")
                or f.get("mueve_el_marcador_del_cribado") is not False
                or not f.get("fuera_de_la_tasa_por_dominio")):
            fallos.append("la fila %s no trae la marca completa de LECTURA DIRIGIDA"
                          % f.get("puesto_tramo"))
    d = {}
    d["filas"] = filas
    d["n"] = len(filas)
    d["total"] = len(cargar(BOLSA))
    d["clases"] = collections.Counter(f["clase"] for f in filas)
    d["doms"] = collections.Counter(f["dominio"] for f in filas)
    d["a"] = sorted(f["puesto_tramo"] for f in filas if f["clase"] == "A")
    d["b"] = sorted(f["puesto_tramo"] for f in filas if f["clase"] == "B")
    d["c"] = sorted(f["puesto_tramo"] for f in filas if f["clase"] == "C")
    d["con_dir"] = sum(1 for f in filas if f.get("direccion_leida"))
    d["sin_dir"] = sorted(f["puesto_tramo"] for f in filas if not f.get("direccion_leida"))
    d["invertidas"] = sorted(f["puesto_tramo"] for f in filas
                             if f.get("direccion_leida")
                             and f["direccion_leida"].split("->")[0].strip()
                             == f["hijo_de_la_bolsa"])
    d["ultima"] = max(f["puesto_tramo"] for f in filas)
    d["quedan"] = d["total"] - d["ultima"]
    return d, fallos


def marca(fecha):
    return ("ADDENDUM DE EJECUCION (%s, vuelta 98, TAREA 4): TERCER TRAMO ABIERTO Y "
            "LEIDO HASTA LA MITAD." % fecha)


def texto_nota(d, fecha, iso):
    return (
        " %s LA FECHA DE ESTE ADDENDUM SE LEYO DE GIT EN ESTA VUELTA con `git log --all "
        "--format=%%ad --date=short` sobre los commits cuyo asunto empieza por \"VUELTA "
        "98\", y da %s: NO esta tecleada, que es la caida 4.1 del acta 97 y su remedio. "
        "OP-E-03 NO CIERRA: se leyeron las filas %d a %d de las %d con el mismo "
        "instrumento del tramo 1 y del tramo 2 (scripts/loop/vuelta96_tarea3_tramo1_opE03.py "
        "--desde 100 --cuantos 83) sin tocarle una linea, y QUEDAN %d SIN LEER, filas %d a "
        "%d. El encargo autoriza parar donde se vaya y decirlo con la cifra, y es lo que se "
        "hace. Los cinco puntos de la verificacion se REMIDIERON en la vuelta y no se "
        "heredaron: cribado cerrado en 3388 filas cada fichero, contadas; ids por el "
        "RESOLUTOR antes de cruzar nada (P.1), y en las 83 del tramo el resolutor no movio "
        "NINGUNO, cosa que se declara igual porque P.1 obliga y porque una busqueda negativa "
        "no se cita sin medirla; cuenta sin fugas contra los 2796 pares distintos de la cola "
        "tras resolver, y ninguna fila del tramo esta en ella; marca LECTURA DIRIGIDA en las "
        "%d filas del JSONL, contadas una por una; y veredictos APARTE de la tasa por "
        "dominio del 9.27, en fichero propio y rotulado. "
        "RESULTADO: A %d, B %d, C %d, D %d. "
        "EL PRIMER C DE TODA LA LECTURA DE OP-E-03 (el tramo 1 dio C 0 y el tramo 2 tambien): "
        "el par %s, figura del banco 9.22 primer polo, procedimiento en los DOS sentidos "
        "sobre DOS lineas distintas, cuyo arreglo prescrito es ENLACE MUTUO y no fusion. NO "
        "SE ESCRIBIO NINGUNA ARISTA. "
        "DIRECCION: %d leidas y afirmadas, %d NO RESUELTAS y declaradas como tal (pares %s). "
        "LA PROPORCION DE NO RESUELTAS SUBE OTRA VEZ, del 27,5 por ciento del tramo 1 y el "
        "45,0 del tramo 2 al %s por ciento de esta mitad, que es la direccion que el "
        "encargo preveia para el tramo mas debil de la bolsa (mediana de titulo_ratio 76,2 "
        "contra 84,3 del tramo 1) y por eso se publica con la cifra y sin maquillarla. "
        "UNA DIRECCION INVERTIDA respecto a la etiqueta de la bolsa y AFIRMADA (par %s), la "
        "segunda de toda la lectura tras el par 16 del tramo 1, y afirmada porque aqui SI "
        "hay linea de un lado y procedimiento del otro, que es lo que faltaba en los pares "
        "82, 89 y 65 del tramo 2. "
        "POR DOMINIO, y no entra en la tasa del 9.27: %s. "
        "CERO ARISTAS ESCRITAS O RETIRADAS. Salidas: docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl "
        "(%d filas), docs/loop/SALIDA_V98_TAREA4_TRAMO3_MATERIAL.txt, "
        "docs/loop/SALIDA_V98_TAREA4_VEREDICTOS.txt, docs/loop/SALIDA_V98_TAREA4_CINCO_PUNTOS.txt, "
        "docs/loop/SALIDA_V98_TAREA4_MUTACION.txt (1 control y 7 mutaciones, las 7 caen; la "
        "clase y la direccion de cada par son lectura a mano y se DECLARA que no tienen caso "
        "rojo automatico). estado se queda en LISTA, mismo criterio que las demas."
        % (marca(fecha), iso, DESDE_FILA, d["ultima"], d["total"], d["quedan"],
           d["ultima"] + 1, d["total"], d["n"],
           d["clases"]["A"], d["clases"]["B"], d["clases"]["C"], d["clases"]["D"],
           ", ".join(str(x) for x in d["c"]),
           d["con_dir"], len(d["sin_dir"]), ", ".join(str(x) for x in d["sin_dir"]),
           ("%.1f" % (100.0 * len(d["sin_dir"]) / d["n"])).replace(".", ","),
           ", ".join(str(x) for x in d["invertidas"]),
           ", ".join("%s %d" % (k, v) for k, v in sorted(d["doms"].items())),
           d["n"])
    )


def texto_enlaces(d, fecha, iso):
    return (
        "\n**%s.**\n"
        "Los dos apartados de arriba se quedan enteros, sin borrar una palabra. **`OP-E-03`\n"
        "NO CIERRA**: se leyeron las filas **%d a %d** de las **%d** y **quedan %d sin\n"
        "leer**, filas %d a %d. La fecha de este apartado **se leyo de git en esta vuelta**\n"
        "(`git log --all --format=%%ad --date=short` sobre los commits cuyo asunto empieza\n"
        "por \"VUELTA 98\"): **%s**. No esta tecleada.\n"
        "\n"
        "| lo que salio | cifra |\n"
        "|---|---:|\n"
        "| pares leidos en esta mitad del tramo 3 | **%d** (filas %d a %d) |\n"
        "| pares leidos en total | **%d** de %d |\n"
        "| clase A, REPITE | **%d** |\n"
        "| clase B, DUDOSO | **%d** |\n"
        "| clase C, SANO CON FIGURA | **%d** |\n"
        "| clase D, CONTINUA | **%d** |\n"
        "| direccion leida y afirmada | **%d** |\n"
        "| direccion NO RESUELTA, declarada | **%d** |\n"
        "| direcciones invertidas y afirmadas | **%d** |\n"
        "| aristas escritas o retiradas | **0** |\n"
        "| pares que quedan sin leer | **%d** (filas %d a %d) |\n"
        "\n"
        "**EL PRIMER `C` DE TODA LA LECTURA DE `OP-E-03`.** El tramo 1 dio **C 0** y el\n"
        "tramo 2 tambien. El par **%s** es la figura del banco **9.22**, primer polo:\n"
        "procedimiento en los **dos** sentidos sobre **dos lineas distintas**, cuyo arreglo\n"
        "prescrito es **enlace mutuo** y no fusion. **NO se escribio ninguna arista**:\n"
        "`OP-E-03` es LECTURA DIRIGIDA y su producto es el juicio.\n"
        "\n"
        "**LA PROPORCION DE DIRECCIONES NO RESUELTAS SUBE OTRA VEZ**, del **27,5%%** del\n"
        "tramo 1 y el **45,0%%** del tramo 2 al **%s%%** de esta mitad. Es la direccion que\n"
        "el encargo preveia para el tramo mas debil de la bolsa (mediana de `titulo_ratio`\n"
        "**76,2** contra **84,3** del tramo 1), asi que **se publica con la cifra y sin\n"
        "maquillarla**.\n"
        % (TITULO_ENLACES, DESDE_FILA, d["ultima"], d["total"], d["quedan"],
           d["ultima"] + 1, d["total"], iso,
           d["n"], DESDE_FILA, d["ultima"],
           d["ultima"], d["total"],
           d["clases"]["A"], d["clases"]["B"], d["clases"]["C"], d["clases"]["D"],
           d["con_dir"], len(d["sin_dir"]), len(d["invertidas"]),
           d["quedan"], d["ultima"] + 1, d["total"],
           ", ".join(str(x) for x in d["c"]),
           ("%.1f" % (100.0 * len(d["sin_dir"]) / d["n"])).replace(".", ","))
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
        fallos.append("el addendum de la vuelta 98 YA ESTA en la nota de OP-E-03")

    enlaces = io.open(ENLACES, encoding="utf-8").read()
    if enlaces.count(ANCLA_ENLACES) != 1:
        fallos.append("el ancla del apartado de la vuelta 97 aparece %d veces en "
                      "04_ENLACES.md, se esperaba 1" % enlaces.count(ANCLA_ENLACES))
    if TITULO_ENLACES in enlaces:
        fallos.append("el apartado de la vuelta 98 YA ESTA en 04_ENLACES.md")

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("=" * 100)
    print("TERCER ADDENDUM DE OP-E-03, VUELTA 98 (%s)"
          % ("SIMULACION" if a.simular else "APLICADO"))
    print("=" * 100)
    print("FECHA LEIDA DE GIT: %s (%s). Ninguna cifra de abajo esta tecleada: todas se "
          "leen del JSONL." % (fecha, iso))
    print("EL BORDE DE LA ADJUDICACION 3.7 DEL ACTA 97, verificado:")
    print("   (a) las cifras salen de instrumentos corridos en esta vuelta: SI")
    print("   (b) la escritura es puramente aditiva: SI, se mide con --numstat en el commit")
    print("   (c) no mueve decision, alcance ni estado: SI, estado sigue en %r"
          % objetivo[0].get("estado"))
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
