# -*- coding: utf-8 -*-
"""vuelta60_correccion_fecha.py . APLICA LA CORRECCION DECLARADA DE LA FECHA
SOBRE LA NOTA DE RATIFICACION DE docs/plan/03_FUSIONES.md.

POR QUE EXISTE Y POR QUE ES UN INSTRUMENTO Y NO UN TECLEO: la caida de reporte
de la vuelta anterior fue LA FECHA. El reporte, la nota de ratificacion y el
campo fecha del plan sellado dijeron un dia y los commits de aquella vuelta son
del dia anterior, medido por git. Corregir esa fecha TECLEANDO otra fecha seria
repetir la especie de la caida un renglon mas abajo: la fecha buena tiene que
salir de una MEDICION. Este instrumento la mide con git y escribe la linea; no
la escribe nadie a mano.

QUE MIDE, y de donde:
  * la fecha de cada commit del rango de la vuelta corregida, por
    `git log --date=format:%Y-%m-%d`, que es la vara que el acta uso para
    nombrar la caida;
  * la fecha del commit que escribio la linea que se corrige, buscado por su
    asunto dentro del mismo rango;
  * la fecha de hoy, del reloj del sistema, para fechar la propia correccion.

QUE ESCRIBE: sustituye la fecha equivocada DENTRO de la linea de ratificacion y
anade DEBAJO una linea de CORRECCION DECLARADA que CITA el texto viejo. El texto
viejo NO se borra (EJECUTOR.md regla 8): una correccion que tapa lo que corrige
no se puede auditar.

LO QUE NO TOCA, a proposito y por encargo: el campo `fecha` del PLAN SELLADO del
lote A. Ese error se declara en el registro del tramo cuando el tramo cierre.

GUARDA: si la linea de destino no esta EXACTAMENTE como se espera (o si ya
esta corregida), no escribe nada y cae en ROJO. Es idempotente por negativa: la
segunda corrida no vuelve a escribir.

Uso:
  python scripts/loop/vuelta60_correccion_fecha.py --rango a248c6a3..d6e98e97 --vuelta-corregida 59 [--simular]
"""
import argparse
import datetime
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FUSIONES = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")

MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]

# LA MARCA DE LA LINEA QUE SE CORRIGE. No se busca por numero de linea (que se
# mueve en cuanto alguien anade un parrafo mas arriba) sino por su texto.
MARCA = "**RATIFICADA POR CORRIDA PROPIA DEL AUDITOR ("
ASUNTO_DEL_COMMIT = "TAREA 1.2: LA RATIFICACION DEL ACTA 58"


def git(*args):
    return subprocess.check_output(["git"] + list(args), cwd=RAIZ).decode("utf-8", "replace").strip()


def humana(iso):
    """2026-08-20 se escribe 20 ago 2026, que es como la casa fecha sus notas."""
    a, m, d = iso.split("-")
    return "%d %s %s" % (int(d), MESES[int(m) - 1], a)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--rango", required=True, help="rango git de la vuelta que se corrige")
    p.add_argument("--vuelta-corregida", type=int, required=True)
    p.add_argument("--simular", action="store_true")
    a = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("CORRECCION DECLARADA DE LA FECHA. La fecha buena se MIDE con git.")
    print("=" * 78)
    print()

    # --- LA MEDICION -------------------------------------------------------
    crudo = git("log", "--format=%h\t%ad\t%s", "--date=format:%Y-%m-%d %H:%M:%S", a.rango)
    filas = [l.split("\t") for l in crudo.splitlines() if l.strip()]
    if not filas:
        print("  ROJO: el rango %s no da ni un commit." % a.rango)
        return 1

    dias = sorted(set(f[1].split(" ")[0] for f in filas))
    print("  commits del rango %s: %d" % (a.rango, len(filas)))
    for h, fecha, asunto in reversed(filas):
        print("    %s  %s  %s" % (h, fecha, asunto[:58]))
    print("  dias distintos medidos: %s" % ", ".join(dias))
    if len(dias) != 1:
        print("  ROJO: el rango abarca mas de un dia; la correccion pide un dia solo.")
        return 1
    dia_bueno_iso = dias[0]
    dia_bueno = humana(dia_bueno_iso)

    autor = [f for f in filas if ASUNTO_DEL_COMMIT in f[2]]
    if len(autor) != 1:
        print("  ROJO: no hay UN solo commit que escribiera la linea (hallados %d)." % len(autor))
        return 1
    h_autor, fecha_autor, _ = autor[0]
    print("  el commit que ESCRIBIO la linea: %s de %s" % (h_autor, fecha_autor))

    # HOY SE MIDE POR DOS RELOJES Y TIENEN QUE COINCIDIR. Es la guarda que la
    # caida de la vuelta anterior pedia: una sola fuente de fecha es lo que
    # permitio suponerla.
    hoy_git = git("log", "-1", "--format=%ad", "--date=format:%Y-%m-%d")
    hoy_sistema = datetime.datetime.now().strftime("%Y-%m-%d")
    print("  hoy, por el ultimo commit del arbol : %s" % hoy_git)
    print("  hoy, por el reloj del sistema       : %s" % hoy_sistema)
    if hoy_git != hoy_sistema:
        print("  ROJO: los dos relojes no coinciden. No se fecha nada a ojo.")
        return 1
    hoy_iso = hoy_sistema
    print()

    # --- LA LINEA ----------------------------------------------------------
    texto = io.open(FUSIONES, encoding="utf-8").read()
    lineas = texto.split("\n")
    idx = [i for i, l in enumerate(lineas) if MARCA in l]
    if len(idx) != 1:
        print("  ROJO: se esperaba UNA linea con la marca y hay %d." % len(idx))
        return 1
    i = idx[0]
    vieja = lineas[i]
    m = re.search(r"\((\d+ [a-z]{3} \d{4}), vuelta %d, TAREA 1\.2 del encargo\)" % a.vuelta_corregida, vieja)
    if not m:
        print("  ROJO: la linea %d no trae la fecha en la forma esperada." % (i + 1))
        print("        %s" % vieja[:160])
        return 1
    fecha_vieja = m.group(1)
    if fecha_vieja == dia_bueno:
        print("  ROJO (por idempotencia): la linea %d YA dice %s. No se escribe nada."
              % (i + 1, dia_bueno))
        return 1

    print("  linea %d de docs/plan/03_FUSIONES.md" % (i + 1))
    print("    dice  : %s" % fecha_vieja)
    print("    y es  : %s" % dia_bueno)
    print()

    nueva = vieja.replace("(%s, vuelta" % fecha_vieja, "(%s, vuelta" % dia_bueno, 1)
    hashes = ", ".join("`%s`" % f[0] for f in reversed(filas))
    correccion = (
        "> **CORRECCION DECLARADA DE LA FECHA DE ESTA MISMA LINEA (%(hoy)s, vuelta 60, TAREA 1.1 "
        "del encargo; hallazgo del acta %(vc)d).** La linea de arriba decia **~~%(vieja)s~~** y la "
        "fecha buena es **%(buena)s**. **EL TEXTO VIEJO NO SE BORRA: queda citado aqui**, que es lo "
        "que la regla 8 del `EJECUTOR.md` pide. **EL MOTIVO ESTA MEDIDO, NO SUPUESTO:** los "
        "**%(n)d commits** de la vuelta %(vc)d (%(hashes)s) llevan **todos** fecha **%(iso)s** por "
        "`git log --date=format:'%%Y-%%m-%%d'`, y el commit que escribio esta misma linea es "
        "**`%(hautor)s`, de %(fautor)s**. **LA FECHA DE LA VUELTA SE SUPUSO EN VEZ DE MEDIRSE**, y de "
        "aqui en adelante **la fecha de todo reporte y de toda nota fechada SE MIDE** (del reloj del "
        "sistema o del commit) **y no se supone**. **EL CAMPO `fecha` DEL PLAN SELLADO DEL LOTE A "
        "(`docs/loop/PLAN_V59_OPU01_LOTE_A.json`) NO SE REEDITA:** su error queda declarado en el "
        "registro de este tramo cuando el tramo cierre."
    ) % {
        "hoy": humana(hoy_iso), "vc": a.vuelta_corregida, "vieja": fecha_vieja,
        "buena": dia_bueno, "n": len(filas), "hashes": hashes, "iso": dia_bueno_iso,
        "hautor": h_autor, "fautor": fecha_autor,
    }

    print("--- LA LINEA CORREGIDA ---")
    print(nueva)
    print()
    print("--- LA CORRECCION DECLARADA QUE SE ANADE DEBAJO ---")
    print(correccion)
    print()

    if a.simular:
        print("SIMULACION: no se escribe nada.")
        return 0

    lineas[i] = nueva
    lineas.insert(i + 1, "")
    lineas.insert(i + 2, correccion)
    io.open(FUSIONES, "w", encoding="utf-8", newline="\n").write("\n".join(lineas))
    print("ESCRITO: %s (linea %d corregida, correccion declarada en la %d)"
          % (FUSIONES, i + 1, i + 3))
    return 0


if __name__ == "__main__":
    sys.exit(main())
