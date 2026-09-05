# -*- coding: utf-8 -*-
r"""vuelta169_anexar_tarea.py . ANEXA LA FILA Y LA SECCION DE UNA TAREA A
docs/loop/REPORTE.md EN EL MOMENTO EN QUE ESA TAREA CIERRA.

POR QUE NACE. Es la otra mitad de scripts/loop/vuelta169_esqueleto_reporte.py.
La regla de EJECUTOR.md 1 ("EL REPORTE ABRE CON LA VUELTA") no pide solo abrir
el reporte: pide que CADA TAREA ANEXE SU FILA AL CERRARSE, no al final de la
vuelta. Si la anexion se hace a mano, vuelve a ser una frase tecleada, que es
la especie que la racha de las vueltas 54, 55, 56, 74, 75, 76, 77, 78 y 79 ya
costo. Asi que la anexion tambien es un instrumento.

LO QUE COMPRUEBA ANTES DE ESCRIBIR, Y CAE EN ROJO SIN TOCAR NADA SI FALLA:
  - que docs/loop/REPORTE.md exista y sea el de la vuelta 169 (su primera linea
    lo dice); anexar sobre el reporte de otra vuelta seria escribir en el
    fichero equivocado;
  - que traiga los cuatro marcadores del esqueleto;
  - que la fila de esa tarea siga diciendo ABIERTA, SIN CERRAR. UNA TAREA NO SE
    CIERRA DOS VECES: si ya esta cerrada, ROJO, porque una segunda anexion
    taparia la primera y una correccion que tapa lo que corrige no se puede
    auditar;
  - que el fichero de seccion exista y no este vacio.

USO:
  python scripts/loop/vuelta169_anexar_tarea.py --tarea 1 \
      --estado "CERRADA" --prueba "`docs/loop/SALIDA_V169_T1_*.txt`" \
      --seccion docs/loop/_v169_t1_seccion.md
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
VUELTA = 169
ABIERTA = "**ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |"

ap = argparse.ArgumentParser()
ap.add_argument("--tarea", required=True)
ap.add_argument("--estado", required=True)
ap.add_argument("--prueba", required=True)
ap.add_argument("--seccion", required=True)
a = ap.parse_args()

fallos = []
if not os.path.exists(RUTA):
    print("ROJO: no existe docs/loop/REPORTE.md; corre antes el esqueleto")
    sys.exit(1)

texto = io.open(RUTA, encoding="utf-8").read()
if not texto.splitlines()[0].startswith("# REPORTE DE LA VUELTA %d " % VUELTA):
    fallos.append("docs/loop/REPORTE.md NO es el de la vuelta %d: su primera linea dice %r"
                  % (VUELTA, texto.splitlines()[0][:80]))
for marca in ("<!-- TABLA DE TAREAS -->", "<!-- FIN TABLA DE TAREAS -->",
              "<!-- ANEXO DE TAREAS -->", "<!-- FIN ANEXO DE TAREAS -->"):
    if marca not in texto:
        fallos.append("falta el marcador %s" % marca)

prefijo = "| **TAREA %s** | " % a.tarea
fila = [l for l in texto.splitlines() if l.startswith(prefijo)]
if len(fila) != 1:
    fallos.append("filas que empiezan por %r: %d (se necesita exactamente 1)" % (prefijo, len(fila)))
elif ABIERTA not in fila[0]:
    fallos.append("LA TAREA %s YA ESTA CERRADA y una tarea no se cierra dos veces. Su fila dice: %s"
                  % (a.tarea, fila[0]))

ruta_sec = a.seccion if os.path.isabs(a.seccion) else os.path.join(RAIZ, a.seccion)
if not os.path.exists(ruta_sec):
    fallos.append("no existe el fichero de seccion %s" % a.seccion)
    seccion = ""
else:
    seccion = io.open(ruta_sec, encoding="utf-8").read().strip()
    if not seccion:
        fallos.append("el fichero de seccion %s esta vacio" % a.seccion)

if fallos:
    print("ROJO, no se anexa nada:")
    for f in fallos:
        print("   " + f)
    sys.exit(1)

vieja = fila[0]
nueva = vieja.replace(ABIERTA, "%s | %s |" % (a.estado, a.prueba))
texto = texto.replace(vieja, nueva)

texto = texto.replace("*(vacio: ninguna tarea ha cerrado todavia)*\n", "")
texto = texto.replace("<!-- FIN ANEXO DE TAREAS -->", seccion + "\n\n<!-- FIN ANEXO DE TAREAS -->")

io.open(RUTA, "w", encoding="utf-8", newline="\n").write(texto)
print("ANEXADA LA TAREA %s a docs/loop/REPORTE.md" % a.tarea)
print("   fila vieja: %s" % vieja)
print("   fila nueva: %s" % nueva)
print("   seccion anexada: %s (%d lineas)" % (a.seccion, seccion.count("\n") + 1))
print("   reporte ahora: %d lineas" % io.open(RUTA, encoding="utf-8").read().count("\n"))
