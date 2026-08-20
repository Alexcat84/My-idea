# -*- coding: utf-8 -*-
"""vuelta52_fotos_fechadas.py . LA TAREA 1.4 DE LA VUELTA 52: LAS DOS FAMILIAS DE
CELDAS QUE SON FOTOS FECHADAS Y SE VENIAN MANTENIENDO COMO SI FUERAN TABLAS
VIGENTES.

POR QUE SE CORRE AL CIERRE Y NO CON EL RESTO DE LA TAREA 1: las dos notas que
este instrumento adosa llevan dentro LA MEDICION DE HOY COMO CONTRASTE, y esta
vuelta MUEVE esa medicion (funde tres actos y voltea seis veredictos por P.16).
La regla 1 del EJECUTOR, segundo renglon, lo dice sin rodeos: EL ESTADO AL
CIERRE SE MIDE AL CIERRE, y medir temprano y publicar tarde sin remedir es la
misma especie de caida que citar sin mirar. Por eso este instrumento se corre
DESPUES del ultimo movimiento de la vuelta y lee las cifras de la corrida de ese
momento.

LAS DOS FAMILIAS, adjudicadas por el acta de la vuelta 51, pregunta 4:

  a) EL APENDICE 95.1 de docs/INTRA_DOMINIO_INFORME.md, MARCADOR al corte 2.900.
     Es un CHECKPOINT DEL CRIBADO del bucle vuelta 4, no una tabla vigente. Su
     rotulo se fecha a su corte y a su corrida, su cadena de tachados se CIERRA
     con una nota fechada que declara que el mantenimiento por resta trato una
     foto como tabla vigente, y la medicion de hoy queda DENTRO de la nota como
     CONTRASTE, no como cifra vigente de la tabla.

  b) LAS DOS TABLAS "EL MARCADOR ... AL CERRAR LA VUELTA" de
     docs/plan/RECOMPUTO_3388.md, los registros de las vueltas 19 y 20, que
     publican 575/83/8/2.722 bajo un encabezado que dice "medido hoy".
     EL ENCARGO MANDA VERIFICAR ANTES DE FECHAR, y se verifico: se leyo del
     propio git el fichero de veredictos en el cierre de la vuelta 19 y en el de
     la 20 y se recomputo el marcador de cada estado
     (scripts/loop/vuelta52_marcador_por_git.py,
     docs/loop/SALIDA_V52_MARCADOR_POR_GIT.txt). LOS DOS ESTADOS MIDEN
     583 / 89 / 7 / 2.709, que es EXACTAMENTE LA PRIMERA CIFRA DE CADA CADENA.
     CALZA, asi que se fecha y se cierra la cadena. Si no hubiera calzado ni con
     su propia corrida, el encargo manda NO fechar y traerlo con las dos
     mediciones.

EL MARCADOR VIGENTE VIVE EN LAS FILAS 246 Y 1079 DE RECOMPUTO_3388.md Y EN EL
APENDICE 100.1 DE INTRA_DOMINIO_INFORME.md, Y EN NINGUN OTRO SITIO. Eso es lo
que estas tres celdas dejan de disputar.

LAS CIFRAS DE CONTRASTE NO SE TECLEAN: se leen de la salida de
scripts/recomputar_marcador.py corrida por este mismo instrumento, en los dos
cortes que hacen falta (2.900 para la familia a, 3.388 para la familia b).

IDEMPOTENTE: cada sustitucion comprueba primero si su resultado ya esta escrito.
Como el texto que escribe depende de la medicion del momento, re-correrlo
DESPUES de otro movimiento anadiria una nota nueva en vez de pisar la vieja, que
es justo lo que la casa quiere: las notas se adosan, no se reescriben.

Uso: python scripts/loop/vuelta52_fotos_fechadas.py [--simular]
"""
import argparse
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INF = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_INFORME.md")
REC = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")


def marcador(corte):
    p = subprocess.run(
        [sys.executable, os.path.join(RAIZ, "scripts", "recomputar_marcador.py"), str(corte)],
        capture_output=True, cwd=RAIZ, check=True)
    txt = p.stdout.decode("utf-8", "replace")
    bloque = txt.split("MARCADOR GLOBAL")[1].split("TASA POR DOMINIO")[0]
    out = {}
    for l in bloque.splitlines():
        m = re.match(r"\s+([ABCD])\s+(\d+)\s+([\d.]+)", l)
        if m:
            out[m.group(1)] = (int(m.group(2)), m.group(3))
    n = int(re.search(r"n = (\d+)", txt).group(1))
    return n, out


def mil(x):
    return "{:,}".format(x).replace(",", ".")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("TAREA 1.4 DE LA VUELTA 52: LAS DOS FAMILIAS DE FOTOS FECHADAS")
    print("modo: %s" % ("SIMULACION, no escribe" if a.simular else "ESCRITURA"))
    print("=" * 78)
    print()

    n29, m29 = marcador(2900)
    n33, m33 = marcador(3388)
    print("  CONTRASTE MEDIDO POR ESTE INSTRUMENTO, despues del ultimo movimiento:")
    print("    corte 2.900 (n %d): A %d, B %d, C %d, D %d"
          % (n29, m29["A"][0], m29["B"][0], m29["C"][0], m29["D"][0]))
    print("    corte 3.388 (n %d): A %d, B %d, C %d, D %d"
          % (n33, m33["A"][0], m33["B"][0], m33["C"][0], m33["D"][0]))
    print()

    contraste_29 = ("**A %d, B %d, C %d, D %s** sobre `n` **%s**, medido HOY con "
                    "`python scripts/recomputar_marcador.py 2900` "
                    "(`../loop/SALIDA_V52_MARCADOR_2900_CIERRE.txt`), corrido DESPUES del "
                    "ultimo movimiento de la vuelta 52"
                    % (m29["A"][0], m29["B"][0], m29["C"][0], mil(m29["D"][0]), mil(n29)))
    contraste_33 = ("**A %d, B %d, C %d, D %s** sobre `n` **%s**, medido HOY con "
                    "`python scripts/recomputar_marcador.py 3388` "
                    "(`../loop/SALIDA_V52_MARCADOR_CIERRE.txt`), corrido DESPUES del ultimo "
                    "movimiento de la vuelta 52"
                    % (m33["A"][0], m33["B"][0], m33["C"][0], mil(m33["D"][0]), mil(n33)))

    NOTA_B = (
        "\n\n> **ROTULO FECHADO Y CADENA CERRADA (20 ago 2026, vuelta 52, TAREA 1.4.b; "
        "adjudicacion del acta de la vuelta 51, pregunta 4). ESTA TABLA ES UNA FOTO "
        "FECHADA, NO UNA TABLA VIGENTE, y su encabezado decia *medido hoy*.** "
        "**LA CIFRA DE SU CORRIDA SE VERIFICO CONTRA GIT ANTES DE FECHAR NADA**, que es lo "
        "que el encargo manda y lo que separa un rotulo envejecido de una cifra que nacio "
        "mal: se leyo `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` del propio objeto de git en los "
        "commits del cierre de la vuelta {VUELTA} y se recomputo el marcador de ese estado "
        "(`python scripts/loop/vuelta52_marcador_por_git.py`, "
        "[`../loop/SALIDA_V52_MARCADOR_POR_GIT.txt`](../loop/SALIDA_V52_MARCADOR_POR_GIT.txt)). "
        "**Mide `A 583, B 89, C 7, D 2.709`, que es EXACTAMENTE LA PRIMERA CIFRA DE ESTA "
        "CADENA, la que hoy esta tachada.** O sea: la cifra nacio BIEN y lo que fallo "
        "despues fue el mantenimiento. **LAS CUATRO CORRECCIONES POSTERIORES DE ESTA CELDA "
        "(582, 581, 576 y 575) SE LE APLICARON A UNA FOTO COMO SI FUERA UNA TABLA VIGENTE, "
        "RESTANDO DE LA CIFRA ANTERIOR EN VEZ DE RE-MEDIR**, y por eso la `B` y la `C` de la "
        "cadena se quedaron congeladas mientras la `A` y la `D` seguian bajando. **LA CADENA "
        "TERMINA AQUI: ninguna vuelta futura la vuelve a mover, porque esta celda no publica "
        "el marcador vigente.** Nada se borra: los cinco valores se quedan tal cual, con el "
        "primero identificado como el bueno de su corrida. **EL MARCADOR VIGENTE VIVE EN LAS "
        "FILAS DEL PASO 1 Y DE LA TABLA POR DOMINIO DE ESTE MISMO DOCUMENTO Y EN EL APENDICE "
        "100.1 DE `../INTRA_DOMINIO_INFORME.md`, Y EN NINGUN OTRO SITIO.** **CONTRASTE, y va "
        "DENTRO de la nota y no en la tabla, porque no es cifra de esta celda:** {CONTRASTE}.")

    CAMBIOS = [
        # ------------------------------------------------ a) el apendice 95.1
        (INF, "1.4.a rotulo del 95.1",
         "### 95.1 MARCADOR (corte 2.900)",
         "### 95.1 MARCADOR (corte 2.900), FOTO FECHADA DEL CHECKPOINT DEL BUCLE VUELTA 4 "
         "(12 ago 2026), NO TABLA VIGENTE"),
        (INF, "1.4.a nota que cierra la cadena del 95.1",
         "de esta seccion ya recomputadas con las dos correcciones aplicadas.",
         "de esta seccion ya recomputadas con las dos correcciones aplicadas.\n"
         "\n"
         "> **ROTULO FECHADO Y CADENA CERRADA (20 ago 2026, vuelta 52, TAREA 1.4.a; "
         "adjudicacion del acta de la vuelta 51, pregunta 4). ESTE APENDICE ES UN CHECKPOINT "
         "DEL CRIBADO, UNA FOTO FECHADA DEL BUCLE VUELTA 4 AL CORTE 2.900, Y NO UNA TABLA "
         "VIGENTE.** La duda que el barrido `9.10` de la vuelta 51 levanto no era de "
         "medicion sino de naturaleza, y esta adjudicada: **es foto.** **Y LA CADENA DE "
         "TACHADOS QUE VUELTAS POSTERIORES LE FUERON APLICANDO A LA `A` Y A LA `D` LE ESTABA "
         "DANDO MANTENIMIENTO A UNA FOTO COMO SI FUERA UNA TABLA VIGENTE, restando de la "
         "cifra anterior en vez de re-medir**, y esa es exactamente la razon de que la `B` "
         "(89) y la `C` (7) se quedaran congeladas en las de la vuelta 4 mientras la `A` y la "
         "`D` bajaban escalon a escalon. **LA CADENA TERMINA AQUI: ninguna vuelta futura la "
         "vuelve a mover.** Nada se borra ni se reescribe: los tachados se quedan como "
         "registro de lo que paso. **CONTRASTE, y va DENTRO de esta nota y NO como cifra de "
         "la tabla, porque el corte 2.900 de hoy no es el checkpoint de la vuelta 4 sino el "
         "mismo tramo del archivo despues de dieciseis vueltas de correcciones y fusiones:** "
         + contraste_29 + ". **EL MARCADOR VIGENTE VIVE EN EL APENDICE 100.1 DE ESTE MISMO "
         "DOCUMENTO Y EN LAS FILAS DEL PASO 1 Y DE LA TABLA POR DOMINIO DE "
         "`plan/RECOMPUTO_3388.md`, Y EN NINGUN OTRO SITIO.**"),

        # ------------------------------------- b) las dos tablas al cerrar la vuelta
        (REC, "1.4.b rotulo de la tabla de la vuelta 19",
         "### 5. EL MARCADOR Y LO RESERVADO, al cerrar la vuelta\n\n| | medido hoy |",
         "### 5. EL MARCADOR Y LO RESERVADO, al cerrar la vuelta\n\n"
         "| | ~~medido hoy~~ **MEDIDO AL CERRAR LA VUELTA 19 (14 ago 2026), FOTO FECHADA** |"),
        (REC, "1.4.b nota de la tabla de la vuelta 19",
         "| **la FASE II** | **las veinte figuras quedan NOMBRADAS. Quien declare el bloque cerrado es el auditor, no esta seccion** |",
         "| **la FASE II** | **las veinte figuras quedan NOMBRADAS. Quien declare el bloque cerrado es el auditor, no esta seccion** |"
         + NOTA_B.replace("{VUELTA}", "19").replace("{CONTRASTE}", contraste_33)),

        (REC, "1.4.b rotulo de la tabla de la vuelta 20",
         "**EL MARCADOR, EL INVENTARIO Y LO RESERVADO, al cerrar la vuelta:**\n\n| | medido hoy |",
         "**EL MARCADOR, EL INVENTARIO Y LO RESERVADO, al cerrar la vuelta:**\n\n"
         "| | ~~medido hoy~~ **MEDIDO AL CERRAR LA VUELTA 20 (14 ago 2026), FOTO FECHADA** |"),
        (REC, "1.4.b nota de la tabla de la vuelta 20",
         "| operaciones en `OPERACIONES.jsonl` | **71**, **cero ejecutadas** |",
         "| operaciones en `OPERACIONES.jsonl` | **71**, **cero ejecutadas** |"
         + NOTA_B.replace("{VUELTA}", "20").replace("{CONTRASTE}", contraste_33)),
    ]

    textos = {}
    hechas = saltadas = 0
    for ruta, etiqueta, viejo, nuevo in CAMBIOS:
        if ruta not in textos:
            textos[ruta] = io.open(ruta, encoding="utf-8").read()
        t = textos[ruta]
        if nuevo in t:
            print("  YA ESTABA   %-44s (idempotente)" % etiqueta)
            saltadas += 1
            continue
        c = t.count(viejo)
        if c != 1:
            print("  ROJO        %-44s el texto viejo aparece %d veces" % (etiqueta, c))
            return 1
        textos[ruta] = t.replace(viejo, nuevo, 1)
        print("  HECHA       %-44s %s" % (etiqueta, os.path.basename(ruta)))
        hechas += 1

    for t in textos.values():
        if u"—" in t or u"–" in t:
            pass  # el fichero puede traer guiones viejos; solo se comprueba lo escrito

    for ruta, etiqueta, viejo, nuevo in CAMBIOS:
        if u"—" in nuevo or u"–" in nuevo:
            print("  ROJO: guion largo o medio en el texto nuevo de %s" % etiqueta)
            return 1

    if not a.simular:
        for ruta, t in textos.items():
            io.open(ruta, "w", encoding="utf-8", newline="\n").write(t)

    print()
    print("  sustituciones HECHAS: %d | ya estaban: %d" % (hechas, saltadas))
    print("  guiones largos y medios en lo escrito: CERO")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
