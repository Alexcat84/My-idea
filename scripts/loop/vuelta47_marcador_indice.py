"""Vuelta 47, TAREA 2: EL MARCADOR DEL 00_INDICE, IMPRESO Y NO TECLEADO.

El cuarto renglon de la regla 1 de docs/loop/EJECUTOR.md manda que toda tabla cuyo
contenido exista en un instrumento se GENERE desde el instrumento y se pegue entera,
con el comando citado al lado. El marcador del 00_INDICE es exactamente esa especie:
una tabla de prosa que ningun instrumento validaba, y cuatro de sus filas llevaban
meses rancias.

Este instrumento no opina: cuenta docs/plan/OPERACIONES.jsonl fase por fase y estado
por estado, y ESCUPE LA TABLA EN MARKDOWN, lista para pegar. De solo lectura.

Mide ademas las otras tres cifras que el marcador y su cierre publican y que tampoco
tenian instrumento: las reglas del banco del plan, las fronteras declaradas y las
entradas del inventario.

Uso: python scripts/loop/vuelta47_marcador_indice.py [--tabla]
     (--tabla imprime SOLO el markdown, sin las secciones de medicion)
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
BANCO = os.path.join(RAIZ, "docs", "plan", "BANCO_DEL_PLAN.md")
FRONT = os.path.join(RAIZ, "docs", "plan", "FRONTERAS_DECLARADAS.md")
INV = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
INDICE = os.path.join(RAIZ, "docs", "plan", "00_INDICE.md")

CORTE = "19 ago 2026"

# El nombre que el marcador del 00_INDICE le da a cada fase, junto al valor exacto
# del campo `fase` en OPERACIONES.jsonl. La pareja se declara aqui para que la fila
# de la tabla NO dependa de que los dos textos coincidan por casualidad.
FASES = [
    ("00_CODIGO", "0 CODIGO"),
    ("01_FUENTES", "01 FUENTES"),
    ("02_DESTEJIDOS", "02 DESTEJIDOS"),
    ("03_FUSIONES", "03 FUSIONES"),
    ("04_ENLACES", "04 ENLACES"),
    ("05_SANEO", "05 SANEO"),
    ("06_MESAS", "06 MESAS"),
    ("07_ADUANA", "07 ADUANA"),
    ("08_VERIFICACION", "08 VERIFICACION"),
    ("09_LECTURAS_DIRIGIDAS", "09 LECTURAS DIRIGIDAS"),
    ("10_INVENTARIO", "10 INVENTARIO"),
]


def sep(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def cargar():
    ops = []
    for l in io.open(OPS, encoding="utf-8"):
        l = l.strip()
        if l:
            ops.append(json.loads(l))
    return ops


def tabla(ops):
    """Devuelve el markdown del marcador, entero y listo para pegar."""
    total = len(ops)
    listas = sum(1 for o in ops if o["estado"] == "LISTA")
    pend = sum(1 for o in ops if o["estado"] == "DECISION PENDIENTE")
    otros = total - listas - pend

    out = []
    out.append("| | |")
    out.append("|---|---:|")
    out.append("| operaciones | **%d** |" % total)
    out.append("| **LISTAS** | **%d** |" % listas)
    out.append("| **DECISION PENDIENTE** | **%d** |" % pend)
    if otros:
        out.append("| **otro estado** | **%d** |" % otros)
    out.append("")
    out.append("| fase | operaciones | LISTAS | pendientes |")
    out.append("|---|---:|---:|---:|")
    vistas = set()
    for clave, nombre in FASES:
        dela = [o for o in ops if o["fase"] == clave]
        vistas.update(o["id_op"] for o in dela)
        out.append("| **%s** | %d | **%d** | %d |"
                   % (nombre,
                      len(dela),
                      sum(1 for o in dela if o["estado"] == "LISTA"),
                      sum(1 for o in dela if o["estado"] == "DECISION PENDIENTE")))
    huerfanas = [o for o in ops if o["id_op"] not in vistas]
    for o in huerfanas:
        out.append("| **%s** (fase no prevista en el marcador) | 1 | %d | %d |"
                   % (o["fase"],
                      1 if o["estado"] == "LISTA" else 0,
                      1 if o["estado"] == "DECISION PENDIENTE" else 0))
    return "\n".join(out), huerfanas


def main():
    ops = cargar()
    md, huerfanas = tabla(ops)

    if "--tabla" in sys.argv:
        print(md)
        return 0

    sep("1. LO QUE SE CUENTA, Y DE DONDE SALE")
    print("  fuente unica: %s" % os.path.relpath(OPS, RAIZ).replace("\\", "/"))
    print("  lineas leidas   : %d" % len(ops))
    print("  ids unicos      : %d" % len(set(o["id_op"] for o in ops)))
    estados = {}
    for o in ops:
        estados[o["estado"]] = estados.get(o["estado"], 0) + 1
    print("  estados         : %s" % estados)
    print("  corte declarado : %s" % CORTE)
    if huerfanas:
        print("  AVISO: %d operacion(es) con una fase que el marcador no preveia: %s"
              % (len(huerfanas), [o["id_op"] for o in huerfanas]))
    else:
        print("  fases cubiertas : las 11 del marcador, sin huerfanas")

    sep("2. LA TABLA, IMPRESA PARA PEGAR ENTERA")
    print(md)

    sep("3. EL CONTRASTE CONTRA LO QUE EL 00_INDICE PUBLICA HOY")
    print("  el instrumento NO reescribe: imprime, y aqui dice cuales filas no calzan")
    texto = io.open(INDICE, encoding="utf-8").read()
    # LIMITE DECLARADO DEL LECTOR (visto en la vuelta 47 ANTES de publicar nada, y
    # corregido): leer TODO lo que sigue a "## EL MARCADOR" tragaba tambien la tabla
    # del marcador VIEJO y la tabla de correcciones que la acompana, y esas dos traen
    # a proposito las cifras rancias en su primera columna. El lector se acota al
    # bloque del marcador VIGENTE, que es el unico que publica cifras de hoy.
    ini = texto.find("### EL MARCADOR VIGENTE")
    if ini < 0:
        ini = texto.find("## EL MARCADOR")
    fin = texto.find("**LAS CUATRO FILAS QUE NO CALZABAN", ini + 1)
    if fin < 0:
        fin = texto.find("\n## ", ini + 1)
    bloque = texto[ini:fin if fin > 0 else len(texto)]
    publicado = {}
    for linea in bloque.split("\n"):
        m = re.match(r"^\|\s*\**([^|*~]+?)\**\s*\|\s*\**(\d+)\**\s*\|", linea)
        if m:
            publicado[m.group(1).strip()] = int(m.group(2))
    print("  bloque leido: %d lineas por count(NL), que calza con wc -l, y %d por len(split(NL)), acotado al marcador VIGENTE"
          % (bloque.count("\n"), len(bloque.split("\n"))))
    medido = {"operaciones": len(ops)}
    for clave, nombre in FASES:
        medido[nombre] = sum(1 for o in ops if o["fase"] == clave)
    print()
    print("  %-24s %10s %10s  %s" % ("fila", "publicado", "medido", "calza"))
    fallan = 0
    for nombre in ["operaciones"] + [n for _, n in FASES]:
        pub = publicado.get(nombre)
        med = medido[nombre]
        if pub is None:
            print("  %-24s %10s %10d  %s" % (nombre, "(sin leer)", med, "?"))
            continue
        ok = pub == med
        if not ok:
            fallan += 1
        print("  %-24s %10d %10d  %s" % (nombre, pub, med, "SI" if ok else "NO"))
    print()
    print("  FILAS QUE NO CALZAN: %d" % fallan)

    sep("4. LAS OTRAS TRES CIFRAS QUE EL INDICE PUBLICA Y NO TENIAN INSTRUMENTO")
    banco = io.open(BANCO, encoding="utf-8").read()
    reglas = sorted(set(re.findall(r"^## (P\.\d+)", banco, re.M)),
                    key=lambda s: int(s.split(".")[1]))
    print("  reglas del banco del plan : %d   %s" % (len(reglas), " ".join(reglas)))
    fro = io.open(FRONT, encoding="utf-8").read()
    titulos = re.findall(r"^### \d+\. (.+)$", fro, re.M)
    print("  fronteras declaradas      : %d" % len(titulos))
    for t in titulos:
        print("      %s" % t.strip())
    n = 0
    for l in io.open(INV, encoding="utf-8"):
        if l.strip():
            n += 1
    print("  entradas del inventario   : %d" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
