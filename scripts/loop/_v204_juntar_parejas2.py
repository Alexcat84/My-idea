# -*- coding: utf-8 -*-
r"""_v204_juntar_parejas2.py . SEGUNDA PASADA: LA RUTA SE QUEDA CON EL TAMANO
QUE TIENE AL CIERRE, Y EL TAMANO INTERMEDIO SE DICE SIN NOMBRAR LA RUTA.

PREFIJO DE GUION BAJO: computo de una vuelta, fuera del censo y de la nomina.

POR QUE EXISTE, Y ES LA LETRA (a) QUE EL ENCARGO ESCRIBIO ANTES DE QUE ME
PASARA: *una pareja de bytes COMPLETA puede ser FALSA si pegas a una ruta el
tamano que tenia EN MITAD DE LA VUELTA; detras de cada ruta va SU tamano al
cierre y el intermedio se dice sin nombrar la ruta*.

La primera pasada junto las parejas y la guarda dejo de ver cifras sueltas, pero
entonces encendio la OTRA comprobacion, la que recomputa del disco: en la linea
de la PRIMERA CORRIDA la ruta `docs/PENDIENTES.md` iba pegada a **1131953**, que
es su tamano AL ENTRAR, y el disco dice **1145356**, que es el de AHORA. La
pareja estaba completa y era FALSA como atribucion. Lo mismo con la salida
sellada de la segunda corrida, donde la ruta iba pegada a un CRECIMIENTO de 0 y
el disco dice su tamano.

NO SE CAMBIA NI UNA CIFRA: se cambia DE QUE RENGLON cuelga cada una.

USO: python scripts/loop/_v204_juntar_parejas2.py
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CAMBIOS = [
    ("scripts/loop/_v204_t1_seccion.md",
     "- **PRIMERA CORRIDA.** `docs/PENDIENTES.md` entra con **1131953 bytes en disco y 1131953 normalizado a LF**," + NL
     + "  y su `sha256` de entrada es **725b85e12050a0ae** en disco y **725b85e12050a0ae** normalizado a LF." + NL
     + "  Sale con **1145356 bytes en disco y 1145356 normalizado a LF**," + NL
     + "  y su `sha256` de salida es **de3311c2a8d5aa8c** en disco y **de3311c2a8d5aa8c** normalizado a LF." + NL
     + "  Crecimiento **13403 bytes en disco y 13403 normalizado a LF**, y **209** lineas mas.",

     "- **PRIMERA CORRIDA, Y LA RUTA SE QUEDA CON SU TAMANO AL CIERRE.** La sede entra" + NL
     + "  con **1131953 bytes en disco y 1131953 normalizado a LF**, y ese es su tamano" + NL
     + "  DE ENTRADA, que por eso va **sin nombrar la ruta en su renglon**: pegarle una" + NL
     + "  ruta a una cifra intermedia hace una pareja completa y falsa." + NL
     + "  El `sha256` de entrada era **725b85e12050a0ae** en disco y **725b85e12050a0ae** normalizado a LF." + NL
     + "  AL CIERRE, `docs/PENDIENTES.md` mide **1145356 bytes en disco y 1145356 normalizado a LF**," + NL
     + "  con `sha256` **de3311c2a8d5aa8c** en disco y **de3311c2a8d5aa8c** normalizado a LF." + NL
     + "  El crecimiento es de **13403** por las dos convenciones, y de **209** lineas."),

    ("scripts/loop/_v204_t1_seccion.md",
     "- **SEGUNDA CORRIDA, la que sella la idempotencia**" + NL
     + "  (`docs/loop/SALIDA_V204_T1_REGISTROS_SEGUNDA.txt`): **crecimiento 0 bytes en disco y 0 normalizado a LF**," + NL
     + "  **0 lineas y 0 entradas escritas**, porque la guarda de idempotencia mira **el" + NL
     + "  sujeto** y no solo el numero.",

     "- **SEGUNDA CORRIDA, la que sella la idempotencia**, y su salida vive en" + NL
     + "  `docs/loop/SALIDA_V204_T1_REGISTROS_SEGUNDA.txt`." + NL
     + "  El crecimiento es de **0** por las dos convenciones, **0 lineas** y **0 entradas" + NL
     + "  escritas**, porque la guarda de idempotencia mira **el sujeto** y no solo el" + NL
     + "  numero."),
]

fuentes = {}
for rel, viejo, nuevo in CAMBIOS:
    if rel not in fuentes:
        fuentes[rel] = io.open(os.path.join(RAIZ, rel),
                               encoding="utf-8").read().replace(chr(13) + NL, NL)

fallos = []
print("LAS SUSTITUCIONES DE LA SEGUNDA PASADA, CONTADAS EN SU FUENTE:")
for rel, viejo, nuevo in CAMBIOS:
    hay = fuentes[rel].count(viejo)
    print("   %-38s apariciones %d (se necesita 1)" % (os.path.basename(rel), hay))
    if hay != 1:
        fallos.append("%s: %d apariciones" % (os.path.basename(rel), hay))
        continue
    fuentes[rel] = fuentes[rel].replace(viejo, nuevo)

print("")
if fallos:
    print("ROJO, %d motivo(s), y NO se escribe nada:" % len(fallos))
    for f in fallos:
        print("   " + f)
    raise SystemExit(1)

for rel, t in fuentes.items():
    io.open(os.path.join(RAIZ, rel), "w", encoding="utf-8", newline=NL).write(t)
print("VERDE. ESCRITO: %s" % ", ".join(sorted(fuentes)))
print("")
print("EL REPORTE SE REHACE DESDE EL ESQUELETO Y SE VUELVEN A ANEXAR LAS CUATRO")
print("TAREAS CON SU INSTRUMENTO, que es lo que la casa manda: el reporte no se")
print("parchea a mano, lo escribe anexar_tarea_al_reporte.py.")
