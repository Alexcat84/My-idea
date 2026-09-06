# -*- coding: utf-8 -*-
r"""_v183b_abrir_fila_tarea3.py . LA FILA VACIA DE LA TAREA QUE TRAE LA
CONTINUACION DE LA VUELTA 183, ABIERTA EN LA TABLA QUE YA EXISTE.

POR QUE HACE FALTA Y POR QUE NO ES UN ESQUELETO NUEVO. `EJECUTOR.md` 1 manda que
el reporte se abra con LAS FILAS VACIAS DE LAS TAREAS ENCARGADAS y que cada tarea
ANEXE SU FILA AL CERRARSE. El encargo de esta continuacion PROHIBE tallar un
esqueleto nuevo y archivar el reporte de la 183 (adjudicacion 5.7 del acta 183),
asi que la fila de la tarea nueva se abre DENTRO de la tabla que ya esta, en
estado ABIERTA, SIN CERRAR, y `scripts/loop/anexar_tarea_al_reporte.py` la cierra
despues sin tocarse.

LA NUMERACION SE DICE EN VEZ DE DISIMULARSE. El encargo de la continuacion llama
TAREA 1 a los registros y TAREA 2 a la bateria. La tabla del reporte YA tiene una
TAREA 1 (la de la primera sesion de la 183, cerrada) y una TAREA 2 (la bateria,
abierta, que es la misma que la TAREA 2 del encargo de hoy). Por eso la tarea
nueva entra como TAREA 3 y su celda dice, con todas las letras, que es la TAREA 1
del encargo de la continuacion. Renumerar la tabla o reusar la fila de la TAREA 1
seria pisar trabajo ya cerrado y ya auditado.

CAE EN ROJO ANTES QUE ESCRIBIR DOS VECES: si la fila ya esta, no la duplica.

USO:
  python scripts/loop/_v183b_abrir_fila_tarea3.py
"""
import io
import os
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
FIN_TABLA = "<!-- FIN TABLA DE TAREAS -->"
ANCLA = "| **TAREA 3** |"

QUE_ENCARGA = (
    "LOS REGISTROS Y LA CORRECCION DE LA ATRIBUCION, BLOQUEANTE Y ANTES DE TOCAR "
    "LA BATERIA. **Es la TAREA 1 del encargo de la CONTINUACION de esta vuelta**, "
    "y entra como TAREA 3 porque la tabla ya tiene una TAREA 1 cerrada y una "
    "TAREA 2 abierta que es la bateria. (a) El acta 183 entra en la serie con el "
    "numero que devuelve `scripts/loop/serie_de_registros.py`, con sus siete "
    "adjudicaciones `5.1` a `5.7`, la caida del ejecutor `E.1`, las CERO caidas "
    "propias del auditor y su caso por mutacion. (b) LA CORRECCION DEL `E.1`, que "
    "es la operacion de codigo: el numero de vuelta y el nombre del lanzador de "
    "la bateria se COMPUTAN de `os.path.basename` y no se clavan, con caso "
    "positivo por mutacion sobre variable computada que CAE si alguien vuelve a "
    "clavarlos. (c) Los tramos 1 y 2 se vuelven a correr despues de (b), con el "
    "coste medido al lado. (d) Las tres rutas de la celda de prueba de la TAREA 1 "
    "se escriben enteras. (e) `scripts/loop/_v183_tallar_cierre.py` se commitea y "
    "no se borra. (f) La relectura al doble del tramo de la ciega del acta 183, "
    "cotejando su `sha256` contra el sello antes de leer un solo puesto")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    texto = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    print("docs/loop/REPORTE.md -> %d bytes LF, %d saltos de linea"
          % (len(texto.encode("utf-8")), texto.count(NL)))
    if texto.count(FIN_TABLA) != 1:
        print("ROJO: la marca %r aparece %d veces." % (FIN_TABLA, texto.count(FIN_TABLA)))
        return 1
    if ANCLA in texto:
        print("NO SE ESCRIBE: la fila de la TAREA 3 ya esta en la tabla.")
        return 0
    fila = ("%s %s | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la "
            "tarea) |" % (ANCLA, QUE_ENCARGA))
    texto = texto.replace(FIN_TABLA, fila + NL + FIN_TABLA, 1)
    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(texto)
    de_nuevo = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    print("ESCRITA la fila de la TAREA 3, en estado ABIERTA, SIN CERRAR.")
    print("docs/loop/REPORTE.md pasa a %d bytes LF, %d saltos de linea"
          % (len(de_nuevo.encode("utf-8")), de_nuevo.count(NL)))
    print("guiones largos o medios en el reporte: %d"
          % (de_nuevo.count(chr(8212)) + de_nuevo.count(chr(8211))))
    dentro = de_nuevo.split("<!-- TABLA DE TAREAS -->", 1)[1].split(FIN_TABLA, 1)[0]
    filas = [l for l in dentro.split(NL) if l.strip().startswith("| **TAREA")]
    print("CIFRA filas de tarea en la tabla, contadas de la tabla: %d" % len(filas))
    for l in filas:
        print("   %s" % l[:96])
    return 0


if __name__ == "__main__":
    sys.exit(main())
