# -*- coding: utf-8 -*-
r"""vuelta190_rehacer_anexo.py . VUELVE A PONER EN EL REPORTE LOS CUERPOS DE LAS
CINCO TAREAS Y LAS CELDAS DE SU TABLA, PARA QUE EL REPORTE Y LOS FICHEROS DE
SECCION DIGAN LO MISMO.

POR QUE EXISTE, Y LA CAUSA ES DE ESTA MISMA VUELTA. La guarda de las dos
convenciones de `cerrar_reporte.py` tumbo el cierre **cinco veces seguidas** por
cifras publicadas sin su pareja o con la pareja partida por un salto de linea. Los
arreglos van en los ficheros de seccion, que son la fuente; pero el reporte ya
llevaba **anexado** el cuerpo de cada tarea, asi que **cada arreglo habia que
hacerlo en los dos sitios a la vez**, y hacerlo a mano dos veces es como se cuelan
las divergencias. Aqui deja de depender de que alguien se acuerde: el cuerpo viejo
se saca **de git**, el nuevo **del fichero de seccion de hoy**, y se cambia uno por
otro. **Si el viejo no aparece en el reporte, se dice y no se toca nada.**

LO QUE ESTE FICHERO NO HACE: no cierra el reporte, no talla ninguna cabecera, no
mide nada y no inventa ningun texto. Solo hace que el reporte diga lo que dicen
los ficheros de seccion.

USO:
  python scripts/loop/vuelta190_rehacer_anexo.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
# EL COMMIT DONDE EL REPORTE QUEDO CON LAS CINCO TAREAS ANEXADAS Y ANTES DE
# CERRARSE. Es de donde se saca el cuerpo VIEJO de cada seccion.
COMMIT_DEL_ANEXADO = "581330e4"
TAREAS = (1, 2, 3, 4, 5)

# LAS CELDAS DE LA TABLA DE TAREAS NO SALEN DE NINGUN FICHERO DE SECCION: se
# pasaron por `--pruebas` a `anexar_tarea_al_reporte.py`. Van aqui con su texto
# viejo y su texto nuevo, para que tampoco haya que acordarse de ellas.
CELDAS = [
    ("`SALIDA_V190_T1A_MUTACION_REGISTRADOR.txt` (6373 bytes), "
     "`SALIDA_V190_T1A_SIMULACION.txt` (28285), "
     "`SALIDA_V190_T1A_REGISTRO_R52.txt` (8854), "
     "`SALIDA_V190_T1A_RECORRIDO_SIN_ESCRIBIR.txt` (9230)",
     "`SALIDA_V190_T1A_MUTACION_REGISTRADOR.txt`, "
     "`SALIDA_V190_T1A_SIMULACION.txt`, `SALIDA_V190_T1A_REGISTRO_R52.txt` y "
     "`SALIDA_V190_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, con sus bytes por las dos "
     "convenciones, disco y LF, en la tabla de la seccion 2"),
    ("`SALIDA_V190_T2A_SIMULACION.txt` (4621 bytes), "
     "`SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt` (6763), "
     "`SALIDA_V190_T2_NOMINA.txt` (4510)",
     "`SALIDA_V190_T2A_SIMULACION.txt`, "
     "`SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt` y `SALIDA_V190_T2_NOMINA.txt`, "
     "con sus bytes por las dos convenciones, disco y LF, en la tabla de la "
     "seccion 2"),
    ("`SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt` (7489 bytes), "
     "`SALIDA_V190_T3_PLAN.txt` (7229), `SALIDA_V190_T3_SIGUIENTE.txt` (1555), "
     "`SALIDA_V190_T3_COTEJO_CLON.txt` (14332)",
     "`SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt`, "
     "`SALIDA_V190_T3_PLAN.txt`, `SALIDA_V190_T3_SIGUIENTE.txt` y "
     "`SALIDA_V190_T3_COTEJO_CLON.txt`, con sus bytes por las dos convenciones, "
     "disco y LF, en la tabla de la seccion 2"),
    ("`SALIDA_V190_T4_AISLAMIENTO.txt` (5301 bytes), "
     "`SALIDA_V190_T4_CIEGA.txt` (39678), `SALIDA_V190_T4_MIS_CLASES.txt` (4934), "
     "`SALIDA_V190_T4_DESTAPE.txt` (31816), `SALIDA_V190_T4_COTEJO.txt` (20783)",
     "`SALIDA_V190_T4_AISLAMIENTO.txt`, `SALIDA_V190_T4_CIEGA.txt`, "
     "`SALIDA_V190_T4_MIS_CLASES.txt`, `SALIDA_V190_T4_DESTAPE.txt` y "
     "`SALIDA_V190_T4_COTEJO.txt`, con sus bytes por las dos convenciones, disco "
     "y LF, en la tabla de la seccion 2"),
    ("`SALIDA_V190_T5_SEDE_OP_L_02.txt` (17879 bytes)",
     "`SALIDA_V190_T5_SEDE_OP_L_02.txt`, con sus bytes por las dos convenciones, "
     "disco y LF, en la tabla de la seccion 2"),
    ("El `sha256` LF del archivo abre y cierra en `0a77b5a35a962621`",
     "El `sha256` del archivo abre y cierra en `0a77b5a35a962621` por las dos "
     "convenciones, en disco y normalizado a LF"),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    t = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    print("docs/loop/REPORTE.md al entrar: %d bytes" % len(t.encode("utf-8")))
    fallos = 0
    for n in TAREAS:
        rel = "scripts/loop/_v190_t%d_seccion.md" % n
        r = subprocess.run(["git", "show", "%s:%s" % (COMMIT_DEL_ANEXADO, rel)],
                           cwd=RAIZ, capture_output=True)
        if r.returncode != 0:
            print("   t%d: no se pudo sacar el cuerpo viejo de git" % n)
            fallos += 1
            continue
        viejo = r.stdout.decode("utf-8").replace(chr(13) + NL, NL).rstrip(NL)
        nuevo = io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                        encoding="utf-8").read().replace(chr(13) + NL, NL).rstrip(NL)
        if viejo == nuevo:
            print("   t%d: sin cambios" % n)
            continue
        if viejo not in t:
            print("   t%d: EL CUERPO VIEJO NO APARECE EN EL REPORTE. No se toca." % n)
            fallos += 1
            continue
        t = t.replace(viejo, nuevo)
        print("   t%d: cuerpo actualizado (%d -> %d bytes)"
              % (n, len(viejo.encode("utf-8")), len(nuevo.encode("utf-8"))))
    for viejo, nuevo in CELDAS:
        if viejo not in t:
            if nuevo in t:
                print("   celda ya actualizada: %r" % viejo[:44])
            else:
                print("   CELDA NO ENCONTRADA: %r" % viejo[:44])
                fallos += 1
            continue
        t = t.replace(viejo, nuevo)
        print("   celda actualizada: %r" % viejo[:44])
    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(t)
    print("docs/loop/REPORTE.md al salir: %d bytes" % len(t.encode("utf-8")))
    print("CIFRA fallos: %d" % fallos)
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
