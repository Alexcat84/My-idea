# -*- coding: utf-8 -*-
r"""_v178_arreglo_parejas.py . LA GUARDA DE LA PAREJA DE CIFRAS CAZO A SU AUTOR,
Y ESTE FICHERO ES LA CORRECCION.

TAREA 1.e de la vuelta 178, aplicada al reporte de la propia vuelta 178. La
guarda `cerrar_reporte.cifras_sin_pareja()` nacio en esta misma vuelta, se corrio
sobre el reporte que esta vuelta llevaba escrito y encontro CUATRO cifras
publicadas sin su pareja. Las cuatro eran mias.

QUE SE ARREGLA, Y EL ARREGLO ES DE REDACCION Y NO DE CIFRA: ninguna cifra cambia
de valor. Lo que cambia es que las DOS convenciones queden EN LA MISMA LINEA, que
es lo que la guarda mide y lo que el acta 177 punto 7.11 pide.

SE ARREGLAN LOS DOS SITIOS A LA VEZ, el borrador de la seccion y el reporte ya
anexado, con la MISMA sustitucion, para que no diverjan. Un borrador que ya no
dice lo que el reporte dice no se puede auditar.

ES UN PARCHE, NO CODIGO VIVO: empieza por guion bajo. Cada sustitucion lleva su
`assert`.
"""
import io
import os

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PARES = [
    ("(3.479 bytes en disco y 3.479 en git, medidos en el bloque H.7 de la apertura)",
     "(3.479 bytes en disco y 3.479 bytes en git, medidos en el bloque H.7)"),
    ("""luego no lo hizo en dos celdas: un tallador en "5.001 bytes" cuando el disco decia
5.021, y un sha `7d683eea4700f18b` que era el de LF. **Las dos cifras eran
verdaderas y las dos hubo que ir a buscarlas.**""",
     """luego no lo hizo en dos celdas: un tallador publicado en 5.001 bytes cuando su medicion de disco decia 5.021 bytes,
y un sha `7d683eea4700f18b`, que es el normalizado a LF y no el de disco. **Las
dos cifras eran verdaderas y las dos hubo que ir a buscarlas.**"""),
    ("""`docs/plan/OP_L_03_TRIANGULOS.jsonl`, **16 filas, 45.168 bytes en disco y 45.168
normalizados a LF**, sha256 en disco y sha256 en LF los dos""",
     """`docs/plan/OP_L_03_TRIANGULOS.jsonl`, **16 filas, 45.168 bytes en disco y 45.168 bytes normalizados a LF**,
sha256 en disco y sha256 en LF los dos"""),
]

DESTINOS = [
    "docs/loop/REPORTE.md",
    "scripts/loop/_v178_t1_seccion.md",
    "scripts/loop/_v178_t3_seccion.md",
]

total = 0
for destino in DESTINOS:
    ruta = os.path.join(RAIZ, destino.replace("/", os.sep))
    t = io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)
    n = 0
    for viejo, nuevo in PARES:
        if viejo in t:
            t = t.replace(viejo, nuevo)
            n += 1
    if n:
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print("%-36s sustituciones aplicadas: %d" % (destino, n))
    total += n

assert total >= len(PARES), (
    "se esperaban al menos %d sustituciones en total y salieron %d"
    % (len(PARES), total))
print("TOTAL DE SUSTITUCIONES: %d" % total)
