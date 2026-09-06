# -*- coding: utf-8 -*-
r"""vuelta166_tarea3b_motivo.py . TAREA 3 de la vuelta 166, segunda mitad.

EL MOTIVO ESCRITO DEL RECOMPUTO, ADOSADO BAJO LA TABLA DEL PASO 1, por letra del
encargo: *"Y VA CON SU MOTIVO ESCRITO, que es lo que 08_VERIFICACION dice de esta
tabla: el retrato de las A es el paso 1 de cuatro y ES EL INSUMO DE TODO LO
DEMAS."*

LA CITA NO SE PARAFRASEA NI SE TECLEA: se LEE hoy de `docs/plan/08_VERIFICACION.md`
y se pega con su linea. Si la frase no esta ahi, el instrumento PARA en vez de
citar de memoria (`EJECUTOR.md` 2, y la regla de la cita con su linea).

Y DECLARA LO QUE NO SE HIZO, que es la otra mitad: los pasos 2, 3 y 4 NO se
recomputan en esta vuelta.

IDEMPOTENTE: si el bloque ya esta, no escribe.

USO:
  python scripts/loop/vuelta166_tarea3b_motivo.py            (mide, NO escribe)
  python scripts/loop/vuelta166_tarea3b_motivo.py --aplicar  (mide y escribe)
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")
VERIF = os.path.join(RAIZ, "docs", "plan", "08_VERIFICACION.md")

ANCLA = "| pares con mas de un veredicto crudo apuntando al mismo par resuelto |"
MARCA = "> **MOTIVO ESCRITO DEL RECOMPUTO (4 sep 2026, vuelta 166, TAREA 3"


def cita_del_insumo():
    """LA CITA SE LEE, NO SE RECUERDA. Devuelve (linea, texto) o (None, None)."""
    for i, l in enumerate(io.open(VERIF, encoding="utf-8").read().split("\n"), 1):
        if "EL RETRATO DE LAS A" in l and "insumo de todo lo demas" in l:
            # SE CITA LA CELDA, NO LA FILA ENTERA: las barras de la tabla no
            # son parte de la frase, y meterlas dentro de una cita la falsea.
            celdas = [c.strip() for c in l.strip().strip("|").split("|")]
            return i, celdas[-1].replace("**", "")
    return None, None


def bloque(linea_cita, texto_cita, otros):
    return (
        "\n"
        "%s, adjudicacion 5.12 del acta 165).** **POR QUE SE RECOMPUTA ESTA TABLA Y NO\n"
        "OTRA, dicho con la regla delante y no como preferencia:** `docs/plan/08_VERIFICACION.md`\n"
        "pone el retrato de las A como **PASO 1 DE CUATRO** y escribe, en su linea **%d** y\n"
        "leida hoy: *\"%s\"*. Los otros dos pasos que lo nombran lo dicen en la misma tabla y\n"
        "tambien se leen hoy: %s. **Una tabla rancia en el paso 1 no falla: contamina los\n"
        "tres siguientes en silencio**, que es exactamente lo que el canon 9 del banco llama\n"
        "degradacion callada.\n"
        "\n"
        "> **Y SE DECLARA LO QUE ESTA VUELTA NO HIZO, para que nadie lo lea como hecho:**\n"
        "> **los PASOS 2, 3 y 4 de este documento NO se recomputan aqui.** El encargo de la\n"
        "> vuelta 166 pide el PASO 1 y nada mas, con estas palabras: *\"NO recomputes los\n"
        "> pasos 2, 3 y 4: no estan encargados y meterlos aqui seria decidir su alcance por\n"
        "> tu cuenta\"*. **Sus cifras siguen siendo las de su corte y no las de hoy**, y quien\n"
        "> las use tiene que saberlo: el insumo se movio debajo de ellas.\n"
        % (MARCA, linea_cita, texto_cita, otros))


def main(aplicar):
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 166, TAREA 3b: EL MOTIVO ESCRITO, CITADO Y NO RECORDADO")
    print("=" * 78)
    print("")

    n_cita, texto_cita = cita_del_insumo()
    print("A) LA CITA, LEIDA HOY DE docs/plan/08_VERIFICACION.md")
    if n_cita is None:
        print("   PARADA: la frase del insumo no esta en el fichero. No se cita de")
        print("   memoria una frase que no se puede senalar con su linea.")
        return 1
    print("   docs/plan/08_VERIFICACION.md:%d" % n_cita)
    print("   %s" % texto_cita)
    otras = []
    for i, l in enumerate(io.open(VERIF, encoding="utf-8").read().split("\n"), 1):
        if "del paso 1" in l and l.startswith("|"):
            otras.append((i, l.strip()))
    print("   CIFRA otras filas que nombran el paso 1: %d" % len(otras))
    for i, l in otras:
        print("      linea %d: %s" % (i, l[:120]))
    if not otras:
        print("   PARADA: la tabla no trae ninguna fila que dependa del paso 1.")
        return 1
    otros_txt = "; ".join(
        "el **PASO %s** (linea %d) dice *\"%s\"*"
        % (re.search(r"^\| \*\*(\d+)\*\*", l).group(1), i,
           l.split("|")[3].strip().replace("**", ""))
        for i, l in otras if re.search(r"^\| \*\*(\d+)\*\*", l))
    print("")

    texto = io.open(DOC, encoding="utf-8").read()
    print("B) LA IDEMPOTENCIA, COMPROBADA ANTES DE ESCRIBIR")
    if MARCA in texto:
        print("   YA ESTABA: el bloque del motivo vive en el documento.")
        print("   CIFRA bloques escritos: 0")
        return 0
    lineas = texto.split("\n")
    anclas = [i for i, l in enumerate(lineas, 1) if l.startswith(ANCLA)]
    print("   CIFRA veces que el ancla (la 4.a fila de la tabla) aparece: %d"
          % len(anclas))
    if len(anclas) != 1:
        print("   PARADA: el ancla no es unica.")
        return 1
    n = anclas[0]
    print("   se inserta DESPUES de docs/plan/RECOMPUTO_3388.md:%d" % n)
    print("")

    b = bloque(n_cita, texto_cita, otros_txt)
    nuevas = lineas[:n] + b.split("\n") + lineas[n:]
    nuevo = "\n".join(nuevas)
    print("C) LAS GUARDAS, SOBRE EL TEXTO NUEVO SIN ESCRIBIRLO")
    guardas = [
        ("1_el_documento_solo_crece", len(nuevo) > len(texto), True),
        ("2_ninguna_linea_vieja_desaparece",
         all(l in nuevas for l in lineas), True),
        ("3_las_cuatro_filas_del_paso_1_siguen_intactas",
         sum(1 for l in lineas if l.startswith("| ") and "|" in l[2:]
             and l in nuevas), sum(1 for l in lineas if l.startswith("| ")
                                   and "|" in l[2:])),
        ("4_el_bloque_cita_la_linea_medida", ("linea **%d**" % n_cita) in nuevo, True),
        ("5_y_declara_lo_que_no_se_hizo", "NO se recomputan aqui" in nuevo, True),
    ]
    malos = 0
    for nombre, real, esp in guardas:
        ok = real == esp
        print("   %-46s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esp))
        if not ok:
            malos += 1
    if malos:
        print("   PARADA: la simulacion falla. NO SE ESCRIBE NADA.")
        return 1
    print("")
    print("D) EL BLOQUE ENTERO, PARA QUE NADA ENTRE SIN LEERSE")
    print(b)
    if not aplicar:
        print("E) NO SE ESCRIBE (falta --aplicar)")
        return 0
    with io.open(DOC, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(nuevo)
    print("E) ESCRITO")
    t2 = io.open(DOC, encoding="utf-8").read()
    print("   CIFRA lineas antes: %d por len(split(NL)) | despues: %d lineas por count(NL), que calza con wc -l, y %d por len(split(NL))"
          % (len(lineas), t2.count("\n"), len(t2.split("\n"))))
    print("   el bloque esta: %s" % (MARCA in t2))
    print("   FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main("--aplicar" in sys.argv))
