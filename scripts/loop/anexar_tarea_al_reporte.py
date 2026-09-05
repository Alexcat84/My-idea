# -*- coding: utf-8 -*-
r"""anexar_tarea_al_reporte.py . LA FILA DE UNA TAREA, ANEXADA AL REPORTE EN
CUANTO ESA TAREA CIERRA.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como `paso0_archivar_anterior.py`,
`archivar_reporte.py`, `serie_de_registros.py` y `tallar_cabecera_reporte.py`:
el esqueleto de cada vuelta deja los dos huecos marcados y este fichero los
rellena tarea a tarea. NO se clona por vuelta.

POR QUE NACE (vuelta 172, TAREA 1). `EJECUTOR.md` 1 dice, desde el 4 sep 2026 y
por decision del fundador, que **el reporte se abre al empezar y CRECE POR
ANEXION: cada tarea anexa su fila AL CERRARSE, no al final de la vuelta**. El
esqueleto ya sabe abrirlo y `cerrar_reporte.py` sabe cerrarlo, pero **anexar era
un paso a mano**, y las vueltas 170 y 171 demostraron lo que le pasa a los pasos
a mano de este tramo: se caen los dos, y cuando se caen no queda nada.

QUE HACE, Y CAE EN ROJO SI NO PUEDE:

  1. Cambia el ESTADO de la fila de la tarea N dentro del bloque
     `<!-- TABLA DE TAREAS -->`, y de paso su celda de pruebas. La fila se
     localiza por `| **TAREA N** |` y tiene que aparecer EXACTAMENTE UNA VEZ.
  2. Anexa el CUERPO de la tarea dentro del bloque
     `<!-- ANEXO DE TAREAS -->`, justo antes de su marca de fin, quitando el
     `*(vacio: ...)*` la primera vez.
  3. RELEE DEL DISCO y comprueba las cuatro cosas: que la fila ya no dice
     ABIERTA, que dice el estado nuevo, que el cuerpo esta byte a byte, y que
     no se han colado guiones largos ni medios.

NO TOCA LA CABECERA NI EL VEREDICTO: eso es de `cerrar_reporte.py`.

USO:
  python scripts/loop/anexar_tarea_al_reporte.py --tarea 1 \
      --estado "CERRADA" --pruebas "`SALIDA_V172_T1A_...`, `_T1B_...`" \
      --cuerpo scripts/loop/_v172_t1_seccion.md
"""
import argparse
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")

FIN_ANEXO = "<!-- FIN ANEXO DE TAREAS -->"
ABRE_ANEXO = "<!-- ANEXO DE TAREAS -->"
ABRE_TABLA = "<!-- TABLA DE TAREAS -->"
FIN_TABLA = "<!-- FIN TABLA DE TAREAS -->"
VACIO = "*(vacio: ninguna tarea ha cerrado todavia)*"


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def anexar(tarea, estado, pruebas, cuerpo, ruta=None):
    """PURA salvo por leer y escribir la ruta que se le pasa. Devuelve
    (ok, informe) con informe como lista de lineas."""
    ruta = ruta or REPORTE
    inf = []
    w = inf.append
    texto = leer(ruta)
    rojos = []

    for marca in (ABRE_TABLA, FIN_TABLA, ABRE_ANEXO, FIN_ANEXO):
        n = texto.count(marca)
        w("   marca %-32s aparece %d vez(ces)" % (marca, n))
        if n != 1:
            rojos.append("la marca %s aparece %d veces" % (marca, n))
    if rojos:
        return False, inf + ["   " + r for r in rojos]

    i_tab, j_tab = texto.index(ABRE_TABLA), texto.index(FIN_TABLA)
    tabla = texto[i_tab:j_tab]
    ancla = "| **TAREA %s** |" % tarea
    filas = [l for l in tabla.split(NL) if l.startswith(ancla)]
    w("   filas que empiezan por %r: %d" % (ancla, len(filas)))
    if len(filas) != 1:
        return False, inf + ["   la fila de la tarea %s no aparece exactamente una vez" % tarea]

    vieja = filas[0]
    celdas = vieja.split(" | ")
    w("   CIFRA celdas de la fila: %d" % len(celdas))
    if len(celdas) != 4:
        return False, inf + ["   la fila de la tarea %s no tiene cuatro celdas" % tarea]
    if "ABIERTA, SIN CERRAR" not in celdas[2]:
        w("   AVISO: la fila no decia ABIERTA, SIN CERRAR sino %r" % celdas[2][:60])
    nueva = " | ".join([celdas[0], celdas[1], "**%s**" % estado, pruebas + " |"])
    texto = texto.replace(vieja, nueva)
    w("   estado escrito: %s" % estado)

    i_an = texto.index(ABRE_ANEXO)
    j_an = texto.index(FIN_ANEXO)
    bloque = texto[i_an + len(ABRE_ANEXO):j_an]
    if VACIO in bloque:
        bloque = bloque.replace(VACIO + NL, "")
        w("   el %r se quita: es la primera tarea que cierra" % VACIO[:22])
    bloque = bloque.rstrip(NL) + NL + NL + cuerpo.strip(NL) + NL + NL
    texto = texto[:i_an + len(ABRE_ANEXO)] + bloque + texto[j_an:]
    w("   cuerpo anexado: %d bytes, %d saltos de linea"
      % (len(cuerpo.encode("utf-8")), cuerpo.count(NL)))

    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    w("   ESCRITO: %s (%d bytes, %d saltos de linea)"
      % (os.path.relpath(ruta, RAIZ).replace(os.sep, "/"),
         len(texto.encode("utf-8")), texto.count(NL)))

    de_nuevo = leer(ruta)
    fallos = 0
    for etiqueta, cond in (
            ("la fila de la tarea %s ya no dice ABIERTA" % tarea,
             not any(l.startswith(ancla) and "ABIERTA, SIN CERRAR" in l
                     for l in de_nuevo.split(NL))),
            ("y dice el estado nuevo",
             any(l.startswith(ancla) and estado in l for l in de_nuevo.split(NL))),
            ("el cuerpo esta byte a byte dentro del anexo",
             cuerpo.strip(NL) in de_nuevo),
            ("cero guiones largos y cero guiones medios",
             chr(8212) not in de_nuevo and chr(8211) not in de_nuevo)):
        w("   %-56s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            fallos += 1
    w("   CIFRA comprobaciones de relectura: 4 | fallan: %d" % fallos)
    return fallos == 0, inf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tarea", required=True)
    ap.add_argument("--estado", required=True)
    ap.add_argument("--pruebas", required=True)
    ap.add_argument("--cuerpo", required=True)
    a = ap.parse_args()

    print("=" * 78)
    print("SE ANEXA LA TAREA %s AL REPORTE, AL CERRARSE Y NO AL FINAL" % a.tarea)
    print("=" * 78)
    cuerpo = leer(os.path.join(RAIZ, a.cuerpo.replace("/", os.sep)))
    print("   cuerpo leido de: %s" % a.cuerpo)
    ok, informe = anexar(a.tarea, a.estado, a.pruebas, cuerpo)
    for l in informe:
        print(l)
    print("")
    if not ok:
        print("ROJO: la tarea %s no queda anexada." % a.tarea)
        return 1
    print("VERDE: la tarea %s queda anexada al reporte." % a.tarea)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
