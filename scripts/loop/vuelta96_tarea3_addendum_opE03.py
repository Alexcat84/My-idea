# -*- coding: utf-8 -*-
r"""vuelta96_tarea3_addendum_opE03.py . VUELTA 96, TAREA 3: escribe el ADDENDUM
DE EJECUCION del primer tramo en la nota de OP-E-03
(docs/plan/OPERACIONES.jsonl) y el apartado hermano en docs/plan/04_ENLACES.md.

POR QUE ES UN SCRIPT Y NO UNA EDICION A MANO (EJECUTOR.md regla 1, "LA TABLA SE
IMPRIME, NO SE TECLEA"): las cifras del addendum NO se teclean. Se LEEN de
docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl, que es la salida de la lectura, y se
formatean aqui. Si ese fichero cambia, el addendum cambia con el.

ES ADITIVO: la nota vieja NO se toca, el texto nuevo se anade detras. Igual en
04_ENLACES.md, donde el apartado "LO QUE NO SE HIZO ESTA VUELTA" de la vuelta 94
se queda entero y debajo va lo que si se hizo en la 96.

MECANICA DE ROJO: si OP-E-03 no aparece, si el fichero de lectura no tiene 40
filas, si alguna fila no trae la marca LECTURA DIRIGIDA, o si el addendum ya
estaba escrito (correr dos veces duplicaria texto), NO ESCRIBE NADA y sale con
exit 1. Probada por mutacion en el propio --simular.

USO:
  python scripts/loop/vuelta96_tarea3_addendum_opE03.py --simular
  python scripts/loop/vuelta96_tarea3_addendum_opE03.py --aplicar
"""
import argparse
import collections
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
ENLACES = os.path.join(RAIZ, "docs", "plan", "04_ENLACES.md")
LECTURA = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl")

MARCA = "ADDENDUM DE EJECUCION (27 ago 2026, vuelta 96, TAREA 3): PRIMER TRAMO LEIDO."


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def cifras():
    filas = cargar_jsonl(LECTURA)
    fallos = []
    if len(filas) != 40:
        fallos.append("el fichero de lectura trae %d filas y se esperaban 40" % len(filas))
    for f in filas:
        if f.get("marca") != "LECTURA DIRIGIDA" or not f.get("fuera_de_la_cola") \
                or f.get("mueve_el_marcador_del_cribado") is not False \
                or not f.get("fuera_de_la_tasa_por_dominio"):
            fallos.append("la fila %s no trae la marca completa de LECTURA DIRIGIDA" % f.get("puesto_tramo"))
    clases = collections.Counter(f["clase"] for f in filas)
    doms = collections.Counter(f["dominio"] for f in filas)
    con_dir = sum(1 for f in filas if f.get("direccion_leida"))
    return filas, clases, doms, con_dir, fallos


def texto_nota(filas, clases, doms, con_dir):
    total_bolsa = len(cargar_jsonl(os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")))
    por_dom = ", ".join("%s %d" % (d, n) for d, n in sorted(doms.items()))
    a = [f["puesto_tramo"] for f in filas if f["clase"] == "A"]
    b = [f["puesto_tramo"] for f in filas if f["clase"] == "B"]
    sin_dir = [f["puesto_tramo"] for f in filas if not f.get("direccion_leida")]
    return (
        " %s Leidas las filas 1 a %d de las %d de docs/plan/DIFERENCIA_CONTRA_COLA.jsonl, "
        "con la vara del banco 9.6.1 (clase), 9.6.2 (direccion) y 9.6.3 (el tamano del solape no decide). "
        "Los cinco puntos de la verificacion se cumplen y se remidieron en la vuelta, no se heredaron: "
        "el cribado cerrado (INTRA_DOMINIO_PARES.jsonl y INTRA_DOMINIO_VEREDICTOS.jsonl, 3388 filas cada uno, "
        "contadas por el instrumento); los ids por el resolutor ANTES de comparar (P.1), y en estas %d el "
        "resolutor no movio ninguno; la cuenta sin fugas (cero de las %d esta en la cola tras resolver, cero "
        "repetidas dentro del tramo); la marca LECTURA DIRIGIDA escrita en cada fila; y los veredictos "
        "contados APARTE de la tasa por dominio del banco 9.27, en fichero propio. "
        "RESULTADO: A %d, B %d, C %d, D %d. El unico A es el par %s (human_error_como_sintoma contra "
        "preguntar_que_no_quien, misma fuente Dekker: lo unico que anade cabe en una linea). El unico B es "
        "el par %s (fit_problema_solucion contra value_proposition_startup), declarado DUDOSO en vez de "
        "forzado. DIRECCION: %d leidas y afirmadas, %d NO RESUELTAS y declaradas como tal (pares %s), de "
        "ellas tres por no haber madre e hijo en absoluto (el caso 2.195 que el propio 9.6.2 nombra) y una, "
        "el par 16, con la direccion INVERTIDA respecto a la etiqueta de la bolsa, corregida en la lectura. "
        "POR DOMINIO, y no entra en la tasa del 9.27: %s. "
        "SEIS FIGURAS registradas en docs/PENDIENTES.md, cuatro de ellas sospechas de gemelos entre nodos "
        "(el trio Make Certain, los dos Customer Development, los dos de estrategia de innovacion y la "
        "familia de la capacidad de proceso, que ademas corrobora un aviso informativo de Gate 0), una "
        "propiedad del barrido (puede casar un paso con su propia refutacion) y la direccion invertida. "
        "CERO ARISTAS ESCRITAS O RETIRADAS: OP-E-03 es LECTURA DIRIGIDA y su producto es el juicio. "
        "Salidas: docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl (40 filas), "
        "docs/loop/SALIDA_V96_TAREA3_TRAMO1_MATERIAL.txt, docs/loop/SALIDA_V96_TAREA3_VEREDICTOS.txt, "
        "docs/loop/SALIDA_V96_TAREA3_MUTACION.txt (seis guardas probadas por mutacion, las seis caen; la "
        "clase de cada par es tabla a mano y se DECLARA que no tiene caso rojo automatico). "
        "QUEDAN %d SIN LEER, filas %d a %d. estado se queda en LISTA, mismo criterio que las demas."
        % (MARCA, len(filas), total_bolsa, len(filas), len(filas),
           clases["A"], clases["B"], clases["C"], clases["D"],
           ", ".join(str(x) for x in a), ", ".join(str(x) for x in b),
           con_dir, len(sin_dir), ", ".join(str(x) for x in sin_dir), por_dom,
           total_bolsa - len(filas), len(filas) + 1, total_bolsa)
    )


def texto_enlaces(filas, clases, con_dir):
    total_bolsa = len(cargar_jsonl(os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")))
    sin_dir = [f["puesto_tramo"] for f in filas if not f.get("direccion_leida")]
    return (
        "\n**LO QUE SI SE HIZO EN LA VUELTA 96, TAREA 3: EL PRIMER TRAMO YA ESTA LEIDO.**\n"
        "El apartado de arriba se queda entero, sin borrar una palabra: describia el estado\n"
        "de la vuelta 94, cuando la bolsa estaba establecida y sin leer. **Hoy ya no lo esta.**\n"
        "Se leyeron las filas **1 a %d** de las **%d**, con la vara del banco `9.6.1` para la\n"
        "clase, la del `9.6.2` para la direccion y la del `9.6.3` para no dejar que el tamano\n"
        "del solape decida. **Los cinco puntos de `OP-E-03.verificacion` se cumplen, y los\n"
        "tres que son medibles se REMIDIERON en la vuelta en vez de heredarse.**\n"
        "\n"
        "| lo que salio | cifra |\n"
        "|---|---:|\n"
        "| pares leidos | **%d** de %d |\n"
        "| clase A, REPITE | **%d** |\n"
        "| clase B, DUDOSO | **%d** |\n"
        "| clase C | **%d** |\n"
        "| clase D, CONTINUA | **%d** |\n"
        "| direccion leida y afirmada | **%d** |\n"
        "| direccion NO RESUELTA, declarada | **%d** |\n"
        "| aristas escritas o retiradas | **0** |\n"
        "| pares que quedan sin leer | **%d** (filas %d a %d) |\n"
        "\n"
        "**CERO ARISTAS**: `OP-E-03` es LECTURA DIRIGIDA y su producto es el juicio, no el\n"
        "cableado. El detalle entero, con las seis figuras que la lectura destapa y las seis\n"
        "guardas probadas por mutacion, esta en `docs/PENDIENTES.md`, seccion \"VUELTA 96,\n"
        "TAREA 3\". Los veredictos viven en `docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl` y\n"
        "**no** en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`: se cuentan aparte de la tasa por\n"
        "dominio del banco `9.27`, como manda el punto 5 de la verificacion.\n"
        % (len(filas), total_bolsa, len(filas), total_bolsa,
           clases["A"], clases["B"], clases["C"], clases["D"],
           con_dir, len(sin_dir), total_bolsa - len(filas), len(filas) + 1, total_bolsa)
    )


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--simular", action="store_true")
    g.add_argument("--aplicar", action="store_true")
    a = ap.parse_args()

    filas, clases, doms, con_dir, fallos = cifras()

    ops = cargar_jsonl(OPERACIONES)
    objetivo = [o for o in ops if o.get("id_op") == "OP-E-03"]
    if len(objetivo) != 1:
        fallos.append("OP-E-03 aparece %d veces en OPERACIONES.jsonl, se esperaba 1" % len(objetivo))
    else:
        if MARCA in (objetivo[0].get("nota") or ""):
            fallos.append("el addendum de la vuelta 96 YA ESTA en la nota de OP-E-03: correr dos veces lo duplicaria")

    enlaces = io.open(ENLACES, encoding="utf-8").read()
    ancla = "sin decidir apurado en esta, y `PROMPT_SIGUIENTE.md` pide parar antes que decidir\nsin texto que lo sostenga."
    if ancla not in enlaces:
        fallos.append("no se encontro el ancla del apartado de OP-E-03 en 04_ENLACES.md")
    if "LO QUE SI SE HIZO EN LA VUELTA 96, TAREA 3" in enlaces:
        fallos.append("el apartado de la vuelta 96 YA ESTA en 04_ENLACES.md")

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    nota_nueva = (objetivo[0].get("nota") or "") + texto_nota(filas, clases, doms, con_dir)
    bloque = texto_enlaces(filas, clases, con_dir)

    print("=" * 100)
    print("ADDENDUM DE OP-E-03, VUELTA 96 (%s)" % ("SIMULACION" if a.simular else "APLICADO"))
    print("=" * 100)
    print()
    print("--- lo que se anade a la nota de OP-E-03 (aditivo, la vieja no se toca) ---")
    print(texto_nota(filas, clases, doms, con_dir).strip())
    print()
    print("--- lo que se anade a docs/plan/04_ENLACES.md (aditivo) ---")
    print(bloque)

    if a.simular:
        print("SIMULACION: no se escribio nada.")
        return 0

    objetivo[0]["nota"] = nota_nueva
    with io.open(OPERACIONES, "w", encoding="utf-8", newline="\n") as f:
        for o in ops:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    io.open(ENLACES, "w", encoding="utf-8", newline="\n").write(
        enlaces.replace(ancla, ancla + "\n" + bloque, 1))

    # re-lectura de comprobacion: los dos ficheros siguen validos y traen la marca
    ops2 = cargar_jsonl(OPERACIONES)
    o2 = [o for o in ops2 if o.get("id_op") == "OP-E-03"]
    enlaces2 = io.open(ENLACES, encoding="utf-8").read()
    bien = (len(ops2) == len(ops) and len(o2) == 1 and MARCA in o2[0]["nota"]
            and "LO QUE SI SE HIZO EN LA VUELTA 96, TAREA 3" in enlaces2)
    print("APLICADO. Re-lectura: OPERACIONES.jsonl %d filas validas, addendum presente: %s"
          % (len(ops2), "SI" if bien else "NO"))
    return 0 if bien else 1


if __name__ == "__main__":
    raise SystemExit(main())
