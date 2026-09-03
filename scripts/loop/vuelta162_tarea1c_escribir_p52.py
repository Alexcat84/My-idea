# -*- coding: utf-8 -*-
r"""vuelta162_tarea1c_escribir_p52.py . TAREA 1.c de la vuelta 162.

ANADE A `P.5.2` DEL BANCO DEL PLAN LA CIFRA RECOMPUTADA TRAS ESCRIBIR LAS 16
MARCAS DE LA CIEGA DEL AUDITOR, **SIN BORRAR NI LA DE APERTURA NI LA DE CIERRE
DE LA VUELTA 161**, que es lo que el encargo pide con esas palabras.

NINGUNA CELDA SE TECLEA: todas se extraen de
`docs/loop/SALIDA_V162_T1C_SEGUNDA_LECTURA.txt`, y las de la vuelta 161 se leen
de la tabla que ya vive en el banco, no se recuerdan.

ES IDEMPOTENTE por marca literal.

USO:  python scripts/loop/vuelta162_tarea1c_escribir_p52.py
"""
import io
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BANCO = os.path.join(RAIZ, "docs", "plan", "BANCO_DEL_PLAN.md")
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V162_T1C_SEGUNDA_LECTURA.txt")
MARCA = "### LA MISMA CIFRA, RECOMPUTADA EN LA VUELTA 162"
ANCLA = """**Y LA FORMA NUEVA SE DECLARA:** la marca que la TAREA 2 escribe,
`RELECTURA DEL TRAMO DE LAS CATORCE EN C, VUELTA 161`, cumple las dos condiciones
de esta regla (dice que es una relectura y dice en que vuelta) y se anadio a
`FORMAS_QUE_CUENTAN` del contador **en la misma vuelta que la escribio**. Una
definicion que no contara la lectura del dia en que nace naceria desfasada.
"""


def cifra(texto, etiqueta):
    m = re.search(r"CIFRA %s: (\d+)" % re.escape(etiqueta), texto)
    if not m:
        raise SystemExit("ROJO: no se halla la cifra %r en la salida." % etiqueta)
    return int(m.group(1))


def bloque_de_actos(texto):
    dentro, filas = False, []
    for linea in texto.split("\n"):
        if linea.startswith("C) LOS ACTOS DE RELECTURA"):
            dentro = True
            continue
        if dentro:
            if linea.strip().startswith("CIFRA "):
                break
            m = re.match(r"^   ([A-Z_]+)\s+vuelta (\d+)\s+(\d+) fila\(s\)$", linea)
            if m:
                filas.append(linea.strip())
    return filas


def celda_del_banco(texto, etiqueta):
    """La celda de CIERRE de la vuelta 161 que ya vive en el banco, leida del
    fichero y no recordada."""
    m = re.search(r"^\| %s \| (\d+) \| \*\*(\d+)\*\* \|$" % re.escape(etiqueta),
                  texto, re.M)
    if not m:
        raise SystemExit("ROJO: no se halla la fila %r en la tabla del banco." % etiqueta)
    return int(m.group(1)), int(m.group(2))


def main():
    print("=" * 78)
    print("VUELTA 162, TAREA 1.c: LA CIFRA DE P.5.2, RECOMPUTADA TRAS LAS 16 MARCAS")
    print("=" * 78)
    print("")

    banco = io.open(BANCO, encoding="utf-8").read()
    if MARCA in banco:
        print("YA ESTABA: la seccion de la vuelta 162 vive en P.5.2. No se toca.")
        print("CIFRA secciones escritas: 0")
        return 0

    salida = io.open(SALIDA, encoding="utf-8").read()
    print("A) LAS CIFRAS DE HOY, EXTRAIDAS DE %s" % os.path.basename(SALIDA))
    ld = cifra(salida, "pares de LECTURA_DIRIGIDA")
    una = cifra(salida, "con AL MENOS UNA segunda lectura independiente")
    dos = cifra(salida, "con DOS O MAS")
    cero = cifra(salida, "con NINGUNA")
    distintos = cifra(salida, "actos distintos (tipo, vuelta)")
    total = cifra(salida, "total de actos sobre filas")
    print("   pares de LECTURA_DIRIGIDA: %d" % ld)
    print("   con al menos una: %d | con dos o mas: %d | con ninguna: %d" % (una, dos, cero))
    print("   actos sobre filas: %d | actos distintos: %d" % (total, distintos))
    actos = bloque_de_actos(salida)
    print("   CIFRA lineas de actos leidas: %d" % len(actos))
    if len(actos) != distintos:
        print("   PARADA: las lineas de actos no cuadran con la cifra de actos distintos.")
        return 1
    print("")

    print("B) LAS CIFRAS DE LA VUELTA 161, LEIDAS DE LA TABLA QUE YA VIVE EN EL BANCO")
    filas = [
        ("con AL MENOS UNA segunda lectura independiente", una),
        ("con DOS O MAS", dos),
        ("con NINGUNA", cero),
        ("actos de relectura contados sobre filas", total),
        ("actos distintos `(tipo, vuelta)`", distintos),
    ]
    tabla = []
    for etiqueta, hoy in filas:
        ap, ci = celda_del_banco(banco, etiqueta)
        print("   %-52s apertura 161 %-4d cierre 161 %-4d hoy %d" % (etiqueta, ap, ci, hoy))
        tabla.append("| %s | %d | %d | **%d** |" % (etiqueta, ap, ci, hoy))
    print("")

    texto = (
        ANCLA
        + "\n"
        + MARCA + ", TRAS ESCRIBIR LAS 16 MARCAS DE LA CIEGA\n"
        "\n"
        "**`EJECUTOR.md` 1: el estado al cierre se mide al cierre, y esta vuelta lo\n"
        "movio otra vez.** La TAREA 1.c de la vuelta 162 escribio, por la **adjudicacion\n"
        "6.7 del acta 161**, las **16 marcas** de la relectura CIEGA DEL AUDITOR de la\n"
        "vuelta 161 (las catorce en `C` mas los ejemplares `100` y `122`), por adicion y\n"
        "**sin mover una sola clase**. **NI LA CIFRA DE APERTURA NI LA DE CIERRE DE LA\n"
        "VUELTA 161 SE BORRAN NI SE SUSTITUYEN**: se quedan enteras, cada una con su\n"
        "corte, y esta se anade a su derecha con el suyo.\n"
        "\n"
        "**Corte: 3 sep 2026, vuelta 162. Autor: ejecutor de la vuelta 162. Instrumento:\n"
        "`scripts/loop/vuelta161_tarea1c_segunda_lectura.py` (el mismo, con la forma nueva\n"
        "declarada). Fichero de salida: `docs/loop/SALIDA_V162_T1C_SEGUNDA_LECTURA.txt`.**\n"
        "Ninguna celda esta tecleada: todas se extraen de ese fichero, y las dos columnas\n"
        "de la vuelta 161 se leen de la tabla de arriba, no se recuerdan.\n"
        "\n"
        "| | apertura de la 161 | cierre de la 161 | **vuelta 162** |\n"
        "|---|---:|---:|---:|\n"
        "%s\n"
        "\n"
        "**Los actos en la vuelta 162, pegados enteros de su fichero:**\n"
        "\n"
        "```\n"
        "%s\n"
        "```\n"
        "\n"
        "**Y LA FORMA NUEVA SE DECLARA, IGUAL QUE SE DECLARO LA DE LA VUELTA 161:** la\n"
        "marca `RELECTURA CIEGA DEL AUDITOR, VUELTA 161` cumple las dos condiciones de\n"
        "esta regla y se anadio a `FORMAS_QUE_CUENTAN` **en la misma vuelta que la\n"
        "escribio**. Sin esa linea, la definicion no contaria justo la lectura que la\n"
        "adjudicacion 6.7 vino a hacer contable.\n"
        "\n"
        "**LO QUE ESTA CIFRA SI MUEVE, Y LO QUE NO.** El **con al menos una** no se mueve\n"
        "(%d y %d): las dieciseis ya tenian una marca de otra pluma. Lo que se mueve es el\n"
        "**con dos o mas**, de %d a %d, que es exactamente lo que `P.5.2` persigue: **una\n"
        "segunda lectura independiente que antes no era contable porque vivia solo en el\n"
        "acta del auditor.**\n"
        % ("\n".join(tabla), "\n".join(actos),
           celda_del_banco(banco, "con AL MENOS UNA segunda lectura independiente")[1],
           una, celda_del_banco(banco, "con DOS O MAS")[1], dos)
    )

    if banco.count(ANCLA) != 1:
        print("ROJO: el ancla aparece %d veces." % banco.count(ANCLA))
        return 1
    banco = banco.replace(ANCLA, texto, 1)
    io.open(BANCO, "w", encoding="utf-8", newline="\n").write(banco)

    print("C) LA ESCRITURA")
    r = subprocess.run(["git", "diff", "--numstat", "--", "docs/plan/BANCO_DEL_PLAN.md"],
                       cwd=RAIZ, capture_output=True, text=True)
    print("   git diff --numstat: %s" % r.stdout.strip())
    partes = r.stdout.strip().split("\t")
    if int(partes[1]) != 0:
        print("   ROJO: tenia que ser adicion pura y borro %s linea(s)." % partes[1])
        return 1
    print("   VERDE: adicion pura, cero borrados. Las dos cifras de la 161 siguen enteras.")
    print("CIFRA secciones escritas: 1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
