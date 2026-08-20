# -*- coding: utf-8 -*-
"""Vuelta 48, TAREA 1.1: LA CITA DE LINEA DE `OP-D-07`, CORREGIDA Y RE-MEDIDA
DESPUES DE LA ULTIMA EDICION DEL FICHERO.

LA CAIDA QUE CORRIGE (contada como caida de cifra publicada en el acta de la
vuelta 47, seccion 3): la fila de `OP-D-07` en la tabla de registros de
docs/plan/02_DESTEJIDOS.md cita "linea 4578"; el encabezado del sello vive hoy
en otra linea, porque el MISMO commit que escribio el sello (62c10658) inserto
lineas ENCIMA de el despues de haberse medido la cita.

EL MOTIVO, MEDIDO Y NO COPIADO: `git show 62c10658 -- docs/plan/02_DESTEJIDOS.md`
trae tres hunks; el primero (@@ -4476,14 +4476,23 @@) suma 9 lineas y el segundo
(@@ -4517,8 +4526,12 @@) suma 4, las dos por encima del sello, que el tercero
anade al final del fichero. 9 mas 4 son las 13 lineas del desplazamiento.

EL ORDEN DE ESTE INSTRUMENTO ES LA REGLA MISMA: primero escribe la correccion
con un HUECO en vez de la cifra, y SOLO DESPUES mide la linea sobre el fichero
ya editado y rellena el hueco. Rellenar el hueco no cambia el numero de lineas,
asi que la medicion sigue siendo valida cuando se publica. Medir antes de
escribir es exactamente la caida que esto corrige.

De propina RE-MIDE LAS NUEVE FILAS de la tabla y compara cada cita con la
medicion de hoy (EJECUTOR.md regla 1: la tabla se imprime, no se teclea).

Uso: python scripts/loop/vuelta48_registros_lineas.py [--escribir]
"""
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAG = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")

HUECO = "@@LINEA_MEDIDA_DESPUES@@"

VIEJO = (
    "**CORREGIDO el 19 ago 2026 (vuelta 47), remedido con el mismo instrumento: "
    "SI**, con el encabezado de la forma anterior, linea **4578**:"
)
NUEVO = (
    "**CORREGIDO el 19 ago 2026 (vuelta 47), remedido con el mismo instrumento: "
    "SI**, con el encabezado de la forma anterior, "
    "~~linea **4578**~~ **CORRECCION DECLARADA el 19 ago 2026 (vuelta 48): "
    "linea " + HUECO + "**, re-medida con "
    "`scripts/loop/vuelta48_registros_lineas.py` DESPUES de la ultima edicion del "
    "fichero. **Motivo:** el commit `62c10658` que escribio el sello inserto ademas "
    "**13 lineas por encima de el** (9 en el hunk de la 4476 y 4 en el de la 4517, "
    "medidos con `git show`), y la cita se tomo antes de esa insercion:"
)

PATRON_CERRADA = re.compile(r"^#+\s+.*OP-D-\d\d.*\s(CERRADA|SELLADA)", re.I)
OPS = ["OP-D-0%d" % i for i in range(1, 10)]
LARGO = "\u2014"
MEDIO = "\u2013"


def sep(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def leer():
    return io.open(PAG, encoding="utf-8", newline="").read()


def escribir(txt):
    with io.open(PAG, "w", encoding="utf-8", newline="") as fh:
        fh.write(txt)


def medir(txt):
    """La linea del ULTIMO encabezado de nivel 2 que nombra cada operacion.
    Mismo criterio que scripts/loop/vuelta46_cierre_fase02.py."""
    lineas = txt.split("\n")
    out = {}
    for oid in OPS:
        cab = [i + 1 for i, l in enumerate(lineas)
               if l.startswith("## ") and oid in l]
        out[oid] = cab[-1] if cab else None
    return out, lineas


def citas(lineas):
    """Lo que la TABLA DE REGISTROS dice hoy, fila por fila, leido del fichero."""
    out = {}
    for i, l in enumerate(lineas):
        if not l.startswith("| `OP-D-0"):
            continue
        m = re.match(r"\| `(OP-D-\d\d)` \|", l)
        if not m:
            continue
        # la ULTIMA cita de linea viva de la celda (las tachadas van entre ~~)
        vivas = re.findall(r"(?<!~)linea \*\*(\d+)\*\*", l)
        out[m.group(1)] = (i + 1, [int(x) for x in vivas])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    txt0 = leer()
    n0 = txt0.count("\n")
    m0, _ = medir(txt0)

    sep("1. ANTES DE TOCAR NADA")
    print("  fichero  : docs/plan/02_DESTEJIDOS.md")
    print("  lineas   : %d" % n0)
    print("  encabezado de OP-D-07 medido AHORA: linea %s" % m0["OP-D-07"])
    print("  la celda cita             : 4578")
    print("  desfase                   : %s" % (m0["OP-D-07"] - 4578))

    if VIEJO not in txt0:
        if HUECO in txt0 or "vuelta 48)" in txt0:
            print()
            print("  YA APLICADA. Nada que escribir.")
            return 0
        print()
        print("  PARADA: no encuentro el texto ancla de la celda. No adivino.")
        return 2

    if not args.escribir:
        sep("2. SIMULACION (sin --escribir no toco el fichero)")
        print("  se sustituiria 1 ocurrencia del ancla")
        print("  lineas antes y despues: %d y %d (la celda es una sola linea)" % (n0, n0))
        return 0

    # --- PASO A: escribir la correccion CON EL HUECO ---
    sep("2. PASO A: la correccion escrita, con HUECO en vez de cifra")
    txt1 = txt0.replace(VIEJO, NUEVO, 1)
    escribir(txt1)
    n1 = txt1.count("\n")
    print("  ancla sustituida: 1 ocurrencia")
    print("  lineas antes %d, despues %d (delta %d)" % (n0, n1, n1 - n0))
    print("  hueco presente: %s" % (HUECO in txt1))

    # --- PASO B: medir SOBRE EL FICHERO YA EDITADO ---
    sep("3. PASO B: la linea, medida SOBRE EL FICHERO YA EDITADO")
    txt1 = leer()
    m1, _ = medir(txt1)
    ln = m1["OP-D-07"]
    print("  encabezado de OP-D-07: linea %s" % ln)
    print("  (esta es la cifra que se publica; no la de antes de editar)")

    # --- PASO C: rellenar el hueco (no mueve lineas) ---
    sep("4. PASO C: el hueco relleno (no cambia el numero de lineas)")
    txt2 = txt1.replace(HUECO, "**%d**" % ln, 1)
    escribir(txt2)
    n2 = txt2.count("\n")
    print("  lineas: %d (igual que tras el paso A: %s)" % (n2, n2 == n1))

    # --- PASO D: re-medir TODO y comparar con lo que la tabla dice ---
    sep("5. LAS NUEVE FILAS, RE-MEDIDAS CONTRA LO QUE LA TABLA CITA")
    txt3 = leer()
    m3, lineas3 = medir(txt3)
    c3 = citas(lineas3)
    print("  %-10s %-12s %-14s %s" % ("op", "medido hoy", "cita viva", "calza"))
    malas = []
    for oid in OPS:
        med = m3[oid]
        fila, viv = c3.get(oid, (None, []))
        ok = viv and viv[-1] == med
        if not ok:
            malas.append(oid)
        print("  %-10s %-12s %-14s %s"
              % (oid, med, viv[-1] if viv else "(sin cita)", "SI" if ok else "NO"))
    print()
    print("  FILAS QUE CALZAN: %d de %d" % (len(OPS) - len(malas), len(OPS)))
    print("  FILAS QUE NO CALZAN: %s" % (", ".join(malas) if malas else "ninguna"))

    sep("6. GUARDAS")
    print("  el texto viejo sigue dentro del nuevo (tachado): %s"
          % ("linea **4578**" in txt3))
    print("  hueco resuelto (no queda ninguno)             : %s" % (HUECO not in txt3))
    print("  guiones largos en el fichero                  : %d" % txt3.count(LARGO))
    print("  guiones medios en el fichero                  : %d" % txt3.count(MEDIO))
    print("  lineas finales                                : %d" % txt3.count("\n"))
    return 0 if not malas else 3


if __name__ == "__main__":
    sys.exit(main())
